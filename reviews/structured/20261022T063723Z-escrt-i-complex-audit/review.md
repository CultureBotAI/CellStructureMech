# Escrt i complex scientific review

- Review: 20261022T063723Z-escrt-i-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:16:18Z
- Finished UTC: 2026-10-22T06:37:23Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ESCRT-I identity, original yeast core, protein examples and recruitment/sorting graph are supported. One grouped minor resolves exact Vps23, Vps28 and fungal Vps37 family grounding; later Mvb12 membership remains explicitly acknowledged.

## Scope And Provenance

Exactly one whole maintained target plus frozen guidance and protein-example skill. Source-specific actual read extents are enumerated per evidence row; no maintained neighboring record supplies scientific evidence.

Selection: Target 7 of batch54, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000813 | data/structures/other/escrt_i_complex.yaml | maintained | ESCRT I complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000813 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000813 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0000813 | Native focused check passed; scientific claims assessed separately. |
| Native verify | passed | True | GO:0000813 | Native focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0000813 | No expression-module inference is used for these structure and pathway claims. |
| Claim-level scientific review | passed | True | GO:0000813 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0000813 | 14 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:9790597: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0000813 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000813 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000813 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000813 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0000813 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact ESCRT-I identity and historically bounded core

identity: supported. Targets: GO:0000813.

Identity, hierarchy/parthood, broad synonym and original yeast canonical example are supported. The three listed proteins are valid members. The record explicitly acknowledges Mvb12 as a later member and does not state that its list is exhaustive.

### Available exact subunit families

grounding: concern. Targets: GO:0000813.

Vps23/TSG101 IPR052070, Vps28 IPR007143 and the explicitly fungal Vps37 IPR017435 resolve the named yeast class mappings. Gene aliases STP22/VPS23 and SRN2/VPS37 are correctly disambiguated. The Vps37 domain and unchecked family narrative are not substitutes for class evidence.

### Yeast historical core and later component evidence

scope: supported. Targets: GO:0000813.

The species and reference-strain identities are correct; the early Katzmann yeast model and SEY6210-derived2003 preparations are distinct from accession reference metadata. Later Mvb12 evidence is acknowledged as a known incomplete inventory boundary, not denied.

### External recruitment and ubiquitinated cargo sorting

graph: supported. Targets: GO:0000813.

The NONMECHANISTIC graph accurately distinguishes core membership from Vps27-mediated recruitment and coarse MVB-sorting output. Direct Vps27/ESCRT-I membrane association supports recruitment without making Vps27 a stable core subunit.

### Unresolved individual formation requirements

grounding: unknown. Targets: GO:0000813.

Sorting loss, localization defects and partial subcomplexes are not generalized to universal individual formation necessity. Curtiss specifically examines Mvb12 stability/association and remaining subcomplexes; the present review does not convert those selected experiments into an all-subunit requirement table.

### Complete maintained target with bounded source inspection

completeness: supported. Targets: GO:0000813.

All maintained fields, evidence notes, graph statements and discussions were checked at the declared source extents. Optional inventories, exact stoichiometry and unresolved formation experiments are not fabricated from validation success.

## Findings

### F1: Resolve the three verified yeast ESCRT-I families

minor / open / confirmed; issue key: escrt-i-exact-families.

The current label-only notes defer exact source-neutral family review. Native type/signature/member evidence now resolves the Vps23/TSG101 and Vps28 classes and the explicitly fungal Vps37 class without relying on a UEV/Modr domain.

## Recommended Actions And Acceptance Checks

### A1

Use IPR052070 for Vps23, IPR007143 for Vps28 and IPR017435 for the explicitly yeast/fungal Vps37 constituent; align current grounding notes/TODO while preserving Mvb12 follow-up.

