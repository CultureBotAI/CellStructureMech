# Source-backed review of cellular bud tip polarisome

- Review: 20261022T045417Z-cellular-bud-tip-polarisome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:37:04Z
- Finished UTC: 2026-10-22T04:54:17Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The localized polarisome identity, source-scoped membership, verified examples and descriptive graph are supported. Formation necessity and inventory completeness remain bounded; no confirmed curation issue was found.

## Scope And Provenance

Exactly one complete target; no neighboring scientific-record verdict is imported. Exact authority, all current component/function/graph/source placements, taxonomic scope, formation semantics, history and discussions were reviewed.

Selection: Batch46 fixed strict path order, index 8; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031561 | data/structures/other/cellular_bud_tip_polarisome.yaml | maintained | cellular bud tip polarisome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031561 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031561 | Focused validator passed. |
| Focused native proteins | passed | True | GO:0031561 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Focused native graphs | passed | True | GO:0031561 | Read-only native check passed; claim-level protein/edge support evaluated separately. |
| Claim-level scientific review | passed | True | GO:0031561 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031561 | 11 of 14 collected target identifiers returned OK. PMID:12361575: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:31699995: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:41065574: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031561 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031561 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031561 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031561 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031561 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Localized polarisome identity

identity: supported. Targets: GO:0031561.

The exact GO term denotes the polarisome at the tip of a growing fungal bud. Its generic-polarisome is_a and regional part_of are supported and distinct. The record does not substitute the whole cellular region for the complex.

### Species, reference strain and phase

scope: supported. Targets: GO:0031561.

Species4932 and reference strain559292 resolve correctly. COMMON means present in most members with exceptional losses; localization in ordinary budding-yeast experiments provides qualitative support, not a prevalence census. The accession strain does not silently assign every cited experiment to S288C.

### Verified protein examples and native citations

grounding: supported. Targets: GO:0031561.

The reviewed accessions, gene symbols/aliases and S288C taxon are correct; exact-symbol reviewed queries return the retained entries. Native Spa2 bud-tip location citations are verified separately from the Valtz neck-localization evidence. Pea2 identity-only support is not upgraded to an unprovided native localization comment.

### Association scope and exact family candidates

grounding: supported. Targets: GO:0031561.

Spa2–Pea2 scaffold membership is strong; Bud6 membership is supported at the explicitly described co-sedimentation/proposed-complex tier. The record correctly avoids relabeling co-fractionation as purified reconstitution. Grouped scaffold and single Bud6 reviewed-label-only identities are not resolved by the inspected broader family or partial-domain candidates.

### Formation necessity remains bounded

grounding: unknown. Targets: GO:0031561.

CONDITIONAL is context-dependent formation necessity. Localization dependence and polarity/actin phenotypes do not establish which conditions require each cohort for complete tip-polarisome formation. Sheu even reports Spa2 localization in bud6Δ. Formation necessity is therefore unknown independently of supported membership and function; neither a universal requirement nor a biological contradiction is inferred.

### Historical proposed complex and contemporary annotation

evidence: supported. Targets: GO:0031561.

The canonical note identifies two-hybrid, co-IP and sedimentation rather than claiming purified structure. The discussion preserves the proposed 12S scope; Xie/Magliozzi independently support current location annotations and keep stress state, experimental strain and cable behavior separate.

### Descriptive proposed-complex graph

graph: supported. Targets: GO:0031561.

Five nodes and four edges distinguish Spa2–Pea2 association, Bud6 co-sedimentation, tip localization and polarity support. The NONMECHANISTIC FUNCTION graph and explanatory notes preserve the proposed 12S interpretation, without fixed stoichiometry or a reconstituted assembly sequence.

### Bounded inventory, source notes and history

completeness: supported. Targets: GO:0031561.

