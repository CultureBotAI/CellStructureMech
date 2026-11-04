# AP-1 adaptor complex scientific review

- Review: 20261022T043541Z-ap-1-adaptor-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:15:16Z
- Finished UTC: 2026-10-22T04:35:41Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Two minor findings: verified AP1 gamma/sigma family groundings are withheld under reviewed-label-only status, and APS1 query uniqueness is overstated. Correct complex/protein identities and scoped biology remain supported.

## Scope And Provenance

Exactly one complete AP-1 record with frozen guidance/schema, exact native identities, all maintained component/example/function/graph/evidence claims and source sections listed in evidence. No uninspected figure pixels, supplementary experiments or universal taxon inventory are claimed.

Selection: Batch44 strict path-ordered target 7; all initial native inspection/schema/strict gates passed at unchanged f97b before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030121 | data/structures/other/ap_1_adaptor_complex.yaml | maintained | AP-1 adaptor complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030121 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030121 | Focused validator passed. |
| Native verify | passed | True | GO:0030121 | Native diagnostic passed; claim-level science and optional coverage are assessed separately. |
| Native causal-graphs | passed | True | GO:0030121 | Native diagnostic passed; claim-level science and optional coverage are assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0030121 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0030121 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030121 | 12 of 12 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030121 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030121 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030121 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030121 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030121 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Correct four identities with one inaccurate uniqueness note

evidence: concern. Targets: GO:0030121.

All four accession/gene/taxon/status identities and AP1 memberships are supported. APL2/APL4/APM1 queries are unique; APS1 returns two entries because DPS1 also carries the APS1 alias. The current P35181 evidence note incorrectly calls it the single reviewed entry, while its role correctly says representative. Historical seeding provenance is not rewritten.

### Yeast occurrence, experimental backgrounds and alternate mu chains

scope: supported. Targets: GO:0030121.

Species and S288C reference identities are correct. COMMON retains its schema meaning of presence in most members with losses exceptional; ordinary yeast characterization supports this qualitative synthesis without a measured strain-prevalence census. GPY/SEY and BY4741/BY4742 experiments are not relabeled as S288C. APM1 is a supported representative of the mu1 class, not an assertion that APM2 never occurs.

### NONMECHANISTIC topology and cargo-specific sorting

graph: supported. Targets: GO:0030121.

All six edges summarize constituent membership, GO coat parthood and source-supported late-Golgi/Golgi-early-endosome sorting. The graph does not require AP1 for every clathrin event. Mil1 remains regulatory machinery, not a fifth heterotetrameric constituent; specific binding and recruitment do not imply a new stable core-subunit class.

### Exact AP-1 heterotetramer and containing-structure boundaries

identity: supported. Targets: GO:0030121.

The maintained definition, ontology identity, parentage, subtype-specific core classes and any coat parthood match the native GO authority. Different AP subtypes and containing coats remain distinct; no identity remapping is warranted.

### Exact subtype families versus deferred broader candidates

grounding: concern. Targets: GO:0030121.

Native family entries support ap1_gamma_subunit → InterPro:IPR017107, ap1_sigma1_subunit → InterPro:IPR044733. These are complete subtype-specific family classes, not merely domains or species-specific proteins, so their current REVIEWED_LABEL_ONLY status is not justified by saying no CURIE was curated in a prior pass. The other broader candidates do not close every remaining subunit class. Biological membership and identity remain supported.

### Constituent identity separated from assembly necessity

evidence: unknown. Targets: GO:0030121.

All four components use UNKNOWN essentiality. The evidence supports the four named constituent classes; transport phenotypes, viability outcomes, interaction assays and reconstituted activity do not independently establish universal formation necessity for every subunit. UNKNOWN is retained rather than replaced by an inferred requirement.

### All maintained fields and bounded source availability

completeness: supported. Targets: GO:0030121.

All target fields and explicit evidence placements were inspected. The four core components are represented. Missing additional taxa, isoforms or exhaustive accessory-protein inventories are not treated as defects; exact-family findings are limited to independently verified matches and the explicit label-only contract.

## Findings

### F1: Ground the verified AP-1 subtype-specific subunit families

minor / open / confirmed; issue key: ap1-verified-subtype-families-label-only.

Exact native InterPro family identities are available for ap1_gamma_subunit → InterPro:IPR017107, ap1_sigma1_subunit → InterPro:IPR044733. The affected components nevertheless carry REVIEWED_LABEL_ONLY and notes saying no exact CURIE was curated in the prior pass. CURATION and schema define this status as no exact assertable family, not deferred curation. The native family types/descriptions match the component classes; other unresolved broad families and domains are not promoted.

### F2: Qualify the APS1 single-entry evidence note

minor / open / confirmed; issue key: ap1-aps1-reviewed-query-not-unique.

The current exact reviewed APS1 query at taxon559292 returns two entries: the correct AP1 sigma P35181 with primary APS1 and P04802 with primary DPS1 and APS1 as an alias. The maintained P35181 evidence note says single reviewed entry, although its role already says representative. This is an inaccurate current query-resolution claim, not a wrong protein accession or subunit membership.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, add the verified mappings ap1_gamma_subunit → InterPro:IPR017107, ap1_sigma1_subunit → InterPro:IPR044733; remove the obsolete reviewed-label-only status/notes on those mapped rows and narrow the existing TODO to unresolved classes. Preserve the exact complex, roles, examples and UNKNOWN formation necessity; do not force broad beta/mu/sigma or domain entries onto other subtype classes.

- Each added CURIE resolves to the stated native subtype-specific family, with current identifier/label correspondence.
- Only the verified classes lose reviewed-label-only status; genuinely unresolved classes and their bounded TODO remain.
- Focused schema/strict, protein/graph diagnostics and source-placement checks pass after authorized curation.

### A2

