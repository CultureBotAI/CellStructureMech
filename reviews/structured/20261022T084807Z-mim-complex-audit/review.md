# Source-backed review of mim complex

- Review: 20261022T084807Z-mim-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T08:17:23Z
- Finished UTC: 2026-10-22T08:48:07Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: exact MIM identity, component examples, substrate-qualified import relationships and tracked figure provenance are supported. Assay differences and heterologous rescue boundaries are explicitly preserved.

## Scope And Provenance

Exactly one entire maintained target and 15 frozen input files. No neighboring maintained record is an unstated premise. Source tiers and actual read extents are declared per evidence row.

Selection: Batch60 strict ordered selection index 4; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0140595 | data/structures/other/mim_complex.yaml | maintained | MIM complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0140595 | Focused validator passed. |
| Focused native strict | passed | True | GO:0140595 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0140595 | Focused check passed; scientific claims assessed independently. |
| Initial focused native verify | failed | False | GO:0140595 | Executed DNS-limited attempt failed; successful network-enabled retry follows. |
| Focused native verify | passed | True | GO:0140595 | Focused check passed; scientific claims assessed independently. |
| Claim-level scientific review | passed | True | GO:0140595 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0140595 | 15 of 18 collected target identifiers returned OK. PMID:15326197: UNREACHABLE; Native Europe PMC uniquely identifies MED15326197: Two novel proteins in the mitochondrial outer membrane mediate beta-barrel protein assembly. (2004); DOI10.1083/jcb.200405138. This is identifier transport verification; full-body scientific reading is separately scoped.; PMID:15608614: UNREACHABLE; Native Europe PMC uniquely identifies MED15608614: Mim1, a protein required for the assembly of the TOM complex of mitochondria. (2005); DOI10.1038/sj.embor.7400318. This is identifier transport verification; full-body scientific reading is separately scoped.; PMID:22467864: UNREACHABLE; Native Europe PMC uniquely identifies MED22467864: A crucial role for Mim2 in the biogenesis of mitochondrial outer membrane proteins. (2012); DOI10.1242/jcs.103804. This is identifier transport verification; full-body scientific reading is separately scoped. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0140595 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0140595 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0140595 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0140595 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0140595 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### MIM remains distinct from its partners and substitute

identity: supported. Targets: GO:0140595.

Exact GO, two native constituent families and yeast proteins support the MIM identity and outer-membrane placement. TOM, SAM and heterologous pATOM36 are partners or substitutes, not added constituents.

### Substrate- and assay-qualified import mechanism

graph: supported. Targets: GO:0140595.

The five function edges reflect separate association/import/assembly experiments. The record already retains the Vitali-versus-Doan tail-anchor distinction, substrate-limited heterologous rescue and the distinction between a SAM-associated Tom6 intermediate and mature TOM. No atomic route, universal substrate dependence or directly observed dynamic exchange is inferred.

### Formation necessity is not asserted

evidence: unknown. Targets: GO:0140595.

The two component rows omit essentiality. Import defects, reduced growth and morphology rescue are not silently converted into universal necessity for physical MIM formation. No corrective finding is required for this optional omission.

### Two exact families and two reviewed examples

grounding: supported. Targets: GO:0140595.

Mim1 and Mim2 family scopes match the named classes; separate UniProt records and exact gene queries support the S288C examples. Historical beta-barrel/TOM assembly annotations do not redefine MIM as a beta-barrel translocase.

### Yeast reference and assay backgrounds remain separate

scope: supported. Targets: GO:0140595.

COMMON retains the schema majority-occurrence meaning, with exceptional losses; the inspected studies provide qualitative yeast-system support, not a census. Doan uses YPH499, Vitali2018 mainly W303 with stated exceptions, and T.brucei complementation is explicitly heterologous. S288C examples are reference identities.

### Verified figure identity and open license

evidence: supported. Targets: GO:0140595.

Tracked Fig5 pixels and caption agree and the native package MD5 matches exactly. CC BY4.0 permits the reuse. The figure demonstrates mitochondrial morphology/rescue, not direct localization of MIM subunits.

### Entire record assessed without manufacturing optional defects

completeness: supported. Targets: GO:0140595.

