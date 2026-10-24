# Arp2/3 subunit identity and molecular-evidence scope review

- Review: 20261021T094741Z-arp2-3-protein-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:08:01Z
- Finished UTC: 2026-10-21T09:47:41Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-complex identity and all seven concrete examples are supported. Two major issues remain: the definition reverses Arc19/Arc18 homolog labels, and detailed subunit mechanisms are falsely attributed to a cortical-patch EM paper.

## Scope And Provenance

Entire single target, exact native ontology/protein/taxon identities, all component and graph claims, source-specific body/abstract boundaries and assembly-necessity limits.

Selection: Seventh selected target in batch fifteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005885 | data/structures/cytoskeleton/arp2_3_protein_complex.yaml | maintained | Arp2/3 protein complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005885 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005885 | Focused validator passed. |
| Native UniProt verify | passed | False | GO:0005885 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0005885 | Native command passed; scientific membership and graph scope assessed independently. |
| Claim-level scientific review | passed | True | GO:0005885 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:0005885 | 20 of 21 exact target identifiers returned OK. Residuals: PMID:9210376 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by arp-agent-pmid-9210376 The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:0005885 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005885 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005885 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005885 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005885 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole complex, patch and polymer remain distinct

identity: supported. Targets: GO:0005885.

The GO identity, kind, parent and actin-cytoskeleton parthood are correct. Component rows deliberately group protein subunits; their concrete examples are not claimed to be equivalent to the whole complex. Actin cortical patches and branched actin polymers are the structures on which the complex acts.

### Arc19 and Arc18 homolog labels are reversed in the definition

grounding: concern. Targets: GO:0005885.

Native reviewed P33204 is ARC19, Arp2/3 subunit4; Q05933 is ARC18, subunit3. The definition instead pairs Arc19 with ARPC3 and Arc18 with ARPC4, contradicting both authorities and the correct component labels/examples later in the same record.

### Seven correct concrete protein examples

evidence: supported. Targets: GO:0005885.

All seven gene/accession/taxon/status identities are correct and native subunit annotations support membership in the yeast complex. The Sagot actin-body notes explicitly retain partial localization and no whole-complex inference. Winter1997 is correctly attributed by native P47117 location evidence; its abstract is accessible, but its full experimental body was not independently audited.

### Young2004 does not establish the claimed subunit mechanisms

evidence: concern. Targets: GO:0005885.

The cited Young paper supports branched cortical-patch morphology and associated patch-protein mutant observations. It does not characterize the Arc35/Arc19 clamp or define Arc40/Arc18/Arc15 coupling to nucleation-promoting factors as the component/graph evidence notes state. Detailed roles may be biologically plausible, but these particular primary-source attributions are incorrect.

### Morphology, activation and internalization require separate evidence

graph: concern. Targets: GO:0005885.

Young supports approximately70-degree patch branches as consistent with Arp2/3-mediated assembly; Kaksonen2003 abstract supports the temporal endocytic pathway and actin requirement. Neither access scope establishes the maintained short-pitch Arp2/Arp3 rearrangement. Galletta supports regulator effects on patch assembly/movement. Basic part-of and patch/endocytosis functions are supported; atomistic activation wording needs a directly inspected structural or biochemical source.

### ESSENTIAL is not established by the cited membership/localization observations

evidence: unknown. Targets: GO:0005885.

All three rows assert ESSENTIAL, which the schema defines as whether the structure forms without the component. Composition, branch formation, endocytic activity and cell viability are not substitutes for that criterion. No complete group-specific removal/assembly experiment was checked. Winter1997 abstract describes a preparation lacking the40kDa member, but this is not removal of the entire three-protein peripheral group and is not generalized as a group-essentiality counterexample.

### Yeast examples are narrower than broad introductory mechanism wording

scope: unknown. Targets: GO:0005885.

S.cerevisiae cortical-patch occurrence and the canonical isolated-patch example are supported, without assigning the S288C reference sequence to every experimental stock. The appended amoeba/filamentous-fungus process list is broader than the cited yeast experiments; it does not establish that every listed taxon performs every listed process.

### Molecular evidence rather than optional data volume is the gap

completeness: supported. Targets: GO:0005885.

All seven known subunits are represented. Splitting the deliberate groups, adding family CURIEs, images or numerical properties is optional. The concrete problems are incorrect homolog labels and claims attributed to a paper that did not test them; unresolved assembly necessity and broader taxon mechanisms remain explicit limits.

## Findings

### F1: Correct the reversed Arc19/ARPC4 and Arc18/ARPC3 pairs

major / open / confirmed; issue key: arp19-arp18-definition-pairings-reversed.

The definition pairs Arc19 with ARPC3 and Arc18 with ARPC4. Native P33204 identifies ARC19 as subunit4, while Q05933 identifies ARC18 as subunit3. The component labels and protein examples already use the correct pairs. Correct the definition without replacing those correct examples.

