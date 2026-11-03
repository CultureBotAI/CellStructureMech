# Inclusion identity, composition and evidence review

- Review: 20261021T103321Z-gas-vesicle-shell-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:13:11Z
- Finished UTC: 2026-10-21T10:33:21Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The gas-vesicle shell identity, composition, strain example and structural/mechanical graph are supported. One minor finding records a verified exact GvpA family grounding; conditional GvpC formation necessity remains unresolved.

## Scope And Provenance

Entire single record with exact authority identities, declared source-reading scopes, protein checks where applicable and component/function/graph boundaries.

Selection: Target 3 in batch nineteen; exact sorted uncovered path at frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033172 | data/structures/inclusion/gas_vesicle_shell.yaml | maintained | gas vesicle shell |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0033172 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Native protein causal-graphs | passed | True | GO:0033172 | Focused native command passed; identity/coverage result is distinct from scientific membership. |
| Focused native schema | passed | True | GO:0033172 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033172 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0033172 | 10 identifiers OK; 5 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0033172 | No expression-module or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | GO:0033172 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0033172 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033172 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033172 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033172 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0033172 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Shell material separated from the gas-filled organelle

identity: supported. Targets: GO:0033172.

Exact identity, synonyms, kind and parthood are supported. The related membrane name does not assert a lipid bilayer. Mature GvpA/GvpC shell material is separated from the whole organelle and its accessory assembly machinery.

### Persistent GvpA wall and qualified GvpC coat

evidence: supported. Targets: GO:0033172.

The primary structural study supports the GvpA wall and GvpC on the outside of characterized cyanobacterial shells. Walsby review and Bayro NMR abstracts support their stated coarse claims. Accessory factors are not assumed to be permanent shell constituents merely because they contact GvpA; the discussion preserves an evidence-dependent boundary, not an exhaustive absence claim.

### Specific GvpA family versus broader and repeat xrefs

grounding: concern. Targets: GO:0033172.

The component lacks an explicit GvpA family grounding despite a verified exact family. Its broad PF00741 graph xref does not carry that equivalence. GvpC candidates checked here are repeats and must not be promoted to whole-protein groundings merely by label. The bounded GvpA grounding follow-up does not assert a wrong existing xref.

### Correct unreviewed strain-paired sequence examples

evidence: supported. Targets: GO:0033172.

Both accession, gene, protein-name, taxon and unreviewed-status pairs match current native entries. Exact reviewed queries return zero for the declared strain; this is only the stated query result. Automated annotations and a preliminary WGS source are not independent microscopy or primary membership evidence, consistent with the maintained identity-only notes.

### Structural constitution and conditional requirement kept distinct

evidence: unknown. Targets: GO:0033172.

GvpA is the observed principal wall polymer, with mutational assembly sensitivity in the tested hybrid expression system. GvpC stripping/rebinding and pressure resistance show a mechanical role after assembly; they do not establish or refute conditional requirements during de novo formation across lineages and pressures. The exact CONDITIONAL classification remains unresolved, without a new defect finding or a universal DISPENSABLE replacement.

### Variable occurrence and an exact structural-study strain

scope: supported. Targets: GO:0033172.

The Walsby review abstract supports variable bacterial and archaeal occurrence; Dutka Results S4/S6 separately identify the haloarchaeal Halobacterium salinarum comparison. No prevalence census is claimed. Dutka key resources and native taxonomy agree on CCAP1403/13F. The Anabaena cylindrica sequence-example strain is separately identified, not substituted for the cryo-ET organism.

### Supported structural and mechanical causal links

graph: supported. Targets: GO:0033172.

The graph links polymer assembly, shell formation, external coating and experimentally supported strengthening, then gas permeability/water exclusion and buoyancy. This is more than static parthood. The direct permeability study measures oxygen movement with a diffusion model; the cryo-ET study supports structure rather than independently measuring gas transport. Gas retention is understood as a water-excluding gas-filled space, not trapping or actively storing a fixed gas dose.

### Bounded record-level coverage

completeness: supported. Targets: GO:0033172.

The entire maintained record and cited claim contexts were inspected at the stated source scopes. Exact additional polymer inventories, numerical properties, images, traits and expanded mechanisms are optional. No verbatim quotation requires repair, and no status or history rewrite is proposed. This bounded review does not assert exhaustive literature completeness.

## Findings

### F1: Record the verified exact GvpA family grounding

minor / open / confirmed; issue key: gas-vesicle-shell-gvpa-family-grounding.

The named GvpA constituent has no grounding or explicit unresolved-grounding discussion. Native IPR047870 specifically denotes GvpA, whereas the existing graph xref PF00741 covers a broader GvpA-like family including GvpJ. Add the exact family at the component; retain broader graph xrefs as related context. The GvpC repeat entries are not whole-protein equivalents.

## Recommended Actions And Acceptance Checks

### A1

Ground the GvpA component to verified InterPro IPR047870 with exact family provenance and appropriate grounding status. Preserve the distinction between exact family identity, concrete protein examples and related graph xrefs.

