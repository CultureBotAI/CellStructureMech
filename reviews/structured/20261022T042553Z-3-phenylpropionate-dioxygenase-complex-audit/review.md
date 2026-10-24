# 3 phenylpropionate dioxygenase complex scientific review

- Review: 20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:58:48Z
- Finished UTC: 2026-10-22T04:25:53Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Four exact Hca protein families and reviewed K12 examples, GO identity/activity and the coarse classIIB electron-transfer graph are supported, with sequence-based assignments distinguished from directly measured whole-cell pathway activity.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 8 of batch43, strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009334 | data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml | maintained | 3-phenylpropionate dioxygenase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0009334 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009334 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:0009334 | Focused check passed; scientific claims assessed separately. |
| Focused native verify | passed | True | GO:0009334 | Focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0009334 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:0009334 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0009334 | 13 of 14 collected target identifiers returned OK. PMID:9603882: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0009334 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009334 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009334 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009334 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0009334 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Four-component oxidoreductase complex

identity: supported. Targets: GO:0009334.

The exact GO definition, parent and activity match the maintained record, with HcaE/HcaF equivalent to historical HcaA1/HcaA2. Downstream HcaB dehydrogenase is not confused with the modern hcaF alias.

### Four exact family-grounded constituents

grounding: supported. Targets: GO:0009334.

All four InterPro terms are exact families; all four reviewed protein examples have correct accession, gene and K12 taxon. The constituent roles agree with the primary cluster study and curated authorities.

### Honest formation uncertainty

grounding: unknown. Targets: GO:0009334.

UNKNOWN values avoid converting pathway activity or a knockout growth phenotype into evidence that the multicomponent assembly cannot form.

### E.coli K12 experimental example

scope: supported. Targets: GO:0009334.

The primary study uses E.coli K12 strains and recombinant Salmonella; the maintained K12 example is correct. No universal bacterial distribution is asserted.

### Dioxygenation distinct from downstream dehydrogenation

evidence: supported. Targets: GO:0009334.

GO0008695 supports the maintained NADH/oxygen/proton reaction and PP-dihydrodiol product. The original whole-cell DHPP assay includes downstream HcaB; neither it nor a database label proves direct per-step enzyme kinetics. The record states pathway architecture rather than a purified reconstitution experiment.

### Coarse mechanistic electron-transfer synthesis

graph: supported. Targets: GO:0009334.

The four edges describe the accepted classIIB reductase-to-ferredoxin-to-oxygenase architecture, alpha/beta core association and catalysis. This is a causal biochemical model beyond parthood, so MECHANISTIC is appropriate, but the cited1998 sequence-based assignments are not independently measured individual electron transfers.

### Complete target and correct reference placement

completeness: supported. Targets: GO:0009334.

