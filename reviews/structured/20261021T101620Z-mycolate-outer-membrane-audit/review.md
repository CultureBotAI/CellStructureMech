# Envelope identity, composition and evidence review

- Review: 20261021T101620Z-mycolate-outer-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:59:40Z
- Finished UTC: 2026-10-21T10:16:20Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The mycomembrane identity, chemical classes, model examples and three protein identities are supported. One minor finding concerns certainty of leaflet organization in otherwise useful descriptive architecture.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 6 in batch eighteen; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036407 | data/structures/envelope/mycolate_outer_membrane.yaml | maintained | mycolate outer membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0036407 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Native protein causal-graphs | passed | True | GO:0036407 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Focused native schema | passed | True | GO:0036407 | Focused validator passed. |
| Focused native strict | passed | True | GO:0036407 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0036407 | 19 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0036407 | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0036407 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0036407 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0036407 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0036407 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0036407 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0036407 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Mycomembrane distinguished from the entire wall core

identity: supported. Targets: GO:0036407.

Exact GO identity, synonyms and outer-membrane parent are supported. The definition retains the mycolate-rich bilayer and covalent AG–PG linkage. The resolved boundary discussion correctly keeps AG and PG as contextual graph nodes rather than local membrane constituents.

### Chemical class versus heterogeneous pools

grounding: supported. Targets: GO:0036407.

Mycolic acid and contextual arabinogalactan match the verified material classes. Extractable lipids and outer-membrane proteins are heterogeneous pools, not single CHEBI or sequence families. Native fractions and review evidence support their presence; one universal lipid recipe is not warranted.

### Structural requirement for mycolates in the tested corynebacterial context

evidence: supported. Targets: GO:0036407.

The tested C. glutamicum mycolate-deficient mutant lacks an outer-membrane bilayer, providing a structural endpoint distinct from viability. This supports a material requirement in that experimental context; it does not establish individual necessity of each extractable lipid or porin.

### Assembly necessity of heterogeneous lipid and protein pools

evidence: unknown. Targets: GO:0036407.

Presence and uptake or growth effects do not establish whether every member of the extractable-lipid and outer-membrane-protein pools is required to form the membrane. The record uses CONDITIONAL for these pools; the reviewed evidence does not resolve that assembly-necessity classification. No individual requirement or dispensability is inferred.

### Reviewed MspA and accurately labeled unreviewed porins

evidence: supported. Targets: GO:0036407.

Accession/name/gene/taxon/status pairs match all three native entries. The exact reviewed query uniquely returns MspA and returns no reviewed PorA/PorB in the declared species. H7C6A6 links a sequenced MH20-22B PorA record; H7C685 links the ATCC13032 PorB sequence. Their source-linked primary abstracts support the named porin identities and channels, while the maintained entry notes remain identity-only. Unreviewed status is not silently promoted.

### Source-supported model taxa with historical names

scope: supported. Targets: GO:0036407.

Bacterial distribution is explicitly variable. Mycobacteria and related corynebacteria are supported; M.smegmatis mc2155 and C.glutamicum are directly represented in the primary sources. ENA currently uses Mycolicibacterium smegmatis for1772; the maintained older genus name is the historical source name, not a different organism. No prevalence census is asserted.

### Permeability barrier and scoped protein channels

evidence: supported. Targets: GO:0036407.

The membrane barrier and porin-mediated hydrophilic uptake are supported by the review and native fractions. MspA evidence is species-specific; the record is not read as saying every mycobacterium carries MspA or that every identified outer-membrane protein is a general porin.

### Preserve uncertainty of leaflet partition

graph: concern. Targets: GO:0036407.

The explicitly NONMECHANISTIC graph correctly gives class-level anchoring and membrane architecture. However, component roles and the pack-into edge state inner/outer-leaflet assignments without the model qualifications present in the cited papers. This is a bounded certainty issue; bilayer existence and covalent linkage remain supported.

### Bounded record-level coverage

completeness: supported. Targets: GO:0036407.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Exact additional polymer inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. A clean result does not assert exhaustive literature completeness.

## Findings

### F1: Retain the sources' uncertainty about leaflet organization

minor / open / confirmed; issue key: mycomembrane-leaflet-model-certainty.

The mycolic-acid role presents a covalently attached inner leaflet and the extractable-lipid role/graph present outer-leaflet packing as settled architecture. Niederweis2010 explicitly discusses extractable lipids in both leaflets and unknown mycolate conformation; Hoffmann2008 gives alternative models, and Chiaradia2017 still calls the outer-leaflet assignment presumed. Qualify the arrangement as a source-scoped model without disputing the observed bilayer or covalent AG linkage.

## Recommended Actions And Acceptance Checks

### A1

Qualify leaflet assignments as the cited model and preserve the possibility of extractable material in both leaflets; retain the directly supported bilayer and covalent linkage.

