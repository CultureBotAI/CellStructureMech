# Nitrate-inducible formate dehydrogenase identity and source assembly review

- Review: 20261021T090554Z-formate-dehydrogenase-n-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:41:45Z
- Finished UTC: 2026-10-21T09:05:54Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact FDH-N identity, FdnGHI protein examples, scoped nonameric source composition and bounded function graph are supported. Narrow family mappings remain unresolved for defensible scope reasons; no concrete curation issue was established.

## Scope And Provenance

Entire single target, all native identities/imported counts and component families; claim-bearing primary structural body and precise graph/organism/inference boundaries.

Selection: Eighth selected target in batch thirteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:formate_dehydrogenase_n_complex | data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml | maintained | formate dehydrogenase N complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | 13 identifiers OK; 5 transport/skipped residuals independently resolved. |
| Native UniProt verify | passed | False | cellstructuremech:formate_dehydrogenase_n_complex | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | cellstructuremech:formate_dehydrogenase_n_complex | Native command passed; scientific membership and graph scope assessed independently. |
| Claim-level scientific review | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:formate_dehydrogenase_n_complex | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Nitrate-inducible complex and broader parents

identity: supported. Targets: cellstructuremech:formate_dehydrogenase_n_complex.

The local identifier consistently denotes FDH-N/FdnGHI. Parent classes are broader is-a categories; they do not equate N, O and H isozymes. Synonym scopes, category and kind agree with native CPX.

### Three subunit types and exact examples

evidence: supported. Targets: cellstructuremech:formate_dehydrogenase_n_complex.

Native CPX, PDB entities and reviewed UniProt agree on FdnG catalytic alpha, FdnH Fe-S relay and FdnI membrane cytochrome. All gene/taxon/accession pairs are exact. Constituent membership does not by itself establish the separate assembly-necessity assertion carried by ESSENTIAL.

### Fdn-specific family scope

grounding: supported. Targets: cellstructuremech:formate_dehydrogenase_n_complex.

The inspected matching whole-family candidates extend into Fdo or other related oxidoreductases; generic cofactor domains are also broader. IPR006443 title alone is misleadingly narrow relative to its definition. The existing label-only rows and bounded family TODO are justified without asserting that no exact family could exist anywhere.

### Source-specific nonamer and cofactor rows

scope: supported. Targets: cellstructuremech:formate_dehydrogenase_n_complex.

The3:3:3 protein assembly agrees between CPX1975 and both PDB biological assemblies. Imported chemical counts and names reproduce CPX; the lone menaquinone participant is not interpreted as proof that the entire physiological trimer has only one potential substrate site. No universal bacterial stoichiometry is inferred.

### K-12 versus species-level deposit metadata

scope: supported. Targets: cellstructuremech:formate_dehydrogenase_n_complex.

CPX and reviewed entries support K-12; original PDB entity source annotations are species562. These compatible levels are retained separately. No direct assignment of every historical preparation to a particular K-12 substrain or all-species prevalence is made.

### Whole-complex reaction and constituent edges

graph: supported. Targets: cellstructuremech:formate_dehydrogenase_n_complex.

All component_ref links and redox substrate/product edges match native function and complex records. The graph explicitly omits individual cofactor steps and does not promote the paper’s coupled redox-loop interpretation into autonomous proton pumping.

### Useful unresolved family question

completeness: supported. Targets: cellstructuremech:formate_dehydrogenase_n_complex.

Identity, membership, source assembly and function are adequately represented. Optional images, chemical rows outside the scoped import, explicit per-cofactor mechanisms and additional examples are not required. No concrete curation defect was established.

### Assembly necessity versus constituent membership

evidence: unknown. Targets: cellstructuremech:formate_dehydrogenase_n_complex.

