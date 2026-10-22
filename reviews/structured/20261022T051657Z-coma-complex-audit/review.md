# Coma complex scientific review

- Review: 20261022T051657Z-coma-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:00:54Z
- Finished UTC: 2026-10-22T05:16:57Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

COMA identity, four subunits and coarse bridge graph are supported. Two minor findings concern the exact Mcm21 family and direct, condition-scoped Okp1 assembly evidence.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph and completeness.

Selection: Target 2 of batch48 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000817 | data/structures/other/coma_complex.yaml | maintained | COMA complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000817 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000817 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0000817 | Focused native check passed; identity and biological support assessed independently. |
| Focused native verify | passed | True | GO:0000817 | Focused native check passed; identity and biological support assessed independently. |
| Expression-module applicability | not_applicable | False | GO:0000817 | No maintained expression-module assertion requires this resource. |
| Claim-level scientific review | passed | True | GO:0000817 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0000817 | 16 of 19 collected target identifiers returned OK. PMID:10323865: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:29046335: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0000817 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000817 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000817 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000817 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0000817 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Four-protein COMA within the larger kinetochore

identity: supported. Targets: GO:0000817.

Exact GO identity, nuclear-complex parent and chromosome/kinetochore parthood agree. The erroneous native Mcm1 synonym remains deliberately omitted. Nkp1/Nkp2 and the wider CCAN network are not silently added to the four-subunit core.

### Mcm21 family is exact; other candidates remain bounded

grounding: concern. Targets: GO:0000817.

IPR018464 explicitly covers yeast Mcm21 and its CENP-O ortholog class. AME1 candidate IPR048743 is typed as a domain, and Ctf19 terminal/RWD entries do not establish whole-protein equivalence. The limited OKP1 text search did not resolve a full family; no exhaustive absence claim is made.

### Correct subunit and graph protein references

grounding: supported. Targets: GO:0000817.

The four component examples and four broader graph-node xrefs resolve to the appropriate S288C proteins. CSE4 is DNA-proximal; Ndc80/Nuf2/Spc24 represent the outer attachment module without asserting that every one directly contacts microtubules. Native localization citation assignments are preserved.

### Condition-scoped Okp1 assembly requirement

grounding: concern. Targets: GO:0000817.

Direct physical-association experiments can refine OKP1 UNKNOWN: restrictive okp1-5 eliminates the C1 complex and an independent native interface deletion prevents association with Ctf19-Mcm21. Surviving Ame1-Okp1/core kinetochore functions and allele-specific conditions prevent universal all-subunit necessity claims.

### Species-level experiment and narrower reference strain

scope: supported. Targets: GO:0000817.

W303 historical experiments and mostly S288C-derived modern clones support the species canonical scope. K.lactis reconstitution is separately bounded. COMMON describes ordinary budding-yeast kinetochore machinery rather than a census.

### Bridge function retains indirect-contact limits

evidence: supported. Targets: GO:0000817.

The GO definition and original assembly study support COMA as an inner-to-outer bridge. Independent recruitment of multiple platforms is compatible with the stated coarse role and does not establish a single obligatory linear assembly chain.

### Nonmechanistic bridge graph

graph: supported. Targets: GO:0000817.

Side-specific predicates and NONMECHANISTIC scope avoid direct pairwise-contact or assembly-order claims. The component groups are illustrative rather than a complete CCAN inventory.

### Family and direct-assembly follow-up

completeness: supported. Targets: GO:0000817.

The four-member core is retained. One exact family and a bounded Okp1 formation dependency are actionable; the native synonym spelling and broader CCAN boundary remain explicitly discussed.

## Findings

### F1: Ground the Mcm21 subunit with its exact ortholog family

minor / open / confirmed; issue key: coma-mcm21-family.

IPR018464 is a full family explicitly including yeast Mcm21 and is cross-referenced by Q06675. The maintained Mcm21 row remains REVIEWED_LABEL_ONLY. AME1 and Ctf19 domain candidates do not justify assigning whole-protein groundings to those rows.

### F2: Capture the condition-scoped Okp1 assembly requirement

minor / open / confirmed; issue key: coma-okp1-formation-evidence.