- Separate observed membrane structure and biochemical fraction composition from inferred leaflet placement.
- Do not infer a universal composition or individual lipid/porin formation necessity.
- Any scientific edit requires separate curation authorization, guarded writes, append-only history and native validation/rendering.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/mycolate_outer_membrane.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| root18-sources-mycomembrane-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009274,GO:0009279,GO:0036407; All three returned term definitions, synonyms and relevant is_a child relation | supports | GO0036407 provides the exact mycolate outer-membrane definition and all three exact synonyms; GO0009279 lists it as a child. The contextual peptidoglycan-wall node remains distinct from the target membrane. |
| root18-sources-NCBITaxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Bacteria at domain rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-NCBITaxon-1763 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1763; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Mycobacterium at genus rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-NCBITaxon-1772 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1772; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Mycolicibacterium smegmatis at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-NCBITaxon-1718 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1718; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Corynebacterium glutamicum at species rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-NCBITaxon-246196 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/246196; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Mycolicibacterium smegmatis MC2 155 at strain rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root18-sources-CHEBI-25438 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/25438/; Exact accession, name, definition where present, synonyms and chemical-class relations | supports | Released three-star CHEBI:25438 identifies mycolic acid. Its chemical-class identity and returned definition/ontology relations are assessed independently of placement in a wall or membrane. |
| root18-sources-CHEBI-27569 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/27569/; Exact accession, name, definition where present, synonyms and chemical-class relations | supports | Released three-star CHEBI:27569 identifies arabinogalactan. Its chemical-class identity and returned definition/ontology relations are assessed independently of placement in a wall or membrane. |
| root18-sources-doi-10.1073_pnas.0709530105 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0709530105; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Disclosure of the mycobacterial outer membrane: cryo-electron tomography and vitreous sections reveal the lipid bilayer structure. PMID 18316738; DOI 10.1073/pnas.0709530105. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-doi-10.1128_JB.01919-07 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/JB.01919-07; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Direct visualization of the outer membrane of mycobacteria and corynebacteria in their native state. PMID 18567661; DOI 10.1128/jb.01919-07. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-doi-10.1016_j.tim.2009.12.005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.tim.2009.12.005; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Mycobacterial outer membranes: in search of proteins. PMID 20060722; DOI 10.1016/j.tim.2009.12.005. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-doi-10.1101_cshperspect.a021113 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1101/cshperspect.a021113; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies The Mycobacterial Cell Wall--Peptidoglycan and Arabinogalactan. PMID 25818664; DOI 10.1101/cshperspect.a021113. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-doi-10.1038_s41598-017-12718-4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/s41598-017-12718-4; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Dissecting the mycobacterial cell envelope and defining the composition of the native mycomembrane. PMID 28993692; DOI 10.1038/s41598-017-12718-4. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-marrakchi-meta-retry | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A24374164%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Mycolic acids: structures, biosynthesis, and beyond. PMID 24374164; DOI 10.1016/j.chembiol.2013.11.011. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-jats-PMC2931330 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2931330.1/PMC2931330.1.xml; Complete review sectionsS1–S4 and S9 including its Box1 context; remaining transport-pathway sections not fully audited. | supports | Niederweis et al.2010 reviews native membrane evidence, porin uptake and alternative lipid arrangements. Its S2 explicitly says extractable lipids may occupy both leaflets and the in situ conformation of mycolates is unknown; S3 supports the MspA diffusion pathway with species-qualified function. |
| root18-sources-legacy-PMC2268800 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2268800/; Abstract/Introduction17–22; all Results24–42 and Discussion43–53 with main captions; culture Methods55–56. No figure-pixel, tomography-volume or full image-processing reanalysis. | supports | Hoffmann et al.2008 directly resolves native outer-membrane bilayers and absence of the bilayer in tested C.glutamicum delta-pks13. Its Discussion contrasts possible lipid arrangements rather than establishing one exclusive inner/outer-leaflet composition. |
| root18-sources-legacy-PMC2519390 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2519390/; Abstract/Introduction18–20; culture Methods27–28; complete C.glutamicum WT/mutant Results60–66 with Fig5 caption. Other Results and complete Discussion not independently reread. | supports | Zuber et al.2008 supports a C.glutamicum outer-membrane example and its loss in the mycolate-deficient mutant. The paper distinguishes native structures from cutting artifacts and frames its lipid arrangement as a model. |
| root18-sources-jats-PMC5634507 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5634507.1/PMC5634507.1.xml; IntroductionSec1; complete ResultsSec3–Sec6 and DiscussionSec7 with captions; MethodsSec9/10 culture/fractionation and Sec14/15 lipid/mycolate analyses. Proteomics raw data, supplementary inventories and remaining Methods not reanalysed. | supports | Chiaradia et al.2017 isolates mycomembrane-containing cell walls, not the detached pure membrane, from M.aurum and M.smegmatis mc2155. Fraction markers and MspA localization support identity; lipid analyses support heterogeneous extractable material while leaflet assignment remains explicitly presumed and species/method dependent. GPL-mutant reasoning is not proof that every lipid-pool constituent is dispensable. |
| root18-sources-legacy-PMC4526729 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4526729/; Abstract/Introduction13–19 and complete Structural Features of Arabinogalactan32–34; detailed biosynthetic-enzyme chapters not audited. | supports | Alderwick et al.2015 reviews covalent PG–AG attachment and mycolates esterified to terminal arabinan. This supports the graph contextual anchoring chain without making the full mAGP complex equivalent to its outer membrane. |
| root18-sources-marrakchi-doi-route | https://doi.org/10.1016/j.chembiol.2013.11.011; Actual source-access response, not article content | context_only | The verified DOI resolves to the publisher linking page for S1074552113004201; the HTTP200 redirect HTML contains no review body. Marrakchi2014 is assessed only from verified native metadata and abstract. |
| root18-sources-UniProtKB-A0QR29 | https://rest.uniprot.org/uniprotkb/A0QR29.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is A0QR29, UniProtKB reviewed (Swiss-Prot), organism taxon 246196. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root18-sources-UniProtKB-H7C6A6 | https://rest.uniprot.org/uniprotkb/H7C6A6.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is H7C6A6, UniProtKB unreviewed (TrEMBL), organism taxon 1718. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root18-sources-UniProtKB-H7C685 | https://rest.uniprot.org/uniprotkb/H7C685.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is H7C685, UniProtKB unreviewed (TrEMBL), organism taxon 1718. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root18-sources-query-mspA-246196 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AmspA%29%20AND%20%28taxonomy_id%3A246196%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 1 entries: A0QR29. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root18-sources-query-porA-1718 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AporA%29%20AND%20%28taxonomy_id%3A1718%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 0 entries: none. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root18-sources-query-porB-1718 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AporB%29%20AND%20%28taxonomy_id%3A1718%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 0 entries: none. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root18-sources-PMID-9790664 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9790664%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Biochemical and biophysical characterization of the cell wall porin of Corynebacterium glutamicum: the channel is formed by a low molecular mass polypeptide. PMID 9790664; DOI 10.1021/bi980961e. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| root18-sources-PMID-14622416 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A14622416%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Identification of an anion-specific channel in the cell wall of the Gram-positive bacterium Corynebacterium glutamicum. PMID 14622416; DOI 10.1046/j.1365-2958.2003.03754.x. Bibliographic fields and returned abstract were inspected; this row does not attest a full-text read. |
| native-verify | /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/mycolate_outer_membrane.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/mycolate_outer_membrane.yaml --causal-graphs; Exact focused native output | supports | data/structures/envelope/mycolate_outer_membrane.yaml  (GO:0036407)<br>  mycolyl_arabinogalactan_mycomembrane	mycolate_outer_membrane_proteins	COVERED	-&gt;mycolate_outer_membrane_proteins (UniProtKB:A0QR29, UniProtKB:H7C6A6, UniProtKB:H7C685)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/envelope/mycolate_outer_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/mycolate_outer_membrane.yaml |
| strict-result | just validate-strict data/structures/envelope/mycolate_outer_membrane.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/mycolate_outer_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/mycolate_outer_membrane.yaml --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/mycolate_outer_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/mycolate_outer_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/mycolate_outer_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 19 of19 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Marrakchi2014 full text was not recovered. Its survival abstract is not substituted for the structural mutant evidence in Hoffmann/Zuber. An earlier guessed publisher path is retained as an unused failed route and is not cited as article content.
- PorA/PorB primary source identities and abstracts were checked, not full article bodies; the maintained UniProt examples remain accurately unreviewed and identity-only.
- Primary microscopy sources were read at stated text/caption scopes without pixel or raw-volume reanalysis. Chiaradia measured MMCW fractions, not purified leaflet composition; method/species differences and contamination caveats are preserved.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T101620Z-mycolate-outer-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Envelope identity, composition and evidence review
started_at: '2026-10-21T09:59:40Z'
finished_at: '2026-10-21T10:16:20Z'
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
summary: The mycomembrane identity, chemical classes, model examples and three protein
  identities are supported. One minor finding concerns certainty of leaflet organization
  in otherwise useful descriptive architecture.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
  state: working_tree
  inputs:
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
  - path: data/structures/envelope/mycolate_outer_membrane.yaml
    sha256: f120a57e032cb65c20843bb2847f7d9647c1fc1d70a011f2853dbe7670584881
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
  - path: scripts/score_causal_graphs.py
    sha256: 5ffe450c5b37c3dc3b0e62672caf0d99b358c8249fcc98a8c4fc7d78e8cd0d2f
    role: context
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0036407
  path: data/structures/envelope/mycolate_outer_membrane.yaml
  label: mycolate outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/mycolate_outer_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 6 in batch eighteen; exact sorted uncovered path at frozen fresh-main
    revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0036407
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0036407
  command: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/mycolate_outer_membrane.yaml
    --verify
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0036407
  command: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/mycolate_outer_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0036407
  command: just validate data/structures/envelope/mycolate_outer_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0036407
  command: just validate-strict data/structures/envelope/mycolate_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/mycolate_outer_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0036407
  summary: 19 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0036407
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0036407
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root18-sources-mycomembrane-go
  - root18-sources-NCBITaxon-2
  - root18-sources-NCBITaxon-1763
  - root18-sources-NCBITaxon-1772
  - root18-sources-NCBITaxon-1718
  - root18-sources-NCBITaxon-246196
  - root18-sources-CHEBI-25438
  - root18-sources-CHEBI-27569
  - root18-sources-doi-10.1073_pnas.0709530105
  - root18-sources-doi-10.1128_JB.01919-07
  - root18-sources-doi-10.1016_j.tim.2009.12.005
  - root18-sources-doi-10.1101_cshperspect.a021113
  - root18-sources-doi-10.1038_s41598-017-12718-4
  - root18-sources-marrakchi-meta-retry
  - root18-sources-jats-PMC2931330
  - root18-sources-legacy-PMC2268800
  - root18-sources-legacy-PMC2519390
  - root18-sources-jats-PMC5634507
  - root18-sources-legacy-PMC4526729
  - root18-sources-marrakchi-doi-route
  - root18-sources-UniProtKB-A0QR29
  - root18-sources-UniProtKB-H7C6A6
  - root18-sources-UniProtKB-H7C685
  - root18-sources-query-mspA-246196
  - root18-sources-query-porA-1718
  - root18-sources-query-porB-1718
  - root18-sources-PMID-9790664
  - root18-sources-PMID-14622416
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0036407
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
  - GO:0036407
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
  - GO:0036407
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
  - GO:0036407
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
  - GO:0036407
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
  reference: data/structures/envelope/mycolate_outer_membrane.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T10:07:58Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T10:07:58Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: root18-sources-mycomembrane-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009274,GO:0009279,GO:0036407
  locator: All three returned term definitions, synonyms and relevant is_a child relation
  accessed_at: '2026-10-21T10:01:00.050306Z'
  support: supports
  summary: GO0036407 provides the exact mycolate outer-membrane definition and all
    three exact synonyms; GO0009279 lists it as a child. The contextual peptidoglycan-wall
    node remains distinct from the target membrane.
  snapshot_sha256: 19f261e0339213d5436617b11887f040dc9740e7f09f2295612472df549abd61