- Keep Vps37 fungal scope explicit rather than claiming one family covers all metazoan paralogs.
- Retain correct gene aliases and the separate Mvb12 inventory discussion.
- Preserve supported identities and biological scope; pass applicable native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/escrt_i_complex.yaml; Entire maintained record including all history, discussions, evidence, components, examples and causal graph | context_only | The entire target was read; dated curation history is not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, essentiality, taxonomic presence and graph scope | context_only | Essentiality concerns formation, not function or viability. COMMON means present in most members, losses the exception; qualitative synthesis does not imply a measured prevalence census. |
| curation | docs/CURATION.md; Component grounding and REVIEWED_LABEL_ONLY contract, including159–160 | context_only | Exact full-protein families are distinct from shared domains or paralog supergroups. A reviewed label-only status is not merely a placeholder for an exact mapping that was not curated this pass. |
| escrt54-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621; Complete target-relevant definitions/synonym scopes and typed child relationships within combined response; unrelated terms not attributed to this record | supports | GO0000813 identifies ESCRT-I with the broad endosomal-sorting synonym; GO0036452 lists its is_a relationship, GO0010008 its part_of relationship, and GO0071985 the MVB sorting process. |
| escrt54-agent-GO0000813-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only ancestor closure independently contains the ESCRT complex and protein-containing-complex classes. It is not a part_of query. |
| escrt54-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA taxonomy response | supports | Taxon4932 is Saccharomyces cerevisiae, rankspecies; its native names and lineage identify this exact node. |
| escrt54-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete ENA taxonomy response | supports | Taxon559292 is Saccharomyces cerevisiae S288C, rankstrain; its native names and lineage identify this exact node. |
| escrt54-agent-protein-P25604 | https://rest.uniprot.org/uniprotkb/P25604.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed P25604: Suppressor protein STP22 of temperature-sensitive alpha-factor receptor and arginine permease; primary genes STP22, synonyms VPS23, taxon559292. Native comments retain their own experimental/inferred evidence scope. The protein response separately supplies its family xrefs; a family-entry response is not treated as this protein-membership proof. |
| escrt54-agent-protein-P40343 | https://rest.uniprot.org/uniprotkb/P40343.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed P40343: Vacuolar protein sorting-associated protein 27; primary genes VPS27, synonyms DID7, GRD11, SSV17, VPL23, VPT27, taxon559292. Native comments retain their own experimental/inferred evidence scope. The protein response separately supplies its family xrefs; a family-entry response is not treated as this protein-membership proof. |
| escrt54-agent-protein-Q02767 | https://rest.uniprot.org/uniprotkb/Q02767.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed Q02767: Vacuolar protein sorting-associated protein 28; primary genes VPS28, synonyms VPT28, taxon559292. Native comments retain their own experimental/inferred evidence scope. The protein response separately supplies its family xrefs; a family-entry response is not treated as this protein-membership proof. |
| escrt54-agent-protein-Q99176 | https://rest.uniprot.org/uniprotkb/Q99176.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed Q99176: Protein SRN2; primary genes SRN2, synonyms SRN10, VPS37, taxon559292. Native comments retain their own experimental/inferred evidence scope. The protein response separately supplies its family xrefs; a family-entry response is not treated as this protein-membership proof. |
| escrt54-agent-gene-VPS23-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS23%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: P25604. Returned gene tokens/aliases identify the maintained protein without confusing its primary name with the queried synonym. |
| escrt54-agent-gene-VPS28-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS28%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: Q02767. Returned gene tokens/aliases identify the maintained protein without confusing its primary name with the queried synonym. |
| escrt54-agent-gene-VPS37-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS37%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: Q99176. Returned gene tokens/aliases identify the maintained protein without confusing its primary name with the queried synonym. |
| escrt54-agent-pmid-11511343 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11511343+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED identity and abstract | supports | MED11511343: Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I. Katzmann DJ, Babst M, Emr SD. (2001), DOI10.1016/s0092-8674(01)00434-2. Exact metadata and complete abstract read; this is not full-body attestation. |
| escrt54-agent-pmid-9790597 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9790597+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED identity and abstract | supports | MED9790597: Isolation of an extragenic suppressor of the rna1-1 mutation in Saccharomyces cerevisiae. Hong SJ, Yi YS, Koh SS, Park OK, Kang HS. (1998), DOI10.1007/s004380050830. Exact metadata and complete abstract read; this is not full-body attestation. |
| escrt54-agent-doi-j_devcel_2011_05_015 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2011.05.015%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: The ESCRT pathway. Henne WM, Buchkovich NJ, Emr SD. (2011), PMID21763610. Complete native abstract read. This is a secondary review, not a new primary experiment. |
| escrt54-agent-doi-jcb_200302136 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200302136%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: Vps27 recruits ESCRT machinery to endosomes during MVB sorting. Katzmann DJ, Stefan CJ, Babst M, Emr SD. (2003), PMID12900393. Complete native abstract read. Independent full-body evidence, where read, is listed separately. |
| escrt54-agent-doi-jcb_200608053 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200608053%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: New component of ESCRT-I regulates endosomal sorting complex assembly. Chu T, Sun J, Saksena S, Emr SD. (2006), PMID17145965. Complete native abstract read. Independent full-body evidence, where read, is listed separately. |
| escrt54-agent-doi-mbc_e06-07-0588 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e06-07-0588%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: Efficient cargo sorting by ESCRT-I and the subsequent release of ESCRT-I from multivesicular bodies requires the subunit Mvb12. Curtiss M, Jones C, Babst M. (2007), PMID17135292. Complete native abstract read. Independent full-body evidence, where read, is listed separately. |
| escrt54-agent-katzmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/; Results sec3/5/6/7, including Fig1/3–6 captions; Methods sec12–15. No claim of independently reading sec4 or whole Discussion. | supports | Katzmann2003 directly tests independent ubiquitin binding, Vps27-dependent ESCRT-I endosomal localization and membrane-associated copurification. Vps27 UIM/VHS mutations do not abolish the association; C-terminal defects impair recruitment and sorting. SEY6210 and derivatives are the yeast systems. This supports an external recruiter rather than a stable core constituent. |
| escrt54-agent-primary-PMC2064680 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2064680/; Results sec3, Fig1/2 captions; Methods sec9. Other oligomer-model Results and Discussion not independently used. | supports | Chu2006 gel filtration and co-IP identify Mvb12 as an additional ESCRT-I member; its deletion gives partial cargo-sorting defects, unlike strong core mutants. The named SEY6210-derived strains are specified. |
| escrt54-agent-primary-PMC1783790 | https://pmc.ncbi.nlm.nih.gov/articles/PMC1783790/; Results sec10/11 and embedded Fig2/3/4/7 captions. Separate Table1/Methods not independently read. | supports | Curtiss2007 independently demonstrates Mvb12 association with ESCRT-I by reciprocal purification and gel filtration; deletion of VPS37 leaves a Vps23/Vps28 subcomplex, while Mvb12 becomes unstable and fails to associate. These observations support the recorded later-subunit follow-up and do not turn apparent gel-filtration mass into exact stoichiometry. |
| escrt54-agent-ipr-IPR052070 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052070/; Native name/type, complete descriptions and curation flags, member signatures and hierarchy; exact protein membership independently evidenced | supports | IPR052070 is typed as a protein family with PTHR23306, despite its UEV-domain-containing label. Its narrative is LLM-generated and unchecked, so no new mechanism rests on that prose. A separate reviewed-member query and the native protein join establish the Vps23/TSG101 class. |
| escrt54-agent-ipr-IPR007143 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007143/; Native name/type, complete descriptions and curation flags, member signatures and hierarchy; exact protein membership independently evidenced | supports | IPR007143 is the complete Vps28 family with PTHR12937/PIRSF017535/PF03997 signatures; its older complex-composition prose is not used to exclude Mvb12. |
| escrt54-agent-ipr-IPR017435 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017435/; Native name/type, complete descriptions and curation flags, member signatures and hierarchy; exact protein membership independently evidenced | supports | IPR017435 identifies fungal Vps37 with PIRSF038214. Its scope matches the explicitly yeast Vps37 row; it must not be advertised as the complete metazoan paralog universe. Its internally inconsistent heterotrimer/four-name prose is not adopted as stoichiometric evidence. |
| escrt54-agent-ipr-IPR009851 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009851/; Native name/type, complete descriptions and curation flags, member signatures and hierarchy; exact protein membership independently evidenced | supports | IPR009851 is a Modr/Vps37 C-terminal domain, not the whole Vps37 family. It is not selected as the constituent identity. |
| escrt54-agent-family-members-IPR052070 | https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR052070%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id&amp;size=500; Complete seven accession/name/aliases/taxon results | supports | All seven returned reviewed proteins are TSG101/Vps23 homolog identities, including human Q99816, yeast P25604, mouse Q61187, rat Q6IRE4, Arabidopsis Q9LHG8/Q9FFY6 and Dictyostelium Q54LJ3. This corroborates the full-class meaning independently of the unchecked family prose. |
| schema-result | just validate data/structures/other/escrt_i_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/escrt_i_complex.yaml |
| strict-result | just validate-strict data/structures/other/escrt_i_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_i_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/escrt_i_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_i_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_i_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_i_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/escrt_i_complex.yaml  (GO:0000813)<br>  yeast_escrt_i_mvb_cargo_sorting	vps23_escrt_i_subunit	COVERED	-&gt;vps23_escrt_i_subunit (UniProtKB:P25604)<br>  yeast_escrt_i_mvb_cargo_sorting	vps28_escrt_i_subunit	COVERED	-&gt;vps28_escrt_i_subunit (UniProtKB:Q02767)<br>  yeast_escrt_i_mvb_cargo_sorting	vps37_escrt_i_subunit	COVERED	-&gt;vps37_escrt_i_subunit (UniProtKB:Q99176)<br>  yeast_escrt_i_mvb_cargo_sorting	vps27_endosomal_recruiter	UNANCHORED_WITH_UNIPROT	Vps27 endosomal ESCRT-I recruiter (UniProtKB:P40343)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_i_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/escrt_i_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:9790597: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates await guarded parent manifest/hash integration.
- No source figure pixels, supplemental experiments or atomic coordinates were independently analyzed. Embedded captions are text evidence only.
- Reference proteins at S288C559292 do not identify every experimental yeast strain. COMMON keeps its majority-occurrence/losses-exception meaning; qualitative source synthesis supports it without measuring population prevalence.
- Katzmann2001 and Hong1998 were read at complete native abstract scope. Henne2011 was read as review abstract only; retained publisher requests for Katzmann2001/Henne2011 returned403.
- Mvb12 is positively supported by later primary studies and native protein annotations; its absent optional row is an acknowledged incomplete inventory rather than an assertion of absence. Exact Mvb12 family/stoichiometry expansion is not performed here.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T063723Z-escrt-i-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Escrt i complex scientific review
started_at: '2026-10-22T06:16:18Z'
finished_at: '2026-10-22T06:37:23Z'
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
summary: ESCRT-I identity, original yeast core, protein examples and recruitment/sorting
  graph are supported. One grouped minor resolves exact Vps23, Vps28 and fungal Vps37
  family grounding; later Mvb12 membership remains explicitly acknowledged.
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
  - path: data/structures/other/escrt_i_complex.yaml
    sha256: 6a62d3c1153274b4912ddbcae5322b2eeecbca045005db9a88c81babbfb406dc
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
- target_id: GO:0000813
  path: data/structures/other/escrt_i_complex.yaml
  label: ESCRT I complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_i_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one whole maintained target plus frozen guidance and protein-example
    skill. Source-specific actual read extents are enumerated per evidence row; no
    maintained neighboring record supplies scientific evidence.
  selection: Target 7 of batch54, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000813
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000813
  command: just validate data/structures/other/escrt_i_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000813
  command: just validate-strict data/structures/other/escrt_i_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_i_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0000813
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_i_complex.yaml
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
  - GO:0000813
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_i_complex.yaml
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
  - GO:0000813
  summary: No expression-module inference is used for these structure and pathway
    claims.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000813
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - escrt54-agent-go
  - escrt54-agent-GO0000813-ancestors
  - escrt54-agent-tax4932
  - escrt54-agent-tax559292
  - escrt54-agent-protein-P25604
  - escrt54-agent-protein-P40343
  - escrt54-agent-protein-Q02767
  - escrt54-agent-protein-Q99176
  - escrt54-agent-gene-VPS23-559292
  - escrt54-agent-gene-VPS28-559292
  - escrt54-agent-gene-VPS37-559292
  - escrt54-agent-pmid-11511343
  - escrt54-agent-pmid-9790597
  - escrt54-agent-doi-j_devcel_2011_05_015
  - escrt54-agent-doi-jcb_200302136
  - escrt54-agent-doi-jcb_200608053
  - escrt54-agent-doi-mbc_e06-07-0588
  - escrt54-agent-katzmann2003-pmc
  - escrt54-agent-primary-PMC2064680
  - escrt54-agent-primary-PMC1783790
  - escrt54-agent-ipr-IPR052070
  - escrt54-agent-ipr-IPR007143
  - escrt54-agent-ipr-IPR017435
  - escrt54-agent-ipr-IPR009851
  - escrt54-agent-family-members-IPR052070
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0000813
  summary: '14 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:9790597: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - escrt54-agent-pmid-11511343
  - escrt54-agent-pmid-9790597
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000813
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
  - GO:0000813
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
  - GO:0000813
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
  - GO:0000813
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
  - GO:0000813
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
  reference: data/structures/other/escrt_i_complex.yaml
  locator: Entire maintained record including all history, discussions, evidence,
    components, examples and causal graph
  accessed_at: '2026-10-22T06:28:05Z'
  support: context_only
  summary: The entire target was read; dated curation history is not independent biological
    evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, essentiality, taxonomic presence and
    graph scope
  accessed_at: '2026-10-22T06:28:05Z'
  support: context_only
  summary: Essentiality concerns formation, not function or viability. COMMON means
    present in most members, losses the exception; qualitative synthesis does not
    imply a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding and REVIEWED_LABEL_ONLY contract, including159–160
  accessed_at: '2026-10-22T06:28:05Z'
  support: context_only
  summary: Exact full-protein families are distinct from shared domains or paralog
    supergroups. A reviewed label-only status is not merely a placeholder for an exact
    mapping that was not curated this pass.
