# Acf complex scientific review

- Review: 20261022T042554Z-acf-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:58:50Z
- Finished UTC: 2026-10-22T04:25:54Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact ACF/ISWI identity, the qualified yeast Isw2/Itc1 example, two reviewed protein examples and nonmechanistic remodeling graph are supported; native two-subunit prevalence and exact class grounding remain bounded.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 9 of batch43, strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0016590 | data/structures/other/acf_complex.yaml | maintained | ACF complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0016590 | Focused validator passed. |
| Focused native strict | passed | True | GO:0016590 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0016590 | Focused check passed; scientific claims assessed separately. |
| Focused native verify | passed | True | GO:0016590 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0016590 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0016590 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0016590 | 9 of 12 collected target identifiers returned OK. PMID:11238944: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:15024052: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0016590 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0016590 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0016590 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0016590 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0016590 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact ACF class and yeast ACF-like example

identity: supported. Targets: GO:0016590.

GO0016590 explicitly includes yeast Isw2 and supports its ISWI-type parent and exact synonym. The target accurately calls its chosen Isw2/Itc1 context ACF-like, distinct from the four-subunit CHRAC-like form.

### Isw2 and Itc1 roles with conservative class grounding

grounding: supported. Targets: GO:0016590.

The two components and WAC-motif description are supported. The inspected native candidates are domains shared across proteins/complexes; withholding them as exact ACF subunit identities is justified. The open TODO does not assert all possible family catalogs were exhausted.

### Verified examples and nuclear source provenance

grounding: supported. Targets: GO:0016590.

Both reviewed accession/gene/taxon pairs and exact single-hit queries agree. Native nuclear annotation sources match the maintained PMIDs; localization alone is not used to prove membership.

### Biochemical dependence is not formation dependence

grounding: unknown. Targets: GO:0016590.

Both components use UNKNOWN. Gelbart demonstrates cooperative biochemical activities, while McConnell explicitly leaves the in-vivo status of the two-subunit versus purification-generated population uncertain.

### Yeast example and purification context

scope: supported. Targets: GO:0016590.

The species and S288C identity examples are correct. The maintained note describes the purified two-subunit complex; the paper leaves its native two-subunit status uncertain. COMMON retains the schema meaning present in most members, with losses exceptional. The selected-strain biochemical evidence supports the qualitative yeast-system scope but does not independently measure its prevalence or exclusive native stoichiometry.

### Correctly limited function graph

graph: supported. Targets: GO:0016590.

The two subunit-to-complex edges and complex-to-remodeling edge summarize demonstrated association and biochemical activity. NONMECHANISTIC explicitly withholds substrate-recognition/sliding order; source limits do not require inventing additional machinery.

### Complete target and open grounding discussion

completeness: supported. Targets: GO:0016590.

