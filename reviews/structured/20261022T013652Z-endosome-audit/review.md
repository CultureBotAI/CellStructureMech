# Endosome identity, source and compartment review

- Review: 20261022T013652Z-endosome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:09:16Z
- Finished UTC: 2026-10-22T01:36:52Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed in the endosome record within the explicitly documented source scopes.

## Scope And Provenance

Entire single maintained target; exact identity, hierarchy, component/protein scope, organism contexts, cited evidence and every graph edge.

Selection: Target 10 of batch twenty-seven; strict uncovered path order on fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005768 | data/structures/membrane_organelle/endosome.yaml | maintained | endosome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native verify | passed | True | GO:0005768 | The focused native identity/coverage check passed; it does not by itself establish biological membership. |
| Focused native causal-graphs | passed | True | GO:0005768 | The focused native identity/coverage check passed; it does not by itself establish biological membership. |
| Focused native schema | passed | True | GO:0005768 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005768 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005768 | Native UniProt is used as the structured protein adapter. No iModulon dataset or expression-module inference is needed to assess these cited physical/functional experiments; UPR evidence is kept at the primary paper scope. |
| Claim-level scientific review | passed | True | GO:0005768 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005768 | 13 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections.; PMID:12194857: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID12194857, DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections.; cellstructuremech:multivesicular_body_intraluminal_vesicle: SKIPPED; Repository-minted identifier resolves to the frozen maintained multivesicular body intraluminal vesicle record at data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml. Root repeated an ignored-inclusive anchored corpus search and verified its exact identifier/input hash. This verifies the reference, not all neighboring biology. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005768 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005768 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005768 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005768 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005768 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Whole endosome versus membrane, lumen and ILV

identity: supported. Targets: GO:0005768.

GO0005768 exactly denotes the whole endosome; membrane/lumen parts and the collective membrane component match native terms. GO0005771 defines an MVB as an endosome containing internal vesicles; the local ILV ID denotes one distinct internal vesicle. No requirement to add optional parentage or duplicate all MVB subtypes is invented.

### Yeast endosomal sorting model

scope: supported. Targets: GO:0005768.

Species4932 is exact and the primary papers support yeast MVB sorting. Katzmann2003 Methods explicitly lists SEY6210 derivatives; Teo uses yeast-derived constructs expressed in E.coli. The reference-strain VPS27 xref denotes the gene/protein identity and does not assert those experiment strains. COMMON is qualitative, not a quantified prevalence survey.

### Boundary constituent versus transient sorting actors

grounding: supported. Targets: GO:0005768.

The membrane row describes the collective bounding bilayer. Vps27 and ESCRT complexes are graph actors, consistent with the discussion keeping transient sorting machinery outside permanent constituent tables. P40343 matches VPS27, and exact GO complex IDs preserve ESCRT-I/II/III boundaries.

### Individual components and formation

evidence: unknown. Targets: GO:0005768.

The complete bilayer is constitutive of the membrane-bounded endosome. Neither this collective ESSENTIAL row nor ESCRT cargo-sorting requirements establish individual lipid necessity or an exhaustive endosome-formation mechanism.

### Endosomal transport and MVB cargo sorting

evidence: supported. Targets: GO:0005768.

Native GO and Katzmann primary evidence support transport of internalized/biosynthetic material and ubiquitin-dependent sorting. Henne is clearly a review supplying context. These functions do not imply all endosomal cargo is ESCRT-dependent or that MVB formation defines every endosome.

### All seven endosomal sorting edges

graph: supported. Targets: GO:0005768.

Enclosure and ILV formation/containment follow the exact GO definitions. Katzmann2003 directly supports Vps27 recruitment/association with ESCRT-I; Katzmann2001 abstract supports ubiquitin cargo recognition. Teo Results support ESCRT-II interaction with Vps20 and enhanced membrane association. Babst abstract supports ESCRT-III membrane oligomerization/cargo sorting, while the exact modern GO ESCRT-III definition corroborates broad remodeling. NONMECHANISTIC scope appropriately avoids claiming complete scission chemistry, deubiquitination or Vps4 recycling.

### Detailed membrane-scission mechanism

evidence: unknown. Targets: GO:0005768.

The broad ESCRT-III membrane role is supported, but Babst full text was not recovered in this review. Exact membrane scission steps and the completeness of the original paper experiments are not independently certified.

### Full target and honest optional gaps

