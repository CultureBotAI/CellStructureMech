# Er to golgi transport vesicle membrane identity, evidence and boundary review

- Review: 20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:18:35Z
- Finished UTC: 2026-10-22T01:37:17Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed in the er to golgi transport vesicle membrane record within the explicitly bounded evidence scope.

## Scope And Provenance

Entire single target: identity, hierarchy, component/protein scope, organisms, cited source claims and every graph edge.

Selection: Target 4 of batch twenty-eight, strict uncovered path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0012507 | data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml | maintained | ER to Golgi transport vesicle membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0012507 | Native focused check passed; biological membership is assessed from sources separately. |
| Native protein causal-graphs | passed | True | GO:0012507 | Native focused check passed; biological membership is assessed from sources separately. |
| Focused native schema | passed | True | GO:0012507 | Focused validator passed. |
| Focused native strict | passed | True | GO:0012507 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0012507 | No expression-module dataset or inference is used; protein identity and the cited physical/localization experiments provide the relevant evidence. |
| Claim-level scientific review | passed | True | GO:0012507 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0012507 | 8 of 10 collected target identifiers returned OK. PMID:8004676: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID8004676, DOI10.1016/0092-8674(94)90138-4 and COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections.; PMID:9568718: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID9568718, DOI10.1016/s0092-8674(00)81577-9 and COPII-coated vesicle formation reconstituted with purified coat proteins and chemically defined liposomes. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0012507 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0012507 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0012507 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0012507 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0012507 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Membrane, coat and whole carrier

identity: supported. Targets: GO:0012507.

Exact GO0012507 definition and exact COPII coated vesicle membrane synonym agree. Both declared is-a parents and whole-vesicle parthood are explicit in native returned child relations. GO0030127 is a distinct coat complex; the graph and discussions keep the lipid boundary separate from coat subunits.

### Budding-yeast COPII examples

scope: supported. Targets: GO:0012507.

Species4932 is exact. Native GO coat identity and Barlowe/Matsuoka primary abstracts support the named Sar1/Sec23-Sec24/Sec13-Sec31 machinery and ER donor context in the stated yeast system. COMMON is qualitative, with no unsupported strain or prevalence extrapolation.

### Collective membrane material

grounding: supported. Targets: GO:0012507.

The REVIEWED_LABEL_ONLY LIPID component and open grounding TODO accurately represent material without substituting the whole membrane class for one chemical species. Protein coat subunits are not miscast as lipid constituents. There are no protein instances to taxon-pair here.

### All three transport-vesicle membrane edges

graph: supported. Targets: GO:0012507.

Parthood and bounds edges follow the exact GO membrane/whole-carrier definitions. ER donation is directly supported by GO0090114 and Barlowe ER-derived budding; Matsuoka provides reconstitution context. Defined-liposome budding is not by itself proof of a complete in-vivo lipid inventory. NONMECHANISTIC scope is appropriate. No optional duplicate function is required solely to repeat topology.

### Constitution versus individual molecular necessity

evidence: unknown. Targets: GO:0012507.

The defining collective bilayer supports the essential boundary material; neither reconstitution nor coat requirements establish necessity of every possible native lipid species for structure formation.

### Full maintained target and honest scope

completeness: supported. Targets: GO:0012507.