All components, protein examples, current graph and history were read. No confirmed mismatch in the maintained identity or bounded claims was established.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml; Entire maintained target including history, evidence, components, graphs and discussions | context_only | All maintained fields were read; past curation actions are historical provenance, not additional experimental evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Exact identity, constituent, formation-necessity and graph contracts | context_only | Source-neutral families differ from species proteins and domains; functional requirement is distinct from formation necessity. |
| root43-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005739,GO:0006338,GO:0008695,GO:0009334,GO:0016590,GO:0020023,GO:0031010,GO:1990204; Complete id/name/active/definition/synonym fields; direct typed parent child entries for the maintained links. Unrelated child lists are not an exhaustive ontology census. | supports | The eight native GO records support kinetoplast and mitochondrial parthood, the four-protein Hca dioxygenase and oxidoreductase parent/activity, and ACF as an ISWI-type complex with chromatin-remodeling activity. |
| root43-sources-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxonomy response | supports | ENA verifies E.coli K-12 and the K12 alias. |
| root43-sources-pmid-9603882 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9603882+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | Exact MED9603882 identifies Diaz,Ferrandez and Garcia1998 DOI10.1128/JB.180.11.2915-2923.1998 and its hca cluster characterization. |
| root43-sources-doi-4 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.180.11.2915-2923.1998&amp;format=json&amp;resultType=core; Complete native MED bibliographic identity and complete returned abstract | supports | The DOI query independently returns the same MED9603882 and PMC107259. Sequence homology assigns the four dioxygenase proteins; resting-cell pathway activity is distinguished from isolated-subunit kinetics. |
| root43-sources-legacy-PMC107259 | https://pmc.ncbi.nlm.nih.gov/articles/PMC107259/?report=xml; Complete Methods sec2 and sec7, Results/Discussion sec10 including Table1 and sec12; other sections/supplements not read | supports | Diaz1998 directly reports hcaA1 disruption, complementation and resting-cell PP-to-DHPP assays, with downstream HcaB distinct from HcaA1/A2/C/D. The four subunit roles and classIIB electron-transfer architecture are based on sequence comparison and established homologous systems, not direct kinetic reconstitution of each transfer step. |
| root43-sources-ipr-IPR020875 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020875/; Complete native accession/name/type and curated description | supports | Native IPR020875 is the exact Hca alpha protein family, not merely its constituent domain. |
| root43-sources-ipr-IPR023712 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023712/; Complete native accession/name/type and curated description | supports | Native IPR023712 is the exact Hca beta protein family, not merely its constituent domain. |
| root43-sources-ipr-IPR023739 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023739/; Complete native accession/name/type and curated description | supports | Native IPR023739 is the exact Hca ferredoxin protein family, not merely its constituent domain. |
| root43-sources-ipr-IPR023744 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023744/; Complete native accession/name/type and curated description | supports | Native IPR023744 is the exact Hca reductase protein family, not merely its constituent domain. |
| root43-sources-protein-P0ABR5 | https://rest.uniprot.org/uniprotkb/P0ABR5.json; Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/SIMILARITY comments and InterPro/Pfam xref identities; sequence and full bibliography not reanalyzed | supports | Reviewed P0ABR5 matches the maintained hcaE identity and E.coli K12 taxon83333. Native function/subunit annotations distinguish established architecture from specific direct activity evidence. |
| root43-sources-protein-Q47140 | https://rest.uniprot.org/uniprotkb/Q47140.json; Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/SIMILARITY comments and InterPro/Pfam xref identities; sequence and full bibliography not reanalyzed | supports | Reviewed Q47140 matches the maintained hcaF identity and E.coli K12 taxon83333. Native function/subunit annotations distinguish established architecture from specific direct activity evidence. |
| root43-sources-protein-P0ABW0 | https://rest.uniprot.org/uniprotkb/P0ABW0.json; Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/SIMILARITY comments and InterPro/Pfam xref identities; sequence and full bibliography not reanalyzed | supports | Reviewed P0ABW0 matches the maintained hcaC identity and E.coli K12 taxon83333. Native function/subunit annotations distinguish established architecture from specific direct activity evidence. |
| root43-sources-protein-P77650 | https://rest.uniprot.org/uniprotkb/P77650.json; Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/SIMILARITY comments and InterPro/Pfam xref identities; sequence and full bibliography not reanalyzed | supports | Reviewed P77650 matches the maintained hcaD identity and E.coli K12 taxon83333. Native function/subunit annotations distinguish established architecture from specific direct activity evidence. |
| schema-result | just validate data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml |
| strict-result | just validate-strict data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/3_phenylpropionate_dioxygenase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/3_phenylpropionate_dioxygenase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/3_phenylpropionate_dioxygenase_complex-strict.tsv |
| native-3_phenylpropionate_dioxygenase_complex-causal-graphs | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml; Complete focused native report | supports | data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml  (GO:0009334)<br>  hca_dioxygenase_function	hcad_ferredoxin_nad_reductase	COVERED	-&gt;hcad_ferredoxin_nad_reductase (UniProtKB:P77650)<br>  hca_dioxygenase_function	hcac_ferredoxin	COVERED	-&gt;hcac_ferredoxin (UniProtKB:P0ABW0)<br>  hca_dioxygenase_function	hcaf_hydroxylase_beta	COVERED	-&gt;hcaf_hydroxylase_beta (UniProtKB:Q47140)<br>  hca_dioxygenase_function	hcae_hydroxylase_alpha	COVERED	-&gt;hcae_hydroxylase_alpha (UniProtKB:P0ABR5)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     4  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     4  total GENE_OR_PROTEIN causal nodes |
| native-3_phenylpropionate_dioxygenase_complex-verify-network-retry | /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 14 collected target identifiers returned OK. PMID:9603882: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were reviewed after the bulk eutils414 transport failure. Biological support remains bounded by the separately recorded abstract or primary-body sections; identity resolution alone is not confirmation of every attached claim. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, supplements, raw experiments, sequence alignments or quantitative taxon census were reanalyzed. Reading scope is specified for each source.
- Only the specified Diaz1998 sections were read. No isolated Hca complex reconstitution, transient transfer kinetics, metal occupancy or sequence alignment was reanalyzed. The mechanistic graph is a source-based biochemical synthesis.
- Initial focused UniProt verify failed only because sandbox DNS could not resolve the public endpoint. The preserved same-target network retry passed; the failure is not a biological accession mismatch.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T042553Z-3-phenylpropionate-dioxygenase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 3 phenylpropionate dioxygenase complex scientific review
started_at: '2026-10-22T03:58:48Z'
finished_at: '2026-10-22T04:25:53Z'
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
summary: Four exact Hca protein families and reviewed K12 examples, GO identity/activity
  and the coarse classIIB electron-transfer graph are supported, with sequence-based
  assignments distinguished from directly measured whole-cell pathway activity.
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
  - path: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
    sha256: 168a39bc1efe333cd3f4d7217f3bfa978db90e560135e1cfaea564df1ea67f2e
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
- target_id: GO:0009334
  path: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  label: 3-phenylpropionate dioxygenase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 8 of batch43, strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009334
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009334
  command: just validate data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009334
  command: just validate-strict data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
    --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/3_phenylpropionate_dioxygenase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-3_phenylpropionate_dioxygenase_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0009334
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-3_phenylpropionate_dioxygenase_complex-causal-graphs
- check_id: native-3_phenylpropionate_dioxygenase_complex-verify-network-retry
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0009334
  command: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  exit_code: 0
  summary: Focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-3_phenylpropionate_dioxygenase_complex-verify-network-retry
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0009334
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009334
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - root43-sources-go
  - root43-sources-tax83333
  - root43-sources-pmid-9603882
  - root43-sources-doi-4
  - root43-sources-legacy-PMC107259
  - root43-sources-ipr-IPR020875
  - root43-sources-ipr-IPR023712
  - root43-sources-ipr-IPR023739
  - root43-sources-ipr-IPR023744
  - root43-sources-protein-P0ABR5
  - root43-sources-protein-Q47140
  - root43-sources-protein-P0ABW0
  - root43-sources-protein-P77650
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0009334
  summary: '13 of 14 collected target identifiers returned OK. PMID:9603882: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim. Native source checks are separately scoped; skipped or
    unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root43-sources-pmid-9603882
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009334
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
  - GO:0009334
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
  - GO:0009334
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
  - GO:0009334
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
  - GO:0009334
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
  reference: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  locator: Entire maintained target including history, evidence, components, graphs
    and discussions
  accessed_at: '2026-10-22T04:09:21Z'
  support: context_only
  summary: All maintained fields were read; past curation actions are historical provenance,
    not additional experimental evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Exact identity, constituent, formation-necessity and graph contracts
  accessed_at: '2026-10-22T04:09:21Z'
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
- evidence_id: root43-sources-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:03:44.352362Z'
  support: supports
  summary: ENA verifies E.coli K-12 and the K12 alias.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: root43-sources-pmid-9603882
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A9603882+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:47.376644Z'
  support: supports
  summary: Exact MED9603882 identifies Diaz,Ferrandez and Garcia1998 DOI10.1128/JB.180.11.2915-2923.1998
    and its hca cluster characterization.
  snapshot_sha256: 454a1ddfe3478c0b3a564db056ff66fd764818bca1a0cf9431091d7046417c20
