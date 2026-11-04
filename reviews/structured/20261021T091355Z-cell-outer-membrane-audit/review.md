# Cell outer membrane identity, canonical barrier and assembly-mechanism scope review

- Review: 20261021T091355Z-cell-outer-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:51:09Z
- Finished UTC: 2026-10-21T09:13:55Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Outer-membrane identity, exact protein/location references and the canonical Gram-negative Lpt/BAM/barrier mechanisms are supported. Broader-envelope, representative-link, source-tier and assembly-necessity limits remain explicit; no concrete curation defect was established.

## Scope And Provenance

Entire single target; all native GO/location/chemical/taxon/protein identities and citation attributions; claim-bearing review body passages supporting both causal graphs, with noncanonical-envelope and assembly-necessity boundaries.

Selection: Tenth selected target in batch fourteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009279 | data/structures/envelope/cell_outer_membrane.yaml | maintained | cell outer membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0009279 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009279 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0009279 | 19 identifiers OK; 6 transport/skipped residuals independently resolved. |
| Native UniProt verify | passed | False | GO:0009279 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0009279 | Native command passed; scientific membership and graph scope assessed independently. |
| Claim-level scientific review | passed | True | GO:0009279 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0009279 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009279 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009279 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009279 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0009279 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Membrane identity and canonical qualifier

identity: supported. Targets: GO:0009279.

GO identity, membrane kind/parent and exact SL0040 mapping are supported. The definition explicitly confines phospholipid/LPS asymmetry to canonical Gram-negative bacteria while defining the larger diderm membrane class. It does not equate the membrane with a lipid molecule or protein cohort.

### Nonexclusive bacterial distribution

scope: supported. Targets: GO:0009279.

VARIABLE Bacteria presence and E.coli canonical scope are compatible with native taxonomy and review evidence. This is a nonexhaustive distribution, not a claim that all Bacteria have an outer membrane or that Archaea never do. Mycolic-acid and other noncanonical outer membranes are outside the mechanistic LPS/BAM example.

### Chemical and protein cohorts

evidence: supported. Targets: GO:0009279.

The LPS-rich leaflet and diverse beta-barrel cohort are supported constituents of the canonical example. OmpA/C/F and BamA are correctly paired reviewed K-12 proteins; porins and assembly proteins have different roles. The cohort spans multiple families, so no single protein-family grounding is forced.

### Collective beta-barrel ESSENTIAL claim

evidence: unknown. Targets: GO:0009279.

The source supports beta-barrel constituent membership and important transport/assembly functions. These facts do not establish that the defined membrane cannot form without the declared collective component under the schema assembly-necessity criterion. No appropriate collective depletion/assembly experiment was checked; neither essential cell viability nor individual OMP activity is substituted for this evidence.

### LPS is not universal to every outer membrane

scope: supported. Targets: GO:0009279.

CONDITIONAL LPS wording and the canonical Gram-negative definition are consistent with review examples of LPS-deficient viable bacteria and noncanonical mycolic-acid envelopes. This does not infer dispensability in E.coli from a different species.

### Lpt and BAM machinery with representative references

graph: supported. Targets: GO:0009279.

The graph correctly assigns LPS movement to the transenvelope Lpt machinery and beta-barrel assembly to BAM. P31554 is LptD, and the BAM accessions identify A/B/C/D members; these are correct representative constituent links, not complete machinery inventories or exact equivalences of each protein to the whole module. The schema allows protein complexes as causal nodes.

### Permeability is reduced rather than abolished

graph: supported. Targets: GO:0009279.

Ordered LPS and porins jointly support a selective barrier: hydrophobic lipid-phase diffusion is slow and porin passage depends on solute size/chemistry. Read with its explicit descriptions inhibits/slows/reducing, the excludes edge is not an absolute zero-influx assertion. The porin node names a subset of the broad component cohort; it does not make BamA a general diffusion porin.

### Direct database attribution versus primary body

provenance: supported. Targets: GO:0009279.

All maintained UniProt location-evidence PMIDs match native entry annotations and exact bibliographic metadata. The four main mechanistic citations are reviews and are retained at review tier. Individual location-study primary bodies were not independently read, so this assessment verifies attribution rather than claiming full experiment replication.

### Partial machinery links and optional enrichment

completeness: supported. Targets: GO:0009279.

