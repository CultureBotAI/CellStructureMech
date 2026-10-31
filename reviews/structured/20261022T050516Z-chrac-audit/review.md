# Chrac scientific review

- Review: 20261022T050516Z-chrac-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:47:03Z
- Finished UTC: 2026-10-22T05:05:16Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The four-subunit yeast CHRAC-like complex, examples and remodeling graph are supported. One minor finding resolves the exact Dpb4 family independently of its multiple complex roles.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 2 of batch47 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0008623 | data/structures/other/chrac.yaml | maintained | CHRAC |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0008623 | Focused validator passed. |
| Focused native strict | passed | True | GO:0008623 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0008623 | Focused native check passed; claim-level support assessed separately. |
| Focused native verify | passed | True | GO:0008623 | Focused native check passed; claim-level support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0008623 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0008623 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0008623 | 11 of 16 collected target identifiers returned OK. PMID:11024162: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:11238944: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14673157: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:15024052: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0008623 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0008623 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0008623 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0008623 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0008623 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Four-subunit yeast CHRAC-like assembly

identity: supported. Targets: GO:0008623.

GO0008623 and ISWI-type parent agree. Primary purifications distinguish the four-subunit yeast assembly from the two-subunit ACF-like form, while the broad GO definition retains cross-lineage compositional variation.

### Dpb4 identity is groundable independently of role

grounding: concern. Targets: GO:0008623.

IPR051377 denotes the Dpb4/POLE3 whole-family class, corroborated by exact accession and reviewed-member joins. Its polymerase-related name does not disqualify the same protein from a separately evidenced CHRAC role. Dls1 IPR050568 spans additional regulators and is too broad; the inspected Isw2/Itc1 xrefs are domains or broader classes.

### Correct reviewed S288C identifiers

grounding: supported. Targets: GO:0008623.

The four accessions, names, gene queries and strain identities match. Localization references are independently identified at abstract level; the examples identify proteins without claiming that all complex purifications used S288C.

### Functional requirement remains distinct from complete assembly

grounding: unknown. Targets: GO:0008623.

Dls1 is needed to differing degrees for remodeling at tested loci and is dispensable for the measured Isw2 chromatin association. Partnered coimmunoprecipitation adds assembly context but does not establish a complete four-subunit depletion matrix. UNKNOWN remains conservative at the current model scope.

### Species-level yeast claims match the experiments

scope: supported. Targets: GO:0008623.

The canonical and distribution rows use S.cerevisiae and permit W303/BJ2168 assay backgrounds while retaining exact S288C reference examples. COMMON retains most-members/losses-exception meaning as qualitative synthesis, not a strain census.

### Chromatin remodeling with locus-dependent Dls1 contribution

evidence: supported. Targets: GO:0008623.

The general ATP-dependent chromatin-remodeling function is supported. The paper-title wording about Dls1 being required is interpreted with the primary locus-specific partial effects; it does not entail universal loss of remodeling or assembly.

### Constituent-to-complex and remodeling directions are supported

graph: supported. Targets: GO:0008623.

The NONMECHANISTIC graph has direct purification support for its four constituents and functional evidence for remodeling. It avoids a fabricated recruitment or ATPase-cycle order.

### One exact family resolves part of the existing TODO

completeness: supported. Targets: GO:0008623.

All fields were reviewed. Ground Dpb4 identity while retaining separately sourced CHRAC membership and unresolved Isw2/Itc1/Dls1 exact classes. An exact family need not encode every role of its members.

## Findings

### F1: Ground Dpb4 independently of its CHRAC role

minor / open / confirmed; issue key: chrac-dpb4-exact-family.

Dpb4 remains REVIEWED_LABEL_ONLY and its note rejects polymerase-associated terms that do not denote the CHRAC role. IPR051377 is a whole Dpb4/POLE3 family, verified by Q04603 and the exact reviewed-member query. The native description is marked LLM-generated/unchecked, so the finding relies on independently matching family membership and identity; primary papers separately establish CHRAC participation.

## Recommended Actions And Acceptance Checks

### A1

Add the exact Dpb4 family identity and revise the role-based rejection in the current note/TODO. Keep CHRAC membership evidence and leave other broader domains/families unresolved.

