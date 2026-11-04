# Nucleoid scientific review

- Review: 20261022T042551Z-nucleoid-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:58:41Z
- Finished UTC: 2026-10-22T04:25:51Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major scope finding: the bacterial-only definition is narrower than generic GO0009295 and its maintained organellar children. Bacterial NAP identities and scoped mechanism remain supported.

## Scope And Provenance

Exactly one full maintained nucleoid record and its frozen guidance/schema; the four-record nucleoid boundary set (target plus three neighbors); source-specific native identities, all maintained claim/evidence placements, and explicitly bounded literature sections. No image pixels or uninspected supplements are claimed.

Selection: Batch43 exact path-ordered target5; initial native inspection/schema/strict passed at the unchanged f97b base before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009295 | data/structures/nucleoid/nucleoid.yaml | maintained | nucleoid |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0009295 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009295 | Focused validator passed. |
| Native verify | passed | True | GO:0009295 | Read-only check passed; diagnostic coverage is assessed separately. |
| Native causal-graphs | passed | True | GO:0009295 | Read-only check passed; diagnostic coverage is assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0009295 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0009295 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0009295 | 15 of 17 collected target identifiers returned OK. PMID:21903814: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:333393: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0009295 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009295 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009295 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009295 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0009295 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Generic GO identity is narrowed by bacterial-only defining content

identity: concern. Targets: GO:0009295.

The identifier GO0009295 is generic and already parents the maintained mitochondrial/plastid records, but the target definition requires a bacterial chromosome. Native GO supplies GO0043590 for that narrower class. This is a material scope mismatch in the defining assertion, independently of the correct bacterial biology elsewhere in the record. Preserve the valid generic identity and make the bacterial evidence explicitly example-level, or undertake an explicitly authorized separate identity decision.

### Supported bacterial DNA and heterogeneous NAP examples

grounding: supported. Targets: GO:0009295.

Within the bacterial context, chromosome DNA and the NAP cohort are supported. All seven example accession/name/gene/taxon/status combinations and current unique exact queries match. Four experimental PMID21903814 location annotations and the H-NS PMID333393 annotation are accurately represented; other entries correctly remain identity-only. There is no exact single family for this heterogeneous cohort.

### Bacterial occurrence versus entire generic class

scope: supported. Targets: GO:0009295.

The Bacteria/E. coli/K-12 native identities are correct and the bacterial sources support the conventional chromosome-containing nucleoid context. UNIVERSAL is not read as every physiological cell state or a universal NAP complement. The E. coli example and bacterial graph do not exhaust the broader generic GO class.

### Bacterial mechanistic synthesis with source-specific limits

graph: supported. Targets: GO:0009295.

The graph explicitly describes the bacterial chromosome and is supported as a review-level multiscale mechanism sketch. NAP binding, DNA geometry changes, supercoiling and packaging are genuine causal content. Its pooled NAP node does not mean each protein performs each action; topological-barrier identities and some in vivo higher-order arrangements remain inferred. The generic structure node can represent the bacterial instance, but cannot cure the bacterial-only definition of the entire generic class.

### Constitution and individual formation necessity

evidence: unknown. Targets: GO:0009295.

Chromosomal DNA is the defining constituting material of the bacterial example. The CONDITIONAL NAP cohort does not establish a necessary assembly role for every named protein, and the reviewed evidence contains condition- and protein-specific effects. Those experimental individual requirements remain unresolved, distinct from positive material membership.

### Full target and exact bounded source scopes

provenance: supported. Targets: GO:0009295.

All maintained target fields were read with the four-record nucleoid boundary set (target plus three neighbors), native identities and the exact source sections declared in evidence. Optional inventories and unresolved experimental formation requirements are not converted into findings. No scientific edits, promotion, save or publication occurred.

## Findings

### F1: Align the bacterial-only definition with the generic nucleoid identity

major / open / confirmed; issue key: nucleoid-generic-identifier-bacterial-definition-scope.

The maintained identifier GO0009295 denotes bacterial, mitochondrial, plastid and viral nucleic-acid regions, and the frozen organellar records use it as their parent. The target definition instead requires a bacterial chromosome. Native GO0043590 is the exact narrower bacterial-nucleoid class. This is more than incomplete taxonomic examples: it changes the defining scope of the generic record. The bacterial NAP evidence, verified E. coli proteins and example-specific mechanism remain valid.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, align the generic GO0009295 definition with its actual scope and clearly qualify bacterial DNA/NAP/examples and graph as bacterial exemplars. Preserve the correct generic identifier and valid organellar child relations. If the intended record is instead specifically bacterial nucleoid, make that a deliberate separate identity/hierarchy decision using verified GO0043590, with all affected references reviewed; do not silently relabel the generic parent.

