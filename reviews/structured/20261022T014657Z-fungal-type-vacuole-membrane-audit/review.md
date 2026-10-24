# Fungal type vacuole membrane identity, compartment and source review

- Review: 20261022T014657Z-fungal-type-vacuole-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:27:43Z
- Finished UTC: 2026-10-22T01:46:57Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed in the fungal type vacuole membrane record within the explicitly bounded source scope.

## Scope And Provenance

Entire single target: exact structure identity, hierarchy, material/protein examples, organisms, source claims and all graph edges.

Selection: Target 5 of batch twenty-nine, strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000329 | data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml | maintained | fungal-type vacuole membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0000329 | Native check passed; claim-level membership assessed independently. |
| Native protein causal-graphs | passed | True | GO:0000329 | Native check passed; claim-level membership assessed independently. |
| Focused native schema | passed | True | GO:0000329 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000329 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0000329 | No expression-module dataset or inference is used. Physical compartment, protein-identity and source-localization evidence are the applicable sources. |
| Claim-level scientific review | passed | True | GO:0000329 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0000329 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0000329 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000329 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000329 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000329 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0000329 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Whole, internal volume and boundary identities

identity: supported. Targets: GO:0000329.

Exact GO identity denotes the fungal vacuole limiting membrane. Vacuolar-membrane parentage is confirmed transitively; fungal-vacuole parthood and enclosed lumen agree. Maintained neighbors retain these distinctions.

### Budding-yeast scope and source contexts

scope: supported. Targets: GO:0000329.

Species4932 is exact and Li/Kane supports the Saccharomyces example and qualitative occurrence. No new strain-specific experiment or measured population prevalence is asserted.

### Appropriately bounded constituent representation

grounding: supported. Targets: GO:0000329.

The single label-only LIPID row is collective bilayer material. ESSENTIAL describes the defining boundary constitution, not knockout proof for each chemical species. The exact V-ATPase is a graph complex, not silently inserted as lipid material.

### Storage, degradation and acidification

evidence: supported. Targets: GO:0000329.

GO0007035 and GO0016471 plus both review bodies support proton transport into the lumen by vacuolar V-ATPase. Vph1/Stv1 localization distinctions prevent treating every V-type complex as permanently vacuolar.

### Every target graph edge

graph: supported. Targets: GO:0000329.

All five NONMECHANISTIC edges are supported: membrane is-a vacuolar membrane, part-of fungal vacuole, bounds lumen, hosts vacuolar V-ATPase and supports ATPase-mediated acidification. Complex localization and activity are not relabeled as complete assembly mechanisms.

### Molecular necessity and complete inventories

evidence: unknown. Targets: GO:0000329.

Neither defining topology nor hydrolysis establishes individual molecular requirements for organelle formation. Li/Kane explicitly cautions that GFP/proteomic localization can include transient degradative cargo. Optional full constituent/transport inventories are not required for the bounded region or membrane claim.

### Full target, history and optional fields

completeness: supported. Targets: GO:0000329.

