# Alpha dna polymerase primase complex scientific review

- Review: 20261022T043540Z-alpha-dna-polymerase-primase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:15:11Z
- Finished UTC: 2026-10-22T04:35:40Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Four-subunit identity, yeast example, protein accessions and primer-synthesis graph are supported. One grouped minor finding resolves the exact POL12 and PRI2 family groundings.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 5 of batch44 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005658 | data/structures/other/alpha_dna_polymerase_primase_complex.yaml | maintained | alpha DNA polymerase:primase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005658 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005658 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0005658 | Focused native check passed; claim-level support assessed separately. |
| Focused native verify | passed | True | GO:0005658 | Focused native check passed; claim-level support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0005658 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0005658 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005658 | 10 of 13 collected target identifiers returned OK. PMID:11395402: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:26975377: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:8621497: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005658 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005658 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005658 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005658 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005658 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Four-subunit polymerase-primase identity

identity: supported. Targets: GO:0005658.

GO0005658, exact synonyms and DNA-polymerase-complex parent agree; broad primosome synonym is correctly not promoted to exact identity.

### Four constituent classes and two exact family gaps

grounding: concern. Targets: GO:0005658.

POL12/B-subunit IPR016722 and eukaryotic PRI2 IPR016558 are exact full families cross-referenced by their verified proteins. POL1 IPR045846 is only its catalytic domain; small-primase families extend to archaeal or viral classes, so those broader candidates are not forced onto a narrower curated class.

### Exact four yeast references

grounding: supported. Targets: GO:0005658.

POL1, POL12, PRI2 and PRI1 each have one reviewed S288C result matching the maintained accession. Physical-complex membership is separately supported by the native subunit comments, yeast abstract and GO.

### Conservative formation labels

grounding: unknown. Targets: GO:0005658.

All four UNKNOWN labels avoid converting replication-essentiality or subunit phosphorylation into a direct formation-depletion result.

### Eukaryotic machinery with yeast canonical example

scope: supported. Targets: GO:0005658.

The review describes eukaryotic alpha-primase and Ferrari1996 explicitly reports four yeast subunits assembled throughout the cell cycle. Human construct experiments remain distinct. COMMON retains the schema meaning present in most members, with losses exceptional; the broad eukaryotic synthesis supports this qualitatively, without an independently measured taxon census.

### RNA-DNA primer synthesis

evidence: supported. Targets: GO:0005658.

GO and complete primary/review abstracts support small-primase RNA initiation and subsequent polymerase extension. The record does not claim exclusion of leading-strand initiation.

### Correctly nonmechanistic summary

graph: supported. Targets: GO:0005658.

Four constituent-to-complex edges and primer-synthesis output agree with the defined scope. The graph explicitly withholds motion, substrate transfer, switching and origin regulation; further mechanism is optional.

### Bounded existing grounding TODO

completeness: supported. Targets: GO:0005658.

All maintained fields and discussions were reviewed. Two verified exact families make a subset of the open TODO actionable without pretending every subunit family is now resolved.

## Findings

### F1: Resolve exact POL12 and PRI2 family groundings

minor / open / confirmed; issue key: pol-alpha-primase-exact-families.

The native full families IPR016722 (DNA polymerase alpha subunit B) and IPR016558 (eukaryotic DNA primase large subunit) match the maintained classes and verified protein mappings. These exact available terms are inconsistent with leaving those two rows REVIEWED_LABEL_ONLY solely because no CURIE was curated in the earlier pass.

## Recommended Actions And Acceptance Checks

### A1

Ground the small polymerase/B-subunit and large primase classes to the two verified families, reconcile their notes and narrow the TODO. Preserve remaining uncertainty for POL1/Pri1; do not use a catalytic domain as a whole-protein identity.