The present record covers core canonical constituents, function and two bounded mechanisms. Full BAM/Lpt reference coverage, extra lipoprotein/phospholipid rows, additional taxa, images and numerical properties are optional. No concrete incorrect identifier or mechanism was established; assembly-necessity support and contextual generalization remain limitations.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/envelope/cell_outer_membrane.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| outer-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009279,GO:0016020; Complete two native term identities, definitions, synonyms/status and hierarchy | supports | Active GO0009279 denotes the cell outer membrane and GO0016020 the membrane parent. Native definitions distinguish the whole membrane from individual beta-barrel proteins. |
| outer-agent-sl-0040 | https://rest.uniprot.org/locations/SL-0040.json; Full native identity, definition, synonyms, isA and GO cross-reference | supports | Native UniProt location SL0040 is Cell outer membrane and explicitly maps to GO0009279. Its definition includes noncanonical bacterial and archaeal cases, so the record canonical Gram-negative qualifier matters. |
| outer-agent-chebi-16412 | https://www.ebi.ac.uk/chebi/backend/api/public/compound/16412/; Native accession, name, definition and synonyms | supports | CHEBI16412 identifies lipopolysaccharide and the LPS synonym used by chemical graph nodes. It does not identify an entire LPS-rich leaflet or all outer membranes. |
| outer-agent-tax-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete native identity, names, rank and lineage | supports | Native taxonomy confirms the maintained Bacteria2, E.coli562 and K-1283333 identities at their distinct ranks. |
| outer-agent-tax-562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native identity, names, rank and lineage | supports | Native taxonomy confirms the maintained Bacteria2, E.coli562 and K-1283333 identities at their distinct ranks. |
| outer-agent-tax-83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native identity, names, rank and lineage | supports | Native taxonomy confirms the maintained Bacteria2, E.coli562 and K-1283333 identities at their distinct ranks. |
| outer-agent-P0A910 | https://rest.uniprot.org/uniprotkb/P0A910.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0A910 identifies Outer membrane protein A, gene ompA, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| outer-agent-query-ompA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AompA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ompA, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0A910. This checks identifier resolution only. |
| outer-agent-P06996 | https://rest.uniprot.org/uniprotkb/P06996.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P06996 identifies Outer membrane porin C, gene ompC, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| outer-agent-query-ompC | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AompC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ompC, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P06996. This checks identifier resolution only. |
| outer-agent-P02931 | https://rest.uniprot.org/uniprotkb/P02931.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P02931 identifies Outer membrane porin F, gene ompF, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| outer-agent-query-ompF | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AompF%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ompF, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P02931. This checks identifier resolution only. |
| outer-agent-P0A940 | https://rest.uniprot.org/uniprotkb/P0A940.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0A940 identifies Outer membrane protein assembly factor BamA, gene bamA, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| outer-agent-query-bamA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AbamA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene bamA, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0A940. This checks identifier resolution only. |
| outer-agent-P31554 | https://rest.uniprot.org/uniprotkb/P31554.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P31554 identifies LPS-assembly protein LptD, gene lptD, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| outer-agent-query-lptD | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AlptD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene lptD, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P31554. This checks identifier resolution only. |
| outer-agent-P77774 | https://rest.uniprot.org/uniprotkb/P77774.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P77774 identifies Outer membrane protein assembly factor BamB, gene bamB, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| outer-agent-query-bamB | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AbamB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene bamB, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P77774. This checks identifier resolution only. |
| outer-agent-P0A903 | https://rest.uniprot.org/uniprotkb/P0A903.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0A903 identifies Outer membrane protein assembly factor BamC, gene bamC, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| outer-agent-query-bamC | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AbamC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene bamC, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0A903. This checks identifier resolution only. |
| outer-agent-P0AC02 | https://rest.uniprot.org/uniprotkb/P0AC02.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P0AC02 identifies Outer membrane protein assembly factor BamD, gene bamD, taxon83333. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| outer-agent-query-bamD | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AbamD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene bamD, organism83333, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P0AC02. This checks identifier resolution only. |
| outer-agent-matches-P0A910 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A910/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| outer-agent-matches-P06996 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P06996/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| outer-agent-matches-P02931 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P02931/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| outer-agent-matches-P0A940 | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A940/?page_size=200; All returned results; native pagination next is null | context_only | Complete integrated InterPro matches for this exact reviewed example were inspected to bound candidate selection. Matching a family or domain does not alone establish exact equivalence to the maintained component. |
| outer-agent-pmid-10636850 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:10636850%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Refolded outer membrane protein A of Escherichia coli forms ion channels with two conductance states in planar lipid bilayers. Authors: Arora A, Rinehart D, Szabo G, Tamm LK.; PMID 10636850; DOI 10.1074/jbc.275.3.1594. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-pmid-10947984 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:10947984%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Degradation of outer membrane protein A in Escherichia coli killing by neutrophil elastase. Authors: Belaaouaj A, Kim KS, Shapiro SD.; PMID 10947984; DOI 10.1126/science.289.5482.1185. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-pmid-16079137 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:16079137%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Protein complexes of the Escherichia coli cell envelope. Authors: Stenberg F, Chovanec P, Maslen SL, Robinson CV, Ilag LL, von Heijne G, Daley DO.; PMID 16079137; DOI 10.1074/jbc.m506479200. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-pmid-23882017 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:23882017%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Receptor polymorphism restricts contact-dependent growth inhibition to members of the same species. Authors: Ruhe ZC, Wallace AB, Low DA, Hayes CS.; PMID 23882017; DOI 10.1128/mbio.00480-13. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-pmid-24619089 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:24619089%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Structural and functional analysis of the β-barrel domain of BamA from Escherichia coli. Authors: Ni D, Wang Y, Yang X, Zhou H, Hou X, Cao B, Lu Z, Zhao X, Yang K, Huang Y.; PMID 24619089; DOI 10.1096/fj.13-248450. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-pmid-2464593 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:2464593%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Existence and purification of porin heterotrimers of Escherichia coli K12 OmpC, OmpF, and PhoE proteins. Authors: Gehring KB, Nikaido H.; PMID 2464593; DOI 10.1016/s0021-9258(19)81685-x. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-doi-cshperspect_a000414 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1101/cshperspect.a000414; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The bacterial cell envelope. Authors: Silhavy TJ, Kahne D, Walker S.; PMID 20452953; DOI 10.1101/cshperspect.a000414. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-doi-jbc_R117_802512 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1074/jbc.R117.802512; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The lipopolysaccharide transport (Lpt) machinery: A nonconventional transporter for lipopolysaccharide assembly at the outer membrane of Gram-negative bacteria. Authors: Sperandeo P, Martorana AM, Polissi A.; PMID 28878019; DOI 10.1074/jbc.r117.802512. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-doi-annurev-biochem-061408-144611 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev-biochem-061408-144611; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies β-Barrel membrane protein assembly by the Bam complex. Authors: Hagan CL, Silhavy TJ, Kahne D.; PMID 21370981; DOI 10.1146/annurev-biochem-061408-144611. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-doi-MMBR_67_4_593-656_2003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/MMBR.67.4.593-656.2003; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Molecular basis of bacterial outer membrane permeability revisited. Authors: Nikaido H.; PMID 14665678; DOI 10.1128/mmbr.67.4.593-656.2003. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| outer-agent-silhavy2010-legacy-html | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2857177/; Genuine PMC2857177 HTML: abstract/Introduction; s1a The Outer Membrane; s1e Transenvelope Machines; claim-bearing BAM/Lpt paragraphs in s1f Envelope Biogenesis; s3 Corynebacterineae. These sections/passages were read, not a full primary experimental audit. | supports | Silhavy2010 is a review. It supports canonical Gram-negative phospholipid/LPS asymmetry, beta-barrel proteins and porins, envelope assembly and permeability. Its Corynebacterineae section explicitly describes a different mycolic-acid outer membrane, preventing universal LPS/BAM extrapolation. |
| outer-agent-sperandeo2017-legacy-html | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5672026/; Genuine PMC5672026 HTML: sec1 Introduction, sec2 LPS structure/functions, sec4 MsbA, sec5 Lpt machinery, sec6 detachment, sec7 bridge and sec8 insertion; relevant Figure2/3 captions. No claim of independently repeating the underlying transport experiments. | supports | Sperandeo2017 is a review of the Gram-negative Lpt machine. It distinguishes MsbA flipping from Lpt extraction/transport and LptDE outer-membrane insertion. LPS-deficient viable bacterial examples and species differences are explicitly described. |
| outer-agent-hagan2011-pdf | https://prokaryotics.com/wp-content/uploads/2017/02/Hagan-et-al-2011.pdf; Actual public PDF: title/abstract and Introduction context; pp194–196 Identification of Assembly Machinery; pp200–201 substrate folding and OmpT reconstitution account; pp202–204 substrate insertion/model/conclusion. Text read; no figure-pixel or original experimental-data reanalysis. | supports | Hagan2011 is a review. The five-subunit E.coli BAM machine facilitates beta-barrel folding/insertion; reconstituted OmpT assembly supports the coarse functional claim, while detailed mechanisms and turnover remain unresolved in the source. |
| outer-agent-nikaido2003-browser1 | https://pmc.ncbi.nlm.nih.gov/articles/PMC309051; Indexed PMC309051 review, Introduction and Classical Porins lines62–113; second returned LamB/ScrY/OprD excerpt is ancillary, not used for extra claims. No native HTTP200 inferred. | supports | Nikaido2003 is a review. Its Introduction and classical-porin discussion support limited hydrophilic diffusion through channels and joint dependence on membrane/barrier properties. |
| outer-agent-nikaido2003-browser2 | https://pmc.ncbi.nlm.nih.gov/articles/PMC309051/; Indexed review lines668–734: Lipid Bilayer as a Diffusion Barrier, Asymmetric Bilayer, General LPS Structure and Low Fluidity. Exact browser access time retained. | supports | Nikaido2003 reviews asymmetric LPS bilayers and low lipid fluidity as causes of slow lipophilic influx. Apparent impermeability can also depend on active efflux; exclusion is not absolute inability of every hydrophobic compound to enter. |
| schema-result | just validate data/structures/envelope/cell_outer_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/envelope/cell_outer_membrane.yaml |
| strict-result | just validate-strict data/structures/envelope/cell_outer_membrane.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/cell_outer_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/envelope/cell_outer_membrane.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/cell_outer_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/cell_outer_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/envelope/cell_outer_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 19 of25 collected target identifiers returned OK at the unchanged base. Residuals: PMID:10636850: UNREACHABLE; resolved by evidence outer-agent-pmid-10636850; PMID:10947984: UNREACHABLE; resolved by evidence outer-agent-pmid-10947984; PMID:16079137: UNREACHABLE; resolved by evidence outer-agent-pmid-16079137; PMID:23882017: UNREACHABLE; resolved by evidence outer-agent-pmid-23882017; PMID:24619089: UNREACHABLE; resolved by evidence outer-agent-pmid-24619089; PMID:2464593: UNREACHABLE; resolved by evidence outer-agent-pmid-2464593. Source-native identity checked separately. |
| native-verify | /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/cell_outer_membrane.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/envelope/cell_outer_membrane.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/envelope/cell_outer_membrane.yaml  (GO:0009279)<br>  lps_bam_outer_membrane_barrier	lpt_machine	UNANCHORED_WITH_UNIPROT	Lpt transenvelope LPS transport machine (UniProtKB:P31554)<br>  lps_bam_outer_membrane_barrier	bam_complex	UNANCHORED_WITH_UNIPROT	beta-barrel assembly machinery complex (UniProtKB:P0A940, UniProtKB:P77774, UniProtKB:P0A903, UniProtKB:P0AC02)<br>  lps_bam_outer_membrane_barrier	outer_membrane_beta_barrels	COVERED	-&gt;outer_membrane_beta_barrels (UniProtKB:P0A910, UniProtKB:P06996, UniProtKB:P02931, UniProtKB:P0A940)<br>  lps_porin_selective_permeability	beta_barrel_porins	COVERED	-&gt;outer_membrane_beta_barrels (UniProtKB:P0A910, UniProtKB:P06996, UniProtKB:P02931, UniProtKB:P0A940)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     2  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The collective beta-barrel ESSENTIAL annotation concerns whether the structure forms without the component, not membership, transport activity or cell viability. The reviewed evidence does not independently establish that assembly-necessity assertion.
- The two mechanistic graphs describe the canonical LPS-rich Gram-negative case established by their references; the broader cell-outer-membrane identity also includes noncanonical envelopes. The definition and conditional LPS row provide that context, and no universal LPS/BAM mechanism is inferred.
- Lpt graph xrefs cover LptD only and BAM xrefs cover A/B/C/D, omitting other constituents. These are partial representative links, not complete inventories. The porin node is narrower than the generic beta-barrel component cohort.
- Silhavy, Sperandeo, Hagan and Nikaido are reviews. The specified native body passages and indexed Nikaido excerpts were read; primary experiments underlying every mechanism and the individual UniProt location studies were not independently audited. Exact location-evidence attribution was checked against UniProt and native metadata.
- Nikaido native routes returned challenge HTML, JATS500 or S3 errors; usable indexed review excerpts were recovered with exact status:null receipts. Hagan was a genuine PDF, and Silhavy/Sperandeo genuine legacy PMC HTML. Failed responses are preserved and not counted as readable bodies.
- Exclusion means reduced lipid-phase influx in this context; active efflux and species/preparation differences also affect measured accumulation. No quantitative permeability constant, universal pore cutoff, exact gene essentiality or atomic assembly sequence is asserted.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All13 native inspection input hashes, focused gates0 and source receipts verified. No scientific edits or mapping-status promotion.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091355Z-cell-outer-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cell outer membrane identity, canonical barrier and assembly-mechanism scope
  review
