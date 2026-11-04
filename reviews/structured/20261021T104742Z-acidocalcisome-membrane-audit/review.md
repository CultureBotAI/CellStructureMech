# Acidocalcisome membrane composition, protein identity and source-scope review

- Review: 20261021T104742Z-acidocalcisome-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:26:59Z
- Finished UTC: 2026-10-21T10:47:42Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact membrane identity, collective bilayer and scoped transport roles are supported. One major omitted bacterial identity conflict and one minor source-author attribution require curation; accession-specific HppA membership remains explicitly unknown.

## Scope And Provenance

Entire exact membrane record: hierarchy, all three components and essentiality classes, HppA identity/family candidates, taxa/example, both functions, all four graph edges, discussion/history and neighboring-record boundary.

Selection: Batch20 index4; complete exact maintained record at frozen main9c0446, reviewed individually.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033102 | data/structures/membrane_organelle/acidocalcisome_membrane.yaml | maintained | acidocalcisome membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Expression-module applicability | not_applicable | False | GO:0033102 | No expression-module or transcriptomic assertion is made; compartment microscopy, biochemical reports and native identity authorities are the relevant sources. |
| native-verify | passed | True | GO:0033102 | Native identities and graph anchors passed; scientific membership and necessity are assessed separately. |
| native-causal-graphs | passed | True | GO:0033102 | Native identities and graph anchors passed; scientific membership and necessity are assessed separately. |
| Focused native schema | passed | True | GO:0033102 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033102 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0033102 | 11 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0033102 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0033102 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033102 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033102 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033102 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0033102 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

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

All three target DOIs resolve to the intended publications. The 2005 paper is a multi-author review and the2024 review is sole-author Docampo, making the repeated Huang attribution incorrect (F2). This review uses the2003 abstract, accessible2005 abstract/key points, actual2020 primary Methods/Results and the specified2024 review sections without upgrading secondary or abstract evidence to full primary-body support.

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

The sole reviewed tax358 hppA example has the exact maintained accession, gene, label and status. Its role explicitly limits it to identifier identity. IPR004131 is an integrated candidate for this PPase fragment, not an exact source-neutral replacement for the grouped proton-pump set including ATPases. Generic cation transporters are not a single gene/family; the existing reviewed-label-only rationale and open grounding TODO are appropriately bounded.

### Accession-specific ion selectivity and experimental localization

evidence: unknown. Targets: GO:0033102.

Q8VPZ0 is a D44 fragment with putative sodium-pump/function and membrane-location predictions by homology. The positive2003 abstract reports K-insensitive PPase activity but does not establish that this accession/strain was assayed. The2020 C58 study instead uses the full-length712-aa Atu_1174 fusion and distinguishes tagged HppA structures from DAPI-positive granules. These contexts do not experimentally settle Q8VPZ0 proton versus sodium selectivity or acidocalcisome membership. Because the record explicitly says identity only, no wrong-accession or experimentally disproved localization finding is manufactured.

### Acidification and cation exchange at reviewed functional scope

evidence: supported. Targets: GO:0033102.

The2005 accessible review key points support proton pumps and exchange systems; the2024 read sections explain acidification, cation transport/release and phosphorus/cation storage with species-dependent systems. These support the broad functional descriptions. They do not identify a universal transporter network, direction for every member, bacterial mechanism for every class, or assembly requirement.

### All four coarse function edges and gene-node anchoring

graph: supported. Targets: GO:0033102.

The membrane-bounds-organelle edge follows the authority definition. Pump-acidifies-lumen and transporter-exchanges-across-membrane reflect the cited reviews; acidity-supports-store remains a coarse functional relationship, not a specified molecular causal chain. NONMECHANISTIC and direction-neutral transport scope are explicit. Proton pumps and cation transporters reference existing components; one identity example covers the declared hppA symbol, while the generic transporter set intentionally declares no gene symbols.

### Bounded open grounding work

completeness: supported. Targets: GO:0033102.

The existing open discussion accurately requests more precise lipid and transporter groundings while recognizing lineage-dependent composition. No exact identifier for the full grouped sets was established by the inspected candidate family, so empty optional family inventories are not treated as an automatic defect. F1 separately requires a durable bacterial identity-conflict discussion.

## Findings

### F1: The sole canonical bacterial example omits an explicit unresolved identity dispute

major / open / confirmed; issue key: acidocalcisome_membrane-bacterial-identity-conflict.

The canonical A. tumefaciens note states that its volutin granules were shown to be membrane-bound acidocalcisome-like organelles, without acknowledging the later disagreement. The 2003 abstract supports the original interpretation; Frank and Jendrossek2020 instead distinguish C58 DAPI-positive polyphosphate granules from HppA/MitoTracker-positive structures using fluorescence and mutants, while Docampo2024 explicitly challenges that interpretation through prior membrane observations and a short-polyphosphate/DAPI limitation. The omission is confirmed, not a conclusion that bacterial acidocalcisomes do not exist. It materially affects the sole canonical example and the bacterial compartment interpretation. The record should retain both source positions and the unresolved strain/preparation and marker limits.

### F2: The 2024 review has one author, Roberto Docampo

minor / open / confirmed; issue key: acidocalcisome_membrane-docampo2024-author.