All current examples and source placements, history and discussions were reviewed. Open enrichment of additional polarisome members is not claimed to be a complete inventory; generic GO membership and later Aip5/Bni1 studies do not by themselves require every optional example in this localized record. Grouped and single-protein label-only mappings remain explicitly bounded.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/cellular_bud_tip_polarisome.yaml; Complete maintained YAML; all components, source notes, graphs, discussions and historical entries | context_only | The entire maintained target was read; no scientific record was changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes | context_only | ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic or transport function. |
| curation | docs/CURATION.md; Components; groundings; associated machinery and chaperone boundaries | context_only | Components are taxon-agnostic molecular families/classes; exact family grounding is preferred when verified. Mature constituents and assembled-structure maintenance machinery differ from transient preassembly chaperones. |
| micro46-shared-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005938,GO:0005737,GO:0005886,GO:0030479,GO:0005940,GO:0097610,GO:0110165,GO:0009986,GO:0097611,GO:0097612,GO:0005933,GO:0033101,GO:0005935,GO:0005934; Exact results for GO0005933/0005934/0005935: name, definition, children and relation types. | supports | The inspected GO0005933 cellular bud, GO0005934 cellular bud tip and GO0005935 cellular bud neck entries identify a whole outgrowth and its distinct regions. The tip is distal to the attachment; the neck is the mother-daughter constriction. Listed part_of children support the corresponding localized-polarisome boundaries. Unrelated entries in this combined response are not relied upon. |
| micro46-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031560,GO:0031561,GO:0000133,GO:0000145; Complete four exact term results: id/name/definition/isObsolete/children, including relation labels and PMID9632790 cross-reference. | supports | GO0031560 is the bud-neck polarisome and GO0031561 the growing-bud-tip polarisome; both are is_a children of GO0000133 and part_of their corresponding regions. Generic GO0000133 names Bni1, Spa2, Pea2 and Bud6, but does not make the present localized inventory exhaustive. GO0000145 is the exocyst tethering complex, distinct from the region receiving it. |
| micro46-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro46-valtz1996-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1083/jcb.135.3.725%22; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED8909546: Pea2 protein of yeast is localized to sites of polarized growth and is required for efficient mating and bipolar budding. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro46-valtz1996-pdf | https://pdfs.semanticscholar.org/8982/cdabd9dce19878a052f4e0fd2474e5ed5917.pdf; Printed pp725–726,728,731–735: abstract/introduction, growth and immunofluorescence methods, antibody controls, expression and localization Results; Fig3–6 captions. Extracted primary PDF text read; figure pixels not inspected. | supports | Valtz and Herskowitz directly localize Pea2 to incipient/small-bud growth sites and to the mother-daughter neck after nuclear division but before cytokinesis. The pattern matches Spa2. Pea2 loss reduces Spa2 localization without eliminating its abundance; Spa2 loss eliminates detectable Pea2 in these experiments. These results support localized scaffold membership and interdependence, not a census of all polarisome subunits or a universal formation-dependency assay. |
| micro46-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId 559292 identifies Saccharomyces cerevisiae S288C at rank strain; aliases and lineage match the record. Identity alone is not prevalence or experimental-condition evidence. |
| micro46-protein-P23201 | https://rest.uniprot.org/uniprotkb/P23201.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P23201 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SPA2']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro46-protein-P40091 | https://rest.uniprot.org/uniprotkb/P40091.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P40091 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['PEA2']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro46-protein-P41697 | https://rest.uniprot.org/uniprotkb/P41697.json; primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR LOCATION comments and their evidence joins; InterPro/Pfam cross-references. | supports | P41697 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['BUD6']. Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity localization and recombinant-study contexts remain distinguished; a native accession is not itself proof of each mechanistic edge. |
| micro46-gene-SPA2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPA2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete native result set for the exact query URL; reviewed taxon559292 only. | supports | The bounded reviewed S288C gene query for SPA2 returned 1 result: P23201. Aliases and gene names were inspected; no query collision was observed. |
| micro46-gene-PEA2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APEA2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete native result set for the exact query URL; reviewed taxon559292 only. | supports | The bounded reviewed S288C gene query for PEA2 returned 1 result: P40091. Aliases and gene names were inspected; no query collision was observed. |
| micro46-gene-BUD6 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABUD6%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete native result set for the exact query URL; reviewed taxon559292 only. | supports | The bounded reviewed S288C gene query for BUD6 returned 1 result: P41697. Aliases and gene names were inspected; no query collision was observed. |
| micro46-gene-AIP3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAIP3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete native result set for the exact query URL; reviewed taxon559292 only. | supports | The bounded reviewed S288C gene query for AIP3 returned 1 result: P41697. Aliases and gene names were inspected; no query collision was observed. |
| micro46-pmid12361575 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12361575%20AND%20SRC%3AMED; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED12361575: Spa2p functions as a scaffold-like protein to recruit the Mpk1p MAP kinase module to sites of polarized growth. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro46-pmid31699995 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A31699995%20AND%20SRC%3AMED; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED31699995: Polarisome scaffolder Spa2-mediated macromolecular condensation of Aip5 for actin polymerization. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro46-xie2019-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6838200/; Complete Results Sec3/Sec7 (including embedded Fig1/5/6 captions), Methods Sec10/Sec15. Main text/captions only; supplements and pixels not inspected. | supports | Xie2019 Sec3 supports Spa2-dependent Aip5 localization at growing tips/necks and colocalization with Bni1/Bud6; Sec7 separates physiological polarity sites from energy-depletion/pH stress condensates. Methods specify S288C strains and live imaging. This verifies the native location-citation context and does not turn a stress condensate or Aip5 into a mandatory inventory addition. |
| micro46-ipr-IPR039892 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039892/; metadata accession/name/type and complete description; family scope. | supports | IPR039892 is the Spa2/Sph1 protein family. It does not identify the combined Spa2-plus-Pea2 component cohort, whose members are distinct proteins. This candidate does not justify replacing the grouped reviewed-label-only identity with a single exact family. |
| micro46-sheu1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1128/MCB.18.7.4053%22; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED9632790: Spa2p interacts with cell polarity proteins and signaling components involved in yeast cell morphogenesis. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro46-pmid41065574 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A41065574%20AND%20SRC%3AMED; Exact native result id/title/authorString/pubYear/doi and complete abstractText. | supports | Unique MED41065574: Aip5 forms a "composite" actin nucleator with Bud6 and caps pointed ends of actin filaments. Authors/year/DOI and the complete native abstract were inspected. This row establishes bibliographic identity and abstract-level content only; detailed experiments require separately specified body evidence. |
| micro46-sheu1998-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC108990/; Complete Methods sec2/Table1, sec7/sec9/sec10; Results sec12/sec15/sec17/sec18 (embedded Fig1/2/4/5 captions and Table4); Discussion sec27. No figure pixels or later unrelated MAPK sections certified. | supports | Sheu1998 directly supports tight Spa2–Pea2 co-IP/two-hybrid association; Bud6 fragments interact in two-hybrid and much Bud6 co-sediments near 12S, but Spa2–Bud6 co-IP was unsuccessful. The paper proposes a 12S polarisome, notes additional candidate components, and reports GFP-Spa2 localization in bud6Δ. These are association and functional-context data, not purified three-component reconstitution or fixed stoichiometry. |
| micro46-magliozzi2025-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12916166/; Complete Results s4/s6 including embedded captions; Methods s10/s13/s14. The native PMID41065574 bud-tip annotation is thus checked against primary live imaging text; no pixels/videos inspected. | supports | Magliozzi2025 directly observes Bud6 puncta enriched at the bud tip and distinguishes their anterograde movement from Bni1/Aip5 retrograde movement. Actin cable phenotypes are not polarisome-formation assays. Methods explicitly use W303, distinct from the S288C reference accession taxon. |
| micro46-ipr-IPR005613 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005613/; Complete metadata accession/name/type and description; exact scope assessed. | supports | IPR005613 is an AIP3 C-terminal domain, not a complete Bud6 class. |
| micro46-ipr-IPR022782 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022782/; Complete metadata accession/name/type and description; exact scope assessed. | supports | IPR022782 is an AIP3-like C-terminal domain shared beyond the fungal Bud6 class. |
| micro46-ipr-IPR056279 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056279/; Complete metadata accession/name/type and description; exact scope assessed. | supports | IPR056279 is the Aip3/Bud6 N-terminal domain, a partial protein domain. |
| micro46-ipr-IPR051825 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051825/; Complete metadata accession/name/type and description; exact scope assessed. | supports | IPR051825 is the broader SRC kinase signaling inhibitor family; its description does not establish an exact taxon-agnostic Bud6 identity. |
| schema-result | just validate data/structures/other/cellular_bud_tip_polarisome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/cellular_bud_tip_polarisome.yaml |
| strict-result | just validate-strict data/structures/other/cellular_bud_tip_polarisome.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip_polarisome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/cellular_bud_tip_polarisome.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip_polarisome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip_polarisome-strict.tsv |
| native-proteins | /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/cellular_bud_tip_polarisome.yaml; Complete read-only focused native proteins log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-graphs | /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud_tip_polarisome.yaml; Complete read-only focused native graphs log | supports | data/structures/other/cellular_bud_tip_polarisome.yaml  (GO:0031561)<br>  bud_tip_12s_polarisome_topology	spa2_pea2_scaffold	COVERED	-&gt;spa2_pea2_scaffold (UniProtKB:P23201, UniProtKB:P40091)<br>  bud_tip_12s_polarisome_topology	bud6_actin_associated_polarity_protein	COVERED	-&gt;bud6_actin_associated_polarity_protein (UniProtKB:P41697)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/cellular_bud_tip_polarisome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 14 collected target identifiers returned OK. PMID:12361575: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:31699995: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:41065574: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- No raw microscopy pixels, supplementary files or videos were inspected. Figure captions were read only within the explicitly identified main-body sections.
- COMMON retains the schema meaning present in most members with exceptional losses. The cited yeast experiments support ordinary localized occurrence qualitatively, not a quantitative species-wide prevalence census.
- Only explicitly listed body sections were read; none of the retained access failures or HTML download/challenge responses is treated as full article text.
- Sheu Table1 identifies S288c backgrounds except starred strains; its two-hybrid strain is an explicit exception. Magliozzi2025 uses W303. Neither the S288C reference accession nor shared species identity erases these experimental differences.
- The inspected Bud6 candidates are partial domains or a broader family, and the scaffold is a multi-protein cohort. This bounded check is not an exhaustive claim that no usable future family grounding exists.
- Conditional formation-necessity labels remain independently unknown; membership, localization dependence, growth/polarity effects and complete complex formation are not interchangeable.
- Van Drogen2002 was read at complete native abstract tier only. Xie2019 and Magliozzi2025 body evidence is limited to the declared sections; no full-paper or supplementary validation is asserted.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- iModulonDB is not applicable to these localized polarity-complex identity, protein family, localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T045417Z-cellular-bud-tip-polarisome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of cellular bud tip polarisome
started_at: '2026-10-22T04:37:04Z'
finished_at: '2026-10-22T04:54:17Z'
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
summary: The localized polarisome identity, source-scoped membership, verified examples
  and descriptive graph are supported. Formation necessity and inventory completeness
  remain bounded; no confirmed curation issue was found.
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
  - path: data/structures/other/cellular_bud_tip_polarisome.yaml
    sha256: a76a9766b8a57ddf49ccd2ec08f36447edbd1b059469c12180aded338fb48f91
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
- target_id: GO:0031561
  path: data/structures/other/cellular_bud_tip_polarisome.yaml
  label: cellular bud tip polarisome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/cellular_bud_tip_polarisome.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; no neighboring scientific-record verdict
    is imported. Exact authority, all current component/function/graph/source placements,
    taxonomic scope, formation semantics, history and discussions were reviewed.
  selection: Batch46 fixed strict path order, index 8; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031561
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031561
  command: just validate data/structures/other/cellular_bud_tip_polarisome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031561
  command: just validate-strict data/structures/other/cellular_bud_tip_polarisome.yaml
    --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip_polarisome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-proteins
  name: Focused native proteins
  status: passed
  required: true
  target_ids:
  - GO:0031561
  command: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/cellular_bud_tip_polarisome.yaml
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
  - GO:0031561
  command: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud_tip_polarisome.yaml
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
  - GO:0031561
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - micro46-shared-go
  - micro46-go
  - micro46-tax4932
  - micro46-valtz1996-meta
  - micro46-valtz1996-pdf
  - micro46-tax559292
  - micro46-protein-P23201
  - micro46-protein-P40091
  - micro46-protein-P41697
  - micro46-gene-SPA2
  - micro46-gene-PEA2
  - micro46-gene-BUD6
  - micro46-gene-AIP3
  - micro46-pmid12361575
  - micro46-pmid31699995
  - micro46-xie2019-legacy
  - micro46-ipr-IPR039892
  - micro46-sheu1998-meta
  - micro46-pmid41065574
  - micro46-sheu1998-legacy
  - micro46-magliozzi2025-legacy
  - micro46-ipr-IPR005613
  - micro46-ipr-IPR022782
  - micro46-ipr-IPR056279
  - micro46-ipr-IPR051825
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031561
  summary: '11 of 14 collected target identifiers returned OK. PMID:12361575: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:31699995:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:41065574: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - micro46-pmid12361575
  - micro46-pmid31699995
  - micro46-pmid41065574
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031561
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031561
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031561
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031561
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031561
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
    and current batch46 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/cellular_bud_tip_polarisome.yaml
  locator: Complete maintained YAML; all components, source notes, graphs, discussions
    and historical entries
  accessed_at: '2026-10-22T04:48:43Z'
  support: context_only
  summary: The entire maintained target was read; no scientific record was changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; ComponentTypeEnum; EssentialityEnum; graph scopes
  accessed_at: '2026-10-22T04:48:43Z'
  support: context_only
  summary: ComponentTypeEnum distinguishes LIPID from the permitted OTHER composite
    class. ESSENTIAL concerns failure of structure formation, not merely loss of catalytic
    or transport function.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components; groundings; associated machinery and chaperone boundaries
  accessed_at: '2026-10-22T04:48:43Z'
  support: context_only
  summary: Components are taxon-agnostic molecular families/classes; exact family
    grounding is preferred when verified. Mature constituents and assembled-structure
    maintenance machinery differ from transient preassembly chaperones.
