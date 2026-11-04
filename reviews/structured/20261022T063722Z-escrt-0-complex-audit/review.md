# Source-backed review of escrt 0 complex

- Review: 20261022T063722Z-escrt-0-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:16:14Z
- Finished UTC: 2026-10-22T06:37:22Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two bounded minors: the visible copied Vps1 definition conflicts with the correctly curated Vps27 complex, and exact Vps27/Hrs family grounding is available. Hse1 broad-family substitution is withheld; supported protein identities and Vps27-specific recruitment are retained.

## Scope And Provenance

Exactly one complete maintained target plus frozen governing/schema/protein/graph guidance. Native identity and directly read literature tiers are distinguished; no neighboring maintained record is an unstated scientific premise.

Selection: Batch54 strict ordered selection, index 5; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033565 | data/structures/other/escrt_0_complex.yaml | maintained | ESCRT-0 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0033565 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033565 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0033565 | Focused check passed; scientific scope independently assessed. |
| Focused native verify | failed | False | GO:0033565 | Executed sandbox attempt failed because DNS was unavailable; optional historical attempt retained, followed by successful network retry. |
| Focused native verify network retry | passed | True | GO:0033565 | Focused check passed; scientific scope independently assessed. |
| Claim-level scientific review | passed | True | GO:0033565 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0033565 | 12 of 16 collected target identifiers returned OK. PMID:12006563: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:12055639: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:12900393: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0033565 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033565 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033565 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033565 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0033565 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Correct ESCRT-0 identity with a localized copied-definition conflict

identity: concern. Targets: GO:0033565.

GO identity, synonyms, parent and endosomal boundary identify ESCRT-0 correctly. The copied definition still names Vps1p even though the record explicitly resolves this discrepancy and represents Vps27/Hse1 elsewhere; the current definition requires a narrow correction with transparent source attribution.

### Two supported constituents and one exact family gap

grounding: concern. Targets: GO:0033565.

Bilodeau complete abstract and native SUBUNIT comments support Vps27/Hse1. IPR017073 exactly addresses the Vps27/Hrs boundary and can resolve that existing class. The independently checked mixed IPR050670/PTHR45929 membership justifies withholding the broader candidate from Hse1; its family label is insufficient.

### Ub-dependent sorting and Vps27-specific recruitment

evidence: supported. Targets: GO:0033565.

The primary abstract supports complex Ub binding/endosomal sorting. Katzmann directly supports Vps27-specific ESCRT-I recruitment and interaction at endosomal membranes. The corrected edge does not require the whole Hse1-containing complex for every measured recruitment result.

### Yeast and mammalian naming boundaries

scope: supported. Targets: GO:0033565.

The S.cerevisiae example and S288C reference accessions are valid, while Katzmann uses explicitly listed SEY6210 derivatives. COMMON retains the schema majority-occurrence meaning with exceptional losses; these experiments are qualitative support, not a measured census. The mammalian Hrs/STAM synonym does not export every yeast perturbation to mammals.

### Protein identities and annotation provenance

grounding: supported. Targets: GO:0033565.

Both exact-organism reviewed queries are single hits matching the existing examples. The five listed PMID occurrences and ECO location assertions match native comments; isolated-domain or survey localization evidence is not promoted to physical complex formation.

### Five bounded descriptive edges

graph: supported. Targets: GO:0033565.

NONMECHANISTIC scope fits the two membership edges, Ub binding, Vps27-specific recruitment and MVB participation. Typed node/component references are correct. The graph avoids an untested full ESCRT handoff or Hse1-dependent recruitment mechanism.

### Both constituent necessity labels remain unknown

evidence: unknown. Targets: GO:0033565.

The existing UNKNOWN labels do not conflate sorting defects, location, Ub binding or lumenal-vesicle production with formation of ESCRT-0 itself. No universal per-subunit formation requirement is established by the inspected abstract/primary sections.

### Whole target with bounded source and unresolved scope

completeness: supported. Targets: GO:0033565.

All current scientific fields, source placements, graph edges, discussions and history were reviewed. Historical first-pass wording is not treated as false merely because present access differs. The stated findings isolate concrete current changes; optional unverified detail remains a limitation.

## Findings

### F1: Reconcile the copied Vps1 definition with the curated Vps27 complex

minor / open / confirmed; issue key: escrt-0-copied-vps1-definition-conflict.

The definition says Vps1p and Hse1p, faithfully reproducing the current GO text, while the exact synonym, Bilodeau abstract, native subunit identities and the record's resolved discussion identify Vps27p/Hse1p. The resolved discussion protects the component table but leaves the misleading definition visible.

### F2: Resolve the verified Vps27/Hrs family grounding

minor / open / confirmed; issue key: escrt-0-vps27-hrs-exact-family-grounding.

The current Vps27 row is REVIEWED_LABEL_ONLY with an open exact-family task. Native IPR017073 explicitly covers Hrs/Vps27 and native P40343 corroborates membership. In contrast, the independently inspected Hse1 candidate is broader and is not part of this correction.

## Recommended Actions And Acceptance Checks

### A1

Correct the local definition to Vps27p with an appropriate primary-source attribution or explicit qualifier documenting the native GO discrepancy. Preserve GO0033565 identity, correct component rows and historical evidence rather than silently rewriting the external source.

- The visible definition no longer presents Vps1 as the curated ESCRT-0 constituent.
- The source relationship and known GO discrepancy remain explicit.
- Native schema, strict and CURIE checks pass after separately authorized curation.

### A2