- Verify exact source identities and reconcile the specified current fields and TODO scope.
- Preserve supported accessions and membership; retain assay, lineage and uncertainty limits.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/chrac.yaml; Entire maintained target, history, components, evidence, discussions and graphs | context_only | All maintained fields were read; history is provenance rather than independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Components, essentiality, COMMON and graph scope | context_only | Whole-protein families differ from shared domains and individual examples. Formation necessity differs from functional and cellular essentiality. COMMON means present in most members, with losses the exception. |
| curation | docs/CURATION.md; Source identity, exact grounding and claim-specific support | context_only | Reviewed label-only means no exact term exists. Verified whole-protein identity may be grounded independently of its separately evidenced role in a complex. Canonical taxon scope must match the cited experiment. |
| root47-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0006260,GO:0006338,GO:0006974,GO:0008623,GO:0015030,GO:0016604,GO:0030896,GO:0031010,GO:0031124,GO:0031261,GO:0031981,GO:0042555,GO:0071162,GO:0071920,GO:0140513; All16 requested terms: complete id/name/active/definition/synonyms/comments and relevant maintained typed links, not every descendant | supports | The requested native GO identities, definitions, synonyms and inspected maintained typed relationships agree with the target classes and functions. Missing direct ontology links alone do not disprove sourced biological parthood. |
| root47-sources-pmid-14673157 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14673157+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED14673157: Noncompetitive counteractions of DNA polymerase epsilon and ISW2/yCHRAC for epigenetic inheritance of telomere position effect in Saccharomyces cerevisiae. DOI 10.1128/mcb.24.1.217-227.2004. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-15024052 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15024052+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED15024052: Histone fold protein Dls1p is required for Isw2-dependent chromatin remodeling in vivo. DOI 10.1128/mcb.24.7.2605-2613.2004. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED14562095: Global analysis of protein localization in budding yeast. DOI 10.1038/nature02026. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-11238944 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11238944+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED11238944: Interactions of Isw2 chromatin remodeling complex with nucleosomal arrays: analyses using recombinant yeast histones and immobilized templates. DOI 10.1128/mcb.21.6.2098-2106.2001. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-pmid-11024162 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11024162+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native identifier/title/authors/year/DOI and abstract | supports | MED11024162: Structure and function of the fourth subunit (Dpb4p) of DNA polymerase epsilon in Saccharomyces cerevisiae. DOI 10.1093/nar/28.20.3846. Complete native bibliographic identity and abstract were inspected. This row certifies abstract-level access only; body inspection is recorded separately. |
| root47-sources-protein-Q08773 | https://rest.uniprot.org/uniprotkb/Q08773.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | Q08773 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-protein-P53125 | https://rest.uniprot.org/uniprotkb/P53125.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | P53125 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-protein-Q04603 | https://rest.uniprot.org/uniprotkb/Q04603.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | Q04603 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-protein-P40366 | https://rest.uniprot.org/uniprotkb/P40366.json; Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR LOCATION and SIMILARITY comments; InterPro/Pfam cross-references | supports | P40366 agrees with the maintained reviewed entry, protein name, gene identity and taxon identifier. Membership and experimental source scope are assessed separately. |
| root47-sources-gene-ISW2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-gene-ITC1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AITC1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-gene-DPB4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-gene-DLS1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADLS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL and all result accession/status/name/gene/taxon fields | supports | The exact reviewed gene/taxon query returns one result, matching the maintained accession, status, names and taxon. |
| root47-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA verifies taxon 4932 and its rank, name and lineage. Species and strain identities are kept distinct. |
| root47-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | ENA verifies taxon 559292 and its rank, name and lineage. Species and strain identities are kept distinct. |
| root47-sources-ipr-IPR051377 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051377/; Complete accession/name/type/description, curation flags and family metadata | supports | IPR051377 is a family named DNA Polymerase Epsilon Subunit. Complete native description and its curation flags were inspected; example cross-references provide an independent identity join. This annotation is not primary evidence of complex membership. |
| root47-sources-ipr-IPR050568 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050568/; Complete accession/name/type/description, curation flags and family metadata | supports | IPR050568 is a family named Transcription/DNA replication regulator. Complete native description and its curation flags were inspected; example cross-references provide an independent identity join. This annotation is not primary evidence of complex membership. |
| root47-sources-family-members-IPR051377 | https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR051377%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100&amp;fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name%2Corganism_id; Exact xref:interpro-IPR051377 AND reviewed:true query, size100; all15 returned accession/status/names/genes/taxa; no sequence/function fields requested | supports | The exact reviewed InterPro-family query returns15 entries, all inspected in full returned identity fields: Dpb4/POLE3 proteins including yeast Q04603 and human POLE3/CHRAC17 Q9NRF9. This independently corroborates the whole Dpb4 family boundary despite the native InterPro description being marked LLM-generated and unchecked. It is not a primary membership experiment or exhaustive homology analysis. |
| root47-sources-legacy-PMC371119 | https://pmc.ncbi.nlm.nih.gov/articles/PMC371119/?report=reader; Complete Methods sec2(Table1)/3/4 and Results sec9/10/11/12 including Fig1–5 captions; other Methods and Discussion not certified | supports | Independent tagged Isw2 and Dls1 purifications identify Itc1, Isw2, Dpb4 and Dls1; Dpb4 is shared with polymerase epsilon, which is not stably associated with Isw2. Two- and four-subunit forms are separated, with purification destabilization retained as an alternative. Dls1 deletion causes locus-dependent functional/remodeling defects without eliminating tested chromatin binding. |
| root47-sources-legacy-PMC303358 | https://pmc.ncbi.nlm.nih.gov/articles/PMC303358/?report=reader; Complete Methods sec2(Table1)/6 and Results sec11 with Fig4 caption; other sections not certified | supports | Dpb4 pull-down, peptide identification, tag shifts and gel filtration distinguish polymerase epsilon from the four-subunit ISW2/yCHRAC assembly. Dpb3/Dls1 deletion comparisons support partnered histone-fold interactions. Experiments include W303 genetic backgrounds and BJ2168-derived purification strains, rather than declaring all assays S288C. |
| schema-result | just validate data/structures/other/chrac.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/chrac.yaml |
| strict-result | just validate-strict data/structures/other/chrac.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/chrac-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/chrac.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/chrac-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/chrac-strict.tsv |
| native-chrac-causal-graphs | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/chrac.yaml; Complete focused native report | supports | data/structures/other/chrac.yaml  (GO:0008623)<br>  yeast_chrac_chromatin_remodeling	isw2_chrac_atpase_subunit	COVERED	-&gt;isw2_chrac_atpase_subunit (UniProtKB:Q08773)<br>  yeast_chrac_chromatin_remodeling	itc1_chrac_acf1_homolog_subunit	COVERED	-&gt;itc1_chrac_acf1_homolog_subunit (UniProtKB:P53125)<br>  yeast_chrac_chromatin_remodeling	dpb4_chrac_histone_fold_subunit	COVERED	-&gt;dpb4_chrac_histone_fold_subunit (UniProtKB:Q04603)<br>  yeast_chrac_chromatin_remodeling	dls1_chrac_histone_fold_subunit	COVERED	-&gt;dls1_chrac_histone_fold_subunit (UniProtKB:P40366)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-chrac-verify | /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/chrac.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/chrac.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 16 collected target identifiers returned OK. PMID:11024162: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:11238944: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14673157: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:15024052: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw experimental data, supplementary files or sequence alignments were reanalyzed. Primary-body inspection is limited to the explicitly listed sections.
- Ohya2000, Gelbart2001 and Huh2003 were inspected at complete native metadata/abstract level only; downloaded bodies for the first two were not substantively read and are not certified.
- The reviewed family-member query is a bounded annotation cross-check; no alignment or exhaustive sequence-based family reassessment was performed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T050516Z-chrac-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Chrac scientific review
started_at: '2026-10-22T04:47:03Z'
finished_at: '2026-10-22T05:05:16Z'
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
summary: The four-subunit yeast CHRAC-like complex, examples and remodeling graph
  are supported. One minor finding resolves the exact Dpb4 family independently of
  its multiple complex roles.
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
  - path: data/structures/other/chrac.yaml
    sha256: d31b095249c6c8d73ddbb45f8c090f2ad0f94e14916bbd42886ad96dcd10e2ba
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
- target_id: GO:0008623
  path: data/structures/other/chrac.yaml
  label: CHRAC
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/chrac.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 2 of batch47 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0008623
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0008623
  command: just validate data/structures/other/chrac.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0008623
  command: just validate-strict data/structures/other/chrac.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/chrac-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-chrac-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0008623
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/chrac.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-chrac-causal-graphs
- check_id: native-chrac-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0008623
  command: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/chrac.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-chrac-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0008623
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0008623
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root47-sources-go
  - root47-sources-pmid-14673157
  - root47-sources-pmid-15024052
  - root47-sources-pmid-14562095
  - root47-sources-pmid-11238944
  - root47-sources-pmid-11024162
  - root47-sources-protein-Q08773
  - root47-sources-protein-P53125
  - root47-sources-protein-Q04603
  - root47-sources-protein-P40366
  - root47-sources-gene-ISW2-559292
  - root47-sources-gene-ITC1-559292
  - root47-sources-gene-DPB4-559292
  - root47-sources-gene-DLS1-559292
  - root47-sources-tax4932
  - root47-sources-tax559292
  - root47-sources-ipr-IPR051377
  - root47-sources-ipr-IPR050568
  - root47-sources-family-members-IPR051377
  - root47-sources-legacy-PMC371119
  - root47-sources-legacy-PMC303358
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0008623
  summary: '11 of 16 collected target identifiers returned OK. PMID:11024162: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:11238944:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force.; PMID:14673157: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force.; PMID:15024052: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root47-sources-pmid-11024162
  - root47-sources-pmid-11238944
  - root47-sources-pmid-14562095
  - root47-sources-pmid-14673157
  - root47-sources-pmid-15024052
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0008623
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0008623
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0008623
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0008623
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0008623
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
    and current batch47 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/chrac.yaml
  locator: Entire maintained target, history, components, evidence, discussions and
    graphs
  accessed_at: '2026-10-22T04:59:18Z'
  support: context_only
  summary: All maintained fields were read; history is provenance rather than independent
    scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Components, essentiality, COMMON and graph scope
  accessed_at: '2026-10-22T04:59:18Z'
  support: context_only
  summary: Whole-protein families differ from shared domains and individual examples.
    Formation necessity differs from functional and cellular essentiality. COMMON
    means present in most members, with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Source identity, exact grounding and claim-specific support
  accessed_at: '2026-10-22T04:59:18Z'
  support: context_only
  summary: Reviewed label-only means no exact term exists. Verified whole-protein
    identity may be grounded independently of its separately evidenced role in a complex.
    Canonical taxon scope must match the cited experiment.
