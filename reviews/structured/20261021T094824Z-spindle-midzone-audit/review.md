# Spindle midzone versus whole-spindle function and evidence review

- Review: 20261021T094824Z-spindle-midzone-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:24:30Z
- Finished UTC: 2026-10-21T09:48:24Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The overlap-region identity and concrete tubulin examples are sound. Two major corrections concern whole-spindle functional transfer and unsupported specific regulator mechanism; two minor corrections concern synonym provenance and graph scope.

## Scope And Provenance

Entire single target, regional identity and component boundaries, native families/proteins/taxa/synonyms, readable primary morphology, scoped live-imaging abstract and review context, every function and graph edge.

Selection: Ninth selected target in batch sixteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0051233 | data/structures/cytoskeleton/spindle_midzone.yaml | maintained | spindle midzone |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0051233 | Focused validator passed. |
| Focused native strict | passed | True | GO:0051233 | Focused validator passed. |
| Native UniProt verify | passed | False | GO:0051233 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0051233 | Native command passed; scientific membership and graph scope assessed independently. |
| Claim-level scientific review | passed | True | GO:0051233 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:0051233 | 15 of 17 exact target identifiers returned OK. Residuals: PMID:11739794 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by midzone-agent-pmid-11739794; PMID:23001566 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by midzone-agent-pmid-23001566 The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:0051233 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0051233 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0051233 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0051233 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0051233 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

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

## Findings

### F1: Give the midzone a region-specific contribution to segregation

major / open / confirmed; issue key: midzone-whole-spindle-kinetochore-function-transfer.

The function and graph directly attach whole-spindle kinetochore-coupling prose to the midzone, citing the whole-spindle GO definition. Preserve the supported overlap identity and an appropriately qualified contribution to segregation, but describe the regional process actually supported by evidence instead of transferring the entire spindle mechanism.

### F2: Support the added midzone regulator mechanism at its taxon scope

major / open / confirmed; issue key: midzone-regulator-definition-source-scope.

The definition cites only GO0051233 while adding Ase1/PRC1, Cin8/Kip1 and chromosomal-passenger identities as an organizing mechanism across yeasts, fungi and microbial eukaryotes. Neither that GO definition nor the inspected primary morphology establishes the entire assertion. The claim needs a matching inspected source and organism/stage qualification.

### F3: Correct the GO attribution of the added synonym

minor / open / confirmed; issue key: midzone-go-synonym-provenance.

The maintained exact synonym central spindle overlap zone is not a synonym supplied by the inspected native GO0051233 record. GO instead supplies central spindle and spindle equator. Repair the provenance or use an actual source-provided synonym.

### F4: Match graph scope to the represented relationships

minor / open / confirmed; issue key: spindle_midzone_mechanism-static-graph-scope.

The FUNCTION graph contains structural parthood and whole-structure-to-process mediates edges. Its descriptions mention biological activities, but the graph does not connect an explicit assembly or functional transition to those activities. MECHANISTIC overstates what is represented; this is a scope classification concern, not a claim that the supported topology is false or a demand for atomic detail.

## Recommended Actions And Acceptance Checks

### A1

During authorized curation, qualify the midzone contribution using directly supported overlap/interpolar behavior, or route the broad kinetochore-coupling function through the whole-spindle node.

- Keep GO0051233 as the regional identity.
- Do not treat the generic spindle definition as proof of a region-specific molecular mechanism.
- Preserve source uncertainty about putative kinetochore fibers in the EM analysis.
- Run focused schema, strict-reference and causal-graph checks.

### A2

During authorized curation, provide source-specific evidence for each retained mechanistic grouping or narrow the definition to the supported overlap structure and bounded yeast behavior.

- Keep ontology and literature-derived statements distinguishable.
- Do not use unidentified ultrastructural crossbridges as identification of Ase1 or CPC.
- Do not infer a uniform molecular cohort across the named taxa.
- Run focused schema and strict-reference checks.

### A3

During authorized curation, use a native synonym or provide a genuine source for the curated phrase.

- Do not imply that GO supplied a string absent from its annotation.
- Preserve exact-versus-curated synonym distinction.
- Run focused schema and strict-reference checks.

### A4

During authorized curation, mark the current descriptive graph NONMECHANISTIC with a clear scope note, or represent a specific source-supported transition at an explicit organism and developmental scope.