The current UNKNOWN field omits direct stable-association evidence. DeWulf sec4 shows loss of the heterotetramer after restrictive okp1-5 inactivation; Schmitzberger sec11 shows a specific Okp1 interface is required for native Ctf19-Mcm21 association while Ame1 and outer-kinetochore localization remain. These are physical-assembly observations rather than a growth-only inference.

## Recommended Actions And Acceptance Checks

### A1

Add the exact Mcm21/CENP-O family mapping IPR018464 and preserve separate current uncertainty for the other three whole-protein families.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.

### A2

Curate a condition-scoped Okp1 formation requirement with the exact allele, temperature and interface contexts. Preserve the remaining subunits as UNKNOWN unless independently supported, and do not equate complete COMA assembly with universal viability.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/coma_complex.yaml; Entire maintained record including history, components, evidence, graph and discussions | context_only | All maintained fields were read. Historical curation notes document earlier decisions rather than independently proving current assertions. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component grounding, formation essentiality, taxonomic presence and graph scope | context_only | Whole-protein families differ from domains and individual examples. Assembly necessity differs from viability or function. COMMON means present in most members, with losses the exception; a qualitative ordinary-machinery assertion need not imply a numerical census. |
| curation | docs/CURATION.md; Exact identities and claim-specific evidence | context_only | A verified component identity and its membership in a complex require distinct support. Reviewed label-only status is reserved for the absence of an exact term; historical deferred searches can be revisited without alleging historical fabrication. |
| root48-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000776,GO:0000817,GO:0003689,GO:0007062,GO:0017119,GO:0031390,GO:0031464,GO:0043494,GO:0048193,GO:0070912,GO:0080008,GO:0099023,GO:0140513; Complete maintained-term identity and definition fields and relevant typed links; not every descendant | supports | All14 requested GO identities, active status, definitions, synonyms, comments and relevant maintained typed relationships were inspected. The custom WDR1-specific assembly is distinct from the broader Cul4 parent. |
| root48-sources-doi-7 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144403%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED14633972: Hierarchical assembly of the budding yeast kinetochore from multiple subcomplexes. DOI 10.1101/gad.1144403. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-doi-10 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fgenetics.112.145276%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED23908374: The composition, functions, and regulation of the budding yeast kinetochore. DOI 10.1534/genetics.112.145276. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-pmid-10323865 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10323865+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED10323865: A putative protein complex consisting of Ctf19, Mcm21, and Okp1 represents a missing link in the budding yeast kinetochore. DOI 10.1101/gad.13.9.1140. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED14562095: Global analysis of protein localization in budding yeast. DOI 10.1038/nature02026. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-pmid-29046335 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29046335+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED29046335: Molecular basis for inner kinetochore configuration through RWD domain-peptide interactions. DOI 10.15252/embj.201796636. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-protein-Q02732 | https://rest.uniprot.org/uniprotkb/Q02732.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native Q02732 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P53298 | https://rest.uniprot.org/uniprotkb/P53298.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P53298 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-Q06675 | https://rest.uniprot.org/uniprotkb/Q06675.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native Q06675 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P38313 | https://rest.uniprot.org/uniprotkb/P38313.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P38313 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P36012 | https://rest.uniprot.org/uniprotkb/P36012.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P36012 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P40460 | https://rest.uniprot.org/uniprotkb/P40460.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P40460 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P33895 | https://rest.uniprot.org/uniprotkb/P33895.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P33895 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-Q04477 | https://rest.uniprot.org/uniprotkb/Q04477.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native Q04477 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-gene-CTF19 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF19+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-OKP1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AOKP1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-MCM21 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMCM21+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-AME1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAME1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | Native taxon 4932 name, rank, lineage and synonym data inspected. Reference strains are distinguished from experimental strains. |
| root48-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | Native taxon 559292 name, rank, lineage and synonym data inspected. Reference strains are distinguished from experimental strains. |
| root48-sources-ipr-IPR018464 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018464/; Complete accession/name/type/description, hierarchy, integrated signatures and curation flags | supports | IPR018464 is classified as family and named Centromere protein O. Native metadata, full description and curation flags inspected. This row supports identity scope, not an independent primary biological experiment. |
| root48-sources-ipr-IPR048743 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048743/; Complete accession/name/type/description, hierarchy, integrated signatures and curation flags | supports | IPR048743 is classified as domain and named Inner kinetochore subunit AME1. Native metadata, full description and curation flags inspected. This row supports identity scope, not an independent primary biological experiment. |
| root48-sources-dewulf2003-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/?_escaped_fragment_=; Complete Results sec4 including Table2/Figure3 captions, sec6/Figure6, Methods sec14/sec15 | supports | W303-derived extracts show a four-subunit C1 species and smaller C2 associations. Inactivation of okp1-5 at37C removes detectable C1/C2 and destabilizes the other subunits, whereas mtw1 control does not. CTF19/MCM21 deletions retain smaller associations. COMA, MIND and Ndc80 kinetochore binding are separable. |
| root48-sources-schmitzberger2017-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC5709738/?_escaped_fragment_=; Complete Results sections0003/0006/0011 and Methods0030, with embedded Fig1/4/5/7 and EV1/EV6 captions; no supplementary datasets/pixels | supports | K.lactis recombinant COMA-Nkp1-Nkp2 composition is distinct from native S.cerevisiae experiments. Removing the Okp1 Ctf19-Mcm21 binding motif prevents native Ctf19 co-immunoprecipitation and centromeric Ctf19/Mcm21 localization; Ame1 and outer-kinetochore signals persist. The targeted interface is needed for this association, not every kinetochore function or cell viability. |
| schema-result | just validate data/structures/other/coma_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/coma_complex.yaml |
| strict-result | just validate-strict data/structures/other/coma_complex.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/coma_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/coma_complex.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/coma_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch48-20261022-ppyyf64c/coma_complex-strict.tsv |
| native-coma_complex-causal-graphs | /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/coma_complex.yaml; Complete focused native report | supports | data/structures/other/coma_complex.yaml  (GO:0000817)<br>  coma_inner_outer_kinetochore_bridge	centromeric_dna_proximal_subunits	UNANCHORED_WITH_UNIPROT	centromeric DNA-proximal kinetochore subunits (UniProtKB:P36012)<br>  coma_inner_outer_kinetochore_bridge	microtubule_bound_subunits	UNANCHORED_WITH_UNIPROT	microtubule-bound kinetochore subunits (UniProtKB:P40460, UniProtKB:P33895, UniProtKB:Q04477)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-coma_complex-verify | /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/coma_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/coma_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 16 of 19 collected target identifiers returned OK. PMID:10323865: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:29046335: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Primary-body reading is limited to the sections explicitly named. No raw experimental data, supplementary datasets or sequence alignments were reanalyzed.
- Biggins2013, Ortiz1999 and Huh2003 are complete native abstract tier only. Modern K.lactis reconstitution and S.cerevisiae native experiments were kept distinct.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes all uncovered reviews, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T051657Z-coma-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Coma complex scientific review
started_at: '2026-10-22T05:00:54Z'
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
summary: COMA identity, four subunits and coarse bridge graph are supported. Two minor
  findings concern the exact Mcm21 family and direct, condition-scoped Okp1 assembly
  evidence.
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
  - path: data/structures/other/coma_complex.yaml
    sha256: d27210c22f2b06eb9eb3d5e8aa3ed93f6bf561ac07ae48ae295b11bf39f561da
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
- target_id: GO:0000817
  path: data/structures/other/coma_complex.yaml
  label: COMA complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph and completeness.
  selection: Target 2 of batch48 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000817
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000817
  command: just validate data/structures/other/coma_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000817
  command: just validate-strict data/structures/other/coma_complex.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/coma_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-coma_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0000817
  command: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/coma_complex.yaml
  exit_code: 0
  summary: Focused native check passed; identity and biological support assessed independently.
  evidence_ids:
  - native-coma_complex-causal-graphs
