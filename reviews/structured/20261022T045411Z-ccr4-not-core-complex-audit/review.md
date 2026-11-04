# Ccr4 not core complex scientific review

- Review: 20261022T045411Z-ccr4-not-core-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:36:50Z
- Finished UTC: 2026-10-22T04:54:11Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The nine-subunit yeast CCR4-NOT core, examples and bounded deadenylation graph are supported. One minor finding resolves four exact protein-family groundings.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 1 of batch46 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030015 | data/structures/other/ccr4_not_core_complex.yaml | maintained | CCR4-NOT core complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030015 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030015 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0030015 | Focused native check passed; claim-level support assessed separately. |
| Focused native verify | passed | True | GO:0030015 | Focused native check passed; claim-level support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0030015 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0030015 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030015 | 17 of 20 collected target identifiers returned OK. PMID:11239395: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:11733989: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:11889048: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030015 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030015 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030015 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030015 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030015 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Nine-subunit budding-yeast core

identity: supported. Targets: GO:0030015.

GO0030015 and Chen2001 native abstract identify the nine-subunit 1.0MDa core, distinguished from the larger 1.9MDa assembly. The generic protein-complex parent is appropriate.

### Four exact families resolve current label-only gaps

grounding: concern. Targets: GO:0030015.

CAF1/Pop2 IPR039637, Not1 IPR040398, Not4 IPR039780 and Caf40 IPR007216 are full relevant subunit families cross-referenced by the examples. CCR4/nocturin and Not2/3/5-related xref names are broader, and Caf130 inspected hits are domains; they are not forced onto the unresolved rows.

### Nine reviewed yeast references

grounding: supported. Targets: GO:0030015.

All accessions, aliases, entry statuses and S288C taxon identities agree; each declared symbol query returns its corresponding maintained entry. Localization annotations are not mistaken for complete membership experiments.

### Formation uncertainty remains explicit

grounding: unknown. Targets: GO:0030015.

All nine formation-necessity fields are UNKNOWN. Functional RNA-decay defects and Not1 cellular essentiality do not establish whether the complete structural complex forms after individual depletion.

### Supported yeast canonical system

scope: supported. Targets: GO:0030015.

The Saccharomyces scope matches purification and functional studies. COMMON retains present-in-most-members/losses-exception meaning as a qualitative ordinary cellular-machinery assessment; no population census was performed.

### Ccr4/Caf1-dependent deadenylation at complex level

evidence: supported. Targets: GO:0030015.

The maintained wording describes the major complex activity and normal in-vivo dependence, not a claim that yeast Pop2 alone is necessarily the catalytic enzyme. Tucker2001 abstract and Tucker2002 experiments support that distinction and the downstream mRNA-decay role.

### Appropriately nonmechanistic function graph

graph: supported. Targets: GO:0030015.

Constituent-to-core links and core-to-deadenylation/decay directions match the cited scope. NONMECHANISTIC correctly withholds recruitment, detailed NOT architecture and downstream decay kinetics.

### Complete target and bounded family TODO

completeness: supported. Targets: GO:0030015.

All current evidence and localization PMID identities were checked. Four verified whole-family mappings are actionable; unresolved domains and broad paralogue families remain bounded.

## Findings

### F1: Ground four verified CCR4-NOT subunit families

minor / open / confirmed; issue key: ccr4-not-four-exact-families.

CAF1/Pop2, Not1, Not4 and Caf40 remain REVIEWED_LABEL_ONLY although native family entries IPR039637, IPR040398, IPR039780 and IPR007216 respectively define their full classes and appear on the exact examples. This resolves only four rows of the broader historical TODO.

## Recommended Actions And Acceptance Checks

### A1

Add the four exact family groundings and reconcile their notes and TODO coverage. Keep CCR4, Not2/3/5 and Caf130 unresolved unless separately verified exact families are found.

