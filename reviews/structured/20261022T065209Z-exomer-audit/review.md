# Source-grounded review of exomer complex

- Review: 20261022T065209Z-exomer-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:28:03Z
- Finished UTC: 2026-10-22T06:52:09Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor findings resolve the exact Chs5 homologous-family mapping and preserve direct, condition-specific Chs5-dependent physical association. The class, five named component types, variable ChAP combinations and external Arf1 recruitment boundary are supported.

## Scope And Provenance

Exactly one complete maintained target, with source-native and primary reading scopes declared individually.

Selection: One complete record in strict-path batch 55 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0034044 | data/structures/other/exomer_complex.yaml | maintained | exomer complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0034044 | Focused validator passed. |
| Focused native strict | passed | True | GO:0034044 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0034044 | Focused check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:0034044 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0034044 | No iModulon-specific claim is assessed; the relevant complex/assay evidence was inspected directly. |
| Claim-level scientific review | passed | True | GO:0034044 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0034044 | 16 of 19 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:16498409: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:17000877: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0034044 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0034044 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0034044 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0034044 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0034044 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Selective cargo-adaptor class and Chs5/6 synonym

identity: supported. Targets: GO:0034044.

Exact GO class and parent match the record. Sanchatjate names the Chs5/6 complex; Wang calls the corresponding Chs5/ChAP coat exomer. The maintained definition does not claim a fixed five-subunit stoichiometry.

### Valid five named classes and one resolved family

grounding: concern. Targets: GO:0034044.

All five reference proteins and exact-gene query identities agree. Chs5 has an exact homologous-family mapping corroborated by the complete reviewed member set. IPR015374 is broader than each individual ChAP class and is withheld as an exact replacement.

### Direct Chs5 dependence exceeds generic scaffold membership

grounding: concern. Targets: GO:0034044.

The role identifies a scaffold and the graph says assembles-with, but the directly measured loss of ChAP coassociation in chs5-deletion extracts and stable TGN retention dependence are not stated. These are bounded structure-level results, separate from whether Chs3 cargo reaches the surface.

### Supported associations and external recruiting GTPase

graph: supported. Targets: GO:0034044.

All Chs5-ChAP membership/association edges, TGN localization and selective export are supported in the declared source scopes. Native UniProt prose includes Arf1 in a membrane-associated assembly, whereas purified Chs5/ChAP complexes form before Arf1 addition; the maintained external-regulator boundary is defensible. NONMECHANISTIC scope avoids claiming a complete coat mechanism.

### Yeast reference and assay scopes

scope: supported. Targets: GO:0034044.

S288C reference accessions are distinct from Sanchatjate DDY1810-derived purification strains and Wang SEY6210/CWY strains and baculovirus expression system. Huranova strain details live in an unread appendix; inspected methods specify growth and FRAP conditions. COMMON is a qualitative category; no prevalence census is claimed.

### Complete maintained target and bounded follow-up

completeness: supported. Targets: GO:0034044.

Every maintained field, evidence row, component/example, graph edge, discussion and history entry was read. Optional unpopulated slots are not defects. Scientific status/history remain unchanged.

## Findings

### F1: Resolve the verified Chs5 family mapping

minor / open / confirmed; issue key: exomer-chs5-exact-family-grounding.

The Chs5 scaffold remains label-only under an open exact-family task, although native IPR052827 names its whole-protein family and Q12114 plus the complete reviewed member set corroborate the homologous class.

### F2: Record the experimentally tested Chs5 scaffold dependence

minor / open / confirmed; issue key: exomer-chs5-bounded-complex-integrity.

Sanchatjate sec12 and Figure5 report that Chs6-TAP association with Bch1,Bud7 and Bch2 depends on Chs5 in the tested extracts. Huranova adds a distinct Chs5-dependent stable TGN retention result. The current generic scaffold role/assembles-with graph does not preserve these tested conditional relationships.

## Recommended Actions And Acceptance Checks

### A1

Ground Chs5 with IPR052827 and narrow the open task to individual ChAP mappings; keep the four paralog-specific rows distinct.

- Do not derive exact identity solely from the generated unchecked InterPro description.
- Do not apply shared IPR015374 to all four rows as if it distinguished their paralog classes.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

### A2

Add the specifically assayed Chs5-dependent physical association result and, if represented, distinguish stable membrane retention from complex coassociation. Retain assay and strain context; do not turn every cargo phenotype into physical essentiality.