Add InterPro:IPR017073 to the existing Vps27 class with exact source evidence and update its grounding state/task. Keep P40343 as the taxon-paired example and retain Hse1 label-only unless a genuinely exact class is separately verified.

- The new grounding denotes the Hrs/Vps27 whole-protein family, not its domains.
- The mixed Hse1 candidate is not adopted as an exact substitute.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/escrt_0_complex.yaml; Complete current YAML: every scientific field, citation, component/example, graph edge, discussion and history | context_only | The entire target was read. No neighboring maintained record supplies an unstated scientific premise. |
| curation | docs/CURATION.md; Component-class grounding, label-only representation and formation necessity | context_only | Known named constituents can be recorded with reviewed label-only grounding when exact families remain unresolved. Protein examples are not family identities; formation necessity is distinct from activity or viability. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum | context_only | COMMON means present in most taxon members, with exceptional losses; UNKNOWN does not claim demonstrated formation necessity. An exact source-neutral class is distinct from a species accession or a shared domain. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope, typed nodes and source-specific edges | context_only | Descriptive composition/function graphs may remain NONMECHANISTIC. Experimental system and actor scope must match each edge. |
| micro54-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native taxId/scientificName/rank and lineage fields. | supports | ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. This identity does not establish a quantitative within-species prevalence census. |
| micro54-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621; Exact target/parent/endosome/function/ESCRT-I entries, definitions, synonyms and relevant typed children in the shared response. | supports | Native GO0033565 retains the Vps1p wording while its exact synonym is Vps27p-Hse1p; the discrepancy is recorded rather than silently treated as correct biology. GO0036452 lists ESCRT-0 as an is_a child and is itself part_of endosome through the typed GO0005768 child list. GO0071985 supplies the MVB sorting process; GO0000813 is ESCRT-I. |
| micro54-GO0033565-ancestors-network | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033565/ancestors?relations=is_a; Complete relations=is_a ancestors array. | supports | The is_a-only array confirms ESCRT-complex and protein-containing-complex ancestry. Endosome location is corroborated separately, not inferred from this array. |
| micro54-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Native taxId/scientificName/rank/lineage fields. | supports | ENA taxId559292 is Saccharomyces cerevisiae S288C, rank strain; the maintained reference-protein examples use this identity correctly. |
| micro54-pmid-12006563-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12006563+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry, exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID12006563: Phosphatidylinositol 3-phosphate induces the membrane penetration of the FYVE domains of Vps27p and Hrs. Stahelin RV, Long F, Diraviyam K, Bruzik KS, Murray D, Cho W. (2002), DOI10.1074/jbc.m201106200. Exact identity and complete native abstract read. The abstract describes isolated FYVE-domain membrane-binding and monolayer assays, not a whole-cell complex-formation test. |
| micro54-pmid-12055639-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12055639+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry, exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID12055639: The Vps27p Hse1p complex binds ubiquitin and mediates endosomal protein sorting. Bilodeau PS, Urbanowski JL, Winistorfer SC, Piper RC. (2002), DOI10.1038/ncb815. Exact identity and complete native abstract read. It explicitly identifies Vps27p/Hse1p, endosomal localization and Ub binding; UIM mutants impair cargo sorting while lumenal membrane generation continues. |
| micro54-pmid-12900393-network | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12900393+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry, exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID12900393: Vps27 recruits ESCRT machinery to endosomes during MVB sorting. Katzmann DJ, Stefan CJ, Babst M, Emr SD. (2003), DOI10.1083/jcb.200302136. Exact identity and complete native abstract read. |
| micro54-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry, exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID14562095: Global analysis of protein localization in budding yeast. Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003), DOI10.1038/nature02026. Exact identity and complete native abstract read. The abstract describes a tagged-yeast localization survey; individual protein annotation evidence is checked in the native UniProt entries, not inferred from the abstract. |
| micro54-doi-j_devcel_2011_05_015 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2011.05.015%22&amp;format=json&amp;resultType=core; Unique MED entry and complete abstractText; no review main-body claim. | supports | Henne/Buchkovich/Emr2011, The ESCRT pathway, DOI10.1016/j.devcel.2011.05.015 PMID21763610, is a secondary review. Its complete native abstract supports the cargo-recognition/membrane-sculpting framework and MVB, viral budding and abscission roles; detailed subunit prose is not certified from this abstract alone. |
| micro54-katzmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/; Genuine primary HTML: sec3–6, Discussion sec9/sec10, Methods sec12–15 and embedded Figure1–4/7 captions. SEY6210-derived strains are explicit. No pixels or Results sec7 are claimed. | supports | Katzmann directly tests Vps27-dependent ESCRT-I endosomal recruitment and membrane-associated interaction, including vps27/vps34 and ESCRT-I perturbations. Its discussion distinguishes Hse1 and expressly notes that Vps27 recruitment/binding and the tested ESCRT-I recruitment need not require Hse1. This supports the existing Vps27-specific edge. |
| micro54-protein-P40343 | https://rest.uniprot.org/uniprotkb/P40343.json; Primary accession/status, recommended name, genes/taxon, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references. | supports | Reviewed P40343 identifies VPS27 in S.cerevisiae S288C taxon559292. SUBUNIT names VPS27/HSE1 ESCRT-0; the maintained endosome-membrane ECO0000269 citations are present. Identity, location, membership and family mapping remain separate assertions. |
| micro54-gene-VPS27-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS27%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual query gene_exact:VPS27, organism_id:559292, reviewed:true; complete returned identity set. | supports | The exact-organism reviewed VPS27 query returns the single P40343 entry. |
| micro54-protein-P38753-network | https://rest.uniprot.org/uniprotkb/P38753.json; Primary accession/status, recommended name, genes/taxon, full FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family cross-references. | supports | Reviewed P38753 identifies HSE1 in S.cerevisiae S288C taxon559292. SUBUNIT names VPS27/HSE1 ESCRT-0; the maintained endosome-membrane ECO0000269 citations are present. Identity, location, membership and family mapping remain separate assertions. |
| micro54-gene-HSE1-network | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHSE1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Actual query gene_exact:HSE1, organism_id:559292, reviewed:true; complete returned identity set. | supports | The exact-organism reviewed HSE1 query returns the single P38753 entry. |
| micro54-ipr-IPR017073 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017073/; Complete native family metadata, description, member signatures and hierarchy. | supports | IPR017073 is a family named Hepatocyte growth factor-regulated tyrosine kinase substrate/VPS27, integrating PTHR46275 and PIRSF036956. Its description explicitly spans Hrs and yeast Vps27; the separate native P40343 entry corroborates membership. This is not merely a VHS/FYVE/UIM domain. |
| micro54-ipr-IPR050670 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050670/; Complete native type/name, PTHR45929 integration, description and LLM/checked flags. | context_only | IPR050670 is named STAM but its unchecked generated prose covers several distinct protein activities. It is not accepted as an exact Hse1/STAM-only class solely from its label. |
| micro54-panther-PTHR45929 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45929/; Complete native family identity, integration and description flags. | context_only | PTHR45929 is the integrated broad STAM family with five subfamilies and unchecked generated text. The source family by itself does not establish a precise Hse1/STAM-only match. |
| micro54-ipr-IPR050670-reviewed | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR050670/?page_size=200; Reviewed-protein endpoint for IPR050670, page_size200; all38 metadata accession/name/gene/taxon identities read, next=null. | context_only | The complete 38-entry reviewed member response contains Hse1/STAM but also SHO1, LSB1, PIN3, csh3, mug137 and SH3D21 proteins. This directly establishes a broader family boundary than the proposed Hse1/STAM class. |
| micro54-panther-PTHR45929-subfamilies | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45929/?extra_fields=subfamilies; Original request/response diagnostic only. | context_only | The attempted extra_fields=subfamilies request returned HTTP404 and establishes no exact subfamily identity. |
| micro54-bilodeau2002-publisher | https://www.nature.com/articles/ncb815; Retained3038-byte challenge HTML and original access receipt. | context_only | The native Nature route returned HTTP200 with a Client Challenge page, not the Bilodeau main body. The complete primary abstract is independently available in the native MED entry. |
| micro54-henne2011-citeseer | https://citeseerx.ist.psu.edu/document?doi=d6f560e1a8e89ec5986bbcb4e2235d99c24bc8f4&amp;repid=rep1&amp;type=pdf; Retained native request and404 response. | context_only | The candidate public PDF URL returned HTTP404 HTML, not the Henne review. No main-body scope is inferred. |
| schema-result | just validate data/structures/other/escrt_0_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/escrt_0_complex.yaml |
| strict-result | just validate-strict data/structures/other/escrt_0_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_0_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/escrt_0_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_0_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_0_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml --causal-graphs; Complete focused native read-only report | supports | data/structures/other/escrt_0_complex.yaml  (GO:0033565)<br>  yeast_escrt_0_mvb_cargo_recognition	vps27_escrt_0_subunit	COVERED	-&gt;vps27_escrt_0_subunit (UniProtKB:P40343)<br>  yeast_escrt_0_mvb_cargo_recognition	hse1_escrt_0_subunit	COVERED	-&gt;hse1_escrt_0_subunit (UniProtKB:P38753)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml --verify; Complete focused native read-only report | context_only | Traceback (most recent call last):<br>  File "/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py", line 922, in &lt;module&gt;<br>    raise SystemExit(main())<br>                     ~~~~^^<br>  File "/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py", line 876, in main<br>    return cmd_verify(records)<br>  File "/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py", line 727, in cmd_verify<br>    issues = verify_records(records)<br>  File "/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py", line 616, in verify_records<br>    entries = fetch_entries_by_accession(all_accs) if all_accs else {}<br>              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^<br>  File "/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py", line 169, in fetch_entries_by_accession<br>    for entry in json.loads(_get(url)).get("results", []):<br>                            ~~~~^^^^^<br>  File "/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py", line 134, in _get<br>    raise RuntimeError(f"UniProt unreachable after {RETRIES} attempts: {last}")<br>RuntimeError: UniProt unreachable after 3 attempts: &lt;urlopen error [Errno 8] nodename nor servname provided, or not known&gt; |
| native-verify-network | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml --verify; Complete focused native read-only report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/escrt_0_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 16 collected target identifiers returned OK. PMID:12006563: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:12055639: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:12900393: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Bilodeau2002, Stahelin2002 and Huh2003 are independently read at complete native abstract tier only. The Nature200 response is a challenge; Huh individual annotations are verified in native UniProt, not raw microscopy.
- Katzmann was read only at the explicitly listed Results/Discussion/Methods/captions; no pixels or unlisted result sections are certified. Henne2011 is secondary complete-abstract evidence only; the candidate PDF route returned404.
- No exact Hse1/STAM-only family is established. IPR050670/PTHR45929 mixed membership and unchecked prose are explicitly excluded as precise replacements; the failed subfamily endpoint supplies no positive identity.
- Original raw bytes, URL, UTC and SHA256 are retained for reused sources. Failed initial DNS fetches are diagnostic receipts, not scientific source bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user requests a review for every unreviewed record, including qualified clean records.
- Native ontology and protein/family databases directly address these claims. No expression-module dataset is established as evidence of physical complex membership.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T063722Z-escrt-0-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of escrt 0 complex
started_at: '2026-10-22T06:16:14Z'
finished_at: '2026-10-22T06:37:22Z'
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
summary: 'Two bounded minors: the visible copied Vps1 definition conflicts with the
  correctly curated Vps27 complex, and exact Vps27/Hrs family grounding is available.
  Hse1 broad-family substitution is withheld; supported protein identities and Vps27-specific
  recruitment are retained.'
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
  - path: data/structures/other/escrt_0_complex.yaml
    sha256: 0ce6528df8bc94b7bb2547b04f8eae797b056cc925a27f04328b6b5f6913666d
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
- target_id: GO:0033565
  path: data/structures/other/escrt_0_complex.yaml
  label: ESCRT-0 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target plus frozen governing/schema/protein/graph
    guidance. Native identity and directly read literature tiers are distinguished;
    no neighboring maintained record is an unstated scientific premise.
  selection: Batch54 strict ordered selection, index 5; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033565
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: just validate data/structures/other/escrt_0_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: just validate-strict data/structures/other/escrt_0_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_0_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific scope independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: failed
  required: false
  target_ids:
  - GO:0033565
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml
    --verify
  exit_code: 1
  summary: Executed sandbox attempt failed because DNS was unavailable; optional historical
    attempt retained, followed by successful network retry.
  evidence_ids:
  - native-verify
