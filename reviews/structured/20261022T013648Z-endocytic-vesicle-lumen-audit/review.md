# Endocytic-vesicle identity, subtype boundaries and source review

- Review: 20261022T013648Z-endocytic-vesicle-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:09:02Z
- Finished UTC: 2026-10-22T01:36:48Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The generic endocytic-vesicle lumen identity, documented parent inference and boundary topology are supported within the declared source scopes. No concrete curation finding was established.

## Scope And Provenance

Entire single maintained target, exact ontology/taxon identities, all component/formation boundaries and graph edges, full Newpher main text and complete Kaksonen primary abstract.

Selection: Target5 of batch twenty-seven, strict uncovered path order at fresh revision f97b1abe; native initial inspections and focused gates completed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0071682 | data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml | maintained | endocytic vesicle lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0071682 | Focused validator passed. |
| Focused native strict | passed | True | GO:0071682 | Focused validator passed. |
| Focused native verify | passed | True | GO:0071682 | Native focused checks passed. No individual protein examples or GENE_OR_PROTEIN nodes are present; scientific claims are assessed separately. |
| Focused native causal-graphs | passed | True | GO:0071682 | Native focused checks passed. No individual protein examples or GENE_OR_PROTEIN nodes are present; scientific claims are assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0071682 | This structural/topological review does not infer expression-module membership or transcriptomic regulation. |
| Claim-level scientific review | passed | True | GO:0071682 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0071682 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0071682 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0071682 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0071682 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0071682 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0071682 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Generic endocytic carrier and exact compartment boundaries

identity: supported. Targets: GO:0071682.

The target identity and definition exactly match its native GO term. The generic carrier is a cytoplasmic vesicle; its membrane and lumen are distinct parts. Narrower clathrin-coated classes and the clathrin coat remain separate from these generic records. The definition is not restricted to one yeast coat/adaptor inventory.

### Budding-yeast occurrence and cortical model

scope: supported. Targets: GO:0071682.

The species identity is exact. Newpher directly supports cortical clathrin/adaptor recruitment and actin-associated endocytic sites in the listed S. cerevisiae strains and assay conditions. Kaksonen primary abstract supports ordered functional modules and vesicle formation in the budding-yeast model. COMMON is qualitative occurrence, not a measured population frequency or uniform coat requirement. No experimental strain, coat-loss timing, direct sealed-lumen measurement or universal molecular mechanism is supplied by inference.

### Explicitly curated narrower lumen parent

grounding: supported. Targets: GO:0071682.

The native direct lumen parent is broader GO0070013. The maintained record openly uses GO0060205 by combining the exact enclosed-volume definitions with the endocytic-vesicle is_a cytoplasmic-vesicle relation. This is a defensible bounded classification inference and is not misreported as a direct GO assertion. No surrounding membrane or cytosolic space is reclassified as lumen.

### Volume and variable cargo remain distinct

completeness: supported. Targets: GO:0071682.

The lumen is a region, not a stable molecular cargo set. The resolved discussion correctly avoids making the surrounding membrane a lumen constituent and leaves variable uptake cargo unspecified. There is no direct constituent, assembly-essentiality or independent biological-process claim to test in this target.

### Two NONMECHANISTIC boundary edges

graph: supported. Targets: GO:0071682.

The lumen is part_of the endocytic vesicle and bounded by its membrane. Exact GO definitions support both. The yeast literature supplies carrier context but does not directly image a sealed aqueous lumen; that distinction is preserved.

### Full target with explicit primary access limits

completeness: supported. Targets: GO:0071682.

