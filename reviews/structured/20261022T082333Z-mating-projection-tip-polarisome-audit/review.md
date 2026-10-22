# Source-grounded review of mating projection tip polarisome

- Review: 20261022T082333Z-mating-projection-tip-polarisome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:57:51Z
- Finished UTC: 2026-10-22T08:23:33Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding asks for condition-specific assembly evidence or qualification of three CONDITIONAL essentiality assignments. Exact localized identity, grouped scaffold boundary, reference proteins and nonmechanistic projection-cycle graph remain supported.

## Scope And Provenance

Exactly one complete target; all evidence tiers and limitations declared individually.

Selection: One complete record in strict-path batch59 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031563 | data/structures/other/mating_projection_tip_polarisome.yaml | maintained | mating projection tip polarisome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031563 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031563 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0031563 | Focused native check passed; scientific claims are assessed separately. |
| Native focused verify | passed | True | GO:0031563 | Focused native check passed; scientific claims are assessed separately. |
| Initial protein verification transport attempt | failed | False | GO:0031563 | Sandbox DNS prevented source access; final required retry passed. |
| Expression-module applicability | not_applicable | False | GO:0031563 | No expression-module claim is assessed; native authorities and direct source scopes address the target. |
| Claim-level scientific review | passed | True | GO:0031563 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031563 | 12 of 15 collected target identifiers returned OK. PMID:12361575: UNREACHABLE; Native Europe PMC uniquely identifies MED12361575: Spa2p functions as a scaffold-like protein to recruit the Mpk1p MAP kinase module to sites of polarized growth. (2002); DOI10.1016/s0960-9822(02)01186-7. Identifier transport verification is distinct from separately scoped primary-source reading.; PMID:31699995: UNREACHABLE; Native Europe PMC uniquely identifies MED31699995: Polarisome scaffolder Spa2-mediated macromolecular condensation of Aip5 for actin polymerization. (2019); DOI10.1038/s41467-019-13125-1. Identifier transport verification is distinct from separately scoped primary-source reading.; PMID:41065574: UNREACHABLE; Native Europe PMC uniquely identifies MED41065574: Aip5 forms a "composite" actin nucleator with Bud6 and caps pointed ends of actin filaments. (2025); DOI10.1083/jcb.202505039. Identifier transport verification is distinct from separately scoped primary-source reading. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031563 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031563 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031563 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031563 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031563 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Localized subtype retains exact identity

identity: supported. Targets: GO:0031563.

The mating-tip polarisome is the GO0031563 subtype of the broader polarisome and is localized at the projection tip. A grouped Spa2/Pea2 scaffold cohort is explicitly functional, not described as one homologous family.

### No verified exact replacement among inspected family candidates

grounding: supported. Targets: GO:0031563.

The available native families are broader than the named components, domain-only, or empty candidate-subfamily responses. The bounded search supports retaining the explicit label-only tasks; it does not establish absence from every authority.

### Composition and phenotype boundaries are explicit

evidence: supported. Targets: GO:0031563.

The source and GO boundary identify Spa2/Pea2, Bni1 and Bud6 as polarisome constituents. The record explicitly omits a Bud6 periodic-projection edge because its deletion had no observed effect in that assay, and keeps Cdc42 regulators and Fus proteins outside the complex boundary.

### Conditional formation claims need their own support

evidence: concern. Targets: GO:0031563.

All three component rows assert CONDITIONAL essentiality, but neither a condition/lineage nor a direct whole-polarisome formation dependency is stated. The cited localization/stability and projection-cycle phenotypes do not by themselves establish this assembly requirement, especially for Bud6 with no projection phenotype in the stated assay.

### Reference proteins and assay strains remain separate

scope: unknown. Targets: GO:0031563.

The reference proteins are reviewed S288C entries. Bidlingmaier uses S288C-congenic strains, while Valtz TableI lists its own isogenic strain series; that series was not independently assigned S288C. VARIABLE prevalence remains unknown rather than redefined as pheromone induction.

### Bounded topology and projection-cycle support

graph: supported. Targets: GO:0031563.

Spa2/Pea2 localization and Bni1 support for periodic projection formation match the sources. The graph is explicitly nonmechanistic, does not assert a complete actin pathway, and appropriately excludes the unsupported Bud6 phenotype edge.

### Complete target with bounded evidence tiers

completeness: supported. Targets: GO:0031563.

Every maintained target field, evidence item, graph node/edge, history entry and discussion was inspected. Optional empty fields and scientific unknowns are not manufactured into defects.

## Findings

### F1: Support or qualify the conditional essentiality assignments

minor / open / confirmed; issue key: mating-tip-polarisome-conditional-formation-support.

Spa2/Pea2, Bni1 and Bud6 are all coded CONDITIONAL without a stated formation condition or lineage. The nearest evidence establishes localization/stability or periodic projection phenotypes; it does not establish whole-complex formation requirements under named conditions. The Bud6 note expressly reports no projection-frequency or morphology effect in the cited assay. This is an unsupported nonempty dependency assertion, not a demand to fill an optional field.

## Recommended Actions And Acceptance Checks

### A1

For each named component, document the precise condition/lineage and a source-backed assembly requirement, or qualify the formation status as unknown while retaining supported membership and functional phenotypes.

