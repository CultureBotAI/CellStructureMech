# Polaroplast scientific review

- Review: 20261022T033000Z-polaroplast-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:14:07Z
- Finished UTC: 2026-10-22T03:30:00Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact polaroplast identity, qualitative taxon scope, membrane-array morphology and a coarse membrane-contribution graph are supported within explicit review and primary-study limits. No concrete curation finding.

## Scope And Provenance

Entire single target including every component, hierarchy, taxon/example, function/graph, source, discussion and history. Additional frozen local inputs are read at the precise scope declared in their evidence rows; literature read extents and image inspection are separately stated.

Selection: Batch39 exact path-ordered target 6; fresh f97b native inspection/schema/strict passed before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0160201 | data/structures/membrane_organelle/polaroplast.yaml | maintained | polaroplast |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0160201 | Focused validator passed. |
| Focused native strict | passed | True | GO:0160201 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0160201 | Native check passed; exact scientific scope was assessed separately. |
| Individual protein verification applicability | not_applicable | False | GO:0160201 | No individual protein accession or gene/protein graph node occurs in the target. |
| Expression-module applicability | not_applicable | False | GO:0160201 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | GO:0160201 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0160201 | 7 of 7 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0160201 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0160201 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0160201 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0160201 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0160201 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Polaroplast and polar-tube boundary

identity: supported. Targets: GO:0160201.

Exact ontology identity, category and declared definition are supported. The polaroplast is the spore membrane apparatus, distinguished from the polar-tube conduit and the eventual sporoplasm membrane.

### Membrane arrays and regional labels

grounding: supported. Targets: GO:0160201.

The three reviewed-label-only LIPID rows describe aggregate membrane material and anterior lamellar/posterior tubular arrangements. They do not falsely assign whole-organelle GO identities as chemical groundings or claim three separate biochemical substances. Exact lipids and transport proteins remain open; regional overlap is a morphological description, not a stoichiometric inventory.

### Individual formation requirements

evidence: unknown. Targets: GO:0160201.

No explicit component essentiality is asserted. Microscopy and protein localization do not determine whether individual named molecular classes are required for assembly. The unresolved machinery discussion remains warranted.

### Microsporidian context and Nosema experiment

scope: supported. Targets: GO:0160201.

The review supports common qualitative occurrence in microsporidian spores, while the primary membrane-contribution evidence is specifically N. bombycis CQ1 under the reported induction/preparation conditions. COMMON is not a numerical census. The species example does not imply all lineages share every experimental detail.

### Source-bounded membrane contribution

graph: supported. Targets: GO:0160201.

Firing-associated membrane rearrangement and contribution to the sporoplasm membrane are supported at the stated coarse NONMECHANISTIC resolution. The contribution wording preserves a partial membrane-source interpretation; tracked/visualized language is read as the study combination of staged observations and markers, not direct continuous tracking of every membrane molecule. The source does not establish unique protein identity, force generation or obligatory causation.

### Bounded source audit and unchanged status

provenance: supported. Targets: GO:0160201.