In separately authorized curation, retain P35181 and its APS1/S288C identity, but describe it as the verified representative with primary gene APS1 and explicitly distinguish the DPS1 alias hit if query resolution is discussed. Do not alter historical seeding provenance or substitute P04802.

- The current evidence note no longer claims that the alias-inclusive reviewed APS1 query has one result.
- P35181 remains linked to AP1 sigma with the correct taxon and primary gene; native protein verification passes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/ap_1_adaptor_complex.yaml; Entire maintained target, including all history, components, examples, evidence, functions, graph and discussions | context_only | Complete target read. Historical actions are provenance rather than independent experimental support. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent grounding/status and essentiality; graph and protein-example contracts | context_only | A reviewed label-only component means no exact family can be asserted; membership and biological activity do not establish individual assembly necessity. |
| curation | docs/CURATION.md; Grounding and REVIEWED_LABEL_ONLY rules, lines150–162 | context_only | The status represents a checked absence of an exact assertable term, not merely an identifier that was not curated in a prior pass. |
| ap44-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030121,GO:0030122,GO:0030123,GO:0030124,GO:0030119,GO:0030131,GO:0098797,GO:0030130,GO:0030128,GO:0030132,GO:0072583; All eleven returned IDs/names/active states/definitions/synonyms and the typed child entries corresponding to maintained parent/parthood links | supports | The eleven native terms exactly identify AP1–AP4, their named subunits and isoform qualifiers, AP-type/clathrin-adaptor parents, AP2 plasma-membrane-complex parent, AP1/AP2 typed coat parthood, and clathrin-dependent endocytosis. The AP3/AP4 definitions retain qualified clathrin association. Typed links were read from the exact parent children; unrelated children are not an exhaustive review scope. |
| ap44-agent-family-search-AP1 | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-1&amp;page_size=100; Complete returned candidate accession/name/type list and pagination | context_only | Bounded native InterPro search for AP-1 returned 12 entries with no next page. Names/types identify candidate adaptor families, alongside unrelated text matches and domains; exact candidate entries are verified separately. This is not an exhaustive search of all protein-family resources. |
| ap44-agent-ipr-IPR017107 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017107/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR017107 is type family, named Adaptor protein complex AP-1, gamma subunit. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-ipr-IPR044733 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044733/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR044733 is type family, named AP-1 complex subunit sigma. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-ipr-IPR016342 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016342/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR016342 is type family, named AP-1/2/4 complex subunit beta. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-ipr-IPR001392 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001392/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR001392 is type family, named Clathrin adaptor, mu subunit. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-ipr-IPR016635 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016635/; Complete accession/name/type, description and LLM flags, integrated member signatures and hierarchy | supports | IPR016635 is type family, named Adaptor protein complex, sigma subunit. Its complete native description and integrated signatures were read to distinguish the named subunit class from broader adaptor families or partial domains. |
| ap44-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA 4932 identifies Saccharomyces cerevisiae, rank species. This verifies the named taxon, not a prevalence measurement or the strain used in every assay. |
| ap44-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | ENA 559292 identifies Saccharomyces cerevisiae S288C, rank strain. This verifies the named taxon, not a prevalence measurement or the strain used in every assay. |
| ap44-agent-yeung1999-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.10.11.3643&amp;format=json&amp;resultType=core; Unique Europe PMC MED bibliographic record: exact DOI/PMID/PMC if returned, authors/title/year and complete abstract | supports | Yeung, Phan and Payne1999, DOI10.1091/mbc.10.11.3643/PMID10564262/PMC25654. The abstract distinguishes physical AP1-clathrin association from AP-complex dispensability for tested clathrin functions under normal yeast conditions. |
| ap44-agent-valdivia2002-meta-exact | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2FS1534-5807%2802%2900127-2%22&amp;format=json&amp;resultType=core; Unique Europe PMC MED bibliographic record: exact DOI/PMID/PMC if returned, authors/title/year and complete abstract | supports | Valdivia, Baggott, Chuang and Schekman2002, DOI10.1016/S1534-5807(02)00127-2/PMID11879634. The complete abstract supports Chs3/Tlg1 retention and proposes early-endosome-to-TGN recycling; no full Methods or new route proof is claimed. |
| ap44-agent-whitfield2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.e15-09-0621&amp;format=json&amp;resultType=core; Unique Europe PMC MED bibliographic record: exact DOI/PMID/PMC if returned, authors/title/year and complete abstract | supports | Whitfield et al.2016, DOI10.1091/mbc.e15-09-0621/PMID26658609/PMC4751606. The complete abstract identifies alternate Apm1/Apm2 forms, distinct sorting outcomes and Mil1-dependent Apm2 recruitment. |
| ap44-agent-yeung1999-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC25654/?report=xml; Genuine complete PMC HTML: Methods sec20 including Table3 and sec21; Results sec27,sec29,sec30 including Figure1/2 captions; entire Discussion sec33. Other Methods/Results, pixels and underlying unpublished observations not independently inspected. | supports | Primary native coimmunoprecipitation identifies Apl2/Apl4/Apm1/Aps1, and binding/coimmunoprecipitation identifies AP1-clathrin association. Apm2 association was conditional in early experiments. The Discussion explicitly preserves lack of tested sorting defects in normal-clathrin AP1-deleted cells, so association is not universal necessity for clathrin function. Strains are GPY/SEY-derived experimental lines. |
| ap44-agent-whitfield2016-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC4751606/?report=xml; Genuine complete PMC HTML: entire Introduction sec1, Results sec3–8, Discussion sec9 and Methods sec11–20, including Figure1–6 captions. Supplementary files, image pixels and underlying cited experiments not read. | supports | Primary yeast deletion, localization, binding and recruitment results distinguish AP1 from Apm2-containing AP1R and support cargo-specific sorting. Mil1 binds Apm2, contributes to membrane recruitment and has a predicted rather than demonstrated lipase activity; the proposed microdomain model remains hypothetical. BY4741/BY4742 strains and specific assays are described. |
| ap44-agent-protein-P36000 | https://rest.uniprot.org/uniprotkb/P36000.json; Exact native identity/status/name/genes/taxon, SUBUNIT/FUNCTION/location comments and family crossrefs | supports | P36000 is a reviewed AP1 subunit with primary gene APL2, organism559292, matching the maintained accession/name/gene/taxon/status. Native SUBUNIT and FUNCTION comments link the experimental Yeung1999 membership annotation; annotations of other locations are not substituted for that primary membership evidence. |
| ap44-agent-gene-APL2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned UniProt entries and primary/synonym gene fields | context_only | The exact reviewed APL2 query at organism559292 returns the single expected P36000. |
| ap44-agent-protein-Q12028 | https://rest.uniprot.org/uniprotkb/Q12028.json; Exact native identity/status/name/genes/taxon, SUBUNIT/FUNCTION/location comments and family crossrefs | supports | Q12028 is a reviewed AP1 subunit with primary gene APL4, organism559292, matching the maintained accession/name/gene/taxon/status. Native SUBUNIT and FUNCTION comments link the experimental Yeung1999 membership annotation; annotations of other locations are not substituted for that primary membership evidence. |
| ap44-agent-gene-APL4 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned UniProt entries and primary/synonym gene fields | context_only | The exact reviewed APL4 query at organism559292 returns the single expected Q12028. |
| ap44-agent-protein-Q00776 | https://rest.uniprot.org/uniprotkb/Q00776.json; Exact native identity/status/name/genes/taxon, SUBUNIT/FUNCTION/location comments and family crossrefs | supports | Q00776 is a reviewed AP1 subunit with primary gene APM1, organism559292, matching the maintained accession/name/gene/taxon/status. Native SUBUNIT and FUNCTION comments link the experimental Yeung1999 membership annotation; annotations of other locations are not substituted for that primary membership evidence. |
| ap44-agent-gene-APM1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned UniProt entries and primary/synonym gene fields | context_only | The exact reviewed APM1 query at organism559292 returns the single expected Q00776. |
| ap44-agent-protein-P35181 | https://rest.uniprot.org/uniprotkb/P35181.json; Exact native identity/status/name/genes/taxon, SUBUNIT/FUNCTION/location comments and family crossrefs | supports | P35181 is a reviewed AP1 subunit with primary gene APS1, organism559292, matching the maintained accession/name/gene/taxon/status. Native SUBUNIT and FUNCTION comments link the experimental Yeung1999 membership annotation; annotations of other locations are not substituted for that primary membership evidence. |
| ap44-agent-gene-APS1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete returned UniProt entries and primary/synonym gene fields | context_only | The exact reviewed APS1 query at organism559292 returns P35181 (primary APS1) and P04802 (primary DPS1, APS1 alias). P35181 remains the correct AP1 sigma representative; the raw query is not unique. |
| schema-result | just validate data/structures/other/ap_1_adaptor_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/ap_1_adaptor_complex.yaml |
| strict-result | just validate-strict data/structures/other/ap_1_adaptor_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_1_adaptor_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/ap_1_adaptor_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_1_adaptor_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_1_adaptor_complex-strict.tsv |
| ap1-verify | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/ap_1_adaptor_complex.yaml; Complete native read-only diagnostic log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| ap1-causal-graphs | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_1_adaptor_complex.yaml; Complete native read-only diagnostic log | supports | data/structures/other/ap_1_adaptor_complex.yaml  (GO:0030121)<br>  ap1_adaptor_complex_topology	ap1_beta1_subunit	COVERED	-&gt;ap1_beta1_subunit (UniProtKB:P36000)<br>  ap1_adaptor_complex_topology	ap1_gamma_subunit	COVERED	-&gt;ap1_gamma_subunit (UniProtKB:Q12028)<br>  ap1_adaptor_complex_topology	ap1_mu1_subunit	COVERED	-&gt;ap1_mu1_subunit (UniProtKB:Q00776)<br>  ap1_adaptor_complex_topology	ap1_sigma1_subunit	COVERED	-&gt;ap1_sigma1_subunit (UniProtKB:P35181)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/ap_1_adaptor_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 12 of 12 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- The five complete same-base batch26 corpus gates await guarded integration by the parent before finalization.
- No image pixels, new sequence alignments, supplementary datasets or quantitative prevalence census were inspected. Exact source-reading sections are declared individually.
- The native family search is bounded to the listed InterPro text query and separately retrieved exact entries. Broad beta1/2/4, mu and sigma families or partial domains do not establish an exact subtype mapping for every remaining component; no all-catalog absence is claimed.
- Valdivia2002 was read at complete native MED abstract scope only. Its DOI route failed TLS certificate verification; no full body is claimed. The initial unquoted DOI query returned zero results, superseded by the exact quoted DOI query; this was query syntax, not an absent citation.
- The S288C protein references establish identity and annotated membership; the original Yeung and Whitfield assays used their explicitly stated experimental backgrounds. Native APS1 ambiguity does not invalidate P35181 or its AP1 membership.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes this review bundle. Parent owns same-base global-gate integration and later finalization; no scientific edits or persistence performed.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T043541Z-ap-1-adaptor-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: AP-1 adaptor complex scientific review
started_at: '2026-10-22T04:15:16Z'
finished_at: '2026-10-22T04:35:41Z'
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
summary: 'Two minor findings: verified AP1 gamma/sigma family groundings are withheld
  under reviewed-label-only status, and APS1 query uniqueness is overstated. Correct
  complex/protein identities and scoped biology remain supported.'
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
  - path: data/structures/other/ap_1_adaptor_complex.yaml
    sha256: 07e8041b35a2b239cc863b961dcea341b80d8b9afc3db0482cf001a4d3f1c03e
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
- target_id: GO:0030121
  path: data/structures/other/ap_1_adaptor_complex.yaml
  label: AP-1 adaptor complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_1_adaptor_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete AP-1 record with frozen guidance/schema, exact
    native identities, all maintained component/example/function/graph/evidence claims
    and source sections listed in evidence. No uninspected figure pixels, supplementary
    experiments or universal taxon inventory are claimed.
  selection: Batch44 strict path-ordered target 7; all initial native inspection/schema/strict
    gates passed at unchanged f97b before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030121
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030121
  command: just validate data/structures/other/ap_1_adaptor_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030121
  command: just validate-strict data/structures/other/ap_1_adaptor_complex.yaml --out
    /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_1_adaptor_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0030121
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ap_1_adaptor_complex.yaml
  exit_code: 0
  summary: Native diagnostic passed; claim-level science and optional coverage are
    assessed separately.
  evidence_ids:
  - ap1-verify
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030121
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_1_adaptor_complex.yaml
  exit_code: 0
  summary: Native diagnostic passed; claim-level science and optional coverage are
    assessed separately.
  evidence_ids:
  - ap1-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030121
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030121
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - ap44-agent-go
  - ap44-agent-family-search-AP1
  - ap44-agent-ipr-IPR017107
  - ap44-agent-ipr-IPR044733
  - ap44-agent-ipr-IPR016342
  - ap44-agent-ipr-IPR001392
  - ap44-agent-ipr-IPR016635
  - ap44-agent-tax4932
  - ap44-agent-tax559292
  - ap44-agent-yeung1999-meta
  - ap44-agent-valdivia2002-meta-exact
  - ap44-agent-whitfield2016-meta
  - ap44-agent-yeung1999-legacy
  - ap44-agent-whitfield2016-legacy
  - ap44-agent-protein-P36000
  - ap44-agent-gene-APL2
  - ap44-agent-protein-Q12028
  - ap44-agent-gene-APL4
  - ap44-agent-protein-Q00776
  - ap44-agent-gene-APM1
  - ap44-agent-protein-P35181
  - ap44-agent-gene-APS1
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030121
  summary: 12 of 12 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030121
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0030121
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0030121
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0030121
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0030121
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
    and current batch44 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/ap_1_adaptor_complex.yaml
  locator: Entire maintained target, including all history, components, examples,
    evidence, functions, graph and discussions
  accessed_at: '2026-10-22T04:20:28Z'
  support: context_only
  summary: Complete target read. Historical actions are provenance rather than independent
    experimental support.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent grounding/status and essentiality; graph and protein-example
    contracts
  accessed_at: '2026-10-22T04:20:28Z'
  support: context_only
  summary: A reviewed label-only component means no exact family can be asserted;
    membership and biological activity do not establish individual assembly necessity.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Grounding and REVIEWED_LABEL_ONLY rules, lines150–162
  accessed_at: '2026-10-22T04:20:28Z'
  support: context_only
  summary: The status represents a checked absence of an exact assertable term, not
    merely an identifier that was not curated in a prior pass.
