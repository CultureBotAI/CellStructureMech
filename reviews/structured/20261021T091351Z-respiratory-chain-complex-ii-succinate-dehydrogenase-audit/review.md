# Succinate dehydrogenase identity, component scope and quinone-coupling review

- Review: 20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:50:42Z
- Finished UTC: 2026-10-21T09:13:51Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Complex II identity, exact four protein examples, grouped membrane module and bounded succinate-to-quinone graph are supported. Candidate family boundaries and assembly-necessity support remain explicitly limited; no concrete curation defect was established.

## Scope And Provenance

Entire single target; native GO/taxon/UniProt/InterPro/PDB identity and ligand scope; exact bibliography/abstracts and bounded primary Stenberg Methods/Results excerpts.

Selection: Seventh selected target in batch fourteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0045273 | data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml | maintained | respiratory chain complex II (succinate dehydrogenase) |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0045273 | Focused validator passed. |
| Focused native strict | passed | True | GO:0045273 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0045273 | 10 identifiers OK; 4 transport/skipped residuals independently resolved. |
| Native UniProt verify | passed | False | GO:0045273 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0045273 | Native command passed; scientific membership and graph scope assessed independently. |
| Claim-level scientific review | passed | True | GO:0045273 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0045273 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0045273 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0045273 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0045273 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0045273 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole respiratory complex

identity: supported. Targets: GO:0045273.

The GO label, related synonym, kind/category and respiratory-chain parent correctly distinguish the whole succinate:quinone oxidoreductase from isolated catalytic proteins and fumarate reductase.

### Four chains represented in three rows

evidence: supported. Targets: GO:0045273.

SdhA, SdhB and the deliberately grouped SdhC/D module agree with exact native proteins and deposited entities. FAD binding, Fe-S relay and membrane-anchor roles are supported. The paired module is a protein complex, not a single family or one accession.

### ESSENTIAL requires assembly evidence

evidence: unknown. Targets: GO:0045273.

The inspected structure, native protein annotations and gel study establish constituent membership and functions. Those observations do not establish that the defined structure cannot form without each component under the schema assembly-necessity criterion. No relevant deletion/assembly experiment was independently checked; activity and intact inventory are not substituted for that evidence.

### Candidate families have non-equivalent boundaries

grounding: supported. Targets: GO:0045273.

The existing label-only treatment is defensible for the stated full SdhA, SdhB and paired C/D scopes. IPR011281 is a narrower SdhA clade; IPR014006/030664 and004489 are broader shared enzyme families; individual SdhC/D families do not ground the whole module. No global absence claim or requirement to split the paired row is made.

### Species and strain contexts

scope: supported. Targets: GO:0045273.

The canonical crystallographic example is E.coli at species level and the exact protein examples are reviewed K-12 entries. Stenberg membrane proteomics uses BL21; the record cites UniProt location attribution rather than falsely assigning that preparation to K-12.

### Coarse relay and structural ligand

graph: supported. Targets: GO:0045273.

The succinate/FAD/Fe-S/quinone relay and whole-complex GO activity are supported at the stated NONMECHANISTIC level. Native coordinates verify modeled ubiquinone-2, not quinone-reduction kinetics by an isolated C/D module. No proton-pumping, ROS mechanism, exact electron-transfer distance or higher-oligomer stoichiometry is asserted.

### Exact source identity and readable scope

provenance: supported. Targets: GO:0045273.

Yankovskaya2003, Stenberg2005 and Daley2005 identities match maintained citations. Native UniProt location evidence lists the exact maintained PMIDs; this attribution was checked directly. Only indexed claim-bearing Stenberg body excerpts were recovered; the complete Yankovskaya and Daley bodies were not read.

### Optional extensions and bounded unresolved evidence

completeness: supported. Targets: GO:0045273.

