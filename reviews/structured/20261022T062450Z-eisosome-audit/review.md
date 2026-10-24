# Source-backed review of eisosome

- Review: 20261022T062450Z-eisosome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:03:34Z
- Finished UTC: 2026-10-22T06:24:50Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: paired eisosome identity, Pil1/Lsp1 scaffold, Sur7 localization and coarse assembly graph are supported. Exact Sur7-only grounding, prevalence and universal formation necessity remain bounded.

## Scope And Provenance

Exactly one complete maintained target with frozen governing/schema/protein/graph guidance. All current scientific assertions were assessed at the declared independently read source tiers; no neighboring maintained record is an unstated premise.

Selection: Batch53 strict ordered selection, index 4; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032126 | data/structures/other/eisosome.yaml | maintained | eisosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032126 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032126 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0032126 | Focused check passed; scientific scope independently assessed. |
| Focused native verify | passed | True | GO:0032126 | Focused check passed; scientific scope independently assessed. |
| Claim-level scientific review | passed | True | GO:0032126 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0032126 | 14 of 19 collected target identifiers returned OK. PMID:11784867: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:12469340: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:16496001: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:25002088: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0032126 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032126 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032126 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032126 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0032126 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Paired membrane-and-scaffold identity

identity: supported. Targets: GO:0032126.

The definition and two has_part terms match native GO. The whole eisosome is not conflated with only its cytoplasmic protein lattice or only MCC membrane.

### Pil1/Lsp1 and Sur7 constituent scope

grounding: supported. Targets: GO:0032126.

The grouped core has exact IPR028245 grounding and verified examples. Sur7 localization is direct; broad IPR009571/PalI-family and unchecked PANTHER metadata do not resolve a Sur7-only match. The existing open exact-grounding task remains bounded rather than a confirmed omission.

### Membrane-domain organization

evidence: supported. Targets: GO:0032126.

The named organization function and canonical S.cerevisiae example agree with the primary scaffold/localization results. The older endocytosis title is not treated as proof that eisosomes universally initiate endocytosis. Moreira and Douglas are assessed at complete-abstract tier only.

### Fungal variability and experimental systems

scope: supported. Targets: GO:0032126.

Fungi VARIABLE is compatible with a non-universal named fungal structure and a directly supported S.cerevisiae example. The W303/S288C-derived yeast work, recombinant E.coli expression and COS7 overexpression are kept distinct; no fungal prevalence census is claimed.

### Supported coarse assembly account

graph: supported. Targets: GO:0032126.

The three edges distinguish Pil1/Lsp1 assembly, membrane scaffolding and Sur7 localization. Direct in-vitro assembly/membrane deformation plus yeast perturbation and in-situ organization support the coarse MECHANISTIC account; it does not assert a complete kinetic pathway or identical structures in every assay.

### Formation necessity not overstated

evidence: unknown. Targets: GO:0032126.

Component essentiality is unset. Localization, filament formation and mutant spatial phenotypes are not converted into universal formation necessity for every grouped protein; no unsupported ESSENTIAL label is present.

### Exact protein examples and annotation placement

grounding: supported. Targets: GO:0032126.

All current accessions, declared genes, reviewed status and S288C pairs match native identities and bounded single-hit queries. Location citations/ECO annotations agree where present; localization is not promoted to physical complex membership.

### Complete target with explicit unresolved scope

completeness: supported. Targets: GO:0032126.