### F2: Replace unsupported subunit-mechanism attributions to Young2004

major / open / confirmed; issue key: arp-subunit-mechanisms-misattributed-to-patch-em.

Both clamp and peripheral component evidence notes claim that Young2004 characterizes seven-subunit requirements or defines Arc40/Arc18/Arc15 activation coupling. The complete inspected paper instead analyzes isolated cortical actin patch networks and sac6/cap1 mutants. Correct these false evidence summaries and support any retained detailed subunit roles with an appropriate inspected primary structural/biochemical source. Apply the same correction to repeated graph descriptions/evidence; independently verify the short-pitch Arp2/Arp3 activation claim rather than treating the accessible Kaksonen abstract as its proof.

## Recommended Actions And Acceptance Checks

### A1

During authorized curation, replace the two reversed definition pairings with Arc19/ARPC4 and Arc18/ARPC3.

- Keep P33204 and Q05933 attached to their current correct genes/components.
- Check the resulting definition against the native reviewed identity snapshots.
- Run focused schema and strict-reference validation.

### A2

During authorized curation, repair source-specific evidence notes and source or qualify each detailed molecular role consistently in components and graph.

- Retain Young2004 for branched patch morphology at its actual experimental scope.
- Use an inspected structural/biochemical source for subunit contacts and activation rearrangements, or remove/qualify unsupported specificity.
- Keep exact protein identities separate from localization, function and assembly necessity.
- Do not treat ESSENTIAL as a synonym for membership or catalytic contribution.
- Run focused schema, strict-reference and causal-graph checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/arp2_3_protein_complex.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| arp-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0005885,GO:0015629,GO:0030479,GO:0030864,GO:0032991,GO:0061645; All seven returned native term identities, definitions and relevant child relations; complex versus patch and process boundaries | supports | GO0005885 is the seven-subunit Arp2/3 protein complex with protein-containing-complex ancestry and actin-cytoskeleton parthood. The cortical patch and its assembly process are distinct identities; GO does not supply the appended yeast Arc19/Arc18 pairings or molecular activation details. |
| arp-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxon identity, rank and lineage | supports | Native taxon4932 identifies Saccharomyces cerevisiae at rank species. This single snapshot attests only this taxon; comparisons to the other species or strain use its separate evidence row. |
| arp-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxon identity, rank and lineage | supports | Native taxon559292 identifies Saccharomyces cerevisiae S288C at rank strain. This single snapshot attests only this taxon; comparisons to the other species or strain use its separate evidence row. |
| arp-agent-P32381 | https://rest.uniprot.org/uniprotkb/P32381.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P32381 identifies Actin-related protein 2, gene ARP2, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| arp-agent-query-ARP2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARP2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ARP2, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P32381. This checks identifier resolution only. |
| arp-agent-P47117 | https://rest.uniprot.org/uniprotkb/P47117.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P47117 identifies Actin-related protein 3, gene ARP3, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| arp-agent-query-ARP3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARP3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ARP3, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P47117. This checks identifier resolution only. |
| arp-agent-P53731 | https://rest.uniprot.org/uniprotkb/P53731.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P53731 identifies Actin-related protein 2/3 complex subunit 2, gene ARC35, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| arp-agent-query-ARC35 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC35%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ARC35, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P53731. This checks identifier resolution only. |
| arp-agent-P33204 | https://rest.uniprot.org/uniprotkb/P33204.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P33204 identifies Actin-related protein 2/3 complex subunit 4, gene ARC19, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| arp-agent-query-ARC19 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC19%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ARC19, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P33204. This checks identifier resolution only. |
| arp-agent-P38328 | https://rest.uniprot.org/uniprotkb/P38328.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P38328 identifies Actin-related protein 2/3 complex subunit 1, gene ARC40, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| arp-agent-query-ARC40 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC40%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ARC40, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P38328. This checks identifier resolution only. |
| arp-agent-Q05933 | https://rest.uniprot.org/uniprotkb/Q05933.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB Q05933 identifies Actin-related protein 2/3 complex subunit 3, gene ARC18, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| arp-agent-query-ARC18 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC18%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ARC18, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns Q05933. This checks identifier resolution only. |
| arp-agent-P40518 | https://rest.uniprot.org/uniprotkb/P40518.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P40518 identifies Actin-related protein 2/3 complex subunit 5, gene ARC15, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| arp-agent-query-ARC15 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3AARC15%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene ARC15, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P40518. This checks identifier resolution only. |
| arp-agent-kaksonen2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID:14622601%20AND%20SRC:MED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies A pathway for association of receptors, adaptors, and actin during endocytic internalization. Authors: Kaksonen M, Sun Y, Drubin DG.; PMID 14622601; DOI 10.1016/s0092-8674(03)00883-3. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| arp-agent-doi-jcb.200404159 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.200404159; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Yeast actin patches are networks of branched actin filaments. Authors: Young ME, Cooper JA, Bridgman PC.; PMID 15337772; DOI 10.1083/jcb.200404159. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| arp-agent-doi-journal.pbio.0060001 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1371/journal.pbio.0060001; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Distinct roles for Arp2/3 regulators in actin assembly and endocytosis. Authors: Galletta BJ, Chuang DY, Cooper JA.; PMID 18177206; DOI 10.1371/journal.pbio.0060001. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| arp-agent-doi-mbc.E06-04-0282 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E06-04-0282; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Actin bodies in yeast quiescent cells: an immediately available actin reserve? Authors: Sagot I, Pinson B, Salin B, Daignan-Fornier B.; PMID 16914523; DOI 10.1091/mbc.e06-04-0282. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| arp-agent-pmid-9210376 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9210376%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The complex containing actin-related proteins Arp2 and Arp3 is required for the motility and integrity of yeast actin patches. Authors: Winter D, Podtelejnikov AV, Mann M, Li R.; PMID 9210376; DOI 10.1016/s0960-9822(06)00223-5. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| arp-agent-jats-jcb.200404159 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2172413.1/PMC2172413.1.xml; Native PMC2172413.1 JATS: complete Introduction, Results, Discussion and Materials/Methods; all main figure captions and TableI. Isolated cross-linked and uncross-linked patches, S1 decoration and preparation limits read. No raw-data reanalysis. | supports | Young, Cooper and Bridgman2004 examine partially purified GFP-labeled yeast cortical actin patches by correlated fluorescence and electron microscopy. Branched filament geometry is consistent with Arp2/3 nucleation; branch angles are measured, and sac6/cap1 mutants are tested. This is not a determination of Arp2/3 individual-subunit clamp architecture or Arc40/18/15 activation coupling. |
| arp-agent-galletta2008-plos | https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060001; Genuine PLoS publisher article: Abstract, Author Summary, Introduction; first Results subsection on Las17 acidic domain and Figure1/2 captions; complete Discussion with Figure7 caption; main Materials/Methods. Other individual-regulator Results subsections and supplemental movies were not read. | supports | Galletta2008 studies Arp2/3 regulators in yeast patch assembly and movement, supporting regulator-dependent actin assembly/endocytosis. Its discussion distinguishes activation from localization and does not make every activator an obligatory on/off switch. |
| arp-agent-sagot2006-browser | https://pmc.ncbi.nlm.nih.gov/articles/PMC1635378/; Indexed PMC1635378 Results, Several Actin-binding Proteins Colocalize with Actin Bodies: 29 GFP-tagged proteins screened; six partial colocalizers including the four maintained examples. Only this claim-bearing returned excerpt is used; unrelated search results are not evidence. | supports | The primary Sagot2006 indexed Results explicitly report partial actin-body colocalization of Arc15, Arc18, Arc35 and Arp2. This supports the carefully limited microscopy notes but is not purification or a complete Arp2/3 occupancy census. |
| schema-result | just validate data/structures/cytoskeleton/arp2_3_protein_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/arp2_3_protein_complex.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/arp2_3_protein_complex.yaml --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/arp2_3_protein_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/arp2_3_protein_complex.yaml --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/arp2_3_protein_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch15-20261021-ohdkgt21/arp2_3_protein_complex-strict.tsv |
| native-verify | /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/arp2_3_protein_complex.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/arp2_3_protein_complex.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/cytoskeleton/arp2_3_protein_complex.yaml  (GO:0005885)<br>  arp2_3_protein_complex_mechanism	arp2_arp3_nucleation_dimer	COVERED	-&gt;arp2_arp3_nucleation_dimer (UniProtKB:P32381, UniProtKB:P47117)<br>  arp2_3_protein_complex_mechanism	arc35_arc19_clamp_subunits	COVERED	-&gt;arc35_arc19_clamp_subunits (UniProtKB:P53731, UniProtKB:P33204)<br>  arp2_3_protein_complex_mechanism	arc40_arc18_arc15_peripheral_subunits	COVERED	-&gt;arc40_arc18_arc15_peripheral_subunits (UniProtKB:P38328, UniProtKB:Q05933, UniProtKB:P40518)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| target-curies-result | just check-curies-strict; data/structures/cytoskeleton/arp2_3_protein_complex.yaml; exact native collect() target slice of original fresh-base TSV | supports | 20 of 21 exact target identifiers returned OK. Residuals: PMID:9210376 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by arp-agent-pmid-9210376 The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Young2004 complete main body/captions/TableI were read; Galletta2008 access was limited to the explicitly listed sections. Kaksonen2003 and Winter1997 were inspected at native abstract/metadata level only; the Kaksonen publisher route returned403. No claim of a full-body Kaksonen or Winter audit is made.
- Sagot2006 was read through a captured indexed primary Results excerpt with status:null. The native S3 JATS route returned404 and browser direct routes were challenged. The excerpt supports partial actin-body colocalization only, not a complete Arp2/3 complex in every body.
- The three ESSENTIAL values remain unverified under the schema assembly-necessity criterion. The reviewed membership/function evidence does not establish that the defined structure fails to form after removal of each declared group.
- Broad amoebal/filamentous-fungal mechanisms and individual-family mappings were not exhaustively surveyed. No cross-taxon universal mechanism, exact stoichiometric occupancy or unverified family equivalence is inferred.
- The first DOI query containing parentheses returned no metadata result; the successful PMID14622601 query supplies the exact Kaksonen citation. Failed/challenge responses are retained as access receipts, not primary bodies.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All13 fresh batch15 inspection input hashes verified. Native schema/strict and UniProt checks passed; scientific content and PROPOSED status remain unchanged.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094741Z-arp2-3-protein-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Arp2/3 subunit identity and molecular-evidence scope review
started_at: '2026-10-21T09:08:01Z'
finished_at: '2026-10-21T09:47:41Z'
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
summary: 'Whole-complex identity and all seven concrete examples are supported. Two
  major issues remain: the definition reverses Arc19/Arc18 homolog labels, and detailed
  subunit mechanisms are falsely attributed to a cortical-patch EM paper.'
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
  - path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    sha256: a612b062735844ba209722df0054d084db27ef18e8a243dc32d6d180303fd44b
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
- target_id: GO:0005885
  path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  label: Arp2/3 protein complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    role: maintained scientific record