- Anchor association to Chs6-TAP purification in the reported wild-type/deletion backgrounds.
- Preserve the observation that loss of individual ChAPs can leave the remaining complex associated.
- Keep UNKNOWN for unestablished universal formation necessity; any scoped inference must state its scope.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/exomer_complex.yaml; Entire maintained target, including all components, evidence, graph edges, discussions and history | context_only | The complete target was read. The maintained YAML owns any later scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope | context_only | Formation necessity is distinct from activity, localization and viability. COMMON is the qualitative category present in most members with exceptional losses, not a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and taxon-paired protein examples | context_only | Protein examples do not replace constituent-class grounding. Shared domains and broader paralog families do not resolve exact class tasks. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Scope and edge-level source support | context_only | Descriptive membership graphs need not assert a complete mechanism; a directly observed conditional physical dependency can be stated without making every constituent universally essential. |
| root55-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000145,GO:0005802,GO:0006887,GO:0006893,GO:0008854,GO:0009338,GO:0032991,GO:0034044,GO:0140535,GO:1902494; Ten native terms: identities, status, complete definitions/comments/synonyms and relevant typed child relations only | supports | GO0034044 exactly identifies the exomer selective cargo adaptor; GO0032991 is the protein-complex parent, GO0006893 its transport process and GO0005802 the TGN localization. |
| root55-sources-GO0034044-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034044/ancestors?relations=is_a; Complete native ancestor response | supports | The complete is_a-only ancestry corroborates the focal identity and any declared parent; it is not a parthood or occurrence survey. |
| root55-sources-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | Native taxId4932 identifies Saccharomyces cerevisiae; species and reference-strain scopes remain distinct. |
| root55-sources-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | Native taxId559292 identifies Saccharomyces cerevisiae S288C; species and reference-strain scopes remain distinct. |
| root55-sources-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED14562095: Global analysis of protein localization in budding yeast. Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003); DOI10.1038/nature02026. Entire native abstract read; this row does not claim the paper body. |
| root55-sources-pmid-16498409 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16498409+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED16498409: Arf1p, Chs5p and the ChAPs are required for export of specialized cargo from the Golgi. Trautwein M, Schindler C, Gauss R, Dengjel J, Hartmann E, Spang A. (2006); DOI10.1038/sj.emboj.7601007. Entire native abstract read; this row does not claim the paper body. |
| root55-sources-pmid-17000877 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17000877+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED17000877: Exomer: A coat complex for transport of select membrane proteins from the trans-Golgi network to the plasma membrane in yeast. Wang CW, Hamamoto S, Orci L, Schekman R. (2006); DOI10.1083/jcb.200605106. Entire native abstract read; this row does not claim the paper body. |
| root55-sources-doi-10.1038_sj.emboj.7601007 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fsj.emboj.7601007%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED16498409: Arf1p, Chs5p and the ChAPs are required for export of specialized cargo from the Golgi. Trautwein M, Schindler C, Gauss R, Dengjel J, Hartmann E, Spang A. (2006). Complete native abstract read; separately declared body evidence has narrower locators. |
| root55-sources-doi-10.1083_jcb.200605106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200605106%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED17000877: Exomer: A coat complex for transport of select membrane proteins from the trans-Golgi network to the plasma membrane in yeast. Wang CW, Hamamoto S, Orci L, Schekman R. (2006). Complete native abstract read; separately declared body evidence has narrower locators. |
| root55-sources-doi-10.1091_mbc.e06-03-0210 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e06-03-0210%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED16855022: Chs5/6 complex: a multiprotein complex that interacts with and conveys chitin synthase III from the trans-Golgi network to the cell surface. Sanchatjate S, Schekman R. (2006). Complete native abstract read; separately declared body evidence has narrower locators. |
| root55-sources-doi-10.15252_embr.201540795 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.15252%2Fembr.201540795%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED26742961: Dynamic assembly of the exomer secretory vesicle cargo adaptor subunits. Huranova M, Muruganandam G, Weiss M, Spang A. (2016). Complete native abstract read; separately declared body evidence has narrower locators. |
| root55-sources-protein-Q12114 | https://rest.uniprot.org/uniprotkb/Q12114.json; Identity/status, recommended and alternative names, genes/aliases, organism; InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | Q12114 matches the declared reviewed CHS5 example and reference taxon. Native function, membership, localization and family annotations were distinguished from direct primary experiments. |
| root55-sources-gene-CHS5 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHS5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set with gene/aliases, status and organism; native exact-gene, organism_id, reviewed and size500 parameters | supports | Exact-gene reviewed query restricted to the declared organism_id returns only Q12114. |
| root55-sources-protein-P40955 | https://rest.uniprot.org/uniprotkb/P40955.json; Identity/status, recommended and alternative names, genes/aliases, organism; InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | P40955 matches the declared reviewed CHS6 example and reference taxon. Native function, membership, localization and family annotations were distinguished from direct primary experiments. |
| root55-sources-gene-CHS6 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHS6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set with gene/aliases, status and organism; native exact-gene, organism_id, reviewed and size500 parameters | supports | Exact-gene reviewed query restricted to the declared organism_id returns only P40955. |
| root55-sources-protein-Q05029 | https://rest.uniprot.org/uniprotkb/Q05029.json; Identity/status, recommended and alternative names, genes/aliases, organism; InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | Q05029 matches the declared reviewed BCH1 example and reference taxon. Native function, membership, localization and family annotations were distinguished from direct primary experiments. |
| root55-sources-gene-BCH1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABCH1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set with gene/aliases, status and organism; native exact-gene, organism_id, reviewed and size500 parameters | supports | Exact-gene reviewed query restricted to the declared organism_id returns only Q05029. |
| root55-sources-protein-Q08754 | https://rest.uniprot.org/uniprotkb/Q08754.json; Identity/status, recommended and alternative names, genes/aliases, organism; InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | Q08754 matches the declared reviewed BUD7 example and reference taxon. Native function, membership, localization and family annotations were distinguished from direct primary experiments. |
| root55-sources-gene-BUD7 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABUD7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set with gene/aliases, status and organism; native exact-gene, organism_id, reviewed and size500 parameters | supports | Exact-gene reviewed query restricted to the declared organism_id returns only Q08754. |
| root55-sources-protein-P36122 | https://rest.uniprot.org/uniprotkb/P36122.json; Identity/status, recommended and alternative names, genes/aliases, organism; InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | P36122 matches the declared reviewed BCH2 example and reference taxon. Native function, membership, localization and family annotations were distinguished from direct primary experiments. |
| root55-sources-gene-BCH2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABCH2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Whole returned identity set with gene/aliases, status and organism; native exact-gene, organism_id, reviewed and size500 parameters | supports | Exact-gene reviewed query restricted to the declared organism_id returns only P36122. |
| root55-sources-protein-P11076 | https://rest.uniprot.org/uniprotkb/P11076.json; Identity/names/genes/organism and complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present | supports | The reviewed yeast GTPase identity corroborates the external graph node; it does not turn the regulator into a constituent of the purified complex. |
| root55-sources-ipr-IPR052827 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052827/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | Native family identity is Exomer complex component Chs5, integrated with PTHR47351. Its generated unchecked description is not treated as independent mechanistic evidence. |
| root55-sources-chs5-reviewed | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR052827/?page_size=200; count3,next:null and complete accession/name/gene/taxon metadata for all three reviewed results | supports | Complete three-member reviewed set contains Candida CHS5 O74161, budding-yeast CHS5 Q12114 and fission-yeast cfr1 Q92357. This corroborates the homologous protein class despite naming differences; it does not establish identical complex roles or cargo specificity in all fungi. |
| root55-sources-ipr-IPR015374 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR015374/; Native accession/name/type, entire description with LLM/curation flags, integrated signatures and hierarchy | supports | The ChAP whole family covers the four named paralogs; its shared membership does not resolve their individual exact constituent classes. |
| root55-sources-PMC1635352-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC1635352/; Methods sec3/4 including Table1; Results sec8/9/11/12 with embedded Figures1/2/4/6 and Tables2/3/4; Figure5 complete caption | supports | Sanchatjate2006 supports stable Chs5/ChAP association and Chs3 cargo binding with distinct member contributions. In chs5-deletion extracts Chs6-TAP fails to copurify the other ChAPs efficiently; ChAP deletions can leave other subunits associated. This physical association result is distinct from cargo transport and does not establish an invariant five-subunit stoichiometry. |
| root55-sources-PMC5290816-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC5290816/; Results sections embr201540795-sec-0005,0007,0010 including Table2/Figure2/FigureEV2/Figure3 captions; Methods0017/0018/0019/0023 in full | supports | Huranova2016 FRAP/fractionation results support assembly at TGN and Chs5-dependent stable ChAP retention. Variable ChAP dynamics and overexpression effects support heterogeneous mixed complexes; recruitment/stability is not equated with viability or a universal five-protein particle. |
| root55-sources-PMC1409733-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC1409733/; Results sec5/7/11/12/13 with embedded Figures2/4/7/8 captions; Methods sec19 and21 | supports | Trautwein2006 shows activated-Arf1 associations, ChAP interactions of variable stoichiometry, Chs5 binding and Chs5-dependent TGN localization. Bch1 localization is explicitly hard to score in those experiments; coimmunoprecipitation does not prove every pair interacts directly. |
| root55-sources-PMC2064389 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2064389/fullTextXML; Four complete Results subsections beginning A purified recombinant complex, Myristoylated Arf1p-GTPgammaS, Stoichiometric recruitment and Chs5-Chs6[all] forms a coated surface, including Figures3–7 captions; Methods Yeast strains/materials,Protein purification,Liposome recruitment assay | supports | Wang2006 coexpression/purification and liposome assays support a stable Chs5/ChAP assembly plus Arf1-facilitated membrane recruitment. Certain lipid formulations recruit complex without Arf1; the general supports-recruitment graph edge is appropriately bounded. Coated liposomes do not by themselves establish vesicle budding. |
| schema-result | just validate data/structures/other/exomer_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/exomer_complex.yaml |
| strict-result | just validate-strict data/structures/other/exomer_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exomer_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/exomer_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exomer_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exomer_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/exomer_complex.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/exomer_complex.yaml  (GO:0034044)<br>  yeast_exomer_tgn_export	chs5_exomer_scaffold	COVERED	-&gt;chs5_exomer_scaffold (UniProtKB:Q12114)<br>  yeast_exomer_tgn_export	chs6_exomer_chap_subunit	COVERED	-&gt;chs6_exomer_chap_subunit (UniProtKB:P40955)<br>  yeast_exomer_tgn_export	bch1_exomer_chap_subunit	COVERED	-&gt;bch1_exomer_chap_subunit (UniProtKB:Q05029)<br>  yeast_exomer_tgn_export	bud7_exomer_chap_subunit	COVERED	-&gt;bud7_exomer_chap_subunit (UniProtKB:Q08754)<br>  yeast_exomer_tgn_export	bch2_exomer_chap_subunit	COVERED	-&gt;bch2_exomer_chap_subunit (UniProtKB:P36122)<br>  yeast_exomer_tgn_export	arf1_gtpase	UNANCHORED_WITH_UNIPROT	Arf1 GTPase (UniProtKB:P11076)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     5  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     6  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/exomer_complex.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/exomer_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 16 of 19 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:16498409: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:17000877: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw datasets, atomic coordinates, sequence alignments or supplemental files were reanalyzed. Body reading is bounded by the exact evidence locators.
- Huranova supplemental strain table and raw figure data were not read. Primary-body scopes are declared per source; no universal quantitative stoichiometry or whole-fungi cargo specificity is inferred.
- Native UniProt includes Arf1 in its subunit prose; primary purification/reconstitution supports the narrower stable Chs5/ChAP core used here. Shared ChAP family membership is not an exact paralog mapping.
- The local absence being assessed is confined to the entire inspected target roles/graph and explicit existing grounding task, not a claim that no related corpus record exists.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations and issue-bearing reviews alike.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T065209Z-exomer-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of exomer complex
started_at: '2026-10-22T06:28:03Z'
finished_at: '2026-10-22T06:52:09Z'
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
summary: Two minor findings resolve the exact Chs5 homologous-family mapping and preserve
  direct, condition-specific Chs5-dependent physical association. The class, five
  named component types, variable ChAP combinations and external Arf1 recruitment
  boundary are supported.
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
  - path: data/structures/other/exomer_complex.yaml
    sha256: 55a7b002a5fa16fd9f559b79056daa52a6699576bb1f5849bcb8f4ad42dbd02a
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
- target_id: GO:0034044
  path: data/structures/other/exomer_complex.yaml
  label: exomer complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/exomer_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, with source-native and primary
    reading scopes declared individually.
  selection: One complete record in strict-path batch 55 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0034044
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0034044
  command: just validate data/structures/other/exomer_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0034044
  command: just validate-strict data/structures/other/exomer_complex.yaml --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exomer_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0034044
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/exomer_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0034044
  command: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/exomer_complex.yaml
    --verify
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0034044
  summary: No iModulon-specific claim is assessed; the relevant complex/assay evidence
    was inspected directly.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0034044
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root55-sources-go
  - root55-sources-GO0034044-ancestors
  - root55-sources-tax-4932
  - root55-sources-tax-559292
  - root55-sources-pmid-14562095
  - root55-sources-pmid-16498409
  - root55-sources-pmid-17000877
  - root55-sources-doi-10.1038_sj.emboj.7601007
  - root55-sources-doi-10.1083_jcb.200605106
  - root55-sources-doi-10.1091_mbc.e06-03-0210
  - root55-sources-doi-10.15252_embr.201540795
  - root55-sources-protein-Q12114
  - root55-sources-gene-CHS5
  - root55-sources-protein-P40955
  - root55-sources-gene-CHS6
  - root55-sources-protein-Q05029
  - root55-sources-gene-BCH1
  - root55-sources-protein-Q08754
  - root55-sources-gene-BUD7
  - root55-sources-protein-P36122
  - root55-sources-gene-BCH2
  - root55-sources-protein-P11076
  - root55-sources-ipr-IPR052827
  - root55-sources-chs5-reviewed
  - root55-sources-ipr-IPR015374
  - root55-sources-PMC1635352-html
  - root55-sources-PMC5290816-html
  - root55-sources-PMC1409733-html
  - root55-sources-PMC2064389
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0034044
  summary: '16 of 19 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:16498409: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:17000877: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - root55-sources-pmid-14562095
  - root55-sources-pmid-16498409
  - root55-sources-pmid-17000877
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0034044
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
  - GO:0034044
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
  - GO:0034044
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
  - GO:0034044
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
  - GO:0034044
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
  reference: data/structures/other/exomer_complex.yaml
  locator: Entire maintained target, including all components, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T06:45:32Z'
  support: context_only
  summary: The complete target was read. The maintained YAML owns any later scientific
    correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope
  accessed_at: '2026-10-22T06:45:32Z'
  support: context_only
  summary: Formation necessity is distinct from activity, localization and viability.
    COMMON is the qualitative category present in most members with exceptional losses,
    not a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and taxon-paired protein examples
  accessed_at: '2026-10-22T06:45:32Z'
  support: context_only
  summary: Protein examples do not replace constituent-class grounding. Shared domains
    and broader paralog families do not resolve exact class tasks.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and edge-level source support
  accessed_at: '2026-10-22T06:45:32Z'
  support: context_only
  summary: Descriptive membership graphs need not assert a complete mechanism; a directly
    observed conditional physical dependency can be stated without making every constituent
    universally essential.