- evidence_id: escrt54-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621
  locator: Complete target-relevant definitions/synonym scopes and typed child relationships
    within combined response; unrelated terms not attributed to this record
  accessed_at: '2026-10-22T06:20:02.063646Z'
  support: supports
  summary: GO0000813 identifies ESCRT-I with the broad endosomal-sorting synonym;
    GO0036452 lists its is_a relationship, GO0010008 its part_of relationship, and
    GO0071985 the MVB sorting process.
  snapshot_sha256: 563ffa6dea1c58c1c92024214051980b0b5f3eefd7984f1ef56cb02432f9999b
- evidence_id: escrt54-agent-GO0000813-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T06:20:11.245548Z'
  support: supports
  summary: The is_a-only ancestor closure independently contains the ESCRT complex
    and protein-containing-complex classes. It is not a part_of query.
  snapshot_sha256: fa49f433545d7947ef44e9ec5541c54ab9935ff19ee26462ac2bbb9f45f1a4a5
- evidence_id: escrt54-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete ENA taxonomy response
  accessed_at: '2026-10-22T06:20:02.063372Z'
  support: supports
  summary: Taxon4932 is Saccharomyces cerevisiae, rankspecies; its native names and
    lineage identify this exact node.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: escrt54-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete ENA taxonomy response
  accessed_at: '2026-10-22T06:20:02.063749Z'
  support: supports
  summary: Taxon559292 is Saccharomyces cerevisiae S288C, rankstrain; its native names
    and lineage identify this exact node.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: escrt54-agent-protein-P25604
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P25604.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:20:02.063816Z'
  support: supports
  summary: 'Reviewed P25604: Suppressor protein STP22 of temperature-sensitive alpha-factor
    receptor and arginine permease; primary genes STP22, synonyms VPS23, taxon559292.
    Native comments retain their own experimental/inferred evidence scope. The protein
    response separately supplies its family xrefs; a family-entry response is not
    treated as this protein-membership proof.'
  snapshot_sha256: b0de38ad67a24e89fe41e94bc13c5f5b5ea036f0d6ccb504d5ce622bf3577414