- Verify exact source identities and reconcile affected current wording and TODO scope.
- Preserve supported example accessions, membership and explicit unresolved claims.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/ccr4_not_core_complex.yaml; Entire maintained target, history, components, evidence, discussions and graphs | context_only | All maintained fields were read; history is provenance rather than independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Components, essentiality, COMMON and graph scope | context_only | Whole-protein families differ from shared domains and example accessions; formation necessity differs from functional or cellular essentiality. COMMON means present in most members, with losses the exception. |
| curation | docs/CURATION.md; Components and REVIEWED_LABEL_ONLY contract | context_only | Reviewed label-only means no exact term exists; a currently verified exact family makes the grounding gap actionable despite a historical TODO. |
| root46-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000288,GO:0004535,GO:0005829,GO:0005832,GO:0006457,GO:0030015,GO:0032991,GO:0043263,GO:0043264; All9 requested terms: complete id/name/active/definition/synonyms/comments and relevant maintained typed links; not all ontology descendants | supports | Native GO identities, definitions, synonyms and inspected maintained typed relationships agree with the target classes and functions. Missing direct ontology links alone do not disprove biologically sourced parentage. |
| root46-sources-pmid-11239395 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11239395+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native id/title/authors/year/DOI and abstract | supports | MED11239395: The transcription factor associated Ccr4 and Caf1 proteins are components of the major cytoplasmic mRNA deadenylase in Saccharomyces cerevisiae. DOI 10.1016/s0092-8674(01)00225-2. Complete native bibliographic identity and abstract inspected. This row certifies abstract-level access only; no full-text access is implied. |
| root46-sources-pmid-11733989 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11733989+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native id/title/authors/year/DOI and abstract | supports | MED11733989: Purification and characterization of the 1.0 MDa CCR4-NOT complex identifies two novel components of the complex. DOI 10.1006/jmbi.2001.5162. Complete native bibliographic identity and abstract inspected. This row certifies abstract-level access only; no full-text access is implied. |
| root46-sources-pmid-11889048 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11889048+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native id/title/authors/year/DOI and abstract | supports | MED11889048: Ccr4p is the catalytic subunit of a Ccr4p/Pop2p/Notp mRNA deadenylase complex in Saccharomyces cerevisiae. DOI 10.1093/emboj/21.6.1427. Complete native bibliographic identity and abstract inspected. This row certifies abstract-level access only; no full-text access is implied. |
| root46-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA verifies the maintained taxonomic identity and lineage for 4932. |
| root46-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | ENA verifies the maintained taxonomic identity and lineage for 559292. |
| root46-sources-protein-P31384 | https://rest.uniprot.org/uniprotkb/P31384.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | P31384 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-protein-P39008 | https://rest.uniprot.org/uniprotkb/P39008.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | P39008 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-protein-P25655 | https://rest.uniprot.org/uniprotkb/P25655.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | P25655 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-protein-P06100 | https://rest.uniprot.org/uniprotkb/P06100.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | P06100 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-protein-P06102 | https://rest.uniprot.org/uniprotkb/P06102.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | P06102 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-protein-P34909 | https://rest.uniprot.org/uniprotkb/P34909.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | P34909 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-protein-Q12514 | https://rest.uniprot.org/uniprotkb/Q12514.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | Q12514 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-protein-P53829 | https://rest.uniprot.org/uniprotkb/P53829.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | P53829 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-protein-P53280 | https://rest.uniprot.org/uniprotkb/P53280.json; Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY comments; InterPro/Pfam xref identifiers | supports | P53280 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained name, genes/aliases and taxon. Membership remains a separate source question. |
| root46-sources-gene-CCR4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACCR4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-gene-CAF1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-gene-NOT1-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-gene-NOT2-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-gene-NOT3-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-gene-NOT4-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-gene-NOT5-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-gene-CAF40-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAF40%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-gene-CAF130-559292 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAF130%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete query URL, result count and all accession/status/name/gene/taxon result fields | supports | Exact gene/taxon query returns the single maintained accession with its stated entry status. |
| root46-sources-ipr-IPR039637 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039637/; Complete native accession/name/type/description and description curation flags | supports | IPR039637 is a family named CCR4-NOT transcription complex subunit 7/8/Pop2. Its complete native description was read; exact example xrefs provide an independent identity join. Family annotation is not primary evidence of membership. |
| root46-sources-ipr-IPR040398 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040398/; Complete native accession/name/type/description and description curation flags | supports | IPR040398 is a family named CCR4-NOT transcription complex subunit 1. Its complete native description was read; exact example xrefs provide an independent identity join. Family annotation is not primary evidence of membership. |
| root46-sources-ipr-IPR039780 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039780/; Complete native accession/name/type/description and description curation flags | supports | IPR039780 is a family named CCR4-NOT transcription complex subunit 4. Its complete native description was read; exact example xrefs provide an independent identity join. Family annotation is not primary evidence of membership. |
| root46-sources-ipr-IPR007216 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007216/; Complete native accession/name/type/description and description curation flags | supports | IPR007216 is a family named CCR4-NOT transcription complex subunit 9. Its complete native description was read; exact example xrefs provide an independent identity join. Family annotation is not primary evidence of membership. |
| root46-sources-legacy-PMC125913 | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC125913/; Complete Results sec3/4/5/6/8/9, Discussion sec12/13/14 and Methods sec20/21, including embedded Fig1–5/7 captions; remaining sections not certified | supports | Ccr4 overexpression suppresses pop2 deletion defects; Ccr4 catalytic-pocket mutants impair deadenylation. Purified Ccr4 retains activity without Pop2, whereas Not1/Not2 localization and NOT deletion phenotypes support a cytoplasmic complex role. The authors explicitly retain possible indirect NOT effects and do not establish formation necessity for all nine subunits. |
| schema-result | just validate data/structures/other/ccr4_not_core_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/ccr4_not_core_complex.yaml |
| strict-result | just validate-strict data/structures/other/ccr4_not_core_complex.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/ccr4_not_core_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/ccr4_not_core_complex.yaml --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/ccr4_not_core_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/ccr4_not_core_complex-strict.tsv |
| native-ccr4_not_core_complex-causal-graphs | /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ccr4_not_core_complex.yaml; Complete focused native report | supports | data/structures/other/ccr4_not_core_complex.yaml  (GO:0030015)<br>  yeast_ccr4_not_deadenylation	ccr4_core_subunit	COVERED	-&gt;ccr4_core_subunit (UniProtKB:P31384)<br>  yeast_ccr4_not_deadenylation	caf1_pop2_core_subunit	COVERED	-&gt;caf1_pop2_core_subunit (UniProtKB:P39008)<br>  yeast_ccr4_not_deadenylation	not1_cdc39_core_subunit	COVERED	-&gt;not1_cdc39_core_subunit (UniProtKB:P25655)<br>  yeast_ccr4_not_deadenylation	not2_cdc36_core_subunit	COVERED	-&gt;not2_cdc36_core_subunit (UniProtKB:P06100)<br>  yeast_ccr4_not_deadenylation	not3_core_subunit	COVERED	-&gt;not3_core_subunit (UniProtKB:P06102)<br>  yeast_ccr4_not_deadenylation	not4_mot2_core_subunit	COVERED	-&gt;not4_mot2_core_subunit (UniProtKB:P34909)<br>  yeast_ccr4_not_deadenylation	not5_core_subunit	COVERED	-&gt;not5_core_subunit (UniProtKB:Q12514)<br>  yeast_ccr4_not_deadenylation	caf40_core_subunit	COVERED	-&gt;caf40_core_subunit (UniProtKB:P53829)<br>  yeast_ccr4_not_deadenylation	caf130_core_subunit	COVERED	-&gt;caf130_core_subunit (UniProtKB:P53280)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     9  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     9  total GENE_OR_PROTEIN causal nodes |
| native-ccr4_not_core_complex-verify | /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/ccr4_not_core_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/ccr4_not_core_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 17 of 20 collected target identifiers returned OK. PMID:11239395: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:11733989: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:11889048: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, supplements or sequence alignments were reanalyzed. Primary-body inspection is limited to the explicitly listed sections.
- Chen2001 and Tucker2001 were accessible as complete native metadata/abstracts; publisher routes returned redirect-only pages, not article bodies. Detailed nine-subunit purification was not independently read in full.
- The failed DOI query for Tucker2001 returned no results; exact PMID11239395 provides its verified title and DOI instead. No bibliographic absence is inferred.
- CCR4 protein evidence inspection excludes FUNCTION comment bodies; membership/function was assessed using the stated complex and primary sources.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T045411Z-ccr4-not-core-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Ccr4 not core complex scientific review
started_at: '2026-10-22T04:36:50Z'
finished_at: '2026-10-22T04:54:11Z'
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
summary: The nine-subunit yeast CCR4-NOT core, examples and bounded deadenylation
  graph are supported. One minor finding resolves four exact protein-family groundings.
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
  - path: data/structures/other/ccr4_not_core_complex.yaml
    sha256: 504a2fab8f0e45f9bad27454f7ff8c51b0aa9caba8dcefa65b8e6647037559a8
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
- target_id: GO:0030015
  path: data/structures/other/ccr4_not_core_complex.yaml
  label: CCR4-NOT core complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ccr4_not_core_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 1 of batch46 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030015
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030015
  command: just validate data/structures/other/ccr4_not_core_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030015
  command: just validate-strict data/structures/other/ccr4_not_core_complex.yaml --out
    /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/ccr4_not_core_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-ccr4_not_core_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0030015
  command: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ccr4_not_core_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-ccr4_not_core_complex-causal-graphs