- check_id: native-coma_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0000817
  command: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/coma_complex.yaml
  exit_code: 0
  summary: Focused native check passed; identity and biological support assessed independently.
  evidence_ids:
  - native-coma_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0000817
  summary: No maintained expression-module assertion requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000817
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root48-sources-go
  - root48-sources-doi-7
  - root48-sources-doi-10
  - root48-sources-pmid-10323865
  - root48-sources-pmid-14562095
  - root48-sources-pmid-29046335
  - root48-sources-protein-Q02732
  - root48-sources-protein-P53298
  - root48-sources-protein-Q06675
  - root48-sources-protein-P38313
  - root48-sources-protein-P36012
  - root48-sources-protein-P40460
  - root48-sources-protein-P33895
  - root48-sources-protein-Q04477
  - root48-sources-gene-CTF19
  - root48-sources-gene-OKP1
  - root48-sources-gene-MCM21
  - root48-sources-gene-AME1
  - root48-sources-tax4932
  - root48-sources-tax559292
  - root48-sources-ipr-IPR018464
  - root48-sources-ipr-IPR048743
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0000817
  summary: '16 of 19 collected target identifiers returned OK. PMID:10323865: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:14562095:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:29046335: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root48-sources-pmid-10323865
  - root48-sources-pmid-14562095
  - root48-sources-pmid-29046335
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000817
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
  - GO:0000817
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
  - GO:0000817
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
  - GO:0000817
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
  - GO:0000817
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
  reference: data/structures/other/coma_complex.yaml
  locator: Entire maintained record including history, components, evidence, graph
    and discussions
  accessed_at: '2026-10-22T05:13:37Z'
  support: context_only
  summary: All maintained fields were read. Historical curation notes document earlier
    decisions rather than independently proving current assertions.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component grounding, formation essentiality, taxonomic presence and graph
    scope
  accessed_at: '2026-10-22T05:13:37Z'
  support: context_only
  summary: Whole-protein families differ from domains and individual examples. Assembly
    necessity differs from viability or function. COMMON means present in most members,
    with losses the exception; a qualitative ordinary-machinery assertion need not
    imply a numerical census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identities and claim-specific evidence
  accessed_at: '2026-10-22T05:13:37Z'
  support: context_only
  summary: A verified component identity and its membership in a complex require distinct
    support. Reviewed label-only status is reserved for the absence of an exact term;
    historical deferred searches can be revisited without alleging historical fabrication.
