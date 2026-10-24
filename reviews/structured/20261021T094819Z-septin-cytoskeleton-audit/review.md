# Septin cytoskeleton identity, family grounding and graph scope review

- Review: 20261021T094819Z-septin-cytoskeleton-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:24:23Z
- Finished UTC: 2026-10-21T09:48:19Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-cytoskeleton identity, developmental examples and all five concrete protein identities are supported. One major correction concerns the expanded definition’s taxon/function evidence scope; two minor corrections concern generic Septin-family grounding and descriptive graph scope.

## Scope And Provenance

Entire single target, native ontology/family/taxon/protein identities, every component and graph claim, stage-specific membership and primary-versus-review source scope.

Selection: Seventh selected target in batch sixteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032156 | data/structures/cytoskeleton/septin_cytoskeleton.yaml | maintained | septin cytoskeleton |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032156 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032156 | Focused validator passed. |
| Native UniProt verify | passed | False | GO:0032156 | Native command passed; scientific membership and graph scope assessed independently. |
| Native UniProt causal-graphs | passed | False | GO:0032156 | Native command passed; scientific membership and graph scope assessed independently. |
| Claim-level scientific review | passed | True | GO:0032156 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Target resolver slice with native transport-failure cross-checks | passed | True | GO:0032156 | 16 of 19 exact target identifiers returned OK. Residuals: PMID:14562095 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by septin-agent-pmid-14562095; PMID:25971666 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by septin-agent-pmid-25971666; PMID:9790978 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by septin-agent-pmid-9790978 The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| Full corpus QC | passed | True | GO:0032156 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032156 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032156 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032156 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032156 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole cytoskeleton and specialized septin assemblies

identity: supported. Targets: GO:0032156.

The GO identity, cytoskeleton parent and declared structural parts are consistent. FILAMENT is a broad local kind classification; the text explicitly includes higher-order complexes and arrays and does not equate the entire framework with a single oligomer.

### An exact generic family is available

grounding: concern. Targets: GO:0032156.

The REVIEWED_LABEL_ONLY rationale requires a family identifier for a complete filament-array-forming cohort. The component itself is the generic septin-proteins class, for which IPR016491 is exact. Family identity does not require an exact inventory of proteins occupying each array.

### Correct vegetative examples remain valid at the broader target scope

evidence: supported. Targets: GO:0032156.

All five reviewed gene/accession/taxon identities are correct. Native UniProt annotations support the specifically attributed Huh, Finnigan and Mino localization notes. Finnigan provides directly read bud-neck experiments; the two other cited papers were metadata/abstract- and native-annotation-scoped. Vegetative members are valid examples for the whole cytoskeleton even though the canonical array examples describe spores.

### Expanded architecture and functions exceed the cited taxon scope

scope: concern. Targets: GO:0032156.

The definition attributes a cortical network to yeasts, filamentous fungi and green algae, then assigns scaffold/barrier and recruitment functions across several sites. Versele S1/P2 supports green-algal ortholog occurrence only; S2/P5 supports yeast roles. Douglas sec18 treats branch-site regulator recruitment as a suggestion, and sec14 distinguishes observed sporulation scaffolding from proposed spore-wall recruitment. Finnigan directly tests vegetative yeast Bni5/Myo1 recruitment. These sources do not support the full combined defining extension, whose sole definition_source is GO. The five-gene parenthesis is treated as a member list, not an ordered rod.

### Developmental examples are nonexhaustive

scope: supported. Targets: GO:0032156.

The two VARIABLE entries explicitly describe sporulation/chlamydospore arrays, supported by their GO child definitions and review context. They do not say that the entire septin cytoskeleton is absent in vegetative cells. No species-wide percentage or exclusive spore membership is inferred.

### Collective material versus individual assembly requirement

evidence: unknown. Targets: GO:0032156.

ESSENTIAL is attached to the whole septin class, not separately to each of the five examples. Septins are defining material of the target, but the cited studies do not constitute removal of the whole class followed by an assembly assay. Individual truncation, viability or recruitment results cannot verify a five-gene universal assembly requirement; none is inferred.

### Supported parthood is not an assembly transition

graph: concern. Targets: GO:0032156.

The three edges record septin-protein, complex and band parthood. They do not describe how assembly happens, despite ASSEMBLY/MECHANISTIC and the mechanism title. Classify the existing descriptive scope accurately or encode a bounded supported transition.

### No mandatory exhaustive inventory

completeness: supported. Targets: GO:0032156.

The broad framework is represented through generic proteins and named substructures. Additional subunit groups, images, functions or quantitative dimensions are optional. The concrete gaps are unjustified generic-family withholding and source/taxon inflation in the expanded definition; specialized composition should not be promoted to a universal cytoskeleton inventory.

## Findings

### F1: Ground the generic septin class at its actual family scope

minor / open / confirmed; issue key: septin-cytoskeleton-generic-family-withheld.

The generic septin-proteins row is REVIEWED_LABEL_ONLY because no identifier was assigned for the complete filament-array-forming cohort. Native IPR016491 identifies the Septin family, matching this generic component without identifying every assembly-specific member. Correct the class-versus-cohort criterion and preserve source-specific membership limits.

### F2: Match graph scope to the represented relationships

minor / open / confirmed; issue key: septin_cytoskeleton_mechanism-static-graph-scope.

The ASSEMBLY graph contains only constituent-to-cytoskeleton parthood edges. Its descriptions mention biological activities, but the graph does not connect an explicit assembly or functional transition to those activities. MECHANISTIC overstates what is represented; this is a scope classification concern, not a claim that the supported topology is false or a demand for atomic detail.