All target scientific fields, source notes, current discussions, graph claims, examples and history were read. Optional missing detail and historical access/search limitations are distinguished from actionable present-field defects; no maintained scientific content was changed.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/mim_complex.yaml; Entire maintained YAML, including all scientific fields, examples, graphs, discussions, images and history | context_only | All target bytes were read. No neighboring maintained record is an unstated scientific premise. |
| curation | docs/CURATION.md; Component-class grounding and reviewed-label-only contract | context_only | Species accessions establish examples, not automatic class groundings. Unknowns and empty optional slots alone are not defects. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum and graph actor semantics | context_only | Formation necessity differs from functional activity, viability and localization. COMMON means present in most members with exceptional losses, not merely known occurrence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Source scope, actor identity and mechanism versus descriptive relationships | context_only | Assay, species and epistemic boundaries apply to each graph claim; coarse supported mechanisms need not invent unresolved intermediates. |
| micro60-pmid-15326197 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15326197+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID15326197: Two novel proteins in the mitochondrial outer membrane mediate beta-barrel protein assembly. Ishikawa D, Yamamoto H, Tamura Y, Moritoh K, Endo T. (2004), DOI10.1083/jcb.200405138. Complete native abstract read; no main-body access is implied by this metadata row. |
| micro60-pmid-15608614 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15608614+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID15608614: Mim1, a protein required for the assembly of the TOM complex of mitochondria. Waizenegger T, Schmitt S, Zivkovic J, Neupert W, Rapaport D. (2005), DOI10.1038/sj.embor.7400318. Complete native abstract read; no main-body access is implied by this metadata row. |
| micro60-pmid-22467864 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22467864+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID22467864: A crucial role for Mim2 in the biogenesis of mitochondrial outer membrane proteins. Dimmer KS, Papić D, Schumann B, Sperl D, Krumpe K, Walther DM, Rapaport D. (2012), DOI10.1242/jcs.103804. Complete native abstract read; no main-body access is implied by this metadata row. |
| micro60-doi-10.1016_j.celrep.2020.107567 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.celrep.2020.107567%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID32348752: The Mitochondrial Import Complex MIM Functions as Main Translocase for α-Helical Outer Membrane Proteins. Doan KN, Grevel A, Mårtensson CU, Ellenrieder L, Thornton N, Wenz LS, Opaliński Ł, Guiard B, Pfanner N, Becker T. (2020), DOI10.1016/j.celrep.2020.107567. Complete native abstract read; no main-body access is implied by this metadata row. |
| micro60-doi-10.1016_j.isci.2019.100779 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.isci.2019.100779%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID31945731: The Biogenesis of Mitochondrial Outer Membrane Proteins Show Variable Dependence on Import Factors. Vitali DG, Drwesh L, Cichocki BA, Kolb A, Rapaport D. (2020), DOI10.1016/j.isci.2019.100779. Complete native abstract read; no main-body access is implied by this metadata row. |
| micro60-doi-10.7554_eLife.34488 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.34488%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity and complete abstractText. | supports | PMID29923829: Independent evolution of functionally exchangeable mitochondrial outer membrane import complexes. Vitali DG, Käser S, Kolb A, Dimmer KS, Schneider A, Rapaport D. (2018), DOI10.7554/elife.34488. Complete native abstract read; no main-body access is implied by this metadata row. |
| micro60-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and relevant synonyms. | supports | ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Experimental cultures are distinguished from reference sequence strains. |
| micro60-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxId, scientificName, rank, lineage and relevant synonyms. | supports | ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain. Experimental cultures are distinguished from reference sequence strains. |
| micro60-protein-Q08176 | https://rest.uniprot.org/uniprotkb/Q08176.json; Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments; InterPro cross-references. | supports | Reviewed Q08176 identifies MIM1 in taxon559292; the inspected function, subunit and location comments distinguish the named constituent or recruited example. InterPro cross-references provide accession membership separately from family metadata. Unlisted annotation papers are not certified as read. |
| micro60-protein-Q3E798 | https://rest.uniprot.org/uniprotkb/Q3E798.json; Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR LOCATION comments; InterPro cross-references. | supports | Reviewed Q3E798 identifies MIM2 in taxon559292; the inspected function, subunit and location comments distinguish the named constituent or recruited example. InterPro cross-references provide accession membership separately from family metadata. Unlisted annotation papers are not certified as read. |
| micro60-gene-MIM1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set and exact gene_exact, organism_id and reviewed:true query in original URL. | supports | The exact reviewed MIM1 query for organism559292 returns only Q08176; the primary gene name matches. |
| micro60-gene-MIM2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIM2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identity set and exact gene_exact, organism_id and reviewed:true query in original URL. | supports | The exact reviewed MIM2 query for organism559292 returns only Q3E798; the primary gene name matches. |
| micro60-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444,GO:0000776,GO:0000940,GO:0001401,GO:0005741,GO:0005742,GO:0005743,GO:0034982,GO:0042720,GO:0098799,GO:0098800,GO:0140595,GO:1905370,GO:7770059; Only these six native entries: identity, definition, synonym qualifiers and relevant typed links. | supports | Active GO0140595 identifies the two-subunit MIM complex and its outer-membrane-complex hierarchy. GO7770059 describes helical protein insertion into the mitochondrial outer membrane. GO0005741, GO0005742 and GO0001401 distinguish membrane, SAM and TOM actors. |
| micro60-GO0140595-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140595/ancestors?relations=is_a; Complete exact requested-term is_a ancestor array. | supports | The is_a-only response includes the outer mitochondrial membrane protein-complex and broader membrane/protein-complex ancestors. It does not turn TOM or SAM into MIM constituents. |
| micro60-IPR013262 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013262/; Complete type/name/descriptions/member_databases, distinguishing family from domain or narrower subgroup. | supports | IPR013262 is the Outer membrane protein, MIM1/TOM13, mitochondrial family. Its exact name, integrated signatures and stated class scope were read. Protein membership is established separately; generic background prose is not a direct mechanistic experiment. |
| micro60-IPR037652 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037652/; Complete type/name/descriptions/member_databases, distinguishing family from domain or narrower subgroup. | supports | IPR037652 is the Mim2 family. Its exact name, integrated signatures and stated class scope were read. Protein membership is established separately; generic background prose is not a direct mechanistic experiment. |
| micro60-PMC6010339-xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC6010339.1/PMC6010339.1.xml; Genuine JATS: entire Introduction s1, Results s2-1 through s2-5 and Discussion s3, including embedded main/supplement captions; Methods s4-1,s4-2,s4-4 through s4-7. Recombinant-DNA s4-3, separate supplements and raw data not read. Front permissions CC BY4.0. | supports | Heterologous pATOM36 partially substitutes for Mim1/Mim2 in tested yeast backgrounds and substrates, while Mim1/Mim2 expression in T.brucei only partly substitutes for pATOM36. The proteins remain evolutionarily distinct; rescue does not make pATOM36 a native MIM constituent. Fig5 assays mitochondrial morphology rather than direct MIM localization. |
| micro60-PMC6965732-xml | https://pmc-oa-opendata.s3.amazonaws.com/PMC6965732.1/PMC6965732.1.xml; Genuine JATS: Results sec2.1,sec2.3,sec2.4 and entire Discussion sec3 including sec3.1 limitations; embedded Fig1/2/4/7 captions. Other Results, Introduction, Methods/supplement files and pixels not read. | supports | The steady-state/localization study finds strong Msp1 and moderate Gem1 dependence, whereas Fis1 and Mcr1 are largely MIM-independent in its conditions. Dependence varies by substrate and context; the paper explicitly discusses indirect effects and assay limitations. |
| micro60-doan2020-browser-initial | https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins; Browser-indexed primary-paper text representation, status:null; no native HTTP200 or downloaded PDF claim. Selected primary-paper lines317–384, portions575–1096 and1873–2151; embedded author/license and Methods text. | supports | Primary-paper excerpts identify the study and selected MIM substrate/import and assay context. |
| micro60-doan2020-browser-results | https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins; Browser-indexed primary-paper text representation, status:null; no native HTTP200 or downloaded PDF claim. Selected lines334–495,528–681 and813–1096. | supports | Controlled mim1-23/import, purification and native-gel experiments support signal-anchor dependence and MIM association with distinct TOM/SAM populations. |
| micro60-doan2020-browser-more | https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins; Browser-indexed primary-paper text representation, status:null; no native HTTP200 or downloaded PDF claim. Selected lines464–605,656–867,1065–1276 and2157–2236. | supports | The tail-anchor experiments support Fis1/Gem1 dependence in the tested import conditions. Tom6 accumulates with SAM-MIM and is followed during assembly; dynamic exchange is a proposed model, not directly observed trafficking. |
| micro60-doan2020-browser-methods | https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins; Browser-indexed primary-paper text representation, status:null; no native HTTP200 or downloaded PDF claim. Selected lines2010–2213,2219–2369 and2370–2459. Unrelated cited-by material after2459 is excluded. | supports | YPH499 backgrounds, isolated-mitochondria import, protease protection, two-step assembly, antibody shifts and affinity methods define the experimental scope. Fig captions are text, not independently inspected figure pixels. |
| micro60-doan2020-freidok | https://freidok.uni-freiburg.de/files/165604/PIIS2211124720305167.pdf; Actual final response title/body and transport metadata; unsuccessful body retrieval. | context_only | This HTTP200 response is an institutional IT/security notice, not the cited paper body. Its bytes are excluded from scientific support; genuine bounded browser text is separately retained. |
| micro60-doan2020-storage | https://storage.freidok.ub.uni-freiburg.de/publications/165604/ieaccMPhkWq1nfS5/PIIS2211124720305167.pdf; Actual final response title/body and transport metadata; unsuccessful body retrieval. | context_only | This HTTP200 response is an institutional IT/security notice, not the cited paper body. Its bytes are excluded from scientific support; genuine bounded browser text is separately retained. |
| micro60-PMC6010339-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC6010339.1.json; Exact article identity, license_code and Fig5 media_urls entry. Other media not inspected. | supports | The native article package identifies Fig5 with MD5 be1d9b473460fba31d802e0c3ea5a1bc, matching the tracked figure. Package CC BY is refined by the article permissions to CC BY4.0. |
| fig5 | data/images/other/mim_complex/pmc6010339_fig5.jpg; Full tracked Fig5 pixels; SHA256 cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1 | context_only | MitoGFP/brightfield panels and morphology bars match the caption: WT and mim deletion cells, empty-vector versus pATOM36 rescue. No microscopy measurements were repeated. |
| schema-result | just validate data/structures/other/mim_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/mim_complex.yaml |
| strict-result | just validate-strict data/structures/other/mim_complex.yaml --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mim_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/mim_complex.yaml --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mim_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mim_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --causal-graphs; Complete focused read-only native log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| native-verify-initial | /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --verify; Retained executed sandbox DNS-failure log | context_only | Traceback (most recent call last):<br>  File "/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py", line 922, in &lt;module&gt;<br>    raise SystemExit(main())<br>                     ~~~~^^<br>  File "/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py", line 876, in main<br>    return cmd_verify(records)<br>  File "/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py", line 727, in cmd_verify<br>    issues = verify_records(records)<br>  File "/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py", line 616, in verify_records<br>    entries = fetch_entries_by_accession(all_accs) if all_accs else {}<br>              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^<br>  File "/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py", line 169, in fetch_entries_by_accession<br>    for entry in json.loads(_get(url)).get("results", []):<br>                            ~~~~^^^^^<br>  File "/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py", line 134, in _get<br>    raise RuntimeError(f"UniProt unreachable after {RETRIES} attempts: {last}")<br>RuntimeError: UniProt unreachable after 3 attempts: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt; |
| native-verify | /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --verify; Complete focused read-only native log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/mim_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 15 of 18 collected target identifiers returned OK. PMID:15326197: UNREACHABLE; Native Europe PMC uniquely identifies MED15326197: Two novel proteins in the mitochondrial outer membrane mediate beta-barrel protein assembly. (2004); DOI10.1083/jcb.200405138. This is identifier transport verification; full-body scientific reading is separately scoped.; PMID:15608614: UNREACHABLE; Native Europe PMC uniquely identifies MED15608614: Mim1, a protein required for the assembly of the TOM complex of mitochondria. (2005); DOI10.1038/sj.embor.7400318. This is identifier transport verification; full-body scientific reading is separately scoped.; PMID:22467864: UNREACHABLE; Native Europe PMC uniquely identifies MED22467864: A crucial role for Mim2 in the biogenesis of mitochondrial outer membrane proteins. (2012); DOI10.1242/jcs.103804. This is identifier transport verification; full-body scientific reading is separately scoped. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Doan2020 was read as retained browser-indexed primary text, not a downloaded full PDF: overlapping excerpts cover Results436–1092 and Discussion1094–1167, selected Introduction, main Fig1–4 captions and specified Methods. No Doan figure pixels or raw import measurements were inspected. Institutional HTTP200 responses were unrelated notices.
- Vitali papers were read only in the exact sections named in their evidence rows. Separate supplemental data, movies and raw measurements were not inspected. Only tracked Vitali2018 Fig5 pixels were inspected.
- COMMON is not reduced to mere presence, but an exhaustive strain prevalence survey was not performed. Native sequence examples do not identify every experimental culture. Formation necessity remains unasserted; dynamic exchange is a model.
- Reused source bytes retain original URL, UTC and SHA256. HTTP status alone is not treated as evidence of article-body readability.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requests a review for every unreviewed record, including qualified clean cases.
- Initial inspections and failed access/check attempts are preserved; no scientific record or historical review is edited.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T084807Z-mim-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of mim complex
started_at: '2026-10-22T08:17:23Z'
finished_at: '2026-10-22T08:48:07Z'
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
summary: 'Qualified pass: exact MIM identity, component examples, substrate-qualified
  import relationships and tracked figure provenance are supported. Assay differences
  and heterologous rescue boundaries are explicitly preserved.'
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
  - path: data/images/other/mim_complex/pmc6010339_fig5.jpg
    sha256: cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1
    role: context
  - path: data/structures/other/mim_complex.yaml
    sha256: dc0d4007dfe5d82f22b45d46cc12e3c934ce3ebe92d7ed7b48c25be1ea715c5f
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
- target_id: GO:0140595
  path: data/structures/other/mim_complex.yaml
  label: MIM complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mim_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire maintained target and 15 frozen input files. No
    neighboring maintained record is an unstated premise. Source tiers and actual
    read extents are declared per evidence row.
  selection: Batch60 strict ordered selection index 4; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0140595
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: just validate data/structures/other/mim_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: just validate-strict data/structures/other/mim_complex.yaml --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mim_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific claims assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify-initial
  name: Initial focused native verify
  status: failed
  required: false
  target_ids:
  - GO:0140595
  command: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --verify
  exit_code: 1
  summary: Executed DNS-limited attempt failed; successful network-enabled retry follows.
  evidence_ids:
  - native-verify-initial
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --verify
  exit_code: 0
  summary: Focused check passed; scientific claims assessed independently.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0140595
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro60-pmid-15326197
  - micro60-pmid-15608614
  - micro60-pmid-22467864
  - micro60-doi-10.1016_j.celrep.2020.107567
  - micro60-doi-10.1016_j.isci.2019.100779
  - micro60-doi-10.7554_eLife.34488
  - micro60-tax4932
  - micro60-tax559292
  - micro60-protein-Q08176
  - micro60-protein-Q3E798
  - micro60-gene-MIM1
  - micro60-gene-MIM2
  - micro60-go
  - micro60-GO0140595-ancestors
  - micro60-IPR013262
  - micro60-IPR037652
  - micro60-PMC6010339-xml
  - micro60-PMC6965732-xml
  - micro60-doan2020-browser-initial
  - micro60-doan2020-browser-results
  - micro60-doan2020-browser-more
  - micro60-doan2020-browser-methods
  - micro60-doan2020-freidok
  - micro60-doan2020-storage
  - micro60-PMC6010339-package
  - fig5
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0140595
  summary: '15 of 18 collected target identifiers returned OK. PMID:15326197: UNREACHABLE;
    Native Europe PMC uniquely identifies MED15326197: Two novel proteins in the mitochondrial
    outer membrane mediate beta-barrel protein assembly. (2004); DOI10.1083/jcb.200405138.
    This is identifier transport verification; full-body scientific reading is separately
    scoped.; PMID:15608614: UNREACHABLE; Native Europe PMC uniquely identifies MED15608614:
    Mim1, a protein required for the assembly of the TOM complex of mitochondria.
    (2005); DOI10.1038/sj.embor.7400318. This is identifier transport verification;
    full-body scientific reading is separately scoped.; PMID:22467864: UNREACHABLE;
    Native Europe PMC uniquely identifies MED22467864: A crucial role for Mim2 in
    the biogenesis of mitochondrial outer membrane proteins. (2012); DOI10.1242/jcs.103804.
    This is identifier transport verification; full-body scientific reading is separately
    scoped. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro60-pmid-15326197
  - micro60-pmid-15608614
  - micro60-pmid-22467864
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0140595
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0140595
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
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/mim_complex.yaml
  locator: Entire maintained YAML, including all scientific fields, examples, graphs,
    discussions, images and history
  accessed_at: '2026-10-22T08:35:21Z'
  support: context_only
  summary: All target bytes were read. No neighboring maintained record is an unstated
    scientific premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component-class grounding and reviewed-label-only contract
  accessed_at: '2026-10-22T08:35:21Z'
  support: context_only
  summary: Species accessions establish examples, not automatic class groundings.
    Unknowns and empty optional slots alone are not defects.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum and graph actor semantics
  accessed_at: '2026-10-22T08:35:21Z'
  support: context_only
  summary: Formation necessity differs from functional activity, viability and localization.
    COMMON means present in most members with exceptional losses, not merely known
    occurrence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Source scope, actor identity and mechanism versus descriptive relationships
  accessed_at: '2026-10-22T08:35:21Z'
  support: context_only
  summary: Assay, species and epistemic boundaries apply to each graph claim; coarse
    supported mechanisms need not invent unresolved intermediates.