- Reconfirm IPR047870 is the GvpA-specific family, with the broader GvpA-like entry kept distinct.
- Do not promote PF01304 or the GvpC repeat entries to whole-protein equivalence.
- Use separately authorized guarded curation, append-only history, focused validators, identifier/product checks and regeneration.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/inclusion/gas_vesicle_shell.yaml; Entire maintained YAML including history, all evidence notes, components, functions, graph edges and discussions | context_only | All maintained fields were read. No scientific edit or mapping-status promotion is made. |
| policy | docs/CURATION.md; Exact identity, claim-level evidence, material versus localization grounding, and component assembly-essentiality contract | context_only | Family identity, concrete protein examples and structure membership are separate; activity and viability are not by themselves formation assays. Optional inventories are not mandatory. |
| root19-sources-gas-shell-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031411,GO:0033172; Both returned definitions, synonyms, comment and inverse part_of child relation | supports | The shell has the exact GO identity and wall synonym, a related membrane synonym, and explicit parthood of the gas vesicle. The containing organelle is not lipid-membrane bounded. |
| whole-neighbor | data/structures/inclusion/gas_vesicle.yaml; Entire neighbor read for shell/whole and accessory-assembly boundary only | context_only | The whole gas-vesicle record separately carries accessory assembly interactions and a structural dataset; these are not silently imported as shell constituents or independently reviewed here. |
| prior-reassessment | reviews/structured/20261014T054100Z-gas-vesicle-finding-reassessment/review.yaml; Summary, assessments, findings and limitations of the whole-organelle reassessment | context_only | Historical rejection of a categorical GvpC-essentiality inference was read. This review independently checks current sources and does not reinstate that finding or re-review the neighbor. |
| root19-sources-NCBITaxon-2 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Bacteria at domain rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root19-sources-NCBITaxon-2157 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Archaea at domain rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root19-sources-NCBITaxon-315271 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/315271; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Dolichospermum flos-aquae CCAP 1403/13F at strain rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root19-sources-NCBITaxon-2692880 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2692880; Exact taxId, scientificName, rank, lineage and relevant alternative names | supports | Native ENA taxonomy identifies Anabaena cylindrica FACHB-318 at strain rank. Only this taxon's identity and names are asserted by this row, not occurrence or experimental stock identity. |
| root19-sources-PMID-8177173 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8177173%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Gas vesicles. PMID 8177173; DOI 10.1128/mr.58.1.94-144.1994. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root19-sources-PMID-22147705 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A22147705%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies An amyloid organelle, solid-state NMR evidence for cross-β assembly of gas vesicles. PMID 22147705; DOI 10.1074/jbc.m111.313049. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root19-sources-PMID-1510555 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A1510555%20AND%20SRC%3AMED; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Gas vesicles are strengthened by the outer-surface protein, GvpC. PMID 1510555; DOI 10.1007/bf00245155. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root19-sources-doi-10.1016_j.str.2023.03.011 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.str.2023.03.011; Exact native title, authors, year, source MED, DOI/PMID and abstract fields | supports | Native citation identifies Structure of Anabaena flos-aquae gas vesicles revealed by cryo-ET. PMID 37040766; DOI 10.1016/j.str.2023.03.011. Exact bibliographic fields and the complete returned abstract were inspected; this row does not attest a full-text read. |
| root19-sources-jats-PMC10185304 | https://pmc-oa-opendata.s3.amazonaws.com/PMC10185304.1/PMC10185304.1.xml; Complete Introduction S1, Results S3-S7, Discussion S8 including limitations S9; Methods S15/S17 and key-resource strain table. No image pixels, volumes, supplements or remaining computational/cloning Methods reanalysis. | supports | Dutka2023 directly resolves the corrugated GvpA shell and a surface GvpC spiral in purified Ana gas vesicles. Native versus stripped subtomogram averages, cross-linking and mechanical simulations have distinct roles. The model uses rigid-body fitting of a homologous GvpA structure; detailed nucleation, GvpC junctions and exact atomic interactions remain unresolved. The resource table identifies Dolichospermum flos-aquae CCAP1403/13F. |
| root19-sources-hayes1992-publisher | https://link.springer.com/article/10.1007/BF00245155; Exact title/authors/year and complete Abstract section Abs1-section; article-access boundary | supports | The complete Hayes1992 publisher abstract reports reduced collapse resistance after GvpC removal and recovery after recombinant GvpC rebinding. This is a mature-shell mechanical experiment, not a de novo formation-necessity test. The page exposes abstract and access information, not the full paper. |
| root19-sources-permeability1992-crossref | https://api.crossref.org/works/10.1099/00221287-138-4-837; Complete native work metadata | supports | Crossref verifies the exact1992 DOI, title, three authors, journal, volume138, issue4 and pages837-845. This bibliographic response supplies no experimental body. |
| root19-sources-permeability1992-browser | https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-138-4-837; Publisher browser text: complete Abstract lines48-52, title and authors; Full-Text loader is not a recovered body | supports | Walsby, Revsbech and Griffel1992 describe oxygen-microelectrode measurements comparing gas-vesicle and agar films, followed by diffusion-model inference of wall permeability. The maintained record claims only direct oxygen-movement quantification. Rapid equilibration does not imply active gas storage. Numerical results and raw data are not imported. |
| root19-sources-UniProtKB-A0ABR7ZBW9 | https://rest.uniprot.org/uniprotkb/A0ABR7ZBW9.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is A0ABR7ZBW9, UniProtKB unreviewed (TrEMBL), organism taxon 2692880. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root19-sources-UniProtKB-A0ABR7ZCB1 | https://rest.uniprot.org/uniprotkb/A0ABR7ZCB1.json; Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR LOCATION and source references | supports | The primary accession is A0ABR7ZCB1, UniProtKB unreviewed (TrEMBL), organism taxon 2692880. Exact name/gene tokens, evidence-qualified location comments and linked publication metadata were inspected. Database identity is not independently a formation-necessity experiment. |
| root19-sources-query-gvpA-2692880 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AgvpA%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 0 entries: none. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root19-sources-query-gvpC-2692880 | https://rest.uniprot.org/uniprotkb/search?format=json&amp;size=500&amp;query=%28gene_exact%3AgvpC%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29; Complete returned result list for gene_exact, taxonomy_id and reviewed:true | supports | Current exact-gene/taxon reviewed query returned 0 entries: none. Returned gene tokens were checked against each native entry; zero reviewed matches do not invalidate a separately identified unreviewed sequence. |
| root19-sources-PF00741 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00741/; Native accession, type, name, description, hierarchy and integrated member signatures | supports | PF00741 is a broader gas-vesicle-protein family including GvpJ; its node xref is related family context, not an exact GvpA grounding. |
| root19-sources-PF01304 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01304/; Native accession, type, name, description, hierarchy and integrated member signatures | supports | PF01304 is a GvpC repeated domain, not the entire protein. Its related node xref is valid without equating the repeat to the constituent. |
| root19-sources-IPR000638 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000638/; Native accession, type, name, description, hierarchy and integrated member signatures | supports | The GvpA-like parent includes GvpJ/GvpM relatives and explicitly parents the specific GvpA family. |
| root19-sources-IPR047870 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047870/; Native accession, type, name, description, hierarchy and integrated member signatures | supports | IPR047870 is a family explicitly specific to GvpA and integrated with HAMAP MF_00576. The verified native GvpA accession carries this entry. |
| root19-sources-IPR050530 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050530/; Native accession, type, name, description, hierarchy and integrated member signatures | supports | Despite its short name, this broader entry description includes GvpJ and GvpM; it is not selected as the exact GvpA family. Its description is flagged LLM-generated and unchecked. |
| root19-sources-IPR002003 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002003/; Native accession, type, name, description, hierarchy and integrated member signatures | supports | The native GvpC entry has type repeat and integrates PF01304/TIGR02641; the label alone does not make it a whole-protein family. |
| root19-sources-IPR018185 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018185/; Native accession, type, name, description, hierarchy and integrated member signatures | supports | IPR018185 is another GvpC repeat/signature entry. These checked candidates do not establish a whole-GvpC family or an exhaustive absence claim. |
| root19-sources-legacy-PMC3271001 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3271001/; Actual source-access response, not article content | context_only | This attempted route did not provide the article body: PMC responses are browser challenges, the Bayro DOI response is a publisher redirect page, and the two journal routes returned403. Metadata/abstract and accessible Dutka evidence are kept at their actual reading tiers. |
| root19-sources-legacy-PMC372955 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC372955/; Actual source-access response, not article content | context_only | This attempted route did not provide the article body: PMC responses are browser challenges, the Bayro DOI response is a publisher redirect page, and the two journal routes returned403. Metadata/abstract and accessible Dutka evidence are kept at their actual reading tiers. |
| root19-sources-bayro2012-doi | https://doi.org/10.1074/jbc.M111.313049; Actual source-access response, not article content | context_only | This attempted route did not provide the article body: PMC responses are browser challenges, the Bayro DOI response is a publisher redirect page, and the two journal routes returned403. Metadata/abstract and accessible Dutka evidence are kept at their actual reading tiers. |
| root19-sources-walsby1994-publisher | https://journals.asm.org/doi/10.1128/mr.58.1.94-144.1994; Actual source-access response, not article content | context_only | This attempted route did not provide the article body: PMC responses are browser challenges, the Bayro DOI response is a publisher redirect page, and the two journal routes returned403. Metadata/abstract and accessible Dutka evidence are kept at their actual reading tiers. |
| root19-sources-permeability1992-publisher | https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-138-4-837; Actual source-access response, not article content | context_only | This attempted route did not provide the article body: PMC responses are browser challenges, the Bayro DOI response is a publisher redirect page, and the two journal routes returned403. Metadata/abstract and accessible Dutka evidence are kept at their actual reading tiers. |
| native-verify | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml --verify; Exact focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml --causal-graphs; Exact focused native output | supports | data/structures/inclusion/gas_vesicle_shell.yaml  (GO:0033172)<br>  gvpa_gvpc_shell_barrier	gvpa	COVERED	-&gt;gvpa (UniProtKB:A0ABR7ZBW9)<br>  gvpa_gvpc_shell_barrier	gvpc	COVERED	-&gt;gvpc (UniProtKB:A0ABR7ZCB1)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/inclusion/gas_vesicle_shell.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/inclusion/gas_vesicle_shell.yaml |
| strict-result | just validate-strict data/structures/inclusion/gas_vesicle_shell.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/gas_vesicle_shell-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/inclusion/gas_vesicle_shell.yaml --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/gas_vesicle_shell-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/gas_vesicle_shell-strict.tsv |
| target-curies | just check-curies-strict; data/structures/inclusion/gas_vesicle_shell.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 10 of15 collected target identifiers returned OK in this fresh base resolver run. Residuals: PMID:1510555: UNREACHABLE; resolved by evidence root19-sources-PMID-1510555; PMID:22147705: UNREACHABLE; resolved by evidence root19-sources-PMID-22147705; PMID:8177173: UNREACHABLE; resolved by evidence root19-sources-PMID-8177173; Pfam:PF00741: SKIPPED; resolved by evidence root19-sources-PF00741; Pfam:PF01304: SKIPPED; resolved by evidence root19-sources-PF01304. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Walsby1994 and Bayro2012 were read at complete native abstract and bibliographic scope. Their full bodies were not recovered from the attempted public routes. Hayes1992 and the1992 permeability paper were read at publisher abstract scope, not full Methods or raw measurements.
- Dutka2023 was read at the specified full text sections. Its rigid-body homology fitting, stripping experiment and mechanical simulation are distinct evidence types. No raw tomogram, NMR spectrum, figure pixels or supplementary model files were reanalysed.
- The whole-gas-vesicle neighbor and its historical reassessment were context only. No new review of its dataset or accessory assembly graph is claimed. Concrete protein identities remain unreviewed and identity-only.
- GvpC conditional assembly necessity is an explicit unknown, not an inferred error. The checked repeat families do not establish an exhaustive absence of a whole-GvpC family identifier.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization; identifier transport and label-adapter limits remain explicit.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized one review for every uncovered target, including a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T103321Z-gas-vesicle-shell-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Inclusion identity, composition and evidence review
started_at: '2026-10-21T10:13:11Z'
finished_at: '2026-10-21T10:33:21Z'
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
summary: The gas-vesicle shell identity, composition, strain example and structural/mechanical
  graph are supported. One minor finding records a verified exact GvpA family grounding;
  conditional GvpC formation necessity remains unresolved.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/inclusion/gas_vesicle.yaml
    sha256: 7bafef7a0ce0bc91ac7189ed216f4d2cdfc786cebbd47eeb5645c5408267f7cb
    role: context
  - path: data/structures/inclusion/gas_vesicle_shell.yaml
    sha256: 06f0f2aa709e62b9e46e2e38d2ce26692fc0d8e0fe16a78d998aa7a51b1e0ae6
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
  - path: reviews/structured/20261014T054100Z-gas-vesicle-finding-reassessment/review.yaml
    sha256: 029b6009a71f95bed1f267a5f2928550139311a16a8fcd353db3198194548f3a
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/score_causal_graphs.py
    sha256: 5ffe450c5b37c3dc3b0e62672caf0d99b358c8249fcc98a8c4fc7d78e8cd0d2f
    role: context
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0033172
  path: data/structures/inclusion/gas_vesicle_shell.yaml
  label: gas vesicle shell
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/gas_vesicle_shell.yaml
    role: maintained scientific record
