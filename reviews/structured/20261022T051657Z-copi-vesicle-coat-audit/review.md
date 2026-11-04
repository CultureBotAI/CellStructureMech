# Source-backed review of copi vesicle coat

- Review: 20261022T051657Z-copi-vesicle-coat-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:00:56Z
- Finished UTC: 2026-10-22T05:16:57Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

COPI identity, constituents, source-scoped recruitment/retrieval and descriptive graph are supported. One minor corrects the RET1 query-uniqueness note while retaining the correct coatomer accession.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch48 fixed strict path order, index 3; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030126 | data/structures/other/copi_vesicle_coat.yaml | maintained | COPI vesicle coat |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030126 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030126 | Focused validator passed. |
| Focused native proteins | passed | True | GO:0030126 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:0030126 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0030126 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030126 | 20 of 22 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:15504911: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030126 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030126 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030126 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030126 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030126 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### COPI coat identity and hierarchy

identity: supported. Targets: GO:0030126.

Active GO0030126, exact synonym coatomer, vesicle-coat parent and coat/vesicle relationship support the target. The molecular coat remains distinct from the lipid membrane. The narrower coatomer building block is not automatically equated with the target identifier merely because GO uses coatomer as a synonym.

### Coatomer and Arf constituents

grounding: supported. Targets: GO:0030126.

The seven named coatomer proteins and Arf1/Arf2 examples fit the coarse two-component model. Sandmann and Yu support coatomer/Arf assembly context, while Waters is verified only at complete abstract tier. A broader ARF-family or Arf1–5 identifier is not forced onto the context-selected cohort; no exact source-neutral narrower coatomer-complex identifier was established by the bounded search. Absence of individual coatomer subunit rows is optional enrichment, not a completeness defect.

### Correct accessions and one query-note discrepancy

grounding: concern. Targets: GO:0030126.

All retained reviewed S288C accession/primary-name/alias pairs are correct. The COP1 alias RET1 is resolved to the correct coatomer P53622. The evidence note nevertheless calls it the single reviewed RET1 hit; the exact query also returns polymerase P22276. Other inspected component queries return the intended single entry.

### Recruitment, retrieval and annotation scope

evidence: supported. Targets: GO:0030126.

Sandmann provides direct yeast cargo-binding and transport/budding experiments. Yu supplies binding/structural evidence and an explicit recruitment model in mixed recombinant contexts; the record’s coarse descriptions do not assert that its model was directly imaged in yeast. Native SEC26 and ARF2 location annotations join Huh2003, and ARF1 joins Gillingham2004; both complete native abstracts were read, without certifying their protein-specific primary images or tables.

### Descriptive coat assembly graph

graph: supported. Targets: GO:0030126.

The seven-node/eight-edge NONMECHANISTIC ASSEMBLY graph separates Golgi association, coatomer/Arf association, constituent parthood, coat-to-vesicle topology and budding/retrieval participation. Its coarse scope does not claim an ordered GTPase cycle or complete experimental reconstitution of every edge.

### Species, reference strain and COMMON meaning

scope: supported. Targets: GO:0030126.

Species4932 and strain559292 identities are correct. COMMON means present in most taxon members with exceptional losses; ordinary yeast-system evidence provides qualitative support, not a measured prevalence census. Native reference accessions are not evidence that every cited experiment used S288C.

### Formation necessity remains unknown

grounding: unknown. Targets: GO:0030126.

All current constituent essentiality labels are UNKNOWN. The inspected membership, localization, transport and reconstitution evidence is not promoted to an unqualified requirement for formation of every represented structure. No necessity finding is inferred from a missing depletion experiment.

### Whole-record coverage and bounded enrichment

completeness: supported. Targets: GO:0030126.

All target bytes, component/examples, function/evidence placements, canonical example, graph, discussions and history were reviewed. Findings concern exact current statements or verified available mappings, not optional inventory expansion or a declaration that historical searches were false. No neighboring record’s scientific verdict is imported.

## Findings

### F1: Correct the RET1 single-hit evidence note

minor / open / confirmed; issue key: copi.ret1_reviewed_query_ambiguity.

The selected P53622 coatomer alpha accession and primary symbol COP1 are correct. Its current evidence note says it is the single reviewed entry for RET1 in S288C. The retained exact native query returns both P53622 (COP1, alias RET1) and P22276 (polymerase subunit RET1), so uniqueness cannot be used as the selection rationale.

## Recommended Actions And Acceptance Checks

### A1

Keep P53622 and COP1 with the RET1 alias; replace the uniqueness claim with explicit disambiguation against polymerase P22276. Preserve dated retrieval history.

