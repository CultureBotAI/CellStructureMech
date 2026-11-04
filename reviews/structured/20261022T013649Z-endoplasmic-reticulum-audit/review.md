# Endoplasmic reticulum identity, source and compartment review

- Review: 20261022T013649Z-endoplasmic-reticulum-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:09:08Z
- Finished UTC: 2026-10-22T01:36:49Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed in the endoplasmic reticulum record within the explicitly documented source scopes.

## Scope And Provenance

Entire single maintained target; exact identity, hierarchy, component/protein scope, organism contexts, cited evidence and every graph edge.

Selection: Target 7 of batch twenty-seven; strict uncovered path order on fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005783 | data/structures/membrane_organelle/endoplasmic_reticulum.yaml | maintained | endoplasmic reticulum |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Initial sandbox protein-check attempt | failed | False | GO:0005783 | Sandbox DNS unavailable; resolved by the documented successful retry. |
| Focused native verify | passed | True | GO:0005783 | The focused native identity/coverage check passed; it does not by itself establish biological membership. |
| Focused native causal-graphs | passed | True | GO:0005783 | The focused native identity/coverage check passed; it does not by itself establish biological membership. |
| Focused native schema | passed | True | GO:0005783 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005783 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005783 | Native UniProt is used as the structured protein adapter. No iModulon dataset or expression-module inference is needed to assess these cited physical/functional experiments; UPR evidence is kept at the primary paper scope. |
| Claim-level scientific review | passed | True | GO:0005783 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005783 | 15 of 16 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID14562095, DOI10.1038/nature02026 and Global analysis of protein localization in budding yeast. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005783 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005783 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005783 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005783 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005783 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### ER, membrane and lumen distinctions

identity: supported. Targets: GO:0005783.

The target exact GO definition and stated kind denote the whole ER organelle. The exact ER synonym is native. GO0043231 directly lists ER as an is-a child; GO0012505 lists it as a part. Membrane, lumen and Sec61 topology remains distinct.

### Budding yeast model and experimental scope

scope: supported. Targets: GO:0005783.

The species4932 identity is exact. COMMON is qualitative occurrence rather than a numerical survey. The canonical example is limited to Sec61-dependent protein entry, while UPR/ERAD is separately sourced. Stirling Table1 names multiple backgrounds and mutant contexts; the review does not silently assign all experiments to one sequenced reference strain.

### Constituent bilayer and optional molecular repertoire

grounding: supported. Targets: GO:0005783.

The LIPID row is a collective boundary material, not one identified chemical species. The exact whole-membrane GO grounding matches that component scope; Sec61 is a defined protein complex rather than an entire organelle or phenotype. Its gene set agrees explicitly with GO0005784.

### Formation necessity versus protein/cell function

evidence: unknown. Targets: GO:0005783.

Collective membrane constitution supports the defining bilayer row. No individual lipid-species necessity is demonstrated. Sec61 remains UNKNOWN: mutant translocation defects and null lethality do not show loss of ER formation.

### Three exact subunit examples and evidence placement

grounding: supported. Targets: GO:0005783.

The three primary reviewed accession/name/gene/taxon tuples and single-entry claims are verified. GO0005784 specifically identifies yeast Sec61p/Sbh1p/Sss1p; Stirling provides direct yeast Sec61 membrane/function evidence. Identity-only notes correctly limit accession inference; SSS1 experimental-location attribution is exactly what UniProt attaches to Huh. The latter is secondary annotation linkage, not a new independent SSS1-image verification.

### Protein entry and coordinated quality control

evidence: supported. Targets: GO:0005783.

GO0005784 and Stirling support co/post-translational channel context and yeast entry/insertion. Travers complete abstract supports UPR/ERAD coordination and misfolded-protein disposal. The function/graph descriptions remain quality-control specific despite the shorter broad-synonym ERAD label; no different process identity is inferred.

### Every descriptive ER edge

graph: supported. Targets: GO:0005783.

All five NONMECHANISTIC edges preserve membrane enclosure/parthood, Sec61 membrane embedding/protein entry, and reciprocal UPR/ERAD coordination. They do not assert an exhaustive translocation or retrotranslocation cycle.

### Full target and honest optional gaps

completeness: supported. Targets: GO:0005783.