All scientific fields, source placements, annotations, graph edges, discussions and history were reviewed. Historical first-pass statements are not declared false merely because current access improves. Optional inventories and unverified exact mappings remain bounded limitations; no concrete required correction was established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/eisosome.yaml; Entire current YAML, including all annotations, graph edges, discussions and history | context_only | The complete target was read; no neighboring maintained record supplies an unstated scientific premise. |
| curation | docs/CURATION.md; Component-class grounding, examples and formation necessity | context_only | Named components and example accessions are distinct from exact source-neutral family classes. Formation necessity is separate from activity, localization and viability. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum | context_only | UNKNOWN or unset essentiality does not assert a demonstrated formation requirement. COMMON means present in most members, with exceptional losses; VARIABLE does not assert universal occurrence. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph scope, typed nodes and edge-level source support | context_only | Mechanistic classification requires a supported causal account; descriptive membership/function graphs may be NONMECHANISTIC. |
| micro53-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126,GO:0036286,GO:0090512,GO:0043231,GO:0031391,GO:0032991,GO:0061860; Seven-term native response; exact target/parent/function entries, definitions, synonyms, source xrefs and relevant typed children only. | supports | Active GO0032126 identifies the paired MCC membrane domain and cytoplasmic filament scaffold. Its typed part_of children are GO0090512 and GO0036286; their native definitions distinguish the membrane and filament classes. |
| micro53-GO0032126-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126/ancestors?relations=is_a; Complete ancestors array from the actual relations=is_a URL. | supports | The exact is_a-only array confirms cellular-anatomical-entity ancestry for eisosome; it is not a protein-complex-only class. |
| micro53-tax4751 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751; Complete taxId/scientificName/rank/lineage/otherNames response. | supports | ENA taxId4751 identifies Fungi, rank kingdom. Reference strain and experimental culture identity remain separate. |
| micro53-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId/scientificName/rank/lineage/otherNames response. | supports | ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Reference strain and experimental culture identity remain separate. |
| micro53-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId/scientificName/rank/lineage/otherNames response. | supports | ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain. Reference strain and experimental culture identity remain separate. |
| micro53-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID14562095: Global analysis of protein localization in budding yeast. Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003), DOI10.1038/nature02026. Bibliographic identity and complete native abstract were read. |
| micro53-pmid-16496001 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16496001%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID16496001: Eisosomes mark static sites of endocytosis. Walther TC, Brickner JH, Aguilar PS, Bernales S, Pantoja C, Walter P. (2006), DOI10.1038/nature04472. Bibliographic identity and complete native abstract were read. |
| micro53-pmid-11784867 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11784867%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID11784867: The Sur7p family defines novel cortical domains in Saccharomyces cerevisiae, affects sphingolipid metabolism, and is involved in sporulation. Young ME, Karpova TS, Brügger B, Moschenross DM, Wang GK, Schneiter R, Wieland FT, Cooper JA. (2002), DOI10.1128/mcb.22.3.927-934.2002. Bibliographic identity and complete native abstract were read. |
| micro53-pmid-12469340 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12469340%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID12469340: Subproteomics: identification of plasma membrane proteins from the yeast Saccharomyces cerevisiae. Navarre C, Degand H, Bennett KL, Crawford JS, Mørtz E, Boutry M. (2002), DOI10.1002/1615-9861(200212)2:12&lt;1706::aid-prot1706&gt;3.0.co;2-k. Bibliographic identity and complete native abstract were read. |
| micro53-pmid-25002088 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25002088%20AND%20SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText. Body reading, where available, is separately scoped. | supports | PMID25002088: Fungal membrane organization: the eisosome concept. Douglas LM, Konopka JB. (2014), DOI10.1146/annurev-micro-091313-103507. Bibliographic identity and complete native abstract were read. This is secondary synthesis, not a primary experiment. |
| micro53-protein-P53252 | https://rest.uniprot.org/uniprotkb/P53252.json; Primary accession/status, recommended name, gene/taxon; full relevant comments and InterPro/PANTHER cross-references. | supports | Reviewed P53252 identifies PIL1 in S.cerevisiae S288C taxon559292. Exact identity, gene, relevant FUNCTION/SUBUNIT/SIMILARITY/location comments and family cross-references were inspected. The maintained Huh lipid-droplet annotation is present; that location alone is not eisosome membership. |
| micro53-gene-PIL1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APIL1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set; actual query uses gene_exact:PIL1, organism_id:559292 and reviewed:true. | supports | The bounded reviewed exact-PIL1 query returns the single P53252 entry at taxon559292. |
| micro53-protein-Q12230 | https://rest.uniprot.org/uniprotkb/Q12230.json; Primary accession/status, recommended name, gene/taxon; full relevant comments and InterPro/PANTHER cross-references. | supports | Reviewed Q12230 identifies LSP1 in S.cerevisiae S288C taxon559292. Exact identity, gene, relevant FUNCTION/SUBUNIT/SIMILARITY/location comments and family cross-references were inspected. The maintained cell-cortex annotations cite Huh and Walther as stated. |
| micro53-gene-LSP1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ALSP1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set; actual query uses gene_exact:LSP1, organism_id:559292 and reviewed:true. | supports | The bounded reviewed exact-LSP1 query returns the single Q12230 entry at taxon559292. |
| micro53-protein-P54003 | https://rest.uniprot.org/uniprotkb/P54003.json; Primary accession/status, recommended name, gene/taxon; full relevant comments and InterPro/PANTHER cross-references. | supports | Reviewed P54003 identifies SUR7 in S.cerevisiae S288C taxon559292. Exact identity, gene, relevant FUNCTION/SUBUNIT/SIMILARITY/location comments and family cross-references were inspected. Maintained membrane/cortex provenance matches Young, Navarre and Walther; broad Sur7/Rim9 family membership does not establish a Sur7-only class. |
| micro53-gene-SUR7 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUR7%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set; actual query uses gene_exact:SUR7, organism_id:559292 and reviewed:true. | supports | The bounded reviewed exact-SUR7 query returns the single P54003 entry at taxon559292. |
| micro53-ipr-IPR028245 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028245/; Complete native family name/type/description/member signatures; separate reviewed proteins corroborate membership. | supports | IPR028245 is a whole-protein Pil1/Lsp1 family, integrated with PF13805 and PTHR31962. It fits the grouped component; its historical endocytosis background is not used to replace the record's membrane-organization function. |
| micro53-family-IPR009571 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009571/; Complete name/type/description and member-signature metadata. | supports | IPR009571 and its PF06687 member cover Sur7, Rim9 and PalI. This broader fungal membrane-protein family is not demonstrated to be an exact match for the named Sur7-only component. |
| micro53-sur7-panther | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR36414/; Complete source-family metadata, integration and generated-text flags; no mechanistic claim is adopted. | context_only | The unintegrated PTHR36414 family is named SUR7 domain-containing protein; its generated description is unchecked. This alone does not resolve an exact allowable Sur7-only class or justify changing the component. |
| micro53-sur7-subfamily | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR36414:SF1/; Retained native request/response receipt; bounded access limitation. | context_only | The candidate subfamily endpoint returned HTTP204 with an empty body. No exact subfamily identity is established from this response. |
| micro53-walther2006-publisher | https://www.nature.com/articles/nature04472; Genuine publisher main HTML, derived paragraph indices7,9–13,17,36: abstract, composition/localization, perturbation and immunopurification Methods. No figure pixels or supplements. | supports | Walther directly supports Pil1/Lsp1 assemblies and Sur7 colocalization in budding yeast. Pil1 deletion disrupts the spatial pattern; Lsp1 or Sur7 perturbations are not equivalent universal formation tests. |
| micro53-olivera-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3128537/; Genuine PMC3128537 HTML: sec4–6, sec9, sec13, sec17–18 and embedded Figure2–5 captions. No pixels or supplemental alignments/assays. | supports | Olivera-Couto directly tests Pil1/Lsp1 lipid binding, membrane tubulation and Pil1 mutant effects on yeast eisosome/MCC organization. Recombinant liposome and heterologous COS7 experiments remain distinct from yeast structures. |
| micro53-karotki | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3257569/fullTextXML; Genuine PMC3257569 JATS: sec3/5/6/9/11 and Methods sec14/15/17/19/20; embedded Figure1–3/6–7 captions. No raw pixels, supplemental images or independent structural reanalysis. | supports | Karotki demonstrates recombinant filament assembly, membrane association and in-situ Pil1/Lsp1-coated furrows. In-vitro closed tubes are distinguished from the half-cylinder-like in-situ scaffold. |
| micro53-moreira | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.e08-03-0313&amp;format=json&amp;resultType=core; Unique native MED bibliographic entry and complete abstractText. | supports | PMID19037108: Pil1 controls eisosome biogenesis. DOI10.1091/mbc.e08-03-0313. Complete native abstract and identity read; Moreira is used only at this tier. |
| micro53-olivera | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.e10-12-1021&amp;format=json&amp;resultType=core; Unique native MED bibliographic entry and complete abstractText. | supports | PMID21593205: The eisosome core is composed of BAR domain proteins. DOI10.1091/mbc.e10-12-1021. Complete native abstract and identity read; Moreira is used only at this tier. |
| micro53-karotki-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1083%2Fjcb.201104040&amp;format=json&amp;resultType=core; Unique native MED bibliographic entry and complete abstractText. | supports | PMID22123866: Eisosome proteins assemble into a membrane scaffold. DOI10.1083/jcb.201104040. Complete native abstract and identity read; Moreira is used only at this tier. |
| micro53-douglas2014-publisher | https://www.annualreviews.org/content/journals/10.1146/annurev-micro-091313-103507; Original403 access receipt and challenge HTML; no body support inferred. | context_only | The retained publisher response is HTTP403, not the Douglas review body. The native MED abstract supplies the independently read secondary tier. |
| schema-result | just validate data/structures/other/eisosome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/eisosome.yaml |
| strict-result | just validate-strict data/structures/other/eisosome.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/eisosome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/eisosome.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/eisosome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch53-20261022-kx679dvh/eisosome-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/eisosome.yaml --causal-graphs; Complete focused native read-only report | supports | data/structures/other/eisosome.yaml  (GO:0032126)<br>  pil1_lsp1_eisosome_scaffold	pil1_lsp1_bar_core	COVERED	-&gt;pil1_lsp1_bar_core (UniProtKB:P53252, UniProtKB:Q12230)<br>  pil1_lsp1_eisosome_scaffold	sur7_membrane_protein	COVERED	-&gt;sur7_membrane_protein (UniProtKB:P54003)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/eisosome.yaml --verify; Complete focused native read-only report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/eisosome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 19 collected target identifiers returned OK. PMID:11784867: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:12469340: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:16496001: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:25002088: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Walther is read at main paragraphs7/9–13/17/36; Olivera and Karotki at the exact sections/captions listed. No primary figure pixels or supplements were inspected. Moreira/Douglas and Young/Navarre/Huh annotation studies are used at complete-native-abstract tier only; the retained Young full body was not independently used here.
- Broad Sur7/Rim9/PalI family membership and unchecked PANTHER prose do not prove an exact Sur7-only class. Additional Nce102/resident inventory and a fungal prevalence census remain unestablished optional enrichment.
- The current experiment-specific assembly account is supported, but it is not an exhaustive native maturation pathway or proof of universal per-protein formation necessity.
- Original source URLs, UTC timestamps and raw SHA256 are retained for reused sources; HTTP success does not imply article readability.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user requests one review for every unreviewed record, including qualified clean records.
- Native ontology, taxonomy and protein/family sources directly address the present claims. No expression-module dataset is asserted to establish physical structure membership.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T062450Z-eisosome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of eisosome
started_at: '2026-10-22T06:03:34Z'
finished_at: '2026-10-22T06:24:50Z'
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
summary: 'Qualified pass: paired eisosome identity, Pil1/Lsp1 scaffold, Sur7 localization
  and coarse assembly graph are supported. Exact Sur7-only grounding, prevalence and
  universal formation necessity remain bounded.'
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
  - path: data/structures/other/eisosome.yaml
    sha256: 032c3bd7a0cc1b125515740752e69d06e4b8bf20529cad61cd62b9559e4f0b72
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
- target_id: GO:0032126
  path: data/structures/other/eisosome.yaml
  label: eisosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/eisosome.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target with frozen governing/schema/protein/graph
    guidance. All current scientific assertions were assessed at the declared independently
    read source tiers; no neighboring maintained record is an unstated premise.
  selection: Batch53 strict ordered selection, index 4; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032126
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032126
  command: just validate data/structures/other/eisosome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032126
  command: just validate-strict data/structures/other/eisosome.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/eisosome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0032126
  command: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/eisosome.yaml --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific scope independently assessed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0032126
  command: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/eisosome.yaml --verify
  exit_code: 0
  summary: Focused check passed; scientific scope independently assessed.
  evidence_ids:
  - native-verify
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032126
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - curation
  - schema
  - graphs
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - micro53-pmid-14562095
  - micro53-pmid-16496001
  - micro53-pmid-11784867
  - micro53-pmid-12469340
  - micro53-pmid-25002088
  - micro53-protein-P53252
  - micro53-gene-PIL1
  - micro53-protein-Q12230
  - micro53-gene-LSP1
  - micro53-protein-P54003
  - micro53-gene-SUR7
  - micro53-ipr-IPR028245
  - micro53-family-IPR009571
  - micro53-sur7-panther
  - micro53-sur7-subfamily
  - micro53-walther2006-publisher
  - micro53-olivera-legacy
  - micro53-karotki
  - micro53-moreira
  - micro53-olivera
  - micro53-karotki-meta
  - micro53-douglas2014-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0032126
  summary: '14 of 19 collected target identifiers returned OK. PMID:11784867: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:12469340: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:16496001: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:25002088: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - micro53-pmid-11784867
  - micro53-pmid-12469340
  - micro53-pmid-14562095
  - micro53-pmid-16496001
  - micro53-pmid-25002088
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032126
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
  - GO:0032126
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
  - GO:0032126
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
  - GO:0032126
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
  - GO:0032126
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
  reference: data/structures/other/eisosome.yaml
  locator: Entire current YAML, including all annotations, graph edges, discussions
    and history
  accessed_at: '2026-10-22T06:15:31Z'
  support: context_only
  summary: The complete target was read; no neighboring maintained record supplies
    an unstated scientific premise.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component-class grounding, examples and formation necessity
  accessed_at: '2026-10-22T06:15:31Z'
  support: context_only
  summary: Named components and example accessions are distinct from exact source-neutral
    family classes. Formation necessity is separate from activity, localization and
    viability.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentGroundingStatusEnum; EssentialityEnum; PresenceEnum
  accessed_at: '2026-10-22T06:15:31Z'
  support: context_only
  summary: UNKNOWN or unset essentiality does not assert a demonstrated formation
    requirement. COMMON means present in most members, with exceptional losses; VARIABLE
    does not assert universal occurrence.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph scope, typed nodes and edge-level source support
  accessed_at: '2026-10-22T06:15:31Z'
  support: context_only
  summary: Mechanistic classification requires a supported causal account; descriptive
    membership/function graphs may be NONMECHANISTIC.