- evidence_id: escrt54-agent-protein-P40343
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40343.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:20:02.992613Z'
  support: supports
  summary: 'Reviewed P40343: Vacuolar protein sorting-associated protein 27; primary
    genes VPS27, synonyms DID7, GRD11, SSV17, VPL23, VPT27, taxon559292. Native comments
    retain their own experimental/inferred evidence scope. The protein response separately
    supplies its family xrefs; a family-entry response is not treated as this protein-membership
    proof.'
  snapshot_sha256: 9722b86a9641dd5d053f0babc34f530ea7656e19571069c2eb081537e836c344
- evidence_id: escrt54-agent-protein-Q02767
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q02767.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:20:03.682852Z'
  support: supports
  summary: 'Reviewed Q02767: Vacuolar protein sorting-associated protein 28; primary
    genes VPS28, synonyms VPT28, taxon559292. Native comments retain their own experimental/inferred
    evidence scope. The protein response separately supplies its family xrefs; a family-entry
    response is not treated as this protein-membership proof.'
  snapshot_sha256: 56eebce70745b9c33357034221b182eb78ae00ce98a3b799854449f0374a0109
- evidence_id: escrt54-agent-protein-Q99176
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q99176.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:20:04.760661Z'
  support: supports
  summary: 'Reviewed Q99176: Protein SRN2; primary genes SRN2, synonyms SRN10, VPS37,
    taxon559292. Native comments retain their own experimental/inferred evidence scope.
    The protein response separately supplies its family xrefs; a family-entry response
    is not treated as this protein-membership proof.'
  snapshot_sha256: bea0740414b183a72cc53af6a86151fd0d79fcb6e3dc8984e880eef4ccc34322
