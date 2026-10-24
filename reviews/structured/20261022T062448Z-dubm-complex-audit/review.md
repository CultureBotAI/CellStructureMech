# Source-grounded review of DUBm complex

- Review: 20261022T062448Z-dubm-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:03:25Z
- Finished UTC: 2026-10-22T06:24:48Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One grouped minor resolves exact Sgf11, Sus1 and Sgf73 families. Four-subunit identity, SAGA/SLIK parthood, yeast context and descriptive deubiquitinase graph are supported; Ubp8 class identity and formation dependencies remain bounded limitations.

## Scope And Provenance

Exactly one complete maintained target; native-source fields and primary reading scopes are declared in evidence. Scientific inputs remain unchanged.

Selection: One complete record in strict-path batch 53 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0071819 | data/structures/other/dubm_complex.yaml | maintained | DUBm complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0071819 | Focused validator passed. |
| Focused native strict | passed | True | GO:0071819 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0071819 | Focused check passed; source claims assessed separately. |
| Native focused verify | passed | True | GO:0071819 | Focused check passed; source claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0071819 | No expression-module or transcriptomic claim requires this resource. |
| Claim-level scientific review | passed | True | GO:0071819 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0071819 | 14 of 18 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:16855026: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:20230609: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:22932476: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0071819 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0071819 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0071819 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0071819 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0071819 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### DUB module within SAGA and SLIK

identity: supported. Targets: GO:0071819.

The four-subunit DUB identity, nuclear protein-complex parent and SAGA/SLIK parthood are supported. The module is distinct from whole SAGA, HAT and core assemblies; its N-terminal Sgf73 portion does not erase the full-protein constituent identity.

### Four correct examples and three exact families

grounding: concern. Targets: GO:0071819.

The four S288C examples match their declared gene/taxon identities and have native DUB annotations. Exact SGF11, ENY2/Sus1 and SGF73 families can resolve three label-only rows. The inspected broad Ubp8 hydrolase family and catalytic domain do not resolve its specific class.

### Resolution and activity scopes

evidence: supported. Targets: GO:0071819.

Wang supports the DUB-nucleosome reconstruction separately from low-resolution apo placement, so the record does not require a false resolution correction. Henry 2003 supports SAGA-associated Ubp8 H2B deubiquitination at complete-abstract tier. Adamus supports SLIK composition and assayed activity but does not establish unrestricted physiological kinetic identity.

### Composition, parthood and broad deubiquitinase activity

graph: supported. Targets: GO:0071819.

The four constituent edges, SAGA/SLIK parthood and broad activity edge are supported. NONMECHANISTIC scope appropriately leaves out exact ubiquitin orientation and catalytic intermediates.

### Budding-yeast module and component localization

scope: supported. Targets: GO:0071819.

The yeast canonical example is supported. Individual nuclear/P-body annotation links do not move the whole DUB module to every location occupied by Sus1 or Sgf73. Huh and Dastidar abstract contents do not independently resolve each protein-specific localization datum. S288C reference entries remain distinct from purification strains.

### Module formation versus recruitment into SAGA

grounding: unknown. Targets: GO:0071819.

Kohler 2006 deletion analysis supports Ubp8/Sgf11 dependence of Sus1 association with SAGA and a salt-dissociable three-protein subcomplex. This does not by itself establish absence behavior of the complete four-protein DUBm including Sgf73. Activity and nucleoplasmic localization dependencies likewise do not automatically settle every formation UNKNOWN.

### Whole maintained record and bounded follow-up

completeness: supported. Targets: GO:0071819.

All maintained fields, evidence, component/example rows, graph edges, discussion entries and history were read. Available exact mappings are distinguished from optional enrichment and source-access limitations. Scientific status and provenance history remain unchanged.

## Findings

### F1: Resolve three DUB constituent family mappings

minor / open / confirmed; issue key: dubm-sgf11-sus1-sgf73-exact-families.

The open mapping task leaves Sgf11, Sus1 and Sgf73 as REVIEWED_LABEL_ONLY despite exact full-protein families IPR013246, IPR018783 and IPR037804, independently present in their example cross-references. The broader UBP8 candidates checked here do not justify a fourth mapping.

## Recommended Actions And Acceptance Checks

### A1

Ground the three verified constituent classes and narrow the remaining task to unresolved Ubp8 identity. Retain four-component module boundaries and taxon-paired examples.