- Preserve exact supported identity, experimental organism and native versus recombinant context.
- Attach source-specific evidence to each changed claim and retain historical provenance.
- Native schema, strict, CURIE, protein and graph checks pass as applicable.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/copi_vesicle_coat.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro48-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139,GO:0005789,GO:0006890,GO:0010008,GO:0030120,GO:0030126,GO:0030127,GO:0030134,GO:0030137,GO:0033263,GO:0035964,GO:0090114,GO:0099023; Complete id/name/isObsolete/definition/synonym/typed-children fields of all 13 returned terms; the hash identifies this combined response, not a source paper. | supports | The 13 exact active entries distinguish COPI/COPII protein coats, their vesicles and membrane locations, and CORVET from its endosome membrane. GO0030120 typed children include both coat classes; GO0099023 typed children include CORVET. Coat-to-whole-vesicle parthood is supported by the definitions, rather than an exposed direct typed relation in this response. GO0033263 explicitly names the six yeast CORVET subunits and pre-SNARE endosomal tethering. |
| micro48-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro48-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 559292 identifies Saccharomyces cerevisiae S288C at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro48-protein-P41810 | https://rest.uniprot.org/uniprotkb/P41810.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P41810 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SEC26']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-protein-P41811 | https://rest.uniprot.org/uniprotkb/P41811.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P41811 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SEC27']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-protein-P32074 | https://rest.uniprot.org/uniprotkb/P32074.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P32074 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SEC21']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-protein-P43621 | https://rest.uniprot.org/uniprotkb/P43621.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P43621 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['RET2']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-protein-P40509 | https://rest.uniprot.org/uniprotkb/P40509.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P40509 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SEC28']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-protein-P53600 | https://rest.uniprot.org/uniprotkb/P53600.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P53600 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['RET3']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-protein-P53622 | https://rest.uniprot.org/uniprotkb/P53622.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P53622 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['COP1']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-protein-P11076 | https://rest.uniprot.org/uniprotkb/P11076.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P11076 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['ARF1']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-protein-P19146 | https://rest.uniprot.org/uniprotkb/P19146.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence joins. | supports | P19146 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['ARF2']. Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro48-gene-SEC26 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC26%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 1 entry/entries: P41810. Primary gene names and aliases were inspected; the intended accession is correctly identified. |
| micro48-gene-SEC27 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC27%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 1 entry/entries: P41811. Primary gene names and aliases were inspected; the intended accession is correctly identified. |
| micro48-gene-SEC21 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC21%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 1 entry/entries: P32074. Primary gene names and aliases were inspected; the intended accession is correctly identified. |
| micro48-gene-RET2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 1 entry/entries: P43621. Primary gene names and aliases were inspected; the intended accession is correctly identified. |
| micro48-gene-SEC28 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC28%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 1 entry/entries: P40509. Primary gene names and aliases were inspected; the intended accession is correctly identified. |
| micro48-gene-RET3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 1 entry/entries: P53600. Primary gene names and aliases were inspected; the intended accession is correctly identified. |
| micro48-gene-RET1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 2 entry/entries: P22276, P53622. Primary gene names and aliases were inspected; RET1 matches the polymerase P22276 as well as COP1/RET1 P53622, so the coatomer accession is correct but the current uniqueness statement is not. |
| micro48-gene-ARF1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 1 entry/entries: P11076. Primary gene names and aliases were inspected; the intended accession is correctly identified. |
| micro48-gene-ARF2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARF2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete results for the exact gene/reviewed/taxon559292 URL. | supports | The exact reviewed S288C query returned 1 entry/entries: P19146. Primary gene names and aliases were inspected; the intended accession is correctly identified. |
| micro48-waters1991-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038%2F349248a0; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED1898986: 'Coatomer': a cytosolic protein complex containing subunits of non-clathrin-coated Golgi transport vesicles. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro48-sandmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091%2Fmbc.e02-11-0736; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED12925749: Suppression of coatomer mutants by a new protein family with COPI and COPII binding motifs in Saccharomyces cerevisiae. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro48-yu2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.cell.2012.01.015; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED22304919: A structure-based mechanism for Arf1-dependent recruitment of coatomer to membranes. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro48-pmid14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14562095%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED14562095: Global analysis of protein localization in budding yeast. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro48-pmid15504911 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15504911+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED15504911: The GTPase Arf1p and the ER to Golgi cargo receptor Erv14p cooperate to recruit the golgin Rud3p to the cis-Golgi. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro48-sandmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC181553/; Genuine PMC181553 HTML: complete Introduction sec1; Methods sec3/Table1, sec7 and sec14; Results sec16 and sec20–23; complete Discussion sec25, including embedded Fig1 and Fig5–7 captions. | supports | Sandmann2003 directly tests sec21-3 suppression, KKXX-dependent coatomer binding and coat-dependent vesicle production. Mst27 overexpression effects depend on motif, concentration and assay context; the paper distinguishes cargo packaging from vesicle number and treats cycling/nucleation explanations as hypotheses. Its purified COPI budding setup uses coatomer plus Arf1. These experiments support the narrow coatomer/cargo-retrieval context without treating Mst27 as a general obligatory coat constituent. |
| micro48-yu2012-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3285272.1/PMC3285272.1.xml; Genuine PMC3285272.1 JATS: complete Introduction S1; Results/Discussion S3–S10; Experimental Procedures S12–S15. Includes distinction between measured binding, composite membrane model, and proposed conformational/GTPase behavior. | supports | Yu2012 demonstrates two Arf1-binding interfaces in coatomer through structural and biochemical assays. The core crystal combines bovine gamma/zeta coatomer fragments with yeast Arf1; other assays use mammalian coatomer, human or yeast truncated Arf1 and human GAP. Bivalent membrane recruitment and subsequent conformational ordering are models derived from those data, not a live yeast coat-assembly movie or complete budding reconstitution. |
| micro48-IPR024156 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024156/; Native metadata accession/name/type and complete description, compared with the exact corresponding protein cross-reference. | supports | IPR024156 is an ARF-type family including Arf, Arl, Arp and SRbeta; its description is broader than the record’s COPI-associated Arf cohort. |
| micro48-IPR045872 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045872/; Native metadata accession/name/type and complete description, compared with the exact corresponding protein cross-reference. | supports | IPR045872 is the Arf1–5 family, including related paralogues with several coat-recruitment and post-Golgi roles. Both yeast examples carry it, but this alone does not establish exact equality to the record’s function-selected COPI-associated cohort. |
| schema-result | just validate data/structures/other/copi_vesicle_coat.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/copi_vesicle_coat.yaml |
| strict-result | just validate-strict data/structures/other/copi_vesicle_coat.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/copi_vesicle_coat-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/copi_vesicle_coat.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/copi_vesicle_coat-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch48-20261022-ppyyf64c/copi_vesicle_coat-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/copi_vesicle_coat.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/copi_vesicle_coat.yaml; Complete read-only focused native graphs log | supports | data/structures/other/copi_vesicle_coat.yaml  (GO:0030126)<br>  copi_coatomer_golgi_budding	arf_gtpase	COVERED	-&gt;arf_gtpase (UniProtKB:P11076, UniProtKB:P19146)<br>  copi_coatomer_golgi_budding	coatomer	COVERED	-&gt;coatomer_complex (UniProtKB:P41810, UniProtKB:P41811, UniProtKB:P32074, UniProtKB:P43621, UniProtKB:P40509, UniProtKB:P53600, UniProtKB:P53622)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/copi_vesicle_coat.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 20 of 22 collected target identifiers returned OK. PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:15504911: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- COMMON retains its schema meaning present in most members with exceptional losses. Yeast experiments support ordinary species-level occurrence qualitatively, without measuring a species-wide prevalence census.
- Reference-entry S288C identity is distinguished from experimental strains, tagged constructs, purified fragments and reconstitution conditions.
- No microscopy pixels, videos or supplementary files were inspected. Primary text and embedded captions were read only at the explicitly named extents.
- All constituent essentiality values are UNKNOWN. Membership, protein function, transport phenotype and necessity for formation of the entire structure are separate claims.
- Waters1991, Huh2003 and Gillingham2004 were read at complete native abstract tier only. Their full main bodies/pixels were not inspected.
- Yu2012 measured interfaces use mixed mammalian/yeast/human recombinant material; membrane orientation, conformational sequencing and physiological GTPase interpretation remain the paper’s models.
- The remote QuickGO coatomer-complex search inspected only its first 25 returned results; it is not an exhaustive ontology absence claim.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these vesicle-coat and CORVET identity, molecular-family, localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T051657Z-copi-vesicle-coat-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of copi vesicle coat
started_at: '2026-10-22T05:00:56Z'
finished_at: '2026-10-22T05:16:57Z'
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
summary: COPI identity, constituents, source-scoped recruitment/retrieval and descriptive
  graph are supported. One minor corrects the RET1 query-uniqueness note while retaining
  the correct coatomer accession.
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
  - path: data/structures/other/copi_vesicle_coat.yaml
    sha256: 1b264ad3800f2c5c8c78d327f63a32bdc73888a003e3be3fcad778bb9f993195
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
- target_id: GO:0030126
  path: data/structures/other/copi_vesicle_coat.yaml
  label: COPI vesicle coat
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copi_vesicle_coat.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch48 fixed strict path order, index 3; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030126
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: just validate data/structures/other/copi_vesicle_coat.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: just validate-strict data/structures/other/copi_vesicle_coat.yaml --out
    /private/tmp/cellstructure-batch48-20261022-ppyyf64c/copi_vesicle_coat-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/copi_vesicle_coat.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-proteins
