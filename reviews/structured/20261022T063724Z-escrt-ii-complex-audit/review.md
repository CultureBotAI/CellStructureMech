# Escrt ii complex scientific review

- Review: 20261022T063724Z-escrt-ii-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:16:20Z
- Finished UTC: 2026-10-22T06:37:24Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

ESCRT-II identity, three-class core, source-specific architecture and activation graph are supported. One grouped minor resolves the exact Vps22, Vps25 and Vps36 families; targeting, activation and formation are kept distinct.

## Scope And Provenance

Exactly one whole maintained target plus frozen guidance and protein-example skill. Source-specific actual read extents are enumerated per evidence row; no maintained neighboring record supplies scientific evidence.

Selection: Target 8 of batch54, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000814 | data/structures/other/escrt_ii_complex.yaml | maintained | ESCRT II complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000814 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000814 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0000814 | Native focused check passed; scientific claims assessed separately. |
| Native verify | passed | True | GO:0000814 | Native focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0000814 | No expression-module inference is used for these structure and pathway claims. |
| Claim-level scientific review | passed | True | GO:0000814 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0000814 | 15 of 16 collected target identifiers returned OK. PMID:12194858: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0000814 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000814 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000814 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000814 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0000814 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact ESCRT-II identity and core architecture

identity: supported. Targets: GO:0000814.

GO identity, parent/parthood and broad synonym are correct. Teo supports the yeast canonical example with truncated structural core and two Vps25 copies. Native and primary sources agree on the three named classes and1:2:1 architecture.

### Three exact family identities

grounding: concern. Targets: GO:0000814.

The verified Vps22, Vps25 and Vps36 full-protein families resolve the current label-only rows. SNF8/VPS22 alias, reviewed accessions, taxa and exact gene-query uniqueness remain correct.

### Source organism versus expression and assay systems

scope: supported. Targets: GO:0000814.

The canonical species4932 is correct, with ATCC9763D-derived recombinant material and bacterial expression explicitly distinguished from S288C reference proteins. Im2008 human constructs/BY4741 yeast and Im2009 human constructs/BY4742 yeast are not treated as one experiment.

### Complex activation versus single-subunit targeting

graph: supported. Targets: GO:0000814.

The NONMECHANISTIC graph states ESCRT-II membership and initiation of ESCRT-III formation. That is supported by direct Vps25/Vps20 binding and GUV activation. Im2009 Vps20 membrane localization independent of ESCRT-II does not contradict activation of the assembled ESCRT-III machinery; the review does not reinterpret the broad GO recruitment wording as a requirement for every Vps20 molecule. Vps4 remains external.

### Do not equate sorting or domain mutation with universal necessity

grounding: unknown. Targets: GO:0000814.

The inspected targeting, interaction and cargo assays do not establish blanket whole-protein formation requirements for every ESCRT-II class. UNKNOWN is retained; demonstrated interfaces and intact stoichiometry remain positive anatomical evidence.

### Complete maintained target with bounded source inspection

completeness: supported. Targets: GO:0000814.

All maintained fields, evidence notes, graph statements and discussions were checked at the declared source extents. Optional inventories, exact stoichiometry and unresolved formation experiments are not fabricated from validation success.

## Findings

### F1: Ground the three ESCRT-II constituent classes

minor / open / confirmed; issue key: escrt-ii-exact-families.

All three named yeast subunits remain label-only although exact full families IPR016689, IPR008570 and IPR037855 are verified with independent protein membership joins.

## Recommended Actions And Acceptance Checks

### A1

Use IPR016689 for Vps22/Snf8, IPR008570 for Vps25 and IPR037855 for Vps36, aligning current notes/TODO.