- Keep supported identity and parthood relationships.
- Do not infer an assembly requirement merely from composition or localization.
- Any added mechanistic edge must cite the source that actually establishes that transition.
- Run focused schema, strict-reference and causal-graph validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/spindle_midzone.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| midzone-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0051233,GO:0072686,GO:0110165; All returned term identities, definitions, synonym annotations and relevant child relations: GO:0005819, GO:0005874, GO:0005876, GO:0007059, GO:0051233, GO:0072686, GO:0110165. GO0051233 exact synonyms are central spindle and spindle equator. | supports | Native definitions distinguish the target structure, its returned related structural classes and relevant processes. Exact returned synonyms and source-specific relations were checked separately from plausible curator-authored language. |
| midzone-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxon identity, rank and lineage | supports | Native taxonomy confirms the named organism and rank; broad clade occurrence is separate from a molecular mechanism established in one yeast. |
| midzone-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxon identity, rank and lineage | supports | Native taxonomy confirms the named organism and rank; broad clade occurrence is separate from a molecular mechanism established in one yeast. |
| midzone-agent-doi-annurev.cellbio.20.022003.114106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev.cellbio.20.022003.114106; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The budding yeast spindle pole body: structure, duplication, and function. Authors: Jaspersen SL, Winey M.; PMID 15473833; DOI 10.1146/annurev.cellbio.20.022003.114106. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| midzone-agent-jaspersen-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript browser extraction, pages5–10, displayed lines185–410: Introduction, SPB organization and core components. This is captured browser text; legacy metadata status200 is not an independently recorded native HTTP response. | supports | Jaspersen and Winey2004 is a review focused on the budding-yeast SPB, its layered structure and nuclear/cytoplasmic microtubule organization. The author manuscript is review-tier context rather than primary experimental proof for all eukaryotic poles. |
| midzone-agent-jaspersen-duplication-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript browser extraction: duplication/separation pages15–20, displayed lines619–705 and730–800; intervening omitted lines were not read. | supports | The review describes budding-yeast SPB duplication and bridge cleavage followed by Cin8/Kip1-dependent pole separation. This supports a scoped yeast pathway, not a uniform pole-duplication mechanism for every microbial eukaryote. |
| midzone-agent-jaspersen-nucleation-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author-manuscript browser extraction: pages24–26 displayed lines976–1077, and pages30–32 lines1213–1308. Read scope includes gamma-tubulin machinery and the SPB/centrosome comparison, not the entire review. | supports | The review treats Tub4/Spc97/Spc98 nucleation complexes, Spc110/Spc72 targeting and comparison with centrosomes. Similarities coexist with structural and duplication differences; mechanistic models and inferred minus-end capping retain their stated uncertainty. |
| midzone-agent-viswanath2017 | https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml; Native PMC5687031.1 JATS: complete Introduction including Figure1 caption. Additional initial Results were consulted but no conclusion here depends on a complete Results audit. | supports | Viswanath et al.2017 provides primary integrative structural work on the yeast SPB core. Its Introduction and Figure1 distinguish inner/outer plaques and gamma-TuSC assemblies; these contextual claims do not constitute an all-taxon pole census or universal molecular mechanism. |
| midzone-agent-P09733 | https://rest.uniprot.org/uniprotkb/P09733.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P09733 identifies Tubulin alpha-1 chain, gene TUB1, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| midzone-agent-query-TUB1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene TUB1, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P09733. This checks identifier resolution only. |
| midzone-agent-P02557 | https://rest.uniprot.org/uniprotkb/P02557.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P02557 identifies Tubulin beta chain, gene TUB2, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| midzone-agent-query-TUB2 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene TUB2, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P02557. This checks identifier resolution only. |
| midzone-agent-P09734 | https://rest.uniprot.org/uniprotkb/P09734.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P09734 identifies Tubulin alpha-3 chain, gene TUB3, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| midzone-agent-query-TUB3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene TUB3, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P09734. This checks identifier resolution only. |
| midzone-agent-doi-jcb.129.6.1601 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.129.6.1601; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Three-dimensional ultrastructural analysis of the Saccharomyces cerevisiae mitotic spindle. Authors: Winey M, Mamay CL, O'Toole ET, Mastronarde DN, Giddings TH, McDonald KL, McIntosh JR.; PMID 7790357; DOI 10.1083/jcb.129.6.1601. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| midzone-agent-doi-science.277.5325.574 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1126/science.277.5325.574; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Mitosis in living budding yeast: anaphase A but no metaphase plate. Authors: Straight AF, Marshall WF, Sedat JW, Murray AW.; PMID 9228009; DOI 10.1126/science.277.5325.574. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| midzone-agent-pmid-11739794 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11739794%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Dominant-lethal alpha-tubulin mutants defective in microtubule depolymerization in yeast. Authors: Anders KR, Botstein D.; PMID 11739794; DOI 10.1091/mbc.12.12.3973. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| midzone-agent-pmid-23001566 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A23001566%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies An inherited TUBB2B mutation alters a kinesin-binding site and causes polymicrogyria, CFEOM and axon dysinnervation. Authors: Cederquist GY, Luchniak A, Tischfield MA, Peeva M, Song Y, Menezes MP, Chan WM, Andrews C, Chew S, Jamieson RV, Gomes L, Flaherty M, Grant PE, Gupta ML, Engle EC.; PMID 23001566; DOI 10.1093/hmg/dds393. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| midzone-agent-IPR000217 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/; Complete native family metadata, description and hierarchy | context_only | Tubulin family IPR000217 includes more than alpha and beta tubulins, whereas IPR002452/2453 separately identify alpha and beta families. None is exact equivalence to the deliberately combined alpha/beta row. |
| midzone-agent-IPR002452 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/; Complete native family metadata, description and hierarchy | context_only | Tubulin family IPR000217 includes more than alpha and beta tubulins, whereas IPR002452/2453 separately identify alpha and beta families. None is exact equivalence to the deliberately combined alpha/beta row. |
| midzone-agent-IPR002453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; Complete native family metadata, description and hierarchy | context_only | Tubulin family IPR000217 includes more than alpha and beta tubulins, whereas IPR002452/2453 separately identify alpha and beta families. None is exact equivalence to the deliberately combined alpha/beta row. |
| midzone-agent-winey1995-pdf | https://pdfs.semanticscholar.org/cb33/a9630ccea6fbdd5e23d396df29c214465892.pdf; Genuine public manuscript PDF, complete scientific main text: Abstract, Introduction, Methods, Results, Discussion, TableI and main figure captions, printed pages1601–1614. Bibliography was not exhaustively read. S288c and an S288c-background diploid, mid-log growth30C, high-pressure freezing/freeze substitution and serial sections; no raw-data reanalysis. | supports | Winey et al.1995 reconstruct15 yeast nuclear spindles by serial-section EM. Interpolar/putative kinetochore assignments and crossbridges are morphological interpretations; the paper does not identify Ase1/CPC molecular mechanisms. Its Introduction explicitly excludes astral microtubules from the spindle per se, unlike the broader GO convention. |
| schema-result | just validate data/structures/cytoskeleton/spindle_midzone.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/spindle_midzone.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/spindle_midzone.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_midzone-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/spindle_midzone.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_midzone-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_midzone-strict.tsv |
| native-verify | /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_midzone.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_midzone.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/cytoskeleton/spindle_midzone.yaml  (GO:0051233)<br>  spindle_midzone_mechanism	alpha_beta_tubulins	COVERED	-&gt;alpha_beta_tubulins (UniProtKB:P09733, UniProtKB:P02557, UniProtKB:P09734)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| target-curies-result | just check-curies-strict; data/structures/cytoskeleton/spindle_midzone.yaml; exact native collect() target slice of original fresh-base TSV | supports | 15 of 17 exact target identifiers returned OK. Residuals: PMID:11739794 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by midzone-agent-pmid-11739794; PMID:23001566 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by midzone-agent-pmid-23001566 The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Jaspersen and Winey2004 is review-tier evidence read through the listed author-manuscript browser extracts, not a complete native publisher full-text download. Original captured times/hashes are retained; legacy status200 on one extraction does not attest to a native HTTP response.
- Viswanath2017 is used for its Introduction/Figure1 yeast-SPB structural context. No claim of a full Results audit, all-eukaryote census or primary proof for every introductory statement is made.
- Winey1995 full scientific main text/captions/TableI were read from a genuine PDF. Kinetochore versus interpolar assignments include morphological inference; molecular identities of observed crossbridges are not established. Its analytic use of midzone should not be reduced to a claim that no kinetochore-associated ends can ever occupy the central region.
- Straight1997 was read at native abstract/metadata scope only. The publisher route returned403 and bounded public searches did not recover a genuine full body. The abstract directly describes GFP-Tub1 imaging, chromosome tracking and biphasic spindle elongation; more specific molecular claims are not inferred from it.
- Anders2001 and Cederquist2012 were read at native metadata/abstract and UniProt annotation scope only. Exact identities/localization attributions are supported; complete assembly necessity, regional occupancy and all-taxon mechanistic conservation remain unverified.
- The combined alpha/beta class is not exactly represented by broad IPR000217 or by either individual alpha/beta family. No mandatory component split, complete regulator census, image or numerical property is imposed.
- The regional microtubule-part wording should be understood as overlap portions, not every entire spindle fiber. No new ontology relation is inferred solely from colocalization or from the whole-spindle definition.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All13 fresh batch16 inspection input hashes verified; focused schema/strict and native UniProt checks passed.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094824Z-spindle-midzone-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Spindle midzone versus whole-spindle function and evidence review
started_at: '2026-10-21T09:24:30Z'
finished_at: '2026-10-21T09:48:24Z'
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
summary: The overlap-region identity and concrete tubulin examples are sound. Two
  major corrections concern whole-spindle functional transfer and unsupported specific
  regulator mechanism; two minor corrections concern synonym provenance and graph
  scope.
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
  - path: data/structures/cytoskeleton/spindle_midzone.yaml
    sha256: 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661
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
- target_id: GO:0051233
  path: data/structures/cytoskeleton/spindle_midzone.yaml
  label: spindle midzone
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
scope:
  description: Entire single target, regional identity and component boundaries, native
    families/proteins/taxa/synonyms, readable primary morphology, scoped live-imaging
    abstract and review context, every function and graph edge.
  selection: Ninth selected target in batch sixteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0051233
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0051233
  command: just validate data/structures/cytoskeleton/spindle_midzone.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0051233
  command: just validate-strict data/structures/cytoskeleton/spindle_midzone.yaml
    --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_midzone-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0051233
  command: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_midzone.yaml
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
  - GO:0051233
  command: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_midzone.yaml
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
  - GO:0051233
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - midzone-agent-go
  - midzone-agent-tax-4932
  - midzone-agent-tax-559292
  - midzone-agent-doi-annurev.cellbio.20.022003.114106
  - midzone-agent-jaspersen-browser
  - midzone-agent-jaspersen-duplication-browser
  - midzone-agent-jaspersen-nucleation-browser
  - midzone-agent-viswanath2017
  - midzone-agent-P09733
  - midzone-agent-query-TUB1
  - midzone-agent-P02557
  - midzone-agent-query-TUB2
  - midzone-agent-P09734
  - midzone-agent-query-TUB3
  - midzone-agent-doi-jcb.129.6.1601
  - midzone-agent-doi-science.277.5325.574
  - midzone-agent-pmid-11739794
  - midzone-agent-pmid-23001566
  - midzone-agent-IPR000217
  - midzone-agent-IPR002452
  - midzone-agent-IPR002453
  - midzone-agent-winey1995-pdf
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:0051233
  summary: '15 of 17 exact target identifiers returned OK. Residuals: PMID:11739794
    returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently
    verified by midzone-agent-pmid-11739794; PMID:23001566 returned UNREACHABLE (eutils
    HTTP414); exact native PMID metadata independently verified by midzone-agent-pmid-23001566
    The shared command exit zero is not interpreted as successful network resolution
    for transport failures.'
  evidence_ids:
  - target-curies-result
  - midzone-agent-pmid-11739794
  - midzone-agent-pmid-23001566
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0051233
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
  - GO:0051233
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
  - GO:0051233
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
  - GO:0051233
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
  - GO:0051233
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
  reference: data/structures/cytoskeleton/spindle_midzone.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T09:37:03Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:37:03Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: midzone-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005819,GO:0005874,GO:0005876,GO:0007059,GO:0051233,GO:0072686,GO:0110165
  locator: 'All returned term identities, definitions, synonym annotations and relevant
    child relations: GO:0005819, GO:0005874, GO:0005876, GO:0007059, GO:0051233, GO:0072686,
    GO:0110165. GO0051233 exact synonyms are central spindle and spindle equator.'
  accessed_at: '2026-10-21T09:25:56.901671Z'
  support: supports
  summary: Native definitions distinguish the target structure, its returned related
    structural classes and relevant processes. Exact returned synonyms and source-specific
    relations were checked separately from plausible curator-authored language.
  snapshot_sha256: 6f51431934e0b34753609506bccef31f6d6165cb993a64547a8495cfc78b0a97
