# Gator2 complex scientific review

- Review: 20261022T065213Z-gator2-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:28:23Z
- Finished UTC: 2026-10-22T06:52:13Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

GATOR2/SEACAT identity, five yeast members and positive TORC1 output are supported by source-specific genetic evidence. One grouped minor resolves three exact families, leaving the shared Sec13/Seh1 boundary explicit.

## Scope And Provenance

Exactly one whole maintained target plus frozen guidance and protein-example skill. Actual source-read extents are enumerated per evidence row; no maintained neighboring record supplies scientific evidence.

Selection: Target 9 of batch55, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0061700 | data/structures/other/gator2_complex.yaml | maintained | GATOR2 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0061700 | Focused validator passed. |
| Focused native strict | passed | True | GO:0061700 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0061700 | Native focused check passed; scientific claims assessed separately. |
| Native verify | passed | True | GO:0061700 | Native focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0061700 | No expression-module inference is used. |
| Claim-level scientific review | passed | True | GO:0061700 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0061700 | 15 of 18 collected target identifiers returned OK. PMID:10684247: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:21454883: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0061700 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0061700 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0061700 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0061700 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0061700 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### GATOR2/SEACAT and shared subunits

identity: supported. Targets: GO:0061700.

Exact GO identity, synonym, parent and SEA parthood agree. The five named yeast constituents are correct; shared Sec13/Seh1 do not imply that the whole NPC or COPII coat is a GATOR2 constituent.

### Three resolved classes, two broader-family limits

grounding: concern. Targets: GO:0061700.

Sea2/RTC1, Sea3/MTC5 and Sea4 have verified exact full families. The shared Sec13/Seh1 family remains too broad for two distinct rows. All accession/primary-name/alias and exact-query claims are correct.

### Named yeast model and measured conditions

scope: supported. Targets: GO:0061700.

Species4932 and S288C reference identities are correct. VARIABLE means patchy lineage- or strain-level presence; no such distribution is inferred from these epistasis/localization experiments. The source uses BY4741/2-derived strains and distinguishes25C sec13-1 from30C seh1 assays. Human/fly experiments are counterpart evidence.

### Positive output through an inhibitory branch

graph: supported. Targets: GO:0061700.

The NONMECHANISTIC graph accurately states the coarse positive TORC1 effect. CellCycle directly tests yeast genetic epistasis and supports the antagonism model; human GATOR data are additional counterpart evidence. Neither an atomically resolved inhibition mechanism nor direct binary GATOR2-Rag binding is inferred.

### Activity and localization are not blanket formation requirements

grounding: unknown. Targets: GO:0061700.

The inspected epistasis, GAP, knockdown and localization assays do not establish universal whole-complex formation necessity for each listed protein. UNKNOWN remains appropriate within this bounded evidence scope. Physical membership is supported separately.

### Distribution qualifier beyond experimental examples

scope: unknown. Targets: GO:0061700.

VARIABLE retains the schema meaning of patchy lineage- or strain-level presence. The inspected model-system observations establish occurrence but do not measure or independently establish that taxon-wide distribution pattern; no absence or prevalence conclusion is inferred.

### Complete maintained target with bounded source inspection

completeness: supported. Targets: GO:0061700.

All maintained fields, evidence notes, graph statements and discussions were checked at the declared source extents. Optional inventories and unmeasured formation requirements are not fabricated from native validation.

## Findings

### F1: Ground the Sea2, Sea3 and Sea4 constituent classes

minor / open / confirmed; issue key: gator2-three-exact-families.

Exact WDR24/Sea2, WDR59/Sea3 and MIOS/Sea4 families resolve three current label-only rows without forcing the wider Sec13/Seh1 group into two specific classes.

## Recommended Actions And Acceptance Checks

### A1

Use IPR037590, IPR049567 and IPR037593 for Sea2, Sea3 and Sea4; preserve correct RTC1/MTC5 aliases and narrow the remaining family TODO.