- check_id: native-verify-network
  name: Focused native verify network retry
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; scientific scope independently assessed.
  evidence_ids:
  - native-verify-network
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033565
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro54-tax4932
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-tax559292
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
  - micro54-doi-j_devcel_2011_05_015
  - micro54-katzmann2003-pmc
  - micro54-protein-P40343
  - micro54-gene-VPS27-network
  - micro54-protein-P38753-network
  - micro54-gene-HSE1-network
  - micro54-ipr-IPR017073
  - micro54-ipr-IPR050670
  - micro54-panther-PTHR45929
  - micro54-ipr-IPR050670-reviewed
  - micro54-panther-PTHR45929-subfamilies
  - micro54-bilodeau2002-publisher
  - micro54-henne2011-citeseer
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0033565
  summary: '12 of 16 collected target identifiers returned OK. PMID:12006563: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:12055639: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:12900393: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0033565
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0033565
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
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/escrt_0_complex.yaml
  locator: 'Complete current YAML: every scientific field, citation, component/example,
    graph edge, discussion and history'
  accessed_at: '2026-10-22T06:30:22Z'
  support: context_only
  summary: The entire target was read. No neighboring maintained record supplies an
    unstated scientific premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component-class grounding, label-only representation and formation necessity
  accessed_at: '2026-10-22T06:30:22Z'
  support: context_only
  summary: Known named constituents can be recorded with reviewed label-only grounding
    when exact families remain unresolved. Protein examples are not family identities;
    formation necessity is distinct from activity or viability.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum
  accessed_at: '2026-10-22T06:30:22Z'
  support: context_only
  summary: COMMON means present in most taxon members, with exceptional losses; UNKNOWN
    does not claim demonstrated formation necessity. An exact source-neutral class
    is distinct from a species accession or a shared domain.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope, typed nodes and source-specific edges
  accessed_at: '2026-10-22T06:30:22Z'
  support: context_only
  summary: Descriptive composition/function graphs may remain NONMECHANISTIC. Experimental
    system and actor scope must match each edge.