Known protein membership is represented. Exact family refinements, added cofactors or stoichiometry, images and fuller mechanism are optional. Assembly-necessity support remains explicitly unresolved; no concrete contradictory assertion was established from the bounded sources.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| sdh-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008177,GO:0045273,GO:0098803; Complete three native term identities, definitions, comments, synonyms, status and returned parent relation | supports | Active GO0045273 identifies respiratory complex II; GO0098803 is the broader respiratory-chain-complex parent. GO0008177 explicitly denotes succinate dehydrogenase quinone activity of the whole complex, not an isolated SdhA protein. |
| sdh-agent-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native names, rank and lineage | supports | Native taxonomy separates Escherichia coli species562 from K-12 strain83333; both maintained labels are correct. |
| sdh-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native names, rank and lineage | supports | Native taxonomy separates Escherichia coli species562 from K-12 strain83333; both maintained labels are correct. |
| sdh-agent-P0AC41 | https://rest.uniprot.org/uniprotkb/P0AC41.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0AC41 identifies Succinate dehydrogenase flavoprotein subunit, gene sdhA, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| sdh-agent-query-sdhA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AsdhA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene sdhA, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0AC41. This checks identifier resolution only. |
| sdh-agent-P07014 | https://rest.uniprot.org/uniprotkb/P07014.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P07014 identifies Succinate dehydrogenase iron-sulfur subunit, gene sdhB, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| sdh-agent-query-sdhB | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AsdhB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene sdhB, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P07014. This checks identifier resolution only. |
| sdh-agent-P69054 | https://rest.uniprot.org/uniprotkb/P69054.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P69054 identifies Succinate dehydrogenase cytochrome b556 subunit, gene sdhC, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| sdh-agent-query-sdhC | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AsdhC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene sdhC, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P69054. This checks identifier resolution only. |
| sdh-agent-P0AC44 | https://rest.uniprot.org/uniprotkb/P0AC44.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0AC44 identifies Succinate dehydrogenase hydrophobic membrane anchor subunit, gene sdhD, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| sdh-agent-query-sdhD | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AsdhD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene sdhD, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0AC44. This checks identifier resolution only. |
| sdh-agent-matches-P0AC41 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AC41/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| sdh-agent-matches-P07014 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P07014/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| sdh-agent-matches-P69054 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P69054/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| sdh-agent-matches-P0AC44 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AC44/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| sdh-agent-IPR011281 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011281/; Complete native metadata accession/type/name and family description | supports | This SdhA family is explicitly a narrowly defined clade and excludes putative succinate dehydrogenases diverging before the E.coli Sdh/Frd split. It is a useful candidate for the E.coli example, not an exact equivalent of every full SdhA lineage. |
| sdh-agent-IPR014006 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014006/; Complete native metadata accession/type/name and family description | supports | The flavoprotein family explicitly includes both succinate dehydrogenase and fumarate reductase; it is broader than the SdhA component. |
| sdh-agent-IPR030664 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030664/; Complete native metadata accession/type/name and family description | supports | This family additionally includes AprA/APS reductase and is too broad for exact SdhA grounding. |
| sdh-agent-IPR004489 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004489/; Complete native metadata accession/type/name and family description | supports | The Fe-S protein family includes both SdhB and FrdB, plus a region of an archaeal fumarate reductase; it is not an exact SdhB family. |
| sdh-agent-IPR014314 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014314/; Complete native metadata accession/type/name and family description | supports | The cytochrome b556 family describes individual SdhC chains, not the combined SdhC/D module. |
| sdh-agent-IPR014312 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014312/; Complete native metadata accession/type/name and family description | supports | The membrane-anchor family describes individual SdhD chains, not the combined SdhC/D module. |
| sdh-agent-IPR065464 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR065464/; Complete native metadata accession/type/name and family description | supports | This SdhD family has gamma/betaproteobacterial scope and again represents one chain rather than the paired module. |
| sdh-agent-pdb-1NEK | https://data.rcsb.org/rest/v1/core/entry/1NEK; Entry title, experimental method, resolution and primary citation | supports | 1NEK is the E.coli succinate-dehydrogenase X-ray deposit at2.6A linked to the exact Yankovskaya2003 citation. |
| sdh-agent-assembly-1NEK | https://data.rcsb.org/rest/v1/core/assembly/1NEK/1; rcsb_assembly_info and author/software assembly annotations | supports | Native assembly1 contains four distinct protein entities and four instances, the source-scoped SdhABCD unit. It is not a universal statement about higher oligomers in membranes. |
| sdh-agent-1NEK-entity-1 | https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/1; Polymer description, source organism, UniProt/SIFTS mapping | supports | Native entity1 identifies the exact maintained accession P0AC41, with species562 source and complete mapped protein identity. |
| sdh-agent-1NEK-entity-2 | https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/2; Polymer description, source organism, UniProt/SIFTS mapping | supports | Native entity2 identifies the exact maintained accession P07014, with species562 source and complete mapped protein identity. |
| sdh-agent-1NEK-entity-3 | https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/3; Polymer description, source organism, UniProt/SIFTS mapping | supports | Native entity3 identifies the exact maintained accession P69054, with species562 source and complete mapped protein identity. |
| sdh-agent-1NEK-entity-4 | https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/4; Polymer description, source organism, UniProt/SIFTS mapping | supports | Native entity4 identifies the exact maintained accession P0AC44, with species562 source and complete mapped protein identity. |
| sdh-agent-1NEK-cif | https://files.rcsb.org/download/1NEK.cif; mmCIF entity/nonpolymer/chemical dictionaries, pdbx_nonpoly_scheme, struct_site AC9 and site members; atom records confirm modeled UQ2. No coordinate refinement or independent contact calculation. | supports | The deposited model contains UQ2, explicitly named ubiquinone-2, as nonpolymer entity14 and residueD306. Its annotated binding site AC9 accompanies the C/D membrane region; the maintained graph correctly says bound ubiquinone-2 rather than claiming an added kinetic experiment. |
| sdh-agent-pmid-12560550 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:12560550%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Architecture of succinate dehydrogenase and reactive oxygen species generation. Authors: Yankovskaya V, Horsefield R, Törnroth S, Luna-Chavez C, Miyoshi H, Léger C, Byrne B, Cecchini G, Iwata S.; PMID 12560550; DOI 10.1126/science.1079605. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| sdh-agent-pmid-15919996 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:15919996%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Global topology analysis of the Escherichia coli inner membrane proteome. Authors: Daley DO, Rapp M, Granseth E, Melén K, Drew D, von Heijne G.; PMID 15919996; DOI 10.1126/science.1109730. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| sdh-agent-pmid-16079137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:16079137%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Protein complexes of the Escherichia coli cell envelope. Authors: Stenberg F, Chovanec P, Maslen SL, Robinson CV, Ilag LL, von Heijne G, Daley DO.; PMID 16079137; DOI 10.1074/jbc.m506479200. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| sdh-agent-bdi-browser5 | https://doi.org/10.1074/jbc.M506479200; Discontinuous indexed JBC primary Results, Protein Complexes in the Inner Membrane &gt; Bioenergetic Complexes; succinate-dehydrogenase paragraph and Figure3 caption. No claim of full article or full Table1 access. | supports | Primary Stenberg2005 results identify SdhA/B by protein analysis, infer C/D by gel size/co-migration and infer an intact higher oligomer from BN/SDS-PAGE. This supports membrane-complex membership with explicit method limits. |
| sdh-agent-bdi-stenberg-methods-search2 | https://doi.org/10.1074/jbc.M506479200; Indexed primary Methods &gt; Preparation of Membrane Vesicles and BN-PAGE; Results &gt; Protein Identification and succinate-dehydrogenase paragraph/Figure3 caption. Original receipt reused unchanged. | supports | Primary preparation uses BL21(DE3)pLysS grown at37C in LB to late log phase, sucrose-separated membrane vesicles and0.5%DDM BN/SDS-PAGE. It does not itself establish K-12 source provenance for every protein example. |
| schema-result | just validate data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml |
| strict-result | just validate-strict data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_ii_succinate_dehydrogenase-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_ii_succinate_dehydrogenase-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_ii_succinate_dehydrogenase-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 10 of14 collected target identifiers returned OK at the unchanged base. Residuals: PDB:1NEK: SKIPPED; resolved by evidence sdh-agent-pdb-1NEK; PMID:12560550: UNREACHABLE; resolved by evidence sdh-agent-pmid-12560550; PMID:15919996: UNREACHABLE; resolved by evidence sdh-agent-pmid-15919996; PMID:16079137: UNREACHABLE; resolved by evidence sdh-agent-pmid-16079137. Source-native identity checked separately. |
| native-verify | /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml  (GO:0045273)<br>  complex_ii_succinate_quinone_coupling	flavoprotein	COVERED	-&gt;sdha_flavoprotein (UniProtKB:P0AC41)<br>  complex_ii_succinate_quinone_coupling	iron_sulfur_subunit	COVERED	-&gt;sdhb_iron_sulfur_subunit (UniProtKB:P07014)<br>  complex_ii_succinate_quinone_coupling	membrane_anchor	COVERED	-&gt;sdhcd_membrane_anchor (UniProtKB:P69054, UniProtKB:P0AC44)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- ESSENTIAL means whether the structure forms without the component. Membership, catalytic role, a deposited complete structure and cell viability do not establish that claim; assembly necessity remains unverified for the three component rows.
- Yankovskaya2003 publisher/PDF access returned403; a university PDF candidate proved to be Lancaster1999 on a different fumarate reductase and was excluded. Yankovskaya support is therefore limited to exact native abstract, reviewed annotations and its actual1NEK deposit. Daley2005 was checked at metadata/abstract and UniProt-attribution level, not full body.
- Stenberg evidence is discontinuous indexed primary body with actual original access timestamps and status:null. A/B identification is distinct from C/D co-migration inference. Its BL21 preparation and inferred trimer do not override the species-level1NEK unit or K-12 example identities.
- Family scope is bounded to the complete integrated matches for four examples and the seven inspected family definitions. IPR011281 is a concrete narrower candidate, not proof that no exact broad family exists.
- Deposited ligand/assembly annotations were read without independent geometry, structure refinement or figure-pixel analysis. No new image, numerical property, source promotion or whole-paper access claim is made.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All13 native inspection input hashes, focused checks0 and source raw/meta hashes verified. Scientific state and corpus remain unchanged.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091351Z-respiratory-chain-complex-ii-succinate-dehydrogenase-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Succinate dehydrogenase identity, component scope and quinone-coupling review
started_at: '2026-10-21T08:50:42Z'
finished_at: '2026-10-21T09:13:51Z'
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
summary: Complex II identity, exact four protein examples, grouped membrane module
  and bounded succinate-to-quinone graph are supported. Candidate family boundaries
  and assembly-necessity support remain explicitly limited; no concrete curation defect
  was established.
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
  - path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    sha256: 9660cbd309d7c81353bf0b1fe1a3cd5a883f6ec574e3a0d9e990166dd861de0f
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
- target_id: GO:0045273
  path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  label: respiratory chain complex II (succinate dehydrogenase)
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    role: maintained scientific record
scope:
  description: Entire single target; native GO/taxon/UniProt/InterPro/PDB identity
    and ligand scope; exact bibliography/abstracts and bounded primary Stenberg Methods/Results
    excerpts.
  selection: Seventh selected target in batch fourteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0045273
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just validate data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just validate-strict data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_ii_succinate_dehydrogenase-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0045273
  summary: 10 identifiers OK; 4 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - sdh-agent-pdb-1NEK
  - sdh-agent-pmid-12560550
  - sdh-agent-pmid-15919996
  - sdh-agent-pmid-16079137
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0045273
  command: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
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
  - GO:0045273
  command: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
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
  - GO:0045273
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - sdh-agent-go
  - sdh-agent-tax-562
  - sdh-agent-tax-83333
  - sdh-agent-P0AC41
  - sdh-agent-query-sdhA
  - sdh-agent-P07014
  - sdh-agent-query-sdhB
  - sdh-agent-P69054
  - sdh-agent-query-sdhC
  - sdh-agent-P0AC44
  - sdh-agent-query-sdhD
  - sdh-agent-matches-P0AC41
  - sdh-agent-matches-P07014
  - sdh-agent-matches-P69054
  - sdh-agent-matches-P0AC44
  - sdh-agent-IPR011281
  - sdh-agent-IPR014006
  - sdh-agent-IPR030664
  - sdh-agent-IPR004489
  - sdh-agent-IPR014314
  - sdh-agent-IPR014312
  - sdh-agent-IPR065464
  - sdh-agent-pdb-1NEK
  - sdh-agent-assembly-1NEK
  - sdh-agent-1NEK-entity-1
  - sdh-agent-1NEK-entity-2
  - sdh-agent-1NEK-entity-3
  - sdh-agent-1NEK-entity-4
  - sdh-agent-1NEK-cif
  - sdh-agent-pmid-12560550
  - sdh-agent-pmid-15919996
  - sdh-agent-pmid-16079137
  - sdh-agent-bdi-browser5
  - sdh-agent-bdi-stenberg-methods-search2
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0045273
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T09:12:53Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:12:53Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: sdh-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0008177,GO:0045273,GO:0098803
  locator: Complete three native term identities, definitions, comments, synonyms,
    status and returned parent relation
  accessed_at: '2026-10-21T09:01:27.864104Z'
  support: supports
  summary: Active GO0045273 identifies respiratory complex II; GO0098803 is the broader
    respiratory-chain-complex parent. GO0008177 explicitly denotes succinate dehydrogenase
    quinone activity of the whole complex, not an isolated SdhA protein.
  snapshot_sha256: ce33121b76b994e5243ffe282c6d5b7b3c3c642d65bb785681c579e1a9b7b667