### F3: Separate supported fungal functions from unverified green-algal architecture

major / open / confirmed; issue key: septin-cytoskeleton-definition-taxon-function-scope.

The expanded definition presents a plasma-membrane septin network across yeasts, filamentous fungi and green algae and combines barrier/scaffold recruitment at bud necks, hyphal branches and prospore membranes, while definition_source cites only GO0032156. Versele supports green-algal septin ortholog occurrence, not that full cortical architecture or function. Its functional examples concern yeast; Douglas retains proposal-level language for branch regulator and spore-wall recruitment, and Finnigan directly studies vegetative budding yeast. Supply matching evidence and qualifiers for the retained expansion rather than carrying these narrower observations across the entire taxon/site list.

## Recommended Actions And Acceptance Checks

### A1

During authorized curation, assign IPR016491 to the generic septin-proteins row and explain that family membership does not establish a complete assembly-specific cohort.

- Retain the correct five reviewed protein examples at whole-cytoskeleton scope.
- Do not equate vegetative and sporulation-specific subunit inventories.
- Do not replace the family with a broader GTPase domain.
- Run focused schema, strict-reference and native protein checks.

### A2

During authorized curation, mark the current descriptive graph NONMECHANISTIC with a clear scope note, or represent a specific source-supported transition at an explicit organism and developmental scope.

- Keep supported identity and parthood relationships.
- Do not infer an assembly requirement merely from composition or localization.
- Any added mechanistic edge must cite the source that actually establishes that transition.
- Run focused schema, strict-reference and causal-graph validation.

### A3

During authorized curation, distinguish the native GO definition, source-specific fungal functions and green-algal ortholog evidence; qualify proposed recruitment roles or obtain directly matching evidence.