completeness: supported. Targets: GO:0005768.

All target fields and edges were read. The target asserts no images, physical measurements, trait links or verbatim snippets. Open molecular inventories remain explicit optional gaps; source-access limits do not become invented defects. PROPOSED status and append-only historical decisions are preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/endosome.yaml; Entire maintained target including history, component and protein examples, all evidence and graph edges, discussions | context_only | All target bytes were read. Scientific content, status and histories remain unchanged. |
| policy | docs/CURATION.md; Structure identity, is-a versus parthood, constituent versus associated machinery, narrow evidence | context_only | The whole organelle, limiting membrane and enclosed region remain distinct. Enzyme activity and gene viability do not establish organelle-formation necessity. |
| protein-contract | src/cellstructuremech/schema/cellstructuremech.yaml; Component.protein_examples and ProteinExample lines448–468; component essentiality contract | context_only | Protein examples require paired biological context; native accession verification alone is not proof of structure membership. Formation necessity differs from protein function and cell viability. |
| neighbor-endoplasmic_reticulum | data/structures/membrane_organelle/endoplasmic_reticulum.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| neighbor-endoplasmic_reticulum_lumen | data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| neighbor-endoplasmic_reticulum_membrane | data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml; Entire neighboring record read, used solely for compartment boundary context | context_only | These neighboring records receive separate reviews. Their unrelated source claims are not incorporated as proof for this target. |
| root27-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005783,GO:0005788,GO:0005789,GO:0005784,GO:0043231,GO:0012505,GO:0043233,GO:0016020,GO:0030968,GO:0036503,GO:0090114,GO:0030127,GO:0005768,GO:0010008,GO:0031904,GO:0005771,GO:0016197,GO:0000813,GO:0000814,GO:0000815; All20 identifiers, active flags, names, definitions, synonyms, comments and returned immediate child relations | supports | Twenty active GO terms were read in full. Exact ER/endosome, membrane/lumen, Sec61, ESCRT, transport and COPII definitions and synonyms support the scoped identities. GO0005784 explicitly names the yeast Sec61p/Sbh1p/Sss1p core. GO0036503 is now named ERAD quality control pathway, with ERAD pathway retained as a broad synonym; the record description specifically identifies misfolded-protein quality control. Returned child links support direct relations only; broader membrane/lumen classes may require transitive or definition-based inference. |
| root27-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies Saccharomyces cerevisiae at species4932; its rank and fungal lineage agree with the target. This does not certify any particular experimental strain or numerical prevalence. |
| root27-sources-katzmann2001-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A11511343%20AND%20SRC%3AMED; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I. by Katzmann DJ, Babst M, Emr SD.; PMID11511343, DOI10.1016/s0092-8674(01)00434-2. The complete primary abstract identifies ESCRT-I, ubiquitin recognition and MVB sorting in yeast, including biosynthetic and cell-surface cargo. It does not make transient ESCRT machinery permanent endosome constituents. |
| root27-sources-katzmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.200302136; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies Vps27 recruits ESCRT machinery to endosomes during MVB sorting. by Katzmann DJ, Stefan CJ, Babst M, Emr SD.; PMID12900393, DOI10.1083/jcb.200302136. The complete primary abstract identifies Vps27/PI(3)P-dependent ESCRT-I recruitment at yeast endosomes. Detailed recruitment and binding results are separately read in the primary body. |
| root27-sources-teo2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2004.09.003; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies ESCRT-II, an endosome-associated complex required for protein sorting: crystal structure and interactions with ESCRT-III and membranes. by Teo H, Perisic O, González B, Williams RL.; PMID15469844, DOI10.1016/j.devcel.2004.09.003. The complete primary abstract reports yeast ESCRT-II architecture, direct Vps20 binding through Vps25 and enhanced membrane binding. It supports the ESCRT-II-to-III handoff, not every molecular transition of a complete ESCRT pathway. |
| root27-sources-babst2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A12194857%20AND%20SRC%3AMED; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting. by Babst M, Katzmann DJ, Estepa-Sabal EJ, Meerloo T, Emr SD.; PMID12194857, DOI10.1016/s1534-5807(02)00220-4. The complete primary abstract describes membrane recruitment and oligomerization of Vps2/Vps20/Vps24/Snf7 into ESCRT-III and cargo sorting/concentration. The target describes broad membrane remodeling; exact scission mechanics are not established by this abstract alone. |
| root27-sources-henne2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.devcel.2011.05.015; Exact single-result bibliography and complete abstract; primary body scope specified separately where recovered | supports | Native MED identifies The ESCRT pathway. by Henne WM, Buchkovich NJ, Emr SD.; PMID21763610, DOI10.1016/j.devcel.2011.05.015. This source is explicitly a review. Its complete abstract supports the MVB cargo-degradation and membrane-sculpting overview; it is not treated as a primary intervention experiment. |
| root27-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Exact taxId, scientificName, rank and lineage | supports | Native strain559292 is Saccharomyces cerevisiae S288C. The Vps27 xref is a reference-strain instance of the named yeast gene, not a claim that Katzmann used exactly that strain. |
| root27-sources-protein-P40343 | https://rest.uniprot.org/uniprotkb/P40343.json; Primary accession, entryType, names, gene tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR LOCATION and relevant PubMed links | supports | Reviewed primary P40343 identifies VPS27/YNR006W in taxon559292. FUNCTION and ER-independent endosome membrane annotation cite PMID12900393 for ESCRT-I recruitment, and native gene synonyms are explicit. Its reference-strain xref does not replace the primary experiment strains. |
| ilv-neighbor | data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml; Lines1–100; identifier, definition, hierarchy and initial source context only | context_only | The local ID resolves to the distinct internal vesicle, with MVB parthood. The whole MVB is not substituted for one ILV. This is not a full neighboring-record review. |
| root27-sources-katzmann2003-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/; Primary HTML sec5,sec6,sec12 complete; Fig3/4 captions included; other body sections not certified here | supports | Complete Results sec5 and sec6, including Fig3/4 captions, and Methods sec12 were directly read. Vps23-GFP localization in vps27/vps34 mutants and reciprocal membrane-fraction copurification support Vps27-dependent ESCRT-I recruitment/association. Methods lists SEY6210 and derived strains, not a strain inferred from the UniProt xref. No image-pixel or quantitative reanalysis was performed. |
| root27-sources-teo2004-primary-pdf | https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf; Original author-hosted primary PDF pp564–566 plus protein-preparation continuation on567; no diffraction-table or figure-pixel reanalysis | supports | Read the complete Vps20-interaction Results across pp564–566, Fig5/6 captions, Conclusions, and Experimental Procedures for plasmids/protein preparation continuing onto p567. Purified ESCRT-II/Vps25 binds Vps20 and enhances brain-liposome association; constructs originate from S.cerevisiae genomic DNA ATCC9763D and are expressed in E.coli. The membrane-orientation model remains proposed, and direct binding to one ESCRT-III subunit is not a complete pathway reconstitution. |
| native-verify | /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome.yaml --verify; Entire focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome.yaml --causal-graphs; Entire focused native output | supports | data/structures/membrane_organelle/endosome.yaml  (GO:0005768)<br>  yeast_escrt_mvb_sorting	vps27_endosomal_recruiter	UNANCHORED_WITH_UNIPROT	Vps27 endosomal ESCRT-I recruiter (UniProtKB:P40343)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/endosome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/endosome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/endosome.yaml --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endosome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/endosome.yaml --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endosome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endosome-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/endosome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent sorting into the multivesicular body pathway requires the function of a conserved endosomal protein sorting complex, ESCRT-I. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections.; PMID:12194857: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID12194857, DOI10.1016/s1534-5807(02)00220-4 and Escrt-III: an endosome-associated heterooligomeric protein complex required for mvb sorting. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections.; cellstructuremech:multivesicular_body_intraluminal_vesicle: SKIPPED; Repository-minted identifier resolves to the frozen maintained multivesicular body intraluminal vesicle record at data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml. Root repeated an ignored-inclusive anchored corpus search and verified its exact identifier/input hash. This verifies the reference, not all neighboring biology. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Native ontology terms, taxonomy and proteins were read directly; definitions and transitive parentage do not imply an unavailable direct ontology edge. Individual molecular formation necessity and exhaustive composition remain unknown.
- Primary access is bounded: Katzmann2003 body scope is sec5/6/12 and captions; Teo body scope is pp564–566 and named methods continuing onto567. Katzmann2001/Babst2002 and Henne2011 are complete-abstract only; publisher retrieval failed or was denied. Detailed scission chemistry and uninspected figures/data remain uncertified.
- Species scope and reference-strain accessions do not identify every primary experimental strain. Historical authorship, previous searches and prior review dispositions are not independently recertified.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly authorizes a bundle for every uncovered target, including honest no-finding reviews. No scientific record edit is authorized.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T013652Z-endosome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Endosome identity, source and compartment review
started_at: '2026-10-22T01:09:16Z'
finished_at: '2026-10-22T01:36:52Z'
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
summary: No concrete curation defect observed in the endosome record within the explicitly
  documented source scopes.
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
    role: context
  - path: data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml
    sha256: 8ffe704fef493506e494107aba2b583e563921f2f12a6e98748971f64976b622
    role: context
  - path: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    sha256: 599774aca4e215829787fe1a818ef52bd2c3772b48c289505d14417c05d0f679
    role: context
  - path: data/structures/membrane_organelle/endosome.yaml
    sha256: 7eb3c5b8022e63698365a49990831c7609d649c6024002eb19f6a28cdfff38a8
    role: target
  - path: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
    sha256: 47e5f39198c321eb8e1df58ff20ac1a0a50ec731170ae0f9d07d22b299594916
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
- target_id: GO:0005768
  path: data/structures/membrane_organelle/endosome.yaml
  label: endosome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/endosome.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target; exact identity, hierarchy, component/protein
    scope, organism contexts, cited evidence and every graph edge.
  selection: Target 10 of batch twenty-seven; strict uncovered path order on fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005768