Entire target and every graph edge were read. There are no target image assets, measurements, trait links or verbatim evidence snippets to verify. Optional molecular inventories and family groundings remain acknowledged; no finding is invented from an empty optional slot. PROPOSED status and historical events are retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml; Entire maintained target including history, evidence, components, every graph node and edge, discussions | context_only | Full target was read; no scientific record, status, history or generated page is changed. |
| policy | docs/CURATION.md; Identity, hierarchy, parthood, component and evidence rules | context_only | Whole structure, boundary material and enclosed region are distinguished. Associated machinery is not automatically a constituent, and functional necessity is distinct from structure formation. |
| protein-contract | src/cellstructuremech/schema/cellstructuremech.yaml; Component essentiality and protein_examples; ProteinExample lines440–468 | context_only | A protein example is a taxon-paired instance whose structure role must have source support. Accession identity alone is insufficient. Collective bilayer constitution does not prove individual lipid-species necessity. |
| root28-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031904,GO:0070013,GO:0005768,GO:0010008,GO:0005771,GO:0071985,GO:0016020,GO:0000813,GO:0000815,GO:0012507,GO:0030658,GO:0030662,GO:0030134,GO:0005789,GO:0090114,GO:0030127,GO:1990413; Complete17-term JSON: identifiers, active flags, names, definitions, synonyms and returned child relations | supports | All17 returned active GO terms were directly read. Exact endosome lumen/membrane, transport-vesicle membrane and eyespot definitions and declared synonyms agree. GO0070013 explicitly lists endosome lumen as an is-a child; GO0005768 lists lumen/membrane as parts. GO0030658/0030662 list GO0012507 as is-a child, while GO0030134 lists it as part. Exact MVB and ESCRT definitions support the limited process context. Broad membrane hierarchy is definition-based where no direct child was returned. |
| root28-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternate names | supports | Native ENA exact species identity and lineage agree with Saccharomyces cerevisiae4932. This is taxonomic identity, not a measured population prevalence or an experimental strain assignment. |
| root28-sources-barlowe1994-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A8004676%20AND%20SRC%3AMED; Single-result bibliography and complete abstract; full-body inspection scope separately specified | supports | Native MED matches COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum., Barlowe C, Orci L, Yeung T, Hosobuchi M, Hamamoto S, Salama N, Rexach MF, Ravazzola M, Amherdt M, Schekman R., PMID8004676, DOI10.1016/0092-8674(94)90138-4. Complete primary abstract describes ER-derived vesicles formed from washed membranes with Sar1 and Sec13/Sec23 complexes, distinct COPII coat and nucleotide-dependent targeting/fusion. It directly supports ER donor membrane context. |
| root28-sources-matsuoka1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A9568718%20AND%20SRC%3AMED; Single-result bibliography and complete abstract; full-body inspection scope separately specified | supports | Native MED matches COPII-coated vesicle formation reconstituted with purified coat proteins and chemically defined liposomes., Matsuoka K, Orci L, Amherdt M, Bednarek SY, Hamamoto S, Schekman R, Yeung T., PMID9568718, DOI10.1016/s0092-8674(00)81577-9. Complete primary abstract describes sequential purified COPII assembly on ER membranes and defined liposomes, phosphoinositide-dependent binding, coated buds and vesicles without rupture. Reconstitution is not a complete native lipid inventory. |
| neighbor-copii-vesicle | data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml; Lines1–65, identifier/definition/history/synonyms | context_only | Whole COPII-coated vesicle identity is distinct from its membrane. |
| neighbor-copii-coat | data/structures/other/copii_vesicle_coat.yaml; Lines1–78, identifier/definition/hierarchy and initial Sar1 context | context_only | The named coat is a separate protein complex. No full audit of its protein examples or assembly graph is implied. |
| native-verify | /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml --verify; Entire native focused output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml --causal-graphs; Entire native focused output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/er_to_golgi_transport_vesicle_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/er_to_golgi_transport_vesicle_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/er_to_golgi_transport_vesicle_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 10 collected target identifiers returned OK. PMID:8004676: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID8004676, DOI10.1016/0092-8674(94)90138-4 and COPII: a membrane coat formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections.; PMID:9568718: UNREACHABLE; The bulk PMID transport returned414; the independently retrieved exact MED record verifies PMID9568718, DOI10.1016/s0092-8674(00)81577-9 and COPII-coated vesicle formation reconstituted with purified coat proteins and chemically defined liposomes. Bibliographic identity is resolved; scientific scope remains restricted to the separately documented abstract/body inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Source identity is not proof of experimental membership. Taxonomic labels do not silently assign study strains, and qualitative COMMON does not encode a prevalence survey. Historical authorship, prior searches and previous dispositions are not independently recertified.
- Barlowe1994 and Matsuoka1998 were read as complete primary abstracts only; full publisher bodies were not recovered in the earlier attempt. No figure or complete in-vivo lipid-composition audit is claimed. Reused source bytes retain original URL/access time/hash.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes review bundles for every uncovered record, including honest no-finding reviews. Scientific records are not edited.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T013717Z-er-to-golgi-transport-vesicle-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Er to golgi transport vesicle membrane identity, evidence and boundary review
started_at: '2026-10-22T01:18:35Z'
finished_at: '2026-10-22T01:37:17Z'
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
summary: No concrete curation defect observed in the er to golgi transport vesicle
  membrane record within the explicitly bounded evidence scope.
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
  - path: data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
    sha256: 141713f26c4f5cc6a2e6c6cb232bf45e194df53bcd60aa4769cc4343ac6599bf
    role: context
  - path: data/structures/membrane_organelle/endoplasmic_reticulum_membrane.yaml
    sha256: 599774aca4e215829787fe1a818ef52bd2c3772b48c289505d14417c05d0f679
    role: context
  - path: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    sha256: 5cdd951707eead318295ce7ceb64c16bdc0c85b465374678d564878481f04a9c
    role: target
  - path: data/structures/other/copii_vesicle_coat.yaml
    sha256: 3b7c89b408581ddfd7f40203a1810eda738e87b1d2457812209b8586abbb0ef2
    role: context
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0012507
  path: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  label: ER to Golgi transport vesicle membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target: identity, hierarchy, component/protein scope,
    organisms, cited source claims and every graph edge.'
  selection: Target 4 of batch twenty-eight, strict uncovered path order at fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0012507
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; biological membership is assessed from sources
    separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; biological membership is assessed from sources
    separately.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: just validate data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: just validate-strict data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/er_to_golgi_transport_vesicle_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0012507
  summary: No expression-module dataset or inference is used; protein identity and
    the cited physical/localization experiments provide the relevant evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0012507
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - protein-contract
  - root28-sources-go
  - root28-sources-tax4932
  - root28-sources-barlowe1994-meta
  - root28-sources-matsuoka1998-meta
  - neighbor-copii-vesicle
  - neighbor-copii-coat
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0012507
  summary: '8 of 10 collected target identifiers returned OK. PMID:8004676: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID8004676, DOI10.1016/0092-8674(94)90138-4 and COPII: a membrane coat
    formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum.
    Bibliographic identity is resolved; scientific scope remains restricted to the
    separately documented abstract/body inspections.; PMID:9568718: UNREACHABLE; The
    bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID9568718, DOI10.1016/s0092-8674(00)81577-9 and COPII-coated vesicle
    formation reconstituted with purified coat proteins and chemically defined liposomes.
    Bibliographic identity is resolved; scientific scope remains restricted to the
    separately documented abstract/body inspections. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root28-sources-barlowe1994-meta
  - root28-sources-matsuoka1998-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0012507
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0012507
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
    and current batch28 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  locator: Entire maintained target including history, evidence, components, every
    graph node and edge, discussions
  accessed_at: '2026-10-22T01:25:03Z'
  support: context_only
  summary: Full target was read; no scientific record, status, history or generated
    page is changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Identity, hierarchy, parthood, component and evidence rules
  accessed_at: '2026-10-22T01:25:03Z'
  support: context_only
  summary: Whole structure, boundary material and enclosed region are distinguished.
    Associated machinery is not automatically a constituent, and functional necessity
    is distinct from structure formation.