- evidence_id: root18-sources-NCBITaxon-2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:01:00.576029Z'
  support: supports
  summary: Native ENA taxonomy identifies Bacteria at domain rank. Only this taxon's
    identity and names are asserted by this row, not occurrence or experimental stock
    identity.
  snapshot_sha256: 7429617438ff0162ee4783c4c660f6127642e6ff686522e670c6ecf3a5b28816
- evidence_id: root18-sources-NCBITaxon-1763
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1763
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:01:00.077028Z'
  support: supports
  summary: Native ENA taxonomy identifies Mycobacterium at genus rank. Only this taxon's
    identity and names are asserted by this row, not occurrence or experimental stock
    identity.
  snapshot_sha256: 0edbe7d1363d6ad3d4cdb1a289384b4c54d81416651598dfe18bab0aa852c454
- evidence_id: root18-sources-NCBITaxon-1772
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1772
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:01:00.167027Z'
  support: supports
  summary: Native ENA taxonomy identifies Mycolicibacterium smegmatis at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: 14b2ace8f8ab45a036ead963baa96eac95bfc3f9b253b5bcdfe624daf739c7b8
- evidence_id: root18-sources-NCBITaxon-1718
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1718
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:01:00.051872Z'
  support: supports
  summary: Native ENA taxonomy identifies Corynebacterium glutamicum at species rank.
    Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: 76df8d9b54ad5e11ffa9568c99005ba3ec62b304714cfe5f21d3dc93b5a2703a