All maintained fields, evidence notes, graph edges and discussions were read. The target asserts no individual protein accession, quantitative physical property, image licence or verbatim evidence snippet. Historical issue resolutions are context, not independently adjudicated predecessors. PROPOSED status and existing histories are preserved.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml; Entire maintained YAML, including every evidence note, history entry, graph edge and discussion | context_only | The complete target was read without scientific edits or status/history changes. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; Component grounding, role and essentiality contracts; frozen local scientific-review rubric | context_only | Generic carrier, lumen, membrane, coat subtype and temporary assembly machinery are distinct. Essentiality means whether the structure forms, not whether a component is present or catalytically active. |
| neighbor-endocytic_vesicle | data/structures/membrane_organelle/endocytic_vesicle.yaml; Entire neighboring maintained YAML read for carrier/lumen/boundary context | context_only | The neighboring records preserve distinct whole-carrier, enclosed-volume and surrounding-bilayer identities. They are context inputs, not additional targets of this review. |
| neighbor-endocytic_vesicle_membrane | data/structures/membrane_organelle/endocytic_vesicle_membrane.yaml; Entire neighboring maintained YAML read for carrier/lumen/boundary context | context_only | The neighboring records preserve distinct whole-carrier, enclosed-volume and surrounding-bilayer identities. They are context inputs, not additional targets of this review. |
| endocytic-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030139,GO:0031410,GO:0030666,GO:0071682,GO:0045334,GO:0030128,GO:0006897,GO:0060205,GO:0106176,GO:0030659,GO:0098588,GO:0030669; Complete returned IDs, names, definitions, active flags and relevant is_a/part_of children; no ontology annotation is inferred solely from a similarly named term | supports | All twelve active GO terms were inspected. GO0030139 defines the generic endocytic carrier and is_a cytoplasmic vesicle; GO0030666 and GO0071682 are its membrane and lumen parts. GO0030659 and GO0098588 explicitly list the membrane as an is_a child. GO0045334, GO0030669 and GO0106176 are narrower clathrin-coated carrier/membrane/lumen classes; GO0030128 is their coat. GO0006897 describes uptake by plasma-membrane invagination. GO0060205 denotes cytoplasmic-vesicle lumen. |
| endocytic-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact taxId, scientificName, rank, lineage and alternate names | supports | ENA identifies NCBITaxon4932 as Saccharomyces cerevisiae, species rank and fungal lineage. This taxon receipt does not identify an experimental strain or quantify vesicle prevalence. |
| endocytic-agent-newpher2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016%2Fj.devcel.2005.04.014%22; Exact bibliography and complete primary abstractText; Kaksonen body not recovered | supports | Native MED confirms In vivo dynamics of clathrin and its adaptor-dependent recruitment to the actin-based endocytic machinery in yeast. by Newpher TM, Smith RP, Lemmon V, Lemmon SK. (2005), PMID15992543, DOI10.1016/j.devcel.2005.04.014. The abstract identifies cortical clathrin recruitment and actin-based endocytic machinery in budding yeast; detailed support is taken from the separately inspected full primary PDF. |
| endocytic-agent-kaksonen2005-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016%2Fj.cell.2005.09.024%22; Exact bibliography and complete primary abstractText; Kaksonen body not recovered | supports | Native MED confirms A modular design for the clathrin- and actin-mediated endocytosis machinery. by Kaksonen M, Toret CP, Drubin DG. (2005), PMID16239147, DOI10.1016/j.cell.2005.09.024. The complete primary abstract reports four modules governing coat formation, membrane invagination, actin assembly and scission in budding yeast, with clathrin assisting initiation but not necessary for invagination or vesicle formation. This supports the broad canonical module-dynamics example without claiming that the inaccessible body was read. |
| endocytic-agent-newpher2005-duke | https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content; Printed pp87–96: complete scientific main text, Introduction, Results, Discussion and Experimental Procedures; Table1 and Fig1–6 captions. Figure pixels, supplemental movies/figures and references as independent studies were not assessed. Original Duke PDF receipt retained unchanged. | supports | The full primary paper studies live S. cerevisiae strains, cortical versus internal clathrin, cargo/adaptor colocalization, LAT-A and deletion perturbations, and TIRF/FLIP dynamics. It directly supports adaptor-dependent recruitment at cortical actin-based endocytic sites. Discussion explicitly cannot distinguish clathrin disassembly before budding from a clathrin-containing bud/vesicle leaving the TIRF field; this review does not convert recruitment into proof of a sealed coated vesicle or lumen. The narrow recruitment notes and broad yeast example are consistent with that scope. |
| endocytic-agent-kaksonen2005-publisher | https://www.sciencedirect.com/science/article/pii/S0092867405009785; Actual native response; access diagnostic only | context_only | The retained ScienceDirect request returnedHTTP403 and did not provide readable article body. |
| endocytic-agent-kaksonen2005-api | https://api.elsevier.com/content/article/PII:S0092867405009785?httpAccept=text/xml; Actual native response; access diagnostic only | context_only | The retained public Elsevier API response returnedHTTP200 but contains only core bibliographic/open-access metadata and links, no scientific body. An open-access flag is not treated as actual body recovery. |
| endocytic-agent-go-intracellular-lumen | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070013; Exact identifier/definition and both relevant is_a child rows | supports | GO0070013 is intracellular organelle lumen and directly lists GO0071682 and GO0060205 as separate is_a children. This confirms the source-direct broader parent described in the discussion, rather than claiming the curated narrower parent is already a GO axiom. |
| endocytic-agent-go-endocytic-lumen-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071682/ancestors?relations=is_a,part_of; Complete requested is_a,part_of ancestor list for GO0071682 | supports | The native is_a/part_of ancestor response for GO0071682 includes the whole endocytic and cytoplasmic vesicle classes and intracellular organelle lumen. It does not list GO0060205. The maintained choice of that narrower lumen class is therefore a documented curator inference, not a directly asserted ancestor in this response. |
| schema-result | just validate data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endocytic_vesicle_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endocytic_vesicle_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endocytic_vesicle_lumen-strict.tsv |
| native-verify | uv run python scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml; Complete focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml; Complete focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- The narrower cytoplasmic-vesicle-lumen parent is a documented curator inference, not a direct GO ancestor assertion in the inspected native response.
- Newpher2005 scientific main text was read completely through printed p96, with Table1 and figure captions; image pixels, supplemental data/movies and raw measurements were not independently reanalyzed. TIRF disappearance cannot by itself discriminate coat disassembly from vesicle/bud movement out of the field.
- Kaksonen2005 is supported only by the exact inspected complete primary abstract. Retained publisher403 and API metadata-only responses are documented. Full methods, figure panels, precise timing and detailed perturbation implementations are not independently certified.
- Yeast-specific cortical recruitment and module behavior do not establish a universal coat/adaptor inventory, quantitative population prevalence or molecular formation necessity for every generic endocytic vesicle.
- The optional molecular inventory is incomplete; no issue is invented solely from an empty optional field or acknowledged unknown.
- The three maintained neighbors were read only for boundary context. No scientific content, native status or history was changed.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit user goal authorizes an honest review for every uncovered target, including clean observations; no finding is invented to satisfy the local issue-only output rule.
- The reused Newpher PDF and Kaksonen access diagnostics retain their original raw bytes, SHA256 and UTC access timestamps.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T013648Z-endocytic-vesicle-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Endocytic-vesicle identity, subtype boundaries and source review
started_at: '2026-10-22T01:09:02Z'
finished_at: '2026-10-22T01:36:48Z'
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
summary: The generic endocytic-vesicle lumen identity, documented parent inference
  and boundary topology are supported within the declared source scopes. No concrete
  curation finding was established.
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
  - path: data/structures/membrane_organelle/endocytic_vesicle.yaml
    sha256: ae5fddc4231f0302846ce5f2baad8665456b8d042bb3cdad58b1675636fe9b82
    role: context
  - path: data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
    sha256: 5f1d0bbdb0ae22d96964222f70d6eda4be22f838ec7d1cbbac19b7857a10790c
    role: target
  - path: data/structures/membrane_organelle/endocytic_vesicle_membrane.yaml
    sha256: 532ded42040e51dfeef59ceb1ec3adfc1114e07d298b5aa96ce01284b3aede36
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
- target_id: GO:0071682
  path: data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
  label: endocytic vesicle lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target, exact ontology/taxon identities, all
    component/formation boundaries and graph edges, full Newpher main text and complete
    Kaksonen primary abstract.
  selection: Target5 of batch twenty-seven, strict uncovered path order at fresh revision
    f97b1abe; native initial inspections and focused gates completed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0071682
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0071682
  command: just validate data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0071682
  command: just validate-strict data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
    --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endocytic_vesicle_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-verify
  name: Focused native verify
  status: passed
  required: true
  target_ids:
  - GO:0071682
  command: uv run python scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
  exit_code: 0
  summary: Native focused checks passed. No individual protein examples or GENE_OR_PROTEIN
    nodes are present; scientific claims are assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Focused native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0071682
  command: uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
  exit_code: 0
  summary: Native focused checks passed. No individual protein examples or GENE_OR_PROTEIN
    nodes are present; scientific claims are assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0071682
  summary: This structural/topological review does not infer expression-module membership
    or transcriptomic regulation.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0071682
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - neighbor-endocytic_vesicle
  - neighbor-endocytic_vesicle_membrane
  - endocytic-agent-go
  - endocytic-agent-tax4932
  - endocytic-agent-newpher2005-meta
  - endocytic-agent-kaksonen2005-meta
  - endocytic-agent-newpher2005-duke
  - endocytic-agent-kaksonen2005-publisher
  - endocytic-agent-kaksonen2005-api
  - endocytic-agent-go-intracellular-lumen
  - endocytic-agent-go-endocytic-lumen-ancestors
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0071682
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0071682
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0071682
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0071682
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0071682
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0071682
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
    and current batch27 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
  locator: Entire maintained YAML, including every evidence note, history entry, graph
    edge and discussion
  accessed_at: '2026-10-22T01:12:57Z'
  support: context_only
  summary: The complete target was read without scientific edits or status/history
    changes.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component grounding, role and essentiality contracts; frozen local scientific-review
    rubric
  accessed_at: '2026-10-22T01:12:57Z'
  support: context_only
  summary: Generic carrier, lumen, membrane, coat subtype and temporary assembly machinery
    are distinct. Essentiality means whether the structure forms, not whether a component
    is present or catalytically active.