- Verify class names/types and each separate accession cross-reference.
- Do not substitute a generic USP domain or hydrolase family for Ubp8.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dubm_complex.yaml; Entire maintained record, including all evidence, components, graph, discussions and history | context_only | The complete maintained target was read; related structures are assessed only where this target names them. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and graph scope | context_only | Formation necessity differs from activity, recruitment into a larger assembly or viability. Where used, COMMON means present in most members with exceptional losses. This category is distinct from a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and REVIEWED_LABEL_ONLY contract | context_only | A family grounds the named protein class, while the taxon-paired accession is a representative instance. Exact class mappings can resolve a label-only task. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph evidence and scope | context_only | Composition, coarse functional chemistry and a detailed molecular mechanism are assessed separately. |
| root53-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000124,GO:0004843,GO:0005783,GO:0006890,GO:0030604,GO:0032991,GO:0046695,GO:0070939,GO:0071819,GO:0099023,GO:0140513,GO:1990065; All twelve term definitions, identity/status, synonyms, comments, source xrefs and relevant typed child links; relation types preserved | supports | The twelve active native terms establish the focal complex identities, declared parents, SAGA/SLIK boundaries, cellular locations and functions. GO0070939 has an unrelated acetolactate-synthase comment that the target does not import. GO0030604 specifies the reversible reductoisomerase reaction; its written reverse direction does not contradict forward NADPH consumption. |
| root53-sources-GO0071819-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819/ancestors?relations=is_a; Complete native ancestor response; no parthood inferred from ancestry | supports | The is_a-only ancestry includes nuclear protein-containing complex GO0140513. SAGA/SLIK parthood is a separate relation. |
| root53-sources-GO0071819-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819/constraints; Focal taxonConstraints presence and complete array where present; inherited broad-term exclusions are not distribution evidence | context_only | The focal term has an only_in_taxon Eukaryota constraint; this is not a survey of occurrence. |
| root53-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA identifies 4932 as Saccharomyces cerevisiae. Species and reference-strain scopes remain distinct. |
| root53-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | ENA identifies 559292 as Saccharomyces cerevisiae S288C. Species and reference-strain scopes remain distinct. |
| root53-sources-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 14562095: Global analysis of protein localization in budding yeast. Authors Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.; year 2003; DOI 10.1038/nature02026. Complete abstract read; primary body scope is separately declared. |
| root53-sources-pmid-16855026 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16855026+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 16855026: The mRNA export factor Sus1 is involved in Spt/Ada/Gcn5 acetyltransferase-mediated H2B deubiquitinylation through its interaction with Ubp8 and Sgf11. Authors Köhler A, Pascual-García P, Llopis A, Zapater M, Posas F, Hurt E, Rodríguez-Navarro S.; year 2006; DOI 10.1091/mbc.e06-02-0098. Complete abstract read; primary body scope is separately declared. |
| root53-sources-pmid-20230609 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20230609+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 20230609: A novel link between Sus1 and the cytoplasmic mRNA decay machinery suggests a broad role in mRNA metabolism. Authors Cuenca-Bono B, García-Molinero V, Pascual-García P, García-Oliver E, Llopis A, Rodríguez-Navarro S.; year 2010; DOI 10.1186/1471-2121-11-19. Complete abstract read; primary body scope is separately declared. |
| root53-sources-pmid-22932476 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22932476+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 22932476: The nuclear localization of SWI/SNF proteins is subjected to oxygen regulation. Authors Dastidar RG, Hooda J, Shah A, Cao TM, Henke RM, Zhang L.; year 2012; DOI 10.1186/2045-3701-2-30. Complete abstract read; primary body scope is separately declared. |
| root53-sources-doi-10.1016_j.jbc.2021.100671 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jbc.2021.100671%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and entire abstractText | supports | The exact DOI resolves to MED 33864814, SAGA and SAGA-like SLIK transcriptional coactivators are structurally and biochemically equivalent., Adamus K, Reboul C, Voss J, Huang C, Schittenhelm RB, Le SN, Ellisdon AM, Elmlund H, Boudes M, Elmlund D. (2021). Its full abstract was read; fetching a body elsewhere does not imply full-body inspection. |
| root53-sources-doi-10.1038_s41586-020-1933-5 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-020-1933-5%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and entire abstractText | supports | The exact DOI resolves to MED 31969703, Structure of the transcription coactivator SAGA., Wang H, Dienemann C, Stützer A, Urlaub H, Cheung ACM, Cramer P. (2020). Its full abstract was read; fetching a body elsewhere does not imply full-body inspection. |
| root53-sources-doi-10.1101_gad.1144003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144003%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and entire abstractText | supports | The exact DOI resolves to MED 14563679, Transcriptional activation via sequential histone H2B ubiquitylation and deubiquitylation, mediated by SAGA-associated Ubp8., Henry KW, Wyce A, Lo WS, Duggan LJ, Emre NC, Kao CF, Pillus L, Shilatifard A, Osley MA, Berger SL. (2003). Its full abstract was read; fetching a body elsewhere does not imply full-body inspection. |
| root53-sources-protein-P50102 | https://rest.uniprot.org/uniprotkb/P50102.json; Identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | P50102 is the reviewed UBP8 entry in taxon 559292. The entry distinguishes the C19 UBP8 subfamily from broad hydrolase and catalytic-domain cross-references. |
| root53-sources-gene-UBP8 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AUBP8%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 559292 returns the declared single accession P50102. |
| root53-sources-protein-Q03067 | https://rest.uniprot.org/uniprotkb/Q03067.json; Identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | Q03067 is the reviewed SGF11 entry in taxon 559292. Native nuclear localization cites PMID14562095, independently of the DUB membership annotation. |
| root53-sources-gene-SGF11 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 559292 returns the declared single accession Q03067. |
| root53-sources-protein-Q6WNK7 | https://rest.uniprot.org/uniprotkb/Q6WNK7.json; Identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | Q6WNK7 is the reviewed SUS1 entry in taxon 559292. Native nucleoplasmic localization cites PMID16855026 and P-body localization cites PMID20230609; the source also distinguishes TREX-2 from SAGA membership. |
| root53-sources-gene-SUS1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 559292 returns the declared single accession Q6WNK7. |
| root53-sources-protein-P53165 | https://rest.uniprot.org/uniprotkb/P53165.json; Identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | P53165 is the reviewed SGF73 entry in taxon 559292. Native nuclear and cytoplasmic annotations cite PMID22932476. That annotation link is not a claim that the paper abstract alone names this protein. |
| root53-sources-gene-SGF73 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF73%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 559292 returns the declared single accession P53165. |
| root53-sources-primary-PMC6994259 | https://pmc.ncbi.nlm.nih.gov/articles/PMC6994259/; Wang 2020: all 13 main scientific text paragraphs; Methods S2 endogenous purification, S4 cryo-EM sample, S5 image processing and S7 model building; Figure 4 caption and entire Extended Data Table 2. Other figure captions/pixels, S3 nucleosome preparation, S6 XLMS and supplements not read. | supports | The SAGA study separates the core and peripheral modules. Apo DUB was fitted at low resolution, while nucleosome-bound DUB was reconstructed at 3.7 A; these are distinct reconstructions. The N-terminal Sgf73 region belongs to DUB, while a central region anchors it to the core. Existing DUB structural templates were used rather than every subunit being built de novo. |
| root53-sources-primary-PMC8131915 | https://pmc.ncbi.nlm.nih.gov/articles/PMC8131915/; Adamus 2021: Results sec1.1 purification, 1.2 XLMS, 1.4 DUB assays and 1.7 EM; Methods sec3.1 purification, 3.4 DUB kinetics and 3.11 model building; Figure 1, 3 and 6 captions. Other sections, supplement tables and pixels not read. | supports | Purified SAGA and SLIK contain the DUB subunits. Mass spectrometry and modular EM support composition; the 22.5 A SLIK map does not independently resolve all individual subunit structures. Minimal-substrate Ub-AMC deubiquitinase assays compare activities, with substrate-range limitations; these are not full physiological H2B kinetic equivalence measurements. |
| root53-sources-ipr-IPR013246 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013246/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | SGF11 whole-protein family, integrating MF03047. |
| root53-sources-ipr-IPR018783 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018783/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | ENY2/Sus1 whole-protein homologous family, integrating MF03046, PF10163 and PTHR12514. |
| root53-sources-ipr-IPR037804 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037804/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | SGF73 whole-protein family, integrating PTHR47805. Descriptive generalizations about SAGA are not independent mechanism evidence. |
| root53-sources-ipr-IPR028889 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028889/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | Broad ubiquitin-specific protease catalytic domain, not the whole Ubp8 constituent class. |
| root53-sources-ipr-IPR050185 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050185/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | Broad ubiquitin carboxyl-terminal hydrolase family PTHR21646, not an exact UBP8 family. Its description is flagged as LLM-generated and checked; that prose is not primary mechanistic evidence. |
| schema-result | just validate data/structures/other/dubm_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dubm_complex.yaml |
| strict-result | just validate-strict data/structures/other/dubm_complex.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dubm_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dubm_complex.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dubm_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch53-20261022-kx679dvh/dubm_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dubm_complex.yaml; Complete focused native report | supports | data/structures/other/dubm_complex.yaml  (GO:0071819)<br>  dubm_saga_family_deubiquitination	ubp8_dubm_subunit	COVERED	-&gt;ubp8_dubm_subunit (UniProtKB:P50102)<br>  dubm_saga_family_deubiquitination	sgf11_dubm_subunit	COVERED	-&gt;sgf11_dubm_subunit (UniProtKB:Q03067)<br>  dubm_saga_family_deubiquitination	sus1_dubm_subunit	COVERED	-&gt;sus1_dubm_subunit (UniProtKB:Q6WNK7)<br>  dubm_saga_family_deubiquitination	sgf73_dubm_anchor_subunit	COVERED	-&gt;sgf73_dubm_anchor_subunit (UniProtKB:P53165)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/dubm_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dubm_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 18 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:16855026: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:20230609: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:22932476: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, atomic coordinates, sequence alignments or supplements were reanalyzed. Native protein annotation links and separately read primary text are distinct evidence tiers.
- Henry 2003 and the older localization/Sus1 studies remain complete-abstract and native-annotation tiers; their full methods were not read. Primary SAGA/SLIK body reading is limited to the explicit sections above. The bounded family check leaves Ubp8 unresolved rather than asserting an exhaustive absence of a class identifier. COMMON is not a measured yeast-strain prevalence estimate.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations as well as issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T062448Z-dubm-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of DUBm complex
started_at: '2026-10-22T06:03:25Z'
finished_at: '2026-10-22T06:24:48Z'
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
summary: One grouped minor resolves exact Sgf11, Sus1 and Sgf73 families. Four-subunit
  identity, SAGA/SLIK parthood, yeast context and descriptive deubiquitinase graph
  are supported; Ubp8 class identity and formation dependencies remain bounded limitations.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/other/dubm_complex.yaml
    sha256: 8d25f0c0e04576f7afff2783cf0c88c5c4ee7f5b3a627df47ecdad6eefcbd591
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
- target_id: GO:0071819
  path: data/structures/other/dubm_complex.yaml
  label: DUBm complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dubm_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target; native-source fields and primary
    reading scopes are declared in evidence. Scientific inputs remain unchanged.
  selection: One complete record in strict-path batch 53 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0071819
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: just validate data/structures/other/dubm_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: just validate-strict data/structures/other/dubm_complex.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dubm_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dubm_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dubm_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0071819
  summary: No expression-module or transcriptomic claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0071819
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root53-sources-go
  - root53-sources-GO0071819-ancestors
  - root53-sources-GO0071819-constraints
  - root53-sources-tax4932
  - root53-sources-tax559292
  - root53-sources-pmid-14562095
  - root53-sources-pmid-16855026
  - root53-sources-pmid-20230609
  - root53-sources-pmid-22932476
  - root53-sources-doi-10.1016_j.jbc.2021.100671
  - root53-sources-doi-10.1038_s41586-020-1933-5
  - root53-sources-doi-10.1101_gad.1144003
  - root53-sources-protein-P50102
  - root53-sources-gene-UBP8
  - root53-sources-protein-Q03067
  - root53-sources-gene-SGF11
  - root53-sources-protein-Q6WNK7
  - root53-sources-gene-SUS1
  - root53-sources-protein-P53165
  - root53-sources-gene-SGF73
  - root53-sources-primary-PMC6994259
  - root53-sources-primary-PMC8131915
  - root53-sources-ipr-IPR013246
  - root53-sources-ipr-IPR018783
  - root53-sources-ipr-IPR037804
  - root53-sources-ipr-IPR028889
  - root53-sources-ipr-IPR050185
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0071819
  summary: '14 of 18 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:16855026: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:20230609: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:22932476: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - root53-sources-pmid-14562095
  - root53-sources-pmid-16855026
  - root53-sources-pmid-20230609
  - root53-sources-pmid-22932476
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0071819
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0071819
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
    and current batch53 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dubm_complex.yaml
  locator: Entire maintained record, including all evidence, components, graph, discussions
    and history
  accessed_at: '2026-10-22T06:15:29Z'
  support: context_only
  summary: The complete maintained target was read; related structures are assessed
    only where this target names them.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and graph scope
  accessed_at: '2026-10-22T06:15:29Z'
  support: context_only
  summary: Formation necessity differs from activity, recruitment into a larger assembly
    or viability. Where used, COMMON means present in most members with exceptional
    losses. This category is distinct from a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and REVIEWED_LABEL_ONLY contract
  accessed_at: '2026-10-22T06:15:29Z'
  support: context_only
  summary: A family grounds the named protein class, while the taxon-paired accession
    is a representative instance. Exact class mappings can resolve a label-only task.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph evidence and scope
  accessed_at: '2026-10-22T06:15:29Z'
  support: context_only
  summary: Composition, coarse functional chemistry and a detailed molecular mechanism
    are assessed separately.