- evidence_id: root55-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000145,GO:0005802,GO:0006887,GO:0006893,GO:0008854,GO:0009338,GO:0032991,GO:0034044,GO:0140535,GO:1902494
  locator: 'Ten native terms: identities, status, complete definitions/comments/synonyms
    and relevant typed child relations only'
  accessed_at: '2026-10-22T06:38:51.764560Z'
  support: supports
  summary: GO0034044 exactly identifies the exomer selective cargo adaptor; GO0032991
    is the protein-complex parent, GO0006893 its transport process and GO0005802 the
    TGN localization.
  snapshot_sha256: 30bebfa68466084ceae0cad027ebee585d5b955925774938ac3aac92d37c72d7
- evidence_id: root55-sources-GO0034044-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0034044/ancestors?relations=is_a
  locator: Complete native ancestor response
  accessed_at: '2026-10-22T06:39:12.396301Z'
  support: supports
  summary: The complete is_a-only ancestry corroborates the focal identity and any
    declared parent; it is not a parthood or occurrence survey.
  snapshot_sha256: 08e4636623c9a8c4164aa5636026c3a6fbb78aa5f5f5bbda9bc5106fc3049601
- evidence_id: root55-sources-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:38:53.047704Z'
  support: supports
  summary: Native taxId4932 identifies Saccharomyces cerevisiae; species and reference-strain
    scopes remain distinct.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root55-sources-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:38:53.165999Z'
  support: supports
  summary: Native taxId559292 identifies Saccharomyces cerevisiae S288C; species and
    reference-strain scopes remain distinct.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root55-sources-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T06:39:01.015608Z'
  support: supports
  summary: 'MED14562095: Global analysis of protein localization in budding yeast.
    Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK. (2003);
    DOI10.1038/nature02026. Entire native abstract read; this row does not claim the
    paper body.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: root55-sources-pmid-16498409
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16498409+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T06:39:02.936795Z'
  support: supports
  summary: 'MED16498409: Arf1p, Chs5p and the ChAPs are required for export of specialized
    cargo from the Golgi. Trautwein M, Schindler C, Gauss R, Dengjel J, Hartmann E,
    Spang A. (2006); DOI10.1038/sj.emboj.7601007. Entire native abstract read; this
    row does not claim the paper body.'
  snapshot_sha256: 50b78e87f17adbe03906f52bdfbde7abb8b47a6c31a9c55cce7211fb73099b69