The schema defines essentiality by whether the structure forms without the component. The inspected sources establish constituent membership and functions, but those observations alone do not establish this assembly-necessity assertion. No subunit-deletion/assembly experiment was independently checked here; catalytic necessity, organismal viability and intact structural membership are distinct questions.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; docs/CURATION.md and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| fdn-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009326,GO:0036397,GO:0098803; All three complete active term results and synonym scopes | supports | GO0009326 is the broader formate dehydrogenase complex, GO0098803 is respiratory-chain complex, and GO0036397 specifically defines formate plus quinone yielding CO2 plus quinol. These parents/function do not equate FDH-N with FDH-O or FDH-H. |
| fdn-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Native taxon names, rank and lineage | supports | Taxon83333 is the E.coli K-12 strain. |
| fdn-agent-CPX-1975 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1975; Complete name/synonyms, organism, properties, participants, evidence and cited references | supports | Native CPX1975 names the K-12 FdnGHI heterononamer, including the maintained synonym variants. All seven imported participant rows, EBI identifiers, source_names and counts match: three each protein/Mo-bisMGD, six hemes, fifteenFe-S clusters and one menaquinone source participant. |
| fdn-agent-P24183 | https://rest.uniprot.org/uniprotkb/P24183.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P24183 identifies Formate dehydrogenase, nitrate-inducible, major subunit, gene fdnG, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| fdn-agent-query-fdnG | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AfdnG%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene fdnG, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P24183. This checks identifier resolution only. |
| fdn-agent-P0AAJ3 | https://rest.uniprot.org/uniprotkb/P0AAJ3.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0AAJ3 identifies Formate dehydrogenase, nitrate-inducible, iron-sulfur subunit, gene fdnH, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| fdn-agent-query-fdnH | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AfdnH%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene fdnH, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0AAJ3. This checks identifier resolution only. |
| fdn-agent-P0AEK7 | https://rest.uniprot.org/uniprotkb/P0AEK7.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0AEK7 identifies Formate dehydrogenase, nitrate-inducible, cytochrome b556(Fdn) subunit, gene fdnI, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| fdn-agent-query-fdnI | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AfdnI%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene fdnI, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0AEK7. This checks identifier resolution only. |
| fdn-agent-IPR006443 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006443/; Full family metadata/type/description, not only name or a matching domain | supports | Although named Formate dehydrogenase-N alpha, the native description explicitly includes both fdn and fdo genes; its scope is not exclusive to nitrate-inducible FdnG. |
| fdn-agent-IPR006470 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006470/; Full family metadata/type/description, not only name or a matching domain | supports | Proteobacterial formate-dehydrogenase Fe-S family is broader than a verified nitrate-specific FdnH class. |
| fdn-agent-IPR014603 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014603/; Full family metadata/type/description, not only name or a matching domain | supports | General formate-dehydrogenase Fe-S family does not establish nitrate-specific identity. |
| fdn-agent-IPR051555 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051555/; Full family metadata/type/description, not only name or a matching domain | supports | Formate-dehydrogenase Fe-S family includes aerobic and anaerobic enzymes. |
| fdn-agent-IPR006471 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006471/; Full family metadata/type/description, not only name or a matching domain | supports | Gamma-subunit family description includes homologous hydrogenase/thiosulfate-reductase membrane cytochromes. |
| fdn-agent-IPR051817 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051817/; Full family metadata/type/description, not only name or a matching domain | supports | Formate-dehydrogenase cytochrome-b556 family spans aerobic and anaerobic forms. |
| fdn-agent-pdb-1KQF | https://data.rcsb.org/rest/v1/core/entry/1KQF; rcsb_id, struct title, exptl, citation and entry identifiers | supports | 1KQF native entry identifies the Jormakka2002 crystallographic FDH-N deposition and exact primary DOI/PMID. |
| fdn-agent-assembly-1KQF | https://data.rcsb.org/rest/v1/core/assembly/1KQF/1; rcsb_assembly_info, pdbx_struct_assembly and pdbx_struct_assembly_gen | supports | Assembly1 of1KQF is author/software-defined nonameric: three protein entities, nine protein instances and three symmetry operations. |
| fdn-agent-1KQF-entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1KQF/1; Polymer entity description, source organism and SIFTS/UniProt identifiers | supports | 1KQF entity1 maps toP24183; native source organism is E.coli562. K-12 precision comes independently from CPX/UniProt. |
| fdn-agent-1KQF-entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/1KQF/2; Polymer entity description, source organism and SIFTS/UniProt identifiers | supports | 1KQF entity2 maps toP0AAJ3; native source organism is E.coli562. K-12 precision comes independently from CPX/UniProt. |
| fdn-agent-1KQF-entity-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/1KQF/3; Polymer entity description, source organism and SIFTS/UniProt identifiers | supports | 1KQF entity3 maps toP0AEK7; native source organism is E.coli562. K-12 precision comes independently from CPX/UniProt. |
| fdn-agent-pdb-1KQG | https://data.rcsb.org/rest/v1/core/entry/1KQG; rcsb_id, struct title, exptl, citation and entry identifiers | supports | 1KQG native entry identifies the Jormakka2002 crystallographic FDH-N deposition and exact primary DOI/PMID. |
| fdn-agent-assembly-1KQG | https://data.rcsb.org/rest/v1/core/assembly/1KQG/1; rcsb_assembly_info, pdbx_struct_assembly and pdbx_struct_assembly_gen | supports | Assembly1 of1KQG is author/software-defined nonameric: three protein entities, nine protein instances and three symmetry operations. |
| fdn-agent-1KQG-entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1KQG/1; Polymer entity description, source organism and SIFTS/UniProt identifiers | supports | 1KQG entity1 maps toP24183; native source organism is E.coli562. K-12 precision comes independently from CPX/UniProt. |
| fdn-agent-1KQG-entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/1KQG/2; Polymer entity description, source organism and SIFTS/UniProt identifiers | supports | 1KQG entity2 maps toP0AAJ3; native source organism is E.coli562. K-12 precision comes independently from CPX/UniProt. |
| fdn-agent-1KQG-entity-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/1KQG/3; Polymer entity description, source organism and SIFTS/UniProt identifiers | supports | 1KQG entity3 maps toP0AEK7; native source organism is E.coli562. K-12 precision comes independently from CPX/UniProt. |
| fdn-agent-chebi-60539 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/60539/; Accession/name/definition and source synonyms | supports | Native chemical identity agrees with the source import; chemical identity does not prove physiological copy number or complete occupancy. |
| fdn-agent-chebi-16374 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/16374/; Accession/name/definition and source synonyms | supports | Native chemical identity agrees with the source import; chemical identity does not prove physiological copy number or complete occupancy. |
| fdn-agent-chebi-30413 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/30413/; Accession/name/definition and source synonyms | supports | Native chemical identity agrees with the source import; chemical identity does not prove physiological copy number or complete occupancy. |
| fdn-agent-chebi-33725 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/33725/; Accession/name/definition and source synonyms | supports | Native chemical identity agrees with the source import; chemical identity does not prove physiological copy number or complete occupancy. |
| fdn-agent-eco-0000353 | https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms?obo_id=ECO:0000353; Exact term id/label/definition | supports | ECO0000353 is physical interaction evidence used in manual assertion. |
| fdn-agent-jormakka2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.1068186; Exact bibliographic fields and abstract | supports | Jormakka, Törnroth, Byrne and Iwata2002, Molecular basis of proton motive force generation: structure of formate dehydrogenase-N, has PMID11884747 and DOI10.1126/science.1068186. |
| fdn-agent-jormakka2002-browser | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; Author-uploaded primary article displayed through browser: Introduction and overall-structure text, printed pp1863–1864. Original combined capture also contains unrelated Caltech metadata, which is not used here. | supports | Primary crystallography supports a trimer of FdnGHI heterotrimers and the physiological electron-donor/acceptor assignment. |
| fdn-agent-jormakka2002-browser2 | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; Primary pp1863–1866: overall structure, Electron transfer, alpha, beta and gamma sections and captions; browser display, no HTTP200 inferred. | supports | The alpha/beta/gamma architecture and cofactor relay agree with the component roles. Native coordinates and reviewed database entries independently corroborate membership. |
| fdn-agent-jormakka2002-browser3 | https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N; Primary pp1865–1868: beta/gamma continuation, Quinone reduction mechanism, Table1 and concluding PMF section; no supplementary Methods or coordinate reanalysis. | supports | Quinone-site chemistry is proposed from an inhibitor-bound structure; the concluding proton-motive-force account is a coupled FDH-N/Nar redox loop, not an autonomous proton pump. |
| schema-result | just validate data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml |
| strict-result | just validate-strict data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/formate_dehydrogenase_n_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/formate_dehydrogenase_n_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/formate_dehydrogenase_n_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 13 of18 collected target identifiers returned OK at the unchanged base. Residuals: ECO:0000353: SKIPPED; resolved by evidence fdn-agent-eco-0000353; PDB:1KQF: SKIPPED; resolved by evidence fdn-agent-pdb-1KQF; PDB:1KQG: SKIPPED; resolved by evidence fdn-agent-pdb-1KQG; PMID:11884747: UNREACHABLE; resolved by evidence fdn-agent-jormakka2002-meta; cellstructuremech:formate_dehydrogenase_n_complex: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| native-verify | /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml  (cellstructuremech:formate_dehydrogenase_n_complex)<br>  formate_dehydrogenase_n_quinone_reduction	fdng	COVERED	-&gt;fdng_alpha_subunit (UniProtKB:P24183)<br>  formate_dehydrogenase_n_quinone_reduction	fdnh	COVERED	-&gt;fdnh_iron_sulfur_subunit (UniProtKB:P0AAJ3)<br>  formate_dehydrogenase_n_quinone_reduction	fdni	COVERED	-&gt;fdni_cytochrome_b_subunit (UniProtKB:P0AEK7)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Full primary body passages were readable through the browser’s author-uploaded text. Native ResearchGate and Colorado-index routes returned403; browser captures are hashed with actual access times and no invented HTTP status. Supplementary crystallization Methods, figure pixels and raw coordinates were not reanalyzed.
- The biological trimer is supported by structural packing/interface evidence and native assembly annotation; this is not an independent in-cell stoichiometric census. CPX chemical occupancy remains explicitly source-scoped.
- Family assessment is bounded to complete native integrated matches on the three exact reviewed examples and the six inspected candidate family definitions; no exhaustive all-database absence claim is made.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The schema defines essentiality by whether the structure forms without the component. The inspected sources establish constituent membership and functions, but those observations alone do not establish this assembly-necessity assertion. No subunit-deletion/assembly experiment was independently checked here; catalytic necessity, organismal viability and intact structural membership are distinct questions.
- All13 native inspection inputs and all source raw/meta hashes verified after fresh focused gates0. No record changes, finalization or status promotion.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T090554Z-formate-dehydrogenase-n-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Nitrate-inducible formate dehydrogenase identity and source assembly review
started_at: '2026-10-21T08:41:45Z'
finished_at: '2026-10-21T09:05:54Z'
reviewer:
  identity: Codex
  kind: agent
  independence: unknown
  independence_basis: Current source review does not establish independent historical
    authorship.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact FDH-N identity, FdnGHI protein examples, scoped nonameric source composition
  and bounded function graph are supported. Narrow family mappings remain unresolved
  for defensible scope reasons; no concrete curation issue was established.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    sha256: ef7276f6532db0b7be7eac0564d02687a9661839dd9181aa89374ff24a6afe62
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
- target_id: cellstructuremech:formate_dehydrogenase_n_complex
  path: data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
  label: formate dehydrogenase N complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    role: maintained scientific record