Every maintained target field and graph edge was read. No image asset, numeric physical measurement, trait link or verbatim evidence snippet is asserted in this target. Optional groundings and machinery inventories are not converted into findings. PROPOSED status, existing discussions and historical curation are retained.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml; Entire target, including history, components, sources, taxonomic examples, functions, all graph edges and discussions | context_only | Maintained record was fully read. No scientific record, status, history or generated page is edited. |
| policy | docs/CURATION.md; Structure identity, is-a/parthood, component membership and narrow evidence rules | context_only | Whole organelle, bounding bilayer and internal volume are distinct. Molecular identity and experimental membership are separate assertions. |
| protein-contract | src/cellstructuremech/schema/cellstructuremech.yaml; Component essentiality, protein_examples and ProteinExample fields | context_only | A protein example is a taxon-paired instance whose structure role needs source support. Collective boundary necessity is not a knockout claim for each lipid. |
| root29-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020020,GO:0000324,GO:0005773,GO:0000329,GO:0000328,GO:0005775,GO:0005774,GO:0007035,GO:0016471; Complete nine-term native JSON, active flags, definitions, names, synonyms and child relations | supports | All nine returned active terms were read. GO0020020 denotes the parasite food vacuole with digestive vacuole as exact synonym. GO0000324 defines the fungal vacuole and its storage/degradative functions, lists the membrane and lumen as parts, and has the recorded exact synonym. GO0000328 is an explicit child of vacuolar lumen. GO0000329/0005774 define enclosing bilayers. GO0016471 is the vacuolar V-type ATPase and GO0007035 the acidification process. |
| root29-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank, lineage | supports | Exact native ENA species identity agrees with Saccharomyces cerevisiae4932. The lookup does not measure population prevalence or establish an experimental strain. |
| root29-sources-li2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.bbamcr.2008.08.003%22; Complete selected MED bibliography and abstract; CTX duplicate excluded where present | supports | Exact native MED bibliography: PMID18786576, DOI10.1016/j.bbamcr.2008.08.003, The yeast lysosome-like vacuole: endpoint and crossroads., Li SC, Kane PM.. Explicit review article. Complete abstract describes the Saccharomyces vacuole as an acidic degradative/storage organelle; source sections separately support molecular and functional claims. |
| root29-sources-kane2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1128/MMBR.70.1.177-191.2006%22; Complete selected MED bibliography and abstract; CTX duplicate excluded where present | supports | Exact native MED bibliography: PMID16524922, DOI10.1128/mmbr.70.1.177-191.2006, The where, when, and how of organelle acidification by the yeast vacuolar H+-ATPase., Kane PM.. Explicit review article. Complete abstract treats structure, targeting, regulation and organelle acidification by the yeast V-ATPase, with original review body sections separately inspected. |
| root29-sources-GO0000329-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329/ancestors?relations=is_a; Complete native ancestors response, query relations=is_a | supports | Exact is_a ancestor response independently includes GO0005774 vacuolar membrane for GO0000329. This verifies the broader parent transitively without inventing a direct ontology edge. |
| root29-sources-li2009-numeric | https://pmc.ncbi.nlm.nih.gov/articles/2906225/; Genuine PMC2906225 review body S3/S13/S16/S20/S21; included Fig2/3 captions read, no figure pixels or underlying primary dataset reanalysis | supports | Read complete sections2.1,4.2,5.1,6.1,6.2. The review explicitly identifies soluble Pep4/CPY/Prb1 proteases, distinguishes membrane proteins and transient degradative cargo, explains endocytic/biosynthetic/autophagic routes, and documents storage of amino acids/ions/polyphosphate. It separates vacuolar Vph1-containing pumps from predominantly Golgi/endosomal Stv1 complexes. Low pH optimizes processing but is not absolutely essential for every hydrolase reaction. |
| root29-sources-kane2006-numeric | https://pmc.ncbi.nlm.nih.gov/articles/1393255/; Genuine PMC1393255 review body sec1/sec3/sec11 and Fig1 caption; no figure-pixel or current-complete-subunit audit | supports | Read complete Introduction, Structure of the Yeast V-ATPase, and Role of V0 a Subunit Isoforms in Targeting. Supports vacuolar membrane V-ATPase acidification with Vph1 versus Stv1 targeting distinction. The 2006 subunit model is historical context, not a newly asserted complete composition or all-complex localization claim. |
| neighbor-vacuolar_membrane | data/structures/membrane_organelle/vacuolar_membrane.yaml; Lines1–70 identity, hierarchy and initial source context | context_only | Named broader compartment resolves to the intended maintained record; this bounded neighbor inspection is not a full review of that separate record. |
| native-verify | /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml --verify; Entire captured native focused output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml --causal-graphs; Entire captured native focused output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/fungal_type_vacuole_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/fungal_type_vacuole_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch29-20261022-_v0k34u7/fungal_type_vacuole_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- COMMON is qualitative occurrence, not a prevalence estimate. Database identity and reference strain are distinct from experimental strain. Historical authorship, earlier reviews and closed issue dispositions are not independently recertified.
- Original PMC-prefixed URL attempts returned browser challenges despite HTTP200; only genuine numeric article responses are used for body evidence.
- Li/Kane2009 is a review, with body scope limited to2.1/4.2/5.1/6.1/6.2 and included captions. It supports bounded synthesis; underlying primary datasets and an exhaustive vacuolar proteome are not independently reanalyzed.
- Kane2006 is a review; original body scope is Introduction, structure and a-subunit targeting sections(sec1/3/11) with included caption. Historical subunit models are not promoted to a current complete composition claim.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes review bundles for every uncovered record, including honest no-finding reviews. Scientific records are unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T014657Z-fungal-type-vacuole-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Fungal type vacuole membrane identity, compartment and source review
started_at: '2026-10-22T01:27:43Z'
finished_at: '2026-10-22T01:46:57Z'
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
summary: No concrete curation defect observed in the fungal type vacuole membrane
  record within the explicitly bounded source scope.
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
  - path: data/structures/membrane_organelle/fungal_type_vacuole.yaml
    sha256: d447fe7bc41bcf0749629f12affde731c10286f9efbb170efbf81bc27b975016
    role: context
  - path: data/structures/membrane_organelle/fungal_type_vacuole_lumen.yaml
    sha256: ef0fef76aaa4813b13015b2fc8b1029f479aa1b997e96a1d7d13950e355eb3aa
    role: context
  - path: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    sha256: 2436643a28b07f28373a3c9d61360377b61b5e8803b0b6bef5b44ec32f1bfc51
    role: target
  - path: data/structures/membrane_organelle/vacuolar_membrane.yaml
    sha256: 89c3bb9baf5507b45606c975ff1bb6ef8d705601ce44bc7e4c3d72572b5f36e0
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
- target_id: GO:0000329
  path: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  label: fungal-type vacuole membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target: exact structure identity, hierarchy, material/protein
    examples, organisms, source claims and all graph edges.'
  selection: Target 5 of batch twenty-nine, strict uncovered path order from fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000329
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --verify
  exit_code: 0
  summary: Native check passed; claim-level membership assessed independently.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Native check passed; claim-level membership assessed independently.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: just validate data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: just validate-strict data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/fungal_type_vacuole_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0000329
  summary: No expression-module dataset or inference is used. Physical compartment,
    protein-identity and source-localization evidence are the applicable sources.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000329
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - protein-contract
  - root29-sources-go
  - root29-sources-tax4932
  - root29-sources-li2009-meta
  - root29-sources-kane2006-meta
  - root29-sources-GO0000329-ancestors
  - root29-sources-li2009-numeric
  - root29-sources-kane2006-numeric
  - neighbor-vacuolar_membrane
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0000329
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
  - GO:0000329
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0000329
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0000329
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
    and current batch29 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  locator: Entire target, including history, components, sources, taxonomic examples,
    functions, all graph edges and discussions
  accessed_at: '2026-10-22T01:35:18Z'
  support: context_only
  summary: Maintained record was fully read. No scientific record, status, history
    or generated page is edited.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Structure identity, is-a/parthood, component membership and narrow evidence
    rules
  accessed_at: '2026-10-22T01:35:18Z'
  support: context_only
  summary: Whole organelle, bounding bilayer and internal volume are distinct. Molecular
    identity and experimental membership are separate assertions.