scope:
  description: Entire single target, exact native ontology/protein/taxon identities,
    all component and graph claims, source-specific body/abstract boundaries and assembly-necessity
    limits.
  selection: Seventh selected target in batch fifteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005885
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005885
  command: just validate data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005885
  command: just validate-strict data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/arp2_3_protein_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0005885
  command: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/arp2_3_protein_complex.yaml
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
  - GO:0005885
  command: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/arp2_3_protein_complex.yaml
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
  - GO:0005885
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - arp-agent-go
  - arp-agent-tax-4932
  - arp-agent-tax-559292
  - arp-agent-P32381
  - arp-agent-query-ARP2
  - arp-agent-P47117
  - arp-agent-query-ARP3
  - arp-agent-P53731
  - arp-agent-query-ARC35
  - arp-agent-P33204
  - arp-agent-query-ARC19
  - arp-agent-P38328
  - arp-agent-query-ARC40
  - arp-agent-Q05933
  - arp-agent-query-ARC18
  - arp-agent-P40518
  - arp-agent-query-ARC15
  - arp-agent-kaksonen2003-meta
  - arp-agent-doi-jcb.200404159
  - arp-agent-doi-journal.pbio.0060001
  - arp-agent-doi-mbc.E06-04-0282
  - arp-agent-pmid-9210376
  - arp-agent-jats-jcb.200404159
  - arp-agent-galletta2008-plos
  - arp-agent-sagot2006-browser
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:0005885
  summary: '20 of 21 exact target identifiers returned OK. Residuals: PMID:9210376
    returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently
    verified by arp-agent-pmid-9210376 The shared command exit zero is not interpreted
    as successful network resolution for transport failures.'
  evidence_ids:
  - target-curies-result
  - arp-agent-pmid-9210376
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005885
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
  - GO:0005885
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
  - GO:0005885
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
  - GO:0005885
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
  - GO:0005885
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
  reference: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T09:24:05Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:24:05Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: arp-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0005885,GO:0015629,GO:0030479,GO:0030864,GO:0032991,GO:0061645
  locator: All seven returned native term identities, definitions and relevant child
    relations; complex versus patch and process boundaries
  accessed_at: '2026-10-21T09:14:54.497799Z'
  support: supports
  summary: GO0005885 is the seven-subunit Arp2/3 protein complex with protein-containing-complex
    ancestry and actin-cytoskeleton parthood. The cortical patch and its assembly
    process are distinct identities; GO does not supply the appended yeast Arc19/Arc18
    pairings or molecular activation details.
  snapshot_sha256: 52609f09b91414176bd0802335b29604b8cea985ab53da1e1aa84198c85a1fa5