scope:
  description: Entire single record with exact authority identities, declared source-reading
    scopes, protein checks where applicable and component/function/graph boundaries.
  selection: Target 3 in batch nineteen; exact sorted uncovered path at frozen fresh-main
    revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033172
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml
    --verify
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native command passed; identity/coverage result is distinct from
    scientific membership.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just validate data/structures/inclusion/gas_vesicle_shell.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just validate-strict data/structures/inclusion/gas_vesicle_shell.yaml --out
    /private/tmp/cellstructure-batch19-20261021-9bkzflrr/gas_vesicle_shell-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0033172
  summary: 10 identifiers OK; 5 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - root19-sources-PMID-1510555
  - root19-sources-PMID-22147705
  - root19-sources-PMID-8177173
  - root19-sources-PF00741
  - root19-sources-PF01304
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0033172
  summary: No expression-module or transcriptomic inference is made by this structural
    review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033172
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root19-sources-gas-shell-go
  - whole-neighbor
  - prior-reassessment
  - root19-sources-NCBITaxon-2
  - root19-sources-NCBITaxon-2157
  - root19-sources-NCBITaxon-315271
  - root19-sources-NCBITaxon-2692880
  - root19-sources-PMID-8177173
  - root19-sources-PMID-22147705
  - root19-sources-PMID-1510555
  - root19-sources-doi-10.1016_j.str.2023.03.011
  - root19-sources-jats-PMC10185304
  - root19-sources-hayes1992-publisher
  - root19-sources-permeability1992-crossref
  - root19-sources-permeability1992-browser
  - root19-sources-UniProtKB-A0ABR7ZBW9
  - root19-sources-UniProtKB-A0ABR7ZCB1
  - root19-sources-query-gvpA-2692880
  - root19-sources-query-gvpC-2692880
  - root19-sources-PF00741
  - root19-sources-PF01304
  - root19-sources-IPR000638
  - root19-sources-IPR047870
  - root19-sources-IPR050530
  - root19-sources-IPR002003
  - root19-sources-IPR018185
  - root19-sources-legacy-PMC3271001
  - root19-sources-legacy-PMC372955
  - root19-sources-bayro2012-doi
  - root19-sources-walsby1994-publisher
  - root19-sources-permeability1992-publisher
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0033172
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/inclusion/gas_vesicle_shell.yaml
  locator: Entire maintained YAML including history, all evidence notes, components,
    functions, graph edges and discussions
  accessed_at: '2026-10-21T10:21:17Z'
  support: context_only
  summary: All maintained fields were read. No scientific edit or mapping-status promotion
    is made.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, claim-level evidence, material versus localization grounding,
    and component assembly-essentiality contract
  accessed_at: '2026-10-21T10:21:17Z'
  support: context_only
  summary: Family identity, concrete protein examples and structure membership are
    separate; activity and viability are not by themselves formation assays. Optional
    inventories are not mandatory.