- evidence_id: sdh-agent-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native names, rank and lineage
  accessed_at: '2026-10-21T09:01:27.864580Z'
  support: supports
  summary: Native taxonomy separates Escherichia coli species562 from K-12 strain83333;
    both maintained labels are correct.
  snapshot_sha256: 66d5c5c74569e24b72fd7b011961dc221b58d841db7db3023337fb534733e200
- evidence_id: sdh-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native names, rank and lineage
  accessed_at: '2026-10-21T09:01:27.864883Z'
  support: supports
  summary: Native taxonomy separates Escherichia coli species562 from K-12 strain83333;
    both maintained labels are correct.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: sdh-agent-P0AC41
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AC41.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:28.495796Z'
  support: supports
  summary: Native reviewed UniProtKB P0AC41 identifies Succinate dehydrogenase flavoprotein
    subunit, gene sdhA, taxon83333. Concrete identity is checked independently of
    membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: dd974a9bf8408ea362e9ac736d2c54fb179c9ec71e753aefdda9943218e22561
- evidence_id: sdh-agent-query-sdhA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AsdhA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene sdhA, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:16.603410Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0AC41. This checks identifier
    resolution only.
  snapshot_sha256: 1f2cfc59ff0d3fa0ad2703fafe26899f7598120362d6446eec48f44f0f31a3ea
  search_scope: UniProtKB query gene_exact:sdhA AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: sdh-agent-P07014
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P07014.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:27.865015Z'
  support: supports
  summary: Native reviewed UniProtKB P07014 identifies Succinate dehydrogenase iron-sulfur
    subunit, gene sdhB, taxon83333. Concrete identity is checked independently of
    membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: 0ab790707f2f780f7a2787ed1065de449585f5fb7d97d51e4672ca1e083b2736