- evidence_id: root43-sources-doi-4
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1128%2FJB.180.11.2915-2923.1998&format=json&resultType=core
  locator: Complete native MED bibliographic identity and complete returned abstract
  accessed_at: '2026-10-22T04:03:46.208955Z'
  support: supports
  summary: The DOI query independently returns the same MED9603882 and PMC107259.
    Sequence homology assigns the four dioxygenase proteins; resting-cell pathway
    activity is distinguished from isolated-subunit kinetics.
  snapshot_sha256: 7d6d14f511c9c16fe962e0755ea60539f750fd28bab81d2321c0a35f331bd0fb
- evidence_id: root43-sources-legacy-PMC107259
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC107259/?report=xml
  locator: Complete Methods sec2 and sec7, Results/Discussion sec10 including Table1
    and sec12; other sections/supplements not read
  accessed_at: '2026-10-22T04:04:07.528028Z'
  support: supports
  summary: Diaz1998 directly reports hcaA1 disruption, complementation and resting-cell
    PP-to-DHPP assays, with downstream HcaB distinct from HcaA1/A2/C/D. The four subunit
    roles and classIIB electron-transfer architecture are based on sequence comparison
    and established homologous systems, not direct kinetic reconstitution of each
    transfer step.
  snapshot_sha256: 89e93993c4d1529660e0fbb0a0d73ffe39b630f3c5eeac931a45571a0fab5db1