- evidence_id: escrt54-agent-gene-VPS23-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS23%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:20:04.793964Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: P25604. Returned gene tokens/aliases
    identify the maintained protein without confusing its primary name with the queried
    synonym.'
  snapshot_sha256: 78cf1cdca34d69ad9d69d07c9a9dccc711cf406e25b50ee2c0525a4ba80b3f92
  search_scope: UniProt gene_exact:VPS23, organism_id:559292, reviewed:true, size500;
    all returned identities inspected.
- evidence_id: escrt54-agent-gene-VPS28-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS28%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:20:04.864114Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: Q02767. Returned gene tokens/aliases
    identify the maintained protein without confusing its primary name with the queried
    synonym.'
  snapshot_sha256: 9fdd0fc16a9ff02fd6fff17d3d0e65fd12df239b284b1bcef5e197468b39d640
  search_scope: UniProt gene_exact:VPS28, organism_id:559292, reviewed:true, size500;
    all returned identities inspected.
- evidence_id: escrt54-agent-gene-VPS37-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS37%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:20:05.650389Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: Q99176. Returned gene tokens/aliases
    identify the maintained protein without confusing its primary name with the queried
    synonym.'
  snapshot_sha256: 66cf662eb6731268cc492fcc3e7732b758ceea8a6bf835e99c96079810b423ec
  search_scope: UniProt gene_exact:VPS37, organism_id:559292, reviewed:true, size500;
    all returned identities inspected.
- evidence_id: escrt54-agent-pmid-11511343
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11511343+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED identity and abstract
  accessed_at: '2026-10-22T06:20:07.935812Z'
  support: supports
  summary: 'MED11511343: Ubiquitin-dependent sorting into the multivesicular body
    pathway requires the function of a conserved endosomal protein sorting complex,
    ESCRT-I. Katzmann DJ, Babst M, Emr SD. (2001), DOI10.1016/s0092-8674(01)00434-2.
    Exact metadata and complete abstract read; this is not full-body attestation.'
  snapshot_sha256: 89b0ab16f1c997094ab3253063701f5097b815c030e16320d5d41f485e3d50a9
- evidence_id: escrt54-agent-pmid-9790597
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9790597+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED identity and abstract
  accessed_at: '2026-10-22T06:20:09.526014Z'
  support: supports
  summary: 'MED9790597: Isolation of an extragenic suppressor of the rna1-1 mutation
    in Saccharomyces cerevisiae. Hong SJ, Yi YS, Koh SS, Park OK, Kang HS. (1998),
    DOI10.1007/s004380050830. Exact metadata and complete abstract read; this is not
    full-body attestation.'
  snapshot_sha256: 765c1486f25fcab25efc5bb92fabeb7927ec582146320700e03c8abddb232cf6
- evidence_id: escrt54-agent-doi-j_devcel_2011_05_015
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2011.05.015%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:10.119810Z'
  support: supports
  summary: 'Exact DOI/MED identity: The ESCRT pathway. Henne WM, Buchkovich NJ, Emr
    SD. (2011), PMID21763610. Complete native abstract read. This is a secondary review,
    not a new primary experiment.'
  snapshot_sha256: c1eb20e3ee3b89412437434900f82d42282d787ea5e51ef2d765091fa59227b0
- evidence_id: escrt54-agent-doi-jcb_200302136
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200302136%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:10.580061Z'
  support: supports
  summary: 'Exact DOI/MED identity: Vps27 recruits ESCRT machinery to endosomes during
    MVB sorting. Katzmann DJ, Stefan CJ, Babst M, Emr SD. (2003), PMID12900393. Complete
    native abstract read. Independent full-body evidence, where read, is listed separately.'
  snapshot_sha256: d4de23d4ecfeb30e41446c0788b94da7ad753012cae90fa16d578a1dcae56d26
