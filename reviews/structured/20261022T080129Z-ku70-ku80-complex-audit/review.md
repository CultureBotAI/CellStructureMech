# Source-backed review of ku70 ku80 complex

- Review: 20261022T080129Z-ku70-ku80-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:34:48Z
- Finished UTC: 2026-10-22T08:01:29Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One grouped minor exact-family gap for Ku70 and Ku80. Heterodimer identity, yeast examples and bounded DNA-end/NHEJ relationships are supported. Yeast primary bodies remain limited to complete native abstracts; Downs2004 is bibliographic-only.

## Scope And Provenance

Exactly one complete target and thirteen frozen target/guidance/schema inputs. Primary bodies, native identities and stated access scopes were independently read; no neighboring record is an unstated premise.

Selection: Batch58 strict ordered selection index 5; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0043564 | data/structures/other/ku70_ku80_complex.yaml | maintained | Ku70:Ku80 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0043564 | Focused validator passed. |
| Focused native strict | passed | True | GO:0043564 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0043564 | Native check passed; scientific support independently assessed. |
| Focused native verify | passed | True | GO:0043564 | Native check passed; scientific support independently assessed. |
| Claim-level scientific review | passed | True | GO:0043564 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0043564 | 12 of 18 collected target identifiers returned OK. PMID:12518983: UNREACHABLE; Native Europe PMC uniquely identifies MED12518983: Dimerization, translocation and localization of Ku70 and Ku80 proteins. (2002); DOI 10.1269/jrr.43.223. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:15122350: UNREACHABLE; Native Europe PMC uniquely identifies MED15122350: A means to a DNA end: the many roles of Ku. (2004); DOI 10.1038/nrm1367. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8890183: UNREACHABLE; Native Europe PMC uniquely identifies MED8890183: Saccharomyces cerevisiae Ku70 potentiates illegitimate DNA double-strand break repair and serves as a barrier to error-prone DNA repair pathways. (1996); DOI 10.1002/j.1460-2075.1996.tb00890.x. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8910371: UNREACHABLE; Native Europe PMC uniquely identifies MED8910371: HDF2, the second subunit of the Ku homologue from Saccharomyces cerevisiae. (1996); DOI 10.1074/jbc.271.44.27765. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8972848: UNREACHABLE; Native Europe PMC uniquely identifies MED8972848: Identification of a Saccharomyces cerevisiae Ku80 homologue: roles in DNA double strand break rejoining and in telomeric maintenance. (1996); DOI 10.1093/nar/24.23.4639. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:9635192: UNREACHABLE; Native Europe PMC uniquely identifies MED9635192: Mutation of yeast Ku genes disrupts the subnuclear organization of telomeres. (1998); DOI 10.1016/s0960-9822(98)70252-0. This resolves the identifier transport residual only; primary-source reading remains separately scoped. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0043564 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0043564 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0043564 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0043564 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0043564 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact heterodimer and nuclear-complex parent

identity: supported. Targets: GO:0043564.

The class is Ku70:Ku80 rather than DNA-PK or a prokaryotic Ku homodimer. The generic channel/function definition is supported at review/ontology level, with organism-specific functions not automatically exported to the yeast example.

### Both named whole subunit classes have exact families

grounding: concern. Targets: GO:0043564.

Reviewed yeast YKU70/P32807 and YKU80/Q04437 identities agree with their exact queries and independently verified family cross-references. IPR006165 and IPR024193 fit the two classes; IPR006164 is only the shared domain.

### Unknown necessity is not replaced by repair essentiality

evidence: unknown. Targets: GO:0043564.

Yeast abstracts establish DNA-binding/rejoining phenotypes and HDF2 identity, while the secondary review discusses heterodimer stability in mammalian cells. These are not a universal yeast loss-of-subunit formation test. Existing UNKNOWN essentiality remains appropriate.

### Yeast reference identity and source access are distinct

scope: supported. Targets: GO:0043564.

COMMON preserves majority occurrence with exceptional losses; the inspected literature provides qualitative yeast context rather than a census. S288C reference accessions are correct. Feldmann and Boulton yeast primary claims were checked at complete native abstract tier, not a falsely claimed full body.

### Bounded nonmechanistic DNA-end recognition and repair

graph: supported. Targets: GO:0043564.

The NON_MECHANISTIC graph expresses Ku subunit participation, DNA-end association and NHEJ support. It expressly leaves detailed mammalian DNA-PK regulation and other interactions unresolved, so no yeast V(D)J/DNA-PK mechanism is inferred.

### Entire target with bounded positive evidence

completeness: supported. Targets: GO:0043564.

All scientific fields, examples, citations, graphs, discussions and history were read. Existing protein examples were checked directly; no empty optional slot alone is treated as an error. Source tiers and actual reading extents are explicit.

## Findings

### F1: Ground the two Ku subunit classes

minor / open / confirmed; issue key: ku70-ku80-exact-subunit-families.

Ku70/Yku70 and Ku80/Yku80 remain REVIEWED_LABEL_ONLY despite exact whole-family identities IPR006165 and IPR024193. Native family types/signatures and separately verified yeast protein cross-references corroborate both mappings.

## Recommended Actions And Acceptance Checks

### A1

Ground Ku70 to IPR006165 and Ku80 to IPR024193, retaining yeast roles, examples and UNKNOWN assembly necessity.