All target fields and edges were read. The target asserts no images, physical measurements, trait links or verbatim snippets. Open molecular inventories remain explicit optional gaps; source-access limits do not become invented defects. PROPOSED status and append-only historical decisions are preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/endoplasmic_reticulum.yaml; Entire maintained target including history, component and protein examples, all evidence and graph edges, discussions | context_only | All target bytes were read. Scientific content, status and histories remain unchanged. |
| policy | docs/CURATION.md; Structure identity, is-a versus parthood, constituent versus associated machinery, narrow evidence | context_only | The whole organelle, limiting membrane and enclosed region remain distinct. Enzyme activity and gene viability do not establish organelle-formation necessity. |
| protein-contract | src/cellstructuremech/schema/cellstructuremech.yaml; Component.protein_examples and ProteinExample lines448–468; component essentiality contract | context_only | Protein examples require paired biological context; native accession verification alone is not proof of structure membership. Formation necessity differs from protein function and cell viability. |
| neighbor-endoplasmic_reticulum_lumen | data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| neighbor-endoplasmic_reticulum_membrane | data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| neighbor-endosome | data/structures/membrane_organelle/endosome.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| root27-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005788,GO:0005789,GO:0005784,GO:0043231,GO:0012505,GO:0043233,GO:0016020,GO:0030968,GO:0036503,GO:0090114,GO:0030127,GO:0005768,GO:0010008,GO:0031904,GO:0005771,GO:0016197,GO:0000813,GO:0000814,GO:0000815; All20 identifiers, active flags, names, definitions, synonyms, comments and returned immediate child relations | supports | Twenty active GO terms were read in full. Exact ER/endosome, membrane/lumen, Sec61, ESCRT, transport and COPII definitions and synonyms support the scoped identities. GO0005784 explicitly names the yeast Sec61p/Sbh1p/Sss1p core. GO0036503 is now named ERAD quality control pathway, with ERAD pathway retained as a broad synonym; the record description specifically identifies misfolded-protein quality control. Returned child links support direct relations only; broader membrane/lumen classes may require transitive or definition-based inference. |
| root27-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies Saccharomyces cerevisiae at species4932; its rank and fungal lineage agree with the target. This does not certify any particular experimental strain or numerical prevalence. |
| root27-sources-stirling1992-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.3.2.129; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies Protein translocation mutants defective in the insertion of integral membrane proteins into the endoplasmic reticulum. by Stirling CJ, Rothblatt J, Hosobuchi M, Deshaies R, Schekman R.; PMID1550957, DOI10.1091/mbc.3.2.129. The complete primary abstract distinguishes old substrate-selective sec alleles from newly selected restrictive sec61/sec65 mutants, and reports Sec61 membrane localization. It supports yeast protein insertion and translocation, not a complete modern translocon structure or organelle-formation knockout. |
| root27-sources-travers2000-meta-exact | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A10847680%20AND%20SRC%3AMED; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies Functional and genomic analyses reveal an essential coordination between the unfolded protein response and ER-associated degradation. by Travers KJ, Patil CK, Wodicka L, Lockhart DJ, Weissman JS, Walter P.; PMID10847680, DOI10.1016/s0092-8674(00)80835-1. The complete primary abstract supports reciprocal UPR/ERAD coordination: intact UPR supports efficient ERAD, induction increases capacity, ERAD loss induces UPR, and combined loss reduces viability. This is functional/transcriptional evidence, not localization of every machinery component or formation necessity. |
| root27-sources-huh2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A14562095%20AND%20SRC%3AMED; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies Global analysis of protein localization in budding yeast. by Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK.; PMID14562095, DOI10.1038/nature02026. The complete primary abstract describes chromosomal GFP localization across yeast proteins. It establishes study scope, not a direct SSS1-specific result; the exact SSS1 citation link is checked in native UniProt separately. |
| root27-sources-stirling1992-page129 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/f89735edf303/mbc00060-0006.png; Original primary page129 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | Title, full abstract and opening Introduction inspected directly in the original scan; old substrate-selective mutants are distinguished from newly restrictive sec61/sec65 alleles. |
| root27-sources-stirling1992-page130 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/55f33db3a3fc/mbc00060-0007.png; Original primary page130 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | Complete Table1 and Introduction continuation read; the experimental strains are explicitly named and not assumed to be the reference S288C accession strain. The strain/media paragraph and opening methods are read; subsequent methods are outside this scan scope. |
| root27-sources-stirling1992-page137 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/b76f0a0c7375/mbc00060-0014.png; Original primary page137 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | The SEC61 coding/viability Results are read. Lethality of the sec61 null and mutation effects establish protein/cell function, not proof that the ER organelle cannot form. |
| root27-sources-stirling1992-page138 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/a2683aa00787/mbc00060-0015.png; Original primary page138 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | The Identification and Localization of Sec61p Results begin here; antiserum and fractionation analysis are read. Fig6 and its caption are visible but the nucleotide sequence is not independently reannotated. |
| root27-sources-stirling1992-page139 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/694d066200ac/mbc00060-0016.png; Original primary page139 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | Localization Results conclude: Sec61p is solubilized by Triton, fractionates with ER material, and shows ER-pattern immunofluorescence. Fig7/caption and the beginning of Discussion were viewed; hydropathy predictions are not modern structure validation. |
| root27-sources-stirling1992-page140 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/8f3b5e3aa4a2/mbc00060-0017.png; Original primary page140 scan from PMC275513; visually read entire page at native resolution, with analysis bounded as described | supports | Complete Fig8 and caption and continuing Discussion read: the original fractionation/blot supports integral ER membrane localization, with different strains/conditions specified. Densities are not quantified; later Discussion is outside this scope. |
| root27-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxId, scientificName, rank and lineage | supports | ENA identifies taxon559292 as Saccharomyces cerevisiae S288C, strain rank. Native protein examples therefore use an exact strain name, while the canonical organism is the broader species. |
| root27-sources-protein-P32915 | https://rest.uniprot.org/uniprotkb/P32915.json; Primary accession, entryType, protein names, all gene tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and exact Huh citation where present | supports | P32915 is a primary reviewed entry for SEC61, taxon559292, with the recorded protein name and exact gene token. The entry identifies ER membrane localization and Sec61-related function. Its own SUBUNIT annotation explicitly names SEC61, SBH1 and SSS1 as the heterotrimeric Sec61 core. |
| root27-sources-query-SEC61 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ASEC61%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Complete returned results, size500; exact gene/taxon/status and single-entry count | supports | The complete reviewed gene_exact:SEC61 AND taxonomy_id:559292 response returns one entry, P32915, whose own primary gene token agrees. This confirms current query cardinality, not biological membership by itself. |
| root27-sources-protein-P52870 | https://rest.uniprot.org/uniprotkb/P52870.json; Primary accession, entryType, protein names, all gene tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and exact Huh citation where present | supports | P52870 is a primary reviewed entry for SBH1, taxon559292, with the recorded protein name and exact gene token. The entry identifies ER membrane localization and Sec61-related function. The SBH1/SSS1 SUBUNIT prose contains SSH1 where the native GO Sec61 definition names SEC61; this inconsistent annotation wording is not used to infer a different complex. The exact GO definition and record sources retain the Sec61 core. |
| root27-sources-query-SBH1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ASBH1%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Complete returned results, size500; exact gene/taxon/status and single-entry count | supports | The complete reviewed gene_exact:SBH1 AND taxonomy_id:559292 response returns one entry, P52870, whose own primary gene token agrees. This confirms current query cardinality, not biological membership by itself. |
| root27-sources-protein-P35179 | https://rest.uniprot.org/uniprotkb/P35179.json; Primary accession, entryType, protein names, all gene tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and exact Huh citation where present | supports | P35179 is a primary reviewed entry for SSS1, taxon559292, with the recorded protein name and exact gene token. The entry identifies ER membrane localization and Sec61-related function. The SSS1 SUBCELLULAR LOCATION explicitly attaches ECO0000269 and PMID14562095 to ER membrane localization; the underlying individual GFP image was not independently recovered. The SBH1/SSS1 SUBUNIT prose contains SSH1 where the native GO Sec61 definition names SEC61; this inconsistent annotation wording is not used to infer a different complex. The exact GO definition and record sources retain the Sec61 core. |
| root27-sources-query-SSS1 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=gene_exact%3ASSS1%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue; Complete returned results, size500; exact gene/taxon/status and single-entry count | supports | The complete reviewed gene_exact:SSS1 AND taxonomy_id:559292 response returns one entry, P35179, whose own primary gene token agrees. This confirms current query cardinality, not biological membership by itself. |
| root27-sources-huh2003-primary-pdf | https://www.weizmann.ac.il/molgen/loqate/sites/molgen.loqate/files/huh.pdf; Original primary PDF pp690–691, Methods construction/imaging/colocalization subsections; abstract separately read in MED | supports | Directly read the original paper Methods on pp690–691: chromosomal C-terminal GFP tagging, ATCC201388 haploid background, microscopy and colocalization refinement using the other mating background. This bounds the large-scale assay; no SSS1-specific original image or all-row dataset audit is claimed. |
| native-verify-network-attempt | /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml --verify; Original failed sandbox attempt log | context_only | Exit1: sandbox DNS could not resolve UniProt after three network retries. This infrastructure result is retained; the network-enabled retry below passed. |
| native-verify | /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml --verify; Entire focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml --causal-graphs; Entire focused native output | supports | data/structures/membrane_organelle/endoplasmic_reticulum.yaml  (GO:0005783)<br>  yeast_er_protein_biogenesis_quality_control	sec61_translocon_complex	COVERED	-&gt;sec61_translocon_complex (UniProtKB:P32915, UniProtKB:P52870, UniProtKB:P35179)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/endoplasmic_reticulum.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/endoplasmic_reticulum.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/endoplasmic_reticulum.yaml --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/endoplasmic_reticulum.yaml --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/endoplasmic_reticulum.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 15 of 16 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID14562095, DOI10.1038/nature02026 and Global analysis of protein localization in budding yeast. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Native ontology terms, taxonomy and proteins were read directly; definitions and transitive parentage do not imply an unavailable direct ontology edge. Individual molecular formation necessity and exhaustive composition remain unknown.
- Primary access is bounded: Stirling original scans129,130,137–140 were read, including Table1 and Fig8; pages131–136 and141–142 and underlying measurements were not independently examined. Travers is complete-abstract only; its DOI request failed, and no full-body claim is made.
- Species scope and reference-strain accessions do not identify every primary experimental strain. Historical authorship, previous searches and prior review dispositions are not independently recertified.
- Huh primary Methods were read, but the exact SSS1 microscopy image/dataset row was not independently recovered; its ER-location experimental citation is verified as a UniProt attribution. Conflicting SSH1 tokens in SBH1/SSS1 SUBUNIT prose are not used to override the explicit yeast Sec61 core in GO.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly authorizes a bundle for every uncovered target, including honest no-finding reviews. No scientific record edit is authorized.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T013649Z-endoplasmic-reticulum-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Endoplasmic reticulum identity, source and compartment review
started_at: '2026-10-22T01:09:08Z'
finished_at: '2026-10-22T01:36:49Z'
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
summary: No concrete curation defect observed in the endoplasmic reticulum record
  within the explicitly documented source scopes.
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
  - path: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    sha256: 7444c8cf7718146040d73012227215c8767122fa1bd1988e2b66e8278c6dcb2f
    role: target
  - path: data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml
    sha256: 8ffe704fef493506e494107aba2b583e563921f2f12a6e98748971f64976b622
    role: context
  - path: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    sha256: 599774aca4e215829787fe1a818ef52bd2c3772b48c289505d14417c05d0f679
    role: context
  - path: data/structures/membrane_organelle/endosome.yaml
    sha256: 7eb3c5b8022e63698365a49990831c7609d649c6024002eb19f6a28cdfff38a8
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0005783
  path: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
  label: endoplasmic reticulum
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target; exact identity, hierarchy, component/protein
    scope, organism contexts, cited evidence and every graph edge.
  selection: Target 7 of batch twenty-seven; strict uncovered path order on fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005783