The target attributes DOI10.1128/MMBR.00042-23 to Docampo and Huang2024. Native bibliographic metadata and the article byline identify Roberto Docampo alone. Correct the attribution in every maintained note for this source; the valid DOI and collection year2024 are unchanged.

## Recommended Actions And Acceptance Checks

### A1

Scope the bacterial example and add a durable unresolved discussion citing the positive2003 report, primary2020 C58 study and2024 review counterargument.

- The canonical example distinguishes reported bacterial acidocalcisome-like compartments from disputed equivalence to DAPI-positive volutin/polyphosphate granules.
- The discussion states that2020 used fluorescence/mutants without TEM and that2024 raises growth-phase/short-polyphosphate detection alternatives; it does not claim either interpretation is conclusively disproved.
- Broad Bacteria presence remains VARIABLE and appropriately scoped; 2003 experimental strain and Q8VPZ0 equivalence are not invented.

### A2

Replace the incorrect Docampo and Huang2024 author attribution with Docampo2024 in every affected source note.

- Every occurrence tied to DOI10.1128/MMBR.00042-23 names its sole author correctly.
- The DOI, valid2024 collection year, source tier and scientific conclusions are retained.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/acidocalcisome_membrane.yaml; Entire YAML including identity, hierarchy, components if present, taxa, canonical example, evidence, graph, discussion and history | context_only | The entire exact target was read. Its compartment identity is distinct from the whole acidocalcisome; its bacterial example and cited source authorship require the bounded corrections below. |
| whole-organelle | data/structures/membrane_organelle/acidocalcisome.yaml; Entire neighboring record, especially composition and bacterial identity discussion | context_only | The whole-organelle record separately models polyphosphate/cation contents and already records a bacterial identity dispute. This is frozen boundary context, not a substitute for reading the primary and review sources. |
| compartment-neighbor | data/structures/membrane_organelle/acidocalcisome_lumen.yaml; Entire neighboring compartment record; definition, composition and graph boundary | context_only | The neighboring compartment record was read to verify the target discussion and the separation between internal volume, bounding membrane and organelle contents. Its assertions are not external scientific evidence. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Scope, nonmechanistic graphs and source support requirements | context_only | Topology and reviewed functional relationships can be explicitly NONMECHANISTIC; a directional label alone is not molecular intervention evidence. |
| acidocalcisome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033985,GO:0033102,GO:0043233,GO:0020022,GO:0016020; results for GO0033985, GO0033102, GO0043233, GO0020022, GO0016020: id/name/isObsolete/definition; GO0020022.children relation fields | supports | Five active native GO cellular-component terms verify lumen, membrane, organelle lumen, acidocalcisome and generic membrane identities. GO0020022 lists GO0033985 and GO0033102 children with part_of relations; this does not turn parthood into is_a. The definitions distinguish enclosed volume from lipid boundary. |
| acidocalcisome-agent-membrane-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033102/ancestors?relations=is_a; results[0].id and ancestors; request relations=is_a | supports | The requested is_a ancestor closure for GO0033102 includes GO0016020 membrane. It is separate from the acidocalcisome part_of relation. |
| acidocalcisome-agent-SL-0003 | https://rest.uniprot.org/locations/SL-0003.json; id/name/definition/synonyms/geneOntologies/isA/partOf | supports | Native SL0003 identifies acidocalcisome membrane, supplies its synonym and GO0033102 cross-reference, has isA SL0162 membrane, and partOf SL0002 acidocalcisome. |
| acidocalcisome-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; taxId, scientificName, rank and lineage | supports | Native taxonomy verifies taxon2 as Bacteria. This identifies the taxon and lineage only; it does not establish organelle occurrence, strain equivalence or universality. |
| acidocalcisome-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; taxId, scientificName, rank and lineage | supports | Native taxonomy verifies taxon2759 as Eukaryota. This identifies the taxon and lineage only; it does not establish organelle occurrence, strain equivalence or universality. |
| acidocalcisome-agent-tax-358 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/358; taxId, scientificName, rank and lineage | supports | Native taxonomy verifies taxon358 as Agrobacterium tumefaciens. This identifies the taxon and lineage only; it does not establish organelle occurrence, strain equivalence or universality. |
| acidocalcisome-agent-doi-2003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074%2Fjbc.M304548200&amp;format=json&amp;resultType=core; resultList.result[0]: title, id, doi, authorString, pubYear and complete abstractText | supports | Exact native metadata identifies Seufferheld and colleagues, PMID12783865, DOI10.1074/jbc.M304548200. The complete abstract reports a surrounding membrane by TEM, PPase localization by immunofluorescence/immuno-EM, enriched PPase/polyphosphate fractions, cations and acidic staining in A. tumefaciens. The abstract calls the PPase K-insensitive. This is primary abstract support, not an inspected full body or a resolved strain/accession bridge. |
| acidocalcisome-agent-doi-2005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro1097&amp;format=json&amp;resultType=core; resultList.result[0]: title, id, doi, authorString, pubYear, abstractText | supports | Exact native citation identifies Acidocalcisomes - conserved from bacteria to man, Docampo, de Souza, Miranda, Rohloff and Moreno, PMID15738951, DOI10.1038/nrmicro1097. Citation and complete abstract were read; this receipt is not the article body. |
| acidocalcisome-agent-review2005-publisher | https://www.nature.com/articles/nrmicro1097; Publisher HTML Abstract section and Key Points bullets1–5 only; no full-main-body claim | supports | The accessible review Abstract and five Key Points describe acidic polyphosphate/cation compartments, broad reported occurrence, and membrane Ca-ATPase, V-ATPase, V-PPase and exchange activities. This is secondary synthesis with lineage variation, not a new primary transport assay. The remaining main article body was not available in this response. |
| acidocalcisome-agent-doi-2020 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FAEM.02759-19&amp;format=json&amp;resultType=core; resultList.result[0]: title, id, pmcid, doi, authorString, pubYear, abstractText | supports | Exact native citation identifies Frank and Jendrossek 2020, PMID32060025, PMC7117937, DOI10.1128/AEM.02759-19. The complete abstract proposes that polyphosphate granules and HppA-positive structures are distinct in A. tumefaciens; actual Methods/Results support is in the separately hashed PMC body. |
| acidocalcisome-agent-pmc2020-native | https://pmc.ncbi.nlm.nih.gov/articles/PMC7117937/; Results and Discussion s2.1–s2.8 including Conclusions; Fig1–8 captions; Methods s3.1–s3.5 direct prose (strain C58, culture, deletions, fusion construction). Figure pixels, supplements and nested strain table not independently read. | supports | Primary C58 experiments use fluorescent stains, HppA fusions and ppk/hppA mutants across growth phases. Results distinguish DAPI-positive polyphosphate from HppA/MitoTracker structures; ppk loss removes polyphosphate without removing the latter. The authors infer membrane-free polyphosphate granules but explicitly did not perform TEM. HppA is the full-length Atu_1174 construct here; the composition, contents and function of the HppA-positive structures remain unresolved in the paper. |
| acidocalcisome-agent-doi-2024 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMMBR.00042-23&amp;format=json&amp;resultType=core; resultList.result[0]: title, id, pmcid, doi, authorString, authorList and pubYear | supports | Exact native citation identifies Advances in the cellular biology, biochemistry, and molecular biology of acidocalcisomes, PMID38099688, PMC10966946, DOI10.1128/MMBR.00042-23, with Roberto Docampo as the sole author. Collection year2024 is valid; no Huang appears in the author list. |
| acidocalcisome-agent-pmc2024-native | https://pmc.ncbi.nlm.nih.gov/articles/PMC10966946/; Byline; s1 Introduction; s2 Phylogenetic distribution (especially bacterial controversy); s3 Structural characteristics; s4 direct composition paragraphs; s5-1 Proton pumps, s5-2 P-type ATPases, s5-4 Channels, s5-5 Membrane transporters, s5-6 Other components; s10 cation/phosphorus storage. No full proteomic-table or figure-pixel review. | supports | This sole-author review describes lineage-dependent acidocalcisome membrane systems and explicitly discusses the 2020 bacterial separation proposal. It counters with earlier membrane evidence, growth-phase effects and DAPI insensitivity to very short polyphosphate, proposing further investigation rather than settling the disagreement. Read transport sections distinguish proton pumps, Ca pumps, channels and partly unidentified exchangers; these are reviewed source claims, not new experiments in this paper. |
| acidocalcisome-agent-Q8VPZ0 | https://rest.uniprot.org/uniprotkb/Q8VPZ0.json; primaryAccession, entryType, proteinDescription, genes, organism, sequence.length, fragment flag, references/source strain, FUNCTION and SUBCELLULAR LOCATION comments/evidence codes | supports | Native Q8VPZ0 is reviewed, gene hppA with synonym vppA, tax358, and the stated putative K-stimulated pyrophosphate-energized sodium-pump name. It is a189-aa fragment submitted from strainD44. Function and cell-inner-membrane annotations are inferred by homology; no experimental acidocalcisome localization is established by this entry. |
| acidocalcisome-agent-hppA-reviewed | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhppA%29%20AND%20%28organism_id%3A358%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; results array: one result, primaryAccession/genes/organism/entryType | supports | The native exact reviewed hppA query restricted to tax358 returns the single entryQ8VPZ0. This verifies the record identity-only selection rationale within this query, not biological localization or every strain homolog. |
| acidocalcisome-agent-Q8VPZ0-matches | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8VPZ0/?page_size=200; count, next and results[0].metadata plus protein match coordinates | supports | The complete native integrated InterPro result has count1 and next=null, assigning the189-aa Q8VPZ0 fragment to IPR004131 over positions1–187. This provides one integrated family candidate for the inspected protein. |
| acidocalcisome-agent-IPR004131 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004131/; metadata accession/name/type/description and member_databases/signature names | supports | IPR004131 is the pyrophosphate-energised proton-pump family; its native description concerns membrane pyrophosphatases and distinguishes K-stimulated/K-insensitive subclasses. The member signatures include a putative sodium-pump signature. |
| native-verify | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml --verify; Complete focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml --causal-graphs; Complete focused native output | supports | data/structures/membrane_organelle/acidocalcisome_membrane.yaml  (GO:0033102)<br>  acidocalcisome_membrane_ion_transport	proton_pumps	COVERED	-&gt;proton_pumps (UniProtKB:Q8VPZ0)<br>  acidocalcisome_membrane_ion_transport	cation_transporters	NO_GENE_SYMBOLS	-&gt;cation_transporters (PROTEIN: acidocalcisome cation transporters)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/acidocalcisome_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/acidocalcisome_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/acidocalcisome_membrane.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/acidocalcisome_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/acidocalcisome_membrane.yaml --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/acidocalcisome_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/acidocalcisome_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/acidocalcisome_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 11 of11 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Seufferheld2003 was read as the complete native abstract only. Publisher DOI/API routes supplied redirect or metadata-only responses; ScienceDirect/JBC requests were denied and the browser extraction failed. These failures are preserved and are not evidence that the paper lacks support. No experimental strain or Q8VPZ0 bridge is inferred from that abstract.
- Docampo et al.2005 publisher coverage is Abstract and all five Key Points only, not the full main body. Docampo2024 is secondary review evidence; only the listed sections/direct paragraphs were read, not all proteomic tables, raw datasets or underlying cited experiments.
- Frank and Jendrossek2020 coverage is all Results/Discussion, captions and Methods3.1–3.5 direct prose. The C58 growth-phase, fluorescent-marker and mutant context is retained; no TEM was performed in that study. Figure pixels, supplementary files and nested strain-table contents were not independently examined.
- The bacterial acidocalcisome/polyphosphate equivalence remains disputed. The review identifies omitted uncertainty; it neither rejects every bacterial acidocalcisome report nor treats all bacterial polyphosphate granules as membrane-bounded organelles.
- Q8VPZ0 is an identity-only D44 sequence fragment with homology-based annotations. This review does not identify it with the2003 preparation or the2020 C58 full-length fusion, nor does it infer an experimental ion-selectivity contradiction from a predicted native protein name.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The collective bilayer constitutional role is kept separate from unknown necessity of individual lipids, pumps and transporters.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T104742Z-acidocalcisome-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Acidocalcisome membrane composition, protein identity and source-scope review
started_at: '2026-10-21T10:26:59Z'
finished_at: '2026-10-21T10:47:42Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Exact membrane identity, collective bilayer and scoped transport roles are
  supported. One major omitted bacterial identity conflict and one minor source-author
  attribution require curation; accession-specific HppA membership remains explicitly
  unknown.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
  state: working_tree
  inputs:
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/acidocalcisome.yaml
    sha256: a694232f7d3e26286500601a55bb4332f35a07c6fc150f6ea85e8e7be640d0f7
    role: context
  - path: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
    sha256: 3238b530f5846e584dfb86651fd4895cb461e26bcc74afa51f3740815fab02e9
    role: context
  - path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    sha256: 2a2a8ddf090bccdc6e8f0fd6b84f3e2ce971789071cb6af97dde48ed834f3a55
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0033102
  path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  label: acidocalcisome membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
