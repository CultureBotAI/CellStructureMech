# Alkanesulfonate monooxygenase complex scientific review

- Review: 20261022T043539Z-alkanesulfonate-monooxygenase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T04:15:09Z
- Finished UTC: 2026-10-22T04:35:39Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact SsuD tetramer identity, family, K-12 protein reference, enzyme activity and SsuE boundary are supported; no confirmed curation finding within the declared source scope.

## Scope And Provenance

Exactly one entire target reviewed for identity, source support, composition, scope, graph claims and completeness.

Selection: Target 4 of batch44 in strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990201 | data/structures/other/alkanesulfonate_monooxygenase_complex.yaml | maintained | alkanesulfonate monooxygenase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990201 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990201 | Focused validator passed. |
| Focused native causal-graphs | passed | True | GO:1990201 | Focused native check passed; claim-level support assessed separately. |
| Focused native verify | passed | True | GO:1990201 | Focused native check passed; claim-level support assessed separately. |
| Expression-module applicability | not_applicable | False | GO:1990201 | No expression-module claim is maintained. |
| Claim-level scientific review | passed | True | GO:1990201 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:1990201 | 11 of 12 collected target identifiers returned OK. PMID:10480865: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:1990201 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990201 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990201 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990201 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:1990201 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### SsuD tetramer distinguished from two-component system

identity: supported. Targets: GO:1990201.

GO1990201 and its oxidoreductase parent/cytosol parthood exactly match. Separate GO1990200 and GO1990202 support exclusion of the SsuE dimer from the SsuD-only complex.

### Verified SsuD family and homotetramer

grounding: supported. Targets: GO:1990201.

The family includes FMN-dependent alkanesulfonate monooxygenases and the exact E.coli accession. The primary abstract explicitly reports purified native SsuD as a homotetramer, supporting both copy count and physical-property context.

### Formation essentiality remains unknown

grounding: unknown. Targets: GO:1990201.

UNKNOWN does not equate catalytic dependence on FMNH2/O2 with a subunit-deletion formation phenotype.

### Species-level biochemical example

scope: supported. Targets: GO:1990201.

E.coli species and K-12 reference protein are verified. The record does not assert every experimental strain or assay used the reference-protein strain.

### Directly reported oxygenolytic cleavage

evidence: supported. Targets: GO:1990201.

The complete primary abstract reports purified-enzyme conversion of alkanesulfonates to sulfite and aldehydes and dependence on reduced flavin and oxygen. SsuE supplies reduced flavin in the wider system; exclusion as a tetramer constituent does not deny that coupling.

### Coarse biochemical mechanism

graph: supported. Targets: GO:1990201.

The chain describes homotetramer formation and FMNH2-dependent substrate conversion. These concrete assembly and catalytic descriptions are supported at the stated coarse level; no atomic catalytic intermediate or association kinetics is claimed.

### Complete bounded target

completeness: supported. Targets: GO:1990201.