- Do not equate IPR037363 with each distinct Sec13 and Seh1 class.
- Preserve supported identities and source scope; pass applicable native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/gator2_complex.yaml; Entire maintained record, including all evidence, examples, graphs, history and discussions | context_only | The entire record was read. Dated curation history is not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, essentiality, taxonomy and graph-scope contracts | context_only | Essentiality concerns formation rather than activity or viability. COMMON means present in most members, with losses the exception; qualitative synthesis is distinct from a measured census. |
| curation | docs/CURATION.md; Component grounding, including REVIEWED_LABEL_ONLY at159–160 | context_only | A verified exact full-protein family is distinct from a shared domain or broader paralog group. Label-only is not simply a placeholder for an available exact mapping uncurated this pass. |
| complex55-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329,GO:0000938,GO:0005802,GO:0015030,GO:0016604,GO:0031981,GO:0032991,GO:0035859,GO:0038202,GO:0042147,GO:0061700,GO:0097504,GO:0099023,GO:1904262,GO:1904263,GO:1990130; Complete target-relevant definitions/synonyms and typed relationships in combined response; no unrelated child is attributed to this target | supports | GO0061700 identifies GATOR2/SEACAT, yeast five-member and human counterpart classes; GO0035859 supplies its part_of relationship. GO1904263/0038202 define positive TORC1 regulation and signaling. The definition does not independently establish a direct binary Rag-binding mechanism. |
| complex55-agent-GO0061700-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061700/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only closure contains the maintained parent class; this request does not establish parthood. |
| complex55-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA taxonomy identity/names/lineage | supports | Taxon4932 is Saccharomyces cerevisiae, rank species; native names and lineage identify this exact taxon. |
| complex55-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete ENA taxonomy identity/names/lineage | supports | Taxon559292 is Saccharomyces cerevisiae S288C, rank strain; native names and lineage identify this exact taxon. |
| complex55-agent-protein-P38164 | https://rest.uniprot.org/uniprotkb/P38164.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed P38164: SEH-associated protein 4; primary genes SEA4, synonyms none, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-protein-P53011 | https://rest.uniprot.org/uniprotkb/P53011.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed P53011: Nucleoporin SEH1; primary genes SEH1, synonyms none, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-protein-Q03897 | https://rest.uniprot.org/uniprotkb/Q03897.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed Q03897: Maintenance of telomere capping protein 5; primary genes MTC5, synonyms SEA3, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-protein-Q04491 | https://rest.uniprot.org/uniprotkb/Q04491.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed Q04491: Protein transport protein SEC13; primary genes SEC13, synonyms ANU3, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-protein-Q08281 | https://rest.uniprot.org/uniprotkb/Q08281.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed Q08281: Restriction of telomere capping protein 1; primary genes RTC1, synonyms SEA2, taxon559292. Native comments preserve their own experimental/inferred evidence scope. This protein response supplies its family membership xrefs independently of the family-entry metadata. |
| complex55-agent-gene-SEA2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: Q08281. Complete returned gene tokens distinguish primary names from queried aliases. |
| complex55-agent-gene-SEA3-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEA3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: Q03897. Complete returned gene tokens distinguish primary names from queried aliases. |
| complex55-agent-gene-SEA4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEA4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: P38164. Complete returned gene tokens distinguish primary names from queried aliases. |
| complex55-agent-gene-SEH1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEH1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: P53011. Complete returned gene tokens distinguish primary names from queried aliases. |
| complex55-agent-gene-SEC13-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC13%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; All returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: Q04491. Complete returned gene tokens distinguish primary names from queried aliases. |
| complex55-agent-pmid-10684247 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10684247+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and abstract | supports | MED10684247: The yeast nuclear pore complex: composition, architecture, and transport mechanism. Rout MP, Aitchison JD, Suprapto A, Hjertaas K, Zhao Y, Chait BT. (2000), DOI10.1083/jcb.148.4.635. Exact metadata and complete native abstract read; primary body is not implied by this row. |
| complex55-agent-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and abstract | supports | MED14562095: Global analysis of protein localization in budding yeast. Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003), DOI10.1038/nature02026. Exact metadata and complete native abstract read; primary body is not implied by this row. |
| complex55-agent-pmid-21454883 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21454883+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete MED identity and abstract | supports | MED21454883: A conserved coatomer-related complex containing Sec13 and Seh1 dynamically associates with the vacuole in Saccharomyces cerevisiae. Dokudovskaya S, Waharte F, Schlessinger A, Pieper U, Devos DP, Cristea IM, Williams R, Salamero J, Chait BT, Sali A, Field MC, Rout MP, Dargemont C. (2011), DOI10.1074/mcp.m110.006478. Exact metadata and complete native abstract read; primary body is not implied by this row. |
| complex55-agent-doi-science_1232044 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1232044%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract when present | supports | Exact DOI/MED identity: A Tumor suppressor complex with GAP activity for the Rag GTPases that signal amino acid sufficiency to mTORC1. Bar-Peled L, Chantranupong L, Cherniack AD, Chen WW, Ottina KA, Grabiner BC, Spear ED, Carter SL, Meyerson M, Sabatini DM. (2013), PMID23723238. Complete native abstract read.  |
| complex55-agent-doi-cc_26000 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.4161%2Fcc.26000%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract when present | supports | Exact DOI/MED identity: SEACing the GAP that nEGOCiates TORC1 activation: evolutionary conservation of Rag GTPase regulation. Panchaud N, Péli-Gulli MP, De Virgilio C. (2013), PMID23974112. Complete native abstract read.  |
| complex55-agent-primary-PMC3108837 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3108837/; Methods sec4/5/6/9; Results sec17 and sec20; embedded Fig1/3/5 captions. Supplemental strain tables and pixels not independently read. | supports | Dokudovskaya2011 reciprocally purifies the eight-member SEA system and detects vacuole-associated proteins. Npr3-GFP was below detection, while carbonate extraction supports peripheral association; the paper explicitly leaves other locations possible. Earlier GFP-atlas discrepancies are discussed rather than erased. Shared Sec13/Seh1 NPC or COPII functions do not make those entire complexes SEA constituents. |
| complex55-agent-primary-PMC3875668 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3875668/; Complete Introduction sec1, Results/Discussion sec2, Materials/Methods sec3–5 including all strains, Fig1–3 captions. No figure pixels. | supports | Panchaud2013 Cell Cycle contains new yeast epistasis data, not merely a literature review: sec13-1 at25C and seh1 deletion at30C reduce Sch9-phosphorylation TORC1 output, rescued by loss of Iml1. The source names SEACIT and SEACAT and presents their antagonism as a model supported by those genetic experiments. Proposed NPC/secretory coupling remains speculative. |
| complex55-agent-primary-PMC3728654 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3728654/; Complete main prose P1–P14, including in-text experimental descriptions. Supplementary Methods/data and figure pixels/captions were not independently used. | supports | Bar-Peled2013 distinguishes human GATOR1 and GATOR2 by co-IP, tests opposite signaling effects in HEK293T and Drosophila S2 cells, and directly assays GATOR1 GAP activity for RagA/B. Sec13 was excluded from functional knockdown interpretation. Those experiments provide cross-system counterpart context, not direct yeast assays. |
| complex55-agent-ipr-IPR037590 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037590/; Native name/type, complete descriptions/curation flags, signatures and hierarchy; protein membership is independently supplied by UniProt | supports | IPR037590 is the full WDR24 family and explicitly includes yeast Rtc1/Sea2 (PTHR46200). |
| complex55-agent-ipr-IPR049567 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR049567/; Native name/type, complete descriptions/curation flags, signatures and hierarchy; protein membership is independently supplied by UniProt | supports | IPR049567 is the full WDR59-like family, explicitly including fungal Mtc5/Sea3 (PTHR46170). |
| complex55-agent-ipr-IPR037593 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037593/; Native name/type, complete descriptions/curation flags, signatures and hierarchy; protein membership is independently supplied by UniProt | supports | IPR037593 is the full MIOS/Sea4 family (PTHR16453), rather than merely its shared WD-repeat fold. |
| complex55-agent-ipr-IPR037363 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037363/; Native name/type, complete descriptions/curation flags, signatures and hierarchy; protein membership is independently supplied by UniProt | supports | IPR037363 spans both Sec13 and Seh1 (PTHR11024), so it does not independently distinguish these two individual classes. Its incidental GATOR1 wording is not adopted as SEA subcomplex assignment. |
| schema-result | just validate data/structures/other/gator2_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/gator2_complex.yaml |
| strict-result | just validate-strict data/structures/other/gator2_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator2_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/gator2_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator2_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator2_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/gator2_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/gator2_complex.yaml  (GO:0061700)<br>  yeast_gator2_torc1_regulation	sea2_gator2_subunit	COVERED	-&gt;sea2_gator2_subunit (UniProtKB:Q08281)<br>  yeast_gator2_torc1_regulation	sea3_gator2_subunit	COVERED	-&gt;sea3_gator2_subunit (UniProtKB:Q03897)<br>  yeast_gator2_torc1_regulation	sea4_gator2_subunit	COVERED	-&gt;sea4_gator2_subunit (UniProtKB:P38164)<br>  yeast_gator2_torc1_regulation	seh1_gator2_subunit	COVERED	-&gt;seh1_gator2_subunit (UniProtKB:P53011)<br>  yeast_gator2_torc1_regulation	sec13_gator2_subunit	COVERED	-&gt;sec13_gator2_subunit (UniProtKB:Q04491)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     5  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     5  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/gator2_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/gator2_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 15 of 18 collected target identifiers returned OK. PMID:10684247: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:21454883: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates await guarded parent manifest/hash integration.
- No supplemental experiments or atomic coordinates were independently analyzed. Source reading is limited to the exact evidence locators.
- Huh2003 and, for GATOR2, Rout2000 were read at native complete-abstract scope. UniProt annotation-source placement is verified, but a multi-reference annotation is not taken to mean every cited paper independently tested every localization.
- Dokudovskaya Npr3 fluorescence was below detection and earlier Sea2 atlas localization differed; the record accurately reports the current UniProt annotation rather than claiming a fresh reanalysis of those images.
- No SEA/GATOR source figure pixels or supplements were read; functional epistasis and direct biochemical activity are distinguished.
- The VARIABLE lineage/strain distribution qualifier is not independently established by the inspected model-system studies; this bounded access/sampling limit is not a claim that the opposite distribution was demonstrated.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T065213Z-gator2-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Gator2 complex scientific review
started_at: '2026-10-22T06:28:23Z'
finished_at: '2026-10-22T06:52:13Z'
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
summary: GATOR2/SEACAT identity, five yeast members and positive TORC1 output are
  supported by source-specific genetic evidence. One grouped minor resolves three
  exact families, leaving the shared Sec13/Seh1 boundary explicit.
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
  - path: data/structures/other/gator2_complex.yaml
    sha256: 32924c59d1fa042e719e851ad1488c1c18550ec2e442d916d29360fa3e5dac8f
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
- target_id: GO:0061700
  path: data/structures/other/gator2_complex.yaml
  label: GATOR2 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gator2_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one whole maintained target plus frozen guidance and protein-example
    skill. Actual source-read extents are enumerated per evidence row; no maintained
    neighboring record supplies scientific evidence.
  selection: Target 9 of batch55, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0061700
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0061700
  command: just validate data/structures/other/gator2_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0061700
  command: just validate-strict data/structures/other/gator2_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator2_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0061700
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gator2_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0061700
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gator2_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0061700
  summary: No expression-module inference is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0061700
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex55-agent-go
  - complex55-agent-GO0061700-ancestors
  - complex55-agent-tax4932
  - complex55-agent-tax559292
  - complex55-agent-protein-P38164
  - complex55-agent-protein-P53011
  - complex55-agent-protein-Q03897
  - complex55-agent-protein-Q04491
  - complex55-agent-protein-Q08281
  - complex55-agent-gene-SEA2-559292
  - complex55-agent-gene-SEA3-559292
  - complex55-agent-gene-SEA4-559292
  - complex55-agent-gene-SEH1-559292
  - complex55-agent-gene-SEC13-559292
  - complex55-agent-pmid-10684247
  - complex55-agent-pmid-14562095
  - complex55-agent-pmid-21454883
  - complex55-agent-doi-science_1232044
  - complex55-agent-doi-cc_26000
  - complex55-agent-primary-PMC3108837
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
  - complex55-agent-ipr-IPR037590
  - complex55-agent-ipr-IPR049567
  - complex55-agent-ipr-IPR037593
  - complex55-agent-ipr-IPR037363
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0061700
  summary: '15 of 18 collected target identifiers returned OK. PMID:10684247: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:21454883: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - complex55-agent-pmid-10684247
  - complex55-agent-pmid-14562095
  - complex55-agent-pmid-21454883
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0061700
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0061700
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0061700
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0061700
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0061700
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
    and current batch55 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/gator2_complex.yaml
  locator: Entire maintained record, including all evidence, examples, graphs, history
    and discussions
  accessed_at: '2026-10-22T06:42:33Z'
  support: context_only
  summary: The entire record was read. Dated curation history is not independent biological
    evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, essentiality, taxonomy and graph-scope contracts
  accessed_at: '2026-10-22T06:42:33Z'
  support: context_only
  summary: Essentiality concerns formation rather than activity or viability. COMMON
    means present in most members, with losses the exception; qualitative synthesis
    is distinct from a measured census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding, including REVIEWED_LABEL_ONLY at159–160
  accessed_at: '2026-10-22T06:42:33Z'
  support: context_only
  summary: A verified exact full-protein family is distinct from a shared domain or
    broader paralog group. Label-only is not simply a placeholder for an available
    exact mapping uncurated this pass.