- evidence_id: micro60-pmid-15326197
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15326197+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:24:39.150279Z'
  support: supports
  summary: 'PMID15326197: Two novel proteins in the mitochondrial outer membrane mediate
    beta-barrel protein assembly. Ishikawa D, Yamamoto H, Tamura Y, Moritoh K, Endo
    T. (2004), DOI10.1083/jcb.200405138. Complete native abstract read; no main-body
    access is implied by this metadata row.'
  snapshot_sha256: 19375ce5ff4b92e669391d5903cbd7efa6bcc53ee6a55e1dbc5c3e546541fe2d
- evidence_id: micro60-pmid-15608614
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15608614+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:24:39.159807Z'
  support: supports
  summary: 'PMID15608614: Mim1, a protein required for the assembly of the TOM complex
    of mitochondria. Waizenegger T, Schmitt S, Zivkovic J, Neupert W, Rapaport D.
    (2005), DOI10.1038/sj.embor.7400318. Complete native abstract read; no main-body
    access is implied by this metadata row.'
  snapshot_sha256: 2f237fcf24e3fe6f056beb601073c71a18085c54857fea87d8b685ba7a351181
- evidence_id: micro60-pmid-22467864
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A22467864+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:24:39.743168Z'
  support: supports
  summary: 'PMID22467864: A crucial role for Mim2 in the biogenesis of mitochondrial
    outer membrane proteins. Dimmer KS, Papić D, Schumann B, Sperl D, Krumpe K, Walther
    DM, Rapaport D. (2012), DOI10.1242/jcs.103804. Complete native abstract read;
    no main-body access is implied by this metadata row.'
  snapshot_sha256: de48c4ae98ef7a6cd2a29473294de08d91150a6633e0f7ec36016ea9cd6f2fd7