- The defining text and identifier denote the same class and do not exclude the maintained mitochondrial/plastid subclasses of generic nucleoid.
- The original bacterial evidence and seven verified protein examples remain explicitly scoped; no unsupported universal protein inventory is introduced.
- Any separately authorized identity change checks all ignored-inclusive inbound references and follows native guarded-writer/history rules.
- Focused schema/strict, native protein/graph and identifier-label gates pass after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/nucleoid/nucleoid.yaml; Entire maintained target, including all evidence, components, taxonomy, examples, functions, graph, discussions and history | context_only | Complete target read; historical curation prose is not independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Structure identity, is-a/parthood, component molecular material, essentiality, protein examples and graph contracts | context_only | Constituent identity, individual formation necessity, exact family identity and experimental membership are distinct claims. |
| neighbor-chloroplast_nucleoid | data/structures/nucleoid/chloroplast_nucleoid.yaml; Entire frozen neighboring nucleoid record | context_only | Read for the generic/organellar boundary and maintained identifier usage, not as independent literature evidence. |
| neighbor-mitochondrial_nucleoid | data/structures/nucleoid/mitochondrial_nucleoid.yaml; Entire frozen neighboring nucleoid record | context_only | Read for the generic/organellar boundary and maintained identifier usage, not as independent literature evidence. |
| neighbor-plastid_nucleoid | data/structures/nucleoid/plastid_nucleoid.yaml; Entire frozen neighboring nucleoid record | context_only | Read for the generic/organellar boundary and maintained identifier usage, not as independent literature evidence. |
| nucleoid-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009295,GO:0042644,GO:0042645,GO:0042646,GO:0009570,GO:0009532,GO:0005759,GO:0051276; Complete eight-term native names, definitions, active states and typed child relations | supports | GO0009295 denotes a nucleic-acid region in a virus, bacterial cell, mitochondrion or chloroplast. GO0042644/0042645/0042646 exactly identify the three organellar nucleoid classes. The returned stroma/matrix terms show their corresponding nucleoid part_of children; GO0051276 is chromosome organization. Each exact term was read; no omitted edge is treated as biological disproof. |
| nucleoid-agent-go-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042644,GO:0042645,GO:0042646/ancestors?relations=is_a; Complete is_a-only ancestor arrays for GO0042644, GO0042645 and GO0042646 | supports | The is_a-only response places chloroplast nucleoid under plastid nucleoid and places both plastid and mitochondrial nucleoids under generic nucleoid. The direct typed child relations are independently visible in the term response. This request does not establish parthood. |
| nucleoid-agent-go-bacterial | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043590; Complete native bacterial term name/definition/active status, read with typed generic child relation | supports | Active GO0043590 is specifically bacterial nucleoid, defined as the bacterial-cell region containing DNA. The separate generic GO0009295 response includes GO0043590 as an is_a child alongside organellar nucleoid children. |
| nucleoid-agent-SL-0187 | https://rest.uniprot.org/locations/SL-0187.json; Complete native name/definition/GO and cytoplasmic hierarchy | supports | UniProt SL0187 describes the prokaryotic nucleoid and maps it to broader GO0009295. This cross-authority scope difference is preserved; the narrower SL wording does not remove the GO organellar subclasses. |
| nucleoid-agent-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Complete native taxId/scientificName/rank/lineage and names | supports | ENA 2 identifies Bacteria, rank domain. This verifies this named taxon only; it does not measure prevalence or identify a different experimental strain. |
| nucleoid-agent-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxId/scientificName/rank/lineage and names | supports | ENA 562 identifies Escherichia coli, rank species. This verifies this named taxon only; it does not measure prevalence or identify a different experimental strain. |
| nucleoid-agent-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxId/scientificName/rank/lineage and names | supports | ENA 83333 identifies Escherichia coli K-12, rank strain. This verifies this named taxon only; it does not measure prevalence or identify a different experimental strain. |
| nucleoid-agent-dillon2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1038/nrmicro2261%22; Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | Dillon SC and Dorman CJ2010, DOI10.1038/nrmicro2261, PMID20140026, is a bacterial NAP review. Its complete abstract supports dynamic interactions between bacterial chromosome architecture, NAPs and transcription; it does not define the organellar scope of GO0009295. |
| nucleoid-agent-verma2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.pgen.1008456%22; Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | Verma SC, Qian Z and Adhya SL2019, DOI10.1371/journal.pgen.1008456/PMC6907758, is a review of E. coli chromosome organization and gene regulation, explicitly centered on that model bacterium. |
| nucleoid-agent-verma2019-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC6907758.1/PMC6907758.1.xml; Genuine JATS secondary review: complete Introduction sec001; NAP section sec002, HU/IHF/H-NS/Fis sec003–006; Supercoiling sec009–010, NAP control sec014 and topological domains sec015, including embedded Figures1–5/7 captions and Tables1–2. Other sections and original cited experiments not independently audited. | supports | The review supports NAP binding, bending/bridging/wrapping, negative-supercoil constraint and hierarchical plectonemic organization in E. coli. It distinguishes specific proteins, concentrations, growth phases and in vitro evidence. Topological-domain barrier identities remain proposed; the generic cohort graph is a coarse synthesis, not direct proof of one universal in vivo sequence. Tables1–2 include HU/IHF/H-NS/Fis/Dps, with distinct properties. |
| nucleoid-agent-PMID21903814 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A21903814%20AND%20SRC%3AMED; Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | PMID21903814 is Wang et al.2011, DOI10.1126/science.1204697, PMC3329943. Complete abstract reports live E. coli super-resolution localization, H-NS clustering and chromosome-conformation capture. |
| nucleoid-agent-PMID21903814-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC3329943/; Genuine PMC primary body: complete main text from Introduction through final discussion paragraph, in-text experimental descriptions and Figures1–4 captions. Supplementary Methods/TableS1/figures and image pixels not inspected. | supports | The primary main text and captions directly support scattered HU/Fis/IHF/StpA and clustered H-NS in live E. coli under defined culture/imaging conditions. H-NS mutants and deletion alter clustering and selected chromosome contacts. The source distinguishes measured contacts from potential loop/anchor interpretations. This supports the explicit UniProt localization provenance without certifying all family members or all bacteria. |
| nucleoid-agent-PMID333393 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A333393%20AND%20SRC%3AMED; Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors, year and complete abstract | supports | PMID333393 is Varshavsky et al.1977, DOI10.1093/nar/4.8.2725, PMC342604. Complete abstract describes proteins1/2 in purified E. coli deoxyribonucleoprotein, with protein2 apparently HU. The modern H-NS/B1 mapping is established by the separately inspected UniProt annotation, not newly reconstructed from the abstract alone. |
| nucleoid-agent-protein-P0ACF0 | https://rest.uniprot.org/uniprotkb/P0ACF0.json; Exact accession/status/name/genes/taxon and location comments/evidence; relevant linked reference identities | supports | P0ACF0 is reviewed DNA-binding protein HU-alpha, primary gene hupA, organism83333, matching the maintained example. The location comment explicitly links Cytoplasm, nucleoid to experimental PMID21903814. Identity and the cited location annotation are assessed separately. |
| nucleoid-agent-gene-hupA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AhupA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The current exact reviewed hupA query in taxon83333 returns one entry P0ACF0, whose primary gene matches. Historical unretained queries are not reconstructed. |
| nucleoid-agent-protein-P0ACF4 | https://rest.uniprot.org/uniprotkb/P0ACF4.json; Exact accession/status/name/genes/taxon and location comments/evidence; relevant linked reference identities | supports | P0ACF4 is reviewed DNA-binding protein HU-beta, primary gene hupB, organism83333, matching the maintained example. Identity and the cited location annotation are assessed separately. |
| nucleoid-agent-gene-hupB | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AhupB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The current exact reviewed hupB query in taxon83333 returns one entry P0ACF4, whose primary gene matches. Historical unretained queries are not reconstructed. |
| nucleoid-agent-protein-P0A6X7 | https://rest.uniprot.org/uniprotkb/P0A6X7.json; Exact accession/status/name/genes/taxon and location comments/evidence; relevant linked reference identities | supports | P0A6X7 is reviewed Integration host factor subunit alpha, primary gene ihfA, organism83333, matching the maintained example. The location comment explicitly links Cytoplasm, nucleoid to experimental PMID21903814. Identity and the cited location annotation are assessed separately. |
| nucleoid-agent-gene-ihfA | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AihfA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The current exact reviewed ihfA query in taxon83333 returns one entry P0A6X7, whose primary gene matches. Historical unretained queries are not reconstructed. |
| nucleoid-agent-protein-P0A6Y1 | https://rest.uniprot.org/uniprotkb/P0A6Y1.json; Exact accession/status/name/genes/taxon and location comments/evidence; relevant linked reference identities | supports | P0A6Y1 is reviewed Integration host factor subunit beta, primary gene ihfB, organism83333, matching the maintained example. Identity and the cited location annotation are assessed separately. |
| nucleoid-agent-gene-ihfB | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AihfB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The current exact reviewed ihfB query in taxon83333 returns one entry P0A6Y1, whose primary gene matches. Historical unretained queries are not reconstructed. |
| nucleoid-agent-protein-P0A6R3 | https://rest.uniprot.org/uniprotkb/P0A6R3.json; Exact accession/status/name/genes/taxon and location comments/evidence; relevant linked reference identities | supports | P0A6R3 is reviewed DNA-binding protein Fis, primary gene fis, organism83333, matching the maintained example. The location comment explicitly links Cytoplasm, nucleoid to experimental PMID21903814. Identity and the cited location annotation are assessed separately. |
| nucleoid-agent-gene-fis | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3Afis%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The current exact reviewed fis query in taxon83333 returns one entry P0A6R3, whose primary gene matches. Historical unretained queries are not reconstructed. |
| nucleoid-agent-protein-P0ACF8 | https://rest.uniprot.org/uniprotkb/P0ACF8.json; Exact accession/status/name/genes/taxon and location comments/evidence; relevant linked reference identities | supports | P0ACF8 is reviewed DNA-binding protein H-NS, primary gene hns, organism83333, matching the maintained example. The location comment explicitly links Cytoplasm, nucleoid to experimental PMID21903814. It also links that location and the Protein B1 alternative name to PMID333393. Identity and the cited location annotation are assessed separately. |
| nucleoid-agent-gene-hns | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3Ahns%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The current exact reviewed hns query in taxon83333 returns one entry P0ACF8, whose primary gene matches. Historical unretained queries are not reconstructed. |
| nucleoid-agent-protein-P0ABT2 | https://rest.uniprot.org/uniprotkb/P0ABT2.json; Exact accession/status/name/genes/taxon and location comments/evidence; relevant linked reference identities | supports | P0ABT2 is reviewed DNA protection during starvation protein, primary gene dps, organism83333, matching the maintained example. Identity and the cited location annotation are assessed separately. |
| nucleoid-agent-gene-dps | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3Adps%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29; Complete current UniProt JSON result array and returned entry genes; query conditions in exact source URL | context_only | The current exact reviewed dps query in taxon83333 returns one entry P0ABT2, whose primary gene matches. Historical unretained queries are not reconstructed. |
| nucleoid-agent-family-IPR000119 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000119/; Native type/name, full description and child families | context_only | IPR000119 covers HU/IHF-like proteins but does not encompass all the separately named NAP families H-NS, Fis and Dps. A relevant family for some examples is not an exact family grounding for the heterogeneous NAP cohort. |
| corpus-boundary-search | rg --no-ignore --hidden -n GO:0043590&#124;identifier:GO:0009295&#124;label:bacterial_nucleoid repo/data/structures; Complete retained matching-line result; argument patterns are documented in search_scope | context_only | The ignored-inclusive maintained data/structures search finds the one generic GO0009295 record and no GO0043590 identifier/reference or exact bacterial-nucleoid label. This search does not claim absence outside that maintained corpus surface. |
| schema-result | just validate data/structures/nucleoid/nucleoid.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/nucleoid/nucleoid.yaml |
| strict-result | just validate-strict data/structures/nucleoid/nucleoid.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/nucleoid-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/nucleoid/nucleoid.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/nucleoid-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/nucleoid-strict.tsv |
| nucleoid-verify | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/nucleoid/nucleoid.yaml; Complete native read-only log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| nucleoid-causal-graphs | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/nucleoid/nucleoid.yaml; Complete native read-only log | supports | data/structures/nucleoid/nucleoid.yaml  (GO:0009295)<br>  nap_supercoiling_chromosome_compaction	nucleoid_associated_proteins	COVERED	-&gt;nucleoid_associated_proteins (UniProtKB:P0ACF0, UniProtKB:P0ACF4, UniProtKB:P0A6X7, UniProtKB:P0A6Y1, UniProtKB:P0A6R3, UniProtKB:P0ACF8, UniProtKB:P0ABT2)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/nucleoid/nucleoid.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 15 of 17 collected target identifiers returned OK. PMID:21903814: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:333393: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Dillon/Dorman2010 is available here at complete native abstract scope only. DOI/Nature responses returnedHTTP200 challenge HTML, not the review body. Verma2019 genuine full JATS was read only at the listed sections and is secondary synthesis; its cited original experiments were not individually recovered.
- Wang2011 genuine complete scientific main text/in-text methods/captions was read, without supplementary Methods/TableS1 or pixels. Native PMID333393 identity and complete abstract were read; its retained legacy PMC page is scan-based and no scanned full body was inspected. The modern H-NS/B1 mapping comes from explicit UniProt annotation.
- Current seven exact reviewed gene queries each return the expected single entry; these do not reconstruct unretained historical query outputs. K-12 identity does not assign every experiment to a particular K-12 substrain.
- The graph is a coarse bacterial/E. coli model. In vitro constraints, protein concentration, magnesium, growth phase and unresolved in vivo domain barriers limit universal mechanistic interpretation. No exhaustive molecular-family inventory, universal NAP necessity or measured all-Bacteria prevalence is certified.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes this one-record bundle even when no defect is found. Parent owns integration of the five completed same-base batch26 global gates and later finalization.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T042551Z-nucleoid-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Nucleoid scientific review
started_at: '2026-10-22T03:58:41Z'
finished_at: '2026-10-22T04:25:51Z'
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
summary: 'One major scope finding: the bacterial-only definition is narrower than
  generic GO0009295 and its maintained organellar children. Bacterial NAP identities
  and scoped mechanism remain supported.'
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/nucleoid/chloroplast_nucleoid.yaml
    sha256: ce04fc40cbf0fc1be723607cbbd2095ca56b7fabc1530a94c14bf6d2f675fa25
    role: context
  - path: data/structures/nucleoid/mitochondrial_nucleoid.yaml
    sha256: c5528f88f4b4d2e0a93245d0abd172ae0b12cc2fd06d9009df8d9c1b802d557d
    role: context
  - path: data/structures/nucleoid/nucleoid.yaml
    sha256: e9524aec530d0a42437605be025e4da7f940b4203085f3622efae68ea2819e08
    role: target
  - path: data/structures/nucleoid/plastid_nucleoid.yaml
    sha256: 08f0a8e488283887c528c2c2e4fe98e6094c34062da928ad0bf47484c0521842
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
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0009295
  path: data/structures/nucleoid/nucleoid.yaml
  label: nucleoid
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/nucleoid.yaml
    role: maintained scientific record