- evidence_id: complex55-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329,GO:0000938,GO:0005802,GO:0015030,GO:0016604,GO:0031981,GO:0032991,GO:0035859,GO:0038202,GO:0042147,GO:0061700,GO:0097504,GO:0099023,GO:1904262,GO:1904263,GO:1990130
  locator: Complete target-relevant definitions/synonyms and typed relationships in
    combined response; no unrelated child is attributed to this target
  accessed_at: '2026-10-22T06:33:48.736958Z'
  support: supports
  summary: GO0061700 identifies GATOR2/SEACAT, yeast five-member and human counterpart
    classes; GO0035859 supplies its part_of relationship. GO1904263/0038202 define
    positive TORC1 regulation and signaling. The definition does not independently
    establish a direct binary Rag-binding mechanism.
  snapshot_sha256: e0100a96ac860dcc76d15e08ab106834853c60e10df6b0165c53a6068133006f
- evidence_id: complex55-agent-GO0061700-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0061700/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T06:33:57.371879Z'
  support: supports
  summary: The is_a-only closure contains the maintained parent class; this request
    does not establish parthood.
  snapshot_sha256: c2c179aad5a5d72253c2b097933555c189c59e09b2ab1020f7f2d6f8583d6dff
- evidence_id: complex55-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete ENA taxonomy identity/names/lineage
  accessed_at: '2026-10-22T06:33:48.737823Z'
  support: supports
  summary: Taxon4932 is Saccharomyces cerevisiae, rank species; native names and lineage
    identify this exact taxon.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: complex55-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete ENA taxonomy identity/names/lineage
  accessed_at: '2026-10-22T06:33:48.737778Z'
  support: supports
  summary: Taxon559292 is Saccharomyces cerevisiae S288C, rank strain; native names
    and lineage identify this exact taxon.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: complex55-agent-protein-P38164
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38164.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:49.484190Z'
  support: supports
  summary: 'Reviewed P38164: SEH-associated protein 4; primary genes SEA4, synonyms
    none, taxon559292. Native comments preserve their own experimental/inferred evidence
    scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: c6a2b4f82bca3bf9a6e97509724ec74500e4f346443dc7bcd61977f0974a2120
