# Source-backed review of glutamate synthase complex

- Review: 20261022T072025Z-glutamate-synthase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:59:42Z
- Finished UTC: 2026-10-22T07:20:25Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One major unsupported taxonomic-scope finding and one minor tunnel-mechanism source-attribution gap. Exact identity, K12 GltB/GltD examples and overall synthesis are supported; neither finding asserts biological absence or disproves the later mechanism.

## Scope And Provenance

Exactly one complete target plus fourteen frozen target/guidance/schema inputs. Source-native identities and precise primary/abstract scopes were independently read; no neighboring record is an unstated premise.

Selection: Batch56 strict ordered selection index 4; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031026 | data/structures/other/glutamate_synthase_complex.yaml | maintained | glutamate synthase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031026 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031026 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0031026 | Native check passed; source support was independently assessed. |
| Focused native verify | passed | True | GO:0031026 | Native check passed; source support was independently assessed. |
| Claim-level scientific review | passed | True | GO:0031026 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031026 | 14 of 16 collected target identifiers returned OK. PMID:3326786: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:4565085: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031026 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031026 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031026 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031026 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031026 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact generic versus NADPH-specific ontology boundary

identity: supported. Targets: GO:0031026.

The maintained identifier and parents match the exact native GO class. The two NADPH protein components are explicitly named as that subtype and tied to K12 examples, rather than treated as a verified inventory for every alternative GOGAT architecture.

### Supported GltB/GltD identities and bounded unresolved families

grounding: supported. Targets: GO:0031026.

CPX, reviewed proteins and Oliver complete abstract support the two K12 subunit classes. Exact gene queries match. The checked GltD families are mixed, and the candidate GltB metadata/subfamily route do not establish the required exact NADPH class; no optional family is forced.

### Formation necessity remains unknown

evidence: unknown. Targets: GO:0031026.

Both components already use UNKNOWN. Purification, subunit composition and whole-enzyme catalysis do not establish a universal loss-of-subunit physical assembly requirement. No fixed protein stoichiometry is imported from Miller into null CPX protein counts.

### Supported overall synthesis with overextended nearest citations

evidence: concern. Targets: GO:0031026.

Overall reductive glutamate synthesis is supported. The added tunnel and specific cofactor-routing account goes beyond the short GO definition and the directly read Miller study, which expressly leaves cofactor arrangement unresolved. This is a source-attribution gap, not proof that the later mechanistic account is biologically false.

### Broad taxon statements need scope-matched provenance

scope: concern. Targets: GO:0031026.

K12 identity and the separate E.coli W experimental context are verified. The record attaches its bacterial, archaeal and fungal distribution notes to Miller1972; that purified E.coli study is not scope-matched evidence for those lineage patterns. COMMON keeps its majority-occurrence meaning; VARIABLE keeps its actual distribution meaning.

### Lineage-wide prevalence and architecture limits remain unresolved

scope: unknown. Targets: GO:0031026.

The inspected material does not quantify COMMON in Bacteria/Fungi or establish the exact archaeal distribution pattern. Nor does it establish one cofactor/tunnel architecture for every GOGAT class. These statements are not independently disproved; modern scope-matched sources are needed.

### Coarse membership and function with the same citation gap

graph: concern. Targets: GO:0031026.

The two component_ref joins are correct and supported for the named NADPH subtype. A coarse enzyme-to-reaction causal claim is reasonable, but the graph repeats the unsupported source attribution for its detailed tunnel description; no additional topology-only finding is invented.

### Complete target with bounded source and optional-field limits

completeness: supported. Targets: GO:0031026.

All maintained scientific fields, discussion/history, graph actors/edges and citations were read. Findings concern concrete source placement or a verified current family task, not empty optional slots. Native protein/family databases address these claims; expression-module inference is not used for physical membership.

## Findings

### F1: Support the asserted cross-lineage GOGAT distribution

major / open / confirmed; issue key: gogat-cross-lineage-presence-source-scope.

The definition extends the account across bacteria, archaea, yeasts and microalgae, while the three distribution rows assert COMMON Bacteria, VARIABLE Archaea and COMMON Fungi using Miller1972. That directly inspected source is an E.coli W biochemical study; GO supplies only an activity-based generic definition, and CPX/UniProt here describe K12. These sources do not establish the broad lineage patterns or their PresenceEnum strengths.

### F2: Attach appropriate evidence to the detailed tunnel account

minor / open / confirmed; issue key: gogat-tunnel-mechanism-source-attribution.

The definition attaches modern cofactor/tunnel detail to the short GO definition; the function and final graph edge cite Miller1972 for the specific intramolecular ammonia-tunnel and FMN/[3Fe4S] account. The inspected paper explicitly leaves cofactor arrangement unresolved. Its demonstrated overall synthesis remains correctly cited.

## Recommended Actions And Acceptance Checks

### A1

Add directly read sources that actually support each lineage and its stated occurrence pattern, qualifying or narrowing the distribution and definition where that support cannot be established. Keep the exact generic GO identity and the separately supported E.coli model.

- Each retained COMMON or VARIABLE row has scope-matched support for that actual enum meaning, not merely one example or an unmeasured pattern.
- The definition distinguishes the generic activity class from experimentally established lineage-specific architectures.
- Native schema, strict and CURIE checks pass after separately authorized curation.

### A2

Retain the source-supported overall reaction and cite a directly read mechanistic source for the tunnel/cofactor expansion, with its subtype and experimental scope; otherwise restrict the explanatory prose to what the current sources establish.