checks:
- check_id: native-verify-network-attempt
  name: Initial sandbox protein-check attempt
  status: failed
  required: false
  target_ids:
  - GO:0005783
  command: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    --verify
  exit_code: 1
  summary: Sandbox DNS unavailable; resolved by the documented successful retry.
  evidence_ids:
  - native-verify-network-attempt
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0005783
  command: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    --verify
  exit_code: 0
  summary: The focused native identity/coverage check passed; it does not by itself
    establish biological membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005783
  command: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    --causal-graphs
  exit_code: 0
  summary: The focused native identity/coverage check passed; it does not by itself
    establish biological membership.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005783
  command: just validate data/structures/membrane_organelle/endoplasmic_reticulum.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005783
  command: just validate-strict data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005783
  summary: Native UniProt is used as the structured protein adapter. No iModulon dataset
    or expression-module inference is needed to assess these cited physical/functional
    experiments; UPR evidence is kept at the primary paper scope.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005783
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - protein-contract
  - neighbor-endoplasmic_reticulum_lumen
  - neighbor-endoplasmic_reticulum_membrane
  - neighbor-endosome
  - root27-sources-go
  - root27-sources-tax4932
  - root27-sources-stirling1992-meta
  - root27-sources-travers2000-meta-exact
  - root27-sources-huh2003-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
  - root27-sources-tax559292
  - root27-sources-protein-P32915
  - root27-sources-query-SEC61
  - root27-sources-protein-P52870
  - root27-sources-query-SBH1
  - root27-sources-protein-P35179
  - root27-sources-query-SSS1
  - root27-sources-huh2003-primary-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005783
  summary: '15 of 16 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID14562095, DOI10.1038/nature02026 and Global analysis of protein localization
    in budding yeast. Bibliographic identity is resolved; scientific scope remains
    restricted to the separately documented abstract/body inspections. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.'
  evidence_ids:
  - target-curies
  - root27-sources-huh2003-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005783
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005783
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005783
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005783
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005783
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
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
  locator: Entire maintained target including history, component and protein examples,
    all evidence and graph edges, discussions
  accessed_at: '2026-10-22T01:15:39Z'
  support: context_only
  summary: All target bytes were read. Scientific content, status and histories remain
    unchanged.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Structure identity, is-a versus parthood, constituent versus associated
    machinery, narrow evidence
  accessed_at: '2026-10-22T01:15:39Z'
  support: context_only
  summary: The whole organelle, limiting membrane and enclosed region remain distinct.
    Enzyme activity and gene viability do not establish organelle-formation necessity.