scope:
  description: 'Entire exact membrane record: hierarchy, all three components and
    essentiality classes, HppA identity/family candidates, taxa/example, both functions,
    all four graph edges, discussion/history and neighboring-record boundary.'
  selection: Batch20 index4; complete exact maintained record at frozen main9c0446,
    reviewed individually.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033102
checks:
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0033102
  summary: No expression-module or transcriptomic assertion is made; compartment microscopy,
    biochemical reports and native identity authorities are the relevant sources.
- check_id: native-verify
  name: native-verify
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --verify
  exit_code: 0
  summary: Native identities and graph anchors passed; scientific membership and necessity
    are assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: native-causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Native identities and graph anchors passed; scientific membership and necessity
    are assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just validate data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just validate-strict data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/acidocalcisome_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0033102
  summary: 11 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033102
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - whole-organelle
  - compartment-neighbor
  - graph-policy
  - acidocalcisome-agent-go
  - acidocalcisome-agent-membrane-ancestors
  - acidocalcisome-agent-SL-0003
  - acidocalcisome-agent-tax-2
  - acidocalcisome-agent-tax-2759
  - acidocalcisome-agent-tax-358
  - acidocalcisome-agent-doi-2003
  - acidocalcisome-agent-doi-2005
  - acidocalcisome-agent-review2005-publisher
  - acidocalcisome-agent-doi-2020
  - acidocalcisome-agent-pmc2020-native
  - acidocalcisome-agent-doi-2024
  - acidocalcisome-agent-pmc2024-native
  - acidocalcisome-agent-Q8VPZ0
  - acidocalcisome-agent-hppA-reviewed
  - acidocalcisome-agent-Q8VPZ0-matches
  - acidocalcisome-agent-IPR004131
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0033102
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  locator: Entire YAML including identity, hierarchy, components if present, taxa,
    canonical example, evidence, graph, discussion and history
  accessed_at: '2026-10-21T10:36:48Z'
  support: context_only
  summary: The entire exact target was read. Its compartment identity is distinct
    from the whole acidocalcisome; its bacterial example and cited source authorship
    require the bounded corrections below.