scope:
  description: Exactly one full maintained nucleoid record and its frozen guidance/schema;
    the four-record nucleoid boundary set (target plus three neighbors); source-specific
    native identities, all maintained claim/evidence placements, and explicitly bounded
    literature sections. No image pixels or uninspected supplements are claimed.
  selection: Batch43 exact path-ordered target5; initial native inspection/schema/strict
    passed at the unchanged f97b base before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009295
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just validate data/structures/nucleoid/nucleoid.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just validate-strict data/structures/nucleoid/nucleoid.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/nucleoid-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/nucleoid/nucleoid.yaml
  exit_code: 0
  summary: Read-only check passed; diagnostic coverage is assessed separately.
  evidence_ids:
  - nucleoid-verify
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/nucleoid/nucleoid.yaml
  exit_code: 0
  summary: Read-only check passed; diagnostic coverage is assessed separately.
  evidence_ids:
  - nucleoid-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009295
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009295
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-chloroplast_nucleoid
  - neighbor-mitochondrial_nucleoid
  - neighbor-plastid_nucleoid
  - nucleoid-agent-go
  - nucleoid-agent-go-ancestors
  - nucleoid-agent-go-bacterial
  - nucleoid-agent-SL-0187
  - nucleoid-agent-tax2
  - nucleoid-agent-tax562
  - nucleoid-agent-tax83333
  - nucleoid-agent-dillon2010-meta
  - nucleoid-agent-verma2019-meta
  - nucleoid-agent-verma2019-jats
  - nucleoid-agent-PMID21903814
  - nucleoid-agent-PMID21903814-pmc
  - nucleoid-agent-PMID333393
  - nucleoid-agent-protein-P0ACF0
  - nucleoid-agent-gene-hupA
  - nucleoid-agent-protein-P0ACF4
  - nucleoid-agent-gene-hupB
  - nucleoid-agent-protein-P0A6X7
  - nucleoid-agent-gene-ihfA
  - nucleoid-agent-protein-P0A6Y1
  - nucleoid-agent-gene-ihfB
  - nucleoid-agent-protein-P0A6R3
  - nucleoid-agent-gene-fis
  - nucleoid-agent-protein-P0ACF8
  - nucleoid-agent-gene-hns
  - nucleoid-agent-protein-P0ABT2
  - nucleoid-agent-gene-dps
  - nucleoid-agent-family-IPR000119
  - corpus-boundary-search
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0009295
  summary: '15 of 17 collected target identifiers returned OK. PMID:21903814: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim.; PMID:333393: UNREACHABLE; Exact native Europe PMC MED
    identifier, title and DOI were reviewed after the bulk eutils414 transport failure.
    Biological support remains bounded by the separately recorded abstract or primary-body
    sections; identity resolution alone is not confirmation of every attached claim.
    Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - nucleoid-agent-PMID21903814
  - nucleoid-agent-PMID333393
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0009295
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:34Z to
    2026-10-22T01:34:04Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/nucleoid/nucleoid.yaml
  locator: Entire maintained target, including all evidence, components, taxonomy,
    examples, functions, graph, discussions and history
  accessed_at: '2026-10-22T04:08:18Z'
  support: context_only
  summary: Complete target read; historical curation prose is not independent scientific
    evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Structure identity, is-a/parthood, component molecular material, essentiality,
    protein examples and graph contracts
  accessed_at: '2026-10-22T04:08:18Z'
  support: context_only
  summary: Constituent identity, individual formation necessity, exact family identity
    and experimental membership are distinct claims.