- evidence_id: protein-contract
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component.protein_examples and ProteinExample lines448–468; component essentiality
    contract
  accessed_at: '2026-10-22T01:15:39Z'
  support: context_only
  summary: Protein examples require paired biological context; native accession verification
    alone is not proof of structure membership. Formation necessity differs from protein
    function and cell viability.
- evidence_id: neighbor-endoplasmic_reticulum_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:15:39Z'
  support: context_only
  summary: These neighboring records receive separate reviews. Their unrelated source
    claims are not incorporated as proof for this target.
- evidence_id: neighbor-endoplasmic_reticulum_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:15:39Z'
  support: context_only
  summary: These neighboring records receive separate reviews. Their unrelated source
    claims are not incorporated as proof for this target.
- evidence_id: neighbor-endosome
  kind: record_content
  reference: data/structures/membrane_organelle/endosome.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:15:39Z'
  support: context_only
  summary: These neighboring records receive separate reviews. Their unrelated source
    claims are not incorporated as proof for this target.
- evidence_id: root27-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005788,GO:0005789,GO:0005784,GO:0043231,GO:0012505,GO:0043233,GO:0016020,GO:0030968,GO:0036503,GO:0090114,GO:0030127,GO:0005768,GO:0010008,GO:0031904,GO:0005771,GO:0016197,GO:0000813,GO:0000814,GO:0000815
  locator: All20 identifiers, active flags, names, definitions, synonyms, comments
    and returned immediate child relations
  accessed_at: '2026-10-22T01:10:57.099012Z'
  support: supports
  summary: Twenty active GO terms were read in full. Exact ER/endosome, membrane/lumen,
    Sec61, ESCRT, transport and COPII definitions and synonyms support the scoped
    identities. GO0005784 explicitly names the yeast Sec61p/Sbh1p/Sss1p core. GO0036503
    is now named ERAD quality control pathway, with ERAD pathway retained as a broad
    synonym; the record description specifically identifies misfolded-protein quality
    control. Returned child links support direct relations only; broader membrane/lumen
    classes may require transitive or definition-based inference.
  snapshot_sha256: ea021845778f0e54effaf639a0ab1d071361b49a8060eac188ad56277eae8350