started_at: '2026-10-21T08:51:09Z'
finished_at: '2026-10-21T09:13:55Z'
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
summary: Outer-membrane identity, exact protein/location references and the canonical
  Gram-negative Lpt/BAM/barrier mechanisms are supported. Broader-envelope, representative-link,
  source-tier and assembly-necessity limits remain explicit; no concrete curation
  defect was established.
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
  - path: data/structures/envelope/cell_outer_membrane.yaml
    sha256: 6a21a7409a3e93aa290cbff61f4734629b927f04a33c469e6166ef1b24673fab
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
- target_id: GO:0009279
  path: data/structures/envelope/cell_outer_membrane.yaml
  label: cell outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/envelope/cell_outer_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire single target; all native GO/location/chemical/taxon/protein
    identities and citation attributions; claim-bearing review body passages supporting
    both causal graphs, with noncanonical-envelope and assembly-necessity boundaries.
  selection: Tenth selected target in batch fourteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009279
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009279
  command: just validate data/structures/envelope/cell_outer_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009279
  command: just validate-strict data/structures/envelope/cell_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/cell_outer_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0009279
  summary: 19 identifiers OK; 6 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - outer-agent-pmid-10636850
  - outer-agent-pmid-10947984
  - outer-agent-pmid-16079137
  - outer-agent-pmid-23882017
  - outer-agent-pmid-24619089
  - outer-agent-pmid-2464593
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0009279
  command: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/cell_outer_membrane.yaml
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
  - GO:0009279
  command: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/cell_outer_membrane.yaml
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
  - GO:0009279
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - outer-agent-go
  - outer-agent-sl-0040
  - outer-agent-chebi-16412
  - outer-agent-tax-2
  - outer-agent-tax-562
  - outer-agent-tax-83333
  - outer-agent-P0A910
  - outer-agent-query-ompA
  - outer-agent-P06996
  - outer-agent-query-ompC
  - outer-agent-P02931
  - outer-agent-query-ompF
  - outer-agent-P0A940
  - outer-agent-query-bamA
  - outer-agent-P31554
  - outer-agent-query-lptD
  - outer-agent-P77774
  - outer-agent-query-bamB
  - outer-agent-P0A903
  - outer-agent-query-bamC
  - outer-agent-P0AC02
  - outer-agent-query-bamD
  - outer-agent-matches-P0A910
  - outer-agent-matches-P06996
  - outer-agent-matches-P02931
  - outer-agent-matches-P0A940
  - outer-agent-pmid-10636850
  - outer-agent-pmid-10947984
  - outer-agent-pmid-16079137
  - outer-agent-pmid-23882017
  - outer-agent-pmid-24619089
  - outer-agent-pmid-2464593
  - outer-agent-doi-cshperspect_a000414
  - outer-agent-doi-jbc_R117_802512
  - outer-agent-doi-annurev-biochem-061408-144611
  - outer-agent-doi-MMBR_67_4_593-656_2003
  - outer-agent-silhavy2010-legacy-html
  - outer-agent-sperandeo2017-legacy-html
  - outer-agent-hagan2011-pdf
  - outer-agent-nikaido2003-browser1
  - outer-agent-nikaido2003-browser2
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009279
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
  - GO:0009279
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
  - GO:0009279
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
  - GO:0009279
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
  - GO:0009279
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
  reference: data/structures/envelope/cell_outer_membrane.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T09:12:56Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:12:56Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: outer-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009279,GO:0016020
  locator: Complete two native term identities, definitions, synonyms/status and hierarchy
  accessed_at: '2026-10-21T09:01:33.152632Z'
  support: supports
  summary: Active GO0009279 denotes the cell outer membrane and GO0016020 the membrane
    parent. Native definitions distinguish the whole membrane from individual beta-barrel
    proteins.
  snapshot_sha256: 4dab2fbd6cdf3233f76bc8d2da58dabff083fa6204c95a319289c6c61a318372