All fields, the subunit-count property, resolved SsuE discussion and later graph addition were checked. No confirmed scientific defect was found within available evidence.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/alkanesulfonate_monooxygenase_complex.yaml; Entire maintained target, history, components, evidence, discussions and graphs | context_only | Every current field and historical note was read; history is provenance rather than independent scientific evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, essentiality and graph scope | context_only | Protein families differ from domains and organism accessions; formation necessity differs from cellular or catalytic essentiality. |
| curation | docs/CURATION.md; Components and REVIEWED_LABEL_ONLY contract, especially lines159–160 | context_only | Reviewed label-only means no exact term exists; an explicitly verified exact family resolves a current gap even when a historical TODO remains. |
| root44-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004402,GO:0005658,GO:0005829,GO:0006269,GO:0008726,GO:0042575,GO:0070461,GO:0140671,GO:1990200,GO:1990201,GO:1990202,GO:1990204; Complete requested id/name/active/definition/synonym fields and typed maintained parent/parthood/activity links | supports | Native GO definitions, synonyms and maintained typed relationships support these exact complex classes. GO0140671 retains the unrelated PMID28966424 xref, which is appropriately excluded from biological support. |
| root44-sources-pmid-10480865 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10480865+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Exact native MED id/title/authors/year/DOI and complete abstract | supports | MED10480865: Characterization of a two-component alkanesulfonate monooxygenase from Escherichia coli. DOI 10.1074/jbc.274.38.26639; complete abstract read. Bibliographic identity and abstract-level findings only; any inspected primary body has its own evidence row. |
| root44-sources-tax562 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562; Complete native taxonomy response | supports | ENA confirms the maintained scientific name, rank, aliases and lineage for 562. |
| root44-sources-tax83333 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333; Complete native taxonomy response | supports | ENA confirms the maintained scientific name, rank, aliases and lineage for 83333. |
| root44-sources-protein-P80645 | https://rest.uniprot.org/uniprotkb/P80645.json; primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY; InterPro/Pfam cross-reference ids | supports | Reviewed accession P80645 has the maintained gene/aliases and taxon. Complete SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization citations do not by themselves establish membership. |
| root44-sources-ipr-IPR019911 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019911/; Complete native accession/name/type/description; not a sequence-alignment reanalysis | supports | IPR019911 is a family named Alkanesulphonate monooxygenase, FMN-dependent. Its complete description was inspected and compared with the component class and protein cross-reference. |
| schema-result | just validate data/structures/other/alkanesulfonate_monooxygenase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/alkanesulfonate_monooxygenase_complex.yaml |
| strict-result | just validate-strict data/structures/other/alkanesulfonate_monooxygenase_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alkanesulfonate_monooxygenase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/alkanesulfonate_monooxygenase_complex.yaml --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alkanesulfonate_monooxygenase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/alkanesulfonate_monooxygenase_complex-strict.tsv |
| native-alkanesulfonate_monooxygenase_complex-causal-graphs | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/alkanesulfonate_monooxygenase_complex.yaml; Complete focused native report | supports | data/structures/other/alkanesulfonate_monooxygenase_complex.yaml  (GO:1990201)<br>  ssud_monooxygenase_function	ssud_alkanesulfonate_monooxygenase	COVERED	-&gt;ssud_alkanesulfonate_monooxygenase (UniProtKB:P80645)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-alkanesulfonate_monooxygenase_complex-verify | /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python -B scripts/uniprot_genes.py --verify --record data/structures/other/alkanesulfonate_monooxygenase_complex.yaml; Complete focused native report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/alkanesulfonate_monooxygenase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 11 of 12 collected target identifiers returned OK. PMID:10480865: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- No figure pixels, raw experiments, supplemental datasets or sequence alignments were reanalyzed. Exact body reading scope is stated in each evidence row.
- Eichhorn1999 was read as its complete native abstract, corroborated by native GO/UniProt; the publisher route failed. Full purification protocols, gel-based mass calculations and detailed kinetics were not independently inspected.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes reviews for all uncovered records, including honest zero-finding bundles.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T043539Z-alkanesulfonate-monooxygenase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Alkanesulfonate monooxygenase complex scientific review
started_at: '2026-10-22T04:15:09Z'
finished_at: '2026-10-22T04:35:39Z'
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
summary: Exact SsuD tetramer identity, family, K-12 protein reference, enzyme activity
  and SsuE boundary are supported; no confirmed curation finding within the declared
  source scope.
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
  - path: data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
    sha256: ac8fbeb8ff0cc8842c6a4dc579722d2860064fff15bb3011c0b726caa440a7ba
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
- target_id: GO:1990201
  path: data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
  label: alkanesulfonate monooxygenase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, source support, composition,
    scope, graph claims and completeness.
  selection: Target 4 of batch44 in strict uncovered path order at fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990201
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990201
  command: just validate data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990201
  command: just validate-strict data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
    --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alkanesulfonate_monooxygenase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-alkanesulfonate_monooxygenase_complex-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:1990201
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-alkanesulfonate_monooxygenase_complex-causal-graphs
- check_id: native-alkanesulfonate_monooxygenase_complex-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:1990201
  command: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
  exit_code: 0
  summary: Focused native check passed; claim-level support assessed separately.
  evidence_ids:
  - native-alkanesulfonate_monooxygenase_complex-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990201
  summary: No expression-module claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990201
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - root44-sources-go
  - root44-sources-pmid-10480865
  - root44-sources-tax562
  - root44-sources-tax83333
  - root44-sources-protein-P80645
  - root44-sources-ipr-IPR019911
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:1990201
  summary: '11 of 12 collected target identifiers returned OK. PMID:10480865: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root44-sources-pmid-10480865
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990201
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
  - GO:1990201
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
  - GO:1990201
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
  - GO:1990201
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
  - GO:1990201
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
  reference: data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
  locator: Entire maintained target, history, components, evidence, discussions and
    graphs
  accessed_at: '2026-10-22T04:20:11Z'
  support: context_only
  summary: Every current field and historical note was read; history is provenance
    rather than independent scientific evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, essentiality and graph scope
  accessed_at: '2026-10-22T04:20:11Z'
  support: context_only
  summary: Protein families differ from domains and organism accessions; formation
    necessity differs from cellular or catalytic essentiality.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Components and REVIEWED_LABEL_ONLY contract, especially lines159–160
  accessed_at: '2026-10-22T04:20:11Z'
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
- evidence_id: root44-sources-pmid-10480865
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A10480865+AND+SRC%3AMED&format=json&resultType=core
  locator: Exact native MED id/title/authors/year/DOI and complete abstract
  accessed_at: '2026-10-22T04:15:39.857056Z'
  support: supports
  summary: 'MED10480865: Characterization of a two-component alkanesulfonate monooxygenase
    from Escherichia coli. DOI 10.1074/jbc.274.38.26639; complete abstract read. Bibliographic
    identity and abstract-level findings only; any inspected primary body has its
    own evidence row.'
  snapshot_sha256: 36fbdb88da80354ffdf2c994887a6e383aa8da288fff17fa78b519297f7271de