- evidence_id: root53-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000124,GO:0004843,GO:0005783,GO:0006890,GO:0030604,GO:0032991,GO:0046695,GO:0070939,GO:0071819,GO:0099023,GO:0140513,GO:1990065
  locator: All twelve term definitions, identity/status, synonyms, comments, source
    xrefs and relevant typed child links; relation types preserved
  accessed_at: '2026-10-22T06:06:00.951715Z'
  support: supports
  summary: The twelve active native terms establish the focal complex identities,
    declared parents, SAGA/SLIK boundaries, cellular locations and functions. GO0070939
    has an unrelated acetolactate-synthase comment that the target does not import.
    GO0030604 specifies the reversible reductoisomerase reaction; its written reverse
    direction does not contradict forward NADPH consumption.
  snapshot_sha256: 1ca0dac2d9f398d290817228e2290a52a1444cc9ebea6b8324d0a056c9cd4c84
- evidence_id: root53-sources-GO0071819-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819/ancestors?relations=is_a
  locator: Complete native ancestor response; no parthood inferred from ancestry
  accessed_at: '2026-10-22T06:06:08.745348Z'
  support: supports
  summary: The is_a-only ancestry includes nuclear protein-containing complex GO0140513.
    SAGA/SLIK parthood is a separate relation.
  snapshot_sha256: af30f0fc4f26edbf10072d95a2232901023c93f0a25cb2a3e806e4ff648f6315