- evidence_id: complex55-agent-protein-P53011
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53011.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:50.337760Z'
  support: supports
  summary: 'Reviewed P53011: Nucleoporin SEH1; primary genes SEH1, synonyms none,
    taxon559292. Native comments preserve their own experimental/inferred evidence
    scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: 35ef24fc4403d262e26dce09ca3df31c0ca581dd03ee5aec359a29f083be89ba
- evidence_id: complex55-agent-protein-Q03897
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q03897.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:50.689444Z'
  support: supports
  summary: 'Reviewed Q03897: Maintenance of telomere capping protein 5; primary genes
    MTC5, synonyms SEA3, taxon559292. Native comments preserve their own experimental/inferred
    evidence scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: 07eba8d4c94ced4b372fcb9a21fc49509bff301bf690b910125c5accee772121
- evidence_id: complex55-agent-protein-Q04491
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04491.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:51.071792Z'
  support: supports
  summary: 'Reviewed Q04491: Protein transport protein SEC13; primary genes SEC13,
    synonyms ANU3, taxon559292. Native comments preserve their own experimental/inferred
    evidence scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: 5ea1f9385e1989653cc9b1251babdb2a1e325e72d3b3617590028f3fca38207c
- evidence_id: complex55-agent-protein-Q08281
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08281.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:33:51.167867Z'
  support: supports
  summary: 'Reviewed Q08281: Restriction of telomere capping protein 1; primary genes
    RTC1, synonyms SEA2, taxon559292. Native comments preserve their own experimental/inferred
    evidence scope. This protein response supplies its family membership xrefs independently
    of the family-entry metadata.'
  snapshot_sha256: 9368c4334b0d13374d7359c494dc53d967c4d1c5d2ac6c77a29473ddb8000a5b