- Verify exact family identity and reconcile affected label-only notes and TODO scope.
- Preserve organism-specific examples, supported membership and current unresolved classes.
- Use guarded curation and pass applicable schema, strict, protein and graph checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/alpha_dna_polymerase_primase_complex.yaml; Entire maintained target, history, components, evidence, discussions and graphs | context_only | Every current field and historical note was read; history is provenance rather than independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, essentiality and graph scope | context_only | Protein families differ from domains and organism accessions; formation necessity differs from cellular or catalytic essentiality. |
| curation | docs/CURATION.md; Components and REVIEWED_LABEL_ONLY contract, especially lines159–160 | context_only | Reviewed label-only means no exact term exists; an explicitly verified exact family resolves a current gap even when a historical TODO remains. |
| root44-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004402,GO:0005658,GO:0005829,GO:0006269,GO:0008726,GO:0042575,GO:0070461,GO:0140671,GO:1990200,GO:1990201,GO:1990202,GO:1990204; Complete requested id/name/active/definition/synonym fields and typed maintained parent/parthood/activity links | supports | Native GO definitions, synonyms and maintained typed relationships support these exact complex classes. GO0140671 retains the unrelated PMID28966424 xref, which is appropriately excluded from biological support. |
| root44-sources-pmid-11395402 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11395402+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native MED id/title/authors/year/DOI and complete abstract | supports | MED11395402: DNA primases. DOI 10.1146/annurev.biochem.70.1.39; complete abstract read. Bibliographic identity and abstract-level findings only; any inspected primary body has its own evidence row. |
| root44-sources-pmid-26975377 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A26975377+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native MED id/title/authors/year/DOI and complete abstract | supports | MED26975377: Mechanism of Concerted RNA-DNA Primer Synthesis by the Human Primosome. DOI 10.1074/jbc.m116.717405; complete abstract read. Bibliographic identity and abstract-level findings only; any inspected primary body has its own evidence row. |
| root44-sources-pmid-8621497 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8621497+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native MED id/title/authors/year/DOI and complete abstract | supports | MED8621497: Phosphorylation of the DNA polymerase alpha-primase B subunit is dependent on its association with the p180 polypeptide. DOI 10.1074/jbc.271.15.8661; complete abstract read. Bibliographic identity and abstract-level findings only; any inspected primary body has its own evidence row. |
| root44-sources-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete native taxonomy response | supports | ENA confirms the maintained scientific name, rank, aliases and lineage for 2759. |
| root44-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA confirms the maintained scientific name, rank, aliases and lineage for 4932. |
| root44-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | ENA confirms the maintained scientific name, rank, aliases and lineage for 559292. |
| root44-sources-protein-P13382 | https://rest.uniprot.org/uniprotkb/P13382.json; primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY; InterPro/Pfam cross-reference ids | supports | Reviewed accession P13382 has the maintained gene/aliases and taxon. Complete SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization citations do not by themselves establish membership. |
| root44-sources-protein-P38121 | https://rest.uniprot.org/uniprotkb/P38121.json; primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY; InterPro/Pfam cross-reference ids | supports | Reviewed accession P38121 has the maintained gene/aliases and taxon. Complete SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization citations do not by themselves establish membership. |
| root44-sources-protein-P20457 | https://rest.uniprot.org/uniprotkb/P20457.json; primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY; InterPro/Pfam cross-reference ids | supports | Reviewed accession P20457 has the maintained gene/aliases and taxon. Complete SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization citations do not by themselves establish membership. |
| root44-sources-protein-P10363 | https://rest.uniprot.org/uniprotkb/P10363.json; primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY; InterPro/Pfam cross-reference ids | supports | Reviewed accession P10363 has the maintained gene/aliases and taxon. Complete SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization citations do not by themselves establish membership. |
| root44-sources-gene-POL1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete result count, accession/status/name/gene/taxon fields | supports | Exact reviewed POL1/taxon559292 query returns one result, the maintained accession. |
| root44-sources-gene-POL12 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL12%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete result count, accession/status/name/gene/taxon fields | supports | Exact reviewed POL12/taxon559292 query returns one result, the maintained accession. |
| root44-sources-gene-PRI2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APRI2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete result count, accession/status/name/gene/taxon fields | supports | Exact reviewed PRI2/taxon559292 query returns one result, the maintained accession. |
| root44-sources-gene-PRI1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APRI1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete result count, accession/status/name/gene/taxon fields | supports | Exact reviewed PRI1/taxon559292 query returns one result, the maintained accession. |
| root44-sources-ipr-IPR016722 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016722/; Complete native accession/name/type/description; not a sequence-alignment reanalysis | supports | IPR016722 is a family named DNA polymerase alpha, subunit B. Its complete description was inspected and compared with the component class and protein cross-reference. |
| root44-sources-ipr-IPR016558 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016558/; Complete native accession/name/type/description; not a sequence-alignment reanalysis | supports | IPR016558 is a family named DNA primase, large subunit, eukaryotic. Its complete description was inspected and compared with the component class and protein cross-reference. |
| root44-sources-ipr-IPR014052 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014052/; Complete native accession/name/type/description; not a sequence-alignment reanalysis | supports | IPR014052 is a family named DNA primase, small subunit, eukaryotic/archaeal. Its complete description was inspected and compared with the component class and protein cross-reference. |
| root44-sources-ipr-IPR002755 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002755/; Complete native accession/name/type/description; not a sequence-alignment reanalysis | supports | IPR002755 is a family named DNA primase, small subunit. Its complete description was inspected and compared with the component class and protein cross-reference. |
| root44-sources-ipr-IPR045846 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045846/; Complete native accession/name/type/description; not a sequence-alignment reanalysis | supports | IPR045846 is a domain named DNA polymerase alpha catalytic subunit, catalytic domain. Its complete description was inspected and compared with the component class and protein cross-reference. |
| root44-sources-legacy-PMC4858955 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4858955/?report=xml; Complete Methods sec5/8 and Results sec16/17 including Fig2–6 captions; later mechanism sections, image pixels and supplements not read | supports | Human primosome crystallography supports the four-subunit framework and two catalytic centers; the recombinant p180 construct lacks residues1–334. This human structural context supports conserved architecture without replacing the yeast canonical evidence or implying native S288C structural measurements. |
| schema-result | just validate data/structures/other/alpha_dna_polymerase_primase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/alpha_dna_polymerase_primase_complex.yaml |
| strict-result | just validate-strict data/structures/other/alpha_dna_polymerase_primase_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alpha_dna_polymerase_primase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/alpha_dna_polymerase_primase_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alpha_dna_polymerase_primase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/alpha_dna_polymerase_primase_complex-strict.tsv |
| native-alpha_dna_polymerase_primase_complex-causal-graphs | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/alpha_dna_polymerase_primase_complex.yaml; Complete focused native report | supports | data/structures/other/alpha_dna_polymerase_primase_complex.yaml  (GO:0005658)<br>  pol_alpha_primase_synthesizes_primers	dna_polymerase_alpha_large_subunit	COVERED	-&gt;dna_polymerase_alpha_large_subunit (UniProtKB:P13382)<br>  pol_alpha_primase_synthesizes_primers	dna_polymerase_alpha_small_subunit	COVERED	-&gt;dna_polymerase_alpha_small_subunit (UniProtKB:P38121)<br>  pol_alpha_primase_synthesizes_primers	dna_primase_large_subunit	COVERED	-&gt;dna_primase_large_subunit (UniProtKB:P20457)<br>  pol_alpha_primase_synthesizes_primers	dna_primase_small_subunit	COVERED	-&gt;dna_primase_small_subunit (UniProtKB:P10363)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-alpha_dna_polymerase_primase_complex-verify | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/alpha_dna_polymerase_primase_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/alpha_dna_polymerase_primase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 13 collected target identifiers returned OK. PMID:11395402: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:26975377: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force.; PMID:8621497: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw experiments, supplemental datasets or sequence alignments were reanalyzed. Exact body reading scope is stated in each evidence row.
- Ferrari1996 and Frick2001 were read at complete-abstract tier; the Ferrari publisher route failed. Human2016 inspection is restricted to the stated sections and engineered-construct context.
- Eukaryotic scope is supported by the review and exact class; the ontology taxon-constraint axiom was not independently retrieved. No quantitative prevalence or universal strain-specific stoichiometry is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T043540Z-alpha-dna-polymerase-primase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Alpha dna polymerase primase complex scientific review
started_at: '2026-10-22T04:15:11Z'
finished_at: '2026-10-22T04:35:40Z'
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
summary: Four-subunit identity, yeast example, protein accessions and primer-synthesis
  graph are supported. One grouped minor finding resolves the exact POL12 and PRI2
  family groundings.
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
  - path: data/structures/other/alpha_dna_polymerase_primase_complex.yaml
    sha256: efa26498f03abfddfde91ca7cb10b78740b65eac7cbd1a9c81436d884a2f5a76
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
- target_id: GO:0005658
  path: data/structures/other/alpha_dna_polymerase_primase_complex.yaml
  label: alpha DNA polymerase:primase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/alpha_dna_polymerase_primase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 5 of batch44 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005658
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005658
  command: just validate data/structures/other/alpha_dna_polymerase_primase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005658
  command: just validate-strict data/structures/other/alpha_dna_polymerase_primase_complex.yaml
    --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alpha_dna_polymerase_primase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-alpha_dna_polymerase_primase_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005658
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/alpha_dna_polymerase_primase_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-alpha_dna_polymerase_primase_complex-causal-graphs
- check_id: native-alpha_dna_polymerase_primase_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0005658
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/alpha_dna_polymerase_primase_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-alpha_dna_polymerase_primase_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005658
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005658
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root44-sources-go
  - root44-sources-pmid-11395402
  - root44-sources-pmid-26975377
  - root44-sources-pmid-8621497
  - root44-sources-tax2759
  - root44-sources-tax4932
  - root44-sources-tax559292
  - root44-sources-protein-P13382
  - root44-sources-protein-P38121
  - root44-sources-protein-P20457
  - root44-sources-protein-P10363
  - root44-sources-gene-POL1
  - root44-sources-gene-POL12
  - root44-sources-gene-PRI2
  - root44-sources-gene-PRI1
  - root44-sources-ipr-IPR016722
  - root44-sources-ipr-IPR016558
  - root44-sources-ipr-IPR014052
  - root44-sources-ipr-IPR002755
  - root44-sources-ipr-IPR045846
  - root44-sources-legacy-PMC4858955
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005658
  summary: '10 of 13 collected target identifiers returned OK. PMID:11395402: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:26975377:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:8621497: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were inspected after the bulk eutils414 transport failure. Identity
    resolution does not certify every attached biological claim; declared abstract/body
    reading scope remains in force. Native source checks are separately scoped; skipped
    or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root44-sources-pmid-11395402
  - root44-sources-pmid-26975377
  - root44-sources-pmid-8621497
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005658
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
  - GO:0005658
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
  - GO:0005658
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
  - GO:0005658
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
  - GO:0005658
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
  reference: data/structures/other/alpha_dna_polymerase_primase_complex.yaml
  locator: Entire maintained target, history, components, evidence, discussions and
    graphs
  accessed_at: '2026-10-22T04:20:12Z'
  support: context_only
  summary: Every current field and historical note was read; history is provenance
    rather than independent scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, essentiality and graph scope
  accessed_at: '2026-10-22T04:20:12Z'
  support: context_only
  summary: Protein families differ from domains and organism accessions; formation
    necessity differs from cellular or catalytic essentiality.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components and REVIEWED_LABEL_ONLY contract, especially lines159–160
  accessed_at: '2026-10-22T04:20:12Z'
  support: context_only
  summary: Reviewed label-only means no exact term exists; an explicitly verified
    exact family resolves a current gap even when a historical TODO remains.