- evidence_id: root43-sources-ipr-IPR020875
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020875/
  locator: Complete native accession/name/type and curated description
  accessed_at: '2026-10-22T04:03:45.127685Z'
  support: supports
  summary: Native IPR020875 is the exact Hca alpha protein family, not merely its
    constituent domain.
  snapshot_sha256: ffb91c473635ef374c44f21d8c166d81d58bbddb0518617e4b368eb5c91ff63e
- evidence_id: root43-sources-ipr-IPR023712
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023712/
  locator: Complete native accession/name/type and curated description
  accessed_at: '2026-10-22T04:03:45.166027Z'
  support: supports
  summary: Native IPR023712 is the exact Hca beta protein family, not merely its constituent
    domain.
  snapshot_sha256: 553f0f946383db786d264b7bc8ce421c703f6c1909eac54310b54a09f9d3ea0a
- evidence_id: root43-sources-ipr-IPR023739
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023739/
  locator: Complete native accession/name/type and curated description
  accessed_at: '2026-10-22T04:03:45.282816Z'
  support: supports
  summary: Native IPR023739 is the exact Hca ferredoxin protein family, not merely
    its constituent domain.
  snapshot_sha256: 578080bcd60af9d87d08da429fadd44fe6ca3e3f4eb5c03e36d33c6da59d2787
- evidence_id: root43-sources-ipr-IPR023744
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR023744/
  locator: Complete native accession/name/type and curated description
  accessed_at: '2026-10-22T04:03:45.732992Z'
  support: supports
  summary: Native IPR023744 is the exact Hca reductase protein family, not merely
    its constituent domain.
  snapshot_sha256: a5ceb7231afbca265e4ce4b6c27e424c86fb1e5cfd98a18972110295f269c272
- evidence_id: root43-sources-protein-P0ABR5
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ABR5.json
  locator: Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/SIMILARITY
    comments and InterPro/Pfam xref identities; sequence and full bibliography not
    reanalyzed
  accessed_at: '2026-10-22T04:03:44.354586Z'
  support: supports
  summary: Reviewed P0ABR5 matches the maintained hcaE identity and E.coli K12 taxon83333.
    Native function/subunit annotations distinguish established architecture from
    specific direct activity evidence.
  snapshot_sha256: 08176c230f3b4a248de3364416a47222d604fa3ee17abcd31de7a61b8bb06b62
- evidence_id: root43-sources-protein-Q47140
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q47140.json
  locator: Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/SIMILARITY
    comments and InterPro/Pfam xref identities; sequence and full bibliography not
    reanalyzed
  accessed_at: '2026-10-22T04:03:45.019014Z'
  support: supports
  summary: Reviewed Q47140 matches the maintained hcaF identity and E.coli K12 taxon83333.
    Native function/subunit annotations distinguish established architecture from
    specific direct activity evidence.
  snapshot_sha256: 08f095db894d9c06832d7216602d49ec9751f8479467f4a93b9ce5aee42bf51a
