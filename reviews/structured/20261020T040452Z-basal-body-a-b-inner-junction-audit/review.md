# Basal-body A-B inner junction evidence and provenance review

- Review: 20261020T040452Z-basal-body-a-b-inner-junction-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T04:00:43Z
- Finished UTC: 2026-10-20T04:04:52Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The structural identity, seven bounded component classes, five contact edges, three reconstructions and hosted image are supported. One minor provenance finding affects the gene-field wording and symbol mappings of five protein examples.

## Scope And Provenance

Entire record including all components/examples, graph, discussions, datasets and image; both structural papers and the original Poc1 localization source.

Selection: Tenth unreviewed path of batch3.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:basal_body_a_b_inner_junction | data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml | maintained | basal body A-B inner junction |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:basal_body_a_b_inner_junction | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:basal_body_a_b_inner_junction | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:basal_body_a_b_inner_junction | 14 identifiers OK; 6 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:basal_body_a_b_inner_junction | No expression-module or transcriptomic claim is asserted; the named-protein questions are assessed through UniProt, InterPro, structural archives and primary papers. |
| Claim-level scientific review | passed | True | cellstructuremech:basal_body_a_b_inner_junction | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:basal_body_a_b_inner_junction | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:basal_body_a_b_inner_junction | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:basal_body_a_b_inner_junction | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:basal_body_a_b_inner_junction | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:basal_body_a_b_inner_junction | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Basal-body junction versus axonemal junction

identity: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

The maintained identity denotes a multiprotein basal-body interface supported by two structural studies. The broad parent and basal-body parthood are valid; the axonemal junction remains distinct.

### Region-specific structural assignments

evidence: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

The seven component classes are supported at their stated evidence level. Proximal FAP52-like identity, core LRR candidate and scaffold stem remain unresolved; neither mutant replacement proteins nor generic tubulin substrates are incorrectly added as ordinary components.

### Exact families versus domains

grounding: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

The two family groundings are exact. The remaining label-only treatment is justified; the additional current POC1 domain does not resolve family identity. The ladder’s bounded no-match claim is reproducible.

### Named symbols and reference loci

provenance: concern. Targets: cellstructuremech:basal_body_a_b_inner_junction.

All five entries resolve and their labels/statuses match, but their ORF fields are called primary gene names and independent symbol mappings are omitted. FAP106B and the family-related W7XDG5 exemplar must remain distinct from the fitted model identities.

### Strain and experiment boundaries

scope: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

Species-level canonical scope is supported. B2086 basal bodies, SB715 ladder study, SB210 sequences and CU428 axonemal models remain explicitly separated. No broad prevalence or uniform knockout failure is asserted.

### Luminal connection and scaffold attachment

evidence: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

Source structures support connection and attachment roles without establishing a unique force threshold, junction-specific pleiotropic phenotype or temporal assembly sequence.

### Five model-derived contacts

graph: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

Poc1 contacts A1/B10; FAP52 contacts B9/B10; IJ34 anchors to A-tubule and tethers FAP52 through its C-terminal helix. The MECHANISTIC contact-network scope explicitly states fitted-model evidence and does not convert possible FAP106/FAP210 contacts into measured binding edges.

### Three released reconstructions and excluded conflicting label

provenance: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

Region, repeat, source organism and citation joins match the three native A-B deposits. The B-C title conflict is preserved outside the linked dataset list.

### Representative image provenance

evidence: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

The hosted density rendering, exact byte hash, source, caption and stated copyright convention are supported. The article figures were inspected separately and are not copied into the corpus.

### Open scientific uncertainties

completeness: supported. Targets: cellstructuremech:basal_body_a_b_inner_junction.

The later ladder identification is integrated without claiming unique perturbation proof. Remaining uncertainties are scientifically bounded rather than silently promoted; PROPOSED status is appropriate.

## Findings

### F1: Protein examples misattribute symbol mappings and ORF names to UniProt primary names

minor / open / confirmed; issue key: basal-body-a-b-inner-junction-example-symbol-provenance.

All five example roles call the TTHERM identifiers primary names, but native UniProt supplies only orfNames. UniProt does not explicitly map the stated POC1/FAP symbols in its gene fields. Cite the independent mapping sources and distinguish family/paralog representatives from fitted proteins: I7LU20 is CFAP106B in the2023 supplement, and W7XDG5 is a related CFAP210-family hit rather than the Q23EX8 model used by8G2Z. This is a bounded provenance defect, not evidence that all selected accession families are wrong.

## Recommended Actions And Acceptance Checks

### A1

Describe TTHERM identifiers as ORF/locus names. Attach explicit symbol-to-accession mappings and qualify paralog/family exemplars; retain separation from the fitted experimental protein identities.