- evidence_id: outer-agent-sl-0040
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0040.json
  locator: Full native identity, definition, synonyms, isA and GO cross-reference
  accessed_at: '2026-10-21T09:01:41.320949Z'
  support: supports
  summary: Native UniProt location SL0040 is Cell outer membrane and explicitly maps
    to GO0009279. Its definition includes noncanonical bacterial and archaeal cases,
    so the record canonical Gram-negative qualifier matters.
  snapshot_sha256: 8a16f96e1b81277a31e7eb3c3384cb13f7786c94b59dcb95424bdeb5bb14a7d9
- evidence_id: outer-agent-chebi-16412
  kind: database
  reference: https://www.ebi.ac.uk/chebi/backend/api/public/compound/16412/
  locator: Native accession, name, definition and synonyms
  accessed_at: '2026-10-21T09:01:41.316798Z'
  support: supports
  summary: CHEBI16412 identifies lipopolysaccharide and the LPS synonym used by chemical
    graph nodes. It does not identify an entire LPS-rich leaflet or all outer membranes.
  snapshot_sha256: 1761021018cb0217a35ea9c6f9b5593f27e56c2c7d406dbeeb24f6870b43e940
- evidence_id: outer-agent-tax-2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete native identity, names, rank and lineage
  accessed_at: '2026-10-21T09:01:33.217730Z'
  support: supports
  summary: Native taxonomy confirms the maintained Bacteria2, E.coli562 and K-1283333
    identities at their distinct ranks.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: outer-agent-tax-562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native identity, names, rank and lineage
  accessed_at: '2026-10-21T09:01:33.281042Z'
  support: supports
  summary: Native taxonomy confirms the maintained Bacteria2, E.coli562 and K-1283333
    identities at their distinct ranks.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: outer-agent-tax-83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native identity, names, rank and lineage
  accessed_at: '2026-10-21T09:01:33.329421Z'
  support: supports
  summary: Native taxonomy confirms the maintained Bacteria2, E.coli562 and K-1283333
    identities at their distinct ranks.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: outer-agent-P0A910
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A910.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:34.572641Z'
  support: supports
  summary: Native reviewed UniProtKB P0A910 identifies Outer membrane protein A, gene
    ompA, taxon83333. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: f9c3d1a94ebd004e99060766ee6a38dd5cd3600b57586db84e3fc1a9d59bf0f8
- evidence_id: outer-agent-query-ompA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ompA, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:17.086097Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0A910. This checks identifier
    resolution only.
  snapshot_sha256: 6d5afaa99881ccc27553912308248a0ae9a68d686e019b97fa3fdb9ec3dc47aa
  search_scope: UniProtKB query gene_exact:ompA AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: outer-agent-P06996
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P06996.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:33.826728Z'
  support: supports
  summary: Native reviewed UniProtKB P06996 identifies Outer membrane porin C, gene
    ompC, taxon83333. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 54a36b2e065d96b31213df239cf617c89b616f16f030f303ee548d7fe56dc9c8
- evidence_id: outer-agent-query-ompC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ompC, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:17.405968Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P06996. This checks identifier
    resolution only.
  snapshot_sha256: 3427cbb25176813fe2877ce6da2675d0931c673339c36b58af3fc4340ff9f14b
  search_scope: UniProtKB query gene_exact:ompC AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: outer-agent-P02931
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P02931.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:33.427159Z'
  support: supports
  summary: Native reviewed UniProtKB P02931 identifies Outer membrane porin F, gene
    ompF, taxon83333. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 2579d79d43b13c340905e07df7efed1871c19dbe5a67eb133857f2d6e4df8a50