- evidence_id: whole-organelle
  kind: record_content
  reference: data/structures/membrane_organelle/acidocalcisome.yaml
  locator: Entire neighboring record, especially composition and bacterial identity
    discussion
  accessed_at: '2026-10-21T10:36:48Z'
  support: context_only
  summary: The whole-organelle record separately models polyphosphate/cation contents
    and already records a bacterial identity dispute. This is frozen boundary context,
    not a substitute for reading the primary and review sources.
- evidence_id: compartment-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/acidocalcisome_lumen.yaml
  locator: Entire neighboring compartment record; definition, composition and graph
    boundary
  accessed_at: '2026-10-21T10:36:48Z'
  support: context_only
  summary: The neighboring compartment record was read to verify the target discussion
    and the separation between internal volume, bounding membrane and organelle contents.
    Its assertions are not external scientific evidence.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope, nonmechanistic graphs and source support requirements
  accessed_at: '2026-10-21T10:36:48Z'
  support: context_only
  summary: Topology and reviewed functional relationships can be explicitly NONMECHANISTIC;
    a directional label alone is not molecular intervention evidence.
- evidence_id: acidocalcisome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033985,GO:0033102,GO:0043233,GO:0020022,GO:0016020
  locator: 'results for GO0033985, GO0033102, GO0043233, GO0020022, GO0016020: id/name/isObsolete/definition;
    GO0020022.children relation fields'
  accessed_at: '2026-10-21T10:29:02.575927Z'
  support: supports
  summary: Five active native GO cellular-component terms verify lumen, membrane,
    organelle lumen, acidocalcisome and generic membrane identities. GO0020022 lists
    GO0033985 and GO0033102 children with part_of relations; this does not turn parthood
    into is_a. The definitions distinguish enclosed volume from lipid boundary.
  snapshot_sha256: 2872720648af18a28afd5e8444b93db63817e9ac8228ab4def9cb131e62a739c