- Do not infer complex formation from growth, projection timing, localization or activity alone.
- Do not infer universal dispensability from the negative Bud6 projection assay.
- Preserve the existing nonmechanistic graph and component-boundary explanations.
- Pass applicable schema, strict, protein and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/mating_projection_tip_polarisome.yaml; Entire maintained YAML, history and discussions | context_only | The entire target was read after inspection. This maintained YAML owns any scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and graph scope | context_only | CONDITIONAL denotes required under some conditions or in some lineages. VARIABLE denotes patchy lineage/strain presence rather than cell state. UNKNOWN formation necessity and unpopulated optional fields are not automatically defects. |
| curation | docs/CURATION.md; Exact identity, component classes and claim-level evidence | context_only | Protein reference identity, biological membership, localization and formation necessity require distinct evidence. A grouped functional cohort is not automatically a homologous family. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Descriptive versus mechanistic graph scope | context_only | An explicitly nonmechanistic graph can faithfully record regional topology, membership and broad function without a complete molecular pathway. |
| root59-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000133,GO:0005937,GO:0006260,GO:0031382,GO:0031563,GO:0032991,GO:0042555,GO:0043332,GO:0070867,GO:0097362,GO:1990819; All eleven focal term identities/status/definitions/synonyms; relevant typed child links only for the large generic protein-complex child list | supports | Native exact GO identities and definitions distinguish the mating-projection tip region, its localized polarisome, the broader polarisome and the generic hexameric MCM class. Typed links were checked separately from mixed-relation ancestry. |
| root59-sources-GO0031563-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031563/ancestors?relations=is_a,part_of; Complete target ancestry; typed direct relationships checked jointly against the GO term responses | supports | The exact target ancestry is consistent with the stated parent or parthood context; mixed is_a/part_of ancestry is not treated as proof of one relation type. |
| root59-sources-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native name/rank/lineage response | supports | Native taxonomy confirms Saccharomyces cerevisiae, taxon4932, rank species. |
| root59-sources-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native name/rank/lineage response | supports | Native taxonomy confirms Saccharomyces cerevisiae S288C, taxon559292, rank strain. |
| root59-sources-pmid-12361575 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12361575+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED bibliography/DOI/PMCID and complete abstractText | supports | MED12361575: Spa2p functions as a scaffold-like protein to recruit the Mpk1p MAP kinase module to sites of polarized growth. van Drogen F, Peter M. (2002); DOI10.1016/s0960-9822(02)01186-7. Native full abstract read; primary-body evidence is claimed only where separately listed. |
| root59-sources-pmid-31699995 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A31699995+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED bibliography/DOI/PMCID and complete abstractText | supports | MED31699995: Polarisome scaffolder Spa2-mediated macromolecular condensation of Aip5 for actin polymerization. Xie Y, Sun J, Han X, Turšić-Wunder A, Toh JDW, Hong W, Gao YG, Miao Y. (2019); DOI10.1038/s41467-019-13125-1. Native full abstract read; primary-body evidence is claimed only where separately listed. |
| root59-sources-pmid-41065574 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A41065574+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED bibliography/DOI/PMCID and complete abstractText | supports | MED41065574: Aip5 forms a "composite" actin nucleator with Bud6 and caps pointed ends of actin filaments. Magliozzi JO, Runyan LA, Welsh A, Padrick SB, Goode BL. (2025); DOI10.1083/jcb.202505039. Native full abstract read; primary-body evidence is claimed only where separately listed. |
| root59-sources-doi-10.1083_jcb.200307065 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200307065%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI-to-MED identity and complete abstractText | supports | Unique DOI result identifies MED14734532: Regulation of polarized growth initiation and termination cycles by the polarisome and Cdc42 regulators. (2004). Complete abstract and bibliography read. |
| root59-sources-doi-10.1083_jcb.135.3.725 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.135.3.725%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI-to-MED identity and complete abstractText | supports | Unique DOI result identifies MED8909546: Pea2 protein of yeast is localized to sites of polarized growth and is required for efficient mating and bipolar budding. (1996). Complete abstract and bibliography read. |
| root59-sources-PMC2172334-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2172334/fullTextXML; Genuine JATS: Introduction section index0; Results indices4/5; Discussion index10 opening topic; all Methods indices17–20 including TableI; embedded captions within these sections. No other Results/Discussion or figure pixels. | supports | Bidlingmaier2004 assayed pheromone-induced projection initiation/termination in S288C-congenic cells. Spa2, Pea2 and Bni1 deletions delay repeated initiation and disrupt termination; bud6 deletion did not change projection frequency or morphology in this assay. These are phenotype/functional observations, not direct measurements of whole-polarisome formation. |
| access-PMC2172334-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2172334/; Response status and diagnostic content only | context_only | HTTP200 returned a browser challenge rather than readable article text; genuine XML was inspected separately. |
| root59-sources-valtz1996-pmc-pdf | https://europepmc.org/articles/PMC2121064?pdf=render; Genuine scanned PDF extraction: printed pages731,732,733,735,736 in full; TableI on727; first25 lines of Discussion page739. No remaining discussion, figure pixels or supplemental data. | supports | Valtz1996 localized Pea2 and Spa2 to polarized sites in budding and mating cells and found reciprocal requirements for normal localization/stability. Its physical-complex interpretation remains a suggestion rather than direct binding or universal assembly proof. |
| root59-sources-PMC6838200-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6838200/fullTextXML; Genuine JATS Sec1,Sec3 including Figure1 caption,Sec10 andSec15 in full. Other Results/Methods, figure pixels and raw data not read. | supports | Xie2019 supports Spa2-dependent Aip5 recruitment/condensation and Bni1/Bud6-associated actin-regulatory context at budding sites in S288C. Those assays are not presented here as direct mating-tip membership or whole-complex formation evidence. |
| access-valtz1996-pdf | https://rupress.org/jcb/article-pdf/135/3/725/1266089/725.pdf; Response status and diagnostic content only | context_only | Publisher PDF route returned403; a genuine PMC PDF was retrieved separately. |
| access-PMC2121064-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2121064/fullTextXML; Response status and diagnostic content only | context_only | This XML supplies metadata/references and a PDF-only availability notice, not the primary body. |
| access-panther-PTHR21601-SF0 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR21601:SF0/; Response status and diagnostic content only | context_only | Candidate Spa2 subfamily request returned204 with no body, so no exact-family identity was established. |
| access-panther-PTHR47102-SF2 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR47102:SF2/; Response status and diagnostic content only | context_only | Candidate Bni1 subfamily request returned204 with no body, so no exact-family identity was established. |
| root59-sources-protein-P23201 | https://rest.uniprot.org/uniprotkb/P23201.json; Identity/status/genes/taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY/MISCELLANEOUS comments; InterPro/PANTHER references | supports | P23201 is the reviewed S288C SPA2 reference. Identity and location-source annotations were checked; bud-tip annotation is not independent proof of membership in the mating-tip complex. |
| root59-sources-gene-SPA2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identities and exact query parameters | supports | The exact reviewed SPA2 query uniquely identifies P23201 in taxon559292. |
| root59-sources-protein-P40091 | https://rest.uniprot.org/uniprotkb/P40091.json; Identity/status/genes/taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY/MISCELLANEOUS comments; InterPro/PANTHER references | supports | P40091 is the reviewed S288C PEA2 reference. Identity and location-source annotations were checked; bud-tip annotation is not independent proof of membership in the mating-tip complex. |
| root59-sources-gene-PEA2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APEA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identities and exact query parameters | supports | The exact reviewed PEA2 query uniquely identifies P40091 in taxon559292. |
| root59-sources-protein-P41832 | https://rest.uniprot.org/uniprotkb/P41832.json; Identity/status/genes/taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY/MISCELLANEOUS comments; InterPro/PANTHER references | supports | P41832 is the reviewed S288C BNI1 reference. Identity and location-source annotations were checked; bud-tip annotation is not independent proof of membership in the mating-tip complex. |
| root59-sources-gene-BNI1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABNI1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identities and exact query parameters | supports | The exact reviewed BNI1 query uniquely identifies P41832 in taxon559292. |
| root59-sources-protein-P41697 | https://rest.uniprot.org/uniprotkb/P41697.json; Identity/status/genes/taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY/MISCELLANEOUS comments; InterPro/PANTHER references | supports | P41697 is the reviewed S288C BUD6 reference. Identity and location-source annotations were checked; bud-tip annotation is not independent proof of membership in the mating-tip complex. |
| root59-sources-gene-BUD6 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABUD6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete result identities and exact query parameters | supports | The exact reviewed BUD6 query uniquely identifies P41697 in taxon559292. |
| root59-sources-ipr-IPR039892 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039892/; Complete native type/name/descriptions, quality flags, signatures and hierarchy | supports | Spa2/Sph1 family includes another paralog and does not identify the grouped Spa2/Pea2 cohort. |
| root59-sources-ipr-IPR062629 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062629/; Complete native type/name/descriptions, quality flags, signatures and hierarchy | supports | Pea2 N-terminal domain is not a whole protein family. |
| root59-sources-ipr-IPR062713 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062713/; Complete native type/name/descriptions, quality flags, signatures and hierarchy | supports | Pea2 middle domain is not a whole protein family. |
| root59-sources-ipr-IPR063286 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063286/; Complete native type/name/descriptions, quality flags, signatures and hierarchy | supports | Pea2 C-terminal domain is not a whole protein family. |
| root59-sources-ipr-IPR056279 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056279/; Complete native type/name/descriptions, quality flags, signatures and hierarchy | supports | Bud6 N-terminal domain is not a whole protein family. |
| root59-sources-ipr-IPR051825 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051825/; Complete native type/name/descriptions, quality flags, signatures and hierarchy | supports | SRCIN1 family is broader than the named yeast Bud6 class and has an unchecked generated description. |
| root59-sources-ipr-IPR051661 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051661/; Complete native type/name/descriptions, quality flags, signatures and hierarchy | supports | Actin-filament-dynamics-regulator family is broader than Bni1 and has an unchecked generated description. |
| root59-sources-bni1-family-reviewed-members | https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR051661/?page_size=100; Complete eleven reviewed member identities/names/genes/taxa | supports | All11 returned reviewed identities include Bni1, Bnr1, For3, Cdc12, Fus1 and RickA, directly demonstrating the proposed family is broader than the named Bni1 class. |
| schema-result | just validate data/structures/other/mating_projection_tip_polarisome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/mating_projection_tip_polarisome.yaml |
| strict-result | just validate-strict data/structures/other/mating_projection_tip_polarisome.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mating_projection_tip_polarisome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/mating_projection_tip_polarisome.yaml --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mating_projection_tip_polarisome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mating_projection_tip_polarisome-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/mating_projection_tip_polarisome.yaml  (GO:0031563)<br>  shmoo_tip_polarisome_topology	spa2_pea2_scaffold	COVERED	-&gt;spa2_pea2_scaffold (UniProtKB:P23201, UniProtKB:P40091)<br>  shmoo_tip_polarisome_topology	bni1_formin	COVERED	-&gt;bni1_formin (UniProtKB:P41832)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-verify-first | /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml --verify; Original sandbox DNS failure log | context_only | Exit1 after three DNS failures contacting UniProt. No scientific mismatch was reported; a network-enabled retry subsequently passed. |
| target-curies | just check-curies-strict; data/structures/other/mating_projection_tip_polarisome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 15 collected target identifiers returned OK. PMID:12361575: UNREACHABLE; Native Europe PMC uniquely identifies MED12361575: Spa2p functions as a scaffold-like protein to recruit the Mpk1p MAP kinase module to sites of polarized growth. (2002); DOI10.1016/s0960-9822(02)01186-7. Identifier transport verification is distinct from separately scoped primary-source reading.; PMID:31699995: UNREACHABLE; Native Europe PMC uniquely identifies MED31699995: Polarisome scaffolder Spa2-mediated macromolecular condensation of Aip5 for actin polymerization. (2019); DOI10.1038/s41467-019-13125-1. Identifier transport verification is distinct from separately scoped primary-source reading.; PMID:41065574: UNREACHABLE; Native Europe PMC uniquely identifies MED41065574: Aip5 forms a "composite" actin nucleator with Bud6 and caps pointed ends of actin filaments. (2025); DOI10.1083/jcb.202505039. Identifier transport verification is distinct from separately scoped primary-source reading. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five same-base batch26 corpus gates and exact target resolver rows are integrated with every manifested input hash verified.
- Primary reading is limited to the listed Valtz PDF and Bidlingmaier/Xie XML scopes. No figure pixels, raw datasets or unlisted source sections read.
- van Drogen2002 and Magliozzi2025 were checked at complete native abstract and UniProt annotation-provenance tier only; no primary body is claimed.
- Exact-family search is bounded; broad matches and empty204 responses do not establish all-authority absence.
- The first native protein verification failed at sandbox DNS; its original exit1/log is preserved and a network-enabled retry passed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes both issue-bearing and qualified clean observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T082333Z-mating-projection-tip-polarisome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of mating projection tip polarisome
started_at: '2026-10-22T07:57:51Z'
finished_at: '2026-10-22T08:23:33Z'
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
summary: One minor finding asks for condition-specific assembly evidence or qualification
  of three CONDITIONAL essentiality assignments. Exact localized identity, grouped
  scaffold boundary, reference proteins and nonmechanistic projection-cycle graph
  remain supported.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/other/mating_projection_tip_polarisome.yaml
    sha256: 5502f8d8c35e2a2c4f05054f1b8560ecf19c88374581927f3107e46512996afe
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
- target_id: GO:0031563
  path: data/structures/other/mating_projection_tip_polarisome.yaml
  label: mating projection tip polarisome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mating_projection_tip_polarisome.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; all evidence tiers and limitations declared
    individually.
  selection: One complete record in strict-path batch59 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031563
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031563
  command: just validate data/structures/other/mating_projection_tip_polarisome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031563
  command: just validate-strict data/structures/other/mating_projection_tip_polarisome.yaml
    --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mating_projection_tip_polarisome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0031563
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; scientific claims are assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0031563
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; scientific claims are assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-verify-first
  name: Initial protein verification transport attempt
  status: failed
  required: false
  target_ids:
  - GO:0031563
  command: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml
    --verify
  exit_code: 1
  summary: Sandbox DNS prevented source access; final required retry passed.
  evidence_ids:
  - native-verify-first
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0031563
  summary: No expression-module claim is assessed; native authorities and direct source
    scopes address the target.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031563
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root59-sources-go
  - root59-sources-GO0031563-ancestors
  - root59-sources-tax-4932
  - root59-sources-tax-559292
  - root59-sources-pmid-12361575
  - root59-sources-pmid-31699995
  - root59-sources-pmid-41065574
  - root59-sources-doi-10.1083_jcb.200307065
  - root59-sources-doi-10.1083_jcb.135.3.725
  - root59-sources-PMC2172334-xml
  - access-PMC2172334-legacy
  - root59-sources-valtz1996-pmc-pdf
  - root59-sources-PMC6838200-xml
  - access-valtz1996-pdf
  - access-PMC2121064-xml
  - access-panther-PTHR21601-SF0
  - access-panther-PTHR47102-SF2
  - root59-sources-protein-P23201
  - root59-sources-gene-SPA2
  - root59-sources-protein-P40091
  - root59-sources-gene-PEA2
  - root59-sources-protein-P41832
  - root59-sources-gene-BNI1
  - root59-sources-protein-P41697
  - root59-sources-gene-BUD6
  - root59-sources-ipr-IPR039892
  - root59-sources-ipr-IPR062629
  - root59-sources-ipr-IPR062713
  - root59-sources-ipr-IPR063286
  - root59-sources-ipr-IPR056279
  - root59-sources-ipr-IPR051825
  - root59-sources-ipr-IPR051661
  - root59-sources-bni1-family-reviewed-members
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031563
  summary: '12 of 15 collected target identifiers returned OK. PMID:12361575: UNREACHABLE;
    Native Europe PMC uniquely identifies MED12361575: Spa2p functions as a scaffold-like
    protein to recruit the Mpk1p MAP kinase module to sites of polarized growth. (2002);
    DOI10.1016/s0960-9822(02)01186-7. Identifier transport verification is distinct
    from separately scoped primary-source reading.; PMID:31699995: UNREACHABLE; Native
    Europe PMC uniquely identifies MED31699995: Polarisome scaffolder Spa2-mediated
    macromolecular condensation of Aip5 for actin polymerization. (2019); DOI10.1038/s41467-019-13125-1.
    Identifier transport verification is distinct from separately scoped primary-source
    reading.; PMID:41065574: UNREACHABLE; Native Europe PMC uniquely identifies MED41065574:
    Aip5 forms a "composite" actin nucleator with Bud6 and caps pointed ends of actin
    filaments. (2025); DOI10.1083/jcb.202505039. Identifier transport verification
    is distinct from separately scoped primary-source reading. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - root59-sources-pmid-12361575
  - root59-sources-pmid-31699995
  - root59-sources-pmid-41065574
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031563
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031563
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031563
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031563
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031563
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
    and current batch59 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/mating_projection_tip_polarisome.yaml
  locator: Entire maintained YAML, history and discussions
  accessed_at: '2026-10-22T08:03:43Z'
  support: context_only
  summary: The entire target was read after inspection. This maintained YAML owns
    any scientific correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and graph scope
  accessed_at: '2026-10-22T08:03:43Z'
  support: context_only
  summary: CONDITIONAL denotes required under some conditions or in some lineages.
    VARIABLE denotes patchy lineage/strain presence rather than cell state. UNKNOWN
    formation necessity and unpopulated optional fields are not automatically defects.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, component classes and claim-level evidence
  accessed_at: '2026-10-22T08:03:43Z'
  support: context_only
  summary: Protein reference identity, biological membership, localization and formation
    necessity require distinct evidence. A grouped functional cohort is not automatically
    a homologous family.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Descriptive versus mechanistic graph scope
  accessed_at: '2026-10-22T08:03:43Z'
  support: context_only
  summary: An explicitly nonmechanistic graph can faithfully record regional topology,
    membership and broad function without a complete molecular pathway.
