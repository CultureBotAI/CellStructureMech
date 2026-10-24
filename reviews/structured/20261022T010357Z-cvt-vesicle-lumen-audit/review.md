# Cvt structure identity, membrane boundaries and source review

- Review: 20261022T010357Z-cvt-vesicle-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:20:48Z
- Finished UTC: 2026-10-22T01:03:57Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The Cvt lumen identity and descriptive topology are supported at the declared source scopes. No concrete curation finding was established.

## Scope And Provenance

Entire single maintained target, exact authority identities, species/source contexts, all component/formation boundaries and every graph edge.

Selection: Target 2 in batch twenty-five, selected by native uncovered path order at frozen revision9c0446.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:cvt_vesicle_lumen | data/structures/membrane_organelle/cvt_vesicle_lumen.yaml | maintained | Cvt vesicle lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:cvt_vesicle_lumen | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:cvt_vesicle_lumen | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:cvt_vesicle_lumen | 6 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Focused native verify | passed | True | cellstructuremech:cvt_vesicle_lumen | Native check passed. The target has no explicit protein accessions or GENE_OR_PROTEIN graph nodes; this does not independently prove biological membership. |
| Focused native causal-graphs | passed | True | cellstructuremech:cvt_vesicle_lumen | Native check passed. The target has no explicit protein accessions or GENE_OR_PROTEIN graph nodes; this does not independently prove biological membership. |
| Expression-module applicability | not_applicable | False | cellstructuremech:cvt_vesicle_lumen | No expression-module, regulator-network or transcriptomic inference is made by this structural review. |
| Claim-level scientific review | passed | True | cellstructuremech:cvt_vesicle_lumen | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:cvt_vesicle_lumen | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:cvt_vesicle_lumen | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:cvt_vesicle_lumen | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:cvt_vesicle_lumen | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:cvt_vesicle_lumen | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Carrier, lumen and individual surrounding bilayer remain distinct

identity: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

The target identifies the stated structure or enclosed region rather than the Cvt cargo protein complex, an individual Atg protein or the pathway itself. Native GO and UniProt definitions support the asserted hierarchy and parthood. Either-bilayer language preserves the double-membrane carrier; it does not collapse both membranes into one bilayer. The mature cargo-containing interior is distinguished from the inner vesicle released after fusion and from the intermembrane space.

### Budding-yeast model and conditional experimental context

scope: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

The species identity and canonical budding-yeast context are supported by Reggiori strains and experiments. COMMON is a qualitative occurrence statement, not a measured prevalence or an assertion that every cell contains a visible carrier. The source distinguishes nutrient-rich Cvt transport from starvation-induced autophagy; its temperature-sensitive mutant results are not generalized to all physiological conditions. Membrane/lumen occurrence follows from the described membrane-bounded carrier and exact location definitions.

### Positive exact source and local identifier

grounding: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

SL0323 directly supports the local lumen definition, hierarchy and containing-vesicle relation. The ignored-inclusive corpus search confirms the identifier is unique. A bounded GO candidate search is recorded without claiming that no exact GO class exists. The lumen is an enclosed region, not an individual cargo or the Cvt pathway.

### Two descriptive boundary relations

graph: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

Both NONMECHANISTIC edges follow the native location definition: lumen part_of the whole Cvt carrier and surrounding membrane bounds the lumen. The mature cargo-containing compartment remains distinct from the space between the two membranes and from the post-fusion inner Cvt body. The record does not assert a soluble-cargo inventory, fusion mechanism or independent biological-process function.

### All maintained fields and bounded source scopes

completeness: supported. Targets: cellstructuremech:cvt_vesicle_lumen.