- evidence_id: root47-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000811,GO:0006260,GO:0006338,GO:0006974,GO:0008623,GO:0015030,GO:0016604,GO:0030896,GO:0031010,GO:0031124,GO:0031261,GO:0031981,GO:0042555,GO:0071162,GO:0071920,GO:0140513
  locator: 'All16 requested terms: complete id/name/active/definition/synonyms/comments
    and relevant maintained typed links, not every descendant'
  accessed_at: '2026-10-22T04:47:53.214339Z'
  support: supports
  summary: The requested native GO identities, definitions, synonyms and inspected
    maintained typed relationships agree with the target classes and functions. Missing
    direct ontology links alone do not disprove sourced biological parthood.
  snapshot_sha256: 7e9a7e9f97cb8700350b218ea7610079c613603a48f19d04ce36665e94dc65ef
- evidence_id: root47-sources-pmid-14673157
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14673157+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:59.748202Z'
  support: supports
  summary: 'MED14673157: Noncompetitive counteractions of DNA polymerase epsilon and
    ISW2/yCHRAC for epigenetic inheritance of telomere position effect in Saccharomyces
    cerevisiae. DOI 10.1128/mcb.24.1.217-227.2004. Complete native bibliographic identity
    and abstract were inspected. This row certifies abstract-level access only; body
    inspection is recorded separately.'
  snapshot_sha256: 1d5260a95aa51526114ebfe7586514998f87eb22951aa9c723000ca6c1ff65a6