- evidence_id: arp-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:14:54.498210Z'
  support: supports
  summary: Native taxon4932 identifies Saccharomyces cerevisiae at rank species. This
    single snapshot attests only this taxon; comparisons to the other species or strain
    use its separate evidence row.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: arp-agent-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:14:54.498363Z'
  support: supports
  summary: Native taxon559292 identifies Saccharomyces cerevisiae S288C at rank strain.
    This single snapshot attests only this taxon; comparisons to the other species
    or strain use its separate evidence row.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: arp-agent-P32381
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32381.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:14:54.498516Z'
  support: supports
  summary: Native reviewed UniProtKB P32381 identifies Actin-related protein 2, gene
    ARP2, taxon559292. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 2b378f480e51da72d42b3b9dce10343e882ecd765163079ebba5dee3a2597bf9
- evidence_id: arp-agent-query-ARP2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARP2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ARP2, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:14:55.791342Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P32381. This checks identifier
    resolution only.
  snapshot_sha256: dfebbdfdb0fb815de18cf04958a76825298435a28c2b14fb2f4d644fbf8cba8a
  search_scope: UniProtKB query gene_exact:ARP2 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: arp-agent-P47117
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47117.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:14:55.226518Z'
  support: supports
  summary: Native reviewed UniProtKB P47117 identifies Actin-related protein 3, gene
    ARP3, taxon559292. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: c1fb00ae697516d543e044536958483b7e17ee1660700e869689adb336de7b71
