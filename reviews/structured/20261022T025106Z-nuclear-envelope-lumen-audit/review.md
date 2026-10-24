# Nuclear envelope lumen scientific review

- Review: 20261022T025106Z-nuclear-envelope-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:36:25Z
- Finished UTC: 2026-10-22T02:51:06Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The perinuclear-lumen identity, exact synonym, hierarchy, ER continuity and boundary-only graph are supported. No concrete curation finding was established within the inspected source scope.

## Scope And Provenance

Entire target within the four-record nuclear-envelope boundary set (target plus three neighbors); definitions, hierarchy, components, taxon/examples, functions, every directed edge, discussions, exact authorities and declared source body/supplement scopes.

Selection: Batch35 target 3; exact native inspection and focused schema/strict gates passed before assessment at unchanged f97b1abe.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005641 | data/structures/membrane_organelle/nuclear_envelope_lumen.yaml | maintained | nuclear envelope lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005641 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005641 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005641 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Protein-instance applicability | not_applicable | False | GO:0005641 | No individual protein_examples or accession-bearing GENE_OR_PROTEIN nodes occur in this target; exact NPC GO identity is checked directly where asserted. |
| Claim-level scientific review | passed | True | GO:0005641 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005641 | 8 of 8 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005641 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005641 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005641 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005641 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005641 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Perinuclear volume rather than nuclear interior

identity: supported. Targets: GO:0005641.

GO0005641 exactly denotes the region between envelope bilayers. Native GO0031970 children confirm organelle-envelope-lumen ancestry; GO0005635 contains it. Perinuclear space is an exact native synonym and is independently used by Hetzer.

### Four descriptive boundary and continuity edges

graph: supported. Targets: GO:0005641.

The NONMECHANISTIC graph distinguishes the volume from the inner/outer bounding bilayers and links the perinuclear volume to the ER lumen. Hetzer Figure1 caption and ER-continuity text support this; the region is not equated with the nucleoplasm or assigned an autonomous transport mechanism.

### Boundary membranes are not lumen constituents

grounding: supported. Targets: GO:0005641.

The resolved boundary discussion correctly leaves the two bordering membranes outside the lumen component list. No molecular constituent, essentiality, canonical strain or mandatory inventory is asserted.

### Broad eukaryotic occurrence

scope: supported. Targets: GO:0005641.

Native2759 identifies Eukaryota. Review context supports a perinuclear lumen in the double-envelope organization, without implying an intact nuclear envelope throughout every cell-cycle phase or quantifying prevalence.

### Source tier, currentness and review limits

evidence: supported. Targets: GO:0005641.