- evidence_id: root18-sources-NCBITaxon-246196
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/246196
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:01:00.657548Z'
  support: supports
  summary: Native ENA taxonomy identifies Mycolicibacterium smegmatis MC2 155 at strain
    rank. Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: 868aa28908b63c934a864ff3443bdc04bd27783cd1e0241a1c08a1689bbda182
- evidence_id: root18-sources-CHEBI-25438
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/25438/
  locator: Exact accession, name, definition where present, synonyms and chemical-class
    relations
  accessed_at: '2026-10-21T10:01:00.743463Z'
  support: supports
  summary: Released three-star CHEBI:25438 identifies mycolic acid. Its chemical-class
    identity and returned definition/ontology relations are assessed independently
    of placement in a wall or membrane.
  snapshot_sha256: 858dfa40d0203d8d22fb393e394c28078ff4a7e00bf62850f9ea23594bbb5a52
- evidence_id: root18-sources-CHEBI-27569
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/27569/
  locator: Exact accession, name, definition where present, synonyms and chemical-class
    relations
  accessed_at: '2026-10-21T10:01:00.730587Z'
  support: supports
  summary: Released three-star CHEBI:27569 identifies arabinogalactan. Its chemical-class
    identity and returned definition/ontology relations are assessed independently
    of placement in a wall or membrane.
  snapshot_sha256: a4367dabdab575ee57322f816251499814905e0cf368c83b050d0c9008e35582
- evidence_id: root18-sources-doi-10.1073_pnas.0709530105
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0709530105
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:01:01.403658Z'
  support: supports
  summary: 'Native citation identifies Disclosure of the mycobacterial outer membrane:
    cryo-electron tomography and vitreous sections reveal the lipid bilayer structure.
    PMID 18316738; DOI 10.1073/pnas.0709530105. Bibliographic fields and returned
    abstract were inspected; this row does not attest a full-text read.'
  snapshot_sha256: 055886ec8e2259022eb6436b66db3c7b90777042d22a9cb383604c83b051ecb4
- evidence_id: root18-sources-doi-10.1128_JB.01919-07
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/JB.01919-07
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:01:02.017260Z'
  support: supports
  summary: Native citation identifies Direct visualization of the outer membrane of
    mycobacteria and corynebacteria in their native state. PMID 18567661; DOI 10.1128/jb.01919-07.
    Bibliographic fields and returned abstract were inspected; this row does not attest
    a full-text read.
  snapshot_sha256: a16e224a48c8e2f35fc90342d5505e3e74f61ad5f0f67707834517575da81692