- evidence_id: arp-agent-query-ARP3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARP3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ARP3, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:14:55.886342Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P47117. This checks identifier
    resolution only.
  snapshot_sha256: 2fd3bf9551a26771c0fa16bbc3e318de130696bc94b2f4760fc8e138bf421e61
  search_scope: UniProtKB query gene_exact:ARP3 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: arp-agent-P53731
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53731.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:14:55.232103Z'
  support: supports
  summary: Native reviewed UniProtKB P53731 identifies Actin-related protein 2/3 complex
    subunit 2, gene ARC35, taxon559292. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: 7c903010adc7254a171b89a0cf935052237882f9599de322c36116a29640f2ad
- evidence_id: arp-agent-query-ARC35
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC35%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ARC35, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:14:56.178940Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P53731. This checks identifier
    resolution only.
  snapshot_sha256: 6cfa62fe3454446fd9c97d4e8ab4b2b8a26222347f367e0f602cf9257c9cb995
  search_scope: UniProtKB query gene_exact:ARC35 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: arp-agent-P33204
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33204.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:14:54.498681Z'
  support: supports
  summary: Native reviewed UniProtKB P33204 identifies Actin-related protein 2/3 complex
    subunit 4, gene ARC19, taxon559292. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: 6a510fff14b0f9054f847c6ad26e13dfc29e391b6c173a27dc6410b509bf7000
- evidence_id: arp-agent-query-ARC19
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC19%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ARC19, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:14:56.218133Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P33204. This checks identifier
    resolution only.
  snapshot_sha256: 1a847c87c46f70cfa1ce9a557d5e37332a3594ef1168d73e6de42081e4fe8c66
  search_scope: UniProtKB query gene_exact:ARC19 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: arp-agent-P38328
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38328.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:14:55.170129Z'
  support: supports
  summary: Native reviewed UniProtKB P38328 identifies Actin-related protein 2/3 complex
    subunit 1, gene ARC40, taxon559292. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: cb2cf7eba6e89e1c6e9a26a6cab12515382eff955ca37f302d7762c99853a6eb
- evidence_id: arp-agent-query-ARC40
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC40%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ARC40, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:14:56.234557Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P38328. This checks identifier
    resolution only.
  snapshot_sha256: 42f2915f586bbecd94d03031300dd449208983f62bc6db4d9af39e1d3c977873
  search_scope: UniProtKB query gene_exact:ARC40 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: arp-agent-Q05933
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q05933.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:14:55.279122Z'
  support: supports
  summary: Native reviewed UniProtKB Q05933 identifies Actin-related protein 2/3 complex
    subunit 3, gene ARC18, taxon559292. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: a0f9700443c987dd59d04c81980287273147117d9c570aa6e3cafdb62636eb51
- evidence_id: arp-agent-query-ARC18
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC18%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ARC18, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:14:56.547687Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns Q05933. This checks identifier
    resolution only.
  snapshot_sha256: f8ea6b20283807a786443913a74fe80a7023003e5e2608a2c103baa8f7fc535a
  search_scope: UniProtKB query gene_exact:ARC18 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: arp-agent-P40518
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40518.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:14:55.215087Z'
  support: supports
  summary: Native reviewed UniProtKB P40518 identifies Actin-related protein 2/3 complex
    subunit 5, gene ARC15, taxon559292. Concrete identity is checked independently
    of membership; relevant subunit/cofactor/location comments retain their own evidence
    scope.
  snapshot_sha256: f6a13b306d4e1740fa932240cf28d5ab9ef710a923167a97c1442d240b3014f2
- evidence_id: arp-agent-query-ARC15
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3AARC15%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene ARC15, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:14:57.274304Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P40518. This checks identifier
    resolution only.
  snapshot_sha256: 75eaaf64f0a1c5a0496ac86ba4e1965a492f606002cc2481475fc5b829c66aa4
  search_scope: UniProtKB query gene_exact:ARC15 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: arp-agent-kaksonen2003-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID:14622601%20AND%20SRC:MED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:15:43.770167Z'
  support: supports
  summary: 'Native metadata identifies A pathway for association of receptors, adaptors,
    and actin during endocytic internalization. Authors: Kaksonen M, Sun Y, Drubin
    DG.; PMID 14622601; DOI 10.1016/s0092-8674(03)00883-3. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 231ebac644f0b6710d7390920df5d22ca887f86426188e1fd407d7e98dae6510