checks:
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0005768
  command: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome.yaml
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
  - GO:0005768
  command: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome.yaml
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
  - GO:0005768
  command: just validate data/structures/membrane_organelle/endosome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005768
  command: just validate-strict data/structures/membrane_organelle/endosome.yaml --out
    /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endosome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005768
  summary: Native UniProt is used as the structured protein adapter. No iModulon dataset
    or expression-module inference is needed to assess these cited physical/functional
    experiments; UPR evidence is kept at the primary paper scope.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005768
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - protein-contract
  - neighbor-endoplasmic_reticulum
  - neighbor-endoplasmic_reticulum_lumen
  - neighbor-endoplasmic_reticulum_membrane
  - root27-sources-go
  - root27-sources-tax4932
  - root27-sources-katzmann2001-meta
  - root27-sources-katzmann2003-meta
  - root27-sources-teo2004-meta
  - root27-sources-babst2002-meta
  - root27-sources-henne2011-meta
  - root27-sources-tax559292
  - root27-sources-protein-P40343
  - ilv-neighbor
  - root27-sources-katzmann2003-pmc
  - root27-sources-teo2004-primary-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005768
  summary: '13 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent
    sorting into the multivesicular body pathway requires the function of a conserved
    endosomal protein sorting complex, ESCRT-I. Bibliographic identity is resolved;
    scientific scope remains restricted to the separately documented abstract/body
    inspections.; PMID:12194857: UNREACHABLE; The bulk PMID transport returned414;
    the independently retrieved exact MED record verifies PMID12194857, DOI10.1016/s1534-5807(02)00220-4
    and Escrt-III: an endosome-associated heterooligomeric protein complex required
    for mvb sorting. Bibliographic identity is resolved; scientific scope remains
    restricted to the separately documented abstract/body inspections.; cellstructuremech:multivesicular_body_intraluminal_vesicle:
    SKIPPED; Repository-minted identifier resolves to the frozen maintained multivesicular
    body intraluminal vesicle record at data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml.
    Root repeated an ignored-inclusive anchored corpus search and verified its exact
    identifier/input hash. This verifies the reference, not all neighboring biology.
    Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root27-sources-katzmann2001-meta
  - root27-sources-babst2002-meta
  - ilv-neighbor
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005768
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
  - GO:0005768
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
  - GO:0005768
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
  - GO:0005768
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
  - GO:0005768
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
  reference: data/structures/membrane_organelle/endosome.yaml
  locator: Entire maintained target including history, component and protein examples,
    all evidence and graph edges, discussions
  accessed_at: '2026-10-22T01:16:44Z'
  support: context_only
  summary: All target bytes were read. Scientific content, status and histories remain
    unchanged.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Structure identity, is-a versus parthood, constituent versus associated
    machinery, narrow evidence
  accessed_at: '2026-10-22T01:16:44Z'
  support: context_only
  summary: The whole organelle, limiting membrane and enclosed region remain distinct.
    Enzyme activity and gene viability do not establish organelle-formation necessity.