- evidence_id: complex55-agent-gene-SEA2-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:33:53.833933Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: Q08281. Complete returned
    gene tokens distinguish primary names from queried aliases.'
  snapshot_sha256: e475f0037b7b78fcca3e868fe117ebb2cd01a4b0f4ed2153dfe6ad64959d706a
  search_scope: UniProt gene_exact:SEA2, organism_id:559292, reviewed:true, size500;
    every returned identity inspected.
- evidence_id: complex55-agent-gene-SEA3-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEA3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:33:53.842606Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: Q03897. Complete returned
    gene tokens distinguish primary names from queried aliases.'
  snapshot_sha256: a3cfef0704e04f3337683d3335fcb154dabe91608c988e01cb07b6dcf934b61e
  search_scope: UniProt gene_exact:SEA3, organism_id:559292, reviewed:true, size500;
    every returned identity inspected.
- evidence_id: complex55-agent-gene-SEA4-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEA4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:33:53.869192Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: P38164. Complete returned
    gene tokens distinguish primary names from queried aliases.'
  snapshot_sha256: 11b5e24e1144e94ad39dbc19c244556d78b8bcad2b84c1ed4ad3e71fa936bc81
  search_scope: UniProt gene_exact:SEA4, organism_id:559292, reviewed:true, size500;
    every returned identity inspected.
- evidence_id: complex55-agent-gene-SEH1-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEH1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:33:53.927911Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: P53011. Complete returned
    gene tokens distinguish primary names from queried aliases.'
  snapshot_sha256: 26ff0ea319ad5227fa8a264045b0f5935f47b9a8634a374b4c53bd9b9a9c5278
  search_scope: UniProt gene_exact:SEH1, organism_id:559292, reviewed:true, size500;
    every returned identity inspected.
- evidence_id: complex55-agent-gene-SEC13-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC13%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: All returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:33:54.843692Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: Q04491. Complete returned
    gene tokens distinguish primary names from queried aliases.'
  snapshot_sha256: 8967ba9e2ec39d6cb3ef7e6da9e8cd5ceb82f150094d58f932574e30155b6cba
  search_scope: UniProt gene_exact:SEC13, organism_id:559292, reviewed:true, size500;
    every returned identity inspected.
- evidence_id: complex55-agent-pmid-10684247
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10684247+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and abstract
  accessed_at: '2026-10-22T06:33:54.960274Z'
  support: supports
  summary: 'MED10684247: The yeast nuclear pore complex: composition, architecture,
    and transport mechanism. Rout MP, Aitchison JD, Suprapto A, Hjertaas K, Zhao Y,
    Chait BT. (2000), DOI10.1083/jcb.148.4.635. Exact metadata and complete native
    abstract read; primary body is not implied by this row.'
  snapshot_sha256: a7793d918549c733dfc82d665450d3381170a18b8dbbfd4915a74bac8386e742
- evidence_id: complex55-agent-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and abstract
  accessed_at: '2026-10-22T06:33:55.616568Z'
  support: supports
  summary: 'MED14562095: Global analysis of protein localization in budding yeast.
    Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK. (2003),
    DOI10.1038/nature02026. Exact metadata and complete native abstract read; primary
    body is not implied by this row.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: complex55-agent-pmid-21454883
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A21454883+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete MED identity and abstract
  accessed_at: '2026-10-22T06:33:56.083276Z'
  support: supports
  summary: 'MED21454883: A conserved coatomer-related complex containing Sec13 and
    Seh1 dynamically associates with the vacuole in Saccharomyces cerevisiae. Dokudovskaya
    S, Waharte F, Schlessinger A, Pieper U, Devos DP, Cristea IM, Williams R, Salamero
    J, Chait BT, Sali A, Field MC, Rout MP, Dargemont C. (2011), DOI10.1074/mcp.m110.006478.
    Exact metadata and complete native abstract read; primary body is not implied
    by this row.'
  snapshot_sha256: 1a6d5e9622ab6bffaf489ff3ef11e5b3ca9c3e41de9dfdb446a36759f2697253
