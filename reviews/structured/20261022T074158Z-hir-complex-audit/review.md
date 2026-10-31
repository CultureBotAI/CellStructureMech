# Source-grounded review of HIR complex

- Review: 20261022T074158Z-hir-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T07:12:37Z
- Finished UTC: 2026-10-22T07:41:58Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

One minor finding resolves the Hir3 homolog family. The four-class HIR boundary, external Asf1 partnership, reference examples and replication-independent deposition function are supported.

## Scope And Provenance

Exactly one complete maintained target, with source-native and primary reading scopes declared individually.

Selection: One complete record in strict-path batch 57 of the explicit all-unreviewed-record goal.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000417 | data/structures/other/hir_complex.yaml | maintained | HIR complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000417 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000417 | Focused validator passed. |
| Native focused causal-graphs | passed | True | GO:0000417 | Focused check passed; scientific claims assessed separately. |
| Native focused verify | passed | True | GO:0000417 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0000417 | No iModulon-specific claim is assessed; the relevant complex/assay evidence was inspected directly. |
| Claim-level scientific review | passed | True | GO:0000417 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0000417 | 11 of 18 collected target identifiers returned OK. PMID:11782447: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:14562095: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:16303565: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:17180700: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:19683497: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:8417331: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:9671488: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0000417 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000417 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000417 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000417 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0000417 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Four HIR constituents and external Asf1 partner

identity: supported. Targets: GO:0000417.

Exact GO identity/synonym and protein-complex parent agree. Hir1/Hir2/Hir3/Hpc2 copurify at300mM KCl. The resolved boundary appropriately treats Asf1 as a cooperating partner; copurification and stimulation do not require adding it to the four-class HIR inventory.

### Resolved Hir3 class and explicitly broader candidates

grounding: concern. Targets: GO:0000417.

Hir3 has a verified whole-family homolog mapping. The inspected HIR1-like entry conflates Hir1/Hir2, and HRD is a shared domain; empty candidate-subfamily routes do not resolve those outstanding classes. No family absence is claimed beyond this bounded search.

### Conditional Hir3 recovery depends on Hpc2

grounding: supported. Targets: GO:0000417.

The maintained roles and membership graph are supported. Green additionally reports no Hir3 detected in Hir2 purifications after hpc2 deletion, with retained subcomplexes after other deletions. Association versus stability remains unresolved. This conditional recovery result is useful context, without demonstrating a material error in the stated inventory or universal constituent necessity. Asf1 recruitment and promoter binding remain separate readouts.

### Supported membership and replication-independent deposition

graph: supported. Targets: GO:0000417.

All four membership edges and the broad histone-deposition outcome are supported. EMSA and DNA-supercoiling assays distinguish HIR-alone activity under specified conditions from stronger combined HIR/Asf1 activity and CAF1-dependent replication-coupled assembly. The record correctly says cooperates without asserting absolute Asf1 dependence in every assay.

### Yeast experimental context and reference strains

scope: supported. Targets: GO:0000417.

The body/captions identify PKY strains and purification salt conditions; detailed genotypes and methods are delegated to unread supplements. S288C reference accessions do not identify all assay strains. COMMON retains the schema meaning present in most members with exceptional losses.

### Universal individual-constituent requirements remain unestablished

grounding: unknown. Targets: GO:0000417.

The bounded interaction, recruitment and activity results do not establish a universal per-constituent formation-necessity profile. UNKNOWN values are not automatically defects and are not converted to ESSENTIAL.

### Complete maintained target and bounded follow-up

completeness: supported. Targets: GO:0000417.

Every maintained field, evidence row, component/example, graph edge, discussion and history entry was read. Optional unpopulated slots are not defects. Scientific status/history remain unchanged.

## Findings

### F1: Resolve the Hir3 whole-family mapping

minor / open / confirmed; issue key: hir-resolve-hir3-family.

The open family task and Hir3 label-only row still defer a mapping despite verified IPR033053 Hir3/CABIN1 whole-family identity and the matching P47171 reference. Other HIR component boundaries remain unresolved by the inspected candidates.

## Recommended Actions And Acceptance Checks

### A1

Ground Hir3 in the verified homolog family and narrow the existing task to the unresolved component classes.