- Do not substitute a shared winged-helix or GLUE/NZF domain.
- Preserve two Vps25 copies where source-scoped stoichiometry is later curated; keep reference-strain/experimental-system distinctions.
- Preserve supported identities and biological scope; pass applicable native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/escrt_ii_complex.yaml; Entire maintained record including all history, discussions, evidence, components, examples and causal graph | context_only | The entire target was read; dated curation history is not independent biological evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ProteinExample, essentiality, taxonomic presence and graph scope | context_only | Essentiality concerns formation, not function or viability. COMMON means present in most members, losses the exception; qualitative synthesis does not imply a measured prevalence census. |
| curation | docs/CURATION.md; Component grounding and REVIEWED_LABEL_ONLY contract, including159–160 | context_only | Exact full-protein families are distinct from shared domains or paralog supergroups. A reviewed label-only status is not merely a placeholder for an exact mapping that was not curated this pass. |
| escrt54-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621; Complete target-relevant definitions/synonym scopes and typed child relationships within combined response; unrelated terms not attributed to this record | supports | GO0000814 identifies ESCRT-II and its broad synonym, downstream sorting and ESCRT-III recruitment role; GO0036452 and GO0010008 separately show is_a and part_of relationships. GO0071985 defines the sorting pathway. |
| escrt54-agent-GO0000814-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000814/ancestors?relations=is_a; Complete is_a-only ancestor response | supports | The is_a-only ancestor closure independently contains the ESCRT complex and protein-containing-complex classes. It is not a part_of query. |
| escrt54-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete ENA taxonomy response | supports | Taxon4932 is Saccharomyces cerevisiae, rankspecies; its native names and lineage identify this exact node. |
| escrt54-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete ENA taxonomy response | supports | Taxon559292 is Saccharomyces cerevisiae S288C, rankstrain; its native names and lineage identify this exact node. |
| escrt54-agent-protein-P47142 | https://rest.uniprot.org/uniprotkb/P47142.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed P47142: Vacuolar protein-sorting-associated protein 25; primary genes VPS25, synonyms VPT25, taxon559292. Native comments retain their own experimental/inferred evidence scope. The protein response separately supplies its family xrefs; a family-entry response is not treated as this protein-membership proof. |
| escrt54-agent-protein-Q06696 | https://rest.uniprot.org/uniprotkb/Q06696.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed Q06696: Vacuolar protein-sorting-associated protein 36; primary genes VPS36, synonyms GRD12, VAC3, VPL11, taxon559292. Native comments retain their own experimental/inferred evidence scope. The protein response separately supplies its family xrefs; a family-entry response is not treated as this protein-membership proof. |
| escrt54-agent-protein-Q12483 | https://rest.uniprot.org/uniprotkb/Q12483.json; Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments and family xrefs | supports | Reviewed Q12483: Vacuolar-sorting protein SNF8; primary genes SNF8, synonyms VPS22, taxon559292. Native comments retain their own experimental/inferred evidence scope. The protein response separately supplies its family xrefs; a family-entry response is not treated as this protein-membership proof. |
| escrt54-agent-gene-VPS22-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS22%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: Q12483. Returned gene tokens/aliases identify the maintained protein without confusing its primary name with the queried synonym. |
| escrt54-agent-gene-VPS25-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS25%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: P47142. Returned gene tokens/aliases identify the maintained protein without confusing its primary name with the queried synonym. |
| escrt54-agent-gene-VPS36-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS36%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned accession/name/genes/organism fields | supports | Exact reviewed-organism query returns 1 entry: Q06696. Returned gene tokens/aliases identify the maintained protein without confusing its primary name with the queried synonym. |
| escrt54-agent-pmid-12194858 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12194858+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED identity and abstract | supports | MED12194858: Endosome-associated complex, ESCRT-II, recruits transport machinery for protein sorting at the multivesicular body. Babst M, Katzmann DJ, Snyder WB, Wendland B, Emr SD. (2002), DOI10.1016/s1534-5807(02)00219-8. Exact metadata and complete abstract read; this is not full-body attestation. |
| escrt54-agent-doi-j_devcel_2004_09_003 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2004.09.003%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: ESCRT-II, an endosome-associated complex required for protein sorting: crystal structure and interactions with ESCRT-III and membranes. Teo H, Perisic O, González B, Williams RL. (2004), PMID15469844. Complete native abstract read. Independent full-body evidence, where read, is listed separately. |
| escrt54-agent-doi-j_devcel_2008_04_004 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2008.04.004%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: Integrated structural model and membrane targeting mechanism of the human ESCRT-II complex. Im YJ, Hurley JH. (2008), PMID18539118. Complete native abstract read. Independent full-body evidence, where read, is listed separately. |
| escrt54-agent-doi-j_devcel_2009_07_008 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2009.07.008%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: Structure and function of the ESCRT-II-III interface in multivesicular body biogenesis. Im YJ, Wollert T, Boura E, Hurley JH. (2009), PMID19686684. Complete native abstract read. Independent full-body evidence, where read, is listed separately. |
| escrt54-agent-doi-nature02914 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature02914%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: Structure of the ESCRT-II endosomal trafficking complex. Hierro A, Sun J, Rusnak AS, Kim J, Prag G, Emr SD, Hurley JH. (2004), PMID15329733. Complete native abstract read. Independent full-body evidence, where read, is listed separately. |
| escrt54-agent-doi-science_1161070 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1161070%22&amp;format=json&amp;resultType=core; Complete native bibliographic identity and abstract | supports | Exact DOI/MED identity: Helical structures of ESCRT-III are disassembled by VPS4. Lata S, Schoehn G, Jain A, Pires R, Piehler J, Gottlinger HG, Weissenhorn W. (2008), PMID18687924. Complete native abstract read. Independent full-body evidence, where read, is listed separately. |
| escrt54-agent-teo2004-primary-pdf | https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf; Printed p559 summary/Introduction; p564–567 direct-interaction/liposome Results, Fig4/5/6 caption text, Conclusions and plasmid/expression/purification/pull-down Methods. Other crystallographic Results/Methods not independently used. | supports | Teo2004 resolves the yeast core with one Vps22, two Vps25 and truncated Vps36; purified ESCRT-II and isolated Vps25 bind Vps20 directly and enhance liposome binding. Removal of Vps22 residues1–40 or Vps36 residues1–370 does not abolish the Vps20 interaction. ATCC9763D yeast genomic material was expressed in C41(DE3)/B834(DE3); this is recombinant yeast anatomy, not native bacterial ESCRT. |
| escrt54-agent-primary-PMC2475506 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2475506/; Results S4/S6/S7 with Fig4/5 captions; Methods S10/S16; complete native abstract supplies structural stoichiometry. No figure pixels or supplement files. | supports | Im/Hurley2008 examines human recombinant complexes and yeast BY4741-derived sorting/localization mutants. GLUE/Vps22-H0 jointly contribute to membrane targeting; the pseudo-intact liposome construct lacks VPS25-WH2. Its membrane-binding defects are not whole-complex formation experiments. |
| escrt54-agent-primary-PMC2749878 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2749878/; Results S2/S5/S6/S7/S8; Discussion S10; Methods S12/S16/S17/S18/S20, Table1 and embedded Fig1–4 captions. No pixels/supplements. | supports | Im2009 directly maps the VPS25/VPS20 interface and activates ESCRT-III budding/scission in a synthetic GUV assay. Vps20 localization can persist without ESCRT-II interaction; the paper distinguishes activation from membrane recruitment of this single protein. Human recombinant crystallography and BY4742 yeast cargo assays are separate systems. |
| escrt54-agent-primary-PMC2758909 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2758909/; Complete main scientific text S1 and Fig1–4 captions. Supplementary Methods/experiments not independently read. | supports | Lata2008 studies engineered human CHMP2A/CHMP3 polymers and VPS4B-dependent ATP/Mg disassembly. This supports Vps4 as an external recycling factor; it is not a yeast ESCRT-II constituent or an exact native yeast polymer architecture. |
| escrt54-agent-ipr-IPR016689 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016689/; Native name/type, complete descriptions and curation flags, member signatures and hierarchy; exact protein membership independently evidenced | supports | IPR016689 identifies the complete Snf8/Vps22 family, with exact PIRSF017215/PTHR12806 signatures; its hierarchy separates it from Vps36 under the broader Snf8/Vps36 parent. |
| escrt54-agent-ipr-IPR008570 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008570/; Native name/type, complete descriptions and curation flags, member signatures and hierarchy; exact protein membership independently evidenced | supports | IPR008570 identifies the complete Vps25 family with PF05871/PTHR13149 signatures. Its incidental Vps35 wording is not adopted as an interaction claim. |
| escrt54-agent-ipr-IPR037855 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037855/; Native name/type, complete descriptions and curation flags, member signatures and hierarchy; exact protein membership independently evidenced | supports | IPR037855 identifies Vps36 with PTHR13128, distinct from its GLUE/NZF domains and from sister Snf8/Vps22. |
| schema-result | just validate data/structures/other/escrt_ii_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/escrt_ii_complex.yaml |
| strict-result | just validate-strict data/structures/other/escrt_ii_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_ii_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/escrt_ii_complex.yaml --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_ii_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_ii_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml --causal-graphs; Complete native focused report | supports | data/structures/other/escrt_ii_complex.yaml  (GO:0000814)<br>  yeast_escrt_ii_mvb_escrt_iii_recruitment	vps22_escrt_ii_subunit	COVERED	-&gt;vps22_escrt_ii_subunit (UniProtKB:Q12483)<br>  yeast_escrt_ii_mvb_escrt_iii_recruitment	vps25_escrt_ii_subunit	COVERED	-&gt;vps25_escrt_ii_subunit (UniProtKB:P47142)<br>  yeast_escrt_ii_mvb_escrt_iii_recruitment	vps36_escrt_ii_subunit	COVERED	-&gt;vps36_escrt_ii_subunit (UniProtKB:Q06696)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/escrt_ii_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 15 of 16 collected target identifiers returned OK. PMID:12194858: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Five completed same-base batch26 global gates await guarded parent manifest/hash integration.
- No source figure pixels, supplemental experiments or atomic coordinates were independently analyzed. Embedded captions are text evidence only.
- Reference proteins at S288C559292 do not identify every experimental yeast strain. COMMON keeps its majority-occurrence/losses-exception meaning; qualitative source synthesis supports it without measuring population prevalence.
- Babst2002 and Hierro2004 were inspected at complete native abstract scope. The retained Hierro publisher200 response is a Client Challenge, not the primary body.
- The existing1:2:1 stoichiometry follow-up is supported by primary anatomy; optional numeric slots are not treated as a required-field defect.
- Teo interface-mutation details outside the declared read extent are not used to assign formation essentiality.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T063724Z-escrt-ii-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Escrt ii complex scientific review
started_at: '2026-10-22T06:16:20Z'
finished_at: '2026-10-22T06:37:24Z'
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
summary: ESCRT-II identity, three-class core, source-specific architecture and activation
  graph are supported. One grouped minor resolves the exact Vps22, Vps25 and Vps36
  families; targeting, activation and formation are kept distinct.
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
  - path: data/structures/other/escrt_ii_complex.yaml
    sha256: e95b7f2a0dfdc218f0b5ffb7918966f72a844bdfe8ccf82accc075c116c98ec7
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
- target_id: GO:0000814
  path: data/structures/other/escrt_ii_complex.yaml
  label: ESCRT II complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_ii_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one whole maintained target plus frozen guidance and protein-example
    skill. Source-specific actual read extents are enumerated per evidence row; no
    maintained neighboring record supplies scientific evidence.
  selection: Target 8 of batch54, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000814
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: just validate data/structures/other/escrt_ii_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: just validate-strict data/structures/other/escrt_ii_complex.yaml --out
    /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_ii_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0000814
  summary: No expression-module inference is used for these structure and pathway
    claims.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000814
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - escrt54-agent-go
  - escrt54-agent-GO0000814-ancestors
  - escrt54-agent-tax4932
  - escrt54-agent-tax559292
  - escrt54-agent-protein-P47142
  - escrt54-agent-protein-Q06696
  - escrt54-agent-protein-Q12483
  - escrt54-agent-gene-VPS22-559292
  - escrt54-agent-gene-VPS25-559292
  - escrt54-agent-gene-VPS36-559292
  - escrt54-agent-pmid-12194858
  - escrt54-agent-doi-j_devcel_2004_09_003
  - escrt54-agent-doi-j_devcel_2008_04_004
  - escrt54-agent-doi-j_devcel_2009_07_008
  - escrt54-agent-doi-nature02914
  - escrt54-agent-doi-science_1161070
  - escrt54-agent-teo2004-primary-pdf
  - escrt54-agent-primary-PMC2475506
  - escrt54-agent-primary-PMC2749878
  - escrt54-agent-primary-PMC2758909
  - escrt54-agent-ipr-IPR016689
  - escrt54-agent-ipr-IPR008570
  - escrt54-agent-ipr-IPR037855
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0000814
  summary: '15 of 16 collected target identifiers returned OK. PMID:12194858: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - escrt54-agent-pmid-12194858
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0000814
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0000814
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
    and current batch54 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/escrt_ii_complex.yaml
  locator: Entire maintained record including all history, discussions, evidence,
    components, examples and causal graph
  accessed_at: '2026-10-22T06:28:22Z'
  support: context_only
  summary: The entire target was read; dated curation history is not independent biological
    evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ProteinExample, essentiality, taxonomic presence and
    graph scope
  accessed_at: '2026-10-22T06:28:22Z'
  support: context_only
  summary: Essentiality concerns formation, not function or viability. COMMON means
    present in most members, losses the exception; qualitative synthesis does not
    imply a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Component grounding and REVIEWED_LABEL_ONLY contract, including159–160
  accessed_at: '2026-10-22T06:28:22Z'
  support: context_only
  summary: Exact full-protein families are distinct from shared domains or paralog
    supergroups. A reviewed label-only status is not merely a placeholder for an exact
    mapping that was not curated this pass.