- evidence_id: root53-sources-GO0071819-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071819/constraints
  locator: Focal taxonConstraints presence and complete array where present; inherited
    broad-term exclusions are not distribution evidence
  accessed_at: '2026-10-22T06:06:08.778048Z'
  support: context_only
  summary: The focal term has an only_in_taxon Eukaryota constraint; this is not a
    survey of occurrence.
  snapshot_sha256: 8fe1072f4c20e5fbe6f56e408ce4a573edf16b04799b994937a8f3d7c6c452a1
- evidence_id: root53-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:06:01.933951Z'
  support: supports
  summary: ENA identifies 4932 as Saccharomyces cerevisiae. Species and reference-strain
    scopes remain distinct.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root53-sources-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:06:02.363688Z'
  support: supports
  summary: ENA identifies 559292 as Saccharomyces cerevisiae S288C. Species and reference-strain
    scopes remain distinct.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root53-sources-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:02.965490Z'
  support: supports
  summary: 'MED 14562095: Global analysis of protein localization in budding yeast.
    Authors Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea
    EK.; year 2003; DOI 10.1038/nature02026. Complete abstract read; primary body
    scope is separately declared.'
  snapshot_sha256: 571f7249c52d66a3b53ae05fa04cfe3012ab729c63308d338c745e9f3c1daa72