- evidence_id: root48-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000776,GO:0000817,GO:0003689,GO:0007062,GO:0017119,GO:0031390,GO:0031464,GO:0043494,GO:0048193,GO:0070912,GO:0080008,GO:0099023,GO:0140513
  locator: Complete maintained-term identity and definition fields and relevant typed
    links; not every descendant
  accessed_at: '2026-10-22T05:04:22.473075Z'
  support: supports
  summary: All14 requested GO identities, active status, definitions, synonyms, comments
    and relevant maintained typed relationships were inspected. The custom WDR1-specific
    assembly is distinct from the broader Cul4 parent.
  snapshot_sha256: d286c944be8950cb0f8aaf019fb391dc88abed2d978bb77bf24beba14a2ea670
- evidence_id: root48-sources-doi-7
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101%2Fgad.1144403%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:29.505428Z'
  support: supports
  summary: 'MED14633972: Hierarchical assembly of the budding yeast kinetochore from
    multiple subcomplexes. DOI 10.1101/gad.1144403. Complete bibliographic identity
    and abstract inspected; full-body access is certified only in separate evidence
    rows.'
  snapshot_sha256: 5b2d9eabcc5cc0b9a45f855a65928f7ec1373400650ff9a1108e3301c14892e9
- evidence_id: root48-sources-doi-10
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1534%2Fgenetics.112.145276%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:29.910332Z'
  support: supports
  summary: 'MED23908374: The composition, functions, and regulation of the budding
    yeast kinetochore. DOI 10.1534/genetics.112.145276. Complete bibliographic identity
    and abstract inspected; full-body access is certified only in separate evidence
    rows.'
  snapshot_sha256: f5dcefd0370997893d49f4b3f292f7d95ade9bb1f860155d5581b508dc0e9f00
- evidence_id: root48-sources-pmid-10323865
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10323865+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:29.948602Z'
  support: supports
  summary: 'MED10323865: A putative protein complex consisting of Ctf19, Mcm21, and
    Okp1 represents a missing link in the budding yeast kinetochore. DOI 10.1101/gad.13.9.1140.
    Complete bibliographic identity and abstract inspected; full-body access is certified
    only in separate evidence rows.'
  snapshot_sha256: a1f5213611e7ba1679d682c8a9bc0cf7a04620ed082252b043d09ac94090d673