- evidence_id: escrt54-agent-doi-jcb_200608053
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200608053%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:10.751708Z'
  support: supports
  summary: 'Exact DOI/MED identity: New component of ESCRT-I regulates endosomal sorting
    complex assembly. Chu T, Sun J, Saksena S, Emr SD. (2006), PMID17145965. Complete
    native abstract read. Independent full-body evidence, where read, is listed separately.'
  snapshot_sha256: 8efe42ab932ec5a7ab17bf7416760239e249b6e82f136d3b59d9ea2aa25490c8
- evidence_id: escrt54-agent-doi-mbc_e06-07-0588
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e06-07-0588%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:10.784973Z'
  support: supports
  summary: 'Exact DOI/MED identity: Efficient cargo sorting by ESCRT-I and the subsequent
    release of ESCRT-I from multivesicular bodies requires the subunit Mvb12. Curtiss
    M, Jones C, Babst M. (2007), PMID17135292. Complete native abstract read. Independent
    full-body evidence, where read, is listed separately.'
  snapshot_sha256: feb914a7d00662263b669d68f98065134a9e392103fec217814cf5c8ed665b9f
- evidence_id: escrt54-agent-katzmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/
  locator: Results sec3/5/6/7, including Fig1/3–6 captions; Methods sec12–15. No claim
    of independently reading sec4 or whole Discussion.
  accessed_at: '2026-10-22T01:12:25.464014Z'
  support: supports
  summary: Katzmann2003 directly tests independent ubiquitin binding, Vps27-dependent
    ESCRT-I endosomal localization and membrane-associated copurification. Vps27 UIM/VHS
    mutations do not abolish the association; C-terminal defects impair recruitment
    and sorting. SEY6210 and derivatives are the yeast systems. This supports an external
    recruiter rather than a stable core constituent.
  snapshot_sha256: d4bc3fc8fd5cbf98c1b88722373dbd34c271f2df8da4bbb78d4f808dc7197233
- evidence_id: escrt54-agent-primary-PMC2064680
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2064680/
  locator: Results sec3, Fig1/2 captions; Methods sec9. Other oligomer-model Results
    and Discussion not independently used.
  accessed_at: '2026-10-22T06:20:44.185196Z'
  support: supports
  summary: Chu2006 gel filtration and co-IP identify Mvb12 as an additional ESCRT-I
    member; its deletion gives partial cargo-sorting defects, unlike strong core mutants.
    The named SEY6210-derived strains are specified.
  snapshot_sha256: 4d6c72c9cb989fa6006f48f35a73776b8227beae64b76a736d81f6bb5ce15c2b
- evidence_id: escrt54-agent-primary-PMC1783790
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1783790/
  locator: Results sec10/11 and embedded Fig2/3/4/7 captions. Separate Table1/Methods
    not independently read.
  accessed_at: '2026-10-22T06:20:44.272074Z'
  support: supports
  summary: Curtiss2007 independently demonstrates Mvb12 association with ESCRT-I by
    reciprocal purification and gel filtration; deletion of VPS37 leaves a Vps23/Vps28
    subcomplex, while Mvb12 becomes unstable and fails to associate. These observations
    support the recorded later-subunit follow-up and do not turn apparent gel-filtration
    mass into exact stoichiometry.
  snapshot_sha256: a0da60ac02779a36c330c7a6cd2d86f8c4eced4d0731f3c782aeccd90bd7fd9a
- evidence_id: escrt54-agent-ipr-IPR052070
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052070/
  locator: Native name/type, complete descriptions and curation flags, member signatures
    and hierarchy; exact protein membership independently evidenced
  accessed_at: '2026-10-22T06:20:42.448243Z'
  support: supports
  summary: IPR052070 is typed as a protein family with PTHR23306, despite its UEV-domain-containing
    label. Its narrative is LLM-generated and unchecked, so no new mechanism rests
    on that prose. A separate reviewed-member query and the native protein join establish
    the Vps23/TSG101 class.
  snapshot_sha256: f7143f6883f4fc55f1725e57924b274e8b641a7ac8c6dac96c0f3cd5a893ca52
- evidence_id: escrt54-agent-ipr-IPR007143
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007143/
  locator: Native name/type, complete descriptions and curation flags, member signatures
    and hierarchy; exact protein membership independently evidenced
  accessed_at: '2026-10-22T06:20:42.448053Z'
  support: supports
  summary: IPR007143 is the complete Vps28 family with PTHR12937/PIRSF017535/PF03997
    signatures; its older complex-composition prose is not used to exclude Mvb12.
  snapshot_sha256: 621f858f83fc3e354313fc64712b5662381288c28e559bbe14d01f7478671392
- evidence_id: escrt54-agent-ipr-IPR017435
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017435/
  locator: Native name/type, complete descriptions and curation flags, member signatures
    and hierarchy; exact protein membership independently evidenced
  accessed_at: '2026-10-22T06:20:42.447660Z'
  support: supports
  summary: IPR017435 identifies fungal Vps37 with PIRSF038214. Its scope matches the
    explicitly yeast Vps37 row; it must not be advertised as the complete metazoan
    paralog universe. Its internally inconsistent heterotrimer/four-name prose is
    not adopted as stoichiometric evidence.
  snapshot_sha256: f2d3d4e441882ac4060dc165dd83002031f749a5dd4133885bfecddaee9c1b8c