- evidence_id: root18-sources-doi-10.1016_j.tim.2009.12.005
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.tim.2009.12.005
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:01:04.528963Z'
  support: supports
  summary: 'Native citation identifies Mycobacterial outer membranes: in search of
    proteins. PMID 20060722; DOI 10.1016/j.tim.2009.12.005. Bibliographic fields and
    returned abstract were inspected; this row does not attest a full-text read.'
  snapshot_sha256: 1c27bfc89478effe14223e69b359be10d9b89a94c0788b54892e79b39f5a740c
- evidence_id: root18-sources-doi-10.1101_cshperspect.a021113
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1101/cshperspect.a021113
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:01:01.554256Z'
  support: supports
  summary: Native citation identifies The Mycobacterial Cell Wall--Peptidoglycan and
    Arabinogalactan. PMID 25818664; DOI 10.1101/cshperspect.a021113. Bibliographic
    fields and returned abstract were inspected; this row does not attest a full-text
    read.
  snapshot_sha256: a98b0066e2f88e6c8bcfeb242e09b492d2fa74d06b4cd422f22ab9e7fd3f092c
- evidence_id: root18-sources-doi-10.1038_s41598-017-12718-4
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/s41598-017-12718-4
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:01:01.988125Z'
  support: supports
  summary: Native citation identifies Dissecting the mycobacterial cell envelope and
    defining the composition of the native mycomembrane. PMID 28993692; DOI 10.1038/s41598-017-12718-4.
    Bibliographic fields and returned abstract were inspected; this row does not attest
    a full-text read.
  snapshot_sha256: b9f7cb69aa92824d7b078d37a5f5227ebeaae6320ce344b22e052db97dd7bdc2
- evidence_id: root18-sources-marrakchi-meta-retry
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A24374164%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:02:16.212888Z'
  support: supports
  summary: 'Native citation identifies Mycolic acids: structures, biosynthesis, and
    beyond. PMID 24374164; DOI 10.1016/j.chembiol.2013.11.011. Bibliographic fields
    and returned abstract were inspected; this row does not attest a full-text read.'
  snapshot_sha256: 5d2e22bdc8f0d743f3bcafbd0298adefc6b5404bff2fe47b5007b003a699ef28
- evidence_id: root18-sources-jats-PMC2931330
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2931330.1/PMC2931330.1.xml
  locator: Complete review sectionsS1–S4 and S9 including its Box1 context; remaining
    transport-pathway sections not fully audited.
  accessed_at: '2026-10-21T10:02:15.985802Z'
  support: supports
  summary: Niederweis et al.2010 reviews native membrane evidence, porin uptake and
    alternative lipid arrangements. Its S2 explicitly says extractable lipids may
    occupy both leaflets and the in situ conformation of mycolates is unknown; S3
    supports the MspA diffusion pathway with species-qualified function.
  snapshot_sha256: fb7483f4b10a97a7c9012e38e14ca42cf497602519eadec1bcefda0737cc5f43
- evidence_id: root18-sources-legacy-PMC2268800
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2268800/
  locator: Abstract/Introduction17–22; all Results24–42 and Discussion43–53 with main
    captions; culture Methods55–56. No figure-pixel, tomography-volume or full image-processing
    reanalysis.
  accessed_at: '2026-10-21T10:02:33.372816Z'
  support: supports
  summary: Hoffmann et al.2008 directly resolves native outer-membrane bilayers and
    absence of the bilayer in tested C.glutamicum delta-pks13. Its Discussion contrasts
    possible lipid arrangements rather than establishing one exclusive inner/outer-leaflet
    composition.
  snapshot_sha256: 36520dcd4d6b4e0cf12c57ea9b7a3383094757a56326591a8fe683946c7e4ed9
- evidence_id: root18-sources-legacy-PMC2519390
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2519390/
  locator: Abstract/Introduction18–20; culture Methods27–28; complete C.glutamicum
    WT/mutant Results60–66 with Fig5 caption. Other Results and complete Discussion
    not independently reread.
  accessed_at: '2026-10-21T10:02:33.681488Z'
  support: supports
  summary: Zuber et al.2008 supports a C.glutamicum outer-membrane example and its
    loss in the mycolate-deficient mutant. The paper distinguishes native structures
    from cutting artifacts and frames its lipid arrangement as a model.
  snapshot_sha256: 448dfec9c9727f4a4b80e688efb0d8efbb864472c80b95e1bfa7820070cf8e20
- evidence_id: root18-sources-jats-PMC5634507
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5634507.1/PMC5634507.1.xml
  locator: IntroductionSec1; complete ResultsSec3–Sec6 and DiscussionSec7 with captions;
    MethodsSec9/10 culture/fractionation and Sec14/15 lipid/mycolate analyses. Proteomics
    raw data, supplementary inventories and remaining Methods not reanalysed.
  accessed_at: '2026-10-21T10:02:16.021440Z'
  support: supports
  summary: Chiaradia et al.2017 isolates mycomembrane-containing cell walls, not the
    detached pure membrane, from M.aurum and M.smegmatis mc2155. Fraction markers
    and MspA localization support identity; lipid analyses support heterogeneous extractable
    material while leaflet assignment remains explicitly presumed and species/method
    dependent. GPL-mutant reasoning is not proof that every lipid-pool constituent
    is dispensable.
  snapshot_sha256: b1e619d1fe5bb256b03df333c8d5681e58673f05d58941032411a686667b547a