- evidence_id: escrt54-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000813,GO:0000814,GO:0000815,GO:0005768,GO:0010008,GO:0016887,GO:0032991,GO:0033565,GO:0036452,GO:0070676,GO:0071985,GO:0090148,GO:1990621
  locator: Complete target-relevant definitions/synonym scopes and typed child relationships
    within combined response; unrelated terms not attributed to this record
  accessed_at: '2026-10-22T06:20:02.063646Z'
  support: supports
  summary: GO0000814 identifies ESCRT-II and its broad synonym, downstream sorting
    and ESCRT-III recruitment role; GO0036452 and GO0010008 separately show is_a and
    part_of relationships. GO0071985 defines the sorting pathway.
  snapshot_sha256: 563ffa6dea1c58c1c92024214051980b0b5f3eefd7984f1ef56cb02432f9999b
- evidence_id: escrt54-agent-GO0000814-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000814/ancestors?relations=is_a
  locator: Complete is_a-only ancestor response
  accessed_at: '2026-10-22T06:20:11.310111Z'
  support: supports
  summary: The is_a-only ancestor closure independently contains the ESCRT complex
    and protein-containing-complex classes. It is not a part_of query.
  snapshot_sha256: a829eb5d826b213e431920de398b9fbfc86638d1b2c04bde4d67034101ad65d2