- evidence_id: sdh-agent-query-sdhB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AsdhB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene sdhB, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:16.690365Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P07014. This checks identifier
    resolution only.
  snapshot_sha256: a8decfb2a151fdd947d339e1b5997d58a0c9ff7def1969b040913b3a43a9ac09
  search_scope: UniProtKB query gene_exact:sdhB AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: sdh-agent-P69054
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P69054.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:29.179359Z'
  support: supports
  summary: Native reviewed UniProtKB P69054 identifies Succinate dehydrogenase cytochrome
    b556 subunit, gene sdhC, taxon83333. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: a861e4627427556398758d3c17389bc35671c262623fd9edd9d9a4d57bf696d1
- evidence_id: sdh-agent-query-sdhC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AsdhC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene sdhC, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:16.692336Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P69054. This checks identifier
    resolution only.
  snapshot_sha256: 3be29b01ee51542249b33ba8fcede02afabe4cda988598d0f12e4004e0b628f6
  search_scope: UniProtKB query gene_exact:sdhC AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: sdh-agent-P0AC44
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AC44.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:28.736808Z'
  support: supports
  summary: Native reviewed UniProtKB P0AC44 identifies Succinate dehydrogenase hydrophobic
    membrane anchor subunit, gene sdhD, taxon83333. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: 5993ab7762d4158d75a9b2798535745537aa8bb7a4b8592a3cc14fdbdefb057d