The complete target, every graph edge and discussion were read. No quantitative property, image licence, trait link, verbatim snippet or individual protein accession is asserted in this target. Empty optional inventories or mechanics do not by themselves establish defects. PROPOSED status and inherited history are preserved; historical search completeness and independent authorship are not recertified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/cvt_vesicle_lumen.yaml; Entire maintained YAML, including every definition, evidence note, component, history, graph edge and discussion | context_only | The entire maintained record was read. No scientific content, curation history or status was changed. Retained input bytes were rechecked on resumed work. |
| policy | docs/CURATION.md; Exact identity, constituent/associated-machinery boundary, molecular grounding and structure-formation necessity | context_only | A whole vesicle, surrounding membrane, enclosed compartment, cargo complex and assembly machinery are distinct. Essentiality concerns whether the structure forms, not cell viability or catalytic activity. |
| neighbor-cvt_vesicle | data/structures/membrane_organelle/cvt_vesicle.yaml; Entire neighboring maintained YAML read; used only for identity and component/part boundary context | context_only | The neighboring carrier, membrane, lumen and cargo-complex records are distinct maintained owners. Their additional protein examples, evidence and historical decisions are not separately certified by this review. |
| neighbor-cvt_vesicle_membrane | data/structures/membrane_organelle/cvt_vesicle_membrane.yaml; Entire neighboring maintained YAML read; used only for identity and component/part boundary context | context_only | The neighboring carrier, membrane, lumen and cargo-complex records are distinct maintained owners. Their additional protein examples, evidence and historical decisions are not separately certified by this review. |
| neighbor-cvt_complex | data/structures/other/cvt_complex.yaml; Entire neighboring maintained YAML read; used only for identity and component/part boundary context | context_only | The neighboring carrier, membrane, lumen and cargo-complex records are distinct maintained owners. Their additional protein examples, evidence and historical decisions are not separately certified by this review. |
| cvt-lumen-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033107,GO:0033110,GO:0034270,GO:0032258,GO:0031410,GO:0060205,GO:0030659,GO:0000324; All eight terms: identifiers, names, definitions, active status, synonyms and relevant is_a/part_of child relations | supports | Eight active GO terms were inspected. GO0033107 defines the double-membrane yeast carrier and its two exact synonyms; GO0033110 denotes either of its two bilayers and is explicitly part_of the vesicle. The cytoplasmic-vesicle and membrane parents explicitly list the target child classes. GO0034270 denotes a preApe1-containing Cvt cargo complex; GO0032258 describes Atg19/Atg11-dependent targeting and expansion around cargo excluding bulk cytoplasm. GO0000324 denotes the fungal destination, and GO0060205 denotes enclosed cytoplasmic-vesicle volume. |
| cvt-lumen-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternative names | supports | ENA identifies only the asserted NCBITaxon4932 species as Saccharomyces cerevisiae, with fungal lineage. It does not identify a particular experimental strain or quantify occurrence. |
| cvt-lumen-agent-reggiori2004-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=EXT_ID%3A15004240%20AND%20SRC%3AMED; Exact PMID, DOI, title, authors, publication year/type and complete abstract | supports | Native MED identifies Early stages of the secretory pathway, but not endosomes, are required for Cvt vesicle and autophagosome assembly in Saccharomyces cerevisiae. (Reggiori F, Wang CW, Nair U, Shintani T, Abeliovich H, Klionsky DJ., 2004), PMID15004240, DOI10.1091/mbc.e03-07-0479. Exact bibliography and complete abstract were read; primary body scope is recorded separately. |
| cvt-lumen-agent-reggiori2004-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC404015/; Complete Introduction sec1; Methods sec3 including strain Table1 and sec6 pulse-chase protocol; complete Results sec13 and sec14, including Figures5–8 captions; complete Discussion sec15–18 including Figure9 caption. Other Results/Methods, figure pixels and underlying data were not independently reanalysed. | supports | The primary paper describes hydrolase sequestration within cytosolic double-membrane Cvt vesicles, outer-membrane fusion and release of an inner vesicle into the vacuole. Yeast sec12/sec7 experiments test PAS organization and transport under explicit growth/temperature conditions. The authors report early-secretory contributions but state that the results cannot distinguish ER from Golgi membrane origin. This supports the maintained yeast example and broad carrier context, without fixing a unique donor or a universal molecular assembly mechanism. |
| cvt-lumen-agent-reggiori2004-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC404015/fullTextXML; Actual failed fullTextXML response only | context_only | This specific Europe PMC XML route returned HTTP500 and no article body. Genuine primary PMC HTML was independently recovered and read; this failure does not imply that the paper body is unavailable. |
| cvt-lumen-agent-SL-0323 | https://rest.uniprot.org/locations/SL-0323.json; Exact native identifier, label, definition, isA/partOf hierarchy and nested GO mappings | supports | SL0323 exactly names and defines the Cvt vesicle lumen, places it under cytoplasmic vesicle lumen SL0325/GO0060205 and part_of Cvt vesicle SL0080/GO0033107. No direct GO cross-reference is returned for SL0323; that is not an exhaustive absence result. Zero indexed proteins are not evidence that the biological lumen lacks cargo. |
| local-identity-search | rg --no-ignore --hidden -n ^identifier: (cellstructuremech:cvt_vesicle_lumen&#124;GO:0033107&#124;GO:0033110&#124;GO:0034270)$ data/structures; Complete anchored identifier matches in the maintained corpus | context_only | The ignored-inclusive search returns exactly one maintained local Cvt-lumen identifier, with distinct whole-vesicle, membrane and cargo-complex records. This proves local identity uniqueness only. |
| cvt-lumen-agent-go-lumen-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Cvt%20vesicle%20lumen&amp;limit=100; Exact query and returned first100 result identifiers/names; pageInfo current1 of7 | context_only | The native search for Cvt vesicle lumen returned 608 hits; the inspected first page contains100 results, including Cvt vesicle, membrane, assembly and broader lumen terms but no exact Cvt-lumen label. The other six pages were not inspected, so this is a bounded candidate check and not proof of ontology absence. SL0323 supplies the positive exact identity. |
| schema-result | just validate data/structures/membrane_organelle/cvt_vesicle_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/cvt_vesicle_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/cvt_vesicle_lumen.yaml --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/cvt_vesicle_lumen.yaml --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle_lumen-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/cvt_vesicle_lumen.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 6 of7 collected target identifiers returned OK in this fresh base resolver run. Residuals: cellstructuremech:cvt_vesicle_lumen: SKIPPED; resolved by evidence local-identity-search. Source-native identity checked separately. |
| native-verify | /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_lumen.yaml --verify; Complete focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_lumen.yaml --causal-graphs; Complete focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The GO lumen search was bounded to the first100 of608 returned candidates. It does not certify exhaustive ontology absence; the local identifier is positively supported by exact SL0323 and is unique in the maintained corpus.
- Reggiori2004 was read in the named primary sections, not the entire paper. Figure pixels, underlying data and measurements were not independently reanalysed. The cited experiments do not establish quantitative population prevalence or a unique membrane donor.
- The native XML routes returned500; genuine archived primary HTML was read instead. Original source access times and raw hashes are retained after resumption.
- Neighbors provide boundary context only. No other record, historical curation decision or individual neighboring protein example is separately reviewed.
- Optional molecular inventories remain incomplete. Collective bilayer constitution does not establish necessity of an individual lipid species, and conditional cargo effects are not universalized.
- Same-base global gates are integrated by the parent at finalization. Deterministic checks do not independently certify scientific claims.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorized an honest review for every uncovered target, including clean observations. No finding is invented to satisfy the local issue-only gate.
- Work paused before drafting and resumed with unchanged input/source bytes. Original source receipts were retained; no new retrieval time was substituted.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T010357Z-cvt-vesicle-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cvt structure identity, membrane boundaries and source review
started_at: '2026-10-21T11:20:48Z'
finished_at: '2026-10-22T01:03:57Z'
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
summary: The Cvt lumen identity and descriptive topology are supported at the declared
  source scopes. No concrete curation finding was established.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/membrane_organelle/cvt_vesicle.yaml
    sha256: cf6eb5075a057a0b8b104cbacb61cdf895298eb4b018945a08b46bcb939c8b0c
    role: context
  - path: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    sha256: 3bb8cb5c3f751ec93619bb4658fb51a2c6e6a94e4e0b16aa0ea8a0833a28c243
    role: target
  - path: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
    sha256: 679cdeb18f93b2ecf38916c132f8461121e7067f0db52e4b24842559b39dbb67
    role: context
  - path: data/structures/other/cvt_complex.yaml
    sha256: 29ffd90803735e2db2a3869531eae7e439bac79b868049f6d7766c6c9a694902
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
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: cellstructuremech:cvt_vesicle_lumen
  path: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  label: Cvt vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target, exact authority identities, species/source
    contexts, all component/formation boundaries and every graph edge.
  selection: Target 2 in batch twenty-five, selected by native uncovered path order
    at frozen revision9c0446.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:cvt_vesicle_lumen
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just validate data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just validate-strict data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  summary: 6 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - local-identity-search
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    --verify
  exit_code: 0
  summary: Native check passed. The target has no explicit protein accessions or GENE_OR_PROTEIN
    graph nodes; this does not independently prove biological membership.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    --causal-graphs
  exit_code: 0
  summary: Native check passed. The target has no explicit protein accessions or GENE_OR_PROTEIN
    graph nodes; this does not independently prove biological membership.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  summary: No expression-module, regulator-network or transcriptomic inference is
    made by this structural review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - neighbor-cvt_vesicle
  - neighbor-cvt_vesicle_membrane
  - neighbor-cvt_complex
  - cvt-lumen-agent-go
  - cvt-lumen-agent-tax4932
  - cvt-lumen-agent-reggiori2004-meta
  - cvt-lumen-agent-reggiori2004-pmc
  - cvt-lumen-agent-reggiori2004-jats
  - cvt-lumen-agent-SL-0323
  - local-identity-search
  - cvt-lumen-agent-go-lumen-search
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  locator: Entire maintained YAML, including every definition, evidence note, component,
    history, graph edge and discussion
  accessed_at: '2026-10-22T00:53:59Z'
  support: context_only
  summary: The entire maintained record was read. No scientific content, curation
    history or status was changed. Retained input bytes were rechecked on resumed
    work.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, constituent/associated-machinery boundary, molecular grounding
    and structure-formation necessity
  accessed_at: '2026-10-22T00:53:59Z'
  support: context_only
  summary: A whole vesicle, surrounding membrane, enclosed compartment, cargo complex
    and assembly machinery are distinct. Essentiality concerns whether the structure
    forms, not cell viability or catalytic activity.
- evidence_id: neighbor-cvt_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle.yaml
  locator: Entire neighboring maintained YAML read; used only for identity and component/part
    boundary context
  accessed_at: '2026-10-22T00:53:59Z'
  support: context_only
  summary: The neighboring carrier, membrane, lumen and cargo-complex records are
    distinct maintained owners. Their additional protein examples, evidence and historical
    decisions are not separately certified by this review.
- evidence_id: neighbor-cvt_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/cvt_vesicle_membrane.yaml
  locator: Entire neighboring maintained YAML read; used only for identity and component/part
    boundary context
  accessed_at: '2026-10-22T00:53:59Z'
  support: context_only
  summary: The neighboring carrier, membrane, lumen and cargo-complex records are
    distinct maintained owners. Their additional protein examples, evidence and historical
    decisions are not separately certified by this review.
- evidence_id: neighbor-cvt_complex
  kind: record_content
  reference: data/structures/other/cvt_complex.yaml
  locator: Entire neighboring maintained YAML read; used only for identity and component/part
    boundary context
  accessed_at: '2026-10-22T00:53:59Z'
  support: context_only
  summary: The neighboring carrier, membrane, lumen and cargo-complex records are
    distinct maintained owners. Their additional protein examples, evidence and historical
    decisions are not separately certified by this review.
- evidence_id: cvt-lumen-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033107,GO:0033110,GO:0034270,GO:0032258,GO:0031410,GO:0060205,GO:0030659,GO:0000324
  locator: 'All eight terms: identifiers, names, definitions, active status, synonyms
    and relevant is_a/part_of child relations'
  accessed_at: '2026-10-21T11:21:38.146133Z'
  support: supports
  summary: Eight active GO terms were inspected. GO0033107 defines the double-membrane
    yeast carrier and its two exact synonyms; GO0033110 denotes either of its two
    bilayers and is explicitly part_of the vesicle. The cytoplasmic-vesicle and membrane
    parents explicitly list the target child classes. GO0034270 denotes a preApe1-containing
    Cvt cargo complex; GO0032258 describes Atg19/Atg11-dependent targeting and expansion
    around cargo excluding bulk cytoplasm. GO0000324 denotes the fungal destination,
    and GO0060205 denotes enclosed cytoplasmic-vesicle volume.
  snapshot_sha256: 996f6e9edc4ec2167e0ee08326490b7e55c8f2c135f0edf88023f2475d5efca1
- evidence_id: cvt-lumen-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternative names
  accessed_at: '2026-10-21T11:21:38.146620Z'
  support: supports
  summary: ENA identifies only the asserted NCBITaxon4932 species as Saccharomyces
    cerevisiae, with fungal lineage. It does not identify a particular experimental
    strain or quantify occurrence.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: cvt-lumen-agent-reggiori2004-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=EXT_ID%3A15004240%20AND%20SRC%3AMED
  locator: Exact PMID, DOI, title, authors, publication year/type and complete abstract
  accessed_at: '2026-10-21T11:21:38.147062Z'
  support: supports
  summary: Native MED identifies Early stages of the secretory pathway, but not endosomes,
    are required for Cvt vesicle and autophagosome assembly in Saccharomyces cerevisiae.
    (Reggiori F, Wang CW, Nair U, Shintani T, Abeliovich H, Klionsky DJ., 2004), PMID15004240,
    DOI10.1091/mbc.e03-07-0479. Exact bibliography and complete abstract were read;
    primary body scope is recorded separately.
  snapshot_sha256: 923b0a91aaa2e0a2ecc4153f810d909c42f0129f6a71ea504c25908ef75af1a8
- evidence_id: cvt-lumen-agent-reggiori2004-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC404015/
  locator: Complete Introduction sec1; Methods sec3 including strain Table1 and sec6
    pulse-chase protocol; complete Results sec13 and sec14, including Figures5–8 captions;
    complete Discussion sec15–18 including Figure9 caption. Other Results/Methods,
    figure pixels and underlying data were not independently reanalysed.
  accessed_at: '2026-10-21T11:21:59.995942Z'
  support: supports
  summary: The primary paper describes hydrolase sequestration within cytosolic double-membrane
    Cvt vesicles, outer-membrane fusion and release of an inner vesicle into the vacuole.
    Yeast sec12/sec7 experiments test PAS organization and transport under explicit
    growth/temperature conditions. The authors report early-secretory contributions
    but state that the results cannot distinguish ER from Golgi membrane origin. This
    supports the maintained yeast example and broad carrier context, without fixing
    a unique donor or a universal molecular assembly mechanism.
  snapshot_sha256: 46db4d7121047a31dc3d6ea7c9eced6272d1228d8ac215109e65cb70f0766022
- evidence_id: cvt-lumen-agent-reggiori2004-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC404015/fullTextXML
  locator: Actual failed fullTextXML response only
  accessed_at: '2026-10-21T11:21:59.995547Z'
  support: context_only
  summary: This specific Europe PMC XML route returned HTTP500 and no article body.
    Genuine primary PMC HTML was independently recovered and read; this failure does
    not imply that the paper body is unavailable.
  snapshot_sha256: 491961d1d36a1d672c7f5033c56bfd163055c47bbb923db31182d2201d708457
- evidence_id: cvt-lumen-agent-SL-0323
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0323.json
  locator: Exact native identifier, label, definition, isA/partOf hierarchy and nested
    GO mappings
  accessed_at: '2026-10-21T11:21:38.146983Z'
  support: supports
  summary: SL0323 exactly names and defines the Cvt vesicle lumen, places it under
    cytoplasmic vesicle lumen SL0325/GO0060205 and part_of Cvt vesicle SL0080/GO0033107.
    No direct GO cross-reference is returned for SL0323; that is not an exhaustive
    absence result. Zero indexed proteins are not evidence that the biological lumen
    lacks cargo.
  snapshot_sha256: f7618f53ff5aed9a3a6b46b3bfe06e236d58ec7397b43999f3b8df448b8e7b4a
- evidence_id: local-identity-search
  kind: search
  reference: 'rg --no-ignore --hidden -n ^identifier: (cellstructuremech:cvt_vesicle_lumen|GO:0033107|GO:0033110|GO:0034270)$
    data/structures'
  locator: Complete anchored identifier matches in the maintained corpus
  accessed_at: '2026-10-21T11:23:37.563928Z'
  support: context_only
  summary: The ignored-inclusive search returns exactly one maintained local Cvt-lumen
    identifier, with distinct whole-vesicle, membrane and cargo-complex records. This
    proves local identity uniqueness only.
  snapshot_sha256: dc19b7fb7b78016b813044f0c66cd550844d49a39861ed1e766df48c4a5ad624
  search_scope: All maintained data/structures files, including ignored and hidden
    files, using exact anchored identifier alternatives for the four Cvt identities.
    No external-ontology absence assertion.
- evidence_id: cvt-lumen-agent-go-lumen-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=Cvt%20vesicle%20lumen&limit=100
  locator: Exact query and returned first100 result identifiers/names; pageInfo current1
    of7
  accessed_at: '2026-10-21T11:21:59.997262Z'
  support: context_only
  summary: The native search for Cvt vesicle lumen returned 608 hits; the inspected
    first page contains100 results, including Cvt vesicle, membrane, assembly and
    broader lumen terms but no exact Cvt-lumen label. The other six pages were not
    inspected, so this is a bounded candidate check and not proof of ontology absence.
    SL0323 supplies the positive exact identity.
  snapshot_sha256: 53ddff600f724b5365e6ac945bb7992736857f613acc0288fb6c8187024a459b
  search_scope: Native QuickGO query Cvt vesicle lumen; page1, limit100, 608 reported
    hits. Other pages and external ontologies not exhaustively searched.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:20:49Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/cvt_vesicle_lumen.yaml'
  snapshot_sha256: 13b032f1e60b1b976531f373a0bbefe9b5054247cf31ccbab74a3c493f7d18b4
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:20:50Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/cvt_vesicle_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cvt_vesicle_lumen-strict.tsv"
  snapshot_sha256: 5f9fc9ba734c13ad44f607167250a98d6aaee165fc521a778bbb6c1eaf75bc16
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/cvt_vesicle_lumen.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-22T00:53:59Z'
  support: supports
  summary: '6 of7 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: cellstructuremech:cvt_vesicle_lumen: SKIPPED; resolved by evidence
    local-identity-search. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    --verify
  locator: Complete focused native output
  accessed_at: '2026-10-21T11:22:15.517173Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/cvt_vesicle_lumen.yaml
    --causal-graphs
  locator: Complete focused native output
  accessed_at: '2026-10-21T11:22:16.092076Z'
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
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: identity
  area: identity
  topic: Carrier, lumen and individual surrounding bilayer remain distinct
  outcome: supported
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  summary: The target identifies the stated structure or enclosed region rather than
    the Cvt cargo protein complex, an individual Atg protein or the pathway itself.
    Native GO and UniProt definitions support the asserted hierarchy and parthood.
    Either-bilayer language preserves the double-membrane carrier; it does not collapse
    both membranes into one bilayer. The mature cargo-containing interior is distinguished
    from the inner vesicle released after fusion and from the intermembrane space.
  evidence_ids:
  - record
  - cvt-lumen-agent-go
  - cvt-lumen-agent-SL-0323
  - cvt-lumen-agent-reggiori2004-pmc
- assessment_id: scope
  area: scope
  topic: Budding-yeast model and conditional experimental context
  outcome: supported
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  summary: The species identity and canonical budding-yeast context are supported
    by Reggiori strains and experiments. COMMON is a qualitative occurrence statement,
    not a measured prevalence or an assertion that every cell contains a visible carrier.
    The source distinguishes nutrient-rich Cvt transport from starvation-induced autophagy;
    its temperature-sensitive mutant results are not generalized to all physiological
    conditions. Membrane/lumen occurrence follows from the described membrane-bounded
    carrier and exact location definitions.
  evidence_ids:
  - record
  - cvt-lumen-agent-tax4932
  - cvt-lumen-agent-reggiori2004-meta
  - cvt-lumen-agent-reggiori2004-pmc
  - cvt-lumen-agent-SL-0323
- assessment_id: lumen-grounding
  area: grounding
  topic: Positive exact source and local identifier
  outcome: supported
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  summary: SL0323 directly supports the local lumen definition, hierarchy and containing-vesicle
    relation. The ignored-inclusive corpus search confirms the identifier is unique.
    A bounded GO candidate search is recorded without claiming that no exact GO class
    exists. The lumen is an enclosed region, not an individual cargo or the Cvt pathway.
  evidence_ids:
  - record
  - cvt-lumen-agent-SL-0323
  - cvt-lumen-agent-go
  - local-identity-search
  - cvt-lumen-agent-go-lumen-search
- assessment_id: graph
  area: graph
  topic: Two descriptive boundary relations
  outcome: supported
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  summary: 'Both NONMECHANISTIC edges follow the native location definition: lumen
    part_of the whole Cvt carrier and surrounding membrane bounds the lumen. The mature
    cargo-containing compartment remains distinct from the space between the two membranes
    and from the post-fusion inner Cvt body. The record does not assert a soluble-cargo
    inventory, fusion mechanism or independent biological-process function.'
  evidence_ids:
  - record
  - cvt-lumen-agent-go
  - cvt-lumen-agent-SL-0323
  - cvt-lumen-agent-reggiori2004-pmc
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and bounded source scopes
  outcome: supported
  target_ids:
  - cellstructuremech:cvt_vesicle_lumen
  summary: The complete target, every graph edge and discussion were read. No quantitative
    property, image licence, trait link, verbatim snippet or individual protein accession
    is asserted in this target. Empty optional inventories or mechanics do not by
    themselves establish defects. PROPOSED status and inherited history are preserved;
    historical search completeness and independent authorship are not recertified.
  evidence_ids:
  - record
  - policy
  - cvt-lumen-agent-go
  - cvt-lumen-agent-reggiori2004-pmc
  - cvt-lumen-agent-SL-0323
findings: []
actions: []
limitations:
- The GO lumen search was bounded to the first100 of608 returned candidates. It does
  not certify exhaustive ontology absence; the local identifier is positively supported
  by exact SL0323 and is unique in the maintained corpus.
- Reggiori2004 was read in the named primary sections, not the entire paper. Figure
  pixels, underlying data and measurements were not independently reanalysed. The
  cited experiments do not establish quantitative population prevalence or a unique
  membrane donor.
- The native XML routes returned500; genuine archived primary HTML was read instead.
  Original source access times and raw hashes are retained after resumption.
- Neighbors provide boundary context only. No other record, historical curation decision
  or individual neighboring protein example is separately reviewed.
- Optional molecular inventories remain incomplete. Collective bilayer constitution
  does not establish necessity of an individual lipid species, and conditional cargo
  effects are not universalized.
- Same-base global gates are integrated by the parent at finalization. Deterministic
  checks do not independently certify scientific claims.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The user explicitly authorized an honest review for every uncovered target, including
  clean observations. No finding is invented to satisfy the local issue-only gate.
- Work paused before drafting and resumed with unchanged input/source bytes. Original
  source receipts were retained; no new retrieval time was substituted.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