- evidence_id: escrt54-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete ENA taxonomy response
  accessed_at: '2026-10-22T06:20:02.063372Z'
  support: supports
  summary: Taxon4932 is Saccharomyces cerevisiae, rankspecies; its native names and
    lineage identify this exact node.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: escrt54-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete ENA taxonomy response
  accessed_at: '2026-10-22T06:20:02.063749Z'
  support: supports
  summary: Taxon559292 is Saccharomyces cerevisiae S288C, rankstrain; its native names
    and lineage identify this exact node.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: escrt54-agent-protein-P47142
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47142.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:20:02.998152Z'
  support: supports
  summary: 'Reviewed P47142: Vacuolar protein-sorting-associated protein 25; primary
    genes VPS25, synonyms VPT25, taxon559292. Native comments retain their own experimental/inferred
    evidence scope. The protein response separately supplies its family xrefs; a family-entry
    response is not treated as this protein-membership proof.'
  snapshot_sha256: d2a16d3f9839384e78be24a7b4e0f21f1e3ed2223f7aab79b09ab1b567057257
- evidence_id: escrt54-agent-protein-Q06696
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q06696.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:20:03.829701Z'
  support: supports
  summary: 'Reviewed Q06696: Vacuolar protein-sorting-associated protein 36; primary
    genes VPS36, synonyms GRD12, VAC3, VPL11, taxon559292. Native comments retain
    their own experimental/inferred evidence scope. The protein response separately
    supplies its family xrefs; a family-entry response is not treated as this protein-membership
    proof.'
  snapshot_sha256: 0fbc4ab1a3fa68f1a3c78fb9b0ff864be16758cd681d50f55101e05f129f5ddb