- evidence_id: neighbor-endocytic_vesicle
  kind: record_content
  reference: data/structures/membrane_organelle/endocytic_vesicle.yaml
  locator: Entire neighboring maintained YAML read for carrier/lumen/boundary context
  accessed_at: '2026-10-22T01:12:57Z'
  support: context_only
  summary: The neighboring records preserve distinct whole-carrier, enclosed-volume
    and surrounding-bilayer identities. They are context inputs, not additional targets
    of this review.
- evidence_id: neighbor-endocytic_vesicle_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/endocytic_vesicle_membrane.yaml
  locator: Entire neighboring maintained YAML read for carrier/lumen/boundary context
  accessed_at: '2026-10-22T01:12:57Z'
  support: context_only
  summary: The neighboring records preserve distinct whole-carrier, enclosed-volume
    and surrounding-bilayer identities. They are context inputs, not additional targets
    of this review.
- evidence_id: endocytic-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030139,GO:0031410,GO:0030666,GO:0071682,GO:0045334,GO:0030128,GO:0006897,GO:0060205,GO:0106176,GO:0030659,GO:0098588,GO:0030669
  locator: Complete returned IDs, names, definitions, active flags and relevant is_a/part_of
    children; no ontology annotation is inferred solely from a similarly named term
  accessed_at: '2026-10-22T01:10:34.317063Z'
  support: supports
  summary: All twelve active GO terms were inspected. GO0030139 defines the generic
    endocytic carrier and is_a cytoplasmic vesicle; GO0030666 and GO0071682 are its
    membrane and lumen parts. GO0030659 and GO0098588 explicitly list the membrane
    as an is_a child. GO0045334, GO0030669 and GO0106176 are narrower clathrin-coated
    carrier/membrane/lumen classes; GO0030128 is their coat. GO0006897 describes uptake
    by plasma-membrane invagination. GO0060205 denotes cytoplasmic-vesicle lumen.
  snapshot_sha256: a38223c5166d9bcf00a9596c8896ed27b37944abfce9aa8e0832b0d22a308237