- Use IPR033053 with the fungal Hir3 reference example and the native homolog breadth stated.
- Do not use mixed HIR1/HIR2 IPR031120 or HRD domain IPR014840 as exact replacements for their named complete classes.
- Pass applicable native schema, strict, identifier and graph checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/hir_complex.yaml; Entire maintained target, including all components, evidence, graph edges, discussions and history | context_only | The complete target was read. The maintained YAML owns any later scientific correction. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope | context_only | Formation necessity is distinct from activity, localization and viability. COMMON is the qualitative category present in most members with exceptional losses, not a measured prevalence census. |
| curation | docs/CURATION.md; Exact class identity and taxon-paired protein examples | context_only | Protein examples do not replace constituent-class grounding. Shared domains and broader paralog families do not resolve exact class tasks. |
| graphs | .claude/skills/curate-causal-graphs/SKILL.md; Scope and edge-level source support | context_only | Descriptive membership graphs need not assert a complete mechanism; a directly observed conditional physical dependency can be stated without making every constituent universally essential. |
| root57-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000118,GO:0000417,GO:0000785,GO:0004407,GO:0006334,GO:0032297,GO:0032991,GO:0044775,GO:0070823,GO:1990078,GO:1990083,GO:1990085; Native identities, status, complete definitions/comments/synonyms and focal typed relationships | supports | The twelve inspected terms establish the focal HDA1, Hda-beta and HIR identities, their parent classes and the named function/substructure targets. Only relevant typed relations were used. |
| root57-sources-GO0000417-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000417/ancestors?relations=is_a; Complete native is_a ancestor response | supports | The complete is_a-only ancestry supports the declared parent class. It does not establish parthood or taxonomic frequency. |
| root57-sources-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | Native taxId 4932 identifies Saccharomyces cerevisiae; broad taxon, species and reference strain are kept distinct. |
| root57-sources-tax-559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | Native taxId 559292 identifies Saccharomyces cerevisiae S288C; broad taxon, species and reference strain are kept distinct. |
| root57-sources-pmid-11782447 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11782447+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 11782447: Chromatin assembly factor I and Hir proteins contribute to building functional kinetochores in S. cerevisiae. Sharp JA, Franco AA, Osley MA, Kaufman PD. (2002); DOI 10.1101/gad.925302. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 14562095: Global analysis of protein localization in budding yeast. Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O'Shea EK. (2003); DOI 10.1038/nature02026. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-16303565 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16303565+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 16303565: Replication-independent histone deposition by the HIR complex and Asf1. Green EM, Antczak AJ, Bailey AO, Franco AA, Wu KJ, Yates JR, Kaufman PD. (2005); DOI 10.1016/j.cub.2005.10.053. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-17180700 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17180700+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 17180700: The histone chaperone Asf1 at the crossroads of chromatin and DNA checkpoint pathways. Mousson F, Ochsenbein F, Mann C. (2007); DOI 10.1007/s00412-006-0087-z. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-19683497 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19683497+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 19683497: Two-color cell array screen reveals interdependent roles for histone chaperones and a chromatin boundary regulator in histone gene repression. Fillingham J, Kainth P, Lambert JP, van Bakel H, Tsui K, Peña-Castillo L, Nislow C, Figeys D, Hughes TR, Greenblatt J, Andrews BJ. (2009); DOI 10.1016/j.molcel.2009.06.023. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-8417331 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8417331+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 8417331: Characterization of HIR1 and HIR2, two genes required for regulation of histone gene transcription in Saccharomyces cerevisiae. Sherwood PW, Tsang SV, Osley MA. (1993); DOI 10.1128/mcb.13.1.28-38.1993. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-pmid-9671488 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9671488+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI/PMCID and full abstractText | supports | MED 9671488: Yeast Ty1 retrotransposition is stimulated by a synergistic interaction between mutations in chromatin assembly factor I and histone regulatory proteins. Qian Z, Huang H, Hong JY, Burck CL, Johnston SD, Berman J, Carol A, Liebman SW. (1998); DOI 10.1128/mcb.18.8.4783. Entire native abstract read; this evidence row does not claim the paper body. |
| root57-sources-doi-10.1007_s00412-006-0087-z | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00412-006-0087-z%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 17180700: The histone chaperone Asf1 at the crossroads of chromatin and DNA checkpoint pathways. Mousson F, Ochsenbein F, Mann C. (2007). Complete abstract read; body evidence is separately located. |
| root57-sources-doi-10.1016_j.cub.2005.10.053 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2005.10.053%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Unique DOI/PMID/title/authors/year/PMCID and entire abstractText | supports | Unique DOI result MED 16303565: Replication-independent histone deposition by the HIR complex and Asf1. Green EM, Antczak AJ, Bailey AO, Franco AA, Wu KJ, Yates JR, Kaufman PD. (2005). Complete abstract read; body evidence is separately located. |
| root57-sources-protein-P32479 | https://rest.uniprot.org/uniprotkb/P32479.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | P32479 is the reviewed HIR1 reference in taxon 559292. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-HIR1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly P32479. |
| root57-sources-protein-P32480 | https://rest.uniprot.org/uniprotkb/P32480.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | P32480 is the reviewed HIR2 reference in taxon 559292. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-HIR2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly P32480. |
| root57-sources-protein-P47171 | https://rest.uniprot.org/uniprotkb/P47171.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | P47171 is the reviewed HIR3 reference in taxon 559292. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-HIR3 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly P47171. |
| root57-sources-protein-Q01448 | https://rest.uniprot.org/uniprotkb/Q01448.json; Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references; complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY and MISCELLANEOUS comments where present | supports | Q01448 is the reviewed HPC2 reference in taxon 559292. Native names/aliases, organism, family cross-references and annotations support the stated identity. Its localization evidence tags were checked directly; this does not imply primary-body inspection of every cited localization assay. |
| root57-sources-gene-HPC2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHPC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=500; Complete returned identity set and literal query parameters | supports | The exact gene and organism query, restricted to reviewed entries, returns exactly Q01448. |
| root57-sources-ipr-IPR033053 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033053/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | The whole Hir3/CABIN1 family spans fungal Hir3 and its animal homolog; this is a homologous protein-class mapping, not a claim of identical complex roles in every lineage. |
| root57-sources-ipr-IPR031120 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031120/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | The HIR1-like family explicitly contains yeast HIR1 and HIR2 plus animal HIRA. It does not distinguish the two named yeast paralogs. |
| root57-sources-ipr-IPR014840 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014840/; Native accession/name/type, complete description with curation flags, integrated signatures and hierarchy | supports | The Hpc2-related/ubinuclein signature is a domain and does not independently identify the complete Hpc2 class. |
| access-panther-PTHR13831-SF0 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR13831:SF0/; Retrieved response status/content type and diagnostic body only | context_only | The reference-protein-linked candidate subfamily route returned HTTP204 and no response body; this route does not independently resolve an exact Hir1/Hir2 class boundary. |
| access-panther-PTHR13831-SF1 | https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR13831:SF1/; Retrieved response status/content type and diagnostic body only | context_only | The reference-protein-linked candidate subfamily route returned HTTP204 and no response body; this route does not independently resolve an exact Hir1/Hir2 class boundary. |
| root57-sources-PMC2819815-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC2819815/; Entire Results/Discussion S2–S6, including Figures1–4 captions, and the S7 Experimental Procedures pointer; supplementary methods/figures were not read | supports | Green2005 establishes the four-protein HIR complex and its cooperation with Asf1. Hir2 purifications retain partners after hir1 or hir3 deletion, while Hir3 is not detected by mass spectrometry after hpc2 deletion. The authors leave reduced association versus reduced stability unresolved. Histone-deposition assays separately demonstrate replication-independent activity and stimulation with Asf1. |
| schema-result | just validate data/structures/other/hir_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/hir_complex.yaml |
| strict-result | just validate-strict data/structures/other/hir_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hir_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/hir_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hir_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hir_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml --causal-graphs; Complete focused native report | supports | data/structures/other/hir_complex.yaml  (GO:0000417)<br>  yeast_hir_nucleosome_assembly	hir1_hir_subunit	COVERED	-&gt;hir1_hir_subunit (UniProtKB:P32479)<br>  yeast_hir_nucleosome_assembly	hir2_hir_subunit	COVERED	-&gt;hir2_hir_subunit (UniProtKB:P32480)<br>  yeast_hir_nucleosome_assembly	hir3_hir_subunit	COVERED	-&gt;hir3_hir_subunit (UniProtKB:P47171)<br>  yeast_hir_nucleosome_assembly	hpc2_hir_subunit	COVERED	-&gt;hpc2_hir_subunit (UniProtKB:Q01448)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml --verify; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/hir_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 18 collected target identifiers returned OK. PMID:11782447: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:14562095: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:16303565: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:17180700: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:19683497: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:8417331: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read.; PMID:9671488: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver is not treated as identifier invalidity or as proof that its primary body was read. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five same-base batch26 corpus gates and exact target resolver rows are integrated with every manifested input hash verified.
- No figure pixels, atomic coordinates, raw assay datasets or sequence alignments were reanalyzed. Primary body reading is limited to the explicitly named sections and embedded captions.
- Any absence finding is confined to the complete inspected target and its existing task; bounded native family queries do not establish absence from all databases.
- Protein localization source notes match native annotation provenance. Except where explicitly described, the cited localization papers were read at abstract tier; their detailed assays were not independently rechecked.
- Green delegates all detailed Experimental Procedures to supplementary material, which was not inspected. S3B physical-recovery conclusions were read in the main Results text, not independently confirmed from supplemental gel pixels or raw mass spectra.
- Mousson2007 and the localization papers were read at complete native abstract tier. No fixed HIR stoichiometry is inferred from copurification or secondary annotation.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes clean observations and issue-bearing reviews alike.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Materiality reassessment removed an optional association-detail omission finding; the source observation remains explicitly assessed and universal formation necessity remains unknown.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T074158Z-hir-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-grounded review of HIR complex
started_at: '2026-10-22T07:12:37Z'
finished_at: '2026-10-22T07:41:58Z'
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
summary: One minor finding resolves the Hir3 homolog family. The four-class HIR boundary,
  external Asf1 partnership, reference examples and replication-independent deposition
  function are supported.
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
  - path: data/structures/other/hir_complex.yaml
    sha256: 8875028f235995bd024fa461075f1ff3053824ea228ba8565d2ccad03bb9fb52
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
- target_id: GO:0000417
  path: data/structures/other/hir_complex.yaml
  label: HIR complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hir_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, with source-native and primary
    reading scopes declared individually.
  selection: One complete record in strict-path batch 57 of the explicit all-unreviewed-record
    goal.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000417
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: just validate data/structures/other/hir_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: just validate-strict data/structures/other/hir_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hir_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native focused causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml --causal-graphs
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native focused verify
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml --verify
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0000417
  summary: No iModulon-specific claim is assessed; the relevant complex/assay evidence
    was inspected directly.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000417
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graphs
  - root57-sources-go
  - root57-sources-GO0000417-ancestors
  - root57-sources-tax-4932
  - root57-sources-tax-559292
  - root57-sources-pmid-11782447
  - root57-sources-pmid-14562095
  - root57-sources-pmid-16303565
  - root57-sources-pmid-17180700
  - root57-sources-pmid-19683497
  - root57-sources-pmid-8417331
  - root57-sources-pmid-9671488
  - root57-sources-doi-10.1007_s00412-006-0087-z
  - root57-sources-doi-10.1016_j.cub.2005.10.053
  - root57-sources-protein-P32479
  - root57-sources-gene-HIR1
  - root57-sources-protein-P32480
  - root57-sources-gene-HIR2
  - root57-sources-protein-P47171
  - root57-sources-gene-HIR3
  - root57-sources-protein-Q01448
  - root57-sources-gene-HPC2
  - root57-sources-ipr-IPR033053
  - root57-sources-ipr-IPR031120
  - root57-sources-ipr-IPR014840
  - access-panther-PTHR13831-SF0
  - access-panther-PTHR13831-SF1
  - root57-sources-PMC2819815-html
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0000417
  summary: '11 of 18 collected target identifiers returned OK. PMID:11782447: UNREACHABLE;
    Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport
    failure in the corpus resolver is not treated as identifier invalidity or as proof
    that its primary body was read.; PMID:14562095: UNREACHABLE; Unique native MED
    identity, exact PMID/title/DOI and bibliography inspected; transport failure in
    the corpus resolver is not treated as identifier invalidity or as proof that its
    primary body was read.; PMID:16303565: UNREACHABLE; Unique native MED identity,
    exact PMID/title/DOI and bibliography inspected; transport failure in the corpus
    resolver is not treated as identifier invalidity or as proof that its primary
    body was read.; PMID:17180700: UNREACHABLE; Unique native MED identity, exact
    PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver
    is not treated as identifier invalidity or as proof that its primary body was
    read.; PMID:19683497: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI
    and bibliography inspected; transport failure in the corpus resolver is not treated
    as identifier invalidity or as proof that its primary body was read.; PMID:8417331:
    UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography
    inspected; transport failure in the corpus resolver is not treated as identifier
    invalidity or as proof that its primary body was read.; PMID:9671488: UNREACHABLE;
    Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport
    failure in the corpus resolver is not treated as identifier invalidity or as proof
    that its primary body was read. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root57-sources-pmid-11782447
  - root57-sources-pmid-14562095
  - root57-sources-pmid-16303565
  - root57-sources-doi-10.1016_j.cub.2005.10.053
  - root57-sources-pmid-17180700
  - root57-sources-doi-10.1007_s00412-006-0087-z
  - root57-sources-pmid-19683497
  - root57-sources-pmid-8417331
  - root57-sources-pmid-9671488
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0000417
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0000417
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
    and current batch57 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/hir_complex.yaml
  locator: Entire maintained target, including all components, evidence, graph edges,
    discussions and history
  accessed_at: '2026-10-22T07:22:39Z'
  support: context_only
  summary: The complete target was read. The maintained YAML owns any later scientific
    correction.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: EssentialityEnum, PresenceEnum, StructuralComponent and causal-graph scope
  accessed_at: '2026-10-22T07:22:39Z'
  support: context_only
  summary: Formation necessity is distinct from activity, localization and viability.
    COMMON is the qualitative category present in most members with exceptional losses,
    not a measured prevalence census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact class identity and taxon-paired protein examples
  accessed_at: '2026-10-22T07:22:39Z'
  support: context_only
  summary: Protein examples do not replace constituent-class grounding. Shared domains
    and broader paralog families do not resolve exact class tasks.