All target claims were reviewed at the declared source read scopes, with primary/secondary/abstract/native authority tiers separated. No scientific mutation, mapping-status promotion, review persistence or publication is implied.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/polaroplast.yaml; Entire maintained YAML including all fields, graphs, history and discussions | context_only | The entire target was read; scientific content, status and history remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent type/grounding/formation-necessity and graph/component_ref contracts | context_only | A LIPID molecular constituent is distinct from a complete GO membrane structure. Accurate OTHER structural constituents are not categorically forbidden. Constitution, localization, regulatory activity and cell viability do not establish individual formation necessity. |
| polaroplast-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160201,GO:0044099; Complete two native term identities and definitions | supports | GO0160201 is active and defines the microsporidian polaroplast with water swelling, pressure and polar-tube eversion; GO0044099 identifies the invasion polar tube. The maintained definition is a shortened faithful rendering of its declared ontology source. |
| polaroplast-agent-tax6029 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/6029; Complete native taxId/name/rank/lineage | supports | ENA6029 confirms Microsporidia at phylum rank; this is identity, not an abundance measurement. |
| polaroplast-agent-tax27978 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/27978; Complete native taxId/name/rank/lineage | supports | ENA27978 confirms Nosema bombycis at species rank; it does not identify an experimental strain by itself. |
| polaroplast-agent-han2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1007/978-3-030-93306-7_8%22; Unique complete MED identity/title/authors/DOI/year and abstract | supports | Han, Takvorian and Weiss2022 chapter, DOI10.1007/978-3-030-93306-7_8/PMID35544004, is a review of the polar tube. |
| polaroplast-agent-chen2023-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1186/s13071-023-05908-9%22; Unique complete MED identity/title/authors/DOI/year and abstract | supports | Chen et al.2023, DOI10.1186/s13071-023-05908-9/PMID37649053, is a review of polar-tube origin, structure, composition and function. |
| polaroplast-agent-lv2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1128/mbio.02749-23%22; Unique complete MED identity/title/authors/DOI/year and abstract | supports | Lv et al.2024, DOI10.1128/mbio.02749-23/PMID38193684, is the primary Nosema polaroplast/sporoplasm study. |
| polaroplast-agent-han2022-legacy | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10037675/; Genuine PMC10037675 HTML: complete Introduction S1 and Structure/Germination S2, including Figures8.1–8.6 captions; no pixels, other sections or underlying cited experiments independently certified. | supports | The review describes packed anterior lamellar membranes and flattened tubules, posterior polaroplast context and membrane rearrangements during germination. It reviews imaging and hypotheses about the invasion apparatus; it is not an independent species-wide pressure or molecular-necessity experiment. |
| polaroplast-agent-chen2023-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10468886/fullTextXML; Genuine PMC10468886 JATS: complete Sec3 Structure and Sec5 Function with embedded captions; primary studies cited within the review were not independently audited. | supports | The review places the polar tube/manubrium and anchoring disk in their surrounding polaroplast context and describes cargo passage during invasion. It does not supply an exact source-neutral polaroplast lipid species or establish an obligatory transport protein inventory. |
| polaroplast-agent-lv2024-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10865828/fullTextXML; Genuine PMC10865828 JATS: complete Introduction s1, all Results s2 and Figure1–8 captions, Discussion s3 and Methods s4; 0.1M KOH induction, CQ1/silkworm propagation, BmE culture, fluorescence/electron microscopy, protein/lipid analyses and statistics read. No figure pixels or supplementary datasets inspected. | supports | In N. bombycis CQ1, the authors combine induced germination, fixed fluorescence stages, TEM/cryoEM, membrane dyes and protein localization with a model of polaroplast-derived membrane contribution to sporoplasm formation. Existing plasma membrane/posterior-vacuole material remains in empty coats. The membrane-origin interpretation combines observations and inference; it is not continuous single-membrane lineage tracing or a loss-of-function necessity test. |
| schema-result | just validate data/structures/membrane_organelle/polaroplast.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/polaroplast.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/polaroplast.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/polaroplast-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/polaroplast.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/polaroplast-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/polaroplast-strict.tsv |
| polaroplast-causal-graphs | /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/polaroplast.yaml; Complete native read-only log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/polaroplast.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 7 of 7 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Han2022 and Chen2023 are reviews, inspected only at the declared sections. Their cited underlying experiments were not independently re-audited.
- Lv2024 was read through complete main science and Methods, but no figure pixels or supplementary datasets were inspected. Its model combines staged fixed observations and markers; continuous lineage tracing, exclusive membrane origin and universal transfer kinetics are not certified.
- The water-pressure wording matches GO0160201; this review did not independently reproduce or resolve the physical pressure mechanism. Exact lipid species, family groundings and experimental individual assembly necessity remain unresolved without making the optional inventory a defect.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes honest clean reviews; no issue was invented for the local issue-only convention. Parent owns finalization, persistence and integration of the five same-base full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T033000Z-polaroplast-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Polaroplast scientific review
started_at: '2026-10-22T03:14:07Z'
finished_at: '2026-10-22T03:30:00Z'
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
summary: Exact polaroplast identity, qualitative taxon scope, membrane-array morphology
  and a coarse membrane-contribution graph are supported within explicit review and
  primary-study limits. No concrete curation finding.
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
  - path: data/structures/membrane_organelle/polaroplast.yaml
    sha256: b755d59c2ad21e4b73e222a7d9979859a4d4b5c3c9f4543f9695dc3749beff69
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
- target_id: GO:0160201
  path: data/structures/membrane_organelle/polaroplast.yaml
  label: polaroplast
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/polaroplast.yaml
    role: maintained scientific record