- evidence_id: root44-sources-tax562
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/562
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:15:35.970412Z'
  support: supports
  summary: ENA confirms the maintained scientific name, rank, aliases and lineage
    for 562.
  snapshot_sha256: ea038c30da3aab3426b7df16ce7a137cf2985e73d6ad8281971b9c390a74d2a8
- evidence_id: root44-sources-tax83333
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/83333
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T04:15:36.706690Z'
  support: supports
  summary: ENA confirms the maintained scientific name, rank, aliases and lineage
    for 83333.
  snapshot_sha256: f499fde9e4fcea85ff811b58a76a405669d32465a62eaf74240a48331b63d8e6
- evidence_id: root44-sources-protein-P80645
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/P80645.json
  locator: primaryAccession/entryType/proteinDescription/genes/organism; full SUBUNIT/LOCATION/SIMILARITY;
    InterPro/Pfam cross-reference ids
  accessed_at: '2026-10-22T04:15:38.214400Z'
  support: supports
  summary: Reviewed accession P80645 has the maintained gene/aliases and taxon. Complete
    SUBUNIT and SUBCELLULAR LOCATION comments and evidence joins were inspected; localization
    citations do not by themselves establish membership.
  snapshot_sha256: 224991876d6c709f6a74fb44cd17e16977ebd36378ce55b0112ddfcd00a08f14
- evidence_id: root44-sources-ipr-IPR019911
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019911/
  locator: Complete native accession/name/type/description; not a sequence-alignment
    reanalysis
  accessed_at: '2026-10-22T04:15:39.260410Z'
  support: supports
  summary: IPR019911 is a family named Alkanesulphonate monooxygenase, FMN-dependent.
    Its complete description was inspected and compared with the component class and
    protein cross-reference.
  snapshot_sha256: 431ce6577c61ce626c2a0e2067e92cfa22fa8628cd7b1fedb3c07c0fb9e27578
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:10Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/alkanesulfonate_monooxygenase_complex.yaml'
  snapshot_sha256: b5514372510f91b287a4a72ac6a186f73c1234e1cb3bbc83350a335ca6e4503a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
    --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alkanesulfonate_monooxygenase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T04:15:11Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/alkanesulfonate_monooxygenase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch44-20261022-b975f18l/alkanesulfonate_monooxygenase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch44-20261022-b975f18l/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch44-20261022-b975f18l/alkanesulfonate_monooxygenase_complex-strict.tsv"
  snapshot_sha256: 1ca3d7edc2aeda72a6c5acf757024ad7acee2a8976efc45b69e09824409f5516
