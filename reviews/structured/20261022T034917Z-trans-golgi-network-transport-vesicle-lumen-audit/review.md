# Trans golgi network transport vesicle lumen scientific review

- Review: 20261022T034917Z-trans-golgi-network-transport-vesicle-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:34:11Z
- Finished UTC: 2026-10-22T03:49:17Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact lumen identity, hierarchy and yeast trafficking example are supported. Two minor findings request source-qualified cargo examples and a descriptive scope label for the parthood-only graph.

## Scope And Provenance

Entire single target and complete five-record TGN boundary set (target plus four neighbors), all source claims and graph edges. Full primary main texts/Methods and captions read; exact native identities and typed relations inspected at declared scope. No record, status, history, generated page or repository index changed.

Selection: Batch41 exact path-ordered target 9; fresh f97b initial inspect/schema/strict passed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0098564 | data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml | maintained | trans-Golgi network transport vesicle lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0098564 | Focused validator passed. |
| Focused native strict | passed | True | GO:0098564 | Focused validator passed. |
| Native causal graph coverage | passed | True | GO:0098564 | Native coverage passed; source support and mechanistic scope assessed separately. |
| Individual protein verification applicability | not_applicable | False | GO:0098564 | The target has no individual protein accession or GENE_OR_PROTEIN graph node. Named background factors are assessed through the primary sources, not treated as verified accession examples. |
| Expression-module applicability | not_applicable | False | GO:0098564 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0098564 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0098564 | 14 of 14 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0098564 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0098564 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0098564 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0098564 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0098564 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact class, hierarchy and compartment boundaries

identity: supported. Targets: GO:0098564.

The exact record identity and structural kind distinguish the target from its four frozen boundary neighbors. All maintained native relationships were checked at the named term/typed-child scope. Definition-based local anatomy is distinguished from exact ontology edges.

### Yeast identity and source-specific examples

scope: supported. Targets: GO:0098564.

The species row accurately attributes the syntaxin study to Holthuis and the canonical adaptor study to Copic. Both are S. cerevisiae primary experiments. The example wording describes their TGN/endosomal model, without claiming direct isolation or a complete inventory of this target compartment. This supports the stated species-level example, with the precise strain/preparation limits retained.

### A volume without an obligatory molecular inventory

grounding: supported. Targets: GO:0098564.

The enclosed-volume class needs no obligatory cargo list to establish its identity. Empty components do not constitute an incomplete mandatory field or evidence that no cargo is present; no component formation-necessity assertion is made.

### Cargo examples need source and organism qualification

evidence: concern. Targets: GO:0098564.

The native definition establishes an enclosed volume. Holthuis assays yeast CPY/invertase/secreted glycoprotein traffic, supporting relevant cargo context but not an isolated TGN-vesicle-lumen census. Copic Chs3 is a membrane protein and its ALP reporter is transmembrane, so neither directly establishes soluble cell-wall-remodeling enzymes in the lumen. The broad microbial-eukaryote cargo extension needs explicit supporting context.

### Structural parthood is not an assembly mechanism

graph: concern. Targets: GO:0098564.

All represented edges are is-part-of topology. The record labels the graph MECHANISTIC and ASSEMBLY despite containing no causal assembly transition. The topology remains supported and needs no invented mechanism to be useful.

### Actual source tiers and unchanged scientific state

provenance: supported. Targets: GO:0098564.

Exact native authorities, complete primary abstracts and recovered full primary bodies are distinguished. Source limitations and uncertainties are retained. This review does not certify uninspected supplemental datasets, image pixels, universal cargo inventories or taxonomic prevalence.

## Findings

### F1: Qualify and source the appended lumen cargo examples

minor / open / confirmed; issue key: tgn-vesicle-lumen-cargo-scope.

The definition adds soluble cargo classes across yeasts and other microbial eukaryotes while citing only the GO volume definition. The cited yeast studies offer trafficking context, but do not establish this broad lumen-specific cargo list; membrane cargo Chs3 cannot be silently counted as a soluble lumen enzyme. No obligatory universal molecular cohort is explicitly claimed.