- evidence_id: graphs
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Scope and edge-level source support
  accessed_at: '2026-10-22T07:22:39Z'
  support: context_only
  summary: Descriptive membership graphs need not assert a complete mechanism; a directly
    observed conditional physical dependency can be stated without making every constituent
    universally essential.
- evidence_id: root57-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000118,GO:0000417,GO:0000785,GO:0004407,GO:0006334,GO:0032297,GO:0032991,GO:0044775,GO:0070823,GO:1990078,GO:1990083,GO:1990085
  locator: Native identities, status, complete definitions/comments/synonyms and focal
    typed relationships
  accessed_at: '2026-10-22T07:09:06.769100Z'
  support: supports
  summary: The twelve inspected terms establish the focal HDA1, Hda-beta and HIR identities,
    their parent classes and the named function/substructure targets. Only relevant
    typed relations were used.
  snapshot_sha256: 21ed713180a84eeed2230337bf1f89ecd5489141f8030b26157ee5ec18456ad0
- evidence_id: root57-sources-GO0000417-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000417/ancestors?relations=is_a
  locator: Complete native is_a ancestor response
  accessed_at: '2026-10-22T07:09:21.078617Z'
  support: supports
  summary: The complete is_a-only ancestry supports the declared parent class. It
    does not establish parthood or taxonomic frequency.
  snapshot_sha256: e03bcdf4ed65c98e31ecfec94bda2aed0113ee595c088d03657013e660b46594