- evidence_id: root18-sources-legacy-PMC4526729
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4526729/
  locator: Abstract/Introduction13–19 and complete Structural Features of Arabinogalactan32–34;
    detailed biosynthetic-enzyme chapters not audited.
  accessed_at: '2026-10-21T10:02:33.784608Z'
  support: supports
  summary: Alderwick et al.2015 reviews covalent PG–AG attachment and mycolates esterified
    to terminal arabinan. This supports the graph contextual anchoring chain without
    making the full mAGP complex equivalent to its outer membrane.
  snapshot_sha256: da78b290f585df7fcf89878ee430dfc1ce09f67a82bbef26febdd2ea86430516
- evidence_id: root18-sources-marrakchi-doi-route
  kind: authority
  reference: https://doi.org/10.1016/j.chembiol.2013.11.011
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:05:12.180117Z'
  support: context_only
  summary: The verified DOI resolves to the publisher linking page for S1074552113004201;
    the HTTP200 redirect HTML contains no review body. Marrakchi2014 is assessed only
    from verified native metadata and abstract.
  snapshot_sha256: 399fc8b506825690939ca5d876b5055a0da43bf47fea1d4bda7103ff7c208a59
- evidence_id: root18-sources-UniProtKB-A0QR29
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0QR29.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:01:00.709936Z'
  support: supports
  summary: The primary accession is A0QR29, UniProtKB reviewed (Swiss-Prot), organism
    taxon 246196. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: c723f93af526ad145205651ae7b64414298a75d4832aef546922ebf76d125f71
- evidence_id: root18-sources-UniProtKB-H7C6A6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/H7C6A6.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:01:01.184236Z'
  support: supports
  summary: The primary accession is H7C6A6, UniProtKB unreviewed (TrEMBL), organism
    taxon 1718. Exact name/gene tokens, evidence-qualified location comments and linked
    publication metadata were inspected. Database identity is not independently a
    formation-necessity experiment.
  snapshot_sha256: 1af1cf8380c422b11c90b959815a925c75f88f6ebf54736e7ca9a22823d51576
- evidence_id: root18-sources-UniProtKB-H7C685
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/H7C685.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:01:00.774453Z'
  support: supports
  summary: The primary accession is H7C685, UniProtKB unreviewed (TrEMBL), organism
    taxon 1718. Exact name/gene tokens, evidence-qualified location comments and linked
    publication metadata were inspected. Database identity is not independently a
    formation-necessity experiment.
  snapshot_sha256: 101f8e14dc6587fbaae3b76e34cbb7971e9222249bd02ac0c90860cda8f2422b
- evidence_id: root18-sources-query-mspA-246196
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AmspA%29%20AND%20%28taxonomy_id%3A246196%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:01:02.120303Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 1 entries: A0QR29. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: 99ce06ef602773faf64f94e64e190d66229e66b8b5f370cbdf313dee27bdb94f
- evidence_id: root18-sources-query-porA-1718
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AporA%29%20AND%20%28taxonomy_id%3A1718%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:01:02.272457Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 0 entries: none. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: root18-sources-query-porB-1718
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AporB%29%20AND%20%28taxonomy_id%3A1718%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:01:02.619637Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 0 entries: none. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: 5021e624e752b001ce3e3846e8f158ed4aeb93a4c9a72fdb35a0c5b14a0eea84
- evidence_id: root18-sources-PMID-9790664
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9790664%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:04:41.403859Z'
  support: supports
  summary: 'Native citation identifies Biochemical and biophysical characterization
    of the cell wall porin of Corynebacterium glutamicum: the channel is formed by
    a low molecular mass polypeptide. PMID 9790664; DOI 10.1021/bi980961e. Bibliographic
    fields and returned abstract were inspected; this row does not attest a full-text
    read.'
  snapshot_sha256: 411ba26c08ed8c73f699b981b1c30a302301dd9bc91e33457ec47a0fb0ffa59d
- evidence_id: root18-sources-PMID-14622416
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14622416%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:04:41.330964Z'
  support: supports
  summary: Native citation identifies Identification of an anion-specific channel
    in the cell wall of the Gram-positive bacterium Corynebacterium glutamicum. PMID
    14622416; DOI 10.1046/j.1365-2958.2003.03754.x. Bibliographic fields and returned
    abstract were inspected; this row does not attest a full-text read.
  snapshot_sha256: a6e7eac3fedf6a6ab5650660842d8ef48715fbef56b75dd4c29795773daed53d
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/mycolate_outer_membrane.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:03:58.516681Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/mycolate_outer_membrane.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:03:59.061174Z'
  support: supports
  summary: "data/structures/envelope/mycolate_outer_membrane.yaml  (GO:0036407)\n\
    \  mycolyl_arabinogalactan_mycomembrane\tmycolate_outer_membrane_proteins\tCOVERED\t\
    ->mycolate_outer_membrane_proteins (UniProtKB:A0QR29, UniProtKB:H7C6A6, UniProtKB:H7C685)\n\
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
  snapshot_sha256: f94b46240696c8791817dde50f1407df1ace900c88a02f91bfc9fd3bee2e33ed
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/mycolate_outer_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:42Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/mycolate_outer_membrane.yaml'
  snapshot_sha256: 2c72c5b4d1dd7d999733183c86c61294b173f2274513f388a40aee4201983073
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/mycolate_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/mycolate_outer_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:59:44Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/mycolate_outer_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/mycolate_outer_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch18-20261021-5wxxz5kh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch18-20261021-5wxxz5kh/mycolate_outer_membrane-strict.tsv"
  snapshot_sha256: 0498beb5be012c1562522d7519a54d1812763459724a6704404f80064ab4cb44
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/mycolate_outer_membrane.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:07:58Z'
  support: supports
  summary: '19 of19 collected target identifiers returned OK in this fresh base resolver
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
  topic: Mycomembrane distinguished from the entire wall core
  outcome: supported
  target_ids:
  - GO:0036407
  summary: Exact GO identity, synonyms and outer-membrane parent are supported. The
    definition retains the mycolate-rich bilayer and covalent AG–PG linkage. The resolved
    boundary discussion correctly keeps AG and PG as contextual graph nodes rather
    than local membrane constituents.
  evidence_ids:
  - root18-sources-mycomembrane-go
  - root18-sources-legacy-PMC2268800
  - root18-sources-legacy-PMC2519390
  - root18-sources-legacy-PMC4526729
  - record