- Each retained tunnel/cofactor claim is attached to a source that actually establishes it.
- Do not attribute an atomic or subunit-resolved model to the1972 whole-enzyme assay.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/glutamate_synthase_complex.yaml; Entire current YAML, including components, examples, all evidence, graph, discussions and history | context_only | All target bytes were read. No neighboring maintained record is an unstated premise. |
| curation | docs/CURATION.md; Exact source-neutral component classes and reviewed-label-only contract | context_only | A family identifies the molecular class; its role in a particular complex need not be exclusive to that complex. A species protein example does not replace family grounding. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and causal graph fields | context_only | UNKNOWN does not assert assembly necessity. COMMON means present in most members with exceptional losses; VARIABLE is a distribution pattern, not a synonym for unmeasured prevalence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Actor identity and edge-level evidence | context_only | A coarse physical assembly and catalysis account may be mechanistic without every intermediate. Association, catalytic activity and formation necessity remain distinct. |
| micro56-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Native taxId, scientificName, rank, lineage and equivalent name. | supports | ENA taxId83333 is Escherichia coli K-12, rank strain; UniProt strain-format labels refer to the same taxon. |
| micro56-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031026,GO:0009342,GO:0004355,GO:0140535,GO:1990204,GO:0005960,GO:1990234,GO:0004375; Only exact GOGAT target/parent/function entries, definitions, synonyms and relevant typed child relations in the combined eight-term response. | supports | GO0031026 identifies the generic glutamate-synthase complex; GO0009342 is its NADPH-specific child and cites PMID4565085. GO0004355 supplies the NADPH reaction and lists the complex capable_of it. GO0140535 and GO1990204 identify intracellular and oxidoreductase complexes. The generic GO definition is only the short activity-based sentence, without the maintained expanded tunnel or cross-domain distribution account. |
| micro56-GO0031026-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031026/ancestors?relations=is_a; Complete exact-target relations=is_a ancestors array; no parthood inference from ancestry. | supports | The is_a-only array confirms the maintained parent relationships for this exact target. |
| micro56-pmid-4565085 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A4565085+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: exact PMID, title, authors, year, DOI and available abstractText. | supports | PMID4565085: Glutamate synthase from Escherichia coli. An iron-sulfide flavoprotein. Miller RE, Stadtman ER. (1972), DOI10.1016/s0021-9258(19)44642-5. No abstract is supplied in this native record. |
| micro56-pmid-3326786 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3326786+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED record: exact PMID, title, authors, year, DOI and available abstractText. | supports | PMID3326786: Determination of the nucleotide sequence for the glutamate synthase structural genes of Escherichia coli K-12. Oliver G, Gosset G, Sanchez-Pescador R, Lozoya E, Ku LM, Flores N, Becerril B, Valle F, Bolivar F. (1987), DOI10.1016/0378-1119(87)90207-1. The complete native abstract was read; no unlisted main-body claim is inferred. |
| micro56-cpx-5041 | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-5041; Complete functions/properties/species/participants/linkedFeatures/crossReferences/evidenceType response. Cofactor participant EBI22228055 and protein participants EBI22228009/10; source spelling stochiometry is retained. | supports | CPX5041 is the E.coli K12 NADPH glutamate synthase, systematic gltB:gltD. The complete response supports overall glutamine/2-oxoglutarate conversion, nitrogen-assimilation context, P09831/P09832 membership, their EBI participant IDs and one CHEBI49883 cofactor linked to GltD. Protein copy counts are null. No subunit-resolved electron-routing mechanism is stated. |
| micro56-miller1972-browser-start | https://www.researchgate.net/publication/348283815_Glutamate_Synthase_from_Escherichia_coli; Genuine primary OCR browser representation, status:null: lines0–696, printed pp7407–7409, title/summary/Introduction and Methods through sedimentation studies/start of sucrose-gradient section. No pixels or unretained Methods. | supports | Miller and Stadtman purified E.coli W glutamate synthase and measured whole-enzyme NADPH-dependent reductive glutamate synthesis, flavins and iron/labile sulfide. This experimental W strain is separate from the K12 CPX and protein examples. The retained initial Methods describe growth/purification, assays and sedimentation preparation. |
| micro56-miller1972-browser-claims | https://www.researchgate.net/publication/348283815_Glutamate_Synthase_from_Escherichia_coli; Browser representation status:null: primary lines1476–1706,2585–2942,3025–3223, printed pp7410–7418 selected Results and Discussion beginning. No figure pixels; unrelated tail excluded. | supports | Selected primary Results identify flavin/iron analysis and two differently sized polypeptide chains, with equimolar composition inferred from gel staining. This is biochemical whole-enzyme/subunit analysis, not an atomic ammonia-tunnel structure. |
| micro56-miller1972-browser-redox | https://www.researchgate.net/publication/348283815_Glutamate_Synthase_from_Escherichia_coli; Browser representation status:null, primary lines1491–2385: absorption/flavin/redox/substrate/kinetic Results and captured captions. The receipt timestamp records retention after retrieval, not a reconstructed network timestamp. No pixels. | supports | The primary whole-enzyme redox/substrate Results distinguish NADPH from NADH and describe coupled substrate-dependent oxidation/reduction. They explicitly qualify flavin/iron interpretation; these measurements do not isolate GltD-to-GltB electron transfer. |
| micro56-miller1972-browser-discussion | https://www.researchgate.net/publication/348283815_Glutamate_Synthase_from_Escherichia_coli; Browser representation status:null: complete scientific Discussion lines3088–3342, printed p7418. References and unrelated citation tail are excluded. | supports | The complete scientific Discussion explicitly states that arrangement of flavin, iron and sulfide had not been resolved; subunit studies were ongoing. It discusses whole-enzyme cofactor possibilities and a four-heterodimer interpretation. It does not establish the subsequently specified intramolecular tunnel or subunit electron pathway. |
| micro56-protein-P09831 | https://rest.uniprot.org/uniprotkb/P09831.json; Native identity/status/name, genes, organism/taxonId; complete FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs. Location annotations, if present, do not independently establish complex membership. | supports | Reviewed K12 P09831 is gltB/aspB, large NADPH GOGAT chain. Native FUNCTION/SUBUNIT cite Miller for overall conversion and aggregation; [3Fe4S] is similarity-based. Its miscellaneous substrate-site wording is tentative and is not used as direct modern tunnel evidence. |
| micro56-gene-gltB | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgltB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results identity set; exact gene_exact, organism_id:83333 and reviewed:true query in the retained URL. | supports | The exact reviewed organism83333 gene query returns one entry, P09831; the returned primary gene or declared synonym matches gltB. |
| micro56-protein-P09832 | https://rest.uniprot.org/uniprotkb/P09832.json; Native identity/status/name, genes, organism/taxonId; complete FUNCTION, CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs. Location annotations, if present, do not independently establish complex membership. | supports | Reviewed K12 P09832 is gltD/aspB, small NADPH GOGAT chain. Native [4Fe4S] annotation is rule-based; whole-enzyme FUNCTION/SUBUNIT cites Miller. No independently demonstrated GltD-to-GltB route is inferred from the shared whole-enzyme annotation. |
| micro56-gene-gltD | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgltD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete results identity set; exact gene_exact, organism_id:83333 and reviewed:true query in the retained URL. | supports | The exact reviewed organism83333 gene query returns one entry, P09832; the returned primary gene or declared synonym matches gltD. |
| micro56-ipr-IPR006006 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006006/; Complete native family name/type/description and TIGR01318 signature metadata. | context_only | IPR006006 is a GltD-like family that explicitly also includes AegA/ucaF relatives; the current broad-family withholding is justified for a specifically NADPH-GltD component. |
| micro56-ncbifam-NF008730 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008730/; Complete native accession/name/type/description/integration/representative_structure fields; no unread structural paper is adopted. | context_only | NF008730 names glutamate synthase large subunit and describes the overall reaction; its representative structure is Synechocystis glutamate synthase1OFD. This metadata does not independently establish specificity for the maintained NADPH large-chain class, so it is a candidate rather than a forced replacement. |
| micro56-ncbifam-TIGR01318 | https://www.ebi.ac.uk/interpro/api/entry/ncbifam/TIGR01318/; Complete native family description and integrated field. | context_only | TIGR01318 explicitly includes small-subunit homologs and related paralogs of unknown function, and is integrated into IPR006006. It therefore does not close the exact GltD task. |
| micro56-panther-PTHR42783 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR42783/; Native type/name and llm:true, checked:false description flags, integration and representative structure. | context_only | PTHR42783 currently names an oxidoreductase/NADPH-dependent synthase domain-containing family. Its broad unchecked generated description is not treated as exact GltD identity or mechanistic evidence. |
| micro56-panther-PTHR11938-SF148 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR11938:SF148/; Original204 receipt and empty raw hash. | context_only | The PANTHER subfamily candidate returned HTTP204 and zero bytes; no current exact family scope is inferred from this response. |
| micro56-miller1972-jbc-pdf | https://www.jbc.org/article/S0021-9258(19)44642-5/pdf; Original native403 response. | context_only | The direct JBC PDF request returned HTTP403 HTML, not an article PDF. Positive body support comes only from the separately retained genuine browser primary passages. |
| micro56-oliver1987-doi | https://doi.org/10.1016/0378-1119(87)90207-1; Original request/error bytes. | context_only | The native Oliver DOI request failed TLS certificate verification with status0. Its complete MED abstract supports gene sequencing; no main-body reading is claimed. |
| micro56-tax2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Native taxId, scientificName and rank. | supports | ENA taxId2 is Bacteria, domain. |
| micro56-tax2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; Native taxId, scientificName and rank. | supports | ENA taxId2157 is Archaea, domain. |
| micro56-tax4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; Native taxId, scientificName and rank. | supports | ENA taxId4751 is Fungi, kingdom. |
| schema-result | just validate data/structures/other/glutamate_synthase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/glutamate_synthase_complex.yaml |
| strict-result | just validate-strict data/structures/other/glutamate_synthase_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glutamate_synthase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/glutamate_synthase_complex.yaml --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glutamate_synthase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glutamate_synthase_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/glutamate_synthase_complex.yaml --causal-graphs; Complete focused read-only native report | supports | data/structures/other/glutamate_synthase_complex.yaml  (GO:0031026)<br>  glutamate_synthase_complex_mechanism	gltb_large_chain	COVERED	-&gt;gltb_large_chain (UniProtKB:P09831)<br>  glutamate_synthase_complex_mechanism	gltd_small_chain	COVERED	-&gt;gltd_small_chain (UniProtKB:P09832)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/glutamate_synthase_complex.yaml --verify; Complete focused read-only native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/glutamate_synthase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 16 collected target identifiers returned OK. PMID:3326786: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:4565085: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Miller1972 was read only in the retained primary browser blocks: summary/Introduction/initial Methods, selected cofactor/subunit/redox/substrate Results and complete scientific Discussion. No image pixels, unretained Methods/Results or supplements were read. The direct JBC PDF route was403.
- Oliver1987 is complete native abstract only; its direct DOI route failed TLS verification. E.coli W in Miller is kept separate from K12 in the CPX/protein examples.
- The native protein cofactor annotations include similarity/rule-based evidence and whole-enzyme biochemical citations. They are not all direct subunit-resolved measurements; tentative native miscellaneous substrate-site text is not adopted as modern mechanism.
- Candidate-family checking is bounded to the retained InterPro/NCBIfam/PANTHER entries, including a204 empty subfamily response. It is not an exhaustive absence claim across all databases.
- Original source URL, actual retained UTC and SHA256 joins are preserved; browser representations have status:null and are not called native HTTP200 bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requests one review for every unreviewed record, including qualified clean cases.
- This is a scientific review with disclosed source access limits, not a claim that every cited paper was fully readable.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T072025Z-glutamate-synthase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of glutamate synthase complex
started_at: '2026-10-22T06:59:42Z'
finished_at: '2026-10-22T07:20:25Z'
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
summary: One major unsupported taxonomic-scope finding and one minor tunnel-mechanism
  source-attribution gap. Exact identity, K12 GltB/GltD examples and overall synthesis
  are supported; neither finding asserts biological absence or disproves the later
  mechanism.
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
  - path: data/structures/other/glutamate_synthase_complex.yaml
    sha256: 23058436ce8a0db4f794546c7afc6a50d364c0bec3a8672cd3fd7fb129c698c0
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
- target_id: GO:0031026
  path: data/structures/other/glutamate_synthase_complex.yaml
  label: glutamate synthase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glutamate_synthase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target plus fourteen frozen target/guidance/schema
    inputs. Source-native identities and precise primary/abstract scopes were independently
    read; no neighboring record is an unstated premise.
  selection: Batch56 strict ordered selection index 4; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031026
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031026
  command: just validate data/structures/other/glutamate_synthase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031026
  command: just validate-strict data/structures/other/glutamate_synthase_complex.yaml
    --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glutamate_synthase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0031026
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glutamate_synthase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native check passed; source support was independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0031026
  command: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glutamate_synthase_complex.yaml
    --verify
  exit_code: 0
  summary: Native check passed; source support was independently assessed.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031026
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-pmid-4565085
  - micro56-pmid-3326786
  - micro56-cpx-5041
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-protein-P09831
  - micro56-gene-gltB
  - micro56-protein-P09832
  - micro56-gene-gltD
  - micro56-ipr-IPR006006
  - micro56-ncbifam-NF008730
  - micro56-ncbifam-TIGR01318
  - micro56-panther-PTHR42783
  - micro56-panther-PTHR11938-SF148
  - micro56-miller1972-jbc-pdf
  - micro56-oliver1987-doi
  - micro56-tax2
  - micro56-tax2157
  - micro56-tax4751
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031026
  summary: '14 of 16 collected target identifiers returned OK. PMID:3326786: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:4565085: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro56-pmid-3326786
  - micro56-pmid-4565085
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031026
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031026
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031026
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031026
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031026
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
    and current batch56 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/glutamate_synthase_complex.yaml
  locator: Entire current YAML, including components, examples, all evidence, graph,
    discussions and history
  accessed_at: '2026-10-22T07:08:49Z'
  support: context_only
  summary: All target bytes were read. No neighboring maintained record is an unstated
    premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact source-neutral component classes and reviewed-label-only contract
  accessed_at: '2026-10-22T07:08:49Z'
  support: context_only
  summary: A family identifies the molecular class; its role in a particular complex
    need not be exclusive to that complex. A species protein example does not replace
    family grounding.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and causal graph fields
  accessed_at: '2026-10-22T07:08:49Z'
  support: context_only
  summary: UNKNOWN does not assert assembly necessity. COMMON means present in most
    members with exceptional losses; VARIABLE is a distribution pattern, not a synonym
    for unmeasured prevalence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor identity and edge-level evidence
  accessed_at: '2026-10-22T07:08:49Z'
  support: context_only
  summary: A coarse physical assembly and catalysis account may be mechanistic without
    every intermediate. Association, catalytic activity and formation necessity remain
    distinct.