- evidence_id: acidocalcisome-agent-membrane-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033102/ancestors?relations=is_a
  locator: results[0].id and ancestors; request relations=is_a
  accessed_at: '2026-10-21T10:31:25.363537Z'
  support: supports
  summary: The requested is_a ancestor closure for GO0033102 includes GO0016020 membrane.
    It is separate from the acidocalcisome part_of relation.
  snapshot_sha256: 619c5a69e707dbe22c0dc4bc35f924c76fd550cae5e61ad09e423c9683f07649
- evidence_id: acidocalcisome-agent-SL-0003
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0003.json
  locator: id/name/definition/synonyms/geneOntologies/isA/partOf
  accessed_at: '2026-10-21T10:29:02.576952Z'
  support: supports
  summary: Native SL0003 identifies acidocalcisome membrane, supplies its synonym
    and GO0033102 cross-reference, has isA SL0162 membrane, and partOf SL0002 acidocalcisome.
  snapshot_sha256: f770848e7dc607ffa0e6f179a939e4d8d5dfe08a4299a2c57e4f902e15aef9f9
- evidence_id: acidocalcisome-agent-tax-2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T10:29:03.303616Z'
  support: supports
  summary: Native taxonomy verifies taxon2 as Bacteria. This identifies the taxon
    and lineage only; it does not establish organelle occurrence, strain equivalence
    or universality.
  snapshot_sha256: 7429617438ff0162ee4783c4c660f6127642e6ff686522e670c6ecf3a5b28816
- evidence_id: acidocalcisome-agent-tax-2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T10:29:03.311762Z'
  support: supports
  summary: Native taxonomy verifies taxon2759 as Eukaryota. This identifies the taxon
    and lineage only; it does not establish organelle occurrence, strain equivalence
    or universality.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: acidocalcisome-agent-tax-358
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/358
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T10:29:03.319711Z'
  support: supports
  summary: Native taxonomy verifies taxon358 as Agrobacterium tumefaciens. This identifies
    the taxon and lineage only; it does not establish organelle occurrence, strain
    equivalence or universality.
  snapshot_sha256: e4ead5c9da75d4204c7fe36f6a16082f03cc88c29192129647e5bc08f4a9b167
- evidence_id: acidocalcisome-agent-doi-2003
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1074%2Fjbc.M304548200&format=json&resultType=core
  locator: 'resultList.result[0]: title, id, doi, authorString, pubYear and complete
    abstractText'
  accessed_at: '2026-10-21T10:29:03.590730Z'
  support: supports
  summary: Exact native metadata identifies Seufferheld and colleagues, PMID12783865,
    DOI10.1074/jbc.M304548200. The complete abstract reports a surrounding membrane
    by TEM, PPase localization by immunofluorescence/immuno-EM, enriched PPase/polyphosphate
    fractions, cations and acidic staining in A. tumefaciens. The abstract calls the
    PPase K-insensitive. This is primary abstract support, not an inspected full body
    or a resolved strain/accession bridge.
  snapshot_sha256: 16d3fd412b4e90ad994a3a8b558763e8b3f7a3683e5dfd2306b487d6d7225dea
- evidence_id: acidocalcisome-agent-doi-2005
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrmicro1097&format=json&resultType=core
  locator: 'resultList.result[0]: title, id, doi, authorString, pubYear, abstractText'
  accessed_at: '2026-10-21T10:29:03.593572Z'
  support: supports
  summary: Exact native citation identifies Acidocalcisomes - conserved from bacteria
    to man, Docampo, de Souza, Miranda, Rohloff and Moreno, PMID15738951, DOI10.1038/nrmicro1097.
    Citation and complete abstract were read; this receipt is not the article body.
  snapshot_sha256: c6d706c662f4f704a6e12fb1dbaf124fde32df6329271e1519c3755d7a5b2f08