- evidence_id: complex55-agent-doi-science_1232044
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1232044%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract when present
  accessed_at: '2026-10-22T06:33:56.698667Z'
  support: supports
  summary: 'Exact DOI/MED identity: A Tumor suppressor complex with GAP activity for
    the Rag GTPases that signal amino acid sufficiency to mTORC1. Bar-Peled L, Chantranupong
    L, Cherniack AD, Chen WW, Ottina KA, Grabiner BC, Spear ED, Carter SL, Meyerson
    M, Sabatini DM. (2013), PMID23723238. Complete native abstract read. '
  snapshot_sha256: 8c43f2aa2133806feabd98634063eb47c9a5badce649c0d0394718c853058ff1
- evidence_id: complex55-agent-doi-cc_26000
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.4161%2Fcc.26000%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract when present
  accessed_at: '2026-10-22T06:33:56.927993Z'
  support: supports
  summary: 'Exact DOI/MED identity: SEACing the GAP that nEGOCiates TORC1 activation:
    evolutionary conservation of Rag GTPase regulation. Panchaud N, Péli-Gulli MP,
    De Virgilio C. (2013), PMID23974112. Complete native abstract read. '
  snapshot_sha256: 6ad0a6ecd5d824bd4a9c7f8d2b1412bc175622f35e481e2952a1ed13e75fd29f
- evidence_id: complex55-agent-primary-PMC3108837
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3108837/
  locator: Methods sec4/5/6/9; Results sec17 and sec20; embedded Fig1/3/5 captions.
    Supplemental strain tables and pixels not independently read.
  accessed_at: '2026-10-22T06:34:37.482929Z'
  support: supports
  summary: Dokudovskaya2011 reciprocally purifies the eight-member SEA system and
    detects vacuole-associated proteins. Npr3-GFP was below detection, while carbonate
    extraction supports peripheral association; the paper explicitly leaves other
    locations possible. Earlier GFP-atlas discrepancies are discussed rather than
    erased. Shared Sec13/Seh1 NPC or COPII functions do not make those entire complexes
    SEA constituents.
  snapshot_sha256: 59b547269d880b49202c1dcdaaa0b7c0a11b73e37d49ac6d5bf72bfef492e299
- evidence_id: complex55-agent-primary-PMC3875668
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3875668/
  locator: Complete Introduction sec1, Results/Discussion sec2, Materials/Methods
    sec3–5 including all strains, Fig1–3 captions. No figure pixels.
  accessed_at: '2026-10-22T06:34:37.254805Z'
  support: supports
  summary: 'Panchaud2013 Cell Cycle contains new yeast epistasis data, not merely
    a literature review: sec13-1 at25C and seh1 deletion at30C reduce Sch9-phosphorylation
    TORC1 output, rescued by loss of Iml1. The source names SEACIT and SEACAT and
    presents their antagonism as a model supported by those genetic experiments. Proposed
    NPC/secretory coupling remains speculative.'
  snapshot_sha256: ec064c7f24e67a4243056b6a8635b2ec44f853a0cf6aff5637cfcba15e0f7cda
- evidence_id: complex55-agent-primary-PMC3728654
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3728654/
  locator: Complete main prose P1–P14, including in-text experimental descriptions.
    Supplementary Methods/data and figure pixels/captions were not independently used.
  accessed_at: '2026-10-22T06:34:37.297541Z'
  support: supports
  summary: Bar-Peled2013 distinguishes human GATOR1 and GATOR2 by co-IP, tests opposite
    signaling effects in HEK293T and Drosophila S2 cells, and directly assays GATOR1
    GAP activity for RagA/B. Sec13 was excluded from functional knockdown interpretation.
    Those experiments provide cross-system counterpart context, not direct yeast assays.
  snapshot_sha256: 962f3e240d6c762e9d8978a81c8f8baf08f2a55af78ba36779156707837d8b58
- evidence_id: complex55-agent-ipr-IPR037590
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037590/
  locator: Native name/type, complete descriptions/curation flags, signatures and
    hierarchy; protein membership is independently supplied by UniProt
  accessed_at: '2026-10-22T06:34:30.540066Z'
  support: supports
  summary: IPR037590 is the full WDR24 family and explicitly includes yeast Rtc1/Sea2
    (PTHR46200).
  snapshot_sha256: 84f64e7a2a4f54ea7162c19d0f2fe8c1ead6c12f95fffb9942a71481799f2650
- evidence_id: complex55-agent-ipr-IPR049567
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR049567/
  locator: Native name/type, complete descriptions/curation flags, signatures and
    hierarchy; protein membership is independently supplied by UniProt
  accessed_at: '2026-10-22T06:34:30.571410Z'
  support: supports
  summary: IPR049567 is the full WDR59-like family, explicitly including fungal Mtc5/Sea3
    (PTHR46170).
  snapshot_sha256: 9df0350b3b4fa3bf41f38a9732745add041feb6d0fe59d6d5a5e3d3e18d67c7f