- Do not promote gene occurrence to a demonstrated cortical network or its molecular functions.
- Preserve budding-yeast versus filamentous-fungal versus sporulation scope and observed-versus-proposed distinctions.
- Keep the correct broad cytoskeleton identity and valid vegetative protein examples.
- Run focused schema, strict-reference and scientific evidence checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/septin_cytoskeleton.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| septin-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0031105,GO:0032156,GO:0032158,GO:0032160,GO:0032161,GO:0032165,GO:0032166; All returned native terms, definitions, synonyms and relevant is_a/part_of child relations, including GO0032156/0032160/0032165/0032166 | supports | Native GO identifies the septin cytoskeleton as the broader framework including septins, associated proteins and complexes. Septin complexes, bands, cleavage apparatus and filament-array subtypes remain distinct constituent identities. The specialized array examples do not exhaust the parent cytoskeleton. |
| septin-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxon identity, rank and lineage | supports | This native receipt identifies Saccharomyces cerevisiae, species. It attests only this taxon identity/rank, not occurrence or the experimental stock used in a paper. |
| septin-agent-tax-5476 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5476; Complete native taxon identity, rank and lineage | supports | This native receipt identifies Candida albicans, species. It attests only this taxon identity/rank, not occurrence or the experimental stock used in a paper. |
| septin-agent-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxon identity, rank and lineage | supports | This native receipt identifies Saccharomyces cerevisiae S288C, strain. It attests only this taxon identity/rank, not occurrence or the experimental stock used in a paper. |
| septin-agent-P32457 | https://rest.uniprot.org/uniprotkb/P32457.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P32457 identifies Cell division control protein 3, gene CDC3, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| septin-agent-query-CDC3 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ACDC3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene CDC3, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P32457. This checks identifier resolution only. |
| septin-agent-P25342 | https://rest.uniprot.org/uniprotkb/P25342.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P25342 identifies Cell division control protein 10, gene CDC10, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| septin-agent-query-CDC10 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ACDC10%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene CDC10, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P25342. This checks identifier resolution only. |
| septin-agent-P32458 | https://rest.uniprot.org/uniprotkb/P32458.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P32458 identifies Cell division control protein 11, gene CDC11, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| septin-agent-query-CDC11 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ACDC11%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene CDC11, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P32458. This checks identifier resolution only. |
| septin-agent-P32468 | https://rest.uniprot.org/uniprotkb/P32468.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB P32468 identifies Cell division control protein 12, gene CDC12, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| septin-agent-query-CDC12 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ACDC12%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene CDC12, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns P32468. This checks identifier resolution only. |
| septin-agent-Q07657 | https://rest.uniprot.org/uniprotkb/Q07657.json; primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR LOCATION comments and cited references where relevant | supports | Native reviewed UniProtKB Q07657 identifies Seventh homolog of septin 1, gene SHS1, taxon559292. Concrete identity is checked independently of membership; relevant subunit/cofactor/location comments retain their own evidence scope. |
| septin-agent-query-SHS1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;query=%28gene_exact%3ASHS1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29; All returned results for exact gene SHS1, organism 559292, reviewed:true; bounded to this query | context_only | Exact gene/taxon/reviewed query returns Q07657. This checks identifier resolution only. |
| septin-agent-IPR016491 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Complete native entry metadata, name, type family and description | supports | IPR016491 is the Septin family. Its generic family scope matches the generic septin-proteins component; it is not a claim of a complete localized cohort, exact rod composition or source-specific stoichiometry. |
| septin-agent-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A14562095%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Global analysis of protein localization in budding yeast. Authors: Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.; PMID 14562095; DOI 10.1038/nature02026. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| septin-agent-pmid-25971666 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A25971666%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The Carboxy-Terminal Tails of Septins Cdc11 and Shs1 Recruit Myosin-II Binding Factor Bni5 to the Bud Neck in Saccharomyces cerevisiae. Authors: Finnigan GC, Booth EA, Duvalyan A, Liao EN, Thorner J.; PMID 25971666; DOI 10.1534/genetics.115.176503. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| septin-agent-pmid-9790978 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9790978%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Shs1p: a novel member of septin that interacts with spa2p, involved in polarized growth in saccharomyces cerevisiae. Authors: Mino A, Tanaka K, Kamei T, Umikawa M, Fujiwara T, Takai Y.; PMID 9790978; DOI 10.1006/bbrc.1998.9541. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| septin-agent-versele2005-correct-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A16009555%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Some assembly required: yeast septins provide the instruction manual. Authors: Versele M, Thorner J.; PMID 16009555; DOI 10.1016/j.tcb.2005.06.007. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| septin-agent-douglas2005-correct-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A16151244%20AND%20SRC%3AMED; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Septin function in yeast model systems and pathogenic fungi. Authors: Douglas LM, Alvarez FJ, McCreary C, Konopka JB.; PMID 16151244; DOI 10.1128/ec.4.9.1503-1512.2005. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| septin-agent-versele-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render; PMC1761124: Introduction S1/P2, Figures1/2 captions, Table1; section2 Functions including P5 scaffold/barrier examples, section3 budding-yeast complex assembly and4 fission yeast. Historical interaction models are not treated as a current exact subunit order. | supports | Versele and Thorner2005 is review-tier synthesis of septin structure, diverse assemblies and barrier/scaffold functions. It distinguishes the five vegetative budding-yeast septins from sporulation-specific members; green-algal ortholog presence does not itself establish the whole cortical architecture claimed here. |
| septin-agent-douglas-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/; PMC1214204: sections5 scaffold overview and7 chitin deposition; section9 including barrier subsections10/11; section14 sporulation; sections17 Candida albicans and18 Aspergillus nidulans. Other sections are not claimed as fully read in this audit. | supports | Douglas et al.2005 reviews fungal diffusion barriers, sporulation and morphogenesis. Its stage-specific arrays support the named examples without confining the whole septin cytoskeleton to those developmental stages. |
| septin-agent-finnigan2015-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC4512547/?pdf=render; Genuine PMC4512547 HTML: Abstract, complete unsectioned Introduction; Methods Culture conditions and Fluorescence/DIC microscopy; Results Shs1 CTE recruitment section including Figure7; Discussion subsections13,14,16,17 including Figure8 caption. Other Results, strain tables and supplements were not fully audited. | supports | Finnigan et al.2015 experimentally links the Cdc11/Shs1 terminal extensions to Bni5 recruitment and Myo1 localization at the vegetative bud neck. Cdc11 and Shs1 are alternative terminal subunits; retained structures and partial recruitment distinguish assembly from downstream function. |
| schema-result | just validate data/structures/cytoskeleton/septin_cytoskeleton.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/septin_cytoskeleton.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/septin_cytoskeleton.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/septin_cytoskeleton-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/septin_cytoskeleton.yaml --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/septin_cytoskeleton-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/septin_cytoskeleton-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/septin_cytoskeleton.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 16 of19 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:14562095: UNREACHABLE; resolved by evidence septin-agent-pmid-14562095; PMID:25971666: UNREACHABLE; resolved by evidence septin-agent-pmid-25971666; PMID:9790978: UNREACHABLE; resolved by evidence septin-agent-pmid-9790978. Source-native identity checked separately. |
| native-verify | /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/septin_cytoskeleton.yaml --verify; Captured focused native verify log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/septin_cytoskeleton.yaml --causal-graphs; Captured focused native causal-graphs log | supports | data/structures/cytoskeleton/septin_cytoskeleton.yaml  (GO:0032156)<br>  septin_cytoskeleton_mechanism	septin_proteins	COVERED	-&gt;septin_proteins (UniProtKB:P32457, UniProtKB:P25342, UniProtKB:P32458, UniProtKB:P32468, UniProtKB:Q07657)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| target-curies-result | just check-curies-strict; data/structures/cytoskeleton/septin_cytoskeleton.yaml; exact native collect() target slice of original fresh-base TSV | supports | 16 of 19 exact target identifiers returned OK. Residuals: PMID:14562095 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by septin-agent-pmid-14562095; PMID:25971666 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by septin-agent-pmid-25971666; PMID:9790978 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently verified by septin-agent-pmid-9790978 The shared command exit zero is not interpreted as successful network resolution for transport failures. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Versele2005 and Douglas2005 are reviews, read only at the listed scopes; their synthesis is not recast as a new primary experiment. Finnigan2015 body access was genuine, but only the specified Methods/Results/Discussion sections were inspected.
- Huh2003 and Mino1998 are checked through exact bibliographic abstracts and native UniProt evidence attribution, not full experimental-body audits. Green-algal architecture and all cross-taxon recruitment mechanisms remain unverified.
- Collective septin material and individual gene necessity remain distinct. No claim that all five vegetative examples are individually indispensable for assembly is made.
- The initial Versele DOI query returned no result and an initial Douglas DOI query returned an unrelated article. Neither is scientific evidence; corrected PMID queries and the genuine article headers establish the actual identities. Finnigan S3 JATS404 and EuropePMC500 are retained failed-route receipts; the valid PMC HTML supplies the body.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All13 fresh batch16 inspection input hashes verified. Native focused schema/strict and UniProt checks passed. The fresh same-base resolver remains separately tracked.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T094819Z-septin-cytoskeleton-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Septin cytoskeleton identity, family grounding and graph scope review
started_at: '2026-10-21T09:24:23Z'
finished_at: '2026-10-21T09:48:19Z'
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
summary: Whole-cytoskeleton identity, developmental examples and all five concrete
  protein identities are supported. One major correction concerns the expanded definition’s
  taxon/function evidence scope; two minor corrections concern generic Septin-family
  grounding and descriptive graph scope.
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
  - path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    sha256: a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e
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
- target_id: GO:0032156
  path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
  label: septin cytoskeleton
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
scope:
  description: Entire single target, native ontology/family/taxon/protein identities,
    every component and graph claim, stage-specific membership and primary-versus-review
    source scope.
  selection: Seventh selected target in batch sixteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032156
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032156
  command: just validate data/structures/cytoskeleton/septin_cytoskeleton.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032156
  command: just validate-strict data/structures/cytoskeleton/septin_cytoskeleton.yaml
    --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/septin_cytoskeleton-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: false
  target_ids:
  - GO:0032156
  command: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/septin_cytoskeleton.yaml
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
  - GO:0032156
  command: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/septin_cytoskeleton.yaml
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
  - GO:0032156
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - septin-agent-go
  - septin-agent-tax-4932
  - septin-agent-tax-5476
  - septin-agent-tax-559292
  - septin-agent-P32457
  - septin-agent-query-CDC3
  - septin-agent-P25342
  - septin-agent-query-CDC10
  - septin-agent-P32458
  - septin-agent-query-CDC11
  - septin-agent-P32468
  - septin-agent-query-CDC12
  - septin-agent-Q07657
  - septin-agent-query-SHS1
  - septin-agent-IPR016491
  - septin-agent-pmid-14562095
  - septin-agent-pmid-25971666
  - septin-agent-pmid-9790978
  - septin-agent-versele2005-correct-meta
  - septin-agent-douglas2005-correct-meta
  - septin-agent-versele-pmc
  - septin-agent-douglas-pmc
  - septin-agent-finnigan2015-pmc