- evidence_id: micro60-doi-10.1016_j.celrep.2020.107567
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.celrep.2020.107567%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:24:39.769931Z'
  support: supports
  summary: 'PMID32348752: The Mitochondrial Import Complex MIM Functions as Main Translocase
    for α-Helical Outer Membrane Proteins. Doan KN, Grevel A, Mårtensson CU, Ellenrieder
    L, Thornton N, Wenz LS, Opaliński Ł, Guiard B, Pfanner N, Becker T. (2020), DOI10.1016/j.celrep.2020.107567.
    Complete native abstract read; no main-body access is implied by this metadata
    row.'
  snapshot_sha256: 33bb31bfa3ffc461d601e8dbccab8fa9ac551de25566392e69a8fec36d50dfc1
- evidence_id: micro60-doi-10.1016_j.isci.2019.100779
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.isci.2019.100779%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:24:39.777515Z'
  support: supports
  summary: 'PMID31945731: The Biogenesis of Mitochondrial Outer Membrane Proteins
    Show Variable Dependence on Import Factors. Vitali DG, Drwesh L, Cichocki BA,
    Kolb A, Rapaport D. (2020), DOI10.1016/j.isci.2019.100779. Complete native abstract
    read; no main-body access is implied by this metadata row.'
  snapshot_sha256: 3c24e758cb92a41b01d1ed7a4db1790ccecf6930f0ac81b5275d161a4285a961
