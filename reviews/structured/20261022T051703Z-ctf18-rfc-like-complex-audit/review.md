# Ctf18 rfc like complex scientific review

- Review: 20261022T051703Z-ctf18-rfc-like-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:01:13Z
- Finished UTC: 2026-10-22T05:17:03Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Ctf18-RFC identity, seven yeast constituents and coarse clamp-loading/cohesion graph are supported. One minor finding resolves three exact component families, with shared RFC-family and primary-body limits retained.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph and completeness.

Selection: Target 10 of batch48 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031390 | data/structures/other/ctf18_rfc_like_complex.yaml | maintained | Ctf18 RFC-like complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0031390 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031390 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0031390 | Focused native check passed; identity and biological support assessed independently. |
| Focused native verify | passed | True | GO:0031390 | Focused native check passed; identity and biological support assessed independently. |
| Expression-module applicability | not_applicable | False | GO:0031390 | No maintained expression-module assertion requires this resource. |
| Claim-level scientific review | passed | True | GO:0031390 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031390 | 14 of 16 collected target identifiers returned OK. PMID:11389843: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14614842: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031390 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031390 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031390 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031390 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031390 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Seven-subunit Ctf18-RFC

identity: supported. Targets: GO:0031390.

GO identity, exact synonyms and nuclear-complex parent agree. Mayer2001 abstract directly identifies Ctf18/Ctf8/Dcc1 with Rfc2-5, excluding Rfc1/Rad24. The separate clamp PCNA is a substrate/client rather than an extra constituent.

### Three exact families versus shared clamp-loader family

grounding: concern. Targets: GO:0031390.

CTF18 IPR053016, Dcc1 IPR019128 and Ctf8 IPR018607 identify exact whole-protein classes. The CTF18 description is marked LLM and unchecked; it is not used as biological evidence. Its native family name/type/integrated signature and independent reviewed ortholog identities establish class identity. IPR050238 and RFC shared domains do not distinguish Rfc2/3/4/5.

### Seven correct yeast reference proteins

grounding: supported. Targets: GO:0031390.

Each exact reviewed gene query returns the maintained S288C accession. Native names/status/taxa and current Ctf8 nuclear citation agree. Shared membership in other RFC-like complexes does not invalidate these examples.

### Functional cohesion defects are not assembly tests

grounding: supported. Targets: GO:0031390.

The inspected Mayer abstract describes deletion-dependent cohesion and chromosome transmission phenotypes; it does not resolve physical complex persistence in every deletion. The maintained UNKNOWN values are conservative.

### Budding-yeast machinery and reference strain

scope: supported. Targets: GO:0031390.

GO and Mayer identify S.cerevisiae; narrower S288C example accessions do not imply that every cited experiment used that strain. COMMON is an ordinary-machinery assessment rather than a quantitative census.

### Clamp loading and cohesion remain coarse

evidence: supported. Targets: GO:0031390.

GO defines PCNA loading and cohesion. Native protein annotations and Mayer support the complex context. Kim/MacNeill is a brief review; its abstract does not itself resolve a complete loading mechanism.

### Explicit nonmechanistic function graph

graph: supported. Targets: GO:0031390.

The graph summarizes seven constituent contributions, clamp loading and cohesion without an ATPase cycle, PCNA ring-opening sequence or a claimed obligatory fork-recruitment mechanism.

### Resolve three exact families and retain body limits

completeness: supported. Targets: GO:0031390.

The stated heptamer inventory is complete. Three family mappings are actionable; the four small RFC paralogues remain unresolved at exact family level in the bounded current search.

## Findings

### F1: Ground Ctf18, Dcc1 and Ctf8 with exact families

minor / open / confirmed; issue key: ctf18-rfc-exact-family-subset.

Current family entries IPR053016, IPR019128 and IPR018607 identify Ctf18, Dcc1 and Ctf8. Their rows remain REVIEWED_LABEL_ONLY. The shared IPR050238 family and AAA/RFC domains are insufficient to distinguish the four small RFC paralogues. CTF18 family identity is separately checked from its unchecked generated description.

## Recommended Actions And Acceptance Checks

### A1