- evidence_id: root55-sources-pmid-17000877
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17000877+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T06:39:02.961111Z'
  support: supports
  summary: 'MED17000877: Exomer: A coat complex for transport of select membrane proteins
    from the trans-Golgi network to the plasma membrane in yeast. Wang CW, Hamamoto
    S, Orci L, Schekman R. (2006); DOI10.1083/jcb.200605106. Entire native abstract
    read; this row does not claim the paper body.'
  snapshot_sha256: b4cada11d8ddb2eee5557c629048f497bf2be5d57e660316ffffc6d8af826b76
- evidence_id: root55-sources-doi-10.1038_sj.emboj.7601007
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fsj.emboj.7601007%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:39:04.815836Z'
  support: supports
  summary: 'Unique DOI result MED16498409: Arf1p, Chs5p and the ChAPs are required
    for export of specialized cargo from the Golgi. Trautwein M, Schindler C, Gauss
    R, Dengjel J, Hartmann E, Spang A. (2006). Complete native abstract read; separately
    declared body evidence has narrower locators.'
  snapshot_sha256: 631925ddf69c3b151457da8b93a71ee52e6568660ba199cf6934c810eefd0ed3
- evidence_id: root55-sources-doi-10.1083_jcb.200605106
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200605106%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:39:05.550827Z'
  support: supports
  summary: 'Unique DOI result MED17000877: Exomer: A coat complex for transport of
    select membrane proteins from the trans-Golgi network to the plasma membrane in
    yeast. Wang CW, Hamamoto S, Orci L, Schekman R. (2006). Complete native abstract
    read; separately declared body evidence has narrower locators.'
  snapshot_sha256: 4baa250e2b07d4fe5b451a96b68ff1978870728bf1b423d8b362a9e4c37b9ebf