- evidence_id: midzone-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:25:57.022371Z'
  support: supports
  summary: Native taxonomy confirms the named organism and rank; broad clade occurrence
    is separate from a molecular mechanism established in one yeast.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: midzone-agent-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:25:57.049516Z'
  support: supports
  summary: Native taxonomy confirms the named organism and rank; broad clade occurrence
    is separate from a molecular mechanism established in one yeast.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: midzone-agent-doi-annurev.cellbio.20.022003.114106
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev.cellbio.20.022003.114106
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:25:58.978444Z'
  support: supports
  summary: 'Native metadata identifies The budding yeast spindle pole body: structure,
    duplication, and function. Authors: Jaspersen SL, Winey M.; PMID 15473833; DOI
    10.1146/annurev.cellbio.20.022003.114106. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: efa766051d38f45bd9e4159bbbb7baf72a1958fd54dc81c63c488d70f1762d03
- evidence_id: midzone-agent-jaspersen-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Author-manuscript browser extraction, pages5–10, displayed lines185–410:
    Introduction, SPB organization and core components. This is captured browser text;
    legacy metadata status200 is not an independently recorded native HTTP response.'
  accessed_at: '2026-10-21T07:24:18Z'
  support: supports
  summary: Jaspersen and Winey2004 is a review focused on the budding-yeast SPB, its
    layered structure and nuclear/cytoplasmic microtubule organization. The author
    manuscript is review-tier context rather than primary experimental proof for all
    eukaryotic poles.
  snapshot_sha256: 8aa2398ded5512b2450c936e832c11bc46d77ac317e4c01a2f7a6b9f1a4fce4e