scope:
  description: Entire single target, all native identities/imported counts and component
    families; claim-bearing primary structural body and precise graph/organism/inference
    boundaries.
  selection: Eighth selected target in batch thirteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: just validate data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: just validate-strict data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/formate_dehydrogenase_n_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: 13 identifiers OK; 5 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - fdn-agent-eco-0000353
  - fdn-agent-pdb-1KQF
  - fdn-agent-pdb-1KQG
  - fdn-agent-jormakka2002-meta
  - record
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    --verify
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: false
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native command passed; scientific membership and graph scope assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - fdn-agent-go
  - fdn-agent-tax-83333
  - fdn-agent-CPX-1975
  - fdn-agent-P24183
  - fdn-agent-query-fdnG
  - fdn-agent-P0AAJ3
  - fdn-agent-query-fdnH
  - fdn-agent-P0AEK7
  - fdn-agent-query-fdnI
  - fdn-agent-IPR006443
  - fdn-agent-IPR006470
  - fdn-agent-IPR014603
  - fdn-agent-IPR051555
  - fdn-agent-IPR006471
  - fdn-agent-IPR051817
  - fdn-agent-pdb-1KQF
  - fdn-agent-assembly-1KQF
  - fdn-agent-1KQF-entity-1
  - fdn-agent-1KQF-entity-2
  - fdn-agent-1KQF-entity-3
  - fdn-agent-pdb-1KQG
  - fdn-agent-assembly-1KQG
  - fdn-agent-1KQG-entity-1
  - fdn-agent-1KQG-entity-2
  - fdn-agent-1KQG-entity-3
  - fdn-agent-chebi-60539
  - fdn-agent-chebi-16374
  - fdn-agent-chebi-30413
  - fdn-agent-chebi-33725
  - fdn-agent-eco-0000353
  - fdn-agent-jormakka2002-meta
  - fdn-agent-jormakka2002-browser
  - fdn-agent-jormakka2002-browser2
  - fdn-agent-jormakka2002-browser3
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T08:55:02Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; docs/CURATION.md and review checklist
  accessed_at: '2026-10-21T08:55:02Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Optional fields are not mandatory. CausalNode
    permits protein complexes; its xrefs contract does not inherit the top-level record
    equivalence restriction.
