# Source-grounded review of Dsl1/NZR complex

- Review: 20261022T062447Z-dsl1-nzr-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T06:03:20Z
- Finished UTC: 2026-10-22T06:24:47Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minors resolve an available Tip20 family mapping and the directly demonstrated Dsl1 bridge requirement in purified ternary assembly. Exact tether identity, Sec39/Dsl3 aliasing, three-protein composition, ER residence and coarse transport graph remain supported.

## Scope And Provenance

Exactly one complete maintained target; native-source fields and primary reading scopes are declared in evidence. Scientific inputs remain unchanged.

Selection: One complete record in strict-path batch 53 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0070939 | data/structures/other/dsl1_nzr_complex.yaml | maintained | Dsl1/NZR complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0070939 | Focused validator passed. |
| Focused native strict | passed | True | GO:0070939 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0070939 | Focused check passed; source claims assessed separately. |
| Native focused verify | passed | True | GO:0070939 | Focused check passed; source claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0070939 | No expression-module or transcriptomic claim requires this resource. |
| Claim-level scientific review | passed | True | GO:0070939 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0070939 | 12 of 16 collected target identifiers returned OK. PMID:11493604: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:11739780: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:15958492: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8334998: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0070939 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0070939 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0070939 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0070939 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0070939 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Three-protein tether and larger interaction partners

identity: supported. Targets: GO:0070939.

Exact GO identity, tethering parent and synonym scopes match the maintained three-protein Dsl1/Tip20/Sec39 core. SEC39/DSL3 aliasing is supported. SNARE/COPI partners remain outside the declared constituent boundary.

### Correct protein examples and one actionable family

grounding: concern. Targets: GO:0070939.

All three S288C examples and their gene/alias identities are correct. Tip20 has an available full-protein homologous family; the inspected Dsl1 and Sec39 entries are domains and are not substitutes for those whole proteins.

### ER-resident tether and transport function

graph: supported. Targets: GO:0070939.

The three membership edges, ER localization and Golgi-to-ER transport involvement are supported. NONMECHANISTIC scope appropriately excludes unresolved individual SNARE/COPI contacts and detailed fusion steps.

### Yeast experiments versus reference examples

scope: supported. Targets: GO:0070939.

The canonical and distribution statements concern the budding-yeast tether, not every eukaryotic CATCHR assembly. S288C reference entries do not identify every purified experimental strain; bacterial recombinant expression hosts are not the biological source of the yeast complex. COMMON is a qualitative curation assertion rather than a measured strain census.

### Specific interaction requirements

grounding: concern. Targets: GO:0070939.

Pairwise purified-protein assays show Sec39 binds Dsl1 but not Tip20, and combining the three produces a ternary complex. Thus Dsl1 supplies a demonstrated bridge for Tip20–Sec39 association under the reconstitution conditions. This specific assembly dependency can resolve the Dsl1 UNKNOWN with experimental scope preserved; it does not justify promoting all constituent requirements or equating assembly with cell viability.

### Whole maintained record and bounded follow-up

completeness: supported. Targets: GO:0070939.

All maintained fields, evidence, component/example rows, graph edges, discussion entries and history were read. Available exact mappings are distinguished from optional enrichment and source-access limitations. Scientific status and provenance history remain unchanged.

## Findings

### F1: Resolve the Tip20 family mapping

minor / open / confirmed; issue key: dsl1-nzr-tip20-exact-family.

Tip20 remains REVIEWED_LABEL_ONLY under an open three-subunit mapping task, but native IPR007528 is a whole-protein RINT1/Tip20 family and P33891 independently has that cross-reference. The inspected Dsl1/Sec39 domain identifiers do not resolve their whole-protein classes.

### F2: Record the demonstrated Dsl1 assembly dependency

minor / open / confirmed; issue key: dsl1-nzr-dsl1-reconstitution-formation-dependency.

Dsl1 essentiality remains UNKNOWN even though Tripathi Results S6/Figure 4 and Meiringer Results sec13/Figure 3 directly compare pairwise interactions and three-protein reconstitution: Tip20 and Sec39/Dsl3 do not associate directly, while Dsl1 binds both and links the ternary complex. This establishes a specific formation dependency in the purified system, distinct from the separate domain-mutant and growth experiments.

## Recommended Actions And Acceptance Checks

### A1

Ground Tip20 with IPR007528 and narrow the open mapping task to genuinely unresolved whole-protein classes. Preserve source-scoped homologous-family identity and yeast examples.

- Verify family type and exact example membership.
- Do not substitute Dsl1 or Sec39 domain accessions for whole proteins.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

### A2

Curate Dsl1 formation necessity using the direct reconstitution and pairwise binding evidence, retaining the tested purified-system context in its supporting notes. Preserve the distinction between the ternary core, remaining pairwise subcomplexes, activity and organism viability.