- evidence_id: protein-contract
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component essentiality and protein_examples; ProteinExample lines440–468
  accessed_at: '2026-10-22T01:25:03Z'
  support: context_only
  summary: A protein example is a taxon-paired instance whose structure role must
    have source support. Accession identity alone is insufficient. Collective bilayer
    constitution does not prove individual lipid-species necessity.
- evidence_id: root28-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031904,GO:0070013,GO:0005768,GO:0010008,GO:0005771,GO:0071985,GO:0016020,GO:0000813,GO:0000815,GO:0012507,GO:0030658,GO:0030662,GO:0030134,GO:0005789,GO:0090114,GO:0030127,GO:1990413
  locator: 'Complete17-term JSON: identifiers, active flags, names, definitions, synonyms
    and returned child relations'
  accessed_at: '2026-10-22T01:21:55.127008Z'
  support: supports
  summary: All17 returned active GO terms were directly read. Exact endosome lumen/membrane,
    transport-vesicle membrane and eyespot definitions and declared synonyms agree.
    GO0070013 explicitly lists endosome lumen as an is-a child; GO0005768 lists lumen/membrane
    as parts. GO0030658/0030662 list GO0012507 as is-a child, while GO0030134 lists
    it as part. Exact MVB and ESCRT definitions support the limited process context.
    Broad membrane hierarchy is definition-based where no direct child was returned.
  snapshot_sha256: 196c0eb6263923cb4c06c3050858f88ab320a65b4a9504075dfc5796e203a956