- evidence_id: midzone-agent-jaspersen-duplication-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Author-manuscript browser extraction: duplication/separation pages15–20,
    displayed lines619–705 and730–800; intervening omitted lines were not read.'
  accessed_at: '2026-10-21T07:40:49Z'
  support: supports
  summary: The review describes budding-yeast SPB duplication and bridge cleavage
    followed by Cin8/Kip1-dependent pole separation. This supports a scoped yeast
    pathway, not a uniform pole-duplication mechanism for every microbial eukaryote.
  snapshot_sha256: 4995a36ec89d47c8e1fe3cf967df63ac1f3c357d9e16d69dd2b01c22408b7d05
- evidence_id: midzone-agent-jaspersen-nucleation-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: 'Author-manuscript browser extraction: pages24–26 displayed lines976–1077,
    and pages30–32 lines1213–1308. Read scope includes gamma-tubulin machinery and
    the SPB/centrosome comparison, not the entire review.'
  accessed_at: '2026-10-21T07:43:49.372408Z'
  support: supports
  summary: The review treats Tub4/Spc97/Spc98 nucleation complexes, Spc110/Spc72 targeting
    and comparison with centrosomes. Similarities coexist with structural and duplication
    differences; mechanistic models and inferred minus-end capping retain their stated
    uncertainty.
  snapshot_sha256: 5c038e01761413d522e0ea145ffefb28f289f6f2f5cc3b55c8deb377bf2aa0cf