- Each mapping identifies the correct whole subunit family.
- Shared Ku domain IPR006164 is not used as an exact whole-subunit identity.
- Native schema, strict and CURIE checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/ku70_ku80_complex.yaml; Entire current YAML, including every scientific field, graph, discussion and history entry | context_only | All target bytes were read. No neighboring maintained record is an unstated premise. |
| curation | docs/CURATION.md; Component-class grounding and reviewed-label-only contract | context_only | A verified species protein example does not replace exact source-neutral class grounding; protein families need not be exclusive to one complex. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and graph fields | context_only | Assembly necessity is distinct from catalytic activity, viability and localization. COMMON means present in most members with exceptional losses; VARIABLE does not merely mean unmeasured prevalence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Actor identity and edge-level evidence | context_only | A coarse supported physical mechanism can be represented without inventing every intermediate; a source-specific demonstration claim must match the actual experiment. |
| micro58-pmid-12518983 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12518983+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED result: exact PMID, title, authors, year, DOI and complete abstractText when present. | supports | PMID12518983: Dimerization, translocation and localization of Ku70 and Ku80 proteins. Koike M. (2002), DOI10.1269/jrr.43.223. The complete native abstract was read; no unlisted body scope is implied. |
| micro58-pmid-15122350 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15122350+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED result: exact PMID, title, authors, year, DOI and complete abstractText when present. | context_only | PMID15122350: A means to a DNA end: the many roles of Ku. Downs JA, Jackson SP. (2004), DOI10.1038/nrm1367. This native MED response has no abstractText; it supplies bibliographic identity only, not scientific body support. |
| micro58-pmid-8890183 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8890183+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED result: exact PMID, title, authors, year, DOI and complete abstractText when present. | supports | PMID8890183: Saccharomyces cerevisiae Ku70 potentiates illegitimate DNA double-strand break repair and serves as a barrier to error-prone DNA repair pathways. Boulton SJ, Jackson SP. (1996), DOI10.1002/j.1460-2075.1996.tb00890.x. The complete native abstract was read; no unlisted body scope is implied. |
| micro58-pmid-8910371 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910371+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED result: exact PMID, title, authors, year, DOI and complete abstractText when present. | supports | PMID8910371: HDF2, the second subunit of the Ku homologue from Saccharomyces cerevisiae. Feldmann H, Driller L, Meier B, Mages G, Kellermann J, Winnacker EL. (1996), DOI10.1074/jbc.271.44.27765. The complete native abstract was read; no unlisted body scope is implied. |
| micro58-pmid-8972848 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8972848+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED result: exact PMID, title, authors, year, DOI and complete abstractText when present. | supports | PMID8972848: Identification of a Saccharomyces cerevisiae Ku80 homologue: roles in DNA double strand break rejoining and in telomeric maintenance. Boulton SJ, Jackson SP. (1996), DOI10.1093/nar/24.23.4639. The complete native abstract was read; no unlisted body scope is implied. |
| micro58-pmid-9635192 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9635192+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED result: exact PMID, title, authors, year, DOI and complete abstractText when present. | supports | PMID9635192: Mutation of yeast Ku genes disrupts the subnuclear organization of telomeres. Laroche T, Martin SG, Gotta M, Gorham HC, Pryde FE, Louis EJ, Gasser SM. (1998), DOI10.1016/s0960-9822(98)70252-0. The complete native abstract was read; no unlisted body scope is implied. |
| micro58-protein-P32807 | https://rest.uniprot.org/uniprotkb/P32807.json; Native identity/status/names, genes, organism/taxonId; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments and relevant InterPro cross-references. | supports | Reviewed P32807 identifies YKU70 in taxon559292; native names, gene aliases, organism, location and subunit comments match this maintained example. Native family cross-references provide separate corroboration of candidate class mappings. Unlisted annotation papers are not claimed as independently read. |
| micro58-gene-YKU70 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYKU70%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set; actual gene_exact, organism_id and reviewed:true query preserved in original URL. | supports | The exact reviewed YKU70 query returns one entry, P32807, with matching primary gene or declared synonym and exact organism. |
| micro58-protein-Q04437 | https://rest.uniprot.org/uniprotkb/Q04437.json; Native identity/status/names, genes, organism/taxonId; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments and relevant InterPro cross-references. | supports | Reviewed Q04437 identifies YKU80 in taxon559292; native names, gene aliases, organism, location and subunit comments match this maintained example. Native family cross-references provide separate corroboration of candidate class mappings. Unlisted annotation papers are not claimed as independently read. |
| micro58-gene-YKU80 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYKU80%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set; actual gene_exact, organism_id and reviewed:true query preserved in original URL. | supports | The exact reviewed YKU80 query returns one entry, Q04437, with matching primary gene or declared synonym and exact organism. |
| micro58-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444,GO:0000776,GO:0000817,GO:0006303,GO:0007059,GO:0031262,GO:0043564,GO:0045027,GO:0062051,GO:0140513,GO:1990351; Only these four exact entries, definitions/synonyms and typed links in the combined response. | supports | GO0043564 is the Ku70:Ku80 heterodimer; GO0140513 is the nuclear protein-containing-complex parent. GO0045027 and GO0006303 identify DNA-end binding and NHEJ. Generic Ku definitions cover several organism-dependent functions and do not establish yeast V(D)J recombination or DNA-PK activation. |
| micro58-GO0043564-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043564/ancestors?relations=is_a; Complete exact-target relations=is_a array. | supports | The is_a-only ancestor array includes nuclear protein-containing complex GO0140513 and protein-containing complex GO0032991. |
| micro58-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA4932 identifies Saccharomyces cerevisiae species. |
| micro58-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Native taxId, scientificName, rank, lineage and relevant equivalent names. | supports | ENA559292 identifies S288C, the reviewed reference-protein strain. |
| micro58-koike2002-jstage-pdf | https://www.jstage.jst.go.jp/article/jrr/43/3/43_3_223/_pdf; Genuine J-STAGE PDF: printed pp223–227, complete Abstract/Introduction, chromosome-location section and dimerization section through its end at the start of p228. Remaining p228 onward and figure pixels not read. | supports | The secondary review describes the two-subunit channel, broad Ku functions, mammalian heterodimer stability and organism-specific NHEJ differences. It explicitly notes no obvious DNA-PKcs homologue in yeast; mammalian V(D)J and DNA-PK context is not assigned to the yeast graph. |
| micro58-IPR006165 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006165/; Complete native family type/name/description/member signatures; accession membership is separately supplied by the protein evidence. | supports | IPR006165 is the whole Ku70 family, with Ku70-specific PIRSF003033 and TIGR00578 signatures. Its identity is distinct from the shared Ku70/Ku80 domain. |
| micro58-IPR024193 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024193/; Complete native family type/name/description/member signatures; accession membership is separately supplied by the protein evidence. | supports | IPR024193 is the Ku80 family with Ku80-specific PIRSF016570 and cd00873 signatures. General evolutionary background about prokaryotic Ku is not substituted for this eukaryotic subunit class. |
| micro58-IPR006164 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006164/; Complete native type/name/description and member signatures. | context_only | IPR006164 is the shared Ku70/Ku80 DNA-binding domain and is not an exact replacement for either whole subunit class. |
| micro58-PMC146307-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC146307/; Actual retained status/body diagnostic and original receipt. | context_only | The retained HTTP200 legacy response is a browser-check challenge, not the Boulton Ku80 main body. |
| micro58-feldmann1996-publisher-html | https://www.sciencedirect.com/science/article/pii/S0021925818352992; Actual retained status/body diagnostic and original receipt. | context_only | The ScienceDirect route returned403 and an error page, not the Feldmann main body. |
| schema-result | just validate data/structures/other/ku70_ku80_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/ku70_ku80_complex.yaml |
| strict-result | just validate-strict data/structures/other/ku70_ku80_complex.yaml --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/ku70_ku80_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/ku70_ku80_complex.yaml --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/ku70_ku80_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/ku70_ku80_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml --causal-graphs; Complete focused read-only native report | supports | data/structures/other/ku70_ku80_complex.yaml  (GO:0043564)<br>  ku70_ku80_dna_end_joining	ku70_subunit	COVERED	-&gt;ku70_subunit (UniProtKB:P32807)<br>  ku70_ku80_dna_end_joining	ku80_subunit	COVERED	-&gt;ku80_subunit (UniProtKB:Q04437)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml --verify; Complete focused read-only native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/ku70_ku80_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 18 collected target identifiers returned OK. PMID:12518983: UNREACHABLE; Native Europe PMC uniquely identifies MED12518983: Dimerization, translocation and localization of Ku70 and Ku80 proteins. (2002); DOI 10.1269/jrr.43.223. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:15122350: UNREACHABLE; Native Europe PMC uniquely identifies MED15122350: A means to a DNA end: the many roles of Ku. (2004); DOI 10.1038/nrm1367. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8890183: UNREACHABLE; Native Europe PMC uniquely identifies MED8890183: Saccharomyces cerevisiae Ku70 potentiates illegitimate DNA double-strand break repair and serves as a barrier to error-prone DNA repair pathways. (1996); DOI 10.1002/j.1460-2075.1996.tb00890.x. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8910371: UNREACHABLE; Native Europe PMC uniquely identifies MED8910371: HDF2, the second subunit of the Ku homologue from Saccharomyces cerevisiae. (1996); DOI 10.1074/jbc.271.44.27765. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:8972848: UNREACHABLE; Native Europe PMC uniquely identifies MED8972848: Identification of a Saccharomyces cerevisiae Ku80 homologue: roles in DNA double strand break rejoining and in telomeric maintenance. (1996); DOI 10.1093/nar/24.23.4639. This resolves the identifier transport residual only; primary-source reading remains separately scoped.; PMID:9635192: UNREACHABLE; Native Europe PMC uniquely identifies MED9635192: Mutation of yeast Ku genes disrupts the subnuclear organization of telomeres. (1998); DOI 10.1016/s0960-9822(98)70252-0. This resolves the identifier transport residual only; primary-source reading remains separately scoped. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Koike is a secondary review and was read only in the specified pp223–228 extent. Boulton/Feldmann and Laroche primary claims were inspected at complete native abstract tier; no inaccessible main body or figure pixels are certified.
- The retained Downs2004 MED record contains no abstractText, so it resolves bibliography only. A DOI content-negotiation response is bibliographic JSON, not a publisher main body.
- Mammalian V(D)J, DNA-PK and stability contexts are not equated with yeast mechanisms. Approximate70/80kDa class names are not claims of directly measured invariant yeast masses.
- COMMON retains its majority meaning; no population census or universal formation requirement is inferred.
- All reused source bytes preserve their original URL, UTC and SHA256. Readability is established from content rather than HTTP200 alone.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requests one review for every unreviewed record, including qualified clean cases.
- No maintained scientific record, historical review or initial native inspection snapshot is edited.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T080129Z-ku70-ku80-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of ku70 ku80 complex
started_at: '2026-10-22T07:34:48Z'
finished_at: '2026-10-22T08:01:29Z'
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
summary: One grouped minor exact-family gap for Ku70 and Ku80. Heterodimer identity,
  yeast examples and bounded DNA-end/NHEJ relationships are supported. Yeast primary
  bodies remain limited to complete native abstracts; Downs2004 is bibliographic-only.
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
  - path: data/structures/other/ku70_ku80_complex.yaml
    sha256: 6f49f9f9be4112bd44c0c606a4cc485466092240af95a3dce5107a46e117de44
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
- target_id: GO:0043564
  path: data/structures/other/ku70_ku80_complex.yaml
  label: Ku70:Ku80 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ku70_ku80_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target and thirteen frozen target/guidance/schema
    inputs. Primary bodies, native identities and stated access scopes were independently
    read; no neighboring record is an unstated premise.
  selection: Batch58 strict ordered selection index 5; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0043564
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: just validate data/structures/other/ku70_ku80_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: just validate-strict data/structures/other/ku70_ku80_complex.yaml --out
    /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/ku70_ku80_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native check passed; scientific support independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml
    --verify
  exit_code: 0
  summary: Native check passed; scientific support independently assessed.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0043564
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro58-pmid-12518983
  - micro58-pmid-15122350
  - micro58-pmid-8890183
  - micro58-pmid-8910371
  - micro58-pmid-8972848
  - micro58-pmid-9635192
  - micro58-protein-P32807
  - micro58-gene-YKU70
  - micro58-protein-Q04437
  - micro58-gene-YKU80
  - micro58-go
  - micro58-GO0043564-ancestors
  - micro58-tax4932
  - micro58-tax559292
  - micro58-koike2002-jstage-pdf
  - micro58-IPR006165
  - micro58-IPR024193
  - micro58-IPR006164
  - micro58-PMC146307-legacy
  - micro58-feldmann1996-publisher-html
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0043564
  summary: '12 of 18 collected target identifiers returned OK. PMID:12518983: UNREACHABLE;
    Native Europe PMC uniquely identifies MED12518983: Dimerization, translocation
    and localization of Ku70 and Ku80 proteins. (2002); DOI 10.1269/jrr.43.223. This
    resolves the identifier transport residual only; primary-source reading remains
    separately scoped.; PMID:15122350: UNREACHABLE; Native Europe PMC uniquely identifies
    MED15122350: A means to a DNA end: the many roles of Ku. (2004); DOI 10.1038/nrm1367.
    This resolves the identifier transport residual only; primary-source reading remains
    separately scoped.; PMID:8890183: UNREACHABLE; Native Europe PMC uniquely identifies
    MED8890183: Saccharomyces cerevisiae Ku70 potentiates illegitimate DNA double-strand
    break repair and serves as a barrier to error-prone DNA repair pathways. (1996);
    DOI 10.1002/j.1460-2075.1996.tb00890.x. This resolves the identifier transport
    residual only; primary-source reading remains separately scoped.; PMID:8910371:
    UNREACHABLE; Native Europe PMC uniquely identifies MED8910371: HDF2, the second
    subunit of the Ku homologue from Saccharomyces cerevisiae. (1996); DOI 10.1074/jbc.271.44.27765.
    This resolves the identifier transport residual only; primary-source reading remains
    separately scoped.; PMID:8972848: UNREACHABLE; Native Europe PMC uniquely identifies
    MED8972848: Identification of a Saccharomyces cerevisiae Ku80 homologue: roles
    in DNA double strand break rejoining and in telomeric maintenance. (1996); DOI
    10.1093/nar/24.23.4639. This resolves the identifier transport residual only;
    primary-source reading remains separately scoped.; PMID:9635192: UNREACHABLE;
    Native Europe PMC uniquely identifies MED9635192: Mutation of yeast Ku genes disrupts
    the subnuclear organization of telomeres. (1998); DOI 10.1016/s0960-9822(98)70252-0.
    This resolves the identifier transport residual only; primary-source reading remains
    separately scoped. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro58-pmid-12518983
  - micro58-pmid-15122350
  - micro58-pmid-8890183
  - micro58-pmid-8910371
  - micro58-pmid-8972848
  - micro58-pmid-9635192
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0043564
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0043564
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
    and current batch58 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/ku70_ku80_complex.yaml
  locator: Entire current YAML, including every scientific field, graph, discussion
    and history entry
  accessed_at: '2026-10-22T07:51:04Z'
  support: context_only
  summary: All target bytes were read. No neighboring maintained record is an unstated
    premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component-class grounding and reviewed-label-only contract
  accessed_at: '2026-10-22T07:51:04Z'
  support: context_only
  summary: A verified species protein example does not replace exact source-neutral
    class grounding; protein families need not be exclusive to one complex.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and graph fields
  accessed_at: '2026-10-22T07:51:04Z'
  support: context_only
  summary: Assembly necessity is distinct from catalytic activity, viability and localization.
    COMMON means present in most members with exceptional losses; VARIABLE does not
    merely mean unmeasured prevalence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Actor identity and edge-level evidence
  accessed_at: '2026-10-22T07:51:04Z'
  support: context_only
  summary: A coarse supported physical mechanism can be represented without inventing
    every intermediate; a source-specific demonstration claim must match the actual
    experiment.