Curate the three exact class mappings and narrow the open family TODO to remaining unresolved paralogue identities. Retain the correct examples and avoid treating family annotation or generated prose as evidence of biological membership.

- Check exact source identifiers and reconcile the named current fields and associated TODO.
- Preserve supported biology, taxon scope, assay limits and distinctions between identity and membership.
- Use guarded curation and pass applicable schema, strict, protein and graph validation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/ctf18_rfc_like_complex.yaml; Entire maintained record including history, components, evidence, graph and discussions | context_only | All maintained fields were read. Historical curation notes document earlier decisions rather than independently proving current assertions. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component grounding, formation essentiality, taxonomic presence and graph scope | context_only | Whole-protein families differ from domains and individual examples. Assembly necessity differs from viability or function. COMMON means present in most members, with losses the exception; a qualitative ordinary-machinery assertion need not imply a numerical census. |
| curation | docs/CURATION.md; Exact identities and claim-specific evidence | context_only | A verified component identity and its membership in a complex require distinct support. Reviewed label-only status is reserved for the absence of an exact term; historical deferred searches can be revisited without alleging historical fabrication. |
| root48-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000228,GO:0000776,GO:0000817,GO:0003689,GO:0007062,GO:0017119,GO:0031390,GO:0031464,GO:0043494,GO:0048193,GO:0070912,GO:0080008,GO:0099023,GO:0140513; Complete maintained-term identity and definition fields and relevant typed links; not every descendant | supports | All14 requested GO identities, active status, definitions, synonyms, comments and relevant maintained typed relationships were inspected. The custom WDR1-specific assembly is distinct from the broader Cul4 parent. |
| root48-sources-doi-1 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2003.10.048%22&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED14614842: Genome stability: a new member of the RFC family. DOI 10.1016/j.cub.2003.10.048. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-pmid-11389843 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11389843+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED identity, authors/year/title/DOI and abstract | supports | MED11389843: Identification of RFC(Ctf18p, Ctf8p, Dcc1p): an alternative RFC complex required for sister chromatid cohesion in S. cerevisiae. DOI 10.1016/s1097-2765(01)00254-4. Complete bibliographic identity and abstract inspected; full-body access is certified only in separate evidence rows. |
| root48-sources-protein-P49956 | https://rest.uniprot.org/uniprotkb/P49956.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P49956 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P40348 | https://rest.uniprot.org/uniprotkb/P40348.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P40348 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P38629 | https://rest.uniprot.org/uniprotkb/P38629.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P38629 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P40339 | https://rest.uniprot.org/uniprotkb/P40339.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P40339 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P38251 | https://rest.uniprot.org/uniprotkb/P38251.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P38251 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P25559 | https://rest.uniprot.org/uniprotkb/P25559.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P25559 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-protein-P38877 | https://rest.uniprot.org/uniprotkb/P38877.json; Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR LOCATION, SIMILARITY comments; InterPro cross-references | supports | Native P38877 identity, entry status, names, genes/ORFs and taxon inspected, with available function, association and location annotations. Any mismatch is assessed explicitly; accession resolution alone does not establish membership. |
| root48-sources-gene-CTF18 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF18+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-RFC2 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC2+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-RFC3 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC3+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-RFC4 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC4+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-RFC5 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC5+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-DCC1 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADCC1+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-gene-CTF8 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF8+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=25; Complete query URL and every result accession/status/name/gene/taxon | supports | Exact reviewed gene query returns one matching yeast accession. Complete returned identity fields agree with the maintained example. |
| root48-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | Native taxon 4932 name, rank, lineage and synonym data inspected. Reference strains are distinguished from experimental strains. |
| root48-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | Native taxon 559292 name, rank, lineage and synonym data inspected. Reference strains are distinguished from experimental strains. |
| root48-sources-ipr-IPR053016 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR053016/; Complete accession/name/type/description, hierarchy, integrated signatures and curation flags | supports | IPR053016 is classified as family and named Chromosome transmission fidelity protein 18. Native metadata, full description and curation flags inspected. This row supports identity scope, not an independent primary biological experiment. |
| root48-sources-ipr-IPR019128 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019128/; Complete accession/name/type/description, hierarchy, integrated signatures and curation flags | supports | IPR019128 is classified as family and named Sister chromatid cohesion protein Dcc1. Native metadata, full description and curation flags inspected. This row supports identity scope, not an independent primary biological experiment. |
| root48-sources-ipr-IPR018607 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018607/; Complete accession/name/type/description, hierarchy, integrated signatures and curation flags | supports | IPR018607 is classified as family and named Chromosome transmission fidelity protein 8. Native metadata, full description and curation flags inspected. This row supports identity scope, not an independent primary biological experiment. |
| root48-sources-ipr-IPR050238 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/; Complete accession/name/type/description, hierarchy, integrated signatures and curation flags | supports | IPR050238 is classified as family and named DNA Replication and Repair Clamp Loader Complex. Native metadata, full description and curation flags inspected. This row supports identity scope, not an independent primary biological experiment. |
| root48-sources-family-members-IPR053016 | https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR053016+AND+reviewed%3Atrue&amp;format=json&amp;size=100&amp;fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name; Exact query and complete returned accession/protein/gene/organism identities | supports | All returned reviewed family-member identities inspected. The result establishes named ortholog classes across the returned taxa; it does not assert that the maintained S.cerevisiae example has this cross-reference. |
| schema-result | just validate data/structures/other/ctf18_rfc_like_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/ctf18_rfc_like_complex.yaml |
| strict-result | just validate-strict data/structures/other/ctf18_rfc_like_complex.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/ctf18_rfc_like_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/ctf18_rfc_like_complex.yaml --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/ctf18_rfc_like_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch48-20261022-ppyyf64c/ctf18_rfc_like_complex-strict.tsv |
| native-ctf18_rfc_like_complex-causal-graphs | /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ctf18_rfc_like_complex.yaml; Complete focused native report | supports | data/structures/other/ctf18_rfc_like_complex.yaml  (GO:0031390)<br>  ctf18_rfc_clamp_loading_and_cohesion	ctf18_subunit	COVERED	-&gt;ctf18_subunit (UniProtKB:P49956)<br>  ctf18_rfc_clamp_loading_and_cohesion	rfc2_subunit	COVERED	-&gt;rfc2_subunit (UniProtKB:P40348)<br>  ctf18_rfc_clamp_loading_and_cohesion	rfc3_subunit	COVERED	-&gt;rfc3_subunit (UniProtKB:P38629)<br>  ctf18_rfc_clamp_loading_and_cohesion	rfc4_subunit	COVERED	-&gt;rfc4_subunit (UniProtKB:P40339)<br>  ctf18_rfc_clamp_loading_and_cohesion	rfc5_subunit	COVERED	-&gt;rfc5_subunit (UniProtKB:P38251)<br>  ctf18_rfc_clamp_loading_and_cohesion	dcc1_subunit	COVERED	-&gt;dcc1_subunit (UniProtKB:P25559)<br>  ctf18_rfc_clamp_loading_and_cohesion	ctf8_subunit	COVERED	-&gt;ctf8_subunit (UniProtKB:P38877)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     7  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     7  total GENE_OR_PROTEIN causal nodes |
| native-ctf18_rfc_like_complex-verify | /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/ctf18_rfc_like_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/ctf18_rfc_like_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 16 collected target identifiers returned OK. PMID:11389843: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:14614842: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Primary-body reading is limited to the sections explicitly named. No raw experimental data, supplementary datasets or sequence alignments were reanalyzed.
- Mayer2001 and Kim/MacNeill2003 were independently read at complete native abstract tier only. Detailed purified loading assays, mutant assembly experiments and original microscopy were not certified.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes all uncovered reviews, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T051703Z-ctf18-rfc-like-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Ctf18 rfc like complex scientific review
started_at: '2026-10-22T05:01:13Z'
finished_at: '2026-10-22T05:17:03Z'
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
summary: Ctf18-RFC identity, seven yeast constituents and coarse clamp-loading/cohesion
  graph are supported. One minor finding resolves three exact component families,
  with shared RFC-family and primary-body limits retained.
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
  - path: data/structures/other/ctf18_rfc_like_complex.yaml
    sha256: abd597266840ca232631d6d1ca9478dda5ec941daf084b31e7815f4660cef6f3
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
- target_id: GO:0031390
  path: data/structures/other/ctf18_rfc_like_complex.yaml
  label: Ctf18 RFC-like complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ctf18_rfc_like_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph and completeness.
  selection: Target 10 of batch48 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031390
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031390
  command: just validate data/structures/other/ctf18_rfc_like_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031390
  command: just validate-strict data/structures/other/ctf18_rfc_like_complex.yaml
    --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/ctf18_rfc_like_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-ctf18_rfc_like_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0031390
  command: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ctf18_rfc_like_complex.yaml
  exit_code: 0
  summary: Focused native check passed; identity and biological support assessed independently.
  evidence_ids:
  - native-ctf18_rfc_like_complex-causal-graphs