- evidence_id: escrt54-agent-protein-Q12483
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12483.json
  locator: Accession/status/name/all gene tokens/organism; complete FUNCTION/SUBUNIT/SUBCELLULAR
    LOCATION/SIMILARITY comments and family xrefs
  accessed_at: '2026-10-22T06:20:04.673960Z'
  support: supports
  summary: 'Reviewed Q12483: Vacuolar-sorting protein SNF8; primary genes SNF8, synonyms
    VPS22, taxon559292. Native comments retain their own experimental/inferred evidence
    scope. The protein response separately supplies its family xrefs; a family-entry
    response is not treated as this protein-membership proof.'
  snapshot_sha256: 41764f2dc6af4a6d21a77ae0e0ffa32f449ca9c48a4f60a86cb9e618d05ef59e
- evidence_id: escrt54-agent-gene-VPS22-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS22%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:20:05.664850Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: Q12483. Returned gene tokens/aliases
    identify the maintained protein without confusing its primary name with the queried
    synonym.'
  snapshot_sha256: acd580440b9baa4add3267b00c726fe7a4472a23f82335561d55e0fe63ac2309
  search_scope: UniProt gene_exact:VPS22, organism_id:559292, reviewed:true, size500;
    all returned identities inspected.
- evidence_id: escrt54-agent-gene-VPS25-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS25%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:20:05.941225Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: P47142. Returned gene tokens/aliases
    identify the maintained protein without confusing its primary name with the queried
    synonym.'
  snapshot_sha256: 167d5536a57df56413adb410d44531c449843c5e91ec318c3129957479893427
  search_scope: UniProt gene_exact:VPS25, organism_id:559292, reviewed:true, size500;
    all returned identities inspected.
- evidence_id: escrt54-agent-gene-VPS36-559292
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AVPS36%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned accession/name/genes/organism fields
  accessed_at: '2026-10-22T06:20:06.029167Z'
  support: supports
  summary: 'Exact reviewed-organism query returns 1 entry: Q06696. Returned gene tokens/aliases
    identify the maintained protein without confusing its primary name with the queried
    synonym.'
  snapshot_sha256: 7ce9197c96302edd9f2cd77c4da31c570480ee6d6a95517b58cd363f449c08dd
  search_scope: UniProt gene_exact:VPS36, organism_id:559292, reviewed:true, size500;
    all returned identities inspected.
- evidence_id: escrt54-agent-pmid-12194858
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A12194858+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED identity and abstract
  accessed_at: '2026-10-22T06:20:08.584628Z'
  support: supports
  summary: 'MED12194858: Endosome-associated complex, ESCRT-II, recruits transport
    machinery for protein sorting at the multivesicular body. Babst M, Katzmann DJ,
    Snyder WB, Wendland B, Emr SD. (2002), DOI10.1016/s1534-5807(02)00219-8. Exact
    metadata and complete abstract read; this is not full-body attestation.'
  snapshot_sha256: ffd8cc626471255908cf7a54d1cf1d41fad9a4b47a78ee7534066153a9bf1363
- evidence_id: escrt54-agent-doi-j_devcel_2004_09_003
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2004.09.003%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:09.542436Z'
  support: supports
  summary: 'Exact DOI/MED identity: ESCRT-II, an endosome-associated complex required
    for protein sorting: crystal structure and interactions with ESCRT-III and membranes.
    Teo H, Perisic O, González B, Williams RL. (2004), PMID15469844. Complete native
    abstract read. Independent full-body evidence, where read, is listed separately.'
  snapshot_sha256: 4f3790f773f82e02d8f37e5998526d4175a42bfccbd913f1ebfe0bf7700b28e2
- evidence_id: escrt54-agent-doi-j_devcel_2008_04_004
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2008.04.004%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:09.953068Z'
  support: supports
  summary: 'Exact DOI/MED identity: Integrated structural model and membrane targeting
    mechanism of the human ESCRT-II complex. Im YJ, Hurley JH. (2008), PMID18539118.
    Complete native abstract read. Independent full-body evidence, where read, is
    listed separately.'
  snapshot_sha256: 9795b4214944ad850f76aee32d027a28807ae181253e56f6fa0307181ffd6f25