- evidence_id: root57-sources-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T07:09:06.769364Z'
  support: supports
  summary: Native taxId 4932 identifies Saccharomyces cerevisiae; broad taxon, species
    and reference strain are kept distinct.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root57-sources-tax-559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T07:09:07.391453Z'
  support: supports
  summary: Native taxId 559292 identifies Saccharomyces cerevisiae S288C; broad taxon,
    species and reference strain are kept distinct.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root57-sources-pmid-11782447
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11782447+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:12.274750Z'
  support: supports
  summary: 'MED 11782447: Chromatin assembly factor I and Hir proteins contribute
    to building functional kinetochores in S. cerevisiae. Sharp JA, Franco AA, Osley
    MA, Kaufman PD. (2002); DOI 10.1101/gad.925302. Entire native abstract read; this
    evidence row does not claim the paper body.'
  snapshot_sha256: 79873e790cb7690fb5b2977cf028d6752a947d0f0f95ee4cd20fb68181cecf34
- evidence_id: root57-sources-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:12.881913Z'
  support: supports
  summary: 'MED 14562095: Global analysis of protein localization in budding yeast.
    Huh WK, Falvo JV, Gerke LC, Carroll AS, Howson RW, Weissman JS, O''Shea EK. (2003);
    DOI 10.1038/nature02026. Entire native abstract read; this evidence row does not
    claim the paper body.'
  snapshot_sha256: 571f7249c52d66a3b53ae05fa04cfe3012ab729c63308d338c745e9f3c1daa72