- check_id: native-ctf18_rfc_like_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0031390
  command: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ctf18_rfc_like_complex.yaml
  exit_code: 0
  summary: Focused native check passed; identity and biological support assessed independently.
  evidence_ids:
  - native-ctf18_rfc_like_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0031390
  summary: No maintained expression-module assertion requires this resource.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031390
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root48-sources-go
  - root48-sources-doi-1
  - root48-sources-pmid-11389843
  - root48-sources-protein-P49956
  - root48-sources-protein-P40348
  - root48-sources-protein-P38629
  - root48-sources-protein-P40339
  - root48-sources-protein-P38251
  - root48-sources-protein-P25559
  - root48-sources-protein-P38877
  - root48-sources-gene-CTF18
  - root48-sources-gene-RFC2
  - root48-sources-gene-RFC3
  - root48-sources-gene-RFC4
  - root48-sources-gene-RFC5
  - root48-sources-gene-DCC1
  - root48-sources-gene-CTF8
  - root48-sources-tax4932
  - root48-sources-tax559292
  - root48-sources-ipr-IPR053016
  - root48-sources-ipr-IPR019128
  - root48-sources-ipr-IPR018607
  - root48-sources-ipr-IPR050238
  - root48-sources-family-members-IPR053016
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031390
  summary: '14 of 16 collected target identifiers returned OK. PMID:11389843: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:14614842:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force. Native source checks are separately scoped; skipped or unreachable identifiers
    are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root48-sources-pmid-11389843
  - root48-sources-doi-1
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031390
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
  - GO:0031390
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
  - GO:0031390
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
  - GO:0031390
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
  - GO:0031390
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
  reference: data/structures/other/ctf18_rfc_like_complex.yaml
  locator: Entire maintained record including history, components, evidence, graph
    and discussions
  accessed_at: '2026-10-22T05:13:38Z'
  support: context_only
  summary: All maintained fields were read. Historical curation notes document earlier
    decisions rather than independently proving current assertions.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component grounding, formation essentiality, taxonomic presence and graph
    scope
  accessed_at: '2026-10-22T05:13:38Z'
  support: context_only
  summary: Whole-protein families differ from domains and individual examples. Assembly
    necessity differs from viability or function. COMMON means present in most members,
    with losses the exception; a qualitative ordinary-machinery assertion need not
    imply a numerical census.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identities and claim-specific evidence
  accessed_at: '2026-10-22T05:13:38Z'
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
- evidence_id: root48-sources-doi-1
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2003.10.048%22&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:28.462684Z'
  support: supports
  summary: 'MED14614842: Genome stability: a new member of the RFC family. DOI 10.1016/j.cub.2003.10.048.
    Complete bibliographic identity and abstract inspected; full-body access is certified
    only in separate evidence rows.'
  snapshot_sha256: e04a0c76526d5d8132f75e5594abd5f3fe54f263cdd2f824ee0b4d1ef3c044f5