- evidence_id: root44-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004402,GO:0005658,GO:0005829,GO:0006269,GO:0008726,GO:0042575,GO:0070461,GO:0140671,GO:1990200,GO:1990201,GO:1990202,GO:1990204
  locator: Complete requested id/name/active/definition/synonym fields and typed maintained
    parent/parthood/activity links
  accessed_at: '2026-10-22T04:15:35.968772Z'
  support: supports
  summary: Native GO definitions, synonyms and maintained typed relationships support
    these exact complex classes. GO0140671 retains the unrelated PMID28966424 xref,
    which is appropriately excluded from biological support.
  snapshot_sha256: fac3f615f0c72d3b731dc777be0ab009b135c9f0f3bcad4ad0df1470840c770e
- evidence_id: root44-sources-pmid-11395402
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11395402+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native MED id/title/authors/year/DOI and complete abstract
  accessed_at: '2026-10-22T04:15:39.929484Z'
  support: supports
  summary: 'MED11395402: DNA primases. DOI 10.1146/annurev.biochem.70.1.39; complete
    abstract read. Bibliographic identity and abstract-level findings only; any inspected
    primary body has its own evidence row.'
  snapshot_sha256: 9bd2bab458c944357ce2c8b46c4b90d887641c6a13a448c4bce538153bf6dea3