- Each symbol mapping cites a source that actually states it or is explicitly qualified as a family/paralog representative.
- I7LU20 is not silently equated to the modeled CFAP106A; W7XDG5 is not equated to the Q23EX8 CFAP210 model.
- Preserve all strain, model-fitting and mutant limitations.
- After separately authorized curation, run native record, history and generated-page checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| basal-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140535,GO:0036064,GO:0160113; Three exact native terms | supports | The broad intracellular-complex parent and basal-body part are correct. GO0160113 specifically denotes the axonemal doublet junction and is not an exact identity for this basal-body structure. |
| basal-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&amp;limit=100; Complete paginated search results | context_only | One page of the complete659-result search for basal body inner junction; all seven pages were inspected together. The only inner-junction-labelled result is the distinct axonemal term. This is bounded search evidence, not proof that no differently worded term could exist. |
| basal-go-search-2 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&amp;limit=100&amp;page=2; Complete paginated search results | context_only | One page of the complete659-result search for basal body inner junction; all seven pages were inspected together. The only inner-junction-labelled result is the distinct axonemal term. This is bounded search evidence, not proof that no differently worded term could exist. |
| basal-go-search-3 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&amp;limit=100&amp;page=3; Complete paginated search results | context_only | One page of the complete659-result search for basal body inner junction; all seven pages were inspected together. The only inner-junction-labelled result is the distinct axonemal term. This is bounded search evidence, not proof that no differently worded term could exist. |
| basal-go-search-4 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&amp;limit=100&amp;page=4; Complete paginated search results | context_only | One page of the complete659-result search for basal body inner junction; all seven pages were inspected together. The only inner-junction-labelled result is the distinct axonemal term. This is bounded search evidence, not proof that no differently worded term could exist. |
| basal-go-search-5 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&amp;limit=100&amp;page=5; Complete paginated search results | context_only | One page of the complete659-result search for basal body inner junction; all seven pages were inspected together. The only inner-junction-labelled result is the distinct axonemal term. This is bounded search evidence, not proof that no differently worded term could exist. |
| basal-go-search-6 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&amp;limit=100&amp;page=6; Complete paginated search results | context_only | One page of the complete659-result search for basal body inner junction; all seven pages were inspected together. The only inner-junction-labelled result is the distinct axonemal term. This is bounded search evidence, not proof that no differently worded term could exist. |
| basal-go-search-7 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&amp;limit=100&amp;page=7; Complete paginated search results | context_only | One page of the complete659-result search for basal body inner junction; all seven pages were inspected together. The only inner-junction-labelled result is the distinct axonemal term. This is bounded search evidence, not proof that no differently worded term could exist. |
| outer-junction-taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=5911,312017; Exact native taxonomic entries | supports | Species5911 and reference strain312017 match Tetrahymena thermophila and SB210. |
| basal-proteins | https://rest.uniprot.org/uniprotkb/search?query=accession:Q229Z6%20OR%20accession:Q22ZH2%20OR%20accession:I7LU20%20OR%20accession:W7XCX2%20OR%20accession:W7XDG5%20OR%20accession:Q23EX8%20OR%20accession:I7M9T0%20OR%20accession:I7LY02%20OR%20accession:I7MJ23%20OR%20accession:Q24C92%20OR%20accession:I7MLQ3%20OR%20accession:Q22N53&amp;format=json; Complete entries; genes, labels, statuses, organisms and InterPro references | context_only | Twelve named reference accessions resolve with the expected strain. The five example labels/statuses match, but all five genes fields contain only ORF names, not primary geneName values or the stated POC1/FAP symbols. Current InterPro cross-references support family/domain distinctions. |
| basal-li | https://pmc-oa-opendata.s3.amazonaws.com/PMC11961760.1/PMC11961760.1.xml; Proximal/core and mutant Results; Figures2,4,EV4; Discussion and strain Methods | supports | Primary Results distinguish proximal/core composition, model-fitted MIPs, unresolved LRR identity and heterogeneous mutant replacements. The five core contact claims match the described fitted models; Methods identify B2086. |
| basal-cai | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/PMC12506977.1.xml; Junction Results, Figure4 and assignment/sample Methods | supports | The later study assigns the alpha-helical junction ladders to I7LY02 by predicted-model fitting. Figure4D-F places the second array at A-B; Methods identify SB715. The unassigned B-C WD40 ladder remains distinct. |
| basal-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s44318-025-00392-6%20OR%20DOI:10.1126/sciadv.ady3689%20OR%20EXT_ID:20008567&amp;format=json&amp;resultType=core; Complete three-result bibliographic joins | supports | Both structural DOIs and the two cited PMIDs match exact titles and PMC identities. |
| basal-poc1-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC2806327.1/PMC2806327.1.xml; Results on GFP constructs and basal-body localization; FigureS2 discussion | supports | Full-length Poc1 and its WD40 region localize to basal bodies in the original study, consistent with the selected UniProt localization provenance. |
| basal-pdb-mappings-valid | https://data.rcsb.org/graphql?query=%7Bentry%28entry_id%3A%228G2Z%22%29%7Bpolymer_entities%7Brcsb_id%20rcsb_polymer_entity%7Bpdbx_description%7D%20rcsb_polymer_entity_container_identifiers%7Breference_sequence_identifiers%7Bdatabase_accession%20database_name%7D%7D%7D%7D%7D; Complete polymer-entity descriptions and UniProt mappings | supports | RCSB8G2Z maps CFAP52A to Q22ZH2, IJ34 to I7M9T0, CFAP45 to W7XCX2 and CFAP210 to Q23EX8. These corroborate the model identifiers, not the identity of every optional paralog exemplar. |
| basal-pdb8g2z | https://data.rcsb.org/rest/v1/core/entry/8G2Z; Entry title and primary citation | supports | The source model is a48-nm axonemal doublet from CU428; it is not a B2086 basal-body deposition. |
| basal-pdb9qzc8 | https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/8; Exact entity mapping | supports | Entity8 maps to I7LY02, supporting the ladder model’s sequence identity. |
| basal-pdb9qzc | https://data.rcsb.org/rest/v1/core/entry/9QZC; Entry title and citation | supports | 9QZC is a proximal A-C-linker repeating-unit deposition with the Cai2025 citation, not an A-B-specific deposition. |
| outer-junction-supplement | https://pmc-oa-opendata.s3.amazonaws.com/PMC10105768.1/41467_2023_37868_MOESM1_ESM.pdf; Supplementary Tables3-4; relevant rows | supports | Table3 names CFAP106B as I7LU20 and CFAP210 as Q23EX8. Table4 lists W7XDG5 as a related hit rather than the named CFAP210 structural model. This supplies missing distinctions between identity exemplars and exact model accessions. |
| basal-IPR050505 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050505; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR020472 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020472; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR050630 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050630; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR052102 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052102; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR027012 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027012; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR028034 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028034; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR040673 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040673; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR033253 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033253; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR039986 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039986; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| basal-IPR056551 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056551; Entry metadata and description | supports | Native entry type/name and definition inspected. IPR033253 and IPR039986 are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats. Newly present IPR056551 is a domain, not a POC1 family resolution. |
| ladder-no-integrated-match | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/I7LY02/; Integrated InterPro entries for UniProtI7LY02 | context_only | The native integrated-entry endpoint returned HTTP204; UniProt also lists no InterPro/Pfam cross-reference. This bounded negative result does not imply absence of the protein or structure. |
| basal-emdb46437 | https://www.ebi.ac.uk/emdb/api/entry/EMD-46437; Admin, natural source and primary citation | supports | Native released entry, title, source taxon5911, depositor authors and exact DOI/PMID citation inspected. The three A-B entries match their region/repeat labels; the excluded46438 entry is proximal B-C, confirming the stated article/archive discrepancy. |
| basal-emdb46439 | https://www.ebi.ac.uk/emdb/api/entry/EMD-46439; Admin, natural source and primary citation | supports | Native released entry, title, source taxon5911, depositor authors and exact DOI/PMID citation inspected. The three A-B entries match their region/repeat labels; the excluded46438 entry is proximal B-C, confirming the stated article/archive discrepancy. |
| basal-emdb46440 | https://www.ebi.ac.uk/emdb/api/entry/EMD-46440; Admin, natural source and primary citation | supports | Native released entry, title, source taxon5911, depositor authors and exact DOI/PMID citation inspected. The three A-B entries match their region/repeat labels; the excluded46438 entry is proximal B-C, confirming the stated article/archive discrepancy. |
| basal-emdb46438 | https://www.ebi.ac.uk/emdb/api/entry/EMD-46438; Admin, natural source and primary citation | supports | Native released entry, title, source taxon5911, depositor authors and exact DOI/PMID citation inspected. The three A-B entries match their region/repeat labels; the excluded46438 entry is proximal B-C, confirming the stated article/archive discrepancy. |
| basal-policy | https://www.ebi.ac.uk/emdb/policies.html; Section3.1.2 | supports | EMDB policy3.1.2 requires representative figures without copyright restrictions, consistent with the record’s declared licence convention. |
| basal-image | https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-46440/images/emd_46440.png; Complete PNG; visual inspection and byte hash | supports | Downloaded representative image visually matches the maintained PNG. Both SHA256 values are feb57c8110b7ff8737f5ac412c1712576437c5441e3097d0df8a8b0f42e4e910. It is an unlabeled density rendering without a scale bar, as captioned. |
| basal-li-fig4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11961760.1/44318_2025_392_Fig8_HTML.jpg; Entire primary figure | supports | The primary figure was visually inspected against its caption and target claims: core protein-model contacts, qualified possible contacts and the separate A-B versus B-C ladders. |
| basal-li-ev4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC11961760.1/44318_2025_392_Fig9_HTML.jpg; Entire primary figure | supports | The primary figure was visually inspected against its caption and target claims: core protein-model contacts, qualified possible contacts and the separate A-B versus B-C ladders. |
| basal-cai-fig4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f4.jpg; Entire primary figure | supports | The primary figure was visually inspected against its caption and target claims: core protein-model contacts, qualified possible contacts and the separate A-B versus B-C ladders. |
| record | data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml; Entire541-line target, seven components, five examples, five graph edges, three datasets, image and all discussions | context_only | The record carefully bounds structural fitting, sample/reference strains, mutant replacements and unresolved densities. Its protein-example roles nevertheless misdescribe ORF fields as primary gene names and leave symbol-to-accession support implicit. |
| local-id | data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml; Exact identifier; hidden/ignored-inclusive rg search across data/structures | context_only | Only the target file declares this local identifier. The maintained local namespace is not an external resolver accession. |
| schema-result | just validate data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/basal_body_a_b_inner_junction-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/basal_body_a_b_inner_junction-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch3-20261019-YKo4JU/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch3-20261019-YKo4JU/basal_body_a_b_inner_junction-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml; exact collect() scope | supports | 14 of20 collected target identifiers returned OK at the unchanged base. Residuals: EMDB:EMD-46437: SKIPPED; resolved by evidence basal-emdb46437; EMDB:EMD-46439: SKIPPED; resolved by evidence basal-emdb46439; EMDB:EMD-46440: SKIPPED; resolved by evidence basal-emdb46440; PMID:20008567: UNREACHABLE; resolved by evidence basal-epmc; PMID:39994484: UNREACHABLE; resolved by evidence basal-epmc; cellstructuremech:basal_body_a_b_inner_junction: SKIPPED; resolved by evidence local-id. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Model fitting supports the stated contacts but does not substitute for binding assays or temporal assembly experiments.
- Reference-strain sequences and axonemal models are not strain-matched basal-body experimental exemplars.
- The integrated-entry no-match result for I7LY02 and the659-result GO search are bounded to the inspected authority responses.
- The full density volumes were not downloaded; dataset identity, metadata, article interpretations and representative images were checked.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T040452Z-basal-body-a-b-inner-junction-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Basal-body A-B inner junction evidence and provenance review
started_at: '2026-10-20T04:00:43Z'
finished_at: '2026-10-20T04:04:52Z'
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
summary: The structural identity, seven bounded component classes, five contact edges,
  three reconstructions and hosted image are supported. One minor provenance finding
  affects the gene-field wording and symbol mappings of five protein examples.
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/images/cytoskeleton/basal_body_a_b_inner_junction/emd_46440.png
    sha256: feb57c8110b7ff8737f5ac412c1712576437c5441e3097d0df8a8b0f42e4e910
    role: context
  - path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    sha256: 6ca65191f50d079b7e7b0d807e6df7e2b1651eed1671d8a55029b7241bc80be4
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
- target_id: cellstructuremech:basal_body_a_b_inner_junction
  path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
  label: basal body A-B inner junction
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    role: maintained scientific record
scope:
  description: Entire record including all components/examples, graph, discussions,
    datasets and image; both structural papers and the original Poc1 localization
    source.
  selection: Tenth unreviewed path of batch3.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  command: just validate data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  command: just validate-strict data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/basal_body_a_b_inner_junction-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: 14 identifiers OK; 6 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - local-id
  - basal-emdb46440
  - basal-emdb46439
  - basal-epmc
  - basal-emdb46437
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: No expression-module or transcriptomic claim is asserted; the named-protein
    questions are assessed through UniProt, InterPro, structural archives and primary
    papers.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - basal-go
  - basal-go-search
  - basal-go-search-2
  - basal-go-search-3
  - basal-go-search-4
  - basal-go-search-5
  - basal-go-search-6
  - basal-go-search-7
  - outer-junction-taxa
  - basal-proteins
  - basal-li
  - basal-cai
  - basal-epmc
  - basal-poc1-paper
  - basal-pdb-mappings-valid
  - basal-pdb8g2z
  - basal-pdb9qzc8
  - basal-pdb9qzc
  - outer-junction-supplement
  - basal-IPR050505
  - basal-IPR020472
  - basal-IPR050630
  - basal-IPR052102
  - basal-IPR027012
  - basal-IPR028034
  - basal-IPR040673
  - basal-IPR033253
  - basal-IPR039986
  - basal-IPR056551
  - ladder-no-integrated-match
  - basal-emdb46437
  - basal-emdb46439
  - basal-emdb46440
  - basal-emdb46438
  - basal-policy
  - basal-image
  - basal-li-fig4
  - basal-li-ev4
  - basal-cai-fig4
  - record
  - local-id
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: basal-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140535,GO:0036064,GO:0160113
  locator: Three exact native terms
  accessed_at: '2026-10-20T04:01:03.550318Z'
  support: supports
  summary: The broad intracellular-complex parent and basal-body part are correct.
    GO0160113 specifically denotes the axonemal doublet junction and is not an exact
    identity for this basal-body structure.
  snapshot_sha256: ff1bf3e7d1d0d44fa46e41651fb0d225bf35375d06cbce944ec49e86868ba509