scope:
  description: Entire single target including every component, hierarchy, taxon/example,
    function/graph, source, discussion and history. Additional frozen local inputs
    are read at the precise scope declared in their evidence rows; literature read
    extents and image inspection are separately stated.
  selection: Batch39 exact path-ordered target 6; fresh f97b native inspection/schema/strict
    passed before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0160201
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: just validate data/structures/membrane_organelle/polaroplast.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: just validate-strict data/structures/membrane_organelle/polaroplast.yaml
    --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/polaroplast-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/polaroplast.yaml
  exit_code: 0
  summary: Native check passed; exact scientific scope was assessed separately.
  evidence_ids:
  - polaroplast-causal-graphs
- check_id: protein-applicability
  name: Individual protein verification applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0160201
  summary: No individual protein accession or gene/protein graph node occurs in the
    target.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0160201
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0160201
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - polaroplast-agent-go
  - polaroplast-agent-tax6029
  - polaroplast-agent-tax27978
  - polaroplast-agent-han2022-meta
  - polaroplast-agent-chen2023-meta
  - polaroplast-agent-lv2024-meta
  - polaroplast-agent-han2022-legacy
  - polaroplast-agent-chen2023-jats
  - polaroplast-agent-lv2024-jats
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0160201
  summary: 7 of 7 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0160201
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0160201
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
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/polaroplast.yaml
  locator: Entire maintained YAML including all fields, graphs, history and discussions
  accessed_at: '2026-10-22T03:22:24Z'
  support: context_only
  summary: The entire target was read; scientific content, status and history remain
    unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent type/grounding/formation-necessity and graph/component_ref
    contracts
  accessed_at: '2026-10-22T03:22:24Z'
  support: context_only
  summary: A LIPID molecular constituent is distinct from a complete GO membrane structure.
    Accurate OTHER structural constituents are not categorically forbidden. Constitution,
    localization, regulatory activity and cell viability do not establish individual
    formation necessity.
- evidence_id: polaroplast-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160201,GO:0044099
  locator: Complete two native term identities and definitions
  accessed_at: '2026-10-22T03:15:33.388650Z'
  support: supports
  summary: GO0160201 is active and defines the microsporidian polaroplast with water
    swelling, pressure and polar-tube eversion; GO0044099 identifies the invasion
    polar tube. The maintained definition is a shortened faithful rendering of its
    declared ontology source.
  snapshot_sha256: 33880b6c13718a1e49c55ee674c90904b1ae7e406c9bdbc993da61f23951e8e0
- evidence_id: polaroplast-agent-tax6029
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/6029
  locator: Complete native taxId/name/rank/lineage
  accessed_at: '2026-10-22T03:15:33.389017Z'
  support: supports
  summary: ENA6029 confirms Microsporidia at phylum rank; this is identity, not an
    abundance measurement.
  snapshot_sha256: 276e5512241f66f7653cac525bfb083cb1ee20aedc2f7e46d8aaa5a2ec0a10f9
- evidence_id: polaroplast-agent-tax27978
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/27978
  locator: Complete native taxId/name/rank/lineage
  accessed_at: '2026-10-22T03:15:33.389276Z'
  support: supports
  summary: ENA27978 confirms Nosema bombycis at species rank; it does not identify
    an experimental strain by itself.
  snapshot_sha256: bd776284e072d75d566a4f14a4e4007db6c95e30f0b23fddef3d95e1763b3016
- evidence_id: polaroplast-agent-han2022-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1007/978-3-030-93306-7_8%22
  locator: Unique complete MED identity/title/authors/DOI/year and abstract
  accessed_at: '2026-10-22T03:15:33.389200Z'
  support: supports
  summary: Han, Takvorian and Weiss2022 chapter, DOI10.1007/978-3-030-93306-7_8/PMID35544004,
    is a review of the polar tube.
  snapshot_sha256: 0390b8d8164deffcbd199b35b042c07850d444a0028fea93153064874694c400