- evidence_id: micro53-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126,GO:0036286,GO:0090512,GO:0043231,GO:0031391,GO:0032991,GO:0061860
  locator: Seven-term native response; exact target/parent/function entries, definitions,
    synonyms, source xrefs and relevant typed children only.
  accessed_at: '2026-10-22T06:08:07.194290Z'
  support: supports
  summary: Active GO0032126 identifies the paired MCC membrane domain and cytoplasmic
    filament scaffold. Its typed part_of children are GO0090512 and GO0036286; their
    native definitions distinguish the membrane and filament classes.
  snapshot_sha256: 795f3880adcbdcfb4852e1c8b5d698cbbdd455db85af41abd1ba2dd5e4a034c9
- evidence_id: micro53-GO0032126-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0032126/ancestors?relations=is_a
  locator: Complete ancestors array from the actual relations=is_a URL.
  accessed_at: '2026-10-22T06:08:07.194036Z'
  support: supports
  summary: The exact is_a-only array confirms cellular-anatomical-entity ancestry
    for eisosome; it is not a protein-complex-only class.
  snapshot_sha256: 71a47a7c125b2266f533e8683a5f8a6c058ff7e39e97a6cab86938678d538d14
- evidence_id: micro53-tax4751
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4751
  locator: Complete taxId/scientificName/rank/lineage/otherNames response.
  accessed_at: '2026-10-22T06:08:07.194533Z'
  support: supports
  summary: ENA taxId4751 identifies Fungi, rank kingdom. Reference strain and experimental
    culture identity remain separate.
  snapshot_sha256: a7bab59bce650c0d29732327d4e7e342f1b648747f7f9635958f923b4a6089e6