- check_id: native-ccr4_not_core_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0030015
  command: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ccr4_not_core_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-ccr4_not_core_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030015
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030015
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root46-sources-go
  - root46-sources-pmid-11239395
  - root46-sources-pmid-11733989
  - root46-sources-pmid-11889048
  - root46-sources-tax4932
  - root46-sources-tax559292
  - root46-sources-protein-P31384
  - root46-sources-protein-P39008
  - root46-sources-protein-P25655
  - root46-sources-protein-P06100
  - root46-sources-protein-P06102
  - root46-sources-protein-P34909
  - root46-sources-protein-Q12514
  - root46-sources-protein-P53829
  - root46-sources-protein-P53280
  - root46-sources-gene-CCR4-559292
  - root46-sources-gene-CAF1-559292
  - root46-sources-gene-NOT1-559292
  - root46-sources-gene-NOT2-559292
  - root46-sources-gene-NOT3-559292
  - root46-sources-gene-NOT4-559292
  - root46-sources-gene-NOT5-559292
  - root46-sources-gene-CAF40-559292
  - root46-sources-gene-CAF130-559292
  - root46-sources-ipr-IPR039637
  - root46-sources-ipr-IPR040398
  - root46-sources-ipr-IPR039780
  - root46-sources-ipr-IPR007216
  - root46-sources-legacy-PMC125913
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030015
  summary: '17 of 20 collected target identifiers returned OK. PMID:11239395: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:11733989:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:11889048: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root46-sources-pmid-11239395
  - root46-sources-pmid-11733989
  - root46-sources-pmid-11889048
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0030015
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
  - GO:0030015
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
  - GO:0030015
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
  - GO:0030015
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
  - GO:0030015
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
  reference: data/structures/other/ccr4_not_core_complex.yaml
  locator: Entire maintained target, history, components, evidence, discussions and
    graphs
  accessed_at: '2026-10-22T04:45:56Z'
  support: context_only
  summary: All maintained fields were read; history is provenance rather than independent
    scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Components, essentiality, COMMON and graph scope
  accessed_at: '2026-10-22T04:45:56Z'
  support: context_only
  summary: Whole-protein families differ from shared domains and example accessions;
    formation necessity differs from functional or cellular essentiality. COMMON means
    present in most members, with losses the exception.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components and REVIEWED_LABEL_ONLY contract
  accessed_at: '2026-10-22T04:45:56Z'
  support: context_only
  summary: Reviewed label-only means no exact term exists; a currently verified exact
    family makes the grounding gap actionable despite a historical TODO.