- Cite Tripathi S6/Figure 4 and Meiringer sec13/Figure 3 for the Dsl1 bridge; do not cite only a domain-mutant growth phenotype.
- Do not infer identical requirements for Tip20/Sec39 or a universal in vivo absence phenotype.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dsl1_nzr_complex.yaml; Entire maintained record, including all evidence, components, graph, discussions and history | context_only | The complete maintained target was read; related structures are assessed only where this target names them. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, PresenceEnum and graph scope | context_only | Formation necessity differs from activity, recruitment into a larger assembly or viability. Where used, COMMON means present in most members with exceptional losses. This category is distinct from a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and REVIEWED_LABEL_ONLY contract | context_only | A family grounds the named protein class, while the taxon-paired accession is a representative instance. Exact class mappings can resolve a label-only task. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Graph evidence and scope | context_only | Composition, coarse functional chemistry and a detailed molecular mechanism are assessed separately. |
| root53-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000124,GO:0004843,GO:0005783,GO:0006890,GO:0030604,GO:0032991,GO:0046695,GO:0070939,GO:0071819,GO:0099023,GO:0140513,GO:1990065; All twelve term definitions, identity/status, synonyms, comments, source xrefs and relevant typed child links; relation types preserved | supports | The twelve active native terms establish the focal complex identities, declared parents, SAGA/SLIK boundaries, cellular locations and functions. GO0070939 has an unrelated acetolactate-synthase comment that the target does not import. GO0030604 specifies the reversible reductoisomerase reaction; its written reverse direction does not contradict forward NADPH consumption. |
| root53-sources-GO0070939-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939/ancestors?relations=is_a; Complete native ancestor response; no parthood inferred from ancestry | supports | The is_a-only ancestry includes vesicle tethering complex GO0099023. |
| root53-sources-GO0070939-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939/constraints; Focal taxonConstraints presence and complete array where present; inherited broad-term exclusions are not distribution evidence | context_only | The focal term has an only_in_taxon Eukaryota constraint; this is not a survey of occurrence. |
| root53-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA identifies 4932 as Saccharomyces cerevisiae. Species and reference-strain scopes remain distinct. |
| root53-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | ENA identifies 559292 as Saccharomyces cerevisiae S288C. Species and reference-strain scopes remain distinct. |
| root53-sources-pmid-11493604 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11493604+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 11493604: The coatomer-interacting protein Dsl1p is required for Golgi-to-endoplasmic reticulum retrieval in yeast. Authors Andag U, Neumann T, Schmitt HD.; year 2001; DOI 10.1074/jbc.m105833200. Complete abstract read; primary body scope is separately declared. |
| root53-sources-pmid-11739780 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11739780+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 11739780: Golgi-to-endoplasmic reticulum (ER) retrograde traffic in yeast requires Dsl1p, a component of the ER target site that interacts with a COPI coat subunit. Authors Reilly BA, Kraynack BA, VanRheenen SM, Waters MG.; year 2001; DOI 10.1091/mbc.12.12.3783. Complete abstract read; primary body scope is separately declared. |
| root53-sources-pmid-15958492 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15958492+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 15958492: Dsl1p, Tip20p, and the novel Dsl3(Sec39) protein are required for the stability of the Q/t-SNARE complex at the endoplasmic reticulum in yeast. Authors Kraynack BA, Chan A, Rosenthal E, Essid M, Umansky B, Waters MG, Schmitt HD.; year 2005; DOI 10.1091/mbc.e05-01-0056. Complete abstract read; primary body scope is separately declared. |
| root53-sources-pmid-8334998 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8334998+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact PMID/title/authors/year/DOI and entire abstractText | supports | MED 8334998: The TIP1 gene of Saccharomyces cerevisiae encodes an 80 kDa cytoplasmic protein that interacts with the cytoplasmic domain of Sec20p. Authors Sweet DJ, Pelham HR.; year 1993; DOI 10.1002/j.1460-2075.1993.tb05944.x. Complete abstract read; primary body scope is separately declared. |
| root53-sources-doi-10.1038_nsmb.1548 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnsmb.1548%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and entire abstractText | supports | The exact DOI resolves to MED 19151722, Structural characterization of Tip20p and Dsl1p, subunits of the Dsl1p vesicle tethering complex., Tripathi A, Ren Y, Jeffrey PD, Hughson FM. (2009). Its full abstract was read; fetching a body elsewhere does not imply full-body inspection. |
| root53-sources-doi-10.1074_jbc.M110.215327 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M110.215327%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and entire abstractText | supports | The exact DOI resolves to MED 21550981, The Dsl1 protein tethering complex is a resident endoplasmic reticulum complex, which interacts with five soluble NSF (N-ethylmaleimide-sensitive factor) attachment protein receptors (SNAREs): implications for fusion and fusion regulation., Meiringer CT, Rethmeier R, Auffarth K, Wilson J, Perz A, Barlowe C, Schmitt HD, Ungermann C. (2011). Its full abstract was read; fetching a body elsewhere does not imply full-body inspection. |
| root53-sources-doi-10.1091_mbc.e05-01-0056 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e05-01-0056%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and entire abstractText | supports | The exact DOI resolves to MED 15958492, Dsl1p, Tip20p, and the novel Dsl3(Sec39) protein are required for the stability of the Q/t-SNARE complex at the endoplasmic reticulum in yeast., Kraynack BA, Chan A, Rosenthal E, Essid M, Umansky B, Waters MG, Schmitt HD. (2005). Its full abstract was read; fetching a body elsewhere does not imply full-body inspection. |
| root53-sources-protein-P53847 | https://rest.uniprot.org/uniprotkb/P53847.json; Identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | P53847 is the reviewed DSL1 entry in taxon 559292. Native ER localization links cite PMID11493604 and PMID11739780. |
| root53-sources-gene-DSL1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 559292 returns the declared single accession P53847. |
| root53-sources-protein-P33891 | https://rest.uniprot.org/uniprotkb/P33891.json; Identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | P33891 is the reviewed TIP20 entry in taxon 559292. TIP1 is a declared alias; native ER localization cites PMID8334998. |
| root53-sources-gene-TIP20 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATIP20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 559292 returns the declared single accession P33891. |
| root53-sources-protein-Q12745 | https://rest.uniprot.org/uniprotkb/Q12745.json; Identity/status/recommended and alternative names, genes, organism; all InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments where present | supports | Q12745 is the reviewed SEC39 entry in taxon 559292. DSL3 is a declared alias of SEC39; native ER localization cites PMID15958492. |
| root53-sources-gene-SEC39 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC39%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 559292 returns the declared single accession Q12745. |
| root53-sources-gene-DSL3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Entire returned identity set; exact-gene plus organism_id and reviewed filter; size 500 | supports | The exact-gene reviewed query restricted to organism_id 559292 returns the declared single accession Q12745. |
| root53-sources-primary-PMC2635920 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2635920/; Tripathi 2009: complete Results S3-S7; Methods S10 protein production and S13 binding; all Figure 1-6 captions. Introduction, Discussion, crystallization/refinement methods, supplement and pixels not read. | supports | Recombinant Dsl1, Tip20 and Sec39 form a stoichiometric ternary complex, with Dsl1 linking the other two proteins. Tip20-Dsl1 binding is measured directly. Domain truncations and interface mutations disrupt specific interactions; some interface mutations lack an observed growth defect. SNARE contacts involve the tether but do not make every contacted SNARE a constituent of the three-protein core. |
| root53-sources-primary-PMC3137077 | https://pmc.ncbi.nlm.nih.gov/articles/PMC3137077/; Meiringer 2011: complete Experimental Procedures sec5-7, Results sec11-14 with Figure 1-4 captions, and Discussion sec15. Introduction, supplement strain table and pixels not read. | supports | ER microscopy and COPII budding assays support resident Dsl tether components, while SNAREs and other vesicle cargo behave differently. The paper distinguishes the tether from its larger SNARE-associated assembly; proposed cooperative fusion models are not direct resolution of every interaction. |
| root53-sources-ipr-IPR007528 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007528/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | RINT1/Tip20 is a whole-protein homologous family including the named yeast Tip20 class and animal/plant homologues. Separate protein P33891 verifies example membership; cross-taxon homologues do not make it a generic CATCHR domain. |
| root53-sources-ipr-IPR021875 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021875/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | Dsl1 N-terminal domain, not a whole-protein class identifier. |
| root53-sources-ipr-IPR021876 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021876/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | Dsl1 C-terminal domain, not a whole-protein class identifier. |
| root53-sources-ipr-IPR013244 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013244/; Native accession/name/type, complete descriptions and flags, hierarchy and integrated member signatures | supports | Sec39 domain also represented in larger homologous proteins, not an exact whole-protein yeast Sec39 class mapping. |
| schema-result | just validate data/structures/other/dsl1_nzr_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dsl1_nzr_complex.yaml |
| strict-result | just validate-strict data/structures/other/dsl1_nzr_complex.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dsl1_nzr_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dsl1_nzr_complex.yaml --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dsl1_nzr_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch53-20261022-kx679dvh/dsl1_nzr_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dsl1_nzr_complex.yaml; Complete focused native report | supports | data/structures/other/dsl1_nzr_complex.yaml  (GO:0070939)<br>  yeast_dsl1_er_tethering	dsl1_dsl1_nzr_subunit	COVERED	-&gt;dsl1_dsl1_nzr_subunit (UniProtKB:P53847)<br>  yeast_dsl1_er_tethering	tip20_dsl1_nzr_subunit	COVERED	-&gt;tip20_dsl1_nzr_subunit (UniProtKB:P33891)<br>  yeast_dsl1_er_tethering	sec39_dsl3_dsl1_nzr_subunit	COVERED	-&gt;sec39_dsl3_dsl1_nzr_subunit (UniProtKB:Q12745)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     3  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     3  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/dsl1_nzr_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/dsl1_nzr_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 16 collected target identifiers returned OK. PMID:11493604: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:11739780: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:15958492: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force.; PMID:8334998: UNREACHABLE; Exact native EuropePMC MED identifier/title/DOI independently read following the bulk eutils414 transport failure. Resolution is identifier identity only; separate primary-body/abstract evidence limits remain in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, atomic coordinates, sequence alignments or supplements were reanalyzed. Native protein annotation links and separately read primary text are distinct evidence tiers.
- Kraynack 2005 and the older localization studies remain native metadata/complete-abstract and annotation tiers. Their genuine bodies were not inspected in this review. The bounded family search verified Tip20 and rejected the inspected domains; it does not establish that no other exact Dsl1/Sec39 class exists.
- The Dsl1 formation finding is restricted to directly tested purified pairwise/ternary association. It does not independently establish a universal in vivo phenotype or formation necessities for all other subunits.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations as well as issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T062447Z-dsl1-nzr-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of Dsl1/NZR complex
started_at: '2026-10-22T06:03:20Z'
finished_at: '2026-10-22T06:24:47Z'
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
summary: Two minors resolve an available Tip20 family mapping and the directly demonstrated
  Dsl1 bridge requirement in purified ternary assembly. Exact tether identity, Sec39/Dsl3
  aliasing, three-protein composition, ER residence and coarse transport graph remain
  supported.
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
  - path: data/structures/other/dsl1_nzr_complex.yaml
    sha256: 409b4fadc71763d017e404c80cddc9aa152421baa38806ebd7f4d032d5ab25c0
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
- target_id: GO:0070939
  path: data/structures/other/dsl1_nzr_complex.yaml
  label: Dsl1/NZR complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target; native-source fields and primary
    reading scopes are declared in evidence. Scientific inputs remain unchanged.
  selection: One complete record in strict-path batch 53 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0070939
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0070939
  command: just validate data/structures/other/dsl1_nzr_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0070939
  command: just validate-strict data/structures/other/dsl1_nzr_complex.yaml --out
    /private/tmp/cellstructure-batch53-20261022-kx679dvh/dsl1_nzr_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0070939
  command: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dsl1_nzr_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0070939
  command: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dsl1_nzr_complex.yaml
  exit_code: 0
  summary: Focused check passed; source claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0070939
  summary: No expression-module or transcriptomic claim requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0070939
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root53-sources-go
  - root53-sources-GO0070939-ancestors
  - root53-sources-GO0070939-constraints
  - root53-sources-tax4932
  - root53-sources-tax559292
  - root53-sources-pmid-11493604
  - root53-sources-pmid-11739780
  - root53-sources-pmid-15958492
  - root53-sources-pmid-8334998
  - root53-sources-doi-10.1038_nsmb.1548
  - root53-sources-doi-10.1074_jbc.M110.215327
  - root53-sources-doi-10.1091_mbc.e05-01-0056
  - root53-sources-protein-P53847
  - root53-sources-gene-DSL1
  - root53-sources-protein-P33891
  - root53-sources-gene-TIP20
  - root53-sources-protein-Q12745
  - root53-sources-gene-SEC39
  - root53-sources-gene-DSL3
  - root53-sources-primary-PMC2635920
  - root53-sources-primary-PMC3137077
  - root53-sources-ipr-IPR007528
  - root53-sources-ipr-IPR021875
  - root53-sources-ipr-IPR021876
  - root53-sources-ipr-IPR013244
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0070939
  summary: '12 of 16 collected target identifiers returned OK. PMID:11493604: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:11739780: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:15958492: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:8334998: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force. Native source checks are
    separately scoped; skipped or unreachable identifiers are not silently counted
    as resolved.'
  evidence_ids:
  - target-curies
  - root53-sources-pmid-11493604
  - root53-sources-pmid-11739780
  - root53-sources-pmid-15958492
  - root53-sources-pmid-8334998
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0070939
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
  - GO:0070939
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
  - GO:0070939
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
  - GO:0070939
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
  - GO:0070939
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
  reference: data/structures/other/dsl1_nzr_complex.yaml
  locator: Entire maintained record, including all evidence, components, graph, discussions
    and history
  accessed_at: '2026-10-22T06:15:28Z'
  support: context_only
  summary: The complete maintained target was read; related structures are assessed
    only where this target names them.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, PresenceEnum and graph scope
  accessed_at: '2026-10-22T06:15:28Z'
  support: context_only
  summary: Formation necessity differs from activity, recruitment into a larger assembly
    or viability. Where used, COMMON means present in most members with exceptional
    losses. This category is distinct from a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and REVIEWED_LABEL_ONLY contract
  accessed_at: '2026-10-22T06:15:28Z'
  support: context_only
  summary: A family grounds the named protein class, while the taxon-paired accession
    is a representative instance. Exact class mappings can resolve a label-only task.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph evidence and scope
  accessed_at: '2026-10-22T06:15:28Z'
  support: context_only
  summary: Composition, coarse functional chemistry and a detailed molecular mechanism
    are assessed separately.