All current claims, history and discussion were read. The later four-subunit discovery is retained and considered; no confirmed defect within the declared source scope was established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/acf_complex.yaml; Entire maintained target including history, evidence, components, graphs and discussions | context_only | All maintained fields were read; past curation actions are historical provenance, not additional experimental evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Exact identity, constituent, formation-necessity and graph contracts | context_only | Source-neutral families differ from species proteins and domains; functional requirement is distinct from formation necessity. |
| root43-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0006338,GO:0008695,GO:0009334,GO:0016590,GO:0020023,GO:0031010,GO:1990204; Complete id/name/active/definition/synonym fields; direct typed parent child entries for the maintained links. Unrelated child lists are not an exhaustive ontology census. | supports | The eight native GO records support kinetoplast and mitochondrial parthood, the four-protein Hca dioxygenase and oxidoreductase parent/activity, and ACF as an ISWI-type complex with chromatin-remodeling activity. |
| root43-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxonomy response | supports | ENA verifies S.cerevisiae and rank/lineage. |
| root43-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete native taxonomy response | supports | ENA verifies S.cerevisiae S288C and rank/lineage. |
| root43-sources-pmid-11238944 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11238944+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Exact MED11238944 identifies Gelbart2001 DOI10.1128/MCB.21.6.2098-2106.2001 and its Isw2/Itc1 reconstitution and activity tests. |
| root43-sources-pmid-15024052 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15024052+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Exact MED15024052 identifies McConnell2004 DOI10.1128/MCB.24.7.2605-2613.2004 and the additional Dls1/Dpb4 subunits of four-subunit Isw2 complexes. |
| root43-sources-pmid-14562095 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Exact MED14562095 identifies Huh2003 DOI10.1038/nature02026 and the tagged yeast localization screen; the specific ISW2 nuclear annotation is verified in native UniProt, not reconstructed from the abstract. |
| root43-sources-legacy-PMC86823 | https://pmc.ncbi.nlm.nih.gov/articles/PMC86823/?report=xml; Complete Methods sec6, Results/Discussion sec14/15 with Fig4/5 captions; other sections not read | supports | Gelbart primary study identifies Itc1, separates monomers and reconstitutes Isw2/Itc1 binding/ATPase/remodeling activities. Activity differs from formation necessity and the monomer caveats are explicit. |
| root43-sources-legacy-PMC371119 | https://pmc.ncbi.nlm.nih.gov/articles/PMC371119/?report=xml; Complete Methods sec3 and Results sec9 with Fig1/2 captions; other sections not read | supports | McConnell primary study separates two- and four-subunit Isw2 fractions and detects incompletely associated populations by immunodepletion. It explicitly cannot rule out that tagging or purification destabilizes the four-subunit complex to generate the two-subunit form. |
| root43-sources-protein-Q08773 | https://rest.uniprot.org/uniprotkb/Q08773.json; Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro/Pfam xref identities; no sequence or full bibliography reanalysis | supports | Reviewed Q08773 matches ISW2 in taxon559292; current subunit annotation includes the four-protein ISW2 complex and a possible stable two-protein subcomplex. |
| root43-sources-protein-P53125 | https://rest.uniprot.org/uniprotkb/P53125.json; Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/LOCATION/SIMILARITY comments and InterPro/Pfam xref identities; no sequence or full bibliography reanalysis | supports | Reviewed P53125 matches ITC1 in taxon559292; current subunit annotation includes the four-protein ISW2 complex and a possible stable two-protein subcomplex. |
| root43-sources-gene-ISW2 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete result count and accession/status/name/gene/taxon fields | supports | Exact reviewed ISW2/taxon559292 query returns its single maintained accession. |
| root43-sources-gene-ITC1 | https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AITC1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&amp;format=json&amp;size=100; Complete result count and accession/status/name/gene/taxon fields | supports | Exact reviewed ITC1/taxon559292 query returns its single maintained accession. |
| root43-sources-ipr-IPR013136 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013136/; Complete accession/name/type and curated description | supports | Native IPR013136 is a WAC domain, not an exact full-length ACF-specific constituent class. |
| root43-sources-ipr-IPR044754 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044754/; Complete accession/name/type and curated description | supports | Native IPR044754 is a Isw1/2 N-terminal domain, not an exact full-length ACF-specific constituent class. |
| schema-result | just validate data/structures/other/acf_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/acf_complex.yaml |
| strict-result | just validate-strict data/structures/other/acf_complex.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acf_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/acf_complex.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acf_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/acf_complex-strict.tsv |
| native-acf_complex-causal-graphs | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/acf_complex.yaml; Complete focused native report | supports | data/structures/other/acf_complex.yaml  (GO:0016590)<br>  yeast_acf_chromatin_remodeling	isw2_acf_atpase_subunit	COVERED	-&gt;isw2_acf_atpase_subunit (UniProtKB:Q08773)<br>  yeast_acf_chromatin_remodeling	itc1_acf_subunit	COVERED	-&gt;itc1_acf_subunit (UniProtKB:P53125)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| native-acf_complex-verify | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/acf_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/acf_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 12 collected target identifiers returned OK. PMID:11238944: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:14562095: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim.; PMID:15024052: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, supplements, raw experiments, sequence alignments or quantitative taxon census were reanalyzed. Reading scope is specified for each source.
- The Huh2003 localization screen is complete-abstract plus exact native UniProt annotation only; the publisher response is a browser challenge, not full text. No individual screen image or table was rechecked.
- McConnell2004 explicitly cannot exclude generation of two-subunit material during tagging/purification. No universal native stoichiometry, frequency or exclusive two-subunit membership is inferred.
- Native WAC and Isw1/2 domain entries were inspected, not every protein-family catalog; the existing source-neutral class-grounding TODO remains open.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T042554Z-acf-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Acf complex scientific review
started_at: '2026-10-22T03:58:50Z'
finished_at: '2026-10-22T04:25:54Z'
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
summary: Exact ACF/ISWI identity, the qualified yeast Isw2/Itc1 example, two reviewed
  protein examples and nonmechanistic remodeling graph are supported; native two-subunit
  prevalence and exact class grounding remain bounded.
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
  - path: data/structures/other/acf_complex.yaml
    sha256: 27edd08119e44be1f4b50bd981e4642df134f6bbc3df8266b5c5b8a41d18905d
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
- target_id: GO:0016590
  path: data/structures/other/acf_complex.yaml
  label: ACF complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/acf_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 9 of batch43, strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0016590
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: just validate data/structures/other/acf_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: just validate-strict data/structures/other/acf_complex.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acf_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-acf_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/acf_complex.yaml
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-acf_complex-causal-graphs
- check_id: native-acf_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/acf_complex.yaml
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-acf_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0016590
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0016590
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - root43-sources-go
  - root43-sources-tax4932
  - root43-sources-tax559292
  - root43-sources-pmid-11238944
  - root43-sources-pmid-15024052
  - root43-sources-pmid-14562095
  - root43-sources-legacy-PMC86823
  - root43-sources-legacy-PMC371119
  - root43-sources-protein-Q08773
  - root43-sources-protein-P53125
  - root43-sources-gene-ISW2
  - root43-sources-gene-ITC1
  - root43-sources-ipr-IPR013136
  - root43-sources-ipr-IPR044754
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0016590
  summary: '9 of 12 collected target identifiers returned OK. PMID:11238944: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim.; PMID:14562095: UNREACHABLE; Exact native Europe PMC
    MED identifier, title and DOI were reviewed after the bulk eutils414 transport
    failure. Biological support remains bounded by the separately recorded abstract
    or primary-body sections; identity resolution alone is not confirmation of every
    attached claim.; PMID:15024052: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were reviewed after the bulk eutils414 transport failure. Biological
    support remains bounded by the separately recorded abstract or primary-body sections;
    identity resolution alone is not confirmation of every attached claim. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root43-sources-pmid-11238944
  - root43-sources-pmid-14562095
  - root43-sources-pmid-15024052
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0016590
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0016590
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
    and current batch43 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/acf_complex.yaml
  locator: Entire maintained target including history, evidence, components, graphs
    and discussions
  accessed_at: '2026-10-22T04:09:22Z'
  support: context_only
  summary: All maintained fields were read; past curation actions are historical provenance,
    not additional experimental evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Exact identity, constituent, formation-necessity and graph contracts
  accessed_at: '2026-10-22T04:09:22Z'
  support: context_only
  summary: Source-neutral families differ from species proteins and domains; functional
    requirement is distinct from formation necessity.