- evidence_id: root44-sources-pmid-26975377
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A26975377+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native MED id/title/authors/year/DOI and complete abstract
  accessed_at: '2026-10-22T04:15:40.455196Z'
  support: supports
  summary: 'MED26975377: Mechanism of Concerted RNA-DNA Primer Synthesis by the Human
    Primosome. DOI 10.1074/jbc.m116.717405; complete abstract read. Bibliographic
    identity and abstract-level findings only; any inspected primary body has its
    own evidence row.'
  snapshot_sha256: 3d42724e8187201cd88f1399e6089f6fcddc7ffae00e0b4fc084968b870298e0
- evidence_id: root44-sources-pmid-8621497
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A8621497+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native MED id/title/authors/year/DOI and complete abstract
  accessed_at: '2026-10-22T04:15:40.540019Z'
  support: supports
  summary: 'MED8621497: Phosphorylation of the DNA polymerase alpha-primase B subunit
    is dependent on its association with the p180 polypeptide. DOI 10.1074/jbc.271.15.8661;
    complete abstract read. Bibliographic identity and abstract-level findings only;
    any inspected primary body has its own evidence row.'
  snapshot_sha256: effabdc3fdfe3f059dec300e19736e0a8e558b4ec318cb591a78cf6e919464d5
- evidence_id: root44-sources-tax2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:15:35.969004Z'
  support: supports
  summary: ENA confirms the maintained scientific name, rank, aliases and lineage
    for 2759.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: root44-sources-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:15:35.969098Z'
  support: supports
  summary: ENA confirms the maintained scientific name, rank, aliases and lineage
    for 4932.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root44-sources-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:15:35.969184Z'
  support: supports
  summary: ENA confirms the maintained scientific name, rank, aliases and lineage
    for 559292.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root44-sources-protein-P13382
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P13382.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY;
    InterPro/Pfam cross-reference ids
  accessed_at: '2026-10-22T04:15:36.751730Z'
  support: supports
  summary: Reviewed accession P13382 has the maintained gene/aliases and taxon. Complete
    SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization
    citations do not by themselves establish membership.
  snapshot_sha256: 53bfe9b9b65e3355a8d5d9a0eecb8e039cbb09dbec5c0f5276d84462b0f2f300