- evidence_id: root28-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: Native ENA exact species identity and lineage agree with Saccharomyces
    cerevisiae4932. This is taxonomic identity, not a measured population prevalence
    or an experimental strain assignment.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root28-sources-barlowe1994-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A8004676%20AND%20SRC%3AMED
  locator: Single-result bibliography and complete abstract; full-body inspection
    scope separately specified
  accessed_at: '2026-10-22T01:10:57.099755Z'
  support: supports
  summary: 'Native MED matches COPII: a membrane coat formed by Sec proteins that
    drive vesicle budding from the endoplasmic reticulum., Barlowe C, Orci L, Yeung
    T, Hosobuchi M, Hamamoto S, Salama N, Rexach MF, Ravazzola M, Amherdt M, Schekman
    R., PMID8004676, DOI10.1016/0092-8674(94)90138-4. Complete primary abstract describes
    ER-derived vesicles formed from washed membranes with Sar1 and Sec13/Sec23 complexes,
    distinct COPII coat and nucleotide-dependent targeting/fusion. It directly supports
    ER donor membrane context.'
  snapshot_sha256: f3ff438cc130518602efe6aa0252c6d5634fafad949d62cf23e3a6e837819fc7
- evidence_id: root28-sources-matsuoka1998-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A9568718%20AND%20SRC%3AMED
  locator: Single-result bibliography and complete abstract; full-body inspection
    scope separately specified
  accessed_at: '2026-10-22T01:10:57.832309Z'
  support: supports
  summary: Native MED matches COPII-coated vesicle formation reconstituted with purified
    coat proteins and chemically defined liposomes., Matsuoka K, Orci L, Amherdt M,
    Bednarek SY, Hamamoto S, Schekman R, Yeung T., PMID9568718, DOI10.1016/s0092-8674(00)81577-9.
    Complete primary abstract describes sequential purified COPII assembly on ER membranes
    and defined liposomes, phosphoinositide-dependent binding, coated buds and vesicles
    without rupture. Reconstitution is not a complete native lipid inventory.
  snapshot_sha256: 0cdaf91dc4f4bf9261f55530522a8ed41116b930c39ac656de0d729c318bf1c0
- evidence_id: neighbor-copii-vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/copii_coated_er_to_golgi_transport_vesicle.yaml
  locator: Lines1–65, identifier/definition/history/synonyms
  accessed_at: '2026-10-22T01:25:03Z'
  support: context_only
  summary: Whole COPII-coated vesicle identity is distinct from its membrane.
- evidence_id: neighbor-copii-coat
  kind: record_content
  reference: data/structures/other/copii_vesicle_coat.yaml
  locator: Lines1–78, identifier/definition/hierarchy and initial Sar1 context
  accessed_at: '2026-10-22T01:25:03Z'
  support: context_only
  summary: The named coat is a separate protein complex. No full audit of its protein
    examples or assembly graph is implied.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    --verify
  locator: Entire native focused output
  accessed_at: '2026-10-22T01:22:09.912687Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    --causal-graphs
  locator: Entire native focused output
  accessed_at: '2026-10-22T01:22:11.935644Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:18:36Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml'
  snapshot_sha256: 6a97dc2b0f1397819028631bb9b26cc08ca589e81d30401deaa895a48c4e23b6
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml
    --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/er_to_golgi_transport_vesicle_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:18:38Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/er_to_golgi_transport_vesicle_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch28-20261022-rd3g_t6z/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch28-20261022-rd3g_t6z/er_to_golgi_transport_vesicle_membrane-strict.tsv"
  snapshot_sha256: 71bc3d9481899c2dfcc88e4951c5877751f166804143d52b0926aaf10f95aeb3
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/er_to_golgi_transport_vesicle_membrane.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 10 collected target identifiers returned OK. PMID:8004676: UNREACHABLE;
    The bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID8004676, DOI10.1016/0092-8674(94)90138-4 and COPII: a membrane coat
    formed by Sec proteins that drive vesicle budding from the endoplasmic reticulum.
    Bibliographic identity is resolved; scientific scope remains restricted to the
    separately documented abstract/body inspections.; PMID:9568718: UNREACHABLE; The
    bulk PMID transport returned414; the independently retrieved exact MED record
    verifies PMID9568718, DOI10.1016/s0092-8674(00)81577-9 and COPII-coated vesicle
    formation reconstituted with purified coat proteins and chemically defined liposomes.
    Bibliographic identity is resolved; scientific scope remains restricted to the
    separately documented abstract/body inspections. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
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
  topic: Membrane, coat and whole carrier
  outcome: supported
  target_ids:
  - GO:0012507
  summary: Exact GO0012507 definition and exact COPII coated vesicle membrane synonym
    agree. Both declared is-a parents and whole-vesicle parthood are explicit in native
    returned child relations. GO0030127 is a distinct coat complex; the graph and
    discussions keep the lipid boundary separate from coat subunits.
  evidence_ids:
  - record
  - root28-sources-go
  - policy
  - neighbor-copii-vesicle
  - neighbor-copii-coat