- evidence_id: root48-sources-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:30.598913Z'
  support: supports
  summary: 'MED14562095: Global analysis of protein localization in budding yeast.
    DOI 10.1038/nature02026. Complete bibliographic identity and abstract inspected;
    full-body access is certified only in separate evidence rows.'
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: root48-sources-pmid-29046335
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A29046335+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:30.903210Z'
  support: supports
  summary: 'MED29046335: Molecular basis for inner kinetochore configuration through
    RWD domain-peptide interactions. DOI 10.15252/embj.201796636. Complete bibliographic
    identity and abstract inspected; full-body access is certified only in separate
    evidence rows.'
  snapshot_sha256: 2d12a06c10f652589302587bceb98c9ca38ab39b0e026e827c2be6feae3c159e
- evidence_id: root48-sources-protein-Q02732
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q02732.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:26.331939Z'
  support: supports
  summary: Native Q02732 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 4300f75049f2449011c3e78557ed639585c8206f4ea707ce6abda1aaa5b6b62d
- evidence_id: root48-sources-protein-P53298
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53298.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:25.492883Z'
  support: supports
  summary: Native P53298 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: e286b14d37ffacdfdacead4d28a714fb2cd7647ebcccc49df73d642fe0756906
- evidence_id: root48-sources-protein-Q06675
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q06675.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:27.412097Z'
  support: supports
  summary: Native Q06675 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: a284987a228269755202e144975329d40045d32097395fa0a3b5efbc26dcd801
- evidence_id: root48-sources-protein-P38313
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38313.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:23.369129Z'
  support: supports
  summary: Native P38313 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 053d6d5cadc71a57b6b685c5ac036757f82d889c4efce071a4a694908c5e0d07
- evidence_id: root48-sources-protein-P36012
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36012.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:23.250107Z'
  support: supports
  summary: Native P36012 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: bca7e7c2253768cc51d28557ea8967dd642ffbff3dff58274cecc9e8fae973f5
- evidence_id: root48-sources-protein-P40460
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40460.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:24.611716Z'
  support: supports
  summary: Native P40460 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: e9118ff7804c75195f78434aabd4f7b07fe4678b12faf54aa90a012fede3f5a6
- evidence_id: root48-sources-protein-P33895
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P33895.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:23.214734Z'
  support: supports
  summary: Native P33895 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 571967574ce29a5f5b3a43ad0c65267df722a3e258d80aeb78fea83a2b7323fe
- evidence_id: root48-sources-protein-Q04477
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q04477.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:26.347358Z'
  support: supports
  summary: Native Q04477 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 7c4ad50bf5ae4e1eb7738038fdb2a60c4f3ba91ee1b8fd9f7484489ef732d559
- evidence_id: root48-sources-gene-CTF19
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF19+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:18.892213Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: a9a47e880c6ddf126c5a8cfc5e899ce09ebe7ebc7a00b39ff7594e40f4a32309
- evidence_id: root48-sources-gene-OKP1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AOKP1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:19.343157Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: cbe45d27fdfe19adae898e1527e55b3a9c8b4ecc618ec106ea301c3e7c94c4a3
- evidence_id: root48-sources-gene-MCM21
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AMCM21+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:19.353196Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: a3cc24e2df5723fb6cec03e1893aaf4548a563624f8dc245d6c6e518e7334abd
- evidence_id: root48-sources-gene-AME1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3AAME1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:19.420957Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: 0d24b7575005296c4ba534d40d5e66dd54a2d6aebf6625ad1180ceb8ff885018
- evidence_id: root48-sources-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:04:22.473582Z'
  support: supports
  summary: Native taxon 4932 name, rank, lineage and synonym data inspected. Reference
    strains are distinguished from experimental strains.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root48-sources-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T05:04:22.473700Z'
  support: supports
  summary: Native taxon 559292 name, rank, lineage and synonym data inspected. Reference
    strains are distinguished from experimental strains.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root48-sources-ipr-IPR018464
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018464/
  locator: Complete accession/name/type/description, hierarchy, integrated signatures
    and curation flags
  accessed_at: '2026-10-22T05:06:12.913114Z'
  support: supports
  summary: IPR018464 is classified as family and named Centromere protein O. Native
    metadata, full description and curation flags inspected. This row supports identity
    scope, not an independent primary biological experiment.
  snapshot_sha256: 96ad879101de27e1856805668c39fea5f0612e63b18cbb014bb0c0e67d69c3d1