- evidence_id: root43-sources-protein-P0ABW0
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P0ABW0.json
  locator: Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/SIMILARITY
    comments and InterPro/Pfam xref identities; sequence and full bibliography not
    reanalyzed
  accessed_at: '2026-10-22T04:03:44.373334Z'
  support: supports
  summary: Reviewed P0ABW0 matches the maintained hcaC identity and E.coli K12 taxon83333.
    Native function/subunit annotations distinguish established architecture from
    specific direct activity evidence.
  snapshot_sha256: 5a0c63f8f56d5fbc19917b7b96d82f83736563385e701c0a391f55e21e1bb875
- evidence_id: root43-sources-protein-P77650
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P77650.json
  locator: Complete accession/status/name/gene/taxon, FUNCTION/SUBUNIT/SIMILARITY
    comments and InterPro/Pfam xref identities; sequence and full bibliography not
    reanalyzed
  accessed_at: '2026-10-22T04:03:44.642137Z'
  support: supports
  summary: Reviewed P77650 matches the maintained hcaD identity and E.coli K12 taxon83333.
    Native function/subunit annotations distinguish established architecture from
    specific direct activity evidence.
  snapshot_sha256: 7781933570445ba5da2b33cdf9f8c58a66120b43916bf9d5d5504b236a2d40e4
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:49Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml'
  snapshot_sha256: fffb74bda89a5f21cecfa219808b3176ff1949bdb8876571b82e32f48e6c0ba4
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
    --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/3_phenylpropionate_dioxygenase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:58:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch43-20261022-u_vlughs/3_phenylpropionate_dioxygenase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch43-20261022-u_vlughs/3_phenylpropionate_dioxygenase_complex-strict.tsv"
  snapshot_sha256: 9c874d41cc1a054623871c74d5698946c215156620c10dc1fa5df25bb4dc4eb3
- evidence_id: native-3_phenylpropionate_dioxygenase_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:04:27.796142Z'
  support: supports
  summary: "data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml  (GO:0009334)\n\
    \  hca_dioxygenase_function\thcad_ferredoxin_nad_reductase\tCOVERED\t->hcad_ferredoxin_nad_reductase\
    \ (UniProtKB:P77650)\n  hca_dioxygenase_function\thcac_ferredoxin\tCOVERED\t->hcac_ferredoxin\
    \ (UniProtKB:P0ABW0)\n  hca_dioxygenase_function\thcaf_hydroxylase_beta\tCOVERED\t\
    ->hcaf_hydroxylase_beta (UniProtKB:Q47140)\n  hca_dioxygenase_function\thcae_hydroxylase_alpha\t\
    COVERED\t->hcae_hydroxylase_alpha (UniProtKB:P0ABR5)\n\ncausal_graphs GENE_OR_PROTEIN\
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
  snapshot_sha256: 643c232d1c030efc53020a6851cb8fbf86dc4243c87cbb2a971fc41c067a79d0
- evidence_id: native-3_phenylpropionate_dioxygenase_complex-verify-network-retry
  kind: validation
  reference: /private/tmp/cellstructure-batch43-20261022-u_vlughs/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:05:02.780338Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '13 of 14 collected target identifiers returned OK. PMID:9603882: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were reviewed after the
    bulk eutils414 transport failure. Biological support remains bounded by the separately
    recorded abstract or primary-body sections; identity resolution alone is not confirmation
    of every attached claim. Native source checks are separately scoped; skipped or
    unreachable identifiers are not silently counted as resolved.'
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
  topic: Four-component oxidoreductase complex
  outcome: supported
  target_ids:
  - GO:0009334
  summary: The exact GO definition, parent and activity match the maintained record,
    with HcaE/HcaF equivalent to historical HcaA1/HcaA2. Downstream HcaB dehydrogenase
    is not confused with the modern hcaF alias.
  evidence_ids:
  - record
  - root43-sources-go
  - root43-sources-legacy-PMC107259
  - root43-sources-protein-P0ABR5
  - root43-sources-protein-Q47140
  - root43-sources-protein-P0ABW0
  - root43-sources-protein-P77650