- evidence_id: micro60-doi-10.7554_eLife.34488
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.7554%2FeLife.34488%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity and complete abstractText.
  accessed_at: '2026-10-22T08:24:40.419597Z'
  support: supports
  summary: 'PMID29923829: Independent evolution of functionally exchangeable mitochondrial
    outer membrane import complexes. Vitali DG, Käser S, Kolb A, Dimmer KS, Schneider
    A, Rapaport D. (2018), DOI10.7554/elife.34488. Complete native abstract read;
    no main-body access is implied by this metadata row.'
  snapshot_sha256: 2503e111dcdcfb07b7f39f37e258250f936563919793afb1cb7386be52908517
- evidence_id: micro60-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and relevant synonyms.
  accessed_at: '2026-10-22T07:38:47.039448Z'
  support: supports
  summary: ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Experimental
    cultures are distinguished from reference sequence strains.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro60-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact taxId, scientificName, rank, lineage and relevant synonyms.
  accessed_at: '2026-10-22T07:38:47.039624Z'
  support: supports
  summary: ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain.
    Experimental cultures are distinguished from reference sequence strains.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro60-protein-Q08176
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08176.json
  locator: Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:24:39.116516Z'
  support: supports
  summary: Reviewed Q08176 identifies MIM1 in taxon559292; the inspected function,
    subunit and location comments distinguish the named constituent or recruited example.
    InterPro cross-references provide accession membership separately from family
    metadata. Unlisted annotation papers are not certified as read.
  snapshot_sha256: 69251da3064165b1d0a522603415ed78e54d26f496b3dc3ac44cb7b22d61ee39
- evidence_id: micro60-protein-Q3E798
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q3E798.json
  locator: Identity/status/names/genes/organism; complete FUNCTION, SUBUNIT and SUBCELLULAR
    LOCATION comments; InterPro cross-references.
  accessed_at: '2026-10-22T08:24:39.133166Z'
  support: supports
  summary: Reviewed Q3E798 identifies MIM2 in taxon559292; the inspected function,
    subunit and location comments distinguish the named constituent or recruited example.
    InterPro cross-references provide accession membership separately from family
    metadata. Unlisted annotation papers are not certified as read.
  snapshot_sha256: 9b91e795c3fd688963d5f0b0d0f97f5df0e85f4eda23313016cbee5c6797fc68
- evidence_id: micro60-gene-MIM1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set and exact gene_exact, organism_id and reviewed:true
    query in original URL.
  accessed_at: '2026-10-22T08:24:40.573051Z'
  support: supports
  summary: The exact reviewed MIM1 query for organism559292 returns only Q08176; the
    primary gene name matches.
  snapshot_sha256: 5ced4c7a1ca1f7f05b29cedd566a10731ba3f58fd8e99cd74fb300e7fd09ddd2
- evidence_id: micro60-gene-MIM2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AMIM2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identity set and exact gene_exact, organism_id and reviewed:true
    query in original URL.
  accessed_at: '2026-10-22T08:24:40.989144Z'
  support: supports
  summary: The exact reviewed MIM2 query for organism559292 returns only Q3E798; the
    primary gene name matches.
  snapshot_sha256: aae3863f67e2e1eca14e330bdfa326f0174228e06af37d45d257e36a76474342
- evidence_id: micro60-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444,GO:0000776,GO:0000940,GO:0001401,GO:0005741,GO:0005742,GO:0005743,GO:0034982,GO:0042720,GO:0098799,GO:0098800,GO:0140595,GO:1905370,GO:7770059
  locator: 'Only these six native entries: identity, definition, synonym qualifiers
    and relevant typed links.'
  accessed_at: '2026-10-22T08:24:38.435749Z'
  support: supports
  summary: Active GO0140595 identifies the two-subunit MIM complex and its outer-membrane-complex
    hierarchy. GO7770059 describes helical protein insertion into the mitochondrial
    outer membrane. GO0005741, GO0005742 and GO0001401 distinguish membrane, SAM and
    TOM actors.
  snapshot_sha256: eaf537ed0db7d257ec37c171677875dcad35ade113b761962915842d91552658