- evidence_id: ap44-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030121,GO:0030122,GO:0030123,GO:0030124,GO:0030119,GO:0030131,GO:0098797,GO:0030130,GO:0030128,GO:0030132,GO:0072583
  locator: All eleven returned IDs/names/active states/definitions/synonyms and the
    typed child entries corresponding to maintained parent/parthood links
  accessed_at: '2026-10-22T04:15:34.948559Z'
  support: supports
  summary: The eleven native terms exactly identify AP1–AP4, their named subunits
    and isoform qualifiers, AP-type/clathrin-adaptor parents, AP2 plasma-membrane-complex
    parent, AP1/AP2 typed coat parthood, and clathrin-dependent endocytosis. The AP3/AP4
    definitions retain qualified clathrin association. Typed links were read from
    the exact parent children; unrelated children are not an exhaustive review scope.
  snapshot_sha256: 3d9d1876f519efc4b9ea1714babdee7f40389f9729404bfc2b51810c509cffba
- evidence_id: ap44-agent-family-search-AP1
  kind: search
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-1&page_size=100
  locator: Complete returned candidate accession/name/type list and pagination
  accessed_at: '2026-10-22T04:18:12.765151Z'
  support: context_only
  summary: Bounded native InterPro search for AP-1 returned 12 entries with no next
    page. Names/types identify candidate adaptor families, alongside unrelated text
    matches and domains; exact candidate entries are verified separately. This is
    not an exhaustive search of all protein-family resources.
  snapshot_sha256: 0e29b5f43f56635c834835fce2a99dc7de01e9b974dbb1f120285f442bb108f2
  search_scope: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=AP-1&page_size=100