- evidence_id: root53-sources-pmid-16855026
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16855026+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:03.170437Z'
  support: supports
  summary: 'MED 16855026: The mRNA export factor Sus1 is involved in Spt/Ada/Gcn5
    acetyltransferase-mediated H2B deubiquitinylation through its interaction with
    Ubp8 and Sgf11. Authors Köhler A, Pascual-García P, Llopis A, Zapater M, Posas
    F, Hurt E, Rodríguez-Navarro S.; year 2006; DOI 10.1091/mbc.e06-02-0098. Complete
    abstract read; primary body scope is separately declared.'
  snapshot_sha256: 6204bc8f705de59356eee8f919a0d71b5912318c8401eb53729d8f8c4c3d468f
- evidence_id: root53-sources-pmid-20230609
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A20230609+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:03.330397Z'
  support: supports
  summary: 'MED 20230609: A novel link between Sus1 and the cytoplasmic mRNA decay
    machinery suggests a broad role in mRNA metabolism. Authors Cuenca-Bono B, García-Molinero
    V, Pascual-García P, García-Oliver E, Llopis A, Rodríguez-Navarro S.; year 2010;
    DOI 10.1186/1471-2121-11-19. Complete abstract read; primary body scope is separately
    declared.'
  snapshot_sha256: d15bb11c61f6171f7c406e034d7b45fed3851c072917bbd8728b6c02f05c0a3a
- evidence_id: root53-sources-pmid-22932476
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22932476+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:03.655364Z'
  support: supports
  summary: 'MED 22932476: The nuclear localization of SWI/SNF proteins is subjected
    to oxygen regulation. Authors Dastidar RG, Hooda J, Shah A, Cao TM, Henke RM,
    Zhang L.; year 2012; DOI 10.1186/2045-3701-2-30. Complete abstract read; primary
    body scope is separately declared.'
  snapshot_sha256: 2d5322f655990ba5189e807044ab3706379839f6e7952a1894dd43cc1270c25d
- evidence_id: root53-sources-doi-10.1016_j.jbc.2021.100671
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.jbc.2021.100671%22+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and
    entire abstractText'
  accessed_at: '2026-10-22T06:06:00.952187Z'
  support: supports
  summary: The exact DOI resolves to MED 33864814, SAGA and SAGA-like SLIK transcriptional
    coactivators are structurally and biochemically equivalent., Adamus K, Reboul
    C, Voss J, Huang C, Schittenhelm RB, Le SN, Ellisdon AM, Elmlund H, Boudes M,
    Elmlund D. (2021). Its full abstract was read; fetching a body elsewhere does
    not imply full-body inspection.
  snapshot_sha256: 3245609b66b7adc12826871961a81b77ce85f53b288cd675fcc7aa6219da686e
- evidence_id: root53-sources-doi-10.1038_s41586-020-1933-5
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fs41586-020-1933-5%22+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and
    entire abstractText'
  accessed_at: '2026-10-22T06:06:00.952245Z'
  support: supports
  summary: The exact DOI resolves to MED 31969703, Structure of the transcription
    coactivator SAGA., Wang H, Dienemann C, Stützer A, Urlaub H, Cheung ACM, Cramer
    P. (2020). Its full abstract was read; fetching a body elsewhere does not imply
    full-body inspection.
  snapshot_sha256: f99f438928fb67f3827d4c5efd020c75cd13594cd2e8a6b6bfb632dd2c53e461
- evidence_id: root53-sources-doi-10.1101_gad.1144003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144003%22+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and
    entire abstractText'
  accessed_at: '2026-10-22T06:06:01.816887Z'
  support: supports
  summary: The exact DOI resolves to MED 14563679, Transcriptional activation via
    sequential histone H2B ubiquitylation and deubiquitylation, mediated by SAGA-associated
    Ubp8., Henry KW, Wyce A, Lo WS, Duggan LJ, Emre NC, Kao CF, Pillus L, Shilatifard
    A, Osley MA, Berger SL. (2003). Its full abstract was read; fetching a body elsewhere
    does not imply full-body inspection.
  snapshot_sha256: 35c8537804a0ffba897a304cdb14ea9b4929b230743b45211f539fd5de85cb19
- evidence_id: root53-sources-protein-P50102
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P50102.json
  locator: Identity/status/recommended and alternative names, genes, organism; all
    InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:06:04.350639Z'
  support: supports
  summary: P50102 is the reviewed UBP8 entry in taxon 559292. The entry distinguishes
    the C19 UBP8 subfamily from broad hydrolase and catalytic-domain cross-references.
  snapshot_sha256: 6e1bebc73faae35a7d10d85e423978880a3c99ee0867b7e9b9f45a1c42535a69