- evidence_id: root46-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000288,GO:0004535,GO:0005829,GO:0005832,GO:0006457,GO:0030015,GO:0032991,GO:0043263,GO:0043264
  locator: 'All9 requested terms: complete id/name/active/definition/synonyms/comments
    and relevant maintained typed links; not all ontology descendants'
  accessed_at: '2026-10-22T04:37:41.642935Z'
  support: supports
  summary: Native GO identities, definitions, synonyms and inspected maintained typed
    relationships agree with the target classes and functions. Missing direct ontology
    links alone do not disprove biologically sourced parentage.
  snapshot_sha256: ec8a67921ee38714d049e648bd88fa03897f191156b58757054dabeec944dbe1
- evidence_id: root46-sources-pmid-11239395
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11239395+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native id/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:37:47.257428Z'
  support: supports
  summary: 'MED11239395: The transcription factor associated Ccr4 and Caf1 proteins
    are components of the major cytoplasmic mRNA deadenylase in Saccharomyces cerevisiae.
    DOI 10.1016/s0092-8674(01)00225-2. Complete native bibliographic identity and
    abstract inspected. This row certifies abstract-level access only; no full-text
    access is implied.'
  snapshot_sha256: f9b16d28cd9d159551127e70cd8f12a9a6dd6b0d66125a1e95e46120cf56c520
- evidence_id: root46-sources-pmid-11733989
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11733989+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native id/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:37:47.578700Z'
  support: supports
  summary: 'MED11733989: Purification and characterization of the 1.0 MDa CCR4-NOT
    complex identifies two novel components of the complex. DOI 10.1006/jmbi.2001.5162.
    Complete native bibliographic identity and abstract inspected. This row certifies
    abstract-level access only; no full-text access is implied.'
  snapshot_sha256: 4d08b1c21f75dd6cf83f00fff32ba6262049f2a3afe6b1c006b58947ba820f85
- evidence_id: root46-sources-pmid-11889048
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11889048+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native id/title/authors/year/DOI and abstract
  accessed_at: '2026-10-22T04:37:47.590517Z'
  support: supports
  summary: 'MED11889048: Ccr4p is the catalytic subunit of a Ccr4p/Pop2p/Notp mRNA
    deadenylase complex in Saccharomyces cerevisiae. DOI 10.1093/emboj/21.6.1427.
    Complete native bibliographic identity and abstract inspected. This row certifies
    abstract-level access only; no full-text access is implied.'
  snapshot_sha256: 394132b097e241cae2455cc2a907f25376f06cfdb0c4bb967e00d6fb386a6d76