- evidence_id: fdn-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009326,GO:0036397,GO:0098803
  locator: All three complete active term results and synonym scopes
  accessed_at: '2026-10-21T08:41:51.223465Z'
  support: supports
  summary: GO0009326 is the broader formate dehydrogenase complex, GO0098803 is respiratory-chain
    complex, and GO0036397 specifically defines formate plus quinone yielding CO2
    plus quinol. These parents/function do not equate FDH-N with FDH-O or FDH-H.
  snapshot_sha256: 0b5328aca2a791bb607e294fffa0abb06b0892fecef371a83b3d4f26ed0d2141
- evidence_id: fdn-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Native taxon names, rank and lineage
  accessed_at: '2026-10-21T08:41:51.223956Z'
  support: supports
  summary: Taxon83333 is the E.coli K-12 strain.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: fdn-agent-CPX-1975
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1975
  locator: Complete name/synonyms, organism, properties, participants, evidence and
    cited references
  accessed_at: '2026-10-21T08:41:54.216152Z'
  support: supports
  summary: 'Native CPX1975 names the K-12 FdnGHI heterononamer, including the maintained
    synonym variants. All seven imported participant rows, EBI identifiers, source_names
    and counts match: three each protein/Mo-bisMGD, six hemes, fifteenFe-S clusters
    and one menaquinone source participant.'
  snapshot_sha256: ed6cdaac9f3fd6c7c485a7721f2c97842d4a80b3fd18339a924bf918350cdc9a
- evidence_id: fdn-agent-P24183
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P24183.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T08:41:52.131653Z'
  support: supports
  summary: Native reviewed UniProtKB P24183 identifies Formate dehydrogenase, nitrate-inducible,
    major subunit, gene fdnG, taxon83333. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: ba2315e5da95abf93454652ba95bbb88544bacfd880ab626d0de191d2a4bbcfd
- evidence_id: fdn-agent-query-fdnG
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AfdnG%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene fdnG, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T08:41:53.722587Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P24183. This checks identifier
    resolution only.
  snapshot_sha256: fd97d9165d2474db32a0256d5d281eee329201683eae5b7ebb318e64c155f782
  search_scope: UniProtKB query gene_exact:fdnG AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: fdn-agent-P0AAJ3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AAJ3.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T08:41:51.778377Z'
  support: supports
  summary: Native reviewed UniProtKB P0AAJ3 identifies Formate dehydrogenase, nitrate-inducible,
    iron-sulfur subunit, gene fdnH, taxon83333. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: dfd5786fd27795f7864c49e371f7f6a2cf4a1be773a8fac4ea377a4a963ba349
- evidence_id: fdn-agent-query-fdnH
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AfdnH%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene fdnH, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T08:41:53.872183Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0AAJ3. This checks identifier
    resolution only.
  snapshot_sha256: 58db8e9048d4c7d73e40a9829a93684bab444f8f15ca2e739b71c55b70dad468
  search_scope: UniProtKB query gene_exact:fdnH AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: fdn-agent-P0AEK7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AEK7.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T08:41:51.845987Z'
  support: supports
  summary: Native reviewed UniProtKB P0AEK7 identifies Formate dehydrogenase, nitrate-inducible,
    cytochrome b556(Fdn) subunit, gene fdnI, taxon83333. Concrete identity is checked
    independently of membership; relevant subunit/cofactor/location comments retain
    their own evidence scope.
  snapshot_sha256: 944e58794aef18b85feefa6325421b4962db8fc0cc0dbb3a3c9c534b3bb00611
- evidence_id: fdn-agent-query-fdnI
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AfdnI%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene fdnI, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T08:41:54.161389Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0AEK7. This checks identifier
    resolution only.
  snapshot_sha256: b4349e8db16c10f14b726c577918be9e7ec446e677516d46ed531953dcc57150
  search_scope: UniProtKB query gene_exact:fdnI AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: fdn-agent-IPR006443
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006443/
  locator: Full family metadata/type/description, not only name or a matching domain
  accessed_at: '2026-10-21T08:42:36.843597Z'
  support: supports
  summary: Although named Formate dehydrogenase-N alpha, the native description explicitly
    includes both fdn and fdo genes; its scope is not exclusive to nitrate-inducible
    FdnG.
  snapshot_sha256: 24f4e300ffb3d9d955944ac1e052fc9f8fa01990be18ca8488598f57636b60d8