- evidence_id: midzone-agent-viswanath2017
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC5687031.1/PMC5687031.1.xml
  locator: 'Native PMC5687031.1 JATS: complete Introduction including Figure1 caption.
    Additional initial Results were consulted but no conclusion here depends on a
    complete Results audit.'
  accessed_at: '2026-10-20T07:38:52.830471Z'
  support: supports
  summary: Viswanath et al.2017 provides primary integrative structural work on the
    yeast SPB core. Its Introduction and Figure1 distinguish inner/outer plaques and
    gamma-TuSC assemblies; these contextual claims do not constitute an all-taxon
    pole census or universal molecular mechanism.
  snapshot_sha256: 004836a027b7fad21def4f6e9eebc94ec5f1e07679d123407a062241f6edb580
- evidence_id: midzone-agent-P09733
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09733.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:25:57.621826Z'
  support: supports
  summary: Native reviewed UniProtKB P09733 identifies Tubulin alpha-1 chain, gene
    TUB1, taxon559292. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: aed535980dd8ac2307085497de3917488ff4f5da0252812d09d17d17c739b426
- evidence_id: midzone-agent-query-TUB1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene TUB1, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:25:57.746041Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P09733. This checks identifier
    resolution only.
  snapshot_sha256: ab3ef6eb4aba30b014094695c817ac553dcd2c55c6f8feda6c32fae65e55e16c
  search_scope: UniProtKB query gene_exact:TUB1 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: midzone-agent-P02557
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P02557.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:25:57.311229Z'
  support: supports
  summary: Native reviewed UniProtKB P02557 identifies Tubulin beta chain, gene TUB2,
    taxon559292. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: d22cba0cfbb4aaa448114cc4356c81a4f7116a79ee7359a05b69dfd659d6b646