- evidence_id: protein-contract
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component.protein_examples and ProteinExample lines448–468; component essentiality
    contract
  accessed_at: '2026-10-22T01:16:44Z'
  support: context_only
  summary: Protein examples require paired biological context; native accession verification
    alone is not proof of structure membership. Formation necessity differs from protein
    function and cell viability.
- evidence_id: neighbor-endoplasmic_reticulum
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:16:44Z'
  support: context_only
  summary: These neighboring records receive separate reviews. Their unrelated source
    claims are not incorporated as proof for this target.
- evidence_id: neighbor-endoplasmic_reticulum_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum_lumen.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:16:44Z'
  support: context_only
  summary: These neighboring records receive separate reviews. Their unrelated source
    claims are not incorporated as proof for this target.
- evidence_id: neighbor-endoplasmic_reticulum_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
  locator: Entire neighboring record read, used solely for compartment boundary context
  accessed_at: '2026-10-22T01:16:44Z'
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
- evidence_id: root27-sources-katzmann2001-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A11511343%20AND%20SRC%3AMED
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.861587Z'
  support: supports
  summary: Native MED identifies Ubiquitin-dependent sorting into the multivesicular
    body pathway requires the function of a conserved endosomal protein sorting complex,
    ESCRT-I. by Katzmann DJ, Babst M, Emr SD.; PMID11511343, DOI10.1016/s0092-8674(01)00434-2.
    The complete primary abstract identifies ESCRT-I, ubiquitin recognition and MVB
    sorting in yeast, including biosynthetic and cell-surface cargo. It does not make
    transient ESCRT machinery permanent endosome constituents.
  snapshot_sha256: 89b0ab16f1c997094ab3253063701f5097b815c030e16320d5d41f485e3d50a9