All target citation identities and native term/protein identities were checked. Relevant primary or review body passages were read within the declared locators. Historical discussions are interpreted in their recorded context, with only concrete current contradictions flagged. No scientific promotion or corpus edit is implied.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/nuclear_envelope_lumen.yaml; Entire maintained YAML, including history, evidence, all directed edges and discussions | context_only | The complete target was independently read. Maintained scientific content and status remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent lines391–444; CausalNode lines843–875; component types1044–1057 | context_only | Molecular lipid identity differs from a complete membrane. GO can ground a protein subcomplex; CHEBI is the stated lipid grounding route. Essentiality denotes formation necessity. Node xrefs can link instances without claiming complete cohort coverage. |
| neighbor-nuclear_envelope | data/structures/membrane_organelle/nuclear_envelope.yaml; Complete maintained nuclear-envelope boundary neighbor | context_only | Exact adjacent record read and frozen for topology and representation context; maintained context is not independent experimental evidence. |
| neighbor-nuclear_inner_membrane | data/structures/membrane_organelle/nuclear_inner_membrane.yaml; Complete maintained nuclear-envelope boundary neighbor | context_only | Exact adjacent record read and frozen for topology and representation context; maintained context is not independent experimental evidence. |
| neighbor-nuclear_outer_membrane | data/structures/membrane_organelle/nuclear_outer_membrane.yaml; Complete maintained nuclear-envelope boundary neighbor | context_only | Exact adjacent record read and frozen for topology and representation context; maintained context is not independent experimental evidence. |
| nuclear-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005635,GO%3A0031967,GO%3A0005634,GO%3A0005637,GO%3A0005640,GO%3A0005641,GO%3A0005643,GO%3A0006913,GO%3A0006998,GO%3A0031970,GO%3A0005788,GO%3A0031090,GO%3A0005774; Complete13 requested native term results: exact IDs, definitions, synonyms, active flags and returned child relations | supports | All13 active native terms were inspected. The definitions distinguish envelope, nucleus, inner/outer bilayers, perinuclear lumen, NPC, ER lumen and vacuolar membrane. Returned children directly support envelope is_a organelle envelope, lumen is_a organelle envelope lumen, and envelope part_of nucleus. GO0005635 exactly supplies the maintained definition, including its20–40nm range and lamina clause; this is ontology wording, not a new universal measurement. |
| nuclear-agent-membrane-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005637,GO%3A0005640/ancestors?relations=is_a; Exact relations=is_a ancestor lists for GO0005637 and GO0005640 | supports | The is_a-only ancestor response places both nuclear membrane terms below GO0031090 organelle membrane. It establishes ancestry, not necessarily an immediate parent edge. |
| nuclear-agent-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete taxId, scientificName, rank and available lineage fields | supports | ENA confirms Eukaryota2759, currently domain rank; identity does not measure prevalence. |
| nuclear-agent-hetzer2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101/cshperspect.a000539%22&amp;format=json&amp;resultType=core; Unique native MED result and full abstract; literature-review tier | supports | Exact DOI10.1101/cshperspect.a000539, PMID20300205, author/year/title and complete abstract match the recovered review. |
| nuclear-agent-hetzer2010-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2829960/; PMC2829960 opening main paragraphs, Table1 context and Figure1 caption; complete s1,s7,s9,s10 with embedded captions. No image pixels or unlisted sections inspected. | supports | Review-tier source supports double-membrane topology, ER continuity and perinuclear-space synonymy. It distinguishes closed yeast/fungal mitosis from metazoan envelope breakdown, and reviews assembly/remodeling. Figure1 caption explicitly identifies the intervening volume as ER lumen or perinuclear space. The source does not establish universal molecular composition or a universal formation requirement. |
| schema-result | just validate data/structures/membrane_organelle/nuclear_envelope_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/nuclear_envelope_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/nuclear_envelope_lumen.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_envelope_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/nuclear_envelope_lumen.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_envelope_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_envelope_lumen-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/nuclear_envelope_lumen.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 8 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Source scope is limited to the exact body sections and captions stated per evidence row. No primary image pixels or quantitative reanalysis is claimed, and no maintained image or verbatim snippet requires reuse/licence verification here.
- Ontological topology and constitutive material identity do not establish individual molecular formation necessity. Optional exact lipid chemistry, stoichiometry and complete resident-protein inventories remain unresolved without invented findings.
- COMMON is qualitative occurrence; native taxon identities do not quantify prevalence or make every primary experimental background identical to a reference strain.
- Hetzer and Aitchison, where used, are literature reviews. Closed yeast mitosis is distinct from metazoan envelope breakdown. The inherited GO definition is not a new experiment proving a universal lamina composition or20–40nm range across every eukaryotic cell.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes clean drafts without inventing findings. Parent owns finalization and persistence; five same-base global gates are staged separately.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025106Z-nuclear-envelope-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Nuclear envelope lumen scientific review
started_at: '2026-10-22T02:36:25Z'
finished_at: '2026-10-22T02:51:06Z'
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
summary: The perinuclear-lumen identity, exact synonym, hierarchy, ER continuity and
  boundary-only graph are supported. No concrete curation finding was established
  within the inspected source scope.
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
  - path: data/structures/membrane_organelle/nuclear_envelope.yaml
    sha256: 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a
    role: context
  - path: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    sha256: 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019
    role: target
  - path: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    sha256: c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df
    role: context
  - path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    sha256: a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb
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
- target_id: GO:0005641
  path: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  label: nuclear envelope lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    role: maintained scientific record
scope:
  description: Entire target within the four-record nuclear-envelope boundary set
    (target plus three neighbors); definitions, hierarchy, components, taxon/examples,
    functions, every directed edge, discussions, exact authorities and declared source
    body/supplement scopes.
  selection: Batch35 target 3; exact native inspection and focused schema/strict gates
    passed before assessment at unchanged f97b1abe.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005641
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: just validate data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: just validate-strict data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_envelope_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005641
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: protein-applicability
  name: Protein-instance applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005641
  summary: No individual protein_examples or accession-bearing GENE_OR_PROTEIN nodes
    occur in this target; exact NPC GO identity is checked directly where asserted.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005641
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-nuclear_envelope
  - neighbor-nuclear_inner_membrane
  - neighbor-nuclear_outer_membrane
  - nuclear-agent-go
  - nuclear-agent-membrane-ancestors
  - nuclear-agent-tax2759
  - nuclear-agent-hetzer2010-meta
  - nuclear-agent-hetzer2010-pmc
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005641
  summary: 8 of 8 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005641
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005641
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
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  locator: Entire maintained YAML, including history, evidence, all directed edges
    and discussions
  accessed_at: '2026-10-22T02:43:32Z'
  support: context_only
  summary: The complete target was independently read. Maintained scientific content
    and status remain unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent lines391–444; CausalNode lines843–875; component types1044–1057
  accessed_at: '2026-10-22T02:43:32Z'
  support: context_only
  summary: Molecular lipid identity differs from a complete membrane. GO can ground
    a protein subcomplex; CHEBI is the stated lipid grounding route. Essentiality
    denotes formation necessity. Node xrefs can link instances without claiming complete
    cohort coverage.