- evidence_id: basal-go-search
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&limit=100
  locator: Complete paginated search results
  accessed_at: '2026-10-20T04:01:48.284385Z'
  support: context_only
  summary: One page of the complete659-result search for basal body inner junction;
    all seven pages were inspected together. The only inner-junction-labelled result
    is the distinct axonemal term. This is bounded search evidence, not proof that
    no differently worded term could exist.
  snapshot_sha256: 524a3b542033681c08056b36f0f95525f40f765c1014d5db66969b5bb61d6867
- evidence_id: basal-go-search-2
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&limit=100&page=2
  locator: Complete paginated search results
  accessed_at: '2026-10-20T04:03:09.505036Z'
  support: context_only
  summary: One page of the complete659-result search for basal body inner junction;
    all seven pages were inspected together. The only inner-junction-labelled result
    is the distinct axonemal term. This is bounded search evidence, not proof that
    no differently worded term could exist.
  snapshot_sha256: 0dc671e267f897f0a18d0a632e6dc1d9638068ff7b3cfd9e4c59611a9cf293cd
- evidence_id: basal-go-search-3
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&limit=100&page=3
  locator: Complete paginated search results
  accessed_at: '2026-10-20T04:03:09.507664Z'
  support: context_only
  summary: One page of the complete659-result search for basal body inner junction;
    all seven pages were inspected together. The only inner-junction-labelled result
    is the distinct axonemal term. This is bounded search evidence, not proof that
    no differently worded term could exist.
  snapshot_sha256: 0370d3911dea71a60bed5ee501ad71405e4b66fef09100b9f695288a73b2286b