- evidence_id: protein-contract
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component essentiality, protein_examples and ProteinExample fields
  accessed_at: '2026-10-22T01:35:18Z'
  support: context_only
  summary: A protein example is a taxon-paired instance whose structure role needs
    source support. Collective boundary necessity is not a knockout claim for each
    lipid.
- evidence_id: root29-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020020,GO:0000324,GO:0005773,GO:0000329,GO:0000328,GO:0005775,GO:0005774,GO:0007035,GO:0016471
  locator: Complete nine-term native JSON, active flags, definitions, names, synonyms
    and child relations
  accessed_at: '2026-10-22T01:31:20.164017Z'
  support: supports
  summary: All nine returned active terms were read. GO0020020 denotes the parasite
    food vacuole with digestive vacuole as exact synonym. GO0000324 defines the fungal
    vacuole and its storage/degradative functions, lists the membrane and lumen as
    parts, and has the recorded exact synonym. GO0000328 is an explicit child of vacuolar
    lumen. GO0000329/0005774 define enclosing bilayers. GO0016471 is the vacuolar
    V-type ATPase and GO0007035 the acidification process.
  snapshot_sha256: 75c75e7439d99f4454531b07a1ea3feed59890a6d8820542801a054d23e7d639
- evidence_id: root29-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank, lineage
  accessed_at: '2026-10-22T01:10:58.502766Z'
  support: supports
  summary: Exact native ENA species identity agrees with Saccharomyces cerevisiae4932.
    The lookup does not measure population prevalence or establish an experimental
    strain.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root29-sources-li2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.bbamcr.2008.08.003%22
  locator: Complete selected MED bibliography and abstract; CTX duplicate excluded
    where present
  accessed_at: '2026-10-22T01:31:22.508649Z'
  support: supports
  summary: 'Exact native MED bibliography: PMID18786576, DOI10.1016/j.bbamcr.2008.08.003,
    The yeast lysosome-like vacuole: endpoint and crossroads., Li SC, Kane PM.. Explicit
    review article. Complete abstract describes the Saccharomyces vacuole as an acidic
    degradative/storage organelle; source sections separately support molecular and
    functional claims.'
  snapshot_sha256: a80dfab6ca988c4f031b90afb9ca5816e91805513281ba402d81aad11ac0142e