- evidence_id: root55-sources-doi-10.1091_mbc.e06-03-0210
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e06-03-0210%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:39:06.168563Z'
  support: supports
  summary: 'Unique DOI result MED16855022: Chs5/6 complex: a multiprotein complex
    that interacts with and conveys chitin synthase III from the trans-Golgi network
    to the cell surface. Sanchatjate S, Schekman R. (2006). Complete native abstract
    read; separately declared body evidence has narrower locators.'
  snapshot_sha256: 0ebbb3623b5b279efc132555f7d2e954e64a57923fb50dc30afce057f050963a
- evidence_id: root55-sources-doi-10.15252_embr.201540795
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.15252%2Fembr.201540795%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique native DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T06:39:06.827164Z'
  support: supports
  summary: 'Unique DOI result MED26742961: Dynamic assembly of the exomer secretory
    vesicle cargo adaptor subunits. Huranova M, Muruganandam G, Weiss M, Spang A.
    (2016). Complete native abstract read; separately declared body evidence has narrower
    locators.'
  snapshot_sha256: 706b27f3985d1ddcab921453edc35d3876a7239b0bf28b405ec559cddf0e0252
- evidence_id: root55-sources-protein-Q12114
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12114.json
  locator: Identity/status, recommended and alternative names, genes/aliases, organism;
    InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC
    ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:39:00.817171Z'
  support: supports
  summary: Q12114 matches the declared reviewed CHS5 example and reference taxon.
    Native function, membership, localization and family annotations were distinguished
    from direct primary experiments.
  snapshot_sha256: a740f8af6c04889e490013d17dec246df13ca056b27a8d156c74a64b3922d5ee
- evidence_id: root55-sources-gene-CHS5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHS5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set with gene/aliases, status and organism; native
    exact-gene, organism_id, reviewed and size500 parameters
  accessed_at: '2026-10-22T06:39:12.674400Z'
  support: supports
  summary: Exact-gene reviewed query restricted to the declared organism_id returns
    only Q12114.
  snapshot_sha256: 8e66d8206c2693bf1118d63e720907f09080154c166c4ccedab208b854bb7e43
- evidence_id: root55-sources-protein-P40955
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40955.json
  locator: Identity/status, recommended and alternative names, genes/aliases, organism;
    InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC
    ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:38:58.843157Z'
  support: supports
  summary: P40955 matches the declared reviewed CHS6 example and reference taxon.
    Native function, membership, localization and family annotations were distinguished
    from direct primary experiments.
  snapshot_sha256: ae6429fb82e3654f0569eeb8b8858a6e7d84b037dc108738e3bd9b99c066188d
- evidence_id: root55-sources-gene-CHS6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACHS6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set with gene/aliases, status and organism; native
    exact-gene, organism_id, reviewed and size500 parameters
  accessed_at: '2026-10-22T06:39:12.979791Z'
  support: supports
  summary: Exact-gene reviewed query restricted to the declared organism_id returns
    only P40955.
  snapshot_sha256: d561094242058fc190c78342b3fe103c090fb173e0dd0fb6f01d1b60237157bb
- evidence_id: root55-sources-protein-Q05029
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q05029.json
  locator: Identity/status, recommended and alternative names, genes/aliases, organism;
    InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC
    ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:38:59.641578Z'
  support: supports
  summary: Q05029 matches the declared reviewed BCH1 example and reference taxon.
    Native function, membership, localization and family annotations were distinguished
    from direct primary experiments.
  snapshot_sha256: d17191d047f9fec6c714f013782fe0186220e0a527669bffcb89e9bf88ae2b9c
- evidence_id: root55-sources-gene-BCH1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABCH1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set with gene/aliases, status and organism; native
    exact-gene, organism_id, reviewed and size500 parameters
  accessed_at: '2026-10-22T06:39:13.542785Z'
  support: supports
  summary: Exact-gene reviewed query restricted to the declared organism_id returns
    only Q05029.
  snapshot_sha256: 760e6563452a65374044fa42a3d1589596f7249df5b9e0a6ad630d516cb4ccaf
- evidence_id: root55-sources-protein-Q08754
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08754.json
  locator: Identity/status, recommended and alternative names, genes/aliases, organism;
    InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC
    ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:39:00.387719Z'
  support: supports
  summary: Q08754 matches the declared reviewed BUD7 example and reference taxon.
    Native function, membership, localization and family annotations were distinguished
    from direct primary experiments.
  snapshot_sha256: 0dbee13e6d94db7f2447961626247d3fac764133c2cd5987534aae9be9a0c12d