- evidence_id: root57-sources-pmid-16303565
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A16303565+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:13.486528Z'
  support: supports
  summary: 'MED 16303565: Replication-independent histone deposition by the HIR complex
    and Asf1. Green EM, Antczak AJ, Bailey AO, Franco AA, Wu KJ, Yates JR, Kaufman
    PD. (2005); DOI 10.1016/j.cub.2005.10.053. Entire native abstract read; this evidence
    row does not claim the paper body.'
  snapshot_sha256: b4d09d381d0bc4d39796e4d6fd2d947339f49ac28d86a70e15713cda6f821e39
- evidence_id: root57-sources-pmid-17180700
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A17180700+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:13.746518Z'
  support: supports
  summary: 'MED 17180700: The histone chaperone Asf1 at the crossroads of chromatin
    and DNA checkpoint pathways. Mousson F, Ochsenbein F, Mann C. (2007); DOI 10.1007/s00412-006-0087-z.
    Entire native abstract read; this evidence row does not claim the paper body.'
  snapshot_sha256: 764ff686c414c27f5454b635a1e43323267ea9a5bf1c11cbf9d59afa5569ec97
- evidence_id: root57-sources-pmid-19683497
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A19683497+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:14.107203Z'
  support: supports
  summary: 'MED 19683497: Two-color cell array screen reveals interdependent roles
    for histone chaperones and a chromatin boundary regulator in histone gene repression.
    Fillingham J, Kainth P, Lambert JP, van Bakel H, Tsui K, Peña-Castillo L, Nislow
    C, Figeys D, Hughes TR, Greenblatt J, Andrews BJ. (2009); DOI 10.1016/j.molcel.2009.06.023.
    Entire native abstract read; this evidence row does not claim the paper body.'
  snapshot_sha256: db8b0d4d68da2bf1b3f5fb1d307a6e9595386814d184feb3aab5cd25de3721c6
- evidence_id: root57-sources-pmid-8417331
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8417331+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:14.735650Z'
  support: supports
  summary: 'MED 8417331: Characterization of HIR1 and HIR2, two genes required for
    regulation of histone gene transcription in Saccharomyces cerevisiae. Sherwood
    PW, Tsang SV, Osley MA. (1993); DOI 10.1128/mcb.13.1.28-38.1993. Entire native
    abstract read; this evidence row does not claim the paper body.'
  snapshot_sha256: f3eecde707fa65ad2322d6f1d1f1ca99563c7ab3da21fe14ea017043ee4133d9
- evidence_id: root57-sources-pmid-9671488
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9671488+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI/PMCID and full abstractText
  accessed_at: '2026-10-22T07:09:15.369410Z'
  support: supports
  summary: 'MED 9671488: Yeast Ty1 retrotransposition is stimulated by a synergistic
    interaction between mutations in chromatin assembly factor I and histone regulatory
    proteins. Qian Z, Huang H, Hong JY, Burck CL, Johnston SD, Berman J, Carol A,
    Liebman SW. (1998); DOI 10.1128/mcb.18.8.4783. Entire native abstract read; this
    evidence row does not claim the paper body.'
  snapshot_sha256: 7ccde244d483900735d011737d26921182f9fa56e3a29847644629934c20e0a2
- evidence_id: root57-sources-doi-10.1007_s00412-006-0087-z
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2Fs00412-006-0087-z%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T07:09:15.992461Z'
  support: supports
  summary: 'Unique DOI result MED 17180700: The histone chaperone Asf1 at the crossroads
    of chromatin and DNA checkpoint pathways. Mousson F, Ochsenbein F, Mann C. (2007).
    Complete abstract read; body evidence is separately located.'
  snapshot_sha256: 6eab0e7967236c19613ff9152b852a3609802150fe6d17ba4dc42521190a776d
- evidence_id: root57-sources-doi-10.1016_j.cub.2005.10.053
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2005.10.053%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Unique DOI/PMID/title/authors/year/PMCID and entire abstractText
  accessed_at: '2026-10-22T07:09:16.266978Z'
  support: supports
  summary: 'Unique DOI result MED 16303565: Replication-independent histone deposition
    by the HIR complex and Asf1. Green EM, Antczak AJ, Bailey AO, Franco AA, Wu KJ,
    Yates JR, Kaufman PD. (2005). Complete abstract read; body evidence is separately
    located.'
  snapshot_sha256: 27748b216e337eb7bfdbcd7f92c22990a8c00df1f9fbdb6c1b1102800d5634a3