- evidence_id: micro56-tax83333
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Native taxId, scientificName, rank, lineage and equivalent name.
  accessed_at: '2026-10-22T06:56:30.426930Z'
  support: supports
  summary: ENA taxId83333 is Escherichia coli K-12, rank strain; UniProt strain-format
    labels refer to the same taxon.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: micro56-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031026,GO:0009342,GO:0004355,GO:0140535,GO:1990204,GO:0005960,GO:1990234,GO:0004375
  locator: Only exact GOGAT target/parent/function entries, definitions, synonyms
    and relevant typed child relations in the combined eight-term response.
  accessed_at: '2026-10-22T06:56:29.752821Z'
  support: supports
  summary: GO0031026 identifies the generic glutamate-synthase complex; GO0009342
    is its NADPH-specific child and cites PMID4565085. GO0004355 supplies the NADPH
    reaction and lists the complex capable_of it. GO0140535 and GO1990204 identify
    intracellular and oxidoreductase complexes. The generic GO definition is only
    the short activity-based sentence, without the maintained expanded tunnel or cross-domain
    distribution account.
  snapshot_sha256: 82929c8bb8ff4aca3063e872086f8cb0653f40f64d99f9220af7f6f194f64762
- evidence_id: micro56-GO0031026-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031026/ancestors?relations=is_a
  locator: Complete exact-target relations=is_a ancestors array; no parthood inference
    from ancestry.
  accessed_at: '2026-10-22T06:56:29.753055Z'
  support: supports
  summary: The is_a-only array confirms the maintained parent relationships for this
    exact target.
  snapshot_sha256: 62ff09dd47612b25e984fe8a2bfbfe9da0dbbf527097ee821f4c200d41e848a2