- evidence_id: acidocalcisome-agent-review2005-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrmicro1097
  locator: Publisher HTML Abstract section and Key Points bullets1–5 only; no full-main-body
    claim
  accessed_at: '2026-10-21T10:29:33.793455Z'
  support: supports
  summary: The accessible review Abstract and five Key Points describe acidic polyphosphate/cation
    compartments, broad reported occurrence, and membrane Ca-ATPase, V-ATPase, V-PPase
    and exchange activities. This is secondary synthesis with lineage variation, not
    a new primary transport assay. The remaining main article body was not available
    in this response.
  snapshot_sha256: 0a77c371f378401decfbb80f30871f930462764d4367e22cba3971cd8e7922d8
- evidence_id: acidocalcisome-agent-doi-2020
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FAEM.02759-19&format=json&resultType=core
  locator: 'resultList.result[0]: title, id, pmcid, doi, authorString, pubYear, abstractText'
  accessed_at: '2026-10-21T10:29:03.916412Z'
  support: supports
  summary: Exact native citation identifies Frank and Jendrossek 2020, PMID32060025,
    PMC7117937, DOI10.1128/AEM.02759-19. The complete abstract proposes that polyphosphate
    granules and HppA-positive structures are distinct in A. tumefaciens; actual Methods/Results
    support is in the separately hashed PMC body.
  snapshot_sha256: 67c068cac424696d77193aba8ae7488026001d621efe5b023350c3e45d606681
- evidence_id: acidocalcisome-agent-pmc2020-native
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7117937/
  locator: Results and Discussion s2.1–s2.8 including Conclusions; Fig1–8 captions;
    Methods s3.1–s3.5 direct prose (strain C58, culture, deletions, fusion construction).
    Figure pixels, supplements and nested strain table not independently read.
  accessed_at: '2026-10-21T10:29:33.792475Z'
  support: supports
  summary: Primary C58 experiments use fluorescent stains, HppA fusions and ppk/hppA
    mutants across growth phases. Results distinguish DAPI-positive polyphosphate
    from HppA/MitoTracker structures; ppk loss removes polyphosphate without removing
    the latter. The authors infer membrane-free polyphosphate granules but explicitly
    did not perform TEM. HppA is the full-length Atu_1174 construct here; the composition,
    contents and function of the HppA-positive structures remain unresolved in the
    paper.
  snapshot_sha256: 2dd6c9a3e8060769caf1aaffc0ed3f2718b0adc8b8fb38211a2939d1f1059c80
- evidence_id: acidocalcisome-agent-doi-2024
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FMMBR.00042-23&format=json&resultType=core
  locator: 'resultList.result[0]: title, id, pmcid, doi, authorString, authorList
    and pubYear'
  accessed_at: '2026-10-21T10:29:03.893148Z'
  support: supports
  summary: Exact native citation identifies Advances in the cellular biology, biochemistry,
    and molecular biology of acidocalcisomes, PMID38099688, PMC10966946, DOI10.1128/MMBR.00042-23,
    with Roberto Docampo as the sole author. Collection year2024 is valid; no Huang
    appears in the author list.
  snapshot_sha256: 76730fcd2d61ed58965979faae8e3f1400d35d6351ae52056d4f3aeb9379f624
- evidence_id: acidocalcisome-agent-pmc2024-native
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC10966946/
  locator: Byline; s1 Introduction; s2 Phylogenetic distribution (especially bacterial
    controversy); s3 Structural characteristics; s4 direct composition paragraphs;
    s5-1 Proton pumps, s5-2 P-type ATPases, s5-4 Channels, s5-5 Membrane transporters,
    s5-6 Other components; s10 cation/phosphorus storage. No full proteomic-table
    or figure-pixel review.
  accessed_at: '2026-10-21T10:29:33.792539Z'
  support: supports
  summary: This sole-author review describes lineage-dependent acidocalcisome membrane
    systems and explicitly discusses the 2020 bacterial separation proposal. It counters
    with earlier membrane evidence, growth-phase effects and DAPI insensitivity to
    very short polyphosphate, proposing further investigation rather than settling
    the disagreement. Read transport sections distinguish proton pumps, Ca pumps,
    channels and partly unidentified exchangers; these are reviewed source claims,
    not new experiments in this paper.
  snapshot_sha256: 89d303c684a70ec9ddd86d12c8e46f5efb96bf2a7a620974c7e6d14dbb3a24d2
- evidence_id: acidocalcisome-agent-Q8VPZ0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q8VPZ0.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism, sequence.length,
    fragment flag, references/source strain, FUNCTION and SUBCELLULAR LOCATION comments/evidence
    codes
  accessed_at: '2026-10-21T10:29:02.577937Z'
  support: supports
  summary: Native Q8VPZ0 is reviewed, gene hppA with synonym vppA, tax358, and the
    stated putative K-stimulated pyrophosphate-energized sodium-pump name. It is a189-aa
    fragment submitted from strainD44. Function and cell-inner-membrane annotations
    are inferred by homology; no experimental acidocalcisome localization is established
    by this entry.
  snapshot_sha256: 62b0cd4de2335cca96e281176133b61f0946d97406349648447beef67f1c0e55