- evidence_id: micro60-GO0140595-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140595/ancestors?relations=is_a
  locator: Complete exact requested-term is_a ancestor array.
  accessed_at: '2026-10-22T08:24:38.436379Z'
  support: supports
  summary: The is_a-only response includes the outer mitochondrial membrane protein-complex
    and broader membrane/protein-complex ancestors. It does not turn TOM or SAM into
    MIM constituents.
  snapshot_sha256: 95aa205830b66eeaf365cfa1456b235d8665fad35c78d13962d2558a01af33ca
- evidence_id: micro60-IPR013262
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013262/
  locator: Complete type/name/descriptions/member_databases, distinguishing family
    from domain or narrower subgroup.
  accessed_at: '2026-10-22T08:24:41.636095Z'
  support: supports
  summary: IPR013262 is the Outer membrane protein, MIM1/TOM13, mitochondrial family.
    Its exact name, integrated signatures and stated class scope were read. Protein
    membership is established separately; generic background prose is not a direct
    mechanistic experiment.
  snapshot_sha256: d8611a20731dfadc51d22a9fb4c2adec8ece54df8833f8b5f0f09afeb9453748
- evidence_id: micro60-IPR037652
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037652/
  locator: Complete type/name/descriptions/member_databases, distinguishing family
    from domain or narrower subgroup.
  accessed_at: '2026-10-22T08:24:42.119791Z'
  support: supports
  summary: IPR037652 is the Mim2 family. Its exact name, integrated signatures and
    stated class scope were read. Protein membership is established separately; generic
    background prose is not a direct mechanistic experiment.
  snapshot_sha256: 112d5a2021eabf25044253c0dee72db297d4099162b73ee2f355ab61f91ef866
- evidence_id: micro60-PMC6010339-xml
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6010339.1/PMC6010339.1.xml
  locator: 'Genuine JATS: entire Introduction s1, Results s2-1 through s2-5 and Discussion
    s3, including embedded main/supplement captions; Methods s4-1,s4-2,s4-4 through
    s4-7. Recombinant-DNA s4-3, separate supplements and raw data not read. Front
    permissions CC BY4.0.'
  accessed_at: '2026-10-22T08:24:42.248550Z'
  support: supports
  summary: Heterologous pATOM36 partially substitutes for Mim1/Mim2 in tested yeast
    backgrounds and substrates, while Mim1/Mim2 expression in T.brucei only partly
    substitutes for pATOM36. The proteins remain evolutionarily distinct; rescue does
    not make pATOM36 a native MIM constituent. Fig5 assays mitochondrial morphology
    rather than direct MIM localization.
  snapshot_sha256: b3015693fe625623165bc43f68c28ecaf411a5927a5d5bd092ee9f8b48746f5c
- evidence_id: micro60-PMC6965732-xml
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC6965732.1/PMC6965732.1.xml
  locator: 'Genuine JATS: Results sec2.1,sec2.3,sec2.4 and entire Discussion sec3
    including sec3.1 limitations; embedded Fig1/2/4/7 captions. Other Results, Introduction,
    Methods/supplement files and pixels not read.'
  accessed_at: '2026-10-22T08:24:42.302274Z'
  support: supports
  summary: The steady-state/localization study finds strong Msp1 and moderate Gem1
    dependence, whereas Fis1 and Mcr1 are largely MIM-independent in its conditions.
    Dependence varies by substrate and context; the paper explicitly discusses indirect
    effects and assay limitations.
  snapshot_sha256: f6bd13aad6474886ce6b05e1865979c0b31b7433d66486451676b59b12c29447
- evidence_id: micro60-doan2020-browser-initial
  kind: primary_source
  reference: https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins
  locator: Browser-indexed primary-paper text representation, status:null; no native
    HTTP200 or downloaded PDF claim. Selected primary-paper lines317–384, portions575–1096
    and1873–2151; embedded author/license and Methods text.
  accessed_at: '2026-10-22T08:27:36.731503Z'
  support: supports
  summary: Primary-paper excerpts identify the study and selected MIM substrate/import
    and assay context.
  snapshot_sha256: 73d033cf6eac6b36d39069cacf9f97efefc5962235cd22e8850f0860b197c0ed
- evidence_id: micro60-doan2020-browser-results
  kind: primary_source
  reference: https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins
  locator: Browser-indexed primary-paper text representation, status:null; no native
    HTTP200 or downloaded PDF claim. Selected lines334–495,528–681 and813–1096.
  accessed_at: '2026-10-22T08:27:48.511460Z'
  support: supports
  summary: Controlled mim1-23/import, purification and native-gel experiments support
    signal-anchor dependence and MIM association with distinct TOM/SAM populations.
  snapshot_sha256: 692e07245d8293a551ce43e51e4931932ee0a2cd8da917c58c11275f367ff59c
- evidence_id: micro60-doan2020-browser-more
  kind: primary_source
  reference: https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins
  locator: Browser-indexed primary-paper text representation, status:null; no native
    HTTP200 or downloaded PDF claim. Selected lines464–605,656–867,1065–1276 and2157–2236.
  accessed_at: '2026-10-22T08:27:59.766800Z'
  support: supports
  summary: The tail-anchor experiments support Fis1/Gem1 dependence in the tested
    import conditions. Tom6 accumulates with SAM-MIM and is followed during assembly;
    dynamic exchange is a proposed model, not directly observed trafficking.
  snapshot_sha256: 36e35e2090883df8905f318e8c2fc2ac840b46e99cfaa3d70111ebc02585080f
- evidence_id: micro60-doan2020-browser-methods
  kind: primary_source
  reference: https://www.researchgate.net/publication/340985619_The_Mitochondrial_Import_Complex_MIM_Functions_as_Main_Translocase_for_a-Helical_Outer_Membrane_Proteins
  locator: Browser-indexed primary-paper text representation, status:null; no native
    HTTP200 or downloaded PDF claim. Selected lines2010–2213,2219–2369 and2370–2459.
    Unrelated cited-by material after2459 is excluded.
  accessed_at: '2026-10-22T08:28:13.896840Z'
  support: supports
  summary: YPH499 backgrounds, isolated-mitochondria import, protease protection,
    two-step assembly, antibody shifts and affinity methods define the experimental
    scope. Fig captions are text, not independently inspected figure pixels.
  snapshot_sha256: 84d46a3a6d7941c7ef0a484f672e2141b17e62225ecc22b806a8be26d56ec0f9