- evidence_id: micro54-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Native taxId/scientificName/rank and lineage fields.
  accessed_at: '2026-10-22T06:20:02.063372Z'
  support: supports
  summary: ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. This identity
    does not establish a quantitative within-species prevalence census.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro54-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621
  locator: Exact target/parent/endosome/function/ESCRT-I entries, definitions, synonyms
    and relevant typed children in the shared response.
  accessed_at: '2026-10-22T06:20:02.063646Z'
  support: supports
  summary: Native GO0033565 retains the Vps1p wording while its exact synonym is Vps27p-Hse1p;
    the discrepancy is recorded rather than silently treated as correct biology. GO0036452
    lists ESCRT-0 as an is_a child and is itself part_of endosome through the typed
    GO0005768 child list. GO0071985 supplies the MVB sorting process; GO0000813 is
    ESCRT-I.
  snapshot_sha256: 563ffa6dea1c58c1c92024214051980b0b5f3eefd7984f1ef56cb02432f9999b
- evidence_id: micro54-GO0033565-ancestors-network
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033565/ancestors?relations=is_a
  locator: Complete relations=is_a ancestors array.
  accessed_at: '2026-10-22T06:23:17.747243Z'
  support: supports
  summary: The is_a-only array confirms ESCRT-complex and protein-containing-complex
    ancestry. Endosome location is corroborated separately, not inferred from this
    array.
  snapshot_sha256: c3f01e5a48d89d949fd4ce84c08c674afb30f56499442c1604ec361e62f72aa7