- check_id: target-curies
  name: Target resolver slice with native transport-failure cross-checks
  status: passed
  required: true
  target_ids:
  - GO:0032156
  summary: '16 of 19 exact target identifiers returned OK. Residuals: PMID:14562095
    returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently
    verified by septin-agent-pmid-14562095; PMID:25971666 returned UNREACHABLE (eutils
    HTTP414); exact native PMID metadata independently verified by septin-agent-pmid-25971666;
    PMID:9790978 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata
    independently verified by septin-agent-pmid-9790978 The shared command exit zero
    is not interpreted as successful network resolution for transport failures.'
  evidence_ids:
  - target-curies-result
  - septin-agent-pmid-14562095
  - septin-agent-pmid-25971666
  - septin-agent-pmid-9790978
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032156
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
  - GO:0032156
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
  - GO:0032156
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
  - GO:0032156
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
  - GO:0032156
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
  reference: data/structures/cytoskeleton/septin_cytoskeleton.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T09:45:44Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:45:44Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: septin-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0031105,GO:0032156,GO:0032158,GO:0032160,GO:0032161,GO:0032165,GO:0032166
  locator: All returned native terms, definitions, synonyms and relevant is_a/part_of
    child relations, including GO0032156/0032160/0032165/0032166
  accessed_at: '2026-10-21T09:25:51.654848Z'
  support: supports
  summary: Native GO identifies the septin cytoskeleton as the broader framework including
    septins, associated proteins and complexes. Septin complexes, bands, cleavage
    apparatus and filament-array subtypes remain distinct constituent identities.
    The specialized array examples do not exhaust the parent cytoskeleton.
  snapshot_sha256: 83ea09e6a23c180ff2b82f59f3e4bae62b7ec9b4b609fea348b1d71111324cfa
- evidence_id: septin-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:25:51.655519Z'
  support: supports
  summary: This native receipt identifies Saccharomyces cerevisiae, species. It attests
    only this taxon identity/rank, not occurrence or the experimental stock used in
    a paper.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: septin-agent-tax-5476
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5476
  locator: Complete native taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:25:51.655742Z'
  support: supports
  summary: This native receipt identifies Candida albicans, species. It attests only
    this taxon identity/rank, not occurrence or the experimental stock used in a paper.
  snapshot_sha256: 9e6eef28141aafa516ea380c0e73325179ce12d9ee35f7cb6f2ad2ab0cf9c275
- evidence_id: septin-agent-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:25:51.656079Z'
  support: supports
  summary: This native receipt identifies Saccharomyces cerevisiae S288C, strain.
    It attests only this taxon identity/rank, not occurrence or the experimental stock
    used in a paper.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: septin-agent-P32457
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32457.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:25:52.362384Z'
  support: supports
  summary: Native reviewed UniProtKB P32457 identifies Cell division control protein
    3, gene CDC3, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 7fc581a719d6b12f8611b58bfc0c11fc057c73e673b217485a3379b8330b6efe
- evidence_id: septin-agent-query-CDC3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene CDC3, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:25:52.427182Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P32457. This checks identifier
    resolution only.
  snapshot_sha256: d15bf1b00b3f29538132111c0a6ab994f6bf134478224348f6857db31c1f4aee
  search_scope: UniProtKB query gene_exact:CDC3 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: septin-agent-P25342
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P25342.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:25:51.656498Z'
  support: supports
  summary: Native reviewed UniProtKB P25342 identifies Cell division control protein
    10, gene CDC10, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 5a5194945989f266f18122a50805faa45f7bc00a599dcefcf7cf6592d753174d