- evidence_id: root43-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0006338,GO:0008695,GO:0009334,GO:0016590,GO:0020023,GO:0031010,GO:1990204
  locator: Complete id/name/active/definition/synonym fields; direct typed parent
    child entries for the maintained links. Unrelated child lists are not an exhaustive
    ontology census.
  accessed_at: '2026-10-22T04:03:43.609653Z'
  support: supports
  summary: The eight native GO records support kinetoplast and mitochondrial parthood,
    the four-protein Hca dioxygenase and oxidoreductase parent/activity, and ACF as
    an ISWI-type complex with chromatin-remodeling activity.
  snapshot_sha256: 758170e2adf2bdecccd550d870e811d4aa0171ee8322ea75ccf5c4e3fd84ca83
- evidence_id: root43-sources-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:03:43.610130Z'
  support: supports
  summary: ENA verifies S.cerevisiae and rank/lineage.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root43-sources-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:03:43.610515Z'
  support: supports
  summary: ENA verifies S.cerevisiae S288C and rank/lineage.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root43-sources-pmid-11238944
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A11238944+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:46.991547Z'
  support: supports
  summary: Exact MED11238944 identifies Gelbart2001 DOI10.1128/MCB.21.6.2098-2106.2001
    and its Isw2/Itc1 reconstitution and activity tests.
  snapshot_sha256: 974b7929fd21cbea568f7c2941433fa0f457c719bbaab8ffe0761ccb67bf1df8