- evidence_id: midzone-agent-query-TUB2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene TUB2, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:25:57.953665Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P02557. This checks identifier
    resolution only.
  snapshot_sha256: 4d1049116e3e865676ca2a31ed8f01bdd757d3cad4b28b84933b5903876ea148
  search_scope: UniProtKB query gene_exact:TUB2 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: midzone-agent-P09734
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09734.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:25:57.639331Z'
  support: supports
  summary: Native reviewed UniProtKB P09734 identifies Tubulin alpha-3 chain, gene
    TUB3, taxon559292. Concrete identity is checked independently of membership; relevant
    subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 0a6865ddaa8955d9ccdc57056008255b39a4ab55d5b75e640a37a0206c197b67
- evidence_id: midzone-agent-query-TUB3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ATUB3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene TUB3, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:25:58.256813Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P09734. This checks identifier
    resolution only.
  snapshot_sha256: 1e154b62a419986ae1256476fa07411bfb9f6cc39e678a36cd482cc505e8e62e
  search_scope: UniProtKB query gene_exact:TUB3 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: midzone-agent-doi-jcb.129.6.1601
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.129.6.1601
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:25:58.577701Z'
  support: supports
  summary: 'Native metadata identifies Three-dimensional ultrastructural analysis
    of the Saccharomyces cerevisiae mitotic spindle. Authors: Winey M, Mamay CL, O''Toole
    ET, Mastronarde DN, Giddings TH, McDonald KL, McIntosh JR.; PMID 7790357; DOI
    10.1083/jcb.129.6.1601. Bibliographic identity and available abstract only; not
    a substitute for inspected article body.'
  snapshot_sha256: 5f72dc2bd259f645d3040a785ce2272074b4076ee1deee2820baa3ecc6a1b4bc
- evidence_id: midzone-agent-doi-science.277.5325.574
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1126/science.277.5325.574
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:25:58.903093Z'
  support: supports
  summary: 'Native metadata identifies Mitosis in living budding yeast: anaphase A
    but no metaphase plate. Authors: Straight AF, Marshall WF, Sedat JW, Murray AW.;
    PMID 9228009; DOI 10.1126/science.277.5325.574. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 85e5bb2644f5eb8b678b868051d04585c6585435bc1a03ca4913aaadce2fa9ae
- evidence_id: midzone-agent-pmid-11739794
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11739794%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:25:58.283022Z'
  support: supports
  summary: 'Native metadata identifies Dominant-lethal alpha-tubulin mutants defective
    in microtubule depolymerization in yeast. Authors: Anders KR, Botstein D.; PMID
    11739794; DOI 10.1091/mbc.12.12.3973. Bibliographic identity and available abstract
    only; not a substitute for inspected article body.'
  snapshot_sha256: 746729054aacbc6190795b8b43f8259b9252dc99aa8ec9894447a2f4e33e42b3
- evidence_id: midzone-agent-pmid-23001566
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A23001566%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:25:58.379637Z'
  support: supports
  summary: 'Native metadata identifies An inherited TUBB2B mutation alters a kinesin-binding
    site and causes polymicrogyria, CFEOM and axon dysinnervation. Authors: Cederquist
    GY, Luchniak A, Tischfield MA, Peeva M, Song Y, Menezes MP, Chan WM, Andrews C,
    Chew S, Jamieson RV, Gomes L, Flaherty M, Grant PE, Gupta ML, Engle EC.; PMID
    23001566; DOI 10.1093/hmg/dds393. Bibliographic identity and available abstract
    only; not a substitute for inspected article body.'
  snapshot_sha256: 11012dca34504a5eb2b11d689f0a93e4ce4338b23cc03fb67b1d2289c64726c1