- evidence_id: micro58-pmid-12518983
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12518983+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED result: exact PMID, title, authors, year, DOI and complete
    abstractText when present.'
  accessed_at: '2026-10-22T07:38:53.322527Z'
  support: supports
  summary: 'PMID12518983: Dimerization, translocation and localization of Ku70 and
    Ku80 proteins. Koike M. (2002), DOI10.1269/jrr.43.223. The complete native abstract
    was read; no unlisted body scope is implied.'
  snapshot_sha256: b4b54375216336ec96f3577a665e13bb4d2707024ac19ed7ea5b584ba1aa33bf
- evidence_id: micro58-pmid-15122350
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15122350+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED result: exact PMID, title, authors, year, DOI and complete
    abstractText when present.'
  accessed_at: '2026-10-22T07:38:54.213221Z'
  support: context_only
  summary: 'PMID15122350: A means to a DNA end: the many roles of Ku. Downs JA, Jackson
    SP. (2004), DOI10.1038/nrm1367. This native MED response has no abstractText;
    it supplies bibliographic identity only, not scientific body support.'
  snapshot_sha256: 91045e5bd1330d5d41f5be6cc60c47c0d9f532d3ebc1044fd264c876e3278db6
- evidence_id: micro58-pmid-8890183
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8890183+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED result: exact PMID, title, authors, year, DOI and complete
    abstractText when present.'
  accessed_at: '2026-10-22T07:38:55.498124Z'
  support: supports
  summary: 'PMID8890183: Saccharomyces cerevisiae Ku70 potentiates illegitimate DNA
    double-strand break repair and serves as a barrier to error-prone DNA repair pathways.
    Boulton SJ, Jackson SP. (1996), DOI10.1002/j.1460-2075.1996.tb00890.x. The complete
    native abstract was read; no unlisted body scope is implied.'
  snapshot_sha256: 4ad8b0a177fd3e4a2514b8d64cd5608eda5ef3a90f35c38b7416bca9e27c909c