- evidence_id: micro56-pmid-4565085
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A4565085+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: exact PMID, title, authors, year, DOI and available
    abstractText.'
  accessed_at: '2026-10-22T06:56:33.922813Z'
  support: supports
  summary: 'PMID4565085: Glutamate synthase from Escherichia coli. An iron-sulfide
    flavoprotein. Miller RE, Stadtman ER. (1972), DOI10.1016/s0021-9258(19)44642-5.
    No abstract is supplied in this native record.'
  snapshot_sha256: 9ccba4054ba7c9fed87a40a135561e76d81af3a105562a8c0232955e854b07c9
- evidence_id: micro56-pmid-3326786
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A3326786+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED record: exact PMID, title, authors, year, DOI and available
    abstractText.'
  accessed_at: '2026-10-22T06:56:33.959928Z'
  support: supports
  summary: 'PMID3326786: Determination of the nucleotide sequence for the glutamate
    synthase structural genes of Escherichia coli K-12. Oliver G, Gosset G, Sanchez-Pescador
    R, Lozoya E, Ku LM, Flores N, Becerril B, Valle F, Bolivar F. (1987), DOI10.1016/0378-1119(87)90207-1.
    The complete native abstract was read; no unlisted main-body claim is inferred.'
  snapshot_sha256: 179d480aa9191ed5f2eb96f3066aa29295a98296f3dd7a179812c82ab9228aab