- evidence_id: root53-sources-gene-UBP8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AUBP8%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:07.356758Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 559292 returns
    the declared single accession P50102.
  snapshot_sha256: 2a06c64ba1bdc6848dc60295e96f0618cc231bc1a4557b292183492b05422ade
- evidence_id: root53-sources-protein-Q03067
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03067.json
  locator: Identity/status/recommended and alternative names, genes, organism; all
    InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:06:04.853596Z'
  support: supports
  summary: Q03067 is the reviewed SGF11 entry in taxon 559292. Native nuclear localization
    cites PMID14562095, independently of the DUB membership annotation.
  snapshot_sha256: 700291af57b16839d1636cabf1913ac5ec904985aba2d2d29e46170c7e28814f
- evidence_id: root53-sources-gene-SGF11
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF11%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:05.735562Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 559292 returns
    the declared single accession Q03067.
  snapshot_sha256: d84fc08150e2ed10c54646bdb17168b99641ac8950397618b074eacaac883769
- evidence_id: root53-sources-protein-Q6WNK7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q6WNK7.json
  locator: Identity/status/recommended and alternative names, genes, organism; all
    InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:06:05.225299Z'
  support: supports
  summary: Q6WNK7 is the reviewed SUS1 entry in taxon 559292. Native nucleoplasmic
    localization cites PMID16855026 and P-body localization cites PMID20230609; the
    source also distinguishes TREX-2 from SAGA membership.
  snapshot_sha256: fe94c71a434c59a7bf47d758eeb5455593b5917dc385277f4acb67c7f919c7c3
- evidence_id: root53-sources-gene-SUS1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:06.777715Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 559292 returns
    the declared single accession Q6WNK7.
  snapshot_sha256: 8f1b694d2387950128b6fbe42ba576cd99e52d43e0a7cd8177f5803cc66f5fbf
- evidence_id: root53-sources-protein-P53165
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53165.json
  locator: Identity/status/recommended and alternative names, genes, organism; all
    InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:06:04.508529Z'
  support: supports
  summary: P53165 is the reviewed SGF73 entry in taxon 559292. Native nuclear and
    cytoplasmic annotations cite PMID22932476. That annotation link is not a claim
    that the paper abstract alone names this protein.
  snapshot_sha256: 4d6bb37039a2002505921506d07c6bd82cd5ff3a7d62d28ec45ecc541450afc9
- evidence_id: root53-sources-gene-SGF73
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASGF73%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:06.066548Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 559292 returns
    the declared single accession P53165.
  snapshot_sha256: f9556c4862e406e37a9ece3b71cfb86ecf82a18a77ecd576539734b8cb080b36
- evidence_id: root53-sources-primary-PMC6994259
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6994259/
  locator: 'Wang 2020: all 13 main scientific text paragraphs; Methods S2 endogenous
    purification, S4 cryo-EM sample, S5 image processing and S7 model building; Figure
    4 caption and entire Extended Data Table 2. Other figure captions/pixels, S3 nucleosome
    preparation, S6 XLMS and supplements not read.'
  accessed_at: '2026-10-22T06:07:06.671525Z'
  support: supports
  summary: The SAGA study separates the core and peripheral modules. Apo DUB was fitted
    at low resolution, while nucleosome-bound DUB was reconstructed at 3.7 A; these
    are distinct reconstructions. The N-terminal Sgf73 region belongs to DUB, while
    a central region anchors it to the core. Existing DUB structural templates were
    used rather than every subunit being built de novo.
  snapshot_sha256: 875833e81b3cf99d78f4aa5216f35b0f4439329e0f13de7abd4967d9f9ca0e5a
- evidence_id: root53-sources-primary-PMC8131915
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC8131915/
  locator: 'Adamus 2021: Results sec1.1 purification, 1.2 XLMS, 1.4 DUB assays and
    1.7 EM; Methods sec3.1 purification, 3.4 DUB kinetics and 3.11 model building;
    Figure 1, 3 and 6 captions. Other sections, supplement tables and pixels not read.'
  accessed_at: '2026-10-22T06:07:06.671090Z'
  support: supports
  summary: Purified SAGA and SLIK contain the DUB subunits. Mass spectrometry and
    modular EM support composition; the 22.5 A SLIK map does not independently resolve
    all individual subunit structures. Minimal-substrate Ub-AMC deubiquitinase assays
    compare activities, with substrate-range limitations; these are not full physiological
    H2B kinetic equivalence measurements.
  snapshot_sha256: c2b89173a5b55778ec42a890e4708f0f645b66d2c0b084a6995116de9aa96a54
- evidence_id: root53-sources-ipr-IPR013246
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013246/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.783024Z'
  support: supports
  summary: SGF11 whole-protein family, integrating MF03047.
  snapshot_sha256: 19e61ef02df71f24ece84502d7c487596e0146f44ae9820867ce251e8122e546