- evidence_id: ap44-agent-ipr-IPR017107
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR017107/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:16:34.048033Z'
  support: supports
  summary: IPR017107 is type family, named Adaptor protein complex AP-1, gamma subunit.
    Its complete native description and integrated signatures were read to distinguish
    the named subunit class from broader adaptor families or partial domains.
  snapshot_sha256: fab955bf78f1eefcb2cc4fd0112adc1e0154c048f07719a85f31919f13d95293
- evidence_id: ap44-agent-ipr-IPR044733
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044733/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:16:34.048528Z'
  support: supports
  summary: IPR044733 is type family, named AP-1 complex subunit sigma. Its complete
    native description and integrated signatures were read to distinguish the named
    subunit class from broader adaptor families or partial domains.
  snapshot_sha256: e9db8af667dede05c7cad0050ffc67949e353fb6402dfc86fc715ebe82ea82d2
- evidence_id: ap44-agent-ipr-IPR016342
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016342/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:16:34.048687Z'
  support: supports
  summary: IPR016342 is type family, named AP-1/2/4 complex subunit beta. Its complete
    native description and integrated signatures were read to distinguish the named
    subunit class from broader adaptor families or partial domains.
  snapshot_sha256: c4471532cb7d1df1f3ac04253e0efb8a2b918bd6d9987262e4715a65518cf48d