- evidence_id: root48-sources-ipr-IPR048743
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR048743/
  locator: Complete accession/name/type/description, hierarchy, integrated signatures
    and curation flags
  accessed_at: '2026-10-22T05:06:16.232937Z'
  support: supports
  summary: IPR048743 is classified as domain and named Inner kinetochore subunit AME1.
    Native metadata, full description and curation flags inspected. This row supports
    identity scope, not an independent primary biological experiment.
  snapshot_sha256: 4703e3109b23c0469085fbfc9953892e015e27831b1dcf085fb61c4139bc9c52
- evidence_id: root48-sources-dewulf2003-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC289150/?_escaped_fragment_=
  locator: Complete Results sec4 including Table2/Figure3 captions, sec6/Figure6,
    Methods sec14/sec15
  accessed_at: '2026-10-22T05:06:26.103217Z'
  support: supports
  summary: W303-derived extracts show a four-subunit C1 species and smaller C2 associations.
    Inactivation of okp1-5 at37C removes detectable C1/C2 and destabilizes the other
    subunits, whereas mtw1 control does not. CTF19/MCM21 deletions retain smaller
    associations. COMA, MIND and Ndc80 kinetochore binding are separable.
  snapshot_sha256: 034589bcc14f7128bc0921e6ff7a638b367bf790c2daa08097624425d5a556af
- evidence_id: root48-sources-schmitzberger2017-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC5709738/?_escaped_fragment_=
  locator: Complete Results sections0003/0006/0011 and Methods0030, with embedded
    Fig1/4/5/7 and EV1/EV6 captions; no supplementary datasets/pixels
  accessed_at: '2026-10-22T05:06:26.171608Z'
  support: supports
  summary: K.lactis recombinant COMA-Nkp1-Nkp2 composition is distinct from native
    S.cerevisiae experiments. Removing the Okp1 Ctf19-Mcm21 binding motif prevents
    native Ctf19 co-immunoprecipitation and centromeric Ctf19/Mcm21 localization;
    Ame1 and outer-kinetochore signals persist. The targeted interface is needed for
    this association, not every kinetochore function or cell viability.
  snapshot_sha256: 8cb93fb4e29d898db9bd8beff9e24d0cbf1d90e11f614273d96adf491e9c8ccf
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/coma_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:00:55Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/coma_complex.yaml'
  snapshot_sha256: bc2754be64b8e60ab381db67e6c9180e924b78525ff6c09adce0b13f782092ab
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/coma_complex.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/coma_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:00:56Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/coma_complex.yaml\
    \ --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/coma_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch48-20261022-ppyyf64c/coma_complex-strict.tsv"
  snapshot_sha256: 864ef72dc408d552ac3fd61d5010af34f5e77d10734e99a1fb67aeb2252e027a
- evidence_id: native-coma_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/coma_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:06:14.686196Z'
  support: supports
  summary: "data/structures/other/coma_complex.yaml  (GO:0000817)\n  coma_inner_outer_kinetochore_bridge\t\
    centromeric_dna_proximal_subunits\tUNANCHORED_WITH_UNIPROT\tcentromeric DNA-proximal\
    \ kinetochore subunits (UniProtKB:P36012)\n  coma_inner_outer_kinetochore_bridge\t\
    microtubule_bound_subunits\tUNANCHORED_WITH_UNIPROT\tmicrotubule-bound kinetochore\
    \ subunits (UniProtKB:P40460, UniProtKB:P33895, UniProtKB:Q04477)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     2  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  COVERED            \
    \       component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_NO_UNIPROT     no component_ref\
    \ and no UniProtKB grounding or xref on the node\n     2  total GENE_OR_PROTEIN\
    \ causal nodes"
  snapshot_sha256: c85c11f66a622ac93e81b66600dc48153bb42dc7d5bc0b64b79e7f16e6b65962