- evidence_id: root59-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000133,GO:0005937,GO:0006260,GO:0031382,GO:0031563,GO:0032991,GO:0042555,GO:0043332,GO:0070867,GO:0097362,GO:1990819
  locator: All eleven focal term identities/status/definitions/synonyms; relevant
    typed child links only for the large generic protein-complex child list
  accessed_at: '2026-10-22T07:46:02.059692Z'
  support: supports
  summary: Native exact GO identities and definitions distinguish the mating-projection
    tip region, its localized polarisome, the broader polarisome and the generic hexameric
    MCM class. Typed links were checked separately from mixed-relation ancestry.
  snapshot_sha256: 00a914e51738d174ad7923e7ef7d803404f6c263db96afb0b4d796c52c3d9b38
- evidence_id: root59-sources-GO0031563-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031563/ancestors?relations=is_a,part_of
  locator: Complete target ancestry; typed direct relationships checked jointly against
    the GO term responses
  accessed_at: '2026-10-22T07:47:24.025573Z'
  support: supports
  summary: The exact target ancestry is consistent with the stated parent or parthood
    context; mixed is_a/part_of ancestry is not treated as proof of one relation type.
  snapshot_sha256: 885f7080357222b5b29cd99478a86048cd0417a03f49e43625687c57654e7815