- evidence_id: midzone-agent-IPR000217
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/
  locator: Complete native family metadata, description and hierarchy
  accessed_at: '2026-10-21T09:25:59.199622Z'
  support: context_only
  summary: Tubulin family IPR000217 includes more than alpha and beta tubulins, whereas
    IPR002452/2453 separately identify alpha and beta families. None is exact equivalence
    to the deliberately combined alpha/beta row.
  snapshot_sha256: ddbf902c6495d576d69c82c85daf1bdf2bc9fea5894925a4efcd87dc45ea3170
- evidence_id: midzone-agent-IPR002452
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/
  locator: Complete native family metadata, description and hierarchy
  accessed_at: '2026-10-21T09:25:59.838123Z'
  support: context_only
  summary: Tubulin family IPR000217 includes more than alpha and beta tubulins, whereas
    IPR002452/2453 separately identify alpha and beta families. None is exact equivalence
    to the deliberately combined alpha/beta row.
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
- evidence_id: midzone-agent-IPR002453
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: Complete native family metadata, description and hierarchy
  accessed_at: '2026-10-21T09:26:00.358326Z'
  support: context_only
  summary: Tubulin family IPR000217 includes more than alpha and beta tubulins, whereas
    IPR002452/2453 separately identify alpha and beta families. None is exact equivalence
    to the deliberately combined alpha/beta row.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: midzone-agent-winey1995-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/cb33/a9630ccea6fbdd5e23d396df29c214465892.pdf
  locator: 'Genuine public manuscript PDF, complete scientific main text: Abstract,
    Introduction, Methods, Results, Discussion, TableI and main figure captions, printed
    pages1601–1614. Bibliography was not exhaustively read. S288c and an S288c-background
    diploid, mid-log growth30C, high-pressure freezing/freeze substitution and serial
    sections; no raw-data reanalysis.'
  accessed_at: '2026-10-21T09:26:34.825251Z'
  support: supports
  summary: Winey et al.1995 reconstruct15 yeast nuclear spindles by serial-section
    EM. Interpolar/putative kinetochore assignments and crossbridges are morphological
    interpretations; the paper does not identify Ase1/CPC molecular mechanisms. Its
    Introduction explicitly excludes astral microtubules from the spindle per se,
    unlike the broader GO convention.
  snapshot_sha256: fbf7dccc8b63812b7a8adb44b11b723160921e874a48d27c738971d0109fc251
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/spindle_midzone.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:36Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/spindle_midzone.yaml'
  snapshot_sha256: a7796f4db7ecee278a58f7cb98122dbf47e211447eb9cc1a79e5300bc647117a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/spindle_midzone.yaml
    --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_midzone-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:39Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/spindle_midzone.yaml\
    \ --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_midzone-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/spindle_midzone-strict.tsv"
  snapshot_sha256: 7cd6620ec903b17e8d0c2492d34af684258fa39d05de6b5ee2eb3847b343b0a2
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_midzone.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T09:26:40.703331Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/spindle_midzone.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T09:26:41.414353Z'
  support: supports
  summary: "data/structures/cytoskeleton/spindle_midzone.yaml  (GO:0051233)\n  spindle_midzone_mechanism\t\
    alpha_beta_tubulins\tCOVERED\t->alpha_beta_tubulins (UniProtKB:P09733, UniProtKB:P02557,\
    \ UniProtKB:P09734)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 3c3326f9d74445c69ed8da08c6b63c4f562e40b1c9996e92824354c3d7bce271
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/spindle_midzone.yaml; exact native collect()
    target slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:48:00.612588Z'
  support: supports
  summary: '15 of 17 exact target identifiers returned OK. Residuals: PMID:11739794
    returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently
    verified by midzone-agent-pmid-11739794; PMID:23001566 returned UNREACHABLE (eutils
    HTTP414); exact native PMID metadata independently verified by midzone-agent-pmid-23001566
    The shared command exit zero is not interpreted as successful network resolution
    for transport failures.'
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
  topic: Overlap region is distinct from the entire spindle
  outcome: supported
  target_ids:
  - GO:0051233
  summary: GO0051233 identifies the region where microtubules from opposite poles
    overlap; its spindle parthood is correct. Microtubule segments occupy the overlap,
    but not every spindle microtubule is thereby wholly contained in the midzone.
    The record should retain this regional boundary when describing parts.
  evidence_ids:
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - record
- assessment_id: tubulin-identity
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
  - midzone-agent-P09733
  - midzone-agent-P02557
  - midzone-agent-P09734
  - midzone-agent-IPR000217
  - midzone-agent-IPR002452
  - midzone-agent-IPR002453
  - midzone-agent-tax-4932
  - midzone-agent-tax-559292
  - record
  - policy