- evidence_id: native-coma_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/coma_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:06:15.896894Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/coma_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '16 of 19 collected target identifiers returned OK. PMID:10323865: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:14562095:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:29046335: UNREACHABLE; Exact native Europe PMC MED identifier,
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
  topic: Four-protein COMA within the larger kinetochore
  outcome: supported
  target_ids:
  - GO:0000817
  summary: Exact GO identity, nuclear-complex parent and chromosome/kinetochore parthood
    agree. The erroneous native Mcm1 synonym remains deliberately omitted. Nkp1/Nkp2
    and the wider CCAN network are not silently added to the four-subunit core.
  evidence_ids:
  - record
  - root48-sources-go
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
  - root48-sources-doi-7
  - root48-sources-doi-10
  - root48-sources-pmid-10323865
  - root48-sources-pmid-14562095
  - root48-sources-pmid-29046335
- assessment_id: families
  area: grounding
  topic: Mcm21 family is exact; other candidates remain bounded
  outcome: concern
  target_ids:
  - GO:0000817
  summary: IPR018464 explicitly covers yeast Mcm21 and its CENP-O ortholog class.
    AME1 candidate IPR048743 is typed as a domain, and Ctf19 terminal/RWD entries
    do not establish whole-protein equivalence. The limited OKP1 text search did not
    resolve a full family; no exhaustive absence claim is made.
  evidence_ids:
  - record
  - curation
  - root48-sources-ipr-IPR018464
  - root48-sources-ipr-IPR048743
  - root48-sources-protein-Q02732
  - root48-sources-protein-P53298
  - root48-sources-protein-Q06675
  - root48-sources-protein-P38313
  - root48-sources-protein-P36012
  - root48-sources-protein-P40460
  - root48-sources-protein-P33895
  - root48-sources-protein-Q04477
- assessment_id: examples
  area: grounding
  topic: Correct subunit and graph protein references
  outcome: supported
  target_ids:
  - GO:0000817
  summary: The four component examples and four broader graph-node xrefs resolve to
    the appropriate S288C proteins. CSE4 is DNA-proximal; Ndc80/Nuf2/Spc24 represent
    the outer attachment module without asserting that every one directly contacts
    microtubules. Native localization citation assignments are preserved.
  evidence_ids:
  - record
  - root48-sources-protein-Q02732
  - root48-sources-protein-P53298
  - root48-sources-protein-Q06675
  - root48-sources-protein-P38313
  - root48-sources-protein-P36012
  - root48-sources-protein-P40460
  - root48-sources-protein-P33895
  - root48-sources-protein-Q04477
  - root48-sources-gene-CTF19
  - root48-sources-gene-OKP1
  - root48-sources-gene-MCM21
  - root48-sources-gene-AME1
  - root48-sources-tax4932
  - root48-sources-tax559292
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
- assessment_id: necessity
  area: grounding
  topic: Condition-scoped Okp1 assembly requirement
  outcome: concern
  target_ids:
  - GO:0000817
  summary: 'Direct physical-association experiments can refine OKP1 UNKNOWN: restrictive
    okp1-5 eliminates the C1 complex and an independent native interface deletion
    prevents association with Ctf19-Mcm21. Surviving Ame1-Okp1/core kinetochore functions
    and allele-specific conditions prevent universal all-subunit necessity claims.'
  evidence_ids:
  - record
  - schema
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
- assessment_id: scope
  area: scope
  topic: Species-level experiment and narrower reference strain
  outcome: supported
  target_ids:
  - GO:0000817
  summary: W303 historical experiments and mostly S288C-derived modern clones support
    the species canonical scope. K.lactis reconstitution is separately bounded. COMMON
    describes ordinary budding-yeast kinetochore machinery rather than a census.
  evidence_ids:
  - record
  - schema
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
  - root48-sources-tax4932
  - root48-sources-tax559292