- evidence_id: root55-sources-gene-BUD7
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABUD7%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set with gene/aliases, status and organism; native
    exact-gene, organism_id, reviewed and size500 parameters
  accessed_at: '2026-10-22T06:39:13.926700Z'
  support: supports
  summary: Exact-gene reviewed query restricted to the declared organism_id returns
    only Q08754.
  snapshot_sha256: b3fb7535b282c28609be8b866b73fa1eac54ec7ca1a2d02c04e01daed4da2975
- evidence_id: root55-sources-protein-P36122
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36122.json
  locator: Identity/status, recommended and alternative names, genes/aliases, organism;
    InterPro cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC
    ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:38:58.214693Z'
  support: supports
  summary: P36122 matches the declared reviewed BCH2 example and reference taxon.
    Native function, membership, localization and family annotations were distinguished
    from direct primary experiments.
  snapshot_sha256: efad3cc50163c8ad08f980bde82154c5318eac26fe0dd64120d289ab1eb3cb54
- evidence_id: root55-sources-gene-BCH2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABCH2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Whole returned identity set with gene/aliases, status and organism; native
    exact-gene, organism_id, reviewed and size500 parameters
  accessed_at: '2026-10-22T06:39:14.383218Z'
  support: supports
  summary: Exact-gene reviewed query restricted to the declared organism_id returns
    only P36122.
  snapshot_sha256: 66dc0163ecff265204089fab78a45fd54c7e158df493a1203fe6ac7abd56c9e2
- evidence_id: root55-sources-protein-P11076
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11076.json
  locator: Identity/names/genes/organism and complete FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, CATALYTIC ACTIVITY and SIMILARITY comments where present
  accessed_at: '2026-10-22T06:38:56.014842Z'
  support: supports
  summary: The reviewed yeast GTPase identity corroborates the external graph node;
    it does not turn the regulator into a constituent of the purified complex.
  snapshot_sha256: fb2ce21f92da7c817647884a2805ab45d84f49b279093b1a68cd4908bbbfb7b4
- evidence_id: root55-sources-ipr-IPR052827
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR052827/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:40:01.394710Z'
  support: supports
  summary: Native family identity is Exomer complex component Chs5, integrated with
    PTHR47351. Its generated unchecked description is not treated as independent mechanistic
    evidence.
  snapshot_sha256: 39a587e7e196266171b59f2d67219b4fdba37040750dbe312059e93b16f2c2e1
- evidence_id: root55-sources-chs5-reviewed
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR052827/?page_size=200
  locator: count3,next:null and complete accession/name/gene/taxon metadata for all
    three reviewed results
  accessed_at: '2026-10-22T06:41:00.332887Z'
  support: supports
  summary: Complete three-member reviewed set contains Candida CHS5 O74161, budding-yeast
    CHS5 Q12114 and fission-yeast cfr1 Q92357. This corroborates the homologous protein
    class despite naming differences; it does not establish identical complex roles
    or cargo specificity in all fungi.
  snapshot_sha256: 31bcaef0ce6abe89a756c948e5d0034a6ed14eb20805cb958f30316ac4eff091
- evidence_id: root55-sources-ipr-IPR015374
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR015374/
  locator: Native accession/name/type, entire description with LLM/curation flags,
    integrated signatures and hierarchy
  accessed_at: '2026-10-22T06:40:01.587334Z'
  support: supports
  summary: The ChAP whole family covers the four named paralogs; its shared membership
    does not resolve their individual exact constituent classes.
  snapshot_sha256: 47d154e810d46c8e7fe30092e77fbfce9d4671ac314aa62b442cda38e49e95b2
- evidence_id: root55-sources-PMC1635352-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1635352/
  locator: Methods sec3/4 including Table1; Results sec8/9/11/12 with embedded Figures1/2/4/6
    and Tables2/3/4; Figure5 complete caption
  accessed_at: '2026-10-22T06:41:01.709645Z'
  support: supports
  summary: Sanchatjate2006 supports stable Chs5/ChAP association and Chs3 cargo binding
    with distinct member contributions. In chs5-deletion extracts Chs6-TAP fails to
    copurify the other ChAPs efficiently; ChAP deletions can leave other subunits
    associated. This physical association result is distinct from cargo transport
    and does not establish an invariant five-subunit stoichiometry.
  snapshot_sha256: 0c9d194ffcd4b859d11275eafba6388c95b45df75934dfcdf1fbe28743212282
- evidence_id: root55-sources-PMC5290816-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5290816/
  locator: Results sections embr201540795-sec-0005,0007,0010 including Table2/Figure2/FigureEV2/Figure3
    captions; Methods0017/0018/0019/0023 in full
  accessed_at: '2026-10-22T06:41:01.723476Z'
  support: supports
  summary: Huranova2016 FRAP/fractionation results support assembly at TGN and Chs5-dependent
    stable ChAP retention. Variable ChAP dynamics and overexpression effects support
    heterogeneous mixed complexes; recruitment/stability is not equated with viability
    or a universal five-protein particle.
  snapshot_sha256: 127a433ca3472f03f790a7cb28d3adb19e3b34f859494283548e20af3b65c6f9
- evidence_id: root55-sources-PMC1409733-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC1409733/
  locator: Results sec5/7/11/12/13 with embedded Figures2/4/7/8 captions; Methods
    sec19 and21
  accessed_at: '2026-10-22T06:41:01.406107Z'
  support: supports
  summary: Trautwein2006 shows activated-Arf1 associations, ChAP interactions of variable
    stoichiometry, Chs5 binding and Chs5-dependent TGN localization. Bch1 localization
    is explicitly hard to score in those experiments; coimmunoprecipitation does not
    prove every pair interacts directly.
  snapshot_sha256: f7cadca3e42d66f824fc6ca4e59a3db0777463d224aec2554a6a21fccd5bb30d