- evidence_id: root19-sources-gas-shell-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031411,GO:0033172
  locator: Both returned definitions, synonyms, comment and inverse part_of child
    relation
  accessed_at: '2026-10-21T10:14:45.437812Z'
  support: supports
  summary: The shell has the exact GO identity and wall synonym, a related membrane
    synonym, and explicit parthood of the gas vesicle. The containing organelle is
    not lipid-membrane bounded.
  snapshot_sha256: ad6c8c92958bfdb85c7422292bdce1ace8fce968688f8f6764494b01853897d4
- evidence_id: whole-neighbor
  kind: record_content
  reference: data/structures/inclusion/gas_vesicle.yaml
  locator: Entire neighbor read for shell/whole and accessory-assembly boundary only
  accessed_at: '2026-10-21T10:21:17Z'
  support: context_only
  summary: The whole gas-vesicle record separately carries accessory assembly interactions
    and a structural dataset; these are not silently imported as shell constituents
    or independently reviewed here.
- evidence_id: prior-reassessment
  kind: record_content
  reference: reviews/structured/20261014T054100Z-gas-vesicle-finding-reassessment/review.yaml
  locator: Summary, assessments, findings and limitations of the whole-organelle reassessment
  accessed_at: '2026-10-21T10:21:17Z'
  support: context_only
  summary: Historical rejection of a categorical GvpC-essentiality inference was read.
    This review independently checks current sources and does not reinstate that finding
    or re-review the neighbor.
- evidence_id: root19-sources-NCBITaxon-2
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:14:45.440368Z'
  support: supports
  summary: Native ENA taxonomy identifies Bacteria at domain rank. Only this taxon's
    identity and names are asserted by this row, not occurrence or experimental stock
    identity.
  snapshot_sha256: 7429617438ff0162ee4783c4c660f6127642e6ff686522e670c6ecf3a5b28816
- evidence_id: root19-sources-NCBITaxon-2157
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2157
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:14:45.440068Z'
  support: supports
  summary: Native ENA taxonomy identifies Archaea at domain rank. Only this taxon's
    identity and names are asserted by this row, not occurrence or experimental stock
    identity.
  snapshot_sha256: 9ddd1001f0c607eb9b7582ecd9e83d3d18a89ddf8e540ec75da7dc4c9939c6ae
- evidence_id: root19-sources-NCBITaxon-315271
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/315271
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:14:45.438007Z'
  support: supports
  summary: Native ENA taxonomy identifies Dolichospermum flos-aquae CCAP 1403/13F
    at strain rank. Only this taxon's identity and names are asserted by this row,
    not occurrence or experimental stock identity.
  snapshot_sha256: 8f2267f7f1758368a7a36f3fbe2ce4d83e27cbea825e483d1c195128fd0f880f
- evidence_id: root19-sources-NCBITaxon-2692880
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2692880
  locator: Exact taxId, scientificName, rank, lineage and relevant alternative names
  accessed_at: '2026-10-21T10:14:45.522664Z'
  support: supports
  summary: Native ENA taxonomy identifies Anabaena cylindrica FACHB-318 at strain
    rank. Only this taxon's identity and names are asserted by this row, not occurrence
    or experimental stock identity.
  snapshot_sha256: e4dab743ef84d8c29af966b0ff5c1625d544ad0b63ef3da600e945e569c1061d
- evidence_id: root19-sources-PMID-8177173
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8177173%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:14:46.184958Z'
  support: supports
  summary: Native citation identifies Gas vesicles. PMID 8177173; DOI 10.1128/mr.58.1.94-144.1994.
    Exact bibliographic fields and the complete returned abstract were inspected;
    this row does not attest a full-text read.
  snapshot_sha256: a3f99e655b2a17b96df629f0fdfd02358a2d88a5b7a6ae8157e52887b338ccb7
- evidence_id: root19-sources-PMID-22147705
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A22147705%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:14:46.171601Z'
  support: supports
  summary: Native citation identifies An amyloid organelle, solid-state NMR evidence
    for cross-β assembly of gas vesicles. PMID 22147705; DOI 10.1074/jbc.m111.313049.
    Exact bibliographic fields and the complete returned abstract were inspected;
    this row does not attest a full-text read.
  snapshot_sha256: df8e22a3dd5a02f4fa5b3be7e03d9f32b86e090bff4d5ee32fe20d01ecdcfd92