- evidence_id: septin-agent-query-CDC10
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC10%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene CDC10, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:25:53.104268Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P25342. This checks identifier
    resolution only.
  snapshot_sha256: f9b9dc13ffea60b8a6bfb9d653d7a4ede1157e95cf417161793bf122b409fa8c
  search_scope: UniProtKB query gene_exact:CDC10 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: septin-agent-P32458
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32458.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:25:52.368239Z'
  support: supports
  summary: Native reviewed UniProtKB P32458 identifies Cell division control protein
    11, gene CDC11, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 839db168d3ac73f1e1718845d2d92024c8bd535a96081c789ff55a1a0e98c922
- evidence_id: septin-agent-query-CDC11
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC11%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene CDC11, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:25:53.111971Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P32458. This checks identifier
    resolution only.
  snapshot_sha256: 384fe6c570f5d6549a3469d520685905279ff9f0303a7f72da1f0d9399322fc5
  search_scope: UniProtKB query gene_exact:CDC11 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: septin-agent-P32468
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32468.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:25:52.371952Z'
  support: supports
  summary: Native reviewed UniProtKB P32468 identifies Cell division control protein
    12, gene CDC12, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 3a96072071fa02a2e65a0d5d80ebcf82c631ff8f674fc6ce5ae642b8b273619e
- evidence_id: septin-agent-query-CDC12
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ACDC12%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene CDC12, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:25:53.132995Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns P32468. This checks identifier
    resolution only.
  snapshot_sha256: 0096f0d783694af4a97eabab1e461dba9433f5de30a034cd6f25b0b667097721
  search_scope: UniProtKB query gene_exact:CDC12 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: septin-agent-Q07657
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q07657.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; SUBUNIT/COFACTOR/SUBCELLULAR
    LOCATION comments and cited references where relevant
  accessed_at: '2026-10-21T09:25:52.373100Z'
  support: supports
  summary: Native reviewed UniProtKB Q07657 identifies Seventh homolog of septin 1,
    gene SHS1, taxon559292. Concrete identity is checked independently of membership;
    relevant subunit/cofactor/location comments retain their own evidence scope.
  snapshot_sha256: 4b3fa80abaa9782dee6cb8412786a5eed43b5df173dd4a150079a04064ec2627
- evidence_id: septin-agent-query-SHS1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&query=%28gene_exact%3ASHS1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29
  locator: All returned results for exact gene SHS1, organism 559292, reviewed:true;
    bounded to this query
  accessed_at: '2026-10-21T09:25:53.298960Z'
  support: context_only
  summary: Exact gene/taxon/reviewed query returns Q07657. This checks identifier
    resolution only.
  snapshot_sha256: 0a077959f8d07e4292e2a3362dd78fb89992cf62800d84b1ad922eca984fd0c2
  search_scope: UniProtKB query gene_exact:SHS1 AND organism_id:559292 AND reviewed:true;
    all returned results inspected, no general absence claim.
- evidence_id: septin-agent-IPR016491
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Complete native entry metadata, name, type family and description
  accessed_at: '2026-10-21T09:25:54.044009Z'
  support: supports
  summary: IPR016491 is the Septin family. Its generic family scope matches the generic
    septin-proteins component; it is not a claim of a complete localized cohort, exact
    rod composition or source-specific stoichiometry.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: septin-agent-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14562095%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:25:53.424090Z'
  support: supports
  summary: 'Native metadata identifies Global analysis of protein localization in
    budding yeast. Authors: Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman
    JS, O''Shea EK.; PMID 14562095; DOI 10.1038/nature02026. Bibliographic identity
    and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: septin-agent-pmid-25971666
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A25971666%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:25:53.907867Z'
  support: supports
  summary: 'Native metadata identifies The Carboxy-Terminal Tails of Septins Cdc11
    and Shs1 Recruit Myosin-II Binding Factor Bni5 to the Bud Neck in Saccharomyces
    cerevisiae. Authors: Finnigan GC, Booth EA, Duvalyan A, Liao EN, Thorner J.; PMID
    25971666; DOI 10.1534/genetics.115.176503. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: d5e54af2eedf5ab8e2fc0f11cb37bdc5f0a64dc495e3c2ceb463d3cb5affed0c
- evidence_id: septin-agent-pmid-9790978
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9790978%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:25:53.918071Z'
  support: supports
  summary: 'Native metadata identifies Shs1p: a novel member of septin that interacts
    with spa2p, involved in polarized growth in saccharomyces cerevisiae. Authors:
    Mino A, Tanaka K, Kamei T, Umikawa M, Fujiwara T, Takai Y.; PMID 9790978; DOI
    10.1006/bbrc.1998.9541. Bibliographic identity and available abstract only; not
    a substitute for inspected article body.'
  snapshot_sha256: d584cee245cd47abf679ce4ce675586bca359618046bfeab9fe401ce170bf9be
- evidence_id: septin-agent-versele2005-correct-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16009555%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:28:54.749583Z'
  support: supports
  summary: 'Native metadata identifies Some assembly required: yeast septins provide
    the instruction manual. Authors: Versele M, Thorner J.; PMID 16009555; DOI 10.1016/j.tcb.2005.06.007.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: e357d697a9b677792c488a9a5c9aa2654f106e7bbf22b5c706aaf6fbb0c331e5