- evidence_id: endocytic-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact taxId, scientificName, rank, lineage and alternate names
  accessed_at: '2026-10-22T01:10:34.317392Z'
  support: supports
  summary: ENA identifies NCBITaxon4932 as Saccharomyces cerevisiae, species rank
    and fungal lineage. This taxon receipt does not identify an experimental strain
    or quantify vesicle prevalence.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: endocytic-agent-newpher2005-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016%2Fj.devcel.2005.04.014%22
  locator: Exact bibliography and complete primary abstractText; Kaksonen body not
    recovered
  accessed_at: '2026-10-22T01:10:34.317531Z'
  support: supports
  summary: Native MED confirms In vivo dynamics of clathrin and its adaptor-dependent
    recruitment to the actin-based endocytic machinery in yeast. by Newpher TM, Smith
    RP, Lemmon V, Lemmon SK. (2005), PMID15992543, DOI10.1016/j.devcel.2005.04.014.
    The abstract identifies cortical clathrin recruitment and actin-based endocytic
    machinery in budding yeast; detailed support is taken from the separately inspected
    full primary PDF.
  snapshot_sha256: 290e57353f122e93eeb68e99c94db4b919fd00d792e000f106bc3efdb0afd4f9
- evidence_id: endocytic-agent-kaksonen2005-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016%2Fj.cell.2005.09.024%22
  locator: Exact bibliography and complete primary abstractText; Kaksonen body not
    recovered
  accessed_at: '2026-10-22T01:10:34.317472Z'
  support: supports
  summary: Native MED confirms A modular design for the clathrin- and actin-mediated
    endocytosis machinery. by Kaksonen M, Toret CP, Drubin DG. (2005), PMID16239147,
    DOI10.1016/j.cell.2005.09.024. The complete primary abstract reports four modules
    governing coat formation, membrane invagination, actin assembly and scission in
    budding yeast, with clathrin assisting initiation but not necessary for invagination
    or vesicle formation. This supports the broad canonical module-dynamics example
    without claiming that the inaccessible body was read.
  snapshot_sha256: 9f5acaad74a800d7b2c5dc356d3c3db03001b9526d1322f2b0482111bfbb7e6c