- evidence_id: root43-sources-pmid-15024052
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A15024052+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:47.138258Z'
  support: supports
  summary: Exact MED15024052 identifies McConnell2004 DOI10.1128/MCB.24.7.2605-2613.2004
    and the additional Dls1/Dpb4 subunits of four-subunit Isw2 complexes.
  snapshot_sha256: f7a985df057bbb16637a1ca3e7a4176f099847b747e91ee3c3435ca05be82afd
- evidence_id: root43-sources-pmid-14562095
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A14562095+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:47.066872Z'
  support: supports
  summary: Exact MED14562095 identifies Huh2003 DOI10.1038/nature02026 and the tagged
    yeast localization screen; the specific ISW2 nuclear annotation is verified in
    native UniProt, not reconstructed from the abstract.
  snapshot_sha256: 8bbeed3381c96852db4221aac079da00e1bf5c50630629c24d4d9136e1645c21
- evidence_id: root43-sources-legacy-PMC86823
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC86823/?report=xml
  locator: Complete Methods sec6, Results/Discussion sec14/15 with Fig4/5 captions;
    other sections not read
  accessed_at: '2026-10-22T04:04:07.825691Z'
  support: supports
  summary: Gelbart primary study identifies Itc1, separates monomers and reconstitutes
    Isw2/Itc1 binding/ATPase/remodeling activities. Activity differs from formation
    necessity and the monomer caveats are explicit.
  snapshot_sha256: 13f42480d26183d2daf84d1f234b686652d3d4657ffcc41c3d467bc729decf54
- evidence_id: root43-sources-legacy-PMC371119
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC371119/?report=xml
  locator: Complete Methods sec3 and Results sec9 with Fig1/2 captions; other sections
    not read
  accessed_at: '2026-10-22T04:04:07.998504Z'
  support: supports
  summary: McConnell primary study separates two- and four-subunit Isw2 fractions
    and detects incompletely associated populations by immunodepletion. It explicitly
    cannot rule out that tagging or purification destabilizes the four-subunit complex
    to generate the two-subunit form.
  snapshot_sha256: 3750cbc491afe0564424b4525210df24e68d0e36acdcf85896f31e8ef4a10ca6
- evidence_id: root43-sources-protein-Q08773
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q08773.json
  locator: Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/LOCATION/SIMILARITY
    comments and InterPro/Pfam xref identities; no sequence or full bibliography reanalysis
  accessed_at: '2026-10-22T04:03:45.010875Z'
  support: supports
  summary: Reviewed Q08773 matches ISW2 in taxon559292; current subunit annotation
    includes the four-protein ISW2 complex and a possible stable two-protein subcomplex.
  snapshot_sha256: 2637bfb5d984e050fbf830b95bf000a10c6cf69fd9895b6921cdfe853f59ee2c
- evidence_id: root43-sources-protein-P53125
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P53125.json
  locator: Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/LOCATION/SIMILARITY
    comments and InterPro/Pfam xref identities; no sequence or full bibliography reanalysis
  accessed_at: '2026-10-22T04:03:44.430483Z'
  support: supports
  summary: Reviewed P53125 matches ITC1 in taxon559292; current subunit annotation
    includes the four-protein ISW2 complex and a possible stable two-protein subcomplex.
  snapshot_sha256: 15a6f5624bd3147df7e928db6e548bf9a5d8e7c586453675ef5661d7d4221fd5
- evidence_id: root43-sources-gene-ISW2
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AISW2%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete result count and accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:03:47.579535Z'
  support: supports
  summary: Exact reviewed ISW2/taxon559292 query returns its single maintained accession.
  snapshot_sha256: 4a0b2c299a8108e3d0211b807a656d0b2a8cc4309334e35a687d00689cca310d