- evidence_id: micro53-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId/scientificName/rank/lineage/otherNames response.
  accessed_at: '2026-10-22T06:08:07.194562Z'
  support: supports
  summary: ENA taxId4932 identifies Saccharomyces cerevisiae, rank species. Reference
    strain and experimental culture identity remain separate.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro53-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId/scientificName/rank/lineage/otherNames response.
  accessed_at: '2026-10-22T06:08:08.381833Z'
  support: supports
  summary: ENA taxId559292 identifies Saccharomyces cerevisiae S288C, rank strain.
    Reference strain and experimental culture identity remain separate.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro53-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:08:10.226991Z'
  support: supports
  summary: 'PMID14562095: Global analysis of protein localization in budding yeast.
    Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK. (2003),
    DOI10.1038/nature02026. Bibliographic identity and complete native abstract were
    read.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: micro53-pmid-16496001
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16496001%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:08:10.291379Z'
  support: supports
  summary: 'PMID16496001: Eisosomes mark static sites of endocytosis. Walther TC,
    Brickner JH, Aguilar PS, Bernales S, Pantoja C, Walter P. (2006), DOI10.1038/nature04472.
    Bibliographic identity and complete native abstract were read.'
  snapshot_sha256: 2d2a92cd519ecc00654099e6b23ffa82a0fa23ce9a6a9ed48057abd74b09e61d