- evidence_id: endocytic-agent-newpher2005-duke
  kind: primary_source
  reference: https://dukespace.lib.duke.edu/server/api/core/bitstreams/e3c70c30-e4a1-4ba0-8ea6-c50af4ba491e/content
  locator: 'Printed pp87–96: complete scientific main text, Introduction, Results,
    Discussion and Experimental Procedures; Table1 and Fig1–6 captions. Figure pixels,
    supplemental movies/figures and references as independent studies were not assessed.
    Original Duke PDF receipt retained unchanged.'
  accessed_at: '2026-10-21T11:00:52.091438Z'
  support: supports
  summary: The full primary paper studies live S. cerevisiae strains, cortical versus
    internal clathrin, cargo/adaptor colocalization, LAT-A and deletion perturbations,
    and TIRF/FLIP dynamics. It directly supports adaptor-dependent recruitment at
    cortical actin-based endocytic sites. Discussion explicitly cannot distinguish
    clathrin disassembly before budding from a clathrin-containing bud/vesicle leaving
    the TIRF field; this review does not convert recruitment into proof of a sealed
    coated vesicle or lumen. The narrow recruitment notes and broad yeast example
    are consistent with that scope.
  snapshot_sha256: c848e911372b9afb9902e4a74e3cb3dd66ef90eb5e102024cc95fff648bb6c21
- evidence_id: endocytic-agent-kaksonen2005-publisher
  kind: authority
  reference: https://www.sciencedirect.com/science/article/pii/S0092867405009785
  locator: Actual native response; access diagnostic only
  accessed_at: '2026-10-21T11:04:59.142998Z'
  support: context_only
  summary: The retained ScienceDirect request returnedHTTP403 and did not provide
    readable article body.
  snapshot_sha256: 2f404f9566166ed7addf3acf1a84c3823e680c96afec905b2082e988e618856e