- evidence_id: acidocalcisome-agent-hppA-reviewed
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AhppA%29%20AND%20%28organism_id%3A358%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: 'results array: one result, primaryAccession/genes/organism/entryType'
  accessed_at: '2026-10-21T10:29:02.578892Z'
  support: supports
  summary: The native exact reviewed hppA query restricted to tax358 returns the single
    entryQ8VPZ0. This verifies the record identity-only selection rationale within
    this query, not biological localization or every strain homolog.
  snapshot_sha256: 61ccab144968d5233122e172bb240b27326a3635f38c330b7fa2172cbb13b9b6
  search_scope: UniProtKB gene_exact:hppA AND organism_id:358 AND reviewed:true; format=json,
    size500; one returned result, no additional page required.
- evidence_id: acidocalcisome-agent-Q8VPZ0-matches
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/Q8VPZ0/?page_size=200
  locator: count, next and results[0].metadata plus protein match coordinates
  accessed_at: '2026-10-21T10:29:02.578498Z'
  support: supports
  summary: The complete native integrated InterPro result has count1 and next=null,
    assigning the189-aa Q8VPZ0 fragment to IPR004131 over positions1–187. This provides
    one integrated family candidate for the inspected protein.
  snapshot_sha256: d9d0da8a0717e20a6554e2532e7bc8bacab510c3f11b92650cc549890c8ac764
- evidence_id: acidocalcisome-agent-IPR004131
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004131/
  locator: metadata accession/name/type/description and member_databases/signature
    names
  accessed_at: '2026-10-21T10:29:34.127616Z'
  support: supports
  summary: IPR004131 is the pyrophosphate-energised proton-pump family; its native
    description concerns membrane pyrophosphatases and distinguishes K-stimulated/K-insensitive
    subclasses. The member signatures include a putative sodium-pump signature.
  snapshot_sha256: e4e648c13a47216105a8d1d88a9ff06c2591ced606c998fceb591cad8b39765e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --verify
  locator: Complete focused native output
  accessed_at: '2026-10-21T10:30:54.270385Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --causal-graphs
  locator: Complete focused native output
  accessed_at: '2026-10-21T10:30:54.680491Z'
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
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/acidocalcisome_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:27:01Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/acidocalcisome_membrane.yaml'
  snapshot_sha256: 1e36efbf4cb8ff1f824267e8fbc7a1123171ba2e7ae3b7259cdf44ba89505fce
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/acidocalcisome_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:27:02Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/acidocalcisome_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch20-20261021-guyhe4k8/acidocalcisome_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch20-20261021-guyhe4k8/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch20-20261021-guyhe4k8/acidocalcisome_membrane-strict.tsv"
  snapshot_sha256: a512e67b5d3786952ed939979ccc2ddc399bb072ff08739a93207b3a8aca6ccf
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/acidocalcisome_membrane.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:36:48Z'
  support: supports
  summary: '11 of11 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
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
  - acidocalcisome-agent-go
  - acidocalcisome-agent-membrane-ancestors
  - acidocalcisome-agent-SL-0003
  - record
- assessment_id: scope
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
  - acidocalcisome-agent-tax-2
  - acidocalcisome-agent-tax-2759
  - acidocalcisome-agent-tax-358
  - acidocalcisome-agent-review2005-publisher
  - acidocalcisome-agent-pmc2024-native
  - record
- assessment_id: bacterial-conflict
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
  - acidocalcisome-agent-doi-2003
  - acidocalcisome-agent-pmc2020-native
  - acidocalcisome-agent-pmc2024-native
  - record
- assessment_id: citation
  area: provenance
  topic: Exact citation identities and source tiers
  outcome: concern
  target_ids:
  - GO:0033102
  summary: All three target DOIs resolve to the intended publications. The 2005 paper
    is a multi-author review and the2024 review is sole-author Docampo, making the
    repeated Huang attribution incorrect (F2). This review uses the2003 abstract,
    accessible2005 abstract/key points, actual2020 primary Methods/Results and the
    specified2024 review sections without upgrading secondary or abstract evidence
    to full primary-body support.
  evidence_ids:
  - acidocalcisome-agent-doi-2003
  - acidocalcisome-agent-doi-2005
  - acidocalcisome-agent-review2005-publisher
  - acidocalcisome-agent-doi-2020
  - acidocalcisome-agent-pmc2020-native
  - acidocalcisome-agent-doi-2024
  - acidocalcisome-agent-pmc2024-native
  - record
- assessment_id: ownership
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
  - record
  - whole-organelle
  - compartment-neighbor
- assessment_id: composition
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
  - record
  - acidocalcisome-agent-go
  - acidocalcisome-agent-SL-0003
  - acidocalcisome-agent-review2005-publisher
  - acidocalcisome-agent-pmc2024-native
- assessment_id: necessity
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
  - record
  - acidocalcisome-agent-go
  - acidocalcisome-agent-review2005-publisher
  - acidocalcisome-agent-pmc2024-native
- assessment_id: protein-identity
  area: grounding
  topic: Reviewed hppA example and native family scope
  outcome: supported
  target_ids:
  - GO:0033102
  summary: The sole reviewed tax358 hppA example has the exact maintained accession,
    gene, label and status. Its role explicitly limits it to identifier identity.
    IPR004131 is an integrated candidate for this PPase fragment, not an exact source-neutral
    replacement for the grouped proton-pump set including ATPases. Generic cation
    transporters are not a single gene/family; the existing reviewed-label-only rationale
    and open grounding TODO are appropriately bounded.
  evidence_ids:
  - record
  - acidocalcisome-agent-Q8VPZ0
  - acidocalcisome-agent-hppA-reviewed
  - acidocalcisome-agent-Q8VPZ0-matches
  - acidocalcisome-agent-IPR004131