- evidence_id: micro53-pmid-11784867
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11784867%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:08:11.150106Z'
  support: supports
  summary: 'PMID11784867: The Sur7p family defines novel cortical domains in Saccharomyces
    cerevisiae, affects sphingolipid metabolism, and is involved in sporulation. Young
    ME, Karpova TS, Brügger B, Moschenross DM, Wang GK, Schneiter R, Wieland FT, Cooper
    JA. (2002), DOI10.1128/mcb.22.3.927-934.2002. Bibliographic identity and complete
    native abstract were read.'
  snapshot_sha256: 9804449f356c8e509cd0dbba58a0cf2dcf0519bbc28e5b4a649a954476410c64
- evidence_id: micro53-pmid-12469340
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12469340%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:08:11.295398Z'
  support: supports
  summary: 'PMID12469340: Subproteomics: identification of plasma membrane proteins
    from the yeast Saccharomyces cerevisiae. Navarre C, Degand H, Bennett KL, Crawford
    JS, Mørtz E, Boutry M. (2002), DOI10.1002/1615-9861(200212)2:12<1706::aid-prot1706>3.0.co;2-k.
    Bibliographic identity and complete native abstract were read.'
  snapshot_sha256: 1e42713179a86a7e310a9bb14bbf16879f4d9f2aef07aaedf94af3fb3c579397
- evidence_id: micro53-pmid-25002088
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A25002088%20AND%20SRC%3AMED&format=json&resultType=core
  locator: Unique MED entry; exact PMID/title/authors/year/DOI and complete abstractText.
    Body reading, where available, is separately scoped.
  accessed_at: '2026-10-22T06:08:11.417283Z'
  support: supports
  summary: 'PMID25002088: Fungal membrane organization: the eisosome concept. Douglas
    LM, Konopka JB. (2014), DOI10.1146/annurev-micro-091313-103507. Bibliographic
    identity and complete native abstract were read. This is secondary synthesis,
    not a primary experiment.'
  snapshot_sha256: 71ecfd6a977ea4cf9b0a84f6d66894714be936e2e3b070bf44dff7d6e2139e1f
- evidence_id: micro53-protein-P53252
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53252.json
  locator: Primary accession/status, recommended name, gene/taxon; full relevant comments
    and InterPro/PANTHER cross-references.
  accessed_at: '2026-10-22T06:08:08.393328Z'
  support: supports
  summary: Reviewed P53252 identifies PIL1 in S.cerevisiae S288C taxon559292. Exact
    identity, gene, relevant FUNCTION/SUBUNIT/SIMILARITY/location comments and family
    cross-references were inspected. The maintained Huh lipid-droplet annotation is
    present; that location alone is not eisosome membership.
  snapshot_sha256: f4f742a1eab8a34224819b63169967aac3323244aa49ccfb6fb6f258bd78e2de
- evidence_id: micro53-gene-PIL1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APIL1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set; actual query uses gene_exact:PIL1, organism_id:559292
    and reviewed:true.
  accessed_at: '2026-10-22T06:08:08.499108Z'
  support: supports
  summary: The bounded reviewed exact-PIL1 query returns the single P53252 entry at
    taxon559292.
  snapshot_sha256: 2d13418365ff6b7b41298917a401bbe0ed436ddc7563af8f13bc10c7d5722b2a
- evidence_id: micro53-protein-Q12230
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12230.json
  locator: Primary accession/status, recommended name, gene/taxon; full relevant comments
    and InterPro/PANTHER cross-references.
  accessed_at: '2026-10-22T06:08:09.043534Z'
  support: supports
  summary: Reviewed Q12230 identifies LSP1 in S.cerevisiae S288C taxon559292. Exact
    identity, gene, relevant FUNCTION/SUBUNIT/SIMILARITY/location comments and family
    cross-references were inspected. The maintained cell-cortex annotations cite Huh
    and Walther as stated.
  snapshot_sha256: 5f0c82d657897c50f60bfe700506437ddc2cb428bb6772074e9196aaef8f68ce
- evidence_id: micro53-gene-LSP1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ALSP1%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set; actual query uses gene_exact:LSP1, organism_id:559292
    and reviewed:true.
  accessed_at: '2026-10-22T06:08:09.057647Z'
  support: supports
  summary: The bounded reviewed exact-LSP1 query returns the single Q12230 entry at
    taxon559292.
  snapshot_sha256: 60c5d64be1e8207cd60ba91e1a26c45f1a408e6512acc4547d2829f667c43a21