- evidence_id: root46-sources-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:37:41.643299Z'
  support: supports
  summary: ENA verifies the maintained taxonomic identity and lineage for 4932.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root46-sources-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:37:42.238539Z'
  support: supports
  summary: ENA verifies the maintained taxonomic identity and lineage for 559292.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root46-sources-protein-P31384
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P31384.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:43.039940Z'
  support: supports
  summary: P31384 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: 7f168b17f3a8fe77a2639e5e91666622c3df72a4e772d63ea26dd71f869de530
- evidence_id: root46-sources-protein-P39008
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P39008.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:43.095617Z'
  support: supports
  summary: P39008 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: 661f301141e148fd7a138a6a760a7be0dcf7a22322873cfa70ace161251ad207
- evidence_id: root46-sources-protein-P25655
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P25655.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:42.894736Z'
  support: supports
  summary: P25655 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: f3b614d50da23a83f196ac538e4f1adcfb6d7df3a3f8e4125d44a20f546b0345
- evidence_id: root46-sources-protein-P06100
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P06100.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:42.296465Z'
  support: supports
  summary: P06100 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: 5a95ada597615719aa46312545ce0f5b6f8c3065ed0207c7c32dcf223ec36411
- evidence_id: root46-sources-protein-P06102
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P06102.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:42.298703Z'
  support: supports
  summary: P06102 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: 0d5830b52d17eb19f3e6bae592d894a932d633004b58f59f3f68141938582e3e
- evidence_id: root46-sources-protein-P34909
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P34909.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:43.084358Z'
  support: supports
  summary: P34909 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: 71b89f1e9c2341e08de56542e4794552027ed06b2b2aeb29fe29cd4305ba855d
- evidence_id: root46-sources-protein-Q12514
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/Q12514.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:46.228465Z'
  support: supports
  summary: Q12514 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: 6104573dc1e82daabc45223b7dd21326d777b94360599d7c694e7ff65338a383
- evidence_id: root46-sources-protein-P53829
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53829.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:45.203978Z'
  support: supports
  summary: P53829 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: 8667f553807a41feaf2166127d90c09e03b1bf90ddb29d71646ed320444a4b77
- evidence_id: root46-sources-protein-P53280
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P53280.json
  locator: Complete identity/status/name/genes/taxon; SUBUNIT/SUBCELLULAR LOCATION/SIMILARITY
    comments; InterPro/Pfam xref identifiers
  accessed_at: '2026-10-22T04:37:44.569213Z'
  support: supports
  summary: P53280 has status UniProtKB reviewed (Swiss-Prot) and agrees with maintained
    name, genes/aliases and taxon. Membership remains a separate source question.
  snapshot_sha256: 87529c83af7e9316ce5ccf6fac26a3268f420a5b48ee24ba616cabeba7e65b3e
- evidence_id: root46-sources-gene-CCR4-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACCR4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:39.389788Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: 07e9ab652f962fb05351dd20adf277a66f600a6bcd8ac24a29e1be839d1ff5df
- evidence_id: root46-sources-gene-CAF1-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAF1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:39.451891Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: 4c540a9375f1de48bf6ed3482b8b36ea283586b44d90640f735b0cdc75f6cc4e
- evidence_id: root46-sources-gene-NOT1-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:39.709475Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: e545c9e4fafcf0ab4abe863a58ce7e5cbff422943f2dc209f6e1045e306b8238
- evidence_id: root46-sources-gene-NOT2-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:39.713321Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: d7db46315647c7e86a15a1b8e1aae150a682bd53b42359777e97258c63c09f15
- evidence_id: root46-sources-gene-NOT3-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT3%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:39.785483Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: dba3a07379aa0800aca3107625a0d83330cc06effa64073cc76597f7199eee1c
- evidence_id: root46-sources-gene-NOT4-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT4%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:40.397631Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: fbdb69d801a77ac097f3cc6b39cc3d3d489e858e19d7f62e731988069b60682b
- evidence_id: root46-sources-gene-NOT5-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ANOT5%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:40.431952Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: e78146d299563f4ae7b8727f3c3b0f6a5c0098e3a69b13f71c58becd43423540
- evidence_id: root46-sources-gene-CAF40-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAF40%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:40.613963Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: fca6cebcc491978818a54399dba821eb284464793d71afd4b5427b48594a7327
- evidence_id: root46-sources-gene-CAF130-559292
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3ACAF130%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete query URL, result count and all accession/status/name/gene/taxon
    result fields
  accessed_at: '2026-10-22T04:38:40.635535Z'
  support: supports
  summary: Exact gene/taxon query returns the single maintained accession with its
    stated entry status.
  snapshot_sha256: 022de9da7600798828eaaf31461fa8fe43cf7b07a98ce26561a3cb8862cd9bf6