- evidence_id: complex55-agent-ipr-IPR037593
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037593/
  locator: Native name/type, complete descriptions/curation flags, signatures and
    hierarchy; protein membership is independently supplied by UniProt
  accessed_at: '2026-10-22T06:34:30.663116Z'
  support: supports
  summary: IPR037593 is the full MIOS/Sea4 family (PTHR16453), rather than merely
    its shared WD-repeat fold.
  snapshot_sha256: 3cfac223a2bf6b8afd4545f1f1419d459a6e03b155d6efda52399ebae497f6b1
- evidence_id: complex55-agent-ipr-IPR037363
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037363/
  locator: Native name/type, complete descriptions/curation flags, signatures and
    hierarchy; protein membership is independently supplied by UniProt
  accessed_at: '2026-10-22T06:34:33.255648Z'
  support: supports
  summary: IPR037363 spans both Sec13 and Seh1 (PTHR11024), so it does not independently
    distinguish these two individual classes. Its incidental GATOR1 wording is not
    adopted as SEA subcomplex assignment.
  snapshot_sha256: 56226988fb5e1207346c5a72c10353602cfc00b2617edd105c2c7966f5765e13
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/gator2_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:24Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/gator2_complex.yaml'
  snapshot_sha256: 5e6ea940ca5efc84728065f26468144272f310fd236140ff6443b0f72a8746e3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/gator2_complex.yaml --out
    /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator2_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:26Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/gator2_complex.yaml\
    \ --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator2_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/gator2_complex-strict.tsv"
  snapshot_sha256: 2b9089b7e8065fc4a9ee540e5208a26784fa5f4e83b1e3480f2b5f855e572468
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gator2_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T06:33:59.338282Z'
  support: supports
  summary: "data/structures/other/gator2_complex.yaml  (GO:0061700)\n  yeast_gator2_torc1_regulation\t\
    sea2_gator2_subunit\tCOVERED\t->sea2_gator2_subunit (UniProtKB:Q08281)\n  yeast_gator2_torc1_regulation\t\
    sea3_gator2_subunit\tCOVERED\t->sea3_gator2_subunit (UniProtKB:Q03897)\n  yeast_gator2_torc1_regulation\t\
    sea4_gator2_subunit\tCOVERED\t->sea4_gator2_subunit (UniProtKB:P38164)\n  yeast_gator2_torc1_regulation\t\
    seh1_gator2_subunit\tCOVERED\t->seh1_gator2_subunit (UniProtKB:P53011)\n  yeast_gator2_torc1_regulation\t\
    sec13_gator2_subunit\tCOVERED\t->sec13_gator2_subunit (UniProtKB:Q04491)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     5  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     5  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: db35303745367e8ad8256402bed7b218634934c51f4875551c7ed46370649dd7
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/gator2_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T06:34:00.506479Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/gator2_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '15 of 18 collected target identifiers returned OK. PMID:10684247: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:21454883: UNREACHABLE;
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
  topic: GATOR2/SEACAT and shared subunits
  outcome: supported
  target_ids:
  - GO:0061700
  summary: Exact GO identity, synonym, parent and SEA parthood agree. The five named
    yeast constituents are correct; shared Sec13/Seh1 do not imply that the whole
    NPC or COPII coat is a GATOR2 constituent.
  evidence_ids:
  - record
  - complex55-agent-go
  - complex55-agent-GO0061700-ancestors
  - complex55-agent-primary-PMC3108837
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
  - complex55-agent-protein-P38164
  - complex55-agent-protein-P53011
  - complex55-agent-protein-Q03897
  - complex55-agent-protein-Q04491
  - complex55-agent-protein-Q08281
- assessment_id: grounding
  area: grounding
  topic: Three resolved classes, two broader-family limits
  outcome: concern
  target_ids:
  - GO:0061700
  summary: Sea2/RTC1, Sea3/MTC5 and Sea4 have verified exact full families. The shared
    Sec13/Seh1 family remains too broad for two distinct rows. All accession/primary-name/alias
    and exact-query claims are correct.
  evidence_ids:
  - record
  - curation
  - complex55-agent-ipr-IPR037590
  - complex55-agent-ipr-IPR049567
  - complex55-agent-ipr-IPR037593
  - complex55-agent-ipr-IPR037363
  - complex55-agent-protein-P38164
  - complex55-agent-protein-P53011
  - complex55-agent-protein-Q03897
  - complex55-agent-protein-Q04491
  - complex55-agent-protein-Q08281
  - complex55-agent-gene-SEA2-559292
  - complex55-agent-gene-SEA3-559292
  - complex55-agent-gene-SEA4-559292
  - complex55-agent-gene-SEH1-559292
  - complex55-agent-gene-SEC13-559292