- evidence_id: escrt54-agent-ipr-IPR009851
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009851/
  locator: Native name/type, complete descriptions and curation flags, member signatures
    and hierarchy; exact protein membership independently evidenced
  accessed_at: '2026-10-22T06:20:42.448005Z'
  support: supports
  summary: IPR009851 is a Modr/Vps37 C-terminal domain, not the whole Vps37 family.
    It is not selected as the constituent identity.
  snapshot_sha256: c2d25396c63d914ec06fc97ba1cd581577695fc05a27b11e9a4646b7c87b830d
- evidence_id: escrt54-agent-family-members-IPR052070
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR052070%29+AND+%28reviewed%3Atrue%29&format=json&fields=accession%2Cid%2Cprotein_name%2Cgene_names%2Corganism_id&size=500
  locator: Complete seven accession/name/aliases/taxon results
  accessed_at: '2026-10-22T06:25:31.005623Z'
  support: supports
  summary: All seven returned reviewed proteins are TSG101/Vps23 homolog identities,
    including human Q99816, yeast P25604, mouse Q61187, rat Q6IRE4, Arabidopsis Q9LHG8/Q9FFY6
    and Dictyostelium Q54LJ3. This corroborates the full-class meaning independently
    of the unchecked family prose.
  snapshot_sha256: 18c36a9a61ee3d0dbe1c0a2844ce3978e2f02079830eb2b6e01b299aade8ae2f
  search_scope: UniProt reviewed:true and xref:interpro-IPR052070, size500; all7 returned
    identities read. This is a bounded reviewed-member query, not an exhaustive evolutionary
    reconstruction.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/escrt_i_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:19Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/escrt_i_complex.yaml'
  snapshot_sha256: e8e846ecb0109b142910d982b9b8c0b9af922cf92247ec9ffb1e3500c8b57650
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/escrt_i_complex.yaml --out
    /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_i_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:20Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/escrt_i_complex.yaml\
    \ --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_i_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_i_complex-strict.tsv"
  snapshot_sha256: 1da949462852174deff69834220cc9f40c2a5663325612b7be383ff43e606d1b
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_i_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T06:25:15.736009Z'
  support: supports
  summary: "data/structures/other/escrt_i_complex.yaml  (GO:0000813)\n  yeast_escrt_i_mvb_cargo_sorting\t\
    vps23_escrt_i_subunit\tCOVERED\t->vps23_escrt_i_subunit (UniProtKB:P25604)\n \
    \ yeast_escrt_i_mvb_cargo_sorting\tvps28_escrt_i_subunit\tCOVERED\t->vps28_escrt_i_subunit\
    \ (UniProtKB:Q02767)\n  yeast_escrt_i_mvb_cargo_sorting\tvps37_escrt_i_subunit\t\
    COVERED\t->vps37_escrt_i_subunit (UniProtKB:Q99176)\n  yeast_escrt_i_mvb_cargo_sorting\t\
    vps27_endosomal_recruiter\tUNANCHORED_WITH_UNIPROT\tVps27 endosomal ESCRT-I recruiter\
    \ (UniProtKB:P40343)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries\
    \ a UniProtKB grounding or xref\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     4\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: aac6b7401b494f165148fbd63ff7a1fd22fde5cb5693ccd03f0e928f51a82f2e
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_i_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T06:25:16.943045Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/escrt_i_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:9790597: UNREACHABLE;
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
  topic: Exact ESCRT-I identity and historically bounded core
  outcome: supported
  target_ids:
  - GO:0000813
  summary: Identity, hierarchy/parthood, broad synonym and original yeast canonical
    example are supported. The three listed proteins are valid members. The record
    explicitly acknowledges Mvb12 as a later member and does not state that its list
    is exhaustive.
  evidence_ids:
  - record
  - escrt54-agent-go
  - escrt54-agent-GO0000813-ancestors
  - escrt54-agent-katzmann2003-pmc
  - escrt54-agent-primary-PMC2064680
  - escrt54-agent-primary-PMC1783790
  - escrt54-agent-pmid-11511343
- assessment_id: grounding
  area: grounding
  topic: Available exact subunit families
  outcome: concern
  target_ids:
  - GO:0000813
  summary: Vps23/TSG101 IPR052070, Vps28 IPR007143 and the explicitly fungal Vps37
    IPR017435 resolve the named yeast class mappings. Gene aliases STP22/VPS23 and
    SRN2/VPS37 are correctly disambiguated. The Vps37 domain and unchecked family
    narrative are not substitutes for class evidence.
  evidence_ids:
  - record
  - curation
  - escrt54-agent-ipr-IPR052070
  - escrt54-agent-ipr-IPR007143
  - escrt54-agent-ipr-IPR017435
  - escrt54-agent-ipr-IPR009851
  - escrt54-agent-family-members-IPR052070
  - escrt54-agent-protein-P25604
  - escrt54-agent-protein-P40343
  - escrt54-agent-protein-Q02767
  - escrt54-agent-protein-Q99176
  - escrt54-agent-gene-VPS23-559292
  - escrt54-agent-gene-VPS28-559292
  - escrt54-agent-gene-VPS37-559292