- evidence_id: root59-sources-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native name/rank/lineage response
  accessed_at: '2026-10-22T07:46:02.694222Z'
  support: supports
  summary: Native taxonomy confirms Saccharomyces cerevisiae, taxon4932, rank species.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: root59-sources-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native name/rank/lineage response
  accessed_at: '2026-10-22T07:46:03.257048Z'
  support: supports
  summary: Native taxonomy confirms Saccharomyces cerevisiae S288C, taxon559292, rank
    strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root59-sources-pmid-12361575
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12361575+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED bibliography/DOI/PMCID and complete abstractText
  accessed_at: '2026-10-22T07:46:05.546529Z'
  support: supports
  summary: 'MED12361575: Spa2p functions as a scaffold-like protein to recruit the
    Mpk1p MAP kinase module to sites of polarized growth. van Drogen F, Peter M. (2002);
    DOI10.1016/s0960-9822(02)01186-7. Native full abstract read; primary-body evidence
    is claimed only where separately listed.'
  snapshot_sha256: 0282aceb622315b57ea330e4b0253425fa3ec6800cd8a68ef20d02bbe1b6f6f3
- evidence_id: root59-sources-pmid-31699995
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A31699995+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED bibliography/DOI/PMCID and complete abstractText
  accessed_at: '2026-10-22T07:46:05.604529Z'
  support: supports
  summary: 'MED31699995: Polarisome scaffolder Spa2-mediated macromolecular condensation
    of Aip5 for actin polymerization. Xie Y, Sun J, Han X, Turšić-Wunder A, Toh JDW,
    Hong W, Gao YG, Miao Y. (2019); DOI10.1038/s41467-019-13125-1. Native full abstract
    read; primary-body evidence is claimed only where separately listed.'
  snapshot_sha256: 0d8535587617f7053fd4101b48cd07d595bc18e4fb11d397cd60f4eec45c5414