- evidence_id: root44-sources-protein-P38121
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P38121.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY;
    InterPro/Pfam cross-reference ids
  accessed_at: '2026-10-22T04:15:38.210682Z'
  support: supports
  summary: Reviewed accession P38121 has the maintained gene/aliases and taxon. Complete
    SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization
    citations do not by themselves establish membership.
  snapshot_sha256: b96475551850dc6e2968f19c089c303bb7b2ebc9b1a627e0b54a5b74dcaeafd4
- evidence_id: root44-sources-protein-P20457
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P20457.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY;
    InterPro/Pfam cross-reference ids
  accessed_at: '2026-10-22T04:15:36.751870Z'
  support: supports
  summary: Reviewed accession P20457 has the maintained gene/aliases and taxon. Complete
    SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization
    citations do not by themselves establish membership.
  snapshot_sha256: 6977005b2ad73751943095ccab0e53b991631a3aab8298c93eb6b6c9b2eb66a5
- evidence_id: root44-sources-protein-P10363
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P10363.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY;
    InterPro/Pfam cross-reference ids
  accessed_at: '2026-10-22T04:15:36.714085Z'
  support: supports
  summary: Reviewed accession P10363 has the maintained gene/aliases and taxon. Complete
    SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization
    citations do not by themselves establish membership.
  snapshot_sha256: b1324eb398c942ba08194aa8d031bce9c64c1d00c760f0bd739e658a4f1e4992
- evidence_id: root44-sources-gene-POL1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete result count, accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:17:40.405348Z'
  support: supports
  summary: Exact reviewed POL1/taxon559292 query returns one result, the maintained
    accession.
  snapshot_sha256: b3696125ee30f08216a597dd7631b9212beb2601746dea728a507e000bd90f76
- evidence_id: root44-sources-gene-POL12
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APOL12%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete result count, accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:17:40.458034Z'
  support: supports
  summary: Exact reviewed POL12/taxon559292 query returns one result, the maintained
    accession.
  snapshot_sha256: 88402b233f5ed8e7bc397a5ce65753cefcf58f9f9e8040c8db264169aef28d54
- evidence_id: root44-sources-gene-PRI2
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APRI2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete result count, accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:17:41.323112Z'
  support: supports
  summary: Exact reviewed PRI2/taxon559292 query returns one result, the maintained
    accession.
  snapshot_sha256: 99968f926c0eff2b55083299153b90cba66bf6e17db5cf32d69e8368051fd70b