- evidence_id: root53-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000124,GO:0004843,GO:0005783,GO:0006890,GO:0030604,GO:0032991,GO:0046695,GO:0070939,GO:0071819,GO:0099023,GO:0140513,GO:1990065
  locator: All twelve term definitions, identity/status, synonyms, comments, source
    xrefs and relevant typed child links; relation types preserved
  accessed_at: '2026-10-22T06:06:00.951715Z'
  support: supports
  summary: The twelve active native terms establish the focal complex identities,
    declared parents, SAGA/SLIK boundaries, cellular locations and functions. GO0070939
    has an unrelated acetolactate-synthase comment that the target does not import.
    GO0030604 specifies the reversible reductoisomerase reaction; its written reverse
    direction does not contradict forward NADPH consumption.
  snapshot_sha256: 1ca0dac2d9f398d290817228e2290a52a1444cc9ebea6b8324d0a056c9cd4c84
- evidence_id: root53-sources-GO0070939-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939/ancestors?relations=is_a
  locator: Complete native ancestor response; no parthood inferred from ancestry
  accessed_at: '2026-10-22T06:06:07.995330Z'
  support: supports
  summary: The is_a-only ancestry includes vesicle tethering complex GO0099023.
  snapshot_sha256: a7fce74e35bc6ca1d05c98ed49a01d880de65a108211c83d2dac5b3e71535286