- evidence_id: micro56-cpx-5041
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-5041
  locator: Complete functions/properties/species/participants/linkedFeatures/crossReferences/evidenceType
    response. Cofactor participant EBI22228055 and protein participants EBI22228009/10;
    source spelling stochiometry is retained.
  accessed_at: '2026-10-22T06:56:35.153044Z'
  support: supports
  summary: CPX5041 is the E.coli K12 NADPH glutamate synthase, systematic gltB:gltD.
    The complete response supports overall glutamine/2-oxoglutarate conversion, nitrogen-assimilation
    context, P09831/P09832 membership, their EBI participant IDs and one CHEBI49883
    cofactor linked to GltD. Protein copy counts are null. No subunit-resolved electron-routing
    mechanism is stated.
  snapshot_sha256: 11e381b9fde6c0e27f4bf681f69a9cd07d7b5729934ee023e98e52d76634e5e7
- evidence_id: micro56-miller1972-browser-start
  kind: primary_source
  reference: https://www.researchgate.net/publication/348283815_Glutamate_Synthase_from_Escherichia_coli
  locator: 'Genuine primary OCR browser representation, status:null: lines0–696, printed
    pp7407–7409, title/summary/Introduction and Methods through sedimentation studies/start
    of sucrose-gradient section. No pixels or unretained Methods.'
  accessed_at: '2026-10-22T06:57:49Z'
  support: supports
  summary: Miller and Stadtman purified E.coli W glutamate synthase and measured whole-enzyme
    NADPH-dependent reductive glutamate synthesis, flavins and iron/labile sulfide.
    This experimental W strain is separate from the K12 CPX and protein examples.
    The retained initial Methods describe growth/purification, assays and sedimentation
    preparation.
  snapshot_sha256: 10e686f930b202c3c48e45b607778b6d861afc42f38b7f9b6238e30f57698296
- evidence_id: micro56-miller1972-browser-claims
  kind: primary_source
  reference: https://www.researchgate.net/publication/348283815_Glutamate_Synthase_from_Escherichia_coli
  locator: 'Browser representation status:null: primary lines1476–1706,2585–2942,3025–3223,
    printed pp7410–7418 selected Results and Discussion beginning. No figure pixels;
    unrelated tail excluded.'
  accessed_at: '2026-10-22T06:59:55Z'
  support: supports
  summary: Selected primary Results identify flavin/iron analysis and two differently
    sized polypeptide chains, with equimolar composition inferred from gel staining.
    This is biochemical whole-enzyme/subunit analysis, not an atomic ammonia-tunnel
    structure.
  snapshot_sha256: 16ac3225b97d9c58370a6e89b7244e735913fbb64b3ea61229e0313b947093c6
- evidence_id: micro56-miller1972-browser-redox
  kind: primary_source
  reference: https://www.researchgate.net/publication/348283815_Glutamate_Synthase_from_Escherichia_coli
  locator: 'Browser representation status:null, primary lines1491–2385: absorption/flavin/redox/substrate/kinetic
    Results and captured captions. The receipt timestamp records retention after retrieval,
    not a reconstructed network timestamp. No pixels.'
  accessed_at: '2026-10-22T07:01:56.980882Z'
  support: supports
  summary: The primary whole-enzyme redox/substrate Results distinguish NADPH from
    NADH and describe coupled substrate-dependent oxidation/reduction. They explicitly
    qualify flavin/iron interpretation; these measurements do not isolate GltD-to-GltB
    electron transfer.
  snapshot_sha256: 14f46c34f59be0fdc3eb9c99a04cf40cc2b5562d400d67afd4a5a0739f227f1e
- evidence_id: micro56-miller1972-browser-discussion
  kind: primary_source
  reference: https://www.researchgate.net/publication/348283815_Glutamate_Synthase_from_Escherichia_coli
  locator: 'Browser representation status:null: complete scientific Discussion lines3088–3342,
    printed p7418. References and unrelated citation tail are excluded.'
  accessed_at: '2026-10-22T06:59:55Z'
  support: supports
  summary: The complete scientific Discussion explicitly states that arrangement of
    flavin, iron and sulfide had not been resolved; subunit studies were ongoing.
    It discusses whole-enzyme cofactor possibilities and a four-heterodimer interpretation.
    It does not establish the subsequently specified intramolecular tunnel or subunit
    electron pathway.
  snapshot_sha256: 37dd3d570a9d9209046b027910c61d58eae77db9ed42ddf69c8c2abbc974365a
- evidence_id: micro56-protein-P09831
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09831.json
  locator: Native identity/status/name, genes, organism/taxonId; complete FUNCTION,
    CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs.
    Location annotations, if present, do not independently establish complex membership.
  accessed_at: '2026-10-22T06:56:31.023737Z'
  support: supports
  summary: Reviewed K12 P09831 is gltB/aspB, large NADPH GOGAT chain. Native FUNCTION/SUBUNIT
    cite Miller for overall conversion and aggregation; [3Fe4S] is similarity-based.
    Its miscellaneous substrate-site wording is tentative and is not used as direct
    modern tunnel evidence.
  snapshot_sha256: b2f7e196a1860b3077336a435191af794505ea0ee109780dccabeec07f342494
- evidence_id: micro56-gene-gltB
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgltB%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results identity set; exact gene_exact, organism_id:83333 and
    reviewed:true query in the retained URL.
  accessed_at: '2026-10-22T06:56:31.837709Z'
  support: supports
  summary: The exact reviewed organism83333 gene query returns one entry, P09831;
    the returned primary gene or declared synonym matches gltB.
  snapshot_sha256: aee5953cf2a5570594858d161c5d6f8eb517b2f3eec79a18e047a20b978f9abd