- evidence_id: root59-sources-pmid-41065574
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A41065574+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED bibliography/DOI/PMCID and complete abstractText
  accessed_at: '2026-10-22T07:46:06.172914Z'
  support: supports
  summary: 'MED41065574: Aip5 forms a "composite" actin nucleator with Bud6 and caps
    pointed ends of actin filaments. Magliozzi JO, Runyan LA, Welsh A, Padrick SB,
    Goode BL. (2025); DOI10.1083/jcb.202505039. Native full abstract read; primary-body
    evidence is claimed only where separately listed.'
  snapshot_sha256: 53a90f67e58d8f655792fa7cd0dc662685d390e9caf429dcc59cf31e8999cf5c
- evidence_id: root59-sources-doi-10.1083_jcb.200307065
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.200307065%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI-to-MED identity and complete abstractText
  accessed_at: '2026-10-22T07:46:07.071798Z'
  support: supports
  summary: 'Unique DOI result identifies MED14734532: Regulation of polarized growth
    initiation and termination cycles by the polarisome and Cdc42 regulators. (2004).
    Complete abstract and bibliography read.'
  snapshot_sha256: 7951d5081d4ca42f22d7807c9f4f1e2480e1a39a4e703c6c16cc7a91b95f8b0a
- evidence_id: root59-sources-doi-10.1083_jcb.135.3.725
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1083%2Fjcb.135.3.725%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI-to-MED identity and complete abstractText
  accessed_at: '2026-10-22T07:46:07.671151Z'
  support: supports
  summary: 'Unique DOI result identifies MED8909546: Pea2 protein of yeast is localized
    to sites of polarized growth and is required for efficient mating and bipolar
    budding. (1996). Complete abstract and bibliography read.'
  snapshot_sha256: 9498ccf88565be25874b5c70e0341861f349828996217b26c5811de64864d165
- evidence_id: root59-sources-PMC2172334-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2172334/fullTextXML
  locator: 'Genuine JATS: Introduction section index0; Results indices4/5; Discussion
    index10 opening topic; all Methods indices17–20 including TableI; embedded captions
    within these sections. No other Results/Discussion or figure pixels.'
  accessed_at: '2026-10-22T07:47:17.193978Z'
  support: supports
  summary: Bidlingmaier2004 assayed pheromone-induced projection initiation/termination
    in S288C-congenic cells. Spa2, Pea2 and Bni1 deletions delay repeated initiation
    and disrupt termination; bud6 deletion did not change projection frequency or
    morphology in this assay. These are phenotype/functional observations, not direct
    measurements of whole-polarisome formation.
  snapshot_sha256: 6df7c78398153531ba15d7369408ad0be25d9dea1bd8e44e6a66a4d99da8063c
- evidence_id: access-PMC2172334-legacy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC2172334/
  locator: Response status and diagnostic content only
  accessed_at: '2026-10-22T07:46:07.779558Z'
  support: context_only
  summary: HTTP200 returned a browser challenge rather than readable article text;
    genuine XML was inspected separately.
  snapshot_sha256: cfca7000e6aa5b49bb16f62abcb179a949f80dc1cd33de8879d7138f52615a6d
- evidence_id: root59-sources-valtz1996-pmc-pdf
  kind: primary_source
  reference: https://europepmc.org/articles/PMC2121064?pdf=render
  locator: 'Genuine scanned PDF extraction: printed pages731,732,733,735,736 in full;
    TableI on727; first25 lines of Discussion page739. No remaining discussion, figure
    pixels or supplemental data.'
  accessed_at: '2026-10-22T07:48:10.207113Z'
  support: supports
  summary: Valtz1996 localized Pea2 and Spa2 to polarized sites in budding and mating
    cells and found reciprocal requirements for normal localization/stability. Its
    physical-complex interpretation remains a suggestion rather than direct binding
    or universal assembly proof.
  snapshot_sha256: 26caa2ada69887356d6c2741e73d813b5e68465384c4dce4e4e88d1621f00fc5
- evidence_id: root59-sources-PMC6838200-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6838200/fullTextXML
  locator: Genuine JATS Sec1,Sec3 including Figure1 caption,Sec10 andSec15 in full.
    Other Results/Methods, figure pixels and raw data not read.
  accessed_at: '2026-10-22T07:47:18.555010Z'
  support: supports
  summary: Xie2019 supports Spa2-dependent Aip5 recruitment/condensation and Bni1/Bud6-associated
    actin-regulatory context at budding sites in S288C. Those assays are not presented
    here as direct mating-tip membership or whole-complex formation evidence.
  snapshot_sha256: d63b5505e36f889f986bbbb6f7df87e8a0843c1caf18949926a1478d9ce95026
- evidence_id: access-valtz1996-pdf
  kind: authority
  reference: https://rupress.org/jcb/article-pdf/135/3/725/1266089/725.pdf
  locator: Response status and diagnostic content only
  accessed_at: '2026-10-22T07:48:09.738287Z'
  support: context_only
  summary: Publisher PDF route returned403; a genuine PMC PDF was retrieved separately.
  snapshot_sha256: fdcbf8b0690edddd85435750d4f7cff0a23b52246c8208d4eb4d24dec6738162