- evidence_id: root48-sources-pmid-11389843
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11389843+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED identity, authors/year/title/DOI and abstract
  accessed_at: '2026-10-22T05:04:30.371662Z'
  support: supports
  summary: 'MED11389843: Identification of RFC(Ctf18p, Ctf8p, Dcc1p): an alternative
    RFC complex required for sister chromatid cohesion in S. cerevisiae. DOI 10.1016/s1097-2765(01)00254-4.
    Complete bibliographic identity and abstract inspected; full-body access is certified
    only in separate evidence rows.'
  snapshot_sha256: f54addbf5314fcad1bfc5cde3cad5084b8003fb3a2a946ed970ebb5cb0fb9cca
- evidence_id: root48-sources-protein-P49956
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P49956.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:24.745013Z'
  support: supports
  summary: Native P49956 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 17fbd45ac56b77d7217359feda21a804a3db9d91e2bceb87b573c94bec6753c9
- evidence_id: root48-sources-protein-P40348
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40348.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:24.505718Z'
  support: supports
  summary: Native P40348 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: cd48db2abc9d05e4a2f8f7736b0aced77e8baa2465fb6a839d4f9e8ed95db94e
- evidence_id: root48-sources-protein-P38629
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38629.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:23.969177Z'
  support: supports
  summary: Native P38629 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 057ded2799f8c2aaf4cd34a49b0bd062aae33e6e6aa9ab81ec59b7c7d74937dd