- evidence_id: septin-agent-douglas2005-correct-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A16151244%20AND%20SRC%3AMED
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:28:54.750022Z'
  support: supports
  summary: 'Native metadata identifies Septin function in yeast model systems and
    pathogenic fungi. Authors: Douglas LM, Alvarez FJ, McCreary C, Konopka JB.; PMID
    16151244; DOI 10.1128/ec.4.9.1503-1512.2005. Bibliographic identity and available
    abstract only; not a substitute for inspected article body.'
  snapshot_sha256: c37a2e2c00b1c97be69b9470c82e32fe542fa83d387685c0ebfa67a97e3ddbcb
- evidence_id: septin-agent-versele-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1761124/?pdf=render
  locator: 'PMC1761124: Introduction S1/P2, Figures1/2 captions, Table1; section2
    Functions including P5 scaffold/barrier examples, section3 budding-yeast complex
    assembly and4 fission yeast. Historical interaction models are not treated as
    a current exact subunit order.'
  accessed_at: '2026-10-21T07:29:14.610794Z'
  support: supports
  summary: Versele and Thorner2005 is review-tier synthesis of septin structure, diverse
    assemblies and barrier/scaffold functions. It distinguishes the five vegetative
    budding-yeast septins from sporulation-specific members; green-algal ortholog
    presence does not itself establish the whole cortical architecture claimed here.
  snapshot_sha256: bfa7c582507daf47688819cdd2ed31ed4dab32ed0d9e14a0d74d40c29249ac9d
- evidence_id: septin-agent-douglas-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1214204/
  locator: 'PMC1214204: sections5 scaffold overview and7 chitin deposition; section9
    including barrier subsections10/11; section14 sporulation; sections17 Candida
    albicans and18 Aspergillus nidulans. Other sections are not claimed as fully read
    in this audit.'
  accessed_at: '2026-10-21T07:11:03.050463Z'
  support: supports
  summary: Douglas et al.2005 reviews fungal diffusion barriers, sporulation and morphogenesis.
    Its stage-specific arrays support the named examples without confining the whole
    septin cytoskeleton to those developmental stages.
  snapshot_sha256: 31a2dd0109697492854f84701ef3f1d1be31f62312b613ab8432223332b69dd3
- evidence_id: septin-agent-finnigan2015-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4512547/?pdf=render
  locator: 'Genuine PMC4512547 HTML: Abstract, complete unsectioned Introduction;
    Methods Culture conditions and Fluorescence/DIC microscopy; Results Shs1 CTE recruitment
    section including Figure7; Discussion subsections13,14,16,17 including Figure8
    caption. Other Results, strain tables and supplements were not fully audited.'
  accessed_at: '2026-10-21T09:28:54.750142Z'
  support: supports
  summary: Finnigan et al.2015 experimentally links the Cdc11/Shs1 terminal extensions
    to Bni5 recruitment and Myo1 localization at the vegetative bud neck. Cdc11 and
    Shs1 are alternative terminal subunits; retained structures and partial recruitment
    distinguish assembly from downstream function.
  snapshot_sha256: db9944b94df1fe2d8e3ec56c3ed0f5309988ac3bd5a34a793bad1a0611098a41
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/septin_cytoskeleton.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:25Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/septin_cytoskeleton.yaml'
  snapshot_sha256: 06d30e7854d616fba1265bb1054009c143880495bf59eb6b8234ab1cc8da19c2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/septin_cytoskeleton.yaml
    --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/septin_cytoskeleton-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:24:27Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/septin_cytoskeleton.yaml\
    \ --out /private/tmp/cellstructure-batch16-20261021-fjx428vi/septin_cytoskeleton-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch16-20261021-fjx428vi/septin_cytoskeleton-strict.tsv"
  snapshot_sha256: c2a270808ca2c04f65a0afddc56a925019b39f0bff01252f5871599205808608
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/septin_cytoskeleton.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:45:44Z'
  support: supports
  summary: '16 of19 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:14562095: UNREACHABLE; resolved by evidence septin-agent-pmid-14562095;
    PMID:25971666: UNREACHABLE; resolved by evidence septin-agent-pmid-25971666; PMID:9790978:
    UNREACHABLE; resolved by evidence septin-agent-pmid-9790978. Source-native identity
    checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/septin_cytoskeleton.yaml
    --verify
  locator: Captured focused native verify log
  accessed_at: '2026-10-21T09:26:36.739828Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch16-20261021-fjx428vi/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/septin_cytoskeleton.yaml
    --causal-graphs
  locator: Captured focused native causal-graphs log
  accessed_at: '2026-10-21T09:26:37.426738Z'
  support: supports
  summary: "data/structures/cytoskeleton/septin_cytoskeleton.yaml  (GO:0032156)\n\
    \  septin_cytoskeleton_mechanism\tseptin_proteins\tCOVERED\t->septin_proteins\
    \ (UniProtKB:P32457, UniProtKB:P25342, UniProtKB:P32458, UniProtKB:P32468, UniProtKB:Q07657)\n\
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
  snapshot_sha256: 1e1a04f602c10f929ad2f5f0910a6957eb4e32db7dd33389e7dfe12bd1d4076e