- evidence_id: micro60-doan2020-freidok
  kind: authority
  reference: https://freidok.uni-freiburg.de/files/165604/PIIS2211124720305167.pdf
  locator: Actual final response title/body and transport metadata; unsuccessful body
    retrieval.
  accessed_at: '2026-10-22T08:25:56.360140Z'
  support: context_only
  summary: This HTTP200 response is an institutional IT/security notice, not the cited
    paper body. Its bytes are excluded from scientific support; genuine bounded browser
    text is separately retained.
  snapshot_sha256: 52d302d4f2e54ce23b47ca8deb0eb52e2a4aa0a09ef50e61f372a6f864c26b1c
- evidence_id: micro60-doan2020-storage
  kind: authority
  reference: https://storage.freidok.ub.uni-freiburg.de/publications/165604/ieaccMPhkWq1nfS5/PIIS2211124720305167.pdf
  locator: Actual final response title/body and transport metadata; unsuccessful body
    retrieval.
  accessed_at: '2026-10-22T08:25:56.359868Z'
  support: context_only
  summary: This HTTP200 response is an institutional IT/security notice, not the cited
    paper body. Its bytes are excluded from scientific support; genuine bounded browser
    text is separately retained.
  snapshot_sha256: 52d302d4f2e54ce23b47ca8deb0eb52e2a4aa0a09ef50e61f372a6f864c26b1c
- evidence_id: micro60-PMC6010339-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC6010339.1.json
  locator: Exact article identity, license_code and Fig5 media_urls entry. Other media
    not inspected.
  accessed_at: '2026-10-22T08:24:42.225194Z'
  support: supports
  summary: The native article package identifies Fig5 with MD5 be1d9b473460fba31d802e0c3ea5a1bc,
    matching the tracked figure. Package CC BY is refined by the article permissions
    to CC BY4.0.
  snapshot_sha256: 1bae97371d88f50dc6b91904b81f4c96bf62c6209d48a761c6042094efab6978
- evidence_id: fig5
  kind: record_content
  reference: data/images/other/mim_complex/pmc6010339_fig5.jpg
  locator: Full tracked Fig5 pixels; SHA256 cdfb8f43e86424b85aa88ac2baa741035d8f107d58fe3b26ad48d595017a5af1
  accessed_at: '2026-10-22T08:35:21Z'
  support: context_only
  summary: 'MitoGFP/brightfield panels and morphology bars match the caption: WT and
    mim deletion cells, empty-vector versus pATOM36 rescue. No microscopy measurements
    were repeated.'
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/mim_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:17:24Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/mim_complex.yaml'
  snapshot_sha256: bb532c5ea85ef04e8a5f0cf8ff013105264ff5e1c740db31cb7563257fbd18b6
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/mim_complex.yaml --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mim_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:17:25Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/mim_complex.yaml\
    \ --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mim_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mim_complex-strict.tsv"
  snapshot_sha256: 089f054a10fc291bfb06b83612731aceacf1aaa7105c9a836dc7565c0cb2a83d
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --causal-graphs
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:24:49.910142Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: native-verify-initial
  kind: validation
  reference: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --verify
  locator: Retained executed sandbox DNS-failure log
  accessed_at: '2026-10-22T08:25:02.360388Z'
  support: context_only
  summary: "Traceback (most recent call last):\n  File \"/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py\"\
    , line 922, in <module>\n    raise SystemExit(main())\n                     ~~~~^^\n\
    \  File \"/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py\"\
    , line 876, in main\n    return cmd_verify(records)\n  File \"/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py\"\
    , line 727, in cmd_verify\n    issues = verify_records(records)\n  File \"/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py\"\
    , line 616, in verify_records\n    entries = fetch_entries_by_accession(all_accs)\
    \ if all_accs else {}\n              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^\n  File\
    \ \"/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py\"\
    , line 169, in fetch_entries_by_accession\n    for entry in json.loads(_get(url)).get(\"\
    results\", []):\n                            ~~~~^^^^^\n  File \"/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/scripts/uniprot_genes.py\"\
    , line 134, in _get\n    raise RuntimeError(f\"UniProt unreachable after {RETRIES}\
    \ attempts: {last}\")\nRuntimeError: UniProt unreachable after 3 attempts: <urlopen\
    \ error [Errno 8] nodename nor servname provided, or not known>"
  snapshot_sha256: 8fb1f2f0bb6a06bd06717a72c33086f65132bee45aeb389260910f990daa5e61
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mim_complex.yaml --verify
  locator: Complete focused read-only native log
  accessed_at: '2026-10-22T08:25:26.487707Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/mim_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '15 of 18 collected target identifiers returned OK. PMID:15326197: UNREACHABLE;
    Native Europe PMC uniquely identifies MED15326197: Two novel proteins in the mitochondrial
    outer membrane mediate beta-barrel protein assembly. (2004); DOI10.1083/jcb.200405138.
    This is identifier transport verification; full-body scientific reading is separately
    scoped.; PMID:15608614: UNREACHABLE; Native Europe PMC uniquely identifies MED15608614:
    Mim1, a protein required for the assembly of the TOM complex of mitochondria.
    (2005); DOI10.1038/sj.embor.7400318. This is identifier transport verification;
    full-body scientific reading is separately scoped.; PMID:22467864: UNREACHABLE;
    Native Europe PMC uniquely identifies MED22467864: A crucial role for Mim2 in
    the biogenesis of mitochondrial outer membrane proteins. (2012); DOI10.1242/jcs.103804.
    This is identifier transport verification; full-body scientific reading is separately
    scoped. Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: MIM remains distinct from its partners and substitute
  outcome: supported
  target_ids:
  - GO:0140595
  summary: Exact GO, two native constituent families and yeast proteins support the
    MIM identity and outer-membrane placement. TOM, SAM and heterologous pATOM36 are
    partners or substitutes, not added constituents.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro60-go
  - micro60-GO0140595-ancestors
  - micro60-PMC6010339-xml
  - micro60-IPR013262
  - micro60-IPR037652
  - micro60-protein-Q08176
  - micro60-protein-Q3E798