- evidence_id: micro58-pmid-8910371
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8910371+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED result: exact PMID, title, authors, year, DOI and complete
    abstractText when present.'
  accessed_at: '2026-10-22T07:38:55.781185Z'
  support: supports
  summary: 'PMID8910371: HDF2, the second subunit of the Ku homologue from Saccharomyces
    cerevisiae. Feldmann H, Driller L, Meier B, Mages G, Kellermann J, Winnacker EL.
    (1996), DOI10.1074/jbc.271.44.27765. The complete native abstract was read; no
    unlisted body scope is implied.'
  snapshot_sha256: 858cb6ba0fdc936c7b423b59c767aaa2b900e43d29418931fc3458222ac25c5d
- evidence_id: micro58-pmid-8972848
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8972848+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED result: exact PMID, title, authors, year, DOI and complete
    abstractText when present.'
  accessed_at: '2026-10-22T07:38:56.059489Z'
  support: supports
  summary: 'PMID8972848: Identification of a Saccharomyces cerevisiae Ku80 homologue:
    roles in DNA double strand break rejoining and in telomeric maintenance. Boulton
    SJ, Jackson SP. (1996), DOI10.1093/nar/24.23.4639. The complete native abstract
    was read; no unlisted body scope is implied.'
  snapshot_sha256: a3d57452587332d2f6f1d15790f58b46339cfe34c288971193c6d90e50852d45