- evidence_id: root48-sources-protein-P40339
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P40339.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:24.107190Z'
  support: supports
  summary: Native P40339 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 09609fcf78c540ff8073114b66b849691895e1fc7de9e81219d81dc51fcc35d7
- evidence_id: root48-sources-protein-P38251
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38251.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:23.366169Z'
  support: supports
  summary: Native P38251 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: bebaced0b8314c495257a26b5d1357bde108a903ac25fc337c51d4970294ff06
- evidence_id: root48-sources-protein-P25559
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P25559.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:23.214613Z'
  support: supports
  summary: Native P25559 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 50a48906aa61a282a8dea0ef8558efc5065eaf82877f919e17108c60e1a57ec9
- evidence_id: root48-sources-protein-P38877
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38877.json
  locator: Complete accession/status/name/genes/taxon and FUNCTION, SUBUNIT, SUBCELLULAR
    LOCATION, SIMILARITY comments; InterPro cross-references
  accessed_at: '2026-10-22T05:04:23.971251Z'
  support: supports
  summary: Native P38877 identity, entry status, names, genes/ORFs and taxon inspected,
    with available function, association and location annotations. Any mismatch is
    assessed explicitly; accession resolution alone does not establish membership.
  snapshot_sha256: 8207f0b46c1a2b1cf5bbc2a038840f091f1753eebe1f72d92c9d715a8dd4f44b
- evidence_id: root48-sources-gene-CTF18
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF18+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:19.644807Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: a4ab5388befbeda39e461e4a30196937ca7bbfbb0d2aaecb7701a7fe07458a86
- evidence_id: root48-sources-gene-RFC2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC2+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:20.530630Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: 5d37684d32d00b6803a2cbe7289849926576cd3f08cc74f6dd6ee2b3c1821068
- evidence_id: root48-sources-gene-RFC3
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC3+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:20.548226Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: a84d7bf13eddb61707649c22403a1d9540d4585cd07d07bb31fcbd5f54cff2c3
- evidence_id: root48-sources-gene-RFC4
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC4+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:20.599769Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: e4ac27ef43308dc3dd4c47939cb4856e61e23e412f8815e785cfb8d758e80a5c
- evidence_id: root48-sources-gene-RFC5
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ARFC5+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:21.438494Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: 7cfa80c9ae09adeac609a00eb5e3ddcecb79fc26d7ce7848ce2f6f772cfcaabb
- evidence_id: root48-sources-gene-DCC1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ADCC1+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:21.728565Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: e2e1ecc46110b84dd7b50f736495e29305f6dbd2a117b34aeea8d8abc069f4f4
- evidence_id: root48-sources-gene-CTF8
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ACTF8+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=25
  locator: Complete query URL and every result accession/status/name/gene/taxon
  accessed_at: '2026-10-22T05:06:21.769236Z'
  support: supports
  summary: Exact reviewed gene query returns one matching yeast accession. Complete
    returned identity fields agree with the maintained example.
  snapshot_sha256: 5f26e82ef1409a8fbf4006d2c55f5ef6f6ea1d272b7d9f8bb6abf00215a7fbc2
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
- evidence_id: root48-sources-ipr-IPR053016
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR053016/
  locator: Complete accession/name/type/description, hierarchy, integrated signatures
    and curation flags
  accessed_at: '2026-10-22T05:07:11.579591Z'
  support: supports
  summary: IPR053016 is classified as family and named Chromosome transmission fidelity
    protein 18. Native metadata, full description and curation flags inspected. This
    row supports identity scope, not an independent primary biological experiment.
  snapshot_sha256: d1d6815cae804e3055ebc8ef4c8172cda80d288d20e7adc5822e9fbd84508d7d