- evidence_id: ap44-agent-ipr-IPR001392
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR001392/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:16:34.864178Z'
  support: supports
  summary: IPR001392 is type family, named Clathrin adaptor, mu subunit. Its complete
    native description and integrated signatures were read to distinguish the named
    subunit class from broader adaptor families or partial domains.
  snapshot_sha256: b514537350700a251483339024cec9ab501f94f7bcb632df44e9dcd5aa3415f4
- evidence_id: ap44-agent-ipr-IPR016635
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016635/
  locator: Complete accession/name/type, description and LLM flags, integrated member
    signatures and hierarchy
  accessed_at: '2026-10-22T04:16:34.821416Z'
  support: supports
  summary: IPR016635 is type family, named Adaptor protein complex, sigma subunit.
    Its complete native description and integrated signatures were read to distinguish
    the named subunit class from broader adaptor families or partial domains.
  snapshot_sha256: 597cc84578003af4a8f1b735aab9676edda62e82a0a06a4fa1422f1658b8aa8e
- evidence_id: ap44-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:15:34.948894Z'
  support: supports
  summary: ENA 4932 identifies Saccharomyces cerevisiae, rank species. This verifies
    the named taxon, not a prevalence measurement or the strain used in every assay.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: ap44-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:15:34.948991Z'
  support: supports
  summary: ENA 559292 identifies Saccharomyces cerevisiae S288C, rank strain. This
    verifies the named taxon, not a prevalence measurement or the strain used in every
    assay.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: ap44-agent-yeung1999-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.10.11.3643&format=json&resultType=core
  locator: 'Unique Europe PMC MED bibliographic record: exact DOI/PMID/PMC if returned,
    authors/title/year and complete abstract'
  accessed_at: '2026-10-22T04:15:36.589009Z'
  support: supports
  summary: Yeung, Phan and Payne1999, DOI10.1091/mbc.10.11.3643/PMID10564262/PMC25654.
    The abstract distinguishes physical AP1-clathrin association from AP-complex dispensability
    for tested clathrin functions under normal yeast conditions.
  snapshot_sha256: 9e7a802648042b6fdef5128dc207e053d878ed2aca7022820d26208ada8e7bbe
- evidence_id: ap44-agent-valdivia2002-meta-exact
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2FS1534-5807%2802%2900127-2%22&format=json&resultType=core
  locator: 'Unique Europe PMC MED bibliographic record: exact DOI/PMID/PMC if returned,
    authors/title/year and complete abstract'
  accessed_at: '2026-10-22T04:16:06.687492Z'
  support: supports
  summary: Valdivia, Baggott, Chuang and Schekman2002, DOI10.1016/S1534-5807(02)00127-2/PMID11879634.
    The complete abstract supports Chs3/Tlg1 retention and proposes early-endosome-to-TGN
    recycling; no full Methods or new route proof is claimed.
  snapshot_sha256: 8a183a15a2054d3436feb3f5c17f84377f5f7795415ed40ab85f2d4289c370fb
- evidence_id: ap44-agent-whitfield2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1091%2Fmbc.e15-09-0621&format=json&resultType=core
  locator: 'Unique Europe PMC MED bibliographic record: exact DOI/PMID/PMC if returned,
    authors/title/year and complete abstract'
  accessed_at: '2026-10-22T04:15:37.168067Z'
  support: supports
  summary: Whitfield et al.2016, DOI10.1091/mbc.e15-09-0621/PMID26658609/PMC4751606.
    The complete abstract identifies alternate Apm1/Apm2 forms, distinct sorting outcomes
    and Mil1-dependent Apm2 recruitment.
  snapshot_sha256: 4d98f51f78ed79f7c99a18fcb9ab418e781da46e51203192dbbc45ee3cd4423d
- evidence_id: ap44-agent-yeung1999-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC25654/?report=xml
  locator: 'Genuine complete PMC HTML: Methods sec20 including Table3 and sec21; Results
    sec27,sec29,sec30 including Figure1/2 captions; entire Discussion sec33. Other
    Methods/Results, pixels and underlying unpublished observations not independently
    inspected.'
  accessed_at: '2026-10-22T04:16:06.686704Z'
  support: supports
  summary: Primary native coimmunoprecipitation identifies Apl2/Apl4/Apm1/Aps1, and
    binding/coimmunoprecipitation identifies AP1-clathrin association. Apm2 association
    was conditional in early experiments. The Discussion explicitly preserves lack
    of tested sorting defects in normal-clathrin AP1-deleted cells, so association
    is not universal necessity for clathrin function. Strains are GPY/SEY-derived
    experimental lines.
  snapshot_sha256: b6ffce7163ebff932d546e202d445f831f12f27fcd3783fab2c79ac4ba2d6a49
- evidence_id: ap44-agent-whitfield2016-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4751606/?report=xml
  locator: 'Genuine complete PMC HTML: entire Introduction sec1, Results sec3–8, Discussion
    sec9 and Methods sec11–20, including Figure1–6 captions. Supplementary files,
    image pixels and underlying cited experiments not read.'
  accessed_at: '2026-10-22T04:16:06.687049Z'
  support: supports
  summary: Primary yeast deletion, localization, binding and recruitment results distinguish
    AP1 from Apm2-containing AP1R and support cargo-specific sorting. Mil1 binds Apm2,
    contributes to membrane recruitment and has a predicted rather than demonstrated
    lipase activity; the proposed microdomain model remains hypothetical. BY4741/BY4742
    strains and specific assays are described.
  snapshot_sha256: 17d808d6316b7def6551cca6f7f5ddc4eabab39025178a2c93230700041c689e