- assessment_id: materials
  area: grounding
  topic: Chemical class versus heterogeneous pools
  outcome: supported
  target_ids:
  - GO:0036407
  summary: Mycolic acid and contextual arabinogalactan match the verified material
    classes. Extractable lipids and outer-membrane proteins are heterogeneous pools,
    not single CHEBI or sequence families. Native fractions and review evidence support
    their presence; one universal lipid recipe is not warranted.
  evidence_ids:
  - root18-sources-mycomembrane-go
  - root18-sources-CHEBI-25438
  - root18-sources-CHEBI-27569
  - root18-sources-jats-PMC2931330
  - root18-sources-jats-PMC5634507
  - record
  - policy
- assessment_id: necessity
  area: evidence
  topic: Structural requirement for mycolates in the tested corynebacterial context
  outcome: supported
  target_ids:
  - GO:0036407
  summary: The tested C. glutamicum mycolate-deficient mutant lacks an outer-membrane
    bilayer, providing a structural endpoint distinct from viability. This supports
    a material requirement in that experimental context; it does not establish individual
    necessity of each extractable lipid or porin.
  evidence_ids:
  - root18-sources-legacy-PMC2268800
  - root18-sources-legacy-PMC2519390
  - root18-sources-jats-PMC2931330
  - root18-sources-jats-PMC5634507
  - record
  - policy
- assessment_id: pool-necessity
  area: evidence
  topic: Assembly necessity of heterogeneous lipid and protein pools
  outcome: unknown
  target_ids:
  - GO:0036407
  summary: Presence and uptake or growth effects do not establish whether every member
    of the extractable-lipid and outer-membrane-protein pools is required to form
    the membrane. The record uses CONDITIONAL for these pools; the reviewed evidence
    does not resolve that assembly-necessity classification. No individual requirement
    or dispensability is inferred.
  evidence_ids:
  - root18-sources-jats-PMC2931330
  - root18-sources-jats-PMC5634507
  - record
  - policy
- assessment_id: proteins
  area: evidence
  topic: Reviewed MspA and accurately labeled unreviewed porins
  outcome: supported
  target_ids:
  - GO:0036407
  summary: Accession/name/gene/taxon/status pairs match all three native entries.
    The exact reviewed query uniquely returns MspA and returns no reviewed PorA/PorB
    in the declared species. H7C6A6 links a sequenced MH20-22B PorA record; H7C685
    links the ATCC13032 PorB sequence. Their source-linked primary abstracts support
    the named porin identities and channels, while the maintained entry notes remain
    identity-only. Unreviewed status is not silently promoted.
  evidence_ids:
  - root18-sources-UniProtKB-A0QR29
  - root18-sources-UniProtKB-H7C6A6
  - root18-sources-UniProtKB-H7C685
  - root18-sources-query-mspA-246196
  - root18-sources-query-porA-1718
  - root18-sources-query-porB-1718
  - root18-sources-PMID-9790664
  - root18-sources-PMID-14622416
  - root18-sources-jats-PMC5634507
  - root18-sources-NCBITaxon-2
  - root18-sources-NCBITaxon-1763
  - root18-sources-NCBITaxon-1772
  - root18-sources-NCBITaxon-1718
  - root18-sources-NCBITaxon-246196
  - record
- assessment_id: taxa
  area: scope
  topic: Source-supported model taxa with historical names
  outcome: supported
  target_ids:
  - GO:0036407
  summary: Bacterial distribution is explicitly variable. Mycobacteria and related
    corynebacteria are supported; M.smegmatis mc2155 and C.glutamicum are directly
    represented in the primary sources. ENA currently uses Mycolicibacterium smegmatis
    for1772; the maintained older genus name is the historical source name, not a
    different organism. No prevalence census is asserted.
  evidence_ids:
  - root18-sources-NCBITaxon-2
  - root18-sources-NCBITaxon-1763
  - root18-sources-NCBITaxon-1772
  - root18-sources-NCBITaxon-1718
  - root18-sources-NCBITaxon-246196
  - root18-sources-jats-PMC2931330
  - root18-sources-jats-PMC5634507
  - root18-sources-legacy-PMC2519390
  - record