- evidence_id: root48-sources-ipr-IPR019128
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019128/
  locator: Complete accession/name/type/description, hierarchy, integrated signatures
    and curation flags
  accessed_at: '2026-10-22T05:06:13.069467Z'
  support: supports
  summary: IPR019128 is classified as family and named Sister chromatid cohesion protein
    Dcc1. Native metadata, full description and curation flags inspected. This row
    supports identity scope, not an independent primary biological experiment.
  snapshot_sha256: fd649e6f522442733dee8c7a873a40ddebe01605c22727dd96d58c693f5581fd
- evidence_id: root48-sources-ipr-IPR018607
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR018607/
  locator: Complete accession/name/type/description, hierarchy, integrated signatures
    and curation flags
  accessed_at: '2026-10-22T05:06:12.915965Z'
  support: supports
  summary: IPR018607 is classified as family and named Chromosome transmission fidelity
    protein 8. Native metadata, full description and curation flags inspected. This
    row supports identity scope, not an independent primary biological experiment.
  snapshot_sha256: cd1fcec19c09b0c0149e1a9934d739fe8a528dbc220a0a6642a67fdfc03c3516
- evidence_id: root48-sources-ipr-IPR050238
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR050238/
  locator: Complete accession/name/type/description, hierarchy, integrated signatures
    and curation flags
  accessed_at: '2026-10-22T05:06:16.632804Z'
  support: supports
  summary: IPR050238 is classified as family and named DNA Replication and Repair
    Clamp Loader Complex. Native metadata, full description and curation flags inspected.
    This row supports identity scope, not an independent primary biological experiment.
  snapshot_sha256: 20cc681dc2b5aa75e096f21d298105d7ac05cc910f786be9e1f63ae05a72dbc0
- evidence_id: root48-sources-family-members-IPR053016
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=xref%3Ainterpro-IPR053016+AND+reviewed%3Atrue&format=json&size=100&fields=accession%2Cprotein_name%2Cgene_names%2Corganism_name
  locator: Exact query and complete returned accession/protein/gene/organism identities
  accessed_at: '2026-10-22T05:08:27.502072Z'
  support: supports
  summary: All returned reviewed family-member identities inspected. The result establishes
    named ortholog classes across the returned taxa; it does not assert that the maintained
    S.cerevisiae example has this cross-reference.
  snapshot_sha256: 4899d18d633743f5a948e97278ee99912cd2af714394decc935ec29caac43671
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/ctf18_rfc_like_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:01:15Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/ctf18_rfc_like_complex.yaml'
  snapshot_sha256: 686fe09c81ad7d5119075564ba1f92cc4501689012993fad6ce48fc267142879
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/ctf18_rfc_like_complex.yaml
    --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/ctf18_rfc_like_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:01:16Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/ctf18_rfc_like_complex.yaml\
    \ --out /private/tmp/cellstructure-batch48-20261022-ppyyf64c/ctf18_rfc_like_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch48-20261022-ppyyf64c/ctf18_rfc_like_complex-strict.tsv"
  snapshot_sha256: 4d814c4757a2bcbaa33406a2765a50aa8952a435f1c0330ae334192ca6c8d302