- evidence_id: neighbor-chloroplast_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/chloroplast_nucleoid.yaml
  locator: Entire frozen neighboring nucleoid record
  accessed_at: '2026-10-22T04:08:18Z'
  support: context_only
  summary: Read for the generic/organellar boundary and maintained identifier usage,
    not as independent literature evidence.
- evidence_id: neighbor-mitochondrial_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/mitochondrial_nucleoid.yaml
  locator: Entire frozen neighboring nucleoid record
  accessed_at: '2026-10-22T04:08:18Z'
  support: context_only
  summary: Read for the generic/organellar boundary and maintained identifier usage,
    not as independent literature evidence.
- evidence_id: neighbor-plastid_nucleoid
  kind: record_content
  reference: data/structures/nucleoid/plastid_nucleoid.yaml
  locator: Entire frozen neighboring nucleoid record
  accessed_at: '2026-10-22T04:08:18Z'
  support: context_only
  summary: Read for the generic/organellar boundary and maintained identifier usage,
    not as independent literature evidence.
- evidence_id: nucleoid-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009295,GO:0042644,GO:0042645,GO:0042646,GO:0009570,GO:0009532,GO:0005759,GO:0051276
  locator: Complete eight-term native names, definitions, active states and typed
    child relations
  accessed_at: '2026-10-22T04:01:32.865895Z'
  support: supports
  summary: GO0009295 denotes a nucleic-acid region in a virus, bacterial cell, mitochondrion
    or chloroplast. GO0042644/0042645/0042646 exactly identify the three organellar
    nucleoid classes. The returned stroma/matrix terms show their corresponding nucleoid
    part_of children; GO0051276 is chromosome organization. Each exact term was read;
    no omitted edge is treated as biological disproof.
  snapshot_sha256: 157b49ca60fedbfa204de107ed8accec843e846c341d6803ca0c7b3b2b8b2b14
- evidence_id: nucleoid-agent-go-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0042644,GO:0042645,GO:0042646/ancestors?relations=is_a
  locator: Complete is_a-only ancestor arrays for GO0042644, GO0042645 and GO0042646
  accessed_at: '2026-10-22T04:01:32.866260Z'
  support: supports
  summary: The is_a-only response places chloroplast nucleoid under plastid nucleoid
    and places both plastid and mitochondrial nucleoids under generic nucleoid. The
    direct typed child relations are independently visible in the term response. This
    request does not establish parthood.
  snapshot_sha256: ca89714e653442f4f3d54532fb4a24f02f4bb7443db4be2ec7d2462c9b738df3
- evidence_id: nucleoid-agent-go-bacterial
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0043590
  locator: Complete native bacterial term name/definition/active status, read with
    typed generic child relation
  accessed_at: '2026-10-22T04:05:29.281098Z'
  support: supports
  summary: Active GO0043590 is specifically bacterial nucleoid, defined as the bacterial-cell
    region containing DNA. The separate generic GO0009295 response includes GO0043590
    as an is_a child alongside organellar nucleoid children.
  snapshot_sha256: 550f8749e696e3800a2081ad9b8d02a9e9b762ea0e015b00b7352c7fd495d733