- evidence_id: sdh-agent-query-sdhD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AsdhD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene sdhD, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:16.910719Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0AC44. This checks identifier
    resolution only.
  snapshot_sha256: 1d1c674d03162fc285526244a3fadf841db347ce11abbf47b7f8fbdc7b90e8a6
  search_scope: UniProtKB query gene_exact:sdhD AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: sdh-agent-matches-P0AC41
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AC41/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T09:01:28.725646Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: 8274cf4827b0355b467e34f081fef73b6792bf2166631bda0ca3fd2ee2eabc70
- evidence_id: sdh-agent-matches-P07014
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P07014/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T09:01:27.865144Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: bab7babafd234baa21b3d71e24fa6443e8b7a7371a957839d887d7cbde728b3c
- evidence_id: sdh-agent-matches-P69054
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P69054/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T09:01:29.487881Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: 189f2eec401afa419d2fb1778284ec73cc8bbb9b1fffd4b4ab507fc034645800
- evidence_id: sdh-agent-matches-P0AC44
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0AC44/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T09:01:28.761949Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: 1ce420bbd621053ef31a694288f3a3a402b643bb591745967dc595bb04534e96
- evidence_id: sdh-agent-IPR011281
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR011281/
  locator: Complete native metadata accession/type/name and family description
  accessed_at: '2026-10-21T09:02:18.824178Z'
  support: supports
  summary: This SdhA family is explicitly a narrowly defined clade and excludes putative
    succinate dehydrogenases diverging before the E.coli Sdh/Frd split. It is a useful
    candidate for the E.coli example, not an exact equivalent of every full SdhA lineage.
  snapshot_sha256: 1af86e373e062b9a8d4461556d679cd22b9266ce7e295b5cf56ba530e5787fa9
- evidence_id: sdh-agent-IPR014006
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014006/
  locator: Complete native metadata accession/type/name and family description
  accessed_at: '2026-10-21T09:01:40.517976Z'
  support: supports
  summary: The flavoprotein family explicitly includes both succinate dehydrogenase
    and fumarate reductase; it is broader than the SdhA component.
  snapshot_sha256: 98addafe843653636aafa954821cc9126e53ae8d87669d6ceb3debf304347fe9
- evidence_id: sdh-agent-IPR030664
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR030664/
  locator: Complete native metadata accession/type/name and family description
  accessed_at: '2026-10-21T09:01:40.651722Z'
  support: supports
  summary: This family additionally includes AprA/APS reductase and is too broad for
    exact SdhA grounding.
  snapshot_sha256: 03a1506a2c0c2378f7a2c4923f6e160036c42080411192aa59051bb76ffb71a4
- evidence_id: sdh-agent-IPR004489
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR004489/
  locator: Complete native metadata accession/type/name and family description
  accessed_at: '2026-10-21T09:01:40.428336Z'
  support: supports
  summary: The Fe-S protein family includes both SdhB and FrdB, plus a region of an
    archaeal fumarate reductase; it is not an exact SdhB family.
  snapshot_sha256: f5209b776ca14700e78ca9330b389e07a61e46b0aea6fae21c6d558cdd1c58a7
- evidence_id: sdh-agent-IPR014314
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014314/
  locator: Complete native metadata accession/type/name and family description
  accessed_at: '2026-10-21T09:02:19.302414Z'
  support: supports
  summary: The cytochrome b556 family describes individual SdhC chains, not the combined
    SdhC/D module.
  snapshot_sha256: 3405c338c549cf5d8432d424e7615fcae9b97b062cb9a707b1deba3dad5dbd0a
- evidence_id: sdh-agent-IPR014312
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014312/
  locator: Complete native metadata accession/type/name and family description
  accessed_at: '2026-10-21T09:02:19.462013Z'
  support: supports
  summary: The membrane-anchor family describes individual SdhD chains, not the combined
    SdhC/D module.
  snapshot_sha256: bb62534fdf2691d88a787eb05e6650f54f4f62490a8c0026aaeb61fc9055dd93
- evidence_id: sdh-agent-IPR065464
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR065464/
  locator: Complete native metadata accession/type/name and family description
  accessed_at: '2026-10-21T09:02:19.570313Z'
  support: supports
  summary: This SdhD family has gamma/betaproteobacterial scope and again represents
    one chain rather than the paired module.
  snapshot_sha256: 41dc0a638addd973d1546cfb086d0c2d3e3090c9b0f52c1ddf9fa232e16903ca
- evidence_id: sdh-agent-pdb-1NEK
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/entry/1NEK
  locator: Entry title, experimental method, resolution and primary citation
  accessed_at: '2026-10-21T09:01:40.785512Z'
  support: supports
  summary: 1NEK is the E.coli succinate-dehydrogenase X-ray deposit at2.6A linked
    to the exact Yankovskaya2003 citation.
  snapshot_sha256: 914721e829789202d7e7c2a2285bb956ac9e53a5290ff0ef0fe098b91c7f094e
- evidence_id: sdh-agent-assembly-1NEK
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/assembly/1NEK/1
  locator: rcsb_assembly_info and author/software assembly annotations
  accessed_at: '2026-10-21T09:01:40.891257Z'
  support: supports
  summary: Native assembly1 contains four distinct protein entities and four instances,
    the source-scoped SdhABCD unit. It is not a universal statement about higher oligomers
    in membranes.
  snapshot_sha256: a38b4de61bb4f1e282d0fba783ff44d64e6e8a78143e8a905d879a7cabc28dfa