- evidence_id: root27-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: ENA identifies Saccharomyces cerevisiae at species4932; its rank and fungal
    lineage agree with the target. This does not certify any particular experimental
    strain or numerical prevalence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root27-sources-stirling1992-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.3.2.129
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.099383Z'
  support: supports
  summary: Native MED identifies Protein translocation mutants defective in the insertion
    of integral membrane proteins into the endoplasmic reticulum. by Stirling CJ,
    Rothblatt J, Hosobuchi M, Deshaies R, Schekman R.; PMID1550957, DOI10.1091/mbc.3.2.129.
    The complete primary abstract distinguishes old substrate-selective sec alleles
    from newly selected restrictive sec61/sec65 mutants, and reports Sec61 membrane
    localization. It supports yeast protein insertion and translocation, not a complete
    modern translocon structure or organelle-formation knockout.
  snapshot_sha256: bc349d2da602b21d01dd29d83db504f59222406f3393a8dea8054d3fc4f848ba
- evidence_id: root27-sources-travers2000-meta-exact
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A10847680%20AND%20SRC%3AMED
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:12:25.463362Z'
  support: supports
  summary: 'Native MED identifies Functional and genomic analyses reveal an essential
    coordination between the unfolded protein response and ER-associated degradation.
    by Travers KJ, Patil CK, Wodicka L, Lockhart DJ, Weissman JS, Walter P.; PMID10847680,
    DOI10.1016/s0092-8674(00)80835-1. The complete primary abstract supports reciprocal
    UPR/ERAD coordination: intact UPR supports efficient ERAD, induction increases
    capacity, ERAD loss induces UPR, and combined loss reduces viability. This is
    functional/transcriptional evidence, not localization of every machinery component
    or formation necessity.'
  snapshot_sha256: e2d7b11b945e3159da7a0e1b7e3b600f06e8f0d1ec27da7cf2314296279b361c
- evidence_id: root27-sources-huh2003-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A14562095%20AND%20SRC%3AMED
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.099655Z'
  support: supports
  summary: Native MED identifies Global analysis of protein localization in budding
    yeast. by Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea
    EK.; PMID14562095, DOI10.1038/nature02026. The complete primary abstract describes
    chromosomal GFP localization across yeast proteins. It establishes study scope,
    not a direct SSS1-specific result; the exact SSS1 citation link is checked in
    native UniProt separately.
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: root27-sources-stirling1992-page129
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/f89735edf303/mbc00060-0006.png
  locator: Original primary page129 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.367993Z'
  support: supports
  summary: Title, full abstract and opening Introduction inspected directly in the
    original scan; old substrate-selective mutants are distinguished from newly restrictive
    sec61/sec65 alleles.
  snapshot_sha256: e593c63dc67e772fd28b3332411e80793ba9d9ec0a828ebc19735125d53f88b8
- evidence_id: root27-sources-stirling1992-page130
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/55f33db3a3fc/mbc00060-0007.png
  locator: Original primary page130 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.368737Z'
  support: supports
  summary: Complete Table1 and Introduction continuation read; the experimental strains
    are explicitly named and not assumed to be the reference S288C accession strain.
    The strain/media paragraph and opening methods are read; subsequent methods are
    outside this scan scope.
  snapshot_sha256: d3362a4527251af8da220c3164757d26148c1edad8ab6f4f54cc66be6833d733
- evidence_id: root27-sources-stirling1992-page137
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/b76f0a0c7375/mbc00060-0014.png
  locator: Original primary page137 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.369340Z'
  support: supports
  summary: The SEC61 coding/viability Results are read. Lethality of the sec61 null
    and mutation effects establish protein/cell function, not proof that the ER organelle
    cannot form.
  snapshot_sha256: ab1ffab6cdf5b7955663c903b6158182effa9bfd0845cb6121f2cbb01698b56e
- evidence_id: root27-sources-stirling1992-page138
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/a2683aa00787/mbc00060-0015.png
  locator: Original primary page138 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.369507Z'
  support: supports
  summary: The Identification and Localization of Sec61p Results begin here; antiserum
    and fractionation analysis are read. Fig6 and its caption are visible but the
    nucleotide sequence is not independently reannotated.
  snapshot_sha256: 32d58645d26060035af1178eb5876043b1497a548410ddfe3635d8cad117eeac