- evidence_id: root19-sources-PMID-1510555
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A1510555%20AND%20SRC%3AMED
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:14:46.198101Z'
  support: supports
  summary: Native citation identifies Gas vesicles are strengthened by the outer-surface
    protein, GvpC. PMID 1510555; DOI 10.1007/bf00245155. Exact bibliographic fields
    and the complete returned abstract were inspected; this row does not attest a
    full-text read.
  snapshot_sha256: 72f0e03c8a21c69a5da11a12c48fd8c69c16b3461cfb32930bc19da94ad8669c
- evidence_id: root19-sources-doi-10.1016_j.str.2023.03.011
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.str.2023.03.011
  locator: Exact native title, authors, year, source MED, DOI/PMID and abstract fields
  accessed_at: '2026-10-21T10:14:46.189161Z'
  support: supports
  summary: Native citation identifies Structure of Anabaena flos-aquae gas vesicles
    revealed by cryo-ET. PMID 37040766; DOI 10.1016/j.str.2023.03.011. Exact bibliographic
    fields and the complete returned abstract were inspected; this row does not attest
    a full-text read.
  snapshot_sha256: 1991640a5c9fd5fcf864d60e95bd30b3360799a9baca39fc49c5bfba9b0b2d5d
- evidence_id: root19-sources-jats-PMC10185304
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC10185304.1/PMC10185304.1.xml
  locator: Complete Introduction S1, Results S3-S7, Discussion S8 including limitations
    S9; Methods S15/S17 and key-resource strain table. No image pixels, volumes, supplements
    or remaining computational/cloning Methods reanalysis.
  accessed_at: '2026-10-21T10:15:35.958749Z'
  support: supports
  summary: Dutka2023 directly resolves the corrugated GvpA shell and a surface GvpC
    spiral in purified Ana gas vesicles. Native versus stripped subtomogram averages,
    cross-linking and mechanical simulations have distinct roles. The model uses rigid-body
    fitting of a homologous GvpA structure; detailed nucleation, GvpC junctions and
    exact atomic interactions remain unresolved. The resource table identifies Dolichospermum
    flos-aquae CCAP1403/13F.
  snapshot_sha256: 4047db6ae79c9d6de989d88eaeb47598151bf2a33e2a91c8b9875afb721c7060
- evidence_id: root19-sources-hayes1992-publisher
  kind: primary_source
  reference: https://link.springer.com/article/10.1007/BF00245155
  locator: Exact title/authors/year and complete Abstract section Abs1-section; article-access
    boundary
  accessed_at: '2026-10-21T10:15:37.060040Z'
  support: supports
  summary: The complete Hayes1992 publisher abstract reports reduced collapse resistance
    after GvpC removal and recovery after recombinant GvpC rebinding. This is a mature-shell
    mechanical experiment, not a de novo formation-necessity test. The page exposes
    abstract and access information, not the full paper.
  snapshot_sha256: e338871863ed5edc48fcb151b44cb20f97f6387c4036b309fda6e6ae3381f215
- evidence_id: root19-sources-permeability1992-crossref
  kind: database
  reference: https://api.crossref.org/works/10.1099/00221287-138-4-837
  locator: Complete native work metadata
  accessed_at: '2026-10-21T10:15:36.100913Z'
  support: supports
  summary: Crossref verifies the exact1992 DOI, title, three authors, journal, volume138,
    issue4 and pages837-845. This bibliographic response supplies no experimental
    body.
  snapshot_sha256: 70d372d8ad10f9d059a1bfc12614660bc8084a55d77246c31223e8fbd3148a28
- evidence_id: root19-sources-permeability1992-browser
  kind: primary_source
  reference: https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-138-4-837
  locator: 'Publisher browser text: complete Abstract lines48-52, title and authors;
    Full-Text loader is not a recovered body'
  accessed_at: '2026-10-21T10:17:35Z'
  support: supports
  summary: Walsby, Revsbech and Griffel1992 describe oxygen-microelectrode measurements
    comparing gas-vesicle and agar films, followed by diffusion-model inference of
    wall permeability. The maintained record claims only direct oxygen-movement quantification.
    Rapid equilibration does not imply active gas storage. Numerical results and raw
    data are not imported.
  snapshot_sha256: 81709e84dc426af2883c231f44d1e436848489c01c8846a07f260b846371c452
- evidence_id: root19-sources-UniProtKB-A0ABR7ZBW9
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0ABR7ZBW9.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:14:45.450739Z'
  support: supports
  summary: The primary accession is A0ABR7ZBW9, UniProtKB unreviewed (TrEMBL), organism
    taxon 2692880. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: 34d92f939cc1dc7899f4c142a659990a2a21ee3745864218f95778e92a569876
- evidence_id: root19-sources-UniProtKB-A0ABR7ZCB1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/A0ABR7ZCB1.json
  locator: Primary accession, entryType, proteinDescription, genes, organism, SUBCELLULAR
    LOCATION and source references
  accessed_at: '2026-10-21T10:14:46.112773Z'
  support: supports
  summary: The primary accession is A0ABR7ZCB1, UniProtKB unreviewed (TrEMBL), organism
    taxon 2692880. Exact name/gene tokens, evidence-qualified location comments and
    linked publication metadata were inspected. Database identity is not independently
    a formation-necessity experiment.
  snapshot_sha256: 7fb97f1d9559cd29d3a714a3e474c9b89c8a2fff0068708c4d41b12119aa2964
- evidence_id: root19-sources-query-gvpA-2692880
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AgvpA%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:14:46.936695Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 0 entries: none. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: 7e5118451ca023452db92758ff8788accbfe362c60551c059442b21eb3c6ce6c
- evidence_id: root19-sources-query-gvpC-2692880
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?format=json&size=500&query=%28gene_exact%3AgvpC%29%20AND%20%28taxonomy_id%3A2692880%29%20AND%20%28reviewed%3Atrue%29
  locator: Complete returned result list for gene_exact, taxonomy_id and reviewed:true
  accessed_at: '2026-10-21T10:14:47.032087Z'
  support: supports
  summary: 'Current exact-gene/taxon reviewed query returned 0 entries: none. Returned
    gene tokens were checked against each native entry; zero reviewed matches do not
    invalidate a separately identified unreviewed sequence.'
  snapshot_sha256: 75ce72662b3715249c0c38ae60cf28f0d5a2c8133776ba6b7e5d518050cffae2