- evidence_id: micro58-pmid-9635192
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9635192+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique MED result: exact PMID, title, authors, year, DOI and complete
    abstractText when present.'
  accessed_at: '2026-10-22T07:38:56.075342Z'
  support: supports
  summary: 'PMID9635192: Mutation of yeast Ku genes disrupts the subnuclear organization
    of telomeres. Laroche T, Martin SG, Gotta M, Gorham HC, Pryde FE, Louis EJ, Gasser
    SM. (1998), DOI10.1016/s0960-9822(98)70252-0. The complete native abstract was
    read; no unlisted body scope is implied.'
  snapshot_sha256: 8f5adb6649536597e1ce7462bc558429bf2db6391cd420b3cae61c0c14e80de2
- evidence_id: micro58-protein-P32807
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32807.json
  locator: Native identity/status/names, genes, organism/taxonId; complete FUNCTION,
    SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments and relevant InterPro cross-references.
  accessed_at: '2026-10-22T07:38:48.989680Z'
  support: supports
  summary: Reviewed P32807 identifies YKU70 in taxon559292; native names, gene aliases,
    organism, location and subunit comments match this maintained example. Native
    family cross-references provide separate corroboration of candidate class mappings.
    Unlisted annotation papers are not claimed as independently read.
  snapshot_sha256: 97b4ff0a59bb5294156d7eeb57199c772db366277ef994a179e5e733c0fe0a2c
- evidence_id: micro58-gene-YKU70
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYKU70%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set; actual gene_exact, organism_id and reviewed:true
    query preserved in original URL.
  accessed_at: '2026-10-22T07:39:01.497122Z'
  support: supports
  summary: The exact reviewed YKU70 query returns one entry, P32807, with matching
    primary gene or declared synonym and exact organism.
  snapshot_sha256: 56193c1470cfac0d0b5ffd1aad8cad276cbce4e55ffef0eb1b8f1e0c32c7b2e1