- evidence_id: root46-sources-ipr-IPR039637
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039637/
  locator: Complete native accession/name/type/description and description curation
    flags
  accessed_at: '2026-10-22T04:38:37.975757Z'
  support: supports
  summary: IPR039637 is a family named CCR4-NOT transcription complex subunit 7/8/Pop2.
    Its complete native description was read; exact example xrefs provide an independent
    identity join. Family annotation is not primary evidence of membership.
  snapshot_sha256: a6b81f2aec1f513feba1b5f013cc0f7b2f5b45cb1f0965ff80a523b982a0ebbf
- evidence_id: root46-sources-ipr-IPR040398
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040398/
  locator: Complete native accession/name/type/description and description curation
    flags
  accessed_at: '2026-10-22T04:38:38.436810Z'
  support: supports
  summary: IPR040398 is a family named CCR4-NOT transcription complex subunit 1. Its
    complete native description was read; exact example xrefs provide an independent
    identity join. Family annotation is not primary evidence of membership.
  snapshot_sha256: 48892848aec299ca0a7b8edff69da4dae1844a774b33215e786827f44052c42c
- evidence_id: root46-sources-ipr-IPR039780
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR039780/
  locator: Complete native accession/name/type/description and description curation
    flags
  accessed_at: '2026-10-22T04:38:38.181106Z'
  support: supports
  summary: IPR039780 is a family named CCR4-NOT transcription complex subunit 4. Its
    complete native description was read; exact example xrefs provide an independent
    identity join. Family annotation is not primary evidence of membership.
  snapshot_sha256: aac6f25637d97e7f620a2931e15f31c150fd722362cad2e63dd3a67e84e5b170
- evidence_id: root46-sources-ipr-IPR007216
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007216/
  locator: Complete native accession/name/type/description and description curation
    flags
  accessed_at: '2026-10-22T04:38:32.542508Z'
  support: supports
  summary: IPR007216 is a family named CCR4-NOT transcription complex subunit 9. Its
    complete native description was read; exact example xrefs provide an independent
    identity join. Family annotation is not primary evidence of membership.
  snapshot_sha256: 829192e6c8176ff877d077cb94702b0a6e1226721a44a6cb843933a056868092
- evidence_id: root46-sources-legacy-PMC125913
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC125913/
  locator: Complete Results sec3/4/5/6/8/9, Discussion sec12/13/14 and Methods sec20/21,
    including embedded Fig1–5/7 captions; remaining sections not certified
  accessed_at: '2026-10-22T04:39:21.338918Z'
  support: supports
  summary: Ccr4 overexpression suppresses pop2 deletion defects; Ccr4 catalytic-pocket
    mutants impair deadenylation. Purified Ccr4 retains activity without Pop2, whereas
    Not1/Not2 localization and NOT deletion phenotypes support a cytoplasmic complex
    role. The authors explicitly retain possible indirect NOT effects and do not establish
    formation necessity for all nine subunits.
  snapshot_sha256: 36d924ee488769b03cc44613f59967ce131417c8bdd5d53f77639b4e56c91158
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/ccr4_not_core_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:36:51Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/ccr4_not_core_complex.yaml'
  snapshot_sha256: dfd29258b53e2883abde5873e355d7019a9d1e7cc738dc19d73a38246661923b
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/ccr4_not_core_complex.yaml
    --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/ccr4_not_core_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:36:52Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/ccr4_not_core_complex.yaml\
    \ --out /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/ccr4_not_core_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/ccr4_not_core_complex-strict.tsv"
  snapshot_sha256: 1fe0edcb982b3c1844765743893d32923b478a7cb464445b9d31b7b156d87e09