- evidence_id: root44-sources-gene-PRI1
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3APRI1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete result count, accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:17:40.520816Z'
  support: supports
  summary: Exact reviewed PRI1/taxon559292 query returns one result, the maintained
    accession.
  snapshot_sha256: 4db39050382ac3a6033b4f5898650a5e8ed863e470922d393bff007e99910ef5
- evidence_id: root44-sources-ipr-IPR016722
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016722/
  locator: Complete native accession/name/type/description; not a sequence-alignment
    reanalysis
  accessed_at: '2026-10-22T04:16:44.015324Z'
  support: supports
  summary: IPR016722 is a family named DNA polymerase alpha, subunit B. Its complete
    description was inspected and compared with the component class and protein cross-reference.
  snapshot_sha256: 1363abf1d9808a390e99bef9522525d899ea8b07f8fe83ab1e801399b9028a7d
- evidence_id: root44-sources-ipr-IPR016558
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016558/
  locator: Complete native accession/name/type/description; not a sequence-alignment
    reanalysis
  accessed_at: '2026-10-22T04:16:43.268541Z'
  support: supports
  summary: IPR016558 is a family named DNA primase, large subunit, eukaryotic. Its
    complete description was inspected and compared with the component class and protein
    cross-reference.
  snapshot_sha256: 24923f319415f3e088568726624511b580a4933260b3279d4ce4f2e837fe19cf
- evidence_id: root44-sources-ipr-IPR014052
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR014052/
  locator: Complete native accession/name/type/description; not a sequence-alignment
    reanalysis
  accessed_at: '2026-10-22T04:16:44.021552Z'
  support: supports
  summary: IPR014052 is a family named DNA primase, small subunit, eukaryotic/archaeal.
    Its complete description was inspected and compared with the component class and
    protein cross-reference.
  snapshot_sha256: 4e7a171848f0229cb8d9d2cfa797ed3cd6a422bf6d50e766d5b9a30fc4725a33
- evidence_id: root44-sources-ipr-IPR002755
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002755/
  locator: Complete native accession/name/type/description; not a sequence-alignment
    reanalysis
  accessed_at: '2026-10-22T04:16:44.047761Z'
  support: supports
  summary: IPR002755 is a family named DNA primase, small subunit. Its complete description
    was inspected and compared with the component class and protein cross-reference.
  snapshot_sha256: 33b5c78d5e145cdb8aa58864999f2437bb12e2be7695489f7a80b436328a0500
- evidence_id: root44-sources-ipr-IPR045846
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR045846/
  locator: Complete native accession/name/type/description; not a sequence-alignment
    reanalysis
  accessed_at: '2026-10-22T04:16:44.033319Z'
  support: supports
  summary: IPR045846 is a domain named DNA polymerase alpha catalytic subunit, catalytic
    domain. Its complete description was inspected and compared with the component
    class and protein cross-reference.
  snapshot_sha256: d3f9c7187f942536b387f905f4b960bb398bdeeb9aab73a86739f2c0c2f9fa5a
- evidence_id: root44-sources-legacy-PMC4858955
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4858955/?report=xml
  locator: Complete Methods sec5/8 and Results sec16/17 including Fig2–6 captions;
    later mechanism sections, image pixels and supplements not read
  accessed_at: '2026-10-22T04:16:10.994867Z'
  support: supports
  summary: Human primosome crystallography supports the four-subunit framework and
    two catalytic centers; the recombinant p180 construct lacks residues1–334. This
    human structural context supports conserved architecture without replacing the
    yeast canonical evidence or implying native S288C structural measurements.
  snapshot_sha256: c71d0c0179cbccbb7b3a5e18c5ad00f2e26d9d69c1b8a17383fd93b6b0b9c03f
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/alpha_dna_polymerase_primase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:12Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/alpha_dna_polymerase_primase_complex.yaml'
  snapshot_sha256: e3fb69d42254acc03ff72388067f9fd8fa242ff47eb59654f004a6630988afce
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/alpha_dna_polymerase_primase_complex.yaml
    --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alpha_dna_polymerase_primase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:13Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/alpha_dna_polymerase_primase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alpha_dna_polymerase_primase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/alpha_dna_polymerase_primase_complex-strict.tsv"
  snapshot_sha256: 6aa32b42328736a39481489d821bbe45259188cd0b1123b891306cf77a4e6210