- evidence_id: micro53-protein-P54003
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P54003.json
  locator: Primary accession/status, recommended name, gene/taxon; full relevant comments
    and InterPro/PANTHER cross-references.
  accessed_at: '2026-10-22T06:08:09.223057Z'
  support: supports
  summary: Reviewed P54003 identifies SUR7 in S.cerevisiae S288C taxon559292. Exact
    identity, gene, relevant FUNCTION/SUBUNIT/SIMILARITY/location comments and family
    cross-references were inspected. Maintained membrane/cortex provenance matches
    Young, Navarre and Walther; broad Sur7/Rim9 family membership does not establish
    a Sur7-only class.
  snapshot_sha256: 9f26f2c5a9984a2a9a67dd5fe8478290ec8522abbc75595d2829145fa791b25d
- evidence_id: micro53-gene-SUR7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASUR7%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set; actual query uses gene_exact:SUR7, organism_id:559292
    and reviewed:true.
  accessed_at: '2026-10-22T06:08:10.021705Z'
  support: supports
  summary: The bounded reviewed exact-SUR7 query returns the single P54003 entry at
    taxon559292.
  snapshot_sha256: 4c29ffd344834d92aed34a0900a95b054e4b46ae7d25df3866413488437ae518
- evidence_id: micro53-ipr-IPR028245
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR028245/
  locator: Complete native family name/type/description/member signatures; separate
    reviewed proteins corroborate membership.
  accessed_at: '2026-10-22T06:08:13.699275Z'
  support: supports
  summary: IPR028245 is a whole-protein Pil1/Lsp1 family, integrated with PF13805
    and PTHR31962. It fits the grouped component; its historical endocytosis background
    is not used to replace the record's membrane-organization function.
  snapshot_sha256: 48661066f7cb3d1fbe562bed3579aa2c4fcefca32c88c4af18443694274cfdf2
- evidence_id: micro53-family-IPR009571
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR009571/
  locator: Complete name/type/description and member-signature metadata.
  accessed_at: '2026-10-21T10:01:29.740199Z'
  support: supports
  summary: IPR009571 and its PF06687 member cover Sur7, Rim9 and PalI. This broader
    fungal membrane-protein family is not demonstrated to be an exact match for the
    named Sur7-only component.
  snapshot_sha256: c74c73d3bc87f92f276f050b86fd528fb0fab53e131f1afa34bc2ad80c075262
- evidence_id: micro53-sur7-panther
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR36414/
  locator: Complete source-family metadata, integration and generated-text flags;
    no mechanistic claim is adopted.
  accessed_at: '2026-10-22T06:09:46.417008Z'
  support: context_only
  summary: The unintegrated PTHR36414 family is named SUR7 domain-containing protein;
    its generated description is unchecked. This alone does not resolve an exact allowable
    Sur7-only class or justify changing the component.
  snapshot_sha256: 7e987b0902894431cbd290fb12b3fc147348808845cc45309909e59e47b105e5
- evidence_id: micro53-sur7-subfamily
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR36414:SF1/
  locator: Retained native request/response receipt; bounded access limitation.
  accessed_at: '2026-10-22T06:09:46.551206Z'
  support: context_only
  summary: The candidate subfamily endpoint returned HTTP204 with an empty body. No
    exact subfamily identity is established from this response.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: micro53-walther2006-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/nature04472
  locator: 'Genuine publisher main HTML, derived paragraph indices7,9–13,17,36: abstract,
    composition/localization, perturbation and immunopurification Methods. No figure
    pixels or supplements.'
  accessed_at: '2026-10-21T10:00:34.700930Z'
  support: supports
  summary: Walther directly supports Pil1/Lsp1 assemblies and Sur7 colocalization
    in budding yeast. Pil1 deletion disrupts the spatial pattern; Lsp1 or Sur7 perturbations
    are not equivalent universal formation tests.
  snapshot_sha256: 145bf600ec6c6dfd955824ec5ffd58f42700bff6ae47b0f2120d69db6cd2993e
- evidence_id: micro53-olivera-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3128537/
  locator: 'Genuine PMC3128537 HTML: sec4–6, sec9, sec13, sec17–18 and embedded Figure2–5
    captions. No pixels or supplemental alignments/assays.'
  accessed_at: '2026-10-22T06:09:46.141319Z'
  support: supports
  summary: Olivera-Couto directly tests Pil1/Lsp1 lipid binding, membrane tubulation
    and Pil1 mutant effects on yeast eisosome/MCC organization. Recombinant liposome
    and heterologous COS7 experiments remain distinct from yeast structures.
  snapshot_sha256: f7b197c972d4731976e01c10cc8a4e37ce57fc8159da5d460cf1cc5a07b3a12a
- evidence_id: micro53-karotki
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3257569/fullTextXML
  locator: 'Genuine PMC3257569 JATS: sec3/5/6/9/11 and Methods sec14/15/17/19/20;
    embedded Figure1–3/6–7 captions. No raw pixels, supplemental images or independent
    structural reanalysis.'
  accessed_at: '2026-10-21T06:56:07.011936Z'
  support: supports
  summary: Karotki demonstrates recombinant filament assembly, membrane association
    and in-situ Pil1/Lsp1-coated furrows. In-vitro closed tubes are distinguished
    from the half-cylinder-like in-situ scaffold.
  snapshot_sha256: 403bb366f2d751bb16d953995b5800338820e4ee1a7f0c79b0c7f1b2d5a67152