- evidence_id: root47-sources-pmid-15024052
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15024052+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:59.748444Z'
  support: supports
  summary: 'MED15024052: Histone fold protein Dls1p is required for Isw2-dependent
    chromatin remodeling in vivo. DOI 10.1128/mcb.24.7.2605-2613.2004. Complete native
    bibliographic identity and abstract were inspected. This row certifies abstract-level
    access only; body inspection is recorded separately.'
  snapshot_sha256: 93db07a29ba531cb3d35283d4ec4b87df5a65b657e1946f3f8799c08b71b2641
- evidence_id: root47-sources-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:59.644868Z'
  support: supports
  summary: 'MED14562095: Global analysis of protein localization in budding yeast.
    DOI 10.1038/nature02026. Complete native bibliographic identity and abstract were
    inspected. This row certifies abstract-level access only; body inspection is recorded
    separately.'
  snapshot_sha256: 571f7249c52d66a3b53ae05fa04cfe3012ab729c63308d338c745e9f3c1daa72
- evidence_id: root47-sources-pmid-11238944
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11238944+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:58.519357Z'
  support: supports
  summary: 'MED11238944: Interactions of Isw2 chromatin remodeling complex with nucleosomal
    arrays: analyses using recombinant yeast histones and immobilized templates. DOI
    10.1128/mcb.21.6.2098-2106.2001. Complete native bibliographic identity and abstract
    were inspected. This row certifies abstract-level access only; body inspection
    is recorded separately.'
  snapshot_sha256: 974b7929fd21cbea568f7c2941433fa0f457c719bbaab8ffe0761ccb67bf1df8