- evidence_id: escrt54-agent-doi-j_devcel_2009_07_008
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.devcel.2009.07.008%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:10.107726Z'
  support: supports
  summary: 'Exact DOI/MED identity: Structure and function of the ESCRT-II-III interface
    in multivesicular body biogenesis. Im YJ, Wollert T, Boura E, Hurley JH. (2009),
    PMID19686684. Complete native abstract read. Independent full-body evidence, where
    read, is listed separately.'
  snapshot_sha256: 7e56ff822ec9da1728abaa2b139fdfbcc4ca2eae66e52c3c55ed07b041438ff5
- evidence_id: escrt54-agent-doi-nature02914
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnature02914%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:10.155687Z'
  support: supports
  summary: 'Exact DOI/MED identity: Structure of the ESCRT-II endosomal trafficking
    complex. Hierro A, Sun J, Rusnak AS, Kim J, Prag G, Emr SD, Hurley JH. (2004),
    PMID15329733. Complete native abstract read. Independent full-body evidence, where
    read, is listed separately.'
  snapshot_sha256: 27d08a5c335e8982f8dc3eaa95690c647d4cbdc20ce57fa684daf4b61606faf5
- evidence_id: escrt54-agent-doi-science_1161070
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1126%2Fscience.1161070%22&format=json&resultType=core
  locator: Complete native bibliographic identity and abstract
  accessed_at: '2026-10-22T06:20:10.844584Z'
  support: supports
  summary: 'Exact DOI/MED identity: Helical structures of ESCRT-III are disassembled
    by VPS4. Lata S, Schoehn G, Jain A, Pires R, Piehler J, Gottlinger HG, Weissenhorn
    W. (2008), PMID18687924. Complete native abstract read. Independent full-body
    evidence, where read, is listed separately.'
  snapshot_sha256: 94989d282d11a3c4cbdc975b56e14959a8d219174d72608515c369055e4058b5
- evidence_id: escrt54-agent-teo2004-primary-pdf
  kind: primary_source
  reference: https://www2.mrc-lmb.cam.ac.uk/groups/rlw/download/publications/15469844.pdf
  locator: Printed p559 summary/Introduction; p564–567 direct-interaction/liposome
    Results, Fig4/5/6 caption text, Conclusions and plasmid/expression/purification/pull-down
    Methods. Other crystallographic Results/Methods not independently used.
  accessed_at: '2026-10-22T01:12:25.464317Z'
  support: supports
  summary: Teo2004 resolves the yeast core with one Vps22, two Vps25 and truncated
    Vps36; purified ESCRT-II and isolated Vps25 bind Vps20 directly and enhance liposome
    binding. Removal of Vps22 residues1–40 or Vps36 residues1–370 does not abolish
    the Vps20 interaction. ATCC9763D yeast genomic material was expressed in C41(DE3)/B834(DE3);
    this is recombinant yeast anatomy, not native bacterial ESCRT.
  snapshot_sha256: 9a62830da92c7a92939524b134a277cf6381382e5539dfdfb47ab58e22817dce
- evidence_id: escrt54-agent-primary-PMC2475506
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2475506/
  locator: Results S4/S6/S7 with Fig4/5 captions; Methods S10/S16; complete native
    abstract supplies structural stoichiometry. No figure pixels or supplement files.
  accessed_at: '2026-10-22T06:20:43.861281Z'
  support: supports
  summary: Im/Hurley2008 examines human recombinant complexes and yeast BY4741-derived
    sorting/localization mutants. GLUE/Vps22-H0 jointly contribute to membrane targeting;
    the pseudo-intact liposome construct lacks VPS25-WH2. Its membrane-binding defects
    are not whole-complex formation experiments.
  snapshot_sha256: bdb4eaeac9639a33fbfc848cf38e7d209bd9be2a1a7114818203b0b59b5cdd64
- evidence_id: escrt54-agent-primary-PMC2749878
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2749878/
  locator: Results S2/S5/S6/S7/S8; Discussion S10; Methods S12/S16/S17/S18/S20, Table1
    and embedded Fig1–4 captions. No pixels/supplements.
  accessed_at: '2026-10-22T06:20:43.864704Z'
  support: supports
  summary: Im2009 directly maps the VPS25/VPS20 interface and activates ESCRT-III
    budding/scission in a synthetic GUV assay. Vps20 localization can persist without
    ESCRT-II interaction; the paper distinguishes activation from membrane recruitment
    of this single protein. Human recombinant crystallography and BY4742 yeast cargo
    assays are separate systems.
  snapshot_sha256: 06ea0d888e6803d2b13dcf259f2ab47817e0fb92dce4ab887225899ef181d568
- evidence_id: escrt54-agent-primary-PMC2758909
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2758909/
  locator: Complete main scientific text S1 and Fig1–4 captions. Supplementary Methods/experiments
    not independently read.
  accessed_at: '2026-10-22T06:20:44.567859Z'
  support: supports
  summary: Lata2008 studies engineered human CHMP2A/CHMP3 polymers and VPS4B-dependent
    ATP/Mg disassembly. This supports Vps4 as an external recycling factor; it is
    not a yeast ESCRT-II constituent or an exact native yeast polymer architecture.
  snapshot_sha256: 90c9bb721fe03ae1386569cd8146ce39d0ca1ebb4eb62ed67a4fc580b8cacc20