- assessment_id: mechanism
  area: graph
  topic: Substrate- and assay-qualified import mechanism
  outcome: supported
  target_ids:
  - GO:0140595
  summary: The five function edges reflect separate association/import/assembly experiments.
    The record already retains the Vitali-versus-Doan tail-anchor distinction, substrate-limited
    heterologous rescue and the distinction between a SAM-associated Tom6 intermediate
    and mature TOM. No atomic route, universal substrate dependence or directly observed
    dynamic exchange is inferred.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro60-go
  - micro60-PMC6010339-xml
  - micro60-PMC6965732-xml
  - micro60-doan2020-browser-initial
  - micro60-doan2020-browser-results
  - micro60-doan2020-browser-more
  - micro60-doan2020-browser-methods
- assessment_id: formation
  area: evidence
  topic: Formation necessity is not asserted
  outcome: unknown
  target_ids:
  - GO:0140595
  summary: The two component rows omit essentiality. Import defects, reduced growth
    and morphology rescue are not silently converted into universal necessity for
    physical MIM formation. No corrective finding is required for this optional omission.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro60-PMC6010339-xml
  - micro60-PMC6965732-xml
  - micro60-doan2020-browser-initial
  - micro60-doan2020-browser-results
  - micro60-doan2020-browser-more
  - micro60-doan2020-browser-methods
- assessment_id: grounding
  area: grounding
  topic: Two exact families and two reviewed examples
  outcome: supported
  target_ids:
  - GO:0140595
  summary: Mim1 and Mim2 family scopes match the named classes; separate UniProt records
    and exact gene queries support the S288C examples. Historical beta-barrel/TOM
    assembly annotations do not redefine MIM as a beta-barrel translocase.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro60-IPR013262
  - micro60-IPR037652
  - micro60-protein-Q08176
  - micro60-protein-Q3E798
  - micro60-gene-MIM1
  - micro60-gene-MIM2
  - micro60-pmid-15326197
  - micro60-pmid-15608614
  - micro60-pmid-22467864
  - micro60-doi-10.1016_j.celrep.2020.107567
  - micro60-doi-10.1016_j.isci.2019.100779
  - micro60-doi-10.7554_eLife.34488
- assessment_id: scope
  area: scope
  topic: Yeast reference and assay backgrounds remain separate
  outcome: supported
  target_ids:
  - GO:0140595
  summary: COMMON retains the schema majority-occurrence meaning, with exceptional
    losses; the inspected studies provide qualitative yeast-system support, not a
    census. Doan uses YPH499, Vitali2018 mainly W303 with stated exceptions, and T.brucei
    complementation is explicitly heterologous. S288C examples are reference identities.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro60-tax4932
  - micro60-tax559292
  - micro60-PMC6010339-xml
  - micro60-PMC6965732-xml
  - micro60-doan2020-browser-initial
  - micro60-doan2020-browser-results
  - micro60-doan2020-browser-more
  - micro60-doan2020-browser-methods
- assessment_id: image
  area: evidence
  topic: Verified figure identity and open license
  outcome: supported
  target_ids:
  - GO:0140595
  summary: Tracked Fig5 pixels and caption agree and the native package MD5 matches
    exactly. CC BY4.0 permits the reuse. The figure demonstrates mitochondrial morphology/rescue,
    not direct localization of MIM subunits.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro60-PMC6010339-xml
  - micro60-PMC6010339-package
  - fig5
- assessment_id: coverage
  area: completeness
  topic: Entire record assessed without manufacturing optional defects
  outcome: supported
  target_ids:
  - GO:0140595
  summary: All target scientific fields, source notes, current discussions, graph
    claims, examples and history were read. Optional missing detail and historical
    access/search limitations are distinguished from actionable present-field defects;
    no maintained scientific content was changed.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro60-go
  - micro60-GO0140595-ancestors
  - micro60-PMC6010339-xml
  - micro60-PMC6965732-xml
  - micro60-PMC6010339-package
  - fig5
  - micro60-doan2020-browser-initial
  - micro60-doan2020-browser-results
  - micro60-doan2020-browser-more
  - micro60-doan2020-browser-methods
  - micro60-doan2020-freidok
  - micro60-doan2020-storage
  - micro60-pmid-15326197
  - micro60-pmid-15608614
  - micro60-pmid-22467864
  - micro60-doi-10.1016_j.celrep.2020.107567
  - micro60-doi-10.1016_j.isci.2019.100779
  - micro60-doi-10.7554_eLife.34488
  - micro60-tax4932
  - micro60-tax559292
  - micro60-IPR013262
  - micro60-IPR037652
  - micro60-protein-Q08176
  - micro60-protein-Q3E798
  - micro60-gene-MIM1
  - micro60-gene-MIM2
findings: []
actions: []
limitations:
- 'Doan2020 was read as retained browser-indexed primary text, not a downloaded full
  PDF: overlapping excerpts cover Results436–1092 and Discussion1094–1167, selected
  Introduction, main Fig1–4 captions and specified Methods. No Doan figure pixels
  or raw import measurements were inspected. Institutional HTTP200 responses were
  unrelated notices.'
- Vitali papers were read only in the exact sections named in their evidence rows.
  Separate supplemental data, movies and raw measurements were not inspected. Only
  tracked Vitali2018 Fig5 pixels were inspected.
- COMMON is not reduced to mere presence, but an exhaustive strain prevalence survey
  was not performed. Native sequence examples do not identify every experimental culture.
  Formation necessity remains unasserted; dynamic exchange is a model.
- Reused source bytes retain original URL, UTC and SHA256. HTTP status alone is not
  treated as evidence of article-body readability.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requests a review for every unreviewed record, including qualified
  clean cases.
- Initial inspections and failed access/check attempts are preserved; no scientific
  record or historical review is edited.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