- evidence_id: micro58-protein-Q04437
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04437.json
  locator: Native identity/status/names, genes, organism/taxonId; complete FUNCTION,
    SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments and relevant InterPro cross-references.
  accessed_at: '2026-10-22T07:38:51.292224Z'
  support: supports
  summary: Reviewed Q04437 identifies YKU80 in taxon559292; native names, gene aliases,
    organism, location and subunit comments match this maintained example. Native
    family cross-references provide separate corroboration of candidate class mappings.
    Unlisted annotation papers are not claimed as independently read.
  snapshot_sha256: 6b53c3dac8841bccdd6fd94d179ad85217e17dd85f06a419c0cfb5ec5ebadcd3
- evidence_id: micro58-gene-YKU80
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AYKU80%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set; actual gene_exact, organism_id and reviewed:true
    query preserved in original URL.
  accessed_at: '2026-10-22T07:39:01.705981Z'
  support: supports
  summary: The exact reviewed YKU80 query returns one entry, Q04437, with matching
    primary gene or declared synonym and exact organism.
  snapshot_sha256: cedf3624a19a6ba4a5bf2f8252edf337727515ab84978260ce94b60948ef9d31
- evidence_id: micro58-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000444,GO:0000776,GO:0000817,GO:0006303,GO:0007059,GO:0031262,GO:0043564,GO:0045027,GO:0062051,GO:0140513,GO:1990351
  locator: Only these four exact entries, definitions/synonyms and typed links in
    the combined response.
  accessed_at: '2026-10-22T07:38:46.369929Z'
  support: supports
  summary: GO0043564 is the Ku70:Ku80 heterodimer; GO0140513 is the nuclear protein-containing-complex
    parent. GO0045027 and GO0006303 identify DNA-end binding and NHEJ. Generic Ku
    definitions cover several organism-dependent functions and do not establish yeast
    V(D)J recombination or DNA-PK activation.
  snapshot_sha256: 250f8bb7ef6c3e14e15534276b68530200b6490913906399353bb07481b31f71
- evidence_id: micro58-GO0043564-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043564/ancestors?relations=is_a
  locator: Complete exact-target relations=is_a array.
  accessed_at: '2026-10-22T07:38:46.370477Z'
  support: supports
  summary: The is_a-only ancestor array includes nuclear protein-containing complex
    GO0140513 and protein-containing complex GO0032991.
  snapshot_sha256: e1e7c030bfc18631a6490f9871801204f800d42102f2268664e61baa47f5bd2c
- evidence_id: micro58-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T07:38:47.039448Z'
  support: supports
  summary: ENA4932 identifies Saccharomyces cerevisiae species.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro58-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Native taxId, scientificName, rank, lineage and relevant equivalent names.
  accessed_at: '2026-10-22T07:38:47.039624Z'
  support: supports
  summary: ENA559292 identifies S288C, the reviewed reference-protein strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro58-koike2002-jstage-pdf
  kind: authority
  reference: https://www.jstage.jst.go.jp/article/jrr/43/3/43_3_223/_pdf
  locator: 'Genuine J-STAGE PDF: printed pp223–227, complete Abstract/Introduction,
    chromosome-location section and dimerization section through its end at the start
    of p228. Remaining p228 onward and figure pixels not read.'
  accessed_at: '2026-10-22T07:41:28.269336Z'
  support: supports
  summary: The secondary review describes the two-subunit channel, broad Ku functions,
    mammalian heterodimer stability and organism-specific NHEJ differences. It explicitly
    notes no obvious DNA-PKcs homologue in yeast; mammalian V(D)J and DNA-PK context
    is not assigned to the yeast graph.
  snapshot_sha256: 4ac70fb22c4df72963efa4f74a797e65fcc2bcc3626ca36c9faee7d44177ac54
- evidence_id: micro58-IPR006165
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006165/
  locator: Complete native family type/name/description/member signatures; accession
    membership is separately supplied by the protein evidence.
  accessed_at: '2026-10-22T07:39:41.334620Z'
  support: supports
  summary: IPR006165 is the whole Ku70 family, with Ku70-specific PIRSF003033 and
    TIGR00578 signatures. Its identity is distinct from the shared Ku70/Ku80 domain.
  snapshot_sha256: 468a80293945de05f280632f853a4bc5c60988ebb0cf696fc8be32e28efd2248
- evidence_id: micro58-IPR024193
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024193/
  locator: Complete native family type/name/description/member signatures; accession
    membership is separately supplied by the protein evidence.
  accessed_at: '2026-10-22T07:39:41.334866Z'
  support: supports
  summary: IPR024193 is the Ku80 family with Ku80-specific PIRSF016570 and cd00873
    signatures. General evolutionary background about prokaryotic Ku is not substituted
    for this eukaryotic subunit class.
  snapshot_sha256: 19728344223f897e6e0aa282f7a6e65bd36d9ad49e90fdbc9e72ee4590a3c6ac
- evidence_id: micro58-IPR006164
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR006164/
  locator: Complete native type/name/description and member signatures.
  accessed_at: '2026-10-22T07:39:41.335126Z'
  support: context_only
  summary: IPR006164 is the shared Ku70/Ku80 DNA-binding domain and is not an exact
    replacement for either whole subunit class.
  snapshot_sha256: 37767860040074bdb317cccb96a77d53a34eb4bec030215c8da1fd34e9d889d0
- evidence_id: micro58-PMC146307-legacy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC146307/
  locator: Actual retained status/body diagnostic and original receipt.
  accessed_at: '2026-10-22T07:40:11.789749Z'
  support: context_only
  summary: The retained HTTP200 legacy response is a browser-check challenge, not
    the Boulton Ku80 main body.
  snapshot_sha256: 23a88ed17b8924b06b1aa09297a6bc80ec9860287a84c67b9c1fd5c285367901