- evidence_id: outer-agent-query-ompF
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AompF%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ompF, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:17.645675Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P02931. This checks identifier
    resolution only.
  snapshot_sha256: ec6003b929dd8d0601b31f254d76acbff398acbd4cd7def61df3f1327ba18820
  search_scope: UniProtKB query gene_exact:ompF AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: outer-agent-P0A940
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A940.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:35.321755Z'
  support: supports
  summary: Native reviewed UniProtKB P0A940 identifies Outer membrane protein assembly
    factor BamA, gene bamA, taxon83333. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: 2ff846ae12669c4bab0ccd5ee26ee045bc2c77b2c49c18bfcf90adaee3a2296d
- evidence_id: outer-agent-query-bamA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene bamA, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:17.710525Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0A940. This checks identifier
    resolution only.
  snapshot_sha256: eedefca132b33d6adebab88357ec41c7c549af0160a80fe342ec9c5c2ed76809
  search_scope: UniProtKB query gene_exact:bamA AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: outer-agent-P31554
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31554.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:37.124106Z'
  support: supports
  summary: Native reviewed UniProtKB P31554 identifies LPS-assembly protein LptD,
    gene lptD, taxon83333. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: dbab992a253dc68cd2b7543da5236b46111557f1f37b9fdd619b4b81794bf178
- evidence_id: outer-agent-query-lptD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AlptD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene lptD, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:18.542922Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P31554. This checks identifier
    resolution only.
  snapshot_sha256: 1cefffb7d372496094e05d2fcba958a834d1b35316006f0c3e13d60d143c15e5
  search_scope: UniProtKB query gene_exact:lptD AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: outer-agent-P77774
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P77774.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:37.410628Z'
  support: supports
  summary: Native reviewed UniProtKB P77774 identifies Outer membrane protein assembly
    factor BamB, gene bamB, taxon83333. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: 2ef03b2f0a01756551013ff513ba85409096bdb8d13b57be1991bd465d1376e1
- evidence_id: outer-agent-query-bamB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene bamB, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:17.829174Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P77774. This checks identifier
    resolution only.
  snapshot_sha256: a5fb6bdb8a6d22d3789192420f7891e4f381de850cf4cc724acdffe4383b890e
  search_scope: UniProtKB query gene_exact:bamB AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: outer-agent-P0A903
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A903.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:33.930781Z'
  support: supports
  summary: Native reviewed UniProtKB P0A903 identifies Outer membrane protein assembly
    factor BamC, gene bamC, taxon83333. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: 584c056225b866005264ce4b2288722d06ff5adf60d6f217a65b59e6b0c22c60
- evidence_id: outer-agent-query-bamC
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamC%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene bamC, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:18.403993Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0A903. This checks identifier
    resolution only.
  snapshot_sha256: 073444923c46fbd03e5e35ea4c1d56f51a2e76205a35aee6e9b0d426378fd5f4
  search_scope: UniProtKB query gene_exact:bamC AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: outer-agent-P0AC02
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0AC02.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:01:36.183382Z'
  support: supports
  summary: Native reviewed UniProtKB P0AC02 identifies Outer membrane protein assembly
    factor BamD, gene bamD, taxon83333. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: 97262e786c9e1d055dd17acbcc26d085df95a8e0206f10d3ad247dc545a4902b
- evidence_id: outer-agent-query-bamD
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AbamD%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene bamD, organism83333, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:05:18.445429Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P0AC02. This checks identifier
    resolution only.
  snapshot_sha256: 3863cd5db0a7c555cf2dba77d3a52ae3a8ebd3681a6821e8628e854c010497ca
  search_scope: UniProtKB query gene_exact:bamD AND organism_id:83333 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: outer-agent-matches-P0A910
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A910/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T09:01:34.574573Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: 0ec8cef330188977db2d695ed1bff88c43fa4dd7213eb2846cb058f488170496
- evidence_id: outer-agent-matches-P06996
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P06996/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T09:01:33.904203Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: 282f81594e0478ea33a48528727a19876beac6498ca177039e369a11e13a4cdb
- evidence_id: outer-agent-matches-P02931
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P02931/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T09:01:33.745859Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: fe51a1dea6b6cce726ced25038d8a4ff0291fccc15352e2b67c7d87dcf93f6c2
- evidence_id: outer-agent-matches-P0A940
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P0A940/?page_size=200
  locator: All returned results; native pagination next is null
  accessed_at: '2026-10-21T09:01:36.097176Z'
  support: context_only
  summary: Complete integrated InterPro matches for this exact reviewed example were
    inspected to bound candidate selection. Matching a family or domain does not alone
    establish exact equivalence to the maintained component.
  snapshot_sha256: 3ef38d21a63df56c8548383507aa702e5e0eb353bd04a67d3e7e6b2503ed5fc6
- evidence_id: outer-agent-pmid-10636850
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:10636850%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:38.093537Z'
  support: supports
  summary: 'Native metadata identifies Refolded outer membrane protein A of Escherichia
    coli forms ion channels with two conductance states in planar lipid bilayers.
    Authors: Arora A, Rinehart D, Szabo G, Tamm LK.; PMID 10636850; DOI 10.1074/jbc.275.3.1594.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 6c68a6c4a20af32afa2878e1f9c0c3ae3aa5af483c997ac4e416d0c758eca9bd
- evidence_id: outer-agent-pmid-10947984
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:10947984%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:38.133507Z'
  support: supports
  summary: 'Native metadata identifies Degradation of outer membrane protein A in
    Escherichia coli killing by neutrophil elastase. Authors: Belaaouaj A, Kim KS,
    Shapiro SD.; PMID 10947984; DOI 10.1126/science.289.5482.1185. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 383bd5a0a51ffe979496ed1e2085e081ed4ca102157d6c53b9e65456207f5e8f
- evidence_id: outer-agent-pmid-16079137
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:16079137%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:38.537173Z'
  support: supports
  summary: 'Native metadata identifies Protein complexes of the Escherichia coli cell
    envelope. Authors: Stenberg F, Chovanec P, Maslen SL, Robinson CV, Ilag LL, von
    Heijne G, Daley DO.; PMID 16079137; DOI 10.1074/jbc.m506479200. Bibliographic
    identity and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 0c8a782dd1022fdd5016d2f9b2ca9cdb04e46072105f4233ec07edeff9af1d38
- evidence_id: outer-agent-pmid-23882017
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:23882017%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:38.747909Z'
  support: supports
  summary: 'Native metadata identifies Receptor polymorphism restricts contact-dependent
    growth inhibition to members of the same species. Authors: Ruhe ZC, Wallace AB,
    Low DA, Hayes CS.; PMID 23882017; DOI 10.1128/mbio.00480-13. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: d1fc76a41efb3d14a5349774a16b7033c4200c9fb052b648065a170ed65738a5