- evidence_id: ap44-agent-protein-P36000
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P36000.json
  locator: Exact native identity/status/name/genes/taxon, SUBUNIT/FUNCTION/location
    comments and family crossrefs
  accessed_at: '2026-10-22T04:15:34.949204Z'
  support: supports
  summary: P36000 is a reviewed AP1 subunit with primary gene APL2, organism559292,
    matching the maintained accession/name/gene/taxon/status. Native SUBUNIT and FUNCTION
    comments link the experimental Yeung1999 membership annotation; annotations of
    other locations are not substituted for that primary membership evidence.
  snapshot_sha256: 526b13f0578f674f0da6edd6f5d896d27525277aaa24102a9f138d00afb7c2f0
- evidence_id: ap44-agent-gene-APL2
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned UniProt entries and primary/synonym gene fields
  accessed_at: '2026-10-22T04:15:35.899164Z'
  support: context_only
  summary: The exact reviewed APL2 query at organism559292 returns the single expected
    P36000.
  snapshot_sha256: 43e854e42512755d38608a38375b2f320cf989cd66644bf4dbeec296798c6006
  search_scope: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
- evidence_id: ap44-agent-protein-Q12028
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12028.json
  locator: Exact native identity/status/name/genes/taxon, SUBUNIT/FUNCTION/location
    comments and family crossrefs
  accessed_at: '2026-10-22T04:15:35.760679Z'
  support: supports
  summary: Q12028 is a reviewed AP1 subunit with primary gene APL4, organism559292,
    matching the maintained accession/name/gene/taxon/status. Native SUBUNIT and FUNCTION
    comments link the experimental Yeung1999 membership annotation; annotations of
    other locations are not substituted for that primary membership evidence.
  snapshot_sha256: 7b81a7d2f259bb7cebda9a454da0bdef2f2cad9042a287d72432713b1464de9c
- evidence_id: ap44-agent-gene-APL4
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned UniProt entries and primary/synonym gene fields
  accessed_at: '2026-10-22T04:15:35.979624Z'
  support: context_only
  summary: The exact reviewed APL4 query at organism559292 returns the single expected
    Q12028.
  snapshot_sha256: f0f5f1c2494566eeb96c492f6225a4c186a5c40ac3adc76c1a294d14ce64920b
  search_scope: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPL4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
- evidence_id: ap44-agent-protein-Q00776
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q00776.json
  locator: Exact native identity/status/name/genes/taxon, SUBUNIT/FUNCTION/location
    comments and family crossrefs
  accessed_at: '2026-10-22T04:15:35.874306Z'
  support: supports
  summary: Q00776 is a reviewed AP1 subunit with primary gene APM1, organism559292,
    matching the maintained accession/name/gene/taxon/status. Native SUBUNIT and FUNCTION
    comments link the experimental Yeung1999 membership annotation; annotations of
    other locations are not substituted for that primary membership evidence.
  snapshot_sha256: de4a35f47bed9a42163c4850e0c8be64e1a3c1041a655a53cf00c9071ccd174c
- evidence_id: ap44-agent-gene-APM1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned UniProt entries and primary/synonym gene fields
  accessed_at: '2026-10-22T04:15:36.452873Z'
  support: context_only
  summary: The exact reviewed APM1 query at organism559292 returns the single expected
    Q00776.
  snapshot_sha256: 9d0251049fa9718e8bc777afe874497ae899fd5266fed0462cadb8474b17cfd6
  search_scope: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPM1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
- evidence_id: ap44-agent-protein-P35181
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P35181.json
  locator: Exact native identity/status/name/genes/taxon, SUBUNIT/FUNCTION/location
    comments and family crossrefs
  accessed_at: '2026-10-22T04:15:35.880526Z'
  support: supports
  summary: P35181 is a reviewed AP1 subunit with primary gene APS1, organism559292,
    matching the maintained accession/name/gene/taxon/status. Native SUBUNIT and FUNCTION
    comments link the experimental Yeung1999 membership annotation; annotations of
    other locations are not substituted for that primary membership evidence.
  snapshot_sha256: d6393e7fc10d38610adc6e52a17a230fe2ab9ec35268039718826364a1480fbb
- evidence_id: ap44-agent-gene-APS1
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete returned UniProt entries and primary/synonym gene fields
  accessed_at: '2026-10-22T04:15:36.553905Z'
  support: context_only
  summary: The exact reviewed APS1 query at organism559292 returns P35181 (primary
    APS1) and P04802 (primary DPS1, APS1 alias). P35181 remains the correct AP1 sigma
    representative; the raw query is not unique.
  snapshot_sha256: c97e8ef19fb1de6f681e884ef0174cc3581ecacefdceeb4353fa6520049aed59
  search_scope: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AAPS1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/ap_1_adaptor_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:17Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/ap_1_adaptor_complex.yaml'
  snapshot_sha256: 1f343eb66142e002b316958a8e32e6a52c3d508878b9bfe81621ecff3deb62ce
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/ap_1_adaptor_complex.yaml
    --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_1_adaptor_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:18Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/ap_1_adaptor_complex.yaml\
    \ --out /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_1_adaptor_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/ap_1_adaptor_complex-strict.tsv"
  snapshot_sha256: 35bb035490936cbf33a464d7e95e6ba823b0c21a25c153ebae38a97fa74001ac