- evidence_id: basal-go-search-4
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&limit=100&page=4
  locator: Complete paginated search results
  accessed_at: '2026-10-20T04:03:09.624330Z'
  support: context_only
  summary: One page of the complete659-result search for basal body inner junction;
    all seven pages were inspected together. The only inner-junction-labelled result
    is the distinct axonemal term. This is bounded search evidence, not proof that
    no differently worded term could exist.
  snapshot_sha256: 81987832fd02ab6b539c86d148cd434309e68b863ba05241924494d36c6b4dc2
- evidence_id: basal-go-search-5
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&limit=100&page=5
  locator: Complete paginated search results
  accessed_at: '2026-10-20T04:03:09.508264Z'
  support: context_only
  summary: One page of the complete659-result search for basal body inner junction;
    all seven pages were inspected together. The only inner-junction-labelled result
    is the distinct axonemal term. This is bounded search evidence, not proof that
    no differently worded term could exist.
  snapshot_sha256: b0264f7d34c73add38bba77ad86d36c35624aae2edac12b943c16369710fe7d8
- evidence_id: basal-go-search-6
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&limit=100&page=6
  locator: Complete paginated search results
  accessed_at: '2026-10-20T04:03:10.751609Z'
  support: context_only
  summary: One page of the complete659-result search for basal body inner junction;
    all seven pages were inspected together. The only inner-junction-labelled result
    is the distinct axonemal term. This is bounded search evidence, not proof that
    no differently worded term could exist.
  snapshot_sha256: 4ccd756ba9baec883978c0b92e473f09550dafcbf76e8790ec3a88f8e79325d0