- evidence_id: fdn-agent-IPR006470
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006470/
  locator: Full family metadata/type/description, not only name or a matching domain
  accessed_at: '2026-10-21T08:42:36.174210Z'
  support: supports
  summary: Proteobacterial formate-dehydrogenase Fe-S family is broader than a verified
    nitrate-specific FdnH class.
  snapshot_sha256: 84eb09c9e62a1c1e495491e40225da1f78ff6a2058fd88392189ec969758187f
- evidence_id: fdn-agent-IPR014603
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014603/
  locator: Full family metadata/type/description, not only name or a matching domain
  accessed_at: '2026-10-21T08:42:36.177143Z'
  support: supports
  summary: General formate-dehydrogenase Fe-S family does not establish nitrate-specific
    identity.
  snapshot_sha256: 8bb0299ccaad43b41a404c591262616896e7787d67647ff3ab87de310c5fdd02
- evidence_id: fdn-agent-IPR051555
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051555/
  locator: Full family metadata/type/description, not only name or a matching domain
  accessed_at: '2026-10-21T08:42:36.409338Z'
  support: supports
  summary: Formate-dehydrogenase Fe-S family includes aerobic and anaerobic enzymes.
  snapshot_sha256: 0b9a9eff7be9ed6a6c783399f853c007079e2ce7f1d5797ee6f85f0e9997fd77
- evidence_id: fdn-agent-IPR006471
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006471/
  locator: Full family metadata/type/description, not only name or a matching domain
  accessed_at: '2026-10-21T08:42:36.831198Z'
  support: supports
  summary: Gamma-subunit family description includes homologous hydrogenase/thiosulfate-reductase
    membrane cytochromes.
  snapshot_sha256: 3d1551fd8933584086ab05290617b611d20f1703641048bbade7301cbe877851
- evidence_id: fdn-agent-IPR051817
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051817/
  locator: Full family metadata/type/description, not only name or a matching domain
  accessed_at: '2026-10-21T08:42:36.833427Z'
  support: supports
  summary: Formate-dehydrogenase cytochrome-b556 family spans aerobic and anaerobic
    forms.
  snapshot_sha256: 9a9fde2804cf8d99257b1bc6434666fd667d70b4eda23fc484a9be2eb6f68331
- evidence_id: fdn-agent-pdb-1KQF
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1KQF
  locator: rcsb_id, struct title, exptl, citation and entry identifiers
  accessed_at: '2026-10-21T08:41:54.506440Z'
  support: supports
  summary: 1KQF native entry identifies the Jormakka2002 crystallographic FDH-N deposition
    and exact primary DOI/PMID.
  snapshot_sha256: 8ce96a993ec257ffc5384e77084bee56759d921389b82efb555737814b81c5c8
- evidence_id: fdn-agent-assembly-1KQF
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1KQF/1
  locator: rcsb_assembly_info, pdbx_struct_assembly and pdbx_struct_assembly_gen
  accessed_at: '2026-10-21T08:41:54.579928Z'
  support: supports
  summary: 'Assembly1 of1KQF is author/software-defined nonameric: three protein entities,
    nine protein instances and three symmetry operations.'
  snapshot_sha256: 396e6dc9767bf66bfd6bd1f127f6b104880235f041f82fcff6edd347d763c3ac
- evidence_id: fdn-agent-1KQF-entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1KQF/1
  locator: Polymer entity description, source organism and SIFTS/UniProt identifiers
  accessed_at: '2026-10-21T08:42:36.848561Z'
  support: supports
  summary: 1KQF entity1 maps toP24183; native source organism is E.coli562. K-12 precision
    comes independently from CPX/UniProt.
  snapshot_sha256: 5e7545a1cc7e208cda532b23c908b84d9dac5b1f2496af215fd4bfa4fc5d2037
- evidence_id: fdn-agent-1KQF-entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1KQF/2
  locator: Polymer entity description, source organism and SIFTS/UniProt identifiers
  accessed_at: '2026-10-21T08:42:36.964773Z'
  support: supports
  summary: 1KQF entity2 maps toP0AAJ3; native source organism is E.coli562. K-12 precision
    comes independently from CPX/UniProt.
  snapshot_sha256: 49b781592b32961712149827a40a20fcf45dada43a52158da7c966aae4be5aab
- evidence_id: fdn-agent-1KQF-entity-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1KQF/3
  locator: Polymer entity description, source organism and SIFTS/UniProt identifiers
  accessed_at: '2026-10-21T08:42:37.027517Z'
  support: supports
  summary: 1KQF entity3 maps toP0AEK7; native source organism is E.coli562. K-12 precision
    comes independently from CPX/UniProt.
  snapshot_sha256: 0edb44ecfa5a61383a3d3334aa8aaaa401fa0cb8eece908d38afb534601f4747
- evidence_id: fdn-agent-pdb-1KQG
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1KQG
  locator: rcsb_id, struct title, exptl, citation and entry identifiers
  accessed_at: '2026-10-21T08:41:54.648249Z'
  support: supports
  summary: 1KQG native entry identifies the Jormakka2002 crystallographic FDH-N deposition
    and exact primary DOI/PMID.
  snapshot_sha256: 947a479b75b8c2f79e647a8fa57c5f1340aef0f31f7afe3524c96395fa8c4bfd
- evidence_id: fdn-agent-assembly-1KQG
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1KQG/1
  locator: rcsb_assembly_info, pdbx_struct_assembly and pdbx_struct_assembly_gen
  accessed_at: '2026-10-21T08:41:54.667082Z'
  support: supports
  summary: 'Assembly1 of1KQG is author/software-defined nonameric: three protein entities,
    nine protein instances and three symmetry operations.'
  snapshot_sha256: 8e17e6a2093dac1fcf1319c1997b8b6964c38f5e7defab8663794451abdd2e65