- evidence_id: endocytic-agent-kaksonen2005-api
  kind: authority
  reference: https://api.elsevier.com/content/article/PII:S0092867405009785?httpAccept=text/xml
  locator: Actual native response; access diagnostic only
  accessed_at: '2026-10-21T11:05:34.914917Z'
  support: context_only
  summary: The retained public Elsevier API response returnedHTTP200 but contains
    only core bibliographic/open-access metadata and links, no scientific body. An
    open-access flag is not treated as actual body recovery.
  snapshot_sha256: 53993cd92f3bb1d1dcd4f4f4887c8a8acd6f0e64d35250a3fd23d05fc0dd0f51
- evidence_id: endocytic-agent-go-intracellular-lumen
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0070013
  locator: Exact identifier/definition and both relevant is_a child rows
  accessed_at: '2026-10-22T01:11:34.939562Z'
  support: supports
  summary: GO0070013 is intracellular organelle lumen and directly lists GO0071682
    and GO0060205 as separate is_a children. This confirms the source-direct broader
    parent described in the discussion, rather than claiming the curated narrower
    parent is already a GO axiom.
  snapshot_sha256: addf72a5ca9bfa86f1f02d5c7c4e73e8f8c9a6f91bba093244d1c1b67de463bc
- evidence_id: endocytic-agent-go-endocytic-lumen-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0071682/ancestors?relations=is_a,part_of
  locator: Complete requested is_a,part_of ancestor list for GO0071682
  accessed_at: '2026-10-22T01:11:34.939949Z'
  support: supports
  summary: The native is_a/part_of ancestor response for GO0071682 includes the whole
    endocytic and cytoplasmic vesicle classes and intracellular organelle lumen. It
    does not list GO0060205. The maintained choice of that narrower lumen class is
    therefore a documented curator inference, not a directly asserted ancestor in
    this response.
  snapshot_sha256: 537edb1a2779935b1e2aa857bc5681a2aa73028aee3b88b3a9a8913f40dea8be
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:09:04Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml'
  snapshot_sha256: f0f3a4f8af992d947c07ec92a2b870ae962fa27332b5eb4026bbec25fe5bf7c8
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
    --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endocytic_vesicle_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:09:05Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endocytic_vesicle_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch27-20261022-bkr4ie9p/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch27-20261022-bkr4ie9p/endocytic_vesicle_lumen-strict.tsv"
  snapshot_sha256: 7aa5afd22097098d38570be87dbf8f2d52a332c8c8e849b573b052cde809b12b
- evidence_id: native-verify
  kind: validation
  reference: uv run python scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
  locator: Complete focused native output
  accessed_at: '2026-10-22T01:11:18.118787Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: uv run python scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml
  locator: Complete focused native output
  accessed_at: '2026-10-22T01:11:18.710317Z'
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
  locator: data/structures/membrane_organelle/endocytic_vesicle_lumen.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
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
  topic: Generic endocytic carrier and exact compartment boundaries
  outcome: supported
  target_ids:
  - GO:0071682
  summary: The target identity and definition exactly match its native GO term. The
    generic carrier is a cytoplasmic vesicle; its membrane and lumen are distinct
    parts. Narrower clathrin-coated classes and the clathrin coat remain separate
    from these generic records. The definition is not restricted to one yeast coat/adaptor
    inventory.
  evidence_ids:
  - record
  - endocytic-agent-go
- assessment_id: scope
  area: scope
  topic: Budding-yeast occurrence and cortical model
  outcome: supported
  target_ids:
  - GO:0071682
  summary: The species identity is exact. Newpher directly supports cortical clathrin/adaptor
    recruitment and actin-associated endocytic sites in the listed S. cerevisiae strains
    and assay conditions. Kaksonen primary abstract supports ordered functional modules
    and vesicle formation in the budding-yeast model. COMMON is qualitative occurrence,
    not a measured population frequency or uniform coat requirement. No experimental
    strain, coat-loss timing, direct sealed-lumen measurement or universal molecular
    mechanism is supplied by inference.
  evidence_ids:
  - record
  - endocytic-agent-tax4932
  - endocytic-agent-newpher2005-duke
  - endocytic-agent-newpher2005-meta
  - endocytic-agent-kaksonen2005-meta