- evidence_id: outer-agent-pmid-24619089
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:24619089%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:38.771684Z'
  support: supports
  summary: 'Native metadata identifies Structural and functional analysis of the β-barrel
    domain of BamA from Escherichia coli. Authors: Ni D, Wang Y, Yang X, Zhou H, Hou
    X, Cao B, Lu Z, Zhao X, Yang K, Huang Y.; PMID 24619089; DOI 10.1096/fj.13-248450.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 3bf39231ef314853e692c8623395a61975e81ced049781a81fa178ed3ef25824
- evidence_id: outer-agent-pmid-2464593
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:2464593%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:39.135555Z'
  support: supports
  summary: 'Native metadata identifies Existence and purification of porin heterotrimers
    of Escherichia coli K12 OmpC, OmpF, and PhoE proteins. Authors: Gehring KB, Nikaido
    H.; PMID 2464593; DOI 10.1016/s0021-9258(19)81685-x. Bibliographic identity and
    available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 0e12629ff3fa85f38336a4940f54b4f000651afcd6a0a08eeef91b97438edc55
- evidence_id: outer-agent-doi-cshperspect_a000414
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1101/cshperspect.a000414
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:39.409675Z'
  support: supports
  summary: 'Native metadata identifies The bacterial cell envelope. Authors: Silhavy
    TJ, Kahne D, Walker S.; PMID 20452953; DOI 10.1101/cshperspect.a000414. Bibliographic
    identity and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 6dbe4b87edaa5c136c12c86c9d1dd160a184f8e75b68e56095dcffb08d567992
- evidence_id: outer-agent-doi-jbc_R117_802512
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074/jbc.R117.802512
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:39.180486Z'
  support: supports
  summary: 'Native metadata identifies The lipopolysaccharide transport (Lpt) machinery:
    A nonconventional transporter for lipopolysaccharide assembly at the outer membrane
    of Gram-negative bacteria. Authors: Sperandeo P, Martorana AM, Polissi A.; PMID
    28878019; DOI 10.1074/jbc.r117.802512. Bibliographic identity and available abstract
    only; not a substitute for inspected article body.'
  snapshot_sha256: 55f94a1127687fe39ee92f7bd4b5348342f2228f5f847a5aadbfc58a244b6146
- evidence_id: outer-agent-doi-annurev-biochem-061408-144611
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev-biochem-061408-144611
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:39.752321Z'
  support: supports
  summary: 'Native metadata identifies β-Barrel membrane protein assembly by the Bam
    complex. Authors: Hagan CL, Silhavy TJ, Kahne D.; PMID 21370981; DOI 10.1146/annurev-biochem-061408-144611.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: be4205eb65a0241ddbc4687ca5bf57ab17430701bda1bcb10c4ef819304caa0b
- evidence_id: outer-agent-doi-MMBR_67_4_593-656_2003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/MMBR.67.4.593-656.2003
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:39.410437Z'
  support: supports
  summary: 'Native metadata identifies Molecular basis of bacterial outer membrane
    permeability revisited. Authors: Nikaido H.; PMID 14665678; DOI 10.1128/mmbr.67.4.593-656.2003.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: c84f43596bae4ea42f992fa8627c1db390ed2c9640e41223452b4317ad6aff55
- evidence_id: outer-agent-silhavy2010-legacy-html
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2857177/
  locator: 'Genuine PMC2857177 HTML: abstract/Introduction; s1a The Outer Membrane;
    s1e Transenvelope Machines; claim-bearing BAM/Lpt paragraphs in s1f Envelope Biogenesis;
    s3 Corynebacterineae. These sections/passages were read, not a full primary experimental
    audit.'
  accessed_at: '2026-10-21T09:03:55.797283Z'
  support: supports
  summary: Silhavy2010 is a review. It supports canonical Gram-negative phospholipid/LPS
    asymmetry, beta-barrel proteins and porins, envelope assembly and permeability.
    Its Corynebacterineae section explicitly describes a different mycolic-acid outer
    membrane, preventing universal LPS/BAM extrapolation.
  snapshot_sha256: 734e73fa7aafdfe44d5c447f32a07431c543b374d715a519947ee42c6b388c28
- evidence_id: outer-agent-sperandeo2017-legacy-html
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5672026/
  locator: 'Genuine PMC5672026 HTML: sec1 Introduction, sec2 LPS structure/functions,
    sec4 MsbA, sec5 Lpt machinery, sec6 detachment, sec7 bridge and sec8 insertion;
    relevant Figure2/3 captions. No claim of independently repeating the underlying
    transport experiments.'
  accessed_at: '2026-10-21T09:03:55.798848Z'
  support: supports
  summary: Sperandeo2017 is a review of the Gram-negative Lpt machine. It distinguishes
    MsbA flipping from Lpt extraction/transport and LptDE outer-membrane insertion.
    LPS-deficient viable bacterial examples and species differences are explicitly
    described.
  snapshot_sha256: 431a875a3dbab5775c83f9bc3612bf69e05a0656e094efedad4e87e99feb1ef8
- evidence_id: outer-agent-hagan2011-pdf
  kind: authority
  reference: https://prokaryotics.com/wp-content/uploads/2017/02/Hagan-et-al-2011.pdf
  locator: 'Actual public PDF: title/abstract and Introduction context; pp194–196
    Identification of Assembly Machinery; pp200–201 substrate folding and OmpT reconstitution
    account; pp202–204 substrate insertion/model/conclusion. Text read; no figure-pixel
    or original experimental-data reanalysis.'
  accessed_at: '2026-10-21T09:02:58.737224Z'
  support: supports
  summary: Hagan2011 is a review. The five-subunit E.coli BAM machine facilitates
    beta-barrel folding/insertion; reconstituted OmpT assembly supports the coarse
    functional claim, while detailed mechanisms and turnover remain unresolved in
    the source.
  snapshot_sha256: 669fe7858117af4b8e258e732d00b1e47af168cf23a6c3665a027f1232d59276