- evidence_id: root57-sources-protein-P32479
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32479.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:08.622500Z'
  support: supports
  summary: P32479 is the reviewed HIR1 reference in taxon 559292. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: 10d8bcab99dd0a21e475c5d92360d1c1c7c61c979e35853b574817bf6abd9133
- evidence_id: root57-sources-gene-HIR1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:21.473136Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly P32479.
  snapshot_sha256: b8becf3976e1f00de83f4e6604230c41697be4249efab0531814d582154e365b
- evidence_id: root57-sources-protein-P32480
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P32480.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:09.019543Z'
  support: supports
  summary: P32480 is the reviewed HIR2 reference in taxon 559292. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: de54c92c878715d9d470fd56aab5a40c071883afef647b5345aba49683ac0a97
- evidence_id: root57-sources-gene-HIR2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:21.767757Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly P32480.
  snapshot_sha256: fa8be3811c9b11dbf4f1be47c71d43cfeead5bbf1abe3b1c118f7b2aa1c72532
- evidence_id: root57-sources-protein-P47171
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P47171.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:09.504824Z'
  support: supports
  summary: P47171 is the reviewed HIR3 reference in taxon 559292. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: 0f569604566cce006a0e23abbf49142baca7c2aee06f2ba2684a54faea42d5bc
- evidence_id: root57-sources-gene-HIR3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHIR3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:22.373929Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly P47171.
  snapshot_sha256: dbe73ca7bf8c6a1501d5fe1ee520ea140e4a253a8c3d705ed9cac3ce57dbd78e
- evidence_id: root57-sources-protein-Q01448
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q01448.json
  locator: Identity/status/names, genes/aliases, organism, InterPro/PANTHER/Pfam cross-references;
    complete FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, CATALYTIC ACTIVITY, SIMILARITY
    and MISCELLANEOUS comments where present
  accessed_at: '2026-10-22T07:09:10.759596Z'
  support: supports
  summary: Q01448 is the reviewed HPC2 reference in taxon 559292. Native names/aliases,
    organism, family cross-references and annotations support the stated identity.
    Its localization evidence tags were checked directly; this does not imply primary-body
    inspection of every cited localization assay.
  snapshot_sha256: 7900b37c1697ed20e978396642a8a655d15283360f44ffec2869ebaaaa3454c6
- evidence_id: root57-sources-gene-HPC2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AHPC2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=500
  locator: Complete returned identity set and literal query parameters
  accessed_at: '2026-10-22T07:09:22.788276Z'
  support: supports
  summary: The exact gene and organism query, restricted to reviewed entries, returns
    exactly Q01448.
  snapshot_sha256: a2c8295ce6a030c468706b34f9ea4c5e8d29fa57c2e624dc089f03583ac65586
- evidence_id: root57-sources-ipr-IPR033053
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR033053/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:54.229099Z'
  support: supports
  summary: The whole Hir3/CABIN1 family spans fungal Hir3 and its animal homolog;
    this is a homologous protein-class mapping, not a claim of identical complex roles
    in every lineage.
  snapshot_sha256: e3476a156c99f54de4db23f4815334b3faa11da85cc74bcff357aac18b8030c4
- evidence_id: root57-sources-ipr-IPR031120
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR031120/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:53.373103Z'
  support: supports
  summary: The HIR1-like family explicitly contains yeast HIR1 and HIR2 plus animal
    HIRA. It does not distinguish the two named yeast paralogs.
  snapshot_sha256: 8c7b01a95abd1f366529f1da46ab474ec3f486dd764c76e68ff45cc18172e5cb
- evidence_id: root57-sources-ipr-IPR014840
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014840/
  locator: Native accession/name/type, complete description with curation flags, integrated
    signatures and hierarchy
  accessed_at: '2026-10-22T07:12:54.311339Z'
  support: supports
  summary: The Hpc2-related/ubinuclein signature is a domain and does not independently
    identify the complete Hpc2 class.
  snapshot_sha256: 55a74a6761e80bc88bcd10dd75e5c1cc15a68b11d71131aeb4d38e697839f626