- evidence_id: root53-sources-GO0070939-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070939/constraints
  locator: Focal taxonConstraints presence and complete array where present; inherited
    broad-term exclusions are not distribution evidence
  accessed_at: '2026-10-22T06:06:08.008319Z'
  support: context_only
  summary: The focal term has an only_in_taxon Eukaryota constraint; this is not a
    survey of occurrence.
  snapshot_sha256: 8104aae88fa5bbcb62f782ec7f407424914aa626317ae59c385e9f9f98bcfcf1
- evidence_id: root53-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:06:01.933951Z'
  support: supports
  summary: ENA identifies 4932 as Saccharomyces cerevisiae. Species and reference-strain
    scopes remain distinct.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root53-sources-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T06:06:02.363688Z'
  support: supports
  summary: ENA identifies 559292 as Saccharomyces cerevisiae S288C. Species and reference-strain
    scopes remain distinct.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root53-sources-pmid-11493604
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11493604+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:02.526054Z'
  support: supports
  summary: 'MED 11493604: The coatomer-interacting protein Dsl1p is required for Golgi-to-endoplasmic
    reticulum retrieval in yeast. Authors Andag U, Neumann T, Schmitt HD.; year 2001;
    DOI 10.1074/jbc.m105833200. Complete abstract read; primary body scope is separately
    declared.'
  snapshot_sha256: ae3ff65bed904d673654f65c5a4441564f4b587e7424ce8902c72a8ce2938429