- evidence_id: basal-go-search-7
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=basal%20body%20inner%20junction&limit=100&page=7
  locator: Complete paginated search results
  accessed_at: '2026-10-20T04:03:10.648080Z'
  support: context_only
  summary: One page of the complete659-result search for basal body inner junction;
    all seven pages were inspected together. The only inner-junction-labelled result
    is the distinct axonemal term. This is bounded search evidence, not proof that
    no differently worded term could exist.
  snapshot_sha256: b339315dc02f8a91a4c738880f8b5159027878d939b17baf548f9f0cb1743c8e
- evidence_id: outer-junction-taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=5911,312017
  locator: Exact native taxonomic entries
  accessed_at: '2026-10-20T03:52:55.154591Z'
  support: supports
  summary: Species5911 and reference strain312017 match Tetrahymena thermophila and
    SB210.
  snapshot_sha256: fda62743792eecc892116e6d58703350304a02ea34bd536d666e735750142c2a
- evidence_id: basal-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=accession:Q229Z6%20OR%20accession:Q22ZH2%20OR%20accession:I7LU20%20OR%20accession:W7XCX2%20OR%20accession:W7XDG5%20OR%20accession:Q23EX8%20OR%20accession:I7M9T0%20OR%20accession:I7LY02%20OR%20accession:I7MJ23%20OR%20accession:Q24C92%20OR%20accession:I7MLQ3%20OR%20accession:Q22N53&format=json
  locator: Complete entries; genes, labels, statuses, organisms and InterPro references
  accessed_at: '2026-10-20T04:01:03.753057Z'
  support: context_only
  summary: Twelve named reference accessions resolve with the expected strain. The
    five example labels/statuses match, but all five genes fields contain only ORF
    names, not primary geneName values or the stated POC1/FAP symbols. Current InterPro
    cross-references support family/domain distinctions.
  snapshot_sha256: 94cf7783b68cce4d2db5f1af3ba8a5a505723d6f83bee53e8da1c6e2bed8a6ae
- evidence_id: basal-li
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11961760.1/PMC11961760.1.xml
  locator: Proximal/core and mutant Results; Figures2,4,EV4; Discussion and strain
    Methods
  accessed_at: '2026-10-20T04:01:03.411389Z'
  support: supports
  summary: Primary Results distinguish proximal/core composition, model-fitted MIPs,
    unresolved LRR identity and heterogeneous mutant replacements. The five core contact
    claims match the described fitted models; Methods identify B2086.
  snapshot_sha256: d1bfd06b3f2d20e19d7118186aee0d8333391748546a179f0694a9611c29bd61
- evidence_id: basal-cai
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/PMC12506977.1.xml
  locator: Junction Results, Figure4 and assignment/sample Methods
  accessed_at: '2026-10-20T04:01:04.096242Z'
  support: supports
  summary: The later study assigns the alpha-helical junction ladders to I7LY02 by
    predicted-model fitting. Figure4D-F places the second array at A-B; Methods identify
    SB715. The unassigned B-C WD40 ladder remains distinct.
  snapshot_sha256: ab8bf23b7821eaa514f3eebd1c4f281e1eb1c2af9ef4dc429aced2fe5dfcb04a
- evidence_id: basal-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1038/s44318-025-00392-6%20OR%20DOI:10.1126/sciadv.ady3689%20OR%20EXT_ID:20008567&format=json&resultType=core
  locator: Complete three-result bibliographic joins
  accessed_at: '2026-10-20T04:01:03.594222Z'
  support: supports
  summary: Both structural DOIs and the two cited PMIDs match exact titles and PMC
    identities.
  snapshot_sha256: 20208f5249e6f4ec1ec9f51c8e8ee7844c4b2541d27c7492dd7ea833b8afba11
- evidence_id: basal-poc1-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2806327.1/PMC2806327.1.xml
  locator: Results on GFP constructs and basal-body localization; FigureS2 discussion
  accessed_at: '2026-10-20T04:03:32.503253Z'
  support: supports
  summary: Full-length Poc1 and its WD40 region localize to basal bodies in the original
    study, consistent with the selected UniProt localization provenance.
  snapshot_sha256: f4c5df75072c24ca64f8b73b93f84cb7b3bead5b31ef02eedaf3f320f0c0ad0a
- evidence_id: basal-pdb-mappings-valid
  kind: authority
  reference: https://data.rcsb.org/graphql?query=%7Bentry%28entry_id%3A%228G2Z%22%29%7Bpolymer_entities%7Brcsb_id%20rcsb_polymer_entity%7Bpdbx_description%7D%20rcsb_polymer_entity_container_identifiers%7Breference_sequence_identifiers%7Bdatabase_accession%20database_name%7D%7D%7D%7D%7D
  locator: Complete polymer-entity descriptions and UniProt mappings
  accessed_at: '2026-10-20T04:02:18.707787Z'
  support: supports
  summary: RCSB8G2Z maps CFAP52A to Q22ZH2, IJ34 to I7M9T0, CFAP45 to W7XCX2 and CFAP210
    to Q23EX8. These corroborate the model identifiers, not the identity of every
    optional paralog exemplar.
  snapshot_sha256: 94d69224ed6dd75475870ac546a3b30cb36b36c6e9250549a99f7115db9dc762
- evidence_id: basal-pdb8g2z
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/entry/8G2Z
  locator: Entry title and primary citation
  accessed_at: '2026-10-20T04:01:04.490781Z'
  support: supports
  summary: The source model is a48-nm axonemal doublet from CU428; it is not a B2086
    basal-body deposition.
  snapshot_sha256: a420f94d0862b01c5353cd7612f4eba1502408999946cfbbdb5833ea2f6c2c71
- evidence_id: basal-pdb9qzc8
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/9QZC/8
  locator: Exact entity mapping
  accessed_at: '2026-10-20T04:01:04.567570Z'
  support: supports
  summary: Entity8 maps to I7LY02, supporting the ladder model’s sequence identity.
  snapshot_sha256: be57ff9ae430382d536725916de77efb95bc96f36666065dfc1716c06d2a25aa