### F2: Label the parthood-only graph as descriptive topology

minor / open / confirmed; issue key: tgn-vesicle-lumen-graph-scope.

The graph contains only structural parthood edges but its scope and title claim an assembly/functional mechanism. This is an explanatory-scope mismatch independent of source-specific definition concerns.

## Recommended Actions And Acceptance Checks

### A1

Keep the exact enclosed-volume definition and move or qualify the cargo examples with source-specific organism and preparation context. Retain only examples with evidence of soluble luminal location; do not infer that location from a membrane-cargo trafficking assay.

- The authority definition is distinguishable from optional biological cargo examples.
- Each retained cargo class is supported at its actual organism and luminal-location scope.
- No Chs3 or transmembrane reporter is presented as evidence of freely soluble luminal cargo.
- Focused schema, strict, identifier and graph checks pass after separately authorized curation.

### A2

Use NONMECHANISTIC scope and descriptive topology wording while preserving the supported structural relations. Add causal steps only after separate source-backed curation.

- Graph scope and title accurately describe existing parthood content.
- Supported relations are preserved without invented assembly events.
- Focused schema, strict, identifier and graph checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml; Entire maintained YAML including all fields, graphs, evidence, discussions and history | context_only | Every target claim was read independently. This review changes no maintained scientific record or status. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent; essentiality; CausalGraph scope and component_ref contracts | context_only | Molecular material, complete structural compartments and formation necessity are distinct. A constituent identity or trafficking perturbation does not establish necessity for formation; a parthood-only graph is not an assembly mechanism. |
| curation | docs/CURATION.md; Evidence and causal graph requirements | context_only | Scientific evidence must support the actual assertion at its organism, preparation and explanatory scope; a correct ontology identity does not automatically support appended mechanisms. |
| neighbor-trans_golgi_network | data/structures/membrane_organelle/trans_golgi_network.yaml; Complete maintained boundary neighbor | context_only | The complete five-record TGN boundary set (target plus four neighbors) was read, distinguishing the network, its membrane, transport vesicle, vesicle lumen and vesicle membrane. Neighbor annotations are context rather than independent scientific experiments. |
| neighbor-trans_golgi_network_membrane | data/structures/membrane_organelle/trans_golgi_network_membrane.yaml; Complete maintained boundary neighbor | context_only | The complete five-record TGN boundary set (target plus four neighbors) was read, distinguishing the network, its membrane, transport vesicle, vesicle lumen and vesicle membrane. Neighbor annotations are context rather than independent scientific experiments. |
| neighbor-trans_golgi_network_transport_vesicle | data/structures/membrane_organelle/trans_golgi_network_transport_vesicle.yaml; Complete maintained boundary neighbor | context_only | The complete five-record TGN boundary set (target plus four neighbors) was read, distinguishing the network, its membrane, transport vesicle, vesicle lumen and vesicle membrane. Neighbor annotations are context rather than independent scientific experiments. |
| neighbor-trans_golgi_network_transport_vesicle_membrane | data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_membrane.yaml; Complete maintained boundary neighbor | context_only | The complete five-record TGN boundary set (target plus four neighbors) was read, distinguishing the network, its membrane, transport vesicle, vesicle lumen and vesicle membrane. Neighbor annotations are context rather than independent scientific experiments. |
| tgn-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005802,GO:0032588,GO:0000139,GO:0005794,GO:0005768,GO:0098791,GO:0030140,GO:0012510,GO:0098564,GO:0005798,GO:0030133,GO:0030136,GO:0034044,GO:0005796,GO:0098566,GO:0030658,GO:0030660,GO:0030665,GO:0030130; Exact target identity/definition/synonyms plus named parent and part typed-child entries in the complete 19-term response; unrelated children not scientifically audited | supports | Active GO0098564 defines only the volume enclosed by a TGN transport-vesicle membrane. GO0005796 and GO0098566 directly list it as an is_a child; GO0030140 lists it as a part_of child. It specifies no soluble cargo classes or microbial-eukaryote occurrence survey. |
| tgn-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxId, scientificName, rank and lineage | supports | ENA4932 identifies Saccharomyces cerevisiae at species rank within Saccharomyces. It verifies the row taxon identity and lineage, not a measured prevalence, a specific experimental strain or occurrence in other microbial groups. |
| tgn-agent-holthuis1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1093/emboj/17.1.113%22; Unique MED metadata and complete primary abstract | supports | Exact primary identity: Holthuis JC, Nichols BJ, Dhruvakumar S and Pelham HR; Two syntaxin homologues in the TGN/endosomal system of yeast; EMBO Journal 1998; DOI10.1093/emboj/17.1.113, PMID9427746, PMC1170363. The complete abstract describes Tlg1/Tlg2 syntaxin localization and selective trafficking phenotypes. |
| tgn-agent-copic2007-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1091/MBC.E06-11-1000%22; Unique MED metadata and complete primary abstract | supports | Exact primary identity: Copic A, Starr TL and Schekman R; Ent3p and Ent5p exhibit cargo-specific functions in trafficking proteins between the trans-Golgi network and the endosomes in yeast; Molecular Biology of the Cell 2007; DOI10.1091/MBC.E06-11-1000, PMID17344475, PMC1855026. |
| tgn-agent-holthuis1998-publisher | https://doi.org/10.1093/emboj/17.1.113; Genuine full publisher HTML: complete Introduction, all Results and Discussion, Figures1–11 captions, and complete Materials and methods (plasmids, strains, antibodies, microscopy, fractionation, trafficking assays and co-immunoprecipitation). Reading-text lines177–1010 cover Results through Methods. No figure pixels or supplemental data inspected. | supports | Tlg2 cofractionation/immunofluorescence supports a TGN assignment; Tlg1 early-endosome assignment remains tentative. Yeast deletions affect Kex2 retrieval and receptor degradation while forward CPY/invertase/general glycoprotein traffic is largely retained. Methods use SEY6210/6211 and specified derivative strains, principally 30 degrees C; SNARE immunoprecipitation uses RSY271. CPY and secreted glycoproteins were assayed, but the study is not a purified TGN-vesicle-lumen cargo census. The membrane-traffic schemes are working models. |
| tgn-agent-copic2007-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1855026/; Genuine PMC1855026 HTML: complete Introduction sec1, all Methods sec3–7 and Table1, all Results sec9–13, complete Discussion sec14 including15–18, and Figures1–9 captions. No figure pixels or supplementary datasets inspected. | supports | Yeast genetic, microscopy, crosslinked interaction and trafficking experiments distinguish cargo-specific Ent3/Ent5/AP1/Gga contributions. Chs3 is a multi-pass membrane cargo; A(F-to-A)-ALP is a transmembrane chimera, not a free soluble hydrolase. Late-Golgi/endosomal membrane fractions were not fully resolved. The final model allows adaptor-mediated incorporation into carriers or retention by exclusion; Figure9 arrows need not be distinct transport routes. Strain backgrounds and perturbations are specified in Table1, not generalized to all microbial eukaryotes. |
| schema-result | just validate data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/trans_golgi_network_transport_vesicle_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/trans_golgi_network_transport_vesicle_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch41-20261022-ex_agh9z/trans_golgi_network_transport_vesicle_lumen-strict.tsv |
| causal-graph-check | /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml; Complete native read-only causal-graph coverage log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 14 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Both cited primary articles were recovered as genuine full HTML and their complete main scientific text, Methods and captions read. No figure pixels, supplemental datasets or independently cited prior experiments were inspected. EuropePMC XML routes returned500; the Holthuis legacy page is abstract/PDF-only and its native PDF route returned HTTP200 challenge HTML. These failed routes do not negate the recovered publisher body.
- COMMON is interpreted as a qualitative species occurrence designation, not a measured fraction of cells or a prevalence survey. Holthuis uses specified SEY/K699/RSY strain contexts; Copic uses its Table1 strain backgrounds. Species identity is not a strain-equivalence assertion.
- Tlg and Ent functional perturbations do not demonstrate that every route or carrier depends on every named factor. Tlg1 early-endosome assignment and the proposed carrier/retention schemes remain qualified as in the primary bodies. A broad compartment example is not direct physical purification of the exact bilayer or enclosed lumen.
- Current GO places this TGN transport-vesicle class under clathrin-coated vesicle while also recording exomer parthood. Those exact authority relationships are retained without interpreting them as universal simultaneous coat composition of every TGN-derived carrier. No independent ontology repair is attempted.
- Holthuis1998 provides trafficking and syntaxin context rather than a direct experimental proof of the abstract membrane/lumen parthood edge. Exact current GO typed relations independently establish that topology.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes clean reviews. Parent owns finalization and integration of the five completed same-base batch26 global gates.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T034917Z-trans-golgi-network-transport-vesicle-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Trans golgi network transport vesicle lumen scientific review
started_at: '2026-10-22T03:34:11Z'
finished_at: '2026-10-22T03:49:17Z'
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
summary: Exact lumen identity, hierarchy and yeast trafficking example are supported.
  Two minor findings request source-qualified cargo examples and a descriptive scope
  label for the parthood-only graph.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/trans_golgi_network.yaml
    sha256: 87b0be103b020a03a3db064561125bb504cd21959ed2986ce813f62ecb6d5ef4
    role: context
  - path: data/structures/membrane_organelle/trans_golgi_network_membrane.yaml
    sha256: 67edbc6da8b52722913b6ff9cad5011d1f38d2f0cf5d16c84e91fe92a854f0a7
    role: context
  - path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle.yaml
    sha256: 0e8fec7988254c43b3f0b6bffe1ba26bde68be5be4543469233acf9564335232
    role: context
  - path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
    sha256: 14224a4767fec087790f0f07c24f9882def0a56df30a7be1d856d5bc6d8e6879
    role: target
  - path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_membrane.yaml
    sha256: 55a3a50f388915b80fc069ee5f2289a014b7ec9803ae3231477801a59650fb30
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
- target_id: GO:0098564
  path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
  label: trans-Golgi network transport vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
    role: maintained scientific record