- evidence_id: arp-agent-doi-jcb.200404159
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.200404159
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:14:57.298129Z'
  support: supports
  summary: 'Native metadata identifies Yeast actin patches are networks of branched
    actin filaments. Authors: Young ME, Cooper JA, Bridgman PC.; PMID 15337772; DOI
    10.1083/jcb.200404159. Bibliographic identity and available abstract only; not
    a substitute for inspected article body.'
  snapshot_sha256: e9459bf7a252db9f77ac4990dc14fd4892fab1fca60c05702a6b63681c6d7cfa
- evidence_id: arp-agent-doi-journal.pbio.0060001
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1371/journal.pbio.0060001
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:14:58.078016Z'
  support: supports
  summary: 'Native metadata identifies Distinct roles for Arp2/3 regulators in actin
    assembly and endocytosis. Authors: Galletta BJ, Chuang DY, Cooper JA.; PMID 18177206;
    DOI 10.1371/journal.pbio.0060001. Bibliographic identity and available abstract
    only; not a substitute for inspected article body.'
  snapshot_sha256: ac7737e4a85ce68ea155e71e279b4cb05d0945a25d329982a6f7bd47c3927e15
- evidence_id: arp-agent-doi-mbc.E06-04-0282
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E06-04-0282
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:14:57.381002Z'
  support: supports
  summary: 'Native metadata identifies Actin bodies in yeast quiescent cells: an immediately
    available actin reserve? Authors: Sagot I, Pinson B, Salin B, Daignan-Fornier
    B.; PMID 16914523; DOI 10.1091/mbc.e06-04-0282. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 7721d53295c55feca2fe04b4a12bea6463a2cc271fd0360986b784b3e31c346a
- evidence_id: arp-agent-pmid-9210376
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9210376%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:14:58.260545Z'
  support: supports
  summary: 'Native metadata identifies The complex containing actin-related proteins
    Arp2 and Arp3 is required for the motility and integrity of yeast actin patches.
    Authors: Winter D, Podtelejnikov AV, Mann M, Li R.; PMID 9210376; DOI 10.1016/s0960-9822(06)00223-5.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 151d04ea747d831de23b637c42a74aea902ce84dab5f5c62c58a0b542506e9bc
- evidence_id: arp-agent-jats-jcb.200404159
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2172413.1/PMC2172413.1.xml
  locator: 'Native PMC2172413.1 JATS: complete Introduction, Results, Discussion and
    Materials/Methods; all main figure captions and TableI. Isolated cross-linked
    and uncross-linked patches, S1 decoration and preparation limits read. No raw-data
    reanalysis.'
  accessed_at: '2026-10-21T09:15:57.521096Z'
  support: supports
  summary: Young, Cooper and Bridgman2004 examine partially purified GFP-labeled yeast
    cortical actin patches by correlated fluorescence and electron microscopy. Branched
    filament geometry is consistent with Arp2/3 nucleation; branch angles are measured,
    and sac6/cap1 mutants are tested. This is not a determination of Arp2/3 individual-subunit
    clamp architecture or Arc40/18/15 activation coupling.
  snapshot_sha256: 7f6584b83df46499ba5c7e041436bf04a67115725fd90c8470d8c5982e073bf4
- evidence_id: arp-agent-galletta2008-plos
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060001
  locator: 'Genuine PLoS publisher article: Abstract, Author Summary, Introduction;
    first Results subsection on Las17 acidic domain and Figure1/2 captions; complete
    Discussion with Figure7 caption; main Materials/Methods. Other individual-regulator
    Results subsections and supplemental movies were not read.'
  accessed_at: '2026-10-21T09:16:18.290045Z'
  support: supports
  summary: Galletta2008 studies Arp2/3 regulators in yeast patch assembly and movement,
    supporting regulator-dependent actin assembly/endocytosis. Its discussion distinguishes
    activation from localization and does not make every activator an obligatory on/off
    switch.
  snapshot_sha256: 2e22ffa309390850ae8694fe35e7c0d3ea83861b18d63757e536009267f1de24