- evidence_id: basal-pdb9qzc
  kind: authority
  reference: https://data.rcsb.org/rest/v1/core/entry/9QZC
  locator: Entry title and citation
  accessed_at: '2026-10-20T04:03:32.036521Z'
  support: supports
  summary: 9QZC is a proximal A-C-linker repeating-unit deposition with the Cai2025
    citation, not an A-B-specific deposition.
  snapshot_sha256: fa18389adfa6aca86365858ae57403936e2d6bb8846950c1756e9c5ea85a3848
- evidence_id: outer-junction-supplement
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10105768.1/41467_2023_37868_MOESM1_ESM.pdf
  locator: Supplementary Tables3-4; relevant rows
  accessed_at: '2026-10-20T03:53:46.492420Z'
  support: supports
  summary: Table3 names CFAP106B as I7LU20 and CFAP210 as Q23EX8. Table4 lists W7XDG5
    as a related hit rather than the named CFAP210 structural model. This supplies
    missing distinctions between identity exemplars and exact model accessions.
  snapshot_sha256: 98c44ea5e4b6bf75d99eec076e2c271bf41e79b2cafbe8f2ef3abe084fdca47a
- evidence_id: basal-IPR050505
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050505
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:05.136709Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: a441faeaa7da8487b8e14015dcc322403b37d7620dc71a539ed189b411dac195
- evidence_id: basal-IPR020472
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020472
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:05.207719Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: f5ceeddc437713cad39c49c699d92bf1b9a5bb9ef18d46e036338a736f24f673
- evidence_id: basal-IPR050630
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050630
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:05.725864Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: c340a2dde37597d177286269701e7b8257cfa2d04b158253513a82c15869970e
- evidence_id: basal-IPR052102
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052102
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:05.806162Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: cb172b48aa0c8dd9b3db6635fa3c121d6fe03b7067d3f9f5f6ba721a317eaadb
- evidence_id: basal-IPR027012
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR027012
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:05.831855Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: 8385ecd42152f23d8d6b8ae56293e8caf5993e2337a3ed88566c40ff50fc0ad3
- evidence_id: basal-IPR028034
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028034
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:06.046559Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: 727dcc002ad5162850b6b298bc64dc505bfcb75fe728087ca82401d64873f4bc
- evidence_id: basal-IPR040673
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040673
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:06.370591Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: 3c70bc123c7054b5994f01ebf97c07e3580fde931eca6699948121482195d7a6
- evidence_id: basal-IPR033253
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033253
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:06.432616Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: 1dea4956c8caeb8c8e36db8bec71eadb3098ae55790cc684741d184fc280da7c
- evidence_id: basal-IPR039986
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039986
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:06.444700Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: 6b3c7dac159b7df69e6414b69fab07e599b3d68e501a60c3a6948cdc310f370c
- evidence_id: basal-IPR056551
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056551
  locator: Entry metadata and description
  accessed_at: '2026-10-20T04:01:47.989671Z'
  support: supports
  summary: Native entry type/name and definition inspected. IPR033253 and IPR039986
    are exact CFAP45/210 families; the other cited entries are broader groups or domains/repeats.
    Newly present IPR056551 is a domain, not a POC1 family resolution.
  snapshot_sha256: 0d4fad01d608cfc20b180d46f26792250befd95a1930d7615e3a832db3169936
- evidence_id: ladder-no-integrated-match
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/I7LY02/
  locator: Integrated InterPro entries for UniProtI7LY02
  accessed_at: '2026-10-20T04:01:48.149997Z'
  support: context_only
  summary: The native integrated-entry endpoint returned HTTP204; UniProt also lists
    no InterPro/Pfam cross-reference. This bounded negative result does not imply
    absence of the protein or structure.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: basal-emdb46437
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-46437
  locator: Admin, natural source and primary citation
  accessed_at: '2026-10-20T04:01:04.314875Z'
  support: supports
  summary: Native released entry, title, source taxon5911, depositor authors and exact
    DOI/PMID citation inspected. The three A-B entries match their region/repeat labels;
    the excluded46438 entry is proximal B-C, confirming the stated article/archive
    discrepancy.
  snapshot_sha256: 71b1e6a6589a13d592916791e4975de8913434595fdcb461cf54307d1f363c09
- evidence_id: basal-emdb46439
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-46439
  locator: Admin, natural source and primary citation
  accessed_at: '2026-10-20T04:01:04.395099Z'
  support: supports
  summary: Native released entry, title, source taxon5911, depositor authors and exact
    DOI/PMID citation inspected. The three A-B entries match their region/repeat labels;
    the excluded46438 entry is proximal B-C, confirming the stated article/archive
    discrepancy.
  snapshot_sha256: 266066856d4c22ad730a5b21441f7fb30bba0534064217e77b0d3a1616f5450c
- evidence_id: basal-emdb46440
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-46440
  locator: Admin, natural source and primary citation
  accessed_at: '2026-10-20T04:01:04.508158Z'
  support: supports
  summary: Native released entry, title, source taxon5911, depositor authors and exact
    DOI/PMID citation inspected. The three A-B entries match their region/repeat labels;
    the excluded46438 entry is proximal B-C, confirming the stated article/archive
    discrepancy.
  snapshot_sha256: cf97761d8a259cc9cfb87fd6a5d2c5326c340b3b38a608ff20de818dad39f87d
- evidence_id: basal-emdb46438
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/api/entry/EMD-46438
  locator: Admin, natural source and primary citation
  accessed_at: '2026-10-20T04:01:48.162691Z'
  support: supports
  summary: Native released entry, title, source taxon5911, depositor authors and exact
    DOI/PMID citation inspected. The three A-B entries match their region/repeat labels;
    the excluded46438 entry is proximal B-C, confirming the stated article/archive
    discrepancy.
  snapshot_sha256: 11925ad540168876c8c998de753acdaab8447261fec3d279d7f0b0e6bb6a0dae