- evidence_id: micro58-feldmann1996-publisher-html
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0021925818352992
  locator: Actual retained status/body diagnostic and original receipt.
  accessed_at: '2026-10-22T07:41:28.162364Z'
  support: context_only
  summary: The ScienceDirect route returned403 and an error page, not the Feldmann
    main body.
  snapshot_sha256: e11a834745d1c85b7a586974bbf9a45fe612ce8118422eb2ada5d26736ddc865
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/ku70_ku80_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:34:49Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/ku70_ku80_complex.yaml'
  snapshot_sha256: 0219fe09b5edd23e95d0b4742faf4e5e18ac990d6dc4d47ce5c3268a05dba4c8
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/ku70_ku80_complex.yaml --out
    /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/ku70_ku80_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:34:49Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/ku70_ku80_complex.yaml\
    \ --out /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/ku70_ku80_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/ku70_ku80_complex-strict.tsv"
  snapshot_sha256: c87f103ed56724e9395946052763212de73085743ae0d5fad97205afed53602d
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml
    --causal-graphs
  locator: Complete focused read-only native report
  accessed_at: '2026-10-22T07:39:23.228663Z'
  support: supports
  summary: "data/structures/other/ku70_ku80_complex.yaml  (GO:0043564)\n  ku70_ku80_dna_end_joining\t\
    ku70_subunit\tCOVERED\t->ku70_subunit (UniProtKB:P32807)\n  ku70_ku80_dna_end_joining\t\
    ku80_subunit\tCOVERED\t->ku80_subunit (UniProtKB:Q04437)\n\ncausal_graphs GENE_OR_PROTEIN\
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
  snapshot_sha256: 8298d3326981375e22726968929f402596c518105adec5b93042793f0569ec3f
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch58-20261022-e3d8mlk1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/ku70_ku80_complex.yaml
    --verify
  locator: Complete focused read-only native report
  accessed_at: '2026-10-22T07:39:24.292499Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/ku70_ku80_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '12 of 18 collected target identifiers returned OK. PMID:12518983: UNREACHABLE;
    Native Europe PMC uniquely identifies MED12518983: Dimerization, translocation
    and localization of Ku70 and Ku80 proteins. (2002); DOI 10.1269/jrr.43.223. This
    resolves the identifier transport residual only; primary-source reading remains
    separately scoped.; PMID:15122350: UNREACHABLE; Native Europe PMC uniquely identifies
    MED15122350: A means to a DNA end: the many roles of Ku. (2004); DOI 10.1038/nrm1367.
    This resolves the identifier transport residual only; primary-source reading remains
    separately scoped.; PMID:8890183: UNREACHABLE; Native Europe PMC uniquely identifies
    MED8890183: Saccharomyces cerevisiae Ku70 potentiates illegitimate DNA double-strand
    break repair and serves as a barrier to error-prone DNA repair pathways. (1996);
    DOI 10.1002/j.1460-2075.1996.tb00890.x. This resolves the identifier transport
    residual only; primary-source reading remains separately scoped.; PMID:8910371:
    UNREACHABLE; Native Europe PMC uniquely identifies MED8910371: HDF2, the second
    subunit of the Ku homologue from Saccharomyces cerevisiae. (1996); DOI 10.1074/jbc.271.44.27765.
    This resolves the identifier transport residual only; primary-source reading remains
    separately scoped.; PMID:8972848: UNREACHABLE; Native Europe PMC uniquely identifies
    MED8972848: Identification of a Saccharomyces cerevisiae Ku80 homologue: roles
    in DNA double strand break rejoining and in telomeric maintenance. (1996); DOI
    10.1093/nar/24.23.4639. This resolves the identifier transport residual only;
    primary-source reading remains separately scoped.; PMID:9635192: UNREACHABLE;
    Native Europe PMC uniquely identifies MED9635192: Mutation of yeast Ku genes disrupts
    the subnuclear organization of telomeres. (1998); DOI 10.1016/s0960-9822(98)70252-0.
    This resolves the identifier transport residual only; primary-source reading remains
    separately scoped. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
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
  topic: Exact heterodimer and nuclear-complex parent
  outcome: supported
  target_ids:
  - GO:0043564
  summary: The class is Ku70:Ku80 rather than DNA-PK or a prokaryotic Ku homodimer.
    The generic channel/function definition is supported at review/ontology level,
    with organism-specific functions not automatically exported to the yeast example.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro58-go
  - micro58-GO0043564-ancestors
  - micro58-koike2002-jstage-pdf
- assessment_id: grounding
  area: grounding
  topic: Both named whole subunit classes have exact families
  outcome: concern
  target_ids:
  - GO:0043564
  summary: Reviewed yeast YKU70/P32807 and YKU80/Q04437 identities agree with their
    exact queries and independently verified family cross-references. IPR006165 and
    IPR024193 fit the two classes; IPR006164 is only the shared domain.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro58-IPR006165
  - micro58-IPR024193
  - micro58-IPR006164
  - micro58-protein-P32807
  - micro58-protein-Q04437
  - micro58-gene-YKU70
  - micro58-gene-YKU80