- evidence_id: micro54-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Native taxId/scientificName/rank/lineage fields.
  accessed_at: '2026-10-22T06:20:02.063749Z'
  support: supports
  summary: ENA taxId559292 is Saccharomyces cerevisiae S288C, rank strain; the maintained
    reference-protein examples use this identity correctly.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro54-pmid-12006563-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12006563+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry, exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:23:16.652653Z'
  support: supports
  summary: 'PMID12006563: Phosphatidylinositol 3-phosphate induces the membrane penetration
    of the FYVE domains of Vps27p and Hrs. Stahelin RV, Long F, Diraviyam K, Bruzik
    KS, Murray D, Cho W. (2002), DOI10.1074/jbc.m201106200. Exact identity and complete
    native abstract read. The abstract describes isolated FYVE-domain membrane-binding
    and monolayer assays, not a whole-cell complex-formation test.'
  snapshot_sha256: f55bb5e09c597f33111d607242e427996b65bd6dbcb559ad5722f790b2edcacb
- evidence_id: micro54-pmid-12055639-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12055639+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry, exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:23:16.660199Z'
  support: supports
  summary: 'PMID12055639: The Vps27p Hse1p complex binds ubiquitin and mediates endosomal
    protein sorting. Bilodeau PS, Urbanowski JL, Winistorfer SC, Piper RC. (2002),
    DOI10.1038/ncb815. Exact identity and complete native abstract read. It explicitly
    identifies Vps27p/Hse1p, endosomal localization and Ub binding; UIM mutants impair
    cargo sorting while lumenal membrane generation continues.'
  snapshot_sha256: 40f43c93fba3bc8c5872e05ebc8a7cba2c32ec105655e7a996a79d1a7c9fc0ed
- evidence_id: micro54-pmid-12900393-network
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12900393+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry, exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:23:16.680359Z'
  support: supports
  summary: 'PMID12900393: Vps27 recruits ESCRT machinery to endosomes during MVB sorting.
    Katzmann DJ, Stefan CJ, Babst M, Emr SD. (2003), DOI10.1083/jcb.200302136. Exact
    identity and complete native abstract read.'
  snapshot_sha256: 5cc0e811f69df85e927ce076d533a0231372784d4411c5154773f4801ee9cf95
- evidence_id: micro54-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry, exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:20:08.791688Z'
  support: supports
  summary: 'PMID14562095: Global analysis of protein localization in budding yeast.
    Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK. (2003),
    DOI10.1038/nature02026. Exact identity and complete native abstract read. The
    abstract describes a tagged-yeast localization survey; individual protein annotation
    evidence is checked in the native UniProt entries, not inferred from the abstract.'
  snapshot_sha256: 571f7249c52d66a3b53ae05fa04cfe3012ab729c63308d338c745e9f3c1daa72
- evidence_id: micro54-doi-j_devcel_2011_05_015
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2011.05.015%22&format=json&resultType=core
  locator: Unique MED entry and complete abstractText; no review main-body claim.
  accessed_at: '2026-10-22T06:20:10.119810Z'
  support: supports
  summary: Henne/Buchkovich/Emr2011, The ESCRT pathway, DOI10.1016/j.devcel.2011.05.015
    PMID21763610, is a secondary review. Its complete native abstract supports the
    cargo-recognition/membrane-sculpting framework and MVB, viral budding and abscission
    roles; detailed subunit prose is not certified from this abstract alone.
  snapshot_sha256: c1eb20e3ee3b89412437434900f82d42282d787ea5e51ef2d765091fa59227b0
- evidence_id: micro54-katzmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/
  locator: 'Genuine primary HTML: sec3–6, Discussion sec9/sec10, Methods sec12–15
    and embedded Figure1–4/7 captions. SEY6210-derived strains are explicit. No pixels
    or Results sec7 are claimed.'
  accessed_at: '2026-10-22T01:12:25.464014Z'
  support: supports
  summary: Katzmann directly tests Vps27-dependent ESCRT-I endosomal recruitment and
    membrane-associated interaction, including vps27/vps34 and ESCRT-I perturbations.
    Its discussion distinguishes Hse1 and expressly notes that Vps27 recruitment/binding
    and the tested ESCRT-I recruitment need not require Hse1. This supports the existing
    Vps27-specific edge.
  snapshot_sha256: d4bc3fc8fd5cbf98c1b88722373dbd34c271f2df8da4bbb78d4f808dc7197233
- evidence_id: micro54-protein-P40343
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40343.json
  locator: Primary accession/status, recommended name, genes/taxon, full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references.
  accessed_at: '2026-10-22T06:20:02.992613Z'
  support: supports
  summary: Reviewed P40343 identifies VPS27 in S.cerevisiae S288C taxon559292. SUBUNIT
    names VPS27/HSE1 ESCRT-0; the maintained endosome-membrane ECO0000269 citations
    are present. Identity, location, membership and family mapping remain separate
    assertions.
  snapshot_sha256: 9722b86a9641dd5d053f0babc34f530ea7656e19571069c2eb081537e836c344
- evidence_id: micro54-gene-VPS27-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS27%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual query gene_exact:VPS27, organism_id:559292, reviewed:true; complete
    returned identity set.
  accessed_at: '2026-10-22T06:23:17.278942Z'
  support: supports
  summary: The exact-organism reviewed VPS27 query returns the single P40343 entry.
  snapshot_sha256: f10595f20fb986f3ccc9d43fbbf528da993ebe082fa89523582413ba156507f3
- evidence_id: micro54-protein-P38753-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38753.json
  locator: Primary accession/status, recommended name, genes/taxon, full FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family cross-references.
  accessed_at: '2026-10-22T06:23:16.929293Z'
  support: supports
  summary: Reviewed P38753 identifies HSE1 in S.cerevisiae S288C taxon559292. SUBUNIT
    names VPS27/HSE1 ESCRT-0; the maintained endosome-membrane ECO0000269 citations
    are present. Identity, location, membership and family mapping remain separate
    assertions.
  snapshot_sha256: 1f241d071d6810f0ea8db2fc2c85bf81395fe6b26fc4478f857d489959df64df