- check_id: native-graphs
  name: Focused native graphs
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/copi_vesicle_coat.yaml
  exit_code: 0
  summary: Read-only native check passed; claim-level protein/edge support evaluated
    separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030126
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro48-go
  - micro48-tax4932
  - micro48-tax559292
  - micro48-protein-P41810
  - micro48-protein-P41811
  - micro48-protein-P32074
  - micro48-protein-P43621
  - micro48-protein-P40509
  - micro48-protein-P53600
  - micro48-protein-P53622
  - micro48-protein-P11076
  - micro48-protein-P19146
  - micro48-gene-SEC26
  - micro48-gene-SEC27
  - micro48-gene-SEC21
  - micro48-gene-RET2
  - micro48-gene-SEC28
  - micro48-gene-RET3
  - micro48-gene-RET1
  - micro48-gene-ARF1
  - micro48-gene-ARF2
  - micro48-waters1991-meta
  - micro48-sandmann2003-meta
  - micro48-yu2012-meta
  - micro48-pmid14562095
  - micro48-pmid15504911
  - micro48-sandmann2003-pmc
  - micro48-yu2012-s3
  - micro48-IPR024156
  - micro48-IPR045872
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030126
  summary: '20 of 22 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:15504911:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro48-pmid14562095
  - micro48-pmid15504911
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030126
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030126
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
    and current batch48 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/copi_vesicle_coat.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T05:08:18Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T05:08:18Z'
  support: context_only
  summary: ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite
    class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic
    or transport function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T05:08:18Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro48-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000139,GO:0005789,GO:0006890,GO:0010008,GO:0030120,GO:0030126,GO:0030127,GO:0030134,GO:0030137,GO:0033263,GO:0035964,GO:0090114,GO:0099023
  locator: Complete id/name/isObsolete/definition/synonym/typed-children fields of
    all 13 returned terms; the hash identifies this combined response, not a source
    paper.
  accessed_at: '2026-10-22T05:02:32.410565Z'
  support: supports
  summary: The 13 exact active entries distinguish COPI/COPII protein coats, their
    vesicles and membrane locations, and CORVET from its endosome membrane. GO0030120
    typed children include both coat classes; GO0099023 typed children include CORVET.
    Coat-to-whole-vesicle parthood is supported by the definitions, rather than an
    exposed direct typed relation in this response. GO0033263 explicitly names the
    six yeast CORVET subunits and pre-SNARE endosomal tethering.
  snapshot_sha256: 7169ecfe80eda6fc5cc8b61c60a3d9b2bd09a42c1fe2bfbcb3ae7a42259a994f