- evidence_id: arp-agent-sagot2006-browser
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1635378/
  locator: 'Indexed PMC1635378 Results, Several Actin-binding Proteins Colocalize
    with Actin Bodies: 29 GFP-tagged proteins screened; six partial colocalizers including
    the four maintained examples. Only this claim-bearing returned excerpt is used;
    unrelated search results are not evidence.'
  accessed_at: '2026-10-21T09:17:17Z'
  support: supports
  summary: The primary Sagot2006 indexed Results explicitly report partial actin-body
    colocalization of Arc15, Arc18, Arc35 and Arp2. This supports the carefully limited
    microscopy notes but is not purification or a complete Arp2/3 occupancy census.
  snapshot_sha256: 3e60c9e736e39e4562c509bb9673ffae5bf60d73231b73919831e3c4d18de321
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:08:08Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/arp2_3_protein_complex.yaml'
  snapshot_sha256: 87ea7e69b2b9db7b87a399356946004ec2bc24da9e987056f9738b9cb11d9fca
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/arp2_3_protein_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:08:13Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/arp2_3_protein_complex.yaml\
    \ --out /private/tmp/cellstructure-batch15-20261021-ohdkgt21/arp2_3_protein_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch15-20261021-ohdkgt21/arp2_3_protein_complex-strict.tsv"
  snapshot_sha256: 431c7bdc8ad363ab78a4215ef1bb1461cdefc5a519efcea1500b0d33ac301be0
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T09:14:55.381568Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch15-20261021-ohdkgt21/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T09:14:55.946343Z'
  support: supports
  summary: "data/structures/cytoskeleton/arp2_3_protein_complex.yaml  (GO:0005885)\n\
    \  arp2_3_protein_complex_mechanism\tarp2_arp3_nucleation_dimer\tCOVERED\t->arp2_arp3_nucleation_dimer\
    \ (UniProtKB:P32381, UniProtKB:P47117)\n  arp2_3_protein_complex_mechanism\tarc35_arc19_clamp_subunits\t\
    COVERED\t->arc35_arc19_clamp_subunits (UniProtKB:P53731, UniProtKB:P33204)\n \
    \ arp2_3_protein_complex_mechanism\tarc40_arc18_arc15_peripheral_subunits\tCOVERED\t\
    ->arc40_arc18_arc15_peripheral_subunits (UniProtKB:P38328, UniProtKB:Q05933, UniProtKB:P40518)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 3ee1f7c6d9fefa540b329cd2e05709cc0e2459a9ab0e66c0ee6415f63ff6f88c
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/arp2_3_protein_complex.yaml; exact native
    collect() target slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:47:06.636114Z'
  support: supports
  summary: '20 of 21 exact target identifiers returned OK. Residuals: PMID:9210376
    returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently
    verified by arp-agent-pmid-9210376 The shared command exit zero is not interpreted
    as successful network resolution for transport failures.'
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
  topic: Whole complex, patch and polymer remain distinct
  outcome: supported
  target_ids:
  - GO:0005885
  summary: The GO identity, kind, parent and actin-cytoskeleton parthood are correct.
    Component rows deliberately group protein subunits; their concrete examples are
    not claimed to be equivalent to the whole complex. Actin cortical patches and
    branched actin polymers are the structures on which the complex acts.
  evidence_ids:
  - arp-agent-go
  - arp-agent-jats-jcb.200404159
  - record
  - policy
- assessment_id: subunit-pairs
  area: grounding
  topic: Arc19 and Arc18 homolog labels are reversed in the definition
  outcome: concern
  target_ids:
  - GO:0005885
  summary: Native reviewed P33204 is ARC19, Arp2/3 subunit4; Q05933 is ARC18, subunit3.
    The definition instead pairs Arc19 with ARPC3 and Arc18 with ARPC4, contradicting
    both authorities and the correct component labels/examples later in the same record.
  evidence_ids:
  - arp-agent-P33204
  - arp-agent-Q05933
  - record
- assessment_id: membership
  area: evidence
  topic: Seven correct concrete protein examples
  outcome: supported
  target_ids:
  - GO:0005885
  summary: All seven gene/accession/taxon/status identities are correct and native
    subunit annotations support membership in the yeast complex. The Sagot actin-body
    notes explicitly retain partial localization and no whole-complex inference. Winter1997
    is correctly attributed by native P47117 location evidence; its abstract is accessible,
    but its full experimental body was not independently audited.
  evidence_ids:
  - arp-agent-P32381
  - arp-agent-P47117
  - arp-agent-P53731
  - arp-agent-P33204
  - arp-agent-P38328
  - arp-agent-Q05933
  - arp-agent-P40518
  - arp-agent-tax-4932
  - arp-agent-tax-559292
  - arp-agent-sagot2006-browser
  - arp-agent-pmid-9210376
  - record
- assessment_id: activation-source
  area: evidence
  topic: Young2004 does not establish the claimed subunit mechanisms
  outcome: concern
  target_ids:
  - GO:0005885
  summary: The cited Young paper supports branched cortical-patch morphology and associated
    patch-protein mutant observations. It does not characterize the Arc35/Arc19 clamp
    or define Arc40/Arc18/Arc15 coupling to nucleation-promoting factors as the component/graph
    evidence notes state. Detailed roles may be biologically plausible, but these
    particular primary-source attributions are incorrect.
  evidence_ids:
  - arp-agent-jats-jcb.200404159
  - arp-agent-P32381
  - arp-agent-P47117
  - arp-agent-P53731
  - arp-agent-P33204
  - arp-agent-P38328
  - arp-agent-Q05933
  - arp-agent-P40518
  - arp-agent-galletta2008-plos
  - record