- assessment_id: scope
  area: scope
  topic: Named yeast model and measured conditions
  outcome: supported
  target_ids:
  - GO:0061700
  summary: Species4932 and S288C reference identities are correct. VARIABLE means
    patchy lineage- or strain-level presence; no such distribution is inferred from
    these epistasis/localization experiments. The source uses BY4741/2-derived strains
    and distinguishes25C sec13-1 from30C seh1 assays. Human/fly experiments are counterpart
    evidence.
  evidence_ids:
  - record
  - schema
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
  - complex55-agent-tax4932
  - complex55-agent-tax559292
- assessment_id: graph
  area: graph
  topic: Positive output through an inhibitory branch
  outcome: supported
  target_ids:
  - GO:0061700
  summary: The NONMECHANISTIC graph accurately states the coarse positive TORC1 effect.
    CellCycle directly tests yeast genetic epistasis and supports the antagonism model;
    human GATOR data are additional counterpart evidence. Neither an atomically resolved
    inhibition mechanism nor direct binary GATOR2-Rag binding is inferred.
  evidence_ids:
  - record
  - complex55-agent-go
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
- assessment_id: formation
  area: grounding
  topic: Activity and localization are not blanket formation requirements
  outcome: unknown
  target_ids:
  - GO:0061700
  summary: The inspected epistasis, GAP, knockdown and localization assays do not
    establish universal whole-complex formation necessity for each listed protein.
    UNKNOWN remains appropriate within this bounded evidence scope. Physical membership
    is supported separately.
  evidence_ids:
  - record
  - schema
  - complex55-agent-primary-PMC3108837
  - complex55-agent-primary-PMC3875668
  - complex55-agent-primary-PMC3728654
- assessment_id: presence-unknown
  area: scope
  topic: Distribution qualifier beyond experimental examples
  outcome: unknown
  target_ids:
  - GO:0061700
  summary: VARIABLE retains the schema meaning of patchy lineage- or strain-level
    presence. The inspected model-system observations establish occurrence but do
    not measure or independently establish that taxon-wide distribution pattern; no
    absence or prevalence conclusion is inferred.
  evidence_ids:
  - record
  - schema
  - complex55-agent-tax4932
  - complex55-agent-tax559292
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target with bounded source inspection
  outcome: supported
  target_ids:
  - GO:0061700
  summary: All maintained fields, evidence notes, graph statements and discussions
    were checked at the declared source extents. Optional inventories and unmeasured
    formation requirements are not fabricated from native validation.
  evidence_ids:
  - record
  - schema
  - curation
  - complex55-agent-go
findings:
- finding_id: F1
  issue_key: gator2-three-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the Sea2, Sea3 and Sea4 constituent classes
  description: Exact WDR24/Sea2, WDR59/Sea3 and MIOS/Sea4 families resolve three current
    label-only rows without forcing the wider Sec13/Seh1 group into two specific classes.
  target_ids:
  - GO:0061700
  field_paths:
  - components#sea2_gator2_subunit.grounding_status
  - components#sea3_gator2_subunit.grounding_status
  - components#sea4_gator2_subunit.grounding_status
  - discussions#resolve_gator2_subunit_family_groundings
  evidence_ids:
  - record
  - curation
  - complex55-agent-ipr-IPR037590
  - complex55-agent-ipr-IPR049567
  - complex55-agent-ipr-IPR037593
  - complex55-agent-ipr-IPR037363
  - complex55-agent-protein-P38164
  - complex55-agent-protein-P53011
  - complex55-agent-protein-Q03897
  - complex55-agent-protein-Q04491
  - complex55-agent-protein-Q08281
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gator2_complex.yaml
    role: maintained scientific record
  rule_id: Exact component grounding and source-backed completeness
  native_severity: minor
  normalization_reason: Structure identity, membership and biological direction remain
    correct; this resolves a bounded existing grounding deferral without changing
    the scientific class.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0061700
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/gator2_complex.yaml
    role: maintained scientific record
  description: Use IPR037590, IPR049567 and IPR037593 for Sea2, Sea3 and Sea4; preserve
    correct RTC1/MTC5 aliases and narrow the remaining family TODO.
  acceptance_checks:
  - Do not equate IPR037363 with each distinct Sec13 and Seh1 class.
  - Preserve supported identities and source scope; pass applicable native gates.
limitations:
- Five completed same-base batch26 global gates await guarded parent manifest/hash
  integration.
- No supplemental experiments or atomic coordinates were independently analyzed. Source
  reading is limited to the exact evidence locators.
- Huh2003 and, for GATOR2, Rout2000 were read at native complete-abstract scope. UniProt
  annotation-source placement is verified, but a multi-reference annotation is not
  taken to mean every cited paper independently tested every localization.
- Dokudovskaya Npr3 fluorescence was below detection and earlier Sea2 atlas localization
  differed; the record accurately reports the current UniProt annotation rather than
  claiming a fresh reanalysis of those images.
- No SEA/GATOR source figure pixels or supplements were read; functional epistasis
  and direct biochemical activity are distinguished.
- The VARIABLE lineage/strain distribution qualifier is not independently established
  by the inspected model-system studies; this bounded access/sampling limit is not
  a claim that the opposite distribution was demonstrated.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