- evidence_id: fdn-agent-1KQG-entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1KQG/1
  locator: Polymer entity description, source organism and SIFTS/UniProt identifiers
  accessed_at: '2026-10-21T08:42:37.094856Z'
  support: supports
  summary: 1KQG entity1 maps toP24183; native source organism is E.coli562. K-12 precision
    comes independently from CPX/UniProt.
  snapshot_sha256: 1f7e83e800749d80c4368cd3eb7198aae540669347c994c778defd577ce1e895
- evidence_id: fdn-agent-1KQG-entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1KQG/2
  locator: Polymer entity description, source organism and SIFTS/UniProt identifiers
  accessed_at: '2026-10-21T08:42:37.113013Z'
  support: supports
  summary: 1KQG entity2 maps toP0AAJ3; native source organism is E.coli562. K-12 precision
    comes independently from CPX/UniProt.
  snapshot_sha256: c4b656a8bb5b39fb13da56aa6d79dc0934c8254cb34156fd294ea6448feb0b3e
- evidence_id: fdn-agent-1KQG-entity-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1KQG/3
  locator: Polymer entity description, source organism and SIFTS/UniProt identifiers
  accessed_at: '2026-10-21T08:42:37.196362Z'
  support: supports
  summary: 1KQG entity3 maps toP0AEK7; native source organism is E.coli562. K-12 precision
    comes independently from CPX/UniProt.
  snapshot_sha256: 54255d83c9a1faf99e8b70cb9f4a8853b38b48a6c93ede33a95043bde6671f51
- evidence_id: fdn-agent-chebi-60539
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/60539/
  locator: Accession/name/definition and source synonyms
  accessed_at: '2026-10-21T08:41:53.531327Z'
  support: supports
  summary: Native chemical identity agrees with the source import; chemical identity
    does not prove physiological copy number or complete occupancy.
  snapshot_sha256: e9ffe51dd2489ba6c59e45d20a75c43d8b34f660eb48899d3fc6e5c52c2fb033
- evidence_id: fdn-agent-chebi-16374
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/16374/
  locator: Accession/name/definition and source synonyms
  accessed_at: '2026-10-21T08:41:52.473321Z'
  support: supports
  summary: Native chemical identity agrees with the source import; chemical identity
    does not prove physiological copy number or complete occupancy.
  snapshot_sha256: d9f59441314e4734e202da12e8097b02f201c48a367412be21510e981ee37437
- evidence_id: fdn-agent-chebi-30413
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/30413/
  locator: Accession/name/definition and source synonyms
  accessed_at: '2026-10-21T08:41:52.859420Z'
  support: supports
  summary: Native chemical identity agrees with the source import; chemical identity
    does not prove physiological copy number or complete occupancy.
  snapshot_sha256: 39ffafcfd4c939d9283d2fa52598b9a119543eaad7841f8de09e625ff264c44e
- evidence_id: fdn-agent-chebi-33725
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/33725/
  locator: Accession/name/definition and source synonyms
  accessed_at: '2026-10-21T08:41:53.198370Z'
  support: supports
  summary: Native chemical identity agrees with the source import; chemical identity
    does not prove physiological copy number or complete occupancy.
  snapshot_sha256: 2f5cedc622b98e05a5f184709fef2ae7f0f5e28949a67bb46221a88c50bdacbf
- evidence_id: fdn-agent-eco-0000353
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/eco/terms?obo_id=ECO:0000353
  locator: Exact term id/label/definition
  accessed_at: '2026-10-21T08:42:04.386738Z'
  support: supports
  summary: ECO0000353 is physical interaction evidence used in manual assertion.
  snapshot_sha256: a85f179a3fca3a554fa914be25c4972efe9e487088eb9d16fdaf28961e63a057
- evidence_id: fdn-agent-jormakka2002-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.1068186
  locator: Exact bibliographic fields and abstract
  accessed_at: '2026-10-21T08:42:03.521343Z'
  support: supports
  summary: 'Jormakka, Törnroth, Byrne and Iwata2002, Molecular basis of proton motive
    force generation: structure of formate dehydrogenase-N, has PMID11884747 and DOI10.1126/science.1068186.'
  snapshot_sha256: 324593e619b6cba9d4c56b18ebdc14c8324171c2240ac6034d7c7225d766241b
- evidence_id: fdn-agent-jormakka2002-browser
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: 'Author-uploaded primary article displayed through browser: Introduction
    and overall-structure text, printed pp1863–1864. Original combined capture also
    contains unrelated Caltech metadata, which is not used here.'
  accessed_at: '2026-10-21T08:42:36Z'
  support: supports
  summary: Primary crystallography supports a trimer of FdnGHI heterotrimers and the
    physiological electron-donor/acceptor assignment.
  snapshot_sha256: cfd04dd5b54ad13716d5aa429d44d3d94e48cfcb427c3f090bcc6e23c34be4b9
- evidence_id: fdn-agent-jormakka2002-browser2
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: 'Primary pp1863–1866: overall structure, Electron transfer, alpha, beta
    and gamma sections and captions; browser display, no HTTP200 inferred.'
  accessed_at: '2026-10-21T08:48:50Z'
  support: supports
  summary: The alpha/beta/gamma architecture and cofactor relay agree with the component
    roles. Native coordinates and reviewed database entries independently corroborate
    membership.
  snapshot_sha256: 3a7d4cf752bc7fc1f0b7f2c8d310f8feee6e4cec7e1be745ebd73733132bc7fd