- evidence_id: root53-sources-pmid-11739780
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11739780+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:02.532775Z'
  support: supports
  summary: 'MED 11739780: Golgi-to-endoplasmic reticulum (ER) retrograde traffic in
    yeast requires Dsl1p, a component of the ER target site that interacts with a
    COPI coat subunit. Authors Reilly BA, Kraynack BA, VanRheenen SM, Waters MG.;
    year 2001; DOI 10.1091/mbc.12.12.3783. Complete abstract read; primary body scope
    is separately declared.'
  snapshot_sha256: ef70127ae9b9f7aa1fe50586eb130acaf86e94ae28069c9747f7f68b7d0be18a
- evidence_id: root53-sources-pmid-15958492
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15958492+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:03.166040Z'
  support: supports
  summary: 'MED 15958492: Dsl1p, Tip20p, and the novel Dsl3(Sec39) protein are required
    for the stability of the Q/t-SNARE complex at the endoplasmic reticulum in yeast.
    Authors Kraynack BA, Chan A, Rosenthal E, Essid M, Umansky B, Waters MG, Schmitt
    HD.; year 2005; DOI 10.1091/mbc.e05-01-0056. Complete abstract read; primary body
    scope is separately declared.'
  snapshot_sha256: 5a5776384751afc21d43813d55bda89701e172fd405ef531db3403753e288559
- evidence_id: root53-sources-pmid-8334998
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8334998+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact PMID/title/authors/year/DOI and entire abstractText
  accessed_at: '2026-10-22T06:06:03.694807Z'
  support: supports
  summary: 'MED 8334998: The TIP1 gene of Saccharomyces cerevisiae encodes an 80 kDa
    cytoplasmic protein that interacts with the cytoplasmic domain of Sec20p. Authors
    Sweet DJ, Pelham HR.; year 1993; DOI 10.1002/j.1460-2075.1993.tb05944.x. Complete
    abstract read; primary body scope is separately declared.'
  snapshot_sha256: f82dae046dd7e5ba1b446ac37f44301de6dd46c026b437a2db22586095643976
- evidence_id: root53-sources-doi-10.1038_nsmb.1548
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1038%2Fnsmb.1548%22+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and
    entire abstractText'
  accessed_at: '2026-10-22T06:06:00.952110Z'
  support: supports
  summary: The exact DOI resolves to MED 19151722, Structural characterization of
    Tip20p and Dsl1p, subunits of the Dsl1p vesicle tethering complex., Tripathi A,
    Ren Y, Jeffrey PD, Hughson FM. (2009). Its full abstract was read; fetching a
    body elsewhere does not imply full-body inspection.
  snapshot_sha256: 0c9d3cf04c4769e7b774480e5cc0cdb6c1de91b7fb4fc5af4d556dd7c4dc4072
- evidence_id: root53-sources-doi-10.1074_jbc.M110.215327
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1074%2Fjbc.M110.215327%22+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and
    entire abstractText'
  accessed_at: '2026-10-22T06:06:01.745227Z'
  support: supports
  summary: 'The exact DOI resolves to MED 21550981, The Dsl1 protein tethering complex
    is a resident endoplasmic reticulum complex, which interacts with five soluble
    NSF (N-ethylmaleimide-sensitive factor) attachment protein receptors (SNAREs):
    implications for fusion and fusion regulation., Meiringer CT, Rethmeier R, Auffarth
    K, Wilson J, Perz A, Barlowe C, Schmitt HD, Ungermann C. (2011). Its full abstract
    was read; fetching a body elsewhere does not imply full-body inspection.'
  snapshot_sha256: 27d75273cbb5ccf2546414ceccbd0c194c35b2c8cdb3af5bfae3d992124fc1da
- evidence_id: root53-sources-doi-10.1091_mbc.e05-01-0056
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091%2Fmbc.e05-01-0056%22+AND+SRC%3AMED&format=json&resultType=core
  locator: 'Unique native DOI result: title/authors/year, DOI/PMID/PMCID fields and
    entire abstractText'
  accessed_at: '2026-10-22T06:06:01.747932Z'
  support: supports
  summary: The exact DOI resolves to MED 15958492, Dsl1p, Tip20p, and the novel Dsl3(Sec39)
    protein are required for the stability of the Q/t-SNARE complex at the endoplasmic
    reticulum in yeast., Kraynack BA, Chan A, Rosenthal E, Essid M, Umansky B, Waters
    MG, Schmitt HD. (2005). Its full abstract was read; fetching a body elsewhere
    does not imply full-body inspection.
  snapshot_sha256: bb99734a7e2d84383677c1987cd31b41d12e86f44884be69790d37a8405b5941