- evidence_id: root27-sources-katzmann2003-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.200302136
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.875261Z'
  support: supports
  summary: Native MED identifies Vps27 recruits ESCRT machinery to endosomes during
    MVB sorting. by Katzmann DJ, Stefan CJ, Babst M, Emr SD.; PMID12900393, DOI10.1083/jcb.200302136.
    The complete primary abstract identifies Vps27/PI(3)P-dependent ESCRT-I recruitment
    at yeast endosomes. Detailed recruitment and binding results are separately read
    in the primary body.
  snapshot_sha256: 7db90817ea355af4a50a7af4ff871e6469a57ef9b2c9e03388f6d02e8c202720
- evidence_id: root27-sources-teo2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2004.09.003
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.877564Z'
  support: supports
  summary: 'Native MED identifies ESCRT-II, an endosome-associated complex required
    for protein sorting: crystal structure and interactions with ESCRT-III and membranes.
    by Teo H, Perisic O, González B, Williams RL.; PMID15469844, DOI10.1016/j.devcel.2004.09.003.
    The complete primary abstract reports yeast ESCRT-II architecture, direct Vps20
    binding through Vps25 and enhanced membrane binding. It supports the ESCRT-II-to-III
    handoff, not every molecular transition of a complete ESCRT pathway.'
  snapshot_sha256: 092a112c9409a79c051d42786aeccd62376d565f07ed37f3176165fd5bc1fddf
- evidence_id: root27-sources-babst2002-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A12194857%20AND%20SRC%3AMED
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:58.446989Z'
  support: supports
  summary: 'Native MED identifies Escrt-III: an endosome-associated heterooligomeric
    protein complex required for mvb sorting. by Babst M, Katzmann DJ, Estepa-Sabal
    EJ, Meerloo T, Emr SD.; PMID12194857, DOI10.1016/s1534-5807(02)00220-4. The complete
    primary abstract describes membrane recruitment and oligomerization of Vps2/Vps20/Vps24/Snf7
    into ESCRT-III and cargo sorting/concentration. The target describes broad membrane
    remodeling; exact scission mechanics are not established by this abstract alone.'
  snapshot_sha256: 154c66e5c81005bcb646718e07a114e6c610e20c4a80803a5505061f4c107317