- evidence_id: micro56-protein-P09832
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P09832.json
  locator: Native identity/status/name, genes, organism/taxonId; complete FUNCTION,
    CATALYTIC ACTIVITY, COFACTOR, SUBUNIT, MISCELLANEOUS and relevant family xrefs.
    Location annotations, if present, do not independently establish complex membership.
  accessed_at: '2026-10-22T06:56:31.116308Z'
  support: supports
  summary: Reviewed K12 P09832 is gltD/aspB, small NADPH GOGAT chain. Native [4Fe4S]
    annotation is rule-based; whole-enzyme FUNCTION/SUBUNIT cites Miller. No independently
    demonstrated GltD-to-GltB route is inferred from the shared whole-enzyme annotation.
  snapshot_sha256: 158a20b579879be81128069517676f72beb2a8f97a47dca3d1e98d564a07112c
- evidence_id: micro56-gene-gltD
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AgltD%29+AND+%28organism_id%3A83333%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete results identity set; exact gene_exact, organism_id:83333 and
    reviewed:true query in the retained URL.
  accessed_at: '2026-10-22T06:56:31.837866Z'
  support: supports
  summary: The exact reviewed organism83333 gene query returns one entry, P09832;
    the returned primary gene or declared synonym matches gltD.
  snapshot_sha256: 4970c8024c2c6985dad12bbca83679077c34b7229b1c521a09668802183834f7
- evidence_id: micro56-ipr-IPR006006
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006006/
  locator: Complete native family name/type/description and TIGR01318 signature metadata.
  accessed_at: '2026-10-22T06:56:34.518159Z'
  support: context_only
  summary: IPR006006 is a GltD-like family that explicitly also includes AegA/ucaF
    relatives; the current broad-family withholding is justified for a specifically
    NADPH-GltD component.
  snapshot_sha256: 89ee16882419f44674ceb63cd5a52673099668347ea658dd1d89d788fc75174d
- evidence_id: micro56-ncbifam-NF008730
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/NF008730/
  locator: Complete native accession/name/type/description/integration/representative_structure
    fields; no unread structural paper is adopted.
  accessed_at: '2026-10-22T06:57:19.177865Z'
  support: context_only
  summary: NF008730 names glutamate synthase large subunit and describes the overall
    reaction; its representative structure is Synechocystis glutamate synthase1OFD.
    This metadata does not independently establish specificity for the maintained
    NADPH large-chain class, so it is a candidate rather than a forced replacement.
  snapshot_sha256: 39f2b48a2d06f403a56cd3c6e127cee1dd1430deb821b2d0ba58518cc17d34b4
- evidence_id: micro56-ncbifam-TIGR01318
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/ncbifam/TIGR01318/
  locator: Complete native family description and integrated field.
  accessed_at: '2026-10-22T06:57:19.188028Z'
  support: context_only
  summary: TIGR01318 explicitly includes small-subunit homologs and related paralogs
    of unknown function, and is integrated into IPR006006. It therefore does not close
    the exact GltD task.
  snapshot_sha256: a2bfea3ae5183c13c40716bf7ea563bc38feab5934dfa873fd46dba64e1d4e14
- evidence_id: micro56-panther-PTHR42783
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR42783/
  locator: Native type/name and llm:true, checked:false description flags, integration
    and representative structure.
  accessed_at: '2026-10-22T06:57:18.519060Z'
  support: context_only
  summary: PTHR42783 currently names an oxidoreductase/NADPH-dependent synthase domain-containing
    family. Its broad unchecked generated description is not treated as exact GltD
    identity or mechanistic evidence.
  snapshot_sha256: 84b19098c9ce5a1795f567ca35b54336e1d67483b62ab857df53b34649b6ff86
- evidence_id: micro56-panther-PTHR11938-SF148
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR11938:SF148/
  locator: Original204 receipt and empty raw hash.
  accessed_at: '2026-10-22T06:57:18.517651Z'
  support: context_only
  summary: The PANTHER subfamily candidate returned HTTP204 and zero bytes; no current
    exact family scope is inferred from this response.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro56-miller1972-jbc-pdf
  kind: authority
  reference: https://www.jbc.org/article/S0021-9258(19)44642-5/pdf
  locator: Original native403 response.
  accessed_at: '2026-10-22T06:57:19.201183Z'
  support: context_only
  summary: The direct JBC PDF request returned HTTP403 HTML, not an article PDF. Positive
    body support comes only from the separately retained genuine browser primary passages.
  snapshot_sha256: 459341401cccd88d1f896e3ce46491bf786d8e2f8db4d847f66153d224d0208e
- evidence_id: micro56-oliver1987-doi
  kind: authority
  reference: https://doi.org/10.1016/0378-1119(87)90207-1
  locator: Original request/error bytes.
  accessed_at: '2026-10-22T06:57:19.302063Z'
  support: context_only
  summary: The native Oliver DOI request failed TLS certificate verification with
    status0. Its complete MED abstract supports gene sequencing; no main-body reading
    is claimed.
  snapshot_sha256: a8014ecefc9b9c4cc3987abe484f64b8ee37dd3e6bc0182a0f12915e702dedb3
- evidence_id: micro56-tax2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Native taxId, scientificName and rank.
  accessed_at: '2026-10-22T06:56:30.432888Z'
  support: supports
  summary: ENA taxId2 is Bacteria, domain.
  snapshot_sha256: 314bd7723b8dea04f1840809fb74e06c514664fba9c6a0619e8f12e2a6dceef1
- evidence_id: micro56-tax2157
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: Native taxId, scientificName and rank.
  accessed_at: '2026-10-22T06:56:30.453199Z'
  support: supports
  summary: ENA taxId2157 is Archaea, domain.
  snapshot_sha256: c6e652011b95e43e933983bf5f3f5cec9508c1925adae00dc55e46cd4e816b19