- evidence_id: root53-sources-protein-P53847
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53847.json
  locator: Identity/status/recommended and alternative names, genes, organism; all
    InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:06:04.611024Z'
  support: supports
  summary: P53847 is the reviewed DSL1 entry in taxon 559292. Native ER localization
    links cite PMID11493604 and PMID11739780.
  snapshot_sha256: 1a5ab310843a1ace362d203aa58924fdd75bfd18eeeebafe8fdf2267c1799732
- evidence_id: root53-sources-gene-DSL1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:05.316200Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 559292 returns
    the declared single accession P53847.
  snapshot_sha256: dc74aeb59a47a0828e178dcdbcad9a3324ced8aab894b59ac922ef9f2b905c73
- evidence_id: root53-sources-protein-P33891
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33891.json
  locator: Identity/status/recommended and alternative names, genes, organism; all
    InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:06:03.824883Z'
  support: supports
  summary: P33891 is the reviewed TIP20 entry in taxon 559292. TIP1 is a declared
    alias; native ER localization cites PMID8334998.
  snapshot_sha256: 17fde0f47f341173ded9336df2821fdc5949d223d9ccfcb8401e39a424d925ea
- evidence_id: root53-sources-gene-TIP20
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ATIP20%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:06.903435Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 559292 returns
    the declared single accession P33891.
  snapshot_sha256: eaf60ba4b2cdb7e7f9cd38459d97de6c9db3cbf7763c81b62ea407f6ab52f734
- evidence_id: root53-sources-protein-Q12745
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12745.json
  locator: Identity/status/recommended and alternative names, genes, organism; all
    InterPro/NCBIfam/Pfam xrefs; complete FUNCTION/SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments where present
  accessed_at: '2026-10-22T06:06:04.959083Z'
  support: supports
  summary: Q12745 is the reviewed SEC39 entry in taxon 559292. DSL3 is a declared
    alias of SEC39; native ER localization cites PMID15958492.
  snapshot_sha256: c651ab454f0bc46e264fca6e399e679febd27fc8a67ce8bf795e266a715b01b2
- evidence_id: root53-sources-gene-SEC39
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ASEC39%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:05.693657Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 559292 returns
    the declared single accession Q12745.
  snapshot_sha256: 60fc3ef9ae7f2a89aa17c98b55a62ae07f979e012b80a78e1a21ebfeb920ef4d
- evidence_id: root53-sources-gene-DSL3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADSL3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Entire returned identity set; exact-gene plus organism_id and reviewed
    filter; size 500
  accessed_at: '2026-10-22T06:06:05.638392Z'
  support: supports
  summary: The exact-gene reviewed query restricted to organism_id 559292 returns
    the declared single accession Q12745.
  snapshot_sha256: 60fc3ef9ae7f2a89aa17c98b55a62ae07f979e012b80a78e1a21ebfeb920ef4d
- evidence_id: root53-sources-primary-PMC2635920
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2635920/
  locator: 'Tripathi 2009: complete Results S3-S7; Methods S10 protein production
    and S13 binding; all Figure 1-6 captions. Introduction, Discussion, crystallization/refinement
    methods, supplement and pixels not read.'
  accessed_at: '2026-10-22T06:07:06.671433Z'
  support: supports
  summary: Recombinant Dsl1, Tip20 and Sec39 form a stoichiometric ternary complex,
    with Dsl1 linking the other two proteins. Tip20-Dsl1 binding is measured directly.
    Domain truncations and interface mutations disrupt specific interactions; some
    interface mutations lack an observed growth defect. SNARE contacts involve the
    tether but do not make every contacted SNARE a constituent of the three-protein
    core.
  snapshot_sha256: 2e85d225f6334b04b985f06fb8e8ed7746aacddf97c569237c7a2641ea3dab6f
- evidence_id: root53-sources-primary-PMC3137077
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3137077/
  locator: 'Meiringer 2011: complete Experimental Procedures sec5-7, Results sec11-14
    with Figure 1-4 captions, and Discussion sec15. Introduction, supplement strain
    table and pixels not read.'
  accessed_at: '2026-10-22T06:07:06.671626Z'
  support: supports
  summary: ER microscopy and COPII budding assays support resident Dsl tether components,
    while SNAREs and other vesicle cargo behave differently. The paper distinguishes
    the tether from its larger SNARE-associated assembly; proposed cooperative fusion
    models are not direct resolution of every interaction.
  snapshot_sha256: fa22dd4d33757ade31127394accd08a7c487608d3fb686fd4682c01b783b4cc7
- evidence_id: root53-sources-ipr-IPR007528
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007528/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.162056Z'
  support: supports
  summary: RINT1/Tip20 is a whole-protein homologous family including the named yeast
    Tip20 class and animal/plant homologues. Separate protein P33891 verifies example
    membership; cross-taxon homologues do not make it a generic CATCHR domain.
  snapshot_sha256: 65941631edcc70f1e82f3beba6f3323cda1bdb7e20b53fc7880dcde43e26b795
- evidence_id: root53-sources-ipr-IPR021875
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021875/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.198592Z'
  support: supports
  summary: Dsl1 N-terminal domain, not a whole-protein class identifier.
  snapshot_sha256: 9da4a43e1a9eef1bc85656f706a703084666d19ed6fe9dd7518f115a2484e851