- evidence_id: root55-sources-PMC2064389
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2064389/fullTextXML
  locator: Four complete Results subsections beginning A purified recombinant complex,
    Myristoylated Arf1p-GTPgammaS, Stoichiometric recruitment and Chs5-Chs6[all] forms
    a coated surface, including Figures3–7 captions; Methods Yeast strains/materials,Protein
    purification,Liposome recruitment assay
  accessed_at: '2026-10-22T06:40:04.459082Z'
  support: supports
  summary: Wang2006 coexpression/purification and liposome assays support a stable
    Chs5/ChAP assembly plus Arf1-facilitated membrane recruitment. Certain lipid formulations
    recruit complex without Arf1; the general supports-recruitment graph edge is appropriately
    bounded. Coated liposomes do not by themselves establish vesicle budding.
  snapshot_sha256: fdbb0bc79f2733c0fa8a2d7367f9cbd464170874323c56d906acc6c0f04c7e90
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/exomer_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:05Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/exomer_complex.yaml'
  snapshot_sha256: d332e92b5abeae73d2f6d4b7255064c6d521fd6e228a1204e1881435a8d711ac
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/exomer_complex.yaml --out
    /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exomer_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:28:06Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/exomer_complex.yaml\
    \ --out /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exomer_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/exomer_complex-strict.tsv"
  snapshot_sha256: a287592210c2ffb67b96280c7bdd40b5318493d04489c5f49fd1ff12192cab13
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/exomer_complex.yaml
    --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:38:57.468609Z'
  support: supports
  summary: "data/structures/other/exomer_complex.yaml  (GO:0034044)\n  yeast_exomer_tgn_export\t\
    chs5_exomer_scaffold\tCOVERED\t->chs5_exomer_scaffold (UniProtKB:Q12114)\n  yeast_exomer_tgn_export\t\
    chs6_exomer_chap_subunit\tCOVERED\t->chs6_exomer_chap_subunit (UniProtKB:P40955)\n\
    \  yeast_exomer_tgn_export\tbch1_exomer_chap_subunit\tCOVERED\t->bch1_exomer_chap_subunit\
    \ (UniProtKB:Q05029)\n  yeast_exomer_tgn_export\tbud7_exomer_chap_subunit\tCOVERED\t\
    ->bud7_exomer_chap_subunit (UniProtKB:Q08754)\n  yeast_exomer_tgn_export\tbch2_exomer_chap_subunit\t\
    COVERED\t->bch2_exomer_chap_subunit (UniProtKB:P36122)\n  yeast_exomer_tgn_export\t\
    arf1_gtpase\tUNANCHORED_WITH_UNIPROT\tArf1 GTPase (UniProtKB:P11076)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     5  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     1  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ PARTIAL_EXAMPLES          component_ref target holds protein_examples but has\
    \ unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target\
    \ declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_NO_UNIPROT     no component_ref\
    \ and no UniProtKB grounding or xref on the node\n     6  total GENE_OR_PROTEIN\
    \ causal nodes"
  snapshot_sha256: a26f9e5dbf195446fdf539e5dd1ff8e21f683e5aed3fa0e2aa030cf0d115dd8b
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch55-20261022-hwfmcxvp/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/exomer_complex.yaml
    --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:38:59.002418Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/exomer_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '16 of 19 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:16498409: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:17000877: UNREACHABLE;
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
  topic: Selective cargo-adaptor class and Chs5/6 synonym
  outcome: supported
  target_ids:
  - GO:0034044
  summary: Exact GO class and parent match the record. Sanchatjate names the Chs5/6
    complex; Wang calls the corresponding Chs5/ChAP coat exomer. The maintained definition
    does not claim a fixed five-subunit stoichiometry.
  evidence_ids:
  - record
  - root55-sources-go
  - root55-sources-GO0034044-ancestors
  - root55-sources-PMC1635352-html
  - root55-sources-PMC2064389
- assessment_id: composition
  area: grounding
  topic: Valid five named classes and one resolved family
  outcome: concern
  target_ids:
  - GO:0034044
  summary: All five reference proteins and exact-gene query identities agree. Chs5
    has an exact homologous-family mapping corroborated by the complete reviewed member
    set. IPR015374 is broader than each individual ChAP class and is withheld as an
    exact replacement.
  evidence_ids:
  - record
  - root55-sources-ipr-IPR052827
  - root55-sources-chs5-reviewed
  - root55-sources-ipr-IPR015374
  - root55-sources-protein-Q12114
  - root55-sources-protein-P40955
  - root55-sources-protein-Q05029
  - root55-sources-protein-Q08754
  - root55-sources-protein-P36122
  - root55-sources-protein-P11076
  - root55-sources-gene-CHS5
  - root55-sources-gene-CHS6
  - root55-sources-gene-BCH1
  - root55-sources-gene-BUD7
  - root55-sources-gene-BCH2
- assessment_id: formation
  area: grounding
  topic: Direct Chs5 dependence exceeds generic scaffold membership
  outcome: concern
  target_ids:
  - GO:0034044
  summary: The role identifies a scaffold and the graph says assembles-with, but the
    directly measured loss of ChAP coassociation in chs5-deletion extracts and stable
    TGN retention dependence are not stated. These are bounded structure-level results,
    separate from whether Chs3 cargo reaches the surface.
  evidence_ids:
  - record
  - schema
  - root55-sources-PMC1635352-html
  - root55-sources-PMC5290816-html
  - root55-sources-PMC1409733-html