- evidence_id: micro56-tax4751
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: Native taxId, scientificName and rank.
  accessed_at: '2026-10-22T06:56:30.463642Z'
  support: supports
  summary: ENA taxId4751 is Fungi, kingdom.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/glutamate_synthase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:43Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/glutamate_synthase_complex.yaml'
  snapshot_sha256: 495b8a067ee2e2fdc7e5cd69aae7a8b89b2002451d81fdc287deadc4c21d055e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/glutamate_synthase_complex.yaml
    --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glutamate_synthase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:59:44Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/glutamate_synthase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glutamate_synthase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/glutamate_synthase_complex-strict.tsv"
  snapshot_sha256: a1c4ad9b6d582a91cb9ab97bf1ddda3a7a8aa4147762c4e2a3ee875ffd2875a6
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glutamate_synthase_complex.yaml
    --causal-graphs
  locator: Complete focused read-only native report
  accessed_at: '2026-10-22T07:03:52.650764Z'
  support: supports
  summary: "data/structures/other/glutamate_synthase_complex.yaml  (GO:0031026)\n\
    \  glutamate_synthase_complex_mechanism\tgltb_large_chain\tCOVERED\t->gltb_large_chain\
    \ (UniProtKB:P09831)\n  glutamate_synthase_complex_mechanism\tgltd_small_chain\t\
    COVERED\t->gltd_small_chain (UniProtKB:P09832)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     2  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 132d8050362f291e087f84d47b3dab7a1219309bbc138e675785bc5f2de4476f
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch56-20261022-3zkw_2l0/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/glutamate_synthase_complex.yaml
    --verify
  locator: Complete focused read-only native report
  accessed_at: '2026-10-22T07:03:53.936780Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/glutamate_synthase_complex.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 16 collected target identifiers returned OK. PMID:3326786: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:4565085: UNREACHABLE;
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
  topic: Exact generic versus NADPH-specific ontology boundary
  outcome: supported
  target_ids:
  - GO:0031026
  summary: The maintained identifier and parents match the exact native GO class.
    The two NADPH protein components are explicitly named as that subtype and tied
    to K12 examples, rather than treated as a verified inventory for every alternative
    GOGAT architecture.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-cpx-5041
  - micro56-protein-P09831
  - micro56-gene-gltB
  - micro56-protein-P09832
  - micro56-gene-gltD
- assessment_id: composition
  area: grounding
  topic: Supported GltB/GltD identities and bounded unresolved families
  outcome: supported
  target_ids:
  - GO:0031026
  summary: CPX, reviewed proteins and Oliver complete abstract support the two K12
    subunit classes. Exact gene queries match. The checked GltD families are mixed,
    and the candidate GltB metadata/subfamily route do not establish the required
    exact NADPH class; no optional family is forced.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-protein-P09831
  - micro56-gene-gltB
  - micro56-protein-P09832
  - micro56-gene-gltD
  - micro56-cpx-5041
  - micro56-ipr-IPR006006
  - micro56-ncbifam-NF008730
  - micro56-ncbifam-TIGR01318
  - micro56-panther-PTHR42783
  - micro56-panther-PTHR11938-SF148
  - micro56-pmid-4565085
  - micro56-pmid-3326786
- assessment_id: formation
  area: evidence
  topic: Formation necessity remains unknown
  outcome: unknown
  target_ids:
  - GO:0031026
  summary: Both components already use UNKNOWN. Purification, subunit composition
    and whole-enzyme catalysis do not establish a universal loss-of-subunit physical
    assembly requirement. No fixed protein stoichiometry is imported from Miller into
    null CPX protein counts.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-cpx-5041
- assessment_id: function
  area: evidence
  topic: Supported overall synthesis with overextended nearest citations
  outcome: concern
  target_ids:
  - GO:0031026
  summary: Overall reductive glutamate synthesis is supported. The added tunnel and
    specific cofactor-routing account goes beyond the short GO definition and the
    directly read Miller study, which expressly leaves cofactor arrangement unresolved.
    This is a source-attribution gap, not proof that the later mechanistic account
    is biologically false.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-protein-P09831
  - micro56-gene-gltB
  - micro56-protein-P09832
  - micro56-gene-gltD
  - micro56-cpx-5041
- assessment_id: scope
  area: scope
  topic: Broad taxon statements need scope-matched provenance
  outcome: concern
  target_ids:
  - GO:0031026
  summary: K12 identity and the separate E.coli W experimental context are verified.
    The record attaches its bacterial, archaeal and fungal distribution notes to Miller1972;
    that purified E.coli study is not scope-matched evidence for those lineage patterns.
    COMMON keeps its majority-occurrence meaning; VARIABLE keeps its actual distribution
    meaning.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-tax2
  - micro56-tax2157
  - micro56-tax4751
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-cpx-5041
- assessment_id: prevalence
  area: scope
  topic: Lineage-wide prevalence and architecture limits remain unresolved
  outcome: unknown
  target_ids:
  - GO:0031026
  summary: The inspected material does not quantify COMMON in Bacteria/Fungi or establish
    the exact archaeal distribution pattern. Nor does it establish one cofactor/tunnel
    architecture for every GOGAT class. These statements are not independently disproved;
    modern scope-matched sources are needed.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-tax2
  - micro56-tax2157
  - micro56-tax4751
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
- assessment_id: graph
  area: graph
  topic: Coarse membership and function with the same citation gap
  outcome: concern
  target_ids:
  - GO:0031026
  summary: The two component_ref joins are correct and supported for the named NADPH
    subtype. A coarse enzyme-to-reaction causal claim is reasonable, but the graph
    repeats the unsupported source attribution for its detailed tunnel description;
    no additional topology-only finding is invented.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-protein-P09831
  - micro56-gene-gltB
  - micro56-protein-P09832
  - micro56-gene-gltD
  - micro56-cpx-5041
  - micro56-ipr-IPR006006
  - micro56-ncbifam-NF008730
  - micro56-ncbifam-TIGR01318
  - micro56-panther-PTHR42783
  - micro56-panther-PTHR11938-SF148
  - micro56-pmid-4565085
  - micro56-pmid-3326786