- evidence_id: nucleoid-agent-SL-0187
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0187.json
  locator: Complete native name/definition/GO and cytoplasmic hierarchy
  accessed_at: '2026-10-22T04:01:32.867898Z'
  support: supports
  summary: UniProt SL0187 describes the prokaryotic nucleoid and maps it to broader
    GO0009295. This cross-authority scope difference is preserved; the narrower SL
    wording does not remove the GO organellar subclasses.
  snapshot_sha256: f012b1f206fcd611ddbc672bf2ffd28df17e2ca416d836d1bd8516a41eb0a999
- evidence_id: nucleoid-agent-tax2
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Complete native taxId/scientificName/rank/lineage and names
  accessed_at: '2026-10-22T04:01:33.625598Z'
  support: supports
  summary: ENA 2 identifies Bacteria, rank domain. This verifies this named taxon
    only; it does not measure prevalence or identify a different experimental strain.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: nucleoid-agent-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxId/scientificName/rank/lineage and names
  accessed_at: '2026-10-22T04:01:34.180229Z'
  support: supports
  summary: ENA 562 identifies Escherichia coli, rank species. This verifies this named
    taxon only; it does not measure prevalence or identify a different experimental
    strain.
  snapshot_sha256: 66d5c5c74569e24b72fd7b011961dc221b58d841db7db3023337fb534733e200
- evidence_id: nucleoid-agent-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxId/scientificName/rank/lineage and names
  accessed_at: '2026-10-22T04:01:34.180518Z'
  support: supports
  summary: ENA 83333 identifies Escherichia coli K-12, rank strain. This verifies
    this named taxon only; it does not measure prevalence or identify a different
    experimental strain.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: nucleoid-agent-dillon2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1038/nrmicro2261%22
  locator: Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors,
    year and complete abstract
  accessed_at: '2026-10-22T04:01:38.131032Z'
  support: supports
  summary: Dillon SC and Dorman CJ2010, DOI10.1038/nrmicro2261, PMID20140026, is a
    bacterial NAP review. Its complete abstract supports dynamic interactions between
    bacterial chromosome architecture, NAPs and transcription; it does not define
    the organellar scope of GO0009295.
  snapshot_sha256: def5ab5be08b30c4daa06ea69491ab86b29af27be69929a95e387b0364c3ff5d
- evidence_id: nucleoid-agent-verma2019-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.pgen.1008456%22
  locator: Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors,
    year and complete abstract
  accessed_at: '2026-10-22T04:01:38.354725Z'
  support: supports
  summary: Verma SC, Qian Z and Adhya SL2019, DOI10.1371/journal.pgen.1008456/PMC6907758,
    is a review of E. coli chromosome organization and gene regulation, explicitly
    centered on that model bacterium.
  snapshot_sha256: 6d10aa37e9fbe3089110ed9a6b1911b3122197a4054775a50dafae741684d586
- evidence_id: nucleoid-agent-verma2019-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6907758.1/PMC6907758.1.xml
  locator: 'Genuine JATS secondary review: complete Introduction sec001; NAP section
    sec002, HU/IHF/H-NS/Fis sec003–006; Supercoiling sec009–010, NAP control sec014
    and topological domains sec015, including embedded Figures1–5/7 captions and Tables1–2.
    Other sections and original cited experiments not independently audited.'
  accessed_at: '2026-10-22T04:02:38.976321Z'
  support: supports
  summary: The review supports NAP binding, bending/bridging/wrapping, negative-supercoil
    constraint and hierarchical plectonemic organization in E. coli. It distinguishes
    specific proteins, concentrations, growth phases and in vitro evidence. Topological-domain
    barrier identities remain proposed; the generic cohort graph is a coarse synthesis,
    not direct proof of one universal in vivo sequence. Tables1–2 include HU/IHF/H-NS/Fis/Dps,
    with distinct properties.
  snapshot_sha256: f0ac2a95634cffece5970d32302e4a843c46f9627f0478b63bc6d2233662b387
- evidence_id: nucleoid-agent-PMID21903814
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A21903814%20AND%20SRC%3AMED
  locator: Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors,
    year and complete abstract
  accessed_at: '2026-10-22T04:01:38.445045Z'
  support: supports
  summary: PMID21903814 is Wang et al.2011, DOI10.1126/science.1204697, PMC3329943.
    Complete abstract reports live E. coli super-resolution localization, H-NS clustering
    and chromosome-conformation capture.
  snapshot_sha256: 1e5a8a5a54ee7409972f3400b871f2380605625c2c6630cc54e2f3e054b3d728
- evidence_id: nucleoid-agent-PMID21903814-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3329943/
  locator: 'Genuine PMC primary body: complete main text from Introduction through
    final discussion paragraph, in-text experimental descriptions and Figures1–4 captions.
    Supplementary Methods/TableS1/figures and image pixels not inspected.'
  accessed_at: '2026-10-22T04:02:20.755418Z'
  support: supports
  summary: The primary main text and captions directly support scattered HU/Fis/IHF/StpA
    and clustered H-NS in live E. coli under defined culture/imaging conditions. H-NS
    mutants and deletion alter clustering and selected chromosome contacts. The source
    distinguishes measured contacts from potential loop/anchor interpretations. This
    supports the explicit UniProt localization provenance without certifying all family
    members or all bacteria.
  snapshot_sha256: 1cee698c80281493bac2bae3a3199e003d3859a282c9dd6850e0a971abc37b90
- evidence_id: nucleoid-agent-PMID333393
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A333393%20AND%20SRC%3AMED
  locator: Unique native Europe PMC MED identity, DOI/PMID/PMC where present, authors,
    year and complete abstract
  accessed_at: '2026-10-22T04:01:38.524497Z'
  support: supports
  summary: PMID333393 is Varshavsky et al.1977, DOI10.1093/nar/4.8.2725, PMC342604.
    Complete abstract describes proteins1/2 in purified E. coli deoxyribonucleoprotein,
    with protein2 apparently HU. The modern H-NS/B1 mapping is established by the
    separately inspected UniProt annotation, not newly reconstructed from the abstract
    alone.
  snapshot_sha256: ef188e5867bde05fdde302addadc9622a559e39a33f1064ce33edcd630873793
- evidence_id: nucleoid-agent-protein-P0ACF0
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ACF0.json
  locator: Exact accession/status/name/genes/taxon and location comments/evidence;
    relevant linked reference identities
  accessed_at: '2026-10-22T04:01:34.234735Z'
  support: supports
  summary: P0ACF0 is reviewed DNA-binding protein HU-alpha, primary gene hupA, organism83333,
    matching the maintained example. The location comment explicitly links Cytoplasm,
    nucleoid to experimental PMID21903814. Identity and the cited location annotation
    are assessed separately.
  snapshot_sha256: 2c196a6263284294e56ac728414727fcb7f484114bea5a93676fc69cd18378e6