- evidence_id: root53-sources-ipr-IPR018783
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018783/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.785107Z'
  support: supports
  summary: ENY2/Sus1 whole-protein homologous family, integrating MF03046, PF10163
    and PTHR12514.
  snapshot_sha256: 95b932aadb7a43b64f7714f593fca731839e603abbdf3e1946889426f699d24c
- evidence_id: root53-sources-ipr-IPR037804
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037804/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.527645Z'
  support: supports
  summary: SGF73 whole-protein family, integrating PTHR47805. Descriptive generalizations
    about SAGA are not independent mechanism evidence.
  snapshot_sha256: a57d32fbdc3ee041327bea0d8e2fbd36aaf8973b058da9a8b96b25031b899ead
- evidence_id: root53-sources-ipr-IPR028889
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028889/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.792613Z'
  support: supports
  summary: Broad ubiquitin-specific protease catalytic domain, not the whole Ubp8
    constituent class.
  snapshot_sha256: 987df85f85dc326871a2520fe381c81f16ba533afa9779bc00e37d969f3c602d
- evidence_id: root53-sources-ipr-IPR050185
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050185/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.894269Z'
  support: supports
  summary: Broad ubiquitin carboxyl-terminal hydrolase family PTHR21646, not an exact
    UBP8 family. Its description is flagged as LLM-generated and checked; that prose
    is not primary mechanistic evidence.
  snapshot_sha256: 5bfe72e631d777b27d95335c387204030e37e00942bce6cb49172853bdad88d6
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dubm_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:03:27Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dubm_complex.yaml'
  snapshot_sha256: c7601c22ccbb78eb06344ac5ddda9304cbc79220735644c93128ff4b5a167be9
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dubm_complex.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dubm_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:03:29Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dubm_complex.yaml\
    \ --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dubm_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch53-20261022-kx679dvh/dubm_complex-strict.tsv"
  snapshot_sha256: 1480f201773fdf581f5d44d86ddec3fe6bb438dae3f2217b81c45d02b59b95f4
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dubm_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:06:07.883184Z'
  support: supports
  summary: "data/structures/other/dubm_complex.yaml  (GO:0071819)\n  dubm_saga_family_deubiquitination\t\
    ubp8_dubm_subunit\tCOVERED\t->ubp8_dubm_subunit (UniProtKB:P50102)\n  dubm_saga_family_deubiquitination\t\
    sgf11_dubm_subunit\tCOVERED\t->sgf11_dubm_subunit (UniProtKB:Q03067)\n  dubm_saga_family_deubiquitination\t\
    sus1_dubm_subunit\tCOVERED\t->sus1_dubm_subunit (UniProtKB:Q6WNK7)\n  dubm_saga_family_deubiquitination\t\
    sgf73_dubm_anchor_subunit\tCOVERED\t->sgf73_dubm_anchor_subunit (UniProtKB:P53165)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     4  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     4\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 41ef97ef6e5f7ed9b222fedc877f99f969f29044d849f5f84419f75ca162120e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dubm_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:06:09.121102Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dubm_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 18 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:16855026: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:20230609: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:22932476: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
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
  topic: DUB module within SAGA and SLIK
  outcome: supported
  target_ids:
  - GO:0071819
  summary: The four-subunit DUB identity, nuclear protein-complex parent and SAGA/SLIK
    parthood are supported. The module is distinct from whole SAGA, HAT and core assemblies;
    its N-terminal Sgf73 portion does not erase the full-protein constituent identity.
  evidence_ids:
  - record
  - root53-sources-go
  - root53-sources-GO0071819-ancestors
  - root53-sources-primary-PMC6994259
  - root53-sources-primary-PMC8131915
  - root53-sources-doi-10.1016_j.jbc.2021.100671
  - root53-sources-doi-10.1038_s41586-020-1933-5
  - root53-sources-doi-10.1101_gad.1144003
- assessment_id: composition
  area: grounding
  topic: Four correct examples and three exact families
  outcome: concern
  target_ids:
  - GO:0071819
  summary: The four S288C examples match their declared gene/taxon identities and
    have native DUB annotations. Exact SGF11, ENY2/Sus1 and SGF73 families can resolve
    three label-only rows. The inspected broad Ubp8 hydrolase family and catalytic
    domain do not resolve its specific class.
  evidence_ids:
  - record
  - root53-sources-primary-PMC6994259
  - root53-sources-primary-PMC8131915
  - root53-sources-ipr-IPR013246
  - root53-sources-ipr-IPR018783
  - root53-sources-ipr-IPR037804
  - root53-sources-ipr-IPR028889
  - root53-sources-ipr-IPR050185
  - root53-sources-protein-P50102
  - root53-sources-protein-Q03067
  - root53-sources-protein-Q6WNK7
  - root53-sources-protein-P53165
  - root53-sources-gene-UBP8
  - root53-sources-gene-SGF11
  - root53-sources-gene-SUS1
  - root53-sources-gene-SGF73