- assessment_id: coverage
  area: completeness
  topic: Complete target with bounded source and optional-field limits
  outcome: supported
  target_ids:
  - GO:0031026
  summary: All maintained scientific fields, discussion/history, graph actors/edges
    and citations were read. Findings concern concrete source placement or a verified
    current family task, not empty optional slots. Native protein/family databases
    address these claims; expression-module inference is not used for physical membership.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-protein-P09831
  - micro56-gene-gltB
  - micro56-protein-P09832
  - micro56-gene-gltD
  - micro56-cpx-5041
  - micro56-ipr-IPR006006
  - micro56-ncbifam-NF008730
  - micro56-ncbifam-TIGR01318
  - micro56-panther-PTHR42783
  - micro56-panther-PTHR11938-SF148
  - micro56-pmid-4565085
  - micro56-pmid-3326786
findings:
- finding_id: F1
  issue_key: gogat-cross-lineage-presence-source-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Support the asserted cross-lineage GOGAT distribution
  description: The definition extends the account across bacteria, archaea, yeasts
    and microalgae, while the three distribution rows assert COMMON Bacteria, VARIABLE
    Archaea and COMMON Fungi using Miller1972. That directly inspected source is an
    E.coli W biochemical study; GO supplies only an activity-based generic definition,
    and CPX/UniProt here describe K12. These sources do not establish the broad lineage
    patterns or their PresenceEnum strengths.
  target_ids:
  - GO:0031026
  field_paths:
  - definition
  - definition_source
  - taxonomic_distribution
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-tax2
  - micro56-tax2157
  - micro56-tax4751
  - micro56-cpx-5041
  - micro56-protein-P09831
  - micro56-gene-gltB
  - micro56-protein-P09832
  - micro56-gene-gltD
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glutamate_synthase_complex.yaml
    role: maintained scientific record
  rule_id: Exact claim-level source support and component-class grounding
  native_severity: major
  normalization_reason: 'Major materially unsupported taxonomic scope: the record
    makes affirmative lineage-wide distribution claims beyond the directly observed
    model context. No biological absence, falsehood or numerical-census requirement
    is inferred; qualitative lineage-relevant support would suffice.'
- finding_id: F2
  issue_key: gogat-tunnel-mechanism-source-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach appropriate evidence to the detailed tunnel account
  description: The definition attaches modern cofactor/tunnel detail to the short
    GO definition; the function and final graph edge cite Miller1972 for the specific
    intramolecular ammonia-tunnel and FMN/[3Fe4S] account. The inspected paper explicitly
    leaves cofactor arrangement unresolved. Its demonstrated overall synthesis remains
    correctly cited.
  target_ids:
  - GO:0031026
  field_paths:
  - definition
  - definition_source
  - functions[0].description
  - functions[0].evidence
  - causal_graphs[0].nodes[3].description
  - causal_graphs[0].edges[2]
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro56-tax83333
  - micro56-go
  - micro56-GO0031026-ancestors
  - micro56-miller1972-browser-start
  - micro56-miller1972-browser-claims
  - micro56-miller1972-browser-redox
  - micro56-miller1972-browser-discussion
  - micro56-cpx-5041
  - micro56-protein-P09831
  - micro56-gene-gltB
  - micro56-protein-P09832
  - micro56-gene-gltD
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glutamate_synthase_complex.yaml
    role: maintained scientific record
  rule_id: Exact claim-level source support and component-class grounding
  native_severity: minor
  normalization_reason: A localized explanatory/source-placement problem within the
    supported overall enzyme reaction. Unlike the separate affirmative lineage-wide
    occurrence finding, this does not alter the generic identity or invent a different
    reaction; it requires source precision without declaring the modern account false.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0031026
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glutamate_synthase_complex.yaml
    role: maintained scientific record
  description: Add directly read sources that actually support each lineage and its
    stated occurrence pattern, qualifying or narrowing the distribution and definition
    where that support cannot be established. Keep the exact generic GO identity and
    the separately supported E.coli model.
  acceptance_checks:
  - Each retained COMMON or VARIABLE row has scope-matched support for that actual
    enum meaning, not merely one example or an unmeasured pattern.
  - The definition distinguishes the generic activity class from experimentally established
    lineage-specific architectures.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0031026
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/glutamate_synthase_complex.yaml
    role: maintained scientific record
  description: Retain the source-supported overall reaction and cite a directly read
    mechanistic source for the tunnel/cofactor expansion, with its subtype and experimental
    scope; otherwise restrict the explanatory prose to what the current sources establish.
  acceptance_checks:
  - Each retained tunnel/cofactor claim is attached to a source that actually establishes
    it.
  - Do not attribute an atomic or subunit-resolved model to the1972 whole-enzyme assay.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- 'Miller1972 was read only in the retained primary browser blocks: summary/Introduction/initial
  Methods, selected cofactor/subunit/redox/substrate Results and complete scientific
  Discussion. No image pixels, unretained Methods/Results or supplements were read.
  The direct JBC PDF route was403.'
- Oliver1987 is complete native abstract only; its direct DOI route failed TLS verification.
  E.coli W in Miller is kept separate from K12 in the CPX/protein examples.
- The native protein cofactor annotations include similarity/rule-based evidence and
  whole-enzyme biochemical citations. They are not all direct subunit-resolved measurements;
  tentative native miscellaneous substrate-site text is not adopted as modern mechanism.
- Candidate-family checking is bounded to the retained InterPro/NCBIfam/PANTHER entries,
  including a204 empty subfamily response. It is not an exhaustive absence claim across
  all databases.
- Original source URL, actual retained UTC and SHA256 joins are preserved; browser
  representations have status:null and are not called native HTTP200 bodies.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requests one review for every unreviewed record, including qualified
  clean cases.
- This is a scientific review with disclosed source access limits, not a claim that
  every cited paper was fully readable.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