- evidence_id: native-alpha_dna_polymerase_primase_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/alpha_dna_polymerase_primase_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:15:55.565280Z'
  support: supports
  summary: "data/structures/other/alpha_dna_polymerase_primase_complex.yaml  (GO:0005658)\n\
    \  pol_alpha_primase_synthesizes_primers\tdna_polymerase_alpha_large_subunit\t\
    COVERED\t->dna_polymerase_alpha_large_subunit (UniProtKB:P13382)\n  pol_alpha_primase_synthesizes_primers\t\
    dna_polymerase_alpha_small_subunit\tCOVERED\t->dna_polymerase_alpha_small_subunit\
    \ (UniProtKB:P38121)\n  pol_alpha_primase_synthesizes_primers\tdna_primase_large_subunit\t\
    COVERED\t->dna_primase_large_subunit (UniProtKB:P20457)\n  pol_alpha_primase_synthesizes_primers\t\
    dna_primase_small_subunit\tCOVERED\t->dna_primase_small_subunit (UniProtKB:P10363)\n\
    \ncausal_graphs GENE_OR_PROTEIN node summary:\n     4  COVERED               \
    \    component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     4\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 4ba9a9745504b77fb4c0171ed82eaf264633876444ee68611246ee4a1ee20f79
- evidence_id: native-alpha_dna_polymerase_primase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/alpha_dna_polymerase_primase_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:15:56.850593Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/alpha_dna_polymerase_primase_complex.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 13 collected target identifiers returned OK. PMID:11395402: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force.; PMID:26975377:
    UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected
    after the bulk eutils414 transport failure. Identity resolution does not certify
    every attached biological claim; declared abstract/body reading scope remains
    in force.; PMID:8621497: UNREACHABLE; Exact native Europe PMC MED identifier,
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
  topic: Four-subunit polymerase-primase identity
  outcome: supported
  target_ids:
  - GO:0005658
  summary: GO0005658, exact synonyms and DNA-polymerase-complex parent agree; broad
    primosome synonym is correctly not promoted to exact identity.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-legacy-PMC4858955
- assessment_id: composition
  area: grounding
  topic: Four constituent classes and two exact family gaps
  outcome: concern
  target_ids:
  - GO:0005658
  summary: POL12/B-subunit IPR016722 and eukaryotic PRI2 IPR016558 are exact full
    families cross-referenced by their verified proteins. POL1 IPR045846 is only its
    catalytic domain; small-primase families extend to archaeal or viral classes,
    so those broader candidates are not forced onto a narrower curated class.
  evidence_ids:
  - record
  - curation
  - root44-sources-go
  - root44-sources-ipr-IPR016722
  - root44-sources-ipr-IPR016558
  - root44-sources-ipr-IPR014052
  - root44-sources-ipr-IPR002755
  - root44-sources-ipr-IPR045846
  - root44-sources-protein-P13382
  - root44-sources-protein-P38121
  - root44-sources-protein-P20457
  - root44-sources-protein-P10363
- assessment_id: examples
  area: grounding
  topic: Exact four yeast references
  outcome: supported
  target_ids:
  - GO:0005658
  summary: POL1, POL12, PRI2 and PRI1 each have one reviewed S288C result matching
    the maintained accession. Physical-complex membership is separately supported
    by the native subunit comments, yeast abstract and GO.
  evidence_ids:
  - record
  - root44-sources-pmid-8621497
  - root44-sources-protein-P13382
  - root44-sources-protein-P38121
  - root44-sources-protein-P20457
  - root44-sources-protein-P10363
  - root44-sources-gene-POL1
  - root44-sources-gene-POL12
  - root44-sources-gene-PRI2
  - root44-sources-gene-PRI1
  - root44-sources-tax2759
  - root44-sources-tax4932
  - root44-sources-tax559292
- assessment_id: necessity
  area: grounding
  topic: Conservative formation labels
  outcome: unknown
  target_ids:
  - GO:0005658
  summary: All four UNKNOWN labels avoid converting replication-essentiality or subunit
    phosphorylation into a direct formation-depletion result.
  evidence_ids:
  - record
  - schema
  - root44-sources-pmid-8621497