- evidence_id: fdn-agent-jormakka2002-browser3
  kind: primary_source
  reference: https://www.researchgate.net/publication/11477910_Molecular_Basis_of_Proton_Motive_Force_Generation_Structure_of_Formate_Dehydrogenase-N
  locator: 'Primary pp1865–1868: beta/gamma continuation, Quinone reduction mechanism,
    Table1 and concluding PMF section; no supplementary Methods or coordinate reanalysis.'
  accessed_at: '2026-10-21T08:49:03Z'
  support: supports
  summary: Quinone-site chemistry is proposed from an inhibitor-bound structure; the
    concluding proton-motive-force account is a coupled FDH-N/Nar redox loop, not
    an autonomous proton pump.
  snapshot_sha256: e5bda83037ed42c0ed4e5009f4932dd31a2ece97de2ff36bbcd3deb07d449eeb
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:48Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml'
  snapshot_sha256: 3f419a53d8ac7bfa055d1fd65126bbe3581feb736463ea8fe64fdb3666f64aec
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/formate_dehydrogenase_n_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml\
    \ --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/formate_dehydrogenase_n_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/formate_dehydrogenase_n_complex-strict.tsv"
  snapshot_sha256: fb4f3abe1c14d317b70a6a0156579a60c019bf21ae6f5a28ab4e5d81240c7f19
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:55:02Z'
  support: supports
  summary: '13 of18 collected target identifiers returned OK at the unchanged base.
    Residuals: ECO:0000353: SKIPPED; resolved by evidence fdn-agent-eco-0000353; PDB:1KQF:
    SKIPPED; resolved by evidence fdn-agent-pdb-1KQF; PDB:1KQG: SKIPPED; resolved
    by evidence fdn-agent-pdb-1KQG; PMID:11884747: UNREACHABLE; resolved by evidence
    fdn-agent-jormakka2002-meta; cellstructuremech:formate_dehydrogenase_n_complex:
    SKIPPED; resolved by evidence record. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T08:43:52.573504Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T08:43:53.247096Z'
  support: supports
  summary: "data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml  (cellstructuremech:formate_dehydrogenase_n_complex)\n\
    \  formate_dehydrogenase_n_quinone_reduction\tfdng\tCOVERED\t->fdng_alpha_subunit\
    \ (UniProtKB:P24183)\n  formate_dehydrogenase_n_quinone_reduction\tfdnh\tCOVERED\t\
    ->fdnh_iron_sulfur_subunit (UniProtKB:P0AAJ3)\n  formate_dehydrogenase_n_quinone_reduction\t\
    fdni\tCOVERED\t->fdni_cytochrome_b_subunit (UniProtKB:P0AEK7)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     3  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: ddbcd01abb0d76eba7fef7d3913e9a99b4dc47b7b86b76d810008e758a4a8d2c
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
  topic: Nitrate-inducible complex and broader parents
  outcome: supported
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: The local identifier consistently denotes FDH-N/FdnGHI. Parent classes
    are broader is-a categories; they do not equate N, O and H isozymes. Synonym scopes,
    category and kind agree with native CPX.
  evidence_ids:
  - fdn-agent-go
  - fdn-agent-CPX-1975
  - fdn-agent-jormakka2002-meta
  - record
- assessment_id: components
  area: evidence
  topic: Three subunit types and exact examples
  outcome: supported
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: Native CPX, PDB entities and reviewed UniProt agree on FdnG catalytic alpha,
    FdnH Fe-S relay and FdnI membrane cytochrome. All gene/taxon/accession pairs are
    exact. Constituent membership does not by itself establish the separate assembly-necessity
    assertion carried by ESSENTIAL.
  evidence_ids:
  - fdn-agent-CPX-1975
  - fdn-agent-P24183
  - fdn-agent-P0AAJ3
  - fdn-agent-P0AEK7
  - fdn-agent-pdb-1KQF
  - fdn-agent-assembly-1KQF
  - fdn-agent-1KQF-entity-1
  - fdn-agent-1KQF-entity-2
  - fdn-agent-1KQF-entity-3
  - fdn-agent-pdb-1KQG
  - fdn-agent-assembly-1KQG
  - fdn-agent-1KQG-entity-1
  - fdn-agent-1KQG-entity-2
  - fdn-agent-1KQG-entity-3
  - fdn-agent-jormakka2002-browser
  - fdn-agent-jormakka2002-browser2
  - record
- assessment_id: grounding
  area: grounding
  topic: Fdn-specific family scope
  outcome: supported
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: The inspected matching whole-family candidates extend into Fdo or other
    related oxidoreductases; generic cofactor domains are also broader. IPR006443
    title alone is misleadingly narrow relative to its definition. The existing label-only
    rows and bounded family TODO are justified without asserting that no exact family
    could exist anywhere.
  evidence_ids:
  - fdn-agent-IPR006443
  - fdn-agent-IPR006470
  - fdn-agent-IPR014603
  - fdn-agent-IPR051555
  - fdn-agent-IPR006471
  - fdn-agent-IPR051817
  - fdn-agent-P24183
  - fdn-agent-P0AAJ3
  - fdn-agent-P0AEK7
  - record
  - policy