- assessment_id: composition
  area: grounding
  topic: Four exact family-grounded constituents
  outcome: supported
  target_ids:
  - GO:0009334
  summary: All four InterPro terms are exact families; all four reviewed protein examples
    have correct accession, gene and K12 taxon. The constituent roles agree with the
    primary cluster study and curated authorities.
  evidence_ids:
  - record
  - root43-sources-ipr-IPR020875
  - root43-sources-ipr-IPR023712
  - root43-sources-ipr-IPR023739
  - root43-sources-ipr-IPR023744
  - root43-sources-protein-P0ABR5
  - root43-sources-protein-Q47140
  - root43-sources-protein-P0ABW0
  - root43-sources-protein-P77650
  - root43-sources-tax83333
  - root43-sources-legacy-PMC107259
- assessment_id: necessity
  area: grounding
  topic: Honest formation uncertainty
  outcome: unknown
  target_ids:
  - GO:0009334
  summary: UNKNOWN values avoid converting pathway activity or a knockout growth phenotype
    into evidence that the multicomponent assembly cannot form.
  evidence_ids:
  - record
  - schema
  - root43-sources-legacy-PMC107259
- assessment_id: scope
  area: scope
  topic: E.coli K12 experimental example
  outcome: supported
  target_ids:
  - GO:0009334
  summary: The primary study uses E.coli K12 strains and recombinant Salmonella; the
    maintained K12 example is correct. No universal bacterial distribution is asserted.
  evidence_ids:
  - record
  - root43-sources-tax83333
  - root43-sources-pmid-9603882
  - root43-sources-legacy-PMC107259
- assessment_id: function
  area: evidence
  topic: Dioxygenation distinct from downstream dehydrogenation
  outcome: supported
  target_ids:
  - GO:0009334
  summary: GO0008695 supports the maintained NADH/oxygen/proton reaction and PP-dihydrodiol
    product. The original whole-cell DHPP assay includes downstream HcaB; neither
    it nor a database label proves direct per-step enzyme kinetics. The record states
    pathway architecture rather than a purified reconstitution experiment.
  evidence_ids:
  - record
  - root43-sources-go
  - root43-sources-legacy-PMC107259
  - root43-sources-pmid-9603882
  - root43-sources-doi-4
- assessment_id: graph
  area: graph
  topic: Coarse mechanistic electron-transfer synthesis
  outcome: supported
  target_ids:
  - GO:0009334
  summary: The four edges describe the accepted classIIB reductase-to-ferredoxin-to-oxygenase
    architecture, alpha/beta core association and catalysis. This is a causal biochemical
    model beyond parthood, so MECHANISTIC is appropriate, but the cited1998 sequence-based
    assignments are not independently measured individual electron transfers.
  evidence_ids:
  - record
  - root43-sources-go
  - root43-sources-legacy-PMC107259
  - root43-sources-protein-P0ABR5
  - root43-sources-protein-Q47140
  - root43-sources-protein-P0ABW0
  - root43-sources-protein-P77650
- assessment_id: coverage
  area: completeness
  topic: Complete target and correct reference placement
  outcome: supported
  target_ids:
  - GO:0009334
  summary: All components, protein examples, current graph and history were read.
    No confirmed mismatch in the maintained identity or bounded claims was established.
  evidence_ids:
  - record
  - root43-sources-legacy-PMC107259
  - root43-sources-ipr-IPR020875
  - root43-sources-ipr-IPR023712
  - root43-sources-ipr-IPR023739
  - root43-sources-ipr-IPR023744
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, supplements, raw experiments, sequence alignments or quantitative
  taxon census were reanalyzed. Reading scope is specified for each source.
- Only the specified Diaz1998 sections were read. No isolated Hca complex reconstitution,
  transient transfer kinetics, metal occupancy or sequence alignment was reanalyzed.
  The mechanistic graph is a source-based biochemical synthesis.
- Initial focused UniProt verify failed only because sandbox DNS could not resolve
  the public endpoint. The preserved same-target network retry passed; the failure
  is not a biological accession mismatch.
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