scope:
  description: Entire single target and complete five-record TGN boundary set (target
    plus four neighbors), all source claims and graph edges. Full primary main texts/Methods
    and captions read; exact native identities and typed relations inspected at declared
    scope. No record, status, history, generated page or repository index changed.
  selection: Batch41 exact path-ordered target 9; fresh f97b initial inspect/schema/strict
    passed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0098564
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0098564
  command: just validate data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0098564
  command: just validate-strict data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
    --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/trans_golgi_network_transport_vesicle_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: causal-graphs
  name: Native causal graph coverage
  status: passed
  required: true
  target_ids:
  - GO:0098564
  command: /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
  exit_code: 0
  summary: Native coverage passed; source support and mechanistic scope assessed separately.
  evidence_ids:
  - causal-graph-check
- check_id: protein-applicability
  name: Individual protein verification applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0098564
  summary: The target has no individual protein accession or GENE_OR_PROTEIN graph
    node. Named background factors are assessed through the primary sources, not treated
    as verified accession examples.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0098564
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0098564
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - neighbor-trans_golgi_network
  - neighbor-trans_golgi_network_membrane
  - neighbor-trans_golgi_network_transport_vesicle
  - neighbor-trans_golgi_network_transport_vesicle_membrane
  - tgn-agent-go
  - tgn-agent-tax4932
  - tgn-agent-holthuis1998-meta
  - tgn-agent-copic2007-meta
  - tgn-agent-holthuis1998-publisher
  - tgn-agent-copic2007-legacy
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0098564
  summary: 14 of 14 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0098564
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0098564
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0098564
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0098564
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0098564
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
    and current batch41 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
  locator: Entire maintained YAML including all fields, graphs, evidence, discussions
    and history
  accessed_at: '2026-10-22T03:42:40Z'
  support: context_only
  summary: Every target claim was read independently. This review changes no maintained
    scientific record or status.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent; essentiality; CausalGraph scope and component_ref
    contracts
  accessed_at: '2026-10-22T03:42:40Z'
  support: context_only
  summary: Molecular material, complete structural compartments and formation necessity
    are distinct. A constituent identity or trafficking perturbation does not establish
    necessity for formation; a parthood-only graph is not an assembly mechanism.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Evidence and causal graph requirements
  accessed_at: '2026-10-22T03:42:40Z'
  support: context_only
  summary: Scientific evidence must support the actual assertion at its organism,
    preparation and explanatory scope; a correct ontology identity does not automatically
    support appended mechanisms.