- assessment_id: annotation-evidence
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
  - midzone-agent-P09733
  - midzone-agent-P02557
  - midzone-agent-P09734
  - midzone-agent-pmid-11739794
  - midzone-agent-pmid-23001566
  - record
- assessment_id: assembly-necessity
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
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - midzone-agent-doi-science.277.5325.574
  - midzone-agent-P09733
  - midzone-agent-P02557
  - midzone-agent-P09734
  - policy
  - record
- assessment_id: function-transfer
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
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - midzone-agent-doi-science.277.5325.574
  - record
- assessment_id: definition-mechanism
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
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - midzone-agent-jaspersen-duplication-browser
  - record
- assessment_id: synonym
  area: provenance
  topic: A plausible phrase is not a source-provided exact synonym
  outcome: concern
  target_ids:
  - GO:0051233
  summary: Native GO0051233 contains central spindle and spindle equator as exact
    synonyms. It does not supply the maintained central spindle overlap zone string.
    The phrase can be curated independently, but its current GO attribution is inaccurate.
  evidence_ids:
  - midzone-agent-go
  - record
- assessment_id: occurrence
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
  - midzone-agent-winey1995-pdf
  - midzone-agent-tax-4932
  - midzone-agent-tax-559292
  - record
- assessment_id: graph-scope
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
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - policy
  - record
- assessment_id: completeness
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
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - policy
  - record
findings:
- finding_id: F1
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
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - midzone-agent-doi-science.277.5325.574
  - record
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
- finding_id: F2
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
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - midzone-agent-jaspersen-duplication-browser
  - record
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
- finding_id: F3
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
  - midzone-agent-go
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: This is a non-blocking provenance error; the phrase does not
    change the target overlap-region identity.
- finding_id: F4
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
  - midzone-agent-go
  - midzone-agent-winey1995-pdf
  - policy
  - record
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
actions:
- action_id: A1
  finding_ids:
  - F1
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
- action_id: A2
  finding_ids:
  - F2
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
- action_id: A3
  finding_ids:
  - F3
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
- action_id: A4
  finding_ids:
  - F4
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
limitations:
- Jaspersen and Winey2004 is review-tier evidence read through the listed author-manuscript
  browser extracts, not a complete native publisher full-text download. Original captured
  times/hashes are retained; legacy status200 on one extraction does not attest to
  a native HTTP response.
- Viswanath2017 is used for its Introduction/Figure1 yeast-SPB structural context.
  No claim of a full Results audit, all-eukaryote census or primary proof for every
  introductory statement is made.
- Winey1995 full scientific main text/captions/TableI were read from a genuine PDF.
  Kinetochore versus interpolar assignments include morphological inference; molecular
  identities of observed crossbridges are not established. Its analytic use of midzone
  should not be reduced to a claim that no kinetochore-associated ends can ever occupy
  the central region.
- Straight1997 was read at native abstract/metadata scope only. The publisher route
  returned403 and bounded public searches did not recover a genuine full body. The
  abstract directly describes GFP-Tub1 imaging, chromosome tracking and biphasic spindle
  elongation; more specific molecular claims are not inferred from it.
- Anders2001 and Cederquist2012 were read at native metadata/abstract and UniProt
  annotation scope only. Exact identities/localization attributions are supported;
  complete assembly necessity, regional occupancy and all-taxon mechanistic conservation
  remain unverified.
- The combined alpha/beta class is not exactly represented by broad IPR000217 or by
  either individual alpha/beta family. No mandatory component split, complete regulator
  census, image or numerical property is imposed.
- The regional microtubule-part wording should be understood as overlap portions,
  not every entire spindle fiber. No new ontology relation is inferred solely from
  colocalization or from the whole-spindle definition.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- All13 fresh batch16 inspection input hashes verified; focused schema/strict and
  native UniProt checks passed.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