- evidence_id: sdh-agent-1NEK-entity-1
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/1
  locator: Polymer description, source organism, UniProt/SIFTS mapping
  accessed_at: '2026-10-21T09:01:40.962016Z'
  support: supports
  summary: Native entity1 identifies the exact maintained accession P0AC41, with species562
    source and complete mapped protein identity.
  snapshot_sha256: 224de66a9cb5788d39589c1cb30d1c13bb35d1a4664806846a86a8693eeb3e4a
- evidence_id: sdh-agent-1NEK-entity-2
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/2
  locator: Polymer description, source organism, UniProt/SIFTS mapping
  accessed_at: '2026-10-21T09:01:41.087517Z'
  support: supports
  summary: Native entity2 identifies the exact maintained accession P07014, with species562
    source and complete mapped protein identity.
  snapshot_sha256: ed28e1ea733071a99154032dbaa8e75f83fa73ea1974f4d14a65d54e39e64610
- evidence_id: sdh-agent-1NEK-entity-3
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/3
  locator: Polymer description, source organism, UniProt/SIFTS mapping
  accessed_at: '2026-10-21T09:01:41.097284Z'
  support: supports
  summary: Native entity3 identifies the exact maintained accession P69054, with species562
    source and complete mapped protein identity.
  snapshot_sha256: 380abe3e6442d55e40277c52d6f73d7cc41f66843b0ceff32d4bccbf9a5207b7
- evidence_id: sdh-agent-1NEK-entity-4
  kind: database
  reference: https://data.rcsb.org/rest/v1/core/polymer_entity/1NEK/4
  locator: Polymer description, source organism, UniProt/SIFTS mapping
  accessed_at: '2026-10-21T09:01:41.177888Z'
  support: supports
  summary: Native entity4 identifies the exact maintained accession P0AC44, with species562
    source and complete mapped protein identity.
  snapshot_sha256: 2e859c21b35901a7a83116fbfab7394c452cb31391b1bf52fc9710cdf8fa7df1
- evidence_id: sdh-agent-1NEK-cif
  kind: database
  reference: https://files.rcsb.org/download/1NEK.cif
  locator: mmCIF entity/nonpolymer/chemical dictionaries, pdbx_nonpoly_scheme, struct_site
    AC9 and site members; atom records confirm modeled UQ2. No coordinate refinement
    or independent contact calculation.
  accessed_at: '2026-10-21T09:09:43.018314Z'
  support: supports
  summary: The deposited model contains UQ2, explicitly named ubiquinone-2, as nonpolymer
    entity14 and residueD306. Its annotated binding site AC9 accompanies the C/D membrane
    region; the maintained graph correctly says bound ubiquinone-2 rather than claiming
    an added kinetic experiment.
  snapshot_sha256: 9b751b5890bfc6128a0c47c69cb1800b64fbf9caa6977ff9acc8b6f2ac1c6397
- evidence_id: sdh-agent-pmid-12560550
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:12560550%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:29.872414Z'
  support: supports
  summary: 'Native metadata identifies Architecture of succinate dehydrogenase and
    reactive oxygen species generation. Authors: Yankovskaya V, Horsefield R, Törnroth
    S, Luna-Chavez C, Miyoshi H, Léger C, Byrne B, Cecchini G, Iwata S.; PMID 12560550;
    DOI 10.1126/science.1079605. Bibliographic identity and available abstract only;
    not a substitute for inspected article body.'
  snapshot_sha256: 71ec39b447ca0c2e09b0022a30553b17a96ddaf003d9b428a95928d713f24a26
- evidence_id: sdh-agent-pmid-15919996
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:15919996%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:30.540786Z'
  support: supports
  summary: 'Native metadata identifies Global topology analysis of the Escherichia
    coli inner membrane proteome. Authors: Daley DO, Rapp M, Granseth E, Melén K,
    Drew D, von Heijne G.; PMID 15919996; DOI 10.1126/science.1109730. Bibliographic
    identity and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: bf238a68f2eaffe3abc2659ccf4a6bdd1cc0660ac62559a2661c58032d4502f5
- evidence_id: sdh-agent-pmid-16079137
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:16079137%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:31.179632Z'
  support: supports
  summary: 'Native metadata identifies Protein complexes of the Escherichia coli cell
    envelope. Authors: Stenberg F, Chovanec P, Maslen SL, Robinson CV, Ilag LL, von
    Heijne G, Daley DO.; PMID 16079137; DOI 10.1074/jbc.m506479200. Bibliographic
    identity and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: cf1c57d1a5343edc60d65a0b5d128f9d7b78f0006ac9526b7a31be6d9945918a
- evidence_id: sdh-agent-bdi-browser5
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M506479200
  locator: Discontinuous indexed JBC primary Results, Protein Complexes in the Inner
    Membrane > Bioenergetic Complexes; succinate-dehydrogenase paragraph and Figure3
    caption. No claim of full article or full Table1 access.
  accessed_at: '2026-10-21T08:42:51.281Z'
  support: supports
  summary: Primary Stenberg2005 results identify SdhA/B by protein analysis, infer
    C/D by gel size/co-migration and infer an intact higher oligomer from BN/SDS-PAGE.
    This supports membrane-complex membership with explicit method limits.
  snapshot_sha256: 1359a24816b54519a127f7c3c2fe0e188ecccb08eb898acadc88b2860e985162