- evidence_id: neighbor-trans_golgi_network
  kind: record_content
  reference: data/structures/membrane_organelle/trans_golgi_network.yaml
  locator: Complete maintained boundary neighbor
  accessed_at: '2026-10-22T03:42:40Z'
  support: context_only
  summary: The complete five-record TGN boundary set (target plus four neighbors)
    was read, distinguishing the network, its membrane, transport vesicle, vesicle
    lumen and vesicle membrane. Neighbor annotations are context rather than independent
    scientific experiments.
- evidence_id: neighbor-trans_golgi_network_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/trans_golgi_network_membrane.yaml
  locator: Complete maintained boundary neighbor
  accessed_at: '2026-10-22T03:42:40Z'
  support: context_only
  summary: The complete five-record TGN boundary set (target plus four neighbors)
    was read, distinguishing the network, its membrane, transport vesicle, vesicle
    lumen and vesicle membrane. Neighbor annotations are context rather than independent
    scientific experiments.
- evidence_id: neighbor-trans_golgi_network_transport_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle.yaml
  locator: Complete maintained boundary neighbor
  accessed_at: '2026-10-22T03:42:40Z'
  support: context_only
  summary: The complete five-record TGN boundary set (target plus four neighbors)
    was read, distinguishing the network, its membrane, transport vesicle, vesicle
    lumen and vesicle membrane. Neighbor annotations are context rather than independent
    scientific experiments.