- evidence_id: micro46-shared-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005938,GO:0005737,GO:0005886,GO:0030479,GO:0005940,GO:0097610,GO:0110165,GO:0009986,GO:0097611,GO:0097612,GO:0005933,GO:0033101,GO:0005935,GO:0005934
  locator: 'Exact results for GO0005933/0005934/0005935: name, definition, children
    and relation types.'
  accessed_at: '2026-10-22T04:38:31.207999Z'
  support: supports
  summary: The inspected GO0005933 cellular bud, GO0005934 cellular bud tip and GO0005935
    cellular bud neck entries identify a whole outgrowth and its distinct regions.
    The tip is distal to the attachment; the neck is the mother-daughter constriction.
    Listed part_of children support the corresponding localized-polarisome boundaries.
    Unrelated entries in this combined response are not relied upon.
  snapshot_sha256: 04958c90f60f753443ae327ebf353b3ab6ac7a8bfaf5cea58634921b40b55b5a
- evidence_id: micro46-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031560,GO:0031561,GO:0000133,GO:0000145
  locator: 'Complete four exact term results: id/name/definition/isObsolete/children,
    including relation labels and PMID9632790 cross-reference.'
  accessed_at: '2026-10-22T04:42:12.245944Z'
  support: supports
  summary: GO0031560 is the bud-neck polarisome and GO0031561 the growing-bud-tip
    polarisome; both are is_a children of GO0000133 and part_of their corresponding
    regions. Generic GO0000133 names Bni1, Spa2, Pea2 and Bud6, but does not make
    the present localized inventory exhaustive. GO0000145 is the exocyst tethering
    complex, distinct from the region receiving it.
  snapshot_sha256: a1ee5792ff712e6ca100621f8ac56712c2d64004b5a8e1dfa383c387714819f3