- evidence_id: access-panther-PTHR13831-SF0
  kind: primary_source
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR13831:SF0/
  locator: Retrieved response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:18:52.670592Z'
  support: context_only
  summary: The reference-protein-linked candidate subfamily route returned HTTP204
    and no response body; this route does not independently resolve an exact Hir1/Hir2
    class boundary.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: access-panther-PTHR13831-SF1
  kind: primary_source
  reference: https://www.ebi.ac.uk/interpro/api/entry/panther/PTHR13831:SF1/
  locator: Retrieved response status/content type and diagnostic body only
  accessed_at: '2026-10-22T07:18:53.270390Z'
  support: context_only
  summary: The reference-protein-linked candidate subfamily route returned HTTP204
    and no response body; this route does not independently resolve an exact Hir1/Hir2
    class boundary.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: root57-sources-PMC2819815-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2819815/
  locator: Entire Results/Discussion S2–S6, including Figures1–4 captions, and the
    S7 Experimental Procedures pointer; supplementary methods/figures were not read
  accessed_at: '2026-10-22T07:12:55.632928Z'
  support: supports
  summary: Green2005 establishes the four-protein HIR complex and its cooperation
    with Asf1. Hir2 purifications retain partners after hir1 or hir3 deletion, while
    Hir3 is not detected by mass spectrometry after hpc2 deletion. The authors leave
    reduced association versus reduced stability unresolved. Histone-deposition assays
    separately demonstrate replication-independent activity and stimulation with Asf1.
  snapshot_sha256: a1c6555973ddaacc1e5b588093fa4f8d18643fa1630881ca2ce96106c4ab0402
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/hir_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:12:39Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/hir_complex.yaml'
  snapshot_sha256: b7711b7af5c5a08c60a6d7a61003e2633d39db4806ce9f6cd206776068d5965b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/hir_complex.yaml --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hir_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T07:12:41Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/hir_complex.yaml\
    \ --out /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hir_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch57-20261022-84r2nmpm/hir_complex-strict.tsv"
  snapshot_sha256: 726f62e8d2bbbc4e5c0fbe0a6afbcc255dd145c1bf815079f752836024bf9d69
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml --causal-graphs
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:17:33.961157Z'
  support: supports
  summary: "data/structures/other/hir_complex.yaml  (GO:0000417)\n  yeast_hir_nucleosome_assembly\t\
    hir1_hir_subunit\tCOVERED\t->hir1_hir_subunit (UniProtKB:P32479)\n  yeast_hir_nucleosome_assembly\t\
    hir2_hir_subunit\tCOVERED\t->hir2_hir_subunit (UniProtKB:P32480)\n  yeast_hir_nucleosome_assembly\t\
    hir3_hir_subunit\tCOVERED\t->hir3_hir_subunit (UniProtKB:P47171)\n  yeast_hir_nucleosome_assembly\t\
    hpc2_hir_subunit\tCOVERED\t->hpc2_hir_subunit (UniProtKB:Q01448)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     4  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     4  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: 96856c000b7ea9ca08297600191ff88679229c41cc7e4bad485dc9450ca1081d
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch57-20261022-84r2nmpm/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/hir_complex.yaml --verify
  locator: Complete focused native report
  accessed_at: '2026-10-22T07:17:35.220274Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/hir_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 18 collected target identifiers returned OK. PMID:11782447: UNREACHABLE;
    Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport
    failure in the corpus resolver is not treated as identifier invalidity or as proof
    that its primary body was read.; PMID:14562095: UNREACHABLE; Unique native MED
    identity, exact PMID/title/DOI and bibliography inspected; transport failure in
    the corpus resolver is not treated as identifier invalidity or as proof that its
    primary body was read.; PMID:16303565: UNREACHABLE; Unique native MED identity,
    exact PMID/title/DOI and bibliography inspected; transport failure in the corpus
    resolver is not treated as identifier invalidity or as proof that its primary
    body was read.; PMID:17180700: UNREACHABLE; Unique native MED identity, exact
    PMID/title/DOI and bibliography inspected; transport failure in the corpus resolver
    is not treated as identifier invalidity or as proof that its primary body was
    read.; PMID:19683497: UNREACHABLE; Unique native MED identity, exact PMID/title/DOI
    and bibliography inspected; transport failure in the corpus resolver is not treated
    as identifier invalidity or as proof that its primary body was read.; PMID:8417331:
    UNREACHABLE; Unique native MED identity, exact PMID/title/DOI and bibliography
    inspected; transport failure in the corpus resolver is not treated as identifier
    invalidity or as proof that its primary body was read.; PMID:9671488: UNREACHABLE;
    Unique native MED identity, exact PMID/title/DOI and bibliography inspected; transport
    failure in the corpus resolver is not treated as identifier invalidity or as proof
    that its primary body was read. Native source checks are separately scoped; skipped
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
  topic: Four HIR constituents and external Asf1 partner
  outcome: supported
  target_ids:
  - GO:0000417
  summary: Exact GO identity/synonym and protein-complex parent agree. Hir1/Hir2/Hir3/Hpc2
    copurify at300mM KCl. The resolved boundary appropriately treats Asf1 as a cooperating
    partner; copurification and stimulation do not require adding it to the four-class
    HIR inventory.
  evidence_ids:
  - record
  - root57-sources-go
  - root57-sources-GO0000417-ancestors
  - root57-sources-PMC2819815-html
- assessment_id: composition
  area: grounding
  topic: Resolved Hir3 class and explicitly broader candidates
  outcome: concern
  target_ids:
  - GO:0000417
  summary: Hir3 has a verified whole-family homolog mapping. The inspected HIR1-like
    entry conflates Hir1/Hir2, and HRD is a shared domain; empty candidate-subfamily
    routes do not resolve those outstanding classes. No family absence is claimed
    beyond this bounded search.
  evidence_ids:
  - record
  - curation
  - root57-sources-ipr-IPR033053
  - root57-sources-ipr-IPR031120
  - root57-sources-ipr-IPR014840
  - root57-sources-protein-P32479
  - root57-sources-protein-P32480
  - root57-sources-protein-P47171
  - root57-sources-protein-Q01448
  - root57-sources-gene-HIR1
  - root57-sources-gene-HIR2
  - root57-sources-gene-HIR3
  - root57-sources-gene-HPC2