- evidence_id: nucleoid-agent-gene-hupA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AhupA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt JSON result array and returned entry genes; query
    conditions in exact source URL
  accessed_at: '2026-10-22T04:01:35.706503Z'
  support: context_only
  summary: The current exact reviewed hupA query in taxon83333 returns one entry P0ACF0,
    whose primary gene matches. Historical unretained queries are not reconstructed.
  snapshot_sha256: f5131b360ffafed8326ba4a6f8e49aa8075273ef04bdd0fe77f4fd2f9a8a6244
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AhupA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: nucleoid-agent-protein-P0ACF4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ACF4.json
  locator: Exact accession/status/name/genes/taxon and location comments/evidence;
    relevant linked reference identities
  accessed_at: '2026-10-22T04:01:34.240281Z'
  support: supports
  summary: P0ACF4 is reviewed DNA-binding protein HU-beta, primary gene hupB, organism83333,
    matching the maintained example. Identity and the cited location annotation are
    assessed separately.
  snapshot_sha256: 0c491ed797820b6ef9cb677d80467eec7879f829b47f44076c40ce27d0b35f09
- evidence_id: nucleoid-agent-gene-hupB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AhupB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt JSON result array and returned entry genes; query
    conditions in exact source URL
  accessed_at: '2026-10-22T04:01:35.776165Z'
  support: context_only
  summary: The current exact reviewed hupB query in taxon83333 returns one entry P0ACF4,
    whose primary gene matches. Historical unretained queries are not reconstructed.
  snapshot_sha256: f6f7f2b99d298b9b720156fbf955840feedd854accfe6be153ab49ce49b73b18
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AhupB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: nucleoid-agent-protein-P0A6X7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6X7.json
  locator: Exact accession/status/name/genes/taxon and location comments/evidence;
    relevant linked reference identities
  accessed_at: '2026-10-22T04:01:34.793388Z'
  support: supports
  summary: P0A6X7 is reviewed Integration host factor subunit alpha, primary gene
    ihfA, organism83333, matching the maintained example. The location comment explicitly
    links Cytoplasm, nucleoid to experimental PMID21903814. Identity and the cited
    location annotation are assessed separately.
  snapshot_sha256: 443ba5d81e02adf48c4e893a050fe589e232d4f74bf55891a91811f34d70dc09
- evidence_id: nucleoid-agent-gene-ihfA
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AihfA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt JSON result array and returned entry genes; query
    conditions in exact source URL
  accessed_at: '2026-10-22T04:01:36.190038Z'
  support: context_only
  summary: The current exact reviewed ihfA query in taxon83333 returns one entry P0A6X7,
    whose primary gene matches. Historical unretained queries are not reconstructed.
  snapshot_sha256: 5a6c232662fddade215e3ec7ee975bac8eb0c554b1ac007be5ecd2d584946197
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AihfA%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: nucleoid-agent-protein-P0A6Y1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6Y1.json
  locator: Exact accession/status/name/genes/taxon and location comments/evidence;
    relevant linked reference identities
  accessed_at: '2026-10-22T04:01:34.820018Z'
  support: supports
  summary: P0A6Y1 is reviewed Integration host factor subunit beta, primary gene ihfB,
    organism83333, matching the maintained example. Identity and the cited location
    annotation are assessed separately.
  snapshot_sha256: 00e7d54c17acfe2db9536cac8f82c66606733b43bb3d6b6a337b744198d6d2e1
- evidence_id: nucleoid-agent-gene-ihfB
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AihfB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt JSON result array and returned entry genes; query
    conditions in exact source URL
  accessed_at: '2026-10-22T04:01:36.338646Z'
  support: context_only
  summary: The current exact reviewed ihfB query in taxon83333 returns one entry P0A6Y1,
    whose primary gene matches. Historical unretained queries are not reconstructed.
  snapshot_sha256: 00dca6f69237cb0cf2fa1bd1489807bdf6c63c8ff390ed3a9dc08ef76e868033
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AihfB%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: nucleoid-agent-protein-P0A6R3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0A6R3.json
  locator: Exact accession/status/name/genes/taxon and location comments/evidence;
    relevant linked reference identities
  accessed_at: '2026-10-22T04:01:34.922573Z'
  support: supports
  summary: P0A6R3 is reviewed DNA-binding protein Fis, primary gene fis, organism83333,
    matching the maintained example. The location comment explicitly links Cytoplasm,
    nucleoid to experimental PMID21903814. Identity and the cited location annotation
    are assessed separately.
  snapshot_sha256: 91fe66ce876b12a17652e63ad345bc4c7badeb7fbdd81ab24b7ff996069f21d9
- evidence_id: nucleoid-agent-gene-fis
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3Afis%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt JSON result array and returned entry genes; query
    conditions in exact source URL
  accessed_at: '2026-10-22T04:01:36.489636Z'
  support: context_only
  summary: The current exact reviewed fis query in taxon83333 returns one entry P0A6R3,
    whose primary gene matches. Historical unretained queries are not reconstructed.
  snapshot_sha256: 359db2d48e14e3708cd83734b39dc68565c7dd321b7aa1381b95f17ce3cdbb42
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3Afis%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: nucleoid-agent-protein-P0ACF8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ACF8.json
  locator: Exact accession/status/name/genes/taxon and location comments/evidence;
    relevant linked reference identities
  accessed_at: '2026-10-22T04:01:34.989074Z'
  support: supports
  summary: P0ACF8 is reviewed DNA-binding protein H-NS, primary gene hns, organism83333,
    matching the maintained example. The location comment explicitly links Cytoplasm,
    nucleoid to experimental PMID21903814. It also links that location and the Protein
    B1 alternative name to PMID333393. Identity and the cited location annotation
    are assessed separately.
  snapshot_sha256: 69765685e6a74d1b208bbeb2ddd51204aa1be75b3b8b411efbe83252cd9523c8
- evidence_id: nucleoid-agent-gene-hns
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3Ahns%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt JSON result array and returned entry genes; query
    conditions in exact source URL
  accessed_at: '2026-10-22T04:01:36.507580Z'
  support: context_only
  summary: The current exact reviewed hns query in taxon83333 returns one entry P0ACF8,
    whose primary gene matches. Historical unretained queries are not reconstructed.
  snapshot_sha256: c2d0e5f91fafe9a823753036538ef81645c7a74225054fb9d4b8b443df015ec0
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3Ahns%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: nucleoid-agent-protein-P0ABT2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P0ABT2.json
  locator: Exact accession/status/name/genes/taxon and location comments/evidence;
    relevant linked reference identities
  accessed_at: '2026-10-22T04:01:34.992336Z'
  support: supports
  summary: P0ABT2 is reviewed DNA protection during starvation protein, primary gene
    dps, organism83333, matching the maintained example. Identity and the cited location
    annotation are assessed separately.
  snapshot_sha256: 5bc26c2d3491d422d27034cfa9f4afb128bbe8403d8b097b9e36bf810df038dc