- evidence_id: root27-sources-henne2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.devcel.2011.05.015
  locator: Exact single-result bibliography and complete abstract; primary body scope
    specified separately where recovered
  accessed_at: '2026-10-22T01:10:57.861442Z'
  support: supports
  summary: Native MED identifies The ESCRT pathway. by Henne WM, Buchkovich NJ, Emr
    SD.; PMID21763610, DOI10.1016/j.devcel.2011.05.015. This source is explicitly
    a review. Its complete abstract supports the MVB cargo-degradation and membrane-sculpting
    overview; it is not treated as a primary intervention experiment.
  snapshot_sha256: 460a530ee4c6be779250900ab8aa406f9e827f57f923f35fbf21cc507303cb55
- evidence_id: root27-sources-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Exact taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T01:10:58.507227Z'
  support: supports
  summary: Native strain559292 is Saccharomyces cerevisiae S288C. The Vps27 xref is
    a reference-strain instance of the named yeast gene, not a claim that Katzmann
    used exactly that strain.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root27-sources-protein-P40343
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40343.json
  locator: Primary accession, entryType, names, gene tokens, organism, FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION and relevant PubMed links
  accessed_at: '2026-10-22T01:10:59.091462Z'
  support: supports
  summary: Reviewed primary P40343 identifies VPS27/YNR006W in taxon559292. FUNCTION
    and ER-independent endosome membrane annotation cite PMID12900393 for ESCRT-I
    recruitment, and native gene synonyms are explicit. Its reference-strain xref
    does not replace the primary experiment strains.
  snapshot_sha256: 9722b86a9641dd5d053f0babc34f530ea7656e19571069c2eb081537e836c344
- evidence_id: ilv-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml
  locator: Lines1–100; identifier, definition, hierarchy and initial source context
    only
  accessed_at: '2026-10-22T01:16:44Z'
  support: context_only
  summary: The local ID resolves to the distinct internal vesicle, with MVB parthood.
    The whole MVB is not substituted for one ILV. This is not a full neighboring-record
    review.
- evidence_id: root27-sources-katzmann2003-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2172707/
  locator: Primary HTML sec5,sec6,sec12 complete; Fig3/4 captions included; other
    body sections not certified here
  accessed_at: '2026-10-22T01:12:25.464014Z'
  support: supports
  summary: Complete Results sec5 and sec6, including Fig3/4 captions, and Methods
    sec12 were directly read. Vps23-GFP localization in vps27/vps34 mutants and reciprocal
    membrane-fraction copurification support Vps27-dependent ESCRT-I recruitment/association.
    Methods lists SEY6210 and derived strains, not a strain inferred from the UniProt
    xref. No image-pixel or quantitative reanalysis was performed.
  snapshot_sha256: d4bc3fc8fd5cbf98c1b88722373dbd34c271f2df8da4bbb78d4f808dc7197233