- evidence_id: root47-sources-pmid-11024162
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11024162+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native identifier/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:47:58.106762Z'
  support: supports
  summary: 'MED11024162: Structure and function of the fourth subunit (Dpb4p) of DNA
    polymerase epsilon in Saccharomyces cerevisiae. DOI 10.1093/nar/28.20.3846. Complete
    native bibliographic identity and abstract were inspected. This row certifies
    abstract-level access only; body inspection is recorded separately.'
  snapshot_sha256: 7bbbb94e8d38953570648bbe635c8f3a2f900b108fe47be7925cde80b102c5c9
- evidence_id: root47-sources-protein-Q08773
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q08773.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:55.647849Z'
  support: supports
  summary: Q08773 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: 2637bfb5d984e050fbf830b95bf000a10c6cf69fd9895b6921cdfe853f59ee2c
- evidence_id: root47-sources-protein-P53125
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53125.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:54.909984Z'
  support: supports
  summary: P53125 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: 15a6f5624bd3147df7e928db6e548bf9a5d8e7c586453675ef5661d7d4221fd5
- evidence_id: root47-sources-protein-Q04603
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04603.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:54.911032Z'
  support: supports
  summary: Q04603 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: bc6495bed9da52fb9fd473800c575ee298e2bc5cac981a70b218ddd5ca507944
- evidence_id: root47-sources-protein-P40366
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40366.json
  locator: Complete identity/status/name/genes/taxon; FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION and SIMILARITY comments; InterPro/Pfam cross-references
  accessed_at: '2026-10-22T04:47:54.786304Z'
  support: supports
  summary: P40366 agrees with the maintained reviewed entry, protein name, gene identity
    and taxon identifier. Membership and experimental source scope are assessed separately.
  snapshot_sha256: 5aa0a202a834babb86528273fab0948bcc9da00364502a9952f6091c4bd08b0a
- evidence_id: root47-sources-gene-ISW2-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:48.732602Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 4a0b2c299a8108e3d0211b807a656d0b2a8cc4309334e35a687d00689cca310d
- evidence_id: root47-sources-gene-ITC1-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AITC1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:49.001241Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 9555d012d20ee604810ec610e8d7bb48fa09ada92bbfafe02f82a3ac4e6f7c2f
- evidence_id: root47-sources-gene-DPB4-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADPB4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:49.123044Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 832a7fb8258ecf2347addedf27fe8c0cf6df41aaf016ee00ef78a5e8fe759233
- evidence_id: root47-sources-gene-DLS1-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ADLS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL and all result accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:48:49.251923Z'
  support: supports
  summary: The exact reviewed gene/taxon query returns one result, matching the maintained
    accession, status, names and taxon.
  snapshot_sha256: 290f1137cb4e24e06bd9e7cc5fb3adfaec0a4ff5dd7b84e820e5505aa6a4bd8e