- evidence_id: nucleoid-agent-gene-dps
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3Adps%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete current UniProt JSON result array and returned entry genes; query
    conditions in exact source URL
  accessed_at: '2026-10-22T04:01:37.209802Z'
  support: context_only
  summary: The current exact reviewed dps query in taxon83333 returns one entry P0ABT2,
    whose primary gene matches. Historical unretained queries are not reconstructed.
  snapshot_sha256: 55916ff15491526e1713c2c33dd025ca4d012ffc4a8ed2f8a596f6dcad3c0619
  search_scope: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3Adps%29%20AND%20%28organism_id%3A83333%29%20AND%20%28reviewed%3Atrue%29
- evidence_id: nucleoid-agent-family-IPR000119
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000119/
  locator: Native type/name, full description and child families
  accessed_at: '2026-10-22T04:02:38.976597Z'
  support: context_only
  summary: IPR000119 covers HU/IHF-like proteins but does not encompass all the separately
    named NAP families H-NS, Fis and Dps. A relevant family for some examples is not
    an exact family grounding for the heterogeneous NAP cohort.
  snapshot_sha256: 2d778c0a6dc148b8ae5dd8242ed2ee98cede39e09253798ac3e85ec4a2de2e88
- evidence_id: corpus-boundary-search
  kind: search
  reference: rg --no-ignore --hidden -n GO:0043590|identifier:GO:0009295|label:bacterial_nucleoid
    repo/data/structures
  locator: Complete retained matching-line result; argument patterns are documented
    in search_scope
  accessed_at: '2026-10-22T04:08:18.983280Z'
  support: context_only
  summary: The ignored-inclusive maintained data/structures search finds the one generic
    GO0009295 record and no GO0043590 identifier/reference or exact bacterial-nucleoid
    label. This search does not claim absence outside that maintained corpus surface.
  snapshot_sha256: fece6cb181e2e6f0a771ac057b643a9168ec2f9b4f7b023f1b8fb3f82199b521
  search_scope: 'rg --no-ignore --hidden -n with exact alternation GO:0043590|identifier:
    GO:0009295|label: bacterial nucleoid over all repo/data/structures files, including
    hidden and gitignored paths.'
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/nucleoid/nucleoid.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:42Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/nucleoid/nucleoid.yaml'
  snapshot_sha256: 881d3855eec91832902ca4e0c3337a6ad971b764935a1bf85c5ddcce2bc6dcca
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/nucleoid/nucleoid.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/nucleoid-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:43Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/nucleoid/nucleoid.yaml\
    \ --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/nucleoid-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/nucleoid-strict.tsv"
  snapshot_sha256: f967c9bc72e435904ae77d2a345e7fef8a0f61559e7737a8a3b6c78487b3635a
- evidence_id: nucleoid-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/nucleoid/nucleoid.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T04:01:55.133290Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: nucleoid-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/nucleoid/nucleoid.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T04:01:55.651680Z'
  support: supports
  summary: "data/structures/nucleoid/nucleoid.yaml  (GO:0009295)\n  nap_supercoiling_chromosome_compaction\t\
    nucleoid_associated_proteins\tCOVERED\t->nucleoid_associated_proteins (UniProtKB:P0ACF0,\
    \ UniProtKB:P0ACF4, UniProtKB:P0A6X7, UniProtKB:P0A6Y1, UniProtKB:P0A6R3, UniProtKB:P0ACF8,\
    \ UniProtKB:P0ABT2)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
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
  snapshot_sha256: 060c0334ea540c0999476872bdce276671f1ffa111deee448f7ebcb5fe1291a1
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/nucleoid/nucleoid.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '15 of 17 collected target identifiers returned OK. PMID:21903814: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim.; PMID:333393: UNREACHABLE; Exact native Europe PMC MED
    identifier, title and DOI were reviewed after the bulk eutils414 transport failure.
    Biological support remains bounded by the separately recorded abstract or primary-body
    sections; identity resolution alone is not confirmation of every attached claim.
    Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  snapshot_sha256: 173c367ec1621e2a96027e149b5cad9f4db0a86f0a3c916455ce192a9aa5f428
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:05:35Z'
  support: supports
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 8696c0d603149cee93ac200eaa3ed26c84320204285cd22cca542eb1ae7ba572
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:37Z'
  support: supports
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  snapshot_sha256: 98a7952c42add0416633f4dee73ff64331e5c6c4c4c8d707e98a152f04fc5b6d
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:59:14Z'
  support: supports
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:40Z'
  support: supports
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  snapshot_sha256: 00cc5664a9143235d28fb9885fc5c43a8a78c9a9c9f47603b1232e1eddddeac1
assessments:
- assessment_id: identity
  area: identity
  topic: Generic GO identity is narrowed by bacterial-only defining content
  outcome: concern
  target_ids:
  - GO:0009295
  summary: The identifier GO0009295 is generic and already parents the maintained
    mitochondrial/plastid records, but the target definition requires a bacterial
    chromosome. Native GO supplies GO0043590 for that narrower class. This is a material
    scope mismatch in the defining assertion, independently of the correct bacterial
    biology elsewhere in the record. Preserve the valid generic identity and make
    the bacterial evidence explicitly example-level, or undertake an explicitly authorized
    separate identity decision.
  evidence_ids:
  - record
  - nucleoid-agent-go
  - nucleoid-agent-go-ancestors
  - nucleoid-agent-go-bacterial
  - nucleoid-agent-SL-0187
  - neighbor-mitochondrial_nucleoid
  - neighbor-plastid_nucleoid
  - corpus-boundary-search
- assessment_id: bacterial-material
  area: grounding
  topic: Supported bacterial DNA and heterogeneous NAP examples
  outcome: supported
  target_ids:
  - GO:0009295
  summary: Within the bacterial context, chromosome DNA and the NAP cohort are supported.
    All seven example accession/name/gene/taxon/status combinations and current unique
    exact queries match. Four experimental PMID21903814 location annotations and the
    H-NS PMID333393 annotation are accurately represented; other entries correctly
    remain identity-only. There is no exact single family for this heterogeneous cohort.
  evidence_ids:
  - record
  - nucleoid-agent-dillon2010-meta
  - nucleoid-agent-verma2019-meta
  - nucleoid-agent-verma2019-jats
  - nucleoid-agent-PMID21903814
  - nucleoid-agent-PMID21903814-pmc
  - nucleoid-agent-PMID333393
  - nucleoid-agent-family-IPR000119
  - nucleoid-agent-protein-P0ACF0
  - nucleoid-agent-protein-P0ACF4
  - nucleoid-agent-protein-P0A6X7
  - nucleoid-agent-protein-P0A6Y1
  - nucleoid-agent-protein-P0A6R3
  - nucleoid-agent-protein-P0ACF8
  - nucleoid-agent-protein-P0ABT2
  - nucleoid-agent-gene-hupA
  - nucleoid-agent-gene-hupB
  - nucleoid-agent-gene-ihfA
  - nucleoid-agent-gene-ihfB
  - nucleoid-agent-gene-fis
  - nucleoid-agent-gene-hns
  - nucleoid-agent-gene-dps