- evidence_id: micro54-gene-HSE1-network
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHSE1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Actual query gene_exact:HSE1, organism_id:559292, reviewed:true; complete
    returned identity set.
  accessed_at: '2026-10-22T06:23:17.424271Z'
  support: supports
  summary: The exact-organism reviewed HSE1 query returns the single P38753 entry.
  snapshot_sha256: ca4f65f91959cfcb0c0c1d6967f5920310daf04d297b98e47dd1fd739f33f8a8
- evidence_id: micro54-ipr-IPR017073
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017073/
  locator: Complete native family metadata, description, member signatures and hierarchy.
  accessed_at: '2026-10-22T06:23:59.007368Z'
  support: supports
  summary: IPR017073 is a family named Hepatocyte growth factor-regulated tyrosine
    kinase substrate/VPS27, integrating PTHR46275 and PIRSF036956. Its description
    explicitly spans Hrs and yeast Vps27; the separate native P40343 entry corroborates
    membership. This is not merely a VHS/FYVE/UIM domain.
  snapshot_sha256: 8e903eb9fb7c4c985f359ae9bf3a22fb5ff31bc932b898e9f77e68cbcaf23f05
- evidence_id: micro54-ipr-IPR050670
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050670/
  locator: Complete native type/name, PTHR45929 integration, description and LLM/checked
    flags.
  accessed_at: '2026-10-22T06:23:59.206821Z'
  support: context_only
  summary: IPR050670 is named STAM but its unchecked generated prose covers several
    distinct protein activities. It is not accepted as an exact Hse1/STAM-only class
    solely from its label.
  snapshot_sha256: 65084d8e26b85f7e864b9f77d99a0742b7b6a3f3de014b6a1d9472081fa4ab47
- evidence_id: micro54-panther-PTHR45929
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45929/
  locator: Complete native family identity, integration and description flags.
  accessed_at: '2026-10-22T06:23:59.570833Z'
  support: context_only
  summary: PTHR45929 is the integrated broad STAM family with five subfamilies and
    unchecked generated text. The source family by itself does not establish a precise
    Hse1/STAM-only match.
  snapshot_sha256: 18df9f78e94f3b6f49a8a05e5c4f8f75b864b76e262e038520e77d309fdb8d11
- evidence_id: micro54-ipr-IPR050670-reviewed
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR050670/?page_size=200
  locator: Reviewed-protein endpoint for IPR050670, page_size200; all38 metadata accession/name/gene/taxon
    identities read, next=null.
  accessed_at: '2026-10-22T06:24:25.663338Z'
  support: context_only
  summary: The complete 38-entry reviewed member response contains Hse1/STAM but also
    SHO1, LSB1, PIN3, csh3, mug137 and SH3D21 proteins. This directly establishes
    a broader family boundary than the proposed Hse1/STAM class.
  snapshot_sha256: 403af0a94db6054becb0842d813a37911fea6dfc551d0b6b7d45c86bdd078547
- evidence_id: micro54-panther-PTHR45929-subfamilies
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR45929/?extra_fields=subfamilies
  locator: Original request/response diagnostic only.
  accessed_at: '2026-10-22T06:24:25.663635Z'
  support: context_only
  summary: The attempted extra_fields=subfamilies request returned HTTP404 and establishes
    no exact subfamily identity.
  snapshot_sha256: aab5b774f3b6987ec232409161bc212533cc4383f53a47babfbc4dc3aaaf729c
- evidence_id: micro54-bilodeau2002-publisher
  kind: authority
  reference: https://www.nature.com/articles/ncb815
  locator: Retained3038-byte challenge HTML and original access receipt.
  accessed_at: '2026-10-22T06:23:59.007405Z'
  support: context_only
  summary: The native Nature route returned HTTP200 with a Client Challenge page,
    not the Bilodeau main body. The complete primary abstract is independently available
    in the native MED entry.
  snapshot_sha256: 32ed63159c77e21ee19ca1b9aa3213ccf0218eb59539560b132a8e68ef0e18ea