- evidence_id: access-PMC2121064-xml
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2121064/fullTextXML
  locator: Response status and diagnostic content only
  accessed_at: '2026-10-22T07:47:18.397853Z'
  support: context_only
  summary: This XML supplies metadata/references and a PDF-only availability notice,
    not the primary body.
  snapshot_sha256: 1f19d7384b7cf37fc520502521d8d90644f34c5241f6ff4d7f45e8fefb4cff6a
- evidence_id: access-panther-PTHR21601-SF0
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR21601:SF0/
  locator: Response status and diagnostic content only
  accessed_at: '2026-10-22T07:47:22.221957Z'
  support: context_only
  summary: Candidate Spa2 subfamily request returned204 with no body, so no exact-family
    identity was established.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: access-panther-PTHR47102-SF2
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR47102:SF2/
  locator: Response status and diagnostic content only
  accessed_at: '2026-10-22T07:47:22.819024Z'
  support: context_only
  summary: Candidate Bni1 subfamily request returned204 with no body, so no exact-family
    identity was established.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: root59-sources-protein-P23201
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P23201.json
  locator: Identity/status/genes/taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY/MISCELLANEOUS
    comments; InterPro/PANTHER references
  accessed_at: '2026-10-22T07:46:03.300300Z'
  support: supports
  summary: P23201 is the reviewed S288C SPA2 reference. Identity and location-source
    annotations were checked; bud-tip annotation is not independent proof of membership
    in the mating-tip complex.
  snapshot_sha256: 04c2e80fad38fe6e6ff321c0661be8951f68dfd056da5f2662b72c808c5a4a91
- evidence_id: root59-sources-gene-SPA2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASPA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identities and exact query parameters
  accessed_at: '2026-10-22T07:46:08.260286Z'
  support: supports
  summary: The exact reviewed SPA2 query uniquely identifies P23201 in taxon559292.
  snapshot_sha256: 34ccb79e3ea14b36c7c9d42d3a3d8faee4632994622d7e6e5bcddd1bc35492ff
- evidence_id: root59-sources-protein-P40091
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40091.json
  locator: Identity/status/genes/taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY/MISCELLANEOUS
    comments; InterPro/PANTHER references
  accessed_at: '2026-10-22T07:46:04.015280Z'
  support: supports
  summary: P40091 is the reviewed S288C PEA2 reference. Identity and location-source
    annotations were checked; bud-tip annotation is not independent proof of membership
    in the mating-tip complex.
  snapshot_sha256: 1e0c1e20310c86d389b0610f0d5f3adaba9951470df79ccc72559b9a7a1b5b24
- evidence_id: root59-sources-gene-PEA2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APEA2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identities and exact query parameters
  accessed_at: '2026-10-22T07:46:08.399351Z'
  support: supports
  summary: The exact reviewed PEA2 query uniquely identifies P40091 in taxon559292.
  snapshot_sha256: e197de95c326fa8328781dd6e431371e916d071c042e8500dd80d84b97617f47
- evidence_id: root59-sources-protein-P41832
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41832.json
  locator: Identity/status/genes/taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY/MISCELLANEOUS
    comments; InterPro/PANTHER references
  accessed_at: '2026-10-22T07:46:04.773757Z'
  support: supports
  summary: P41832 is the reviewed S288C BNI1 reference. Identity and location-source
    annotations were checked; bud-tip annotation is not independent proof of membership
    in the mating-tip complex.
  snapshot_sha256: 1d95c3eb7f1c02228c6b84873742dc2e1dc6abb6a7b2c609d6353191efde972a
- evidence_id: root59-sources-gene-BNI1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABNI1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identities and exact query parameters
  accessed_at: '2026-10-22T07:46:09.139837Z'
  support: supports
  summary: The exact reviewed BNI1 query uniquely identifies P41832 in taxon559292.
  snapshot_sha256: b78c26468ef0aeffff98bfacc745f6a4edf5473ca1263ec21f74ae673ca25187
- evidence_id: root59-sources-protein-P41697
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P41697.json
  locator: Identity/status/genes/taxon; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY/MISCELLANEOUS
    comments; InterPro/PANTHER references
  accessed_at: '2026-10-22T07:46:04.124074Z'
  support: supports
  summary: P41697 is the reviewed S288C BUD6 reference. Identity and location-source
    annotations were checked; bud-tip annotation is not independent proof of membership
    in the mating-tip complex.
  snapshot_sha256: 0abda308efd037012fe40e3ee0abf4b455b7ceb6dd60b67a2afaf835a2db2c01
- evidence_id: root59-sources-gene-BUD6
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ABUD6%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete result identities and exact query parameters
  accessed_at: '2026-10-22T07:46:09.371876Z'
  support: supports
  summary: The exact reviewed BUD6 query uniquely identifies P41697 in taxon559292.
  snapshot_sha256: 934fc25e5008f7ffbd019810fe413600a2f56905d184e8a4e757e4225317c4d5
- evidence_id: root59-sources-ipr-IPR039892
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039892/
  locator: Complete native type/name/descriptions, quality flags, signatures and hierarchy
  accessed_at: '2026-10-22T07:47:19.926711Z'
  support: supports
  summary: Spa2/Sph1 family includes another paralog and does not identify the grouped
    Spa2/Pea2 cohort.
  snapshot_sha256: 6476f3f836012c74087ca05a1402415a40723e51e74135035b060d96fafabc01
- evidence_id: root59-sources-ipr-IPR062629
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062629/
  locator: Complete native type/name/descriptions, quality flags, signatures and hierarchy
  accessed_at: '2026-10-22T07:47:20.967263Z'
  support: supports
  summary: Pea2 N-terminal domain is not a whole protein family.
  snapshot_sha256: 96e2ea7934c9bab50a38b8f5c08c1484389fa493cff95757a3a54c24d63e1d31
- evidence_id: root59-sources-ipr-IPR062713
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR062713/
  locator: Complete native type/name/descriptions, quality flags, signatures and hierarchy
  accessed_at: '2026-10-22T07:47:20.519571Z'
  support: supports
  summary: Pea2 middle domain is not a whole protein family.
  snapshot_sha256: aa46e64b9ff5403488de0d38afb7f6929b37867aa0e7d6744e83079d6a52814c