- evidence_id: sdh-agent-bdi-stenberg-methods-search2
  kind: primary_source
  reference: https://doi.org/10.1074/jbc.M506479200
  locator: Indexed primary Methods > Preparation of Membrane Vesicles and BN-PAGE;
    Results > Protein Identification and succinate-dehydrogenase paragraph/Figure3
    caption. Original receipt reused unchanged.
  accessed_at: '2026-10-21T08:43:22.725Z'
  support: supports
  summary: Primary preparation uses BL21(DE3)pLysS grown at37C in LB to late log phase,
    sucrose-separated membrane vesicles and0.5%DDM BN/SDS-PAGE. It does not itself
    establish K-12 source provenance for every protein example.
  snapshot_sha256: 9cb13cd4e0ee40b1493ce919ebc6ba74b467ea5adc5849fc0a92a4b394aa2e0d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:50:46Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml'
  snapshot_sha256: b45adfff6ba6a6b3880d831049f4217256c64fbb39f56e088a4ebd0deaa33183
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_ii_succinate_dehydrogenase-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:50:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml\
    \ --out /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_ii_succinate_dehydrogenase-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/respiratory_chain_complex_ii_succinate_dehydrogenase-strict.tsv"
  snapshot_sha256: 55318137fb42c3cd504fe3b06f7f250682f56a8a4e82aa284488b38a3eff0d2c
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:12:53Z'
  support: supports
  summary: '10 of14 collected target identifiers returned OK at the unchanged base.
    Residuals: PDB:1NEK: SKIPPED; resolved by evidence sdh-agent-pdb-1NEK; PMID:12560550:
    UNREACHABLE; resolved by evidence sdh-agent-pmid-12560550; PMID:15919996: UNREACHABLE;
    resolved by evidence sdh-agent-pmid-15919996; PMID:16079137: UNREACHABLE; resolved
    by evidence sdh-agent-pmid-16079137. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T09:01:31.384054Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T09:01:32.199329Z'
  support: supports
  summary: "data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml\
    \  (GO:0045273)\n  complex_ii_succinate_quinone_coupling\tflavoprotein\tCOVERED\t\
    ->sdha_flavoprotein (UniProtKB:P0AC41)\n  complex_ii_succinate_quinone_coupling\t\
    iron_sulfur_subunit\tCOVERED\t->sdhb_iron_sulfur_subunit (UniProtKB:P07014)\n\
    \  complex_ii_succinate_quinone_coupling\tmembrane_anchor\tCOVERED\t->sdhcd_membrane_anchor\
    \ (UniProtKB:P69054, UniProtKB:P0AC44)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n\
    \     3  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     3  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 80d0a4439ebf3fc5efc9c149ca8dd16309e5c2482d4a18223120024cb5e555d1
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
  topic: Whole respiratory complex
  outcome: supported
  target_ids:
  - GO:0045273
  summary: The GO label, related synonym, kind/category and respiratory-chain parent
    correctly distinguish the whole succinate:quinone oxidoreductase from isolated
    catalytic proteins and fumarate reductase.
  evidence_ids:
  - sdh-agent-go
  - sdh-agent-pdb-1NEK
  - sdh-agent-pmid-12560550
  - record
- assessment_id: components
  area: evidence
  topic: Four chains represented in three rows
  outcome: supported
  target_ids:
  - GO:0045273
  summary: SdhA, SdhB and the deliberately grouped SdhC/D module agree with exact
    native proteins and deposited entities. FAD binding, Fe-S relay and membrane-anchor
    roles are supported. The paired module is a protein complex, not a single family
    or one accession.
  evidence_ids:
  - sdh-agent-P0AC41
  - sdh-agent-P07014
  - sdh-agent-P69054
  - sdh-agent-P0AC44
  - sdh-agent-pdb-1NEK
  - sdh-agent-1NEK-entity-1
  - sdh-agent-1NEK-entity-2
  - sdh-agent-1NEK-entity-3
  - sdh-agent-1NEK-entity-4
  - sdh-agent-bdi-browser5
  - record
- assessment_id: assembly-necessity
  area: evidence
  topic: ESSENTIAL requires assembly evidence
  outcome: unknown
  target_ids:
  - GO:0045273
  summary: The inspected structure, native protein annotations and gel study establish
    constituent membership and functions. Those observations do not establish that
    the defined structure cannot form without each component under the schema assembly-necessity
    criterion. No relevant deletion/assembly experiment was independently checked;
    activity and intact inventory are not substituted for that evidence.
  evidence_ids:
  - sdh-agent-pdb-1NEK
  - sdh-agent-assembly-1NEK
  - sdh-agent-bdi-browser5
  - sdh-agent-bdi-stenberg-methods-search2
  - record
  - policy