- evidence_id: micro54-henne2011-citeseer
  kind: authority
  reference: https://citeseerx.ist.psu.edu/document?doi=d6f560e1a8e89ec5986bbcb4e2235d99c24bc8f4&repid=rep1&type=pdf
  locator: Retained native request and404 response.
  accessed_at: '2026-10-22T06:27:03.280566Z'
  support: context_only
  summary: The candidate public PDF URL returned HTTP404 HTML, not the Henne review.
    No main-body scope is inferred.
  snapshot_sha256: 687dd819f7af05e60aee60b6885521ddf2373a3eebf141975e936763a929a0bd
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/escrt_0_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:15Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/escrt_0_complex.yaml'
  snapshot_sha256: cc1d3ba3a70a14d4cea5d044be6290ae0cd644645c7491578f94eae23c08c493
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/escrt_0_complex.yaml --out
    /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_0_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:16Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/escrt_0_complex.yaml\
    \ --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_0_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_0_complex-strict.tsv"
  snapshot_sha256: e8727373d0ea6f8f72d242ecd307bf2e972e11d238e11862b33617dcbde3fb7b
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml
    --causal-graphs
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:23:19.837728Z'
  support: supports
  summary: "data/structures/other/escrt_0_complex.yaml  (GO:0033565)\n  yeast_escrt_0_mvb_cargo_recognition\t\
    vps27_escrt_0_subunit\tCOVERED\t->vps27_escrt_0_subunit (UniProtKB:P40343)\n \
    \ yeast_escrt_0_mvb_cargo_recognition\thse1_escrt_0_subunit\tCOVERED\t->hse1_escrt_0_subunit\
    \ (UniProtKB:P38753)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 8d965b4762c6f13e759cf9a9f2c993dde6bd0f8922fe5998302d843e0f3efa5e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml
    --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:23:32.355308Z'
  support: context_only
  summary: "Traceback (most recent call last):\n  File \"/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py\"\
    , line 922, in <module>\n    raise SystemExit(main())\n                     ~~~~^^\n\
    \  File \"/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py\"\
    , line 876, in main\n    return cmd_verify(records)\n  File \"/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py\"\
    , line 727, in cmd_verify\n    issues = verify_records(records)\n  File \"/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py\"\
    , line 616, in verify_records\n    entries = fetch_entries_by_accession(all_accs)\
    \ if all_accs else {}\n              ~~~~~~~~~~~~~~~~~~~~~~~~~~^^^^^^^^^^\n  File\
    \ \"/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py\"\
    , line 169, in fetch_entries_by_accession\n    for entry in json.loads(_get(url)).get(\"\
    results\", []):\n                            ~~~~^^^^^\n  File \"/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/scripts/uniprot_genes.py\"\
    , line 134, in _get\n    raise RuntimeError(f\"UniProt unreachable after {RETRIES}\
    \ attempts: {last}\")\nRuntimeError: UniProt unreachable after 3 attempts: <urlopen\
    \ error [Errno 8] nodename nor servname provided, or not known>"
  snapshot_sha256: d35e957c24825a4e0ecab1204683c0ce7801d8e0176311b0ee53c0998f393f0c
- evidence_id: native-verify-network
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_0_complex.yaml
    --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:23:56.327122Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/escrt_0_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '12 of 16 collected target identifiers returned OK. PMID:12006563: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:12055639: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:12900393: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE;
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
  topic: Correct ESCRT-0 identity with a localized copied-definition conflict
  outcome: concern
  target_ids:
  - GO:0033565
  summary: GO identity, synonyms, parent and endosomal boundary identify ESCRT-0 correctly.
    The copied definition still names Vps1p even though the record explicitly resolves
    this discrepancy and represents Vps27/Hse1 elsewhere; the current definition requires
    a narrow correction with transparent source attribution.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
  - micro54-protein-P40343
  - micro54-gene-VPS27-network
  - micro54-protein-P38753-network
  - micro54-gene-HSE1-network
- assessment_id: composition
  area: grounding
  topic: Two supported constituents and one exact family gap
  outcome: concern
  target_ids:
  - GO:0033565
  summary: Bilodeau complete abstract and native SUBUNIT comments support Vps27/Hse1.
    IPR017073 exactly addresses the Vps27/Hrs boundary and can resolve that existing
    class. The independently checked mixed IPR050670/PTHR45929 membership justifies
    withholding the broader candidate from Hse1; its family label is insufficient.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-protein-P40343
  - micro54-gene-VPS27-network
  - micro54-protein-P38753-network
  - micro54-gene-HSE1-network
  - micro54-ipr-IPR017073
  - micro54-ipr-IPR050670
  - micro54-panther-PTHR45929
  - micro54-ipr-IPR050670-reviewed
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
- assessment_id: function
  area: evidence
  topic: Ub-dependent sorting and Vps27-specific recruitment
  outcome: supported
  target_ids:
  - GO:0033565
  summary: The primary abstract supports complex Ub binding/endosomal sorting. Katzmann
    directly supports Vps27-specific ESCRT-I recruitment and interaction at endosomal
    membranes. The corrected edge does not require the whole Hse1-containing complex
    for every measured recruitment result.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-katzmann2003-pmc
  - micro54-doi-j_devcel_2011_05_015
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
- assessment_id: scope
  area: scope
  topic: Yeast and mammalian naming boundaries
  outcome: supported
  target_ids:
  - GO:0033565
  summary: The S.cerevisiae example and S288C reference accessions are valid, while
    Katzmann uses explicitly listed SEY6210 derivatives. COMMON retains the schema
    majority-occurrence meaning with exceptional losses; these experiments are qualitative
    support, not a measured census. The mammalian Hrs/STAM synonym does not export
    every yeast perturbation to mammals.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-protein-P40343
  - micro54-gene-VPS27-network
  - micro54-protein-P38753-network
  - micro54-gene-HSE1-network
  - micro54-katzmann2003-pmc
  - micro54-doi-j_devcel_2011_05_015
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
- assessment_id: examples
  area: grounding
  topic: Protein identities and annotation provenance
  outcome: supported
  target_ids:
  - GO:0033565
  summary: Both exact-organism reviewed queries are single hits matching the existing
    examples. The five listed PMID occurrences and ECO location assertions match native
    comments; isolated-domain or survey localization evidence is not promoted to physical
    complex formation.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-protein-P40343
  - micro54-gene-VPS27-network
  - micro54-protein-P38753-network
  - micro54-gene-HSE1-network
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
- assessment_id: graph
  area: graph
  topic: Five bounded descriptive edges
  outcome: supported
  target_ids:
  - GO:0033565
  summary: NONMECHANISTIC scope fits the two membership edges, Ub binding, Vps27-specific
    recruitment and MVB participation. Typed node/component references are correct.
    The graph avoids an untested full ESCRT handoff or Hse1-dependent recruitment
    mechanism.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - graphs
  - micro54-katzmann2003-pmc
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
- assessment_id: formation
  area: evidence
  topic: Both constituent necessity labels remain unknown
  outcome: unknown
  target_ids:
  - GO:0033565
  summary: The existing UNKNOWN labels do not conflate sorting defects, location,
    Ub binding or lumenal-vesicle production with formation of ESCRT-0 itself. No
    universal per-subunit formation requirement is established by the inspected abstract/primary
    sections.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-katzmann2003-pmc
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
- assessment_id: coverage
  area: completeness
  topic: Whole target with bounded source and unresolved scope
  outcome: supported
  target_ids:
  - GO:0033565
  summary: All current scientific fields, source placements, graph edges, discussions
    and history were reviewed. Historical first-pass wording is not treated as false
    merely because present access differs. The stated findings isolate concrete current
    changes; optional unverified detail remains a limitation.
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-protein-P40343
  - micro54-gene-VPS27-network
  - micro54-protein-P38753-network
  - micro54-gene-HSE1-network
  - micro54-katzmann2003-pmc
  - micro54-doi-j_devcel_2011_05_015
  - micro54-ipr-IPR017073
  - micro54-ipr-IPR050670
  - micro54-panther-PTHR45929
  - micro54-ipr-IPR050670-reviewed
  - micro54-pmid-12006563-network
  - micro54-pmid-12055639-network
  - micro54-pmid-12900393-network
  - micro54-pmid-14562095