- assessment_id: stoichiometry
  area: scope
  topic: Source-specific nonamer and cofactor rows
  outcome: supported
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: The3:3:3 protein assembly agrees between CPX1975 and both PDB biological
    assemblies. Imported chemical counts and names reproduce CPX; the lone menaquinone
    participant is not interpreted as proof that the entire physiological trimer has
    only one potential substrate site. No universal bacterial stoichiometry is inferred.
  evidence_ids:
  - fdn-agent-CPX-1975
  - fdn-agent-pdb-1KQF
  - fdn-agent-assembly-1KQF
  - fdn-agent-1KQF-entity-1
  - fdn-agent-1KQF-entity-2
  - fdn-agent-1KQF-entity-3
  - fdn-agent-pdb-1KQG
  - fdn-agent-assembly-1KQG
  - fdn-agent-1KQG-entity-1
  - fdn-agent-1KQG-entity-2
  - fdn-agent-1KQG-entity-3
  - fdn-agent-chebi-60539
  - fdn-agent-chebi-16374
  - fdn-agent-chebi-30413
  - fdn-agent-chebi-33725
  - record
- assessment_id: taxon
  area: scope
  topic: K-12 versus species-level deposit metadata
  outcome: supported
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: CPX and reviewed entries support K-12; original PDB entity source annotations
    are species562. These compatible levels are retained separately. No direct assignment
    of every historical preparation to a particular K-12 substrain or all-species
    prevalence is made.
  evidence_ids:
  - fdn-agent-tax-83333
  - fdn-agent-CPX-1975
  - fdn-agent-P24183
  - fdn-agent-P0AAJ3
  - fdn-agent-P0AEK7
  - fdn-agent-pdb-1KQF
  - fdn-agent-assembly-1KQF
  - fdn-agent-1KQF-entity-1
  - fdn-agent-1KQF-entity-2
  - fdn-agent-1KQF-entity-3
  - fdn-agent-pdb-1KQG
  - fdn-agent-assembly-1KQG
  - fdn-agent-1KQG-entity-1
  - fdn-agent-1KQG-entity-2
  - fdn-agent-1KQG-entity-3
  - record
- assessment_id: function-graph
  area: graph
  topic: Whole-complex reaction and constituent edges
  outcome: supported
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: All component_ref links and redox substrate/product edges match native
    function and complex records. The graph explicitly omits individual cofactor steps
    and does not promote the paper’s coupled redox-loop interpretation into autonomous
    proton pumping.
  evidence_ids:
  - fdn-agent-go
  - fdn-agent-CPX-1975
  - fdn-agent-jormakka2002-browser
  - fdn-agent-jormakka2002-browser2
  - fdn-agent-jormakka2002-browser3
  - record
- assessment_id: completeness
  area: completeness
  topic: Useful unresolved family question
  outcome: supported
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: Identity, membership, source assembly and function are adequately represented.
    Optional images, chemical rows outside the scoped import, explicit per-cofactor
    mechanisms and additional examples are not required. No concrete curation defect
    was established.
  evidence_ids:
  - fdn-agent-go
  - fdn-agent-CPX-1975
  - fdn-agent-IPR006443
  - fdn-agent-IPR006470
  - fdn-agent-IPR014603
  - fdn-agent-IPR051555
  - fdn-agent-IPR006471
  - fdn-agent-IPR051817
  - record
  - policy
- assessment_id: assembly-necessity
  area: evidence
  topic: Assembly necessity versus constituent membership
  outcome: unknown
  target_ids:
  - cellstructuremech:formate_dehydrogenase_n_complex
  summary: The schema defines essentiality by whether the structure forms without
    the component. The inspected sources establish constituent membership and functions,
    but those observations alone do not establish this assembly-necessity assertion.
    No subunit-deletion/assembly experiment was independently checked here; catalytic
    necessity, organismal viability and intact structural membership are distinct
    questions.
  evidence_ids:
  - fdn-agent-CPX-1975
  - fdn-agent-P24183
  - fdn-agent-P0AAJ3
  - fdn-agent-P0AEK7
  - fdn-agent-pdb-1KQF
  - fdn-agent-assembly-1KQF
  - fdn-agent-1KQF-entity-1
  - fdn-agent-1KQF-entity-2
  - fdn-agent-1KQF-entity-3
  - fdn-agent-pdb-1KQG
  - fdn-agent-assembly-1KQG
  - fdn-agent-1KQG-entity-1
  - fdn-agent-1KQG-entity-2
  - fdn-agent-1KQG-entity-3
  - fdn-agent-jormakka2002-browser
  - fdn-agent-jormakka2002-browser2
  - record
  - policy
findings: []
actions: []
limitations:
- Full primary body passages were readable through the browser’s author-uploaded text.
  Native ResearchGate and Colorado-index routes returned403; browser captures are
  hashed with actual access times and no invented HTTP status. Supplementary crystallization
  Methods, figure pixels and raw coordinates were not reanalyzed.
- The biological trimer is supported by structural packing/interface evidence and
  native assembly annotation; this is not an independent in-cell stoichiometric census.
  CPX chemical occupancy remains explicitly source-scoped.
- Family assessment is bounded to complete native integrated matches on the three
  exact reviewed examples and the six inspected candidate family definitions; no exhaustive
  all-database absence claim is made.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
- The schema defines essentiality by whether the structure forms without the component.
  The inspected sources establish constituent membership and functions, but those
  observations alone do not establish this assembly-necessity assertion. No subunit-deletion/assembly
  experiment was independently checked here; catalytic necessity, organismal viability
  and intact structural membership are distinct questions.
notes:
- All13 native inspection inputs and all source raw/meta hashes verified after fresh
  focused gates0. No record changes, finalization or status promotion.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