- assessment_id: function
  area: evidence
  topic: Permeability barrier and scoped protein channels
  outcome: supported
  target_ids:
  - GO:0036407
  summary: The membrane barrier and porin-mediated hydrophilic uptake are supported
    by the review and native fractions. MspA evidence is species-specific; the record
    is not read as saying every mycobacterium carries MspA or that every identified
    outer-membrane protein is a general porin.
  evidence_ids:
  - root18-sources-jats-PMC2931330
  - root18-sources-jats-PMC5634507
  - root18-sources-PMID-9790664
  - root18-sources-PMID-14622416
  - record
- assessment_id: architecture
  area: graph
  topic: Preserve uncertainty of leaflet partition
  outcome: concern
  target_ids:
  - GO:0036407
  summary: The explicitly NONMECHANISTIC graph correctly gives class-level anchoring
    and membrane architecture. However, component roles and the pack-into edge state
    inner/outer-leaflet assignments without the model qualifications present in the
    cited papers. This is a bounded certainty issue; bilayer existence and covalent
    linkage remain supported.
  evidence_ids:
  - root18-sources-jats-PMC2931330
  - root18-sources-legacy-PMC2268800
  - root18-sources-jats-PMC5634507
  - root18-sources-legacy-PMC4526729
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0036407
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Exact additional polymer inventories, numerical properties,
    images, traits and expanded mechanisms are optional. No verbatim quotation requires
    repair, and no status or history rewrite is proposed. A clean result does not
    assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - root18-sources-mycomembrane-go
  - root18-sources-NCBITaxon-2
  - root18-sources-NCBITaxon-1763
  - root18-sources-NCBITaxon-1772
  - root18-sources-NCBITaxon-1718
  - root18-sources-NCBITaxon-246196
  - root18-sources-CHEBI-25438
  - root18-sources-CHEBI-27569
  - root18-sources-doi-10.1073_pnas.0709530105
  - root18-sources-doi-10.1128_JB.01919-07
  - root18-sources-doi-10.1016_j.tim.2009.12.005
  - root18-sources-doi-10.1101_cshperspect.a021113
  - root18-sources-doi-10.1038_s41598-017-12718-4
  - root18-sources-marrakchi-meta-retry
  - root18-sources-jats-PMC2931330
  - root18-sources-legacy-PMC2268800
  - root18-sources-legacy-PMC2519390
  - root18-sources-jats-PMC5634507
  - root18-sources-legacy-PMC4526729
  - root18-sources-marrakchi-doi-route
  - root18-sources-UniProtKB-A0QR29
  - root18-sources-UniProtKB-H7C6A6
  - root18-sources-UniProtKB-H7C685
  - root18-sources-query-mspA-246196
  - root18-sources-query-porA-1718
  - root18-sources-query-porB-1718
  - root18-sources-PMID-9790664
  - root18-sources-PMID-14622416
findings:
- finding_id: F1
  issue_key: mycomembrane-leaflet-model-certainty
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Retain the sources' uncertainty about leaflet organization
  description: The mycolic-acid role presents a covalently attached inner leaflet
    and the extractable-lipid role/graph present outer-leaflet packing as settled
    architecture. Niederweis2010 explicitly discusses extractable lipids in both leaflets
    and unknown mycolate conformation; Hoffmann2008 gives alternative models, and
    Chiaradia2017 still calls the outer-leaflet assignment presumed. Qualify the arrangement
    as a source-scoped model without disputing the observed bilayer or covalent AG
    linkage.
  target_ids:
  - GO:0036407
  field_paths:
  - components[component_id=mycolic_acid].role
  - components[component_id=extractable_mycomembrane_lipids].role
  - components[component_id=extractable_mycomembrane_lipids].grounding_notes
  - causal_graphs[graph_id=mycolyl_arabinogalactan_mycomembrane].edges[subject=extractable_mycomembrane_lipids,predicate=pack
    into,object=mycolate_outer_membrane]
  evidence_ids:
  - root18-sources-jats-PMC2931330
  - root18-sources-legacy-PMC2268800
  - root18-sources-jats-PMC5634507
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/mycolate_outer_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The target identity, membrane existence and component classes
    are sound; source uncertainty is lost in a bounded architectural formulation.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0036407
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/mycolate_outer_membrane.yaml
    role: maintained scientific record
  description: Qualify leaflet assignments as the cited model and preserve the possibility
    of extractable material in both leaflets; retain the directly supported bilayer
    and covalent linkage.
  acceptance_checks:
  - Separate observed membrane structure and biochemical fraction composition from
    inferred leaflet placement.
  - Do not infer a universal composition or individual lipid/porin formation necessity.
  - Any scientific edit requires separate curation authorization, guarded writes,
    append-only history and native validation/rendering.
limitations:
- Marrakchi2014 full text was not recovered. Its survival abstract is not substituted
  for the structural mutant evidence in Hoffmann/Zuber. An earlier guessed publisher
  path is retained as an unused failed route and is not cited as article content.
- PorA/PorB primary source identities and abstracts were checked, not full article
  bodies; the maintained UniProt examples remain accurately unreviewed and identity-only.
- Primary microscopy sources were read at stated text/caption scopes without pixel
  or raw-volume reanalysis. Chiaradia measured MMCW fractions, not purified leaflet
  composition; method/species differences and contamination caveats are preserved.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches
  and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization;
  identifier transport and label-adapter limits remain explicit.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized one review for every uncovered target, including
  a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