- evidence_id: basal-policy
  kind: authority
  reference: https://www.ebi.ac.uk/emdb/policies.html
  locator: Section3.1.2
  accessed_at: '2026-10-20T04:01:05.425069Z'
  support: supports
  summary: EMDB policy3.1.2 requires representative figures without copyright restrictions,
    consistent with the record’s declared licence convention.
  snapshot_sha256: 20723befa3d18968826e22b70ae9c6679c4b41cdf6bb08b6001f0b412c281a00
- evidence_id: basal-image
  kind: authority
  reference: https://ftp.ebi.ac.uk/pub/databases/emdb/structures/EMD-46440/images/emd_46440.png
  locator: Complete PNG; visual inspection and byte hash
  accessed_at: '2026-10-20T04:01:05.103237Z'
  support: supports
  summary: Downloaded representative image visually matches the maintained PNG. Both
    SHA256 values are feb57c8110b7ff8737f5ac412c1712576437c5441e3097d0df8a8b0f42e4e910.
    It is an unlabeled density rendering without a scale bar, as captioned.
  snapshot_sha256: feb57c8110b7ff8737f5ac412c1712576437c5441e3097d0df8a8b0f42e4e910
- evidence_id: basal-li-fig4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11961760.1/44318_2025_392_Fig8_HTML.jpg
  locator: Entire primary figure
  accessed_at: '2026-10-20T04:02:19.198799Z'
  support: supports
  summary: 'The primary figure was visually inspected against its caption and target
    claims: core protein-model contacts, qualified possible contacts and the separate
    A-B versus B-C ladders.'
  snapshot_sha256: dd9ff5965867a4c6472fc2e9b35013409f26b8ee433a1c84365b533923e6fc63
- evidence_id: basal-li-ev4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC11961760.1/44318_2025_392_Fig9_HTML.jpg
  locator: Entire primary figure
  accessed_at: '2026-10-20T04:02:19.154309Z'
  support: supports
  summary: 'The primary figure was visually inspected against its caption and target
    claims: core protein-model contacts, qualified possible contacts and the separate
    A-B versus B-C ladders.'
  snapshot_sha256: 727e12e18795207632501dc119de4c12471621bd88b97b86ceffe0024497091b
- evidence_id: basal-cai-fig4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12506977.1/sciadv.ady3689-f4.jpg
  locator: Entire primary figure
  accessed_at: '2026-10-20T04:02:19.314075Z'
  support: supports
  summary: 'The primary figure was visually inspected against its caption and target
    claims: core protein-model contacts, qualified possible contacts and the separate
    A-B versus B-C ladders.'
  snapshot_sha256: 1db3325f905ae3d30234a23b6184ebfac416f2b1fd56a63ca9e84c63c1094fd7
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
  locator: Entire541-line target, seven components, five examples, five graph edges,
    three datasets, image and all discussions
  accessed_at: '2026-10-20T04:04:52Z'
  support: context_only
  summary: The record carefully bounds structural fitting, sample/reference strains,
    mutant replacements and unresolved densities. Its protein-example roles nevertheless
    misdescribe ORF fields as primary gene names and leave symbol-to-accession support
    implicit.
- evidence_id: local-id
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
  locator: Exact identifier; hidden/ignored-inclusive rg search across data/structures
  accessed_at: '2026-10-20T04:04:52Z'
  support: context_only
  summary: Only the target file declares this local identifier. The maintained local
    namespace is not an external resolver accession.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T04:00:45Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml'
  snapshot_sha256: 7400877b363e35a258075edba4202520a252f9a22a4b4d218721d22594920cca
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/basal_body_a_b_inner_junction-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T04:00:46Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml\
    \ --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/basal_body_a_b_inner_junction-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch3-20261019-YKo4JU/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch3-20261019-YKo4JU/basal_body_a_b_inner_junction-strict.tsv"
  snapshot_sha256: 9fdee7970f6a71f578db6ea5e81539458b04865cda6fe909f77f70915c4a0020
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml; exact
    collect() scope
  accessed_at: '2026-10-20T04:04:52Z'
  support: supports
  summary: '14 of20 collected target identifiers returned OK at the unchanged base.
    Residuals: EMDB:EMD-46437: SKIPPED; resolved by evidence basal-emdb46437; EMDB:EMD-46439:
    SKIPPED; resolved by evidence basal-emdb46439; EMDB:EMD-46440: SKIPPED; resolved
    by evidence basal-emdb46440; PMID:20008567: UNREACHABLE; resolved by evidence
    basal-epmc; PMID:39994484: UNREACHABLE; resolved by evidence basal-epmc; cellstructuremech:basal_body_a_b_inner_junction:
    SKIPPED; resolved by evidence local-id. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: Basal-body junction versus axonemal junction
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: The maintained identity denotes a multiprotein basal-body interface supported
    by two structural studies. The broad parent and basal-body parthood are valid;
    the axonemal junction remains distinct.
  evidence_ids:
  - basal-go
  - basal-li
  - basal-cai
  - record
  - basal-go-search
  - basal-go-search-2
  - basal-go-search-3
  - basal-go-search-4
  - basal-go-search-5
  - basal-go-search-6
  - basal-go-search-7
- assessment_id: composition
  area: evidence
  topic: Region-specific structural assignments
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: The seven component classes are supported at their stated evidence level.
    Proximal FAP52-like identity, core LRR candidate and scaffold stem remain unresolved;
    neither mutant replacement proteins nor generic tubulin substrates are incorrectly
    added as ordinary components.
  evidence_ids:
  - basal-li
  - basal-cai
  - basal-pdb-mappings-valid
  - basal-pdb9qzc8
  - record