- evidence_id: neighbor-nuclear_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_envelope.yaml
  locator: Complete maintained nuclear-envelope boundary neighbor
  accessed_at: '2026-10-22T02:43:32Z'
  support: context_only
  summary: Exact adjacent record read and frozen for topology and representation context;
    maintained context is not independent experimental evidence.
- evidence_id: neighbor-nuclear_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
  locator: Complete maintained nuclear-envelope boundary neighbor
  accessed_at: '2026-10-22T02:43:32Z'
  support: context_only
  summary: Exact adjacent record read and frozen for topology and representation context;
    maintained context is not independent experimental evidence.
- evidence_id: neighbor-nuclear_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  locator: Complete maintained nuclear-envelope boundary neighbor
  accessed_at: '2026-10-22T02:43:32Z'
  support: context_only
  summary: Exact adjacent record read and frozen for topology and representation context;
    maintained context is not independent experimental evidence.
- evidence_id: nuclear-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005635,GO%3A0031967,GO%3A0005634,GO%3A0005637,GO%3A0005640,GO%3A0005641,GO%3A0005643,GO%3A0006913,GO%3A0006998,GO%3A0031970,GO%3A0005788,GO%3A0031090,GO%3A0005774
  locator: 'Complete13 requested native term results: exact IDs, definitions, synonyms,
    active flags and returned child relations'
  accessed_at: '2026-10-22T02:39:01.002553Z'
  support: supports
  summary: All13 active native terms were inspected. The definitions distinguish envelope,
    nucleus, inner/outer bilayers, perinuclear lumen, NPC, ER lumen and vacuolar membrane.
    Returned children directly support envelope is_a organelle envelope, lumen is_a
    organelle envelope lumen, and envelope part_of nucleus. GO0005635 exactly supplies
    the maintained definition, including its20–40nm range and lamina clause; this
    is ontology wording, not a new universal measurement.
  snapshot_sha256: 18627a592c0f8bace3b7cf3d8847639aae864fec38a5ee52dbf84c4746d35298
- evidence_id: nuclear-agent-membrane-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005637,GO%3A0005640/ancestors?relations=is_a
  locator: Exact relations=is_a ancestor lists for GO0005637 and GO0005640
  accessed_at: '2026-10-22T02:39:55.152921Z'
  support: supports
  summary: The is_a-only ancestor response places both nuclear membrane terms below
    GO0031090 organelle membrane. It establishes ancestry, not necessarily an immediate
    parent edge.
  snapshot_sha256: e57c228227ef0b047dd587cb5ac0fb2f89e7083e9d3d3cf43b21619398af3dc5
- evidence_id: nuclear-agent-tax2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete taxId, scientificName, rank and available lineage fields
  accessed_at: '2026-10-22T02:39:01.649159Z'
  support: supports
  summary: ENA confirms Eukaryota2759, currently domain rank; identity does not measure
    prevalence.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: nuclear-agent-hetzer2010-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1101/cshperspect.a000539%22&format=json&resultType=core
  locator: Unique native MED result and full abstract; literature-review tier
  accessed_at: '2026-10-22T02:39:01.003407Z'
  support: supports
  summary: Exact DOI10.1101/cshperspect.a000539, PMID20300205, author/year/title and
    complete abstract match the recovered review.
  snapshot_sha256: af844e87c53974d25c44b22693637b74d5594ac6563362dd5bf6fb716230abac