- assessment_id: formation
  area: grounding
  topic: Conditional Hir3 recovery depends on Hpc2
  outcome: supported
  target_ids:
  - GO:0000417
  summary: The maintained roles and membership graph are supported. Green additionally
    reports no Hir3 detected in Hir2 purifications after hpc2 deletion, with retained
    subcomplexes after other deletions. Association versus stability remains unresolved.
    This conditional recovery result is useful context, without demonstrating a material
    error in the stated inventory or universal constituent necessity. Asf1 recruitment
    and promoter binding remain separate readouts.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC2819815-html
- assessment_id: graph
  area: graph
  topic: Supported membership and replication-independent deposition
  outcome: supported
  target_ids:
  - GO:0000417
  summary: All four membership edges and the broad histone-deposition outcome are
    supported. EMSA and DNA-supercoiling assays distinguish HIR-alone activity under
    specified conditions from stronger combined HIR/Asf1 activity and CAF1-dependent
    replication-coupled assembly. The record correctly says cooperates without asserting
    absolute Asf1 dependence in every assay.
  evidence_ids:
  - record
  - graphs
  - root57-sources-go
  - root57-sources-PMC2819815-html
  - root57-sources-doi-10.1007_s00412-006-0087-z
  - root57-sources-doi-10.1016_j.cub.2005.10.053
- assessment_id: scope
  area: scope
  topic: Yeast experimental context and reference strains
  outcome: supported
  target_ids:
  - GO:0000417
  summary: The body/captions identify PKY strains and purification salt conditions;
    detailed genotypes and methods are delegated to unread supplements. S288C reference
    accessions do not identify all assay strains. COMMON retains the schema meaning
    present in most members with exceptional losses.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC2819815-html
  - root57-sources-tax-4932
  - root57-sources-tax-559292
  - root57-sources-protein-P32479
  - root57-sources-protein-P32480
  - root57-sources-protein-P47171
  - root57-sources-protein-Q01448
- assessment_id: formation-necessity
  area: grounding
  topic: Universal individual-constituent requirements remain unestablished
  outcome: unknown
  target_ids:
  - GO:0000417
  summary: The bounded interaction, recruitment and activity results do not establish
    a universal per-constituent formation-necessity profile. UNKNOWN values are not
    automatically defects and are not converted to ESSENTIAL.
  evidence_ids:
  - record
  - schema
  - root57-sources-PMC2819815-html
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target and bounded follow-up
  outcome: supported
  target_ids:
  - GO:0000417
  summary: Every maintained field, evidence row, component/example, graph edge, discussion
    and history entry was read. Optional unpopulated slots are not defects. Scientific
    status/history remain unchanged.
  evidence_ids:
  - record
  - schema
  - curation
  - root57-sources-go
  - root57-sources-doi-10.1007_s00412-006-0087-z
  - root57-sources-doi-10.1016_j.cub.2005.10.053
findings:
- finding_id: F1
  issue_key: hir-resolve-hir3-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve the Hir3 whole-family mapping
  description: The open family task and Hir3 label-only row still defer a mapping
    despite verified IPR033053 Hir3/CABIN1 whole-family identity and the matching
    P47171 reference. Other HIR component boundaries remain unresolved by the inspected
    candidates.
  target_ids:
  - GO:0000417
  field_paths:
  - components[2].grounding_status
  - discussions[1]
  evidence_ids:
  - record
  - curation
  - root57-sources-ipr-IPR033053
  - root57-sources-protein-P32479
  - root57-sources-protein-P32480
  - root57-sources-protein-P47171
  - root57-sources-protein-Q01448
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hir_complex.yaml
    role: maintained scientific record
  rule_id: Exact constituent-class grounding
  native_severity: minor
  normalization_reason: A bounded actionable class mapping under the existing explicit
    task; the complex identity and named protein examples remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000417
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/hir_complex.yaml
    role: maintained scientific record
  description: Ground Hir3 in the verified homolog family and narrow the existing
    task to the unresolved component classes.
  acceptance_checks:
  - Use IPR033053 with the fungal Hir3 reference example and the native homolog breadth
    stated.
  - Do not use mixed HIR1/HIR2 IPR031120 or HRD domain IPR014840 as exact replacements
    for their named complete classes.
  - Pass applicable native schema, strict, identifier and graph checks after separately
    authorized curation.
limitations:
- All five same-base batch26 corpus gates and exact target resolver rows are integrated
  with every manifested input hash verified.
- No figure pixels, atomic coordinates, raw assay datasets or sequence alignments
  were reanalyzed. Primary body reading is limited to the explicitly named sections
  and embedded captions.
- Any absence finding is confined to the complete inspected target and its existing
  task; bounded native family queries do not establish absence from all databases.
- Protein localization source notes match native annotation provenance. Except where
  explicitly described, the cited localization papers were read at abstract tier;
  their detailed assays were not independently rechecked.
- Green delegates all detailed Experimental Procedures to supplementary material,
  which was not inspected. S3B physical-recovery conclusions were read in the main
  Results text, not independently confirmed from supplemental gel pixels or raw mass
  spectra.
- Mousson2007 and the localization papers were read at complete native abstract tier.
  No fixed HIR stoichiometry is inferred from copurification or secondary annotation.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes clean observations and issue-bearing reviews
  alike.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Materiality reassessment removed an optional association-detail omission finding;
  the source observation remains explicitly assessed and universal formation necessity
  remains unknown.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