- assessment_id: functions
  area: evidence
  topic: Bridge function retains indirect-contact limits
  outcome: supported
  target_ids:
  - GO:0000817
  summary: The GO definition and original assembly study support COMA as an inner-to-outer
    bridge. Independent recruitment of multiple platforms is compatible with the stated
    coarse role and does not establish a single obligatory linear assembly chain.
  evidence_ids:
  - record
  - root48-sources-go
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
- assessment_id: graph
  area: graph
  topic: Nonmechanistic bridge graph
  outcome: supported
  target_ids:
  - GO:0000817
  summary: Side-specific predicates and NONMECHANISTIC scope avoid direct pairwise-contact
    or assembly-order claims. The component groups are illustrative rather than a
    complete CCAN inventory.
  evidence_ids:
  - record
  - root48-sources-go
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
- assessment_id: coverage
  area: completeness
  topic: Family and direct-assembly follow-up
  outcome: supported
  target_ids:
  - GO:0000817
  summary: The four-member core is retained. One exact family and a bounded Okp1 formation
    dependency are actionable; the native synonym spelling and broader CCAN boundary
    remain explicitly discussed.
  evidence_ids:
  - record
  - root48-sources-ipr-IPR018464
  - root48-sources-ipr-IPR048743
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
findings:
- finding_id: F1
  issue_key: coma-mcm21-family
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the Mcm21 subunit with its exact ortholog family
  description: IPR018464 is a full family explicitly including yeast Mcm21 and is
    cross-referenced by Q06675. The maintained Mcm21 row remains REVIEWED_LABEL_ONLY.
    AME1 and Ctf19 domain candidates do not justify assigning whole-protein groundings
    to those rows.
  target_ids:
  - GO:0000817
  field_paths:
  - components#mcm21_subunit
  evidence_ids:
  - record
  - curation
  - root48-sources-ipr-IPR018464
  - root48-sources-ipr-IPR048743
  - root48-sources-protein-Q02732
  - root48-sources-protein-P53298
  - root48-sources-protein-Q06675
  - root48-sources-protein-P38313
  - root48-sources-protein-P36012
  - root48-sources-protein-P40460
  - root48-sources-protein-P33895
  - root48-sources-protein-Q04477
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: minor
  normalization_reason: Bounded curation correction supported by exact current authorities
    or condition-scoped primary assays; structural identity is retained.
- finding_id: F2
  issue_key: coma-okp1-formation-evidence
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Capture the condition-scoped Okp1 assembly requirement
  description: The current UNKNOWN field omits direct stable-association evidence.
    DeWulf sec4 shows loss of the heterotetramer after restrictive okp1-5 inactivation;
    Schmitzberger sec11 shows a specific Okp1 interface is required for native Ctf19-Mcm21
    association while Ame1 and outer-kinetochore localization remain. These are physical-assembly
    observations rather than a growth-only inference.
  target_ids:
  - GO:0000817
  field_paths:
  - components#okp1_subunit.essentiality
  - components#okp1_subunit.evidence
  evidence_ids:
  - record
  - schema
  - root48-sources-dewulf2003-legacy
  - root48-sources-schmitzberger2017-legacy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
  rule_id: Exact component identity and source-specific biological support
  native_severity: minor
  normalization_reason: Bounded curation correction supported by exact current authorities
    or condition-scoped primary assays; structural identity is retained.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000817
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
  description: Add the exact Mcm21/CENP-O family mapping IPR018464 and preserve separate
    current uncertainty for the other three whole-protein families.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0000817
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/coma_complex.yaml
    role: maintained scientific record
  description: Curate a condition-scoped Okp1 formation requirement with the exact
    allele, temperature and interface contexts. Preserve the remaining subunits as
    UNKNOWN unless independently supported, and do not equate complete COMA assembly
    with universal viability.
  acceptance_checks:
  - Check exact source identifiers and reconcile the named current fields and associated
    TODO.
  - Preserve supported biology, taxon scope, assay limits and distinctions between
    identity and membership.
  - Use guarded curation and pass applicable schema, strict, protein and graph validation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Primary-body reading is limited to the sections explicitly named. No raw experimental
  data, supplementary datasets or sequence alignments were reanalyzed.
- Biggins2013, Ortiz1999 and Huh2003 are complete native abstract tier only. Modern
  K.lactis reconstitution and S.cerevisiae native experiments were kept distinct.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorizes all uncovered reviews, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