- evidence_id: root59-sources-ipr-IPR063286
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063286/
  locator: Complete native type/name/descriptions, quality flags, signatures and hierarchy
  accessed_at: '2026-10-22T07:47:20.378427Z'
  support: supports
  summary: Pea2 C-terminal domain is not a whole protein family.
  snapshot_sha256: aed1f0179db8291c8ab99d8f46ad042ed2da900db416bfe8d6e79fbe3f416ebb
- evidence_id: root59-sources-ipr-IPR056279
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR056279/
  locator: Complete native type/name/descriptions, quality flags, signatures and hierarchy
  accessed_at: '2026-10-22T07:47:21.114107Z'
  support: supports
  summary: Bud6 N-terminal domain is not a whole protein family.
  snapshot_sha256: cbd0232d0cf6250d7501d90b3e9ba586552b5dae84dc660b420addb4a7761ce9
- evidence_id: root59-sources-ipr-IPR051825
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051825/
  locator: Complete native type/name/descriptions, quality flags, signatures and hierarchy
  accessed_at: '2026-10-22T07:47:21.549216Z'
  support: supports
  summary: SRCIN1 family is broader than the named yeast Bud6 class and has an unchecked
    generated description.
  snapshot_sha256: 34dc77dcf99b4747caa75d530205831b3d9edd66f5e4df7833319637fb3bb245
- evidence_id: root59-sources-ipr-IPR051661
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051661/
  locator: Complete native type/name/descriptions, quality flags, signatures and hierarchy
  accessed_at: '2026-10-22T07:47:21.707951Z'
  support: supports
  summary: Actin-filament-dynamics-regulator family is broader than Bni1 and has an
    unchecked generated description.
  snapshot_sha256: babdb17855c5f01a4a0410ef193cff0c2e95c9eaafe0dfda2a58b7bad3b33e04
- evidence_id: root59-sources-bni1-family-reviewed-members
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/protein/reviewed/entry/interpro/IPR051661/?page_size=100
  locator: Complete eleven reviewed member identities/names/genes/taxa
  accessed_at: '2026-10-22T07:48:14.814611Z'
  support: supports
  summary: All11 returned reviewed identities include Bni1, Bnr1, For3, Cdc12, Fus1
    and RickA, directly demonstrating the proposed family is broader than the named
    Bni1 class.
  snapshot_sha256: 77a8be8aab7488e022428157399edef9eb9b778b4955432b71a3107075a295f9
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/mating_projection_tip_polarisome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:57:52Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/mating_projection_tip_polarisome.yaml'
  snapshot_sha256: 1c4101902eb78437ca587bb543166de8e649b817a1c0a963dcf78813cf6deecd
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/mating_projection_tip_polarisome.yaml
    --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mating_projection_tip_polarisome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:57:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/mating_projection_tip_polarisome.yaml\
    \ --out /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mating_projection_tip_polarisome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch59-20261022-t3ere5ku/mating_projection_tip_polarisome-strict.tsv"
  snapshot_sha256: 322664ee74d58ecfb43e2f8638001e4cf726c40881d84afead7e9d1736667da6
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml
    --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:59:08.161875Z'
  support: supports
  summary: "data/structures/other/mating_projection_tip_polarisome.yaml  (GO:0031563)\n\
    \  shmoo_tip_polarisome_topology\tspa2_pea2_scaffold\tCOVERED\t->spa2_pea2_scaffold\
    \ (UniProtKB:P23201, UniProtKB:P40091)\n  shmoo_tip_polarisome_topology\tbni1_formin\t\
    COVERED\t->bni1_formin (UniProtKB:P41832)\n\ncausal_graphs GENE_OR_PROTEIN node\
    \ summary:\n     2  COVERED                   component_ref target holds protein_examples\
    \ covering all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref\
    \ target holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref\
    \ on the node\n     2  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 91e6e3ad699e6b3ac1412c3adb208b9c650fe646dc6d3c349865ba6a2c0d02e8
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml
    --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:59:57.858416Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-verify-first
  kind: validation
  reference: /private/tmp/cellstructure-batch59-20261022-t3ere5ku/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mating_projection_tip_polarisome.yaml
    --verify
  locator: Original sandbox DNS failure log
  accessed_at: '2026-10-22T07:59:20.589410Z'
  support: context_only
  summary: Exit1 after three DNS failures contacting UniProt. No scientific mismatch
    was reported; a network-enabled retry subsequently passed.
  snapshot_sha256: b4195e63d6cf4ff26c17bdfe513a3919a8e8d7383dfde5acd4c0b8c0ed752012
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/mating_projection_tip_polarisome.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '12 of 15 collected target identifiers returned OK. PMID:12361575: UNREACHABLE;
    Native Europe PMC uniquely identifies MED12361575: Spa2p functions as a scaffold-like
    protein to recruit the Mpk1p MAP kinase module to sites of polarized growth. (2002);
    DOI10.1016/s0960-9822(02)01186-7. Identifier transport verification is distinct
    from separately scoped primary-source reading.; PMID:31699995: UNREACHABLE; Native
    Europe PMC uniquely identifies MED31699995: Polarisome scaffolder Spa2-mediated
    macromolecular condensation of Aip5 for actin polymerization. (2019); DOI10.1038/s41467-019-13125-1.
    Identifier transport verification is distinct from separately scoped primary-source
    reading.; PMID:41065574: UNREACHABLE; Native Europe PMC uniquely identifies MED41065574:
    Aip5 forms a "composite" actin nucleator with Bud6 and caps pointed ends of actin
    filaments. (2025); DOI10.1083/jcb.202505039. Identifier transport verification
    is distinct from separately scoped primary-source reading. Native source checks
    are separately scoped; skipped or unreachable identifiers are not silently counted
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
  topic: Localized subtype retains exact identity
  outcome: supported
  target_ids:
  - GO:0031563
  summary: The mating-tip polarisome is the GO0031563 subtype of the broader polarisome
    and is localized at the projection tip. A grouped Spa2/Pea2 scaffold cohort is
    explicitly functional, not described as one homologous family.
  evidence_ids:
  - record
  - curation
  - root59-sources-go
  - root59-sources-GO0031563-ancestors
  - root59-sources-valtz1996-pmc-pdf
  - root59-sources-PMC2172334-xml