- evidence_id: root19-sources-PF00741
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF00741/
  locator: Native accession, type, name, description, hierarchy and integrated member
    signatures
  accessed_at: '2026-10-21T10:15:36.598278Z'
  support: supports
  summary: PF00741 is a broader gas-vesicle-protein family including GvpJ; its node
    xref is related family context, not an exact GvpA grounding.
  snapshot_sha256: 094064b336ab239cf609df86bac5b25cc3ad373caa44cd1796ebd8a4bf4a4936
- evidence_id: root19-sources-PF01304
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF01304/
  locator: Native accession, type, name, description, hierarchy and integrated member
    signatures
  accessed_at: '2026-10-21T10:15:36.605265Z'
  support: supports
  summary: PF01304 is a GvpC repeated domain, not the entire protein. Its related
    node xref is valid without equating the repeat to the constituent.
  snapshot_sha256: ac3440f2567cdc7a520c86932e6e48572da87a6b929996f1e6825f1588ac08bb
- evidence_id: root19-sources-IPR000638
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000638/
  locator: Native accession, type, name, description, hierarchy and integrated member
    signatures
  accessed_at: '2026-10-21T10:16:40.247338Z'
  support: supports
  summary: The GvpA-like parent includes GvpJ/GvpM relatives and explicitly parents
    the specific GvpA family.
  snapshot_sha256: b8a432cd24b4028ffa38aa595c4f64ce3b73ef3b9eca03bc4b32315b2f698905
- evidence_id: root19-sources-IPR047870
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR047870/
  locator: Native accession, type, name, description, hierarchy and integrated member
    signatures
  accessed_at: '2026-10-21T10:16:40.900983Z'
  support: supports
  summary: IPR047870 is a family explicitly specific to GvpA and integrated with HAMAP
    MF_00576. The verified native GvpA accession carries this entry.
  snapshot_sha256: 0cd1400385b42f3e2e41ae75b7e5db55e227e5a7a1e3a561b9fc69349d395833
- evidence_id: root19-sources-IPR050530
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050530/
  locator: Native accession, type, name, description, hierarchy and integrated member
    signatures
  accessed_at: '2026-10-21T10:16:39.747925Z'
  support: supports
  summary: Despite its short name, this broader entry description includes GvpJ and
    GvpM; it is not selected as the exact GvpA family. Its description is flagged
    LLM-generated and unchecked.
  snapshot_sha256: cc3ca729aece182c5415a7eb34a6b2b813dd867864ce6cba3b32c4fc23eab0f6
- evidence_id: root19-sources-IPR002003
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002003/
  locator: Native accession, type, name, description, hierarchy and integrated member
    signatures
  accessed_at: '2026-10-21T10:16:39.752905Z'
  support: supports
  summary: The native GvpC entry has type repeat and integrates PF01304/TIGR02641;
    the label alone does not make it a whole-protein family.
  snapshot_sha256: d31616233044357ce15cb317a8bdef4507b3725e7a3b3cb575631e0f95377503
- evidence_id: root19-sources-IPR018185
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018185/
  locator: Native accession, type, name, description, hierarchy and integrated member
    signatures
  accessed_at: '2026-10-21T10:16:39.742876Z'
  support: supports
  summary: IPR018185 is another GvpC repeat/signature entry. These checked candidates
    do not establish a whole-GvpC family or an exhaustive absence claim.
  snapshot_sha256: 54cdbb1f2c04b33103217fd2d44fb827c0fd43350c97ef38dd081329ac6d25ef
- evidence_id: root19-sources-legacy-PMC3271001
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3271001/
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:16:39.090622Z'
  support: context_only
  summary: 'This attempted route did not provide the article body: PMC responses are
    browser challenges, the Bayro DOI response is a publisher redirect page, and the
    two journal routes returned403. Metadata/abstract and accessible Dutka evidence
    are kept at their actual reading tiers.'
  snapshot_sha256: 036ac5044f88fb4967bea59adfb9aa3bebab5782d738f4d56f590ae849e73220
- evidence_id: root19-sources-legacy-PMC372955
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC372955/
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:16:39.054812Z'
  support: context_only
  summary: 'This attempted route did not provide the article body: PMC responses are
    browser challenges, the Bayro DOI response is a publisher redirect page, and the
    two journal routes returned403. Metadata/abstract and accessible Dutka evidence
    are kept at their actual reading tiers.'
  snapshot_sha256: 2a19a24e6bcbc2a77a371f5139a79e30af68b3ef0e40e54e9ecd0481c9a1f73e
- evidence_id: root19-sources-bayro2012-doi
  kind: authority
  reference: https://doi.org/10.1074/jbc.M111.313049
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:17:49.570087Z'
  support: context_only
  summary: 'This attempted route did not provide the article body: PMC responses are
    browser challenges, the Bayro DOI response is a publisher redirect page, and the
    two journal routes returned403. Metadata/abstract and accessible Dutka evidence
    are kept at their actual reading tiers.'
  snapshot_sha256: bf92a6ce06f89491f9360db8373443cd27f14384cc760b7d91fcbb44205d6db2
- evidence_id: root19-sources-walsby1994-publisher
  kind: authority
  reference: https://journals.asm.org/doi/10.1128/mr.58.1.94-144.1994
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:17:49.100559Z'
  support: context_only
  summary: 'This attempted route did not provide the article body: PMC responses are
    browser challenges, the Bayro DOI response is a publisher redirect page, and the
    two journal routes returned403. Metadata/abstract and accessible Dutka evidence
    are kept at their actual reading tiers.'
  snapshot_sha256: 60e5718c3d522cd2c954a600222c2d5990b9ad3e8c7299b2fee3424dac4e0fec