- evidence_id: native-ctf18_rfc_like_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ctf18_rfc_like_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:06:18.919420Z'
  support: supports
  summary: "data/structures/other/ctf18_rfc_like_complex.yaml  (GO:0031390)\n  ctf18_rfc_clamp_loading_and_cohesion\t\
    ctf18_subunit\tCOVERED\t->ctf18_subunit (UniProtKB:P49956)\n  ctf18_rfc_clamp_loading_and_cohesion\t\
    rfc2_subunit\tCOVERED\t->rfc2_subunit (UniProtKB:P40348)\n  ctf18_rfc_clamp_loading_and_cohesion\t\
    rfc3_subunit\tCOVERED\t->rfc3_subunit (UniProtKB:P38629)\n  ctf18_rfc_clamp_loading_and_cohesion\t\
    rfc4_subunit\tCOVERED\t->rfc4_subunit (UniProtKB:P40339)\n  ctf18_rfc_clamp_loading_and_cohesion\t\
    rfc5_subunit\tCOVERED\t->rfc5_subunit (UniProtKB:P38251)\n  ctf18_rfc_clamp_loading_and_cohesion\t\
    dcc1_subunit\tCOVERED\t->dcc1_subunit (UniProtKB:P25559)\n  ctf18_rfc_clamp_loading_and_cohesion\t\
    ctf8_subunit\tCOVERED\t->ctf8_subunit (UniProtKB:P38877)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     7  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     7  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: b77337cdd5a7bc8793f4ed2e383dc3ecee05ecee0677dc4c1b3314167dd0a613
- evidence_id: native-ctf18_rfc_like_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch48-20261022-ppyyf64c/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ctf18_rfc_like_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T05:06:20.592721Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/ctf18_rfc_like_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '14 of 16 collected target identifiers returned OK. PMID:11389843: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:14614842:
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
  topic: Seven-subunit Ctf18-RFC
  outcome: supported
  target_ids:
  - GO:0031390
  summary: GO identity, exact synonyms and nuclear-complex parent agree. Mayer2001
    abstract directly identifies Ctf18/Ctf8/Dcc1 with Rfc2-5, excluding Rfc1/Rad24.
    The separate clamp PCNA is a substrate/client rather than an extra constituent.
  evidence_ids:
  - record
  - root48-sources-go
  - root48-sources-doi-1
  - root48-sources-pmid-11389843
- assessment_id: families
  area: grounding
  topic: Three exact families versus shared clamp-loader family
  outcome: concern
  target_ids:
  - GO:0031390
  summary: CTF18 IPR053016, Dcc1 IPR019128 and Ctf8 IPR018607 identify exact whole-protein
    classes. The CTF18 description is marked LLM and unchecked; it is not used as
    biological evidence. Its native family name/type/integrated signature and independent
    reviewed ortholog identities establish class identity. IPR050238 and RFC shared
    domains do not distinguish Rfc2/3/4/5.
  evidence_ids:
  - record
  - curation
  - root48-sources-ipr-IPR053016
  - root48-sources-ipr-IPR019128
  - root48-sources-ipr-IPR018607
  - root48-sources-ipr-IPR050238
  - root48-sources-family-members-IPR053016
  - root48-sources-protein-P49956
  - root48-sources-protein-P40348
  - root48-sources-protein-P38629
  - root48-sources-protein-P40339
  - root48-sources-protein-P38251
  - root48-sources-protein-P25559
  - root48-sources-protein-P38877
- assessment_id: examples
  area: grounding
  topic: Seven correct yeast reference proteins
  outcome: supported
  target_ids:
  - GO:0031390
  summary: Each exact reviewed gene query returns the maintained S288C accession.
    Native names/status/taxa and current Ctf8 nuclear citation agree. Shared membership
    in other RFC-like complexes does not invalidate these examples.
  evidence_ids:
  - record
  - root48-sources-protein-P49956
  - root48-sources-protein-P40348
  - root48-sources-protein-P38629
  - root48-sources-protein-P40339
  - root48-sources-protein-P38251
  - root48-sources-protein-P25559
  - root48-sources-protein-P38877
  - root48-sources-gene-CTF18
  - root48-sources-gene-RFC2
  - root48-sources-gene-RFC3
  - root48-sources-gene-RFC4
  - root48-sources-gene-RFC5
  - root48-sources-gene-DCC1
  - root48-sources-gene-CTF8
  - root48-sources-tax4932
  - root48-sources-tax559292
  - root48-sources-doi-1
  - root48-sources-pmid-11389843