- evidence_id: micro53-moreira
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.e08-03-0313&format=json&resultType=core
  locator: Unique native MED bibliographic entry and complete abstractText.
  accessed_at: '2026-10-22T06:08:12.787492Z'
  support: supports
  summary: 'PMID19037108: Pil1 controls eisosome biogenesis. DOI10.1091/mbc.e08-03-0313.
    Complete native abstract and identity read; Moreira is used only at this tier.'
  snapshot_sha256: 0009dc1b36ac44f0ec74b16933716fc977c18d0cd573e91cbbcb7f921323a4e0
- evidence_id: micro53-olivera
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.e10-12-1021&format=json&resultType=core
  locator: Unique native MED bibliographic entry and complete abstractText.
  accessed_at: '2026-10-22T06:08:12.826000Z'
  support: supports
  summary: 'PMID21593205: The eisosome core is composed of BAR domain proteins. DOI10.1091/mbc.e10-12-1021.
    Complete native abstract and identity read; Moreira is used only at this tier.'
  snapshot_sha256: 69798005c6a5ef320383215083fcd8364f2f0d1def0617e0ab5ea42d66d102d3
- evidence_id: micro53-karotki-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1083%2Fjcb.201104040&format=json&resultType=core
  locator: Unique native MED bibliographic entry and complete abstractText.
  accessed_at: '2026-10-22T06:08:13.299751Z'
  support: supports
  summary: 'PMID22123866: Eisosome proteins assemble into a membrane scaffold. DOI10.1083/jcb.201104040.
    Complete native abstract and identity read; Moreira is used only at this tier.'
  snapshot_sha256: 6af51947242b209d6709b77f7edd72602fb91ee777f4e8e57686c7d6ba8f9a62
- evidence_id: micro53-douglas2014-publisher
  kind: authority
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-micro-091313-103507
  locator: Original403 access receipt and challenge HTML; no body support inferred.
  accessed_at: '2026-10-21T10:00:34.701299Z'
  support: context_only
  summary: The retained publisher response is HTTP403, not the Douglas review body.
    The native MED abstract supplies the independently read secondary tier.
  snapshot_sha256: b1f4711f6f03e0c79150315105c200a454323178003dcc32b35f9bb6d4e03e1d
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/eisosome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:03:37Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/eisosome.yaml'
  snapshot_sha256: 6783026a8cd924031dbad6fe0fe729e3fc050d9849cb69cdc43bbf59c87e987d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/eisosome.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/eisosome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:03:39Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/eisosome.yaml\
    \ --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/eisosome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch53-20261022-kx679dvh/eisosome-strict.tsv"
  snapshot_sha256: 476ff2eba763fc4a4763965fc67fb76ad6d39885d9826768eb6c6cec08af2344
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/eisosome.yaml --causal-graphs
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:08:14.073085Z'
  support: supports
  summary: "data/structures/other/eisosome.yaml  (GO:0032126)\n  pil1_lsp1_eisosome_scaffold\t\
    pil1_lsp1_bar_core\tCOVERED\t->pil1_lsp1_bar_core (UniProtKB:P53252, UniProtKB:Q12230)\n\
    \  pil1_lsp1_eisosome_scaffold\tsur7_membrane_protein\tCOVERED\t->sur7_membrane_protein\
    \ (UniProtKB:P54003)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED\
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
  snapshot_sha256: b0e108f81d2b02fa358798328d9b302fd746704f610e9c3665ab02ca281b9d99
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/eisosome.yaml --verify
  locator: Complete focused native read-only report
  accessed_at: '2026-10-22T06:08:15.716226Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/eisosome.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 19 collected target identifiers returned OK. PMID:11784867: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:12469340: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:16496001: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:25002088: UNREACHABLE;
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
  topic: Paired membrane-and-scaffold identity
  outcome: supported
  target_ids:
  - GO:0032126
  summary: The definition and two has_part terms match native GO. The whole eisosome
    is not conflated with only its cytoplasmic protein lattice or only MCC membrane.
  evidence_ids:
  - record
  - curation
  - schema
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - micro53-walther2006-publisher
  - micro53-karotki
- assessment_id: composition
  area: grounding
  topic: Pil1/Lsp1 and Sur7 constituent scope
  outcome: supported
  target_ids:
  - GO:0032126
  summary: The grouped core has exact IPR028245 grounding and verified examples. Sur7
    localization is direct; broad IPR009571/PalI-family and unchecked PANTHER metadata
    do not resolve a Sur7-only match. The existing open exact-grounding task remains
    bounded rather than a confirmed omission.
  evidence_ids:
  - record
  - curation
  - schema
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - micro53-protein-P53252
  - micro53-gene-PIL1
  - micro53-protein-Q12230
  - micro53-gene-LSP1
  - micro53-protein-P54003
  - micro53-gene-SUR7
  - micro53-ipr-IPR028245
  - micro53-family-IPR009571
  - micro53-sur7-panther
  - micro53-walther2006-publisher
  - micro53-olivera-legacy
  - micro53-karotki