- evidence_id: native-ccr4_not_core_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/ccr4_not_core_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:37:53.086716Z'
  support: supports
  summary: "data/structures/other/ccr4_not_core_complex.yaml  (GO:0030015)\n  yeast_ccr4_not_deadenylation\t\
    ccr4_core_subunit\tCOVERED\t->ccr4_core_subunit (UniProtKB:P31384)\n  yeast_ccr4_not_deadenylation\t\
    caf1_pop2_core_subunit\tCOVERED\t->caf1_pop2_core_subunit (UniProtKB:P39008)\n\
    \  yeast_ccr4_not_deadenylation\tnot1_cdc39_core_subunit\tCOVERED\t->not1_cdc39_core_subunit\
    \ (UniProtKB:P25655)\n  yeast_ccr4_not_deadenylation\tnot2_cdc36_core_subunit\t\
    COVERED\t->not2_cdc36_core_subunit (UniProtKB:P06100)\n  yeast_ccr4_not_deadenylation\t\
    not3_core_subunit\tCOVERED\t->not3_core_subunit (UniProtKB:P06102)\n  yeast_ccr4_not_deadenylation\t\
    not4_mot2_core_subunit\tCOVERED\t->not4_mot2_core_subunit (UniProtKB:P34909)\n\
    \  yeast_ccr4_not_deadenylation\tnot5_core_subunit\tCOVERED\t->not5_core_subunit\
    \ (UniProtKB:Q12514)\n  yeast_ccr4_not_deadenylation\tcaf40_core_subunit\tCOVERED\t\
    ->caf40_core_subunit (UniProtKB:P53829)\n  yeast_ccr4_not_deadenylation\tcaf130_core_subunit\t\
    COVERED\t->caf130_core_subunit (UniProtKB:P53280)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     9  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     9  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: df77fec6b04694be677db0370c563d253fc0eb419d12d6e2be505a6ab7deaa7c
- evidence_id: native-ccr4_not_core_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch46-20261022-nrgmxxyw/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/ccr4_not_core_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:37:55.099008Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/ccr4_not_core_complex.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '17 of 20 collected target identifiers returned OK. PMID:11239395: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:11733989:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:11889048: UNREACHABLE; Exact native Europe PMC MED identifier,
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
  topic: Nine-subunit budding-yeast core
  outcome: supported
  target_ids:
  - GO:0030015
  summary: GO0030015 and Chen2001 native abstract identify the nine-subunit 1.0MDa
    core, distinguished from the larger 1.9MDa assembly. The generic protein-complex
    parent is appropriate.
  evidence_ids:
  - record
  - root46-sources-go
  - root46-sources-pmid-11733989
- assessment_id: composition
  area: grounding
  topic: Four exact families resolve current label-only gaps
  outcome: concern
  target_ids:
  - GO:0030015
  summary: CAF1/Pop2 IPR039637, Not1 IPR040398, Not4 IPR039780 and Caf40 IPR007216
    are full relevant subunit families cross-referenced by the examples. CCR4/nocturin
    and Not2/3/5-related xref names are broader, and Caf130 inspected hits are domains;
    they are not forced onto the unresolved rows.
  evidence_ids:
  - record
  - curation
  - root46-sources-ipr-IPR039637
  - root46-sources-ipr-IPR040398
  - root46-sources-ipr-IPR039780
  - root46-sources-ipr-IPR007216
  - root46-sources-protein-P31384
  - root46-sources-protein-P39008
  - root46-sources-protein-P25655
  - root46-sources-protein-P06100
  - root46-sources-protein-P06102
  - root46-sources-protein-P34909
  - root46-sources-protein-Q12514
  - root46-sources-protein-P53829
  - root46-sources-protein-P53280
- assessment_id: examples
  area: grounding
  topic: Nine reviewed yeast references
  outcome: supported
  target_ids:
  - GO:0030015
  summary: All accessions, aliases, entry statuses and S288C taxon identities agree;
    each declared symbol query returns its corresponding maintained entry. Localization
    annotations are not mistaken for complete membership experiments.
  evidence_ids:
  - record
  - root46-sources-protein-P31384
  - root46-sources-protein-P39008
  - root46-sources-protein-P25655
  - root46-sources-protein-P06100
  - root46-sources-protein-P06102
  - root46-sources-protein-P34909
  - root46-sources-protein-Q12514
  - root46-sources-protein-P53829
  - root46-sources-protein-P53280
  - root46-sources-gene-CCR4-559292
  - root46-sources-gene-CAF1-559292
  - root46-sources-gene-NOT1-559292
  - root46-sources-gene-NOT2-559292
  - root46-sources-gene-NOT3-559292
  - root46-sources-gene-NOT4-559292
  - root46-sources-gene-NOT5-559292
  - root46-sources-gene-CAF40-559292
  - root46-sources-gene-CAF130-559292
  - root46-sources-tax4932
  - root46-sources-tax559292
  - root46-sources-pmid-11239395
  - root46-sources-pmid-11733989
  - root46-sources-pmid-11889048
- assessment_id: necessity
  area: grounding
  topic: Formation uncertainty remains explicit
  outcome: unknown
  target_ids:
  - GO:0030015
  summary: All nine formation-necessity fields are UNKNOWN. Functional RNA-decay defects
    and Not1 cellular essentiality do not establish whether the complete structural
    complex forms after individual depletion.
  evidence_ids:
  - record
  - schema
  - root46-sources-legacy-PMC125913