- evidence_id: polaroplast-agent-chen2023-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1186/s13071-023-05908-9%22
  locator: Unique complete MED identity/title/authors/DOI/year and abstract
  accessed_at: '2026-10-22T03:15:33.389337Z'
  support: supports
  summary: Chen et al.2023, DOI10.1186/s13071-023-05908-9/PMID37649053, is a review
    of polar-tube origin, structure, composition and function.
  snapshot_sha256: 845a1e49ad4a2e11a5ecd16e13fa5cc506511b286497fbe2293179e1c20665e7
- evidence_id: polaroplast-agent-lv2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1128/mbio.02749-23%22
  locator: Unique complete MED identity/title/authors/DOI/year and abstract
  accessed_at: '2026-10-22T03:15:34.100757Z'
  support: supports
  summary: Lv et al.2024, DOI10.1128/mbio.02749-23/PMID38193684, is the primary Nosema
    polaroplast/sporoplasm study.
  snapshot_sha256: 1bfef6da448310148f6144530064c6469a5b9093cb089a79064f883f96d2c222
- evidence_id: polaroplast-agent-han2022-legacy
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC10037675/
  locator: 'Genuine PMC10037675 HTML: complete Introduction S1 and Structure/Germination
    S2, including Figures8.1–8.6 captions; no pixels, other sections or underlying
    cited experiments independently certified.'
  accessed_at: '2026-10-22T03:16:04.203735Z'
  support: supports
  summary: The review describes packed anterior lamellar membranes and flattened tubules,
    posterior polaroplast context and membrane rearrangements during germination.
    It reviews imaging and hypotheses about the invasion apparatus; it is not an independent
    species-wide pressure or molecular-necessity experiment.
  snapshot_sha256: 391685539c08729999e363eeac8e0acc7bcca713c6607239cadeeddae682e3e3
- evidence_id: polaroplast-agent-chen2023-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10468886/fullTextXML
  locator: 'Genuine PMC10468886 JATS: complete Sec3 Structure and Sec5 Function with
    embedded captions; primary studies cited within the review were not independently
    audited.'
  accessed_at: '2026-10-22T03:16:04.212105Z'
  support: supports
  summary: The review places the polar tube/manubrium and anchoring disk in their
    surrounding polaroplast context and describes cargo passage during invasion. It
    does not supply an exact source-neutral polaroplast lipid species or establish
    an obligatory transport protein inventory.
  snapshot_sha256: 106e5478ad73978851583f4ccfe5c4567073dcd0711da0225d8158d07ac4db21
- evidence_id: polaroplast-agent-lv2024-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC10865828/fullTextXML
  locator: 'Genuine PMC10865828 JATS: complete Introduction s1, all Results s2 and
    Figure1–8 captions, Discussion s3 and Methods s4; 0.1M KOH induction, CQ1/silkworm
    propagation, BmE culture, fluorescence/electron microscopy, protein/lipid analyses
    and statistics read. No figure pixels or supplementary datasets inspected.'
  accessed_at: '2026-10-22T03:16:04.213433Z'
  support: supports
  summary: In N. bombycis CQ1, the authors combine induced germination, fixed fluorescence
    stages, TEM/cryoEM, membrane dyes and protein localization with a model of polaroplast-derived
    membrane contribution to sporoplasm formation. Existing plasma membrane/posterior-vacuole
    material remains in empty coats. The membrane-origin interpretation combines observations
    and inference; it is not continuous single-membrane lineage tracing or a loss-of-function
    necessity test.
  snapshot_sha256: 4bead1cf30701d71d7acecb84ec49b99f077edc6866f7c0b59f15d563e71dc58
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/polaroplast.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:14:08Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/polaroplast.yaml'
  snapshot_sha256: ad3cc287c9c085e1c6e42d68f273616ba75cb19bc14ffc277bf5dbdf644531bb
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/polaroplast.yaml
    --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/polaroplast-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:14:09Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/polaroplast.yaml\
    \ --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/polaroplast-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/polaroplast-strict.tsv"
  snapshot_sha256: 360332355a23d2f02c047b64c617085c183c2fe226bf6582fe1943607bdeae87
- evidence_id: polaroplast-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/polaroplast.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T03:20:18.778393Z'
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
  locator: data/structures/membrane_organelle/polaroplast.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 7 of 7 collected target identifiers returned OK. No residuals. Native source
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
  topic: Polaroplast and polar-tube boundary
  outcome: supported
  target_ids:
  - GO:0160201
  summary: Exact ontology identity, category and declared definition are supported.
    The polaroplast is the spore membrane apparatus, distinguished from the polar-tube
    conduit and the eventual sporoplasm membrane.
  evidence_ids:
  - record
  - polaroplast-agent-go
  - polaroplast-agent-han2022-legacy