- assessment_id: necessity
  area: grounding
  topic: Functional cohesion defects are not assembly tests
  outcome: supported
  target_ids:
  - GO:0031390
  summary: The inspected Mayer abstract describes deletion-dependent cohesion and
    chromosome transmission phenotypes; it does not resolve physical complex persistence
    in every deletion. The maintained UNKNOWN values are conservative.
  evidence_ids:
  - record
  - schema
  - root48-sources-doi-1
  - root48-sources-pmid-11389843
- assessment_id: scope
  area: scope
  topic: Budding-yeast machinery and reference strain
  outcome: supported
  target_ids:
  - GO:0031390
  summary: GO and Mayer identify S.cerevisiae; narrower S288C example accessions do
    not imply that every cited experiment used that strain. COMMON is an ordinary-machinery
    assessment rather than a quantitative census.
  evidence_ids:
  - record
  - schema
  - root48-sources-go
  - root48-sources-doi-1
  - root48-sources-pmid-11389843
  - root48-sources-tax4932
  - root48-sources-tax559292
- assessment_id: function
  area: evidence
  topic: Clamp loading and cohesion remain coarse
  outcome: supported
  target_ids:
  - GO:0031390
  summary: GO defines PCNA loading and cohesion. Native protein annotations and Mayer
    support the complex context. Kim/MacNeill is a brief review; its abstract does
    not itself resolve a complete loading mechanism.
  evidence_ids:
  - record
  - root48-sources-go
  - root48-sources-doi-1
  - root48-sources-pmid-11389843
  - root48-sources-protein-P49956
  - root48-sources-protein-P40348
  - root48-sources-protein-P38629
  - root48-sources-protein-P40339
  - root48-sources-protein-P38251
  - root48-sources-protein-P25559
  - root48-sources-protein-P38877
- assessment_id: graph
  area: graph
  topic: Explicit nonmechanistic function graph
  outcome: supported
  target_ids:
  - GO:0031390
  summary: The graph summarizes seven constituent contributions, clamp loading and
    cohesion without an ATPase cycle, PCNA ring-opening sequence or a claimed obligatory
    fork-recruitment mechanism.
  evidence_ids:
  - record
  - root48-sources-go
  - root48-sources-doi-1
  - root48-sources-pmid-11389843
- assessment_id: coverage
  area: completeness
  topic: Resolve three exact families and retain body limits
  outcome: supported
  target_ids:
  - GO:0031390
  summary: The stated heptamer inventory is complete. Three family mappings are actionable;
    the four small RFC paralogues remain unresolved at exact family level in the bounded
    current search.
  evidence_ids:
  - record
  - root48-sources-ipr-IPR053016
  - root48-sources-ipr-IPR019128
  - root48-sources-ipr-IPR018607
  - root48-sources-ipr-IPR050238
findings:
- finding_id: F1
  issue_key: ctf18-rfc-exact-family-subset
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground Ctf18, Dcc1 and Ctf8 with exact families
  description: Current family entries IPR053016, IPR019128 and IPR018607 identify
    Ctf18, Dcc1 and Ctf8. Their rows remain REVIEWED_LABEL_ONLY. The shared IPR050238
    family and AAA/RFC domains are insufficient to distinguish the four small RFC
    paralogues. CTF18 family identity is separately checked from its unchecked generated
    description.
  target_ids:
  - GO:0031390
  field_paths:
  - components#ctf18_subunit
  - components#dcc1_subunit
  - components#ctf8_subunit
  - discussions#resolve_ctf18_rfc_subunit_groundings
  evidence_ids:
  - record
  - curation
  - root48-sources-ipr-IPR053016
  - root48-sources-ipr-IPR019128
  - root48-sources-ipr-IPR018607
  - root48-sources-ipr-IPR050238
  - root48-sources-family-members-IPR053016
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ctf18_rfc_like_complex.yaml
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
  - GO:0031390
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ctf18_rfc_like_complex.yaml
    role: maintained scientific record
  description: Curate the three exact class mappings and narrow the open family TODO
    to remaining unresolved paralogue identities. Retain the correct examples and
    avoid treating family annotation or generated prose as evidence of biological
    membership.
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
- Mayer2001 and Kim/MacNeill2003 were independently read at complete native abstract
  tier only. Detailed purified loading assays, mutant assembly experiments and original
  microscopy were not certified.
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