- assessment_id: families
  area: grounding
  topic: Candidate families have non-equivalent boundaries
  outcome: supported
  target_ids:
  - GO:0045273
  summary: The existing label-only treatment is defensible for the stated full SdhA,
    SdhB and paired C/D scopes. IPR011281 is a narrower SdhA clade; IPR014006/030664
    and004489 are broader shared enzyme families; individual SdhC/D families do not
    ground the whole module. No global absence claim or requirement to split the paired
    row is made.
  evidence_ids:
  - sdh-agent-IPR011281
  - sdh-agent-IPR014006
  - sdh-agent-IPR030664
  - sdh-agent-IPR004489
  - sdh-agent-IPR014314
  - sdh-agent-IPR014312
  - sdh-agent-IPR065464
  - sdh-agent-matches-P0AC41
  - sdh-agent-matches-P07014
  - sdh-agent-matches-P69054
  - sdh-agent-matches-P0AC44
  - record
  - policy
- assessment_id: taxon
  area: scope
  topic: Species and strain contexts
  outcome: supported
  target_ids:
  - GO:0045273
  summary: The canonical crystallographic example is E.coli at species level and the
    exact protein examples are reviewed K-12 entries. Stenberg membrane proteomics
    uses BL21; the record cites UniProt location attribution rather than falsely assigning
    that preparation to K-12.
  evidence_ids:
  - sdh-agent-tax-562
  - sdh-agent-tax-83333
  - sdh-agent-P0AC41
  - sdh-agent-P07014
  - sdh-agent-P69054
  - sdh-agent-P0AC44
  - sdh-agent-1NEK-entity-1
  - sdh-agent-1NEK-entity-2
  - sdh-agent-1NEK-entity-3
  - sdh-agent-1NEK-entity-4
  - sdh-agent-bdi-stenberg-methods-search2
  - record
- assessment_id: reaction-graph
  area: graph
  topic: Coarse relay and structural ligand
  outcome: supported
  target_ids:
  - GO:0045273
  summary: The succinate/FAD/Fe-S/quinone relay and whole-complex GO activity are
    supported at the stated NONMECHANISTIC level. Native coordinates verify modeled
    ubiquinone-2, not quinone-reduction kinetics by an isolated C/D module. No proton-pumping,
    ROS mechanism, exact electron-transfer distance or higher-oligomer stoichiometry
    is asserted.
  evidence_ids:
  - sdh-agent-go
  - sdh-agent-P0AC41
  - sdh-agent-P07014
  - sdh-agent-P69054
  - sdh-agent-P0AC44
  - sdh-agent-pdb-1NEK
  - sdh-agent-1NEK-cif
  - sdh-agent-pmid-12560550
  - record
- assessment_id: provenance
  area: provenance
  topic: Exact source identity and readable scope
  outcome: supported
  target_ids:
  - GO:0045273
  summary: Yankovskaya2003, Stenberg2005 and Daley2005 identities match maintained
    citations. Native UniProt location evidence lists the exact maintained PMIDs;
    this attribution was checked directly. Only indexed claim-bearing Stenberg body
    excerpts were recovered; the complete Yankovskaya and Daley bodies were not read.
  evidence_ids:
  - sdh-agent-pmid-12560550
  - sdh-agent-pmid-15919996
  - sdh-agent-pmid-16079137
  - sdh-agent-P0AC41
  - sdh-agent-P07014
  - sdh-agent-P69054
  - sdh-agent-P0AC44
  - sdh-agent-bdi-browser5
  - sdh-agent-bdi-stenberg-methods-search2
  - record
- assessment_id: completeness
  area: completeness
  topic: Optional extensions and bounded unresolved evidence
  outcome: supported
  target_ids:
  - GO:0045273
  summary: Known protein membership is represented. Exact family refinements, added
    cofactors or stoichiometry, images and fuller mechanism are optional. Assembly-necessity
    support remains explicitly unresolved; no concrete contradictory assertion was
    established from the bounded sources.
  evidence_ids:
  - sdh-agent-go
  - sdh-agent-IPR011281
  - sdh-agent-IPR014006
  - sdh-agent-IPR030664
  - sdh-agent-IPR004489
  - sdh-agent-IPR014314
  - sdh-agent-IPR014312
  - sdh-agent-IPR065464
  - sdh-agent-assembly-1NEK
  - record
  - policy
findings: []
actions: []
limitations:
- ESSENTIAL means whether the structure forms without the component. Membership, catalytic
  role, a deposited complete structure and cell viability do not establish that claim;
  assembly necessity remains unverified for the three component rows.
- Yankovskaya2003 publisher/PDF access returned403; a university PDF candidate proved
  to be Lancaster1999 on a different fumarate reductase and was excluded. Yankovskaya
  support is therefore limited to exact native abstract, reviewed annotations and
  its actual1NEK deposit. Daley2005 was checked at metadata/abstract and UniProt-attribution
  level, not full body.
- Stenberg evidence is discontinuous indexed primary body with actual original access
  timestamps and status:null. A/B identification is distinct from C/D co-migration
  inference. Its BL21 preparation and inferred trimer do not override the species-level1NEK
  unit or K-12 example identities.
- Family scope is bounded to the complete integrated matches for four examples and
  the seven inspected family definitions. IPR011281 is a concrete narrower candidate,
  not proof that no exact broad family exists.
- Deposited ligand/assembly annotations were read without independent geometry, structure
  refinement or figure-pixel analysis. No new image, numerical property, source promotion
  or whole-paper access claim is made.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- All13 native inspection input hashes, focused checks0 and source raw/meta hashes
  verified. Scientific state and corpus remain unchanged.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