- evidence_id: root27-sources-teo2004-primary-pdf
  kind: primary_source
  reference: https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf
  locator: Original author-hosted primary PDF pp564–566 plus protein-preparation continuation
    on567; no diffraction-table or figure-pixel reanalysis
  accessed_at: '2026-10-22T01:12:25.464317Z'
  support: supports
  summary: Read the complete Vps20-interaction Results across pp564–566, Fig5/6 captions,
    Conclusions, and Experimental Procedures for plasmids/protein preparation continuing
    onto p567. Purified ESCRT-II/Vps25 binds Vps20 and enhances brain-liposome association;
    constructs originate from S.cerevisiae genomic DNA ATCC9763D and are expressed
    in E.coli. The membrane-orientation model remains proposed, and direct binding
    to one ESCRT-III subunit is not a complete pathway reconstitution.
  snapshot_sha256: 9a62830da92c7a92939524b134a277cf6381382e5539dfdfb47ab58e22817dce
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome.yaml
    --verify
  locator: Entire focused native output
  accessed_at: '2026-10-22T01:11:37.128034Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/endosome.yaml
    --causal-graphs
  locator: Entire focused native output
  accessed_at: '2026-10-22T01:11:37.720315Z'
  support: supports
  summary: "data/structures/membrane_organelle/endosome.yaml  (GO:0005768)\n  yeast_escrt_mvb_sorting\t\
    vps27_endosomal_recruiter\tUNANCHORED_WITH_UNIPROT\tVps27 endosomal ESCRT-I recruiter\
    \ (UniProtKB:P40343)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  UNANCHORED_WITH_UNIPROT\
    \   no component_ref, but node carries a UniProtKB grounding or xref\n     0 \
    \ COVERED                   component_ref target holds protein_examples covering\
    \ all declared symbols\n     0  PARTIAL_EXAMPLES          component_ref target\
    \ holds protein_examples but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES\
    \   component_ref target declares gene_symbols but holds no protein_examples\n\
    \     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols\
    \ and holds no protein_examples\n     0  DANGLING_COMPONENT_REF    component_ref\
    \ names a component_id that does not exist on the record\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: c8061fd7772098b2ced41bf99dcf0e34c7c32d4f23dc97daf67e9dafb3e7dc2b
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/endosome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:09:17Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/endosome.yaml'
  snapshot_sha256: f1967fe9a6c8970fa9617167be97f3d3c9009d9512f271eee8fe321eb1f69afa
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/endosome.yaml
    --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endosome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:09:18Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/endosome.yaml\
    \ --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endosome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endosome-strict.tsv"
  snapshot_sha256: 47561a4bebc30f1cad63ef0260a62f5959290fded09b0ea8eebac66a00b082e7
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/endosome.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '13 of 16 collected target identifiers returned OK. PMID:11511343: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID11511343, DOI10.1016/s0092-8674(01)00434-2 and Ubiquitin-dependent
    sorting into the multivesicular body pathway requires the function of a conserved
    endosomal protein sorting complex, ESCRT-I. Bibliographic identity is resolved;
    scientific scope remains restricted to the separately documented abstract/body
    inspections.; PMID:12194857: UNREACHABLE; The bulk PMID transport returned414;
    the independently retrieved exact MED record verifies PMID12194857, DOI10.1016/s1534-5807(02)00220-4
    and Escrt-III: an endosome-associated heterooligomeric protein complex required
    for mvb sorting. Bibliographic identity is resolved; scientific scope remains
    restricted to the separately documented abstract/body inspections.; cellstructuremech:multivesicular_body_intraluminal_vesicle:
    SKIPPED; Repository-minted identifier resolves to the frozen maintained multivesicular
    body intraluminal vesicle record at data/structures/membrane_organelle/multivesicular_body_intraluminal_vesicle.yaml.
    Root repeated an ignored-inclusive anchored corpus search and verified its exact
    identifier/input hash. This verifies the reference, not all neighboring biology.
    Native source checks are separately scoped; skipped or unreachable identifiers
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
  topic: Whole endosome versus membrane, lumen and ILV
  outcome: supported
  target_ids:
  - GO:0005768
  summary: GO0005768 exactly denotes the whole endosome; membrane/lumen parts and
    the collective membrane component match native terms. GO0005771 defines an MVB
    as an endosome containing internal vesicles; the local ILV ID denotes one distinct
    internal vesicle. No requirement to add optional parentage or duplicate all MVB
    subtypes is invented.
  evidence_ids:
  - record
  - root27-sources-go
  - ilv-neighbor
  - policy
- assessment_id: scope
  area: scope
  topic: Yeast endosomal sorting model
  outcome: supported
  target_ids:
  - GO:0005768
  summary: Species4932 is exact and the primary papers support yeast MVB sorting.
    Katzmann2003 Methods explicitly lists SEY6210 derivatives; Teo uses yeast-derived
    constructs expressed in E.coli. The reference-strain VPS27 xref denotes the gene/protein
    identity and does not assert those experiment strains. COMMON is qualitative,
    not a quantified prevalence survey.
  evidence_ids:
  - record
  - root27-sources-tax4932
  - root27-sources-tax559292
  - root27-sources-protein-P40343
  - root27-sources-katzmann2001-meta
  - root27-sources-katzmann2003-meta
  - root27-sources-teo2004-meta
  - root27-sources-babst2002-meta
  - root27-sources-henne2011-meta
  - root27-sources-katzmann2003-pmc
  - root27-sources-teo2004-primary-pdf
- assessment_id: composition
  area: grounding
  topic: Boundary constituent versus transient sorting actors
  outcome: supported
  target_ids:
  - GO:0005768
  summary: The membrane row describes the collective bounding bilayer. Vps27 and ESCRT
    complexes are graph actors, consistent with the discussion keeping transient sorting
    machinery outside permanent constituent tables. P40343 matches VPS27, and exact
    GO complex IDs preserve ESCRT-I/II/III boundaries.
  evidence_ids:
  - record
  - root27-sources-go
  - protein-contract
  - root27-sources-tax559292
  - root27-sources-protein-P40343
  - root27-sources-katzmann2003-pmc
  - root27-sources-teo2004-primary-pdf