- evidence_id: root29-sources-kane2006-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1128/MMBR.70.1.177-191.2006%22
  locator: Complete selected MED bibliography and abstract; CTX duplicate excluded
    where present
  accessed_at: '2026-10-22T01:31:22.576024Z'
  support: supports
  summary: 'Exact native MED bibliography: PMID16524922, DOI10.1128/mmbr.70.1.177-191.2006,
    The where, when, and how of organelle acidification by the yeast vacuolar H+-ATPase.,
    Kane PM.. Explicit review article. Complete abstract treats structure, targeting,
    regulation and organelle acidification by the yeast V-ATPase, with original review
    body sections separately inspected.'
  snapshot_sha256: 61b77e1e74943bfce906bd49ed525db7b02ead05cea30b802740df4dcbdf1ed4
- evidence_id: root29-sources-GO0000329-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000329/ancestors?relations=is_a
  locator: Complete native ancestors response, query relations=is_a
  accessed_at: '2026-10-22T01:31:56.650420Z'
  support: supports
  summary: Exact is_a ancestor response independently includes GO0005774 vacuolar
    membrane for GO0000329. This verifies the broader parent transitively without
    inventing a direct ontology edge.
  snapshot_sha256: 284018be139505e9831a1934d7d7b076c3d809976816de14d5364eac78add038
- evidence_id: root29-sources-li2009-numeric
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/2906225/
  locator: Genuine PMC2906225 review body S3/S13/S16/S20/S21; included Fig2/3 captions
    read, no figure pixels or underlying primary dataset reanalysis
  accessed_at: '2026-10-22T01:32:07.202194Z'
  support: supports
  summary: Read complete sections2.1,4.2,5.1,6.1,6.2. The review explicitly identifies
    soluble Pep4/CPY/Prb1 proteases, distinguishes membrane proteins and transient
    degradative cargo, explains endocytic/biosynthetic/autophagic routes, and documents
    storage of amino acids/ions/polyphosphate. It separates vacuolar Vph1-containing
    pumps from predominantly Golgi/endosomal Stv1 complexes. Low pH optimizes processing
    but is not absolutely essential for every hydrolase reaction.
  snapshot_sha256: 949eb84ba53fa6400a1c205d2459f909e323b5f8eeb58e3672234730830c256b
- evidence_id: root29-sources-kane2006-numeric
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/1393255/
  locator: Genuine PMC1393255 review body sec1/sec3/sec11 and Fig1 caption; no figure-pixel
    or current-complete-subunit audit
  accessed_at: '2026-10-22T01:32:07.202322Z'
  support: supports
  summary: Read complete Introduction, Structure of the Yeast V-ATPase, and Role of
    V0 a Subunit Isoforms in Targeting. Supports vacuolar membrane V-ATPase acidification
    with Vph1 versus Stv1 targeting distinction. The 2006 subunit model is historical
    context, not a newly asserted complete composition or all-complex localization
    claim.
  snapshot_sha256: 20b0e18976d5c76dee0ae4e1d58559f54fa8e2b6409bc902ac708c5e1654e1bd
- evidence_id: neighbor-vacuolar_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/vacuolar_membrane.yaml
  locator: Lines1–70 identity, hierarchy and initial source context
  accessed_at: '2026-10-22T01:35:18Z'
  support: context_only
  summary: Named broader compartment resolves to the intended maintained record; this
    bounded neighbor inspection is not a full review of that separate record.
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --verify
  locator: Entire captured native focused output
  accessed_at: '2026-10-22T01:31:28.809868Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --causal-graphs
  locator: Entire captured native focused output
  accessed_at: '2026-10-22T01:31:29.362611Z'
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
  reference: just validate data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:27:45Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml'
  snapshot_sha256: 897096f5415f2ecd739008e377c63f2dbdde7ffedb2762c3b4749e8e142cf9e8
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml
    --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/fungal_type_vacuole_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:27:46Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch29-20261022-_v0k34u7/fungal_type_vacuole_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch29-20261022-_v0k34u7/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch29-20261022-_v0k34u7/fungal_type_vacuole_membrane-strict.tsv"
  snapshot_sha256: ad703c4e1640904dd212e378f7cf07e18657943d3f2f018214d132967238a42a
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/fungal_type_vacuole_membrane.yaml; native
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
  topic: Whole, internal volume and boundary identities
  outcome: supported
  target_ids:
  - GO:0000329
  summary: Exact GO identity denotes the fungal vacuole limiting membrane. Vacuolar-membrane
    parentage is confirmed transitively; fungal-vacuole parthood and enclosed lumen
    agree. Maintained neighbors retain these distinctions.
  evidence_ids:
  - record
  - root29-sources-go
  - policy
  - root29-sources-GO0000329-ancestors
  - root29-sources-li2009-numeric
  - root29-sources-kane2006-numeric