- assessment_id: scope
  area: scope
  topic: Bacterial occurrence versus entire generic class
  outcome: supported
  target_ids:
  - GO:0009295
  summary: The Bacteria/E. coli/K-12 native identities are correct and the bacterial
    sources support the conventional chromosome-containing nucleoid context. UNIVERSAL
    is not read as every physiological cell state or a universal NAP complement. The
    E. coli example and bacterial graph do not exhaust the broader generic GO class.
  evidence_ids:
  - record
  - nucleoid-agent-go
  - nucleoid-agent-go-bacterial
  - nucleoid-agent-dillon2010-meta
  - nucleoid-agent-verma2019-jats
  - nucleoid-agent-tax2
  - nucleoid-agent-tax562
  - nucleoid-agent-tax83333
- assessment_id: graph
  area: graph
  topic: Bacterial mechanistic synthesis with source-specific limits
  outcome: supported
  target_ids:
  - GO:0009295
  summary: The graph explicitly describes the bacterial chromosome and is supported
    as a review-level multiscale mechanism sketch. NAP binding, DNA geometry changes,
    supercoiling and packaging are genuine causal content. Its pooled NAP node does
    not mean each protein performs each action; topological-barrier identities and
    some in vivo higher-order arrangements remain inferred. The generic structure
    node can represent the bacterial instance, but cannot cure the bacterial-only
    definition of the entire generic class.
  evidence_ids:
  - record
  - nucleoid-agent-dillon2010-meta
  - nucleoid-agent-verma2019-jats
  - nucleoid-agent-PMID21903814-pmc
- assessment_id: formation
  area: evidence
  topic: Constitution and individual formation necessity
  outcome: unknown
  target_ids:
  - GO:0009295
  summary: Chromosomal DNA is the defining constituting material of the bacterial
    example. The CONDITIONAL NAP cohort does not establish a necessary assembly role
    for every named protein, and the reviewed evidence contains condition- and protein-specific
    effects. Those experimental individual requirements remain unresolved, distinct
    from positive material membership.
  evidence_ids:
  - record
  - schema
  - nucleoid-agent-verma2019-jats
  - nucleoid-agent-PMID21903814-pmc
- assessment_id: coverage
  area: provenance
  topic: Full target and exact bounded source scopes
  outcome: supported
  target_ids:
  - GO:0009295
  summary: All maintained target fields were read with the four-record nucleoid boundary
    set (target plus three neighbors), native identities and the exact source sections
    declared in evidence. Optional inventories and unresolved experimental formation
    requirements are not converted into findings. No scientific edits, promotion,
    save or publication occurred.
  evidence_ids:
  - record
  - schema
  - nucleoid-agent-go
  - nucleoid-agent-go-ancestors
findings:
- finding_id: F1
  issue_key: nucleoid-generic-identifier-bacterial-definition-scope
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Align the bacterial-only definition with the generic nucleoid identity
  description: 'The maintained identifier GO0009295 denotes bacterial, mitochondrial,
    plastid and viral nucleic-acid regions, and the frozen organellar records use
    it as their parent. The target definition instead requires a bacterial chromosome.
    Native GO0043590 is the exact narrower bacterial-nucleoid class. This is more
    than incomplete taxonomic examples: it changes the defining scope of the generic
    record. The bacterial NAP evidence, verified E. coli proteins and example-specific
    mechanism remain valid.'
  target_ids:
  - GO:0009295
  field_paths:
  - definition
  - definition_source
  - identifier
  evidence_ids:
  - record
  - nucleoid-agent-go
  - nucleoid-agent-go-ancestors
  - nucleoid-agent-go-bacterial
  - nucleoid-agent-SL-0187
  - neighbor-mitochondrial_nucleoid
  - neighbor-plastid_nucleoid
  - corpus-boundary-search
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/nucleoid.yaml
    role: maintained scientific record
  rule_id: Exact GO identity and source scope
  native_severity: major
  normalization_reason: An affirmative bacterial-only definition materially narrows
    an explicitly generic ontology identity and excludes its maintained organellar
    children. Major scope/identity normalization is warranted; blocker is unnecessary
    because the generic identifier remains valid and the biological example material
    is usable.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0009295
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/nucleoid/nucleoid.yaml
    role: maintained scientific record
  description: In separately authorized curation, align the generic GO0009295 definition
    with its actual scope and clearly qualify bacterial DNA/NAP/examples and graph
    as bacterial exemplars. Preserve the correct generic identifier and valid organellar
    child relations. If the intended record is instead specifically bacterial nucleoid,
    make that a deliberate separate identity/hierarchy decision using verified GO0043590,
    with all affected references reviewed; do not silently relabel the generic parent.
  acceptance_checks:
  - The defining text and identifier denote the same class and do not exclude the
    maintained mitochondrial/plastid subclasses of generic nucleoid.
  - The original bacterial evidence and seven verified protein examples remain explicitly
    scoped; no unsupported universal protein inventory is introduced.
  - Any separately authorized identity change checks all ignored-inclusive inbound
    references and follows native guarded-writer/history rules.
  - Focused schema/strict, native protein/graph and identifier-label gates pass after
    authorized curation.
limitations:
- Dillon/Dorman2010 is available here at complete native abstract scope only. DOI/Nature
  responses returnedHTTP200 challenge HTML, not the review body. Verma2019 genuine
  full JATS was read only at the listed sections and is secondary synthesis; its cited
  original experiments were not individually recovered.
- Wang2011 genuine complete scientific main text/in-text methods/captions was read,
  without supplementary Methods/TableS1 or pixels. Native PMID333393 identity and
  complete abstract were read; its retained legacy PMC page is scan-based and no scanned
  full body was inspected. The modern H-NS/B1 mapping comes from explicit UniProt
  annotation.
- Current seven exact reviewed gene queries each return the expected single entry;
  these do not reconstruct unretained historical query outputs. K-12 identity does
  not assign every experiment to a particular K-12 substrain.
- The graph is a coarse bacterial/E. coli model. In vitro constraints, protein concentration,
  magnesium, growth phase and unresolved in vivo domain barriers limit universal mechanistic
  interpretation. No exhaustive molecular-family inventory, universal NAP necessity
  or measured all-Bacteria prevalence is certified.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes this one-record bundle even when no defect is found.
  Parent owns integration of the five completed same-base batch26 global gates and
  later finalization.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