- evidence_id: root19-sources-permeability1992-publisher
  kind: authority
  reference: https://www.microbiologyresearch.org/content/journal/micro/10.1099/00221287-138-4-837
  locator: Actual source-access response, not article content
  accessed_at: '2026-10-21T10:15:35.778285Z'
  support: context_only
  summary: 'This attempted route did not provide the article body: PMC responses are
    browser challenges, the Bayro DOI response is a publisher redirect page, and the
    two journal routes returned403. Metadata/abstract and accessible Dutka evidence
    are kept at their actual reading tiers.'
  snapshot_sha256: c3cc292edcd58301b0d60183cdba290b5b67ab2bc913b2b3fa3ab247cb981d04
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml
    --verify
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:15:37.775388Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/inclusion/gas_vesicle_shell.yaml
    --causal-graphs
  locator: Exact focused native output
  accessed_at: '2026-10-21T10:15:40.882416Z'
  support: supports
  summary: "data/structures/inclusion/gas_vesicle_shell.yaml  (GO:0033172)\n  gvpa_gvpc_shell_barrier\t\
    gvpa\tCOVERED\t->gvpa (UniProtKB:A0ABR7ZBW9)\n  gvpa_gvpc_shell_barrier\tgvpc\t\
    COVERED\t->gvpc (UniProtKB:A0ABR7ZCB1)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n\
    \     2  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     2  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 9e7d806f0c580e411b6b49c7ec0d01ce5bbdcbd0a6d719d8e37be21bb7bcea18
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/inclusion/gas_vesicle_shell.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:13Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/inclusion/gas_vesicle_shell.yaml'
  snapshot_sha256: 6ac95eec959d1bf3ec909749669200aca1dd86eff07059d38940ed59018a3364
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/inclusion/gas_vesicle_shell.yaml
    --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/gas_vesicle_shell-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:13:14Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/inclusion/gas_vesicle_shell.yaml\
    \ --out /private/tmp/cellstructure-batch19-20261021-9bkzflrr/gas_vesicle_shell-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch19-20261021-9bkzflrr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch19-20261021-9bkzflrr/gas_vesicle_shell-strict.tsv"
  snapshot_sha256: 1763ebcc28f3dc5a8b9a5811ae4459a7670d9c9657dee341c97bda113deb7b6a
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/inclusion/gas_vesicle_shell.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:21:17Z'
  support: supports
  summary: '10 of15 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: PMID:1510555: UNREACHABLE; resolved by evidence root19-sources-PMID-1510555;
    PMID:22147705: UNREACHABLE; resolved by evidence root19-sources-PMID-22147705;
    PMID:8177173: UNREACHABLE; resolved by evidence root19-sources-PMID-8177173; Pfam:PF00741:
    SKIPPED; resolved by evidence root19-sources-PF00741; Pfam:PF01304: SKIPPED; resolved
    by evidence root19-sources-PF01304. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Shell material separated from the gas-filled organelle
  outcome: supported
  target_ids:
  - GO:0033172
  summary: Exact identity, synonyms, kind and parthood are supported. The related
    membrane name does not assert a lipid bilayer. Mature GvpA/GvpC shell material
    is separated from the whole organelle and its accessory assembly machinery.
  evidence_ids:
  - root19-sources-gas-shell-go
  - root19-sources-jats-PMC10185304
  - whole-neighbor
  - record
- assessment_id: composition
  area: evidence
  topic: Persistent GvpA wall and qualified GvpC coat
  outcome: supported
  target_ids:
  - GO:0033172
  summary: The primary structural study supports the GvpA wall and GvpC on the outside
    of characterized cyanobacterial shells. Walsby review and Bayro NMR abstracts
    support their stated coarse claims. Accessory factors are not assumed to be permanent
    shell constituents merely because they contact GvpA; the discussion preserves
    an evidence-dependent boundary, not an exhaustive absence claim.
  evidence_ids:
  - root19-sources-jats-PMC10185304
  - root19-sources-hayes1992-publisher
  - root19-sources-PMID-8177173
  - root19-sources-PMID-22147705
  - root19-sources-PMID-1510555
  - record
  - policy
- assessment_id: grounding
  area: grounding
  topic: Specific GvpA family versus broader and repeat xrefs
  outcome: concern
  target_ids:
  - GO:0033172
  summary: The component lacks an explicit GvpA family grounding despite a verified
    exact family. Its broad PF00741 graph xref does not carry that equivalence. GvpC
    candidates checked here are repeats and must not be promoted to whole-protein
    groundings merely by label. The bounded GvpA grounding follow-up does not assert
    a wrong existing xref.
  evidence_ids:
  - root19-sources-PF00741
  - root19-sources-PF01304
  - root19-sources-IPR000638
  - root19-sources-IPR047870
  - root19-sources-IPR050530
  - root19-sources-IPR002003
  - root19-sources-IPR018185
  - root19-sources-UniProtKB-A0ABR7ZBW9
  - root19-sources-UniProtKB-A0ABR7ZCB1
  - record
  - policy
- assessment_id: protein-identities
  area: evidence
  topic: Correct unreviewed strain-paired sequence examples
  outcome: supported
  target_ids:
  - GO:0033172
  summary: Both accession, gene, protein-name, taxon and unreviewed-status pairs match
    current native entries. Exact reviewed queries return zero for the declared strain;
    this is only the stated query result. Automated annotations and a preliminary
    WGS source are not independent microscopy or primary membership evidence, consistent
    with the maintained identity-only notes.
  evidence_ids:
  - root19-sources-UniProtKB-A0ABR7ZBW9
  - root19-sources-UniProtKB-A0ABR7ZCB1
  - root19-sources-query-gvpA-2692880
  - root19-sources-query-gvpC-2692880
  - root19-sources-NCBITaxon-2
  - root19-sources-NCBITaxon-2157
  - root19-sources-NCBITaxon-315271
  - root19-sources-NCBITaxon-2692880
  - record
- assessment_id: assembly-necessity
  area: evidence
  topic: Structural constitution and conditional requirement kept distinct
  outcome: unknown
  target_ids:
  - GO:0033172
  summary: GvpA is the observed principal wall polymer, with mutational assembly sensitivity
    in the tested hybrid expression system. GvpC stripping/rebinding and pressure
    resistance show a mechanical role after assembly; they do not establish or refute
    conditional requirements during de novo formation across lineages and pressures.
    The exact CONDITIONAL classification remains unresolved, without a new defect
    finding or a universal DISPENSABLE replacement.
  evidence_ids:
  - root19-sources-jats-PMC10185304
  - root19-sources-hayes1992-publisher
  - root19-sources-PMID-8177173
  - root19-sources-PMID-22147705
  - root19-sources-PMID-1510555
  - record
  - policy
  - prior-reassessment