- assessment_id: formation
  area: evidence
  topic: Unknown necessity is not replaced by repair essentiality
  outcome: unknown
  target_ids:
  - GO:0043564
  summary: Yeast abstracts establish DNA-binding/rejoining phenotypes and HDF2 identity,
    while the secondary review discusses heterodimer stability in mammalian cells.
    These are not a universal yeast loss-of-subunit formation test. Existing UNKNOWN
    essentiality remains appropriate.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro58-koike2002-jstage-pdf
  - micro58-pmid-12518983
  - micro58-pmid-15122350
  - micro58-pmid-8890183
  - micro58-pmid-8910371
  - micro58-pmid-8972848
  - micro58-pmid-9635192
- assessment_id: scope
  area: scope
  topic: Yeast reference identity and source access are distinct
  outcome: supported
  target_ids:
  - GO:0043564
  summary: COMMON preserves majority occurrence with exceptional losses; the inspected
    literature provides qualitative yeast context rather than a census. S288C reference
    accessions are correct. Feldmann and Boulton yeast primary claims were checked
    at complete native abstract tier, not a falsely claimed full body.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro58-tax4932
  - micro58-tax559292
  - micro58-pmid-12518983
  - micro58-pmid-15122350
  - micro58-pmid-8890183
  - micro58-pmid-8910371
  - micro58-pmid-8972848
  - micro58-pmid-9635192
  - micro58-protein-P32807
  - micro58-protein-Q04437
  - micro58-gene-YKU70
  - micro58-gene-YKU80
  - micro58-PMC146307-legacy
  - micro58-feldmann1996-publisher-html
- assessment_id: graph
  area: graph
  topic: Bounded nonmechanistic DNA-end recognition and repair
  outcome: supported
  target_ids:
  - GO:0043564
  summary: The NON_MECHANISTIC graph expresses Ku subunit participation, DNA-end association
    and NHEJ support. It expressly leaves detailed mammalian DNA-PK regulation and
    other interactions unresolved, so no yeast V(D)J/DNA-PK mechanism is inferred.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro58-go
  - micro58-koike2002-jstage-pdf
  - micro58-pmid-12518983
  - micro58-pmid-15122350
  - micro58-pmid-8890183
  - micro58-pmid-8910371
  - micro58-pmid-8972848
  - micro58-pmid-9635192
  - micro58-protein-P32807
  - micro58-protein-Q04437
- assessment_id: coverage
  area: completeness
  topic: Entire target with bounded positive evidence
  outcome: supported
  target_ids:
  - GO:0043564
  summary: All scientific fields, examples, citations, graphs, discussions and history
    were read. Existing protein examples were checked directly; no empty optional
    slot alone is treated as an error. Source tiers and actual reading extents are
    explicit.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro58-go
  - micro58-GO0043564-ancestors
  - micro58-koike2002-jstage-pdf
  - micro58-IPR006165
  - micro58-IPR024193
  - micro58-IPR006164
  - micro58-tax4932
  - micro58-tax559292
  - micro58-pmid-12518983
  - micro58-pmid-15122350
  - micro58-pmid-8890183
  - micro58-pmid-8910371
  - micro58-pmid-8972848
  - micro58-pmid-9635192
  - micro58-protein-P32807
  - micro58-protein-Q04437
  - micro58-gene-YKU70
  - micro58-gene-YKU80
  - micro58-PMC146307-legacy
  - micro58-feldmann1996-publisher-html
findings:
- finding_id: F1
  issue_key: ku70-ku80-exact-subunit-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the two Ku subunit classes
  description: Ku70/Yku70 and Ku80/Yku80 remain REVIEWED_LABEL_ONLY despite exact
    whole-family identities IPR006165 and IPR024193. Native family types/signatures
    and separately verified yeast protein cross-references corroborate both mappings.
  target_ids:
  - GO:0043564
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - components[1].grounding_status
  - components[1].grounding_notes
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro58-IPR006165
  - micro58-IPR024193
  - micro58-IPR006164
  - micro58-protein-P32807
  - micro58-protein-Q04437
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ku70_ku80_complex.yaml
    role: maintained scientific record
  rule_id: Exact source support and current component-class grounding
  native_severity: minor
  normalization_reason: One grouped minor grounding gap with correct membership, accessions
    and biological roles already present. Neither a generic domain nor an organism-specific
    gene identifier is substituted for the class.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0043564
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ku70_ku80_complex.yaml
    role: maintained scientific record
  description: Ground Ku70 to IPR006165 and Ku80 to IPR024193, retaining yeast roles,
    examples and UNKNOWN assembly necessity.
  acceptance_checks:
  - Each mapping identifies the correct whole subunit family.
  - Shared Ku domain IPR006164 is not used as an exact whole-subunit identity.
  - Native schema, strict and CURIE checks pass after separately authorized curation.
limitations:
- Koike is a secondary review and was read only in the specified pp223–228 extent.
  Boulton/Feldmann and Laroche primary claims were inspected at complete native abstract
  tier; no inaccessible main body or figure pixels are certified.
- The retained Downs2004 MED record contains no abstractText, so it resolves bibliography
  only. A DOI content-negotiation response is bibliographic JSON, not a publisher
  main body.
- Mammalian V(D)J, DNA-PK and stability contexts are not equated with yeast mechanisms.
  Approximate70/80kDa class names are not claims of directly measured invariant yeast
  masses.
- COMMON retains its majority meaning; no population census or universal formation
  requirement is inferred.
- All reused source bytes preserve their original URL, UTC and SHA256. Readability
  is established from content rather than HTTP200 alone.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requests one review for every unreviewed record, including qualified
  clean cases.
- No maintained scientific record, historical review or initial native inspection
  snapshot is edited.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