- assessment_id: scope
  area: scope
  topic: Supported yeast canonical system
  outcome: supported
  target_ids:
  - GO:0030015
  summary: The Saccharomyces scope matches purification and functional studies. COMMON
    retains present-in-most-members/losses-exception meaning as a qualitative ordinary
    cellular-machinery assessment; no population census was performed.
  evidence_ids:
  - record
  - schema
  - root46-sources-pmid-11733989
  - root46-sources-legacy-PMC125913
  - root46-sources-tax4932
  - root46-sources-tax559292
- assessment_id: function
  area: evidence
  topic: Ccr4/Caf1-dependent deadenylation at complex level
  outcome: supported
  target_ids:
  - GO:0030015
  summary: The maintained wording describes the major complex activity and normal
    in-vivo dependence, not a claim that yeast Pop2 alone is necessarily the catalytic
    enzyme. Tucker2001 abstract and Tucker2002 experiments support that distinction
    and the downstream mRNA-decay role.
  evidence_ids:
  - record
  - root46-sources-go
  - root46-sources-pmid-11239395
  - root46-sources-legacy-PMC125913
- assessment_id: graph
  area: graph
  topic: Appropriately nonmechanistic function graph
  outcome: supported
  target_ids:
  - GO:0030015
  summary: Constituent-to-core links and core-to-deadenylation/decay directions match
    the cited scope. NONMECHANISTIC correctly withholds recruitment, detailed NOT
    architecture and downstream decay kinetics.
  evidence_ids:
  - record
  - root46-sources-go
  - root46-sources-pmid-11733989
  - root46-sources-pmid-11239395
  - root46-sources-legacy-PMC125913
- assessment_id: coverage
  area: completeness
  topic: Complete target and bounded family TODO
  outcome: supported
  target_ids:
  - GO:0030015
  summary: All current evidence and localization PMID identities were checked. Four
    verified whole-family mappings are actionable; unresolved domains and broad paralogue
    families remain bounded.
  evidence_ids:
  - record
  - curation
  - root46-sources-ipr-IPR039637
  - root46-sources-ipr-IPR040398
  - root46-sources-ipr-IPR039780
  - root46-sources-ipr-IPR007216
  - root46-sources-pmid-11239395
  - root46-sources-pmid-11733989
  - root46-sources-pmid-11889048
findings:
- finding_id: F1
  issue_key: ccr4-not-four-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Ground four verified CCR4-NOT subunit families
  description: CAF1/Pop2, Not1, Not4 and Caf40 remain REVIEWED_LABEL_ONLY although
    native family entries IPR039637, IPR040398, IPR039780 and IPR007216 respectively
    define their full classes and appear on the exact examples. This resolves only
    four rows of the broader historical TODO.
  target_ids:
  - GO:0030015
  field_paths:
  - components[1].grounding_status
  - components[2].grounding_status
  - components[5].grounding_status
  - components[7].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root46-sources-ipr-IPR039637
  - root46-sources-ipr-IPR040398
  - root46-sources-ipr-IPR039780
  - root46-sources-ipr-IPR007216
  - root46-sources-protein-P31384
  - root46-sources-protein-P39008
  - root46-sources-protein-P25655
  - root46-sources-protein-P06100
  - root46-sources-protein-P06102
  - root46-sources-protein-P34909
  - root46-sources-protein-Q12514
  - root46-sources-protein-P53829
  - root46-sources-protein-P53280
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ccr4_not_core_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md REVIEWED_LABEL_ONLY
  native_severity: minor
  normalization_reason: Bounded curation correction; supported biological identity
    and membership remain intact. Historical search honesty is not questioned.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0030015
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/ccr4_not_core_complex.yaml
    role: maintained scientific record
  description: Add the four exact family groundings and reconcile their notes and
    TODO coverage. Keep CCR4, Not2/3/5 and Caf130 unresolved unless separately verified
    exact families are found.
  acceptance_checks:
  - Verify exact source identities and reconcile affected current wording and TODO
    scope.
  - Preserve supported example accessions, membership and explicit unresolved claims.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw data, supplements or sequence alignments were reanalyzed.
  Primary-body inspection is limited to the explicitly listed sections.
- Chen2001 and Tucker2001 were accessible as complete native metadata/abstracts; publisher
  routes returned redirect-only pages, not article bodies. Detailed nine-subunit purification
  was not independently read in full.
- The failed DOI query for Tucker2001 returned no results; exact PMID11239395 provides
  its verified title and DOI instead. No bibliographic absence is inferred.
- CCR4 protein evidence inspection excludes FUNCTION comment bodies; membership/function
  was assessed using the stated complex and primary sources.
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