- evidence_id: micro46-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:38:31.951602Z'
  support: supports
  summary: ENA taxId 4932 identifies Saccharomyces cerevisiae at rank species; aliases
    and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: micro46-valtz1996-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1083/jcb.135.3.725%22
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:38:32.557137Z'
  support: supports
  summary: 'Unique MED8909546: Pea2 protein of yeast is localized to sites of polarized
    growth and is required for efficient mating and bipolar budding. Authors/year/DOI
    and the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 5995f18fa905450fc26415293cae1475f7acb5da7cc4752f3db0356906c58c43
- evidence_id: micro46-valtz1996-pdf
  kind: primary_source
  reference: https://pdfs.semanticscholar.org/8982/cdabd9dce19878a052f4e0fd2474e5ed5917.pdf
  locator: 'Printed pp725–726,728,731–735: abstract/introduction, growth and immunofluorescence
    methods, antibody controls, expression and localization Results; Fig3–6 captions.
    Extracted primary PDF text read; figure pixels not inspected.'
  accessed_at: '2026-10-21T09:48:11.208322Z'
  support: supports
  summary: Valtz and Herskowitz directly localize Pea2 to incipient/small-bud growth
    sites and to the mother-daughter neck after nuclear division but before cytokinesis.
    The pattern matches Spa2. Pea2 loss reduces Spa2 localization without eliminating
    its abundance; Spa2 loss eliminates detectable Pea2 in these experiments. These
    results support localized scaffold membership and interdependence, not a census
    of all polarisome subunits or a universal formation-dependency assay.
  snapshot_sha256: c06951939912dcb3700b5cd867b40a7d9c2a74f41460bb93f31839852509d9c9