- assessment_id: inferred-parent
  area: grounding
  topic: Explicitly curated narrower lumen parent
  outcome: supported
  target_ids:
  - GO:0071682
  summary: The native direct lumen parent is broader GO0070013. The maintained record
    openly uses GO0060205 by combining the exact enclosed-volume definitions with
    the endocytic-vesicle is_a cytoplasmic-vesicle relation. This is a defensible
    bounded classification inference and is not misreported as a direct GO assertion.
    No surrounding membrane or cytosolic space is reclassified as lumen.
  evidence_ids:
  - record
  - endocytic-agent-go
  - endocytic-agent-go-intracellular-lumen
  - endocytic-agent-go-endocytic-lumen-ancestors
- assessment_id: components
  area: completeness
  topic: Volume and variable cargo remain distinct
  outcome: supported
  target_ids:
  - GO:0071682
  summary: The lumen is a region, not a stable molecular cargo set. The resolved discussion
    correctly avoids making the surrounding membrane a lumen constituent and leaves
    variable uptake cargo unspecified. There is no direct constituent, assembly-essentiality
    or independent biological-process claim to test in this target.
  evidence_ids:
  - record
  - policy
  - endocytic-agent-go
- assessment_id: graph
  area: graph
  topic: Two NONMECHANISTIC boundary edges
  outcome: supported
  target_ids:
  - GO:0071682
  summary: The lumen is part_of the endocytic vesicle and bounded by its membrane.
    Exact GO definitions support both. The yeast literature supplies carrier context
    but does not directly image a sealed aqueous lumen; that distinction is preserved.
  evidence_ids:
  - record
  - endocytic-agent-go
  - endocytic-agent-newpher2005-duke
- assessment_id: coverage
  area: completeness
  topic: Full target with explicit primary access limits
  outcome: supported
  target_ids:
  - GO:0071682
  summary: All maintained fields, evidence notes, graph edges and discussions were
    read. The target asserts no individual protein accession, quantitative physical
    property, image licence or verbatim evidence snippet. Historical issue resolutions
    are context, not independently adjudicated predecessors. PROPOSED status and existing
    histories are preserved.
  evidence_ids:
  - record
  - policy
  - endocytic-agent-go
  - endocytic-agent-newpher2005-duke
  - endocytic-agent-newpher2005-meta
  - endocytic-agent-kaksonen2005-meta
findings: []
actions: []
limitations:
- The narrower cytoplasmic-vesicle-lumen parent is a documented curator inference,
  not a direct GO ancestor assertion in the inspected native response.
- Newpher2005 scientific main text was read completely through printed p96, with Table1
  and figure captions; image pixels, supplemental data/movies and raw measurements
  were not independently reanalyzed. TIRF disappearance cannot by itself discriminate
  coat disassembly from vesicle/bud movement out of the field.
- Kaksonen2005 is supported only by the exact inspected complete primary abstract.
  Retained publisher403 and API metadata-only responses are documented. Full methods,
  figure panels, precise timing and detailed perturbation implementations are not
  independently certified.
- Yeast-specific cortical recruitment and module behavior do not establish a universal
  coat/adaptor inventory, quantitative population prevalence or molecular formation
  necessity for every generic endocytic vesicle.
- The optional molecular inventory is incomplete; no issue is invented solely from
  an empty optional field or acknowledged unknown.
- The three maintained neighbors were read only for boundary context. No scientific
  content, native status or history was changed.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit user goal authorizes an honest review for every uncovered target, including
  clean observations; no finding is invented to satisfy the local issue-only output
  rule.
- The reused Newpher PDF and Kaksonen access diagnostics retain their original raw
  bytes, SHA256 and UTC access timestamps.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