- assessment_id: scope
  area: scope
  topic: Budding-yeast scope and source contexts
  outcome: supported
  target_ids:
  - GO:0000329
  summary: Species4932 is exact and Li/Kane supports the Saccharomyces example and
    qualitative occurrence. No new strain-specific experiment or measured population
    prevalence is asserted.
  evidence_ids:
  - record
  - root29-sources-tax4932
  - root29-sources-li2009-meta
  - root29-sources-kane2006-meta
  - root29-sources-GO0000329-ancestors
  - root29-sources-li2009-numeric
  - root29-sources-kane2006-numeric
- assessment_id: composition
  area: grounding
  topic: Appropriately bounded constituent representation
  outcome: supported
  target_ids:
  - GO:0000329
  summary: The single label-only LIPID row is collective bilayer material. ESSENTIAL
    describes the defining boundary constitution, not knockout proof for each chemical
    species. The exact V-ATPase is a graph complex, not silently inserted as lipid
    material.
  evidence_ids:
  - record
  - root29-sources-go
  - protein-contract
  - root29-sources-GO0000329-ancestors
  - root29-sources-li2009-numeric
  - root29-sources-kane2006-numeric
- assessment_id: function
  area: evidence
  topic: Storage, degradation and acidification
  outcome: supported
  target_ids:
  - GO:0000329
  summary: GO0007035 and GO0016471 plus both review bodies support proton transport
    into the lumen by vacuolar V-ATPase. Vph1/Stv1 localization distinctions prevent
    treating every V-type complex as permanently vacuolar.
  evidence_ids:
  - record
  - root29-sources-go
  - root29-sources-GO0000329-ancestors
  - root29-sources-li2009-numeric
  - root29-sources-kane2006-numeric
- assessment_id: graph
  area: graph
  topic: Every target graph edge
  outcome: supported
  target_ids:
  - GO:0000329
  summary: 'All five NONMECHANISTIC edges are supported: membrane is-a vacuolar membrane,
    part-of fungal vacuole, bounds lumen, hosts vacuolar V-ATPase and supports ATPase-mediated
    acidification. Complex localization and activity are not relabeled as complete
    assembly mechanisms.'
  evidence_ids:
  - record
  - root29-sources-go
  - root29-sources-GO0000329-ancestors
  - root29-sources-li2009-numeric
  - root29-sources-kane2006-numeric
- assessment_id: limits
  area: evidence
  topic: Molecular necessity and complete inventories
  outcome: unknown
  target_ids:
  - GO:0000329
  summary: Neither defining topology nor hydrolysis establishes individual molecular
    requirements for organelle formation. Li/Kane explicitly cautions that GFP/proteomic
    localization can include transient degradative cargo. Optional full constituent/transport
    inventories are not required for the bounded region or membrane claim.
  evidence_ids:
  - record
  - root29-sources-go
  - protein-contract
  - root29-sources-GO0000329-ancestors
  - root29-sources-li2009-numeric
  - root29-sources-kane2006-numeric
- assessment_id: coverage
  area: completeness
  topic: Full target, history and optional fields
  outcome: supported
  target_ids:
  - GO:0000329
  summary: Every maintained target field and graph edge was read. No image asset,
    numeric physical measurement, trait link or verbatim evidence snippet is asserted
    in this target. Optional groundings and machinery inventories are not converted
    into findings. PROPOSED status, existing discussions and historical curation are
    retained.
  evidence_ids:
  - record
  - policy
  - root29-sources-go
  - root29-sources-li2009-meta
  - root29-sources-kane2006-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- COMMON is qualitative occurrence, not a prevalence estimate. Database identity and
  reference strain are distinct from experimental strain. Historical authorship, earlier
  reviews and closed issue dispositions are not independently recertified.
- Original PMC-prefixed URL attempts returned browser challenges despite HTTP200;
  only genuine numeric article responses are used for body evidence.
- Li/Kane2009 is a review, with body scope limited to2.1/4.2/5.1/6.1/6.2 and included
  captions. It supports bounded synthesis; underlying primary datasets and an exhaustive
  vacuolar proteome are not independently reanalyzed.
- Kane2006 is a review; original body scope is Introduction, structure and a-subunit
  targeting sections(sec1/3/11) with included caption. Historical subunit models are
  not promoted to a current complete composition claim.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes review bundles for every uncovered record, including
  honest no-finding reviews. Scientific records are unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