- evidence_id: target-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/septin_cytoskeleton.yaml; exact native collect()
    target slice of original fresh-base TSV
  accessed_at: '2026-10-21T09:48:00.458099Z'
  support: supports
  summary: '16 of 19 exact target identifiers returned OK. Residuals: PMID:14562095
    returned UNREACHABLE (eutils HTTP414); exact native PMID metadata independently
    verified by septin-agent-pmid-14562095; PMID:25971666 returned UNREACHABLE (eutils
    HTTP414); exact native PMID metadata independently verified by septin-agent-pmid-25971666;
    PMID:9790978 returned UNREACHABLE (eutils HTTP414); exact native PMID metadata
    independently verified by septin-agent-pmid-9790978 The shared command exit zero
    is not interpreted as successful network resolution for transport failures.'
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
  topic: Whole cytoskeleton and specialized septin assemblies
  outcome: supported
  target_ids:
  - GO:0032156
  summary: The GO identity, cytoskeleton parent and declared structural parts are
    consistent. FILAMENT is a broad local kind classification; the text explicitly
    includes higher-order complexes and arrays and does not equate the entire framework
    with a single oligomer.
  evidence_ids:
  - septin-agent-go
  - septin-agent-versele-pmc
  - septin-agent-douglas-pmc
  - record
- assessment_id: family
  area: grounding
  topic: An exact generic family is available
  outcome: concern
  target_ids:
  - GO:0032156
  summary: The REVIEWED_LABEL_ONLY rationale requires a family identifier for a complete
    filament-array-forming cohort. The component itself is the generic septin-proteins
    class, for which IPR016491 is exact. Family identity does not require an exact
    inventory of proteins occupying each array.
  evidence_ids:
  - septin-agent-IPR016491
  - septin-agent-go
  - record
  - policy
- assessment_id: examples
  area: evidence
  topic: Correct vegetative examples remain valid at the broader target scope
  outcome: supported
  target_ids:
  - GO:0032156
  summary: All five reviewed gene/accession/taxon identities are correct. Native UniProt
    annotations support the specifically attributed Huh, Finnigan and Mino localization
    notes. Finnigan provides directly read bud-neck experiments; the two other cited
    papers were metadata/abstract- and native-annotation-scoped. Vegetative members
    are valid examples for the whole cytoskeleton even though the canonical array
    examples describe spores.
  evidence_ids:
  - septin-agent-P32457
  - septin-agent-P25342
  - septin-agent-P32458
  - septin-agent-P32468
  - septin-agent-Q07657
  - septin-agent-tax-4932
  - septin-agent-tax-5476
  - septin-agent-tax-559292
  - septin-agent-pmid-14562095
  - septin-agent-pmid-25971666
  - septin-agent-pmid-9790978
  - septin-agent-versele2005-correct-meta
  - septin-agent-douglas2005-correct-meta
  - septin-agent-finnigan2015-pmc
  - septin-agent-versele-pmc
  - septin-agent-douglas-pmc
  - record
- assessment_id: biology
  area: scope
  topic: Expanded architecture and functions exceed the cited taxon scope
  outcome: concern
  target_ids:
  - GO:0032156
  summary: The definition attributes a cortical network to yeasts, filamentous fungi
    and green algae, then assigns scaffold/barrier and recruitment functions across
    several sites. Versele S1/P2 supports green-algal ortholog occurrence only; S2/P5
    supports yeast roles. Douglas sec18 treats branch-site regulator recruitment as
    a suggestion, and sec14 distinguishes observed sporulation scaffolding from proposed
    spore-wall recruitment. Finnigan directly tests vegetative yeast Bni5/Myo1 recruitment.
    These sources do not support the full combined defining extension, whose sole
    definition_source is GO. The five-gene parenthesis is treated as a member list,
    not an ordered rod.
  evidence_ids:
  - septin-agent-versele-pmc
  - septin-agent-douglas-pmc
  - septin-agent-finnigan2015-pmc
  - septin-agent-go
  - record
- assessment_id: distribution
  area: scope
  topic: Developmental examples are nonexhaustive
  outcome: supported
  target_ids:
  - GO:0032156
  summary: The two VARIABLE entries explicitly describe sporulation/chlamydospore
    arrays, supported by their GO child definitions and review context. They do not
    say that the entire septin cytoskeleton is absent in vegetative cells. No species-wide
    percentage or exclusive spore membership is inferred.
  evidence_ids:
  - septin-agent-go
  - septin-agent-versele-pmc
  - septin-agent-douglas-pmc
  - septin-agent-tax-4932
  - septin-agent-tax-5476
  - septin-agent-tax-559292
  - record
- assessment_id: essentiality
  area: evidence
  topic: Collective material versus individual assembly requirement
  outcome: unknown
  target_ids:
  - GO:0032156
  summary: ESSENTIAL is attached to the whole septin class, not separately to each
    of the five examples. Septins are defining material of the target, but the cited
    studies do not constitute removal of the whole class followed by an assembly assay.
    Individual truncation, viability or recruitment results cannot verify a five-gene
    universal assembly requirement; none is inferred.
  evidence_ids:
  - septin-agent-go
  - septin-agent-finnigan2015-pmc
  - septin-agent-versele-pmc
  - policy
  - record
- assessment_id: graph
  area: graph
  topic: Supported parthood is not an assembly transition
  outcome: concern
  target_ids:
  - GO:0032156
  summary: The three edges record septin-protein, complex and band parthood. They
    do not describe how assembly happens, despite ASSEMBLY/MECHANISTIC and the mechanism
    title. Classify the existing descriptive scope accurately or encode a bounded
    supported transition.
  evidence_ids:
  - septin-agent-go
  - septin-agent-finnigan2015-pmc
  - policy
  - record