- assessment_id: scope
  area: scope
  topic: Variable occurrence and an exact structural-study strain
  outcome: supported
  target_ids:
  - GO:0033172
  summary: The Walsby review abstract supports variable bacterial and archaeal occurrence;
    Dutka Results S4/S6 separately identify the haloarchaeal Halobacterium salinarum
    comparison. No prevalence census is claimed. Dutka key resources and native taxonomy
    agree on CCAP1403/13F. The Anabaena cylindrica sequence-example strain is separately
    identified, not substituted for the cryo-ET organism.
  evidence_ids:
  - root19-sources-jats-PMC10185304
  - root19-sources-PMID-8177173
  - root19-sources-PMID-22147705
  - root19-sources-PMID-1510555
  - root19-sources-NCBITaxon-2
  - root19-sources-NCBITaxon-2157
  - root19-sources-NCBITaxon-315271
  - root19-sources-NCBITaxon-2692880
  - root19-sources-UniProtKB-A0ABR7ZBW9
  - root19-sources-UniProtKB-A0ABR7ZCB1
  - record
- assessment_id: function-graph
  area: graph
  topic: Supported structural and mechanical causal links
  outcome: supported
  target_ids:
  - GO:0033172
  summary: The graph links polymer assembly, shell formation, external coating and
    experimentally supported strengthening, then gas permeability/water exclusion
    and buoyancy. This is more than static parthood. The direct permeability study
    measures oxygen movement with a diffusion model; the cryo-ET study supports structure
    rather than independently measuring gas transport. Gas retention is understood
    as a water-excluding gas-filled space, not trapping or actively storing a fixed
    gas dose.
  evidence_ids:
  - root19-sources-gas-shell-go
  - root19-sources-jats-PMC10185304
  - root19-sources-hayes1992-publisher
  - root19-sources-permeability1992-browser
  - root19-sources-permeability1992-crossref
  - root19-sources-PMID-8177173
  - root19-sources-PMID-22147705
  - root19-sources-PMID-1510555
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded record-level coverage
  outcome: supported
  target_ids:
  - GO:0033172
  summary: The entire maintained record and cited claim contexts were inspected at
    the stated source scopes. Exact additional polymer inventories, numerical properties,
    images, traits and expanded mechanisms are optional. No verbatim quotation requires
    repair, and no status or history rewrite is proposed. This bounded review does
    not assert exhaustive literature completeness.
  evidence_ids:
  - record
  - policy
  - root19-sources-gas-shell-go
  - whole-neighbor
  - prior-reassessment
  - root19-sources-NCBITaxon-2
  - root19-sources-NCBITaxon-2157
  - root19-sources-NCBITaxon-315271
  - root19-sources-NCBITaxon-2692880
  - root19-sources-PMID-8177173
  - root19-sources-PMID-22147705
  - root19-sources-PMID-1510555
  - root19-sources-doi-10.1016_j.str.2023.03.011
  - root19-sources-jats-PMC10185304
  - root19-sources-hayes1992-publisher
  - root19-sources-permeability1992-crossref
  - root19-sources-permeability1992-browser
  - root19-sources-UniProtKB-A0ABR7ZBW9
  - root19-sources-UniProtKB-A0ABR7ZCB1
  - root19-sources-query-gvpA-2692880
  - root19-sources-query-gvpC-2692880
  - root19-sources-PF00741
  - root19-sources-PF01304
  - root19-sources-IPR000638
  - root19-sources-IPR047870
  - root19-sources-IPR050530
  - root19-sources-IPR002003
  - root19-sources-IPR018185
  - root19-sources-legacy-PMC3271001
  - root19-sources-legacy-PMC372955
  - root19-sources-bayro2012-doi
  - root19-sources-walsby1994-publisher
  - root19-sources-permeability1992-publisher
findings:
- finding_id: F1
  issue_key: gas-vesicle-shell-gvpa-family-grounding
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Record the verified exact GvpA family grounding
  description: The named GvpA constituent has no grounding or explicit unresolved-grounding
    discussion. Native IPR047870 specifically denotes GvpA, whereas the existing graph
    xref PF00741 covers a broader GvpA-like family including GvpJ. Add the exact family
    at the component; retain broader graph xrefs as related context. The GvpC repeat
    entries are not whole-protein equivalents.
  target_ids:
  - GO:0033172
  field_paths:
  - components[component_id=gvpa].grounding
  - components[component_id=gvpa].grounding_status
  evidence_ids:
  - root19-sources-PF00741
  - root19-sources-IPR000638
  - root19-sources-IPR047870
  - root19-sources-UniProtKB-A0ABR7ZBW9
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/gas_vesicle_shell.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: The biological identity, membership and existing related xref
    are sound; the correction records an available exact family without changing scientific
    scope.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0033172
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/inclusion/gas_vesicle_shell.yaml
    role: maintained scientific record
  description: Ground the GvpA component to verified InterPro IPR047870 with exact
    family provenance and appropriate grounding status. Preserve the distinction between
    exact family identity, concrete protein examples and related graph xrefs.
  acceptance_checks:
  - Reconfirm IPR047870 is the GvpA-specific family, with the broader GvpA-like entry
    kept distinct.
  - Do not promote PF01304 or the GvpC repeat entries to whole-protein equivalence.
  - Use separately authorized guarded curation, append-only history, focused validators,
    identifier/product checks and regeneration.
limitations:
- Walsby1994 and Bayro2012 were read at complete native abstract and bibliographic
  scope. Their full bodies were not recovered from the attempted public routes. Hayes1992
  and the1992 permeability paper were read at publisher abstract scope, not full Methods
  or raw measurements.
- Dutka2023 was read at the specified full text sections. Its rigid-body homology
  fitting, stripping experiment and mechanical simulation are distinct evidence types.
  No raw tomogram, NMR spectrum, figure pixels or supplementary model files were reanalysed.
- The whole-gas-vesicle neighbor and its historical reassessment were context only.
  No new review of its dataset or accessory assembly graph is claimed. Concrete protein
  identities remain unreviewed and identity-only.
- GvpC conditional assembly necessity is an explicit unknown, not an inferred error.
  The checked repeat families do not establish an exhaustive absence of a whole-GvpC
  family identifier.
- No raw microscopy or quantitative datasets were reanalysed. Historical curator searches
  and independent historical authorship are not certified.
- The completed fresh-base batch15 global gates are attached only at finalization;
  identifier transport and label-adapter limits remain explicit.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized one review for every uncovered target, including
  a review with no findings. Only this review bundle is intended for persistence.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