- evidence_id: ap1-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ap_1_adaptor_complex.yaml
  locator: Complete native read-only diagnostic log
  accessed_at: '2026-10-22T04:16:22.795517Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: ap1-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ap_1_adaptor_complex.yaml
  locator: Complete native read-only diagnostic log
  accessed_at: '2026-10-22T04:16:23.291985Z'
  support: supports
  summary: "data/structures/other/ap_1_adaptor_complex.yaml  (GO:0030121)\n  ap1_adaptor_complex_topology\t\
    ap1_beta1_subunit\tCOVERED\t->ap1_beta1_subunit (UniProtKB:P36000)\n  ap1_adaptor_complex_topology\t\
    ap1_gamma_subunit\tCOVERED\t->ap1_gamma_subunit (UniProtKB:Q12028)\n  ap1_adaptor_complex_topology\t\
    ap1_mu1_subunit\tCOVERED\t->ap1_mu1_subunit (UniProtKB:Q00776)\n  ap1_adaptor_complex_topology\t\
    ap1_sigma1_subunit\tCOVERED\t->ap1_sigma1_subunit (UniProtKB:P35181)\n\ncausal_graphs\
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
  snapshot_sha256: 0b56d8a5a4c0c8605f8632c7a287242a1fcdc6a699aa1023de31d68b74ea97e0
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/ap_1_adaptor_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 12 of 12 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
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
- assessment_id: protein-examples
  area: evidence
  topic: Correct four identities with one inaccurate uniqueness note
  outcome: concern
  target_ids:
  - GO:0030121
  summary: All four accession/gene/taxon/status identities and AP1 memberships are
    supported. APL2/APL4/APM1 queries are unique; APS1 returns two entries because
    DPS1 also carries the APS1 alias. The current P35181 evidence note incorrectly
    calls it the single reviewed entry, while its role correctly says representative.
    Historical seeding provenance is not rewritten.
  evidence_ids:
  - record
  - ap44-agent-yeung1999-legacy
  - ap44-agent-protein-P36000
  - ap44-agent-protein-Q12028
  - ap44-agent-protein-Q00776
  - ap44-agent-protein-P35181
  - ap44-agent-gene-APL2
  - ap44-agent-gene-APL4
  - ap44-agent-gene-APM1
  - ap44-agent-gene-APS1
- assessment_id: scope
  area: scope
  topic: Yeast occurrence, experimental backgrounds and alternate mu chains
  outcome: supported
  target_ids:
  - GO:0030121
  summary: Species and S288C reference identities are correct. COMMON retains its
    schema meaning of presence in most members with losses exceptional; ordinary yeast
    characterization supports this qualitative synthesis without a measured strain-prevalence
    census. GPY/SEY and BY4741/BY4742 experiments are not relabeled as S288C. APM1
    is a supported representative of the mu1 class, not an assertion that APM2 never
    occurs.
  evidence_ids:
  - record
  - ap44-agent-go
  - ap44-agent-tax4932
  - ap44-agent-tax559292
  - ap44-agent-yeung1999-meta
  - ap44-agent-valdivia2002-meta-exact
  - ap44-agent-whitfield2016-meta
  - ap44-agent-yeung1999-legacy
  - ap44-agent-whitfield2016-legacy
  - ap44-agent-protein-P36000
  - ap44-agent-protein-Q12028
  - ap44-agent-protein-Q00776
  - ap44-agent-protein-P35181
- assessment_id: function-graph
  area: graph
  topic: NONMECHANISTIC topology and cargo-specific sorting
  outcome: supported
  target_ids:
  - GO:0030121
  summary: All six edges summarize constituent membership, GO coat parthood and source-supported
    late-Golgi/Golgi-early-endosome sorting. The graph does not require AP1 for every
    clathrin event. Mil1 remains regulatory machinery, not a fifth heterotetrameric
    constituent; specific binding and recruitment do not imply a new stable core-subunit
    class.
  evidence_ids:
  - record
  - ap44-agent-go
  - ap44-agent-yeung1999-meta
  - ap44-agent-valdivia2002-meta-exact
  - ap44-agent-whitfield2016-meta
  - ap44-agent-yeung1999-legacy
  - ap44-agent-whitfield2016-legacy
- assessment_id: identity
  area: identity
  topic: Exact AP-1 heterotetramer and containing-structure boundaries
  outcome: supported
  target_ids:
  - GO:0030121
  summary: The maintained definition, ontology identity, parentage, subtype-specific
    core classes and any coat parthood match the native GO authority. Different AP
    subtypes and containing coats remain distinct; no identity remapping is warranted.
  evidence_ids:
  - record
  - ap44-agent-go
  - ap44-agent-yeung1999-meta
  - ap44-agent-valdivia2002-meta-exact
  - ap44-agent-whitfield2016-meta
  - ap44-agent-yeung1999-legacy
  - ap44-agent-whitfield2016-legacy
- assessment_id: grounding
  area: grounding
  topic: Exact subtype families versus deferred broader candidates
  outcome: concern
  target_ids:
  - GO:0030121
  summary: Native family entries support ap1_gamma_subunit → InterPro:IPR017107, ap1_sigma1_subunit
    → InterPro:IPR044733. These are complete subtype-specific family classes, not
    merely domains or species-specific proteins, so their current REVIEWED_LABEL_ONLY
    status is not justified by saying no CURIE was curated in a prior pass. The other
    broader candidates do not close every remaining subunit class. Biological membership
    and identity remain supported.
  evidence_ids:
  - record
  - schema
  - curation
  - ap44-agent-family-search-AP1
  - ap44-agent-ipr-IPR017107
  - ap44-agent-ipr-IPR044733
  - ap44-agent-ipr-IPR016342
  - ap44-agent-ipr-IPR001392
  - ap44-agent-ipr-IPR016635
  - ap44-agent-protein-P36000
  - ap44-agent-protein-Q12028
  - ap44-agent-protein-Q00776
  - ap44-agent-protein-P35181
- assessment_id: formation
  area: evidence
  topic: Constituent identity separated from assembly necessity
  outcome: unknown
  target_ids:
  - GO:0030121
  summary: All four components use UNKNOWN essentiality. The evidence supports the
    four named constituent classes; transport phenotypes, viability outcomes, interaction
    assays and reconstituted activity do not independently establish universal formation
    necessity for every subunit. UNKNOWN is retained rather than replaced by an inferred
    requirement.
  evidence_ids:
  - record
  - schema
  - ap44-agent-go
  - ap44-agent-yeung1999-meta
  - ap44-agent-valdivia2002-meta-exact
  - ap44-agent-whitfield2016-meta
  - ap44-agent-yeung1999-legacy
  - ap44-agent-whitfield2016-legacy
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and bounded source availability
  outcome: supported
  target_ids:
  - GO:0030121
  summary: All target fields and explicit evidence placements were inspected. The
    four core components are represented. Missing additional taxa, isoforms or exhaustive
    accessory-protein inventories are not treated as defects; exact-family findings
    are limited to independently verified matches and the explicit label-only contract.
  evidence_ids:
  - record
  - ap44-agent-go
  - ap44-agent-family-search-AP1
  - ap44-agent-yeung1999-meta
  - ap44-agent-valdivia2002-meta-exact
  - ap44-agent-whitfield2016-meta
  - ap44-agent-yeung1999-legacy
  - ap44-agent-whitfield2016-legacy