- evidence_id: root47-sources-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:47:53.215839Z'
  support: supports
  summary: ENA verifies taxon 4932 and its rank, name and lineage. Species and strain
    identities are kept distinct.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root47-sources-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:47:53.996027Z'
  support: supports
  summary: ENA verifies taxon 559292 and its rank, name and lineage. Species and strain
    identities are kept distinct.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root47-sources-ipr-IPR051377
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR051377/
  locator: Complete accession/name/type/description, curation flags and family metadata
  accessed_at: '2026-10-22T04:48:48.266933Z'
  support: supports
  summary: IPR051377 is a family named DNA Polymerase Epsilon Subunit. Complete native
    description and its curation flags were inspected; example cross-references provide
    an independent identity join. This annotation is not primary evidence of complex
    membership.
  snapshot_sha256: 9bdfe311b53f978a624fea4228263d4408ef60630986f7a2e4649c9474aa9c95
- evidence_id: root47-sources-ipr-IPR050568
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050568/
  locator: Complete accession/name/type/description, curation flags and family metadata
  accessed_at: '2026-10-22T04:48:48.051226Z'
  support: supports
  summary: IPR050568 is a family named Transcription/DNA replication regulator. Complete
    native description and its curation flags were inspected; example cross-references
    provide an independent identity join. This annotation is not primary evidence
    of complex membership.
  snapshot_sha256: 11f3355159a9e41625de92336d1d3d830ae1f087f1a4ed5ff9a86470bca3ef83
- evidence_id: root47-sources-family-members-IPR051377
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28xref%3Ainterpro-IPR051377%29+AND+%28reviewed%3Atrue%29&format=json&size=100&fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name%2Corganism_id
  locator: Exact xref:interpro-IPR051377 AND reviewed:true query, size100; all15 returned
    accession/status/names/genes/taxa; no sequence/function fields requested
  accessed_at: '2026-10-22T04:55:24.663014Z'
  support: supports
  summary: 'The exact reviewed InterPro-family query returns15 entries, all inspected
    in full returned identity fields: Dpb4/POLE3 proteins including yeast Q04603 and
    human POLE3/CHRAC17 Q9NRF9. This independently corroborates the whole Dpb4 family
    boundary despite the native InterPro description being marked LLM-generated and
    unchecked. It is not a primary membership experiment or exhaustive homology analysis.'
  snapshot_sha256: f7bd88c84d35f4a25472367ca8fd6cda09fbf335218fc06818f8471908daaa86
- evidence_id: root47-sources-legacy-PMC371119
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC371119/?report=reader
  locator: Complete Methods sec2(Table1)/3/4 and Results sec9/10/11/12 including Fig1–5
    captions; other Methods and Discussion not certified
  accessed_at: '2026-10-22T04:48:51.013626Z'
  support: supports
  summary: Independent tagged Isw2 and Dls1 purifications identify Itc1, Isw2, Dpb4
    and Dls1; Dpb4 is shared with polymerase epsilon, which is not stably associated
    with Isw2. Two- and four-subunit forms are separated, with purification destabilization
    retained as an alternative. Dls1 deletion causes locus-dependent functional/remodeling
    defects without eliminating tested chromatin binding.
  snapshot_sha256: b2696ccf7cd5a3ed57b78e567101ed90867d574cdecdcf947b34b856af231763
- evidence_id: root47-sources-legacy-PMC303358
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC303358/?report=reader
  locator: Complete Methods sec2(Table1)/6 and Results sec11 with Fig4 caption; other
    sections not certified
  accessed_at: '2026-10-22T04:48:50.922965Z'
  support: supports
  summary: Dpb4 pull-down, peptide identification, tag shifts and gel filtration distinguish
    polymerase epsilon from the four-subunit ISW2/yCHRAC assembly. Dpb3/Dls1 deletion
    comparisons support partnered histone-fold interactions. Experiments include W303
    genetic backgrounds and BJ2168-derived purification strains, rather than declaring
    all assays S288C.
  snapshot_sha256: 44f8d64377ab30a5c8197339474be61af0653077d87d037b1e12652f33aec5cf
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/chrac.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:04Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/chrac.yaml'
  snapshot_sha256: 7268211afe3614ffa5efb53e2b2eb3075cf8d0961ff286a52ec78335a4ea5621
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/chrac.yaml --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/chrac-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:47:07Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/chrac.yaml\
    \ --out /private/tmp/cellstructure-batch47-20261022-cz2022xg/chrac-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch47-20261022-cz2022xg/chrac-strict.tsv"
  snapshot_sha256: d3556fbb550d791058771965f83d6ac38f2b6ac6621b87942aa7b7439e264a87