- evidence_id: micro46-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T04:42:12.246278Z'
  support: supports
  summary: ENA taxId 559292 identifies Saccharomyces cerevisiae S288C at rank strain;
    aliases and lineage match the record. Identity alone is not prevalence or experimental-condition
    evidence.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: micro46-protein-P23201
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P23201.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:42:12.246336Z'
  support: supports
  summary: P23201 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['SPA2'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 04c2e80fad38fe6e6ff321c0661be8951f68dfd056da5f2662b72c808c5a4a91
- evidence_id: micro46-protein-P40091
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40091.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:42:12.246520Z'
  support: supports
  summary: P40091 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['PEA2'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 1e0c1e20310c86d389b0610f0d5f3adaba9951470df79ccc72559b9a7a1b5b24
- evidence_id: micro46-protein-P41697
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41697.json
  locator: primaryAccession/entryType; organism; proteinDescription; genes; full SUBCELLULAR
    LOCATION comments and their evidence joins; InterPro/Pfam cross-references.
  accessed_at: '2026-10-22T04:42:12.246493Z'
  support: supports
  summary: P41697 is UniProtKB reviewed (Swiss-Prot), taxon 559292, genes ['BUD6'].
    Recommended identity, gene aliases, full SUBCELLULAR LOCATION comments, evidence
    codes/PMIDs and InterPro/Pfam cross-references were inspected. Direct, inferred/by-similarity
    localization and recombinant-study contexts remain distinguished; a native accession
    is not itself proof of each mechanistic edge.
  snapshot_sha256: 0abda308efd037012fe40e3ee0abf4b455b7ceb6dd60b67a2afaf835a2db2c01
- evidence_id: micro46-gene-SPA2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPA2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete native result set for the exact query URL; reviewed taxon559292
    only.
  accessed_at: '2026-10-22T04:42:13.035823Z'
  support: supports
  summary: 'The bounded reviewed S288C gene query for SPA2 returned 1 result: P23201.
    Aliases and gene names were inspected; no query collision was observed.'
  snapshot_sha256: 34ccb79e3ea14b36c7c9d42d3a3d8faee4632994622d7e6e5bcddd1bc35492ff
  search_scope: Remote UniProt reviewed proteins for exact query symbol SPA2 and organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro46-gene-PEA2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APEA2%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete native result set for the exact query URL; reviewed taxon559292
    only.
  accessed_at: '2026-10-22T04:42:13.036598Z'
  support: supports
  summary: 'The bounded reviewed S288C gene query for PEA2 returned 1 result: P40091.
    Aliases and gene names were inspected; no query collision was observed.'
  snapshot_sha256: e197de95c326fa8328781dd6e431371e916d071c042e8500dd80d84b97617f47
  search_scope: Remote UniProt reviewed proteins for exact query symbol PEA2 and organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro46-gene-BUD6
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABUD6%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete native result set for the exact query URL; reviewed taxon559292
    only.
  accessed_at: '2026-10-22T04:42:13.136021Z'
  support: supports
  summary: 'The bounded reviewed S288C gene query for BUD6 returned 1 result: P41697.
    Aliases and gene names were inspected; no query collision was observed.'
  snapshot_sha256: 934fc25e5008f7ffbd019810fe413600a2f56905d184e8a4e757e4225317c4d5
  search_scope: Remote UniProt reviewed proteins for exact query symbol BUD6 and organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro46-gene-AIP3
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAIP3%29%20AND%20%28organism_id%3A559292%29%20AND%20%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete native result set for the exact query URL; reviewed taxon559292
    only.
  accessed_at: '2026-10-22T04:42:13.182669Z'
  support: supports
  summary: 'The bounded reviewed S288C gene query for AIP3 returned 1 result: P41697.
    Aliases and gene names were inspected; no query collision was observed.'
  snapshot_sha256: 934fc25e5008f7ffbd019810fe413600a2f56905d184e8a4e757e4225317c4d5
  search_scope: Remote UniProt reviewed proteins for exact query symbol AIP3 and organism_id559292
    only; complete returned result set inspected. Local ignored files are not applicable
    to this remote query.
- evidence_id: micro46-pmid12361575
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12361575%20AND%20SRC%3AMED
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:42:14.158554Z'
  support: supports
  summary: 'Unique MED12361575: Spa2p functions as a scaffold-like protein to recruit
    the Mpk1p MAP kinase module to sites of polarized growth. Authors/year/DOI and
    the complete native abstract were inspected. This row establishes bibliographic
    identity and abstract-level content only; detailed experiments require separately
    specified body evidence.'
  snapshot_sha256: 0282aceb622315b57ea330e4b0253425fa3ec6800cd8a68ef20d02bbe1b6f6f3
- evidence_id: micro46-pmid31699995
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A31699995%20AND%20SRC%3AMED
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:42:14.171931Z'
  support: supports
  summary: 'Unique MED31699995: Polarisome scaffolder Spa2-mediated macromolecular
    condensation of Aip5 for actin polymerization. Authors/year/DOI and the complete
    native abstract were inspected. This row establishes bibliographic identity and
    abstract-level content only; detailed experiments require separately specified
    body evidence.'
  snapshot_sha256: 0d8535587617f7053fd4101b48cd07d595bc18e4fb11d397cd60f4eec45c5414
- evidence_id: micro46-xie2019-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6838200/
  locator: Complete Results Sec3/Sec7 (including embedded Fig1/5/6 captions), Methods
    Sec10/Sec15. Main text/captions only; supplements and pixels not inspected.
  accessed_at: '2026-10-22T04:42:46.388559Z'
  support: supports
  summary: Xie2019 Sec3 supports Spa2-dependent Aip5 localization at growing tips/necks
    and colocalization with Bni1/Bud6; Sec7 separates physiological polarity sites
    from energy-depletion/pH stress condensates. Methods specify S288C strains and
    live imaging. This verifies the native location-citation context and does not
    turn a stress condensate or Aip5 into a mandatory inventory addition.
  snapshot_sha256: b383ba5d5cc1e667dc40ead0daba4b0bd599f2a4dc2c7defb89a09901626cf8f
- evidence_id: micro46-ipr-IPR039892
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039892/
  locator: metadata accession/name/type and complete description; family scope.
  accessed_at: '2026-10-22T04:42:46.699026Z'
  support: supports
  summary: IPR039892 is the Spa2/Sph1 protein family. It does not identify the combined
    Spa2-plus-Pea2 component cohort, whose members are distinct proteins. This candidate
    does not justify replacing the grouped reviewed-label-only identity with a single
    exact family.
  snapshot_sha256: 6476f3f836012c74087ca05a1402415a40723e51e74135035b060d96fafabc01
- evidence_id: micro46-sheu1998-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1128/MCB.18.7.4053%22
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:42:14.006374Z'
  support: supports
  summary: 'Unique MED9632790: Spa2p interacts with cell polarity proteins and signaling
    components involved in yeast cell morphogenesis. Authors/year/DOI and the complete
    native abstract were inspected. This row establishes bibliographic identity and
    abstract-level content only; detailed experiments require separately specified
    body evidence.'
  snapshot_sha256: 4734aea3824b4b0174bc6b7df283e7692799ac3878fc20e1069d8fac42c4d44d
- evidence_id: micro46-pmid41065574
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A41065574%20AND%20SRC%3AMED
  locator: Exact native result id/title/authorString/pubYear/doi and complete abstractText.
  accessed_at: '2026-10-22T04:42:14.329352Z'
  support: supports
  summary: 'Unique MED41065574: Aip5 forms a "composite" actin nucleator with Bud6
    and caps pointed ends of actin filaments. Authors/year/DOI and the complete native
    abstract were inspected. This row establishes bibliographic identity and abstract-level
    content only; detailed experiments require separately specified body evidence.'
  snapshot_sha256: 53a90f67e58d8f655792fa7cd0dc662685d390e9caf429dcc59cf31e8999cf5c
- evidence_id: micro46-sheu1998-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC108990/
  locator: Complete Methods sec2/Table1, sec7/sec9/sec10; Results sec12/sec15/sec17/sec18
    (embedded Fig1/2/4/5 captions and Table4); Discussion sec27. No figure pixels
    or later unrelated MAPK sections certified.
  accessed_at: '2026-10-22T04:42:46.388070Z'
  support: supports
  summary: Sheu1998 directly supports tight Spa2–Pea2 co-IP/two-hybrid association;
    Bud6 fragments interact in two-hybrid and much Bud6 co-sediments near 12S, but
    Spa2–Bud6 co-IP was unsuccessful. The paper proposes a 12S polarisome, notes additional
    candidate components, and reports GFP-Spa2 localization in bud6Δ. These are association
    and functional-context data, not purified three-component reconstitution or fixed
    stoichiometry.
  snapshot_sha256: aa8b6a329520c159204c92d7cf9f8af124606aeee8f081a8cf7ba74ba89b4df7
- evidence_id: micro46-magliozzi2025-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC12916166/
  locator: Complete Results s4/s6 including embedded captions; Methods s10/s13/s14.
    The native PMID41065574 bud-tip annotation is thus checked against primary live
    imaging text; no pixels/videos inspected.
  accessed_at: '2026-10-22T04:42:46.388517Z'
  support: supports
  summary: Magliozzi2025 directly observes Bud6 puncta enriched at the bud tip and
    distinguishes their anterograde movement from Bni1/Aip5 retrograde movement. Actin
    cable phenotypes are not polarisome-formation assays. Methods explicitly use W303,
    distinct from the S288C reference accession taxon.
  snapshot_sha256: ac363ee44e1abf0ce80769045be8094312543c83ec6a3037d2a7cff8b546ea72
- evidence_id: micro46-ipr-IPR005613
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005613/
  locator: Complete metadata accession/name/type and description; exact scope assessed.
  accessed_at: '2026-10-22T04:42:47.311641Z'
  support: supports
  summary: IPR005613 is an AIP3 C-terminal domain, not a complete Bud6 class.
  snapshot_sha256: fb5fcc01176bdf1c791037a95e8eea506334e800026596c02dd9bdfdcc98143c
- evidence_id: micro46-ipr-IPR022782
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR022782/
  locator: Complete metadata accession/name/type and description; exact scope assessed.
  accessed_at: '2026-10-22T04:42:47.387020Z'
  support: supports
  summary: IPR022782 is an AIP3-like C-terminal domain shared beyond the fungal Bud6
    class.
  snapshot_sha256: 45872d65da30d7a0b70a6e7e5b32d8573ae6351e73d78a548bc04ebe6eea1443
- evidence_id: micro46-ipr-IPR056279
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056279/
  locator: Complete metadata accession/name/type and description; exact scope assessed.
  accessed_at: '2026-10-22T04:42:47.471816Z'
  support: supports
  summary: IPR056279 is the Aip3/Bud6 N-terminal domain, a partial protein domain.
  snapshot_sha256: cbd0232d0cf6250d7501d90b3e9ba586552b5dae84dc660b420addb4a7761ce9
- evidence_id: micro46-ipr-IPR051825
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051825/
  locator: Complete metadata accession/name/type and description; exact scope assessed.
  accessed_at: '2026-10-22T04:42:47.150652Z'
  support: supports
  summary: IPR051825 is the broader SRC kinase signaling inhibitor family; its description
    does not establish an exact taxon-agnostic Bud6 identity.
  snapshot_sha256: 34dc77dcf99b4747caa75d530205831b3d9edd66f5e4df7833319637fb3bb245
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/cellular_bud_tip_polarisome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:37:06Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/cellular_bud_tip_polarisome.yaml'
  snapshot_sha256: e27397a29a395cb4634fa52c4f5d4623093b69b67e8723af77e50464746b356a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/cellular_bud_tip_polarisome.yaml
    --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip_polarisome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:37:07Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/cellular_bud_tip_polarisome.yaml\
    \ --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip_polarisome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/cellular_bud_tip_polarisome-strict.tsv"
  snapshot_sha256: ba03de6aa4643ebe472e0ebd1c56e3613c68a85868ff9f3ce89d6ecd61d11154
- evidence_id: native-proteins
  kind: validation
  reference: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/cellular_bud_tip_polarisome.yaml
  locator: Complete read-only focused native proteins log
  accessed_at: '2026-10-22T04:43:23.608446Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/cellular_bud_tip_polarisome.yaml
  locator: Complete read-only focused native graphs log
  accessed_at: '2026-10-22T04:43:24.075467Z'
  support: supports
  summary: "data/structures/other/cellular_bud_tip_polarisome.yaml  (GO:0031561)\n\
    \  bud_tip_12s_polarisome_topology\tspa2_pea2_scaffold\tCOVERED\t->spa2_pea2_scaffold\
    \ (UniProtKB:P23201, UniProtKB:P40091)\n  bud_tip_12s_polarisome_topology\tbud6_actin_associated_polarity_protein\t\
    COVERED\t->bud6_actin_associated_polarity_protein (UniProtKB:P41697)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 9b2cb3a14eac55e63ef1c711781fedc164344a3bf6f27f1229e1c9e9ad5441ee
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/cellular_bud_tip_polarisome.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 14 collected target identifiers returned OK. PMID:12361575: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:31699995:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:41065574: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
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
  topic: Localized polarisome identity
  outcome: supported
  target_ids:
  - GO:0031561
  summary: The exact GO term denotes the polarisome at the tip of a growing fungal
    bud. Its generic-polarisome is_a and regional part_of are supported and distinct.
    The record does not substitute the whole cellular region for the complex.
  evidence_ids:
  - micro46-go
  - micro46-shared-go
- assessment_id: scope
  area: scope
  topic: Species, reference strain and phase
  outcome: supported
  target_ids:
  - GO:0031561
  summary: Species4932 and reference strain559292 resolve correctly. COMMON means
    present in most members with exceptional losses; localization in ordinary budding-yeast
    experiments provides qualitative support, not a prevalence census. The accession
    strain does not silently assign every cited experiment to S288C.
  evidence_ids:
  - micro46-tax4932
  - micro46-tax559292
  - micro46-valtz1996-pdf
  - schema
- assessment_id: proteins
  area: grounding
  topic: Verified protein examples and native citations
  outcome: supported
  target_ids:
  - GO:0031561
  summary: The reviewed accessions, gene symbols/aliases and S288C taxon are correct;
    exact-symbol reviewed queries return the retained entries. Native Spa2 bud-tip
    location citations are verified separately from the Valtz neck-localization evidence.
    Pea2 identity-only support is not upgraded to an unprovided native localization
    comment.
  evidence_ids:
  - micro46-protein-P23201
  - micro46-protein-P40091
  - micro46-protein-P41697
  - micro46-gene-SPA2
  - micro46-gene-PEA2
  - micro46-gene-BUD6
  - micro46-gene-AIP3
  - micro46-pmid12361575
  - micro46-pmid31699995
  - micro46-xie2019-legacy
  - micro46-valtz1996-pdf
- assessment_id: components
  area: grounding
  topic: Association scope and exact family candidates
  outcome: supported
  target_ids:
  - GO:0031561
  summary: Spa2–Pea2 scaffold membership is strong; Bud6 membership is supported at
    the explicitly described co-sedimentation/proposed-complex tier. The record correctly
    avoids relabeling co-fractionation as purified reconstitution. Grouped scaffold
    and single Bud6 reviewed-label-only identities are not resolved by the inspected
    broader family or partial-domain candidates.
  evidence_ids:
  - micro46-sheu1998-legacy
  - micro46-sheu1998-meta
  - micro46-ipr-IPR039892
  - micro46-ipr-IPR005613
  - micro46-ipr-IPR022782
  - micro46-ipr-IPR056279
  - micro46-ipr-IPR051825
  - record
  - curation
- assessment_id: necessity
  area: grounding
  topic: Formation necessity remains bounded
  outcome: unknown
  target_ids:
  - GO:0031561
  summary: CONDITIONAL is context-dependent formation necessity. Localization dependence
    and polarity/actin phenotypes do not establish which conditions require each cohort
    for complete tip-polarisome formation. Sheu even reports Spa2 localization in
    bud6Δ. Formation necessity is therefore unknown independently of supported membership
    and function; neither a universal requirement nor a biological contradiction is
    inferred.
  evidence_ids:
  - micro46-sheu1998-legacy
  - micro46-magliozzi2025-legacy
  - schema
  - record
- assessment_id: function
  area: evidence
  topic: Historical proposed complex and contemporary annotation
  outcome: supported
  target_ids:
  - GO:0031561
  summary: The canonical note identifies two-hybrid, co-IP and sedimentation rather
    than claiming purified structure. The discussion preserves the proposed 12S scope;
    Xie/Magliozzi independently support current location annotations and keep stress
    state, experimental strain and cable behavior separate.
  evidence_ids:
  - micro46-sheu1998-meta
  - micro46-sheu1998-legacy
  - micro46-xie2019-legacy
  - micro46-magliozzi2025-legacy
  - micro46-pmid41065574
  - record
- assessment_id: graph
  area: graph
  topic: Descriptive proposed-complex graph
  outcome: supported
  target_ids:
  - GO:0031561
  summary: Five nodes and four edges distinguish Spa2–Pea2 association, Bud6 co-sedimentation,
    tip localization and polarity support. The NONMECHANISTIC FUNCTION graph and explanatory
    notes preserve the proposed 12S interpretation, without fixed stoichiometry or
    a reconstituted assembly sequence.
  evidence_ids:
  - micro46-go
  - micro46-sheu1998-legacy
  - micro46-valtz1996-pdf
  - record
- assessment_id: coverage
  area: completeness
  topic: Bounded inventory, source notes and history
  outcome: supported
  target_ids:
  - GO:0031561
  summary: All current examples and source placements, history and discussions were
    reviewed. Open enrichment of additional polarisome members is not claimed to be
    a complete inventory; generic GO membership and later Aip5/Bni1 studies do not
    by themselves require every optional example in this localized record. Grouped
    and single-protein label-only mappings remain explicitly bounded.
  evidence_ids:
  - micro46-go
  - micro46-ipr-IPR039892
  - micro46-xie2019-legacy
  - record
  - curation
findings: []
actions: []
limitations:
- No raw microscopy pixels, supplementary files or videos were inspected. Figure captions
  were read only within the explicitly identified main-body sections.
- COMMON retains the schema meaning present in most members with exceptional losses.
  The cited yeast experiments support ordinary localized occurrence qualitatively,
  not a quantitative species-wide prevalence census.
- Only explicitly listed body sections were read; none of the retained access failures
  or HTML download/challenge responses is treated as full article text.
- Sheu Table1 identifies S288c backgrounds except starred strains; its two-hybrid
  strain is an explicit exception. Magliozzi2025 uses W303. Neither the S288C reference
  accession nor shared species identity erases these experimental differences.
- The inspected Bud6 candidates are partial domains or a broader family, and the scaffold
  is a multi-protein cohort. This bounded check is not an exhaustive claim that no
  usable future family grounding exists.
- Conditional formation-necessity labels remain independently unknown; membership,
  localization dependence, growth/polarity effects and complete complex formation
  are not interchangeable.
- Van Drogen2002 was read at complete native abstract tier only. Xie2019 and Magliozzi2025
  body evidence is limited to the declared sections; no full-paper or supplementary
  validation is asserted.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- iModulonDB is not applicable to these localized polarity-complex identity, protein
  family, localization and formation claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