findings:
- finding_id: F1
  issue_key: escrt-0-copied-vps1-definition-conflict
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Reconcile the copied Vps1 definition with the curated Vps27 complex
  description: The definition says Vps1p and Hse1p, faithfully reproducing the current
    GO text, while the exact synonym, Bilodeau abstract, native subunit identities
    and the record's resolved discussion identify Vps27p/Hse1p. The resolved discussion
    protects the component table but leaves the misleading definition visible.
  target_ids:
  - GO:0033565
  field_paths:
  - definition
  - definition_source
  - discussions[1]
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-protein-P40343
  - micro54-gene-VPS27-network
  - micro54-protein-P38753-network
  - micro54-gene-HSE1-network
  - micro54-pmid-12055639-network
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
  rule_id: Exact source support and component representation
  native_severity: minor
  normalization_reason: This is a localized wording/source conflict in an otherwise
    correctly identified and explicitly discussed complex. The component table, examples
    and graph already use Vps27, so it does not make the whole record denote a different
    complex.
- finding_id: F2
  issue_key: escrt-0-vps27-hrs-exact-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the verified Vps27/Hrs family grounding
  description: The current Vps27 row is REVIEWED_LABEL_ONLY with an open exact-family
    task. Native IPR017073 explicitly covers Hrs/Vps27 and native P40343 corroborates
    membership. In contrast, the independently inspected Hse1 candidate is broader
    and is not part of this correction.
  target_ids:
  - GO:0033565
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - schema
  - micro54-tax4932
  - micro54-tax559292
  - micro54-go
  - micro54-GO0033565-ancestors-network
  - micro54-protein-P40343
  - micro54-gene-VPS27-network
  - micro54-protein-P38753-network
  - micro54-gene-HSE1-network
  - micro54-ipr-IPR017073
  - micro54-ipr-IPR050670
  - micro54-ipr-IPR050670-reviewed
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
  rule_id: Exact source support and component representation
  native_severity: minor
  normalization_reason: The named subunit and protein example are correct. This is
    a bounded actionable class-grounding gap under the existing explicit task, not
    missing optional inventory or a mandate to force every candidate.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0033565
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
  description: Correct the local definition to Vps27p with an appropriate primary-source
    attribution or explicit qualifier documenting the native GO discrepancy. Preserve
    GO0033565 identity, correct component rows and historical evidence rather than
    silently rewriting the external source.
  acceptance_checks:
  - The visible definition no longer presents Vps1 as the curated ESCRT-0 constituent.
  - The source relationship and known GO discrepancy remain explicit.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0033565
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_0_complex.yaml
    role: maintained scientific record
  description: Add InterPro:IPR017073 to the existing Vps27 class with exact source
    evidence and update its grounding state/task. Keep P40343 as the taxon-paired
    example and retain Hse1 label-only unless a genuinely exact class is separately
    verified.
  acceptance_checks:
  - The new grounding denotes the Hrs/Vps27 whole-protein family, not its domains.
  - The mixed Hse1 candidate is not adopted as an exact substitute.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Bilodeau2002, Stahelin2002 and Huh2003 are independently read at complete native
  abstract tier only. The Nature200 response is a challenge; Huh individual annotations
  are verified in native UniProt, not raw microscopy.
- Katzmann was read only at the explicitly listed Results/Discussion/Methods/captions;
  no pixels or unlisted result sections are certified. Henne2011 is secondary complete-abstract
  evidence only; the candidate PDF route returned404.
- No exact Hse1/STAM-only family is established. IPR050670/PTHR45929 mixed membership
  and unchecked prose are explicitly excluded as precise replacements; the failed
  subfamily endpoint supplies no positive identity.
- Original raw bytes, URL, UTC and SHA256 are retained for reused sources. Failed
  initial DNS fetches are diagnostic receipts, not scientific source bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user requests a review for every unreviewed record, including qualified clean
  records.
- Native ontology and protein/family databases directly address these claims. No expression-module
  dataset is established as evidence of physical complex membership.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