- evidence_id: native-chrac-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/chrac.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:47:59.421948Z'
  support: supports
  summary: "data/structures/other/chrac.yaml  (GO:0008623)\n  yeast_chrac_chromatin_remodeling\t\
    isw2_chrac_atpase_subunit\tCOVERED\t->isw2_chrac_atpase_subunit (UniProtKB:Q08773)\n\
    \  yeast_chrac_chromatin_remodeling\titc1_chrac_acf1_homolog_subunit\tCOVERED\t\
    ->itc1_chrac_acf1_homolog_subunit (UniProtKB:P53125)\n  yeast_chrac_chromatin_remodeling\t\
    dpb4_chrac_histone_fold_subunit\tCOVERED\t->dpb4_chrac_histone_fold_subunit (UniProtKB:Q04603)\n\
    \  yeast_chrac_chromatin_remodeling\tdls1_chrac_histone_fold_subunit\tCOVERED\t\
    ->dls1_chrac_histone_fold_subunit (UniProtKB:P40366)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     4  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     4  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: c118b89abf84c352cbc1863934759c0680aaee97ee052c1ee279efae0e303656
- evidence_id: native-chrac-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch47-20261022-cz2022xg/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/chrac.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:48:01.750133Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/chrac.yaml; native collect() exact identifier slice;
    SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 16 collected target identifiers returned OK. PMID:11024162: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:11238944:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force.; PMID:14673157: UNREACHABLE; Exact native Europe
    PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport
    failure. Identity resolution does not certify every attached biological claim;
    declared abstract/body reading scope remains in force.; PMID:15024052: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
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
  topic: Four-subunit yeast CHRAC-like assembly
  outcome: supported
  target_ids:
  - GO:0008623
  summary: GO0008623 and ISWI-type parent agree. Primary purifications distinguish
    the four-subunit yeast assembly from the two-subunit ACF-like form, while the
    broad GO definition retains cross-lineage compositional variation.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC371119
  - root47-sources-legacy-PMC303358
- assessment_id: composition
  area: grounding
  topic: Dpb4 identity is groundable independently of role
  outcome: concern
  target_ids:
  - GO:0008623
  summary: IPR051377 denotes the Dpb4/POLE3 whole-family class, corroborated by exact
    accession and reviewed-member joins. Its polymerase-related name does not disqualify
    the same protein from a separately evidenced CHRAC role. Dls1 IPR050568 spans
    additional regulators and is too broad; the inspected Isw2/Itc1 xrefs are domains
    or broader classes.
  evidence_ids:
  - record
  - curation
  - root47-sources-ipr-IPR051377
  - root47-sources-ipr-IPR050568
  - root47-sources-family-members-IPR051377
  - root47-sources-protein-Q08773
  - root47-sources-protein-P53125
  - root47-sources-protein-Q04603
  - root47-sources-protein-P40366
- assessment_id: examples
  area: grounding
  topic: Correct reviewed S288C identifiers
  outcome: supported
  target_ids:
  - GO:0008623
  summary: The four accessions, names, gene queries and strain identities match. Localization
    references are independently identified at abstract level; the examples identify
    proteins without claiming that all complex purifications used S288C.
  evidence_ids:
  - record
  - root47-sources-protein-Q08773
  - root47-sources-protein-P53125
  - root47-sources-protein-Q04603
  - root47-sources-protein-P40366
  - root47-sources-gene-ISW2-559292
  - root47-sources-gene-ITC1-559292
  - root47-sources-gene-DPB4-559292
  - root47-sources-gene-DLS1-559292
  - root47-sources-tax4932
  - root47-sources-tax559292
  - root47-sources-pmid-14673157
  - root47-sources-pmid-15024052
  - root47-sources-pmid-14562095
  - root47-sources-pmid-11238944
  - root47-sources-pmid-11024162
- assessment_id: necessity
  area: grounding
  topic: Functional requirement remains distinct from complete assembly
  outcome: unknown
  target_ids:
  - GO:0008623
  summary: Dls1 is needed to differing degrees for remodeling at tested loci and is
    dispensable for the measured Isw2 chromatin association. Partnered coimmunoprecipitation
    adds assembly context but does not establish a complete four-subunit depletion
    matrix. UNKNOWN remains conservative at the current model scope.
  evidence_ids:
  - record
  - schema
  - root47-sources-legacy-PMC371119
  - root47-sources-legacy-PMC303358