- assessment_id: grounding
  area: grounding
  topic: No verified exact replacement among inspected family candidates
  outcome: supported
  target_ids:
  - GO:0031563
  summary: The available native families are broader than the named components, domain-only,
    or empty candidate-subfamily responses. The bounded search supports retaining
    the explicit label-only tasks; it does not establish absence from every authority.
  evidence_ids:
  - record
  - curation
  - root59-sources-ipr-IPR039892
  - root59-sources-ipr-IPR062629
  - root59-sources-ipr-IPR062713
  - root59-sources-ipr-IPR063286
  - root59-sources-ipr-IPR056279
  - root59-sources-ipr-IPR051825
  - root59-sources-ipr-IPR051661
  - root59-sources-bni1-family-reviewed-members
  - root59-sources-protein-P23201
  - root59-sources-protein-P40091
  - root59-sources-protein-P41832
  - root59-sources-protein-P41697
  - root59-sources-gene-SPA2
  - root59-sources-gene-PEA2
  - root59-sources-gene-BNI1
  - root59-sources-gene-BUD6
- assessment_id: membership
  area: evidence
  topic: Composition and phenotype boundaries are explicit
  outcome: supported
  target_ids:
  - GO:0031563
  summary: The source and GO boundary identify Spa2/Pea2, Bni1 and Bud6 as polarisome
    constituents. The record explicitly omits a Bud6 periodic-projection edge because
    its deletion had no observed effect in that assay, and keeps Cdc42 regulators
    and Fus proteins outside the complex boundary.
  evidence_ids:
  - record
  - root59-sources-go
  - root59-sources-valtz1996-pmc-pdf
  - root59-sources-PMC2172334-xml
  - root59-sources-PMC6838200-xml
  - root59-sources-protein-P23201
  - root59-sources-protein-P40091
  - root59-sources-protein-P41832
  - root59-sources-protein-P41697
- assessment_id: formation
  area: evidence
  topic: Conditional formation claims need their own support
  outcome: concern
  target_ids:
  - GO:0031563
  summary: All three component rows assert CONDITIONAL essentiality, but neither a
    condition/lineage nor a direct whole-polarisome formation dependency is stated.
    The cited localization/stability and projection-cycle phenotypes do not by themselves
    establish this assembly requirement, especially for Bud6 with no projection phenotype
    in the stated assay.
  evidence_ids:
  - record
  - schema
  - root59-sources-valtz1996-pmc-pdf
  - root59-sources-PMC2172334-xml
- assessment_id: scope
  area: scope
  topic: Reference proteins and assay strains remain separate
  outcome: unknown
  target_ids:
  - GO:0031563
  summary: The reference proteins are reviewed S288C entries. Bidlingmaier uses S288C-congenic
    strains, while Valtz TableI lists its own isogenic strain series; that series
    was not independently assigned S288C. VARIABLE prevalence remains unknown rather
    than redefined as pheromone induction.
  evidence_ids:
  - record
  - schema
  - root59-sources-valtz1996-pmc-pdf
  - root59-sources-PMC2172334-xml
  - root59-sources-tax-4932
  - root59-sources-tax-559292
  - root59-sources-protein-P23201
  - root59-sources-protein-P40091
  - root59-sources-protein-P41832
  - root59-sources-protein-P41697
- assessment_id: graph
  area: graph
  topic: Bounded topology and projection-cycle support
  outcome: supported
  target_ids:
  - GO:0031563
  summary: Spa2/Pea2 localization and Bni1 support for periodic projection formation
    match the sources. The graph is explicitly nonmechanistic, does not assert a complete
    actin pathway, and appropriately excludes the unsupported Bud6 phenotype edge.
  evidence_ids:
  - record
  - graphs
  - root59-sources-go
  - root59-sources-valtz1996-pmc-pdf
  - root59-sources-PMC2172334-xml
- assessment_id: coverage
  area: completeness
  topic: Complete target with bounded evidence tiers
  outcome: supported
  target_ids:
  - GO:0031563
  summary: Every maintained target field, evidence item, graph node/edge, history
    entry and discussion was inspected. Optional empty fields and scientific unknowns
    are not manufactured into defects.
  evidence_ids:
  - record
  - schema
  - curation
  - root59-sources-go
findings:
- finding_id: F1
  issue_key: mating-tip-polarisome-conditional-formation-support
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Support or qualify the conditional essentiality assignments
  description: Spa2/Pea2, Bni1 and Bud6 are all coded CONDITIONAL without a stated
    formation condition or lineage. The nearest evidence establishes localization/stability
    or periodic projection phenotypes; it does not establish whole-complex formation
    requirements under named conditions. The Bud6 note expressly reports no projection-frequency
    or morphology effect in the cited assay. This is an unsupported nonempty dependency
    assertion, not a demand to fill an optional field.
  target_ids:
  - GO:0031563
  field_paths:
  - components[0].essentiality
  - components[1].essentiality
  - components[2].essentiality
  evidence_ids:
  - record
  - schema
  - root59-sources-valtz1996-pmc-pdf
  - root59-sources-PMC2172334-xml
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mating_projection_tip_polarisome.yaml
    role: maintained scientific record
  rule_id: Formation essentiality must retain assay and condition scope
  native_severity: minor
  normalization_reason: Bounded evidence qualification; exact structure identity and
    supported membership/function remain intact.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0031563
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mating_projection_tip_polarisome.yaml
    role: maintained scientific record
  description: For each named component, document the precise condition/lineage and
    a source-backed assembly requirement, or qualify the formation status as unknown
    while retaining supported membership and functional phenotypes.
  acceptance_checks:
  - Do not infer complex formation from growth, projection timing, localization or
    activity alone.
  - Do not infer universal dispensability from the negative Bud6 projection assay.
  - Preserve the existing nonmechanistic graph and component-boundary explanations.
  - Pass applicable schema, strict, protein and graph checks after separately authorized
    curation.
limitations:
- All five same-base batch26 corpus gates and exact target resolver rows are integrated
  with every manifested input hash verified.
- Primary reading is limited to the listed Valtz PDF and Bidlingmaier/Xie XML scopes.
  No figure pixels, raw datasets or unlisted source sections read.
- van Drogen2002 and Magliozzi2025 were checked at complete native abstract and UniProt
  annotation-provenance tier only; no primary body is claimed.
- Exact-family search is bounded; broad matches and empty204 responses do not establish
  all-authority absence.
- The first native protein verification failed at sandbox DNS; its original exit1/log
  is preserved and a network-enabled retry passed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes both issue-bearing and qualified clean observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