- evidence_id: root53-sources-ipr-IPR021876
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR021876/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.265505Z'
  support: supports
  summary: Dsl1 C-terminal domain, not a whole-protein class identifier.
  snapshot_sha256: eed5f734db9c4050435ed6cb8535ce9f93070c6fe1f91994ad5306e5b806e0fd
- evidence_id: root53-sources-ipr-IPR013244
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013244/
  locator: Native accession/name/type, complete descriptions and flags, hierarchy
    and integrated member signatures
  accessed_at: '2026-10-22T06:07:07.185833Z'
  support: supports
  summary: Sec39 domain also represented in larger homologous proteins, not an exact
    whole-protein yeast Sec39 class mapping.
  snapshot_sha256: e27da0c1dbbe835c548fccac3186b8e828f9915c474c876c2fa734a464603ecb
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dsl1_nzr_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:03:23Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dsl1_nzr_complex.yaml'
  snapshot_sha256: 964e4402ad3ac32df62ea00127a7b1f00ccfe651b3edc1e879b00ea48e4c4989
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dsl1_nzr_complex.yaml --out
    /private/tmp/cellstructure-batch53-20261022-kx679dvh/dsl1_nzr_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T06:03:25Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dsl1_nzr_complex.yaml\
    \ --out /private/tmp/cellstructure-batch53-20261022-kx679dvh/dsl1_nzr_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch53-20261022-kx679dvh/dsl1_nzr_complex-strict.tsv"
  snapshot_sha256: f5570e62cdcb7bd43f5acac454eb4a83cd2332d0231447a761ecaac019e04fb3
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dsl1_nzr_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:06:05.123359Z'
  support: supports
  summary: "data/structures/other/dsl1_nzr_complex.yaml  (GO:0070939)\n  yeast_dsl1_er_tethering\t\
    dsl1_dsl1_nzr_subunit\tCOVERED\t->dsl1_dsl1_nzr_subunit (UniProtKB:P53847)\n \
    \ yeast_dsl1_er_tethering\ttip20_dsl1_nzr_subunit\tCOVERED\t->tip20_dsl1_nzr_subunit\
    \ (UniProtKB:P33891)\n  yeast_dsl1_er_tethering\tsec39_dsl3_dsl1_nzr_subunit\t\
    COVERED\t->sec39_dsl3_dsl1_nzr_subunit (UniProtKB:Q12745)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     3  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     3  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 087c7ae1c1ed5570e68b1849441b8171b6fc5520408fe4812cd3c9d4cd6d205a
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch53-20261022-kx679dvh/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/dsl1_nzr_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T06:06:06.931915Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/dsl1_nzr_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '12 of 16 collected target identifiers returned OK. PMID:11493604: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:11739780: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:15958492: UNREACHABLE;
    Exact native EuropePMC MED identifier/title/DOI independently read following the
    bulk eutils414 transport failure. Resolution is identifier identity only; separate
    primary-body/abstract evidence limits remain in force.; PMID:8334998: UNREACHABLE;
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
  topic: Three-protein tether and larger interaction partners
  outcome: supported
  target_ids:
  - GO:0070939
  summary: Exact GO identity, tethering parent and synonym scopes match the maintained
    three-protein Dsl1/Tip20/Sec39 core. SEC39/DSL3 aliasing is supported. SNARE/COPI
    partners remain outside the declared constituent boundary.
  evidence_ids:
  - record
  - root53-sources-go
  - root53-sources-GO0070939-ancestors
  - root53-sources-primary-PMC2635920
  - root53-sources-primary-PMC3137077
  - root53-sources-doi-10.1038_nsmb.1548
  - root53-sources-doi-10.1074_jbc.M110.215327
  - root53-sources-doi-10.1091_mbc.e05-01-0056
  - root53-sources-protein-P53847
  - root53-sources-protein-P33891
  - root53-sources-protein-Q12745
- assessment_id: composition
  area: grounding
  topic: Correct protein examples and one actionable family
  outcome: concern
  target_ids:
  - GO:0070939
  summary: All three S288C examples and their gene/alias identities are correct. Tip20
    has an available full-protein homologous family; the inspected Dsl1 and Sec39
    entries are domains and are not substitutes for those whole proteins.
  evidence_ids:
  - record
  - root53-sources-primary-PMC2635920
  - root53-sources-ipr-IPR007528
  - root53-sources-ipr-IPR021875
  - root53-sources-ipr-IPR021876
  - root53-sources-ipr-IPR013244
  - root53-sources-protein-P53847
  - root53-sources-protein-P33891
  - root53-sources-protein-Q12745
  - root53-sources-gene-DSL1
  - root53-sources-gene-TIP20
  - root53-sources-gene-SEC39
  - root53-sources-gene-DSL3
- assessment_id: graph
  area: graph
  topic: ER-resident tether and transport function
  outcome: supported
  target_ids:
  - GO:0070939
  summary: The three membership edges, ER localization and Golgi-to-ER transport involvement
    are supported. NONMECHANISTIC scope appropriately excludes unresolved individual
    SNARE/COPI contacts and detailed fusion steps.
  evidence_ids:
  - record
  - graphs
  - root53-sources-go
  - root53-sources-primary-PMC2635920
  - root53-sources-primary-PMC3137077