- assessment_id: evidence
  area: evidence
  topic: Resolution and activity scopes
  outcome: supported
  target_ids:
  - GO:0071819
  summary: Wang supports the DUB-nucleosome reconstruction separately from low-resolution
    apo placement, so the record does not require a false resolution correction. Henry
    2003 supports SAGA-associated Ubp8 H2B deubiquitination at complete-abstract tier.
    Adamus supports SLIK composition and assayed activity but does not establish unrestricted
    physiological kinetic identity.
  evidence_ids:
  - record
  - root53-sources-primary-PMC6994259
  - root53-sources-primary-PMC8131915
  - root53-sources-doi-10.1016_j.jbc.2021.100671
  - root53-sources-doi-10.1038_s41586-020-1933-5
  - root53-sources-doi-10.1101_gad.1144003
- assessment_id: graph
  area: graph
  topic: Composition, parthood and broad deubiquitinase activity
  outcome: supported
  target_ids:
  - GO:0071819
  summary: The four constituent edges, SAGA/SLIK parthood and broad activity edge
    are supported. NONMECHANISTIC scope appropriately leaves out exact ubiquitin orientation
    and catalytic intermediates.
  evidence_ids:
  - record
  - graphs
  - root53-sources-go
  - root53-sources-primary-PMC6994259
  - root53-sources-primary-PMC8131915
- assessment_id: scope
  area: scope
  topic: Budding-yeast module and component localization
  outcome: supported
  target_ids:
  - GO:0071819
  summary: The yeast canonical example is supported. Individual nuclear/P-body annotation
    links do not move the whole DUB module to every location occupied by Sus1 or Sgf73.
    Huh and Dastidar abstract contents do not independently resolve each protein-specific
    localization datum. S288C reference entries remain distinct from purification
    strains.
  evidence_ids:
  - record
  - root53-sources-GO0071819-constraints
  - root53-sources-primary-PMC6994259
  - root53-sources-primary-PMC8131915
  - root53-sources-tax4932
  - root53-sources-tax559292
  - root53-sources-protein-P50102
  - root53-sources-protein-Q03067
  - root53-sources-protein-Q6WNK7
  - root53-sources-protein-P53165
  - root53-sources-pmid-14562095
  - root53-sources-pmid-16855026
  - root53-sources-pmid-20230609
  - root53-sources-pmid-22932476
- assessment_id: formation
  area: grounding
  topic: Module formation versus recruitment into SAGA
  outcome: unknown
  target_ids:
  - GO:0071819
  summary: Kohler 2006 deletion analysis supports Ubp8/Sgf11 dependence of Sus1 association
    with SAGA and a salt-dissociable three-protein subcomplex. This does not by itself
    establish absence behavior of the complete four-protein DUBm including Sgf73.
    Activity and nucleoplasmic localization dependencies likewise do not automatically
    settle every formation UNKNOWN.
  evidence_ids:
  - record
  - schema
  - root53-sources-pmid-16855026
  - root53-sources-primary-PMC6994259
  - root53-sources-primary-PMC8131915
- assessment_id: coverage
  area: completeness
  topic: Whole maintained record and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0071819
  summary: All maintained fields, evidence, component/example rows, graph edges, discussion
    entries and history were read. Available exact mappings are distinguished from
    optional enrichment and source-access limitations. Scientific status and provenance
    history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root53-sources-go
  - root53-sources-doi-10.1016_j.jbc.2021.100671
  - root53-sources-doi-10.1038_s41586-020-1933-5
  - root53-sources-doi-10.1101_gad.1144003
findings:
- finding_id: F1
  issue_key: dubm-sgf11-sus1-sgf73-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve three DUB constituent family mappings
  description: The open mapping task leaves Sgf11, Sus1 and Sgf73 as REVIEWED_LABEL_ONLY
    despite exact full-protein families IPR013246, IPR018783 and IPR037804, independently
    present in their example cross-references. The broader UBP8 candidates checked
    here do not justify a fourth mapping.
  target_ids:
  - GO:0071819
  field_paths:
  - components[1].grounding_status
  - components[2].grounding_status
  - components[3].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root53-sources-ipr-IPR013246
  - root53-sources-ipr-IPR018783
  - root53-sources-ipr-IPR037804
  - root53-sources-protein-P50102
  - root53-sources-protein-Q03067
  - root53-sources-protein-Q6WNK7
  - root53-sources-protein-P53165
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dubm_complex.yaml
    role: maintained scientific record
  rule_id: Exact protein class grounding
  native_severity: minor
  normalization_reason: Identity and supported composition remain intact; this is
    a bounded available class mapping that can resolve an existing task.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0071819
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dubm_complex.yaml
    role: maintained scientific record
  description: Ground the three verified constituent classes and narrow the remaining
    task to unresolved Ubp8 identity. Retain four-component module boundaries and
    taxon-paired examples.
  acceptance_checks:
  - Verify class names/types and each separate accession cross-reference.
  - Do not substitute a generic USP domain or hydrolase family for Ubp8.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, atomic coordinates, sequence alignments or supplements
  were reanalyzed. Native protein annotation links and separately read primary text
  are distinct evidence tiers.
- Henry 2003 and the older localization/Sus1 studies remain complete-abstract and
  native-annotation tiers; their full methods were not read. Primary SAGA/SLIK body
  reading is limited to the explicit sections above. The bounded family check leaves
  Ubp8 unresolved rather than asserting an exhaustive absence of a class identifier.
  COMMON is not a measured yeast-strain prevalence estimate.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations as well as issue-bearing
  reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