- assessment_id: graph
  area: graph
  topic: Supported associations and external recruiting GTPase
  outcome: supported
  target_ids:
  - GO:0034044
  summary: All Chs5-ChAP membership/association edges, TGN localization and selective
    export are supported in the declared source scopes. Native UniProt prose includes
    Arf1 in a membrane-associated assembly, whereas purified Chs5/ChAP complexes form
    before Arf1 addition; the maintained external-regulator boundary is defensible.
    NONMECHANISTIC scope avoids claiming a complete coat mechanism.
  evidence_ids:
  - record
  - graphs
  - root55-sources-PMC1635352-html
  - root55-sources-PMC5290816-html
  - root55-sources-PMC1409733-html
  - root55-sources-PMC2064389
  - root55-sources-protein-Q12114
  - root55-sources-protein-P40955
  - root55-sources-protein-Q05029
  - root55-sources-protein-Q08754
  - root55-sources-protein-P36122
  - root55-sources-protein-P11076
- assessment_id: scope
  area: scope
  topic: Yeast reference and assay scopes
  outcome: supported
  target_ids:
  - GO:0034044
  summary: S288C reference accessions are distinct from Sanchatjate DDY1810-derived
    purification strains and Wang SEY6210/CWY strains and baculovirus expression system.
    Huranova strain details live in an unread appendix; inspected methods specify
    growth and FRAP conditions. COMMON is a qualitative category; no prevalence census
    is claimed.
  evidence_ids:
  - record
  - schema
  - root55-sources-PMC1635352-html
  - root55-sources-PMC5290816-html
  - root55-sources-PMC2064389
  - root55-sources-tax-4932
  - root55-sources-tax-559292
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0034044
  summary: Every maintained field, evidence row, component/example, graph edge, discussion
    and history entry was read. Optional unpopulated slots are not defects. Scientific
    status/history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root55-sources-go
  - root55-sources-doi-10.1038_sj.emboj.7601007
  - root55-sources-doi-10.1083_jcb.200605106
  - root55-sources-doi-10.1091_mbc.e06-03-0210
  - root55-sources-doi-10.15252_embr.201540795
findings:
- finding_id: F1
  issue_key: exomer-chs5-exact-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the verified Chs5 family mapping
  description: The Chs5 scaffold remains label-only under an open exact-family task,
    although native IPR052827 names its whole-protein family and Q12114 plus the complete
    reviewed member set corroborate the homologous class.
  target_ids:
  - GO:0034044
  field_paths:
  - components[0].grounding_status
  - components[0].grounding_notes
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root55-sources-ipr-IPR052827
  - root55-sources-chs5-reviewed
  - root55-sources-protein-Q12114
  - root55-sources-protein-P40955
  - root55-sources-protein-Q05029
  - root55-sources-protein-Q08754
  - root55-sources-protein-P36122
  - root55-sources-protein-P11076
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/exomer_complex.yaml
    role: maintained scientific record
  rule_id: Exact constituent-class grounding
  native_severity: minor
  normalization_reason: A bounded actionable class mapping under the existing explicit
    task; the complex identity and named protein examples remain supported.
- finding_id: F2
  issue_key: exomer-chs5-bounded-complex-integrity
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Record the experimentally tested Chs5 scaffold dependence
  description: Sanchatjate sec12 and Figure5 report that Chs6-TAP association with
    Bch1,Bud7 and Bch2 depends on Chs5 in the tested extracts. Huranova adds a distinct
    Chs5-dependent stable TGN retention result. The current generic scaffold role/assembles-with
    graph does not preserve these tested conditional relationships.
  target_ids:
  - GO:0034044
  field_paths:
  - components[0].role
  - causal_graphs[0]
  evidence_ids:
  - record
  - schema
  - graphs
  - root55-sources-PMC1635352-html
  - root55-sources-PMC5290816-html
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/exomer_complex.yaml
    role: maintained scientific record
  rule_id: Resolvable source-backed scaffold dependence
  native_severity: minor
  normalization_reason: A bounded omission of direct physical-complex evidence in
    an otherwise correct scaffold representation; optional complete mechanisms are
    not required.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0034044
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/exomer_complex.yaml
    role: maintained scientific record
  description: Ground Chs5 with IPR052827 and narrow the open task to individual ChAP
    mappings; keep the four paralog-specific rows distinct.
  acceptance_checks:
  - Do not derive exact identity solely from the generated unchecked InterPro description.
  - Do not apply shared IPR015374 to all four rows as if it distinguished their paralog
    classes.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0034044
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/exomer_complex.yaml
    role: maintained scientific record
  description: Add the specifically assayed Chs5-dependent physical association result
    and, if represented, distinguish stable membrane retention from complex coassociation.
    Retain assay and strain context; do not turn every cargo phenotype into physical
    essentiality.
  acceptance_checks:
  - Anchor association to Chs6-TAP purification in the reported wild-type/deletion
    backgrounds.
  - Preserve the observation that loss of individual ChAPs can leave the remaining
    complex associated.
  - Keep UNKNOWN for unestablished universal formation necessity; any scoped inference
    must state its scope.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw datasets, atomic coordinates, sequence alignments or supplemental
  files were reanalyzed. Body reading is bounded by the exact evidence locators.
- Huranova supplemental strain table and raw figure data were not read. Primary-body
  scopes are declared per source; no universal quantitative stoichiometry or whole-fungi
  cargo specificity is inferred.
- Native UniProt includes Arf1 in its subunit prose; primary purification/reconstitution
  supports the narrower stable Chs5/ChAP core used here. Shared ChAP family membership
  is not an exact paralog mapping.
- The local absence being assessed is confined to the entire inspected target roles/graph
  and explicit existing grounding task, not a claim that no related corpus record
  exists.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations and issue-bearing reviews
  alike.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