- evidence_id: outer-agent-nikaido2003-browser1
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC309051
  locator: Indexed PMC309051 review, Introduction and Classical Porins lines62–113;
    second returned LamB/ScrY/OprD excerpt is ancillary, not used for extra claims.
    No native HTTP200 inferred.
  accessed_at: '2026-10-21T09:06:08Z'
  support: supports
  summary: Nikaido2003 is a review. Its Introduction and classical-porin discussion
    support limited hydrophilic diffusion through channels and joint dependence on
    membrane/barrier properties.
  snapshot_sha256: 83041f617738cd36d69737a794e9ff38abcb85d5492204ae5e6025a8faaeebcc
- evidence_id: outer-agent-nikaido2003-browser2
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC309051/
  locator: 'Indexed review lines668–734: Lipid Bilayer as a Diffusion Barrier, Asymmetric
    Bilayer, General LPS Structure and Low Fluidity. Exact browser access time retained.'
  accessed_at: '2026-10-21T09:06:26Z'
  support: supports
  summary: Nikaido2003 reviews asymmetric LPS bilayers and low lipid fluidity as causes
    of slow lipophilic influx. Apparent impermeability can also depend on active efflux;
    exclusion is not absolute inability of every hydrophobic compound to enter.
  snapshot_sha256: 40e1e64bd6fc6ebbac4496deb0eec288bb1b5fffe781175162fa48d80b0c1d02
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/envelope/cell_outer_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:51:15Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/envelope/cell_outer_membrane.yaml'
  snapshot_sha256: fd479f7c947141a7a82909563c232e65f987755ae01f3c445b2f1f9bc5eb4ea4
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/envelope/cell_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/cell_outer_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:51:19Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/envelope/cell_outer_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch14-20261021-g0felisv/cell_outer_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/cell_outer_membrane-strict.tsv"
  snapshot_sha256: 0697115ac0b9c251fc1ab30741f7e6579b90dfd3555295d2cae9675802ba421c
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/envelope/cell_outer_membrane.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:12:56Z'
  support: supports
  summary: '19 of25 collected target identifiers returned OK at the unchanged base.
    Residuals: PMID:10636850: UNREACHABLE; resolved by evidence outer-agent-pmid-10636850;
    PMID:10947984: UNREACHABLE; resolved by evidence outer-agent-pmid-10947984; PMID:16079137:
    UNREACHABLE; resolved by evidence outer-agent-pmid-16079137; PMID:23882017: UNREACHABLE;
    resolved by evidence outer-agent-pmid-23882017; PMID:24619089: UNREACHABLE; resolved
    by evidence outer-agent-pmid-24619089; PMID:2464593: UNREACHABLE; resolved by
    evidence outer-agent-pmid-2464593. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/cell_outer_membrane.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T09:01:33.832066Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch14-20261021-g0felisv/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/envelope/cell_outer_membrane.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T09:01:35.739149Z'
  support: supports
  summary: "data/structures/envelope/cell_outer_membrane.yaml  (GO:0009279)\n  lps_bam_outer_membrane_barrier\t\
    lpt_machine\tUNANCHORED_WITH_UNIPROT\tLpt transenvelope LPS transport machine\
    \ (UniProtKB:P31554)\n  lps_bam_outer_membrane_barrier\tbam_complex\tUNANCHORED_WITH_UNIPROT\t\
    beta-barrel assembly machinery complex (UniProtKB:P0A940, UniProtKB:P77774, UniProtKB:P0A903,\
    \ UniProtKB:P0AC02)\n  lps_bam_outer_membrane_barrier\touter_membrane_beta_barrels\t\
    COVERED\t->outer_membrane_beta_barrels (UniProtKB:P0A910, UniProtKB:P06996, UniProtKB:P02931,\
    \ UniProtKB:P0A940)\n  lps_porin_selective_permeability\tbeta_barrel_porins\t\
    COVERED\t->outer_membrane_beta_barrels (UniProtKB:P0A910, UniProtKB:P06996, UniProtKB:P02931,\
    \ UniProtKB:P0A940)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     2  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries\
    \ a UniProtKB grounding or xref\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     4\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 87b37b47801767dd2839a3b62e9d840fcbf3123db8bf19c31e9660ca4d0daadd
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
  topic: Membrane identity and canonical qualifier
  outcome: supported
  target_ids:
  - GO:0009279
  summary: GO identity, membrane kind/parent and exact SL0040 mapping are supported.
    The definition explicitly confines phospholipid/LPS asymmetry to canonical Gram-negative
    bacteria while defining the larger diderm membrane class. It does not equate the
    membrane with a lipid molecule or protein cohort.
  evidence_ids:
  - outer-agent-go
  - outer-agent-sl-0040
  - outer-agent-silhavy2010-legacy-html
  - record
- assessment_id: taxon
  area: scope
  topic: Nonexclusive bacterial distribution
  outcome: supported
  target_ids:
  - GO:0009279
  summary: VARIABLE Bacteria presence and E.coli canonical scope are compatible with
    native taxonomy and review evidence. This is a nonexhaustive distribution, not
    a claim that all Bacteria have an outer membrane or that Archaea never do. Mycolic-acid
    and other noncanonical outer membranes are outside the mechanistic LPS/BAM example.
  evidence_ids:
  - outer-agent-tax-2
  - outer-agent-tax-562
  - outer-agent-tax-83333
  - outer-agent-silhavy2010-legacy-html
  - outer-agent-sl-0040
  - record
- assessment_id: composition
  area: evidence
  topic: Chemical and protein cohorts
  outcome: supported
  target_ids:
  - GO:0009279
  summary: The LPS-rich leaflet and diverse beta-barrel cohort are supported constituents
    of the canonical example. OmpA/C/F and BamA are correctly paired reviewed K-12
    proteins; porins and assembly proteins have different roles. The cohort spans
    multiple families, so no single protein-family grounding is forced.
  evidence_ids:
  - outer-agent-chebi-16412
  - outer-agent-P0A910
  - outer-agent-P06996
  - outer-agent-P02931
  - outer-agent-P0A940
  - outer-agent-P31554
  - outer-agent-P77774
  - outer-agent-P0A903
  - outer-agent-P0AC02
  - outer-agent-matches-P0A910
  - outer-agent-matches-P06996
  - outer-agent-matches-P02931
  - outer-agent-matches-P0A940
  - outer-agent-silhavy2010-legacy-html
  - record