- assessment_id: nucleation-scope
  area: graph
  topic: Morphology, activation and internalization require separate evidence
  outcome: concern
  target_ids:
  - GO:0005885
  summary: Young supports approximately70-degree patch branches as consistent with
    Arp2/3-mediated assembly; Kaksonen2003 abstract supports the temporal endocytic
    pathway and actin requirement. Neither access scope establishes the maintained
    short-pitch Arp2/Arp3 rearrangement. Galletta supports regulator effects on patch
    assembly/movement. Basic part-of and patch/endocytosis functions are supported;
    atomistic activation wording needs a directly inspected structural or biochemical
    source.
  evidence_ids:
  - arp-agent-go
  - arp-agent-jats-jcb.200404159
  - arp-agent-galletta2008-plos
  - arp-agent-kaksonen2003-meta
  - record
- assessment_id: assembly-necessity
  area: evidence
  topic: ESSENTIAL is not established by the cited membership/localization observations
  outcome: unknown
  target_ids:
  - GO:0005885
  summary: All three rows assert ESSENTIAL, which the schema defines as whether the
    structure forms without the component. Composition, branch formation, endocytic
    activity and cell viability are not substitutes for that criterion. No complete
    group-specific removal/assembly experiment was checked. Winter1997 abstract describes
    a preparation lacking the40kDa member, but this is not removal of the entire three-protein
    peripheral group and is not generalized as a group-essentiality counterexample.
  evidence_ids:
  - arp-agent-pmid-9210376
  - arp-agent-jats-jcb.200404159
  - arp-agent-P32381
  - arp-agent-P47117
  - arp-agent-P53731
  - arp-agent-P33204
  - arp-agent-P38328
  - arp-agent-Q05933
  - arp-agent-P40518
  - record
  - policy
- assessment_id: taxonomy
  area: scope
  topic: Yeast examples are narrower than broad introductory mechanism wording
  outcome: unknown
  target_ids:
  - GO:0005885
  summary: S.cerevisiae cortical-patch occurrence and the canonical isolated-patch
    example are supported, without assigning the S288C reference sequence to every
    experimental stock. The appended amoeba/filamentous-fungus process list is broader
    than the cited yeast experiments; it does not establish that every listed taxon
    performs every listed process.
  evidence_ids:
  - arp-agent-tax-4932
  - arp-agent-tax-559292
  - arp-agent-kaksonen2003-meta
  - arp-agent-jats-jcb.200404159
  - arp-agent-sagot2006-browser
  - record
- assessment_id: completeness
  area: completeness
  topic: Molecular evidence rather than optional data volume is the gap
  outcome: supported
  target_ids:
  - GO:0005885
  summary: All seven known subunits are represented. Splitting the deliberate groups,
    adding family CURIEs, images or numerical properties is optional. The concrete
    problems are incorrect homolog labels and claims attributed to a paper that did
    not test them; unresolved assembly necessity and broader taxon mechanisms remain
    explicit limits.
  evidence_ids:
  - arp-agent-go
  - arp-agent-P32381
  - arp-agent-P47117
  - arp-agent-P53731
  - arp-agent-P33204
  - arp-agent-P38328
  - arp-agent-Q05933
  - arp-agent-P40518
  - arp-agent-jats-jcb.200404159
  - policy
  - record
findings:
- finding_id: F1
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
  - arp-agent-P33204
  - arp-agent-Q05933
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: This is an explicit molecular identity error in the defining
    composition, not an optional nomenclature preference.
- finding_id: F2
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
  - arp-agent-jats-jcb.200404159
  - arp-agent-galletta2008-plos
  - arp-agent-kaksonen2003-meta
  - record
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
actions:
- action_id: A1
  finding_ids:
  - F1
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
- action_id: A2
  finding_ids:
  - F2
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
limitations:
- Young2004 complete main body/captions/TableI were read; Galletta2008 access was
  limited to the explicitly listed sections. Kaksonen2003 and Winter1997 were inspected
  at native abstract/metadata level only; the Kaksonen publisher route returned403.
  No claim of a full-body Kaksonen or Winter audit is made.
- Sagot2006 was read through a captured indexed primary Results excerpt with status:null.
  The native S3 JATS route returned404 and browser direct routes were challenged.
  The excerpt supports partial actin-body colocalization only, not a complete Arp2/3
  complex in every body.
- The three ESSENTIAL values remain unverified under the schema assembly-necessity
  criterion. The reviewed membership/function evidence does not establish that the
  defined structure fails to form after removal of each declared group.
- Broad amoebal/filamentous-fungal mechanisms and individual-family mappings were
  not exhaustively surveyed. No cross-taxon universal mechanism, exact stoichiometric
  occupancy or unverified family equivalence is inferred.
- The first DOI query containing parentheses returned no metadata result; the successful
  PMID14622601 query supplies the exact Kaksonen citation. Failed/challenge responses
  are retained as access receipts, not primary bodies.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- All13 fresh batch15 inspection input hashes verified. Native schema/strict and UniProt
  checks passed; scientific content and PROPOSED status remain unchanged.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