- evidence_id: neighbor-trans_golgi_network_transport_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_membrane.yaml
  locator: Complete maintained boundary neighbor
  accessed_at: '2026-10-22T03:42:40Z'
  support: context_only
  summary: The complete five-record TGN boundary set (target plus four neighbors)
    was read, distinguishing the network, its membrane, transport vesicle, vesicle
    lumen and vesicle membrane. Neighbor annotations are context rather than independent
    scientific experiments.
- evidence_id: tgn-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005802,GO:0032588,GO:0000139,GO:0005794,GO:0005768,GO:0098791,GO:0030140,GO:0012510,GO:0098564,GO:0005798,GO:0030133,GO:0030136,GO:0034044,GO:0005796,GO:0098566,GO:0030658,GO:0030660,GO:0030665,GO:0030130
  locator: Exact target identity/definition/synonyms plus named parent and part typed-child
    entries in the complete 19-term response; unrelated children not scientifically
    audited
  accessed_at: '2026-10-22T03:34:34.860606Z'
  support: supports
  summary: Active GO0098564 defines only the volume enclosed by a TGN transport-vesicle
    membrane. GO0005796 and GO0098566 directly list it as an is_a child; GO0030140
    lists it as a part_of child. It specifies no soluble cargo classes or microbial-eukaryote
    occurrence survey.
  snapshot_sha256: ff19daf6d51d3dbcb64aa0db3e970ebe09ebf5f77ca92022cc977203dc0a019f
- evidence_id: tgn-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T03:34:34.861421Z'
  support: supports
  summary: ENA4932 identifies Saccharomyces cerevisiae at species rank within Saccharomyces.
    It verifies the row taxon identity and lineage, not a measured prevalence, a specific
    experimental strain or occurrence in other microbial groups.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: tgn-agent-holthuis1998-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1093/emboj/17.1.113%22
  locator: Unique MED metadata and complete primary abstract
  accessed_at: '2026-10-22T03:34:34.861287Z'
  support: supports
  summary: 'Exact primary identity: Holthuis JC, Nichols BJ, Dhruvakumar S and Pelham
    HR; Two syntaxin homologues in the TGN/endosomal system of yeast; EMBO Journal
    1998; DOI10.1093/emboj/17.1.113, PMID9427746, PMC1170363. The complete abstract
    describes Tlg1/Tlg2 syntaxin localization and selective trafficking phenotypes.'
  snapshot_sha256: b748fed83899299afa140027d82e55a4f0cf0ab89dafce281c6df76a3a6fc7eb