- evidence_id: root43-sources-gene-ITC1
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=%28gene_exact%3AITC1%29+AND+%28organism_id%3A559292%29+AND+%28reviewed%3Atrue%29&format=json&size=100
  locator: Complete result count and accession/status/name/gene/taxon fields
  accessed_at: '2026-10-22T04:03:47.691166Z'
  support: supports
  summary: Exact reviewed ITC1/taxon559292 query returns its single maintained accession.
  snapshot_sha256: 9555d012d20ee604810ec610e8d7bb48fa09ada92bbfafe02f82a3ac4e6f7c2f
- evidence_id: root43-sources-ipr-IPR013136
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR013136/
  locator: Complete accession/name/type and curated description
  accessed_at: '2026-10-22T04:06:48.390952Z'
  support: supports
  summary: Native IPR013136 is a WAC domain, not an exact full-length ACF-specific
    constituent class.
  snapshot_sha256: 488a03063928728b3bf2a6a15a1a53cfd9746338990d7028aa065f067d117d1e
- evidence_id: root43-sources-ipr-IPR044754
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR044754/
  locator: Complete accession/name/type and curated description
  accessed_at: '2026-10-22T04:06:48.391291Z'
  support: supports
  summary: Native IPR044754 is a Isw1/2 N-terminal domain, not an exact full-length
    ACF-specific constituent class.
  snapshot_sha256: 061068d91ce4e280dc97c8d9a97b780be29b8b80f8c5df5475c0f0511e87bf06
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/acf_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:52Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/acf_complex.yaml'
  snapshot_sha256: 08c269053e0a58e58a1a55f27f068106ddc0b955b372ef99616a9e330b55ee06
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/acf_complex.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acf_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/acf_complex.yaml\
    \ --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/acf_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/acf_complex-strict.tsv"
  snapshot_sha256: 08a93d50e9c1552ed35138fadcaa7e98b81ffa3dc55f657db1fa9625cb7741cd
- evidence_id: native-acf_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/acf_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:05:04.539710Z'
  support: supports
  summary: "data/structures/other/acf_complex.yaml  (GO:0016590)\n  yeast_acf_chromatin_remodeling\t\
    isw2_acf_atpase_subunit\tCOVERED\t->isw2_acf_atpase_subunit (UniProtKB:Q08773)\n\
    \  yeast_acf_chromatin_remodeling\titc1_acf_subunit\tCOVERED\t->itc1_acf_subunit\
    \ (UniProtKB:P53125)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     2  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     2\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: e34e9c8cebb57c5f572bee3aa6dcdb3271c14c814833d2bbe620d8bddfa7862f
- evidence_id: native-acf_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/acf_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:05:05.815438Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/acf_complex.yaml; native collect() exact identifier
    slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '9 of 12 collected target identifiers returned OK. PMID:11238944: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim.; PMID:14562095: UNREACHABLE; Exact native Europe PMC
    MED identifier, title and DOI were reviewed after the bulk eutils414 transport
    failure. Biological support remains bounded by the separately recorded abstract
    or primary-body sections; identity resolution alone is not confirmation of every
    attached claim.; PMID:15024052: UNREACHABLE; Exact native Europe PMC MED identifier,
    title and DOI were reviewed after the bulk eutils414 transport failure. Biological
    support remains bounded by the separately recorded abstract or primary-body sections;
    identity resolution alone is not confirmation of every attached claim. Native
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
  topic: Exact ACF class and yeast ACF-like example
  outcome: supported
  target_ids:
  - GO:0016590
  summary: GO0016590 explicitly includes yeast Isw2 and supports its ISWI-type parent
    and exact synonym. The target accurately calls its chosen Isw2/Itc1 context ACF-like,
    distinct from the four-subunit CHRAC-like form.
  evidence_ids:
  - record
  - root43-sources-go
  - root43-sources-legacy-PMC86823
  - root43-sources-legacy-PMC371119