- evidence_id: root27-sources-stirling1992-page139
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/694d066200ac/mbc00060-0016.png
  locator: Original primary page139 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.715334Z'
  support: supports
  summary: 'Localization Results conclude: Sec61p is solubilized by Triton, fractionates
    with ER material, and shows ER-pattern immunofluorescence. Fig7/caption and the
    beginning of Discussion were viewed; hydropathy predictions are not modern structure
    validation.'
  snapshot_sha256: b7684416c694989dfc41afdd05cc51d8498b823af6fd7a98b676868654e27405
- evidence_id: root27-sources-stirling1992-page140
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/642c/275513/8f3b5e3aa4a2/mbc00060-0017.png
  locator: Original primary page140 scan from PMC275513; visually read entire page
    at native resolution, with analysis bounded as described
  accessed_at: '2026-10-22T01:13:54.756969Z'
  support: supports
  summary: 'Complete Fig8 and caption and continuing Discussion read: the original
    fractionation/blot supports integral ER membrane localization, with different
    strains/conditions specified. Densities are not quantified; later Discussion is
    outside this scope.'
  snapshot_sha256: 2e05803d7f0719e16200e9b22fd30da2e9f7687e55454baeb8bc755cc91464f4
- evidence_id: root27-sources-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T01:10:58.507227Z'
  support: supports
  summary: ENA identifies taxon559292 as Saccharomyces cerevisiae S288C, strain rank.
    Native protein examples therefore use an exact strain name, while the canonical
    organism is the broader species.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root27-sources-protein-P32915
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32915.json
  locator: Primary accession, entryType, protein names, all gene tokens, organism,
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and exact Huh citation where present
  accessed_at: '2026-10-22T01:10:58.509342Z'
  support: supports
  summary: P32915 is a primary reviewed entry for SEC61, taxon559292, with the recorded
    protein name and exact gene token. The entry identifies ER membrane localization
    and Sec61-related function. Its own SUBUNIT annotation explicitly names SEC61,
    SBH1 and SSS1 as the heterotrimeric Sec61 core.
  snapshot_sha256: e696d3f3947e47d88105469ae6ad609c5cd7120b4f157c1c40c5199b89a08fe7
- evidence_id: root27-sources-query-SEC61
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ASEC61%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Complete returned results, size500; exact gene/taxon/status and single-entry
    count
  accessed_at: '2026-10-22T01:10:59.272988Z'
  support: supports
  summary: The complete reviewed gene_exact:SEC61 AND taxonomy_id:559292 response
    returns one entry, P32915, whose own primary gene token agrees. This confirms
    current query cardinality, not biological membership by itself.
  snapshot_sha256: a80fbd253be8e1f8f9c0766b833a3856b555da67b68ee59fa8a0bcab842d7f22
- evidence_id: root27-sources-protein-P52870
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P52870.json
  locator: Primary accession, entryType, protein names, all gene tokens, organism,
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and exact Huh citation where present
  accessed_at: '2026-10-22T01:10:58.532719Z'
  support: supports
  summary: P52870 is a primary reviewed entry for SBH1, taxon559292, with the recorded
    protein name and exact gene token. The entry identifies ER membrane localization
    and Sec61-related function. The SBH1/SSS1 SUBUNIT prose contains SSH1 where the
    native GO Sec61 definition names SEC61; this inconsistent annotation wording is
    not used to infer a different complex. The exact GO definition and record sources
    retain the Sec61 core.
  snapshot_sha256: cf77dd1b1fd866e112463f02fe04f1537704b0427adf9c263235d6b5d512c50e
- evidence_id: root27-sources-query-SBH1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ASBH1%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Complete returned results, size500; exact gene/taxon/status and single-entry
    count
  accessed_at: '2026-10-22T01:10:59.280916Z'
  support: supports
  summary: The complete reviewed gene_exact:SBH1 AND taxonomy_id:559292 response returns
    one entry, P52870, whose own primary gene token agrees. This confirms current
    query cardinality, not biological membership by itself.
  snapshot_sha256: 183f292c5ac6e8b09e6098ae11ed3ac081996f076d232099b94cf31290290792
- evidence_id: root27-sources-protein-P35179
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P35179.json
  locator: Primary accession, entryType, protein names, all gene tokens, organism,
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments and exact Huh citation where present
  accessed_at: '2026-10-22T01:10:59.077768Z'
  support: supports
  summary: P35179 is a primary reviewed entry for SSS1, taxon559292, with the recorded
    protein name and exact gene token. The entry identifies ER membrane localization
    and Sec61-related function. The SSS1 SUBCELLULAR LOCATION explicitly attaches
    ECO0000269 and PMID14562095 to ER membrane localization; the underlying individual
    GFP image was not independently recovered. The SBH1/SSS1 SUBUNIT prose contains
    SSH1 where the native GO Sec61 definition names SEC61; this inconsistent annotation
    wording is not used to infer a different complex. The exact GO definition and
    record sources retain the Sec61 core.
  snapshot_sha256: 7509af9595b06816944dd360b1d2d68f982a785ae57e0ea4af77034899bc7d71