- evidence_id: tgn-agent-copic2007-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1091/MBC.E06-11-1000%22
  locator: Unique MED metadata and complete primary abstract
  accessed_at: '2026-10-22T03:34:34.861469Z'
  support: supports
  summary: 'Exact primary identity: Copic A, Starr TL and Schekman R; Ent3p and Ent5p
    exhibit cargo-specific functions in trafficking proteins between the trans-Golgi
    network and the endosomes in yeast; Molecular Biology of the Cell 2007; DOI10.1091/MBC.E06-11-1000,
    PMID17344475, PMC1855026.'
  snapshot_sha256: 09909f8bae863a3012e64a0bce970c6adbb0a9b2aa37e74863037263656b0324
- evidence_id: tgn-agent-holthuis1998-publisher
  kind: primary_source
  reference: https://doi.org/10.1093/emboj/17.1.113
  locator: 'Genuine full publisher HTML: complete Introduction, all Results and Discussion,
    Figures1–11 captions, and complete Materials and methods (plasmids, strains, antibodies,
    microscopy, fractionation, trafficking assays and co-immunoprecipitation). Reading-text
    lines177–1010 cover Results through Methods. No figure pixels or supplemental
    data inspected.'
  accessed_at: '2026-10-22T03:35:14.264054Z'
  support: supports
  summary: Tlg2 cofractionation/immunofluorescence supports a TGN assignment; Tlg1
    early-endosome assignment remains tentative. Yeast deletions affect Kex2 retrieval
    and receptor degradation while forward CPY/invertase/general glycoprotein traffic
    is largely retained. Methods use SEY6210/6211 and specified derivative strains,
    principally 30 degrees C; SNARE immunoprecipitation uses RSY271. CPY and secreted
    glycoproteins were assayed, but the study is not a purified TGN-vesicle-lumen
    cargo census. The membrane-traffic schemes are working models.
  snapshot_sha256: ababced7dd49fb9fc5abef23396d5053da12c0c0ddcd616699223f8990450385
- evidence_id: tgn-agent-copic2007-legacy
  kind: primary_source
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1855026/
  locator: 'Genuine PMC1855026 HTML: complete Introduction sec1, all Methods sec3–7
    and Table1, all Results sec9–13, complete Discussion sec14 including15–18, and
    Figures1–9 captions. No figure pixels or supplementary datasets inspected.'
  accessed_at: '2026-10-22T03:34:42.623228Z'
  support: supports
  summary: Yeast genetic, microscopy, crosslinked interaction and trafficking experiments
    distinguish cargo-specific Ent3/Ent5/AP1/Gga contributions. Chs3 is a multi-pass
    membrane cargo; A(F-to-A)-ALP is a transmembrane chimera, not a free soluble hydrolase.
    Late-Golgi/endosomal membrane fractions were not fully resolved. The final model
    allows adaptor-mediated incorporation into carriers or retention by exclusion;
    Figure9 arrows need not be distinct transport routes. Strain backgrounds and perturbations
    are specified in Table1, not generalized to all microbial eukaryotes.
  snapshot_sha256: 76a44cb1e37cc310dc9a385d170d0cc4374480a5546c4ff79f188ee9dc8a790e
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:34:14Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml'
  snapshot_sha256: 86ecfb8b08790c2980eadfc1a1bf9a21720b030b04ed50ff36d5ebf6cee8a18e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
    --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/trans_golgi_network_transport_vesicle_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:34:15Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/trans_golgi_network_transport_vesicle_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch41-20261022-ex_agh9z/trans_golgi_network_transport_vesicle_lumen-strict.tsv"
  snapshot_sha256: 15de75e2e6b313324670d03db22b7248eb7955b9037c6d0d8dddc6e699afdee5