- evidence_id: native-alkanesulfonate_monooxygenase_complex-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:15:53.149949Z'
  support: supports
  summary: "data/structures/other/alkanesulfonate_monooxygenase_complex.yaml  (GO:1990201)\n\
    \  ssud_monooxygenase_function\tssud_alkanesulfonate_monooxygenase\tCOVERED\t\
    ->ssud_alkanesulfonate_monooxygenase (UniProtKB:P80645)\n\ncausal_graphs GENE_OR_PROTEIN\
    \ node summary:\n     1  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  UNANCHORED_NO_UNIPROT     no component_ref and no\
    \ UniProtKB grounding or xref on the node\n     1  total GENE_OR_PROTEIN causal\
    \ nodes"
  snapshot_sha256: df8199357e4dbee46f9b4d59809a3f10362f612f5e0d87aef5e73070e4bbea21
- evidence_id: native-alkanesulfonate_monooxygenase_complex-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch44-20261022-b975f18l/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --verify --record data/structures/other/alkanesulfonate_monooxygenase_complex.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T04:15:54.488119Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/alkanesulfonate_monooxygenase_complex.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '11 of 12 collected target identifiers returned OK. PMID:10480865: UNREACHABLE;
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
  topic: SsuD tetramer distinguished from two-component system
  outcome: supported
  target_ids:
  - GO:1990201
  summary: GO1990201 and its oxidoreductase parent/cytosol parthood exactly match.
    Separate GO1990200 and GO1990202 support exclusion of the SsuE dimer from the
    SsuD-only complex.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-pmid-10480865
- assessment_id: composition
  area: grounding
  topic: Verified SsuD family and homotetramer
  outcome: supported
  target_ids:
  - GO:1990201
  summary: The family includes FMN-dependent alkanesulfonate monooxygenases and the
    exact E.coli accession. The primary abstract explicitly reports purified native
    SsuD as a homotetramer, supporting both copy count and physical-property context.
  evidence_ids:
  - record
  - root44-sources-ipr-IPR019911
  - root44-sources-pmid-10480865
  - root44-sources-protein-P80645
- assessment_id: necessity
  area: grounding
  topic: Formation essentiality remains unknown
  outcome: unknown
  target_ids:
  - GO:1990201
  summary: UNKNOWN does not equate catalytic dependence on FMNH2/O2 with a subunit-deletion
    formation phenotype.
  evidence_ids:
  - record
  - schema
  - root44-sources-pmid-10480865
- assessment_id: scope
  area: scope
  topic: Species-level biochemical example
  outcome: supported
  target_ids:
  - GO:1990201
  summary: E.coli species and K-12 reference protein are verified. The record does
    not assert every experimental strain or assay used the reference-protein strain.
  evidence_ids:
  - record
  - root44-sources-pmid-10480865
  - root44-sources-tax562
  - root44-sources-tax83333
  - root44-sources-protein-P80645
- assessment_id: function
  area: evidence
  topic: Directly reported oxygenolytic cleavage
  outcome: supported
  target_ids:
  - GO:1990201
  summary: The complete primary abstract reports purified-enzyme conversion of alkanesulfonates
    to sulfite and aldehydes and dependence on reduced flavin and oxygen. SsuE supplies
    reduced flavin in the wider system; exclusion as a tetramer constituent does not
    deny that coupling.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-pmid-10480865
- assessment_id: graph
  area: graph
  topic: Coarse biochemical mechanism
  outcome: supported
  target_ids:
  - GO:1990201
  summary: The chain describes homotetramer formation and FMNH2-dependent substrate
    conversion. These concrete assembly and catalytic descriptions are supported at
    the stated coarse level; no atomic catalytic intermediate or association kinetics
    is claimed.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-pmid-10480865
- assessment_id: coverage
  area: completeness
  topic: Complete bounded target
  outcome: supported
  target_ids:
  - GO:1990201
  summary: All fields, the subunit-count property, resolved SsuE discussion and later
    graph addition were checked. No confirmed scientific defect was found within available
    evidence.
  evidence_ids:
  - record
  - root44-sources-go
  - root44-sources-ipr-IPR019911
  - root44-sources-pmid-10480865
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- No figure pixels, raw experiments, supplemental datasets or sequence alignments
  were reanalyzed. Exact body reading scope is stated in each evidence row.
- Eichhorn1999 was read as its complete native abstract, corroborated by native GO/UniProt;
  the publisher route failed. Full purification protocols, gel-based mass calculations
  and detailed kinetics were not independently inspected.
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