- assessment_id: composition
  area: grounding
  topic: Isw2 and Itc1 roles with conservative class grounding
  outcome: supported
  target_ids:
  - GO:0016590
  summary: The two components and WAC-motif description are supported. The inspected
    native candidates are domains shared across proteins/complexes; withholding them
    as exact ACF subunit identities is justified. The open TODO does not assert all
    possible family catalogs were exhausted.
  evidence_ids:
  - record
  - schema
  - root43-sources-legacy-PMC86823
  - root43-sources-legacy-PMC371119
  - root43-sources-ipr-IPR013136
  - root43-sources-ipr-IPR044754
  - root43-sources-protein-Q08773
  - root43-sources-protein-P53125
- assessment_id: proteins
  area: grounding
  topic: Verified examples and nuclear source provenance
  outcome: supported
  target_ids:
  - GO:0016590
  summary: Both reviewed accession/gene/taxon pairs and exact single-hit queries agree.
    Native nuclear annotation sources match the maintained PMIDs; localization alone
    is not used to prove membership.
  evidence_ids:
  - record
  - root43-sources-pmid-11238944
  - root43-sources-pmid-14562095
  - root43-sources-protein-Q08773
  - root43-sources-protein-P53125
  - root43-sources-gene-ISW2
  - root43-sources-gene-ITC1
  - root43-sources-tax4932
  - root43-sources-tax559292
- assessment_id: formation
  area: grounding
  topic: Biochemical dependence is not formation dependence
  outcome: unknown
  target_ids:
  - GO:0016590
  summary: Both components use UNKNOWN. Gelbart demonstrates cooperative biochemical
    activities, while McConnell explicitly leaves the in-vivo status of the two-subunit
    versus purification-generated population uncertain.
  evidence_ids:
  - record
  - schema
  - root43-sources-legacy-PMC86823
  - root43-sources-legacy-PMC371119
- assessment_id: scope
  area: scope
  topic: Yeast example and purification context
  outcome: supported
  target_ids:
  - GO:0016590
  summary: The species and S288C identity examples are correct. The maintained note
    describes the purified two-subunit complex; the paper leaves its native two-subunit
    status uncertain. COMMON retains the schema meaning present in most members, with
    losses exceptional. The selected-strain biochemical evidence supports the qualitative
    yeast-system scope but does not independently measure its prevalence or exclusive
    native stoichiometry.
  evidence_ids:
  - record
  - root43-sources-legacy-PMC86823
  - root43-sources-legacy-PMC371119
  - root43-sources-tax4932
  - root43-sources-tax559292
- assessment_id: graph
  area: graph
  topic: Correctly limited function graph
  outcome: supported
  target_ids:
  - GO:0016590
  summary: The two subunit-to-complex edges and complex-to-remodeling edge summarize
    demonstrated association and biochemical activity. NONMECHANISTIC explicitly withholds
    substrate-recognition/sliding order; source limits do not require inventing additional
    machinery.
  evidence_ids:
  - record
  - root43-sources-go
  - root43-sources-legacy-PMC86823
  - root43-sources-legacy-PMC371119
- assessment_id: coverage
  area: completeness
  topic: Complete target and open grounding discussion
  outcome: supported
  target_ids:
  - GO:0016590
  summary: All current claims, history and discussion were read. The later four-subunit
    discovery is retained and considered; no confirmed defect within the declared
    source scope was established.
  evidence_ids:
  - record
  - root43-sources-legacy-PMC86823
  - root43-sources-legacy-PMC371119
  - root43-sources-ipr-IPR013136
  - root43-sources-ipr-IPR044754
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, supplements, raw experiments, sequence alignments or quantitative
  taxon census were reanalyzed. Reading scope is specified for each source.
- The Huh2003 localization screen is complete-abstract plus exact native UniProt annotation
  only; the publisher response is a browser challenge, not full text. No individual
  screen image or table was rechecked.
- McConnell2004 explicitly cannot exclude generation of two-subunit material during
  tagging/purification. No universal native stoichiometry, frequency or exclusive
  two-subunit membership is inferred.
- Native WAC and Isw1/2 domain entries were inspected, not every protein-family catalog;
  the existing source-neutral class-grounding TODO remains open.
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