- evidence_id: micro48-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:15:34.948894Z'
  support: supports
  summary: ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro48-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:15:34.948991Z'
  support: supports
  summary: ENA taxId 559292 identifies Saccharomyces cerevisiae S288C at rank strain;
    aliases and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro48-protein-P41810
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41810.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:34.619403Z'
  support: supports
  summary: P41810 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SEC26'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 14db746dd9b7298b293cb31c5f9c75daf9d58bf6702ffb741a3c9678c17d1520
- evidence_id: micro48-protein-P41811
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41811.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:34.810244Z'
  support: supports
  summary: P41811 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SEC27'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 9c0c30568e621781e7f544ae72f36ecd3889e7b738a153b35b5b3e262d85e741
- evidence_id: micro48-protein-P32074
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32074.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:33.301775Z'
  support: supports
  summary: P32074 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SEC21'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 7bf09236856fbe6260a97d9275999613f6bddb1b4dff29b5d2ba0556d23adf5a
- evidence_id: micro48-protein-P43621
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P43621.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:35.267540Z'
  support: supports
  summary: P43621 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['RET2'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 203f70e6015b5f82bae9395f2195f5cef7e5d6ffa0f536540519ff0e36d76fbd
- evidence_id: micro48-protein-P40509
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40509.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:34.349978Z'
  support: supports
  summary: P40509 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SEC28'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: d45cedfa27d3a43cd9b9a2666a91b3f35ae4ca29ba7397ac99687002f1cf696a
- evidence_id: micro48-protein-P53600
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53600.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:35.365461Z'
  support: supports
  summary: P53600 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['RET3'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 05bc720904df87f1debcb5075ba2f0803c2ad2c1984fa00736022aff773e3725
- evidence_id: micro48-protein-P53622
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53622.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:35.399398Z'
  support: supports
  summary: P53622 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['COP1'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 3fa8e6ac02935b57b3588e23901528210478283bbb5311fd3d3118999af5ced3
- evidence_id: micro48-protein-P11076
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P11076.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:32.410946Z'
  support: supports
  summary: P11076 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['ARF1'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: fb2ce21f92da7c817647884a2805ab45d84f49b279093b1a68cd4908bbbfb7b4
- evidence_id: micro48-protein-P19146
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P19146.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBUNIT/SUBCELLULAR
    LOCATION comments and their evidence joins.
  accessed_at: '2026-10-22T05:02:32.411444Z'
  support: supports
  summary: P19146 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['ARF2'].
    Recommended identity, gene aliases, full SUBUNIT/SUBCELLULAR LOCATION comments
    and their evidence codes/PMIDs were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 24708ced3c9aedaec94d8882a3a8027bda48da9a3a35e0df473b614ef3f457e2
- evidence_id: micro48-gene-SEC26
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC26%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:39.629440Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 1 entry/entries: P41810. Primary
    gene names and aliases were inspected; the intended accession is correctly identified.'
  snapshot_sha256: 7d2571f17957840503323f13c6caa07bafaac786466d4aae0c7d4755b2e4818a
  search_scope: Remote UniProt query for exact gene SEC26, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-gene-SEC27
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC27%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:39.783337Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 1 entry/entries: P41811. Primary
    gene names and aliases were inspected; the intended accession is correctly identified.'
  snapshot_sha256: f8566b61bd037de14fac0d3c3c89f12d3404a0a9eae7d2569987828226a54c12
  search_scope: Remote UniProt query for exact gene SEC27, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-gene-SEC21
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC21%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:38.868515Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 1 entry/entries: P32074. Primary
    gene names and aliases were inspected; the intended accession is correctly identified.'
  snapshot_sha256: 72e1ffb549dbe9841bda3065c956ba6d19c7862e34e5f738c10c9f7ff605cb2c
  search_scope: Remote UniProt query for exact gene SEC21, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-gene-RET2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:37.552175Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 1 entry/entries: P43621. Primary
    gene names and aliases were inspected; the intended accession is correctly identified.'
  snapshot_sha256: 148535d31ff8a3ee38c2a69b54bd4139f95fb77388bee719258ba2913ff05d75
  search_scope: Remote UniProt query for exact gene RET2, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-gene-SEC28
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC28%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:40.560006Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 1 entry/entries: P40509. Primary
    gene names and aliases were inspected; the intended accession is correctly identified.'
  snapshot_sha256: 70b3a3a5af8033de86c7cbc1416a464f87f00ddbd5a7ee064af02d9243f2ae6b
  search_scope: Remote UniProt query for exact gene SEC28, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-gene-RET3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:38.476564Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 1 entry/entries: P53600. Primary
    gene names and aliases were inspected; the intended accession is correctly identified.'
  snapshot_sha256: f4821afa93da261dd0ce5ac0590689bc1a0ea886087ff2c1791837bf3eb1ab68
  search_scope: Remote UniProt query for exact gene RET3, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-gene-RET1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ARET1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:37.527696Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 2 entry/entries: P22276, P53622.
    Primary gene names and aliases were inspected; RET1 matches the polymerase P22276
    as well as COP1/RET1 P53622, so the coatomer accession is correct but the current
    uniqueness statement is not.'
  snapshot_sha256: e08053c7530d77cd89e56c7471167d1ff5c188e01f31390c1a89d329b7b1fe7a
  search_scope: Remote UniProt query for exact gene RET1, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-gene-ARF1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:36.284614Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 1 entry/entries: P11076. Primary
    gene names and aliases were inspected; the intended accession is correctly identified.'
  snapshot_sha256: 554d864c11d13c2eab3f7b69ffa33fea857144e092250db66629ff6b7ea2ddb0
  search_scope: Remote UniProt query for exact gene ARF1, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-gene-ARF2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AARF2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete results for the exact gene/reviewed/taxon559292 URL.
  accessed_at: '2026-10-22T05:02:36.388427Z'
  support: supports
  summary: 'The exact reviewed S288C query returned 1 entry/entries: P19146. Primary
    gene names and aliases were inspected; the intended accession is correctly identified.'
  snapshot_sha256: 16a8b178e7a640fb093ba5195007566a96d962d35fc60e4c1caef5c05bda7bc2
  search_scope: Remote UniProt query for exact gene ARF2, reviewed entries, organism_id559292;
    complete returned result set inspected. Local ignored files are not applicable
    to this remote search.
- evidence_id: micro48-waters1991-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038%2F349248a0
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-21T11:12:18.649126Z'
  support: supports
  summary: 'Unique MED1898986: ''Coatomer'': a cytosolic protein complex containing
    subunits of non-clathrin-coated Golgi transport vesicles. Authors/year/DOI and
    the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 3e43f878d50ac2de9872db7f7d40d491953149c1244b1cd0a4b036b0a8cbd481
- evidence_id: micro48-sandmann2003-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091%2Fmbc.e02-11-0736
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-21T11:12:18.649055Z'
  support: supports
  summary: 'Unique MED12925749: Suppression of coatomer mutants by a new protein family
    with COPI and COPII binding motifs in Saccharomyces cerevisiae. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 022eedace493fd025dfedbc5584f496bf17c339d8c252d617e82628790b24a76
- evidence_id: micro48-yu2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.cell.2012.01.015
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-21T10:57:50.763483Z'
  support: supports
  summary: 'Unique MED22304919: A structure-based mechanism for Arf1-dependent recruitment
    of coatomer to membranes. Authors/year/DOI and the complete native abstract were
    inspected. This row establishes bibliographic identity and abstract-level content
    only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 6841c2debb7f955140354263ebfd0b3434249dd893cd6add2faecee4101a7632
- evidence_id: micro48-pmid14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:14562095%20AND%20SRC:MED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:51:26.516975Z'
  support: supports
  summary: 'Unique MED14562095: Global analysis of protein localization in budding
    yeast. Authors/year/DOI and the complete native abstract were inspected. This
    row establishes bibliographic identity and abstract-level content only; detailed
    experiments require separately specified body evidence.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: micro48-pmid15504911
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15504911+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T05:02:43.061379Z'
  support: supports
  summary: 'Unique MED15504911: The GTPase Arf1p and the ER to Golgi cargo receptor
    Erv14p cooperate to recruit the golgin Rud3p to the cis-Golgi. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: be219fcd874aa21bd72e253d1eaf87aceaaaa4fc148d339740542c9dec1dcecd
- evidence_id: micro48-sandmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC181553/
  locator: 'Genuine PMC181553 HTML: complete Introduction sec1; Methods sec3/Table1,
    sec7 and sec14; Results sec16 and sec20–23; complete Discussion sec25, including
    embedded Fig1 and Fig5–7 captions.'
  accessed_at: '2026-10-21T11:12:53.605970Z'
  support: supports
  summary: Sandmann2003 directly tests sec21-3 suppression, KKXX-dependent coatomer
    binding and coat-dependent vesicle production. Mst27 overexpression effects depend
    on motif, concentration and assay context; the paper distinguishes cargo packaging
    from vesicle number and treats cycling/nucleation explanations as hypotheses.
    Its purified COPI budding setup uses coatomer plus Arf1. These experiments support
    the narrow coatomer/cargo-retrieval context without treating Mst27 as a general
    obligatory coat constituent.
  snapshot_sha256: cffe4575f5abb83724d453c57de119c644e3608b33e4ca827c6f2338d0d26d7d
- evidence_id: micro48-yu2012-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3285272.1/PMC3285272.1.xml
  locator: 'Genuine PMC3285272.1 JATS: complete Introduction S1; Results/Discussion
    S3–S10; Experimental Procedures S12–S15. Includes distinction between measured
    binding, composite membrane model, and proposed conformational/GTPase behavior.'
  accessed_at: '2026-10-21T11:00:51.605958Z'
  support: supports
  summary: Yu2012 demonstrates two Arf1-binding interfaces in coatomer through structural
    and biochemical assays. The core crystal combines bovine gamma/zeta coatomer fragments
    with yeast Arf1; other assays use mammalian coatomer, human or yeast truncated
    Arf1 and human GAP. Bivalent membrane recruitment and subsequent conformational
    ordering are models derived from those data, not a live yeast coat-assembly movie
    or complete budding reconstitution.
  snapshot_sha256: a7adecb3e84137dcc05565185633b97cd4c07fc8e2556c98e9922152c7d34ea6
- evidence_id: micro48-IPR024156
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR024156/
  locator: Native metadata accession/name/type and complete description, compared
    with the exact corresponding protein cross-reference.
  accessed_at: '2026-10-22T05:04:38.857611Z'
  support: supports
  summary: IPR024156 is an ARF-type family including Arf, Arl, Arp and SRbeta; its
    description is broader than the record’s COPI-associated Arf cohort.
  snapshot_sha256: 9541ba207e66c81066e6f5747cc862ed040cdbc835f9dca1fd8eeaed18ac9845
- evidence_id: micro48-IPR045872
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045872/
  locator: Native metadata accession/name/type and complete description, compared
    with the exact corresponding protein cross-reference.
  accessed_at: '2026-10-22T05:04:38.857889Z'
  support: supports
  summary: IPR045872 is the Arf1–5 family, including related paralogues with several
    coat-recruitment and post-Golgi roles. Both yeast examples carry it, but this
    alone does not establish exact equality to the record’s function-selected COPI-associated
    cohort.
  snapshot_sha256: 57787b15cfc080275c6a68573f237abe003d8bb925b72c3b986b605567d9d6fd
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/copi_vesicle_coat.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:00:57Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/copi_vesicle_coat.yaml'
  snapshot_sha256: dfac12e1fc1dad969e6f1caf4f8e4d9c63f37eadb4556185bc182de0adfee4f2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/copi_vesicle_coat.yaml --out
    /private/tmp/cellstructure-batch48-20261022-ppyyf64c/copi_vesicle_coat-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:00:59Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/copi_vesicle_coat.yaml\
    \ --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/copi_vesicle_coat-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch48-20261022-ppyyf64c/copi_vesicle_coat-strict.tsv"
  snapshot_sha256: 37a52d5f6adde8034957d9eaa2d4b7f3a3b5e56da3710e7cbdf145ce592b0e7d
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/copi_vesicle_coat.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T05:02:32.206718Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/copi_vesicle_coat.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T05:02:32.638001Z'
  support: supports
  summary: "data/structures/other/copi_vesicle_coat.yaml  (GO:0030126)\n  copi_coatomer_golgi_budding\t\
    arf_gtpase\tCOVERED\t->arf_gtpase (UniProtKB:P11076, UniProtKB:P19146)\n  copi_coatomer_golgi_budding\t\
    coatomer\tCOVERED\t->coatomer_complex (UniProtKB:P41810, UniProtKB:P41811, UniProtKB:P32074,\
    \ UniProtKB:P43621, UniProtKB:P40509, UniProtKB:P53600, UniProtKB:P53622)\n\n\
    causal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED                 \
    \  component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 62b80549c9d8c2786488904a26b8a4e91d32a624b11000f16ebce03c1fe02395
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/copi_vesicle_coat.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '20 of 22 collected target identifiers returned OK. PMID:14562095: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:15504911:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: COPI coat identity and hierarchy
  outcome: supported
  target_ids:
  - GO:0030126
  summary: Active GO0030126, exact synonym coatomer, vesicle-coat parent and coat/vesicle
    relationship support the target. The molecular coat remains distinct from the
    lipid membrane. The narrower coatomer building block is not automatically equated
    with the target identifier merely because GO uses coatomer as a synonym.
  evidence_ids:
  - micro48-go
  - record
- assessment_id: components
  area: grounding
  topic: Coatomer and Arf constituents
  outcome: supported
  target_ids:
  - GO:0030126
  summary: The seven named coatomer proteins and Arf1/Arf2 examples fit the coarse
    two-component model. Sandmann and Yu support coatomer/Arf assembly context, while
    Waters is verified only at complete abstract tier. A broader ARF-family or Arf1–5
    identifier is not forced onto the context-selected cohort; no exact source-neutral
    narrower coatomer-complex identifier was established by the bounded search. Absence
    of individual coatomer subunit rows is optional enrichment, not a completeness
    defect.
  evidence_ids:
  - micro48-go
  - micro48-waters1991-meta
  - micro48-sandmann2003-meta
  - micro48-yu2012-meta
  - micro48-sandmann2003-pmc
  - micro48-yu2012-s3
  - micro48-IPR024156
  - micro48-IPR045872
  - micro48-protein-P41810
  - micro48-protein-P41811
  - micro48-protein-P32074
  - micro48-protein-P43621
  - micro48-protein-P40509
  - micro48-protein-P53600
  - micro48-protein-P53622
  - micro48-protein-P11076
  - micro48-protein-P19146
  - record
  - curation
- assessment_id: proteins
  area: grounding
  topic: Correct accessions and one query-note discrepancy
  outcome: concern
  target_ids:
  - GO:0030126
  summary: All retained reviewed S288C accession/primary-name/alias pairs are correct.
    The COP1 alias RET1 is resolved to the correct coatomer P53622. The evidence note
    nevertheless calls it the single reviewed RET1 hit; the exact query also returns
    polymerase P22276. Other inspected component queries return the intended single
    entry.
  evidence_ids:
  - micro48-protein-P41810
  - micro48-protein-P41811
  - micro48-protein-P32074
  - micro48-protein-P43621
  - micro48-protein-P40509
  - micro48-protein-P53600
  - micro48-protein-P53622
  - micro48-protein-P11076
  - micro48-protein-P19146
  - micro48-gene-SEC26
  - micro48-gene-SEC27
  - micro48-gene-SEC21
  - micro48-gene-RET2
  - micro48-gene-SEC28
  - micro48-gene-RET3
  - micro48-gene-RET1
  - micro48-gene-ARF1
  - micro48-gene-ARF2
- assessment_id: sources
  area: evidence
  topic: Recruitment, retrieval and annotation scope
  outcome: supported
  target_ids:
  - GO:0030126
  summary: Sandmann provides direct yeast cargo-binding and transport/budding experiments.
    Yu supplies binding/structural evidence and an explicit recruitment model in mixed
    recombinant contexts; the record’s coarse descriptions do not assert that its
    model was directly imaged in yeast. Native SEC26 and ARF2 location annotations
    join Huh2003, and ARF1 joins Gillingham2004; both complete native abstracts were
    read, without certifying their protein-specific primary images or tables.
  evidence_ids:
  - micro48-waters1991-meta
  - micro48-sandmann2003-meta
  - micro48-yu2012-meta
  - micro48-sandmann2003-pmc
  - micro48-yu2012-s3
  - micro48-pmid14562095
  - micro48-pmid15504911
  - micro48-protein-P41810
  - micro48-protein-P19146
  - micro48-protein-P11076
  - record
- assessment_id: graph
  area: graph
  topic: Descriptive coat assembly graph
  outcome: supported
  target_ids:
  - GO:0030126
  summary: The seven-node/eight-edge NONMECHANISTIC ASSEMBLY graph separates Golgi
    association, coatomer/Arf association, constituent parthood, coat-to-vesicle topology
    and budding/retrieval participation. Its coarse scope does not claim an ordered
    GTPase cycle or complete experimental reconstitution of every edge.
  evidence_ids:
  - micro48-go
  - micro48-sandmann2003-pmc
  - micro48-yu2012-s3
  - record
- assessment_id: scope
  area: scope
  topic: Species, reference strain and COMMON meaning
  outcome: supported
  target_ids:
  - GO:0030126
  summary: Species4932 and strain559292 identities are correct. COMMON means present
    in most taxon members with exceptional losses; ordinary yeast-system evidence
    provides qualitative support, not a measured prevalence census. Native reference
    accessions are not evidence that every cited experiment used S288C.
  evidence_ids:
  - micro48-tax4932
  - micro48-tax559292
  - schema
  - micro48-waters1991-meta
  - micro48-sandmann2003-meta
  - micro48-yu2012-meta
  - micro48-sandmann2003-pmc
  - micro48-yu2012-s3
- assessment_id: necessity
  area: grounding
  topic: Formation necessity remains unknown
  outcome: unknown
  target_ids:
  - GO:0030126
  summary: All current constituent essentiality labels are UNKNOWN. The inspected
    membership, localization, transport and reconstitution evidence is not promoted
    to an unqualified requirement for formation of every represented structure. No
    necessity finding is inferred from a missing depletion experiment.
  evidence_ids:
  - micro48-go
  - schema
  - record
  - micro48-waters1991-meta
  - micro48-sandmann2003-meta
  - micro48-yu2012-meta
  - micro48-sandmann2003-pmc
  - micro48-yu2012-s3
- assessment_id: coverage
  area: completeness
  topic: Whole-record coverage and bounded enrichment
  outcome: supported
  target_ids:
  - GO:0030126
  summary: All target bytes, component/examples, function/evidence placements, canonical
    example, graph, discussions and history were reviewed. Findings concern exact
    current statements or verified available mappings, not optional inventory expansion
    or a declaration that historical searches were false. No neighboring record’s
    scientific verdict is imported.
  evidence_ids:
  - micro48-go
  - record
  - curation
  - micro48-waters1991-meta
  - micro48-sandmann2003-meta
  - micro48-yu2012-meta
  - micro48-sandmann2003-pmc
  - micro48-yu2012-s3
findings:
- finding_id: F1
  issue_key: copi.ret1_reviewed_query_ambiguity
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the RET1 single-hit evidence note
  description: The selected P53622 coatomer alpha accession and primary symbol COP1
    are correct. Its current evidence note says it is the single reviewed entry for
    RET1 in S288C. The retained exact native query returns both P53622 (COP1, alias
    RET1) and P22276 (polymerase subunit RET1), so uniqueness cannot be used as the
    selection rationale.
  target_ids:
  - GO:0030126
  field_paths:
  - components[0].protein_examples[6].evidence[0].notes
  evidence_ids:
  - micro48-gene-RET1
  - micro48-protein-P53622
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copi_vesicle_coat.yaml
    role: maintained scientific record
  rule_id: Exact source scope, protein grounding and formation-specific essentiality
  native_severity: minor
  normalization_reason: 'Minor: accession identity, coatomer membership and biology
    remain correct; only a current query-selection provenance statement is inaccurate.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030126
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/copi_vesicle_coat.yaml
    role: maintained scientific record
  description: Keep P53622 and COP1 with the RET1 alias; replace the uniqueness claim
    with explicit disambiguation against polymerase P22276. Preserve dated retrieval
    history.
  acceptance_checks:
  - Preserve exact supported identity, experimental organism and native versus recombinant
    context.
  - Attach source-specific evidence to each changed claim and retain historical provenance.
  - Native schema, strict, CURIE, protein and graph checks pass as applicable.
limitations:
- COMMON retains its schema meaning present in most members with exceptional losses.
  Yeast experiments support ordinary species-level occurrence qualitatively, without
  measuring a species-wide prevalence census.
- Reference-entry S288C identity is distinguished from experimental strains, tagged
  constructs, purified fragments and reconstitution conditions.
- No microscopy pixels, videos or supplementary files were inspected. Primary text
  and embedded captions were read only at the explicitly named extents.
- All constituent essentiality values are UNKNOWN. Membership, protein function, transport
  phenotype and necessity for formation of the entire structure are separate claims.
- Waters1991, Huh2003 and Gillingham2004 were read at complete native abstract tier
  only. Their full main bodies/pixels were not inspected.
- Yu2012 measured interfaces use mixed mammalian/yeast/human recombinant material;
  membrane orientation, conformational sequencing and physiological GTPase interpretation
  remain the paper’s models.
- The remote QuickGO coatomer-complex search inspected only its first 25 returned
  results; it is not an exhaustive ontology absence claim.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these vesicle-coat and CORVET identity, molecular-family,
  localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