- assessment_id: function
  area: evidence
  topic: Membrane-domain organization
  outcome: supported
  target_ids:
  - GO:0032126
  summary: The named organization function and canonical S.cerevisiae example agree
    with the primary scaffold/localization results. The older endocytosis title is
    not treated as proof that eisosomes universally initiate endocytosis. Moreira
    and Douglas are assessed at complete-abstract tier only.
  evidence_ids:
  - record
  - curation
  - schema
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - micro53-walther2006-publisher
  - micro53-olivera-legacy
  - micro53-karotki
  - micro53-moreira
  - micro53-olivera
  - micro53-karotki-meta
  - micro53-pmid-14562095
  - micro53-pmid-16496001
  - micro53-pmid-11784867
  - micro53-pmid-12469340
  - micro53-pmid-25002088
- assessment_id: scope
  area: scope
  topic: Fungal variability and experimental systems
  outcome: supported
  target_ids:
  - GO:0032126
  summary: Fungi VARIABLE is compatible with a non-universal named fungal structure
    and a directly supported S.cerevisiae example. The W303/S288C-derived yeast work,
    recombinant E.coli expression and COS7 overexpression are kept distinct; no fungal
    prevalence census is claimed.
  evidence_ids:
  - record
  - curation
  - schema
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - micro53-walther2006-publisher
  - micro53-olivera-legacy
  - micro53-karotki
- assessment_id: graph
  area: graph
  topic: Supported coarse assembly account
  outcome: supported
  target_ids:
  - GO:0032126
  summary: The three edges distinguish Pil1/Lsp1 assembly, membrane scaffolding and
    Sur7 localization. Direct in-vitro assembly/membrane deformation plus yeast perturbation
    and in-situ organization support the coarse MECHANISTIC account; it does not assert
    a complete kinetic pathway or identical structures in every assay.
  evidence_ids:
  - record
  - curation
  - schema
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - graphs
  - micro53-walther2006-publisher
  - micro53-olivera-legacy
  - micro53-karotki
- assessment_id: formation
  area: evidence
  topic: Formation necessity not overstated
  outcome: unknown
  target_ids:
  - GO:0032126
  summary: Component essentiality is unset. Localization, filament formation and mutant
    spatial phenotypes are not converted into universal formation necessity for every
    grouped protein; no unsupported ESSENTIAL label is present.
  evidence_ids:
  - record
  - curation
  - schema
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - micro53-walther2006-publisher
  - micro53-olivera-legacy
  - micro53-karotki
- assessment_id: examples
  area: grounding
  topic: Exact protein examples and annotation placement
  outcome: supported
  target_ids:
  - GO:0032126
  summary: All current accessions, declared genes, reviewed status and S288C pairs
    match native identities and bounded single-hit queries. Location citations/ECO
    annotations agree where present; localization is not promoted to physical complex
    membership.
  evidence_ids:
  - record
  - curation
  - schema
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - micro53-protein-P53252
  - micro53-gene-PIL1
  - micro53-protein-Q12230
  - micro53-gene-LSP1
  - micro53-protein-P54003
  - micro53-gene-SUR7
  - micro53-pmid-14562095
  - micro53-pmid-16496001
  - micro53-pmid-11784867
  - micro53-pmid-12469340
  - micro53-pmid-25002088
- assessment_id: coverage
  area: completeness
  topic: Complete target with explicit unresolved scope
  outcome: supported
  target_ids:
  - GO:0032126
  summary: All scientific fields, source placements, annotations, graph edges, discussions
    and history were reviewed. Historical first-pass statements are not declared false
    merely because current access improves. Optional inventories and unverified exact
    mappings remain bounded limitations; no concrete required correction was established.
  evidence_ids:
  - record
  - curation
  - schema
  - micro53-go
  - micro53-GO0032126-ancestors
  - micro53-tax4751
  - micro53-tax4932
  - micro53-tax559292
  - micro53-protein-P53252
  - micro53-gene-PIL1
  - micro53-protein-Q12230
  - micro53-gene-LSP1
  - micro53-protein-P54003
  - micro53-gene-SUR7
  - micro53-walther2006-publisher
  - micro53-olivera-legacy
  - micro53-karotki
  - micro53-ipr-IPR028245
  - micro53-family-IPR009571
  - micro53-moreira
  - micro53-olivera
  - micro53-karotki-meta
  - micro53-pmid-14562095
  - micro53-pmid-16496001
  - micro53-pmid-11784867
  - micro53-pmid-12469340
  - micro53-pmid-25002088
findings: []
actions: []
limitations:
- Walther is read at main paragraphs7/9–13/17/36; Olivera and Karotki at the exact
  sections/captions listed. No primary figure pixels or supplements were inspected.
  Moreira/Douglas and Young/Navarre/Huh annotation studies are used at complete-native-abstract
  tier only; the retained Young full body was not independently used here.
- Broad Sur7/Rim9/PalI family membership and unchecked PANTHER prose do not prove
  an exact Sur7-only class. Additional Nce102/resident inventory and a fungal prevalence
  census remain unestablished optional enrichment.
- The current experiment-specific assembly account is supported, but it is not an
  exhaustive native maturation pathway or proof of universal per-protein formation
  necessity.
- Original source URLs, UTC timestamps and raw SHA256 are retained for reused sources;
  HTTP success does not imply article readability.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user requests one review for every unreviewed record, including qualified clean
  records.
- Native ontology, taxonomy and protein/family sources directly address the present
  claims. No expression-module dataset is asserted to establish physical structure
  membership.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