- assessment_id: scope
  area: scope
  topic: Budding-yeast COPII examples
  outcome: supported
  target_ids:
  - GO:0012507
  summary: Species4932 is exact. Native GO coat identity and Barlowe/Matsuoka primary
    abstracts support the named Sar1/Sec23-Sec24/Sec13-Sec31 machinery and ER donor
    context in the stated yeast system. COMMON is qualitative, with no unsupported
    strain or prevalence extrapolation.
  evidence_ids:
  - record
  - root28-sources-tax4932
  - root28-sources-go
  - root28-sources-barlowe1994-meta
  - root28-sources-matsuoka1998-meta
- assessment_id: composition
  area: grounding
  topic: Collective membrane material
  outcome: supported
  target_ids:
  - GO:0012507
  summary: The REVIEWED_LABEL_ONLY LIPID component and open grounding TODO accurately
    represent material without substituting the whole membrane class for one chemical
    species. Protein coat subunits are not miscast as lipid constituents. There are
    no protein instances to taxon-pair here.
  evidence_ids:
  - record
  - root28-sources-go
  - protein-contract
- assessment_id: graph
  area: graph
  topic: All three transport-vesicle membrane edges
  outcome: supported
  target_ids:
  - GO:0012507
  summary: Parthood and bounds edges follow the exact GO membrane/whole-carrier definitions.
    ER donation is directly supported by GO0090114 and Barlowe ER-derived budding;
    Matsuoka provides reconstitution context. Defined-liposome budding is not by itself
    proof of a complete in-vivo lipid inventory. NONMECHANISTIC scope is appropriate.
    No optional duplicate function is required solely to repeat topology.
  evidence_ids:
  - record
  - root28-sources-go
  - root28-sources-barlowe1994-meta
  - root28-sources-matsuoka1998-meta
- assessment_id: necessity
  area: evidence
  topic: Constitution versus individual molecular necessity
  outcome: unknown
  target_ids:
  - GO:0012507
  summary: The defining collective bilayer supports the essential boundary material;
    neither reconstitution nor coat requirements establish necessity of every possible
    native lipid species for structure formation.
  evidence_ids:
  - record
  - root28-sources-go
  - protein-contract
  - root28-sources-barlowe1994-meta
  - root28-sources-matsuoka1998-meta
- assessment_id: coverage
  area: completeness
  topic: Full maintained target and honest scope
  outcome: supported
  target_ids:
  - GO:0012507
  summary: Entire target and every graph edge were read. There are no target image
    assets, measurements, trait links or verbatim evidence snippets to verify. Optional
    molecular inventories and family groundings remain acknowledged; no finding is
    invented from an empty optional slot. PROPOSED status and historical events are
    retained.
  evidence_ids:
  - record
  - policy
  - root28-sources-go
  - root28-sources-barlowe1994-meta
  - root28-sources-matsuoka1998-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Source identity is not proof of experimental membership. Taxonomic labels do not
  silently assign study strains, and qualitative COMMON does not encode a prevalence
  survey. Historical authorship, prior searches and previous dispositions are not
  independently recertified.
- Barlowe1994 and Matsuoka1998 were read as complete primary abstracts only; full
  publisher bodies were not recovered in the earlier attempt. No figure or complete
  in-vivo lipid-composition audit is claimed. Reused source bytes retain original
  URL/access time/hash.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes review bundles for every uncovered record, including
  honest no-finding reviews. Scientific records are not edited.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