- assessment_id: protein-membership-limit
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
  - record
  - acidocalcisome-agent-Q8VPZ0
  - acidocalcisome-agent-doi-2003
  - acidocalcisome-agent-pmc2020-native
- assessment_id: functions
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
  - record
  - acidocalcisome-agent-review2005-publisher
  - acidocalcisome-agent-pmc2024-native
- assessment_id: graph
  area: graph
  topic: All four coarse function edges and gene-node anchoring
  outcome: supported
  target_ids:
  - GO:0033102
  summary: The membrane-bounds-organelle edge follows the authority definition. Pump-acidifies-lumen
    and transporter-exchanges-across-membrane reflect the cited reviews; acidity-supports-store
    remains a coarse functional relationship, not a specified molecular causal chain.
    NONMECHANISTIC and direction-neutral transport scope are explicit. Proton pumps
    and cation transporters reference existing components; one identity example covers
    the declared hppA symbol, while the generic transporter set intentionally declares
    no gene symbols.
  evidence_ids:
  - record
  - graph-policy
  - acidocalcisome-agent-go
  - acidocalcisome-agent-review2005-publisher
  - acidocalcisome-agent-pmc2024-native
  - acidocalcisome-agent-Q8VPZ0
- assessment_id: discussion
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
  - record
  - acidocalcisome-agent-IPR004131
  - acidocalcisome-agent-Q8VPZ0-matches
  - acidocalcisome-agent-pmc2024-native
findings:
- finding_id: F1
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
  - record
  - acidocalcisome-agent-doi-2003
  - acidocalcisome-agent-pmc2020-native
  - acidocalcisome-agent-pmc2024-native
  normalization_reason: Major because the central sole canonical example presents
    disputed compartment identity as settled; the required correction is scoped evidence
    reconciliation, not deletion of the taxon or reversal of the ontology definition.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
- finding_id: F2
  issue_key: acidocalcisome_membrane-docampo2024-author
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
  - GO:0033102
  field_paths:
  - components[2].evidence
  - functions[1].evidence
  - evidence
  - causal_graphs[0].edges[2].evidence
  evidence_ids:
  - record
  - acidocalcisome-agent-doi-2024
  - acidocalcisome-agent-pmc2024-native
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Scope the bacterial example and add a durable unresolved discussion
    citing the positive2003 report, primary2020 C58 study and2024 review counterargument.
  finding_ids:
  - F1
  target_ids:
  - GO:0033102
  acceptance_checks:
  - The canonical example distinguishes reported bacterial acidocalcisome-like compartments
    from disputed equivalence to DAPI-positive volutin/polyphosphate granules.
  - The discussion states that2020 used fluorescence/mutants without TEM and that2024
    raises growth-phase/short-polyphosphate detection alternatives; it does not claim
    either interpretation is conclusively disproved.
  - Broad Bacteria presence remains VARIABLE and appropriately scoped; 2003 experimental
    strain and Q8VPZ0 equivalence are not invented.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
- action_id: A2
  description: Replace the incorrect Docampo and Huang2024 author attribution with
    Docampo2024 in every affected source note.
  finding_ids:
  - F2
  target_ids:
  - GO:0033102
  acceptance_checks:
  - Every occurrence tied to DOI10.1128/MMBR.00042-23 names its sole author correctly.
  - The DOI, valid2024 collection year, source tier and scientific conclusions are
    retained.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/acidocalcisome_membrane.yaml
    role: maintained scientific record
limitations:
- Seufferheld2003 was read as the complete native abstract only. Publisher DOI/API
  routes supplied redirect or metadata-only responses; ScienceDirect/JBC requests
  were denied and the browser extraction failed. These failures are preserved and
  are not evidence that the paper lacks support. No experimental strain or Q8VPZ0
  bridge is inferred from that abstract.
- Docampo et al.2005 publisher coverage is Abstract and all five Key Points only,
  not the full main body. Docampo2024 is secondary review evidence; only the listed
  sections/direct paragraphs were read, not all proteomic tables, raw datasets or
  underlying cited experiments.
- Frank and Jendrossek2020 coverage is all Results/Discussion, captions and Methods3.1–3.5
  direct prose. The C58 growth-phase, fluorescent-marker and mutant context is retained;
  no TEM was performed in that study. Figure pixels, supplementary files and nested
  strain-table contents were not independently examined.
- The bacterial acidocalcisome/polyphosphate equivalence remains disputed. The review
  identifies omitted uncertainty; it neither rejects every bacterial acidocalcisome
  report nor treats all bacterial polyphosphate granules as membrane-bounded organelles.
- Q8VPZ0 is an identity-only D44 sequence fragment with homology-based annotations.
  This review does not identify it with the2003 preparation or the2020 C58 full-length
  fusion, nor does it infer an experimental ion-selectivity contradiction from a predicted
  native protein name.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The collective bilayer constitutional role is kept separate from unknown necessity
  of individual lipids, pumps and transporters.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