- assessment_id: scope
  area: scope
  topic: Eukaryotic machinery with yeast canonical example
  outcome: supported
  target_ids:
  - GO:0005658
  summary: The review describes eukaryotic alpha-primase and Ferrari1996 explicitly
    reports four yeast subunits assembled throughout the cell cycle. Human construct
    experiments remain distinct. COMMON retains the schema meaning present in most
    members, with losses exceptional; the broad eukaryotic synthesis supports this
    qualitatively, without an independently measured taxon census.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-legacy-PMC4858955
  - root44-sources-tax2759
  - root44-sources-tax4932
  - root44-sources-tax559292
  - root44-sources-pmid-11395402
  - root44-sources-pmid-26975377
  - root44-sources-pmid-8621497
- assessment_id: function
  area: evidence
  topic: RNA-DNA primer synthesis
  outcome: supported
  target_ids:
  - GO:0005658
  summary: GO and complete primary/review abstracts support small-primase RNA initiation
    and subsequent polymerase extension. The record does not claim exclusion of leading-strand
    initiation.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-legacy-PMC4858955
  - root44-sources-pmid-11395402
  - root44-sources-pmid-26975377
  - root44-sources-pmid-8621497
- assessment_id: graph
  area: graph
  topic: Correctly nonmechanistic summary
  outcome: supported
  target_ids:
  - GO:0005658
  summary: Four constituent-to-complex edges and primer-synthesis output agree with
    the defined scope. The graph explicitly withholds motion, substrate transfer,
    switching and origin regulation; further mechanism is optional.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-legacy-PMC4858955
- assessment_id: coverage
  area: completeness
  topic: Bounded existing grounding TODO
  outcome: supported
  target_ids:
  - GO:0005658
  summary: All maintained fields and discussions were reviewed. Two verified exact
    families make a subset of the open TODO actionable without pretending every subunit
    family is now resolved.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-ipr-IPR016722
  - root44-sources-ipr-IPR016558
  - root44-sources-ipr-IPR014052
  - root44-sources-ipr-IPR002755
  - root44-sources-ipr-IPR045846
findings:
- finding_id: F1
  issue_key: pol-alpha-primase-exact-families
  category: grounding
  severity: minor
  status: open
  certainty: confirmed
  title: Resolve exact POL12 and PRI2 family groundings
  description: The native full families IPR016722 (DNA polymerase alpha subunit B)
    and IPR016558 (eukaryotic DNA primase large subunit) match the maintained classes
    and verified protein mappings. These exact available terms are inconsistent with
    leaving those two rows REVIEWED_LABEL_ONLY solely because no CURIE was curated
    in the earlier pass.
  target_ids:
  - GO:0005658
  field_paths:
  - components[1].grounding_status
  - components[2].grounding_status
  - discussions[0]
  evidence_ids:
  - record
  - curation
  - root44-sources-ipr-IPR016722
  - root44-sources-ipr-IPR016558
  - root44-sources-protein-P13382
  - root44-sources-protein-P38121
  - root44-sources-protein-P20457
  - root44-sources-protein-P10363
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/alpha_dna_polymerase_primase_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md REVIEWED_LABEL_ONLY
  native_severity: minor
  normalization_reason: Correct biological identity and membership; a verified exact
    family makes this bounded grounding gap actionable. Historical search honesty
    is not questioned.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005658
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/alpha_dna_polymerase_primase_complex.yaml
    role: maintained scientific record
  description: Ground the small polymerase/B-subunit and large primase classes to
    the two verified families, reconcile their notes and narrow the TODO. Preserve
    remaining uncertainty for POL1/Pri1; do not use a catalytic domain as a whole-protein
    identity.
  acceptance_checks:
  - Verify exact family identity and reconcile affected label-only notes and TODO
    scope.
  - Preserve organism-specific examples, supported membership and current unresolved
    classes.
  - Use guarded curation and pass applicable schema, strict, protein and graph checks.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw experiments, supplemental datasets or sequence alignments
  were reanalyzed. Exact body reading scope is stated in each evidence row.
- Ferrari1996 and Frick2001 were read at complete-abstract tier; the Ferrari publisher
  route failed. Human2016 inspection is restricted to the stated sections and engineered-construct
  context.
- Eukaryotic scope is supported by the review and exact class; the ontology taxon-constraint
  axiom was not independently retrieved. No quantitative prevalence or universal strain-specific
  stoichiometry is inferred.
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