- evidence_id: nuclear-agent-hetzer2010-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2829960/
  locator: PMC2829960 opening main paragraphs, Table1 context and Figure1 caption;
    complete s1,s7,s9,s10 with embedded captions. No image pixels or unlisted sections
    inspected.
  accessed_at: '2026-10-22T02:39:20.762508Z'
  support: supports
  summary: Review-tier source supports double-membrane topology, ER continuity and
    perinuclear-space synonymy. It distinguishes closed yeast/fungal mitosis from
    metazoan envelope breakdown, and reviews assembly/remodeling. Figure1 caption
    explicitly identifies the intervening volume as ER lumen or perinuclear space.
    The source does not establish universal molecular composition or a universal formation
    requirement.
  snapshot_sha256: 972f3e2896034c3e4c0a60a309dc098259eee64d6f0d669c54e391ffbf9bd564
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:26Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/nuclear_envelope_lumen.yaml'
  snapshot_sha256: 29892ffe39699ffbaf40053463487eadfe32472313c2ac4da5e09fd0853a59e2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_envelope_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:28Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/nuclear_envelope_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_envelope_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_envelope_lumen-strict.tsv"
  snapshot_sha256: 2a79e20edb597b1d434a36a947e94940eb91324168d8f4daf933d54fdca7e99f
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 8 of 8 collected target identifiers returned OK. No residuals. Native source
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
  topic: Perinuclear volume rather than nuclear interior
  outcome: supported
  target_ids:
  - GO:0005641
  summary: GO0005641 exactly denotes the region between envelope bilayers. Native
    GO0031970 children confirm organelle-envelope-lumen ancestry; GO0005635 contains
    it. Perinuclear space is an exact native synonym and is independently used by
    Hetzer.
  evidence_ids:
  - record
  - nuclear-agent-go
  - nuclear-agent-hetzer2010-pmc
- assessment_id: topology
  area: graph
  topic: Four descriptive boundary and continuity edges
  outcome: supported
  target_ids:
  - GO:0005641
  summary: The NONMECHANISTIC graph distinguishes the volume from the inner/outer
    bounding bilayers and links the perinuclear volume to the ER lumen. Hetzer Figure1
    caption and ER-continuity text support this; the region is not equated with the
    nucleoplasm or assigned an autonomous transport mechanism.
  evidence_ids:
  - record
  - nuclear-agent-go
  - nuclear-agent-hetzer2010-pmc
- assessment_id: components
  area: grounding
  topic: Boundary membranes are not lumen constituents
  outcome: supported
  target_ids:
  - GO:0005641
  summary: The resolved boundary discussion correctly leaves the two bordering membranes
    outside the lumen component list. No molecular constituent, essentiality, canonical
    strain or mandatory inventory is asserted.
  evidence_ids:
  - record
  - schema
  - nuclear-agent-go
- assessment_id: scope
  area: scope
  topic: Broad eukaryotic occurrence
  outcome: supported
  target_ids:
  - GO:0005641
  summary: Native2759 identifies Eukaryota. Review context supports a perinuclear
    lumen in the double-envelope organization, without implying an intact nuclear
    envelope throughout every cell-cycle phase or quantifying prevalence.
  evidence_ids:
  - record
  - nuclear-agent-tax2759
  - nuclear-agent-hetzer2010-pmc
- assessment_id: access-completeness
  area: evidence
  topic: Source tier, currentness and review limits
  outcome: supported
  target_ids:
  - GO:0005641
  summary: All target citation identities and native term/protein identities were
    checked. Relevant primary or review body passages were read within the declared
    locators. Historical discussions are interpreted in their recorded context, with
    only concrete current contradictions flagged. No scientific promotion or corpus
    edit is implied.
  evidence_ids:
  - record
  - nuclear-agent-go
  - nuclear-agent-membrane-ancestors
  - nuclear-agent-tax2759
  - nuclear-agent-hetzer2010-meta
  - nuclear-agent-hetzer2010-pmc
findings: []
actions: []
limitations:
- Source scope is limited to the exact body sections and captions stated per evidence
  row. No primary image pixels or quantitative reanalysis is claimed, and no maintained
  image or verbatim snippet requires reuse/licence verification here.
- Ontological topology and constitutive material identity do not establish individual
  molecular formation necessity. Optional exact lipid chemistry, stoichiometry and
  complete resident-protein inventories remain unresolved without invented findings.
- COMMON is qualitative occurrence; native taxon identities do not quantify prevalence
  or make every primary experimental background identical to a reference strain.
- Hetzer and Aitchison, where used, are literature reviews. Closed yeast mitosis is
  distinct from metazoan envelope breakdown. The inherited GO definition is not a
  new experiment proving a universal lamina composition or20–40nm range across every
  eukaryotic cell.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes clean drafts without inventing findings. Parent
  owns finalization and persistence; five same-base global gates are staged separately.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