- evidence_id: root27-sources-query-SSS1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=gene_exact%3ASSS1%20AND%20taxonomy_id%3A559292%20AND%20reviewed%3Atrue
  locator: Complete returned results, size500; exact gene/taxon/status and single-entry
    count
  accessed_at: '2026-10-22T01:10:59.295547Z'
  support: supports
  summary: The complete reviewed gene_exact:SSS1 AND taxonomy_id:559292 response returns
    one entry, P35179, whose own primary gene token agrees. This confirms current
    query cardinality, not biological membership by itself.
  snapshot_sha256: 7660708b556cf364be5e383109a901641e5fc0b7a06e760fc6a4005de939f5b6
- evidence_id: root27-sources-huh2003-primary-pdf
  kind: primary_source
  reference: https://www.weizmann.ac.il/molgen/loqate/sites/molgen.loqate/files/huh.pdf
  locator: Original primary PDF pp690–691, Methods construction/imaging/colocalization
    subsections; abstract separately read in MED
  accessed_at: '2026-10-22T01:12:25.824788Z'
  support: supports
  summary: 'Directly read the original paper Methods on pp690–691: chromosomal C-terminal
    GFP tagging, ATCC201388 haploid background, microscopy and colocalization refinement
    using the other mating background. This bounds the large-scale assay; no SSS1-specific
    original image or all-row dataset audit is claimed.'
  snapshot_sha256: 664a4205db1726d46b115fa5a856b3683da811f2a0112ba26d4bada34d40f65c
- evidence_id: native-verify-network-attempt
  kind: validation
  reference: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    --verify
  locator: Original failed sandbox attempt log
  accessed_at: '2026-10-22T01:11:11.723338Z'
  support: context_only
  summary: 'Exit1: sandbox DNS could not resolve UniProt after three network retries.
    This infrastructure result is retained; the network-enabled retry below passed.'
  snapshot_sha256: 73763bbc4f094a615f51f18dd414116a673da5a512c72ec84fe63042e52f4b1f
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    --verify
  locator: Entire focused native output
  accessed_at: '2026-10-22T01:11:30.702112Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    --causal-graphs
  locator: Entire focused native output
  accessed_at: '2026-10-22T01:11:31.315414Z'
  support: supports
  summary: "data/structures/membrane_organelle/endoplasmic_reticulum.yaml  (GO:0005783)\n\
    \  yeast_er_protein_biogenesis_quality_control\tsec61_translocon_complex\tCOVERED\t\
    ->sec61_translocon_complex (UniProtKB:P32915, UniProtKB:P52870, UniProtKB:P35179)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: f30d61043dddf56222b899514c5210e8aebd0e346c858257dac85e4937bb79af
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/endoplasmic_reticulum.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:09:10Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/endoplasmic_reticulum.yaml'
  snapshot_sha256: 1672f1954c9311641d8598d58c1ebb9331283acbddfdedba2d774eca1a0735ff
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/endoplasmic_reticulum.yaml
    --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:09:11Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/endoplasmic_reticulum.yaml\
    \ --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endoplasmic_reticulum-strict.tsv"
  snapshot_sha256: 1b0605066e4e9f9979361e28254e71f33c02b113d38c5d717b0563dc73151d49
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/endoplasmic_reticulum.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '15 of 16 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID14562095, DOI10.1038/nature02026 and Global analysis of protein localization
    in budding yeast. Bibliographic identity is resolved; scientific scope remains
    restricted to the separately documented abstract/body inspections. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.'
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
  topic: ER, membrane and lumen distinctions
  outcome: supported
  target_ids:
  - GO:0005783
  summary: The target exact GO definition and stated kind denote the whole ER organelle.
    The exact ER synonym is native. GO0043231 directly lists ER as an is-a child;
    GO0012505 lists it as a part. Membrane, lumen and Sec61 topology remains distinct.
  evidence_ids:
  - record
  - root27-sources-go
  - policy
- assessment_id: scope
  area: scope
  topic: Budding yeast model and experimental scope
  outcome: supported
  target_ids:
  - GO:0005783
  summary: The species4932 identity is exact. COMMON is qualitative occurrence rather
    than a numerical survey. The canonical example is limited to Sec61-dependent protein
    entry, while UPR/ERAD is separately sourced. Stirling Table1 names multiple backgrounds
    and mutant contexts; the review does not silently assign all experiments to one
    sequenced reference strain.
  evidence_ids:
  - record
  - root27-sources-tax4932
  - root27-sources-stirling1992-meta
  - root27-sources-travers2000-meta-exact
  - root27-sources-huh2003-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
  - root27-sources-huh2003-primary-pdf