- evidence_id: escrt54-agent-ipr-IPR016689
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016689/
  locator: Native name/type, complete descriptions and curation flags, member signatures
    and hierarchy; exact protein membership independently evidenced
  accessed_at: '2026-10-22T06:20:42.448270Z'
  support: supports
  summary: IPR016689 identifies the complete Snf8/Vps22 family, with exact PIRSF017215/PTHR12806
    signatures; its hierarchy separates it from Vps36 under the broader Snf8/Vps36
    parent.
  snapshot_sha256: 21d49936fd534f5d56fed35c60d3044d204f5c27c7dad02ee033ce3ca5032418
- evidence_id: escrt54-agent-ipr-IPR008570
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR008570/
  locator: Native name/type, complete descriptions and curation flags, member signatures
    and hierarchy; exact protein membership independently evidenced
  accessed_at: '2026-10-22T06:20:43.189098Z'
  support: supports
  summary: IPR008570 identifies the complete Vps25 family with PF05871/PTHR13149 signatures.
    Its incidental Vps35 wording is not adopted as an interaction claim.
  snapshot_sha256: 59342a0d75cb4488b4e3dc04de325d2d86049267dec3373c593728ee2b18d72b
- evidence_id: escrt54-agent-ipr-IPR037855
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037855/
  locator: Native name/type, complete descriptions and curation flags, member signatures
    and hierarchy; exact protein membership independently evidenced
  accessed_at: '2026-10-22T06:20:43.224028Z'
  support: supports
  summary: IPR037855 identifies Vps36 with PTHR13128, distinct from its GLUE/NZF domains
    and from sister Snf8/Vps22.
  snapshot_sha256: c5b91d705a08cc381af4134f3cf2c870d85259a8426f2d64a48566963f5ef6a0
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/escrt_ii_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:21Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/escrt_ii_complex.yaml'
  snapshot_sha256: e4e38a498371cb17ef3fa7ebdd131dbd953027e2fa17958849d8d8d0b05284e8
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/escrt_ii_complex.yaml --out
    /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_ii_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:16:22Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/escrt_ii_complex.yaml\
    \ --out /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_ii_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch54-20261022-hapbq96w/escrt_ii_complex-strict.tsv"
  snapshot_sha256: d921e1461afdf8dbed9fd30b993094809c3f021c332dedf8ba17e14e636305ad
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T06:25:17.982728Z'
  support: supports
  summary: "data/structures/other/escrt_ii_complex.yaml  (GO:0000814)\n  yeast_escrt_ii_mvb_escrt_iii_recruitment\t\
    vps22_escrt_ii_subunit\tCOVERED\t->vps22_escrt_ii_subunit (UniProtKB:Q12483)\n\
    \  yeast_escrt_ii_mvb_escrt_iii_recruitment\tvps25_escrt_ii_subunit\tCOVERED\t\
    ->vps25_escrt_ii_subunit (UniProtKB:P47142)\n  yeast_escrt_ii_mvb_escrt_iii_recruitment\t\
    vps36_escrt_ii_subunit\tCOVERED\t->vps36_escrt_ii_subunit (UniProtKB:Q06696)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     3  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     3\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 60759d4c40ce1830fe803c161ca1781c61fb986ff0f374f0aea3909d75974588
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch54-20261022-hapbq96w/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/escrt_ii_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T06:25:19.140056Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/escrt_ii_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '15 of 16 collected target identifiers returned OK. PMID:12194858: UNREACHABLE;
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
  topic: Exact ESCRT-II identity and core architecture
  outcome: supported
  target_ids:
  - GO:0000814
  summary: GO identity, parent/parthood and broad synonym are correct. Teo supports
    the yeast canonical example with truncated structural core and two Vps25 copies.
    Native and primary sources agree on the three named classes and1:2:1 architecture.
  evidence_ids:
  - record
  - escrt54-agent-go
  - escrt54-agent-GO0000814-ancestors
  - escrt54-agent-teo2004-primary-pdf
  - escrt54-agent-primary-PMC2475506
  - escrt54-agent-protein-P47142
  - escrt54-agent-protein-Q06696
  - escrt54-agent-protein-Q12483
- assessment_id: grounding
  area: grounding
  topic: Three exact family identities
  outcome: concern
  target_ids:
  - GO:0000814
  summary: The verified Vps22, Vps25 and Vps36 full-protein families resolve the current
    label-only rows. SNF8/VPS22 alias, reviewed accessions, taxa and exact gene-query
    uniqueness remain correct.
  evidence_ids:
  - record
  - curation
  - escrt54-agent-ipr-IPR016689
  - escrt54-agent-ipr-IPR008570
  - escrt54-agent-ipr-IPR037855
  - escrt54-agent-protein-P47142
  - escrt54-agent-protein-Q06696
  - escrt54-agent-protein-Q12483
  - escrt54-agent-gene-VPS22-559292
  - escrt54-agent-gene-VPS25-559292
  - escrt54-agent-gene-VPS36-559292