- assessment_id: grounding
  area: grounding
  topic: Exact families versus domains
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: The two family groundings are exact. The remaining label-only treatment
    is justified; the additional current POC1 domain does not resolve family identity.
    The ladder’s bounded no-match claim is reproducible.
  evidence_ids:
  - basal-IPR050505
  - basal-IPR020472
  - basal-IPR050630
  - basal-IPR052102
  - basal-IPR027012
  - basal-IPR028034
  - basal-IPR040673
  - basal-IPR033253
  - basal-IPR039986
  - basal-IPR056551
  - ladder-no-integrated-match
  - basal-proteins
  - record
- assessment_id: examples
  area: provenance
  topic: Named symbols and reference loci
  outcome: concern
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: All five entries resolve and their labels/statuses match, but their ORF
    fields are called primary gene names and independent symbol mappings are omitted.
    FAP106B and the family-related W7XDG5 exemplar must remain distinct from the fitted
    model identities.
  evidence_ids:
  - basal-proteins
  - basal-pdb-mappings-valid
  - outer-junction-supplement
  - record
- assessment_id: scope
  area: scope
  topic: Strain and experiment boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: Species-level canonical scope is supported. B2086 basal bodies, SB715 ladder
    study, SB210 sequences and CU428 axonemal models remain explicitly separated.
    No broad prevalence or uniform knockout failure is asserted.
  evidence_ids:
  - outer-junction-taxa
  - basal-li
  - basal-cai
  - basal-proteins
  - basal-pdb8g2z
  - record
- assessment_id: function
  area: evidence
  topic: Luminal connection and scaffold attachment
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: Source structures support connection and attachment roles without establishing
    a unique force threshold, junction-specific pleiotropic phenotype or temporal
    assembly sequence.
  evidence_ids:
  - basal-li
  - record
- assessment_id: graph
  area: graph
  topic: Five model-derived contacts
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: Poc1 contacts A1/B10; FAP52 contacts B9/B10; IJ34 anchors to A-tubule and
    tethers FAP52 through its C-terminal helix. The MECHANISTIC contact-network scope
    explicitly states fitted-model evidence and does not convert possible FAP106/FAP210
    contacts into measured binding edges.
  evidence_ids:
  - basal-li
  - basal-li-fig4
  - basal-li-ev4
  - record
- assessment_id: data
  area: provenance
  topic: Three released reconstructions and excluded conflicting label
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: Region, repeat, source organism and citation joins match the three native
    A-B deposits. The B-C title conflict is preserved outside the linked dataset list.
  evidence_ids:
  - basal-emdb46437
  - basal-emdb46439
  - basal-emdb46440
  - basal-emdb46438
  - basal-li
  - record
- assessment_id: image
  area: evidence
  topic: Representative image provenance
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: The hosted density rendering, exact byte hash, source, caption and stated
    copyright convention are supported. The article figures were inspected separately
    and are not copied into the corpus.
  evidence_ids:
  - basal-image
  - basal-policy
  - basal-emdb46440
  - record
- assessment_id: status
  area: completeness
  topic: Open scientific uncertainties
  outcome: supported
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  summary: The later ladder identification is integrated without claiming unique perturbation
    proof. Remaining uncertainties are scientifically bounded rather than silently
    promoted; PROPOSED status is appropriate.
  evidence_ids:
  - basal-li
  - basal-cai
  - basal-pdb9qzc8
  - record
findings:
- finding_id: F1
  issue_key: basal-body-a-b-inner-junction-example-symbol-provenance
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Protein examples misattribute symbol mappings and ORF names to UniProt primary
    names
  description: 'All five example roles call the TTHERM identifiers primary names,
    but native UniProt supplies only orfNames. UniProt does not explicitly map the
    stated POC1/FAP symbols in its gene fields. Cite the independent mapping sources
    and distinguish family/paralog representatives from fitted proteins: I7LU20 is
    CFAP106B in the2023 supplement, and W7XDG5 is a related CFAP210-family hit rather
    than the Q23EX8 model used by8G2Z. This is a bounded provenance defect, not evidence
    that all selected accession families are wrong.'
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  field_paths:
  - components[component_id=poc1].protein_examples
  - components[component_id=fap52].protein_examples
  - components[component_id=fap106].protein_examples
  - components[component_id=fap45].protein_examples
  - components[component_id=fap210].protein_examples
  evidence_ids:
  - basal-proteins
  - basal-pdb-mappings-valid
  - outer-junction-supplement
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    role: maintained scientific record
  rule_id: review-checklist:Evidence standard and Components
  native_severity: minor
  normalization_reason: Core membership and reference-strain separation are supported;
    the defect is inaccurate gene-field terminology and omitted identity-mapping provenance
    in restricted exemplars.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:basal_body_a_b_inner_junction
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    role: maintained scientific record
  description: Describe TTHERM identifiers as ORF/locus names. Attach explicit symbol-to-accession
    mappings and qualify paralog/family exemplars; retain separation from the fitted
    experimental protein identities.
  acceptance_checks:
  - Each symbol mapping cites a source that actually states it or is explicitly qualified
    as a family/paralog representative.
  - I7LU20 is not silently equated to the modeled CFAP106A; W7XDG5 is not equated
    to the Q23EX8 CFAP210 model.
  - Preserve all strain, model-fitting and mutant limitations.
  - After separately authorized curation, run native record, history and generated-page
    checks.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- Model fitting supports the stated contacts but does not substitute for binding assays
  or temporal assembly experiments.
- Reference-strain sequences and axonemal models are not strain-matched basal-body
  experimental exemplars.
- The integrated-entry no-match result for I7LY02 and the659-result GO search are
  bounded to the inspected authority responses.
- The full density volumes were not downloaded; dataset identity, metadata, article
  interpretations and representative images were checked.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