- assessment_id: scope
  area: scope
  topic: Yeast historical core and later component evidence
  outcome: supported
  target_ids:
  - GO:0000813
  summary: The species and reference-strain identities are correct; the early Katzmann
    yeast model and SEY6210-derived2003 preparations are distinct from accession reference
    metadata. Later Mvb12 evidence is acknowledged as a known incomplete inventory
    boundary, not denied.
  evidence_ids:
  - record
  - schema
  - escrt54-agent-katzmann2003-pmc
  - escrt54-agent-primary-PMC2064680
  - escrt54-agent-primary-PMC1783790
  - escrt54-agent-tax4932
  - escrt54-agent-tax559292
  - escrt54-agent-protein-P25604
  - escrt54-agent-protein-P40343
  - escrt54-agent-protein-Q02767
  - escrt54-agent-protein-Q99176
- assessment_id: graph
  area: graph
  topic: External recruitment and ubiquitinated cargo sorting
  outcome: supported
  target_ids:
  - GO:0000813
  summary: The NONMECHANISTIC graph accurately distinguishes core membership from
    Vps27-mediated recruitment and coarse MVB-sorting output. Direct Vps27/ESCRT-I
    membrane association supports recruitment without making Vps27 a stable core subunit.
  evidence_ids:
  - record
  - escrt54-agent-go
  - escrt54-agent-katzmann2003-pmc
  - escrt54-agent-pmid-11511343
  - escrt54-agent-protein-P25604
  - escrt54-agent-protein-P40343
  - escrt54-agent-protein-Q02767
  - escrt54-agent-protein-Q99176
- assessment_id: formation
  area: grounding
  topic: Unresolved individual formation requirements
  outcome: unknown
  target_ids:
  - GO:0000813
  summary: Sorting loss, localization defects and partial subcomplexes are not generalized
    to universal individual formation necessity. Curtiss specifically examines Mvb12
    stability/association and remaining subcomplexes; the present review does not
    convert those selected experiments into an all-subunit requirement table.
  evidence_ids:
  - record
  - schema
  - escrt54-agent-katzmann2003-pmc
  - escrt54-agent-primary-PMC1783790
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target with bounded source inspection
  outcome: supported
  target_ids:
  - GO:0000813
  summary: All maintained fields, evidence notes, graph statements and discussions
    were checked at the declared source extents. Optional inventories, exact stoichiometry
    and unresolved formation experiments are not fabricated from validation success.
  evidence_ids:
  - record
  - schema
  - curation
  - escrt54-agent-go
findings:
- finding_id: F1
  issue_key: escrt-i-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the three verified yeast ESCRT-I families
  description: The current label-only notes defer exact source-neutral family review.
    Native type/signature/member evidence now resolves the Vps23/TSG101 and Vps28
    classes and the explicitly fungal Vps37 class without relying on a UEV/Modr domain.
  target_ids:
  - GO:0000813
  field_paths:
  - components[*].grounding_status
  - discussions#resolve_escrt_i_family_groundings
  evidence_ids:
  - record
  - curation
  - escrt54-agent-ipr-IPR052070
  - escrt54-agent-ipr-IPR007143
  - escrt54-agent-ipr-IPR017435
  - escrt54-agent-ipr-IPR009851
  - escrt54-agent-family-members-IPR052070
  - escrt54-agent-protein-P25604
  - escrt54-agent-protein-P40343
  - escrt54-agent-protein-Q02767
  - escrt54-agent-protein-Q99176
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_i_complex.yaml
    role: maintained scientific record
  rule_id: Exact full-component grounding
  native_severity: minor
  normalization_reason: The correct structure and protein identities remain intact.
    The available exact family mappings resolve a bounded existing label-only deferral
    without changing complex membership or mechanism.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000813
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_i_complex.yaml
    role: maintained scientific record
  description: Use IPR052070 for Vps23, IPR007143 for Vps28 and IPR017435 for the
    explicitly yeast/fungal Vps37 constituent; align current grounding notes/TODO
    while preserving Mvb12 follow-up.
  acceptance_checks:
  - Keep Vps37 fungal scope explicit rather than claiming one family covers all metazoan
    paralogs.
  - Retain correct gene aliases and the separate Mvb12 inventory discussion.
  - Preserve supported identities and biological scope; pass applicable native gates.
limitations:
- Five completed same-base batch26 global gates await guarded parent manifest/hash
  integration.
- No source figure pixels, supplemental experiments or atomic coordinates were independently
  analyzed. Embedded captions are text evidence only.
- Reference proteins at S288C559292 do not identify every experimental yeast strain.
  COMMON keeps its majority-occurrence/losses-exception meaning; qualitative source
  synthesis supports it without measuring population prevalence.
- Katzmann2001 and Hong1998 were read at complete native abstract scope. Henne2011
  was read as review abstract only; retained publisher requests for Katzmann2001/Henne2011
  returned403.
- Mvb12 is positively supported by later primary studies and native protein annotations;
  its absent optional row is an acknowledged incomplete inventory rather than an assertion
  of absence. Exact Mvb12 family/stoichiometry expansion is not performed here.
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