- assessment_id: scope
  area: scope
  topic: Source organism versus expression and assay systems
  outcome: supported
  target_ids:
  - GO:0000814
  summary: The canonical species4932 is correct, with ATCC9763D-derived recombinant
    material and bacterial expression explicitly distinguished from S288C reference
    proteins. Im2008 human constructs/BY4741 yeast and Im2009 human constructs/BY4742
    yeast are not treated as one experiment.
  evidence_ids:
  - record
  - schema
  - escrt54-agent-teo2004-primary-pdf
  - escrt54-agent-primary-PMC2475506
  - escrt54-agent-primary-PMC2749878
  - escrt54-agent-tax4932
  - escrt54-agent-tax559292
- assessment_id: graph
  area: graph
  topic: Complex activation versus single-subunit targeting
  outcome: supported
  target_ids:
  - GO:0000814
  summary: The NONMECHANISTIC graph states ESCRT-II membership and initiation of ESCRT-III
    formation. That is supported by direct Vps25/Vps20 binding and GUV activation.
    Im2009 Vps20 membrane localization independent of ESCRT-II does not contradict
    activation of the assembled ESCRT-III machinery; the review does not reinterpret
    the broad GO recruitment wording as a requirement for every Vps20 molecule. Vps4
    remains external.
  evidence_ids:
  - record
  - escrt54-agent-go
  - escrt54-agent-teo2004-primary-pdf
  - escrt54-agent-primary-PMC2475506
  - escrt54-agent-primary-PMC2749878
  - escrt54-agent-primary-PMC2758909
- assessment_id: formation
  area: grounding
  topic: Do not equate sorting or domain mutation with universal necessity
  outcome: unknown
  target_ids:
  - GO:0000814
  summary: The inspected targeting, interaction and cargo assays do not establish
    blanket whole-protein formation requirements for every ESCRT-II class. UNKNOWN
    is retained; demonstrated interfaces and intact stoichiometry remain positive
    anatomical evidence.
  evidence_ids:
  - record
  - schema
  - escrt54-agent-teo2004-primary-pdf
  - escrt54-agent-primary-PMC2475506
  - escrt54-agent-primary-PMC2749878
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target with bounded source inspection
  outcome: supported
  target_ids:
  - GO:0000814
  summary: All maintained fields, evidence notes, graph statements and discussions
    were checked at the declared source extents. Optional inventories, exact stoichiometry
    and unresolved formation experiments are not fabricated from validation success.
  evidence_ids:
  - record
  - schema
  - curation
  - escrt54-agent-go
findings:
- finding_id: F1
  issue_key: escrt-ii-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the three ESCRT-II constituent classes
  description: All three named yeast subunits remain label-only although exact full
    families IPR016689, IPR008570 and IPR037855 are verified with independent protein
    membership joins.
  target_ids:
  - GO:0000814
  field_paths:
  - components[*].grounding_status
  - discussions#resolve_escrt_ii_family_groundings
  evidence_ids:
  - record
  - curation
  - escrt54-agent-ipr-IPR016689
  - escrt54-agent-ipr-IPR008570
  - escrt54-agent-ipr-IPR037855
  - escrt54-agent-protein-P47142
  - escrt54-agent-protein-Q06696
  - escrt54-agent-protein-Q12483
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_ii_complex.yaml
    role: maintained scientific record
  rule_id: Exact full-component grounding
  native_severity: minor
  normalization_reason: The correct structure and protein identities remain intact.
    The available exact family mappings resolve a bounded existing label-only deferral
    without changing complex membership or mechanism.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000814
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/escrt_ii_complex.yaml
    role: maintained scientific record
  description: Use IPR016689 for Vps22/Snf8, IPR008570 for Vps25 and IPR037855 for
    Vps36, aligning current notes/TODO.
  acceptance_checks:
  - Do not substitute a shared winged-helix or GLUE/NZF domain.
  - Preserve two Vps25 copies where source-scoped stoichiometry is later curated;
    keep reference-strain/experimental-system distinctions.
  - Preserve supported identities and biological scope; pass applicable native gates.
limitations:
- Five completed same-base batch26 global gates await guarded parent manifest/hash
  integration.
- No source figure pixels, supplemental experiments or atomic coordinates were independently
  analyzed. Embedded captions are text evidence only.
- Reference proteins at S288C559292 do not identify every experimental yeast strain.
  COMMON keeps its majority-occurrence/losses-exception meaning; qualitative source
  synthesis supports it without measuring population prevalence.
- Babst2002 and Hierro2004 were inspected at complete native abstract scope. The retained
  Hierro publisher200 response is a Client Challenge, not the primary body.
- The existing1:2:1 stoichiometry follow-up is supported by primary anatomy; optional
  numeric slots are not treated as a required-field defect.
- Teo interface-mutation details outside the declared read extent are not used to
  assign formation essentiality.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