- assessment_id: scope
  area: scope
  topic: Species-level yeast claims match the experiments
  outcome: supported
  target_ids:
  - GO:0008623
  summary: The canonical and distribution rows use S.cerevisiae and permit W303/BJ2168
    assay backgrounds while retaining exact S288C reference examples. COMMON retains
    most-members/losses-exception meaning as qualitative synthesis, not a strain census.
  evidence_ids:
  - record
  - schema
  - root47-sources-legacy-PMC371119
  - root47-sources-legacy-PMC303358
  - root47-sources-tax4932
  - root47-sources-tax559292
- assessment_id: function
  area: evidence
  topic: Chromatin remodeling with locus-dependent Dls1 contribution
  outcome: supported
  target_ids:
  - GO:0008623
  summary: The general ATP-dependent chromatin-remodeling function is supported. The
    paper-title wording about Dls1 being required is interpreted with the primary
    locus-specific partial effects; it does not entail universal loss of remodeling
    or assembly.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC371119
  - root47-sources-pmid-11238944
- assessment_id: graph
  area: graph
  topic: Constituent-to-complex and remodeling directions are supported
  outcome: supported
  target_ids:
  - GO:0008623
  summary: The NONMECHANISTIC graph has direct purification support for its four constituents
    and functional evidence for remodeling. It avoids a fabricated recruitment or
    ATPase-cycle order.
  evidence_ids:
  - record
  - root47-sources-go
  - root47-sources-legacy-PMC371119
  - root47-sources-legacy-PMC303358
- assessment_id: coverage
  area: completeness
  topic: One exact family resolves part of the existing TODO
  outcome: supported
  target_ids:
  - GO:0008623
  summary: All fields were reviewed. Ground Dpb4 identity while retaining separately
    sourced CHRAC membership and unresolved Isw2/Itc1/Dls1 exact classes. An exact
    family need not encode every role of its members.
  evidence_ids:
  - record
  - curation
  - root47-sources-ipr-IPR051377
  - root47-sources-family-members-IPR051377
  - root47-sources-legacy-PMC371119
findings:
- finding_id: F1
  issue_key: chrac-dpb4-exact-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground Dpb4 independently of its CHRAC role
  description: Dpb4 remains REVIEWED_LABEL_ONLY and its note rejects polymerase-associated
    terms that do not denote the CHRAC role. IPR051377 is a whole Dpb4/POLE3 family,
    verified by Q04603 and the exact reviewed-member query. The native description
    is marked LLM-generated/unchecked, so the finding relies on independently matching
    family membership and identity; primary papers separately establish CHRAC participation.
  target_ids:
  - GO:0008623
  field_paths:
  - components[2].grounding_status
  - components[2].grounding_notes
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root47-sources-ipr-IPR051377
  - root47-sources-family-members-IPR051377
  - root47-sources-protein-Q04603
  - root47-sources-legacy-PMC371119
  - root47-sources-legacy-PMC303358
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/chrac.yaml
    role: maintained scientific record
  rule_id: Exact component identity and claim-specific source scope
  native_severity: minor
  normalization_reason: Bounded evidence-backed curation correction; supported structural
    identity and constituent membership remain intact. Historical search honesty is
    not questioned.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0008623
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/chrac.yaml
    role: maintained scientific record
  description: Add the exact Dpb4 family identity and revise the role-based rejection
    in the current note/TODO. Keep CHRAC membership evidence and leave other broader
    domains/families unresolved.
  acceptance_checks:
  - Verify exact source identities and reconcile the specified current fields and
    TODO scope.
  - Preserve supported accessions and membership; retain assay, lineage and uncertainty
    limits.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw experimental data, supplementary files or sequence alignments
  were reanalyzed. Primary-body inspection is limited to the explicitly listed sections.
- Ohya2000, Gelbart2001 and Huh2003 were inspected at complete native metadata/abstract
  level only; downloaded bodies for the first two were not substantively read and
  are not certified.
- The reviewed family-member query is a bounded annotation cross-check; no alignment
  or exhaustive sequence-based family reassessment was performed.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorizes reviews for all uncovered records, including honest zero-finding
  bundles.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