- evidence_id: causal-graph-check
  kind: validation
  reference: /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
  locator: Complete native read-only causal-graph coverage log
  accessed_at: '2026-10-22T03:40:33.939075Z'
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
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 14 of 14 collected target identifiers returned OK. No residuals. Native
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
- assessment_id: identity
  area: identity
  topic: Exact class, hierarchy and compartment boundaries
  outcome: supported
  target_ids:
  - GO:0098564
  summary: The exact record identity and structural kind distinguish the target from
    its four frozen boundary neighbors. All maintained native relationships were checked
    at the named term/typed-child scope. Definition-based local anatomy is distinguished
    from exact ontology edges.
  evidence_ids:
  - record
  - tgn-agent-go
- assessment_id: scope
  area: scope
  topic: Yeast identity and source-specific examples
  outcome: supported
  target_ids:
  - GO:0098564
  summary: The species row accurately attributes the syntaxin study to Holthuis and
    the canonical adaptor study to Copic. Both are S. cerevisiae primary experiments.
    The example wording describes their TGN/endosomal model, without claiming direct
    isolation or a complete inventory of this target compartment. This supports the
    stated species-level example, with the precise strain/preparation limits retained.
  evidence_ids:
  - record
  - tgn-agent-tax4932
  - tgn-agent-holthuis1998-meta
  - tgn-agent-copic2007-meta
  - tgn-agent-holthuis1998-publisher
  - tgn-agent-copic2007-legacy
- assessment_id: components
  area: grounding
  topic: A volume without an obligatory molecular inventory
  outcome: supported
  target_ids:
  - GO:0098564
  summary: The enclosed-volume class needs no obligatory cargo list to establish its
    identity. Empty components do not constitute an incomplete mandatory field or
    evidence that no cargo is present; no component formation-necessity assertion
    is made.
  evidence_ids:
  - record
  - schema
  - tgn-agent-go
- assessment_id: definition
  area: evidence
  topic: Cargo examples need source and organism qualification
  outcome: concern
  target_ids:
  - GO:0098564
  summary: The native definition establishes an enclosed volume. Holthuis assays yeast
    CPY/invertase/secreted glycoprotein traffic, supporting relevant cargo context
    but not an isolated TGN-vesicle-lumen census. Copic Chs3 is a membrane protein
    and its ALP reporter is transmembrane, so neither directly establishes soluble
    cell-wall-remodeling enzymes in the lumen. The broad microbial-eukaryote cargo
    extension needs explicit supporting context.
  evidence_ids:
  - record
  - tgn-agent-go
  - tgn-agent-holthuis1998-publisher
  - tgn-agent-copic2007-legacy
- assessment_id: graph-scope
  area: graph
  topic: Structural parthood is not an assembly mechanism
  outcome: concern
  target_ids:
  - GO:0098564
  summary: All represented edges are is-part-of topology. The record labels the graph
    MECHANISTIC and ASSEMBLY despite containing no causal assembly transition. The
    topology remains supported and needs no invented mechanism to be useful.
  evidence_ids:
  - record
  - schema
  - tgn-agent-go
- assessment_id: provenance
  area: provenance
  topic: Actual source tiers and unchanged scientific state
  outcome: supported
  target_ids:
  - GO:0098564
  summary: Exact native authorities, complete primary abstracts and recovered full
    primary bodies are distinguished. Source limitations and uncertainties are retained.
    This review does not certify uninspected supplemental datasets, image pixels,
    universal cargo inventories or taxonomic prevalence.
  evidence_ids:
  - record
  - tgn-agent-go
  - tgn-agent-tax4932
  - tgn-agent-holthuis1998-meta
  - tgn-agent-copic2007-meta
  - tgn-agent-holthuis1998-publisher
  - tgn-agent-copic2007-legacy