- assessment_id: assembly-necessity
  area: evidence
  topic: Collective beta-barrel ESSENTIAL claim
  outcome: unknown
  target_ids:
  - GO:0009279
  summary: The source supports beta-barrel constituent membership and important transport/assembly
    functions. These facts do not establish that the defined membrane cannot form
    without the declared collective component under the schema assembly-necessity
    criterion. No appropriate collective depletion/assembly experiment was checked;
    neither essential cell viability nor individual OMP activity is substituted for
    this evidence.
  evidence_ids:
  - outer-agent-silhavy2010-legacy-html
  - outer-agent-hagan2011-pdf
  - outer-agent-P0A910
  - outer-agent-P06996
  - outer-agent-P02931
  - outer-agent-P0A940
  - outer-agent-P31554
  - outer-agent-P77774
  - outer-agent-P0A903
  - outer-agent-P0AC02
  - record
  - policy
- assessment_id: lps-conditional
  area: scope
  topic: LPS is not universal to every outer membrane
  outcome: supported
  target_ids:
  - GO:0009279
  summary: CONDITIONAL LPS wording and the canonical Gram-negative definition are
    consistent with review examples of LPS-deficient viable bacteria and noncanonical
    mycolic-acid envelopes. This does not infer dispensability in E.coli from a different
    species.
  evidence_ids:
  - outer-agent-silhavy2010-legacy-html
  - outer-agent-sperandeo2017-legacy-html
  - record
- assessment_id: assembly-graph
  area: graph
  topic: Lpt and BAM machinery with representative references
  outcome: supported
  target_ids:
  - GO:0009279
  summary: The graph correctly assigns LPS movement to the transenvelope Lpt machinery
    and beta-barrel assembly to BAM. P31554 is LptD, and the BAM accessions identify
    A/B/C/D members; these are correct representative constituent links, not complete
    machinery inventories or exact equivalences of each protein to the whole module.
    The schema allows protein complexes as causal nodes.
  evidence_ids:
  - outer-agent-sperandeo2017-legacy-html
  - outer-agent-hagan2011-pdf
  - outer-agent-silhavy2010-legacy-html
  - outer-agent-P0A910
  - outer-agent-P06996
  - outer-agent-P02931
  - outer-agent-P0A940
  - outer-agent-P31554
  - outer-agent-P77774
  - outer-agent-P0A903
  - outer-agent-P0AC02
  - record
  - policy
- assessment_id: barrier-graph
  area: graph
  topic: Permeability is reduced rather than abolished
  outcome: supported
  target_ids:
  - GO:0009279
  summary: 'Ordered LPS and porins jointly support a selective barrier: hydrophobic
    lipid-phase diffusion is slow and porin passage depends on solute size/chemistry.
    Read with its explicit descriptions inhibits/slows/reducing, the excludes edge
    is not an absolute zero-influx assertion. The porin node names a subset of the
    broad component cohort; it does not make BamA a general diffusion porin.'
  evidence_ids:
  - outer-agent-silhavy2010-legacy-html
  - outer-agent-nikaido2003-browser1
  - outer-agent-nikaido2003-browser2
  - record
- assessment_id: evidence-attribution
  area: provenance
  topic: Direct database attribution versus primary body
  outcome: supported
  target_ids:
  - GO:0009279
  summary: All maintained UniProt location-evidence PMIDs match native entry annotations
    and exact bibliographic metadata. The four main mechanistic citations are reviews
    and are retained at review tier. Individual location-study primary bodies were
    not independently read, so this assessment verifies attribution rather than claiming
    full experiment replication.
  evidence_ids:
  - outer-agent-pmid-10636850
  - outer-agent-pmid-10947984
  - outer-agent-pmid-16079137
  - outer-agent-pmid-23882017
  - outer-agent-pmid-24619089
  - outer-agent-pmid-2464593
  - outer-agent-doi-cshperspect_a000414
  - outer-agent-doi-jbc_R117_802512
  - outer-agent-doi-annurev-biochem-061408-144611
  - outer-agent-doi-MMBR_67_4_593-656_2003
  - outer-agent-P0A910
  - outer-agent-P06996
  - outer-agent-P02931
  - outer-agent-P0A940
  - outer-agent-P31554
  - outer-agent-P77774
  - outer-agent-P0A903
  - outer-agent-P0AC02
  - outer-agent-silhavy2010-legacy-html
  - outer-agent-sperandeo2017-legacy-html
  - outer-agent-hagan2011-pdf
  - outer-agent-nikaido2003-browser1
  - outer-agent-nikaido2003-browser2
  - record
- assessment_id: completeness
  area: completeness
  topic: Partial machinery links and optional enrichment
  outcome: supported
  target_ids:
  - GO:0009279
  summary: The present record covers core canonical constituents, function and two
    bounded mechanisms. Full BAM/Lpt reference coverage, extra lipoprotein/phospholipid
    rows, additional taxa, images and numerical properties are optional. No concrete
    incorrect identifier or mechanism was established; assembly-necessity support
    and contextual generalization remain limitations.
  evidence_ids:
  - outer-agent-silhavy2010-legacy-html
  - outer-agent-sperandeo2017-legacy-html
  - outer-agent-hagan2011-pdf
  - record
  - policy
findings: []
actions: []
limitations:
- The collective beta-barrel ESSENTIAL annotation concerns whether the structure forms
  without the component, not membership, transport activity or cell viability. The
  reviewed evidence does not independently establish that assembly-necessity assertion.
- The two mechanistic graphs describe the canonical LPS-rich Gram-negative case established
  by their references; the broader cell-outer-membrane identity also includes noncanonical
  envelopes. The definition and conditional LPS row provide that context, and no universal
  LPS/BAM mechanism is inferred.
- Lpt graph xrefs cover LptD only and BAM xrefs cover A/B/C/D, omitting other constituents.
  These are partial representative links, not complete inventories. The porin node
  is narrower than the generic beta-barrel component cohort.
- Silhavy, Sperandeo, Hagan and Nikaido are reviews. The specified native body passages
  and indexed Nikaido excerpts were read; primary experiments underlying every mechanism
  and the individual UniProt location studies were not independently audited. Exact
  location-evidence attribution was checked against UniProt and native metadata.
- Nikaido native routes returned challenge HTML, JATS500 or S3 errors; usable indexed
  review excerpts were recovered with exact status:null receipts. Hagan was a genuine
  PDF, and Silhavy/Sperandeo genuine legacy PMC HTML. Failed responses are preserved
  and not counted as readable bodies.
- Exclusion means reduced lipid-phase influx in this context; active efflux and species/preparation
  differences also affect measured accumulation. No quantitative permeability constant,
  universal pore cutoff, exact gene essentiality or atomic assembly sequence is asserted.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- All13 native inspection input hashes, focused gates0 and source receipts verified.
  No scientific edits or mapping-status promotion.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