- assessment_id: composition
  area: grounding
  topic: Membrane arrays and regional labels
  outcome: supported
  target_ids:
  - GO:0160201
  summary: The three reviewed-label-only LIPID rows describe aggregate membrane material
    and anterior lamellar/posterior tubular arrangements. They do not falsely assign
    whole-organelle GO identities as chemical groundings or claim three separate biochemical
    substances. Exact lipids and transport proteins remain open; regional overlap
    is a morphological description, not a stoichiometric inventory.
  evidence_ids:
  - record
  - schema
  - polaroplast-agent-han2022-legacy
  - polaroplast-agent-lv2024-jats
- assessment_id: necessity
  area: evidence
  topic: Individual formation requirements
  outcome: unknown
  target_ids:
  - GO:0160201
  summary: No explicit component essentiality is asserted. Microscopy and protein
    localization do not determine whether individual named molecular classes are required
    for assembly. The unresolved machinery discussion remains warranted.
  evidence_ids:
  - record
  - schema
  - polaroplast-agent-lv2024-jats
- assessment_id: scope
  area: scope
  topic: Microsporidian context and Nosema experiment
  outcome: supported
  target_ids:
  - GO:0160201
  summary: The review supports common qualitative occurrence in microsporidian spores,
    while the primary membrane-contribution evidence is specifically N. bombycis CQ1
    under the reported induction/preparation conditions. COMMON is not a numerical
    census. The species example does not imply all lineages share every experimental
    detail.
  evidence_ids:
  - record
  - polaroplast-agent-go
  - polaroplast-agent-tax6029
  - polaroplast-agent-tax27978
  - polaroplast-agent-han2022-legacy
  - polaroplast-agent-lv2024-jats
- assessment_id: function-graph
  area: graph
  topic: Source-bounded membrane contribution
  outcome: supported
  target_ids:
  - GO:0160201
  summary: Firing-associated membrane rearrangement and contribution to the sporoplasm
    membrane are supported at the stated coarse NONMECHANISTIC resolution. The contribution
    wording preserves a partial membrane-source interpretation; tracked/visualized
    language is read as the study combination of staged observations and markers,
    not direct continuous tracking of every membrane molecule. The source does not
    establish unique protein identity, force generation or obligatory causation.
  evidence_ids:
  - record
  - polaroplast-agent-go
  - polaroplast-agent-han2022-legacy
  - polaroplast-agent-chen2023-jats
  - polaroplast-agent-lv2024-jats
- assessment_id: provenance
  area: provenance
  topic: Bounded source audit and unchanged status
  outcome: supported
  target_ids:
  - GO:0160201
  summary: All target claims were reviewed at the declared source read scopes, with
    primary/secondary/abstract/native authority tiers separated. No scientific mutation,
    mapping-status promotion, review persistence or publication is implied.
  evidence_ids:
  - record
  - polaroplast-agent-go
  - polaroplast-agent-tax6029
  - polaroplast-agent-tax27978
  - polaroplast-agent-han2022-meta
  - polaroplast-agent-chen2023-meta
  - polaroplast-agent-lv2024-meta
  - polaroplast-agent-han2022-legacy
  - polaroplast-agent-chen2023-jats
  - polaroplast-agent-lv2024-jats
findings: []
actions: []
limitations:
- Han2022 and Chen2023 are reviews, inspected only at the declared sections. Their
  cited underlying experiments were not independently re-audited.
- Lv2024 was read through complete main science and Methods, but no figure pixels
  or supplementary datasets were inspected. Its model combines staged fixed observations
  and markers; continuous lineage tracing, exclusive membrane origin and universal
  transfer kinetics are not certified.
- The water-pressure wording matches GO0160201; this review did not independently
  reproduce or resolve the physical pressure mechanism. Exact lipid species, family
  groundings and experimental individual assembly necessity remain unresolved without
  making the optional inventory a defect.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes honest clean reviews; no issue was invented for
  the local issue-only convention. Parent owns finalization, persistence and integration
  of the five same-base full-corpus gates.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
