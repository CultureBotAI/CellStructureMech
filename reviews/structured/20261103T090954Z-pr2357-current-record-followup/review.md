# PR 2357: current-input review of ten records and adversarial follow-up

- Review: 20261103T090954Z-pr2357-current-record-followup
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-11-03T08:53:23.110159Z
- Finished UTC: 2026-11-03T09:09:54Z
- Reviewer: Codex root synthesis with three independent read-only adversarial reviewers (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Current-input reassessment of all ten records in PR2357. Six stale reviews are substantively refreshed against current changes. Independent scientific reviews retain all15 original findings (seven major,eight minor; one minor remains provisional), correct eight structured-source applicability defects and complete the predecessor repository field without editing records.

## Scope And Provenance

Exact ten-record PR cohort reassessed against current main 3d7d64088fafc5698ce6d66811594cb26b800f34. Changed inputs are substantively reassessed. Scientific records remain unchanged.

Selection: Complete cohort of ten maintained records reviewed in original PR head 6331a7f4a88273b06a55952d737921b2d1738f97.
Coverage: full; 10 reviewed / 10 in the declared population.
Source: working_tree at Git base e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0034515 | data/structures/inclusion/proteasome_storage_granule.yaml | maintained | proteasome storage granule |
| GO:0140453 | data/structures/inclusion/protein_aggregate_center.yaml | maintained | protein aggregate center |
| GO:0033985 | data/structures/membrane_organelle/acidocalcisome_lumen.yaml | maintained | acidocalcisome lumen |
| GO:0033102 | data/structures/membrane_organelle/acidocalcisome_membrane.yaml | maintained | acidocalcisome membrane |
| cellstructuremech:actinophryid_extrusome | data/structures/membrane_organelle/actinophryid_extrusome.yaml | maintained | actinophryid extrusome |
| GO:0044222 | data/structures/membrane_organelle/anammoxosome.yaml | maintained | anammoxosome |
| cellstructuremech:anammoxosome_membrane | data/structures/membrane_organelle/anammoxosome_membrane.yaml | maintained | anammoxosome membrane |
| GO:0020026 | data/structures/membrane_organelle/apicomplexan_dense_granule.yaml | maintained | apicomplexan dense granule |
| GO:0030668 | data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml | maintained | apicomplexan dense granule membrane |
| GO:0020011 | data/structures/membrane_organelle/apicoplast.yaml | maintained | apicoplast |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Full native QC | passed | True | GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011 | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| Native label correspondence | passed | True | GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011 | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| TraitMech references | passed | True | GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011 | Native TraitMech link check passed. |
| Pinned governed files | passed | True | GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011 | Pinned governed files match; native vendored check passed. |
| Native identifier resolver | passed | True | GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011 | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| validate GO:0034515 | passed | True | GO:0034515 | Documented focused command passed. |
| validate-strict GO:0034515 | passed | True | GO:0034515 | Documented focused command passed. |
| validate GO:0140453 | passed | True | GO:0140453 | Documented focused command passed. |
| validate-strict GO:0140453 | passed | True | GO:0140453 | Documented focused command passed. |
| validate GO:0033985 | passed | True | GO:0033985 | Documented focused command passed. |
| validate-strict GO:0033985 | passed | True | GO:0033985 | Documented focused command passed. |
| validate GO:0033102 | passed | True | GO:0033102 | Documented focused command passed. |
| validate-strict GO:0033102 | passed | True | GO:0033102 | Documented focused command passed. |
| validate cellstructuremech:actinophryid_extrusome | passed | True | cellstructuremech:actinophryid_extrusome | Documented focused command passed. |
| validate-strict cellstructuremech:actinophryid_extrusome | passed | True | cellstructuremech:actinophryid_extrusome | Documented focused command passed. |
| validate GO:0044222 | passed | True | GO:0044222 | Documented focused command passed. |
| validate-strict GO:0044222 | passed | True | GO:0044222 | Documented focused command passed. |
| validate cellstructuremech:anammoxosome_membrane | passed | True | cellstructuremech:anammoxosome_membrane | Documented focused command passed. |
| validate-strict cellstructuremech:anammoxosome_membrane | passed | True | cellstructuremech:anammoxosome_membrane | Documented focused command passed. |
| validate GO:0020026 | passed | True | GO:0020026 | Documented focused command passed. |
| validate-strict GO:0020026 | passed | True | GO:0020026 | Documented focused command passed. |
| validate GO:0030668 | passed | True | GO:0030668 | Documented focused command passed. |
| validate-strict GO:0030668 | passed | True | GO:0030668 | Documented focused command passed. |
| validate GO:0020011 | passed | True | GO:0020011 | Documented focused command passed. |
| validate-strict GO:0020011 | passed | True | GO:0020011 | Documented focused command passed. |
| Supplemental bounded PMID authority checks | passed | True | GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011 | 909 PMIDs all OK in bounded native requests; full-command limitations remain separate. |
| Official structured-source applicability and covered-dataset cross-checks | passed | False | GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011 | Actual molecular and pathway assertions were compared with the official catalogue and represented organism scopes. Eight original reviews require correction: four unsupported expression-only exemptions (acidocalcisome membrane, actinophryid extrusome, anammoxosome and anammoxosome membrane) and four omissions (PSG, PAC, apicomplexan dense granule and apicoplast). The anammoxosome membrane has a named metabolic-pathway trigger despite an empty protein inventory. Acidocalcisome lumen and dense-granule membrane are sparse compartment/material exclusions, with no invented molecular queries. Missing matching dataset coverage is bounded resource noncoverage, not biological absence. Historical native-runner unavailability is separate, with no fresh invocation or successful execution claimed. |
| Independent claim-level source review | passed | True | GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011 | Three read-only reviewers covered the complete ten-record cohort, including changed inputs, with explicit scientific findings and source-access limits. Final artifact/head acceptance occurs after saving. |
| Retained historical adapter runner availability | unavailable | False | GO:0034515, GO:0140453, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0020011 | Historical 00:49Z invocation unavailable due to OS access restriction. Official catalogue source fallback was inspected separately; no current invocation or successful adapter execution is claimed. The actual historical exit code 1 is retained in the evidence receipt, since the native unavailable-check model has no execution exit-code field. |
| Native proteasome storage granule UniProt verify check | passed | True | GO:0034515 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native proteasome storage granule UniProt causal check | passed | True | GO:0034515 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native protein aggregate center UniProt verify check | passed | True | GO:0140453 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native protein aggregate center UniProt causal check | passed | True | GO:0140453 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native acidocalcisome lumen UniProt verify check | passed | True | GO:0033985 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native acidocalcisome lumen UniProt causal check | passed | True | GO:0033985 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native acidocalcisome membrane UniProt verify check | passed | True | GO:0033102 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native acidocalcisome membrane UniProt causal check | passed | True | GO:0033102 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native actinophryid extrusome UniProt verify check | passed | True | cellstructuremech:actinophryid_extrusome | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native actinophryid extrusome UniProt causal check | passed | True | cellstructuremech:actinophryid_extrusome | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native anammoxosome UniProt verify check | passed | True | GO:0044222 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native anammoxosome UniProt causal check | passed | True | GO:0044222 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native anammoxosome membrane UniProt verify check | passed | True | cellstructuremech:anammoxosome_membrane | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native anammoxosome membrane UniProt causal check | passed | True | cellstructuremech:anammoxosome_membrane | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native apicomplexan dense granule UniProt verify check | passed | True | GO:0020026 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native apicomplexan dense granule UniProt causal check | passed | True | GO:0020026 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native apicomplexan dense granule membrane UniProt verify check | passed | True | GO:0030668 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native apicomplexan dense granule membrane UniProt causal check | passed | True | GO:0030668 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native apicoplast UniProt verify check | passed | True | GO:0020011 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |
| Native apicoplast UniProt causal check | passed | True | GO:0020011 | Read-only native command returned zero. Exact represented inventory and coverage limits are retained in evidence. Empty inventories or zero molecular graph nodes do not validate narrative molecules, mechanism, taxon transfer or assembly necessity. |

## Scientific And Domain Assessments

### Exact compartment identity, synonym and distinct hierarchy relations

identity: supported. Targets: GO:0033985.

Native GO and UniProt location definitions support the exact compartment, synonym and parthood. The requested is_a closure supports the asserted broader parent. Parentage, part_of and a cross-reference are kept separate; the membrane and enclosed volume are not collapsed into the whole organelle.

### Taxon identity and reported occurrence

scope: supported. Targets: GO:0033985.

The three native taxon identities are valid. VARIABLE across Bacteria and Eukaryota does not assert that every cell has acidocalcisomes. Reviews support broad reported distributions, while the sole bacterial exemplar requires the disputed-identity qualification in F1; this is not a blanket absence finding.

### Reported bacterial compartments versus disputed granule equivalence

evidence: concern. Targets: GO:0033985.

The 2003 primary abstract positively supports the original interpretation. The later C58 primary body and the2024 review explicitly disagree about whether the fluorescence-visible granules represent the same structures. Neither the negative staining/failed isolation in2020 nor the short-polyphosphate explanation in2024 alone settles the identity. The target omits this material conflict, yielding F1.

### Exact citation identities and source tiers

provenance: concern. Targets: GO:0033985.

Exact publication identities are valid, but Docampo2024 is sole-authored and Huang attribution remains incorrect (F2). Current evidence uses the2003 primary abstract,2005 review abstract/key points, selected actual2020 primary Methods/Results and selected2024 review body; no primary/secondary or abstract/body tier is upgraded.

### Status, history and local boundary dependencies

provenance: supported. Targets: GO:0033985.

The target remains PROPOSED and agent-authored; this review does not promote status or edit history. Whole-organelle and adjacent-compartment dependencies are frozen native inspection inputs and used only for the target boundary discussion. No hosted image or external image claim is present.

### Deliberate separation of volume, contents and membrane machinery

completeness: supported. Targets: GO:0033985.

This record denotes enclosed volume. Its resolved discussion deliberately places polyphosphate/cation matrix on the whole-organelle record and transport proteins on the membrane record. The frozen neighbors substantiate that representation boundary. Empty optional molecular inventory and function slots are not missing-data findings, and this review does not invent a source-neutral lumen scaffold.

### Both descriptive topology edges

graph: supported. Targets: GO:0033985.

The two edges state that the lumen is part of the acidocalcisome and that its membrane bounds it. Native definitions and location parthood support these claims. NONMECHANISTIC accurately describes this topology; the graph does not claim intervention, transporter membership or a molecular assembly mechanism.

### Lumen contents versus assembly necessity

evidence: unknown. Targets: GO:0033985.

No lumen component essentiality is asserted. The existence of an enclosed volume does not establish which individual matrix molecule or membrane protein is necessary to assemble an acidocalcisome.

### Original immutable input and deterministic artifact checks

provenance: supported. Targets: GO:0033985.

Original YAML validates and its Markdown is exactly the native render. Historical target bytes match the original frozen target hash. Current inputs are independently frozen and reviewed; stale records receive new observations rather than edits to the originals.

### Native protein identity and graph-symbol checks

schema: supported. Targets: GO:0033985.

Both actual focused checks exited0. Sparse material targets have no molecular nodes; generic heterogeneous sets can report NO_GENE_SYMBOLS without implying a missing required protein. Identity checking is separate from localization, mechanism and necessity.

### Structured-source applicability for a sparse compartment/material record

scope: not_applicable. Targets: GO:0033985.

The target makes compartment/bilayer topology claims and has no gene, locus, accession, regulator, molecular pathway, stress-response or transcriptomic claim requiring a matched module check. No molecular inventory is imposed. The original no-expression wording for lumen is clarified by this actual trigger assessment; the sparse membrane omission is not classified as a defect.

### Exact compartment identity, synonym and distinct hierarchy relations

identity: supported. Targets: GO:0033102.

Native GO and UniProt location definitions support the exact compartment, synonym and parthood. The requested is_a closure supports the asserted broader parent. Parentage, part_of and a cross-reference are kept separate; the membrane and enclosed volume are not collapsed into the whole organelle.

### Taxon identity and reported occurrence

scope: supported. Targets: GO:0033102.

The three native taxon identities are valid. VARIABLE across Bacteria and Eukaryota does not assert that every cell has acidocalcisomes. Reviews support broad reported distributions, while the sole bacterial exemplar requires the disputed-identity qualification in F1; this is not a blanket absence finding.

### Reported bacterial compartments versus disputed granule equivalence

evidence: concern. Targets: GO:0033102.

The 2003 primary abstract positively supports the original interpretation. The later C58 primary body and the2024 review explicitly disagree about whether the fluorescence-visible granules represent the same structures. Neither the negative staining/failed isolation in2020 nor the short-polyphosphate explanation in2024 alone settles the identity. The target omits this material conflict, yielding F1.

### Exact citation identities and source tiers

provenance: concern. Targets: GO:0033102.

Exact publication identities are valid, but Docampo2024 is sole-authored and Huang attribution remains incorrect (F2). Current evidence uses the2003 primary abstract,2005 review abstract/key points, selected actual2020 primary Methods/Results and selected2024 review body; no primary/secondary or abstract/body tier is upgraded.

### Status, history and local boundary dependencies

provenance: supported. Targets: GO:0033102.

The target remains PROPOSED and agent-authored; this review does not promote status or edit history. Whole-organelle and adjacent-compartment dependencies are frozen native inspection inputs and used only for the target boundary discussion. No hosted image or external image claim is present.

### Constitutional bilayer and variable associated transport systems

evidence: supported. Targets: GO:0033102.

The collective lipid bilayer is the membrane boundary itself, supporting its constitutional role and ESSENTIAL classification at that collective level. Accessible review material supports proton-pump and cation-transport systems with lineage-specific membership. A broad class label does not assert every named pump in every species, and no fixed subunit stoichiometry or universal lipid recipe is supplied.

### Individual assembly requirements remain untested

evidence: unknown. Targets: GO:0033102.

The record correctly keeps grouped proton pumps and cation transporters UNKNOWN for formation or assembly necessity. Localization, ion transport and effects on acidity/storage do not establish organelle assembly dependence. The constitutional requirement for a lipid boundary does not establish necessity of any individual lipid species or class.

### Reviewed hppA example and native family scope

grounding: supported. Targets: GO:0033102.

The record’s sole reviewed tax358 hppA example has the exact maintained accession, gene, label and status. Its role explicitly limits it to identifier identity. IPR004131 is an integrated candidate for this PPase fragment, not an exact source-neutral replacement for the grouped proton-pump set including ATPases. Generic cation transporters are not a single gene/family; the existing reviewed-label-only rationale and open grounding TODO are appropriately bounded.

### Accession-specific ion selectivity and experimental localization

evidence: unknown. Targets: GO:0033102.

Q8VPZ0 is a D44 fragment with putative sodium-pump/function and membrane-location predictions by homology. The positive2003 abstract reports K-insensitive PPase activity but does not establish that this accession/strain was assayed. The2020 C58 study instead uses the full-length712-aa Atu_1174 fusion and distinguishes tagged HppA structures from DAPI-positive granules. These contexts do not experimentally settle Q8VPZ0 proton versus sodium selectivity or acidocalcisome membership. Because the record explicitly says identity only, no wrong-accession or experimentally disproved localization finding is manufactured.

### Acidification and cation exchange at reviewed functional scope

evidence: supported. Targets: GO:0033102.

The2005 accessible review key points support proton pumps and exchange systems; the2024 read sections explain acidification, cation transport/release and phosphorus/cation storage with species-dependent systems. These support the broad functional descriptions. They do not identify a universal transporter network, direction for every member, bacterial mechanism for every class, or assembly requirement.

### All four coarse function edges and gene-node anchoring

graph: supported. Targets: GO:0033102.

All seven current edges were reassessed. Four prior coarse edges remain supported. New bilayer-forms-membrane and pump-resides-in-membrane edges follow GO and the 2005 accessible key points; new transporter-contributes-to-store is supported by the 2024 §§5.1,5.2,5.5 and10 synthesis of Ca2+ uptake and metal/proton exchange. It is a bounded functional storage relationship, not a claim that every transporter in every taxon only imports ions. NONMECHANISTIC remains appropriate. The new edge repeats the F2 author-attribution error.

### Bounded open grounding work

completeness: supported. Targets: GO:0033102.

The existing open discussion accurately requests more precise lipid and transporter groundings while recognizing lineage-dependent composition. No exact identifier for the full grouped sets was established by the inspected candidate family, so empty optional family inventories are not treated as an automatic defect. F1 separately requires a durable bacterial identity-conflict discussion.

### Original immutable input and deterministic artifact checks

provenance: supported. Targets: GO:0033102.

Original YAML validates and its Markdown is exactly the native render. Historical target bytes match the original frozen target hash. Current inputs are independently frozen and reviewed; stale records receive new observations rather than edits to the originals.

### Native protein identity and graph-symbol checks

schema: supported. Targets: GO:0033102.

Both actual focused checks exited0. Sparse material targets have no molecular nodes; generic heterogeneous sets can report NO_GENE_SYMBOLS without implying a missing required protein. Identity checking is separate from localization, mechanism and necessity.

### Actual molecular triggers and current covered-organism catalogue

scope: supported. Targets: GO:0033102.

Named hppA/GRA accessions trigger applicability assessment. Historical runner unavailability is separately disclosed. Fresh complete source catalogue has no matching Agrobacterium or Toxoplasma dataset, so no downstream gene/module search is applicable. Broad taxon classes do not license substitution of another species; lack of expression prose is not the rationale.

### Secretory organelle and membrane boundary

identity: supported. Targets: GO:0020026.

Exact GO identity, RELATED synonym and secretory-granule hierarchy are supported. The whole granule is kept separate from its membrane, lumen and the host-parasite vacuole membrane where secreted cargo later acts.

### Heterogeneous cargo and concrete examples

grounding: supported. Targets: GO:0020026.

Current membrane and heterogeneous cargo cohorts are supported without a universal protein census. Gra2/Gra6 candidate families cannot ground the full cargo set. Exact UniProt entries support three reviewed examples and two unreviewed ME49 examples; primary Table1 bridges ME49 loci to GRA17/GRA23. Inconclusive exact-protein InterPro attempts do not establish family absence or invalidate the bounded label-only cohort.

### Unresolved individual assembly requirements

evidence: unknown. Targets: GO:0020026.

A lipid boundary constitutes this membrane-bounded organelle; the ESSENTIAL membrane row is collective material. None of the named GRA species is thereby proven necessary for formation of a dense granule. PVM permeability, parasite growth and cargo secretion phenotypes do not establish granule-assembly necessity; individual cargo entries correctly remain UNKNOWN.

### Taxonomy and model-system boundaries

scope: supported. Targets: GO:0020026.

The native taxonomy entries attest their own ranks and identities. Mercier2005 supplies review-tier cross-apicomplexan context for qualitative COMMON and specialized eukaryotic RARE wording; it is not a prevalence measurement. Toxoplasma experiments and ME49 reference identity remain distinct from a universal apicomplexan GRA inventory.

### Secretion, permeability and host-cell effects

evidence: supported. Targets: GO:0020026.

After-invasion secretion is supported and is not phrased as exclusive of extracellular secretion. Gold2015 supports the paired permeability function with unequal single-deletion phenotypes. The native Bougdour2013 abstract explicitly supports GRA16 nuclear export and host-gene effects; Masatani2013 abstract supports GRA23 dense-granule/PVM/IVN localization. Full bodies of those two studies were unavailable.

### Cargo release and later PVM activity

graph: supported. Targets: GO:0020026.

The graph represents cargo release, delivery/localization and an experimentally tested permeability consequence, in addition to boundary topology. It distinguishes granule membrane from PVM, does not identify a pore stoichiometry, and does not imply GRA17/GRA23 are required to build the secretory organelle.

### Bounded clean review

completeness: supported. Targets: GO:0020026.

No new scientific curation defect was established. Current GRA17 protein identity and new exported-effector edges were substantively reassessed. Optional complete proteomes, resident membrane-protein censuses and universal lipid inventories are not mandatory. Adapter-process omission is reported separately from record science.

### Original immutable input and deterministic artifact checks

provenance: supported. Targets: GO:0020026.

Original YAML validates and its Markdown is exactly the native render. Historical target bytes match the original frozen target hash. Current inputs are independently frozen and reviewed; stale records receive new observations rather than edits to the originals.

### Native protein identity and graph-symbol checks

schema: supported. Targets: GO:0020026.

Both actual focused checks exited0. Sparse material targets have no molecular nodes; generic heterogeneous sets can report NO_GENE_SYMBOLS without implying a missing required protein. Identity checking is separate from localization, mechanism and necessity.

### Actual molecular triggers and current covered-organism catalogue

scope: supported. Targets: GO:0020026.

Named hppA/GRA accessions trigger applicability assessment. Historical runner unavailability is separately disclosed. Fresh complete source catalogue has no matching Agrobacterium or Toxoplasma dataset, so no downstream gene/module search is applicable. Broad taxon classes do not license substitution of another species; lack of expression prose is not the rationale.

### Membrane distinct from the whole secretory organelle

identity: supported. Targets: GO:0030668.

The ontology definition, broader organelle-membrane parent and part_of dense-granule relation are supported. The record consistently represents the bounding membrane, not the stored lumen/cargo or the parasitophorous-vacuole membrane.

### Collective lipid matrix

grounding: supported. Targets: GO:0030668.

The generic lipid-bilayer row represents the constituting membrane material. GO0030668 identifies the whole membrane and is not an exact chemical-family identifier for its constituent lipids; label-only material grounding is justified. No universal lipid-species census is asserted.

### Individual formation requirements remain untested

evidence: unknown. Targets: GO:0030668.

ESSENTIAL denotes the collective constituting lipid bilayer. The cited synthesis and ontology do not identify which individual lipid species or proteins are necessary for membrane formation, and no such removal experiment is inferred from ordinary boundary identity.

### Cross-apicomplexan context and Toxoplasma example

scope: supported. Targets: GO:0030668.

Native taxonomy verifies Apicomplexa and Toxoplasma identities. Mercier2005 review abstract supplies qualitative cross-apicomplexan context; Griffith selected review body supports Toxoplasma membrane-bounded granule biogenesis. These are not measured prevalence or universal cargo inventories.

### Explicit nonmechanistic topology

graph: supported. Targets: GO:0030668.

The boundary function and single part-of graph edge follow the native definition. NONMECHANISTIC accurately describes this topology; no cargo secretion mechanism or particular PVM permeability protein has been transferred onto the granule membrane.

### Bounded clean review

completeness: supported. Targets: GO:0030668.

No corrective issue was established. The open generic-lipid grounding question is not an error, and optional resident-membrane-protein inventories are not required to make this topology record valid. The whole-granule neighbor supplies context only.

### Original immutable input and deterministic artifact checks

provenance: supported. Targets: GO:0030668.

Original YAML validates and its Markdown is exactly the native render. Historical target bytes match the original frozen target hash. Current inputs are independently frozen and reviewed; stale records receive new observations rather than edits to the originals.

### Native protein identity and graph-symbol checks

schema: supported. Targets: GO:0030668.

Both actual focused checks exited0. Sparse material targets have no molecular nodes; generic heterogeneous sets can report NO_GENE_SYMBOLS without implying a missing required protein. Identity checking is separate from localization, mechanism and necessity.

### Structured-source applicability for a sparse compartment/material record

scope: not_applicable. Targets: GO:0030668.

The target makes compartment/bilayer topology claims and has no gene, locus, accession, regulator, molecular pathway, stress-response or transcriptomic claim requiring a matched module check. No molecular inventory is imposed. The original no-expression wording for lumen is clarified by this actual trigger assessment; the sparse membrane omission is not classified as a defect.

### Substantive refresh of added membrane material and transporter edges

graph: supported. Targets: GO:0033102.

The new phospholipid-bilayer node and three edges retain the established membrane identity and variable transporter scope. Docampo2024 explicitly describes cation sequestration by metal/proton exchange alongside Ca2+-ATPases; it also describes release systems and unknown transporter roles, so the review preserves these limits. Added edge6 inherits the same sole-author attribution finding. No unrefreshable delta remains.

### Substantive GRA17 and exported-effector refresh

evidence: supported. Targets: GO:0020026.

S8GTZ8/NCBI7895641 identify ME49 TGME49_222170; the primary PMC7202600 Table1 supplies its exact GRA17 bridge. Gold2015 GT1/RH experimental effects are not silently transferred as ME49 experimental verification. Bougdour2013 primary abstract supports the two new GRA16 secretion/export edges; Griffith body provides secondary context. GRA17/23 small-molecule permeability remains separate from GRA16 export.

### Original artifact integrity and current input boundary

schema: supported. Targets: GO:0034515.

Original native validate/render pass and frozen source blob matches its recorded hash. Current record is changed and substantively reassessed; old artifacts are retained unchanged.

### Current native protein verification and coverage

schema: supported. Targets: GO:0034515.

Three reference protein_examples verify; both recovery graphs contain zero GENE_OR_PROTEIN nodes. Coverage does not certify other component completeness.

### Structured-source applicability and current bounded fallback

evidence: not_applicable. Targets: GO:0034515.

Named BLM10/UBP6/UBI4 and quiescence/refeeding claims require assessment. Current full catalogue contains no matching organism. No downstream module result is fabricated; historical runner unavailability is dated separately.

### Original artifact integrity and current input boundary

schema: supported. Targets: GO:0140453.

Original native validate/render pass and frozen source blob matches its recorded hash. Current record is byte-identical and reassessed; old artifacts are retained unchanged.

### Current native protein verification and coverage

schema: supported. Targets: GO:0140453.

Three reference protein_examples verify; no GENE_OR_PROTEIN causal nodes. This does not validate biological necessity or count every chaperone.

### Structured-source applicability and current bounded fallback

evidence: not_applicable. Targets: GO:0140453.

Named HSP42/BTN2/HSP104 and heat-shock mutant/recovery claims require assessment. Current full catalogue contains no matching organism. No downstream module result is fabricated; historical runner unavailability is dated separately.

### Original artifact integrity and current input boundary

schema: supported. Targets: cellstructuremech:actinophryid_extrusome.

Original native validate/render pass and frozen source blob matches its recorded hash. Current record is changed and substantively reassessed; old artifacts are retained unchanged.

### Current native protein verification and coverage

schema: supported. Targets: cellstructuremech:actinophryid_extrusome.

The verifier has no protein_examples to check; the new single GP40 protein node is component-anchored but NO_GENE_SYMBOLS. Label-only identity and lack of experimentally assigned isoform are explicit, not false complete coverage.

### Structured-source applicability and current bounded fallback

evidence: not_applicable. Targets: cellstructuremech:actinophryid_extrusome.

Named GP40 and calcium/drug perturbation claims require assessment even without transcriptomic inference. Current full catalogue contains no matching organism. No downstream module result is fabricated; historical runner unavailability is dated separately.

### PSG identity, type and anatomical parts

identity: supported. Targets: GO:0034515.

GO0034515 matches the cytoplasmic quiescent CP/RP granule. INCLUSION_BODY and membraneless parent, cytoplasmic part-of and core/regulatory has-parts preserve structure identity. Nuclear precursor assemblies in2026 are distinguished from the record cytoplasmic PSG focus.

### Associated proteins and processed ubiquitin

representation: supported. Targets: GO:0034515.

Blm10/Ubp6 associations have direct2017 microscopy/enrichment support and appropriate reference examples. UBI4 is explicitly a precursor reference for processed unconjugated ubiquitin, not an unprocessed granule subunit; the manipulated reporter is distinguished from native cargo. Broad ubiquitin-family grounding stays deferred. UNKNOWN formation necessity avoids global extrapolation from assay-dependent mutants.

### Assembly architecture and differing assay scopes

evidence: supported. Targets: GO:0034515.

2008 colocalization does not establish active26S;2017 lysate PAGE and crosslink enrichment do not dictate intact in situ state.2026 cryo-ET supports paracrystalline intact inactive26S arrays and explains purification instability. No universal liquid-phase/stoichiometry claim is inferred.

### Stale refresh: refeeding edges and cycloheximide control

graph: supported. Targets: GO:0034515.

New descriptions correctly restrict both PSG disappearance and nuclear reaccumulation to four-day yeast shifted to freshYPD versus water; recovery persists with100ug/mL CHX preincubated1h. This excludes a need for de novo synthesis in that assay, without identifying a molecular dissolution mechanism.

### Stale refresh: retracted source placement

evidence: supported. Targets: GO:0034515.

Structured REFUTE evidence now makes the excluded2018 DOI machine-readable. No proteaphagy-protection function or Arabidopsis canonical example is imported from it. Historical#2430 is context only; no whole grouped issue or unfrozen category predecessor is terminally resolved.

### Canonical organisms and reference strains

scope: supported. Targets: GO:0034515.

Budding yeast BY4741/2/3 and fission-yeast Pad1-GFP examples have source support; S288C protein authority entries are reference identifiers, not the exact experimental strain. No global taxonomic prevalence is inferred.

### Linked Figure2 image and license

provenance: supported. Targets: GO:0034515.

Source pixels/caption, package checksum and CC BY-NC-SA3.0 permissions agree with the bounded localization caption. No repository-hosted-image requirement or new morphometric estimate is invented.

### Bounded clean current assessment

completeness: supported. Targets: GO:0034515.

No additional material defect observed across definition, parts, components, functions, graphs and image. Missing precise mature-ubiquitin family and universal granule stoichiometry remain explicit scientific limits, not fabricated findings. Current verdict remains pass_with_limitations.

### PAC identity and boundaries

identity: supported. Targets: GO:0140453.

GO0140453 matches reversible misfolded-protein/chaperone assemblies. INCLUSION_BODY and membraneless parent fit; PAC broad acronym is not a unique exact synonym. Nuclear/cytoplasmic possibilities prevent an exclusive cytoplasm placement. INQ/CytoQ overlap and severe-heat NuRs are not collapsed into exact identity.

### Chaperone identities and conditional necessity

representation: supported. Targets: GO:0140453.

Hsp42Q12329/BTN2P53286/Hsp104P31539 are reviewed559292 references. Joint BTN2/HSP42 loss does not assign single-gene universal necessity; W303-specific BTN2 phenotype supports only conditional role, while Hsp104 is dispensable for formation but participates in clearance. Domain-only BTN2 and broad ClpA/B groundings remain deferred.

### Assembly graph and combined mutant scope

graph: supported. Targets: GO:0140453.

37C reporter PAC assembly, BTN2/HSP42 combined impairment and CHX at induction are supported in the specified backgrounds. Rho1.C17R-GFP is engineered and C-terminal tagging disrupts geranylgeranylation. No42C NuR mechanism or general endogenous-protein universality is inferred.

### Protection and degradation graph

graph: supported. Targets: GO:0140453.

At37C CHX or combined small-chaperone loss accelerates reporter turnover with immunoblot support;25C is a distinct control. Foci loss alone is not proteolysis, and Ydj1/Rsp5 phenotype does not automatically make them structural components.

### Recovery graph and timing

graph: supported. Targets: GO:0140453.

After37C30min assembly, return to25C with CHX added for recovery permits clearance; HSP104 deletion impairs this and delays chronic-heat reporter degradation. Recovery CHX timing is distinct from formation blockade.

### Experimental yeasts and reference identity

scope: supported. Targets: GO:0140453.

W303, BY4741 and S.pombe972 claims match the2023 study. Reference protein accession taxon559292 is not represented as proof of each experimental strain sequence.2020 fission-yeast conclusions remain abstract-scoped.

### Tracked Figure2 pixels, provenance and scope

provenance: supported. Targets: GO:0140453.

Tracked bytes match PMC package MD5 and CC BY4.0 permissions; direct pixel inspection confirms separate Btn2/Hsp42/Hsp104 reporter rows and temperature/time panels. Caption avoids treating panel recruitment as universal necessity or three-way colocalization.

### Versioned dataset provenance

evidence: supported. Targets: GO:0140453.

Exact dataset DOI/title/creator/issued date/license resolve in DataCite. No claim of raw-data verification or complete file-manifest inspection is made.

### Scientific limitations and current verdict

completeness: supported. Targets: GO:0140453.

No material new defect observed. Hsp16/Mas5/Ssa2 follow-up and heterogeneous cargo lack of fixed stoichiometry are explicit; the record does not claim exhaustive PAC proteomics. Current verdict remains pass_with_limitations.

### Local extrusome identity and membrane boundaries

identity: supported. Targets: cellstructuremech:actinophryid_extrusome.

The membrane-bounded Actinophrys granule has a defensible local identity and broad intracellular-membrane-bounded parent. Golgi-origin secretory-granule and parasite food-vacuole GO terms are not exact identities. Current bounded GO label search is negative only within its literal query.

### GP40 scope, sequence candidates and membrane component

representation: supported. Targets: cellstructuremech:actinophryid_extrusome.

Primary2001 abstract establishes secretory GP40 association. Current unreviewed gp40-1/-2 entries and broad beta-glucanase/lectin domains do not assign a localized exact protein family. Deleted IPR050546 is not valid grounding. Label-only GP40 and membrane with UNKNOWN formation necessity are appropriate limits.

### Stale refresh: GP40 residence and adhesion edges

graph: supported. Targets: cellstructuremech:actinophryid_extrusome.

Both new component-anchored GP40 edges follow the primary2001 abstract; the graph does not conflate residence or adhesion activity with organelle-formation necessity. No accession is guessed for the assayed protein.

### Existing membrane-donation graph

graph: supported. Targets: cellstructuremech:actinophryid_extrusome.

1982 abstract directly supports extrusome expansion/fusion with each other and plasma membrane during funnel-pseudopod enclosure, providing food-vacuole membrane. Generic cell/process nodes preserve this observational edge scope without a hypothetical fusogen.

### Pharmacology is not component localization

evidence: supported. Targets: cellstructuremech:actinophryid_extrusome.

2008 author-manuscript Results/Discussion support calcium/ConA perturbation context, while ionophore depletion is speculative and damage/other glycoconjugates remain alternatives. No unique channel or receptor member is inferred.

### Canonical example versus COMMON frequency

scope: concern. Targets: cellstructuremech:actinophryid_extrusome.

Actinophrys sol canonical identity is supported. The inherited minor/provisional finding remains: evidence for organelle abundance in studied cells does not establish the encoded taxon-wide COMMON frequency. Full1998 text remains unread; variability is not demonstrated.

### No claimed image or quantitative morphology inventory

provenance: not_applicable. Targets: cellstructuremech:actinophryid_extrusome.

This target contains no image or physical-measurement inventory to validate. No hypothetical image deficiency or molecular inventory is invented.

### Current verdict and exact predecessor

completeness: concern. Targets: cellstructuremech:actinophryid_extrusome.

Current needs_curation verdict retains only the existing minor/provisional presence-abundance issue with exact predecessor20261021T104743Z-actinophryid-extrusome-audit/F1. Other scientific uncertainties are explicit and do not justify new findings.

### Native schema, rendering and frozen-input integrity

schema: supported. Targets: GO:0044222.

Original bundle validates and renders exactly; frozen target content matches its original revision. Local root-run protein checks pass within their explicitly limited inventory scopes. Staleness is assessed separately from schema validity.

### Structured-source applicability and available taxon coverage

scope: not_applicable. Targets: GO:0044222.

The record names specific molecular actors and pathways. Applicability was assessed using the current complete catalogue; no target-matched organism/dataset exists. Thus downstream gene/module queries are not applicable. Historical runner unavailability is separately disclosed and absence of expression claims is not the basis.

### Native schema, rendering and frozen-input integrity

schema: supported. Targets: cellstructuremech:anammoxosome_membrane.

Original bundle validates and renders exactly; frozen target content matches its original revision. Local root-run protein checks pass within their explicitly limited inventory scopes. Staleness is assessed separately from schema validity.

### Structured-source applicability and available taxon coverage

scope: not_applicable. Targets: cellstructuremech:anammoxosome_membrane.

The record names hydrazine/anammox metabolism despite its material-only protein inventory. Applicability was assessed using the current complete catalogue; no target-matched organism/dataset exists. Thus downstream gene/module queries are not applicable. Historical runner unavailability is separately disclosed and absence of expression claims is not the basis.

### Native schema, rendering and frozen-input integrity

schema: supported. Targets: GO:0020011.

Original bundle validates and renders exactly; frozen target content matches its original revision. Local root-run protein checks pass within their explicitly limited inventory scopes. Staleness is assessed separately from schema validity.

### Structured-source applicability and available taxon coverage

scope: not_applicable. Targets: GO:0020011.

The record names specific molecular actors and pathways. Applicability was assessed using the current complete catalogue; no target-matched organism/dataset exists. Thus downstream gene/module queries are not applicable. Historical runner unavailability is separately disclosed and absence of expression claims is not the basis.

### Organelle identity and refreshed membrane parthood

identity: supported. Targets: GO:0044222.

GO0044222 is the whole intracellular compartment; current reciprocal has_part points to the separately maintained ladderane membrane. Native GO definition, membrane record and de Almeida localization study support the boundary. The added history and parthood do not correct older reaction, necessity or source-attribution defects.

### Taxon scope and Kuenenia example

scope: supported. Targets: GO:0044222.

Rare occurrence within the broad Bacteria/Planctomycetota rows is explicitly limited to anammox lineages. Kuenenia174633 is the source-specific immunolocalization organism. Current corrected taxon spelling and historical synonym resolve to that same taxon.

### HZS reaction and HDH versus HOX role

evidence: concern. Targets: GO:0044222.

Current HZS electron-source wording and grouped HDH/HAO role remain unsupported as encoded; retain original F1/F2. The Q1PX48 reviewed side reaction does not turn HOX into physiological HDH.

### Constitution versus metabolic or formation requirement

evidence: concern. Targets: GO:0044222.

The bounding membrane is constitutive, but cited enzyme catalysis and localization do not demonstrate that HZS or the entire HDH/HAO cohort is essential for organelle formation. Retain original F3 without asserting dispensability.

### Carrier model and edge-level localization scope

evidence: concern. Targets: GO:0044222.

The proposed quinone-linked energetic model is retained as a model. The current membrane-carrier localization edge misuses a study of soluble matrix enzymes; original F4 remains. Exact carrier machinery and formation dependencies stay unresolved.

### Concrete protein identity and grouped class scope

grounding: supported. Targets: GO:0044222.

The three unreviewed HZS examples resolve to named hzs subunits in taxon174633. HDH Q1PYC5 is unreviewed; Q1PX48 is reviewed hao/hox. HZS is a multisubunit complex and heterogeneous HDH/HAO and carrier groups are not assigned a single whole-group family from one example. Functional conflation is separately retained as F2.

### Exact author/year/source correspondence

evidence: concern. Targets: GO:0044222.

PMID15098544 is van Niftrik2004, a review; Sinninghe Damste2002 is PMID12384695. DOI10.1128/JB.00186-15 is de Almeida2015. Both currently cited sources remain relevant, but repeated attributions require correction.

### Exact author/year/source correspondence

evidence: concern. Targets: cellstructuremech:anammoxosome_membrane.

PMID15098544 is van Niftrik2004, a review; Sinninghe Damste2002 is PMID12384695. DOI10.1128/JB.00186-15 is de Almeida2015. Both currently cited sources remain relevant, but repeated attributions require correction.

### Distinct local membrane identity and current reciprocal boundary

identity: supported. Targets: cellstructuremech:anammoxosome_membrane.

The local identifier denotes the bounding membrane, not the whole GO0044222 compartment. GO0016020 is a broader parent. The neighboring whole organelle now reciprocates part_of with has_part; exact OLS lookup is bounded and does not establish universal ontology absence.

### Collective bilayer constituent and lipid scope

grounding: supported. Targets: cellstructuremech:anammoxosome_membrane.

The generic ladderane-containing lipid bilayer is a collective constitutive boundary; it is not equivalent to one lipid molecule or a protein family. No new chemical accession, exact lipid inventory or universal permeability coefficient is inferred from the available sources.

### Topology graph, metabolic confinement and source limits

scope: supported. Targets: cellstructuremech:anammoxosome_membrane.

The NONMECHANISTIC graph records membrane parthood and confinement of anammox metabolism. Named hydrazine pathway triggers coverage assessment but does not turn this graph into an enzyme mechanism. Proposed energy-conservation/barrier function is retained at review/model scope; soluble-enzyme localization does not prove exact membrane-carrier membership.

### Anammox lineage and example scope

scope: supported. Targets: cellstructuremech:anammoxosome_membrane.

Broad taxonomic rows explicitly restrict occurrence to anammox lineages; the canonical example is Kuenenia174633. No unrelated covered iModulon species substitutes for that source-specific scope.

### Plastid identity and membrane constituent boundary

identity: supported. Targets: GO:0020011.

GO0020011 identifies the apicoplast and GO0160211 its membrane constituent. Frozen neighboring parthood and native GO relationships agree; the record is an organelle, not one imported protein.

### Substantive refresh of added IspG identity example

grounding: supported. Targets: GO:0020011.

Fresh Q8IJH7 metadata verifies unreviewed status, taxon36329 and PF3D7_1022800 locus; exact example-specific InterPro matches support IspG-family identity. The native query returns this entry via the locus alternative. These are computational identity checks, not new experimental apicoplast localization. Native causal coverage now covers all three declared protein nodes.

### Four membranes in the stated Plasmodium example

evidence: supported. Targets: GO:0020011.

Lemgruber2013 Results and captions support four membranes around P. falciparum merozoite apicoplasts. No new pixel count, raw-tomogram reanalysis or blanket statement across all secondary plastids is made.

### Variable apicomplexan distribution and exemplar identity

scope: supported. Targets: GO:0020011.

Native Apicomplexa, Toxoplasma and Plasmodium taxon identities match the record. Secondary review context supports variable distribution and loss in some lineages; no universal presence claim is encoded.

### Example identities versus cellular paralogs

grounding: concern. Targets: GO:0020011.

Native accession/status checks pass for the maintained examples. However, B9PY98 maps to deposited Der1ER1, not apicoplast Der1Ap; original F1 remains. O97275 is assessed separately using its locus/peptide bridge and is not discarded merely because automated generic UniProt wording says ER.

### Tic20 class-level family grounding

grounding: concern. Targets: GO:0020011.

IPR005691 is a family and directly matches maintained S8GBF3. A missing reviewed species accession does not justify leaving this class ungrounded. The heterogeneous SELMA and metabolic-enzyme cohorts still should not be assigned one whole-group family.

### Nuclear precursor targeting and import dependency

evidence: supported. Targets: GO:0020011.

The author-hosted Waller1998 primary paper supports targeting sequences and tested ACP leader sufficiency. The selected import studies support protein-import dependence and localization; these claims remain distinct from the pore and endogenous-modifier overclaims retained below.

### Tic20 requirement versus direct channel action

evidence: concern. Targets: GO:0020011.

The primary Tic20 study and reproduced author appendix support inner-membrane import requirement while explicitly considering accessory/regulatory roles. Current translocon/translocates wording over-resolves the mechanism; original F3 remains. This is a source-support finding, not a claim that Tic20 can never form a channel.

### Endogenous ubiquitylation modifier

evidence: concern. Targets: GO:0020011.

Agrawal2013 directly leaves endogenous ubiquitin versus ubiquitin-like modifier unresolved. In-vitro activity on human ubiquitin and import phenotypes support machinery involvement, not the current unqualified endogenous-substrate assertion. Original F4 remains.

### Metabolic pathways and blood-stage IPP function

scope: supported. Targets: GO:0020011.

Distinct imported enzyme families support a broad metabolic inventory, without claiming every pathway is essential at every stage. IPP rescue is explicitly P. falciparum asexual blood-stage evidence. Review-only heme/FAS/iron-sulfur context is identified as secondary, and the Annual Review source remains abstract-only.

### Organelle constitution and protein requirements

evidence: unknown. Targets: GO:0020011.

Collective envelope membranes are constitutive. Current UNKNOWN necessity for named protein cohorts avoids extending import, maintenance, growth or stage-specific metabolic dependence into a universal formation requirement; no new necessity assignment is proposed.

### Current scoped scientific verdict and retained lineage

completeness: concern. Targets: GO:0044222.

needs_curation remains warranted for this target. All original findings are preserved at exact prior review/finding lineage; current checks and stale-input refresh do not repair domain content. Record edits are deferred to separately authorized curation.

### Current scoped scientific verdict and retained lineage

completeness: concern. Targets: cellstructuremech:anammoxosome_membrane.

needs_curation remains warranted for this target. All original findings are preserved at exact prior review/finding lineage; current checks and stale-input refresh do not repair domain content. Record edits are deferred to separately authorized curation.

### Current scoped scientific verdict and retained lineage

completeness: concern. Targets: GO:0020011.

needs_curation remains warranted for this target. All original findings are preserved at exact prior review/finding lineage; current checks and stale-input refresh do not repair domain content. Record edits are deferred to separately authorized curation.

### Complete frozen-input comparison and bounded refresh

provenance: supported. Targets: GO:0034515, GO:0140453, GO:0033985, GO:0033102, cellstructuremech:actinophryid_extrusome, GO:0044222, cellstructuremech:anammoxosome_membrane, GO:0020026, GO:0030668, GO:0020011.

6 of ten original target hashes differ from current main. The changed content is substantively reassessed in the target-specific assessments; original observations remain historical and unchanged. All current target and used context bytes are frozen.

## Findings

### plaque-t2-F1: The sole canonical bacterial example omits an explicit unresolved identity dispute

major / open / confirmed; issue key: acidocalcisome_lumen-bacterial-identity-conflict.

The canonical A. tumefaciens note states that its volutin granules establish a lumenal storage compartment, without acknowledging the later disagreement. The 2003 abstract supports the original interpretation; Frank and Jendrossek2020 instead distinguish C58 DAPI-positive polyphosphate granules from HppA/MitoTracker-positive structures using fluorescence and mutants, while Docampo2024 explicitly challenges that interpretation through prior membrane observations and a short-polyphosphate/DAPI limitation. The omission is confirmed, not a conclusion that bacterial acidocalcisomes do not exist. It materially affects the sole canonical example and the bacterial compartment interpretation. The record should retain both source positions and the unresolved strain/preparation and marker limits.

### plaque-t2-F2: The 2024 review has one author, Roberto Docampo

minor / open / confirmed; issue key: acidocalcisome_lumen-docampo2024-author.

The target attributes DOI10.1128/MMBR.00042-23 to Docampo and Huang2024. Native bibliographic metadata and the article byline identify Roberto Docampo alone. Correct the attribution in every maintained note for this source; the valid DOI and collection year2024 are unchanged.

### plaque-t3-F1: The sole canonical bacterial example omits an explicit unresolved identity dispute

major / open / confirmed; issue key: acidocalcisome_membrane-bacterial-identity-conflict.

The canonical A. tumefaciens note states that its volutin granules were shown to be membrane-bound acidocalcisome-like organelles, without acknowledging the later disagreement. The 2003 abstract supports the original interpretation; Frank and Jendrossek2020 instead distinguish C58 DAPI-positive polyphosphate granules from HppA/MitoTracker-positive structures using fluorescence and mutants, while Docampo2024 explicitly challenges that interpretation through prior membrane observations and a short-polyphosphate/DAPI limitation. The omission is confirmed, not a conclusion that bacterial acidocalcisomes do not exist. It materially affects the sole canonical example and the bacterial compartment interpretation. The record should retain both source positions and the unresolved strain/preparation and marker limits.

### plaque-t3-F2: The 2024 review has one author, Roberto Docampo

minor / open / confirmed; issue key: acidocalcisome_membrane-docampo2024-author.

The target attributes DOI10.1128/MMBR.00042-23 to Docampo and Huang2024. Native bibliographic metadata and the article byline identify Roberto Docampo alone. Correct the attribution in every maintained note for this source; the valid DOI and collection year2024 are unchanged. The new current edge6 repeats the same inaccurate author attribution; the supported new transport relationship does not resolve this provenance defect.

### micro-F1: Separate cellular abundance from encoded taxonomic frequency

minor / open / provisional; issue key: actinophryid-extrusome-presence-abundance.

COMMON encodes occurrence in most taxon members, while the cited1998 Summary and distribution note establish abundant organelles in examined cells. This remains a bounded provenance gap, not demonstrated strain variability. The canonical species example is supported; full1998 text remains unread.

### septin-S2357-F1: Separate ammonium substrate from the HZS electron supply

major / open / confirmed; issue key: anammoxosome-hzs-electron-source.

The current HZS role and edge describe ammonium-derived reducing equivalents. The inspected 2015 primary Introduction separates ammonium substrate from the three-electron input and recycles electrons released by hydrazine oxidation. The wording still misstates the electron-transfer loop.

### septin-S2357-F2: Keep HDH and HOX physiological reactions separate

major / open / confirmed; issue key: anammoxosome-hdh-hox-functional-conflation.

The grouped HDH/HAO cohort and Q1PX48 example still receive a universal hydrazine-to-N2 role. The primary source distinguishes HDH/kustc0694 from HOX/kustc1061 and an HAO-like pair of unknown function; reviewed Q1PX48 qualifies its hydrazine side reaction as probably nonphysiological.

### septin-S2357-F3: Do not infer organelle formation requirements from catabolic activity

major / open / confirmed; issue key: anammoxosome-enzyme-assembly-essentiality.

HZS and the grouped HDH/HAO constituent class remain ESSENTIAL. Catalysis/localization evidence does not demonstrate organelle-formation failure after loss; repository essentiality concerns formation. This bounded source-support finding does not assert dispensability.

### septin-S2357-F4: Keep soluble-enzyme localization distinct from membrane-carrier membership

major / open / confirmed; issue key: anammoxosome-membrane-carrier-localization-source.

The graph links its membrane-associated carrier cohort to the 2015 localization experiment, whose Discussion explicitly identifies all measured complexes as soluble. That assay cannot establish the encoded membrane-carrier localization. The secondary review provides a proposed model with unresolved exact carriers.

### septin-S2357-F5: Correct the ladderane-paper and localization-paper attribution

minor / open / confirmed; issue key: anammoxosome-ladderane-citation-attribution.

PMID15098544 is van Niftrik et al.2004, The anammoxosome: an intracytoplasmic compartment in anammox bacteria, not the stated Sinninghe Damste2002 lipid-discovery paper. The 2002 paper is independently identified by PMID12384695. DOI10.1128/JB.00186-15 is de Almeida et al.2015, not a first-author Kartal paper. Both currently cited works are relevant, but their repeated author/year notes misidentify the source and evidence tier.

### septin-S2357-F6: Correct the ladderane-paper and localization-paper attribution

minor / open / confirmed; issue key: anammoxosome-membrane-ladderane-citation-attribution.

PMID15098544 is van Niftrik et al.2004, The anammoxosome: an intracytoplasmic compartment in anammox bacteria, not the stated Sinninghe Damste2002 lipid-discovery paper. The 2002 paper is independently identified by PMID12384695. DOI10.1128/JB.00186-15 is de Almeida et al.2015, not a first-author Kartal paper. Both currently cited works are relevant, but their repeated author/year notes misidentify the source and evidence tier.

### septin-S2357-F7: The Toxoplasma Der1 example is the ER paralog

major / open / confirmed; issue key: apicoplast-der1-er-paralog-example.

B9PY98 is linked by native ENA/UniProt records to Der1ER1 FJ976521/ACU32856.1. The author primary-study chapter distinguishes apicoplast Der1Ap FJ976520/ACU32855.1, now C9WWW6. An identity-only disclaimer does not make the ER paralog an appropriate concrete example of apicoplast SELMA.

### septin-S2357-F8: The Tic20 protein class has an available family grounding

minor / open / confirmed; issue key: apicoplast-tic20-family-grounding.

IPR005691 is a family entry for Tic20 and is matched by the maintained S8GBF3 example. The present label-only rationale combines lack of an exact family with absence of a reviewed species accession. Family-class grounding does not require a Swiss-Prot entry or a localization-specific family.

### septin-S2357-F9: Direct Tic20 translocation exceeds the cited experiment

minor / open / confirmed; issue key: apicoplast-tic20-direct-channel-overclaim.

The current Tic20 label, role and translocates edge encode direct channel action. The cited primary Results passage, independently inspected in the author appendix, establishes inner-membrane localization/import dependence but explicitly discusses accessory/regulatory alternatives. Retain the import requirement without over-resolving that mechanism.

### septin-S2357-F10: The cited study does not identify the endogenous modifier as ubiquitin

minor / open / confirmed; issue key: apicoplast-endogenous-ubiquitin-unresolved.

The SELMA role definitively says the machinery uses ubiquitin. Agrawal2013 demonstrates an apicoplast ubiquitylation system and enzyme activity with recombinant ubiquitin, but Discussion explicitly leaves endogenous ubiquitin versus a ubiquitin-like modifier unresolved.

## Recommended Actions And Acceptance Checks

### plaque-t2-A1

Preserve both the2003 positive interpretation and2020 contrary C58 results with the2024 counterargument, their strain/preparation/marker limits and an unresolved identity-conflict discussion.

- Retain exact stable issue key and previous occurrence; no claim that this review PR edited the scientific record.
- Use separately authorized guarded curation and append-only history for later record changes.
- Recheck claim-level source scopes and run documented native schema/strict, label, reference, history and QC gates after later curation.

### plaque-t2-A2

Correct every maintained attribution of DOI10.1128/MMBR.00042-23 to Roberto Docampo alone, including any newly added edge evidence; keep the valid DOI and collection year.

- Retain exact stable issue key and previous occurrence; no claim that this review PR edited the scientific record.
- Use separately authorized guarded curation and append-only history for later record changes.
- Recheck claim-level source scopes and run documented native schema/strict, label, reference, history and QC gates after later curation.

### plaque-t3-A1

Preserve both the2003 positive interpretation and2020 contrary C58 results with the2024 counterargument, their strain/preparation/marker limits and an unresolved identity-conflict discussion.

- Retain exact stable issue key and previous occurrence; no claim that this review PR edited the scientific record.
- Use separately authorized guarded curation and append-only history for later record changes.
- Recheck claim-level source scopes and run documented native schema/strict, label, reference, history and QC gates after later curation.

### plaque-t3-A2

Correct every maintained attribution of DOI10.1128/MMBR.00042-23 to Roberto Docampo alone, including any newly added edge evidence; keep the valid DOI and collection year.

- Retain exact stable issue key and previous occurrence; no claim that this review PR edited the scientific record.
- Use separately authorized guarded curation and append-only history for later record changes.
- Recheck claim-level source scopes and run documented native schema/strict, label, reference, history and QC gates after later curation.

### micro-A1

Retain the canonical example; either provide evidence for the encoded taxon-wide frequency and explain it in the distribution note, or remove the unsupported frequency row. Do not substitute a guessed VARIABLE value.

- The justification for COMMON concerns occurrence among taxon members, not organelle abundance within a cell.
- Species/culture adhesion and membrane-donation evidence remain preserved.
- Use separately authorized guarded curation, append-only history, native focused/identifier/product checks and regeneration.

### septin-S2357-C1

Describe ammonium and nitric oxide as HZS substrates with a distinct input of reducing equivalents from the supported electron-transfer loop. Preserve uncertainty about the exact carrier mechanism.

- Role, edge and evidence note agree with the cited balanced reaction.
- Do not claim ammonium supplies the three electrons to its own condensation step.
- Use separately authorized guarded curation, append-only history, native focused/identifier/product checks and regeneration.

### septin-S2357-C2

Separate the HDH role from HOX and other HAO-like enzymes, or explicitly qualify a grouped inventory so only the experimentally identified HDH supplies the hydrazine oxidation edge. Preserve valid localization and identity examples.

- Q1PX48 is not represented as the physiological HDH based on a weak in-vitro side reaction.
- Unresolved HAO-like functions remain unresolved; graph component identity matches the reacting enzyme.
- Use separately authorized guarded curation, append-only history, native focused/identifier/product checks and regeneration.

### septin-S2357-C3

Record assembly requirements as unresolved unless direct source-specific organelle-formation evidence can be supplied. Keep proven localization and catalytic importance in their appropriate fields.

- Distinguish organelle formation from anammox activity, growth and viability.
- Do not change the collective membrane constitutional requirement merely because individual lipid perturbations are unknown.
- Use separately authorized guarded curation, append-only history, native focused/identifier/product checks and regeneration.

### septin-S2357-C4

Retarget the localization assertion to the measured soluble enzymes, or provide a direct source for the membrane-associated carrier cohort. Preserve the explicitly proposed energy-transfer model without presenting the2015 study as its localization assay.

- Distinguish soluble matrix enzymes from the putative membrane carriers.
- Do not infer absence of membrane carriers from this experiment.
- Use separately authorized guarded curation, append-only history, native focused/identifier/product checks and regeneration.

### septin-S2357-C5

Correct repeated attribution and retain the2004 review where it actually supports the claim; cite the independently verified2002 discovery paper only where its inspected scope is intended. Correct the2015 first-author shorthand.

- Every PMID/DOI and author/year/title combination agrees with native bibliographic metadata.
- Do not replace relevant references indiscriminately or imply new full-text access to the2002 paper.
- Use separately authorized guarded curation, append-only history, native focused/identifier/product checks and regeneration.

### septin-S2357-C6

Correct repeated attribution and retain the2004 review where it actually supports the claim; cite the independently verified2002 discovery paper only where its inspected scope is intended. Correct the2015 first-author shorthand.

- Every PMID/DOI and author/year/title combination agrees with native bibliographic metadata.
- Do not replace relevant references indiscriminately or imply new full-text access to the2002 paper.
- Use separately authorized guarded curation, append-only history, native focused/identifier/product checks and regeneration.

### septin-S2357-C7

Remove B9PY98 from this apicoplast component or replace it with the independently verified C9WWW6/Der1Ap example and source bridge. Preserve its unreviewed status, correct taxon and the absence of a native gene-name field; retain other examples on their own evidence.

- Native sequence cross-references distinguish ER and apicoplast paralogs.
- Replacement example has exact taxon/status and source-supported alias, without inventing a UniProt primary gene symbol.
- Run focused schema, strict CURIE and UniProt checks.

### septin-S2357-C8

Ground the Tic20 protein class to InterPro:IPR005691 and update its note/TODO without extending that identifier to the whole import complex or heterogeneous SELMA system.

- Native entry is Family and the example matches it.
- Organism-specific localization and import evidence remain separate.
- Focused validators pass.

### septin-S2357-C9

Use Tic20 inner-membrane import component and an import-dependency predicate/description, or cite direct evidence for the stronger channel claim. Preserve the paper’s accessory/regulatory uncertainty.

- Graph wording distinguishes import requirement from demonstrated pore/translocation activity.
- Supported inner-membrane localization and import phenotype remain.
- Focused validators pass.

### septin-S2357-C10

Describe the demonstrated ubiquitylation/ubiquitin-like machinery while retaining the unresolved endogenous modifier, or provide direct evidence for ubiquitin use in vivo.

- Component wording distinguishes the tested in-vitro substrate from the endogenous modifier.
- Import-perturbation and enzyme-activity evidence remain accurately scoped.
- Focused validators pass.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| current-record-0 | data/structures/inclusion/proteasome_storage_granule.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 e09339d5bc79d9ee31b2e5e342b82a67992e86fc4d2fd16559791fefa46121af; current SHA256 c905148a1f69e6dbcdca6de2e92701f51186b790ade37268bd009786a08b49d0. Changed record reassessed against current sources. |
| original-review-0 | reviews/structured/20261021T104739Z-proteasome-storage-granule-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-1 | data/structures/inclusion/protein_aggregate_center.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b; current SHA256 c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b. Record bytes unchanged since the original review. |
| original-review-1 | reviews/structured/20261021T104740Z-protein-aggregate-center-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-2 | data/structures/membrane_organelle/acidocalcisome_lumen.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 3238b530f5846e584dfb86651fd4895cb461e26bcc74afa51f3740815fab02e9; current SHA256 3238b530f5846e584dfb86651fd4895cb461e26bcc74afa51f3740815fab02e9. Record bytes unchanged since the original review. |
| original-review-2 | reviews/structured/20261021T104741Z-acidocalcisome-lumen-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-3 | data/structures/membrane_organelle/acidocalcisome_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 2a2a8ddf090bccdc6e8f0fd6b84f3e2ce971789071cb6af97dde48ed834f3a55; current SHA256 50bb07e7d5b68718300fd375225e45528a00f82eb091e413d4c184a66134fca8. Changed record reassessed against current sources. |
| original-review-3 | reviews/structured/20261021T104742Z-acidocalcisome-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-4 | data/structures/membrane_organelle/actinophryid_extrusome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 4b0f4ea17353cf6db5e343ef4a88ddc1458185fdcb508b74ca4fa8685421d0ea; current SHA256 48d64d84e4dcd8ddfd271c19c1b259b2357e09ef92625ecfaa09e65c9b26bbe5. Changed record reassessed against current sources. |
| original-review-4 | reviews/structured/20261021T104743Z-actinophryid-extrusome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-5 | data/structures/membrane_organelle/anammoxosome.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 c98e06c7ce32979c1cb1a54179f4395700a59adfcc5c0a1947c5b30f9fb34b84; current SHA256 50adeae38935dda1315b70ceec936b8224d4e6db33f07cd5caf60da96e95b1fa. Changed record reassessed against current sources. |
| original-review-5 | reviews/structured/20261021T104744Z-anammoxosome-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-6 | data/structures/membrane_organelle/anammoxosome_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 0a47b8cfa7bc71dcfc8cb69ba625087ce23025f9a1204b0fe578d185c2035f61; current SHA256 0a47b8cfa7bc71dcfc8cb69ba625087ce23025f9a1204b0fe578d185c2035f61. Record bytes unchanged since the original review. |
| original-review-6 | reviews/structured/20261021T104745Z-anammoxosome-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-7 | data/structures/membrane_organelle/apicomplexan_dense_granule.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 49d7347778d1dd9a80bf5ab53049d35eeefad4aee5581cb2c493dab7bb1c0bb2; current SHA256 f78f51681a7a3d41ee0b7e4cdd0472b998e517b697cd25abdcf1e3e2cf5aa4d1. Changed record reassessed against current sources. |
| original-review-7 | reviews/structured/20261021T104745Z-apicomplexan-dense-granule-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-8 | data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b; current SHA256 bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b. Record bytes unchanged since the original review. |
| original-review-8 | reviews/structured/20261021T104746Z-apicomplexan-dense-granule-membrane-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| current-record-9 | data/structures/membrane_organelle/apicoplast.yaml; Whole current maintained record; exact bytes frozen by native inspect | context_only | Original frozen SHA256 92a545baa209311fdb4b224a2253a543c1a67c87b35b8004334c9bebf02f5186; current SHA256 00971d8425f63fc5d490907a43c00b6760c2d88c5413fce6bdbc2dd09919410e. Changed record reassessed against current sources. |
| original-review-9 | reviews/structured/20261021T104747Z-apicoplast-audit/review.yaml; Original immutable observation: sources, checks, scientific verdict, findings, actions and limitations | context_only | Historical review retained without rewriting its evidence or promoting old checks to current execution. |
| plaque-current-2 | data/structures/membrane_organelle/acidocalcisome_lumen.yaml; Entire current YAML at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4; every field, history and graph edge | context_only | Entire maintained target read against the frozen inspection bytes; current PROPOSED status is preserved. No target image is declared. |
| plaque-original-2 | reviews/structured/20261021T104741Z-acidocalcisome-lumen-audit/review.yaml; Complete authoritative YAML and exact derived Markdown; findings, checks, source inputs and all assessments | context_only | Original review 20261021T104741Z-acidocalcisome-lumen-audit independently inspected. Native validation and exact render passed; the historical target bytes match its frozen hash. |
| plaque-current-3 | data/structures/membrane_organelle/acidocalcisome_membrane.yaml; Entire current YAML at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4; every field, history and graph edge | context_only | Entire maintained target read against the frozen inspection bytes; current PROPOSED status is preserved. No target image is declared. |
| plaque-original-3 | reviews/structured/20261021T104742Z-acidocalcisome-membrane-audit/review.yaml; Complete authoritative YAML and exact derived Markdown; findings, checks, source inputs and all assessments | context_only | Original review 20261021T104742Z-acidocalcisome-membrane-audit independently inspected. Native validation and exact render passed; the historical target bytes match its frozen hash. |
| plaque-current-7 | data/structures/membrane_organelle/apicomplexan_dense_granule.yaml; Entire current YAML at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4; every field, history and graph edge | context_only | Entire maintained target read against the frozen inspection bytes; current PROPOSED status is preserved. No target image is declared. |
| plaque-original-7 | reviews/structured/20261021T104745Z-apicomplexan-dense-granule-audit/review.yaml; Complete authoritative YAML and exact derived Markdown; findings, checks, source inputs and all assessments | context_only | Original review 20261021T104745Z-apicomplexan-dense-granule-audit independently inspected. Native validation and exact render passed; the historical target bytes match its frozen hash. |
| plaque-current-8 | data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml; Entire current YAML at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4; every field, history and graph edge | context_only | Entire maintained target read against the frozen inspection bytes; current PROPOSED status is preserved. No target image is declared. |
| plaque-original-8 | reviews/structured/20261021T104746Z-apicomplexan-dense-granule-membrane-audit/review.yaml; Complete authoritative YAML and exact derived Markdown; findings, checks, source inputs and all assessments | context_only | Original review 20261021T104746Z-apicomplexan-dense-granule-membrane-audit independently inspected. Native validation and exact render passed; the historical target bytes match its frozen hash. |
| plaque-whole-organelle | data/structures/membrane_organelle/acidocalcisome.yaml; Frozen local context; relevant boundary, evidence, schema and review rules | context_only | Whole organelle supplies boundary and existing bacterial-dispute context only, not an independent scientific review of that neighboring record. |
| plaque-policy | .claude/skills/review-yaml-record/SKILL.md; Frozen local context; relevant boundary, evidence, schema and review rules | context_only | Repository policy requires claim-level support, exact input provenance, separate identity/membership/necessity, bounded adapter applicability and immutable reviews. |
| plaque-rubric | .claude/skills/curate-yaml-record/references/review-checklist.md; Frozen local context; relevant boundary, evidence, schema and review rules | context_only | Repository policy requires claim-level support, exact input provenance, separate identity/membership/necessity, bounded adapter applicability and immutable reviews. |
| plaque-graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Frozen local context; relevant boundary, evidence, schema and review rules | context_only | Repository policy requires claim-level support, exact input provenance, separate identity/membership/necessity, bounded adapter applicability and immutable reviews. |
| plaque-schema-policy | src/cellstructuremech/schema/cellstructuremech.yaml; Frozen local context; relevant boundary, evidence, schema and review rules | context_only | Repository policy requires claim-level support, exact input provenance, separate identity/membership/necessity, bounded adapter applicability and immutable reviews. |
| plaque-acidocalcisome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033985,GO:0033102,GO:0043233,GO:0020022,GO:0016020; results for GO0033985, GO0033102, GO0043233, GO0020022, GO0016020: id/name/isObsolete/definition; GO0020022.children relation fields | supports | Five active native GO cellular-component terms verify lumen, membrane, organelle lumen, acidocalcisome and generic membrane identities. GO0020022 lists GO0033985 and GO0033102 children with part_of relations; this does not turn parthood into is_a. The definitions distinguish enclosed volume from lipid boundary. |
| plaque-acidocalcisome-agent-lumen-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033985/ancestors?relations=is_a; results[0].id and ancestors; request relations=is_a | supports | The requested is_a ancestor closure for GO0033985 includes GO0043233 organelle lumen. Acidocalcisome parthood is independently supported by the separate native term and location responses. |
| plaque-acidocalcisome-agent-SL-0316 | https://rest.uniprot.org/locations/SL-0316.json; id/name/definition/synonyms/geneOntologies/partOf | supports | Native SL0316 identifies acidocalcisome lumen, supplies the acidocalcisomal lumen synonym and GO0033985 cross-reference, and places it partOf SL0002 acidocalcisome. Its definition specifies the membrane-bounded compartment. |
| plaque-acidocalcisome-agent-SL-0003 | https://rest.uniprot.org/locations/SL-0003.json; id/name/definition/synonyms/geneOntologies/isA/partOf | supports | Native SL0003 identifies acidocalcisome membrane, supplies its synonym and GO0033102 cross-reference, has isA SL0162 membrane, and partOf SL0002 acidocalcisome. |
| plaque-acidocalcisome-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Native taxId, scientificName, rank and supplied lineage fields; identity only. | supports | Native taxonomy verifies taxon2 as Bacteria. This identifies the taxon and lineage only; it does not establish organelle occurrence, strain equivalence or universality. |
| plaque-acidocalcisome-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Native taxId, scientificName, rank and supplied lineage fields; identity only. | supports | Native taxonomy verifies taxon2759 as Eukaryota. This identifies the taxon and lineage only; it does not establish organelle occurrence, strain equivalence or universality. |
| plaque-acidocalcisome-agent-tax-358 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/358; Native taxId, scientificName, rank and supplied lineage fields; identity only. | supports | Native taxonomy verifies taxon358 as Agrobacterium tumefaciens. This identifies the taxon and lineage only; it does not establish organelle occurrence, strain equivalence or universality. |
| plaque-acidocalcisome-agent-doi-2003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074%2Fjbc.M304548200&amp;format=json&amp;resultType=core; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Exact native metadata identifies Seufferheld and colleagues, PMID12783865, DOI10.1074/jbc.M304548200. The complete abstract reports a surrounding membrane by TEM, PPase localization by immunofluorescence/immuno-EM, enriched PPase/polyphosphate fractions, cations and acidic staining in A. tumefaciens. The abstract calls the PPase K-insensitive. This is primary abstract support, not an inspected full body or a resolved strain/accession bridge. |
| plaque-acidocalcisome-agent-doi-2005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro1097&amp;format=json&amp;resultType=core; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Exact native citation identifies Acidocalcisomes - conserved from bacteria to man, Docampo, de Souza, Miranda, Rohloff and Moreno, PMID15738951, DOI10.1038/nrmicro1097. Citation and complete abstract were read; this receipt is not the article body. |
| plaque-acidocalcisome-agent-review2005-publisher | https://www.nature.com/articles/nrmicro1097; Publisher HTML Abstract section and Key Points bullets1–5 only; no full-main-body claim | supports | The accessible review Abstract and five Key Points describe acidic polyphosphate/cation compartments, broad reported occurrence, and membrane Ca-ATPase, V-ATPase, V-PPase and exchange activities. This is secondary synthesis with lineage variation, not a new primary transport assay. The remaining main article body was not available in this response. |
| plaque-acidocalcisome-agent-doi-2020 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FAEM.02759-19&amp;format=json&amp;resultType=core; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Exact native citation identifies Frank and Jendrossek 2020, PMID32060025, PMC7117937, DOI10.1128/AEM.02759-19. The complete abstract proposes that polyphosphate granules and HppA-positive structures are distinct in A. tumefaciens; actual Methods/Results support is in the separately hashed PMC body. |
| plaque-acidocalcisome-agent-pmc2020-native | https://pmc.ncbi.nlm.nih.gov/articles/PMC7117937/; Primary HTML: Results/Discussion §§2.1–2.3,2.5–2.6,2.8 and Methods §§3.1–3.5; Figure5 caption. No figure-pixel or supplementary-data audit. | supports | Frank and Jendrossek 2020 use C58 fluorescence, marker-localization and mutant experiments to distinguish DAPI-positive polyphosphate granules from HppA/MitoTracker-associated structures. They explicitly lack TEM confirmation. Full-length C58 Atu_1174 is not the D44 Q8VPZ0 fragment. The results challenge, rather than definitively disprove, the original bacterial acidocalcisome interpretation. |
| plaque-acidocalcisome-agent-doi-2024 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMMBR.00042-23&amp;format=json&amp;resultType=core; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Exact native citation identifies Advances in the cellular biology, biochemistry, and molecular biology of acidocalcisomes, PMID38099688, PMC10966946, DOI10.1128/MMBR.00042-23, with Roberto Docampo as the sole author. Collection year2024 is valid; no Huang appears in the author list. |
| plaque-acidocalcisome-agent-pmc2024-native | https://pmc.ncbi.nlm.nih.gov/articles/PMC10966946/; Secondary review HTML: byline; §§1–3; §4 direct chemical-composition paragraphs; §§5.1 proton pumps,5.2 P-type ATPases,5.5 membrane transporters; §10 cation/phosphorus storage. No comprehensive proteomic-table or figure-pixel audit. | supports | Sole author Roberto Docampo. The distribution section preserves and challenges the C58 interpretation, including short-polyphosphate/DAPI limits. Membrane sections distinguish lineage-dependent pumps, Ca2+ uptake, metal/proton exchange, phosphate/sodium release and incompletely characterized transporters. §10 explicitly supports metal sequestration driven by proton gradients; this is secondary synthesis, not new primary experiments or universal transporter direction. |
| plaque-acidocalcisome-agent-membrane-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033102/ancestors?relations=is_a; results[0].id and ancestors; request relations=is_a | supports | The requested is_a ancestor closure for GO0033102 includes GO0016020 membrane. It is separate from the acidocalcisome part_of relation. |
| plaque-acidocalcisome-agent-Q8VPZ0 | https://rest.uniprot.org/uniprotkb/Q8VPZ0.json; primaryAccession, entryType, proteinDescription, genes, organism, sequence.length, fragment flag, references/source strain, FUNCTION and SUBCELLULAR LOCATION comments/evidence codes | supports | Native Q8VPZ0 is reviewed, gene hppA with synonym vppA, tax358, and the stated putative K-stimulated pyrophosphate-energized sodium-pump name. It is a189-aa fragment submitted from strainD44. Function and cell-inner-membrane annotations are inferred by homology; no experimental acidocalcisome localization is established by this entry. |
| plaque-acidocalcisome-agent-Q8VPZ0-matches | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8VPZ0/?page_size=200; count, next and results[0].metadata plus protein match coordinates | supports | The complete native integrated InterPro result has count1 and next=null, assigning the189-aa Q8VPZ0 fragment to IPR004131 over positions1–187. This provides one integrated family candidate for the inspected protein. |
| plaque-acidocalcisome-agent-IPR004131 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004131/; metadata accession/name/type/description and member_databases/signature names | supports | IPR004131 is the pyrophosphate-energised proton-pump family; its native description concerns membrane pyrophosphatases and distinguishes K-stimulated/K-insensitive subclasses. The member signatures include a putative sodium-pump signature. |
| plaque-granule-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020026,GO:0030141,GO:0030668; Complete GO0020026, GO0030141 and GO0030668 definitions, synonyms and relevant relations | supports | Native GO confirms the secretory dense-granule definition, RELATED dense body synonym, secretory-granule parent and distinct bounding-membrane part. |
| plaque-granule-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Native taxId, scientificName, rank and supplied lineage fields; identity only. | supports | Native ENA taxonomy identifies Eukaryota, domain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plaque-granule-agent-tax-5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; Native taxId, scientificName, rank and supplied lineage fields; identity only. | supports | Native ENA taxonomy identifies Apicomplexa, phylum. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plaque-granule-agent-tax-5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Native taxId, scientificName, rank and supplied lineage fields; identity only. | supports | Native ENA taxonomy identifies Toxoplasma gondii, species. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plaque-granule-agent-tax-508771 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771; Native taxId, scientificName, rank and supplied lineage fields; identity only. | supports | Native ENA taxonomy identifies Toxoplasma gondii ME49, strain. This receipt attests that identity and rank only, not occurrence or the experimental strain. |
| plaque-granule-agent-P13403 | https://rest.uniprot.org/uniprotkb/P13403.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant location/function comments, sequence references and cross-references | supports | Native UniProtKB reviewed (Swiss-Prot) P13403: Dense granule protein 1; taxon 5811; gene fields [{"geneName": {"value": "GRA1"}}]. Accession identity and predicted location annotations do not by themselves prove membership in the maintained structure. |
| plaque-granule-agent-P13404 | https://rest.uniprot.org/uniprotkb/P13404.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant location/function comments, sequence references and cross-references | supports | Native UniProtKB reviewed (Swiss-Prot) P13404: Dense granule protein 2; taxon 5811; gene fields [{"geneName": {"value": "GRA2"}}]. Accession identity and predicted location annotations do not by themselves prove membership in the maintained structure. |
| plaque-granule-agent-Q27003 | https://rest.uniprot.org/uniprotkb/Q27003.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant location/function comments, sequence references and cross-references | supports | Native UniProtKB reviewed (Swiss-Prot) Q27003: Dense granule protein 6; taxon 5811; gene fields [{"geneName": {"value": "GRA6"}, "synonyms": [{"value": "TG24"}]}]. Accession identity and predicted location annotations do not by themselves prove membership in the maintained structure. |
| plaque-granule-agent-A0A125YME4 | https://rest.uniprot.org/uniprotkb/A0A125YME4.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant location/function comments, sequence references and cross-references | supports | Native UniProtKB unreviewed (TrEMBL) A0A125YME4: Dense granule protein DG32; taxon 508771; gene fields [{"orfNames": [{"evidences": [{"evidenceCode": "ECO:0000313", "source": "EMBL", "id": "EPT32203.1"}], "value": "TGME49_297880"}]}]. Accession identity and predicted location annotations do not by themselves prove membership in the maintained structure. |
| plaque-granule-agent-matches-P13404 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13404/?page_size=200; All results; next is null | context_only | Complete integrated matches were inspected; these individual-family matches do not identify the aggregate GRA cargo or exported-effector cohort. |
| plaque-granule-agent-matches-Q27003 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q27003/?page_size=200; All results; next is null | context_only | Complete integrated matches were inspected; these individual-family matches do not identify the aggregate GRA cargo or exported-effector cohort. |
| plaque-granule-agent-IPR008118 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008118/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | Gra2 protein is a specific family, not an exact grounding for the whole dense-granule cargo cohort. |
| plaque-granule-agent-IPR008119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008119/; Native InterPro metadata name/type, description and membership scope; predictive description provenance retained where marked | supports | Dense granule protein6/2 is a family entry for a subset of cargo, not the unrelated full GRA or exported-effector cohort. |
| plaque-granule-agent-doi-10.1111_jeu.12904 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/jeu.12904; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Native metadata identifies Dense granule biogenesis, secretion, and function in Toxoplasma gondii. Authors: Griffith MB, Pearce CS, Heaslip AT.; PMID 35302693; DOI 10.1111/jeu.12904. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plaque-granule-agent-doi-10.1016_j.pt.2014.12.002 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.pt.2014.12.002; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Native metadata identifies Toxoplasma secretory granules: one population or more? Authors: Mercier C, Cesbron-Delauw MF.; PMID 25599584; DOI 10.1016/j.pt.2014.12.002. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plaque-granule-agent-doi-10.1016_j.ijpara.2005.03.011 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.ijpara.2005.03.011; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Mercier2005 review abstract compares Plasmodium and Toxoplasma dense-granule systems and their variable PV adaptations. This supports qualitative cross-apicomplexan occurrence, not measured prevalence or identical cargo. Publisher body returned403 and is not represented as inspected. |
| plaque-granule-agent-doi-10.1016_j.chom.2015.04.003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.chom.2015.04.003; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Native metadata identifies The Toxoplasma Dense Granule Proteins GRA17 and GRA23 Mediate the Movement of Small Molecules between the Host and the Parasitophorous Vacuole. Authors: Gold DA, Kaplan AD, Lis A, Bett GC, Rosowski EE, Cirelli KM, Bougdour A, Sidik SM, Beck JR, Lourido S, Egea PF, Bradley PJ, Hakimi MA, Rasmusson RL, Saeij JP.; PMID 25974303; DOI 10.1016/j.chom.2015.04.003. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plaque-granule-agent-doi-10.1016_j.parint.2013.04.003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.parint.2013.04.003; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Masatani2013 primary abstract reports GRA23 immuno-EM localization in dense granules, PVM and intravacuolar network. Only abstract/bibliographic evidence is used. |
| plaque-granule-agent-doi-10.1016_j.chom.2013.03.002 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.chom.2013.03.002; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Bougdour2013 primary abstract explicitly identifies GRA16 as dense-granule cargo exported across the PVM to the host nucleus, where it modulates host gene expression. This supports the new GRA16 edges at abstract scope; the complete primary body was not accessed. |
| plaque-granule-agent-pmid-9208224 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9208224%20AND%20SRC%3AMED; Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID and available abstract; no full-body inference from this endpoint. | supports | Native metadata identifies Sequential protein secretion from three distinct organelles of Toxoplasma gondii accompanies invasion of human fibroblasts. Authors: Carruthers VB, Sibley LD.; PMID 9208224; DOI None. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| plaque-granule-agent-jats-PMC9482668 | https://pmc-oa-opendata.s3.amazonaws.com/PMC9482668.1/PMC9482668.1.xml; Secondary JATS review: §§S2–S8,S13,S18,S20,S21 direct paragraphs. No independent figures, supplements or full-proteome audit. | supports | Griffith2022 supports dense-granule biogenesis, stored cargo, membrane boundary, secretion and later cargo functions. It separates stored transmembrane cargo from resident granule membrane proteins and distinguishes PVM permeability from effector export. Unresolved individual assembly requirements and incomplete resident-protein inventories are explicit. |
| plaque-granule-agent-jats-PMC4435723 | https://pmc-oa-opendata.s3.amazonaws.com/PMC4435723.1/PMC4435723.1.xml; Primary JATS: Results §§S3,S4,S6,S7,S8; Discussion S9; Methods S12,S14,S15,S16,S18; complete Table1. No independent figure-pixel or supplementary-data audit. | supports | Gold2015 supports dense-granule/PVM localization, passive small-molecule permeability, unequal GRA17/GRA23 single-deletion phenotypes and synergistic growth requirements. RH/other experimental strain contexts and Xenopus oocyte assays remain scoped. Table1 names GT1 loci; it does not alone bridge the current ME49 accessions. GRA17/23 protein-export effects and pore stoichiometry are not established; neither is organelle-assembly necessity. |
| plaque-granule-agent-pmc-PMC13475723 | https://pmc.ncbi.nlm.nih.gov/articles/PMC13475723/; Primary HTML: Methods S3, Results S15–S18 and Discussion S19 direct paragraphs; no figure-pixel or other supplementary-data audit. | supports | Carruthers/Sibley1997 RH tachyzoite/HFF experiments measure delayed GRA1/NTPase secretion after invasion, compared with earlier microneme/rhoptry secretion, while extracellular secretion remains possible. This supports timing in the stated model, not exclusive secretion after invasion or a universal apicomplexan rate. |
| plaque-granule-agent-jats-PMC7202600 | https://pmc-oa-opendata.s3.amazonaws.com/PMC7202600.1/PMC7202600.1.xml; Primary JATS complete Table1 identity rows specifically TGME49_222170/GRA17 and TGME49_297880/GRA23; bibliographic identity only. | supports | The published table bridges both exact ME49 locus identifiers to GRA17 and GRA23. This is an identifier bridge, not an independent reassessment of that paper’s experimental findings or a transfer of GT1 phenotype data to ME49. |
| plaque-granule-agent-gene-7901472 | https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/7901472; Complete gene identity, locus_tag, organism and annotation fields | supports | NCBI Gene7901472 identifies the ME49 locus TGME49_297880 as dense granule protein DG32, taxon508771. This is the native locus bridge, not independent functional evidence. |
| plaque-granule-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020026,GO:0030668,GO:0031090; Complete definitions, synonyms and relevant relations of all three native terms | supports | GO0030668 identifies the lipid bilayer surrounding an apicomplexan dense granule. GO0031090 is the broader organelle-membrane class; GO0020026 identifies the bounded secretory organelle. |
| plaque-gra17-S8GTZ8 | https://rest.uniprot.org/uniprotkb/S8GTZ8.json; Accession, unreviewed status, submitted protein name, TGME49_222170 ORF name, ME49 taxon508771, reference and GeneID/RefSeq links | supports | S8GTZ8 is an unreviewed ME49 dense-granule-antigen DG32 entry with ORF TGME49_222170. The source does not experimentally establish GRA17 function or localization; exact GRA17 linkage comes from the independently read primary Table1. |
| plaque-gra17-gene | https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/7895641; reports[0].gene identity, locus_tag, tax_id, taxname, description and annotation | supports | NCBI Gene7895641 verifies the ME49 TGME49_222170 locus and DG32 annotation. This cross-check is identity evidence only. |
| plaque-catalogue | https://imodulondb.org/api/datasets; Entire native /api/datasets response: all20 organism rows and dataset keys; no pagination | supports | Fresh catalogue has no Agrobacterium tumefaciens or Toxoplasma gondii organism/dataset. Broad Bacteria/Eukaryota distribution does not authorize substituting a different organism for hppA or GRA accessions. No matched gene/module query applies; catalogue absence is not biological absence. |
| plaque-gra17-matches | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/S8GTZ8/?page_size=200; Exact accession InterPro endpoint attempt; HTTP204 plus curl92 malformed-header transport failure and empty response | context_only | Inconclusive endpoint response; no assertion of zero families, absence of a gene or absence of biological function. |
| plaque-gra23-matches | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A0A125YME4/?page_size=200; Exact accession InterPro endpoint attempt; HTTP204 plus curl92 malformed-header transport failure and empty response | context_only | Inconclusive endpoint response; no assertion of zero families, absence of a gene or absence of biological function. |
| plaque-gra1-matches | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13403/?page_size=200; Exact accession InterPro endpoint attempt; HTTP204 plus curl92 malformed-header transport failure and empty response | context_only | Inconclusive endpoint response; no assertion of zero families, absence of a gene or absence of biological function. |
| plaque-historical-runner | /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources imodulondb datasets; Historical receipt and stdout/stderr independently reread and hash-verified; execution occurred00:49Z, not during this subreview | context_only | Historical runner exited1 before dataset execution because of OS PermissionError reading pyvenv.cfg. It remains unavailable historical context; current source catalogue fallback is separately fetched. No current adapter-run success is claimed. |
| plaque-native-acidocalcisome_lumen-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_lumen.yaml --verify; Actual root-owned acidocalcisome_lumen-uniprot-verify-receipt.json and exact stdout log independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-acidocalcisome_lumen-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_lumen.yaml --causal-graphs; Actual root-owned acidocalcisome_lumen-uniprot-causal-receipt.json and exact stdout log independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| plaque-native-acidocalcisome_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml --verify; Actual root-owned acidocalcisome_membrane-uniprot-verify-receipt.json and exact stdout log independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-acidocalcisome_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml --causal-graphs; Actual root-owned acidocalcisome_membrane-uniprot-causal-receipt.json and exact stdout log independently read/hash-verified | supports | data/structures/membrane_organelle/acidocalcisome_membrane.yaml  (GO:0033102)<br>  acidocalcisome_membrane_ion_transport	proton_pumps	COVERED	-&gt;proton_pumps (UniProtKB:Q8VPZ0)<br>  acidocalcisome_membrane_ion_transport	cation_transporters	NO_GENE_SYMBOLS	-&gt;cation_transporters (PROTEIN: acidocalcisome cation transporters)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| plaque-native-apicomplexan_dense_granule-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml --verify; Actual root-owned apicomplexan_dense_granule-uniprot-verify-receipt.json and exact stdout log independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-apicomplexan_dense_granule-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml --causal-graphs; Actual root-owned apicomplexan_dense_granule-uniprot-causal-receipt.json and exact stdout log independently read/hash-verified | supports | data/structures/membrane_organelle/apicomplexan_dense_granule.yaml  (GO:0020026)<br>  dense_granule_cargo_pvm_permeability	dense_granule_proteins	COVERED	-&gt;dense_granule_proteins (UniProtKB:P13403, UniProtKB:P13404, UniProtKB:Q27003)<br>  dense_granule_cargo_pvm_permeability	gra17_gra23_permeability_factors	COVERED	-&gt;gra17_gra23_permeability_factors (UniProtKB:A0A125YME4, UniProtKB:S8GTZ8)<br>  dense_granule_cargo_pvm_permeability	exported_dense_granule_effectors	NO_GENE_SYMBOLS	-&gt;exported_dense_granule_effectors (PROTEIN: exported dense granule effectors)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| plaque-native-apicomplexan_dense_granule_membrane-verify | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml --verify; Actual root-owned apicomplexan_dense_granule_membrane-uniprot-verify-receipt.json and exact stdout log independently read/hash-verified | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| plaque-native-apicomplexan_dense_granule_membrane-causal | .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml --causal-graphs; Actual root-owned apicomplexan_dense_granule_membrane-uniprot-causal-receipt.json and exact stdout log independently read/hash-verified | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| micro-review-policy | .claude/skills/review-yaml-record/SKILL.md; Evidence Rules; Structured Source Cross-Checks; Output | supports | Native read-only claim-scoped review; named genes/proteins/stress claims trigger structured-source applicability before downstream matching. A missing expression claim is not an exemption. |
| micro-review-config | conf/record_review.yaml; version1 skills and rubrics | supports | The frozen configuration and all17 common policy/schema/verifier files are byte-identical to the prior independently read cohort; config, review skill and profile were freshly reread. No unknown local dependency was silently adopted. |
| micro-presence-enum | src/cellstructuremech/schema/cellstructuremech.yaml; PresenceEnum.COMMON | supports | COMMON means occurrence in most taxon members, not numerous organelles in a cell. |
| micro-original-validation-inputs | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/adversary-microtubule/original-validation-inputs.json; All3 original bundles: native validate and render --content; original source blob/current hash comparison | supports | All three validate and deterministic Markdown comparisons pass. PSG and extrusome hashes differ from their original frozen inputs; PAC is unchanged. This proves historical artifact integrity, not current scientific sufficiency. |
| micro-record-proteasome_storage_granule | data/structures/inclusion/proteasome_storage_granule.yaml; Entire current YAML including components, causal graphs, discussions, evidence and history | supports | Current source record independently read; SHA256 c905148a1f69e6dbcdca6de2e92701f51186b790ade37268bd009786a08b49d0. Original frozen input e09339d5bc79d9ee31b2e5e342b82a67992e86fc4d2fd16559791fefa46121af; stale=True. |
| micro-prior-proteasome_storage_granule | reviews/structured/20261021T104739Z-proteasome-storage-granule-audit/review.yaml; Entire original structured review and native rendered Markdown; checks, assessments, verdict, findings/actions and frozen inputs | supports | Preserved historical observation 20261021T104739Z-proteasome-storage-granule-audit; original verdict pass_with_limitations. The original stable finding is retained only where present; clean original verdict does not certify a changed record. |
| micro-native-proteasome_storage_granule-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/proteasome_storage_granule-uniprot-verify-receipt.json; Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml --verify; adjacent log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source command returned0 at 2026-11-03T08:54:26.748129+00:00. Scope: 3 protein_examples; no GENE_OR_PROTEIN causal nodes. Identity/coverage checks do not establish localization, biological necessity, complete inventory or source support. |
| micro-native-proteasome_storage_granule-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/proteasome_storage_granule-uniprot-causal-receipt.json; Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml --causal-graphs; adjacent log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual current-source command returned0 at 2026-11-03T08:54:27.172124+00:00. Scope: 0 GENE_OR_PROTEIN causal nodes. Identity/coverage checks do not establish localization, biological necessity, complete inventory or source support. |
| micro-record-protein_aggregate_center | data/structures/inclusion/protein_aggregate_center.yaml; Entire current YAML including components, causal graphs, discussions, evidence and history | supports | Current source record independently read; SHA256 c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b. Original frozen input c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b; stale=False. |
| micro-prior-protein_aggregate_center | reviews/structured/20261021T104740Z-protein-aggregate-center-audit/review.yaml; Entire original structured review and native rendered Markdown; checks, assessments, verdict, findings/actions and frozen inputs | supports | Preserved historical observation 20261021T104740Z-protein-aggregate-center-audit; original verdict pass_with_limitations. The original stable finding is retained only where present; clean original verdict does not certify a changed record. |
| micro-native-protein_aggregate_center-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/protein_aggregate_center-uniprot-verify-receipt.json; Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml --verify; adjacent log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source command returned0 at 2026-11-03T08:54:28.328672+00:00. Scope: 3 protein_examples; no GENE_OR_PROTEIN causal nodes. Identity/coverage checks do not establish localization, biological necessity, complete inventory or source support. |
| micro-native-protein_aggregate_center-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/protein_aggregate_center-uniprot-causal-receipt.json; Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml --causal-graphs; adjacent log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual current-source command returned0 at 2026-11-03T08:54:28.744398+00:00. Scope: 0 GENE_OR_PROTEIN causal nodes. Identity/coverage checks do not establish localization, biological necessity, complete inventory or source support. |
| micro-record-actinophryid_extrusome | data/structures/membrane_organelle/actinophryid_extrusome.yaml; Entire current YAML including components, causal graphs, discussions, evidence and history | supports | Current source record independently read; SHA256 48d64d84e4dcd8ddfd271c19c1b259b2357e09ef92625ecfaa09e65c9b26bbe5. Original frozen input 4b0f4ea17353cf6db5e343ef4a88ddc1458185fdcb508b74ca4fa8685421d0ea; stale=True. |
| micro-prior-actinophryid_extrusome | reviews/structured/20261021T104743Z-actinophryid-extrusome-audit/review.yaml; Entire original structured review and native rendered Markdown; checks, assessments, verdict, findings/actions and frozen inputs | supports | Preserved historical observation 20261021T104743Z-actinophryid-extrusome-audit; original verdict needs_curation. The original stable finding is retained only where present; clean original verdict does not certify a changed record. |
| micro-native-actinophryid_extrusome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/actinophryid_extrusome-uniprot-verify-receipt.json; Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml --verify; adjacent log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual current-source command returned0 at 2026-11-03T08:54:31.749630+00:00. Scope: 0 protein_examples; no accession-bearing protein causal xref. Identity/coverage checks do not establish localization, biological necessity, complete inventory or source support. |
| micro-native-actinophryid_extrusome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/actinophryid_extrusome-uniprot-causal-receipt.json; Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml --causal-graphs; adjacent log SHA256 261ce8f1199383b4ea3d3ab45e538eb12884ed3cbbd8544871b73a5fb8a2a4bf | supports | Actual current-source command returned0 at 2026-11-03T08:54:32.154161+00:00. Scope: 1 GENE_OR_PROTEIN node, anchored to GP40 component but NO_GENE_SYMBOLS; no protein_examples. Identity/coverage checks do not establish localization, biological necessity, complete inventory or source support. |
| micro-laporte2008 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.xml; Full main Introduction, Results/discussion, Methods and Figures1–5 captions; permissions; no supplementary panels/raw movies | supports | Yeast quiescent CP/RP foci and reporter colocalization, rapid nuclear return after refeeding, water control and cycloheximide context support the bounded PSG definition, parts and recovery graphs. Colocalization alone does not resolve active holoenzyme state. |
| micro-gu2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5597321.1/PMC5597321.1.xml; All Results/Discussion; Methods yeast strains/manual microscopy/proteomic analysis; all Figures1–8 captions. Introduction and automated-acquisition/dSTORM Methods were not read | supports | Blm10/Ubp6 and processed ubiquitin reporter observations support association. Crosslinked PSG enrichment and native lysate PAGE have distinct scopes; free ubiquitin is distinguished from UBI4 precursor and polyubiquitin cargo. Specific loss phenotypes are not universal structural necessity. |
| micro-tang2026 | https://pure.mpg.de/rest/items/item_3702910_1/component/file_3702923/content; Selected PDF physical pages1–4,9–13: graphical abstract, Summary, initial Results/Figure1, Figure5/6/7 captions, Discussion and first limitations page; not the entire35-page PDF | supports | In situ cryo-ET supports inactive intact26S trimers and paracrystalline fibers under energy limitation, including cytoplasmic and nuclear arrangements. Purification destabilizes assemblies; transient partners remain unresolved. The record accurately distinguishes these data from earlier colocalization/lysate results; its older abstract-only wording describes prior curation scope. |
| micro-psg-retraction | https://elifesciences.org/articles/82988; Retraction notice for eLife34532; statement on manipulated/duplicated images and unreliable archived data | supports | Retraction of DOI10.7554/eLife.34532 justifies excluding it from positive PSG claims. The record added structured REFUTE evidence for that exclusion; this does not prove every biological proposition false or resolve a whole multi-target historical issue. |
| micro-psg-commentary | https://pubmed.ncbi.nlm.nih.gov/30204036/; PubMed30204036 abstract only; related commentary, not independent primary experiments | context_only | The commentary reiterates the proteaphagy-protection claim tied to the retracted study. It is contextual exclusion evidence, not a positive source for record functions. |
| micro-boronat2023 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.xml; Full main Introduction, Results2.1–2.5, Discussion, Methods4.1–4.7, Conclusions; all Figure1–7 captions; no supplementary panel pixels/raw data | supports | W303/BY4741/972 reporter experiments distinguish37C PAC assembly, genotype/strain/time-specific persistence, Hsp104-dependent clearance, induction versus recovery CHX timing, and immunoblot-supported degradation from loss of fluorescent puncta.42C NuRs are a separate context. |
| micro-cabrera2020 | https://pubmed.ncbi.nlm.nih.gov/32075773/; PubMed32075773 complete primary abstract only | supports | Fission-yeast PAC formation, chaperone involvement and refolding are supported at abstract scope. Hsp16/Mas5/Ssa2 are bounded follow-up leads; this abstract does not alone establish all protein localization or formation necessity. No2020 full-body access is claimed. |
| micro-hausmann1982 | https://api.crossref.org/works/10.1002/cm.970020103; Publisher-deposited Crossref abstract only; DOI10.1002/cm.970020103 | supports | The abstract directly describes expanding/fusing extrusomes providing membrane during funnel-pseudopod prey enclosure. It does not identify a molecular fusogen or specific ion-channel protein. |
| micro-sakaguchi1998 | https://link.springer.com/article/10.1007/BF01279469; Publisher Summary lines35–39 in saved browser extraction; subscription preview only | supports | Summary supports axopodial extrusome abundance and adhesion in examined preparations; it does not quantify species-wide frequency. Full1998 paper was not read. |
| micro-sakaguchi2001 | https://pubmed.ncbi.nlm.nih.gov/11401035/; Primary abstract lines239–242 in saved browser extraction; PMID11401035/DOI10.1078/1434-4610-00041 | supports | Abstract directly places GP40 in extrusomes and reports adhesion/ingestion of GP40-coated beads. This supports the new component-anchored residence and adhesion edges, without assigning unreviewed sequence isoforms to the purified protein or proving organelle-formation necessity. |
| micro-kakuta2008 | https://da.lib.kobe-u.ac.jp/da/kernel/90000974/90000974.pdf; Author-manuscript PDF physical pages2–10: title, Summary, Introduction, Methods, Results and Discussion; no figure pixels/raw data | supports | Brackish Actinophrys cultures, extracellular-calcium and pharmacological adhesion assays support context-limited roles. ConA and calcium-channel blocker effects do not identify GP40 as the unique drug target or establish a localized channel inventory; ionophore depletion was proposed, not demonstrated. |
| micro-metadata-sakaguchi1998-crossref | https://api.crossref.org/works/10.1007/BF01279469; Exact DOI Crossref metadata | context_only | Exact bibliographic identity checked; metadata availability is not full-body access. |
| micro-metadata-sakaguchi2001-crossref | https://api.crossref.org/works/10.1078/1434-4610-00041; Exact DOI Crossref metadata | context_only | Exact bibliographic identity checked; metadata availability is not full-body access. |
| micro-metadata-kakuta-crossref | https://api.crossref.org/works/10.1016/j.ejop.2007.11.001; Exact DOI Crossref metadata | context_only | Exact bibliographic identity checked; metadata availability is not full-body access. |
| micro-metadata-tang2026-crossref | https://api.crossref.org/works/10.1016/j.cell.2025.12.035; Exact DOI Crossref metadata | context_only | Exact bibliographic identity checked; metadata availability is not full-body access. |
| micro-metadata-retracted2018-crossref | https://api.crossref.org/works/10.7554/eLife.34532; Exact DOI Crossref metadata | context_only | Exact bibliographic identity checked; metadata availability is not full-body access. |
| micro-go-terms | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034515,GO:0043232,GO:0005737,GO:0005839,GO:0005838,GO:0140453,GO:0020020,GO:0030141,GO:0043231; QuickGO exact retrieval of9 named GO cellular-component terms; labels, active status and definitions | supports | PSG0034515 and PAC0140453 are exact active identities; parent0043232, cytoplasm5737 and proteasome parts5839/5838 are appropriate.0043231 is a broad extrusome parent;0030141 requires Golgi origin, and0020020 has parasite-food-vacuole scope, so neither is adopted as exact extrusome/food-vacuole identity. |
| micro-extrusome-go-search | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;queryFields=label,synonym&amp;rows=100&amp;q=actinophryid%20extrusome; OLS4 GO search response: numFound0 | supports | No exact label/synonym result in this bounded query; it does not prove that all possible GO phrasings are absent. |
| micro-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA taxonomy exact taxId/scientificName/rank/lineage | supports | Exact organism identity checked. Species4932/4896 and Actinophrys238771 are distinguished from reference strain559292; authority identity does not show taxon-wide organelle occurrence. |
| micro-tax-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; ENA taxonomy exact taxId/scientificName/rank/lineage | supports | Exact organism identity checked. Species4932/4896 and Actinophrys238771 are distinguished from reference strain559292; authority identity does not show taxon-wide organelle occurrence. |
| micro-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; ENA taxonomy exact taxId/scientificName/rank/lineage | supports | Exact organism identity checked. Species4932/4896 and Actinophrys238771 are distinguished from reference strain559292; authority identity does not show taxon-wide organelle occurrence. |
| micro-tax-238771 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/238771; ENA taxonomy exact taxId/scientificName/rank/lineage | supports | Exact organism identity checked. Species4932/4896 and Actinophrys238771 are distinguished from reference strain559292; authority identity does not show taxon-wide organelle occurrence. |
| micro-uniprot-P43583 | https://rest.uniprot.org/uniprotkb/P43583.json; UniProt entry status, name, gene, taxon and relevant processing features | supports | Current accession/gene/taxon checked. Reviewed S288C reference entries are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free ubiquitin as an entire precursor. |
| micro-matches-P43583 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P43583/?page_size=200; InterPro integrated entry matches for the exact protein; returned count, names and types | supports | Exact membership checked separately from grounding suitability. A domain or broad family match does not establish a specific structure component identity or localized functional isoform. |
| micro-uniprot-P43593 | https://rest.uniprot.org/uniprotkb/P43593.json; UniProt entry status, name, gene, taxon and relevant processing features | supports | Current accession/gene/taxon checked. Reviewed S288C reference entries are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free ubiquitin as an entire precursor. |
| micro-matches-P43593 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P43593/?page_size=200; InterPro integrated entry matches for the exact protein; returned count, names and types | supports | Exact membership checked separately from grounding suitability. A domain or broad family match does not establish a specific structure component identity or localized functional isoform. |
| micro-uniprot-P0CG63 | https://rest.uniprot.org/uniprotkb/P0CG63.json; UniProt entry status, name, gene, taxon and relevant processing features | supports | Current accession/gene/taxon checked. Reviewed S288C reference entries are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free ubiquitin as an entire precursor. |
| micro-matches-P0CG63 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0CG63/?page_size=200; InterPro integrated entry matches for the exact protein; returned count, names and types | supports | Exact membership checked separately from grounding suitability. A domain or broad family match does not establish a specific structure component identity or localized functional isoform. |
| micro-uniprot-Q12329 | https://rest.uniprot.org/uniprotkb/Q12329.json; UniProt entry status, name, gene, taxon and relevant processing features | supports | Current accession/gene/taxon checked. Reviewed S288C reference entries are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free ubiquitin as an entire precursor. |
| micro-matches-Q12329 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200; InterPro integrated entry matches for the exact protein; returned count, names and types | supports | Exact membership checked separately from grounding suitability. A domain or broad family match does not establish a specific structure component identity or localized functional isoform. |
| micro-uniprot-P53286 | https://rest.uniprot.org/uniprotkb/P53286.json; UniProt entry status, name, gene, taxon and relevant processing features | supports | Current accession/gene/taxon checked. Reviewed S288C reference entries are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free ubiquitin as an entire precursor. |
| micro-matches-P53286 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P53286/?page_size=200; InterPro integrated entry matches for the exact protein; returned count, names and types | supports | Exact membership checked separately from grounding suitability. A domain or broad family match does not establish a specific structure component identity or localized functional isoform. |
| micro-uniprot-P31539 | https://rest.uniprot.org/uniprotkb/P31539.json; UniProt entry status, name, gene, taxon and relevant processing features | supports | Current accession/gene/taxon checked. Reviewed S288C reference entries are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free ubiquitin as an entire precursor. |
| micro-matches-P31539 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200; InterPro integrated entry matches for the exact protein; returned count, names and types | supports | Exact membership checked separately from grounding suitability. A domain or broad family match does not establish a specific structure component identity or localized functional isoform. |
| micro-uniprot-B2NIF0 | https://rest.uniprot.org/uniprotkb/B2NIF0.json; UniProt entry status, name, gene, taxon and relevant processing features | supports | Current accession/gene/taxon checked. Reviewed S288C reference entries are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free ubiquitin as an entire precursor. |
| micro-matches-B2NIF0 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B2NIF0/?page_size=200; InterPro integrated entry matches for the exact protein; returned count, names and types | supports | Exact membership checked separately from grounding suitability. A domain or broad family match does not establish a specific structure component identity or localized functional isoform. |
| micro-uniprot-B2NIF1 | https://rest.uniprot.org/uniprotkb/B2NIF1.json; UniProt entry status, name, gene, taxon and relevant processing features | supports | Current accession/gene/taxon checked. Reviewed S288C reference entries are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free ubiquitin as an entire precursor. |
| micro-matches-B2NIF1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B2NIF1/?page_size=200; InterPro integrated entry matches for the exact protein; returned count, names and types | supports | Exact membership checked separately from grounding suitability. A domain or broad family match does not establish a specific structure component identity or localized functional isoform. |
| micro-reviewed-BLM10 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABLM10&amp;format=json&amp;size=500; UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page link | supports | Bounded reviewed reference-strain gene query confirms the single declared accession without a synonym split; not a global ortholog inventory. |
| micro-reviewed-UBP6 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AUBP6&amp;format=json&amp;size=500; UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page link | supports | Bounded reviewed reference-strain gene query confirms the single declared accession without a synonym split; not a global ortholog inventory. |
| micro-reviewed-UBI4 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AUBI4&amp;format=json&amp;size=500; UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page link | supports | Bounded reviewed reference-strain gene query confirms the single declared accession without a synonym split; not a global ortholog inventory. |
| micro-reviewed-HSP42 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP42&amp;format=json&amp;size=500; UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page link | supports | Bounded reviewed reference-strain gene query confirms the single declared accession without a synonym split; not a global ortholog inventory. |
| micro-reviewed-BTN2 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABTN2&amp;format=json&amp;size=500; UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page link | supports | Bounded reviewed reference-strain gene query confirms the single declared accession without a synonym split; not a global ortholog inventory. |
| micro-reviewed-HSP104 | https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&amp;format=json&amp;size=500; UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page link | supports | Bounded reviewed reference-strain gene query confirms the single declared accession without a synonym split; not a global ortholog inventory. |
| micro-entry-IPR035309 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035309/; Current entry accession, name, type, integrated signatures and scope | supports | Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp families and lectin domains are not promoted to unsupported exact component grounding. InterPro descriptions are authority context, not independent localization experiments. |
| micro-entry-IPR044635 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044635/; Current entry accession, name, type, integrated signatures and scope | supports | Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp families and lectin domains are not promoted to unsupported exact component grounding. InterPro descriptions are authority context, not independent localization experiments. |
| micro-entry-IPR050158 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050158/; Current entry accession, name, type, integrated signatures and scope | supports | Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp families and lectin domains are not promoted to unsupported exact component grounding. InterPro descriptions are authority context, not independent localization experiments. |
| micro-entry-IPR031107 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/; Current entry accession, name, type, integrated signatures and scope | supports | Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp families and lectin domains are not promoted to unsupported exact component grounding. InterPro descriptions are authority context, not independent localization experiments. |
| micro-entry-IPR001270 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/; Current entry accession, name, type, integrated signatures and scope | supports | Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp families and lectin domains are not promoted to unsupported exact component grounding. InterPro descriptions are authority context, not independent localization experiments. |
| micro-entry-IPR050130 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/; Current entry accession, name, type, integrated signatures and scope | supports | Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp families and lectin domains are not promoted to unsupported exact component grounding. InterPro descriptions are authority context, not independent localization experiments. |
| micro-entry-IPR000757 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000757/; Current entry accession, name, type, integrated signatures and scope | supports | Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp families and lectin domains are not promoted to unsupported exact component grounding. InterPro descriptions are authority context, not independent localization experiments. |
| micro-entry-IPR013320 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013320/; Current entry accession, name, type, integrated signatures and scope | supports | Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp families and lectin domains are not promoted to unsupported exact component grounding. InterPro descriptions are authority context, not independent localization experiments. |
| micro-entry-IPR062150 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062150/; Current metadata after initial429; type=domain, BTN2-like N-terminal | supports | Successful retry confirms an N-terminal domain including BTN2-related proteins; the record appropriately keeps BTN2 label-only instead of treating this as an exact family. |
| micro-deleted-IPR050546 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050546/; HTTP410 deleted-entry metadata; deletion_date2026-05-13 | context_only | Current deleted status confirms why the historical candidate is not usable grounding; the initial429 did not itself establish deletion. |
| micro-pac-dataset | https://api.datacite.org/dois/10.17632/z3hvg9wtvg.2; DataCite metadata for exact version DOI10.17632/z3hvg9wtvg.2 | supports | Margarita Cabrera, March21,2023 issuance and CC BY4.0 metadata verified. No raw files, content manifest or reanalysis inspected; this supports dataset provenance only. |
| micro-psg-image | https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/jcb1810737f02.jpg; Direct pixels of Laporte2008 Figure2; source caption in laporte2008; package media MD5a1a61298bd0533aa42ad5121b7f29e34 | supports | Image shows paired proteasome reporter signals and merged foci plus time-course categories; scale2um. It supports depicted localization/colocalization only, not universal assembly state. It remains a link-only record image. |
| micro-pac-image | data/images/inclusion/protein_aggregate_center/pmc10342647_ijms_24_11202_f002.jpg; Direct original pixels inspected; Figure2 source caption and PMC package MD5d43e6b98317eb43129ceb3af1a7d9b2b matched | supports | BY4741 Btn2/Hsp42/Hsp104 separate GFP rows show25C and37C15/30/60/120min observations, percentages and5um scale. Separate panels are not three-way colocalization or proof of necessity. |
| micro-package-PMC2396804 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.json; PMC open-data package identity/media checksum/license metadata, crosschecked with source JATS permissions | supports | Figure bytes match package MD5; Laporte2008 is CC BY-NC-SA3.0, represented as OTHER with license text, and Boronat2023 is CC BY4.0. Package metadata and pixel inspection are distinct checks. |
| micro-package-PMC10342647 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.json; PMC open-data package identity/media checksum/license metadata, crosschecked with source JATS permissions | supports | Figure bytes match package MD5; Laporte2008 is CC BY-NC-SA3.0, represented as OTHER with license text, and Boronat2023 is CC BY4.0. Package metadata and pixel inspection are distinct checks. |
| micro-adapter-catalogue | https://imodulondb.org/api/datasets; Complete returned iModulonDB dataset catalogue;20 organism rows,28 organism-dataset pairs,22 distinct literal dataset-name strings | supports | No listed Saccharomyces cerevisiae, Schizosaccharomyces pombe or Actinophrys sol organism key. Named proteins/stress/perturbation claims trigger applicability assessment, but no covered target organism permits downstream gene/module matching here. Catalogue absence is not negative biological evidence. |
| micro-historical-adapter-runner | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Retained actual00:49Z adapter invocation; command, error and status fields | supports | Earlier actual runner command returned1 because OS denied pyvenv.cfg access. This historical availability receipt is not a fresh invocation or a successful adapter run; current catalogue fallback was fetched independently. |
| septin-native-review-policy | .claude/skills/review-yaml-record/SKILL.md; Structured Source Cross-Checks; native record-review process | supports | Named genes, accessions or pathways trigger applicability assessment. Lack of an expression claim is not an exemption; unmatched organisms permit bounded downstream non-applicability. Native review-only mutation boundary and current input capture apply. |
| septin-native-curation-policy | docs/CURATION.md; Components; essentiality; evidence scope | supports | Component grounding is class-level, protein examples are taxon-specific, and essentiality concerns structure formation. Identity, localization, metabolic function and formation dependency require distinct support. |
| septin-record-anammoxosome | data/structures/membrane_organelle/anammoxosome.yaml; Entire current record at e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4 | supports | Full maintained record, including history, identity, components, examples, taxonomic scope, functions, evidence, graph and TODOs; no tracked image is present. |
| septin-original-anammoxosome | reviews/structured/20261021T104744Z-anammoxosome-audit/review.yaml; Entire original YAML and deterministic Markdown; findings/actions retained | supports | Original review at 20261021T104744Z-anammoxosome-audit; historical verdict needs_curation. This successor reassesses current content without overwriting the original. |
| septin-record-anammoxosome_membrane | data/structures/membrane_organelle/anammoxosome_membrane.yaml; Entire current record at e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4 | supports | Full maintained record, including history, identity, components, examples, taxonomic scope, functions, evidence, graph and TODOs; no tracked image is present. |
| septin-original-anammoxosome_membrane | reviews/structured/20261021T104745Z-anammoxosome-membrane-audit/review.yaml; Entire original YAML and deterministic Markdown; findings/actions retained | supports | Original review at 20261021T104745Z-anammoxosome-membrane-audit; historical verdict needs_curation. This successor reassesses current content without overwriting the original. |
| septin-record-apicoplast | data/structures/membrane_organelle/apicoplast.yaml; Entire current record at e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4 | supports | Full maintained record, including history, identity, components, examples, taxonomic scope, functions, evidence, graph and TODOs; no tracked image is present. |
| septin-original-apicoplast | reviews/structured/20261021T104747Z-apicoplast-audit/review.yaml; Entire original YAML and deterministic Markdown; findings/actions retained | supports | Original review at 20261021T104747Z-apicoplast-audit; historical verdict needs_curation. This successor reassesses current content without overwriting the original. |
| septin-context-apicoplast-membrane | data/structures/membrane_organelle/apicoplast_membrane.yaml; Frozen neighbor: identity, parthood and membrane/whole-organelle boundary only | supports | GO:0160211 is the membrane constituent, part of GO:0020011; the whole-organelle record and membrane record remain distinct. This is not a full adjudication or resolution of the neighbor protein examples. |
| septin-root20-sources-anammoxosome-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043231,GO:0044222; QuickGO exact requested identifiers: names, definitions, obsolete status, aspect and returned relationships | supports | Exact current GO terms inspected; broader parent identity is kept distinct from the structure or its membrane constituent. |
| septin-root20-sources-NCBITaxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Taxon identity/lineage is verified. Corrected current Kuenenia spelling and historical synonym do not imply a different organism; native name conventions are not silently rewritten. |
| septin-root20-sources-NCBITaxon-203682 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/203682; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Taxon identity/lineage is verified. Corrected current Kuenenia spelling and historical synonym do not imply a different organism; native name conventions are not silently rewritten. |
| septin-root20-sources-NCBITaxon-174633 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/174633; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Taxon identity/lineage is verified. Corrected current Kuenenia spelling and historical synonym do not imply a different organism; native name conventions are not silently rewritten. |
| septin-root20-sources-doi-10.1111_1574-6976.12014 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/1574-6976.12014; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID23210799: Kartal B, de Almeida NM, Maalcke WJ, Op den Camp HJ, Jetten MS, Keltjens JT. (2013), How to make a living from anaerobic ammonium oxidation.. Full publication body is not attested by this metadata/abstract response. |
| septin-root20-sources-doi-10.1128_JB.00186-15 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/JB.00186-15; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID25962914: de Almeida NM, Neumann S, Mesman RJ, Ferousi C, Keltjens JT, Jetten MS, Kartal B, van Niftrik L. (2015), Immunogold Localization of Key Metabolic Enzymes in the Anammoxosome and on the Tubule-Like Structures of Kuenenia stuttgartiensis.. Full publication body is not attested by this metadata/abstract response. |
| septin-root20-sources-PMID-15098544 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15098544%20AND%20SRC%3AMED; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID15098544: van Niftrik LA, Fuerst JA, Sinninghe Damsté JS, Kuenen JG, Jetten MS, Strous M. (2004), The anammoxosome: an intracytoplasmic compartment in anammox bacteria.. Full publication body is not attested by this metadata/abstract response. |
| septin-root20-sources-PMID-25962914 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A25962914%20AND%20SRC%3AMED; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID25962914: de Almeida NM, Neumann S, Mesman RJ, Ferousi C, Keltjens JT, Jetten MS, Kartal B, van Niftrik L. (2015), Immunogold Localization of Key Metabolic Enzymes in the Anammoxosome and on the Tubule-Like Structures of Kuenenia stuttgartiensis.. Full publication body is not attested by this metadata/abstract response. |
| septin-root20-sources-PMID-12384695 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:12384695%20AND%20SRC:MED; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID12384695: Sinninghe Damsté JS, Strous M, Rijpstra WI, Hopmans EC, Geenevasen JA, van Duin AC, van Niftrik LA, Jetten MS. (2002), Linearly concatenated cyclobutane lipids form a dense bacterial membrane.. Full publication body is not attested by this metadata/abstract response. |
| septin-root20-sources-legacy-PMC4524196 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4524196/; de Almeida et al. 2015: Introduction equations 1–4, Fig.1 caption, Results localization sections and Discussion; body text inspected, no figure pixels/raw image quantification | supports | The paper distinguishes HZS, HDH/kustc0694, HOX/kustc1061 and an HAO-like pair of unknown function. Hydrazine oxidation supplies electrons to reductive steps. All five localized complexes are soluble inside the anammoxosome; membrane-carrier localization and organelle-assembly requirements were not measured. |
| septin-root20-sources-UniProtKB-A0A2C9CHN2 | https://rest.uniprot.org/uniprotkb/A0A2C9CHN2.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | A0A2C9CHN2: UniProtKB unreviewed (TrEMBL); taxon 174633; native gene/ORF values hzsA_1, hzsA_2, KSMBR1_2713, KSMBR1_3603. Identity/status metadata does not alone establish organelle membership. |
| septin-root20-sources-UniProtKB-A0A2C9CH14 | https://rest.uniprot.org/uniprotkb/A0A2C9CH14.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | A0A2C9CH14: UniProtKB unreviewed (TrEMBL); taxon 174633; native gene/ORF values hzsB_1, hzsB_2, hzsB_3, KSMBR1_2704, KSMBR1_2712, KSMBR1_3602. Identity/status metadata does not alone establish organelle membership. |
| septin-root20-sources-UniProtKB-A0A2C9CHM2 | https://rest.uniprot.org/uniprotkb/A0A2C9CHM2.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | A0A2C9CHM2: UniProtKB unreviewed (TrEMBL); taxon 174633; native gene/ORF values hzsC_3, hzsC_1, hzsC_2, KSMBR1_2703, KSMBR1_2711, KSMBR1_3601. Identity/status metadata does not alone establish organelle membership. |
| septin-root20-sources-UniProtKB-Q1PX48 | https://rest.uniprot.org/uniprotkb/Q1PX48.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Q1PX48: UniProtKB reviewed (Swiss-Prot); taxon 174633; native gene/ORF values hao, hao_3, hox, H3C64_04740, KsCSTR_43280, KSMBR1_2670, kustc1061. Identity/status metadata does not alone establish organelle membership. Reviewed functional annotation identifies hydroxylamine-to-NO activity and qualifies slower hydrazine oxidation as probably nonphysiological; hao/hox/kustc1061 is distinct from HDH. |
| septin-root20-sources-UniProtKB-Q1PYC5 | https://rest.uniprot.org/uniprotkb/Q1PYC5.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Q1PYC5: UniProtKB unreviewed (TrEMBL); taxon 174633; native gene/ORF values hdh, KSMBR1_1220. Identity/status metadata does not alone establish organelle membership. |
| septin-root20-sources-query-hzsA_1-174633 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AhzsA_1%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 0 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-root20-sources-query-hzsB_1-174633 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AhzsB_1%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 0 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-root20-sources-query-hzsC_3-174633 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AhzsC_3%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 0 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-root20-sources-query-hao-174633 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3Ahao%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 1 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-root20-sources-query-hdh-174633 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3Ahdh%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 0 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-root20-sources-anammox-membrane-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016020,GO:0044222; QuickGO exact requested identifiers: names, definitions, obsolete status, aspect and returned relationships | supports | Exact current GO terms inspected; broader parent identity is kept distinct from the structure or its membrane constituent. |
| septin-root20-sources-ols-exact-anammoxosome-membrane | https://www.ebi.ac.uk/ols4/api/search?ontology=go&amp;exact=true&amp;queryFields=label,synonym&amp;rows=100&amp;q=anammoxosome%20membrane; Complete exact GO name lookup response | supports | The bounded exact anammoxosome membrane name query returned no exact GO term; GO membrane remains a broader parent, not identity. No claim of exhaustive ontology absence. |
| septin-apicoplast-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009536,GO:0020011,GO:0160211; QuickGO exact requested identifiers: names, definitions, obsolete status, aspect and returned relationships | supports | Exact current GO terms inspected; broader parent identity is kept distinct from the structure or its membrane constituent. |
| septin-apicoplast-agent-tax-5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Taxon identity/lineage is verified. Corrected current Kuenenia spelling and historical synonym do not imply a different organism; native name conventions are not silently rewritten. |
| septin-apicoplast-agent-tax-5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Taxon identity/lineage is verified. Corrected current Kuenenia spelling and historical synonym do not imply a different organism; native name conventions are not silently rewritten. |
| septin-apicoplast-agent-tax-5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Taxon identity/lineage is verified. Corrected current Kuenenia spelling and historical synonym do not imply a different organism; native name conventions are not silently rewritten. |
| septin-apicoplast-agent-tax-508771 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Taxon identity/lineage is verified. Corrected current Kuenenia spelling and historical synonym do not imply a different organism; native name conventions are not silently rewritten. |
| septin-apicoplast-agent-tax-36329 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/36329; ENA taxonomy exact tax-id response: current name, aliases, rank and lineage | supports | Taxon identity/lineage is verified. Corrected current Kuenenia spelling and historical synonym do not imply a different organism; native name conventions are not silently rewritten. |
| septin-apicoplast-agent-S8GBF3 | https://rest.uniprot.org/uniprotkb/S8GBF3.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | S8GBF3: UniProtKB unreviewed (TrEMBL); taxon 508771; native gene/ORF values TIC20, TGME49_255370. Identity/status metadata does not alone establish organelle membership. |
| septin-apicoplast-agent-O97275 | https://rest.uniprot.org/uniprotkb/O97275.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | O97275: UniProtKB unreviewed (TrEMBL); taxon 36329; native gene/ORF values PF3D7_0314300. Identity/status metadata does not alone establish organelle membership. |
| septin-apicoplast-agent-B9PY98 | https://rest.uniprot.org/uniprotkb/B9PY98.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | B9PY98: UniProtKB unreviewed (TrEMBL); taxon 5811; native gene/ORF values no native gene-name field. Identity/status metadata does not alone establish organelle membership. EMBL cross-reference is FJ976521/ACU32856.1, independently deposited as Der1ER1. |
| septin-apicoplast-agent-Q8I295 | https://rest.uniprot.org/uniprotkb/Q8I295.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Q8I295: UniProtKB reviewed (Swiss-Prot); taxon 36329; native gene/ORF values LytB, IspH, PF3D7_0104400. Identity/status metadata does not alone establish organelle membership. |
| septin-apicoplast-agent-Q965D5 | https://rest.uniprot.org/uniprotkb/Q965D5.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Q965D5: UniProtKB unreviewed (TrEMBL); taxon 5833; native gene/ORF values fabI. Identity/status metadata does not alone establish organelle membership. |
| septin-apicoplast-agent-Q965D7 | https://rest.uniprot.org/uniprotkb/Q965D7.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Q965D7: UniProtKB unreviewed (TrEMBL); taxon 5833; native gene/ORF values fabZ. Identity/status metadata does not alone establish organelle membership. |
| septin-apicoplast-agent-C9WWW6 | https://rest.uniprot.org/uniprotkb/C9WWW6.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | C9WWW6: UniProtKB unreviewed (TrEMBL); taxon 5811; native gene/ORF values no native gene-name field. Identity/status metadata does not alone establish organelle membership. EMBL cross-reference is FJ976520/ACU32855.1, independently deposited as apicoplast Der1; automated ER wording is not accepted as a replacement for primary localization. |
| septin-apicoplast-agent-query-TIC20-508771 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3ATIC20%29%20AND%20%28organism_id%3A508771%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 1 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-apicoplast-agent-query-ispH-36329 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AispH%29%20AND%20%28organism_id%3A36329%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 1 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-apicoplast-agent-query-fabI | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AfabI%29%20AND%20%28organism_id%3A5833%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 3 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-apicoplast-agent-query-fabZ | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AfabZ%29%20AND%20%28organism_id%3A5833%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 1 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-apicoplast-agent-matches-S8GBF3 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/S8GBF3/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Native example matches: IPR005691:family. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-matches-O97275 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O97275/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Native example matches: IPR007599:family, IPR035952:homologous_superfamily. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-matches-B9PY98 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B9PY98/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Native example matches: IPR007599:family, IPR035952:homologous_superfamily. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-matches-Q8I295 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8I295/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Native example matches: IPR003451:family. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-matches-Q965D5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q965D5/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Native example matches: IPR002347:family, IPR014358:family, IPR036291:homologous_superfamily. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-matches-Q965D7 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q965D7/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Native example matches: IPR010084:family, IPR013114:family, IPR029069:homologous_superfamily. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-apicoplast-agent-IPR005691 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005691/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR005691 is type family, name {'name': 'Chloroplast protein import component Tic20', 'short': 'Tic20'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-apicoplast-agent-IPR007599 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007599/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR007599 is type family, name {'name': 'Derlin', 'short': 'DER1'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-apicoplast-agent-IPR036291 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR036291/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR036291 is type homologous_superfamily, name {'name': 'NAD(P)-binding domain superfamily', 'short': 'NAD(P)-bd_dom_sf'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-apicoplast-agent-IPR010084 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010084/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR010084 is type family, name {'name': 'Beta-hydroxyacyl-(acyl-carrier-protein) dehydratase FabZ', 'short': 'FabZ'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-apicoplast-agent-IPR013114 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013114/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR013114 is type family, name {'name': 'Beta-hydroxydecanoyl thiol ester dehydrase, FabA/FabZ', 'short': 'FabA_FabZ'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-apicoplast-agent-IPR029069 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029069/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR029069 is type homologous_superfamily, name {'name': 'HotDog domain superfamily', 'short': 'HotDog_dom_sf'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-apicoplast-agent-doi-10.1073_pnas.95.21.12352 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.95.21.12352; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID9770490: Waller RF, Keeling PJ, Donald RG, Striepen B, Handman E, Lang-Unnasch N, Cowman AF, Besra GS, Roos DS, McFadden GI. (1998), Nuclear-encoded proteins target to the plastid in Toxoplasma gondii and Plasmodium falciparum.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1098_rstb.2009.0273 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1098/rstb.2009.0273; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID20124342: Lim L, McFadden GI. (2010), The evolution, metabolism and functions of the apicoplast.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1073_pnas.0803862105 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0803862105; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID18757752: van Dooren GG, Tomova C, Agrawal S, Humbel BM, Striepen B. (2008), Toxoplasma gondii Tic20 is essential for apicoplast protein import.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1371_journal.ppat.1003426 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371/journal.ppat.1003426; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID23785288: Agrawal S, Chung DW, Ponts N, van Dooren GG, Prudhomme J, Brooks CF, Rodrigues EM, Tan JC, Ferdig MT, Striepen B, Le Roch KG. (2013), An apicoplast localized ubiquitylation system is required for the import of nuclear-encoded plastid proteins.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1186_1475-2875-12-25 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1186/1475-2875-12-25; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID23331966: Lemgruber L, Kudryashev M, Dekiwadia C, Riglar DT, Baum J, Stahlberg H, Ralph SA, Frischknecht F. (2013), Cryo-electron tomography reveals four-membrane architecture of the Plasmodium apicoplast.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1146_annurev-micro-092412-155741 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev-micro-092412-155741; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID23808340: van Dooren GG, Striepen B. (2013), The algal past and parasite present of the apicoplast.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1371_journal.pbio.1001138 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371/journal.pbio.1001138; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID21912516: Yeh E, DeRisi JL. (2011), Chemical rescue of malaria parasites lacking an apicoplast defines organelle function in blood-stage Plasmodium falciparum.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1016_j.ijpara.2016.08.005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.ijpara.2016.08.005; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID27773518: McFadden GI, Yeh E. (2017), The apicoplast: now you see it, now you don't.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1074_jbc.M109.044024 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1074/jbc.M109.044024; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID19808683: Agrawal S, van Dooren GG, Beatty WL, Striepen B. (2009), Genetic evidence that an endosymbiont-derived endoplasmic reticulum-associated protein degradation (ERAD) system functions in import of apicoplast proteins.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-doi-10.1128_EC.00061-09 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI:10.1128/EC.00061-09; Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID and abstract only | supports | PMID19502580: Kalanon M, Tonkin CJ, McFadden GI. (2009), Characterization of two putative protein translocation components in the apicoplast of Plasmodium falciparum.. Full publication body is not attested by this metadata/abstract response. |
| septin-apicoplast-agent-jats-PMC3681736 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3681736.1/PMC3681736.1.xml; Agrawal et al. 2013 JATS: Abstract, apicoplast enzyme localization/import experiments, Discussion including unresolved endogenous modifier paragraphs | supports | Supports an apicoplast ubiquitylation-system import role and tested enzyme activity, while explicitly leaving endogenous ubiquitin versus ubiquitin-like modifier unresolved. Recombinant human ubiquitin is the tested in-vitro substrate. |
| septin-apicoplast-agent-jats-PMC3662607 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3662607.1/PMC3662607.1.xml; Lemgruber et al. 2013 JATS: Abstract, Results four-membrane reconstructions, figure captions and Conclusions; no new pixel audit | supports | Cryo-electron tomography of P. falciparum merozoites resolves four envelope membranes; local apposition explains slices apparently showing three. Supports the scoped membrane-boundary claim, not protein identities. |
| septin-apicoplast-agent-jats-PMC3166167 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3166167.1/PMC3166167.1.xml; Yeh and DeRisi 2011 JATS: Abstract and Results on IPP rescue, organelle-loss assays and blood-stage scope | supports | IPP supplementation sustains apicoplast-minus asexual blood-stage P. falciparum. Retain this stage/species scope; it does not establish identical metabolic essentiality in all apicomplexans or life stages. |
| septin-apicoplast-agent-jats-PMC2817234 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2817234.1/PMC2817234.1.xml; Lim and McFadden 2010 secondary review JATS: origin/envelope, targeting and metabolic pathway sections | supports | Secondary synthesis supports signal/transit targeting and distinct fatty-acid, isoprenoid, heme and iron-sulfur pathways with stage-dependent requirements. It is not a new primary localization or assembly experiment. |
| septin-apicoplast-agent-jats-PMC5406208 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5406208.1/PMC5406208.1.xml; McFadden and Yeh 2017 secondary review JATS: apicoplast loss and stage-specific metabolic function sections | supports | Secondary context supports variable apicomplexan presence including Cryptosporidium loss and life-stage distinctions. No universal family or life-stage metabolic requirement is inferred. |
| septin-apicoplast-agent-ena-FJ976521 | https://www.ebi.ac.uk/ena/browser/api/embl/FJ976521?download=false; ENA native flatfile DE/CDS product/protein_id and translation | supports | FJ976521 explicitly names Der1ER1 and ACU32856.1; exact accession bridge to unreviewed B9PY98, the ER paralog. |
| septin-apicoplast-agent-ena-FJ976520 | https://www.ebi.ac.uk/ena/browser/api/embl/FJ976520?download=false; ENA native flatfile DE/CDS product/note/protein_id and translation | supports | FJ976520 explicitly names apicoplast Der1/Der1Ap and ACU32855.1; exact accession bridge to unreviewed C9WWW6. Automated generic ER location in that UniProt entry is not substituted for the primary paralog evidence. |
| septin-apicoplast-agent-ena-CAB38986 | https://www.ebi.ac.uk/ena/browser/api/embl/CAB38986.4?download=false; Native sequence/locus metadata; exact gene and old-locus bridge only | supports | Supports current O97275/CAB38986.4/PF3D7_0314300 and older PFC0590c identity bridge; the old identifier string and new locus name are not treated as identical literal strings. |
| septin-apicoplast-agent-gene-814456 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&amp;id=814456&amp;retmode=json; Native sequence/locus metadata; exact gene and old-locus bridge only | supports | Supports current O97275/CAB38986.4/PF3D7_0314300 and older PFC0590c identity bridge; the old identifier string and new locus name are not treated as identical literal strings. |
| septin-apicoplast-agent-kalanon2009-pdf | https://fad.webmate.me/McFadden_Lab/Mcfadden_Papers/2009/Kalanon_Euk_Cell_2009.pdf; Author-hosted Kalanon et al. 2009 PDF: Methods antibody peptide printed p.1148; PfsDer1 paralog Results/Table1/Fig.4 caption printed pp.1149–1152 | supports | Separates PfsDer1-1 from PfsDer1-2/PFC0590c. Published anti-Der1-2 peptide IKDCVSKYTSRSSTNN occurs at residues303–318 of current O97275. Full-length Der1-1 localization experiments are not transferred to Der1-2. |
| septin-current-adapter-catalogue | https://imodulondb.org/api/datasets; Complete official /api/datasets response, all 20 organism rows and 28 organism/dataset pairs (22 distinct literal dataset names) | supports | No Kuenenia, Brocadiales/Planctomycetota, Plasmodium, Toxoplasma or other apicomplexan dataset matches these three targets. Broad Bacteria scope does not justify substituting unrelated covered species. No gene/module query is applicable to an unmatched organism. |
| septin-apicoplast-current-Q8IJH7 | https://rest.uniprot.org/uniprotkb/Q8IJH7.json; Native accession, entry status, organism/taxon, gene/ORF names, protein name, sequence and cross-reference fields | supports | Q8IJH7: UniProtKB unreviewed (TrEMBL); taxon 36329; native gene/ORF values PF3D7_1022800. Identity/status metadata does not alone establish organelle membership. Added current example is the IspG-family enzyme at PF3D7_1022800; this is an ORF/locus field, not an asserted literal native ispG gene-name field. Its annotation is computational and is not new experimental localization. |
| septin-apicoplast-current-query-ispG | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AispG%20OR%20gene_exact%3APF3D7_1022800%29%20AND%20%28organism_id%3A36329%29; Native UniProt exact query response; first page size500; result metadata only | supports | Returned 1 entries for the exact query. Zero reviewed exact-symbol hits do not establish absence of homologs or structural membership. |
| septin-apicoplast-current-matches-Q8IJH7 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8IJH7/?page_size=200; Complete example-specific native InterPro matches response; accession/type/match positions and pagination inspected | supports | Native example matches: IPR004588:family, IPR011005:homologous_superfamily, IPR017178:family, IPR045854:homologous_superfamily, IPR058578:domain, IPR058579:domain. Protein family, domain and homologous-superfamily types remain distinct; generated biological descriptions are not used. |
| septin-current-IPR035952 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035952/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR035952 is type homologous_superfamily, name {'name': 'Rhomboid-like superfamily', 'short': 'Rhomboid-like_sf'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-current-IPR003451 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003451/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR003451 is type family, name {'name': '4-hydroxy-3-methylbut-2-enyl diphosphate reductase', 'short': 'LytB/IspH'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-current-IPR002347 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002347/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR002347 is type family, name {'name': 'Short-chain dehydrogenase/reductase SDR', 'short': 'SDR_fam'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-current-IPR014358 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014358/; Native InterPro metadata accession/name/type/hierarchy/member signatures only | supports | IPR014358 is type family, name {'name': 'Enoyl-[acyl-carrier-protein] reductase (NADH)', 'short': 'Enoyl-ACP_Rdtase_NADH'}. Only metadata/classification is used; generic domain/superfamily matches do not identify a heterogeneous whole import machine. Generated description text is excluded. |
| septin-waller1998-author-pdf | https://fad.webmate.me/McFadden_Lab/Mcfadden_Papers/1998/Waller_et_al_PNAS.pdf; Author-hosted published Waller et al. 1998 PDF pp.12352–12357: Abstract, targeting Results, signal/transit-sequence and ACP-GFP captions; extracted text, not image pixels | supports | Supports nuclear-encoded plastid protein targeting, N-terminal signal/transit architecture and sufficiency of the tested ACP leader for apicoplast targeting. General precursor targeting is separate from proof that Tic20 itself is a pore. |
| septin-agrawal2011-thesis | https://openscholar.uga.edu/record/21126/files/agrawal_swati_201105_phd.pdf; University of Georgia author dissertation: Chapter3 Methods printed p.46/PDF59 and Table3.1 p.81/PDF94; Appendix2 (Tic20 study) pp.176–188, especially p.188/PDF201 | supports | Author-reproduced primary studies independently distinguish Der1ER1 FJ976521 from Der1Ap FJ976520. The Tic20 appendix reports inner-membrane import dependency and explicitly discusses accessory/regulatory alternatives to direct channel action. This is an institutional thesis copy, not a successful new PMC full-body fetch. |
| septin-current-tic20-indexed-primary | https://pmc.ncbi.nlm.nih.gov/articles/PMC2533231/; Indexed primary Results/Discussion passage returned by bounded web retrieval; not full live PMC body | supports | Primary passage explicitly discusses import impairment with residual activity after Tic20 falls below detection and accessory/regulatory alternatives; independently corroborated in author dissertation Appendix2. |
| septin-current-tic20-indexed-primary-retrieval | https://pmc.ncbi.nlm.nih.gov/articles/PMC2533231/; Bounded source-location search; returned first response only | supports | Search was used to locate exact primary or author copies. Unrelated returned hits were not used as evidence; no absence conclusion is drawn. |
| septin-current-kartal-indexed-review | https://academic.oup.com/femsre/article/37/3/428/585200; Indexed secondary review sections on membranes, catabolism and proposed quinone/electron-transfer model; not a successful PDF download | supports | Kartal2013 is a secondary synthesis. Indexed passage states central quinone/electron-transfer proposals and unresolved exact systems; direct native PDF requests timed out. |
| septin-current-kartal-indexed-review-retrieval | https://academic.oup.com/femsre/article/37/3/428/585200; Bounded source-location search; returned first response only | supports | Search was used to locate exact primary or author copies. Unrelated returned hits were not used as evidence; no absence conclusion is drawn. |
| septin-historical-adapter-runner-unavailable | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Actual historical attempt 2026-11-03T00:49:00.848907Z–00:49:00.863225Z; exit1 PermissionError reading runner pyvenv.cfg | supports | Historical runner availability failure only; no fresh runner invocation is claimed. Current official catalogue/source fallback is separate. |
| septin-original-validation-anammoxosome | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/adversary-septin/original-checks.json; Native validate; render --content; frozen revision git show and SHA256 comparison | supports | Original YAML validates and original Markdown is byte-identical to native render. Frozen target SHA matches the original source revision. Current target is stale and reassessed. |
| septin-native-anammoxosome-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome-uniprot-verify-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome.yaml --verify; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4. Causal check has two COVERED nodes and one NO_GENE_SYMBOLS carrier node; neither check establishes physiological reaction, carrier localization or organelle formation requirement. |
| septin-native-anammoxosome-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome-uniprot-causal-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome.yaml --causal-graphs; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome-uniprot-causal.log SHA256 52e5fdd545e1b6d279558f3545e9afa178d74496cb2f5b08a165e560f97b3bc7 | supports | Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4. Causal check has two COVERED nodes and one NO_GENE_SYMBOLS carrier node; neither check establishes physiological reaction, carrier localization or organelle formation requirement. |
| septin-original-validation-anammoxosome_membrane | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/adversary-septin/original-checks.json; Native validate; render --content; frozen revision git show and SHA256 comparison | supports | Original YAML validates and original Markdown is byte-identical to native render. Frozen target SHA matches the original source revision. Current target is byte-unchanged and reassessed. |
| septin-native-anammoxosome_membrane-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome_membrane-uniprot-verify-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome_membrane.yaml --verify; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome_membrane-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4. Protein inventory and typed GENE_OR_PROTEIN graph-node inventory are empty; success does not validate narrative pathway claims. |
| septin-native-anammoxosome_membrane-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome_membrane-uniprot-causal-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome_membrane.yaml --causal-graphs; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome_membrane-uniprot-causal.log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5 | supports | Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4. Protein inventory and typed GENE_OR_PROTEIN graph-node inventory are empty; success does not validate narrative pathway claims. |
| septin-original-validation-apicoplast | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/adversary-septin/original-checks.json; Native validate; render --content; frozen revision git show and SHA256 comparison | supports | Original YAML validates and original Markdown is byte-identical to native render. Frozen target SHA matches the original source revision. Current target is stale and reassessed. |
| septin-native-apicoplast-verify | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/apicoplast-uniprot-verify-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicoplast.yaml --verify; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/apicoplast-uniprot-verify.log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289 | supports | Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4. All three typed protein nodes are now symbol-covered, including added ispG identity. Identifier/coverage success does not validate Der1 cellular-paralog choice or Tic20/ubiquitin mechanistic claims. |
| septin-native-apicoplast-causal | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/apicoplast-uniprot-causal-receipt.json; .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicoplast.yaml --causal-graphs; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/apicoplast-uniprot-causal.log SHA256 67050afcbbb6c42ff95f9912fecf9cd6ae035749b2c2bc8ccb6540289df936da | supports | Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4. All three typed protein nodes are now symbol-covered, including added ispG identity. Identifier/coverage success does not validate Der1 cellular-paralog choice or Tic20/ubiquitin mechanistic claims. |
| check-qc | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/qc.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history, generated products and corpus gates passed. |
| check-labels | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/labels.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER pairs remain unverified by an authority adapter. |
| check-trait-links | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/trait-links.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Native TraitMech link check passed. |
| check-vendored | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/vendored.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Pinned governed files match; native vendored check passed. |
| check-curies | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/curies.log; Actual command stdout/stderr; receipt contains exact head/base and start/finish | supports | Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED. Existing #2514 tracks batching/reporting. Supplemental bounded requests verified the 909 PMIDs separately; skipped identifiers are not claimed resolved. |
| focused | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/focused-results.json; All twenty actual target schema/strict command outputs | supports | Ten schema and ten strict commands returned exit zero. |
| supplemental-pmid | /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/pmid-chunks-receipt.json; Complete native-report PMID set checked with unchanged resolver in batches of at most fifty | supports | 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers remain unverified. |
| historical-adapter-runner-availability | /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json; Historical runner invocation receipt, cross-checked against exact stdout/stderr hashes; reread during PR2357 synthesis | context_only | Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS PermissionError reading the configured runner pyvenv.cfg. This is a retained historical availability observation, not a fresh attempt or a scientific validation failure. Native policy permits inspected source-catalogue fallback. |

## Limits And Additional Notes

- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: The2003 bacterial identification is assessed at primary abstract scope; the original experimental strain/accession and figure pixels were not independently verified. The2020 selected primary body and2024 selected secondary body preserve rather than settle the conflict.
- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: Docampo2005 access was limited to publisher abstract and key points. Docampo2024 is secondary synthesis; selected relevant sections were read, not a comprehensive proteomic-table or figure audit.
- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: Bougdour2013 and Masatani2013 are used at primary abstract scope. Mercier2005 and2015 are secondary abstract context; the2005 publisher body request returned403. No full-body support is claimed for those sources.
- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: Gold2015 selected primary body and Table1 were inspected, but figure pixels and supplements were not independently audited. Experimental GT1/RH/other strains, ME49 reference identity and Xenopus assays remain distinct. PMC7202600 is used solely for exact ME49 GRA17/GRA23 identity rows.
- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: Q8VPZ0 is a189-aa D44 fragment with homology-derived sodium-pump/location annotations, distinct from C58 Atu_1174 and the unbridged2003 assay. The maintained protein example explicitly says identity only; it does not prove accession-specific acidocalcisome membership or proton selectivity.
- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: Exact InterPro GRA1/GRA17/GRA23 attempts returned204 plus curl92 malformed-header failures and no readable result; these are inconclusive, not zero-hit absence evidence. Verified GRA2/GRA6 family entries do not ground a heterogeneous cargo cohort.
- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: The shared adapter runner failure is a reread historical00:49Z receipt, not a fresh execution. Current native source catalogue was fetched independently. No covered Agrobacterium or Toxoplasma dataset exists in that response; no unrelated strain modules or generated module prose support localization.
- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: Sparse lumen and dense-granule membrane records do not require invented molecular inventories. Collective bilayer necessity is distinct from individual lipid/protein assembly necessity. All four targets remain PROPOSED.
- Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent subreview: No repository, original bundle, record or GitHub mutation was made by this independent reviewer. Root owns global gates and issue deduplication/publication.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: This independent slice covers only PSG, PAC and actinophryid extrusome; corpus-wide gates and GitHub dedup/publication belong to root. No record, original bundle or GitHub mutation was performed.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: Fresh primary retrieval tiers differ: Laporte2008 main text/captions, Gu2017 Results/Discussion plus specified Methods/captions, Boronat2023 full main text/captions, selected Tang2026 PDF pages and Kakuta2008 author manuscript. No raw microscopy, tomograms, mass spectra or supplementary image pixels were reanalyzed.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: Sakaguchi1998 was read only through publisher Summary; direct requests returned challenge HTML. Sakaguchi2001 was read only through primary PubMed abstract; direct publisher response was403. Browser extraction cache ages are preserved in saved packet. Hausmann1982 uses publisher-deposited Crossref abstract; Cabrera2020 uses PubMed abstract. No unavailable full-body access is claimed.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: Tang2026 selected physical pages1–4 and9–13 were inspected, not the entire35-page PDF. The record older abstract-only wording is historical curator access scope; fresh selected body access does not rewrite that history.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: PAC dataset check covers exact version DOI metadata, not a raw-data manifest. Only PAC tracked Figure2 and the linked PSG Figure2 had direct pixel inspection in this slice; other figure claims were checked in captions and body text.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: Current authority identity, entry type and protein matches do not independently establish organelle localization, necessity, precise mature-product grounding or exhaustive inventory. GP40 candidates remain unreviewed and unassigned to the purified localized isoform.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: All6 native protein commands returned0, but PSG/PAC each have3 examples and zero protein graph nodes; extrusome has no examples and one component-anchored NO_GENE_SYMBOLS node. Empty/limited coverage is not successful biological completeness.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: Historical adapter runner failure occurred at00:49Z, not during this slice. Current source catalogue was fetched at08:54:46Z and lacks matched yeast/Actinophrys organisms; no expression-module search/summarize result was invented.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: Closed historical#2430 is mentioned only as record-history context. Its grouped category predecessor was not read/frozen and no category-wide finding or whole issue is resolved here.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: One exploratory extraction invoked system python without PyYAML and stopped before reading YAML; rerun with repository .venv succeeded. This was an interpreter-routing error, not a failed scientific/native validation check.
- Proteasome storage granule, protein aggregate center and actinophryid extrusome independent subreview: No gitignored repository search is used to infer a missing source/record. Claims about original review checks concern complete specific frozen files, and external negative queries are explicitly bounded.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Current source checks use actual 2026-11-03 fetch timestamps. The runner receipt is explicitly historical at00:49Z; no new adapter-runner invocation or adapter query success is claimed.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Direct PMC requests for Waller1998, Tic20/vanDooren2008 and Agrawal2009 returned challenge HTML; alternative full-text APIs failed. Waller was read in an author-hosted published PDF. Tic20 was checked via indexed primary Results and the author dissertation Appendix2; Der1 was checked through native deposits and Chapter3 Methods/Table3.1. These are not represented as new successful live PMC full-body reads.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Kartal2013 repository PDF requests timed out and the direct publisher route failed. Fresh native abstract/bibliography and specifically returned indexed secondary-review passages were inspected instead; no fresh complete PDF read is claimed. The 2015 primary article supplies direct reaction and localization scope used for the current findings.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Sinninghe Damste2002 and van Niftrik2004 were inspected at native complete abstract/bibliographic scope only. The cited Annual Review2013 was likewise abstract/bibliographic scope; no undisclosed full-body access.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: No raw images, tomography, quantitative localization assays, supplementary alignments or experimental datasets were independently reanalysed. These targets have no maintained image attachments. Inspected publication captions are not pixel inspection.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Individual exact carriers, uncharacterized HAO paralogs, whole-organelle assembly dependencies, complete lipid composition and quantitative barrier efficiency remain unresolved. Native identifier/coverage checks cannot establish these claims.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Current protein metadata distinguishes unreviewed examples, native ORF fields and absent native gene fields. Family matches do not prove cellular localization; automated generic ER annotations are not substituted for the primary Der1 paralog evidence. O97275/Der1-2 evidence is not the full-length Der1-1 experiment.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: The source-specific membrane-position model for ERAD/SELMA and secondary review metabolic synthesis remain distinct from direct membrane-resolved experiments. No exhaustive search of every import-machine family or pathway representation is claimed.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Native taxonomy corrects historical Kuenenia spelling; the retained historical synonym denotes the same taxon. No taxonomy record edit is performed here.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: A bounded exact OLS label query and exact UniProt queries do not establish broad ontology, gene or homology absence. The complete official catalogue is sufficient only for the stated current dataset coverage assessment; it is not negative biological evidence.
- Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Frozen apicoplast membrane neighbor was used only for boundary/context, not to resolve all of its scientific assertions. No broader historical finding is marked resolved. Root-owned global QC/CI and public issue filing are reported separately with their actual receipts.
- Historical observations remain immutable; their old checks are not represented as current-head execution.
- The adapter runner was not rerun after the canary established OS access failure. Catalogue-based coverage is assessed directly; fresh and reused responses retain actual access timestamps.
- Native label checks include 923 no-adapter skips. Native identifier checks include 909 PMID transport failures and 254 skipped identifiers; bounded supplemental checks independently resolve the 909 PMIDs.
- Scientific record-curation findings stay in separate issues; no record is edited by this review PR.
- Final trusted-base post-save review-check, exact-head independent acceptance, final-head CI and merge-group CI occur after saving this immutable observation and are not represented here as already completed.
- All ten original YAML/Markdown pairs remain unchanged. Current main was merged normally and pushed without force.
- This explicit issue-bearing ten-record cohort follows the native persistence policy. Every inherited finding is reassessed and retains exact predecessor identity.
- Issue #2632 tracks six stale reviews. Scientific record curation remains separately tracked and open. Existing validator #2514 remains open.
- Current PSG retraction-exclusion evidence is assessed directly. The history reference to closed grouped #2430 is context only; neither that whole multi-record issue nor an unfrozen category finding is terminally resolved.
- Source commit e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4 is retained by tag review-base/pr2357-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native configuration, graph/protein policies, verifier source, the tracked PAC figure and the requested apicoplast membrane and whole acidocalcisome neighbors. Neighbors are context, not additional targets.
- Fresh source inspection retains actual access dates. Primary bodies, abstracts, secondary reviews, authority metadata and actual image-pixel inspection retain distinct scopes.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not validate molecular mechanisms or names appearing only in prose. Identity, taxon, membership, location, function and assembly necessity remain separate judgments.
- Issue #2633 tracks eight applicability defects. Four omissions and four unsupported expression-only rationales are distinguished from the two genuine sparse exclusions.
- Issue #2638 tracks adding the required repository field to the exact extrusome predecessor reference in the uncommitted synthesis source; scientific content and lineage identity are unchanged.
- All15 original scientific findings retain exact occurrence lineage and remain open for record curation: seven major and eight minor, with the extrusome frequency-scope finding provisional. The four targets without scientific findings retain qualified passes. No scientific finding is terminally resolved.
- Issue #2650 tracks removing repeated evidence references from four uncommitted draft assessments. First-occurrence order, evidence records and scientific conclusions are unchanged. The failed native validation draft and receipt are retained.
- Issue #2651 tracks adding required normalization reasons for the two minor acidocalcisome author-attribution findings. Valid DOI/year, biological scope, severity and original lineage remain unchanged; failed uncommitted validation receipts are retained.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261103T090954Z-pr2357-current-record-followup
kind: batch
repository: CultureBotAI/CellStructureMech
title: 'PR 2357: current-input review of ten records and adversarial follow-up'
started_at: '2026-11-03T08:53:23.110159Z'
finished_at: '2026-11-03T09:09:54Z'
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
summary: Current-input reassessment of all ten records in PR2357. Six stale reviews
  are substantively refreshed against current changes. Independent scientific reviews
  retain all15 original findings (seven major,eight minor; one minor remains provisional),
  correct eight structured-source applicability defects and complete the predecessor
  repository field without editing records.
source:
  git_revision: e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4
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
  - path: data/images/inclusion/protein_aggregate_center/pmc10342647_ijms_24_11202_f002.jpg
    sha256: 7d9c957cdb378c0a51800a3890e66cf2d0d0b05d7596bf0e220e0224b374c6da
    role: context
  - path: data/structures/inclusion/proteasome_storage_granule.yaml
    sha256: c905148a1f69e6dbcdca6de2e92701f51186b790ade37268bd009786a08b49d0
    role: target
  - path: data/structures/inclusion/protein_aggregate_center.yaml
    sha256: c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b
    role: target
  - path: data/structures/membrane_organelle/acidocalcisome.yaml
    sha256: 329d7abce6fd71669130238f2b8a83e0f9373989acc34553172acb575153bbf0
    role: context
  - path: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    sha256: 3238b530f5846e584dfb86651fd4895cb461e26bcc74afa51f3740815fab02e9
    role: target
  - path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    sha256: 50bb07e7d5b68718300fd375225e45528a00f82eb091e413d4c184a66134fca8
    role: target
  - path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
    sha256: 48d64d84e4dcd8ddfd271c19c1b259b2357e09ef92625ecfaa09e65c9b26bbe5
    role: target
  - path: data/structures/membrane_organelle/anammoxosome.yaml
    sha256: 50adeae38935dda1315b70ceec936b8224d4e6db33f07cd5caf60da96e95b1fa
    role: target
  - path: data/structures/membrane_organelle/anammoxosome_membrane.yaml
    sha256: 0a47b8cfa7bc71dcfc8cb69ba625087ce23025f9a1204b0fe578d185c2035f61
    role: target
  - path: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    sha256: f78f51681a7a3d41ee0b7e4cdd0472b998e517b697cd25abdcf1e3e2cf5aa4d1
    role: target
  - path: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    sha256: bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b
    role: target
  - path: data/structures/membrane_organelle/apicoplast.yaml
    sha256: 00971d8425f63fc5d490907a43c00b6760c2d88c5413fce6bdbc2dd09919410e
    role: target
  - path: data/structures/membrane_organelle/apicoplast_membrane.yaml
    sha256: fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58
    role: context
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
  - path: reviews/structured/20261021T104739Z-proteasome-storage-granule-audit/review.md
    sha256: 8907581631d9f2cffede80db19f71b124dd2a9d62404c05356f06c21a5757726
    role: context
  - path: reviews/structured/20261021T104739Z-proteasome-storage-granule-audit/review.yaml
    sha256: db51f766110e6156276e23d8cf924755b2a50ed59d87e8be08042756377c629c
    role: context
  - path: reviews/structured/20261021T104740Z-protein-aggregate-center-audit/review.md
    sha256: 7c6fc82e09607dae57dd7f96a544a309caaa77883c98f43027f22dac6fbf2e71
    role: context
  - path: reviews/structured/20261021T104740Z-protein-aggregate-center-audit/review.yaml
    sha256: 78d0d83b502947841a73324f940748fd9d90cd42b5a2477b6e7d16d9c69f5c7c
    role: context
  - path: reviews/structured/20261021T104741Z-acidocalcisome-lumen-audit/review.md
    sha256: 6d9afe126662390b57b57c7077a7515bc302537b4c39043beea7e6f052d91ed7
    role: context
  - path: reviews/structured/20261021T104741Z-acidocalcisome-lumen-audit/review.yaml
    sha256: 3a1885dabede938ce5cf6905a0175ff1b22824666fe68477a8ed9591543a386b
    role: context
  - path: reviews/structured/20261021T104742Z-acidocalcisome-membrane-audit/review.md
    sha256: 418df02c0099606eeb3c884f11030f22b9bc44b6320520e5f8cd0e49d9e0de8d
    role: context
  - path: reviews/structured/20261021T104742Z-acidocalcisome-membrane-audit/review.yaml
    sha256: f48e0f4ae66a74d9319535eca2f336224fe9f29f15b3b04e332bb07a22fbb813
    role: context
  - path: reviews/structured/20261021T104743Z-actinophryid-extrusome-audit/review.md
    sha256: 80603ccdc34112f5f0e1c7dd690adc112127dd30a51541f39dcc152ddf38e246
    role: context
  - path: reviews/structured/20261021T104743Z-actinophryid-extrusome-audit/review.yaml
    sha256: c942a77f51e9e5965e8e8dcfb61dd0e38ad2958d5f0c5cccdc82b787ef2a881d
    role: context
  - path: reviews/structured/20261021T104744Z-anammoxosome-audit/review.md
    sha256: db815243b38a39c3810dec74aabb0652713b7eacb9d735d3ade602cebf528509
    role: context
  - path: reviews/structured/20261021T104744Z-anammoxosome-audit/review.yaml
    sha256: f7bf58ff4275f8d356cbbec870247f66368df856a869ff8fc0fbf5a31d686760
    role: context
  - path: reviews/structured/20261021T104745Z-anammoxosome-membrane-audit/review.md
    sha256: ed7a2ad7c5e146a4c4a0403e91cd18b7400b02e67ed6eb45b1408d73ff4797f7
    role: context
  - path: reviews/structured/20261021T104745Z-anammoxosome-membrane-audit/review.yaml
    sha256: b70be8aad6601ca4814aa5b88b02c824c06c7f7e26776f28073bed2795dc9209
    role: context
  - path: reviews/structured/20261021T104745Z-apicomplexan-dense-granule-audit/review.md
    sha256: 2fa1bc3e1e9b28ede3c95c302ca945364daef099a7b0682d4d7bb25c11d4219a
    role: context
  - path: reviews/structured/20261021T104745Z-apicomplexan-dense-granule-audit/review.yaml
    sha256: 5d5e8d36becac6c6ec3030b3406562a952faeff8096a91a295d2c854f3b18396
    role: context
  - path: reviews/structured/20261021T104746Z-apicomplexan-dense-granule-membrane-audit/review.md
    sha256: efa39ebc0ea69cbd5ed23734049c9a8f794d5a3dc6489f282c050e7a61c180d3
    role: context
  - path: reviews/structured/20261021T104746Z-apicomplexan-dense-granule-membrane-audit/review.yaml
    sha256: e7b91a1f900b63a597b464203c22ece492919fa2ba42f1321133160cfe30ff9f
    role: context
  - path: reviews/structured/20261021T104747Z-apicoplast-audit/review.md
    sha256: 18ce9be00270cd332041cf7984cbc6806e94e876be02457f1f5ab2f023756bc0
    role: context
  - path: reviews/structured/20261021T104747Z-apicoplast-audit/review.yaml
    sha256: b63be1349a513ab07fd8e898e69383852dd8d539a6177f0dda4579ee298c216f
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
- target_id: GO:0034515
  path: data/structures/inclusion/proteasome_storage_granule.yaml
  label: proteasome storage granule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/proteasome_storage_granule.yaml
    role: maintained scientific record
- target_id: GO:0140453
  path: data/structures/inclusion/protein_aggregate_center.yaml
  label: protein aggregate center
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/protein_aggregate_center.yaml
    role: maintained scientific record
- target_id: GO:0033985
  path: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
  label: acidocalcisome lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    role: maintained scientific record
- target_id: GO:0033102
  path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  label: acidocalcisome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
- target_id: cellstructuremech:actinophryid_extrusome
  path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
  label: actinophryid extrusome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
    role: maintained scientific record
- target_id: GO:0044222
  path: data/structures/membrane_organelle/anammoxosome.yaml
  label: anammoxosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
- target_id: cellstructuremech:anammoxosome_membrane
  path: data/structures/membrane_organelle/anammoxosome_membrane.yaml
  label: anammoxosome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome_membrane.yaml
    role: maintained scientific record
- target_id: GO:0020026
  path: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  label: apicomplexan dense granule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    role: maintained scientific record
- target_id: GO:0030668
  path: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  label: apicomplexan dense granule membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    role: maintained scientific record
- target_id: GO:0020011
  path: data/structures/membrane_organelle/apicoplast.yaml
  label: apicoplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
scope:
  description: Exact ten-record PR cohort reassessed against current main 3d7d64088fafc5698ce6d66811594cb26b800f34.
    Changed inputs are substantively reassessed. Scientific records remain unchanged.
  selection: Complete cohort of ten maintained records reviewed in original PR head
    6331a7f4a88273b06a55952d737921b2d1738f97.
  coverage: full
  population_size: 10
  reviewed_target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
checks:
- check_id: qc
  name: Full native QC
  status: passed
  required: true
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
  command: just qc
  exit_code: 0
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  scope_note: Actual local execution at main-merge head e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-qc
- check_id: labels
  name: Native label correspondence
  status: passed
  required: true
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
  command: just validate-products
  exit_code: 0
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  scope_note: Actual local execution at main-merge head e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-labels
- check_id: trait-links
  name: TraitMech references
  status: passed
  required: true
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
  command: just check-trait-links --check
  exit_code: 0
  summary: Native TraitMech link check passed.
  scope_note: Actual local execution at main-merge head e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-trait-links
- check_id: vendored
  name: Pinned governed files
  status: passed
  required: true
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
  command: just vendored-check
  exit_code: 0
  summary: Pinned governed files match; native vendored check passed.
  scope_note: Actual local execution at main-merge head e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-vendored
- check_id: curies
  name: Native identifier resolver
  status: passed
  required: true
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  scope_note: Actual local execution at main-merge head e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Final post-save checks and CI are separate later gates.
  evidence_ids:
  - check-curies
- check_id: focused-0
  name: validate GO:0034515
  status: passed
  required: true
  target_ids:
  - GO:0034515
  command: just validate data/structures/inclusion/proteasome_storage_granule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-1
  name: validate-strict GO:0034515
  status: passed
  required: true
  target_ids:
  - GO:0034515
  command: just validate-strict data/structures/inclusion/proteasome_storage_granule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-2
  name: validate GO:0140453
  status: passed
  required: true
  target_ids:
  - GO:0140453
  command: just validate data/structures/inclusion/protein_aggregate_center.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-3
  name: validate-strict GO:0140453
  status: passed
  required: true
  target_ids:
  - GO:0140453
  command: just validate-strict data/structures/inclusion/protein_aggregate_center.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-4
  name: validate GO:0033985
  status: passed
  required: true
  target_ids:
  - GO:0033985
  command: just validate data/structures/membrane_organelle/acidocalcisome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-5
  name: validate-strict GO:0033985
  status: passed
  required: true
  target_ids:
  - GO:0033985
  command: just validate-strict data/structures/membrane_organelle/acidocalcisome_lumen.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-6
  name: validate GO:0033102
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just validate data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-7
  name: validate-strict GO:0033102
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just validate-strict data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-8
  name: validate cellstructuremech:actinophryid_extrusome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just validate data/structures/membrane_organelle/actinophryid_extrusome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-9
  name: validate-strict cellstructuremech:actinophryid_extrusome
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: just validate-strict data/structures/membrane_organelle/actinophryid_extrusome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-10
  name: validate GO:0044222
  status: passed
  required: true
  target_ids:
  - GO:0044222
  command: just validate data/structures/membrane_organelle/anammoxosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-11
  name: validate-strict GO:0044222
  status: passed
  required: true
  target_ids:
  - GO:0044222
  command: just validate-strict data/structures/membrane_organelle/anammoxosome.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-12
  name: validate cellstructuremech:anammoxosome_membrane
  status: passed
  required: true
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  command: just validate data/structures/membrane_organelle/anammoxosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-13
  name: validate-strict cellstructuremech:anammoxosome_membrane
  status: passed
  required: true
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  command: just validate-strict data/structures/membrane_organelle/anammoxosome_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-14
  name: validate GO:0020026
  status: passed
  required: true
  target_ids:
  - GO:0020026
  command: just validate data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-15
  name: validate-strict GO:0020026
  status: passed
  required: true
  target_ids:
  - GO:0020026
  command: just validate-strict data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-16
  name: validate GO:0030668
  status: passed
  required: true
  target_ids:
  - GO:0030668
  command: just validate data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-17
  name: validate-strict GO:0030668
  status: passed
  required: true
  target_ids:
  - GO:0030668
  command: just validate-strict data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-18
  name: validate GO:0020011
  status: passed
  required: true
  target_ids:
  - GO:0020011
  command: just validate data/structures/membrane_organelle/apicoplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: focused-19
  name: validate-strict GO:0020011
  status: passed
  required: true
  target_ids:
  - GO:0020011
  command: just validate-strict data/structures/membrane_organelle/apicoplast.yaml
  exit_code: 0
  summary: Documented focused command passed.
  evidence_ids:
  - focused
- check_id: supplemental-pmid
  name: Supplemental bounded PMID authority checks
  status: passed
  required: true
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
  command: .venv/bin/python /private/tmp/cellstructure-batches-2346-2397-20261103/check_pmid_chunks.py
    /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357
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
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
  summary: 'Actual molecular and pathway assertions were compared with the official
    catalogue and represented organism scopes. Eight original reviews require correction:
    four unsupported expression-only exemptions (acidocalcisome membrane, actinophryid
    extrusome, anammoxosome and anammoxosome membrane) and four omissions (PSG, PAC,
    apicomplexan dense granule and apicoplast). The anammoxosome membrane has a named
    metabolic-pathway trigger despite an empty protein inventory. Acidocalcisome lumen
    and dense-granule membrane are sparse compartment/material exclusions, with no
    invented molecular queries. Missing matching dataset coverage is bounded resource
    noncoverage, not biological absence. Historical native-runner unavailability is
    separate, with no fresh invocation or successful execution claimed.'
  evidence_ids:
  - plaque-catalogue
  - plaque-historical-runner
  - micro-adapter-catalogue
  - septin-current-adapter-catalogue
- check_id: independent-scientific-review
  name: Independent claim-level source review
  status: passed
  required: true
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
  summary: Three read-only reviewers covered the complete ten-record cohort, including
    changed inputs, with explicit scientific findings and source-access limits. Final
    artifact/head acceptance occurs after saving.
  evidence_ids:
  - plaque-policy
  - plaque-rubric
  - plaque-graph-policy
  - plaque-schema-policy
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-lumen-ancestors
  - plaque-acidocalcisome-agent-SL-0316
  - plaque-acidocalcisome-agent-SL-0003
  - plaque-acidocalcisome-agent-tax-2
  - plaque-acidocalcisome-agent-tax-2759
  - plaque-acidocalcisome-agent-tax-358
  - plaque-acidocalcisome-agent-doi-2003
  - plaque-acidocalcisome-agent-doi-2005
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-doi-2020
  - plaque-acidocalcisome-agent-pmc2020-native
  - plaque-acidocalcisome-agent-doi-2024
  - plaque-acidocalcisome-agent-pmc2024-native
  - plaque-acidocalcisome-agent-membrane-ancestors
  - plaque-acidocalcisome-agent-Q8VPZ0
  - plaque-acidocalcisome-agent-Q8VPZ0-matches
  - plaque-acidocalcisome-agent-IPR004131
  - plaque-granule-agent-go
  - plaque-granule-agent-tax-2759
  - plaque-granule-agent-tax-5794
  - plaque-granule-agent-tax-5811
  - plaque-granule-agent-tax-508771
  - plaque-granule-agent-P13403
  - plaque-granule-agent-P13404
  - plaque-granule-agent-Q27003
  - plaque-granule-agent-A0A125YME4
  - plaque-granule-agent-matches-P13404
  - plaque-granule-agent-matches-Q27003
  - plaque-granule-agent-IPR008118
  - plaque-granule-agent-IPR008119
  - plaque-granule-agent-doi-10.1111_jeu.12904
  - plaque-granule-agent-doi-10.1016_j.pt.2014.12.002
  - plaque-granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - plaque-granule-agent-doi-10.1016_j.chom.2015.04.003
  - plaque-granule-agent-doi-10.1016_j.parint.2013.04.003
  - plaque-granule-agent-doi-10.1016_j.chom.2013.03.002
  - plaque-granule-agent-pmid-9208224
  - plaque-granule-agent-jats-PMC9482668
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-pmc-PMC13475723
  - plaque-granule-agent-jats-PMC7202600
  - plaque-granule-agent-gene-7901472
  - plaque-granule-membrane-agent-go
  - plaque-gra17-S8GTZ8
  - plaque-gra17-gene
  - plaque-catalogue
  - micro-review-policy
  - micro-review-config
  - micro-presence-enum
  - micro-laporte2008
  - micro-gu2017
  - micro-tang2026
  - micro-psg-retraction
  - micro-psg-commentary
  - micro-boronat2023
  - micro-cabrera2020
  - micro-hausmann1982
  - micro-sakaguchi1998
  - micro-sakaguchi2001
  - micro-kakuta2008
  - micro-metadata-sakaguchi1998-crossref
  - micro-metadata-sakaguchi2001-crossref
  - micro-metadata-kakuta-crossref
  - micro-metadata-tang2026-crossref
  - micro-metadata-retracted2018-crossref
  - micro-go-terms
  - micro-tax-4932
  - micro-tax-4896
  - micro-tax-559292
  - micro-tax-238771
  - micro-uniprot-P43583
  - micro-matches-P43583
  - micro-uniprot-P43593
  - micro-matches-P43593
  - micro-uniprot-P0CG63
  - micro-matches-P0CG63
  - micro-uniprot-Q12329
  - micro-matches-Q12329
  - micro-uniprot-P53286
  - micro-matches-P53286
  - micro-uniprot-P31539
  - micro-matches-P31539
  - micro-uniprot-B2NIF0
  - micro-matches-B2NIF0
  - micro-uniprot-B2NIF1
  - micro-matches-B2NIF1
  - micro-entry-IPR035309
  - micro-entry-IPR044635
  - micro-entry-IPR050158
  - micro-entry-IPR031107
  - micro-entry-IPR001270
  - micro-entry-IPR050130
  - micro-entry-IPR000757
  - micro-entry-IPR013320
  - micro-entry-IPR062150
  - micro-deleted-IPR050546
  - micro-pac-dataset
  - micro-psg-image
  - micro-package-PMC2396804
  - micro-package-PMC10342647
  - micro-adapter-catalogue
  - septin-native-review-policy
  - septin-native-curation-policy
  - septin-root20-sources-anammoxosome-go
  - septin-root20-sources-NCBITaxon-2
  - septin-root20-sources-NCBITaxon-203682
  - septin-root20-sources-NCBITaxon-174633
  - septin-root20-sources-doi-10.1111_1574-6976.12014
  - septin-root20-sources-doi-10.1128_JB.00186-15
  - septin-root20-sources-PMID-15098544
  - septin-root20-sources-PMID-25962914
  - septin-root20-sources-PMID-12384695
  - septin-root20-sources-legacy-PMC4524196
  - septin-root20-sources-UniProtKB-A0A2C9CHN2
  - septin-root20-sources-UniProtKB-A0A2C9CH14
  - septin-root20-sources-UniProtKB-A0A2C9CHM2
  - septin-root20-sources-UniProtKB-Q1PX48
  - septin-root20-sources-UniProtKB-Q1PYC5
  - septin-root20-sources-anammox-membrane-go
  - septin-apicoplast-agent-go
  - septin-apicoplast-agent-tax-5794
  - septin-apicoplast-agent-tax-5811
  - septin-apicoplast-agent-tax-5833
  - septin-apicoplast-agent-tax-508771
  - septin-apicoplast-agent-tax-36329
  - septin-apicoplast-agent-S8GBF3
  - septin-apicoplast-agent-O97275
  - septin-apicoplast-agent-B9PY98
  - septin-apicoplast-agent-Q8I295
  - septin-apicoplast-agent-Q965D5
  - septin-apicoplast-agent-Q965D7
  - septin-apicoplast-agent-C9WWW6
  - septin-apicoplast-agent-matches-S8GBF3
  - septin-apicoplast-agent-matches-O97275
  - septin-apicoplast-agent-matches-B9PY98
  - septin-apicoplast-agent-matches-Q8I295
  - septin-apicoplast-agent-matches-Q965D5
  - septin-apicoplast-agent-matches-Q965D7
  - septin-apicoplast-agent-IPR005691
  - septin-apicoplast-agent-IPR007599
  - septin-apicoplast-agent-IPR036291
  - septin-apicoplast-agent-IPR010084
  - septin-apicoplast-agent-IPR013114
  - septin-apicoplast-agent-IPR029069
  - septin-apicoplast-agent-doi-10.1073_pnas.95.21.12352
  - septin-apicoplast-agent-doi-10.1098_rstb.2009.0273
  - septin-apicoplast-agent-doi-10.1073_pnas.0803862105
  - septin-apicoplast-agent-doi-10.1371_journal.ppat.1003426
  - septin-apicoplast-agent-doi-10.1186_1475-2875-12-25
  - septin-apicoplast-agent-doi-10.1146_annurev-micro-092412-155741
  - septin-apicoplast-agent-doi-10.1371_journal.pbio.1001138
  - septin-apicoplast-agent-doi-10.1016_j.ijpara.2016.08.005
  - septin-apicoplast-agent-doi-10.1074_jbc.M109.044024
  - septin-apicoplast-agent-doi-10.1128_EC.00061-09
  - septin-apicoplast-agent-jats-PMC3681736
  - septin-apicoplast-agent-jats-PMC3662607
  - septin-apicoplast-agent-jats-PMC3166167
  - septin-apicoplast-agent-jats-PMC2817234
  - septin-apicoplast-agent-jats-PMC5406208
  - septin-apicoplast-agent-ena-FJ976521
  - septin-apicoplast-agent-ena-FJ976520
  - septin-apicoplast-agent-ena-CAB38986
  - septin-apicoplast-agent-gene-814456
  - septin-apicoplast-agent-kalanon2009-pdf
  - septin-current-adapter-catalogue
  - septin-apicoplast-current-Q8IJH7
  - septin-apicoplast-current-matches-Q8IJH7
  - septin-current-IPR035952
  - septin-current-IPR003451
  - septin-current-IPR002347
  - septin-current-IPR014358
  - septin-waller1998-author-pdf
  - septin-agrawal2011-thesis
  - septin-current-tic20-indexed-primary
  - septin-current-kartal-indexed-review
- check_id: historical-adapter-runner
  name: Retained historical adapter runner availability
  status: unavailable
  required: false
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0020011
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
- check_id: proteasome_storage_granule-uniprot-verify
  name: Native proteasome storage granule UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0034515
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-proteasome_storage_granule-verify
- check_id: proteasome_storage_granule-uniprot-causal
  name: Native proteasome storage granule UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0034515
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-proteasome_storage_granule-causal
- check_id: protein_aggregate_center-uniprot-verify
  name: Native protein aggregate center UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0140453
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-protein_aggregate_center-verify
- check_id: protein_aggregate_center-uniprot-causal
  name: Native protein aggregate center UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0140453
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-protein_aggregate_center-causal
- check_id: acidocalcisome_lumen-uniprot-verify
  name: Native acidocalcisome lumen UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033985
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-acidocalcisome_lumen-verify
- check_id: acidocalcisome_lumen-uniprot-causal
  name: Native acidocalcisome lumen UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033985
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-acidocalcisome_lumen-causal
- check_id: acidocalcisome_membrane-uniprot-verify
  name: Native acidocalcisome membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-acidocalcisome_membrane-verify
- check_id: acidocalcisome_membrane-uniprot-causal
  name: Native acidocalcisome membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-acidocalcisome_membrane-causal
- check_id: actinophryid_extrusome-uniprot-verify
  name: Native actinophryid extrusome UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-actinophryid_extrusome-verify
- check_id: actinophryid_extrusome-uniprot-causal
  name: Native actinophryid extrusome UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - micro-native-actinophryid_extrusome-causal
- check_id: anammoxosome-uniprot-verify
  name: Native anammoxosome UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0044222
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-anammoxosome-verify
- check_id: anammoxosome-uniprot-causal
  name: Native anammoxosome UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0044222
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-anammoxosome-causal
- check_id: anammoxosome_membrane-uniprot-verify
  name: Native anammoxosome membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-anammoxosome_membrane-verify
- check_id: anammoxosome_membrane-uniprot-causal
  name: Native anammoxosome membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-anammoxosome_membrane-causal
- check_id: apicomplexan_dense_granule-uniprot-verify
  name: Native apicomplexan dense granule UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020026
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-apicomplexan_dense_granule-verify
- check_id: apicomplexan_dense_granule-uniprot-causal
  name: Native apicomplexan dense granule UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020026
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-apicomplexan_dense_granule-causal
- check_id: apicomplexan_dense_granule_membrane-uniprot-verify
  name: Native apicomplexan dense granule membrane UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0030668
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-apicomplexan_dense_granule_membrane-verify
- check_id: apicomplexan_dense_granule_membrane-uniprot-causal
  name: Native apicomplexan dense granule membrane UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0030668
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - plaque-native-apicomplexan_dense_granule_membrane-causal
- check_id: apicoplast-uniprot-verify
  name: Native apicoplast UniProt verify check
  status: passed
  required: true
  target_ids:
  - GO:0020011
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicoplast.yaml
    --verify
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-apicoplast-verify
- check_id: apicoplast-uniprot-causal
  name: Native apicoplast UniProt causal check
  status: passed
  required: true
  target_ids:
  - GO:0020011
  command: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicoplast.yaml
    --causal-graphs
  exit_code: 0
  summary: Read-only native command returned zero. Exact represented inventory and
    coverage limits are retained in evidence. Empty inventories or zero molecular
    graph nodes do not validate narrative molecules, mechanism, taxon transfer or
    assembly necessity.
  scope_note: Actual execution at current main-merge head; verifier source frozen
    before assessment.
  evidence_ids:
  - septin-native-apicoplast-causal
evidence:
- evidence_id: current-record-0
  kind: record_content
  reference: data/structures/inclusion/proteasome_storage_granule.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 e09339d5bc79d9ee31b2e5e342b82a67992e86fc4d2fd16559791fefa46121af;
    current SHA256 c905148a1f69e6dbcdca6de2e92701f51186b790ade37268bd009786a08b49d0.
    Changed record reassessed against current sources.
  snapshot_sha256: c905148a1f69e6dbcdca6de2e92701f51186b790ade37268bd009786a08b49d0
- evidence_id: original-review-0
  kind: prior_review
  reference: reviews/structured/20261021T104739Z-proteasome-storage-granule-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: db51f766110e6156276e23d8cf924755b2a50ed59d87e8be08042756377c629c
- evidence_id: current-record-1
  kind: record_content
  reference: data/structures/inclusion/protein_aggregate_center.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b;
    current SHA256 c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b.
    Record bytes unchanged since the original review.
  snapshot_sha256: c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b
- evidence_id: original-review-1
  kind: prior_review
  reference: reviews/structured/20261021T104740Z-protein-aggregate-center-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 78d0d83b502947841a73324f940748fd9d90cd42b5a2477b6e7d16d9c69f5c7c
- evidence_id: current-record-2
  kind: record_content
  reference: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 3238b530f5846e584dfb86651fd4895cb461e26bcc74afa51f3740815fab02e9;
    current SHA256 3238b530f5846e584dfb86651fd4895cb461e26bcc74afa51f3740815fab02e9.
    Record bytes unchanged since the original review.
  snapshot_sha256: 3238b530f5846e584dfb86651fd4895cb461e26bcc74afa51f3740815fab02e9
- evidence_id: original-review-2
  kind: prior_review
  reference: reviews/structured/20261021T104741Z-acidocalcisome-lumen-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 3a1885dabede938ce5cf6905a0175ff1b22824666fe68477a8ed9591543a386b
- evidence_id: current-record-3
  kind: record_content
  reference: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 2a2a8ddf090bccdc6e8f0fd6b84f3e2ce971789071cb6af97dde48ed834f3a55;
    current SHA256 50bb07e7d5b68718300fd375225e45528a00f82eb091e413d4c184a66134fca8.
    Changed record reassessed against current sources.
  snapshot_sha256: 50bb07e7d5b68718300fd375225e45528a00f82eb091e413d4c184a66134fca8
- evidence_id: original-review-3
  kind: prior_review
  reference: reviews/structured/20261021T104742Z-acidocalcisome-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f48e0f4ae66a74d9319535eca2f336224fe9f29f15b3b04e332bb07a22fbb813
- evidence_id: current-record-4
  kind: record_content
  reference: data/structures/membrane_organelle/actinophryid_extrusome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 4b0f4ea17353cf6db5e343ef4a88ddc1458185fdcb508b74ca4fa8685421d0ea;
    current SHA256 48d64d84e4dcd8ddfd271c19c1b259b2357e09ef92625ecfaa09e65c9b26bbe5.
    Changed record reassessed against current sources.
  snapshot_sha256: 48d64d84e4dcd8ddfd271c19c1b259b2357e09ef92625ecfaa09e65c9b26bbe5
- evidence_id: original-review-4
  kind: prior_review
  reference: reviews/structured/20261021T104743Z-actinophryid-extrusome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: c942a77f51e9e5965e8e8dcfb61dd0e38ad2958d5f0c5cccdc82b787ef2a881d
- evidence_id: current-record-5
  kind: record_content
  reference: data/structures/membrane_organelle/anammoxosome.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 c98e06c7ce32979c1cb1a54179f4395700a59adfcc5c0a1947c5b30f9fb34b84;
    current SHA256 50adeae38935dda1315b70ceec936b8224d4e6db33f07cd5caf60da96e95b1fa.
    Changed record reassessed against current sources.
  snapshot_sha256: 50adeae38935dda1315b70ceec936b8224d4e6db33f07cd5caf60da96e95b1fa
- evidence_id: original-review-5
  kind: prior_review
  reference: reviews/structured/20261021T104744Z-anammoxosome-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: f7bf58ff4275f8d356cbbec870247f66368df856a869ff8fc0fbf5a31d686760
- evidence_id: current-record-6
  kind: record_content
  reference: data/structures/membrane_organelle/anammoxosome_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 0a47b8cfa7bc71dcfc8cb69ba625087ce23025f9a1204b0fe578d185c2035f61;
    current SHA256 0a47b8cfa7bc71dcfc8cb69ba625087ce23025f9a1204b0fe578d185c2035f61.
    Record bytes unchanged since the original review.
  snapshot_sha256: 0a47b8cfa7bc71dcfc8cb69ba625087ce23025f9a1204b0fe578d185c2035f61
- evidence_id: original-review-6
  kind: prior_review
  reference: reviews/structured/20261021T104745Z-anammoxosome-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b70be8aad6601ca4814aa5b88b02c824c06c7f7e26776f28073bed2795dc9209
- evidence_id: current-record-7
  kind: record_content
  reference: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 49d7347778d1dd9a80bf5ab53049d35eeefad4aee5581cb2c493dab7bb1c0bb2;
    current SHA256 f78f51681a7a3d41ee0b7e4cdd0472b998e517b697cd25abdcf1e3e2cf5aa4d1.
    Changed record reassessed against current sources.
  snapshot_sha256: f78f51681a7a3d41ee0b7e4cdd0472b998e517b697cd25abdcf1e3e2cf5aa4d1
- evidence_id: original-review-7
  kind: prior_review
  reference: reviews/structured/20261021T104745Z-apicomplexan-dense-granule-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: 5d5e8d36becac6c6ec3030b3406562a952faeff8096a91a295d2c854f3b18396
- evidence_id: current-record-8
  kind: record_content
  reference: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b;
    current SHA256 bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b.
    Record bytes unchanged since the original review.
  snapshot_sha256: bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b
- evidence_id: original-review-8
  kind: prior_review
  reference: reviews/structured/20261021T104746Z-apicomplexan-dense-granule-membrane-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: e7b91a1f900b63a597b464203c22ece492919fa2ba42f1321133160cfe30ff9f
- evidence_id: current-record-9
  kind: record_content
  reference: data/structures/membrane_organelle/apicoplast.yaml
  locator: Whole current maintained record; exact bytes frozen by native inspect
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Original frozen SHA256 92a545baa209311fdb4b224a2253a543c1a67c87b35b8004334c9bebf02f5186;
    current SHA256 00971d8425f63fc5d490907a43c00b6760c2d88c5413fce6bdbc2dd09919410e.
    Changed record reassessed against current sources.
  snapshot_sha256: 00971d8425f63fc5d490907a43c00b6760c2d88c5413fce6bdbc2dd09919410e
- evidence_id: original-review-9
  kind: prior_review
  reference: reviews/structured/20261021T104747Z-apicoplast-audit/review.yaml
  locator: 'Original immutable observation: sources, checks, scientific verdict, findings,
    actions and limitations'
  accessed_at: '2026-11-03T09:09:54Z'
  support: context_only
  summary: Historical review retained without rewriting its evidence or promoting
    old checks to current execution.
  snapshot_sha256: b63be1349a513ab07fd8e898e69383852dd8d539a6177f0dda4579ee298c216f
- evidence_id: plaque-current-2
  kind: record_content
  reference: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
  locator: Entire current YAML at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4;
    every field, history and graph edge
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Entire maintained target read against the frozen inspection bytes; current
    PROPOSED status is preserved. No target image is declared.
  snapshot_sha256: 3238b530f5846e584dfb86651fd4895cb461e26bcc74afa51f3740815fab02e9
- evidence_id: plaque-original-2
  kind: prior_review
  reference: reviews/structured/20261021T104741Z-acidocalcisome-lumen-audit/review.yaml
  locator: Complete authoritative YAML and exact derived Markdown; findings, checks,
    source inputs and all assessments
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Original review 20261021T104741Z-acidocalcisome-lumen-audit independently
    inspected. Native validation and exact render passed; the historical target bytes
    match its frozen hash.
  snapshot_sha256: 3a1885dabede938ce5cf6905a0175ff1b22824666fe68477a8ed9591543a386b
- evidence_id: plaque-current-3
  kind: record_content
  reference: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  locator: Entire current YAML at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4;
    every field, history and graph edge
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Entire maintained target read against the frozen inspection bytes; current
    PROPOSED status is preserved. No target image is declared.
  snapshot_sha256: 50bb07e7d5b68718300fd375225e45528a00f82eb091e413d4c184a66134fca8
- evidence_id: plaque-original-3
  kind: prior_review
  reference: reviews/structured/20261021T104742Z-acidocalcisome-membrane-audit/review.yaml
  locator: Complete authoritative YAML and exact derived Markdown; findings, checks,
    source inputs and all assessments
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Original review 20261021T104742Z-acidocalcisome-membrane-audit independently
    inspected. Native validation and exact render passed; the historical target bytes
    match its frozen hash.
  snapshot_sha256: f48e0f4ae66a74d9319535eca2f336224fe9f29f15b3b04e332bb07a22fbb813
- evidence_id: plaque-current-7
  kind: record_content
  reference: data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
  locator: Entire current YAML at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4;
    every field, history and graph edge
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Entire maintained target read against the frozen inspection bytes; current
    PROPOSED status is preserved. No target image is declared.
  snapshot_sha256: f78f51681a7a3d41ee0b7e4cdd0472b998e517b697cd25abdcf1e3e2cf5aa4d1
- evidence_id: plaque-original-7
  kind: prior_review
  reference: reviews/structured/20261021T104745Z-apicomplexan-dense-granule-audit/review.yaml
  locator: Complete authoritative YAML and exact derived Markdown; findings, checks,
    source inputs and all assessments
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Original review 20261021T104745Z-apicomplexan-dense-granule-audit independently
    inspected. Native validation and exact render passed; the historical target bytes
    match its frozen hash.
  snapshot_sha256: 5d5e8d36becac6c6ec3030b3406562a952faeff8096a91a295d2c854f3b18396
- evidence_id: plaque-current-8
  kind: record_content
  reference: data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
  locator: Entire current YAML at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4;
    every field, history and graph edge
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Entire maintained target read against the frozen inspection bytes; current
    PROPOSED status is preserved. No target image is declared.
  snapshot_sha256: bd48fa3c1773cf7be7066602608acdd61ba386a9fbc5fc3fd19ddaa25dcab51b
- evidence_id: plaque-original-8
  kind: prior_review
  reference: reviews/structured/20261021T104746Z-apicomplexan-dense-granule-membrane-audit/review.yaml
  locator: Complete authoritative YAML and exact derived Markdown; findings, checks,
    source inputs and all assessments
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Original review 20261021T104746Z-apicomplexan-dense-granule-membrane-audit
    independently inspected. Native validation and exact render passed; the historical
    target bytes match its frozen hash.
  snapshot_sha256: e7b91a1f900b63a597b464203c22ece492919fa2ba42f1321133160cfe30ff9f
- evidence_id: plaque-whole-organelle
  kind: record_content
  reference: data/structures/membrane_organelle/acidocalcisome.yaml
  locator: Frozen local context; relevant boundary, evidence, schema and review rules
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Whole organelle supplies boundary and existing bacterial-dispute context
    only, not an independent scientific review of that neighboring record.
  snapshot_sha256: 329d7abce6fd71669130238f2b8a83e0f9373989acc34553172acb575153bbf0
- evidence_id: plaque-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Frozen local context; relevant boundary, evidence, schema and review rules
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Repository policy requires claim-level support, exact input provenance,
    separate identity/membership/necessity, bounded adapter applicability and immutable
    reviews.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
- evidence_id: plaque-rubric
  kind: authority
  reference: .claude/skills/curate-yaml-record/references/review-checklist.md
  locator: Frozen local context; relevant boundary, evidence, schema and review rules
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Repository policy requires claim-level support, exact input provenance,
    separate identity/membership/necessity, bounded adapter applicability and immutable
    reviews.
  snapshot_sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
- evidence_id: plaque-graph-policy
  kind: authority
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Frozen local context; relevant boundary, evidence, schema and review rules
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Repository policy requires claim-level support, exact input provenance,
    separate identity/membership/necessity, bounded adapter applicability and immutable
    reviews.
  snapshot_sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
- evidence_id: plaque-schema-policy
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Frozen local context; relevant boundary, evidence, schema and review rules
  accessed_at: '2026-11-03T09:01:38.219209Z'
  support: context_only
  summary: Repository policy requires claim-level support, exact input provenance,
    separate identity/membership/necessity, bounded adapter applicability and immutable
    reviews.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
- evidence_id: plaque-acidocalcisome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033985,GO:0033102,GO:0043233,GO:0020022,GO:0016020
  locator: 'results for GO0033985, GO0033102, GO0043233, GO0020022, GO0016020: id/name/isObsolete/definition;
    GO0020022.children relation fields'
  accessed_at: '2026-11-03T08:56:54.658021Z'
  support: supports
  summary: Five active native GO cellular-component terms verify lumen, membrane,
    organelle lumen, acidocalcisome and generic membrane identities. GO0020022 lists
    GO0033985 and GO0033102 children with part_of relations; this does not turn parthood
    into is_a. The definitions distinguish enclosed volume from lipid boundary.
  snapshot_sha256: 2872720648af18a28afd5e8444b93db63817e9ac8228ab4def9cb131e62a739c
- evidence_id: plaque-acidocalcisome-agent-lumen-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033985/ancestors?relations=is_a
  locator: results[0].id and ancestors; request relations=is_a
  accessed_at: '2026-11-03T08:56:54.658238Z'
  support: supports
  summary: The requested is_a ancestor closure for GO0033985 includes GO0043233 organelle
    lumen. Acidocalcisome parthood is independently supported by the separate native
    term and location responses.
  snapshot_sha256: 68c056c1e651478155b100675d8235af417a7e97cd599ff82ff69886074553a5
- evidence_id: plaque-acidocalcisome-agent-SL-0316
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0316.json
  locator: id/name/definition/synonyms/geneOntologies/partOf
  accessed_at: '2026-11-03T08:56:54.658304Z'
  support: supports
  summary: Native SL0316 identifies acidocalcisome lumen, supplies the acidocalcisomal
    lumen synonym and GO0033985 cross-reference, and places it partOf SL0002 acidocalcisome.
    Its definition specifies the membrane-bounded compartment.
  snapshot_sha256: a40c2904e72927940ccf1f7a556648c152be4cb9e6f95478788150abf1dc8c4d
- evidence_id: plaque-acidocalcisome-agent-SL-0003
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0003.json
  locator: id/name/definition/synonyms/geneOntologies/isA/partOf
  accessed_at: '2026-11-03T08:56:54.658410Z'
  support: supports
  summary: Native SL0003 identifies acidocalcisome membrane, supplies its synonym
    and GO0033102 cross-reference, has isA SL0162 membrane, and partOf SL0002 acidocalcisome.
  snapshot_sha256: f770848e7dc607ffa0e6f179a939e4d8d5dfe08a4299a2c57e4f902e15aef9f9
- evidence_id: plaque-acidocalcisome-agent-tax-2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Native taxId, scientificName, rank and supplied lineage fields; identity
    only.
  accessed_at: '2026-11-03T08:56:54.658864Z'
  support: supports
  summary: Native taxonomy verifies taxon2 as Bacteria. This identifies the taxon
    and lineage only; it does not establish organelle occurrence, strain equivalence
    or universality.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: plaque-acidocalcisome-agent-tax-2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Native taxId, scientificName, rank and supplied lineage fields; identity
    only.
  accessed_at: '2026-11-03T08:56:54.660077Z'
  support: supports
  summary: Native taxonomy verifies taxon2759 as Eukaryota. This identifies the taxon
    and lineage only; it does not establish organelle occurrence, strain equivalence
    or universality.
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: plaque-acidocalcisome-agent-tax-358
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/358
  locator: Native taxId, scientificName, rank and supplied lineage fields; identity
    only.
  accessed_at: '2026-11-03T08:56:54.660537Z'
  support: supports
  summary: Native taxonomy verifies taxon358 as Agrobacterium tumefaciens. This identifies
    the taxon and lineage only; it does not establish organelle occurrence, strain
    equivalence or universality.
  snapshot_sha256: e4ead5c9da75d4204c7fe36f6a16082f03cc88c29192129647e5bc08f4a9b167
- evidence_id: plaque-acidocalcisome-agent-doi-2003
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074%2Fjbc.M304548200&format=json&resultType=core
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:54.667571Z'
  support: supports
  summary: Exact native metadata identifies Seufferheld and colleagues, PMID12783865,
    DOI10.1074/jbc.M304548200. The complete abstract reports a surrounding membrane
    by TEM, PPase localization by immunofluorescence/immuno-EM, enriched PPase/polyphosphate
    fractions, cations and acidic staining in A. tumefaciens. The abstract calls the
    PPase K-insensitive. This is primary abstract support, not an inspected full body
    or a resolved strain/accession bridge.
  snapshot_sha256: 16d3fd412b4e90ad994a3a8b558763e8b3f7a3683e5dfd2306b487d6d7225dea
- evidence_id: plaque-acidocalcisome-agent-doi-2005
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro1097&format=json&resultType=core
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:54.670637Z'
  support: supports
  summary: Exact native citation identifies Acidocalcisomes - conserved from bacteria
    to man, Docampo, de Souza, Miranda, Rohloff and Moreno, PMID15738951, DOI10.1038/nrmicro1097.
    Citation and complete abstract were read; this receipt is not the article body.
  snapshot_sha256: 1a42be47f760e3cb298aebdc687e611a1d261fd6af36a763b8516ff83223f02f
- evidence_id: plaque-acidocalcisome-agent-review2005-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrmicro1097
  locator: Publisher HTML Abstract section and Key Points bullets1–5 only; no full-main-body
    claim
  accessed_at: '2026-11-03T08:56:54.672146Z'
  support: supports
  summary: The accessible review Abstract and five Key Points describe acidic polyphosphate/cation
    compartments, broad reported occurrence, and membrane Ca-ATPase, V-ATPase, V-PPase
    and exchange activities. This is secondary synthesis with lineage variation, not
    a new primary transport assay. The remaining main article body was not available
    in this response.
  snapshot_sha256: f041477c1b413d433509c4f399fa4cb3598007c743197cf3e0c3c21b52f4ac50
- evidence_id: plaque-acidocalcisome-agent-doi-2020
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FAEM.02759-19&format=json&resultType=core
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:55.258476Z'
  support: supports
  summary: Exact native citation identifies Frank and Jendrossek 2020, PMID32060025,
    PMC7117937, DOI10.1128/AEM.02759-19. The complete abstract proposes that polyphosphate
    granules and HppA-positive structures are distinct in A. tumefaciens; actual Methods/Results
    support is in the separately hashed PMC body.
  snapshot_sha256: 67c068cac424696d77193aba8ae7488026001d621efe5b023350c3e45d606681
- evidence_id: plaque-acidocalcisome-agent-pmc2020-native
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7117937/
  locator: 'Primary HTML: Results/Discussion §§2.1–2.3,2.5–2.6,2.8 and Methods §§3.1–3.5;
    Figure5 caption. No figure-pixel or supplementary-data audit.'
  accessed_at: '2026-11-03T08:56:55.273167Z'
  support: supports
  summary: Frank and Jendrossek 2020 use C58 fluorescence, marker-localization and
    mutant experiments to distinguish DAPI-positive polyphosphate granules from HppA/MitoTracker-associated
    structures. They explicitly lack TEM confirmation. Full-length C58 Atu_1174 is
    not the D44 Q8VPZ0 fragment. The results challenge, rather than definitively disprove,
    the original bacterial acidocalcisome interpretation.
  snapshot_sha256: f9eeca4d0a6b8316562001c217f6b3fa3f5de87e9514911f601347ec85627e4d
- evidence_id: plaque-acidocalcisome-agent-doi-2024
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMMBR.00042-23&format=json&resultType=core
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:55.421662Z'
  support: supports
  summary: Exact native citation identifies Advances in the cellular biology, biochemistry,
    and molecular biology of acidocalcisomes, PMID38099688, PMC10966946, DOI10.1128/MMBR.00042-23,
    with Roberto Docampo as the sole author. Collection year2024 is valid; no Huang
    appears in the author list.
  snapshot_sha256: 76730fcd2d61ed58965979faae8e3f1400d35d6351ae52056d4f3aeb9379f624
- evidence_id: plaque-acidocalcisome-agent-pmc2024-native
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10966946/
  locator: 'Secondary review HTML: byline; §§1–3; §4 direct chemical-composition paragraphs;
    §§5.1 proton pumps,5.2 P-type ATPases,5.5 membrane transporters; §10 cation/phosphorus
    storage. No comprehensive proteomic-table or figure-pixel audit.'
  accessed_at: '2026-11-03T08:56:55.434199Z'
  support: supports
  summary: Sole author Roberto Docampo. The distribution section preserves and challenges
    the C58 interpretation, including short-polyphosphate/DAPI limits. Membrane sections
    distinguish lineage-dependent pumps, Ca2+ uptake, metal/proton exchange, phosphate/sodium
    release and incompletely characterized transporters. §10 explicitly supports metal
    sequestration driven by proton gradients; this is secondary synthesis, not new
    primary experiments or universal transporter direction.
  snapshot_sha256: 9c24a1b61117cc3fe919e083577711bd88447926218d2fd2b9268ca9609341e1
- evidence_id: plaque-acidocalcisome-agent-membrane-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033102/ancestors?relations=is_a
  locator: results[0].id and ancestors; request relations=is_a
  accessed_at: '2026-11-03T08:56:55.436805Z'
  support: supports
  summary: The requested is_a ancestor closure for GO0033102 includes GO0016020 membrane.
    It is separate from the acidocalcisome part_of relation.
  snapshot_sha256: 619c5a69e707dbe22c0dc4bc35f924c76fd550cae5e61ad09e423c9683f07649
- evidence_id: plaque-acidocalcisome-agent-Q8VPZ0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8VPZ0.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, sequence.length,
    fragment flag, references/source strain, FUNCTION and SUBCELLULAR LOCATION comments/evidence
    codes
  accessed_at: '2026-11-03T08:56:55.439102Z'
  support: supports
  summary: Native Q8VPZ0 is reviewed, gene hppA with synonym vppA, tax358, and the
    stated putative K-stimulated pyrophosphate-energized sodium-pump name. It is a189-aa
    fragment submitted from strainD44. Function and cell-inner-membrane annotations
    are inferred by homology; no experimental acidocalcisome localization is established
    by this entry.
  snapshot_sha256: 62b0cd4de2335cca96e281176133b61f0946d97406349648447beef67f1c0e55
- evidence_id: plaque-acidocalcisome-agent-Q8VPZ0-matches
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8VPZ0/?page_size=200
  locator: count, next and results[0].metadata plus protein match coordinates
  accessed_at: '2026-11-03T08:56:55.461605Z'
  support: supports
  summary: The complete native integrated InterPro result has count1 and next=null,
    assigning the189-aa Q8VPZ0 fragment to IPR004131 over positions1–187. This provides
    one integrated family candidate for the inspected protein.
  snapshot_sha256: d9d0da8a0717e20a6554e2532e7bc8bacab510c3f11b92650cc549890c8ac764
- evidence_id: plaque-acidocalcisome-agent-IPR004131
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004131/
  locator: metadata accession/name/type/description and member_databases/signature
    names
  accessed_at: '2026-11-03T08:56:55.470014Z'
  support: supports
  summary: IPR004131 is the pyrophosphate-energised proton-pump family; its native
    description concerns membrane pyrophosphatases and distinguishes K-stimulated/K-insensitive
    subclasses. The member signatures include a putative sodium-pump signature.
  snapshot_sha256: e4e648c13a47216105a8d1d88a9ff06c2591ced606c998fceb591cad8b39765e
- evidence_id: plaque-granule-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020026,GO:0030141,GO:0030668
  locator: Complete GO0020026, GO0030141 and GO0030668 definitions, synonyms and relevant
    relations
  accessed_at: '2026-11-03T08:56:55.482546Z'
  support: supports
  summary: Native GO confirms the secretory dense-granule definition, RELATED dense
    body synonym, secretory-granule parent and distinct bounding-membrane part.
  snapshot_sha256: 695903e78d25a97c58e5261f3429538fd447ddb63c8855a77475aa24a0d0e2e6
- evidence_id: plaque-granule-agent-tax-2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Native taxId, scientificName, rank and supplied lineage fields; identity
    only.
  accessed_at: '2026-11-03T08:56:55.725219Z'
  support: supports
  summary: Native ENA taxonomy identifies Eukaryota, domain. This receipt attests
    that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: 61a68c76c70762c97e0b218568ab037d9a30c0207847247e9e055b5764a61634
- evidence_id: plaque-granule-agent-tax-5794
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: Native taxId, scientificName, rank and supplied lineage fields; identity
    only.
  accessed_at: '2026-11-03T08:56:55.959129Z'
  support: supports
  summary: Native ENA taxonomy identifies Apicomplexa, phylum. This receipt attests
    that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: 617b42c27ae95a801b69abf63e1a545eff8565fd0af2f4a81be359d3fb6b3cbf
- evidence_id: plaque-granule-agent-tax-5811
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: Native taxId, scientificName, rank and supplied lineage fields; identity
    only.
  accessed_at: '2026-11-03T08:56:55.987978Z'
  support: supports
  summary: Native ENA taxonomy identifies Toxoplasma gondii, species. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: cbb209002c87051ce78d0a34bc169d2f6623f6bbfbb21edad170d43eb16d4032
- evidence_id: plaque-granule-agent-tax-508771
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771
  locator: Native taxId, scientificName, rank and supplied lineage fields; identity
    only.
  accessed_at: '2026-11-03T08:56:56.033460Z'
  support: supports
  summary: Native ENA taxonomy identifies Toxoplasma gondii ME49, strain. This receipt
    attests that identity and rank only, not occurrence or the experimental strain.
  snapshot_sha256: d1622dee69e1fe2abfea4351893585852f4200cfff6eac3b42e5a014283cd0b0
- evidence_id: plaque-granule-agent-P13403
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P13403.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    location/function comments, sequence references and cross-references
  accessed_at: '2026-11-03T08:56:56.057940Z'
  support: supports
  summary: 'Native UniProtKB reviewed (Swiss-Prot) P13403: Dense granule protein 1;
    taxon 5811; gene fields [{"geneName": {"value": "GRA1"}}]. Accession identity
    and predicted location annotations do not by themselves prove membership in the
    maintained structure.'
  snapshot_sha256: 013fde27eadf7408ef9d4164b73b9b9f983364f784b16d9546996d6314517d56
- evidence_id: plaque-granule-agent-P13404
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P13404.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    location/function comments, sequence references and cross-references
  accessed_at: '2026-11-03T08:56:56.093881Z'
  support: supports
  summary: 'Native UniProtKB reviewed (Swiss-Prot) P13404: Dense granule protein 2;
    taxon 5811; gene fields [{"geneName": {"value": "GRA2"}}]. Accession identity
    and predicted location annotations do not by themselves prove membership in the
    maintained structure.'
  snapshot_sha256: 8cb1d2d1b3a875fa86b5272522e5caee8050f737919eb05ab83b1fddd56f1fd3
- evidence_id: plaque-granule-agent-Q27003
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q27003.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    location/function comments, sequence references and cross-references
  accessed_at: '2026-11-03T08:56:56.096310Z'
  support: supports
  summary: 'Native UniProtKB reviewed (Swiss-Prot) Q27003: Dense granule protein 6;
    taxon 5811; gene fields [{"geneName": {"value": "GRA6"}, "synonyms": [{"value":
    "TG24"}]}]. Accession identity and predicted location annotations do not by themselves
    prove membership in the maintained structure.'
  snapshot_sha256: 3ddafda8d3e05dcf6d5e658b1ee69409dcef54e7f55b2717d7c33d60a0abf8ca
- evidence_id: plaque-granule-agent-A0A125YME4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A125YME4.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    location/function comments, sequence references and cross-references
  accessed_at: '2026-11-03T08:56:56.109488Z'
  support: supports
  summary: 'Native UniProtKB unreviewed (TrEMBL) A0A125YME4: Dense granule protein
    DG32; taxon 508771; gene fields [{"orfNames": [{"evidences": [{"evidenceCode":
    "ECO:0000313", "source": "EMBL", "id": "EPT32203.1"}], "value": "TGME49_297880"}]}].
    Accession identity and predicted location annotations do not by themselves prove
    membership in the maintained structure.'
  snapshot_sha256: 3d8f8e9505305e626813fb812d5c3ff040591ae3570a2fd6c4653bf90f4428d2
- evidence_id: plaque-granule-agent-matches-P13404
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13404/?page_size=200
  locator: All results; next is null
  accessed_at: '2026-11-03T08:56:56.313169Z'
  support: context_only
  summary: Complete integrated matches were inspected; these individual-family matches
    do not identify the aggregate GRA cargo or exported-effector cohort.
  snapshot_sha256: 9aebb3e387072f6dd110eb330e5ddfc3fabb5773ae1e483d76ff643bdada3b55
- evidence_id: plaque-granule-agent-matches-Q27003
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q27003/?page_size=200
  locator: All results; next is null
  accessed_at: '2026-11-03T08:56:56.329226Z'
  support: context_only
  summary: Complete integrated matches were inspected; these individual-family matches
    do not identify the aggregate GRA cargo or exported-effector cohort.
  snapshot_sha256: 523e3999008513c979d787768d1ed295135662690d308959c8acc3ecfdeabe18
- evidence_id: plaque-granule-agent-IPR008118
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008118/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-11-03T08:56:56.394749Z'
  support: supports
  summary: Gra2 protein is a specific family, not an exact grounding for the whole
    dense-granule cargo cohort.
  snapshot_sha256: e6e63144405f10b9cc7313f0fdc4806301bf642d16e8e3391a9919b3da1be685
- evidence_id: plaque-granule-agent-IPR008119
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008119/
  locator: Native InterPro metadata name/type, description and membership scope; predictive
    description provenance retained where marked
  accessed_at: '2026-11-03T08:56:56.562252Z'
  support: supports
  summary: Dense granule protein6/2 is a family entry for a subset of cargo, not the
    unrelated full GRA or exported-effector cohort.
  snapshot_sha256: 2ddf4eaa83d6dc7a9d0de341b9299784a55e841fd0b966aea5d526077d41ed02
- evidence_id: plaque-granule-agent-doi-10.1111_jeu.12904
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/jeu.12904
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:56.585732Z'
  support: supports
  summary: 'Native metadata identifies Dense granule biogenesis, secretion, and function
    in Toxoplasma gondii. Authors: Griffith MB, Pearce CS, Heaslip AT.; PMID 35302693;
    DOI 10.1111/jeu.12904. Bibliographic identity and available abstract only; not
    a substitute for inspected article body.'
  snapshot_sha256: deab13eca62c55b1cdbdff5590b100d2be74786a62b86faca60ae5aefcb396c6
- evidence_id: plaque-granule-agent-doi-10.1016_j.pt.2014.12.002
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.pt.2014.12.002
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:56.678556Z'
  support: supports
  summary: 'Native metadata identifies Toxoplasma secretory granules: one population
    or more? Authors: Mercier C, Cesbron-Delauw MF.; PMID 25599584; DOI 10.1016/j.pt.2014.12.002.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: bdb126dfd922e90f2316186dfac813bf65f131186f21dd8995fc0675c2f8521c
- evidence_id: plaque-granule-agent-doi-10.1016_j.ijpara.2005.03.011
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.ijpara.2005.03.011
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:56.679665Z'
  support: supports
  summary: Mercier2005 review abstract compares Plasmodium and Toxoplasma dense-granule
    systems and their variable PV adaptations. This supports qualitative cross-apicomplexan
    occurrence, not measured prevalence or identical cargo. Publisher body returned403
    and is not represented as inspected.
  snapshot_sha256: 307927676c236dd13ff837efd912a469ef2a2d11e46cba9ad2b1962d964f323f
- evidence_id: plaque-granule-agent-doi-10.1016_j.chom.2015.04.003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.chom.2015.04.003
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:57.012280Z'
  support: supports
  summary: 'Native metadata identifies The Toxoplasma Dense Granule Proteins GRA17
    and GRA23 Mediate the Movement of Small Molecules between the Host and the Parasitophorous
    Vacuole. Authors: Gold DA, Kaplan AD, Lis A, Bett GC, Rosowski EE, Cirelli KM,
    Bougdour A, Sidik SM, Beck JR, Lourido S, Egea PF, Bradley PJ, Hakimi MA, Rasmusson
    RL, Saeij JP.; PMID 25974303; DOI 10.1016/j.chom.2015.04.003. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 4e023c6f5dbe4604bcf121d7e2fff6128da96b64ed365d50e1b63f3985e75f24
- evidence_id: plaque-granule-agent-doi-10.1016_j.parint.2013.04.003
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.parint.2013.04.003
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:57.030473Z'
  support: supports
  summary: Masatani2013 primary abstract reports GRA23 immuno-EM localization in dense
    granules, PVM and intravacuolar network. Only abstract/bibliographic evidence
    is used.
  snapshot_sha256: 4279e454df394b4c7b96b1c9fbe989e3c7b224fcc5f8655b3a2c5e40befd4534
- evidence_id: plaque-granule-agent-doi-10.1016_j.chom.2013.03.002
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.chom.2013.03.002
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:57.101235Z'
  support: supports
  summary: Bougdour2013 primary abstract explicitly identifies GRA16 as dense-granule
    cargo exported across the PVM to the host nucleus, where it modulates host gene
    expression. This supports the new GRA16 edges at abstract scope; the complete
    primary body was not accessed.
  snapshot_sha256: b945b23e9a44480d899e0fddd240b8f7f2bc5d4ff86b03c0d5dcf162116a5943
- evidence_id: plaque-granule-agent-pmid-9208224
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9208224%20AND%20SRC%3AMED
  locator: 'Exact Europe PMC query: bibliographic identity, authors, DOI/PMID/PMCID
    and available abstract; no full-body inference from this endpoint.'
  accessed_at: '2026-11-03T08:56:57.205105Z'
  support: supports
  summary: 'Native metadata identifies Sequential protein secretion from three distinct
    organelles of Toxoplasma gondii accompanies invasion of human fibroblasts. Authors:
    Carruthers VB, Sibley LD.; PMID 9208224; DOI None. Bibliographic identity and
    available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: f6c9b29dd4f7787063b73d03098af65746123bee5598dbd927580c5a1ce4230b
- evidence_id: plaque-granule-agent-jats-PMC9482668
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC9482668.1/PMC9482668.1.xml
  locator: 'Secondary JATS review: §§S2–S8,S13,S18,S20,S21 direct paragraphs. No independent
    figures, supplements or full-proteome audit.'
  accessed_at: '2026-11-03T08:56:57.207320Z'
  support: supports
  summary: Griffith2022 supports dense-granule biogenesis, stored cargo, membrane
    boundary, secretion and later cargo functions. It separates stored transmembrane
    cargo from resident granule membrane proteins and distinguishes PVM permeability
    from effector export. Unresolved individual assembly requirements and incomplete
    resident-protein inventories are explicit.
  snapshot_sha256: c299f0194d8df4f3f95ed870283b1cc9212a3b8f7a39bfab4328c318d08a1b8c
- evidence_id: plaque-granule-agent-jats-PMC4435723
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4435723.1/PMC4435723.1.xml
  locator: 'Primary JATS: Results §§S3,S4,S6,S7,S8; Discussion S9; Methods S12,S14,S15,S16,S18;
    complete Table1. No independent figure-pixel or supplementary-data audit.'
  accessed_at: '2026-11-03T08:56:57.280626Z'
  support: supports
  summary: Gold2015 supports dense-granule/PVM localization, passive small-molecule
    permeability, unequal GRA17/GRA23 single-deletion phenotypes and synergistic growth
    requirements. RH/other experimental strain contexts and Xenopus oocyte assays
    remain scoped. Table1 names GT1 loci; it does not alone bridge the current ME49
    accessions. GRA17/23 protein-export effects and pore stoichiometry are not established;
    neither is organelle-assembly necessity.
  snapshot_sha256: e6f28f80777e2f2b3133f12e50371e7e9835d4ef70e2c409b7cb02ce88bda3d6
- evidence_id: plaque-granule-agent-pmc-PMC13475723
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13475723/
  locator: 'Primary HTML: Methods S3, Results S15–S18 and Discussion S19 direct paragraphs;
    no figure-pixel or other supplementary-data audit.'
  accessed_at: '2026-11-03T08:56:57.347590Z'
  support: supports
  summary: Carruthers/Sibley1997 RH tachyzoite/HFF experiments measure delayed GRA1/NTPase
    secretion after invasion, compared with earlier microneme/rhoptry secretion, while
    extracellular secretion remains possible. This supports timing in the stated model,
    not exclusive secretion after invasion or a universal apicomplexan rate.
  snapshot_sha256: 8f1cf522908b4eabe4a7d34b5e24264a1589755f9180d2b61a18ede8bacd3b60
- evidence_id: plaque-granule-agent-jats-PMC7202600
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC7202600.1/PMC7202600.1.xml
  locator: Primary JATS complete Table1 identity rows specifically TGME49_222170/GRA17
    and TGME49_297880/GRA23; bibliographic identity only.
  accessed_at: '2026-11-03T08:56:57.372069Z'
  support: supports
  summary: The published table bridges both exact ME49 locus identifiers to GRA17
    and GRA23. This is an identifier bridge, not an independent reassessment of that
    paper’s experimental findings or a transfer of GT1 phenotype data to ME49.
  snapshot_sha256: e6d90de8d0e521999bafd7a9252ffc16a6d8538e241e659aa2f8690306764ff4
- evidence_id: plaque-granule-agent-gene-7901472
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/7901472
  locator: Complete gene identity, locus_tag, organism and annotation fields
  accessed_at: '2026-11-03T08:56:57.373871Z'
  support: supports
  summary: NCBI Gene7901472 identifies the ME49 locus TGME49_297880 as dense granule
    protein DG32, taxon508771. This is the native locus bridge, not independent functional
    evidence.
  snapshot_sha256: d81dffa2bcb0b09b79c83aa5843312b37e47080c16bb3813c89f1ad75858af3a
- evidence_id: plaque-granule-membrane-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020026,GO:0030668,GO:0031090
  locator: Complete definitions, synonyms and relevant relations of all three native
    terms
  accessed_at: '2026-11-03T08:56:57.746179Z'
  support: supports
  summary: GO0030668 identifies the lipid bilayer surrounding an apicomplexan dense
    granule. GO0031090 is the broader organelle-membrane class; GO0020026 identifies
    the bounded secretory organelle.
  snapshot_sha256: d93916e4ebfb03cc1f9d6c567264d2af79d565945eeb574a85c7a792d8c7fb5f
- evidence_id: plaque-gra17-S8GTZ8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/S8GTZ8.json
  locator: Accession, unreviewed status, submitted protein name, TGME49_222170 ORF
    name, ME49 taxon508771, reference and GeneID/RefSeq links
  accessed_at: '2026-11-03T08:56:57.941747Z'
  support: supports
  summary: S8GTZ8 is an unreviewed ME49 dense-granule-antigen DG32 entry with ORF
    TGME49_222170. The source does not experimentally establish GRA17 function or
    localization; exact GRA17 linkage comes from the independently read primary Table1.
  snapshot_sha256: ecd0cd93b0cab590dffb8aa715e90f2f2f9f1176da2a03903d85e57ff0b1cc28
- evidence_id: plaque-gra17-gene
  kind: database
  reference: https://api.ncbi.nlm.nih.gov/datasets/v2/gene/id/7895641
  locator: reports[0].gene identity, locus_tag, tax_id, taxname, description and annotation
  accessed_at: '2026-11-03T08:58:01.482327Z'
  support: supports
  summary: NCBI Gene7895641 verifies the ME49 TGME49_222170 locus and DG32 annotation.
    This cross-check is identity evidence only.
  snapshot_sha256: 2235d733f5eda384718d9e5f0b14c4e098004a706cb87b14fcfa97dfb8115193
- evidence_id: plaque-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: 'Entire native /api/datasets response: all20 organism rows and dataset
    keys; no pagination'
  accessed_at: '2026-11-03T08:58:01.482117Z'
  support: supports
  summary: Fresh catalogue has no Agrobacterium tumefaciens or Toxoplasma gondii organism/dataset.
    Broad Bacteria/Eukaryota distribution does not authorize substituting a different
    organism for hppA or GRA accessions. No matched gene/module query applies; catalogue
    absence is not biological absence.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
- evidence_id: plaque-gra17-matches
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/S8GTZ8/?page_size=200
  locator: Exact accession InterPro endpoint attempt; HTTP204 plus curl92 malformed-header
    transport failure and empty response
  accessed_at: '2026-11-03T08:58:01.482425Z'
  support: context_only
  summary: Inconclusive endpoint response; no assertion of zero families, absence
    of a gene or absence of biological function.
  search_scope: InterPro exact accession query https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/S8GTZ8/?page_size=200;
    requested page_size=200 on 2026-11-03T08:58:01.482425+00:00; no readable results
    or next-page field obtained. Transport failure prevents an absence inference;
    no whole-database family search claimed.
  snapshot_sha256: 3fdc071e633a8f639f35b53c93522cea10e6a9edcb7c7c267d43fa5973ac9a90
- evidence_id: plaque-gra23-matches
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A0A125YME4/?page_size=200
  locator: Exact accession InterPro endpoint attempt; HTTP204 plus curl92 malformed-header
    transport failure and empty response
  accessed_at: '2026-11-03T08:58:01.482478Z'
  support: context_only
  summary: Inconclusive endpoint response; no assertion of zero families, absence
    of a gene or absence of biological function.
  search_scope: InterPro exact accession query https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/A0A125YME4/?page_size=200;
    requested page_size=200 on 2026-11-03T08:58:01.482478+00:00; no readable results
    or next-page field obtained. Transport failure prevents an absence inference;
    no whole-database family search claimed.
  snapshot_sha256: 54de8a9e8938c3a9875ab118cdccdef31ce1c4557915253b8a8dedd4acb788bb
- evidence_id: plaque-gra1-matches
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13403/?page_size=200
  locator: Exact accession InterPro endpoint attempt; HTTP204 plus curl92 malformed-header
    transport failure and empty response
  accessed_at: '2026-11-03T08:58:01.484362Z'
  support: context_only
  summary: Inconclusive endpoint response; no assertion of zero families, absence
    of a gene or absence of biological function.
  search_scope: InterPro exact accession query https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P13403/?page_size=200;
    requested page_size=200 on 2026-11-03T08:58:01.484362+00:00; no readable results
    or next-page field obtained. Transport failure prevents an absence inference;
    no whole-database family search claimed.
  snapshot_sha256: 7d84316c8940709aedb7a107b32c37c2d982ff2324a6dbecd6bfa678f7fd3a59
- evidence_id: plaque-historical-runner
  kind: validation
  reference: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  locator: Historical receipt and stdout/stderr independently reread and hash-verified;
    execution occurred00:49Z, not during this subreview
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  summary: Historical runner exited1 before dataset execution because of OS PermissionError
    reading pyvenv.cfg. It remains unavailable historical context; current source
    catalogue fallback is separately fetched. No current adapter-run success is claimed.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
- evidence_id: plaque-native-acidocalcisome_lumen-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    --verify
  locator: Actual root-owned acidocalcisome_lumen-uniprot-verify-receipt.json and
    exact stdout log independently read/hash-verified
  accessed_at: '2026-11-03T08:54:29.146478Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-acidocalcisome_lumen-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    --causal-graphs
  locator: Actual root-owned acidocalcisome_lumen-uniprot-causal-receipt.json and
    exact stdout log independently read/hash-verified
  accessed_at: '2026-11-03T08:54:29.548762Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: plaque-native-acidocalcisome_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --verify
  locator: Actual root-owned acidocalcisome_membrane-uniprot-verify-receipt.json and
    exact stdout log independently read/hash-verified
  accessed_at: '2026-11-03T08:54:30.943735Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-acidocalcisome_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --causal-graphs
  locator: Actual root-owned acidocalcisome_membrane-uniprot-causal-receipt.json and
    exact stdout log independently read/hash-verified
  accessed_at: '2026-11-03T08:54:31.344041Z'
  support: supports
  summary: "data/structures/membrane_organelle/acidocalcisome_membrane.yaml  (GO:0033102)\n\
    \  acidocalcisome_membrane_ion_transport\tproton_pumps\tCOVERED\t->proton_pumps\
    \ (UniProtKB:Q8VPZ0)\n  acidocalcisome_membrane_ion_transport\tcation_transporters\t\
    NO_GENE_SYMBOLS\t->cation_transporters (PROTEIN: acidocalcisome cation transporters)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     1  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 9ee7586c32edeb60c028f9b3d6ae18cc8ebb9161459bf05d7ec9d98858e771e7
- evidence_id: plaque-native-apicomplexan_dense_granule-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --verify
  locator: Actual root-owned apicomplexan_dense_granule-uniprot-verify-receipt.json
    and exact stdout log independently read/hash-verified
  accessed_at: '2026-11-03T08:54:36.858574Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-apicomplexan_dense_granule-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule.yaml
    --causal-graphs
  locator: Actual root-owned apicomplexan_dense_granule-uniprot-causal-receipt.json
    and exact stdout log independently read/hash-verified
  accessed_at: '2026-11-03T08:54:37.308697Z'
  support: supports
  summary: "data/structures/membrane_organelle/apicomplexan_dense_granule.yaml  (GO:0020026)\n\
    \  dense_granule_cargo_pvm_permeability\tdense_granule_proteins\tCOVERED\t->dense_granule_proteins\
    \ (UniProtKB:P13403, UniProtKB:P13404, UniProtKB:Q27003)\n  dense_granule_cargo_pvm_permeability\t\
    gra17_gra23_permeability_factors\tCOVERED\t->gra17_gra23_permeability_factors\
    \ (UniProtKB:A0A125YME4, UniProtKB:S8GTZ8)\n  dense_granule_cargo_pvm_permeability\t\
    exported_dense_granule_effectors\tNO_GENE_SYMBOLS\t->exported_dense_granule_effectors\
    \ (PROTEIN: exported dense granule effectors)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     2  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     1  NO_GENE_SYMBOLS    \
    \       component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 02d0baad111412a4137b86dadc6050d7bc90bc7441214c20158805aae30e98d4
- evidence_id: plaque-native-apicomplexan_dense_granule_membrane-verify
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --verify
  locator: Actual root-owned apicomplexan_dense_granule_membrane-uniprot-verify-receipt.json
    and exact stdout log independently read/hash-verified
  accessed_at: '2026-11-03T08:54:37.741497Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: plaque-native-apicomplexan_dense_granule_membrane-causal
  kind: validation
  reference: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicomplexan_dense_granule_membrane.yaml
    --causal-graphs
  locator: Actual root-owned apicomplexan_dense_granule_membrane-uniprot-causal-receipt.json
    and exact stdout log independently read/hash-verified
  accessed_at: '2026-11-03T08:54:38.162285Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: micro-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Evidence Rules; Structured Source Cross-Checks; Output
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: Native read-only claim-scoped review; named genes/proteins/stress claims
    trigger structured-source applicability before downstream matching. A missing
    expression claim is not an exemption.
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  support: supports
- evidence_id: micro-review-config
  kind: authority
  reference: conf/record_review.yaml
  locator: version1 skills and rubrics
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: The frozen configuration and all17 common policy/schema/verifier files
    are byte-identical to the prior independently read cohort; config, review skill
    and profile were freshly reread. No unknown local dependency was silently adopted.
  snapshot_sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
  support: supports
- evidence_id: micro-presence-enum
  kind: authority
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: PresenceEnum.COMMON
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: COMMON means occurrence in most taxon members, not numerous organelles
    in a cell.
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  support: supports
- evidence_id: micro-original-validation-inputs
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/adversary-microtubule/original-validation-inputs.json
  locator: 'All3 original bundles: native validate and render --content; original
    source blob/current hash comparison'
  accessed_at: '2026-11-03T08:55:11.145588Z'
  summary: All three validate and deterministic Markdown comparisons pass. PSG and
    extrusome hashes differ from their original frozen inputs; PAC is unchanged. This
    proves historical artifact integrity, not current scientific sufficiency.
  snapshot_sha256: c6d46b7ed875484896aae567d5b8c3a590ea72edf854e734535f3dfc503dfbad
  support: supports
- evidence_id: micro-record-proteasome_storage_granule
  kind: record_content
  reference: data/structures/inclusion/proteasome_storage_granule.yaml
  locator: Entire current YAML including components, causal graphs, discussions, evidence
    and history
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: Current source record independently read; SHA256 c905148a1f69e6dbcdca6de2e92701f51186b790ade37268bd009786a08b49d0.
    Original frozen input e09339d5bc79d9ee31b2e5e342b82a67992e86fc4d2fd16559791fefa46121af;
    stale=True.
  snapshot_sha256: c905148a1f69e6dbcdca6de2e92701f51186b790ade37268bd009786a08b49d0
  support: supports
- evidence_id: micro-prior-proteasome_storage_granule
  kind: prior_review
  reference: reviews/structured/20261021T104739Z-proteasome-storage-granule-audit/review.yaml
  locator: Entire original structured review and native rendered Markdown; checks,
    assessments, verdict, findings/actions and frozen inputs
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: Preserved historical observation 20261021T104739Z-proteasome-storage-granule-audit;
    original verdict pass_with_limitations. The original stable finding is retained
    only where present; clean original verdict does not certify a changed record.
  snapshot_sha256: db51f766110e6156276e23d8cf924755b2a50ed59d87e8be08042756377c629c
  support: supports
- evidence_id: micro-native-proteasome_storage_granule-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/proteasome_storage_granule-uniprot-verify-receipt.json
  locator: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml
    --verify; adjacent log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T08:54:25.652089Z'
  summary: 'Actual current-source command returned0 at 2026-11-03T08:54:26.748129+00:00.
    Scope: 3 protein_examples; no GENE_OR_PROTEIN causal nodes. Identity/coverage
    checks do not establish localization, biological necessity, complete inventory
    or source support.'
  snapshot_sha256: b4f1413df0cd81f200bfe3de2aaca44ebfae78dcd346675bfbb98335b89e30aa
  support: supports
- evidence_id: micro-native-proteasome_storage_granule-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/proteasome_storage_granule-uniprot-causal-receipt.json
  locator: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/proteasome_storage_granule.yaml
    --causal-graphs; adjacent log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T08:54:26.779238Z'
  summary: 'Actual current-source command returned0 at 2026-11-03T08:54:27.172124+00:00.
    Scope: 0 GENE_OR_PROTEIN causal nodes. Identity/coverage checks do not establish
    localization, biological necessity, complete inventory or source support.'
  snapshot_sha256: 102acf4f3af2709943f1af847e67af6f93842e6aa023da9c8b165768532a4989
  support: supports
- evidence_id: micro-record-protein_aggregate_center
  kind: record_content
  reference: data/structures/inclusion/protein_aggregate_center.yaml
  locator: Entire current YAML including components, causal graphs, discussions, evidence
    and history
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: Current source record independently read; SHA256 c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b.
    Original frozen input c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b;
    stale=False.
  snapshot_sha256: c598bb2eae3dd31eb4ca363ddbea3b61ccdb85dd71ae8fc56385abd867ff4c9b
  support: supports
- evidence_id: micro-prior-protein_aggregate_center
  kind: prior_review
  reference: reviews/structured/20261021T104740Z-protein-aggregate-center-audit/review.yaml
  locator: Entire original structured review and native rendered Markdown; checks,
    assessments, verdict, findings/actions and frozen inputs
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: Preserved historical observation 20261021T104740Z-protein-aggregate-center-audit;
    original verdict pass_with_limitations. The original stable finding is retained
    only where present; clean original verdict does not certify a changed record.
  snapshot_sha256: 78d0d83b502947841a73324f940748fd9d90cd42b5a2477b6e7d16d9c69f5c7c
  support: supports
- evidence_id: micro-native-protein_aggregate_center-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/protein_aggregate_center-uniprot-verify-receipt.json
  locator: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml
    --verify; adjacent log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T08:54:27.202556Z'
  summary: 'Actual current-source command returned0 at 2026-11-03T08:54:28.328672+00:00.
    Scope: 3 protein_examples; no GENE_OR_PROTEIN causal nodes. Identity/coverage
    checks do not establish localization, biological necessity, complete inventory
    or source support.'
  snapshot_sha256: 53d7410dd92313d0e4f631e9e2520429adae731eae396687356a0c62afadee4e
  support: supports
- evidence_id: micro-native-protein_aggregate_center-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/protein_aggregate_center-uniprot-causal-receipt.json
  locator: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/protein_aggregate_center.yaml
    --causal-graphs; adjacent log SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  accessed_at: '2026-11-03T08:54:28.359459Z'
  summary: 'Actual current-source command returned0 at 2026-11-03T08:54:28.744398+00:00.
    Scope: 0 GENE_OR_PROTEIN causal nodes. Identity/coverage checks do not establish
    localization, biological necessity, complete inventory or source support.'
  snapshot_sha256: d69b16c082034f8823a9cb6b5a420b960a78a8394e5d89dc9515eaf3787372de
  support: supports
- evidence_id: micro-record-actinophryid_extrusome
  kind: record_content
  reference: data/structures/membrane_organelle/actinophryid_extrusome.yaml
  locator: Entire current YAML including components, causal graphs, discussions, evidence
    and history
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: Current source record independently read; SHA256 48d64d84e4dcd8ddfd271c19c1b259b2357e09ef92625ecfaa09e65c9b26bbe5.
    Original frozen input 4b0f4ea17353cf6db5e343ef4a88ddc1458185fdcb508b74ca4fa8685421d0ea;
    stale=True.
  snapshot_sha256: 48d64d84e4dcd8ddfd271c19c1b259b2357e09ef92625ecfaa09e65c9b26bbe5
  support: supports
- evidence_id: micro-prior-actinophryid_extrusome
  kind: prior_review
  reference: reviews/structured/20261021T104743Z-actinophryid-extrusome-audit/review.yaml
  locator: Entire original structured review and native rendered Markdown; checks,
    assessments, verdict, findings/actions and frozen inputs
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: Preserved historical observation 20261021T104743Z-actinophryid-extrusome-audit;
    original verdict needs_curation. The original stable finding is retained only
    where present; clean original verdict does not certify a changed record.
  snapshot_sha256: c942a77f51e9e5965e8e8dcfb61dd0e38ad2958d5f0c5cccdc82b787ef2a881d
  support: supports
- evidence_id: micro-native-actinophryid_extrusome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/actinophryid_extrusome-uniprot-verify-receipt.json
  locator: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --verify; adjacent log SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  accessed_at: '2026-11-03T08:54:31.375812Z'
  summary: 'Actual current-source command returned0 at 2026-11-03T08:54:31.749630+00:00.
    Scope: 0 protein_examples; no accession-bearing protein causal xref. Identity/coverage
    checks do not establish localization, biological necessity, complete inventory
    or source support.'
  snapshot_sha256: 9b08f5ebd702abd0e23223565b46070a99d21ae4fff88f1ef4c7e33e2ae25e07
  support: supports
- evidence_id: micro-native-actinophryid_extrusome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/actinophryid_extrusome-uniprot-causal-receipt.json
  locator: Command .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/actinophryid_extrusome.yaml
    --causal-graphs; adjacent log SHA256 261ce8f1199383b4ea3d3ab45e538eb12884ed3cbbd8544871b73a5fb8a2a4bf
  accessed_at: '2026-11-03T08:54:31.781087Z'
  summary: 'Actual current-source command returned0 at 2026-11-03T08:54:32.154161+00:00.
    Scope: 1 GENE_OR_PROTEIN node, anchored to GP40 component but NO_GENE_SYMBOLS;
    no protein_examples. Identity/coverage checks do not establish localization, biological
    necessity, complete inventory or source support.'
  snapshot_sha256: 5e56e467e6a948f5001a2d879c44207f0b6c0d66b00da92ce3006cc9b0050873
  support: supports
- evidence_id: micro-laporte2008
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.xml
  locator: Full main Introduction, Results/discussion, Methods and Figures1–5 captions;
    permissions; no supplementary panels/raw movies
  accessed_at: '2026-11-03T08:54:46.011497Z'
  summary: Yeast quiescent CP/RP foci and reporter colocalization, rapid nuclear return
    after refeeding, water control and cycloheximide context support the bounded PSG
    definition, parts and recovery graphs. Colocalization alone does not resolve active
    holoenzyme state.
  snapshot_sha256: fdb31b38a84b5b23ca9c704375068b54582e998b5bd92aedc88ebeaaea18b1d9
  support: supports
- evidence_id: micro-gu2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5597321.1/PMC5597321.1.xml
  locator: All Results/Discussion; Methods yeast strains/manual microscopy/proteomic
    analysis; all Figures1–8 captions. Introduction and automated-acquisition/dSTORM
    Methods were not read
  accessed_at: '2026-11-03T08:54:46.011763Z'
  summary: Blm10/Ubp6 and processed ubiquitin reporter observations support association.
    Crosslinked PSG enrichment and native lysate PAGE have distinct scopes; free ubiquitin
    is distinguished from UBI4 precursor and polyubiquitin cargo. Specific loss phenotypes
    are not universal structural necessity.
  snapshot_sha256: 065f844203d82efea45e3eb6a2135cc231dd0484ae6f7646801cd58ac9ccc0d4
  support: supports
- evidence_id: micro-tang2026
  kind: primary_source
  reference: https://pure.mpg.de/rest/items/item_3702910_1/component/file_3702923/content
  locator: 'Selected PDF physical pages1–4,9–13: graphical abstract, Summary, initial
    Results/Figure1, Figure5/6/7 captions, Discussion and first limitations page;
    not the entire35-page PDF'
  accessed_at: '2026-11-03T08:54:46.513812Z'
  summary: In situ cryo-ET supports inactive intact26S trimers and paracrystalline
    fibers under energy limitation, including cytoplasmic and nuclear arrangements.
    Purification destabilizes assemblies; transient partners remain unresolved. The
    record accurately distinguishes these data from earlier colocalization/lysate
    results; its older abstract-only wording describes prior curation scope.
  snapshot_sha256: b0b18cfb67343d26ad1630f02775cb843141169a5b70542d45ca86909718f7d2
  support: supports
- evidence_id: micro-psg-retraction
  kind: primary_source
  reference: https://elifesciences.org/articles/82988
  locator: Retraction notice for eLife34532; statement on manipulated/duplicated images
    and unreliable archived data
  accessed_at: '2026-11-03T08:54:46.527962Z'
  summary: Retraction of DOI10.7554/eLife.34532 justifies excluding it from positive
    PSG claims. The record added structured REFUTE evidence for that exclusion; this
    does not prove every biological proposition false or resolve a whole multi-target
    historical issue.
  snapshot_sha256: cde8850f87bb46a5b53fe113381672e8441f4a3ba4a66e33d25785d80b0c20c6
  support: supports
- evidence_id: micro-psg-commentary
  kind: authority
  reference: https://pubmed.ncbi.nlm.nih.gov/30204036/
  locator: PubMed30204036 abstract only; related commentary, not independent primary
    experiments
  accessed_at: '2026-11-03T08:54:46.797799Z'
  summary: The commentary reiterates the proteaphagy-protection claim tied to the
    retracted study. It is contextual exclusion evidence, not a positive source for
    record functions.
  snapshot_sha256: 74fb5626f9e1ca7034ef22fc22408eabcbd92218967b32b171e19f1e84b83b00
  support: context_only
- evidence_id: micro-boronat2023
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.xml
  locator: Full main Introduction, Results2.1–2.5, Discussion, Methods4.1–4.7, Conclusions;
    all Figure1–7 captions; no supplementary panel pixels/raw data
  accessed_at: '2026-11-03T08:54:46.011851Z'
  summary: W303/BY4741/972 reporter experiments distinguish37C PAC assembly, genotype/strain/time-specific
    persistence, Hsp104-dependent clearance, induction versus recovery CHX timing,
    and immunoblot-supported degradation from loss of fluorescent puncta.42C NuRs
    are a separate context.
  snapshot_sha256: 0d9e2ef9309ef2e4467b02c001c4919d47818a1423120307660a6fee775d7552
  support: supports
- evidence_id: micro-cabrera2020
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/32075773/
  locator: PubMed32075773 complete primary abstract only
  accessed_at: '2026-11-03T08:54:46.739040Z'
  summary: Fission-yeast PAC formation, chaperone involvement and refolding are supported
    at abstract scope. Hsp16/Mas5/Ssa2 are bounded follow-up leads; this abstract
    does not alone establish all protein localization or formation necessity. No2020
    full-body access is claimed.
  snapshot_sha256: ae60ab126752972ea58d48d5ad8235b73579e307269916b8b8ef825f185e5b1a
  support: supports
- evidence_id: micro-hausmann1982
  kind: primary_source
  reference: https://api.crossref.org/works/10.1002/cm.970020103
  locator: Publisher-deposited Crossref abstract only; DOI10.1002/cm.970020103
  accessed_at: '2026-11-03T08:55:56.572424Z'
  summary: The abstract directly describes expanding/fusing extrusomes providing membrane
    during funnel-pseudopod prey enclosure. It does not identify a molecular fusogen
    or specific ion-channel protein.
  snapshot_sha256: 23ee7d7ac2e25bb5b1335a60658c77d34dc17e5f8501b3624ec75b11a55f6a45
  support: supports
- evidence_id: micro-sakaguchi1998
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/BF01279469
  locator: Publisher Summary lines35–39 in saved browser extraction; subscription
    preview only
  accessed_at: '2026-11-03T09:00:56Z'
  summary: Summary supports axopodial extrusome abundance and adhesion in examined
    preparations; it does not quantify species-wide frequency. Full1998 paper was
    not read.
  snapshot_sha256: 248b2b498ba416688d71932aa2b67cedf169e94f75793cf828bbebbd13491365
  support: supports
- evidence_id: micro-sakaguchi2001
  kind: primary_source
  reference: https://pubmed.ncbi.nlm.nih.gov/11401035/
  locator: Primary abstract lines239–242 in saved browser extraction; PMID11401035/DOI10.1078/1434-4610-00041
  accessed_at: '2026-11-03T09:00:56Z'
  summary: Abstract directly places GP40 in extrusomes and reports adhesion/ingestion
    of GP40-coated beads. This supports the new component-anchored residence and adhesion
    edges, without assigning unreviewed sequence isoforms to the purified protein
    or proving organelle-formation necessity.
  snapshot_sha256: 248b2b498ba416688d71932aa2b67cedf169e94f75793cf828bbebbd13491365
  support: supports
- evidence_id: micro-kakuta2008
  kind: primary_source
  reference: https://da.lib.kobe-u.ac.jp/da/kernel/90000974/90000974.pdf
  locator: 'Author-manuscript PDF physical pages2–10: title, Summary, Introduction,
    Methods, Results and Discussion; no figure pixels/raw data'
  accessed_at: '2026-11-03T08:54:46.620353Z'
  summary: Brackish Actinophrys cultures, extracellular-calcium and pharmacological
    adhesion assays support context-limited roles. ConA and calcium-channel blocker
    effects do not identify GP40 as the unique drug target or establish a localized
    channel inventory; ionophore depletion was proposed, not demonstrated.
  snapshot_sha256: 0c19dae3cd4ee6f44d208a8e27d45a9589c96a8f91383b4c83c262c54efd3806
  support: supports
- evidence_id: micro-metadata-sakaguchi1998-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.1007/BF01279469
  locator: Exact DOI Crossref metadata
  accessed_at: '2026-11-03T08:54:47.447428Z'
  summary: Exact bibliographic identity checked; metadata availability is not full-body
    access.
  snapshot_sha256: 5beded05f133c2dbf26a5bbd3341275b4deef09c2c0ac37debdb01b5583e95be
  support: context_only
- evidence_id: micro-metadata-sakaguchi2001-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.1078/1434-4610-00041
  locator: Exact DOI Crossref metadata
  accessed_at: '2026-11-03T08:54:47.653842Z'
  summary: Exact bibliographic identity checked; metadata availability is not full-body
    access.
  snapshot_sha256: e9e3654bbfd162f5c1b8bfae02d6a87c5b70f78d40189d6dda2a5009d5131726
  support: context_only
- evidence_id: micro-metadata-kakuta-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.1016/j.ejop.2007.11.001
  locator: Exact DOI Crossref metadata
  accessed_at: '2026-11-03T08:54:47.409286Z'
  summary: Exact bibliographic identity checked; metadata availability is not full-body
    access.
  snapshot_sha256: b3ca47a8cd47f45c80555e4f4fb72e24a5ed520c833ce102b43861b28eb70ea4
  support: context_only
- evidence_id: micro-metadata-tang2026-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.1016/j.cell.2025.12.035
  locator: Exact DOI Crossref metadata
  accessed_at: '2026-11-03T08:54:47.701893Z'
  summary: Exact bibliographic identity checked; metadata availability is not full-body
    access.
  snapshot_sha256: e7eb34022e4ad7272aa7548b9898a6f1e5f64487816859e304ecd265646a83fc
  support: context_only
- evidence_id: micro-metadata-retracted2018-crossref
  kind: authority
  reference: https://api.crossref.org/works/10.7554/eLife.34532
  locator: Exact DOI Crossref metadata
  accessed_at: '2026-11-03T08:54:47.777585Z'
  summary: Exact bibliographic identity checked; metadata availability is not full-body
    access.
  snapshot_sha256: 10c074f76b44ec82e2fd8cb3f15a9fcff9b528633eff5a8363b3541f2eed9303
  support: context_only
- evidence_id: micro-go-terms
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034515,GO:0043232,GO:0005737,GO:0005839,GO:0005838,GO:0140453,GO:0020020,GO:0030141,GO:0043231
  locator: QuickGO exact retrieval of9 named GO cellular-component terms; labels,
    active status and definitions
  accessed_at: '2026-11-03T08:54:47.031259Z'
  summary: PSG0034515 and PAC0140453 are exact active identities; parent0043232, cytoplasm5737
    and proteasome parts5839/5838 are appropriate.0043231 is a broad extrusome parent;0030141
    requires Golgi origin, and0020020 has parasite-food-vacuole scope, so neither
    is adopted as exact extrusome/food-vacuole identity.
  snapshot_sha256: 2e8111e98d7ba14158160238c3f5ac3701998c1e785a46ed35f46b1588d87987
  support: supports
- evidence_id: micro-extrusome-go-search
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&queryFields=label,synonym&rows=100&q=actinophryid%20extrusome
  locator: 'OLS4 GO search response: numFound0'
  accessed_at: '2026-11-03T08:54:47.163451Z'
  summary: No exact label/synonym result in this bounded query; it does not prove
    that all possible GO phrasings are absent.
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: 'OLS4 GO, 2026-11-03: q=actinophryid extrusome; exact=true; queryFields=label,synonym;
    rows=100; one response, numFound=0. No synonym expansion or ontology-wide semantic
    absence claim.'
  support: supports
- evidence_id: micro-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage
  accessed_at: '2026-11-03T08:54:47.906461Z'
  summary: Exact organism identity checked. Species4932/4896 and Actinophrys238771
    are distinguished from reference strain559292; authority identity does not show
    taxon-wide organelle occurrence.
  snapshot_sha256: d930c884e1154be4c050977652c0d6baf3666d183a90fa17ead8d01cce2c770f
  support: supports
- evidence_id: micro-tax-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage
  accessed_at: '2026-11-03T08:54:47.937562Z'
  summary: Exact organism identity checked. Species4932/4896 and Actinophrys238771
    are distinguished from reference strain559292; authority identity does not show
    taxon-wide organelle occurrence.
  snapshot_sha256: cdb53b3f4ab5e6bb4476de3bf0db333ae647e307a9fa8f98108827f98fe7f4d3
  support: supports
- evidence_id: micro-tax-559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage
  accessed_at: '2026-11-03T08:54:48.047086Z'
  summary: Exact organism identity checked. Species4932/4896 and Actinophrys238771
    are distinguished from reference strain559292; authority identity does not show
    taxon-wide organelle occurrence.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
  support: supports
- evidence_id: micro-tax-238771
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/238771
  locator: ENA taxonomy exact taxId/scientificName/rank/lineage
  accessed_at: '2026-11-03T08:54:48.107251Z'
  summary: Exact organism identity checked. Species4932/4896 and Actinophrys238771
    are distinguished from reference strain559292; authority identity does not show
    taxon-wide organelle occurrence.
  snapshot_sha256: d81416bf978839f22184692a1feed290335117e53f48d80b7360811fddc030f6
  support: supports
- evidence_id: micro-uniprot-P43583
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P43583.json
  locator: UniProt entry status, name, gene, taxon and relevant processing features
  accessed_at: '2026-11-03T08:54:48.500074Z'
  summary: Current accession/gene/taxon checked. Reviewed S288C reference entries
    are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys
    direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome
    examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free
    ubiquitin as an entire precursor.
  snapshot_sha256: fff0ae0abd33c736a3fa6cdfac72d5ba8ea9aacc4f315bdd02b168f220b13a97
  support: supports
- evidence_id: micro-matches-P43583
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P43583/?page_size=200
  locator: InterPro integrated entry matches for the exact protein; returned count,
    names and types
  accessed_at: '2026-11-03T08:54:48.515848Z'
  summary: Exact membership checked separately from grounding suitability. A domain
    or broad family match does not establish a specific structure component identity
    or localized functional isoform.
  snapshot_sha256: af48ff95cae271a6befc0c0d70f0c641789af1951ffadb7b6e163059e1212c88
  support: supports
- evidence_id: micro-uniprot-P43593
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P43593.json
  locator: UniProt entry status, name, gene, taxon and relevant processing features
  accessed_at: '2026-11-03T08:54:48.660739Z'
  summary: Current accession/gene/taxon checked. Reviewed S288C reference entries
    are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys
    direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome
    examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free
    ubiquitin as an entire precursor.
  snapshot_sha256: 9b33a9a6fa866ed3baf1243cc28f84adfb6659b658057773871fda6202ff14ac
  support: supports
- evidence_id: micro-matches-P43593
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P43593/?page_size=200
  locator: InterPro integrated entry matches for the exact protein; returned count,
    names and types
  accessed_at: '2026-11-03T08:54:48.706930Z'
  summary: Exact membership checked separately from grounding suitability. A domain
    or broad family match does not establish a specific structure component identity
    or localized functional isoform.
  snapshot_sha256: 5f73c565ef0fb334e0bddaf3e66c2710c19c6745f24de5d5fc2e63706a55d9b5
  support: supports
- evidence_id: micro-uniprot-P0CG63
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0CG63.json
  locator: UniProt entry status, name, gene, taxon and relevant processing features
  accessed_at: '2026-11-03T08:54:49.757657Z'
  summary: Current accession/gene/taxon checked. Reviewed S288C reference entries
    are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys
    direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome
    examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free
    ubiquitin as an entire precursor.
  snapshot_sha256: b0987c6267a3608e544fac75e771b2f931b95c2cac977b2dd206806fcce863bb
  support: supports
- evidence_id: micro-matches-P0CG63
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0CG63/?page_size=200
  locator: InterPro integrated entry matches for the exact protein; returned count,
    names and types
  accessed_at: '2026-11-03T08:54:49.890811Z'
  summary: Exact membership checked separately from grounding suitability. A domain
    or broad family match does not establish a specific structure component identity
    or localized functional isoform.
  snapshot_sha256: 279adb4f854a9497dc9f3d8d8a22be5c24c9f96460e1e6cbc8175f97c4dcb615
  support: supports
- evidence_id: micro-uniprot-Q12329
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q12329.json
  locator: UniProt entry status, name, gene, taxon and relevant processing features
  accessed_at: '2026-11-03T08:54:50.126029Z'
  summary: Current accession/gene/taxon checked. Reviewed S288C reference entries
    are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys
    direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome
    examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free
    ubiquitin as an entire precursor.
  snapshot_sha256: 2fd80fe65790b403d51e6d01659e4c94ec91a1455e5b4be00301e2350656a1cc
  support: supports
- evidence_id: micro-matches-Q12329
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q12329/?page_size=200
  locator: InterPro integrated entry matches for the exact protein; returned count,
    names and types
  accessed_at: '2026-11-03T08:54:50.342583Z'
  summary: Exact membership checked separately from grounding suitability. A domain
    or broad family match does not establish a specific structure component identity
    or localized functional isoform.
  snapshot_sha256: b5fd5350c5ea8e5ac5d6bdda8ab01a8f4ab0036d09974a5a02fce9361203a6a2
  support: supports
- evidence_id: micro-uniprot-P53286
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53286.json
  locator: UniProt entry status, name, gene, taxon and relevant processing features
  accessed_at: '2026-11-03T08:54:51.092402Z'
  summary: Current accession/gene/taxon checked. Reviewed S288C reference entries
    are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys
    direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome
    examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free
    ubiquitin as an entire precursor.
  snapshot_sha256: d0122a2554484d191dfb1e8f702aeaca61392ab658f762dbc30916c27580c110
  support: supports
- evidence_id: micro-matches-P53286
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P53286/?page_size=200
  locator: InterPro integrated entry matches for the exact protein; returned count,
    names and types
  accessed_at: '2026-11-03T08:54:51.119141Z'
  summary: Exact membership checked separately from grounding suitability. A domain
    or broad family match does not establish a specific structure component identity
    or localized functional isoform.
  snapshot_sha256: 2150123692223413fbe5ca58407117f0775384d53d6c3c9d16f7af500dbea6ab
  support: supports
- evidence_id: micro-uniprot-P31539
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P31539.json
  locator: UniProt entry status, name, gene, taxon and relevant processing features
  accessed_at: '2026-11-03T08:54:51.700293Z'
  summary: Current accession/gene/taxon checked. Reviewed S288C reference entries
    are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys
    direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome
    examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free
    ubiquitin as an entire precursor.
  snapshot_sha256: 8636decea760cdb2a2da238bfa589822867a778a41fd6a04c45a74fe5802ee13
  support: supports
- evidence_id: micro-matches-P31539
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P31539/?page_size=200
  locator: InterPro integrated entry matches for the exact protein; returned count,
    names and types
  accessed_at: '2026-11-03T08:54:52.005217Z'
  summary: Exact membership checked separately from grounding suitability. A domain
    or broad family match does not establish a specific structure component identity
    or localized functional isoform.
  snapshot_sha256: 750867aa538d4dd5c6c6a982138e7401b8b788d9653ecb84bf5d145c8ff6d3ee
  support: supports
- evidence_id: micro-uniprot-B2NIF0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/B2NIF0.json
  locator: UniProt entry status, name, gene, taxon and relevant processing features
  accessed_at: '2026-11-03T08:54:52.621207Z'
  summary: Current accession/gene/taxon checked. Reviewed S288C reference entries
    are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys
    direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome
    examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free
    ubiquitin as an entire precursor.
  snapshot_sha256: 89519e99dc7c08c3d797401a8cb7e4056afc4fe558a62d2f9d25904efa269b6f
  support: supports
- evidence_id: micro-matches-B2NIF0
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B2NIF0/?page_size=200
  locator: InterPro integrated entry matches for the exact protein; returned count,
    names and types
  accessed_at: '2026-11-03T08:54:53.120236Z'
  summary: Exact membership checked separately from grounding suitability. A domain
    or broad family match does not establish a specific structure component identity
    or localized functional isoform.
  snapshot_sha256: 303b28811f2395af46f74a4eb26f655cfb018abe1a42dc179fbd81c808a75c79
  support: supports
- evidence_id: micro-uniprot-B2NIF1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/B2NIF1.json
  locator: UniProt entry status, name, gene, taxon and relevant processing features
  accessed_at: '2026-11-03T08:54:53.267814Z'
  summary: Current accession/gene/taxon checked. Reviewed S288C reference entries
    are distinguished from experimental strains. B2NIF0/B2NIF1 are unreviewed Actinophrys
    direct-submission gp40-1/gp40-2 entries, not demonstrated isoform-specific extrusome
    examples. P0CG63 is a polyubiquitin precursor producing mature chains, not free
    ubiquitin as an entire precursor.
  snapshot_sha256: 527dea7c98d06606040a8141560bf03237c2e3ff4c6f434737a4ad7a070d7290
  support: supports
- evidence_id: micro-matches-B2NIF1
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B2NIF1/?page_size=200
  locator: InterPro integrated entry matches for the exact protein; returned count,
    names and types
  accessed_at: '2026-11-03T08:54:53.924501Z'
  summary: Exact membership checked separately from grounding suitability. A domain
    or broad family match does not establish a specific structure component identity
    or localized functional isoform.
  snapshot_sha256: a5b6e22df882dbb3241e4397bebf8f17bee67695f0f512d1c98eb529a99c959a
  support: supports
- evidence_id: micro-reviewed-BLM10
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABLM10&format=json&size=500
  locator: UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page
    link
  accessed_at: '2026-11-03T08:54:48.531519Z'
  summary: Bounded reviewed reference-strain gene query confirms the single declared
    accession without a synonym split; not a global ortholog inventory.
  snapshot_sha256: 37909aa74a91555ebc927dd72535340037f3cf7a138a655440e90688cf9389a9
  search_scope: 'UniProtKB,2026-11-03: reviewed:true AND organism_id:559292 AND gene_exact:BLM10;
    format=json,size=500; first response total1/returned1,no next link. Scope only
    this exact reference-strain gene, not related species or all homologs.'
  support: supports
- evidence_id: micro-reviewed-UBP6
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AUBP6&format=json&size=500
  locator: UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page
    link
  accessed_at: '2026-11-03T08:54:49.425163Z'
  summary: Bounded reviewed reference-strain gene query confirms the single declared
    accession without a synonym split; not a global ortholog inventory.
  snapshot_sha256: 64db4c5181db33ae8e6195822fdfd307b2292750684caccbfa137968a701fb57
  search_scope: 'UniProtKB,2026-11-03: reviewed:true AND organism_id:559292 AND gene_exact:UBP6;
    format=json,size=500; first response total1/returned1,no next link. Scope only
    this exact reference-strain gene, not related species or all homologs.'
  support: supports
- evidence_id: micro-reviewed-UBI4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AUBI4&format=json&size=500
  locator: UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page
    link
  accessed_at: '2026-11-03T08:54:50.105372Z'
  summary: Bounded reviewed reference-strain gene query confirms the single declared
    accession without a synonym split; not a global ortholog inventory.
  snapshot_sha256: 84ef4059b029713f1572bb9ebd365ba0d5b6969256641e059fa589f799aa82e5
  search_scope: 'UniProtKB,2026-11-03: reviewed:true AND organism_id:559292 AND gene_exact:UBI4;
    format=json,size=500; first response total1/returned1,no next link. Scope only
    this exact reference-strain gene, not related species or all homologs.'
  support: supports
- evidence_id: micro-reviewed-HSP42
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP42&format=json&size=500
  locator: UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page
    link
  accessed_at: '2026-11-03T08:54:50.942951Z'
  summary: Bounded reviewed reference-strain gene query confirms the single declared
    accession without a synonym split; not a global ortholog inventory.
  snapshot_sha256: f293170bb43d8482c94e6ef06e0447afe7d1dcb10ffa734d42c94920324e5ae4
  search_scope: 'UniProtKB,2026-11-03: reviewed:true AND organism_id:559292 AND gene_exact:HSP42;
    format=json,size=500; first response total1/returned1,no next link. Scope only
    this exact reference-strain gene, not related species or all homologs.'
  support: supports
- evidence_id: micro-reviewed-BTN2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3ABTN2&format=json&size=500
  locator: UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page
    link
  accessed_at: '2026-11-03T08:54:51.194030Z'
  summary: Bounded reviewed reference-strain gene query confirms the single declared
    accession without a synonym split; not a global ortholog inventory.
  snapshot_sha256: b2f4bdbd062bb47911a6c781f0eeb60f29e4558d1e1772e425012e87471f5159
  search_scope: 'UniProtKB,2026-11-03: reviewed:true AND organism_id:559292 AND gene_exact:BTN2;
    format=json,size=500; first response total1/returned1,no next link. Scope only
    this exact reference-strain gene, not related species or all homologs.'
  support: supports
- evidence_id: micro-reviewed-HSP104
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=reviewed%3Atrue+AND+organism_id%3A559292+AND+gene_exact%3AHSP104&format=json&size=500
  locator: UniProt search returns exactly1 reviewed entry; X-Total-Results1, no next-page
    link
  accessed_at: '2026-11-03T08:54:52.207285Z'
  summary: Bounded reviewed reference-strain gene query confirms the single declared
    accession without a synonym split; not a global ortholog inventory.
  snapshot_sha256: 4e2938a5a1292a9626b18e30b225ebfc7a30d63069235f01cd0bc3d007279322
  search_scope: 'UniProtKB,2026-11-03: reviewed:true AND organism_id:559292 AND gene_exact:HSP104;
    format=json,size=500; first response total1/returned1,no next link. Scope only
    this exact reference-strain gene, not related species or all homologs.'
  support: supports
- evidence_id: micro-entry-IPR035309
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035309/
  locator: Current entry accession, name, type, integrated signatures and scope
  accessed_at: '2026-11-03T08:54:53.971028Z'
  summary: Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp
    families and lectin domains are not promoted to unsupported exact component grounding.
    InterPro descriptions are authority context, not independent localization experiments.
  snapshot_sha256: fdbc1221b8adce63ab7091a28e6befcd142df6653ddc0033da5d1b453d400fef
  support: supports
- evidence_id: micro-entry-IPR044635
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044635/
  locator: Current entry accession, name, type, integrated signatures and scope
  accessed_at: '2026-11-03T08:54:54.019908Z'
  summary: Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp
    families and lectin domains are not promoted to unsupported exact component grounding.
    InterPro descriptions are authority context, not independent localization experiments.
  snapshot_sha256: 1caae0331f5173bdc4bc19b430fead937b0cc4116be2eca5e2108870ee351bef
  support: supports
- evidence_id: micro-entry-IPR050158
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050158/
  locator: Current entry accession, name, type, integrated signatures and scope
  accessed_at: '2026-11-03T08:54:54.556972Z'
  summary: Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp
    families and lectin domains are not promoted to unsupported exact component grounding.
    InterPro descriptions are authority context, not independent localization experiments.
  snapshot_sha256: 665d6b43cc1bedd8b45b2ba5fada2f4994418d081996b5f644c4b1c871733491
  support: supports
- evidence_id: micro-entry-IPR031107
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031107/
  locator: Current entry accession, name, type, integrated signatures and scope
  accessed_at: '2026-11-03T08:54:54.618741Z'
  summary: Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp
    families and lectin domains are not promoted to unsupported exact component grounding.
    InterPro descriptions are authority context, not independent localization experiments.
  snapshot_sha256: 7db6f5da4dd897dfbcaa6435cbeb744a4691f43cb10433977995a30bb1d91293
  support: supports
- evidence_id: micro-entry-IPR001270
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001270/
  locator: Current entry accession, name, type, integrated signatures and scope
  accessed_at: '2026-11-03T08:54:55.175580Z'
  summary: Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp
    families and lectin domains are not promoted to unsupported exact component grounding.
    InterPro descriptions are authority context, not independent localization experiments.
  snapshot_sha256: ed0a09c17fa611e58cd0d00b904d4dce2757228cd7e411301eddcfb9b391e0dd
  support: supports
- evidence_id: micro-entry-IPR050130
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050130/
  locator: Current entry accession, name, type, integrated signatures and scope
  accessed_at: '2026-11-03T08:54:55.206063Z'
  summary: Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp
    families and lectin domains are not promoted to unsupported exact component grounding.
    InterPro descriptions are authority context, not independent localization experiments.
  snapshot_sha256: e654bc8d2d359d203a225be0690247071616a63341156fcd507f197717f78701
  support: supports
- evidence_id: micro-entry-IPR000757
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000757/
  locator: Current entry accession, name, type, integrated signatures and scope
  accessed_at: '2026-11-03T08:54:55.294822Z'
  summary: Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp
    families and lectin domains are not promoted to unsupported exact component grounding.
    InterPro descriptions are authority context, not independent localization experiments.
  snapshot_sha256: 57b8272533921c9703879d38d4e62e9448412f969928ff6f3dd3031d7698c019
  support: supports
- evidence_id: micro-entry-IPR013320
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013320/
  locator: Current entry accession, name, type, integrated signatures and scope
  accessed_at: '2026-11-03T08:54:55.349089Z'
  summary: Entry type/scope checked against exact protein matches. Broad ubiquitin/Clp
    families and lectin domains are not promoted to unsupported exact component grounding.
    InterPro descriptions are authority context, not independent localization experiments.
  snapshot_sha256: 1a6d786fbc2d08458a4cafec72c3ce8f2a87b5a8e6369196333aab188899ca56
  support: supports
- evidence_id: micro-entry-IPR062150
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062150/
  locator: Current metadata after initial429; type=domain, BTN2-like N-terminal
  accessed_at: '2026-11-03T08:55:56.572902Z'
  summary: Successful retry confirms an N-terminal domain including BTN2-related proteins;
    the record appropriately keeps BTN2 label-only instead of treating this as an
    exact family.
  snapshot_sha256: 052706313e73f7f6ab7d3e132b810e14be2212db1662112174f4a522ed92fed1
  support: supports
- evidence_id: micro-deleted-IPR050546
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050546/
  locator: HTTP410 deleted-entry metadata; deletion_date2026-05-13
  accessed_at: '2026-11-03T08:55:56.573003Z'
  summary: Current deleted status confirms why the historical candidate is not usable
    grounding; the initial429 did not itself establish deletion.
  snapshot_sha256: 7b43a6c3facfb712608446516580f235ab94c0b0239442015a3394b2015e87b7
  support: context_only
- evidence_id: micro-pac-dataset
  kind: database
  reference: https://api.datacite.org/dois/10.17632/z3hvg9wtvg.2
  locator: DataCite metadata for exact version DOI10.17632/z3hvg9wtvg.2
  accessed_at: '2026-11-03T08:54:46.803939Z'
  summary: Margarita Cabrera, March21,2023 issuance and CC BY4.0 metadata verified.
    No raw files, content manifest or reanalysis inspected; this supports dataset
    provenance only.
  snapshot_sha256: 63433417e861604b5d15f61d207b47669e38e48be2a89d88284a66fdc19a3f02
  support: supports
- evidence_id: micro-psg-image
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/jcb1810737f02.jpg
  locator: Direct pixels of Laporte2008 Figure2; source caption in laporte2008; package
    media MD5a1a61298bd0533aa42ad5121b7f29e34
  accessed_at: '2026-11-03T08:54:46.011989Z'
  summary: Image shows paired proteasome reporter signals and merged foci plus time-course
    categories; scale2um. It supports depicted localization/colocalization only, not
    universal assembly state. It remains a link-only record image.
  snapshot_sha256: ceedede7c232a35e128bbd7a2771f6bbacfa073410611bc8bc50e0759a60977a
  support: supports
- evidence_id: micro-pac-image
  kind: record_content
  reference: data/images/inclusion/protein_aggregate_center/pmc10342647_ijms_24_11202_f002.jpg
  locator: Direct original pixels inspected; Figure2 source caption and PMC package
    MD5d43e6b98317eb43129ceb3af1a7d9b2b matched
  accessed_at: '2026-11-03T09:04:15.641986Z'
  summary: BY4741 Btn2/Hsp42/Hsp104 separate GFP rows show25C and37C15/30/60/120min
    observations, percentages and5um scale. Separate panels are not three-way colocalization
    or proof of necessity.
  snapshot_sha256: 7d9c957cdb378c0a51800a3890e66cf2d0d0b05d7596bf0e220e0224b374c6da
  support: supports
- evidence_id: micro-package-PMC2396804
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2396804.1/PMC2396804.1.json
  locator: PMC open-data package identity/media checksum/license metadata, crosschecked
    with source JATS permissions
  accessed_at: '2026-11-03T08:54:46.011910Z'
  summary: Figure bytes match package MD5; Laporte2008 is CC BY-NC-SA3.0, represented
    as OTHER with license text, and Boronat2023 is CC BY4.0. Package metadata and
    pixel inspection are distinct checks.
  snapshot_sha256: fa1dd566efaf7dd07ac9f73731bc445e96675fd58b3cc00384c4206a22677acc
  support: supports
- evidence_id: micro-package-PMC10342647
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10342647.1/PMC10342647.1.json
  locator: PMC open-data package identity/media checksum/license metadata, crosschecked
    with source JATS permissions
  accessed_at: '2026-11-03T08:54:46.011953Z'
  summary: Figure bytes match package MD5; Laporte2008 is CC BY-NC-SA3.0, represented
    as OTHER with license text, and Boronat2023 is CC BY4.0. Package metadata and
    pixel inspection are distinct checks.
  snapshot_sha256: 3c1b51d3c79b6d45de60c44b57038bcd6baca139e8e531d549a36f570cf1eda5
  support: supports
- evidence_id: micro-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete returned iModulonDB dataset catalogue;20 organism rows,28 organism-dataset
    pairs,22 distinct literal dataset-name strings
  accessed_at: '2026-11-03T08:54:46.891536Z'
  summary: No listed Saccharomyces cerevisiae, Schizosaccharomyces pombe or Actinophrys
    sol organism key. Named proteins/stress/perturbation claims trigger applicability
    assessment, but no covered target organism permits downstream gene/module matching
    here. Catalogue absence is not negative biological evidence.
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  support: supports
- evidence_id: micro-historical-adapter-runner
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Retained actual00:49Z adapter invocation; command, error and status fields
  accessed_at: '2026-11-03T00:49:00.848907Z'
  summary: Earlier actual runner command returned1 because OS denied pyvenv.cfg access.
    This historical availability receipt is not a fresh invocation or a successful
    adapter run; current catalogue fallback was fetched independently.
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  support: supports
- evidence_id: septin-native-review-policy
  kind: authority
  reference: .claude/skills/review-yaml-record/SKILL.md
  locator: Structured Source Cross-Checks; native record-review process
  summary: Named genes, accessions or pathways trigger applicability assessment. Lack
    of an expression claim is not an exemption; unmatched organisms permit bounded
    downstream non-applicability. Native review-only mutation boundary and current
    input capture apply.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
  support: supports
- evidence_id: septin-native-curation-policy
  kind: authority
  reference: docs/CURATION.md
  locator: Components; essentiality; evidence scope
  summary: Component grounding is class-level, protein examples are taxon-specific,
    and essentiality concerns structure formation. Identity, localization, metabolic
    function and formation dependency require distinct support.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: supports
- evidence_id: septin-record-anammoxosome
  kind: record_content
  reference: data/structures/membrane_organelle/anammoxosome.yaml
  locator: Entire current record at e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4
  summary: Full maintained record, including history, identity, components, examples,
    taxonomic scope, functions, evidence, graph and TODOs; no tracked image is present.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: 50adeae38935dda1315b70ceec936b8224d4e6db33f07cd5caf60da96e95b1fa
  support: supports
- evidence_id: septin-original-anammoxosome
  kind: prior_review
  reference: reviews/structured/20261021T104744Z-anammoxosome-audit/review.yaml
  locator: Entire original YAML and deterministic Markdown; findings/actions retained
  summary: Original review at 20261021T104744Z-anammoxosome-audit; historical verdict
    needs_curation. This successor reassesses current content without overwriting
    the original.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: f7bf58ff4275f8d356cbbec870247f66368df856a869ff8fc0fbf5a31d686760
  support: supports
- evidence_id: septin-record-anammoxosome_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/anammoxosome_membrane.yaml
  locator: Entire current record at e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4
  summary: Full maintained record, including history, identity, components, examples,
    taxonomic scope, functions, evidence, graph and TODOs; no tracked image is present.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: 0a47b8cfa7bc71dcfc8cb69ba625087ce23025f9a1204b0fe578d185c2035f61
  support: supports
- evidence_id: septin-original-anammoxosome_membrane
  kind: prior_review
  reference: reviews/structured/20261021T104745Z-anammoxosome-membrane-audit/review.yaml
  locator: Entire original YAML and deterministic Markdown; findings/actions retained
  summary: Original review at 20261021T104745Z-anammoxosome-membrane-audit; historical
    verdict needs_curation. This successor reassesses current content without overwriting
    the original.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: b70be8aad6601ca4814aa5b88b02c824c06c7f7e26776f28073bed2795dc9209
  support: supports
- evidence_id: septin-record-apicoplast
  kind: record_content
  reference: data/structures/membrane_organelle/apicoplast.yaml
  locator: Entire current record at e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4
  summary: Full maintained record, including history, identity, components, examples,
    taxonomic scope, functions, evidence, graph and TODOs; no tracked image is present.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: 00971d8425f63fc5d490907a43c00b6760c2d88c5413fce6bdbc2dd09919410e
  support: supports
- evidence_id: septin-original-apicoplast
  kind: prior_review
  reference: reviews/structured/20261021T104747Z-apicoplast-audit/review.yaml
  locator: Entire original YAML and deterministic Markdown; findings/actions retained
  summary: Original review at 20261021T104747Z-apicoplast-audit; historical verdict
    needs_curation. This successor reassesses current content without overwriting
    the original.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: b63be1349a513ab07fd8e898e69383852dd8d539a6177f0dda4579ee298c216f
  support: supports
- evidence_id: septin-context-apicoplast-membrane
  kind: record_content
  reference: data/structures/membrane_organelle/apicoplast_membrane.yaml
  locator: 'Frozen neighbor: identity, parthood and membrane/whole-organelle boundary
    only'
  summary: GO:0160211 is the membrane constituent, part of GO:0020011; the whole-organelle
    record and membrane record remain distinct. This is not a full adjudication or
    resolution of the neighbor protein examples.
  accessed_at: '2026-11-03T09:06:21.010337Z'
  snapshot_sha256: fb3e343e0ed2a8711dff2305abea2166c589cb0a7b169d291c67fed81990ca58
  support: supports
- evidence_id: septin-root20-sources-anammoxosome-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043231,GO:0044222
  locator: 'QuickGO exact requested identifiers: names, definitions, obsolete status,
    aspect and returned relationships'
  summary: Exact current GO terms inspected; broader parent identity is kept distinct
    from the structure or its membrane constituent.
  accessed_at: '2026-11-03T08:55:08.339033Z'
  snapshot_sha256: 7c2c65b9f3f110753067d98ace76756125792c0ce7ad92f80dd0e51111f49fc3
  support: supports
- evidence_id: septin-root20-sources-NCBITaxon-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Taxon identity/lineage is verified. Corrected current Kuenenia spelling
    and historical synonym do not imply a different organism; native name conventions
    are not silently rewritten.
  accessed_at: '2026-11-03T08:55:08.339290Z'
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
  support: supports
- evidence_id: septin-root20-sources-NCBITaxon-203682
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/203682
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Taxon identity/lineage is verified. Corrected current Kuenenia spelling
    and historical synonym do not imply a different organism; native name conventions
    are not silently rewritten.
  accessed_at: '2026-11-03T08:55:08.339384Z'
  snapshot_sha256: cabea42376203d63ce418097cfad44d4856cead69ee9c0a09e8e1aa8e29d2e34
  support: supports
- evidence_id: septin-root20-sources-NCBITaxon-174633
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/174633
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Taxon identity/lineage is verified. Corrected current Kuenenia spelling
    and historical synonym do not imply a different organism; native name conventions
    are not silently rewritten.
  accessed_at: '2026-11-03T08:55:08.339435Z'
  snapshot_sha256: 38581b2b4068fae84ebbbe768dd6bb6cecb03825247f458077adf15dcf8d1236
  support: supports
- evidence_id: septin-root20-sources-doi-10.1111_1574-6976.12014
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/1574-6976.12014
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID23210799: Kartal B, de Almeida NM, Maalcke WJ, Op den Camp HJ, Jetten
    MS, Keltjens JT. (2013), How to make a living from anaerobic ammonium oxidation..
    Full publication body is not attested by this metadata/abstract response.'
  accessed_at: '2026-11-03T08:55:08.339512Z'
  snapshot_sha256: 831f716c924bd89ae6fca52cd6fb0d6613c5ffacf374ed262023e0a41bdf7a8d
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1111/1574-6976.12014;
    retrieved 2026-11-03T08:55:08.339512Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-root20-sources-doi-10.1128_JB.00186-15
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/JB.00186-15
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID25962914: de Almeida NM, Neumann S, Mesman RJ, Ferousi C, Keltjens
    JT, Jetten MS, Kartal B, van Niftrik L. (2015), Immunogold Localization of Key
    Metabolic Enzymes in the Anammoxosome and on the Tubule-Like Structures of Kuenenia
    stuttgartiensis.. Full publication body is not attested by this metadata/abstract
    response.'
  accessed_at: '2026-11-03T08:55:09.084060Z'
  snapshot_sha256: 67f2cacdf010153f05c6c23d74f8c48710cb6b55cd3dfec5bed875c7852b5f0d
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1128/JB.00186-15;
    retrieved 2026-11-03T08:55:09.084060Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-root20-sources-PMID-15098544
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15098544%20AND%20SRC%3AMED
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID15098544: van Niftrik LA, Fuerst JA, Sinninghe Damsté JS, Kuenen JG,
    Jetten MS, Strous M. (2004), The anammoxosome: an intracytoplasmic compartment
    in anammox bacteria.. Full publication body is not attested by this metadata/abstract
    response.'
  accessed_at: '2026-11-03T08:55:09.102948Z'
  snapshot_sha256: 3e14a653651c1f9fc37660cd57bca8966b40627bab708f0a40af54d084891eb6
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:15098544
    AND SRC:MED; retrieved 2026-11-03T08:55:09.102948Z; returned metadata/abstract
    scope only.
  support: supports
- evidence_id: septin-root20-sources-PMID-25962914
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A25962914%20AND%20SRC%3AMED
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID25962914: de Almeida NM, Neumann S, Mesman RJ, Ferousi C, Keltjens
    JT, Jetten MS, Kartal B, van Niftrik L. (2015), Immunogold Localization of Key
    Metabolic Enzymes in the Anammoxosome and on the Tubule-Like Structures of Kuenenia
    stuttgartiensis.. Full publication body is not attested by this metadata/abstract
    response.'
  accessed_at: '2026-11-03T08:55:09.145128Z'
  snapshot_sha256: ee212ad6a7dfca0423093b5e987c960defbf1e4eb238e920aef9b009581b550c
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:25962914
    AND SRC:MED; retrieved 2026-11-03T08:55:09.145128Z; returned metadata/abstract
    scope only.
  support: supports
- evidence_id: septin-root20-sources-PMID-12384695
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:12384695%20AND%20SRC:MED
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID12384695: Sinninghe Damsté JS, Strous M, Rijpstra WI, Hopmans EC,
    Geenevasen JA, van Duin AC, van Niftrik LA, Jetten MS. (2002), Linearly concatenated
    cyclobutane lipids form a dense bacterial membrane.. Full publication body is
    not attested by this metadata/abstract response.'
  accessed_at: '2026-11-03T08:55:09.145237Z'
  snapshot_sha256: f7011ae45b57c7ef445ef775a6cba0a71075de90f6c1b8d140eda757b87f5966
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:12384695
    AND SRC:MED; retrieved 2026-11-03T08:55:09.145237Z; returned metadata/abstract
    scope only.
  support: supports
- evidence_id: septin-root20-sources-legacy-PMC4524196
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4524196/
  locator: 'de Almeida et al. 2015: Introduction equations 1–4, Fig.1 caption, Results
    localization sections and Discussion; body text inspected, no figure pixels/raw
    image quantification'
  summary: The paper distinguishes HZS, HDH/kustc0694, HOX/kustc1061 and an HAO-like
    pair of unknown function. Hydrazine oxidation supplies electrons to reductive
    steps. All five localized complexes are soluble inside the anammoxosome; membrane-carrier
    localization and organelle-assembly requirements were not measured.
  accessed_at: '2026-11-03T08:55:09.723352Z'
  snapshot_sha256: 858f58c2bc82af064b21c2c190a601e4b039b7eb849816aa97779447fff8d033
  support: supports
- evidence_id: septin-root20-sources-UniProtKB-A0A2C9CHN2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A2C9CHN2.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'A0A2C9CHN2: UniProtKB unreviewed (TrEMBL); taxon 174633; native gene/ORF
    values hzsA_1, hzsA_2, KSMBR1_2713, KSMBR1_3603. Identity/status metadata does
    not alone establish organelle membership.'
  accessed_at: '2026-11-03T08:55:09.773446Z'
  snapshot_sha256: 56b9bbb3155f41d63e98a3a9ae77ee2542a033630b76851f04bab5493e66bf17
  support: supports
- evidence_id: septin-root20-sources-UniProtKB-A0A2C9CH14
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A2C9CH14.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'A0A2C9CH14: UniProtKB unreviewed (TrEMBL); taxon 174633; native gene/ORF
    values hzsB_1, hzsB_2, hzsB_3, KSMBR1_2704, KSMBR1_2712, KSMBR1_3602. Identity/status
    metadata does not alone establish organelle membership.'
  accessed_at: '2026-11-03T08:55:09.787280Z'
  snapshot_sha256: bb24d7e8c20f155aad3d97da2b4f67b47448a56cd4809a9cc5cde8ce9737b3a0
  support: supports
- evidence_id: septin-root20-sources-UniProtKB-A0A2C9CHM2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0A2C9CHM2.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'A0A2C9CHM2: UniProtKB unreviewed (TrEMBL); taxon 174633; native gene/ORF
    values hzsC_3, hzsC_1, hzsC_2, KSMBR1_2703, KSMBR1_2711, KSMBR1_3601. Identity/status
    metadata does not alone establish organelle membership.'
  accessed_at: '2026-11-03T08:55:09.826355Z'
  snapshot_sha256: 19f041db73b906d2675a21c482395e1eee238fea795a9aa84a6ef64a6cfaa61c
  support: supports
- evidence_id: septin-root20-sources-UniProtKB-Q1PX48
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q1PX48.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Q1PX48: UniProtKB reviewed (Swiss-Prot); taxon 174633; native gene/ORF
    values hao, hao_3, hox, H3C64_04740, KsCSTR_43280, KSMBR1_2670, kustc1061. Identity/status
    metadata does not alone establish organelle membership. Reviewed functional annotation
    identifies hydroxylamine-to-NO activity and qualifies slower hydrazine oxidation
    as probably nonphysiological; hao/hox/kustc1061 is distinct from HDH.'
  accessed_at: '2026-11-03T08:55:10.181207Z'
  snapshot_sha256: f754ee5d44fe712d2fd40180f5b38e0ec07e5236865c4907b7c261084f644a5c
  support: supports
- evidence_id: septin-root20-sources-UniProtKB-Q1PYC5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q1PYC5.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Q1PYC5: UniProtKB unreviewed (TrEMBL); taxon 174633; native gene/ORF values
    hdh, KSMBR1_1220. Identity/status metadata does not alone establish organelle
    membership.'
  accessed_at: '2026-11-03T08:55:10.387452Z'
  snapshot_sha256: dc4a0d31043811cf18b0dd452d1487a507861c799805522fc17152a0a5a8a3ac
  support: supports
- evidence_id: septin-root20-sources-query-hzsA_1-174633
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AhzsA_1%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 0 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:10.411528Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProtKB REST search; query=['(gene_exact:hzsA_1) AND (taxonomy_id:174633)
    AND (reviewed:true)']; size=['500']; retrieved 2026-11-03T08:55:10.411528Z; one
    explicit response page, no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-root20-sources-query-hzsB_1-174633
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AhzsB_1%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 0 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:11.080865Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProtKB REST search; query=['(gene_exact:hzsB_1) AND (taxonomy_id:174633)
    AND (reviewed:true)']; size=['500']; retrieved 2026-11-03T08:55:11.080865Z; one
    explicit response page, no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-root20-sources-query-hzsC_3-174633
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AhzsC_3%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 0 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:11.165142Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProtKB REST search; query=['(gene_exact:hzsC_3) AND (taxonomy_id:174633)
    AND (reviewed:true)']; size=['500']; retrieved 2026-11-03T08:55:11.165142Z; one
    explicit response page, no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-root20-sources-query-hao-174633
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3Ahao%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 1 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:11.993357Z'
  snapshot_sha256: b65949b6e08dafd96f8f1120c2338f60269aecb24b552ceb1b762074273e757f
  search_scope: UniProtKB REST search; query=['(gene_exact:hao) AND (taxonomy_id:174633)
    AND (reviewed:true)']; size=['500']; retrieved 2026-11-03T08:55:11.993357Z; one
    explicit response page, no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-root20-sources-query-hdh-174633
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3Ahdh%29%20AND%20%28taxonomy_id%3A174633%29%20AND%20%28reviewed%3Atrue%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 0 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:12.239707Z'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
  search_scope: UniProtKB REST search; query=['(gene_exact:hdh) AND (taxonomy_id:174633)
    AND (reviewed:true)']; size=['500']; retrieved 2026-11-03T08:55:12.239707Z; one
    explicit response page, no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-root20-sources-anammox-membrane-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0016020,GO:0044222
  locator: 'QuickGO exact requested identifiers: names, definitions, obsolete status,
    aspect and returned relationships'
  summary: Exact current GO terms inspected; broader parent identity is kept distinct
    from the structure or its membrane constituent.
  accessed_at: '2026-11-03T08:55:12.963298Z'
  snapshot_sha256: 44f5cfe5d9cb0a69359c0d8a622f5f9804694212486e8d498ceb7fe9bf40f9e2
  support: supports
- evidence_id: septin-root20-sources-ols-exact-anammoxosome-membrane
  kind: search
  reference: https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&queryFields=label,synonym&rows=100&q=anammoxosome%20membrane
  locator: Complete exact GO name lookup response
  summary: The bounded exact anammoxosome membrane name query returned no exact GO
    term; GO membrane remains a broader parent, not identity. No claim of exhaustive
    ontology absence.
  accessed_at: '2026-11-03T08:55:13.325147Z'
  snapshot_sha256: 8d33fdeb26a2d16294a3c5f4a7f444578bb462aa6036d45a15e9bfadfe47fbd2
  search_scope: OLS search at https://www.ebi.ac.uk/ols4/api/search?ontology=go&exact=true&queryFields=label,synonym&rows=100&q=anammoxosome%20membrane;
    exact query and ontology constraints as encoded; retrieved 2026-11-03T08:55:13.325147Z;
    returned response inspected, not a broad semantic synonym search.
  support: supports
- evidence_id: septin-apicoplast-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009536,GO:0020011,GO:0160211
  locator: 'QuickGO exact requested identifiers: names, definitions, obsolete status,
    aspect and returned relationships'
  summary: Exact current GO terms inspected; broader parent identity is kept distinct
    from the structure or its membrane constituent.
  accessed_at: '2026-11-03T08:55:13.553249Z'
  snapshot_sha256: b69177f751226895a3c7fd524367d90cd42d221c35107cbbbb4594cc53be6bca
  support: supports
- evidence_id: septin-apicoplast-agent-tax-5794
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Taxon identity/lineage is verified. Corrected current Kuenenia spelling
    and historical synonym do not imply a different organism; native name conventions
    are not silently rewritten.
  accessed_at: '2026-11-03T08:55:13.959999Z'
  snapshot_sha256: 617b42c27ae95a801b69abf63e1a545eff8565fd0af2f4a81be359d3fb6b3cbf
  support: supports
- evidence_id: septin-apicoplast-agent-tax-5811
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Taxon identity/lineage is verified. Corrected current Kuenenia spelling
    and historical synonym do not imply a different organism; native name conventions
    are not silently rewritten.
  accessed_at: '2026-11-03T08:55:14.075206Z'
  snapshot_sha256: cbb209002c87051ce78d0a34bc169d2f6623f6bbfbb21edad170d43eb16d4032
  support: supports
- evidence_id: septin-apicoplast-agent-tax-5833
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Taxon identity/lineage is verified. Corrected current Kuenenia spelling
    and historical synonym do not imply a different organism; native name conventions
    are not silently rewritten.
  accessed_at: '2026-11-03T08:55:14.170990Z'
  snapshot_sha256: 47c9da135299ea0515b9cbddde80166e0e7256bcf1daac4cdf87f8ae3e0ecd11
  support: supports
- evidence_id: septin-apicoplast-agent-tax-508771
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/508771
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Taxon identity/lineage is verified. Corrected current Kuenenia spelling
    and historical synonym do not imply a different organism; native name conventions
    are not silently rewritten.
  accessed_at: '2026-11-03T08:55:14.482604Z'
  snapshot_sha256: d1622dee69e1fe2abfea4351893585852f4200cfff6eac3b42e5a014283cd0b0
  support: supports
- evidence_id: septin-apicoplast-agent-tax-36329
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/36329
  locator: 'ENA taxonomy exact tax-id response: current name, aliases, rank and lineage'
  summary: Taxon identity/lineage is verified. Corrected current Kuenenia spelling
    and historical synonym do not imply a different organism; native name conventions
    are not silently rewritten.
  accessed_at: '2026-11-03T08:55:14.671962Z'
  snapshot_sha256: 6d1389e6a3af3a09ef4bf23157b95ec8d94dac9b395b8f8ccf0d1952beddc306
  support: supports
- evidence_id: septin-apicoplast-agent-S8GBF3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/S8GBF3.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'S8GBF3: UniProtKB unreviewed (TrEMBL); taxon 508771; native gene/ORF values
    TIC20, TGME49_255370. Identity/status metadata does not alone establish organelle
    membership.'
  accessed_at: '2026-11-03T08:55:14.763108Z'
  snapshot_sha256: 6f8ee8170f0800a4b6cc9e8c5cea4930f69f83c3d0d4392d8cfc6c3eee95ebd4
  support: supports
- evidence_id: septin-apicoplast-agent-O97275
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O97275.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'O97275: UniProtKB unreviewed (TrEMBL); taxon 36329; native gene/ORF values
    PF3D7_0314300. Identity/status metadata does not alone establish organelle membership.'
  accessed_at: '2026-11-03T08:55:14.979966Z'
  snapshot_sha256: aa2a0c336bb23dcf2519f28ca86594f604bde1109843da9c2009d44459e0d241
  support: supports
- evidence_id: septin-apicoplast-agent-B9PY98
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/B9PY98.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'B9PY98: UniProtKB unreviewed (TrEMBL); taxon 5811; native gene/ORF values
    no native gene-name field. Identity/status metadata does not alone establish organelle
    membership. EMBL cross-reference is FJ976521/ACU32856.1, independently deposited
    as Der1ER1.'
  accessed_at: '2026-11-03T08:55:15.188599Z'
  snapshot_sha256: 5e769e2158976bdd00e8f8faedecee43ff930efff08515488ea2e999900edb70
  support: supports
- evidence_id: septin-apicoplast-agent-Q8I295
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8I295.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Q8I295: UniProtKB reviewed (Swiss-Prot); taxon 36329; native gene/ORF
    values LytB, IspH, PF3D7_0104400. Identity/status metadata does not alone establish
    organelle membership.'
  accessed_at: '2026-11-03T08:55:15.259582Z'
  snapshot_sha256: fbf23236890cbb286f7187b2d6cf9ee3c0e99a51755db5d1e71b9ecbf63994e3
  support: supports
- evidence_id: septin-apicoplast-agent-Q965D5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q965D5.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Q965D5: UniProtKB unreviewed (TrEMBL); taxon 5833; native gene/ORF values
    fabI. Identity/status metadata does not alone establish organelle membership.'
  accessed_at: '2026-11-03T08:55:15.377528Z'
  snapshot_sha256: 494803a71b64af3106da8cfaff33db472624f0f0dbc957523701ab202acb0dbb
  support: supports
- evidence_id: septin-apicoplast-agent-Q965D7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q965D7.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Q965D7: UniProtKB unreviewed (TrEMBL); taxon 5833; native gene/ORF values
    fabZ. Identity/status metadata does not alone establish organelle membership.'
  accessed_at: '2026-11-03T08:55:15.620175Z'
  snapshot_sha256: 91433d2a32ddbebd30a84cf2180205a68ab753b6968930a88c17bb7fae59b969
  support: supports
- evidence_id: septin-apicoplast-agent-C9WWW6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/C9WWW6.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'C9WWW6: UniProtKB unreviewed (TrEMBL); taxon 5811; native gene/ORF values
    no native gene-name field. Identity/status metadata does not alone establish organelle
    membership. EMBL cross-reference is FJ976520/ACU32855.1, independently deposited
    as apicoplast Der1; automated ER wording is not accepted as a replacement for
    primary localization.'
  accessed_at: '2026-11-03T08:55:16.014524Z'
  snapshot_sha256: 322c5fb4f1e71820ed84f3e03f57edeb35c06f1e671641702a129d00c727cf0e
  support: supports
- evidence_id: septin-apicoplast-agent-query-TIC20-508771
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3ATIC20%29%20AND%20%28organism_id%3A508771%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 1 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:16.146671Z'
  snapshot_sha256: 35a6c87eab0bae30ee1cc55f0bc32fbc90a9b21c7f07584dd76db1af04e4dcd7
  search_scope: UniProtKB REST search; query=['(gene_exact:TIC20) AND (organism_id:508771)'];
    size=['500']; retrieved 2026-11-03T08:55:16.146671Z; one explicit response page,
    no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-apicoplast-agent-query-ispH-36329
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AispH%29%20AND%20%28organism_id%3A36329%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 1 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:16.969768Z'
  snapshot_sha256: 3d9c15d68cca856c85c28a84a06123eb3e972e24f1acafc2c30cd5f9415b7c87
  search_scope: UniProtKB REST search; query=['(gene_exact:ispH) AND (organism_id:36329)'];
    size=['500']; retrieved 2026-11-03T08:55:16.969768Z; one explicit response page,
    no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-apicoplast-agent-query-fabI
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AfabI%29%20AND%20%28organism_id%3A5833%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 3 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:17.006892Z'
  snapshot_sha256: 353a3cba86413102955d8e53c0ed065f063ea0517140a7dbac46e55dbff8385c
  search_scope: UniProtKB REST search; query=['(gene_exact:fabI) AND (organism_id:5833)'];
    size=['500']; retrieved 2026-11-03T08:55:17.006892Z; one explicit response page,
    no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-apicoplast-agent-query-fabZ
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AfabZ%29%20AND%20%28organism_id%3A5833%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 1 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:17.997861Z'
  snapshot_sha256: d7e80ecb29e8e76aacf335f89608fa51328daf2e700f214f1f7bfbb653b67e6f
  search_scope: UniProtKB REST search; query=['(gene_exact:fabZ) AND (organism_id:5833)'];
    size=['500']; retrieved 2026-11-03T08:55:17.997861Z; one explicit response page,
    no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-apicoplast-agent-matches-S8GBF3
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/S8GBF3/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Native example matches: IPR005691:family. Protein family, domain and homologous-superfamily
    types remain distinct; generated biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:18.399340Z'
  snapshot_sha256: 43cd8b9d7fde94abf9038d7fc9785aae46b79d52245b9672587e64cac9020ceb
  support: supports
- evidence_id: septin-apicoplast-agent-matches-O97275
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O97275/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Native example matches: IPR007599:family, IPR035952:homologous_superfamily.
    Protein family, domain and homologous-superfamily types remain distinct; generated
    biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:19.035669Z'
  snapshot_sha256: 751500a2527a56fd64a534a58d8cb850d8fbe6010609087cf75b459243cc1eaa
  support: supports
- evidence_id: septin-apicoplast-agent-matches-B9PY98
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/B9PY98/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Native example matches: IPR007599:family, IPR035952:homologous_superfamily.
    Protein family, domain and homologous-superfamily types remain distinct; generated
    biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:19.293895Z'
  snapshot_sha256: e3f9e802aee474bbb0bddc4c7e9fb7007c014b7ee37fe22382c8deca667ae831
  support: supports
- evidence_id: septin-apicoplast-agent-matches-Q8I295
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8I295/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Native example matches: IPR003451:family. Protein family, domain and homologous-superfamily
    types remain distinct; generated biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:19.469135Z'
  snapshot_sha256: e291cd13102c9c8a6efe74340b5a5a4ff6d88038a2a13042cf605d24c3f6229a
  support: supports
- evidence_id: septin-apicoplast-agent-matches-Q965D5
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q965D5/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Native example matches: IPR002347:family, IPR014358:family, IPR036291:homologous_superfamily.
    Protein family, domain and homologous-superfamily types remain distinct; generated
    biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:20.035054Z'
  snapshot_sha256: 61a6fba1a7467efad5724c0ebde15af47f57f8ac012280633fa81081a993e1b2
  support: supports
- evidence_id: septin-apicoplast-agent-matches-Q965D7
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q965D7/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Native example matches: IPR010084:family, IPR013114:family, IPR029069:homologous_superfamily.
    Protein family, domain and homologous-superfamily types remain distinct; generated
    biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:20.051442Z'
  snapshot_sha256: 590519ba218ef2dbedff31268934487d95ed336e4305b1a3dfdf3e893f4f2fbf
  support: supports
- evidence_id: septin-apicoplast-agent-IPR005691
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005691/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR005691 is type family, name {''name'': ''Chloroplast protein import
    component Tic20'', ''short'': ''Tic20''}. Only metadata/classification is used;
    generic domain/superfamily matches do not identify a heterogeneous whole import
    machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:55:20.077053Z'
  snapshot_sha256: e7db56a3422efafa4695821230f0f6ac9caf851f4d67509c0528c119c5a67070
  support: supports
- evidence_id: septin-apicoplast-agent-IPR007599
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007599/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR007599 is type family, name {''name'': ''Derlin'', ''short'': ''DER1''}.
    Only metadata/classification is used; generic domain/superfamily matches do not
    identify a heterogeneous whole import machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:55:20.188800Z'
  snapshot_sha256: e82a628179ff9cf75d826bc42804aec4fee648285a5951e3028dcf560819a944
  support: supports
- evidence_id: septin-apicoplast-agent-IPR036291
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR036291/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR036291 is type homologous_superfamily, name {''name'': ''NAD(P)-binding
    domain superfamily'', ''short'': ''NAD(P)-bd_dom_sf''}. Only metadata/classification
    is used; generic domain/superfamily matches do not identify a heterogeneous whole
    import machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:55:21.236090Z'
  snapshot_sha256: 76bffc1e5b5163e613a57a0d1473fa8ead89a3661421e3ec7a400d3bed30cad2
  support: supports
- evidence_id: septin-apicoplast-agent-IPR010084
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR010084/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR010084 is type family, name {''name'': ''Beta-hydroxyacyl-(acyl-carrier-protein)
    dehydratase FabZ'', ''short'': ''FabZ''}. Only metadata/classification is used;
    generic domain/superfamily matches do not identify a heterogeneous whole import
    machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:55:21.257148Z'
  snapshot_sha256: b8649388fa37837bbe6468463e77b168774ba96bca5ef43a087a0cacb99ceb45
  support: supports
- evidence_id: septin-apicoplast-agent-IPR013114
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013114/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR013114 is type family, name {''name'': ''Beta-hydroxydecanoyl thiol
    ester dehydrase, FabA/FabZ'', ''short'': ''FabA_FabZ''}. Only metadata/classification
    is used; generic domain/superfamily matches do not identify a heterogeneous whole
    import machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:55:21.266361Z'
  snapshot_sha256: 48a25564fa21cc57aef1101d929162fca24f24ad89caaa17ba3caf0c7010fc9b
  support: supports
- evidence_id: septin-apicoplast-agent-IPR029069
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR029069/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR029069 is type homologous_superfamily, name {''name'': ''HotDog domain
    superfamily'', ''short'': ''HotDog_dom_sf''}. Only metadata/classification is
    used; generic domain/superfamily matches do not identify a heterogeneous whole
    import machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:55:21.407626Z'
  snapshot_sha256: 2da134cfd5468fda3c7b149611bbc2fee9b8a62a0bd6a20098b5188971a5c79b
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1073_pnas.95.21.12352
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.95.21.12352
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID9770490: Waller RF, Keeling PJ, Donald RG, Striepen B, Handman E,
    Lang-Unnasch N, Cowman AF, Besra GS, Roos DS, McFadden GI. (1998), Nuclear-encoded
    proteins target to the plastid in Toxoplasma gondii and Plasmodium falciparum..
    Full publication body is not attested by this metadata/abstract response.'
  accessed_at: '2026-11-03T08:55:21.854174Z'
  snapshot_sha256: 78788c07e75c55656f2df2b5f813a79193e83157f0cdb83b13b3b57702b25efa
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1073/pnas.95.21.12352;
    retrieved 2026-11-03T08:55:21.854174Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1098_rstb.2009.0273
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1098/rstb.2009.0273
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID20124342: Lim L, McFadden GI. (2010), The evolution, metabolism and
    functions of the apicoplast.. Full publication body is not attested by this metadata/abstract
    response.'
  accessed_at: '2026-11-03T08:55:21.865225Z'
  snapshot_sha256: 991b7c396b7075762d8d54bca1983efdaa0231339bc942f69de4e6b984fcd715
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1098/rstb.2009.0273;
    retrieved 2026-11-03T08:55:21.865225Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1073_pnas.0803862105
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0803862105
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID18757752: van Dooren GG, Tomova C, Agrawal S, Humbel BM, Striepen
    B. (2008), Toxoplasma gondii Tic20 is essential for apicoplast protein import..
    Full publication body is not attested by this metadata/abstract response.'
  accessed_at: '2026-11-03T08:55:22.028284Z'
  snapshot_sha256: 73796de2a5b5c1e415e9121ea437fcc1eb547f7aeab1c48a824ab3a730969217
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1073/pnas.0803862105;
    retrieved 2026-11-03T08:55:22.028284Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1371_journal.ppat.1003426
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.ppat.1003426
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID23785288: Agrawal S, Chung DW, Ponts N, van Dooren GG, Prudhomme J,
    Brooks CF, Rodrigues EM, Tan JC, Ferdig MT, Striepen B, Le Roch KG. (2013), An
    apicoplast localized ubiquitylation system is required for the import of nuclear-encoded
    plastid proteins.. Full publication body is not attested by this metadata/abstract
    response.'
  accessed_at: '2026-11-03T08:55:22.029417Z'
  snapshot_sha256: ad3c1b31793b0249654f5e68f6f13a6975f0e24b4d7bf67032b1524c89be7548
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1371/journal.ppat.1003426;
    retrieved 2026-11-03T08:55:22.029417Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1186_1475-2875-12-25
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1186/1475-2875-12-25
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID23331966: Lemgruber L, Kudryashev M, Dekiwadia C, Riglar DT, Baum
    J, Stahlberg H, Ralph SA, Frischknecht F. (2013), Cryo-electron tomography reveals
    four-membrane architecture of the Plasmodium apicoplast.. Full publication body
    is not attested by this metadata/abstract response.'
  accessed_at: '2026-11-03T08:55:22.475390Z'
  snapshot_sha256: d52a8201ddfa74c2eb86cb4d75449d14d05af21d4a291d8525eef5158b3b3497
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1186/1475-2875-12-25;
    retrieved 2026-11-03T08:55:22.475390Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1146_annurev-micro-092412-155741
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev-micro-092412-155741
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID23808340: van Dooren GG, Striepen B. (2013), The algal past and parasite
    present of the apicoplast.. Full publication body is not attested by this metadata/abstract
    response.'
  accessed_at: '2026-11-03T08:55:22.491459Z'
  snapshot_sha256: f51e74215bd68a149825c99cec576f0dbdc6bccb1fb5a07314e3f28a804d816a
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1146/annurev-micro-092412-155741;
    retrieved 2026-11-03T08:55:22.491459Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1371_journal.pbio.1001138
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.pbio.1001138
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID21912516: Yeh E, DeRisi JL. (2011), Chemical rescue of malaria parasites
    lacking an apicoplast defines organelle function in blood-stage Plasmodium falciparum..
    Full publication body is not attested by this metadata/abstract response.'
  accessed_at: '2026-11-03T08:55:22.696746Z'
  snapshot_sha256: e3aa250872a7ea1b3bad026415735c45f886e76b79c7b0648b5e3f03ffe259a3
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1371/journal.pbio.1001138;
    retrieved 2026-11-03T08:55:22.696746Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1016_j.ijpara.2016.08.005
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.ijpara.2016.08.005
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID27773518: McFadden GI, Yeh E. (2017), The apicoplast: now you see
    it, now you don''t.. Full publication body is not attested by this metadata/abstract
    response.'
  accessed_at: '2026-11-03T08:55:22.737548Z'
  snapshot_sha256: 831d3c68e735b3f2faa3c2e1bb69350206fe6fbd614549309aa717707ab1d48c
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1016/j.ijpara.2016.08.005;
    retrieved 2026-11-03T08:55:22.737548Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1074_jbc.M109.044024
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074/jbc.M109.044024
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID19808683: Agrawal S, van Dooren GG, Beatty WL, Striepen B. (2009),
    Genetic evidence that an endosymbiont-derived endoplasmic reticulum-associated
    protein degradation (ERAD) system functions in import of apicoplast proteins..
    Full publication body is not attested by this metadata/abstract response.'
  accessed_at: '2026-11-03T08:55:23.105861Z'
  snapshot_sha256: 2b6d98e78aff0daa494f06954a5cd5e4e0e024326fc252c2aa81a23e978732a3
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1074/jbc.M109.044024;
    retrieved 2026-11-03T08:55:23.105861Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-doi-10.1128_EC.00061-09
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1128/EC.00061-09
  locator: 'Europe PMC exact bibliographic query: returned author/year/title/DOI/PMID
    and abstract only'
  summary: 'PMID19502580: Kalanon M, Tonkin CJ, McFadden GI. (2009), Characterization
    of two putative protein translocation components in the apicoplast of Plasmodium
    falciparum.. Full publication body is not attested by this metadata/abstract response.'
  accessed_at: '2026-11-03T08:55:23.118536Z'
  snapshot_sha256: 78f37f0a66a2ea2d6d8d11926080f05f8769bf75d92e33899f2a30710e5d9e7e
  search_scope: Europe PMC exact identifier query https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI:10.1128/EC.00061-09;
    retrieved 2026-11-03T08:55:23.118536Z; returned metadata/abstract scope only.
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC3681736
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3681736.1/PMC3681736.1.xml
  locator: 'Agrawal et al. 2013 JATS: Abstract, apicoplast enzyme localization/import
    experiments, Discussion including unresolved endogenous modifier paragraphs'
  summary: Supports an apicoplast ubiquitylation-system import role and tested enzyme
    activity, while explicitly leaving endogenous ubiquitin versus ubiquitin-like
    modifier unresolved. Recombinant human ubiquitin is the tested in-vitro substrate.
  accessed_at: '2026-11-03T08:55:23.487064Z'
  snapshot_sha256: 8e546449838569e9d2d6a7d89bffc348f344d421df0c04c833ca170916a26897
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC3662607
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3662607.1/PMC3662607.1.xml
  locator: 'Lemgruber et al. 2013 JATS: Abstract, Results four-membrane reconstructions,
    figure captions and Conclusions; no new pixel audit'
  summary: Cryo-electron tomography of P. falciparum merozoites resolves four envelope
    membranes; local apposition explains slices apparently showing three. Supports
    the scoped membrane-boundary claim, not protein identities.
  accessed_at: '2026-11-03T08:55:23.544521Z'
  snapshot_sha256: 6a8d19405baff6d46f39c9c039da72718883c8b15c1850da7249c229af07f642
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC3166167
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3166167.1/PMC3166167.1.xml
  locator: 'Yeh and DeRisi 2011 JATS: Abstract and Results on IPP rescue, organelle-loss
    assays and blood-stage scope'
  summary: IPP supplementation sustains apicoplast-minus asexual blood-stage P. falciparum.
    Retain this stage/species scope; it does not establish identical metabolic essentiality
    in all apicomplexans or life stages.
  accessed_at: '2026-11-03T08:55:23.747429Z'
  snapshot_sha256: a501217e5e07c4792e454d88376994aac9edf25247c7c5f38c06086bcb618886
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC2817234
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2817234.1/PMC2817234.1.xml
  locator: 'Lim and McFadden 2010 secondary review JATS: origin/envelope, targeting
    and metabolic pathway sections'
  summary: Secondary synthesis supports signal/transit targeting and distinct fatty-acid,
    isoprenoid, heme and iron-sulfur pathways with stage-dependent requirements. It
    is not a new primary localization or assembly experiment.
  accessed_at: '2026-11-03T08:55:23.770969Z'
  snapshot_sha256: 600962f47c1fa8ce333826e38b6df45e8fd8e4c252cabbb68c723d849fbe0352
  support: supports
- evidence_id: septin-apicoplast-agent-jats-PMC5406208
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5406208.1/PMC5406208.1.xml
  locator: 'McFadden and Yeh 2017 secondary review JATS: apicoplast loss and stage-specific
    metabolic function sections'
  summary: Secondary context supports variable apicomplexan presence including Cryptosporidium
    loss and life-stage distinctions. No universal family or life-stage metabolic
    requirement is inferred.
  accessed_at: '2026-11-03T08:55:23.938665Z'
  snapshot_sha256: 3bd5749b77dc8ad8c1f12559b31e1c8f18780cd68b53430e021e1191ac3457b3
  support: supports
- evidence_id: septin-apicoplast-agent-ena-FJ976521
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/FJ976521?download=false
  locator: ENA native flatfile DE/CDS product/protein_id and translation
  summary: FJ976521 explicitly names Der1ER1 and ACU32856.1; exact accession bridge
    to unreviewed B9PY98, the ER paralog.
  accessed_at: '2026-11-03T08:55:24.022634Z'
  snapshot_sha256: c828fa0bcfedada7e3f1681cf850c2171324afdb4832e582f84733fd96c20831
  support: supports
- evidence_id: septin-apicoplast-agent-ena-FJ976520
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/FJ976520?download=false
  locator: ENA native flatfile DE/CDS product/note/protein_id and translation
  summary: FJ976520 explicitly names apicoplast Der1/Der1Ap and ACU32855.1; exact
    accession bridge to unreviewed C9WWW6. Automated generic ER location in that UniProt
    entry is not substituted for the primary paralog evidence.
  accessed_at: '2026-11-03T08:55:24.218558Z'
  snapshot_sha256: 47671e2466a074e673610363f3c8e7d8429c5063b2dbba1cf947b0212e32bfd2
  support: supports
- evidence_id: septin-apicoplast-agent-ena-CAB38986
  kind: database
  reference: https://www.ebi.ac.uk/ena/browser/api/embl/CAB38986.4?download=false
  locator: Native sequence/locus metadata; exact gene and old-locus bridge only
  summary: Supports current O97275/CAB38986.4/PF3D7_0314300 and older PFC0590c identity
    bridge; the old identifier string and new locus name are not treated as identical
    literal strings.
  accessed_at: '2026-11-03T08:55:24.473949Z'
  snapshot_sha256: a30a4b80383caa9e201851e7e8e9ed3edc23a763419f786e1df7926037f532ef
  support: supports
- evidence_id: septin-apicoplast-agent-gene-814456
  kind: database
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=gene&id=814456&retmode=json
  locator: Native sequence/locus metadata; exact gene and old-locus bridge only
  summary: Supports current O97275/CAB38986.4/PF3D7_0314300 and older PFC0590c identity
    bridge; the old identifier string and new locus name are not treated as identical
    literal strings.
  accessed_at: '2026-11-03T08:55:24.497062Z'
  snapshot_sha256: 95978f67da120777d7cd6b2f19bab33265c5ed897b6a435c3981275833603ed7
  support: supports
- evidence_id: septin-apicoplast-agent-kalanon2009-pdf
  kind: primary_source
  reference: https://fad.webmate.me/McFadden_Lab/Mcfadden_Papers/2009/Kalanon_Euk_Cell_2009.pdf
  locator: 'Author-hosted Kalanon et al. 2009 PDF: Methods antibody peptide printed
    p.1148; PfsDer1 paralog Results/Table1/Fig.4 caption printed pp.1149–1152'
  summary: Separates PfsDer1-1 from PfsDer1-2/PFC0590c. Published anti-Der1-2 peptide
    IKDCVSKYTSRSSTNN occurs at residues303–318 of current O97275. Full-length Der1-1
    localization experiments are not transferred to Der1-2.
  accessed_at: '2026-11-03T08:55:24.648334Z'
  snapshot_sha256: b38fbf7d4b2afc6cc5b36f4797f94c46a25f859d093d64b031f656485bc12add
  support: supports
- evidence_id: septin-current-adapter-catalogue
  kind: database
  reference: https://imodulondb.org/api/datasets
  locator: Complete official /api/datasets response, all 20 organism rows and 28 organism/dataset
    pairs (22 distinct literal dataset names)
  summary: No Kuenenia, Brocadiales/Planctomycetota, Plasmodium, Toxoplasma or other
    apicomplexan dataset matches these three targets. Broad Bacteria scope does not
    justify substituting unrelated covered species. No gene/module query is applicable
    to an unmatched organism.
  accessed_at: '2026-11-03T08:55:24.707230Z'
  snapshot_sha256: 155607e7023efdead5ebab3919279a0776d5665a7de9e28b67f02f8f521b0693
  support: supports
- evidence_id: septin-apicoplast-current-Q8IJH7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8IJH7.json
  locator: Native accession, entry status, organism/taxon, gene/ORF names, protein
    name, sequence and cross-reference fields
  summary: 'Q8IJH7: UniProtKB unreviewed (TrEMBL); taxon 36329; native gene/ORF values
    PF3D7_1022800. Identity/status metadata does not alone establish organelle membership.
    Added current example is the IspG-family enzyme at PF3D7_1022800; this is an ORF/locus
    field, not an asserted literal native ispG gene-name field. Its annotation is
    computational and is not new experimental localization.'
  accessed_at: '2026-11-03T08:55:24.773413Z'
  snapshot_sha256: ad07a537b5818ea3645f99996222755e8da404bcaaf363ddc815fe0da0689d9e
  support: supports
- evidence_id: septin-apicoplast-current-query-ispG
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AispG%20OR%20gene_exact%3APF3D7_1022800%29%20AND%20%28organism_id%3A36329%29
  locator: Native UniProt exact query response; first page size500; result metadata
    only
  summary: Returned 1 entries for the exact query. Zero reviewed exact-symbol hits
    do not establish absence of homologs or structural membership.
  accessed_at: '2026-11-03T08:55:24.863096Z'
  snapshot_sha256: 3c13f6dd03b33f6e30bad87ac1be57100eb85d1710fee717fe2bb4f92c4797b5
  search_scope: UniProtKB REST search; query=['(gene_exact:ispG OR gene_exact:PF3D7_1022800)
    AND (organism_id:36329)']; size=['500']; retrieved 2026-11-03T08:55:24.863096Z;
    one explicit response page, no broader synonym/homology absence claim.
  support: supports
- evidence_id: septin-apicoplast-current-matches-Q8IJH7
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8IJH7/?page_size=200
  locator: Complete example-specific native InterPro matches response; accession/type/match
    positions and pagination inspected
  summary: 'Native example matches: IPR004588:family, IPR011005:homologous_superfamily,
    IPR017178:family, IPR045854:homologous_superfamily, IPR058578:domain, IPR058579:domain.
    Protein family, domain and homologous-superfamily types remain distinct; generated
    biological descriptions are not used.'
  accessed_at: '2026-11-03T08:55:25.188262Z'
  snapshot_sha256: 38608161b43e653a093dc591a84a97bf8cba7f24502f789241835fc7c12f3f3b
  support: supports
- evidence_id: septin-current-IPR035952
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR035952/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR035952 is type homologous_superfamily, name {''name'': ''Rhomboid-like
    superfamily'', ''short'': ''Rhomboid-like_sf''}. Only metadata/classification
    is used; generic domain/superfamily matches do not identify a heterogeneous whole
    import machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:57:34.045519Z'
  snapshot_sha256: 54c39c940a1c98977176381073ed83761db133518e80cf6c935b4c1f8741f1b3
  support: supports
- evidence_id: septin-current-IPR003451
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR003451/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR003451 is type family, name {''name'': ''4-hydroxy-3-methylbut-2-enyl
    diphosphate reductase'', ''short'': ''LytB/IspH''}. Only metadata/classification
    is used; generic domain/superfamily matches do not identify a heterogeneous whole
    import machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:57:34.653998Z'
  snapshot_sha256: ff811b6765a6b19264d8001bb52b9c1c5c6d6ab2ab089796485b46017b565e19
  support: supports
- evidence_id: septin-current-IPR002347
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002347/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR002347 is type family, name {''name'': ''Short-chain dehydrogenase/reductase
    SDR'', ''short'': ''SDR_fam''}. Only metadata/classification is used; generic
    domain/superfamily matches do not identify a heterogeneous whole import machine.
    Generated description text is excluded.'
  accessed_at: '2026-11-03T08:57:35.255226Z'
  snapshot_sha256: 8719e4dee0cd1302acc88e65a346a6fff37771f9670d32165f613d46124ca595
  support: supports
- evidence_id: septin-current-IPR014358
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014358/
  locator: Native InterPro metadata accession/name/type/hierarchy/member signatures
    only
  summary: 'IPR014358 is type family, name {''name'': ''Enoyl-[acyl-carrier-protein]
    reductase (NADH)'', ''short'': ''Enoyl-ACP_Rdtase_NADH''}. Only metadata/classification
    is used; generic domain/superfamily matches do not identify a heterogeneous whole
    import machine. Generated description text is excluded.'
  accessed_at: '2026-11-03T08:57:35.892418Z'
  snapshot_sha256: fc8b4e91f6ed775c3f9d3e41b58ebd66fa58a65388ce3718dc4753c5b1ac4650
  support: supports
- evidence_id: septin-waller1998-author-pdf
  kind: primary_source
  reference: https://fad.webmate.me/McFadden_Lab/Mcfadden_Papers/1998/Waller_et_al_PNAS.pdf
  locator: 'Author-hosted published Waller et al. 1998 PDF pp.12352–12357: Abstract,
    targeting Results, signal/transit-sequence and ACP-GFP captions; extracted text,
    not image pixels'
  summary: Supports nuclear-encoded plastid protein targeting, N-terminal signal/transit
    architecture and sufficiency of the tested ACP leader for apicoplast targeting.
    General precursor targeting is separate from proof that Tic20 itself is a pore.
  accessed_at: '2026-11-03T09:00:17.320055Z'
  snapshot_sha256: b129feb38e452e0d98ca44d57f7dc2ea1616bf6092947d390ae380eebc04b5a9
  support: supports
- evidence_id: septin-agrawal2011-thesis
  kind: primary_source
  reference: https://openscholar.uga.edu/record/21126/files/agrawal_swati_201105_phd.pdf
  locator: 'University of Georgia author dissertation: Chapter3 Methods printed p.46/PDF59
    and Table3.1 p.81/PDF94; Appendix2 (Tic20 study) pp.176–188, especially p.188/PDF201'
  summary: Author-reproduced primary studies independently distinguish Der1ER1 FJ976521
    from Der1Ap FJ976520. The Tic20 appendix reports inner-membrane import dependency
    and explicitly discusses accessory/regulatory alternatives to direct channel action.
    This is an institutional thesis copy, not a successful new PMC full-body fetch.
  accessed_at: '2026-11-03T09:00:17.320297Z'
  snapshot_sha256: f0a1550c929a23dbcd8a50bb95a4e4a7042aff6d1acfa0cbbc50d990c2cc6a36
  support: supports
- evidence_id: septin-current-tic20-indexed-primary
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2533231/
  locator: Indexed primary Results/Discussion passage returned by bounded web retrieval;
    not full live PMC body
  summary: Primary passage explicitly discusses import impairment with residual activity
    after Tic20 falls below detection and accessory/regulatory alternatives; independently
    corroborated in author dissertation Appendix2.
  accessed_at: '2026-11-03T09:00:14Z'
  snapshot_sha256: 76a6991a0201165c86ae7cbd9cfa86ab68967342e23540378441a397c244de8a
  support: supports
- evidence_id: septin-current-tic20-indexed-primary-retrieval
  kind: search
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2533231/
  locator: Bounded source-location search; returned first response only
  summary: Search was used to locate exact primary or author copies. Unrelated returned
    hits were not used as evidence; no absence conclusion is drawn.
  accessed_at: '2026-11-03T09:00:14Z'
  snapshot_sha256: 76a6991a0201165c86ae7cbd9cfa86ab68967342e23540378441a397c244de8a
  search_scope: Web search queries ["\"Tic20\" \"accessory\" \"2008\"", "\"Tic20\"
    \"regulatory\" \"van Dooren\" \"2008\"", "\"Toxoplasma gondii Tic20 is essential\"
    filetype:pdf"]; date 2026-11-03 09:00:14 UTC; first tool result set, no pagination
    or date restriction; only named original source passages and author/institutional
    copies used.
  support: supports
- evidence_id: septin-current-kartal-indexed-review
  kind: authority
  reference: https://academic.oup.com/femsre/article/37/3/428/585200
  locator: Indexed secondary review sections on membranes, catabolism and proposed
    quinone/electron-transfer model; not a successful PDF download
  summary: Kartal2013 is a secondary synthesis. Indexed passage states central quinone/electron-transfer
    proposals and unresolved exact systems; direct native PDF requests timed out.
  accessed_at: '2026-11-03T08:59:56Z'
  snapshot_sha256: 421516f5c9028a54770f6fa338b86b2793905b7d9f1d628a14af5f3a374b8d49
  support: supports
- evidence_id: septin-current-kartal-indexed-review-retrieval
  kind: search
  reference: https://academic.oup.com/femsre/article/37/3/428/585200
  locator: Bounded source-location search; returned first response only
  summary: Search was used to locate exact primary or author copies. Unrelated returned
    hits were not used as evidence; no absence conclusion is drawn.
  accessed_at: '2026-11-03T08:59:56Z'
  snapshot_sha256: 421516f5c9028a54770f6fa338b86b2793905b7d9f1d628a14af5f3a374b8d49
  search_scope: Web search queries ["\"Toxoplasma gondii Tic20\" \"channel\"", "\"Toxoplasma
    gondii Tic20\" pdf", "\"Nuclear-encoded proteins target to the plastid\" pdf",
    "\"How to make a living from anaerobic ammonium oxidation\" pdf"]; date 2026-11-03
    08:59:56 UTC; first tool result set, no pagination or date restriction; only named
    original source passages and author/institutional copies used.
  support: supports
- evidence_id: septin-historical-adapter-runner-unavailable
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Actual historical attempt 2026-11-03T00:49:00.848907Z–00:49:00.863225Z;
    exit1 PermissionError reading runner pyvenv.cfg
  summary: Historical runner availability failure only; no fresh runner invocation
    is claimed. Current official catalogue/source fallback is separate.
  accessed_at: '2026-11-03T00:49:00.863225Z'
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  support: supports
- evidence_id: septin-original-validation-anammoxosome
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/adversary-septin/original-checks.json
  locator: Native validate; render --content; frozen revision git show and SHA256
    comparison
  summary: Original YAML validates and original Markdown is byte-identical to native
    render. Frozen target SHA matches the original source revision. Current target
    is stale and reassessed.
  accessed_at: '2026-11-03T09:00:37.804216Z'
  snapshot_sha256: 51cda0dc9e213b18941fafe07257d6e488257989a9fddb0aacca52aa496fe1f7
  support: supports
- evidence_id: septin-native-anammoxosome-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome-uniprot-verify-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome.yaml
    --verify; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Causal check has two COVERED nodes and one NO_GENE_SYMBOLS carrier node; neither
    check establishes physiological reaction, carrier localization or organelle formation
    requirement.
  accessed_at: '2026-11-03T08:54:34.328321Z'
  snapshot_sha256: 97b28326c0bf983b04d5facbdcffaa511f45aae3097609ddbf3dd9711ba76937
  support: supports
- evidence_id: septin-native-anammoxosome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome-uniprot-causal-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome.yaml
    --causal-graphs; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome-uniprot-causal.log
    SHA256 52e5fdd545e1b6d279558f3545e9afa178d74496cb2f5b08a165e560f97b3bc7
  summary: Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Causal check has two COVERED nodes and one NO_GENE_SYMBOLS carrier node; neither
    check establishes physiological reaction, carrier localization or organelle formation
    requirement.
  accessed_at: '2026-11-03T08:54:34.727756Z'
  snapshot_sha256: c4192f7d4bfe109c4bbadfcfdbdbc08557315f0b2196f72a93bcfd6a34ff16c3
  support: supports
- evidence_id: septin-original-validation-anammoxosome_membrane
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/adversary-septin/original-checks.json
  locator: Native validate; render --content; frozen revision git show and SHA256
    comparison
  summary: Original YAML validates and original Markdown is byte-identical to native
    render. Frozen target SHA matches the original source revision. Current target
    is byte-unchanged and reassessed.
  accessed_at: '2026-11-03T09:00:38.884858Z'
  snapshot_sha256: 51cda0dc9e213b18941fafe07257d6e488257989a9fddb0aacca52aa496fe1f7
  support: supports
- evidence_id: septin-native-anammoxosome_membrane-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome_membrane-uniprot-verify-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome_membrane.yaml
    --verify; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome_membrane-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Protein inventory and typed GENE_OR_PROTEIN graph-node inventory are empty; success
    does not validate narrative pathway claims.
  accessed_at: '2026-11-03T08:54:35.134380Z'
  snapshot_sha256: 66828298a950a7e8c9855fc2b480f00a2f46b1b31ebcd16c2ebd51883d21ec8d
  support: supports
- evidence_id: septin-native-anammoxosome_membrane-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome_membrane-uniprot-causal-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/anammoxosome_membrane.yaml
    --causal-graphs; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/anammoxosome_membrane-uniprot-causal.log
    SHA256 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
  summary: Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    Protein inventory and typed GENE_OR_PROTEIN graph-node inventory are empty; success
    does not validate narrative pathway claims.
  accessed_at: '2026-11-03T08:54:35.540677Z'
  snapshot_sha256: 2c822a63878ea47e76e70e945600a259df6e1260b7fc063af3541ce5dd6f8329
  support: supports
- evidence_id: septin-original-validation-apicoplast
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/adversary-septin/original-checks.json
  locator: Native validate; render --content; frozen revision git show and SHA256
    comparison
  summary: Original YAML validates and original Markdown is byte-identical to native
    render. Frozen target SHA matches the original source revision. Current target
    is stale and reassessed.
  accessed_at: '2026-11-03T09:00:40.052682Z'
  snapshot_sha256: 51cda0dc9e213b18941fafe07257d6e488257989a9fddb0aacca52aa496fe1f7
  support: supports
- evidence_id: septin-native-apicoplast-verify
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/apicoplast-uniprot-verify-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicoplast.yaml
    --verify; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/apicoplast-uniprot-verify.log
    SHA256 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
  summary: Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    All three typed protein nodes are now symbol-covered, including added ispG identity.
    Identifier/coverage success does not validate Der1 cellular-paralog choice or
    Tic20/ubiquitin mechanistic claims.
  accessed_at: '2026-11-03T08:54:39.919026Z'
  snapshot_sha256: 6ac87697c5fe5c99db998029cfbad57dc2c75e3efed33e3a4e60f1ef79f7091f
  support: supports
- evidence_id: septin-native-apicoplast-causal
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/apicoplast-uniprot-causal-receipt.json
  locator: .venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/apicoplast.yaml
    --causal-graphs; log /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/apicoplast-uniprot-causal.log
    SHA256 67050afcbbb6c42ff95f9912fecf9cd6ae035749b2c2bc8ccb6540289df936da
  summary: Actual root-run native command exited0 at source e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4.
    All three typed protein nodes are now symbol-covered, including added ispG identity.
    Identifier/coverage success does not validate Der1 cellular-paralog choice or
    Tic20/ubiquitin mechanistic claims.
  accessed_at: '2026-11-03T08:54:40.340681Z'
  snapshot_sha256: 9a1ccb5935132feed871defa67ecaa341c4b60b19e4fda54506c5daaaa6305eb
  support: supports
- evidence_id: check-qc
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/qc.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T09:00:22.769772Z'
  support: supports
  summary: 'Full native QC passed: 1054 tests passed, 3 skipped; schema, strict, history,
    generated products and corpus gates passed.'
  snapshot_sha256: fa92a6eb93fa5c06e9e958de8c3ddefa8bce794d0df13d2178929306c914f4da
- evidence_id: check-labels
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/labels.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:55:00.965317Z'
  support: supports
  summary: 4234 canonical, 50 synonym and 9 exception matches; 923 SKIPPED_NO_ADAPTER
    pairs remain unverified by an authority adapter.
  snapshot_sha256: 6cdfb05df9a27194f05a5fd7f851783f817ac1523ca0bbfa54fe0e0d18775905
- evidence_id: check-trait-links
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/trait-links.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:54:44.789067Z'
  support: supports
  summary: Native TraitMech link check passed.
  snapshot_sha256: 8b336cdefbbd3daf6da8787990efdbe346c95e2c8361d50b7eb68a18f2d5a44a
- evidence_id: check-vendored
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/vendored.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:54:33.311201Z'
  support: supports
  summary: Pinned governed files match; native vendored check passed.
  snapshot_sha256: b1f169d103aaefa930745468bcca171e5867b9cc49e4e74311e458097e3252a6
- evidence_id: check-curies
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/curies.log
  locator: Actual command stdout/stderr; receipt contains exact head/base and start/finish
  accessed_at: '2026-11-03T08:55:02.289897Z'
  support: supports
  summary: 'Exit zero: 5264 OK, 909 UNREACHABLE PMIDs due to HTTP414, 254 SKIPPED.
    Existing #2514 tracks batching/reporting. Supplemental bounded requests verified
    the 909 PMIDs separately; skipped identifiers are not claimed resolved.'
  snapshot_sha256: fb3be251020aac118f6df680372ae7aaa32c2a1dd3366648cde95494f19d9dd2
- evidence_id: focused
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/focused-results.json
  locator: All twenty actual target schema/strict command outputs
  accessed_at: '2026-11-03T09:09:54Z'
  support: supports
  summary: Ten schema and ten strict commands returned exit zero.
  snapshot_sha256: e5bf34cf3f448e34e7299e3207f5f8010290c2ae88ab0d4784ad0a5e71264560
- evidence_id: supplemental-pmid
  kind: validation
  reference: /private/tmp/cellstructure-batches-2346-2397-20261103/pr2357/pmid-chunks-receipt.json
  locator: Complete native-report PMID set checked with unchanged resolver in batches
    of at most fifty
  accessed_at: '2026-11-03T08:56:09.694034Z'
  support: supports
  summary: 909 PMIDs returned OK. Original report/cache unchanged; skipped identifiers
    remain unverified.
  snapshot_sha256: 2c27aaaf8735cf868409bb76b13728b2ab8098730ed95e42422ccec997918167
- evidence_id: historical-adapter-runner-availability
  kind: validation
  reference: /private/tmp/cellstructure-pr2344-20261102-agy3x2dx/adversary-septin/adapter-datasets-receipt.json
  locator: Historical runner invocation receipt, cross-checked against exact stdout/stderr
    hashes; reread during PR2357 synthesis
  accessed_at: '2026-11-03T00:49:00.863225Z'
  support: context_only
  snapshot_sha256: c3305faf20767e2af8e5a4dd03945d40f8491c872990b7ac28b87bd93c2e177d
  summary: Actual runner invocation at 2026-11-03T00:49:00Z returned exit1 with OS
    PermissionError reading the configured runner pyvenv.cfg. This is a retained historical
    availability observation, not a fresh attempt or a scientific validation failure.
    Native policy permits inspected source-catalogue fallback.
assessments:
- assessment_id: plaque-t2-identity
  area: identity
  topic: Exact compartment identity, synonym and distinct hierarchy relations
  outcome: supported
  target_ids:
  - GO:0033985
  summary: Native GO and UniProt location definitions support the exact compartment,
    synonym and parthood. The requested is_a closure supports the asserted broader
    parent. Parentage, part_of and a cross-reference are kept separate; the membrane
    and enclosed volume are not collapsed into the whole organelle.
  evidence_ids:
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-lumen-ancestors
  - plaque-acidocalcisome-agent-SL-0316
  - plaque-current-2
- assessment_id: plaque-t2-scope
  area: scope
  topic: Taxon identity and reported occurrence
  outcome: supported
  target_ids:
  - GO:0033985
  summary: The three native taxon identities are valid. VARIABLE across Bacteria and
    Eukaryota does not assert that every cell has acidocalcisomes. Reviews support
    broad reported distributions, while the sole bacterial exemplar requires the disputed-identity
    qualification in F1; this is not a blanket absence finding.
  evidence_ids:
  - plaque-acidocalcisome-agent-tax-2
  - plaque-acidocalcisome-agent-tax-2759
  - plaque-acidocalcisome-agent-tax-358
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-pmc2024-native
  - plaque-current-2
- assessment_id: plaque-t2-bacterial-conflict
  area: evidence
  topic: Reported bacterial compartments versus disputed granule equivalence
  outcome: concern
  target_ids:
  - GO:0033985
  summary: The 2003 primary abstract positively supports the original interpretation.
    The later C58 primary body and the2024 review explicitly disagree about whether
    the fluorescence-visible granules represent the same structures. Neither the negative
    staining/failed isolation in2020 nor the short-polyphosphate explanation in2024
    alone settles the identity. The target omits this material conflict, yielding
    F1.
  evidence_ids:
  - plaque-acidocalcisome-agent-doi-2003
  - plaque-acidocalcisome-agent-pmc2020-native
  - plaque-acidocalcisome-agent-pmc2024-native
  - plaque-current-2
- assessment_id: plaque-t2-citation
  area: provenance
  topic: Exact citation identities and source tiers
  outcome: concern
  target_ids:
  - GO:0033985
  summary: Exact publication identities are valid, but Docampo2024 is sole-authored
    and Huang attribution remains incorrect (F2). Current evidence uses the2003 primary
    abstract,2005 review abstract/key points, selected actual2020 primary Methods/Results
    and selected2024 review body; no primary/secondary or abstract/body tier is upgraded.
  evidence_ids:
  - plaque-acidocalcisome-agent-doi-2003
  - plaque-acidocalcisome-agent-doi-2005
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-doi-2020
  - plaque-acidocalcisome-agent-pmc2020-native
  - plaque-acidocalcisome-agent-doi-2024
  - plaque-acidocalcisome-agent-pmc2024-native
  - plaque-current-2
- assessment_id: plaque-t2-ownership
  area: provenance
  topic: Status, history and local boundary dependencies
  outcome: supported
  target_ids:
  - GO:0033985
  summary: The target remains PROPOSED and agent-authored; this review does not promote
    status or edit history. Whole-organelle and adjacent-compartment dependencies
    are frozen native inspection inputs and used only for the target boundary discussion.
    No hosted image or external image claim is present.
  evidence_ids:
  - plaque-current-2
  - plaque-whole-organelle
  - plaque-current-3
- assessment_id: plaque-t2-composition-boundary
  area: completeness
  topic: Deliberate separation of volume, contents and membrane machinery
  outcome: supported
  target_ids:
  - GO:0033985
  summary: This record denotes enclosed volume. Its resolved discussion deliberately
    places polyphosphate/cation matrix on the whole-organelle record and transport
    proteins on the membrane record. The frozen neighbors substantiate that representation
    boundary. Empty optional molecular inventory and function slots are not missing-data
    findings, and this review does not invent a source-neutral lumen scaffold.
  evidence_ids:
  - plaque-current-2
  - plaque-whole-organelle
  - plaque-current-3
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-pmc2024-native
- assessment_id: plaque-t2-graph
  area: graph
  topic: Both descriptive topology edges
  outcome: supported
  target_ids:
  - GO:0033985
  summary: The two edges state that the lumen is part of the acidocalcisome and that
    its membrane bounds it. Native definitions and location parthood support these
    claims. NONMECHANISTIC accurately describes this topology; the graph does not
    claim intervention, transporter membership or a molecular assembly mechanism.
  evidence_ids:
  - plaque-current-2
  - plaque-graph-policy
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-SL-0316
  - plaque-acidocalcisome-agent-SL-0003
- assessment_id: plaque-t2-necessity
  area: evidence
  topic: Lumen contents versus assembly necessity
  outcome: unknown
  target_ids:
  - GO:0033985
  summary: No lumen component essentiality is asserted. The existence of an enclosed
    volume does not establish which individual matrix molecule or membrane protein
    is necessary to assemble an acidocalcisome.
  evidence_ids:
  - plaque-current-2
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-pmc2024-native
- assessment_id: plaque-t2-bundle-provenance
  area: provenance
  topic: Original immutable input and deterministic artifact checks
  outcome: supported
  summary: Original YAML validates and its Markdown is exactly the native render.
    Historical target bytes match the original frozen target hash. Current inputs
    are independently frozen and reviewed; stale records receive new observations
    rather than edits to the originals.
  target_ids:
  - GO:0033985
  evidence_ids:
  - plaque-original-2
  - plaque-current-2
- assessment_id: plaque-t2-native-protein
  area: schema
  topic: Native protein identity and graph-symbol checks
  outcome: supported
  summary: Both actual focused checks exited0. Sparse material targets have no molecular
    nodes; generic heterogeneous sets can report NO_GENE_SYMBOLS without implying
    a missing required protein. Identity checking is separate from localization, mechanism
    and necessity.
  target_ids:
  - GO:0033985
  evidence_ids:
  - plaque-native-acidocalcisome_lumen-verify
  - plaque-native-acidocalcisome_lumen-causal
  - plaque-current-2
- assessment_id: plaque-t2-adapter
  area: scope
  topic: Structured-source applicability for a sparse compartment/material record
  outcome: not_applicable
  summary: The target makes compartment/bilayer topology claims and has no gene, locus,
    accession, regulator, molecular pathway, stress-response or transcriptomic claim
    requiring a matched module check. No molecular inventory is imposed. The original
    no-expression wording for lumen is clarified by this actual trigger assessment;
    the sparse membrane omission is not classified as a defect.
  target_ids:
  - GO:0033985
  evidence_ids:
  - plaque-current-2
  - plaque-policy
  - plaque-catalogue
- assessment_id: plaque-t3-identity
  area: identity
  topic: Exact compartment identity, synonym and distinct hierarchy relations
  outcome: supported
  target_ids:
  - GO:0033102
  summary: Native GO and UniProt location definitions support the exact compartment,
    synonym and parthood. The requested is_a closure supports the asserted broader
    parent. Parentage, part_of and a cross-reference are kept separate; the membrane
    and enclosed volume are not collapsed into the whole organelle.
  evidence_ids:
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-membrane-ancestors
  - plaque-acidocalcisome-agent-SL-0003
  - plaque-current-3
- assessment_id: plaque-t3-scope
  area: scope
  topic: Taxon identity and reported occurrence
  outcome: supported
  target_ids:
  - GO:0033102
  summary: The three native taxon identities are valid. VARIABLE across Bacteria and
    Eukaryota does not assert that every cell has acidocalcisomes. Reviews support
    broad reported distributions, while the sole bacterial exemplar requires the disputed-identity
    qualification in F1; this is not a blanket absence finding.
  evidence_ids:
  - plaque-acidocalcisome-agent-tax-2
  - plaque-acidocalcisome-agent-tax-2759
  - plaque-acidocalcisome-agent-tax-358
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-pmc2024-native
  - plaque-current-3
- assessment_id: plaque-t3-bacterial-conflict
  area: evidence
  topic: Reported bacterial compartments versus disputed granule equivalence
  outcome: concern
  target_ids:
  - GO:0033102
  summary: The 2003 primary abstract positively supports the original interpretation.
    The later C58 primary body and the2024 review explicitly disagree about whether
    the fluorescence-visible granules represent the same structures. Neither the negative
    staining/failed isolation in2020 nor the short-polyphosphate explanation in2024
    alone settles the identity. The target omits this material conflict, yielding
    F1.
  evidence_ids:
  - plaque-acidocalcisome-agent-doi-2003
  - plaque-acidocalcisome-agent-pmc2020-native
  - plaque-acidocalcisome-agent-pmc2024-native
  - plaque-current-3
- assessment_id: plaque-t3-citation
  area: provenance
  topic: Exact citation identities and source tiers
  outcome: concern
  target_ids:
  - GO:0033102
  summary: Exact publication identities are valid, but Docampo2024 is sole-authored
    and Huang attribution remains incorrect (F2). Current evidence uses the2003 primary
    abstract,2005 review abstract/key points, selected actual2020 primary Methods/Results
    and selected2024 review body; no primary/secondary or abstract/body tier is upgraded.
  evidence_ids:
  - plaque-acidocalcisome-agent-doi-2003
  - plaque-acidocalcisome-agent-doi-2005
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-doi-2020
  - plaque-acidocalcisome-agent-pmc2020-native
  - plaque-acidocalcisome-agent-doi-2024
  - plaque-acidocalcisome-agent-pmc2024-native
  - plaque-current-3
- assessment_id: plaque-t3-ownership
  area: provenance
  topic: Status, history and local boundary dependencies
  outcome: supported
  target_ids:
  - GO:0033102
  summary: The target remains PROPOSED and agent-authored; this review does not promote
    status or edit history. Whole-organelle and adjacent-compartment dependencies
    are frozen native inspection inputs and used only for the target boundary discussion.
    No hosted image or external image claim is present.
  evidence_ids:
  - plaque-current-3
  - plaque-whole-organelle
  - plaque-current-2
- assessment_id: plaque-t3-composition
  area: evidence
  topic: Constitutional bilayer and variable associated transport systems
  outcome: supported
  target_ids:
  - GO:0033102
  summary: The collective lipid bilayer is the membrane boundary itself, supporting
    its constitutional role and ESSENTIAL classification at that collective level.
    Accessible review material supports proton-pump and cation-transport systems with
    lineage-specific membership. A broad class label does not assert every named pump
    in every species, and no fixed subunit stoichiometry or universal lipid recipe
    is supplied.
  evidence_ids:
  - plaque-current-3
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-SL-0003
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-pmc2024-native
- assessment_id: plaque-t3-necessity
  area: evidence
  topic: Individual assembly requirements remain untested
  outcome: unknown
  target_ids:
  - GO:0033102
  summary: The record correctly keeps grouped proton pumps and cation transporters
    UNKNOWN for formation or assembly necessity. Localization, ion transport and effects
    on acidity/storage do not establish organelle assembly dependence. The constitutional
    requirement for a lipid boundary does not establish necessity of any individual
    lipid species or class.
  evidence_ids:
  - plaque-current-3
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-pmc2024-native
- assessment_id: plaque-t3-protein-identity
  area: grounding
  topic: Reviewed hppA example and native family scope
  outcome: supported
  target_ids:
  - GO:0033102
  summary: The record’s sole reviewed tax358 hppA example has the exact maintained
    accession, gene, label and status. Its role explicitly limits it to identifier
    identity. IPR004131 is an integrated candidate for this PPase fragment, not an
    exact source-neutral replacement for the grouped proton-pump set including ATPases.
    Generic cation transporters are not a single gene/family; the existing reviewed-label-only
    rationale and open grounding TODO are appropriately bounded.
  evidence_ids:
  - plaque-current-3
  - plaque-acidocalcisome-agent-Q8VPZ0
  - plaque-acidocalcisome-agent-Q8VPZ0-matches
  - plaque-acidocalcisome-agent-IPR004131
- assessment_id: plaque-t3-protein-membership-limit
  area: evidence
  topic: Accession-specific ion selectivity and experimental localization
  outcome: unknown
  target_ids:
  - GO:0033102
  summary: Q8VPZ0 is a D44 fragment with putative sodium-pump/function and membrane-location
    predictions by homology. The positive2003 abstract reports K-insensitive PPase
    activity but does not establish that this accession/strain was assayed. The2020
    C58 study instead uses the full-length712-aa Atu_1174 fusion and distinguishes
    tagged HppA structures from DAPI-positive granules. These contexts do not experimentally
    settle Q8VPZ0 proton versus sodium selectivity or acidocalcisome membership. Because
    the record explicitly says identity only, no wrong-accession or experimentally
    disproved localization finding is manufactured.
  evidence_ids:
  - plaque-current-3
  - plaque-acidocalcisome-agent-Q8VPZ0
  - plaque-acidocalcisome-agent-doi-2003
  - plaque-acidocalcisome-agent-pmc2020-native
- assessment_id: plaque-t3-functions
  area: evidence
  topic: Acidification and cation exchange at reviewed functional scope
  outcome: supported
  target_ids:
  - GO:0033102
  summary: The2005 accessible review key points support proton pumps and exchange
    systems; the2024 read sections explain acidification, cation transport/release
    and phosphorus/cation storage with species-dependent systems. These support the
    broad functional descriptions. They do not identify a universal transporter network,
    direction for every member, bacterial mechanism for every class, or assembly requirement.
  evidence_ids:
  - plaque-current-3
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-pmc2024-native
- assessment_id: plaque-t3-graph
  area: graph
  topic: All four coarse function edges and gene-node anchoring
  outcome: supported
  target_ids:
  - GO:0033102
  summary: All seven current edges were reassessed. Four prior coarse edges remain
    supported. New bilayer-forms-membrane and pump-resides-in-membrane edges follow
    GO and the 2005 accessible key points; new transporter-contributes-to-store is
    supported by the 2024 §§5.1,5.2,5.5 and10 synthesis of Ca2+ uptake and metal/proton
    exchange. It is a bounded functional storage relationship, not a claim that every
    transporter in every taxon only imports ions. NONMECHANISTIC remains appropriate.
    The new edge repeats the F2 author-attribution error.
  evidence_ids:
  - plaque-current-3
  - plaque-graph-policy
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-pmc2024-native
  - plaque-acidocalcisome-agent-Q8VPZ0
- assessment_id: plaque-t3-discussion
  area: completeness
  topic: Bounded open grounding work
  outcome: supported
  target_ids:
  - GO:0033102
  summary: The existing open discussion accurately requests more precise lipid and
    transporter groundings while recognizing lineage-dependent composition. No exact
    identifier for the full grouped sets was established by the inspected candidate
    family, so empty optional family inventories are not treated as an automatic defect.
    F1 separately requires a durable bacterial identity-conflict discussion.
  evidence_ids:
  - plaque-current-3
  - plaque-acidocalcisome-agent-IPR004131
  - plaque-acidocalcisome-agent-Q8VPZ0-matches
  - plaque-acidocalcisome-agent-pmc2024-native
- assessment_id: plaque-t3-bundle-provenance
  area: provenance
  topic: Original immutable input and deterministic artifact checks
  outcome: supported
  summary: Original YAML validates and its Markdown is exactly the native render.
    Historical target bytes match the original frozen target hash. Current inputs
    are independently frozen and reviewed; stale records receive new observations
    rather than edits to the originals.
  target_ids:
  - GO:0033102
  evidence_ids:
  - plaque-original-3
  - plaque-current-3
- assessment_id: plaque-t3-native-protein
  area: schema
  topic: Native protein identity and graph-symbol checks
  outcome: supported
  summary: Both actual focused checks exited0. Sparse material targets have no molecular
    nodes; generic heterogeneous sets can report NO_GENE_SYMBOLS without implying
    a missing required protein. Identity checking is separate from localization, mechanism
    and necessity.
  target_ids:
  - GO:0033102
  evidence_ids:
  - plaque-native-acidocalcisome_membrane-verify
  - plaque-native-acidocalcisome_membrane-causal
  - plaque-current-3
- assessment_id: plaque-t3-adapter
  area: scope
  topic: Actual molecular triggers and current covered-organism catalogue
  outcome: supported
  summary: Named hppA/GRA accessions trigger applicability assessment. Historical
    runner unavailability is separately disclosed. Fresh complete source catalogue
    has no matching Agrobacterium or Toxoplasma dataset, so no downstream gene/module
    search is applicable. Broad taxon classes do not license substitution of another
    species; lack of expression prose is not the rationale.
  target_ids:
  - GO:0033102
  evidence_ids:
  - plaque-current-3
  - plaque-policy
  - plaque-historical-runner
  - plaque-catalogue
- assessment_id: plaque-t7-identity
  area: identity
  topic: Secretory organelle and membrane boundary
  outcome: supported
  target_ids:
  - GO:0020026
  summary: Exact GO identity, RELATED synonym and secretory-granule hierarchy are
    supported. The whole granule is kept separate from its membrane, lumen and the
    host-parasite vacuole membrane where secreted cargo later acts.
  evidence_ids:
  - plaque-granule-agent-go
  - plaque-current-7
  - plaque-granule-agent-jats-PMC9482668
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-pmc-PMC13475723
- assessment_id: plaque-t7-composition
  area: grounding
  topic: Heterogeneous cargo and concrete examples
  outcome: supported
  target_ids:
  - GO:0020026
  summary: Current membrane and heterogeneous cargo cohorts are supported without
    a universal protein census. Gra2/Gra6 candidate families cannot ground the full
    cargo set. Exact UniProt entries support three reviewed examples and two unreviewed
    ME49 examples; primary Table1 bridges ME49 loci to GRA17/GRA23. Inconclusive exact-protein
    InterPro attempts do not establish family absence or invalidate the bounded label-only
    cohort.
  evidence_ids:
  - plaque-granule-agent-P13403
  - plaque-granule-agent-P13404
  - plaque-granule-agent-Q27003
  - plaque-granule-agent-A0A125YME4
  - plaque-granule-agent-matches-P13404
  - plaque-granule-agent-matches-Q27003
  - plaque-granule-agent-IPR008118
  - plaque-granule-agent-IPR008119
  - plaque-granule-agent-jats-PMC7202600
  - plaque-granule-agent-gene-7901472
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-jats-PMC9482668
  - plaque-current-7
  - plaque-gra17-S8GTZ8
  - plaque-gra17-gene
  - plaque-gra17-matches
  - plaque-gra23-matches
  - plaque-gra1-matches
- assessment_id: plaque-t7-necessity
  area: evidence
  topic: Unresolved individual assembly requirements
  outcome: unknown
  target_ids:
  - GO:0020026
  summary: A lipid boundary constitutes this membrane-bounded organelle; the ESSENTIAL
    membrane row is collective material. None of the named GRA species is thereby
    proven necessary for formation of a dense granule. PVM permeability, parasite
    growth and cargo secretion phenotypes do not establish granule-assembly necessity;
    individual cargo entries correctly remain UNKNOWN.
  evidence_ids:
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-pmc-PMC13475723
  - plaque-granule-agent-jats-PMC9482668
  - plaque-current-7
  - plaque-schema-policy
- assessment_id: plaque-t7-scope
  area: scope
  topic: Taxonomy and model-system boundaries
  outcome: supported
  target_ids:
  - GO:0020026
  summary: The native taxonomy entries attest their own ranks and identities. Mercier2005
    supplies review-tier cross-apicomplexan context for qualitative COMMON and specialized
    eukaryotic RARE wording; it is not a prevalence measurement. Toxoplasma experiments
    and ME49 reference identity remain distinct from a universal apicomplexan GRA
    inventory.
  evidence_ids:
  - plaque-granule-agent-tax-2759
  - plaque-granule-agent-tax-5794
  - plaque-granule-agent-tax-5811
  - plaque-granule-agent-tax-508771
  - plaque-granule-agent-doi-10.1111_jeu.12904
  - plaque-granule-agent-doi-10.1016_j.pt.2014.12.002
  - plaque-granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - plaque-granule-agent-doi-10.1016_j.chom.2015.04.003
  - plaque-granule-agent-doi-10.1016_j.parint.2013.04.003
  - plaque-granule-agent-doi-10.1016_j.chom.2013.03.002
  - plaque-granule-agent-pmid-9208224
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-pmc-PMC13475723
  - plaque-current-7
- assessment_id: plaque-t7-functions
  area: evidence
  topic: Secretion, permeability and host-cell effects
  outcome: supported
  target_ids:
  - GO:0020026
  summary: After-invasion secretion is supported and is not phrased as exclusive of
    extracellular secretion. Gold2015 supports the paired permeability function with
    unequal single-deletion phenotypes. The native Bougdour2013 abstract explicitly
    supports GRA16 nuclear export and host-gene effects; Masatani2013 abstract supports
    GRA23 dense-granule/PVM/IVN localization. Full bodies of those two studies were
    unavailable.
  evidence_ids:
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-pmc-PMC13475723
  - plaque-granule-agent-jats-PMC9482668
  - plaque-granule-agent-doi-10.1111_jeu.12904
  - plaque-granule-agent-doi-10.1016_j.pt.2014.12.002
  - plaque-granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - plaque-granule-agent-doi-10.1016_j.chom.2015.04.003
  - plaque-granule-agent-doi-10.1016_j.parint.2013.04.003
  - plaque-granule-agent-doi-10.1016_j.chom.2013.03.002
  - plaque-granule-agent-pmid-9208224
  - plaque-current-7
- assessment_id: plaque-t7-graph
  area: graph
  topic: Cargo release and later PVM activity
  outcome: supported
  target_ids:
  - GO:0020026
  summary: The graph represents cargo release, delivery/localization and an experimentally
    tested permeability consequence, in addition to boundary topology. It distinguishes
    granule membrane from PVM, does not identify a pore stoichiometry, and does not
    imply GRA17/GRA23 are required to build the secretory organelle.
  evidence_ids:
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-pmc-PMC13475723
  - plaque-granule-agent-jats-PMC9482668
  - plaque-granule-agent-doi-10.1111_jeu.12904
  - plaque-granule-agent-doi-10.1016_j.pt.2014.12.002
  - plaque-granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - plaque-granule-agent-doi-10.1016_j.chom.2015.04.003
  - plaque-granule-agent-doi-10.1016_j.parint.2013.04.003
  - plaque-granule-agent-doi-10.1016_j.chom.2013.03.002
  - plaque-granule-agent-pmid-9208224
  - plaque-current-7
- assessment_id: plaque-t7-coverage
  area: completeness
  topic: Bounded clean review
  outcome: supported
  target_ids:
  - GO:0020026
  summary: No new scientific curation defect was established. Current GRA17 protein
    identity and new exported-effector edges were substantively reassessed. Optional
    complete proteomes, resident membrane-protein censuses and universal lipid inventories
    are not mandatory. Adapter-process omission is reported separately from record
    science.
  evidence_ids:
  - plaque-granule-agent-go
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-jats-PMC9482668
  - plaque-granule-agent-matches-P13404
  - plaque-granule-agent-matches-Q27003
  - plaque-granule-agent-IPR008118
  - plaque-granule-agent-IPR008119
  - plaque-current-7
  - plaque-schema-policy
- assessment_id: plaque-t7-bundle-provenance
  area: provenance
  topic: Original immutable input and deterministic artifact checks
  outcome: supported
  summary: Original YAML validates and its Markdown is exactly the native render.
    Historical target bytes match the original frozen target hash. Current inputs
    are independently frozen and reviewed; stale records receive new observations
    rather than edits to the originals.
  target_ids:
  - GO:0020026
  evidence_ids:
  - plaque-original-7
  - plaque-current-7
- assessment_id: plaque-t7-native-protein
  area: schema
  topic: Native protein identity and graph-symbol checks
  outcome: supported
  summary: Both actual focused checks exited0. Sparse material targets have no molecular
    nodes; generic heterogeneous sets can report NO_GENE_SYMBOLS without implying
    a missing required protein. Identity checking is separate from localization, mechanism
    and necessity.
  target_ids:
  - GO:0020026
  evidence_ids:
  - plaque-native-apicomplexan_dense_granule-verify
  - plaque-native-apicomplexan_dense_granule-causal
  - plaque-current-7
- assessment_id: plaque-t7-adapter
  area: scope
  topic: Actual molecular triggers and current covered-organism catalogue
  outcome: supported
  summary: Named hppA/GRA accessions trigger applicability assessment. Historical
    runner unavailability is separately disclosed. Fresh complete source catalogue
    has no matching Agrobacterium or Toxoplasma dataset, so no downstream gene/module
    search is applicable. Broad taxon classes do not license substitution of another
    species; lack of expression prose is not the rationale.
  target_ids:
  - GO:0020026
  evidence_ids:
  - plaque-current-7
  - plaque-policy
  - plaque-historical-runner
  - plaque-catalogue
- assessment_id: plaque-t8-identity
  area: identity
  topic: Membrane distinct from the whole secretory organelle
  outcome: supported
  target_ids:
  - GO:0030668
  summary: The ontology definition, broader organelle-membrane parent and part_of
    dense-granule relation are supported. The record consistently represents the bounding
    membrane, not the stored lumen/cargo or the parasitophorous-vacuole membrane.
  evidence_ids:
  - plaque-granule-agent-go
  - plaque-current-7
  - plaque-granule-agent-jats-PMC9482668
  - plaque-current-8
  - plaque-granule-membrane-agent-go
- assessment_id: plaque-t8-composition
  area: grounding
  topic: Collective lipid matrix
  outcome: supported
  target_ids:
  - GO:0030668
  summary: The generic lipid-bilayer row represents the constituting membrane material.
    GO0030668 identifies the whole membrane and is not an exact chemical-family identifier
    for its constituent lipids; label-only material grounding is justified. No universal
    lipid-species census is asserted.
  evidence_ids:
  - plaque-granule-agent-go
  - plaque-granule-agent-jats-PMC9482668
  - plaque-current-8
  - plaque-schema-policy
- assessment_id: plaque-t8-necessity
  area: evidence
  topic: Individual formation requirements remain untested
  outcome: unknown
  target_ids:
  - GO:0030668
  summary: ESSENTIAL denotes the collective constituting lipid bilayer. The cited
    synthesis and ontology do not identify which individual lipid species or proteins
    are necessary for membrane formation, and no such removal experiment is inferred
    from ordinary boundary identity.
  evidence_ids:
  - plaque-granule-agent-go
  - plaque-granule-agent-jats-PMC9482668
  - plaque-current-8
  - plaque-schema-policy
- assessment_id: plaque-t8-scope
  area: scope
  topic: Cross-apicomplexan context and Toxoplasma example
  outcome: supported
  target_ids:
  - GO:0030668
  summary: Native taxonomy verifies Apicomplexa and Toxoplasma identities. Mercier2005
    review abstract supplies qualitative cross-apicomplexan context; Griffith selected
    review body supports Toxoplasma membrane-bounded granule biogenesis. These are
    not measured prevalence or universal cargo inventories.
  evidence_ids:
  - plaque-granule-agent-tax-5794
  - plaque-granule-agent-tax-5811
  - plaque-granule-agent-doi-10.1111_jeu.12904
  - plaque-granule-agent-doi-10.1016_j.ijpara.2005.03.011
  - plaque-granule-agent-jats-PMC9482668
  - plaque-current-8
- assessment_id: plaque-t8-function-graph
  area: graph
  topic: Explicit nonmechanistic topology
  outcome: supported
  target_ids:
  - GO:0030668
  summary: The boundary function and single part-of graph edge follow the native definition.
    NONMECHANISTIC accurately describes this topology; no cargo secretion mechanism
    or particular PVM permeability protein has been transferred onto the granule membrane.
  evidence_ids:
  - plaque-granule-agent-go
  - plaque-granule-agent-jats-PMC9482668
  - plaque-current-8
- assessment_id: plaque-t8-coverage
  area: completeness
  topic: Bounded clean review
  outcome: supported
  target_ids:
  - GO:0030668
  summary: No corrective issue was established. The open generic-lipid grounding question
    is not an error, and optional resident-membrane-protein inventories are not required
    to make this topology record valid. The whole-granule neighbor supplies context
    only.
  evidence_ids:
  - plaque-granule-agent-go
  - plaque-granule-agent-jats-PMC9482668
  - plaque-current-7
  - plaque-current-8
  - plaque-schema-policy
- assessment_id: plaque-t8-bundle-provenance
  area: provenance
  topic: Original immutable input and deterministic artifact checks
  outcome: supported
  summary: Original YAML validates and its Markdown is exactly the native render.
    Historical target bytes match the original frozen target hash. Current inputs
    are independently frozen and reviewed; stale records receive new observations
    rather than edits to the originals.
  target_ids:
  - GO:0030668
  evidence_ids:
  - plaque-original-8
  - plaque-current-8
- assessment_id: plaque-t8-native-protein
  area: schema
  topic: Native protein identity and graph-symbol checks
  outcome: supported
  summary: Both actual focused checks exited0. Sparse material targets have no molecular
    nodes; generic heterogeneous sets can report NO_GENE_SYMBOLS without implying
    a missing required protein. Identity checking is separate from localization, mechanism
    and necessity.
  target_ids:
  - GO:0030668
  evidence_ids:
  - plaque-native-apicomplexan_dense_granule_membrane-verify
  - plaque-native-apicomplexan_dense_granule_membrane-causal
  - plaque-current-8
- assessment_id: plaque-t8-adapter
  area: scope
  topic: Structured-source applicability for a sparse compartment/material record
  outcome: not_applicable
  summary: The target makes compartment/bilayer topology claims and has no gene, locus,
    accession, regulator, molecular pathway, stress-response or transcriptomic claim
    requiring a matched module check. No molecular inventory is imposed. The original
    no-expression wording for lumen is clarified by this actual trigger assessment;
    the sparse membrane omission is not classified as a defect.
  target_ids:
  - GO:0030668
  evidence_ids:
  - plaque-current-8
  - plaque-policy
  - plaque-catalogue
- assessment_id: plaque-membrane-stale-refresh
  area: graph
  topic: Substantive refresh of added membrane material and transporter edges
  outcome: supported
  summary: The new phospholipid-bilayer node and three edges retain the established
    membrane identity and variable transporter scope. Docampo2024 explicitly describes
    cation sequestration by metal/proton exchange alongside Ca2+-ATPases; it also
    describes release systems and unknown transporter roles, so the review preserves
    these limits. Added edge6 inherits the same sole-author attribution finding. No
    unrefreshable delta remains.
  target_ids:
  - GO:0033102
  evidence_ids:
  - plaque-current-3
  - plaque-original-3
  - plaque-acidocalcisome-agent-go
  - plaque-acidocalcisome-agent-review2005-publisher
  - plaque-acidocalcisome-agent-pmc2024-native
- assessment_id: plaque-granule-stale-refresh
  area: evidence
  topic: Substantive GRA17 and exported-effector refresh
  outcome: supported
  summary: S8GTZ8/NCBI7895641 identify ME49 TGME49_222170; the primary PMC7202600
    Table1 supplies its exact GRA17 bridge. Gold2015 GT1/RH experimental effects are
    not silently transferred as ME49 experimental verification. Bougdour2013 primary
    abstract supports the two new GRA16 secretion/export edges; Griffith body provides
    secondary context. GRA17/23 small-molecule permeability remains separate from
    GRA16 export.
  target_ids:
  - GO:0020026
  evidence_ids:
  - plaque-current-7
  - plaque-original-7
  - plaque-gra17-S8GTZ8
  - plaque-gra17-gene
  - plaque-granule-agent-jats-PMC7202600
  - plaque-granule-agent-jats-PMC4435723
  - plaque-granule-agent-doi-10.1016_j.chom.2013.03.002
  - plaque-granule-agent-jats-PMC9482668
- assessment_id: micro-proteasome_storage_granule-a1
  area: schema
  topic: Original artifact integrity and current input boundary
  outcome: supported
  summary: Original native validate/render pass and frozen source blob matches its
    recorded hash. Current record is changed and substantively reassessed; old artifacts
    are retained unchanged.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-prior-proteasome_storage_granule
  - micro-original-validation-inputs
- assessment_id: micro-proteasome_storage_granule-a2
  area: schema
  topic: Current native protein verification and coverage
  outcome: supported
  summary: Three reference protein_examples verify; both recovery graphs contain zero
    GENE_OR_PROTEIN nodes. Coverage does not certify other component completeness.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-native-proteasome_storage_granule-verify
  - micro-native-proteasome_storage_granule-causal
- assessment_id: micro-proteasome_storage_granule-a3
  area: evidence
  topic: Structured-source applicability and current bounded fallback
  outcome: not_applicable
  summary: Named BLM10/UBP6/UBI4 and quiescence/refeeding claims require assessment.
    Current full catalogue contains no matching organism. No downstream module result
    is fabricated; historical runner unavailability is dated separately.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-protein_aggregate_center-a1
  area: schema
  topic: Original artifact integrity and current input boundary
  outcome: supported
  summary: Original native validate/render pass and frozen source blob matches its
    recorded hash. Current record is byte-identical and reassessed; old artifacts
    are retained unchanged.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-prior-protein_aggregate_center
  - micro-original-validation-inputs
- assessment_id: micro-protein_aggregate_center-a2
  area: schema
  topic: Current native protein verification and coverage
  outcome: supported
  summary: Three reference protein_examples verify; no GENE_OR_PROTEIN causal nodes.
    This does not validate biological necessity or count every chaperone.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-native-protein_aggregate_center-verify
  - micro-native-protein_aggregate_center-causal
- assessment_id: micro-protein_aggregate_center-a3
  area: evidence
  topic: Structured-source applicability and current bounded fallback
  outcome: not_applicable
  summary: Named HSP42/BTN2/HSP104 and heat-shock mutant/recovery claims require assessment.
    Current full catalogue contains no matching organism. No downstream module result
    is fabricated; historical runner unavailability is dated separately.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-actinophryid_extrusome-a1
  area: schema
  topic: Original artifact integrity and current input boundary
  outcome: supported
  summary: Original native validate/render pass and frozen source blob matches its
    recorded hash. Current record is changed and substantively reassessed; old artifacts
    are retained unchanged.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-prior-actinophryid_extrusome
  - micro-original-validation-inputs
- assessment_id: micro-actinophryid_extrusome-a2
  area: schema
  topic: Current native protein verification and coverage
  outcome: supported
  summary: The verifier has no protein_examples to check; the new single GP40 protein
    node is component-anchored but NO_GENE_SYMBOLS. Label-only identity and lack of
    experimentally assigned isoform are explicit, not false complete coverage.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-native-actinophryid_extrusome-verify
  - micro-native-actinophryid_extrusome-causal
- assessment_id: micro-actinophryid_extrusome-a3
  area: evidence
  topic: Structured-source applicability and current bounded fallback
  outcome: not_applicable
  summary: Named GP40 and calcium/drug perturbation claims require assessment even
    without transcriptomic inference. Current full catalogue contains no matching
    organism. No downstream module result is fabricated; historical runner unavailability
    is dated separately.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-review-policy
  - micro-adapter-catalogue
  - micro-historical-adapter-runner
- assessment_id: micro-proteasome_storage_granule-a4
  area: identity
  topic: PSG identity, type and anatomical parts
  outcome: supported
  summary: GO0034515 matches the cytoplasmic quiescent CP/RP granule. INCLUSION_BODY
    and membraneless parent, cytoplasmic part-of and core/regulatory has-parts preserve
    structure identity. Nuclear precursor assemblies in2026 are distinguished from
    the record cytoplasmic PSG focus.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-go-terms
  - micro-laporte2008
  - micro-tang2026
- assessment_id: micro-proteasome_storage_granule-a5
  area: representation
  topic: Associated proteins and processed ubiquitin
  outcome: supported
  summary: Blm10/Ubp6 associations have direct2017 microscopy/enrichment support and
    appropriate reference examples. UBI4 is explicitly a precursor reference for processed
    unconjugated ubiquitin, not an unprocessed granule subunit; the manipulated reporter
    is distinguished from native cargo. Broad ubiquitin-family grounding stays deferred.
    UNKNOWN formation necessity avoids global extrapolation from assay-dependent mutants.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-gu2017
  - micro-uniprot-P43583
  - micro-uniprot-P43593
  - micro-uniprot-P0CG63
  - micro-matches-P43583
  - micro-matches-P43593
  - micro-matches-P0CG63
  - micro-entry-IPR035309
  - micro-entry-IPR044635
  - micro-entry-IPR050158
  - micro-reviewed-BLM10
  - micro-reviewed-UBP6
  - micro-reviewed-UBI4
- assessment_id: micro-proteasome_storage_granule-a6
  area: evidence
  topic: Assembly architecture and differing assay scopes
  outcome: supported
  summary: 2008 colocalization does not establish active26S;2017 lysate PAGE and crosslink
    enrichment do not dictate intact in situ state.2026 cryo-ET supports paracrystalline
    intact inactive26S arrays and explains purification instability. No universal
    liquid-phase/stoichiometry claim is inferred.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-laporte2008
  - micro-gu2017
  - micro-tang2026
- assessment_id: micro-proteasome_storage_granule-a7
  area: graph
  topic: 'Stale refresh: refeeding edges and cycloheximide control'
  outcome: supported
  summary: New descriptions correctly restrict both PSG disappearance and nuclear
    reaccumulation to four-day yeast shifted to freshYPD versus water; recovery persists
    with100ug/mL CHX preincubated1h. This excludes a need for de novo synthesis in
    that assay, without identifying a molecular dissolution mechanism.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-laporte2008
  - micro-original-validation-inputs
- assessment_id: micro-proteasome_storage_granule-a8
  area: evidence
  topic: 'Stale refresh: retracted source placement'
  outcome: supported
  summary: Structured REFUTE evidence now makes the excluded2018 DOI machine-readable.
    No proteaphagy-protection function or Arabidopsis canonical example is imported
    from it. Historical#2430 is context only; no whole grouped issue or unfrozen category
    predecessor is terminally resolved.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-psg-retraction
  - micro-psg-commentary
  - micro-metadata-retracted2018-crossref
- assessment_id: micro-proteasome_storage_granule-a9
  area: scope
  topic: Canonical organisms and reference strains
  outcome: supported
  summary: Budding yeast BY4741/2/3 and fission-yeast Pad1-GFP examples have source
    support; S288C protein authority entries are reference identifiers, not the exact
    experimental strain. No global taxonomic prevalence is inferred.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-laporte2008
  - micro-gu2017
  - micro-tax-4932
  - micro-tax-4896
  - micro-tax-559292
- assessment_id: micro-proteasome_storage_granule-a10
  area: provenance
  topic: Linked Figure2 image and license
  outcome: supported
  summary: Source pixels/caption, package checksum and CC BY-NC-SA3.0 permissions
    agree with the bounded localization caption. No repository-hosted-image requirement
    or new morphometric estimate is invented.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-laporte2008
  - micro-psg-image
  - micro-package-PMC2396804
- assessment_id: micro-proteasome_storage_granule-a11
  area: completeness
  topic: Bounded clean current assessment
  outcome: supported
  summary: No additional material defect observed across definition, parts, components,
    functions, graphs and image. Missing precise mature-ubiquitin family and universal
    granule stoichiometry remain explicit scientific limits, not fabricated findings.
    Current verdict remains pass_with_limitations.
  target_ids:
  - GO:0034515
  evidence_ids:
  - micro-record-proteasome_storage_granule
  - micro-laporte2008
  - micro-gu2017
  - micro-tang2026
- assessment_id: micro-protein_aggregate_center-a4
  area: identity
  topic: PAC identity and boundaries
  outcome: supported
  summary: GO0140453 matches reversible misfolded-protein/chaperone assemblies. INCLUSION_BODY
    and membraneless parent fit; PAC broad acronym is not a unique exact synonym.
    Nuclear/cytoplasmic possibilities prevent an exclusive cytoplasm placement. INQ/CytoQ
    overlap and severe-heat NuRs are not collapsed into exact identity.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-go-terms
  - micro-boronat2023
  - micro-cabrera2020
- assessment_id: micro-protein_aggregate_center-a5
  area: representation
  topic: Chaperone identities and conditional necessity
  outcome: supported
  summary: Hsp42Q12329/BTN2P53286/Hsp104P31539 are reviewed559292 references. Joint
    BTN2/HSP42 loss does not assign single-gene universal necessity; W303-specific
    BTN2 phenotype supports only conditional role, while Hsp104 is dispensable for
    formation but participates in clearance. Domain-only BTN2 and broad ClpA/B groundings
    remain deferred.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-boronat2023
  - micro-uniprot-Q12329
  - micro-uniprot-P53286
  - micro-uniprot-P31539
  - micro-matches-Q12329
  - micro-matches-P53286
  - micro-matches-P31539
  - micro-entry-IPR031107
  - micro-entry-IPR062150
  - micro-entry-IPR001270
  - micro-entry-IPR050130
  - micro-reviewed-HSP42
  - micro-reviewed-BTN2
  - micro-reviewed-HSP104
- assessment_id: micro-protein_aggregate_center-a6
  area: graph
  topic: Assembly graph and combined mutant scope
  outcome: supported
  summary: 37C reporter PAC assembly, BTN2/HSP42 combined impairment and CHX at induction
    are supported in the specified backgrounds. Rho1.C17R-GFP is engineered and C-terminal
    tagging disrupts geranylgeranylation. No42C NuR mechanism or general endogenous-protein
    universality is inferred.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-boronat2023
- assessment_id: micro-protein_aggregate_center-a7
  area: graph
  topic: Protection and degradation graph
  outcome: supported
  summary: At37C CHX or combined small-chaperone loss accelerates reporter turnover
    with immunoblot support;25C is a distinct control. Foci loss alone is not proteolysis,
    and Ydj1/Rsp5 phenotype does not automatically make them structural components.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-boronat2023
- assessment_id: micro-protein_aggregate_center-a8
  area: graph
  topic: Recovery graph and timing
  outcome: supported
  summary: After37C30min assembly, return to25C with CHX added for recovery permits
    clearance; HSP104 deletion impairs this and delays chronic-heat reporter degradation.
    Recovery CHX timing is distinct from formation blockade.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-boronat2023
- assessment_id: micro-protein_aggregate_center-a9
  area: scope
  topic: Experimental yeasts and reference identity
  outcome: supported
  summary: W303, BY4741 and S.pombe972 claims match the2023 study. Reference protein
    accession taxon559292 is not represented as proof of each experimental strain
    sequence.2020 fission-yeast conclusions remain abstract-scoped.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-boronat2023
  - micro-cabrera2020
  - micro-tax-4932
  - micro-tax-4896
  - micro-tax-559292
- assessment_id: micro-protein_aggregate_center-a10
  area: provenance
  topic: Tracked Figure2 pixels, provenance and scope
  outcome: supported
  summary: Tracked bytes match PMC package MD5 and CC BY4.0 permissions; direct pixel
    inspection confirms separate Btn2/Hsp42/Hsp104 reporter rows and temperature/time
    panels. Caption avoids treating panel recruitment as universal necessity or three-way
    colocalization.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-boronat2023
  - micro-pac-image
  - micro-package-PMC10342647
- assessment_id: micro-protein_aggregate_center-a11
  area: evidence
  topic: Versioned dataset provenance
  outcome: supported
  summary: Exact dataset DOI/title/creator/issued date/license resolve in DataCite.
    No claim of raw-data verification or complete file-manifest inspection is made.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-pac-dataset
- assessment_id: micro-protein_aggregate_center-a12
  area: completeness
  topic: Scientific limitations and current verdict
  outcome: supported
  summary: No material new defect observed. Hsp16/Mas5/Ssa2 follow-up and heterogeneous
    cargo lack of fixed stoichiometry are explicit; the record does not claim exhaustive
    PAC proteomics. Current verdict remains pass_with_limitations.
  target_ids:
  - GO:0140453
  evidence_ids:
  - micro-record-protein_aggregate_center
  - micro-cabrera2020
  - micro-boronat2023
- assessment_id: micro-actinophryid_extrusome-a4
  area: identity
  topic: Local extrusome identity and membrane boundaries
  outcome: supported
  summary: The membrane-bounded Actinophrys granule has a defensible local identity
    and broad intracellular-membrane-bounded parent. Golgi-origin secretory-granule
    and parasite food-vacuole GO terms are not exact identities. Current bounded GO
    label search is negative only within its literal query.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-go-terms
  - micro-extrusome-go-search
  - micro-hausmann1982
  - micro-kakuta2008
- assessment_id: micro-actinophryid_extrusome-a5
  area: representation
  topic: GP40 scope, sequence candidates and membrane component
  outcome: supported
  summary: Primary2001 abstract establishes secretory GP40 association. Current unreviewed
    gp40-1/-2 entries and broad beta-glucanase/lectin domains do not assign a localized
    exact protein family. Deleted IPR050546 is not valid grounding. Label-only GP40
    and membrane with UNKNOWN formation necessity are appropriate limits.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-sakaguchi2001
  - micro-uniprot-B2NIF0
  - micro-uniprot-B2NIF1
  - micro-matches-B2NIF0
  - micro-matches-B2NIF1
  - micro-entry-IPR000757
  - micro-entry-IPR013320
  - micro-deleted-IPR050546
- assessment_id: micro-actinophryid_extrusome-a6
  area: graph
  topic: 'Stale refresh: GP40 residence and adhesion edges'
  outcome: supported
  summary: Both new component-anchored GP40 edges follow the primary2001 abstract;
    the graph does not conflate residence or adhesion activity with organelle-formation
    necessity. No accession is guessed for the assayed protein.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-sakaguchi2001
  - micro-native-actinophryid_extrusome-causal
  - micro-original-validation-inputs
- assessment_id: micro-actinophryid_extrusome-a7
  area: graph
  topic: Existing membrane-donation graph
  outcome: supported
  summary: 1982 abstract directly supports extrusome expansion/fusion with each other
    and plasma membrane during funnel-pseudopod enclosure, providing food-vacuole
    membrane. Generic cell/process nodes preserve this observational edge scope without
    a hypothetical fusogen.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-hausmann1982
- assessment_id: micro-actinophryid_extrusome-a8
  area: evidence
  topic: Pharmacology is not component localization
  outcome: supported
  summary: 2008 author-manuscript Results/Discussion support calcium/ConA perturbation
    context, while ionophore depletion is speculative and damage/other glycoconjugates
    remain alternatives. No unique channel or receptor member is inferred.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-kakuta2008
- assessment_id: micro-actinophryid_extrusome-a9
  area: scope
  topic: Canonical example versus COMMON frequency
  outcome: concern
  summary: 'Actinophrys sol canonical identity is supported. The inherited minor/provisional
    finding remains: evidence for organelle abundance in studied cells does not establish
    the encoded taxon-wide COMMON frequency. Full1998 text remains unread; variability
    is not demonstrated.'
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-presence-enum
  - micro-sakaguchi1998
  - micro-sakaguchi2001
  - micro-tax-238771
  - micro-prior-actinophryid_extrusome
- assessment_id: micro-actinophryid_extrusome-a10
  area: provenance
  topic: No claimed image or quantitative morphology inventory
  outcome: not_applicable
  summary: This target contains no image or physical-measurement inventory to validate.
    No hypothetical image deficiency or molecular inventory is invented.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
- assessment_id: micro-actinophryid_extrusome-a11
  area: completeness
  topic: Current verdict and exact predecessor
  outcome: concern
  summary: Current needs_curation verdict retains only the existing minor/provisional
    presence-abundance issue with exact predecessor20261021T104743Z-actinophryid-extrusome-audit/F1.
    Other scientific uncertainties are explicit and do not justify new findings.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-prior-actinophryid_extrusome
  - micro-sakaguchi1998
  - micro-presence-enum
- assessment_id: septin-anammoxosome-schema
  area: schema
  topic: Native schema, rendering and frozen-input integrity
  outcome: supported
  summary: Original bundle validates and renders exactly; frozen target content matches
    its original revision. Local root-run protein checks pass within their explicitly
    limited inventory scopes. Staleness is assessed separately from schema validity.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-original-validation-anammoxosome
  - septin-native-anammoxosome-verify
  - septin-native-anammoxosome-causal
  - septin-record-anammoxosome
- assessment_id: septin-anammoxosome-adapter
  area: scope
  topic: Structured-source applicability and available taxon coverage
  outcome: not_applicable
  summary: The record names specific molecular actors and pathways. Applicability
    was assessed using the current complete catalogue; no target-matched organism/dataset
    exists. Thus downstream gene/module queries are not applicable. Historical runner
    unavailability is separately disclosed and absence of expression claims is not
    the basis.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-record-anammoxosome
  - septin-native-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner-unavailable
- assessment_id: septin-anammoxosome_membrane-schema
  area: schema
  topic: Native schema, rendering and frozen-input integrity
  outcome: supported
  summary: Original bundle validates and renders exactly; frozen target content matches
    its original revision. Local root-run protein checks pass within their explicitly
    limited inventory scopes. Staleness is assessed separately from schema validity.
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  evidence_ids:
  - septin-original-validation-anammoxosome_membrane
  - septin-native-anammoxosome_membrane-verify
  - septin-native-anammoxosome_membrane-causal
  - septin-record-anammoxosome_membrane
- assessment_id: septin-anammoxosome_membrane-adapter
  area: scope
  topic: Structured-source applicability and available taxon coverage
  outcome: not_applicable
  summary: The record names hydrazine/anammox metabolism despite its material-only
    protein inventory. Applicability was assessed using the current complete catalogue;
    no target-matched organism/dataset exists. Thus downstream gene/module queries
    are not applicable. Historical runner unavailability is separately disclosed and
    absence of expression claims is not the basis.
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  evidence_ids:
  - septin-record-anammoxosome_membrane
  - septin-native-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner-unavailable
- assessment_id: septin-apicoplast-schema
  area: schema
  topic: Native schema, rendering and frozen-input integrity
  outcome: supported
  summary: Original bundle validates and renders exactly; frozen target content matches
    its original revision. Local root-run protein checks pass within their explicitly
    limited inventory scopes. Staleness is assessed separately from schema validity.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-original-validation-apicoplast
  - septin-native-apicoplast-verify
  - septin-native-apicoplast-causal
  - septin-record-apicoplast
- assessment_id: septin-apicoplast-adapter
  area: scope
  topic: Structured-source applicability and available taxon coverage
  outcome: not_applicable
  summary: The record names specific molecular actors and pathways. Applicability
    was assessed using the current complete catalogue; no target-matched organism/dataset
    exists. Thus downstream gene/module queries are not applicable. Historical runner
    unavailability is separately disclosed and absence of expression claims is not
    the basis.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-native-review-policy
  - septin-current-adapter-catalogue
  - septin-historical-adapter-runner-unavailable
- assessment_id: septin-anammoxosome-identity
  area: identity
  topic: Organelle identity and refreshed membrane parthood
  outcome: supported
  summary: GO0044222 is the whole intracellular compartment; current reciprocal has_part
    points to the separately maintained ladderane membrane. Native GO definition,
    membrane record and de Almeida localization study support the boundary. The added
    history and parthood do not correct older reaction, necessity or source-attribution
    defects.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-record-anammoxosome
  - septin-record-anammoxosome_membrane
  - septin-root20-sources-anammoxosome-go
  - septin-root20-sources-legacy-PMC4524196
- assessment_id: septin-anammoxosome-taxa
  area: scope
  topic: Taxon scope and Kuenenia example
  outcome: supported
  summary: Rare occurrence within the broad Bacteria/Planctomycetota rows is explicitly
    limited to anammox lineages. Kuenenia174633 is the source-specific immunolocalization
    organism. Current corrected taxon spelling and historical synonym resolve to that
    same taxon.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-root20-sources-NCBITaxon-2
  - septin-root20-sources-NCBITaxon-203682
  - septin-root20-sources-NCBITaxon-174633
  - septin-root20-sources-legacy-PMC4524196
- assessment_id: septin-anammoxosome-metabolism
  area: evidence
  topic: HZS reaction and HDH versus HOX role
  outcome: concern
  summary: Current HZS electron-source wording and grouped HDH/HAO role remain unsupported
    as encoded; retain original F1/F2. The Q1PX48 reviewed side reaction does not
    turn HOX into physiological HDH.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-record-anammoxosome
  - septin-root20-sources-legacy-PMC4524196
  - septin-root20-sources-UniProtKB-Q1PX48
- assessment_id: septin-anammoxosome-necessity
  area: evidence
  topic: Constitution versus metabolic or formation requirement
  outcome: concern
  summary: The bounding membrane is constitutive, but cited enzyme catalysis and localization
    do not demonstrate that HZS or the entire HDH/HAO cohort is essential for organelle
    formation. Retain original F3 without asserting dispensability.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-record-anammoxosome
  - septin-native-curation-policy
  - septin-root20-sources-legacy-PMC4524196
- assessment_id: septin-anammoxosome-carriers
  area: evidence
  topic: Carrier model and edge-level localization scope
  outcome: concern
  summary: The proposed quinone-linked energetic model is retained as a model. The
    current membrane-carrier localization edge misuses a study of soluble matrix enzymes;
    original F4 remains. Exact carrier machinery and formation dependencies stay unresolved.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-record-anammoxosome
  - septin-root20-sources-legacy-PMC4524196
  - septin-root20-sources-doi-10.1111_1574-6976.12014
  - septin-current-kartal-indexed-review
- assessment_id: septin-anammoxosome-protein-identities
  area: grounding
  topic: Concrete protein identity and grouped class scope
  outcome: supported
  summary: The three unreviewed HZS examples resolve to named hzs subunits in taxon174633.
    HDH Q1PYC5 is unreviewed; Q1PX48 is reviewed hao/hox. HZS is a multisubunit complex
    and heterogeneous HDH/HAO and carrier groups are not assigned a single whole-group
    family from one example. Functional conflation is separately retained as F2.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-root20-sources-UniProtKB-A0A2C9CHN2
  - septin-root20-sources-UniProtKB-A0A2C9CH14
  - septin-root20-sources-UniProtKB-A0A2C9CHM2
  - septin-root20-sources-UniProtKB-Q1PYC5
  - septin-root20-sources-UniProtKB-Q1PX48
  - septin-native-anammoxosome-causal
- assessment_id: septin-anammoxosome-attribution
  area: evidence
  topic: Exact author/year/source correspondence
  outcome: concern
  summary: PMID15098544 is van Niftrik2004, a review; Sinninghe Damste2002 is PMID12384695.
    DOI10.1128/JB.00186-15 is de Almeida2015. Both currently cited sources remain
    relevant, but repeated attributions require correction.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-record-anammoxosome
  - septin-root20-sources-PMID-15098544
  - septin-root20-sources-PMID-12384695
  - septin-root20-sources-PMID-25962914
- assessment_id: septin-anammoxosome_membrane-attribution
  area: evidence
  topic: Exact author/year/source correspondence
  outcome: concern
  summary: PMID15098544 is van Niftrik2004, a review; Sinninghe Damste2002 is PMID12384695.
    DOI10.1128/JB.00186-15 is de Almeida2015. Both currently cited sources remain
    relevant, but repeated attributions require correction.
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  evidence_ids:
  - septin-record-anammoxosome_membrane
  - septin-root20-sources-PMID-15098544
  - septin-root20-sources-PMID-12384695
  - septin-root20-sources-PMID-25962914
- assessment_id: septin-anammoxosome_membrane-identity
  area: identity
  topic: Distinct local membrane identity and current reciprocal boundary
  outcome: supported
  summary: The local identifier denotes the bounding membrane, not the whole GO0044222
    compartment. GO0016020 is a broader parent. The neighboring whole organelle now
    reciprocates part_of with has_part; exact OLS lookup is bounded and does not establish
    universal ontology absence.
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  evidence_ids:
  - septin-record-anammoxosome_membrane
  - septin-record-anammoxosome
  - septin-root20-sources-anammox-membrane-go
  - septin-root20-sources-ols-exact-anammoxosome-membrane
  - septin-root20-sources-PMID-15098544
- assessment_id: septin-anammoxosome_membrane-material
  area: grounding
  topic: Collective bilayer constituent and lipid scope
  outcome: supported
  summary: The generic ladderane-containing lipid bilayer is a collective constitutive
    boundary; it is not equivalent to one lipid molecule or a protein family. No new
    chemical accession, exact lipid inventory or universal permeability coefficient
    is inferred from the available sources.
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  evidence_ids:
  - septin-record-anammoxosome_membrane
  - septin-root20-sources-PMID-15098544
  - septin-root20-sources-PMID-12384695
  - septin-native-curation-policy
- assessment_id: septin-anammoxosome_membrane-topology
  area: scope
  topic: Topology graph, metabolic confinement and source limits
  outcome: supported
  summary: The NONMECHANISTIC graph records membrane parthood and confinement of anammox
    metabolism. Named hydrazine pathway triggers coverage assessment but does not
    turn this graph into an enzyme mechanism. Proposed energy-conservation/barrier
    function is retained at review/model scope; soluble-enzyme localization does not
    prove exact membrane-carrier membership.
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  evidence_ids:
  - septin-record-anammoxosome_membrane
  - septin-root20-sources-legacy-PMC4524196
  - septin-root20-sources-doi-10.1111_1574-6976.12014
  - septin-current-kartal-indexed-review
- assessment_id: septin-anammoxosome_membrane-taxa
  area: scope
  topic: Anammox lineage and example scope
  outcome: supported
  summary: Broad taxonomic rows explicitly restrict occurrence to anammox lineages;
    the canonical example is Kuenenia174633. No unrelated covered iModulon species
    substitutes for that source-specific scope.
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  evidence_ids:
  - septin-record-anammoxosome_membrane
  - septin-root20-sources-NCBITaxon-174633
  - septin-current-adapter-catalogue
- assessment_id: septin-apicoplast-identity
  area: identity
  topic: Plastid identity and membrane constituent boundary
  outcome: supported
  summary: GO0020011 identifies the apicoplast and GO0160211 its membrane constituent.
    Frozen neighboring parthood and native GO relationships agree; the record is an
    organelle, not one imported protein.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-context-apicoplast-membrane
  - septin-apicoplast-agent-go
- assessment_id: septin-apicoplast-stale-ispg
  area: grounding
  topic: Substantive refresh of added IspG identity example
  outcome: supported
  summary: Fresh Q8IJH7 metadata verifies unreviewed status, taxon36329 and PF3D7_1022800
    locus; exact example-specific InterPro matches support IspG-family identity. The
    native query returns this entry via the locus alternative. These are computational
    identity checks, not new experimental apicoplast localization. Native causal coverage
    now covers all three declared protein nodes.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-current-Q8IJH7
  - septin-apicoplast-current-query-ispG
  - septin-apicoplast-current-matches-Q8IJH7
  - septin-native-apicoplast-causal
- assessment_id: septin-apicoplast-membranes
  area: evidence
  topic: Four membranes in the stated Plasmodium example
  outcome: supported
  summary: Lemgruber2013 Results and captions support four membranes around P. falciparum
    merozoite apicoplasts. No new pixel count, raw-tomogram reanalysis or blanket
    statement across all secondary plastids is made.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-agent-jats-PMC3662607
  - septin-apicoplast-agent-go
- assessment_id: septin-apicoplast-taxa
  area: scope
  topic: Variable apicomplexan distribution and exemplar identity
  outcome: supported
  summary: Native Apicomplexa, Toxoplasma and Plasmodium taxon identities match the
    record. Secondary review context supports variable distribution and loss in some
    lineages; no universal presence claim is encoded.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-agent-tax-5794
  - septin-apicoplast-agent-tax-5811
  - septin-apicoplast-agent-tax-5833
  - septin-apicoplast-agent-tax-508771
  - septin-apicoplast-agent-tax-36329
  - septin-apicoplast-agent-jats-PMC5406208
- assessment_id: septin-apicoplast-protein-examples
  area: grounding
  topic: Example identities versus cellular paralogs
  outcome: concern
  summary: Native accession/status checks pass for the maintained examples. However,
    B9PY98 maps to deposited Der1ER1, not apicoplast Der1Ap; original F1 remains.
    O97275 is assessed separately using its locus/peptide bridge and is not discarded
    merely because automated generic UniProt wording says ER.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-apicoplast-agent-B9PY98
  - septin-apicoplast-agent-C9WWW6
  - septin-apicoplast-agent-ena-FJ976521
  - septin-apicoplast-agent-ena-FJ976520
  - septin-agrawal2011-thesis
  - septin-apicoplast-agent-O97275
  - septin-apicoplast-agent-kalanon2009-pdf
  - septin-apicoplast-agent-ena-CAB38986
  - septin-apicoplast-agent-gene-814456
- assessment_id: septin-apicoplast-tic20-family
  area: grounding
  topic: Tic20 class-level family grounding
  outcome: concern
  summary: IPR005691 is a family and directly matches maintained S8GBF3. A missing
    reviewed species accession does not justify leaving this class ungrounded. The
    heterogeneous SELMA and metabolic-enzyme cohorts still should not be assigned
    one whole-group family.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-agent-IPR005691
  - septin-apicoplast-agent-matches-S8GBF3
  - septin-apicoplast-agent-S8GBF3
  - septin-native-curation-policy
- assessment_id: septin-apicoplast-targeting
  area: evidence
  topic: Nuclear precursor targeting and import dependency
  outcome: supported
  summary: The author-hosted Waller1998 primary paper supports targeting sequences
    and tested ACP leader sufficiency. The selected import studies support protein-import
    dependence and localization; these claims remain distinct from the pore and endogenous-modifier
    overclaims retained below.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-waller1998-author-pdf
  - septin-agrawal2011-thesis
  - septin-apicoplast-agent-jats-PMC3681736
- assessment_id: septin-apicoplast-tic20-mechanism
  area: evidence
  topic: Tic20 requirement versus direct channel action
  outcome: concern
  summary: The primary Tic20 study and reproduced author appendix support inner-membrane
    import requirement while explicitly considering accessory/regulatory roles. Current
    translocon/translocates wording over-resolves the mechanism; original F3 remains.
    This is a source-support finding, not a claim that Tic20 can never form a channel.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-current-tic20-indexed-primary
  - septin-agrawal2011-thesis
- assessment_id: septin-apicoplast-modifier
  area: evidence
  topic: Endogenous ubiquitylation modifier
  outcome: concern
  summary: Agrawal2013 directly leaves endogenous ubiquitin versus ubiquitin-like
    modifier unresolved. In-vitro activity on human ubiquitin and import phenotypes
    support machinery involvement, not the current unqualified endogenous-substrate
    assertion. Original F4 remains.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-agent-jats-PMC3681736
- assessment_id: septin-apicoplast-metabolic-scope
  area: scope
  topic: Metabolic pathways and blood-stage IPP function
  outcome: supported
  summary: Distinct imported enzyme families support a broad metabolic inventory,
    without claiming every pathway is essential at every stage. IPP rescue is explicitly
    P. falciparum asexual blood-stage evidence. Review-only heme/FAS/iron-sulfur context
    is identified as secondary, and the Annual Review source remains abstract-only.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-agent-jats-PMC3166167
  - septin-apicoplast-agent-jats-PMC2817234
  - septin-apicoplast-agent-jats-PMC5406208
  - septin-apicoplast-agent-doi-10.1146_annurev-micro-092412-155741
- assessment_id: septin-apicoplast-necessity
  area: evidence
  topic: Organelle constitution and protein requirements
  outcome: unknown
  summary: Collective envelope membranes are constitutive. Current UNKNOWN necessity
    for named protein cohorts avoids extending import, maintenance, growth or stage-specific
    metabolic dependence into a universal formation requirement; no new necessity
    assignment is proposed.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-native-curation-policy
  - septin-apicoplast-agent-jats-PMC3662607
  - septin-agrawal2011-thesis
  - septin-apicoplast-agent-jats-PMC3166167
- assessment_id: septin-anammoxosome-verdict
  area: completeness
  topic: Current scoped scientific verdict and retained lineage
  outcome: concern
  summary: needs_curation remains warranted for this target. All original findings
    are preserved at exact prior review/finding lineage; current checks and stale-input
    refresh do not repair domain content. Record edits are deferred to separately
    authorized curation.
  target_ids:
  - GO:0044222
  evidence_ids:
  - septin-record-anammoxosome
  - septin-original-anammoxosome
  - septin-current-kartal-indexed-review
  - septin-native-curation-policy
  - septin-root20-sources-PMID-12384695
  - septin-root20-sources-PMID-15098544
  - septin-root20-sources-PMID-25962914
  - septin-root20-sources-UniProtKB-Q1PX48
  - septin-root20-sources-doi-10.1111_1574-6976.12014
  - septin-root20-sources-legacy-PMC4524196
- assessment_id: septin-anammoxosome_membrane-verdict
  area: completeness
  topic: Current scoped scientific verdict and retained lineage
  outcome: concern
  summary: needs_curation remains warranted for this target. All original findings
    are preserved at exact prior review/finding lineage; current checks and stale-input
    refresh do not repair domain content. Record edits are deferred to separately
    authorized curation.
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  evidence_ids:
  - septin-record-anammoxosome_membrane
  - septin-original-anammoxosome_membrane
  - septin-root20-sources-PMID-12384695
  - septin-root20-sources-PMID-15098544
  - septin-root20-sources-PMID-25962914
- assessment_id: septin-apicoplast-verdict
  area: completeness
  topic: Current scoped scientific verdict and retained lineage
  outcome: concern
  summary: needs_curation remains warranted for this target. All original findings
    are preserved at exact prior review/finding lineage; current checks and stale-input
    refresh do not repair domain content. Record edits are deferred to separately
    authorized curation.
  target_ids:
  - GO:0020011
  evidence_ids:
  - septin-record-apicoplast
  - septin-original-apicoplast
  - septin-agrawal2011-thesis
  - septin-apicoplast-agent-B9PY98
  - septin-apicoplast-agent-C9WWW6
  - septin-apicoplast-agent-IPR005691
  - septin-apicoplast-agent-S8GBF3
  - septin-apicoplast-agent-ena-FJ976520
  - septin-apicoplast-agent-ena-FJ976521
  - septin-apicoplast-agent-jats-PMC3681736
  - septin-apicoplast-agent-matches-S8GBF3
  - septin-current-tic20-indexed-primary
- assessment_id: current-input-comparison
  area: provenance
  topic: Complete frozen-input comparison and bounded refresh
  outcome: supported
  summary: 6 of ten original target hashes differ from current main. The changed content
    is substantively reassessed in the target-specific assessments; original observations
    remain historical and unchanged. All current target and used context bytes are
    frozen.
  target_ids:
  - GO:0034515
  - GO:0140453
  - GO:0033985
  - GO:0033102
  - cellstructuremech:actinophryid_extrusome
  - GO:0044222
  - cellstructuremech:anammoxosome_membrane
  - GO:0020026
  - GO:0030668
  - GO:0020011
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
- finding_id: plaque-t2-F1
  issue_key: acidocalcisome_lumen-bacterial-identity-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The sole canonical bacterial example omits an explicit unresolved identity
    dispute
  description: The canonical A. tumefaciens note states that its volutin granules
    establish a lumenal storage compartment, without acknowledging the later disagreement.
    The 2003 abstract supports the original interpretation; Frank and Jendrossek2020
    instead distinguish C58 DAPI-positive polyphosphate granules from HppA/MitoTracker-positive
    structures using fluorescence and mutants, while Docampo2024 explicitly challenges
    that interpretation through prior membrane observations and a short-polyphosphate/DAPI
    limitation. The omission is confirmed, not a conclusion that bacterial acidocalcisomes
    do not exist. It materially affects the sole canonical example and the bacterial
    compartment interpretation. The record should retain both source positions and
    the unresolved strain/preparation and marker limits.
  target_ids:
  - GO:0033985
  field_paths:
  - canonical_examples[0].note
  - taxonomic_distribution[0].note
  - evidence
  - discussions
  evidence_ids:
  - plaque-current-2
  - plaque-acidocalcisome-agent-doi-2003
  - plaque-acidocalcisome-agent-pmc2020-native
  - plaque-acidocalcisome-agent-pmc2024-native
  normalization_reason: Major because the central sole canonical example presents
    disputed compartment identity as settled; the required correction is scoped evidence
    reconciliation, not deletion of the taxon or reversal of the ontology definition.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    role: maintained scientific record
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104741Z-acidocalcisome-lumen-audit
    finding_id: F1
  native_severity: major
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2634
- finding_id: plaque-t2-F2
  issue_key: acidocalcisome_lumen-docampo2024-author
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The 2024 review has one author, Roberto Docampo
  description: The target attributes DOI10.1128/MMBR.00042-23 to Docampo and Huang2024.
    Native bibliographic metadata and the article byline identify Roberto Docampo
    alone. Correct the attribution in every maintained note for this source; the valid
    DOI and collection year2024 are unchanged.
  target_ids:
  - GO:0033985
  field_paths:
  - evidence
  evidence_ids:
  - plaque-current-2
  - plaque-acidocalcisome-agent-doi-2024
  - plaque-acidocalcisome-agent-pmc2024-native
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    role: maintained scientific record
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104741Z-acidocalcisome-lumen-audit
    finding_id: F2
  native_severity: minor
  normalization_reason: 'Minor because this is a bounded author-attribution/provenance
    correction: native bibliographic metadata and the article byline identify Roberto
    Docampo alone, while the DOI and publication year remain valid and the biological
    claim scope is unchanged.'
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2635
- finding_id: plaque-t3-F1
  issue_key: acidocalcisome_membrane-bacterial-identity-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: The sole canonical bacterial example omits an explicit unresolved identity
    dispute
  description: The canonical A. tumefaciens note states that its volutin granules
    were shown to be membrane-bound acidocalcisome-like organelles, without acknowledging
    the later disagreement. The 2003 abstract supports the original interpretation;
    Frank and Jendrossek2020 instead distinguish C58 DAPI-positive polyphosphate granules
    from HppA/MitoTracker-positive structures using fluorescence and mutants, while
    Docampo2024 explicitly challenges that interpretation through prior membrane observations
    and a short-polyphosphate/DAPI limitation. The omission is confirmed, not a conclusion
    that bacterial acidocalcisomes do not exist. It materially affects the sole canonical
    example and the bacterial compartment interpretation. The record should retain
    both source positions and the unresolved strain/preparation and marker limits.
  target_ids:
  - GO:0033102
  field_paths:
  - canonical_examples[0].note
  - taxonomic_distribution[0].note
  - evidence
  - discussions
  evidence_ids:
  - plaque-current-3
  - plaque-acidocalcisome-agent-doi-2003
  - plaque-acidocalcisome-agent-pmc2020-native
  - plaque-acidocalcisome-agent-pmc2024-native
  normalization_reason: Major because the central sole canonical example presents
    disputed compartment identity as settled; the required correction is scoped evidence
    reconciliation, not deletion of the taxon or reversal of the ontology definition.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104742Z-acidocalcisome-membrane-audit
    finding_id: F1
  native_severity: major
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2636
- finding_id: plaque-t3-F2
  issue_key: acidocalcisome_membrane-docampo2024-author
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: The 2024 review has one author, Roberto Docampo
  description: The target attributes DOI10.1128/MMBR.00042-23 to Docampo and Huang2024.
    Native bibliographic metadata and the article byline identify Roberto Docampo
    alone. Correct the attribution in every maintained note for this source; the valid
    DOI and collection year2024 are unchanged. The new current edge6 repeats the same
    inaccurate author attribution; the supported new transport relationship does not
    resolve this provenance defect.
  target_ids:
  - GO:0033102
  field_paths:
  - components[2].evidence
  - functions[1].evidence
  - evidence
  - causal_graphs[0].edges[2].evidence
  - causal_graphs[0].edges[6].evidence
  evidence_ids:
  - plaque-current-3
  - plaque-acidocalcisome-agent-doi-2024
  - plaque-acidocalcisome-agent-pmc2024-native
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104742Z-acidocalcisome-membrane-audit
    finding_id: F2
  native_severity: minor
  normalization_reason: 'Minor because this is a bounded author-attribution/provenance
    correction: native bibliographic metadata and the article byline identify Roberto
    Docampo alone, while the DOI and publication year remain valid and the biological
    claim scope is unchanged.'
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2637
- finding_id: micro-F1
  issue_key: actinophryid-extrusome-presence-abundance
  category: scope
  severity: minor
  status: open
  certainty: provisional
  title: Separate cellular abundance from encoded taxonomic frequency
  description: COMMON encodes occurrence in most taxon members, while the cited1998
    Summary and distribution note establish abundant organelles in examined cells.
    This remains a bounded provenance gap, not demonstrated strain variability. The
    canonical species example is supported; full1998 text remains unread.
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  field_paths:
  - taxonomic_distribution[taxon_id=NCBITaxon:238771].presence
  - taxonomic_distribution[taxon_id=NCBITaxon:238771].note
  evidence_ids:
  - micro-record-actinophryid_extrusome
  - micro-presence-enum
  - micro-sakaguchi1998
  - micro-kakuta2008
  - micro-tax-238771
  - micro-prior-actinophryid_extrusome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; docs/record-reviews.md:Verdict And Severity
  native_severity: minor
  normalization_reason: A bounded provenance or scope correction preserves the structure
    identity.
  previous_occurrences:
  - review_id: 20261021T104743Z-actinophryid-extrusome-audit
    finding_id: F1
    repository: CultureBotAI/CellStructureMech
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2639
- finding_id: septin-S2357-F1
  issue_key: anammoxosome-hzs-electron-source
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate ammonium substrate from the HZS electron supply
  description: The current HZS role and edge describe ammonium-derived reducing equivalents.
    The inspected 2015 primary Introduction separates ammonium substrate from the
    three-electron input and recycles electrons released by hydrazine oxidation. The
    wording still misstates the electron-transfer loop.
  target_ids:
  - GO:0044222
  field_paths:
  - components[component_id=hydrazine_synthase].role
  - causal_graphs[graph_id=hydrazine_loop_energy_conservation].edges[subject=hzs,object=ammonium].description
  - causal_graphs[graph_id=hydrazine_loop_energy_conservation].edges[subject=hzs,object=ammonium].evidence
  evidence_ids:
  - septin-record-anammoxosome
  - septin-root20-sources-legacy-PMC4524196
  - septin-root20-sources-doi-10.1111_1574-6976.12014
  - septin-native-curation-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; docs/record-reviews.md:Verdict And Severity
  native_severity: major
  normalization_reason: A material claim or encoded scope needs correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104744Z-anammoxosome-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2640
- finding_id: septin-S2357-F2
  issue_key: anammoxosome-hdh-hox-functional-conflation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Keep HDH and HOX physiological reactions separate
  description: The grouped HDH/HAO cohort and Q1PX48 example still receive a universal
    hydrazine-to-N2 role. The primary source distinguishes HDH/kustc0694 from HOX/kustc1061
    and an HAO-like pair of unknown function; reviewed Q1PX48 qualifies its hydrazine
    side reaction as probably nonphysiological.
  target_ids:
  - GO:0044222
  field_paths:
  - components[component_id=hydrazine_dehydrogenase].role
  - components[component_id=hydrazine_dehydrogenase].protein_examples[uniprot_id=UniProtKB:Q1PX48].role
  - causal_graphs[graph_id=hydrazine_loop_energy_conservation].nodes[node_id=hdh].component_ref
  evidence_ids:
  - septin-record-anammoxosome
  - septin-root20-sources-legacy-PMC4524196
  - septin-root20-sources-UniProtKB-Q1PX48
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; docs/record-reviews.md:Verdict And Severity
  native_severity: major
  normalization_reason: A material claim or encoded scope needs correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104744Z-anammoxosome-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2641
- finding_id: septin-S2357-F3
  issue_key: anammoxosome-enzyme-assembly-essentiality
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Do not infer organelle formation requirements from catabolic activity
  description: HZS and the grouped HDH/HAO constituent class remain ESSENTIAL. Catalysis/localization
    evidence does not demonstrate organelle-formation failure after loss; repository
    essentiality concerns formation. This bounded source-support finding does not
    assert dispensability.
  target_ids:
  - GO:0044222
  field_paths:
  - components[component_id=hydrazine_synthase].essentiality
  - components[component_id=hydrazine_dehydrogenase].essentiality
  evidence_ids:
  - septin-record-anammoxosome
  - septin-root20-sources-legacy-PMC4524196
  - septin-native-curation-policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; docs/record-reviews.md:Verdict And Severity
  native_severity: major
  normalization_reason: A material claim or encoded scope needs correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104744Z-anammoxosome-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2642
- finding_id: septin-S2357-F4
  issue_key: anammoxosome-membrane-carrier-localization-source
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Keep soluble-enzyme localization distinct from membrane-carrier membership
  description: The graph links its membrane-associated carrier cohort to the 2015
    localization experiment, whose Discussion explicitly identifies all measured complexes
    as soluble. That assay cannot establish the encoded membrane-carrier localization.
    The secondary review provides a proposed model with unresolved exact carriers.
  target_ids:
  - GO:0044222
  field_paths:
  - causal_graphs[graph_id=hydrazine_loop_energy_conservation].nodes[node_id=electron_carriers].component_ref
  - causal_graphs[graph_id=hydrazine_loop_energy_conservation].edges[subject=electron_carriers,object=anammoxosome]
  evidence_ids:
  - septin-record-anammoxosome
  - septin-root20-sources-legacy-PMC4524196
  - septin-current-kartal-indexed-review
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; docs/record-reviews.md:Verdict And Severity
  native_severity: major
  normalization_reason: A material claim or encoded scope needs correction.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104744Z-anammoxosome-audit
    finding_id: F4
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2643
- finding_id: septin-S2357-F5
  issue_key: anammoxosome-ladderane-citation-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the ladderane-paper and localization-paper attribution
  description: 'PMID15098544 is van Niftrik et al.2004, The anammoxosome: an intracytoplasmic
    compartment in anammox bacteria, not the stated Sinninghe Damste2002 lipid-discovery
    paper. The 2002 paper is independently identified by PMID12384695. DOI10.1128/JB.00186-15
    is de Almeida et al.2015, not a first-author Kartal paper. Both currently cited
    works are relevant, but their repeated author/year notes misidentify the source
    and evidence tier.'
  target_ids:
  - GO:0044222
  field_paths:
  - components[].evidence[reference=PMID:15098544].notes
  - evidence[reference=PMID:15098544].notes
  - evidence[reference=DOI:10.1128/JB.00186-15].notes
  - causal_graphs[].edges[].evidence[reference=DOI:10.1128/JB.00186-15].notes
  - components[].evidence[reference=DOI:10.1128/JB.00186-15].notes
  evidence_ids:
  - septin-record-anammoxosome
  - septin-root20-sources-PMID-15098544
  - septin-root20-sources-PMID-12384695
  - septin-root20-sources-PMID-25962914
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; docs/record-reviews.md:Verdict And Severity
  native_severity: minor
  normalization_reason: A bounded provenance or scope correction preserves the structure
    identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104744Z-anammoxosome-audit
    finding_id: F5
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2644
- finding_id: septin-S2357-F6
  issue_key: anammoxosome-membrane-ladderane-citation-attribution
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the ladderane-paper and localization-paper attribution
  description: 'PMID15098544 is van Niftrik et al.2004, The anammoxosome: an intracytoplasmic
    compartment in anammox bacteria, not the stated Sinninghe Damste2002 lipid-discovery
    paper. The 2002 paper is independently identified by PMID12384695. DOI10.1128/JB.00186-15
    is de Almeida et al.2015, not a first-author Kartal paper. Both currently cited
    works are relevant, but their repeated author/year notes misidentify the source
    and evidence tier.'
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  field_paths:
  - components[].evidence[reference=PMID:15098544].notes
  - evidence[reference=PMID:15098544].notes
  - evidence[reference=DOI:10.1128/JB.00186-15].notes
  - functions[].evidence[reference=PMID:15098544].notes
  - causal_graphs[].edges[].evidence[reference=DOI:10.1128/JB.00186-15].notes
  - discussions[].evidence[reference=PMID:15098544].notes
  evidence_ids:
  - septin-record-anammoxosome_membrane
  - septin-root20-sources-PMID-15098544
  - septin-root20-sources-PMID-12384695
  - septin-root20-sources-PMID-25962914
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome_membrane.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components; docs/record-reviews.md:Verdict And Severity
  native_severity: minor
  normalization_reason: A bounded provenance or scope correction preserves the structure
    identity.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104745Z-anammoxosome-membrane-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2645
- finding_id: septin-S2357-F7
  issue_key: apicoplast-der1-er-paralog-example
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: The Toxoplasma Der1 example is the ER paralog
  description: B9PY98 is linked by native ENA/UniProt records to Der1ER1 FJ976521/ACU32856.1.
    The author primary-study chapter distinguishes apicoplast Der1Ap FJ976520/ACU32855.1,
    now C9WWW6. An identity-only disclaimer does not make the ER paralog an appropriate
    concrete example of apicoplast SELMA.
  target_ids:
  - GO:0020011
  field_paths:
  - components#selma_erad_import_machinery.protein_examples
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-agent-B9PY98
  - septin-apicoplast-agent-C9WWW6
  - septin-apicoplast-agent-ena-FJ976521
  - septin-apicoplast-agent-ena-FJ976520
  - septin-agrawal2011-thesis
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: Major because an explicit protein example resolves to the
    wrong cellular paralog of the maintained component.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104747Z-apicoplast-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2646
- finding_id: septin-S2357-F8
  issue_key: apicoplast-tic20-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: The Tic20 protein class has an available family grounding
  description: IPR005691 is a family entry for Tic20 and is matched by the maintained
    S8GBF3 example. The present label-only rationale combines lack of an exact family
    with absence of a reviewed species accession. Family-class grounding does not
    require a Swiss-Prot entry or a localization-specific family.
  target_ids:
  - GO:0020011
  field_paths:
  - components#tic20_inner_membrane_translocon.grounding_status
  - components#tic20_inner_membrane_translocon.grounding_notes
  - discussions#protein_import_grounding
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-agent-IPR005691
  - septin-apicoplast-agent-matches-S8GBF3
  - septin-apicoplast-agent-S8GBF3
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: Minor because the biological class is correct but a verified
    class-level grounding is omitted for an inapplicable reason.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104747Z-apicoplast-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2647
- finding_id: septin-S2357-F9
  issue_key: apicoplast-tic20-direct-channel-overclaim
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Direct Tic20 translocation exceeds the cited experiment
  description: The current Tic20 label, role and translocates edge encode direct channel
    action. The cited primary Results passage, independently inspected in the author
    appendix, establishes inner-membrane localization/import dependence but explicitly
    discusses accessory/regulatory alternatives. Retain the import requirement without
    over-resolving that mechanism.
  target_ids:
  - GO:0020011
  field_paths:
  - components#tic20_inner_membrane_translocon.label
  - components#tic20_inner_membrane_translocon.role
  - causal_graphs#bipartite_leader_apicoplast_import.description
  - causal_graphs#bipartite_leader_apicoplast_import.nodes#tic20_translocon
  - causal_graphs#bipartite_leader_apicoplast_import.edges
  evidence_ids:
  - septin-record-apicoplast
  - septin-current-tic20-indexed-primary
  - septin-agrawal2011-thesis
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: Minor because the supported import function remains correct;
    the direct physical mechanism is overstated.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104747Z-apicoplast-audit
    finding_id: F3
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2648
- finding_id: septin-S2357-F10
  issue_key: apicoplast-endogenous-ubiquitin-unresolved
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: The cited study does not identify the endogenous modifier as ubiquitin
  description: The SELMA role definitively says the machinery uses ubiquitin. Agrawal2013
    demonstrates an apicoplast ubiquitylation system and enzyme activity with recombinant
    ubiquitin, but Discussion explicitly leaves endogenous ubiquitin versus a ubiquitin-like
    modifier unresolved.
  target_ids:
  - GO:0020011
  field_paths:
  - components#selma_erad_import_machinery.role
  evidence_ids:
  - septin-record-apicoplast
  - septin-apicoplast-agent-jats-PMC3681736
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: Minor because machinery involvement is supported but the exact
    endogenous modifier is not established.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261021T104747Z-apicoplast-audit
    finding_id: F4
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2649
actions:
- action_id: plaque-t2-A1
  finding_ids:
  - plaque-t2-F1
  target_ids:
  - GO:0033985
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    role: maintained scientific record
  description: Preserve both the2003 positive interpretation and2020 contrary C58
    results with the2024 counterargument, their strain/preparation/marker limits and
    an unresolved identity-conflict discussion.
  acceptance_checks:
  - Retain exact stable issue key and previous occurrence; no claim that this review
    PR edited the scientific record.
  - Use separately authorized guarded curation and append-only history for later record
    changes.
  - Recheck claim-level source scopes and run documented native schema/strict, label,
    reference, history and QC gates after later curation.
- action_id: plaque-t2-A2
  finding_ids:
  - plaque-t2-F2
  target_ids:
  - GO:0033985
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    role: maintained scientific record
  description: Correct every maintained attribution of DOI10.1128/MMBR.00042-23 to
    Roberto Docampo alone, including any newly added edge evidence; keep the valid
    DOI and collection year.
  acceptance_checks:
  - Retain exact stable issue key and previous occurrence; no claim that this review
    PR edited the scientific record.
  - Use separately authorized guarded curation and append-only history for later record
    changes.
  - Recheck claim-level source scopes and run documented native schema/strict, label,
    reference, history and QC gates after later curation.
- action_id: plaque-t3-A1
  finding_ids:
  - plaque-t3-F1
  target_ids:
  - GO:0033102
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
  description: Preserve both the2003 positive interpretation and2020 contrary C58
    results with the2024 counterargument, their strain/preparation/marker limits and
    an unresolved identity-conflict discussion.
  acceptance_checks:
  - Retain exact stable issue key and previous occurrence; no claim that this review
    PR edited the scientific record.
  - Use separately authorized guarded curation and append-only history for later record
    changes.
  - Recheck claim-level source scopes and run documented native schema/strict, label,
    reference, history and QC gates after later curation.
- action_id: plaque-t3-A2
  finding_ids:
  - plaque-t3-F2
  target_ids:
  - GO:0033102
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
  description: Correct every maintained attribution of DOI10.1128/MMBR.00042-23 to
    Roberto Docampo alone, including any newly added edge evidence; keep the valid
    DOI and collection year.
  acceptance_checks:
  - Retain exact stable issue key and previous occurrence; no claim that this review
    PR edited the scientific record.
  - Use separately authorized guarded curation and append-only history for later record
    changes.
  - Recheck claim-level source scopes and run documented native schema/strict, label,
    reference, history and QC gates after later curation.
- action_id: micro-A1
  finding_ids:
  - micro-F1
  target_ids:
  - cellstructuremech:actinophryid_extrusome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/actinophryid_extrusome.yaml
    role: maintained scientific record
  description: Retain the canonical example; either provide evidence for the encoded
    taxon-wide frequency and explain it in the distribution note, or remove the unsupported
    frequency row. Do not substitute a guessed VARIABLE value.
  acceptance_checks:
  - The justification for COMMON concerns occurrence among taxon members, not organelle
    abundance within a cell.
  - Species/culture adhesion and membrane-donation evidence remain preserved.
  - Use separately authorized guarded curation, append-only history, native focused/identifier/product
    checks and regeneration.
- action_id: septin-S2357-C1
  finding_ids:
  - septin-S2357-F1
  target_ids:
  - GO:0044222
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  description: Describe ammonium and nitric oxide as HZS substrates with a distinct
    input of reducing equivalents from the supported electron-transfer loop. Preserve
    uncertainty about the exact carrier mechanism.
  acceptance_checks:
  - Role, edge and evidence note agree with the cited balanced reaction.
  - Do not claim ammonium supplies the three electrons to its own condensation step.
  - Use separately authorized guarded curation, append-only history, native focused/identifier/product
    checks and regeneration.
- action_id: septin-S2357-C2
  finding_ids:
  - septin-S2357-F2
  target_ids:
  - GO:0044222
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  description: Separate the HDH role from HOX and other HAO-like enzymes, or explicitly
    qualify a grouped inventory so only the experimentally identified HDH supplies
    the hydrazine oxidation edge. Preserve valid localization and identity examples.
  acceptance_checks:
  - Q1PX48 is not represented as the physiological HDH based on a weak in-vitro side
    reaction.
  - Unresolved HAO-like functions remain unresolved; graph component identity matches
    the reacting enzyme.
  - Use separately authorized guarded curation, append-only history, native focused/identifier/product
    checks and regeneration.
- action_id: septin-S2357-C3
  finding_ids:
  - septin-S2357-F3
  target_ids:
  - GO:0044222
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  description: Record assembly requirements as unresolved unless direct source-specific
    organelle-formation evidence can be supplied. Keep proven localization and catalytic
    importance in their appropriate fields.
  acceptance_checks:
  - Distinguish organelle formation from anammox activity, growth and viability.
  - Do not change the collective membrane constitutional requirement merely because
    individual lipid perturbations are unknown.
  - Use separately authorized guarded curation, append-only history, native focused/identifier/product
    checks and regeneration.
- action_id: septin-S2357-C4
  finding_ids:
  - septin-S2357-F4
  target_ids:
  - GO:0044222
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  description: Retarget the localization assertion to the measured soluble enzymes,
    or provide a direct source for the membrane-associated carrier cohort. Preserve
    the explicitly proposed energy-transfer model without presenting the2015 study
    as its localization assay.
  acceptance_checks:
  - Distinguish soluble matrix enzymes from the putative membrane carriers.
  - Do not infer absence of membrane carriers from this experiment.
  - Use separately authorized guarded curation, append-only history, native focused/identifier/product
    checks and regeneration.
- action_id: septin-S2357-C5
  finding_ids:
  - septin-S2357-F5
  target_ids:
  - GO:0044222
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome.yaml
    role: maintained scientific record
  description: Correct repeated attribution and retain the2004 review where it actually
    supports the claim; cite the independently verified2002 discovery paper only where
    its inspected scope is intended. Correct the2015 first-author shorthand.
  acceptance_checks:
  - Every PMID/DOI and author/year/title combination agrees with native bibliographic
    metadata.
  - Do not replace relevant references indiscriminately or imply new full-text access
    to the2002 paper.
  - Use separately authorized guarded curation, append-only history, native focused/identifier/product
    checks and regeneration.
- action_id: septin-S2357-C6
  finding_ids:
  - septin-S2357-F6
  target_ids:
  - cellstructuremech:anammoxosome_membrane
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/anammoxosome_membrane.yaml
    role: maintained scientific record
  description: Correct repeated attribution and retain the2004 review where it actually
    supports the claim; cite the independently verified2002 discovery paper only where
    its inspected scope is intended. Correct the2015 first-author shorthand.
  acceptance_checks:
  - Every PMID/DOI and author/year/title combination agrees with native bibliographic
    metadata.
  - Do not replace relevant references indiscriminately or imply new full-text access
    to the2002 paper.
  - Use separately authorized guarded curation, append-only history, native focused/identifier/product
    checks and regeneration.
- action_id: septin-S2357-C7
  finding_ids:
  - septin-S2357-F7
  target_ids:
  - GO:0020011
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
  description: Remove B9PY98 from this apicoplast component or replace it with the
    independently verified C9WWW6/Der1Ap example and source bridge. Preserve its unreviewed
    status, correct taxon and the absence of a native gene-name field; retain other
    examples on their own evidence.
  acceptance_checks:
  - Native sequence cross-references distinguish ER and apicoplast paralogs.
  - Replacement example has exact taxon/status and source-supported alias, without
    inventing a UniProt primary gene symbol.
  - Run focused schema, strict CURIE and UniProt checks.
- action_id: septin-S2357-C8
  finding_ids:
  - septin-S2357-F8
  target_ids:
  - GO:0020011
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
  description: Ground the Tic20 protein class to InterPro:IPR005691 and update its
    note/TODO without extending that identifier to the whole import complex or heterogeneous
    SELMA system.
  acceptance_checks:
  - Native entry is Family and the example matches it.
  - Organism-specific localization and import evidence remain separate.
  - Focused validators pass.
- action_id: septin-S2357-C9
  finding_ids:
  - septin-S2357-F9
  target_ids:
  - GO:0020011
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
  description: Use Tic20 inner-membrane import component and an import-dependency
    predicate/description, or cite direct evidence for the stronger channel claim.
    Preserve the paper’s accessory/regulatory uncertainty.
  acceptance_checks:
  - Graph wording distinguishes import requirement from demonstrated pore/translocation
    activity.
  - Supported inner-membrane localization and import phenotype remain.
  - Focused validators pass.
- action_id: septin-S2357-C10
  finding_ids:
  - septin-S2357-F10
  target_ids:
  - GO:0020011
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/apicoplast.yaml
    role: maintained scientific record
  description: Describe the demonstrated ubiquitylation/ubiquitin-like machinery while
    retaining the unresolved endogenous modifier, or provide direct evidence for ubiquitin
    use in vivo.
  acceptance_checks:
  - Component wording distinguishes the tested in-vitro substrate from the endogenous
    modifier.
  - Import-perturbation and enzyme-activity evidence remain accurately scoped.
  - Focused validators pass.
limitations:
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: The2003 bacterial identification is assessed at primary abstract scope;
  the original experimental strain/accession and figure pixels were not independently
  verified. The2020 selected primary body and2024 selected secondary body preserve
  rather than settle the conflict.'
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: Docampo2005 access was limited to publisher abstract and key points.
  Docampo2024 is secondary synthesis; selected relevant sections were read, not a
  comprehensive proteomic-table or figure audit.'
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: Bougdour2013 and Masatani2013 are used at primary abstract scope. Mercier2005
  and2015 are secondary abstract context; the2005 publisher body request returned403.
  No full-body support is claimed for those sources.'
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: Gold2015 selected primary body and Table1 were inspected, but figure
  pixels and supplements were not independently audited. Experimental GT1/RH/other
  strains, ME49 reference identity and Xenopus assays remain distinct. PMC7202600
  is used solely for exact ME49 GRA17/GRA23 identity rows.'
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: Q8VPZ0 is a189-aa D44 fragment with homology-derived sodium-pump/location
  annotations, distinct from C58 Atu_1174 and the unbridged2003 assay. The maintained
  protein example explicitly says identity only; it does not prove accession-specific
  acidocalcisome membership or proton selectivity.'
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: Exact InterPro GRA1/GRA17/GRA23 attempts returned204 plus curl92 malformed-header
  failures and no readable result; these are inconclusive, not zero-hit absence evidence.
  Verified GRA2/GRA6 family entries do not ground a heterogeneous cargo cohort.'
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: The shared adapter runner failure is a reread historical00:49Z receipt,
  not a fresh execution. Current native source catalogue was fetched independently.
  No covered Agrobacterium or Toxoplasma dataset exists in that response; no unrelated
  strain modules or generated module prose support localization.'
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: Sparse lumen and dense-granule membrane records do not require invented
  molecular inventories. Collective bilayer necessity is distinct from individual
  lipid/protein assembly necessity. All four targets remain PROPOSED.'
- 'Acidocalcisome lumen/membrane and apicomplexan dense granule/membrane independent
  subreview: No repository, original bundle, record or GitHub mutation was made by
  this independent reviewer. Root owns global gates and issue deduplication/publication.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: This independent slice covers only PSG, PAC and actinophryid
  extrusome; corpus-wide gates and GitHub dedup/publication belong to root. No record,
  original bundle or GitHub mutation was performed.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: Fresh primary retrieval tiers differ: Laporte2008 main text/captions,
  Gu2017 Results/Discussion plus specified Methods/captions, Boronat2023 full main
  text/captions, selected Tang2026 PDF pages and Kakuta2008 author manuscript. No
  raw microscopy, tomograms, mass spectra or supplementary image pixels were reanalyzed.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: Sakaguchi1998 was read only through publisher Summary; direct
  requests returned challenge HTML. Sakaguchi2001 was read only through primary PubMed
  abstract; direct publisher response was403. Browser extraction cache ages are preserved
  in saved packet. Hausmann1982 uses publisher-deposited Crossref abstract; Cabrera2020
  uses PubMed abstract. No unavailable full-body access is claimed.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: Tang2026 selected physical pages1–4 and9–13 were inspected,
  not the entire35-page PDF. The record older abstract-only wording is historical
  curator access scope; fresh selected body access does not rewrite that history.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: PAC dataset check covers exact version DOI metadata, not
  a raw-data manifest. Only PAC tracked Figure2 and the linked PSG Figure2 had direct
  pixel inspection in this slice; other figure claims were checked in captions and
  body text.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: Current authority identity, entry type and protein matches
  do not independently establish organelle localization, necessity, precise mature-product
  grounding or exhaustive inventory. GP40 candidates remain unreviewed and unassigned
  to the purified localized isoform.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: All6 native protein commands returned0, but PSG/PAC each
  have3 examples and zero protein graph nodes; extrusome has no examples and one component-anchored
  NO_GENE_SYMBOLS node. Empty/limited coverage is not successful biological completeness.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: Historical adapter runner failure occurred at00:49Z, not
  during this slice. Current source catalogue was fetched at08:54:46Z and lacks matched
  yeast/Actinophrys organisms; no expression-module search/summarize result was invented.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: Closed historical#2430 is mentioned only as record-history
  context. Its grouped category predecessor was not read/frozen and no category-wide
  finding or whole issue is resolved here.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: One exploratory extraction invoked system python without
  PyYAML and stopped before reading YAML; rerun with repository .venv succeeded. This
  was an interpreter-routing error, not a failed scientific/native validation check.'
- 'Proteasome storage granule, protein aggregate center and actinophryid extrusome
  independent subreview: No gitignored repository search is used to infer a missing
  source/record. Claims about original review checks concern complete specific frozen
  files, and external negative queries are explicitly bounded.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Current
  source checks use actual 2026-11-03 fetch timestamps. The runner receipt is explicitly
  historical at00:49Z; no new adapter-runner invocation or adapter query success is
  claimed.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Direct
  PMC requests for Waller1998, Tic20/vanDooren2008 and Agrawal2009 returned challenge
  HTML; alternative full-text APIs failed. Waller was read in an author-hosted published
  PDF. Tic20 was checked via indexed primary Results and the author dissertation Appendix2;
  Der1 was checked through native deposits and Chapter3 Methods/Table3.1. These are
  not represented as new successful live PMC full-body reads.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Kartal2013
  repository PDF requests timed out and the direct publisher route failed. Fresh native
  abstract/bibliography and specifically returned indexed secondary-review passages
  were inspected instead; no fresh complete PDF read is claimed. The 2015 primary
  article supplies direct reaction and localization scope used for the current findings.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Sinninghe
  Damste2002 and van Niftrik2004 were inspected at native complete abstract/bibliographic
  scope only. The cited Annual Review2013 was likewise abstract/bibliographic scope;
  no undisclosed full-body access.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: No raw
  images, tomography, quantitative localization assays, supplementary alignments or
  experimental datasets were independently reanalysed. These targets have no maintained
  image attachments. Inspected publication captions are not pixel inspection.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Individual
  exact carriers, uncharacterized HAO paralogs, whole-organelle assembly dependencies,
  complete lipid composition and quantitative barrier efficiency remain unresolved.
  Native identifier/coverage checks cannot establish these claims.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Current
  protein metadata distinguishes unreviewed examples, native ORF fields and absent
  native gene fields. Family matches do not prove cellular localization; automated
  generic ER annotations are not substituted for the primary Der1 paralog evidence.
  O97275/Der1-2 evidence is not the full-length Der1-1 experiment.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: The source-specific
  membrane-position model for ERAD/SELMA and secondary review metabolic synthesis
  remain distinct from direct membrane-resolved experiments. No exhaustive search
  of every import-machine family or pathway representation is claimed.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Native
  taxonomy corrects historical Kuenenia spelling; the retained historical synonym
  denotes the same taxon. No taxonomy record edit is performed here.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: A bounded
  exact OLS label query and exact UniProt queries do not establish broad ontology,
  gene or homology absence. The complete official catalogue is sufficient only for
  the stated current dataset coverage assessment; it is not negative biological evidence.'
- 'Anammoxosome, anammoxosome membrane and apicoplast independent subreview: Frozen
  apicoplast membrane neighbor was used only for boundary/context, not to resolve
  all of its scientific assertions. No broader historical finding is marked resolved.
  Root-owned global QC/CI and public issue filing are reported separately with their
  actual receipts.'
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
- 'Issue #2632 tracks six stale reviews. Scientific record curation remains separately
  tracked and open. Existing validator #2514 remains open.'
- 'Current PSG retraction-exclusion evidence is assessed directly. The history reference
  to closed grouped #2430 is context only; neither that whole multi-record issue nor
  an unfrozen category finding is terminally resolved.'
- Source commit e3d2c26d3623aefa90f36c9e00ef889d6ee94ac4 is retained by tag review-base/pr2357-current-record-followup-20261103.
- CLAUDE.md is an alias of AGENTS.md; canonical regular AGENTS.md bytes are frozen.
- Used local context was frozen before assessment, including native configuration,
  graph/protein policies, verifier source, the tracked PAC figure and the requested
  apicoplast membrane and whole acidocalcisome neighbors. Neighbors are context, not
  additional targets.
- Fresh source inspection retains actual access dates. Primary bodies, abstracts,
  secondary reviews, authority metadata and actual image-pixel inspection retain distinct
  scopes.
- Native checks with empty protein inventories or zero GENE_OR_PROTEIN nodes do not
  validate molecular mechanisms or names appearing only in prose. Identity, taxon,
  membership, location, function and assembly necessity remain separate judgments.
- 'Issue #2633 tracks eight applicability defects. Four omissions and four unsupported
  expression-only rationales are distinguished from the two genuine sparse exclusions.'
- 'Issue #2638 tracks adding the required repository field to the exact extrusome
  predecessor reference in the uncommitted synthesis source; scientific content and
  lineage identity are unchanged.'
- 'All15 original scientific findings retain exact occurrence lineage and remain open
  for record curation: seven major and eight minor, with the extrusome frequency-scope
  finding provisional. The four targets without scientific findings retain qualified
  passes. No scientific finding is terminally resolved.'
- 'Issue #2650 tracks removing repeated evidence references from four uncommitted
  draft assessments. First-occurrence order, evidence records and scientific conclusions
  are unchanged. The failed native validation draft and receipt are retained.'
- 'Issue #2651 tracks adding required normalization reasons for the two minor acidocalcisome
  author-attribution findings. Valid DOI/year, biological scope, severity and original
  lineage remain unchanged; failed uncommitted validation receipts are retained.'
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104739Z-proteasome-storage-granule-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104740Z-protein-aggregate-center-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104741Z-acidocalcisome-lumen-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104742Z-acidocalcisome-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104743Z-actinophryid-extrusome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104744Z-anammoxosome-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104745Z-anammoxosome-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104745Z-apicomplexan-dense-granule-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104746Z-apicomplexan-dense-granule-membrane-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261021T104747Z-apicoplast-audit
  relationship: Current-input follow-up retaining the original immutable observation
    and exact finding lineage.
links:
- https://github.com/CultureBotAI/CellStructureMech/pull/2357
- https://github.com/CultureBotAI/CellStructureMech/issues/2514
- https://github.com/CultureBotAI/CellStructureMech/issues/2632
- https://github.com/CultureBotAI/CellStructureMech/issues/2633
- https://github.com/CultureBotAI/CellStructureMech/issues/2634
- https://github.com/CultureBotAI/CellStructureMech/issues/2635
- https://github.com/CultureBotAI/CellStructureMech/issues/2636
- https://github.com/CultureBotAI/CellStructureMech/issues/2637
- https://github.com/CultureBotAI/CellStructureMech/issues/2638
- https://github.com/CultureBotAI/CellStructureMech/issues/2639
- https://github.com/CultureBotAI/CellStructureMech/issues/2640
- https://github.com/CultureBotAI/CellStructureMech/issues/2641
- https://github.com/CultureBotAI/CellStructureMech/issues/2642
- https://github.com/CultureBotAI/CellStructureMech/issues/2643
- https://github.com/CultureBotAI/CellStructureMech/issues/2644
- https://github.com/CultureBotAI/CellStructureMech/issues/2645
- https://github.com/CultureBotAI/CellStructureMech/issues/2646
- https://github.com/CultureBotAI/CellStructureMech/issues/2647
- https://github.com/CultureBotAI/CellStructureMech/issues/2648
- https://github.com/CultureBotAI/CellStructureMech/issues/2649
- https://github.com/CultureBotAI/CellStructureMech/issues/2650
- https://github.com/CultureBotAI/CellStructureMech/issues/2651
```