- assessment_id: necessity
  area: evidence
  topic: Individual components and formation
  outcome: unknown
  target_ids:
  - GO:0005768
  summary: The complete bilayer is constitutive of the membrane-bounded endosome.
    Neither this collective ESSENTIAL row nor ESCRT cargo-sorting requirements establish
    individual lipid necessity or an exhaustive endosome-formation mechanism.
  evidence_ids:
  - record
  - root27-sources-go
  - root27-sources-katzmann2001-meta
  - root27-sources-katzmann2003-meta
  - root27-sources-teo2004-meta
  - root27-sources-babst2002-meta
  - root27-sources-henne2011-meta
- assessment_id: functions
  area: evidence
  topic: Endosomal transport and MVB cargo sorting
  outcome: supported
  target_ids:
  - GO:0005768
  summary: Native GO and Katzmann primary evidence support transport of internalized/biosynthetic
    material and ubiquitin-dependent sorting. Henne is clearly a review supplying
    context. These functions do not imply all endosomal cargo is ESCRT-dependent or
    that MVB formation defines every endosome.
  evidence_ids:
  - record
  - root27-sources-go
  - root27-sources-katzmann2001-meta
  - root27-sources-katzmann2003-meta
  - root27-sources-teo2004-meta
  - root27-sources-babst2002-meta
  - root27-sources-henne2011-meta
  - root27-sources-katzmann2003-pmc
  - root27-sources-teo2004-primary-pdf
- assessment_id: graph
  area: graph
  topic: All seven endosomal sorting edges
  outcome: supported
  target_ids:
  - GO:0005768
  summary: Enclosure and ILV formation/containment follow the exact GO definitions.
    Katzmann2003 directly supports Vps27 recruitment/association with ESCRT-I; Katzmann2001
    abstract supports ubiquitin cargo recognition. Teo Results support ESCRT-II interaction
    with Vps20 and enhanced membrane association. Babst abstract supports ESCRT-III
    membrane oligomerization/cargo sorting, while the exact modern GO ESCRT-III definition
    corroborates broad remodeling. NONMECHANISTIC scope appropriately avoids claiming
    complete scission chemistry, deubiquitination or Vps4 recycling.
  evidence_ids:
  - record
  - root27-sources-go
  - root27-sources-katzmann2001-meta
  - root27-sources-katzmann2003-meta
  - root27-sources-teo2004-meta
  - root27-sources-babst2002-meta
  - root27-sources-henne2011-meta
  - root27-sources-katzmann2003-pmc
  - root27-sources-teo2004-primary-pdf
  - ilv-neighbor
- assessment_id: source-limit
  area: evidence
  topic: Detailed membrane-scission mechanism
  outcome: unknown
  target_ids:
  - GO:0005768
  summary: The broad ESCRT-III membrane role is supported, but Babst full text was
    not recovered in this review. Exact membrane scission steps and the completeness
    of the original paper experiments are not independently certified.
  evidence_ids:
  - record
  - root27-sources-babst2002-meta
  - root27-sources-go
- assessment_id: coverage
  area: completeness
  topic: Full target and honest optional gaps
  outcome: supported
  target_ids:
  - GO:0005768
  summary: All target fields and edges were read. The target asserts no images, physical
    measurements, trait links or verbatim snippets. Open molecular inventories remain
    explicit optional gaps; source-access limits do not become invented defects. PROPOSED
    status and append-only historical decisions are preserved.
  evidence_ids:
  - record
  - policy
  - root27-sources-go
  - root27-sources-katzmann2001-meta
  - root27-sources-katzmann2003-meta
  - root27-sources-teo2004-meta
  - root27-sources-babst2002-meta
  - root27-sources-henne2011-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Native ontology terms, taxonomy and proteins were read directly; definitions and
  transitive parentage do not imply an unavailable direct ontology edge. Individual
  molecular formation necessity and exhaustive composition remain unknown.
- 'Primary access is bounded: Katzmann2003 body scope is sec5/6/12 and captions; Teo
  body scope is pp564–566 and named methods continuing onto567. Katzmann2001/Babst2002
  and Henne2011 are complete-abstract only; publisher retrieval failed or was denied.
  Detailed scission chemistry and uninspected figures/data remain uncertified.'
- Species scope and reference-strain accessions do not identify every primary experimental
  strain. Historical authorship, previous searches and prior review dispositions are
  not independently recertified.
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