- assessment_id: composition
  area: grounding
  topic: Constituent bilayer and optional molecular repertoire
  outcome: supported
  target_ids:
  - GO:0005783
  summary: The LIPID row is a collective boundary material, not one identified chemical
    species. The exact whole-membrane GO grounding matches that component scope; Sec61
    is a defined protein complex rather than an entire organelle or phenotype. Its
    gene set agrees explicitly with GO0005784.
  evidence_ids:
  - record
  - root27-sources-go
  - policy
  - root27-sources-tax559292
  - root27-sources-protein-P32915
  - root27-sources-query-SEC61
  - root27-sources-protein-P52870
  - root27-sources-query-SBH1
  - root27-sources-protein-P35179
  - root27-sources-query-SSS1
- assessment_id: necessity
  area: evidence
  topic: Formation necessity versus protein/cell function
  outcome: unknown
  target_ids:
  - GO:0005783
  summary: 'Collective membrane constitution supports the defining bilayer row. No
    individual lipid-species necessity is demonstrated. Sec61 remains UNKNOWN: mutant
    translocation defects and null lethality do not show loss of ER formation.'
  evidence_ids:
  - record
  - root27-sources-go
  - protein-contract
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
  - root27-sources-huh2003-primary-pdf
- assessment_id: proteins
  area: grounding
  topic: Three exact subunit examples and evidence placement
  outcome: supported
  target_ids:
  - GO:0005783
  summary: The three primary reviewed accession/name/gene/taxon tuples and single-entry
    claims are verified. GO0005784 specifically identifies yeast Sec61p/Sbh1p/Sss1p;
    Stirling provides direct yeast Sec61 membrane/function evidence. Identity-only
    notes correctly limit accession inference; SSS1 experimental-location attribution
    is exactly what UniProt attaches to Huh. The latter is secondary annotation linkage,
    not a new independent SSS1-image verification.
  evidence_ids:
  - record
  - root27-sources-go
  - root27-sources-tax559292
  - root27-sources-protein-P32915
  - root27-sources-query-SEC61
  - root27-sources-protein-P52870
  - root27-sources-query-SBH1
  - root27-sources-protein-P35179
  - root27-sources-query-SSS1
  - root27-sources-huh2003-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
  - root27-sources-huh2003-primary-pdf
- assessment_id: function
  area: evidence
  topic: Protein entry and coordinated quality control
  outcome: supported
  target_ids:
  - GO:0005783
  summary: GO0005784 and Stirling support co/post-translational channel context and
    yeast entry/insertion. Travers complete abstract supports UPR/ERAD coordination
    and misfolded-protein disposal. The function/graph descriptions remain quality-control
    specific despite the shorter broad-synonym ERAD label; no different process identity
    is inferred.
  evidence_ids:
  - record
  - root27-sources-go
  - root27-sources-stirling1992-meta
  - root27-sources-travers2000-meta-exact
  - root27-sources-huh2003-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
  - root27-sources-huh2003-primary-pdf
- assessment_id: graph
  area: graph
  topic: Every descriptive ER edge
  outcome: supported
  target_ids:
  - GO:0005783
  summary: All five NONMECHANISTIC edges preserve membrane enclosure/parthood, Sec61
    membrane embedding/protein entry, and reciprocal UPR/ERAD coordination. They do
    not assert an exhaustive translocation or retrotranslocation cycle.
  evidence_ids:
  - record
  - root27-sources-go
  - root27-sources-stirling1992-meta
  - root27-sources-travers2000-meta-exact
  - root27-sources-huh2003-meta
  - root27-sources-stirling1992-page129
  - root27-sources-stirling1992-page130
  - root27-sources-stirling1992-page137
  - root27-sources-stirling1992-page138
  - root27-sources-stirling1992-page139
  - root27-sources-stirling1992-page140
  - root27-sources-huh2003-primary-pdf
- assessment_id: coverage
  area: completeness
  topic: Full target and honest optional gaps
  outcome: supported
  target_ids:
  - GO:0005783
  summary: All target fields and edges were read. The target asserts no images, physical
    measurements, trait links or verbatim snippets. Open molecular inventories remain
    explicit optional gaps; source-access limits do not become invented defects. PROPOSED
    status and append-only historical decisions are preserved.
  evidence_ids:
  - record
  - policy
  - root27-sources-go
  - root27-sources-stirling1992-meta
  - root27-sources-travers2000-meta-exact
  - root27-sources-huh2003-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Native ontology terms, taxonomy and proteins were read directly; definitions and
  transitive parentage do not imply an unavailable direct ontology edge. Individual
  molecular formation necessity and exhaustive composition remain unknown.
- 'Primary access is bounded: Stirling original scans129,130,137–140 were read, including
  Table1 and Fig8; pages131–136 and141–142 and underlying measurements were not independently
  examined. Travers is complete-abstract only; its DOI request failed, and no full-body
  claim is made.'
- Species scope and reference-strain accessions do not identify every primary experimental
  strain. Historical authorship, previous searches and prior review dispositions are
  not independently recertified.
- Huh primary Methods were read, but the exact SSS1 microscopy image/dataset row was
  not independently recovered; its ER-location experimental citation is verified as
  a UniProt attribution. Conflicting SSH1 tokens in SBH1/SSS1 SUBUNIT prose are not
  used to override the explicit yeast Sec61 core in GO.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly authorizes a bundle for every uncovered target, including honest
  no-finding reviews. No scientific record edit is authorized.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