- assessment_id: scope
  area: scope
  topic: Yeast experiments versus reference examples
  outcome: supported
  target_ids:
  - GO:0070939
  summary: The canonical and distribution statements concern the budding-yeast tether,
    not every eukaryotic CATCHR assembly. S288C reference entries do not identify
    every purified experimental strain; bacterial recombinant expression hosts are
    not the biological source of the yeast complex. COMMON is a qualitative curation
    assertion rather than a measured strain census.
  evidence_ids:
  - record
  - root53-sources-GO0070939-constraints
  - root53-sources-primary-PMC2635920
  - root53-sources-primary-PMC3137077
  - root53-sources-tax4932
  - root53-sources-tax559292
  - root53-sources-protein-P53847
  - root53-sources-protein-P33891
  - root53-sources-protein-Q12745
- assessment_id: formation
  area: grounding
  topic: Specific interaction requirements
  outcome: concern
  target_ids:
  - GO:0070939
  summary: Pairwise purified-protein assays show Sec39 binds Dsl1 but not Tip20, and
    combining the three produces a ternary complex. Thus Dsl1 supplies a demonstrated
    bridge for Tip20–Sec39 association under the reconstitution conditions. This specific
    assembly dependency can resolve the Dsl1 UNKNOWN with experimental scope preserved;
    it does not justify promoting all constituent requirements or equating assembly
    with cell viability.
  evidence_ids:
  - record
  - schema
  - root53-sources-primary-PMC2635920
  - root53-sources-primary-PMC3137077
- assessment_id: coverage
  area: completeness
  topic: Whole maintained record and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0070939
  summary: All maintained fields, evidence, component/example rows, graph edges, discussion
    entries and history were read. Available exact mappings are distinguished from
    optional enrichment and source-access limitations. Scientific status and provenance
    history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root53-sources-go
  - root53-sources-doi-10.1038_nsmb.1548
  - root53-sources-doi-10.1074_jbc.M110.215327
  - root53-sources-doi-10.1091_mbc.e05-01-0056
findings:
- finding_id: F1
  issue_key: dsl1-nzr-tip20-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the Tip20 family mapping
  description: Tip20 remains REVIEWED_LABEL_ONLY under an open three-subunit mapping
    task, but native IPR007528 is a whole-protein RINT1/Tip20 family and P33891 independently
    has that cross-reference. The inspected Dsl1/Sec39 domain identifiers do not resolve
    their whole-protein classes.
  target_ids:
  - GO:0070939
  field_paths:
  - components[1].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root53-sources-ipr-IPR007528
  - root53-sources-protein-P53847
  - root53-sources-protein-P33891
  - root53-sources-protein-Q12745
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
  rule_id: Exact protein class grounding
  native_severity: minor
  normalization_reason: Identity and supported composition remain intact; this is
    a bounded available class mapping that can resolve an existing task.
- finding_id: F2
  issue_key: dsl1-nzr-dsl1-reconstitution-formation-dependency
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Record the demonstrated Dsl1 assembly dependency
  description: 'Dsl1 essentiality remains UNKNOWN even though Tripathi Results S6/Figure
    4 and Meiringer Results sec13/Figure 3 directly compare pairwise interactions
    and three-protein reconstitution: Tip20 and Sec39/Dsl3 do not associate directly,
    while Dsl1 binds both and links the ternary complex. This establishes a specific
    formation dependency in the purified system, distinct from the separate domain-mutant
    and growth experiments.'
  target_ids:
  - GO:0070939
  field_paths:
  - components[0].essentiality
  - components[0].evidence
  evidence_ids:
  - record
  - schema
  - root53-sources-primary-PMC2635920
  - root53-sources-primary-PMC3137077
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
  rule_id: Formation necessity must follow a directly tested assembly dependency
  native_severity: minor
  normalization_reason: The correct complex identity and composition remain intact;
    a presently unknown component requirement is resolvable within an explicit purified-assay
    scope.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0070939
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
  description: Ground Tip20 with IPR007528 and narrow the open mapping task to genuinely
    unresolved whole-protein classes. Preserve source-scoped homologous-family identity
    and yeast examples.
  acceptance_checks:
  - Verify family type and exact example membership.
  - Do not substitute Dsl1 or Sec39 domain accessions for whole proteins.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0070939
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dsl1_nzr_complex.yaml
    role: maintained scientific record
  description: Curate Dsl1 formation necessity using the direct reconstitution and
    pairwise binding evidence, retaining the tested purified-system context in its
    supporting notes. Preserve the distinction between the ternary core, remaining
    pairwise subcomplexes, activity and organism viability.
  acceptance_checks:
  - Cite Tripathi S6/Figure 4 and Meiringer sec13/Figure 3 for the Dsl1 bridge; do
    not cite only a domain-mutant growth phenotype.
  - Do not infer identical requirements for Tip20/Sec39 or a universal in vivo absence
    phenotype.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, atomic coordinates, sequence alignments or supplements
  were reanalyzed. Native protein annotation links and separately read primary text
  are distinct evidence tiers.
- Kraynack 2005 and the older localization studies remain native metadata/complete-abstract
  and annotation tiers. Their genuine bodies were not inspected in this review. The
  bounded family search verified Tip20 and rejected the inspected domains; it does
  not establish that no other exact Dsl1/Sec39 class exists.
- The Dsl1 formation finding is restricted to directly tested purified pairwise/ternary
  association. It does not independently establish a universal in vivo phenotype or
  formation necessities for all other subunits.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations as well as issue-bearing
  reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