findings:
- finding_id: F1
  issue_key: tgn-vesicle-lumen-cargo-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify and source the appended lumen cargo examples
  description: The definition adds soluble cargo classes across yeasts and other microbial
    eukaryotes while citing only the GO volume definition. The cited yeast studies
    offer trafficking context, but do not establish this broad lumen-specific cargo
    list; membrane cargo Chs3 cannot be silently counted as a soluble lumen enzyme.
    No obligatory universal molecular cohort is explicitly claimed.
  target_ids:
  - GO:0098564
  field_paths:
  - definition
  - definition_source
  evidence_ids:
  - record
  - tgn-agent-go
  - tgn-agent-holthuis1998-publisher
  - tgn-agent-copic2007-legacy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
    role: maintained scientific record
  rule_id: Claim-level source and graph scope contract
  native_severity: minor
  normalization_reason: This is bounded source/location qualification of possible
    cargo examples, not a demonstrated wrong volume identity or an asserted obligatory
    cohort; minor is proportionate.
- finding_id: F2
  issue_key: tgn-vesicle-lumen-graph-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Label the parthood-only graph as descriptive topology
  description: The graph contains only structural parthood edges but its scope and
    title claim an assembly/functional mechanism. This is an explanatory-scope mismatch
    independent of source-specific definition concerns.
  target_ids:
  - GO:0098564
  field_paths:
  - causal_graphs[0].scope_status
  - causal_graphs[0].title
  - causal_graphs[0].description
  evidence_ids:
  - record
  - schema
  - tgn-agent-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
    role: maintained scientific record
  rule_id: Claim-level source and graph scope contract
  native_severity: minor
  normalization_reason: The structural information is correct; the defect is its bounded
    mechanistic classification.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0098564
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
    role: maintained scientific record
  description: Keep the exact enclosed-volume definition and move or qualify the cargo
    examples with source-specific organism and preparation context. Retain only examples
    with evidence of soluble luminal location; do not infer that location from a membrane-cargo
    trafficking assay.
  acceptance_checks:
  - The authority definition is distinguishable from optional biological cargo examples.
  - Each retained cargo class is supported at its actual organism and luminal-location
    scope.
  - No Chs3 or transmembrane reporter is presented as evidence of freely soluble luminal
    cargo.
  - Focused schema, strict, identifier and graph checks pass after separately authorized
    curation.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0098564
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/trans_golgi_network_transport_vesicle_lumen.yaml
    role: maintained scientific record
  description: Use NONMECHANISTIC scope and descriptive topology wording while preserving
    the supported structural relations. Add causal steps only after separate source-backed
    curation.
  acceptance_checks:
  - Graph scope and title accurately describe existing parthood content.
  - Supported relations are preserved without invented assembly events.
  - Focused schema, strict, identifier and graph checks pass after separately authorized
    curation.
limitations:
- Both cited primary articles were recovered as genuine full HTML and their complete
  main scientific text, Methods and captions read. No figure pixels, supplemental
  datasets or independently cited prior experiments were inspected. EuropePMC XML
  routes returned500; the Holthuis legacy page is abstract/PDF-only and its native
  PDF route returned HTTP200 challenge HTML. These failed routes do not negate the
  recovered publisher body.
- COMMON is interpreted as a qualitative species occurrence designation, not a measured
  fraction of cells or a prevalence survey. Holthuis uses specified SEY/K699/RSY strain
  contexts; Copic uses its Table1 strain backgrounds. Species identity is not a strain-equivalence
  assertion.
- Tlg and Ent functional perturbations do not demonstrate that every route or carrier
  depends on every named factor. Tlg1 early-endosome assignment and the proposed carrier/retention
  schemes remain qualified as in the primary bodies. A broad compartment example is
  not direct physical purification of the exact bilayer or enclosed lumen.
- Current GO places this TGN transport-vesicle class under clathrin-coated vesicle
  while also recording exomer parthood. Those exact authority relationships are retained
  without interpreting them as universal simultaneous coat composition of every TGN-derived
  carrier. No independent ontology repair is attempted.
- Holthuis1998 provides trafficking and syntaxin context rather than a direct experimental
  proof of the abstract membrane/lumen parthood edge. Exact current GO typed relations
  independently establish that topology.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes clean reviews. Parent owns finalization and integration
  of the five completed same-base batch26 global gates.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