- assessment_id: completeness
  area: completeness
  topic: No mandatory exhaustive inventory
  outcome: supported
  target_ids:
  - GO:0032156
  summary: The broad framework is represented through generic proteins and named substructures.
    Additional subunit groups, images, functions or quantitative dimensions are optional.
    The concrete gaps are unjustified generic-family withholding and source/taxon
    inflation in the expanded definition; specialized composition should not be promoted
    to a universal cytoskeleton inventory.
  evidence_ids:
  - septin-agent-go
  - septin-agent-IPR016491
  - septin-agent-versele-pmc
  - septin-agent-finnigan2015-pmc
  - policy
  - record
findings:
- finding_id: F1
  issue_key: septin-cytoskeleton-generic-family-withheld
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the generic septin class at its actual family scope
  description: The generic septin-proteins row is REVIEWED_LABEL_ONLY because no identifier
    was assigned for the complete filament-array-forming cohort. Native IPR016491
    identifies the Septin family, matching this generic component without identifying
    every assembly-specific member. Correct the class-versus-cohort criterion and
    preserve source-specific membership limits.
  target_ids:
  - GO:0032156
  field_paths:
  - components[component_id=septin_proteins].grounding
  - components[component_id=septin_proteins].grounding_status
  - components[component_id=septin_proteins].grounding_notes
  evidence_ids:
  - septin-agent-IPR016491
  - septin-agent-go
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The existing biological class and concrete examples are correct;
    this is a bounded grounding omission caused by an overly narrow criterion.
- finding_id: F2
  issue_key: septin_cytoskeleton_mechanism-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to the represented relationships
  description: The ASSEMBLY graph contains only constituent-to-cytoskeleton parthood
    edges. Its descriptions mention biological activities, but the graph does not
    connect an explicit assembly or functional transition to those activities. MECHANISTIC
    overstates what is represented; this is a scope classification concern, not a
    claim that the supported topology is false or a demand for atomic detail.
  target_ids:
  - GO:0032156
  field_paths:
  - causal_graphs[graph_id=septin_cytoskeleton_mechanism].scope_status
  - causal_graphs[graph_id=septin_cytoskeleton_mechanism].scope_notes
  - causal_graphs[graph_id=septin_cytoskeleton_mechanism].edges
  evidence_ids:
  - septin-agent-go
  - septin-agent-finnigan2015-pmc
  - policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The identities and many relationships remain useful. The bounded
    correction concerns the promised explanatory scope, not biological identity or
    missing optional components.
- finding_id: F3
  issue_key: septin-cytoskeleton-definition-taxon-function-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate supported fungal functions from unverified green-algal architecture
  description: The expanded definition presents a plasma-membrane septin network across
    yeasts, filamentous fungi and green algae and combines barrier/scaffold recruitment
    at bud necks, hyphal branches and prospore membranes, while definition_source
    cites only GO0032156. Versele supports green-algal septin ortholog occurrence,
    not that full cortical architecture or function. Its functional examples concern
    yeast; Douglas retains proposal-level language for branch regulator and spore-wall
    recruitment, and Finnigan directly studies vegetative budding yeast. Supply matching
    evidence and qualifiers for the retained expansion rather than carrying these
    narrower observations across the entire taxon/site list.
  target_ids:
  - GO:0032156
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - septin-agent-go
  - septin-agent-versele-pmc
  - septin-agent-douglas-pmc
  - septin-agent-finnigan2015-pmc
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: major
  normalization_reason: The unsupported taxon and function extension is part of the
    defining biological claim, consistent with the major rubric for evidence scope
    inflation. It does not establish that green algae lack septin structures or that
    the proposed fungal functions are false.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032156
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  description: During authorized curation, assign IPR016491 to the generic septin-proteins
    row and explain that family membership does not establish a complete assembly-specific
    cohort.
  acceptance_checks:
  - Retain the correct five reviewed protein examples at whole-cytoskeleton scope.
  - Do not equate vegetative and sporulation-specific subunit inventories.
  - Do not replace the family with a broader GTPase domain.
  - Run focused schema, strict-reference and native protein checks.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0032156
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
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
- action_id: A3
  finding_ids:
  - F3
  target_ids:
  - GO:0032156
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained scientific record
  description: During authorized curation, distinguish the native GO definition, source-specific
    fungal functions and green-algal ortholog evidence; qualify proposed recruitment
    roles or obtain directly matching evidence.
  acceptance_checks:
  - Do not promote gene occurrence to a demonstrated cortical network or its molecular
    functions.
  - Preserve budding-yeast versus filamentous-fungal versus sporulation scope and
    observed-versus-proposed distinctions.
  - Keep the correct broad cytoskeleton identity and valid vegetative protein examples.
  - Run focused schema, strict-reference and scientific evidence checks.
limitations:
- Versele2005 and Douglas2005 are reviews, read only at the listed scopes; their synthesis
  is not recast as a new primary experiment. Finnigan2015 body access was genuine,
  but only the specified Methods/Results/Discussion sections were inspected.
- Huh2003 and Mino1998 are checked through exact bibliographic abstracts and native
  UniProt evidence attribution, not full experimental-body audits. Green-algal architecture
  and all cross-taxon recruitment mechanisms remain unverified.
- Collective septin material and individual gene necessity remain distinct. No claim
  that all five vegetative examples are individually indispensable for assembly is
  made.
- The initial Versele DOI query returned no result and an initial Douglas DOI query
  returned an unrelated article. Neither is scientific evidence; corrected PMID queries
  and the genuine article headers establish the actual identities. Finnigan S3 JATS404
  and EuropePMC500 are retained failed-route receipts; the valid PMC HTML supplies
  the body.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- All13 fresh batch16 inspection input hashes verified. Native focused schema/strict
  and UniProt checks passed. The fresh same-base resolver remains separately tracked.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