findings:
- finding_id: F1
  issue_key: ap1-verified-subtype-families-label-only
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground the verified AP-1 subtype-specific subunit families
  description: Exact native InterPro family identities are available for ap1_gamma_subunit
    → InterPro:IPR017107, ap1_sigma1_subunit → InterPro:IPR044733. The affected components
    nevertheless carry REVIEWED_LABEL_ONLY and notes saying no exact CURIE was curated
    in the prior pass. CURATION and schema define this status as no exact assertable
    family, not deferred curation. The native family types/descriptions match the
    component classes; other unresolved broad families and domains are not promoted.
  target_ids:
  - GO:0030121
  field_paths:
  - components#ap1_gamma_subunit.grounding_status
  - components#ap1_sigma1_subunit.grounding_status
  - components#ap1_gamma_subunit.grounding_notes
  - components#ap1_sigma1_subunit.grounding_notes
  - discussions#resolve_ap1_subunit_groundings
  evidence_ids:
  - record
  - schema
  - curation
  - ap44-agent-family-search-AP1
  - ap44-agent-ipr-IPR017107
  - ap44-agent-ipr-IPR044733
  - ap44-agent-protein-P36000
  - ap44-agent-protein-Q12028
  - ap44-agent-protein-Q00776
  - ap44-agent-protein-P35181
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_1_adaptor_complex.yaml
    role: maintained scientific record
  rule_id: Exact protein-family grounding and reviewed-label-only semantics
  native_severity: minor
  normalization_reason: The correct complex and biological subunits are retained.
    The defect is a bounded omitted family mapping and incompatible status/notes for
    verified exact classes; it does not invalidate the whole record or require broader-domain
    substitution.
- finding_id: F2
  issue_key: ap1-aps1-reviewed-query-not-unique
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the APS1 single-entry evidence note
  description: 'The current exact reviewed APS1 query at taxon559292 returns two entries:
    the correct AP1 sigma P35181 with primary APS1 and P04802 with primary DPS1 and
    APS1 as an alias. The maintained P35181 evidence note says single reviewed entry,
    although its role already says representative. This is an inaccurate current query-resolution
    claim, not a wrong protein accession or subunit membership.'
  target_ids:
  - GO:0030121
  field_paths:
  - components#ap1_sigma1_subunit.protein_examples[0].evidence[0].notes
  evidence_ids:
  - record
  - ap44-agent-protein-P35181
  - ap44-agent-gene-APS1
  - ap44-agent-yeung1999-legacy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_1_adaptor_complex.yaml
    role: maintained scientific record
  rule_id: Exact protein example and native query provenance
  native_severity: minor
  normalization_reason: Identity, taxon and experimental AP1 membership are correct;
    only the stated uniqueness of gene resolution needs qualification. Historical
    query state is not reconstructed.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030121
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_1_adaptor_complex.yaml
    role: maintained scientific record
  description: In separately authorized curation, add the verified mappings ap1_gamma_subunit
    → InterPro:IPR017107, ap1_sigma1_subunit → InterPro:IPR044733; remove the obsolete
    reviewed-label-only status/notes on those mapped rows and narrow the existing
    TODO to unresolved classes. Preserve the exact complex, roles, examples and UNKNOWN
    formation necessity; do not force broad beta/mu/sigma or domain entries onto other
    subtype classes.
  acceptance_checks:
  - Each added CURIE resolves to the stated native subtype-specific family, with current
    identifier/label correspondence.
  - Only the verified classes lose reviewed-label-only status; genuinely unresolved
    classes and their bounded TODO remain.
  - Focused schema/strict, protein/graph diagnostics and source-placement checks pass
    after authorized curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0030121
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ap_1_adaptor_complex.yaml
    role: maintained scientific record
  description: In separately authorized curation, retain P35181 and its APS1/S288C
    identity, but describe it as the verified representative with primary gene APS1
    and explicitly distinguish the DPS1 alias hit if query resolution is discussed.
    Do not alter historical seeding provenance or substitute P04802.
  acceptance_checks:
  - The current evidence note no longer claims that the alias-inclusive reviewed APS1
    query has one result.
  - P35181 remains linked to AP1 sigma with the correct taxon and primary gene; native
    protein verification passes.
limitations:
- The five complete same-base batch26 corpus gates await guarded integration by the
  parent before finalization.
- No image pixels, new sequence alignments, supplementary datasets or quantitative
  prevalence census were inspected. Exact source-reading sections are declared individually.
- The native family search is bounded to the listed InterPro text query and separately
  retrieved exact entries. Broad beta1/2/4, mu and sigma families or partial domains
  do not establish an exact subtype mapping for every remaining component; no all-catalog
  absence is claimed.
- Valdivia2002 was read at complete native MED abstract scope only. Its DOI route
  failed TLS certificate verification; no full body is claimed. The initial unquoted
  DOI query returned zero results, superseded by the exact quoted DOI query; this
  was query syntax, not an absent citation.
- The S288C protein references establish identity and annotated membership; the original
  Yeung and Whitfield assays used their explicitly stated experimental backgrounds.
  Native APS1 ambiguity does not invalidate P35181 or its AP1 membership.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes this review bundle. Parent owns same-base global-gate
  integration and later finalization; no scientific edits or persistence performed.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
