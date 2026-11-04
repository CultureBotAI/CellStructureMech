# Toxicyst scientific review

- Review: 20261022T034911Z-toxicyst-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:33:58Z
- Finished UTC: 2026-10-22T03:49:11Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Toxicyst structure, observed predation and bounded Coleps discharge chemistry are supported. One minor finding corrects seven repeated first-author attribution strings.

## Scope And Provenance

Exactly one entire target reviewed for identity, constituents, evidence, scope, graph joins and completeness.

Selection: Target 5 of batch41, next uncovered strict-path-order target at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:toxicyst | data/structures/membrane_organelle/toxicyst.yaml | maintained | toxicyst |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:toxicyst | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:toxicyst | Focused validator passed. |
| Focused protein or graph check | passed | True | cellstructuremech:toxicyst | Focused native check passed; biological scope separately reviewed. |
| Expression-module applicability | not_applicable | False | cellstructuremech:toxicyst | No expression-module regulatory claim is maintained. |
| Claim-level scientific review | passed | True | cellstructuremech:toxicyst | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:toxicyst | 5 of 6 collected target identifiers returned OK. cellstructuremech:toxicyst: SKIPPED; Exact current local identity occurs once in an ignored-inclusive identifier search and is a frozen maintained input. The bounded native GO lexical search has no exact toxicyst result; no exhaustive ontology absence is inferred. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:toxicyst | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:toxicyst | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:toxicyst | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:toxicyst | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:toxicyst | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Offensive extrusome boundary

identity: supported. Targets: cellstructuremech:toxicyst.

The local identity, membrane-bounded parent and prey-contact definition match the read article. The exact native GO lexical search has no hit; local ignored-inclusive search finds one maintained identity. Candidate genes are not used as structure identity.

### Collective membrane and unresolved discharge mixture

grounding: supported. Targets: cellstructuremech:toxicyst.

Label-only membrane material has no erroneous whole-GO grounding. Collective constitutional membrane necessity differs from individual molecular requirements. Coleps discharge chemistry supports an unresolved small-molecule mixture; UNKNOWN cargo formation necessity and the chemistry TODO are appropriate. No inference that every FFA is a resident resting-organelle cargo is made.

### Haptorian and Coleps evidence remain separated

scope: supported. Targets: cellstructuremech:toxicyst.

Li2024 reports the haptorian typeI scope and Litonotus TEM; Buonanno independently supports Coleps oral toxicysts and isolated discharge. The record does not generalize Coleps chemical composition into a verified universal haptorian toxin recipe.

### Four descriptive discharge/function edges

graph: supported. Targets: cellstructuremech:toxicyst.

Boundary, prey-contact trigger, release and cytotoxic support are source-compatible at their stated scope. NONMECHANISTIC avoids importing candidate PKS/LAAO genes as mature constituents or asserting exact fusion machinery.

### Repeated first-author attribution mismatch

evidence: concern. Targets: cellstructuremech:toxicyst.

The correct DOI and paper title are retained, but notes repeatedly call this Chen etal2024 although native MED and genuine article metadata put Li first. This is a bibliographic attribution correction; the supporting article remains the same.

### Full target and resolved boundary discussion

completeness: supported. Targets: cellstructuremech:toxicyst.

All fields including the removed historical Didinium citation and both discussions were inspected. Candidate gene expansions remain appropriately outside the mature constituent list.

### Individual molecular formation requirements

evidence: unknown. Targets: cellstructuremech:toxicyst.

The available Coleps discharge chemistry does not identify which individual molecules are necessary to form resting toxicysts. UNKNOWN cargo essentiality and unresolved molecular chemistry remain appropriate.

## Findings

### F1: Correct the first author of the toxicyst genomics source

minor / open / confirmed; issue key: toxicyst-li2024-first-author.

Seven maintained notes/rationale call DOI10.1186/s12915-024-01904-2 Chen etal2024. The article and native MED list Zaihan Li first, followed by Xiao Chen, Fangqing Zhao and Miao Miao. Correct the prose attribution to Li etal2024 while preserving this DOI and its supported claims.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, correct the seven current source-attribution strings to Li etal2024; retain the DOI, title, taxon boundaries and candidate-gene interpretation.

- Current evidence notes match the ordered author list.
- The verified scientific claims and original history are preserved.
- Native schema, strict, graph and applicable history checks pass after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/toxicyst.yaml; Entire maintained target including history, all components, graph edges, evidence and discussions | context_only | All current fields were read. Historical events are provenance rather than independent experimental support. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component, essentiality, graph and source contracts | context_only | Exact anatomy differs from constituent material; activity and localization alone do not establish individual formation necessity. |
| root41-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0062160,GO:0062159,GO:0043231,GO:0033176,GO:0005802,GO:0098791,GO:0005794,GO:0032588,GO:0005768; Complete nine id/name/definition/active/synonym fields and applicable typed children; generic organelle child list read as context, not an exhaustive ontology search. | supports | Nine active GO entries verify exact spongiome and TGN identities, their applicable anatomy, and the generic proton-transporting V-type ATPase complex. GO0062159 has0062160 part_of;0098791 has0005802 is_a;0005802 has0032588 part_of. |
| root41-sources-go-search-toxicyst | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=toxicyst&amp;limit=100; Complete zero-hit response and exact URL query | supports | Exact native GO toxicyst name query returned zero hits. This is a bounded lexical search, not proof that every possible synonym or ontology lacks a term. |
| root41-sources-tax197905 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/197905; Complete native taxonomy response | supports | Native ENA verifies Haptoria subclass identity and rank. |
| root41-sources-tax60000 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/60000; Complete native taxonomy response | supports | Native ENA verifies Coleps hirtus species identity and rank. |
| root41-sources-chen2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1186%2Fs12915-024-01904-2&amp;format=json&amp;resultType=core; Complete native title, ordered author list, DOI/PMC/year and abstract | supports | Unique MED38715037/PMC11077807 DOI10.1186/s12915-024-01904-2 identifies Li Z, Chen X, Zhao F, Miao M in that order. Complete abstract distinguishes seven-species observations/sequencing and candidate toxin-gene expansions. |
| root41-sources-chen2024-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11077807/fullTextXML; Ordered article-meta authors; complete Sec1 Background, Sec3 Morphology and lifestyle with Fig1 caption, Sec6 candidate gene expansion with Fig4 caption, Sec7 Discussion, Sec8 Conclusions, Sec10 sample collection, Sec11 TEM; no figure pixels/supplements | supports | Genuine article lists Zaihan Li first and Xiao Chen second. The body directly documents Litonotus TEM and haptorian predation, describes broader ultrastructure/discharge background, and explicitly leaves PKS/LAAO toxin functions as candidates needing study. |
| root41-sources-buonanno2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111%2Fjeu.12106&amp;format=json&amp;resultType=core; Complete native identity and primary abstract only | supports | Unique MED24512001 DOI10.1111/jeu.12106 identifies Buonanno etal2014. Complete abstract reports discharge isolated from living Coleps, cytotoxic tests, effective-predation dependence and19 free fatty acids plus minor phytanic acid by LC-ES-MS and GC-MS. It does not localize exact chemical species inside resting organelles. |
| root41-sources-buonanno2014-publisher | https://doi.org/10.1111/jeu.12106; Retained failure response only; not article text | context_only | Native status 403 failed to supply a readable article body. No full-text access is inferred. |
| local-identity | rg --no-ignore --hidden -n ^identifier: cellstructuremech:toxicyst$ data/structures; Ignored-inclusive exact top-level identifier search in data/structures | supports | data/structures/membrane_organelle/toxicyst.yaml:1:identifier: cellstructuremech:toxicyst |
| schema-result | just validate data/structures/membrane_organelle/toxicyst.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/toxicyst.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/toxicyst.yaml --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/toxicyst-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/toxicyst.yaml --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/toxicyst-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch41-20261022-ex_agh9z/toxicyst-strict.tsv |
| native-toxicyst-causal | /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/toxicyst.yaml; Complete focused native report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/toxicyst.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 5 of 6 collected target identifiers returned OK. cellstructuremech:toxicyst: SKIPPED; Exact current local identity occurs once in an ignored-inclusive identifier search and is a frozen maintained input. The bounded native GO lexical search has no exact toxicyst result; no exhaustive ontology absence is inferred. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Presence is qualitative and taxon examples are bounded; no complete species census, measured occurrence frequency or exhaustive molecular inventory is inferred.
- Buonanno2014 was read as complete native identity and abstract only; publisher403 prevented full Methods, toxicity controls and exact19-species chemical inventory inspection.
- Li2024 body scope is precisely listed in its evidence row. Other genomic Results/Methods, figure pixels, supplements and raw genomic or mass-spectrometry data were not reanalyzed. The native GO no-hit result is only an exact lexical query, not an exhaustive ontology absence claim.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User requests all uncovered records, including honest zero-finding reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T034911Z-toxicyst-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Toxicyst scientific review
started_at: '2026-10-22T03:33:58Z'
finished_at: '2026-10-22T03:49:11Z'
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
summary: Toxicyst structure, observed predation and bounded Coleps discharge chemistry
  are supported. One minor finding corrects seven repeated first-author attribution
  strings.
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
  - path: data/structures/membrane_organelle/toxicyst.yaml
    sha256: 672baa23fe05a4cd16b6319696b5837b2a446f13e14e453e6fa983e36bdb5c57
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
- target_id: cellstructuremech:toxicyst
  path: data/structures/membrane_organelle/toxicyst.yaml
  label: toxicyst
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/toxicyst.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target reviewed for identity, constituents, evidence,
    scope, graph joins and completeness.
  selection: Target 5 of batch41, next uncovered strict-path-order target at fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:toxicyst
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:toxicyst
  command: just validate data/structures/membrane_organelle/toxicyst.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:toxicyst
  command: just validate-strict data/structures/membrane_organelle/toxicyst.yaml --out
    /private/tmp/cellstructure-batch41-20261022-ex_agh9z/toxicyst-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-toxicyst-causal
  name: Focused protein or graph check
  status: passed
  required: true
  target_ids:
  - cellstructuremech:toxicyst
  command: /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/toxicyst.yaml
  exit_code: 0
  summary: Focused native check passed; biological scope separately reviewed.
  evidence_ids:
  - native-toxicyst-causal
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:toxicyst
  summary: No expression-module regulatory claim is maintained.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:toxicyst
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - root41-sources-go
  - root41-sources-go-search-toxicyst
  - root41-sources-tax197905
  - root41-sources-tax60000
  - root41-sources-chen2024-meta
  - root41-sources-chen2024-jats
  - root41-sources-buonanno2014-meta
  - root41-sources-buonanno2014-publisher
  - local-identity
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:toxicyst
  summary: '5 of 6 collected target identifiers returned OK. cellstructuremech:toxicyst:
    SKIPPED; Exact current local identity occurs once in an ignored-inclusive identifier
    search and is a frozen maintained input. The bounded native GO lexical search
    has no exact toxicyst result; no exhaustive ontology absence is inferred. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:toxicyst
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
  - cellstructuremech:toxicyst
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
  - cellstructuremech:toxicyst
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
  - cellstructuremech:toxicyst
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
  - cellstructuremech:toxicyst
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
  reference: data/structures/membrane_organelle/toxicyst.yaml
  locator: Entire maintained target including history, all components, graph edges,
    evidence and discussions
  accessed_at: '2026-10-22T03:45:25Z'
  support: context_only
  summary: All current fields were read. Historical events are provenance rather than
    independent experimental support.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component, essentiality, graph and source contracts
  accessed_at: '2026-10-22T03:45:25Z'
  support: context_only
  summary: Exact anatomy differs from constituent material; activity and localization
    alone do not establish individual formation necessity.
- evidence_id: root41-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0062160,GO:0062159,GO:0043231,GO:0033176,GO:0005802,GO:0098791,GO:0005794,GO:0032588,GO:0005768
  locator: Complete nine id/name/definition/active/synonym fields and applicable typed
    children; generic organelle child list read as context, not an exhaustive ontology
    search.
  accessed_at: '2026-10-22T03:36:16.668427Z'
  support: supports
  summary: Nine active GO entries verify exact spongiome and TGN identities, their
    applicable anatomy, and the generic proton-transporting V-type ATPase complex.
    GO0062159 has0062160 part_of;0098791 has0005802 is_a;0005802 has0032588 part_of.
  snapshot_sha256: 2422d30d8ab6355062d2ee5b73f7d06600669b7af572330b7cc8d560570acca9
- evidence_id: root41-sources-go-search-toxicyst
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=toxicyst&limit=100
  locator: Complete zero-hit response and exact URL query
  accessed_at: '2026-10-22T03:36:16.668871Z'
  support: supports
  summary: Exact native GO toxicyst name query returned zero hits. This is a bounded
    lexical search, not proof that every possible synonym or ontology lacks a term.
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
- evidence_id: root41-sources-tax197905
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/197905
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T03:36:17.433892Z'
  support: supports
  summary: Native ENA verifies Haptoria subclass identity and rank.
  snapshot_sha256: 2541d02ab11002daf8b822e8d7154a557e718846a29364953f12538a29e74419
- evidence_id: root41-sources-tax60000
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/60000
  locator: Complete native taxonomy response
  accessed_at: '2026-10-22T03:36:17.442091Z'
  support: supports
  summary: Native ENA verifies Coleps hirtus species identity and rank.
  snapshot_sha256: 9d000b25ab0962278890158a8d838765e9b2864f5377502067679c925a16861e
- evidence_id: root41-sources-chen2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1186%2Fs12915-024-01904-2&format=json&resultType=core
  locator: Complete native title, ordered author list, DOI/PMC/year and abstract
  accessed_at: '2026-10-22T03:36:19.318894Z'
  support: supports
  summary: Unique MED38715037/PMC11077807 DOI10.1186/s12915-024-01904-2 identifies
    Li Z, Chen X, Zhao F, Miao M in that order. Complete abstract distinguishes seven-species
    observations/sequencing and candidate toxin-gene expansions.
  snapshot_sha256: 97acdd660398518c4d690d7118a63f5b126fdc08dbd69c9c29538367fd038b53
- evidence_id: root41-sources-chen2024-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC11077807/fullTextXML
  locator: Ordered article-meta authors; complete Sec1 Background, Sec3 Morphology
    and lifestyle with Fig1 caption, Sec6 candidate gene expansion with Fig4 caption,
    Sec7 Discussion, Sec8 Conclusions, Sec10 sample collection, Sec11 TEM; no figure
    pixels/supplements
  accessed_at: '2026-10-22T03:37:20.879116Z'
  support: supports
  summary: Genuine article lists Zaihan Li first and Xiao Chen second. The body directly
    documents Litonotus TEM and haptorian predation, describes broader ultrastructure/discharge
    background, and explicitly leaves PKS/LAAO toxin functions as candidates needing
    study.
  snapshot_sha256: 914a79293dd45456f11e2fc3655e214c1c61a233ee8ad60a5c2d08baf8c67fb8
- evidence_id: root41-sources-buonanno2014-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1111%2Fjeu.12106&format=json&resultType=core
  locator: Complete native identity and primary abstract only
  accessed_at: '2026-10-22T03:36:19.350350Z'
  support: supports
  summary: Unique MED24512001 DOI10.1111/jeu.12106 identifies Buonanno etal2014. Complete
    abstract reports discharge isolated from living Coleps, cytotoxic tests, effective-predation
    dependence and19 free fatty acids plus minor phytanic acid by LC-ES-MS and GC-MS.
    It does not localize exact chemical species inside resting organelles.
  snapshot_sha256: ff0115ebd1fa19ebd3e9c23a39f2f65c3ba25711ef2a689dd49bf85ef3c13271
- evidence_id: root41-sources-buonanno2014-publisher
  kind: primary_source
  reference: https://doi.org/10.1111/jeu.12106
  locator: Retained failure response only; not article text
  accessed_at: '2026-10-22T03:37:20.878844Z'
  support: context_only
  summary: Native status 403 failed to supply a readable article body. No full-text
    access is inferred.
  snapshot_sha256: 2c2873bdf134c12dac371e7a31fb4bfcb06fc12929d133fa412699560cd80e5b
- evidence_id: local-identity
  kind: search
  reference: 'rg --no-ignore --hidden -n ^identifier: cellstructuremech:toxicyst$
    data/structures'
  locator: Ignored-inclusive exact top-level identifier search in data/structures
  accessed_at: '2026-10-22T03:43:37.612926Z'
  support: supports
  summary: 'data/structures/membrane_organelle/toxicyst.yaml:1:identifier: cellstructuremech:toxicyst'
  snapshot_sha256: 57c00f4a9a525da4bd22d2ad1685f65f101aa2dfadae60b20bc355674860a232
  search_scope: Exact anchored identifier search under data/structures using rg --no-ignore
    --hidden; includes ignored and hidden files in this maintained record scope, not
    all literature or ontologies.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/toxicyst.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:33:59Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/toxicyst.yaml'
  snapshot_sha256: 3bb5a439496608d6e3bc7c860f6836e0ffbae8728b3aa7cc54ac1b7d1899f0f6
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/toxicyst.yaml
    --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/toxicyst-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:34:01Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/toxicyst.yaml\
    \ --out /private/tmp/cellstructure-batch41-20261022-ex_agh9z/toxicyst-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch41-20261022-ex_agh9z/toxicyst-strict.tsv"
  snapshot_sha256: e49ea8b974343ff327b5914757048897deccfbcc6e98c5f4a890207ff1de6656
- evidence_id: native-toxicyst-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch41-20261022-ex_agh9z/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/toxicyst.yaml
  locator: Complete focused native report
  accessed_at: '2026-10-22T03:42:20.223221Z'
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
  locator: data/structures/membrane_organelle/toxicyst.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '5 of 6 collected target identifiers returned OK. cellstructuremech:toxicyst:
    SKIPPED; Exact current local identity occurs once in an ignored-inclusive identifier
    search and is a frozen maintained input. The bounded native GO lexical search
    has no exact toxicyst result; no exhaustive ontology absence is inferred. Native
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
  topic: Offensive extrusome boundary
  outcome: supported
  target_ids:
  - cellstructuremech:toxicyst
  summary: The local identity, membrane-bounded parent and prey-contact definition
    match the read article. The exact native GO lexical search has no hit; local ignored-inclusive
    search finds one maintained identity. Candidate genes are not used as structure
    identity.
  evidence_ids:
  - record
  - root41-sources-go
  - root41-sources-go-search-toxicyst
  - local-identity
  - root41-sources-chen2024-jats
- assessment_id: composition
  area: grounding
  topic: Collective membrane and unresolved discharge mixture
  outcome: supported
  target_ids:
  - cellstructuremech:toxicyst
  summary: Label-only membrane material has no erroneous whole-GO grounding. Collective
    constitutional membrane necessity differs from individual molecular requirements.
    Coleps discharge chemistry supports an unresolved small-molecule mixture; UNKNOWN
    cargo formation necessity and the chemistry TODO are appropriate. No inference
    that every FFA is a resident resting-organelle cargo is made.
  evidence_ids:
  - record
  - schema
  - root41-sources-chen2024-jats
  - root41-sources-buonanno2014-meta
- assessment_id: taxonomy
  area: scope
  topic: Haptorian and Coleps evidence remain separated
  outcome: supported
  target_ids:
  - cellstructuremech:toxicyst
  summary: Li2024 reports the haptorian typeI scope and Litonotus TEM; Buonanno independently
    supports Coleps oral toxicysts and isolated discharge. The record does not generalize
    Coleps chemical composition into a verified universal haptorian toxin recipe.
  evidence_ids:
  - record
  - root41-sources-chen2024-jats
  - root41-sources-buonanno2014-meta
  - root41-sources-tax197905
  - root41-sources-tax60000
- assessment_id: graph
  area: graph
  topic: Four descriptive discharge/function edges
  outcome: supported
  target_ids:
  - cellstructuremech:toxicyst
  summary: Boundary, prey-contact trigger, release and cytotoxic support are source-compatible
    at their stated scope. NONMECHANISTIC avoids importing candidate PKS/LAAO genes
    as mature constituents or asserting exact fusion machinery.
  evidence_ids:
  - record
  - root41-sources-chen2024-jats
  - root41-sources-buonanno2014-meta
- assessment_id: attribution
  area: evidence
  topic: Repeated first-author attribution mismatch
  outcome: concern
  target_ids:
  - cellstructuremech:toxicyst
  summary: The correct DOI and paper title are retained, but notes repeatedly call
    this Chen etal2024 although native MED and genuine article metadata put Li first.
    This is a bibliographic attribution correction; the supporting article remains
    the same.
  evidence_ids:
  - record
  - root41-sources-chen2024-meta
  - root41-sources-chen2024-jats
- assessment_id: coverage
  area: completeness
  topic: Full target and resolved boundary discussion
  outcome: supported
  target_ids:
  - cellstructuremech:toxicyst
  summary: All fields including the removed historical Didinium citation and both
    discussions were inspected. Candidate gene expansions remain appropriately outside
    the mature constituent list.
  evidence_ids:
  - record
  - root41-sources-chen2024-jats
  - root41-sources-buonanno2014-meta
- assessment_id: formation
  area: evidence
  topic: Individual molecular formation requirements
  outcome: unknown
  target_ids:
  - cellstructuremech:toxicyst
  summary: The available Coleps discharge chemistry does not identify which individual
    molecules are necessary to form resting toxicysts. UNKNOWN cargo essentiality
    and unresolved molecular chemistry remain appropriate.
  evidence_ids:
  - record
  - schema
  - root41-sources-buonanno2014-meta
findings:
- finding_id: F1
  issue_key: toxicyst-li2024-first-author
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the first author of the toxicyst genomics source
  description: Seven maintained notes/rationale call DOI10.1186/s12915-024-01904-2
    Chen etal2024. The article and native MED list Zaihan Li first, followed by Xiao
    Chen, Fangqing Zhao and Miao Miao. Correct the prose attribution to Li etal2024
    while preserving this DOI and its supported claims.
  target_ids:
  - cellstructuremech:toxicyst
  field_paths:
  - components[0].evidence[0].notes
  - functions[0].evidence[1].notes
  - evidence[0].notes
  - causal_graphs[0].edges[0].evidence[0].notes
  - causal_graphs[0].edges[1].evidence[0].notes
  - discussions[1].rationale
  - discussions[1].evidence[0].notes
  evidence_ids:
  - record
  - root41-sources-chen2024-meta
  - root41-sources-chen2024-jats
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/toxicyst.yaml
    role: maintained scientific record
  rule_id: Exact source attribution and component identity must match maintained claims
  native_severity: minor
  normalization_reason: A localized attribution or graph-reference correction preserves
    the supported anatomical identity and biological claim.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:toxicyst
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/toxicyst.yaml
    role: maintained scientific record
  description: In separately authorized curation, correct the seven current source-attribution
    strings to Li etal2024; retain the DOI, title, taxon boundaries and candidate-gene
    interpretation.
  acceptance_checks:
  - Current evidence notes match the ordered author list.
  - The verified scientific claims and original history are preserved.
  - Native schema, strict, graph and applicable history checks pass after separately
    authorized curation.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Presence is qualitative and taxon examples are bounded; no complete species census,
  measured occurrence frequency or exhaustive molecular inventory is inferred.
- Buonanno2014 was read as complete native identity and abstract only; publisher403
  prevented full Methods, toxicity controls and exact19-species chemical inventory
  inspection.
- Li2024 body scope is precisely listed in its evidence row. Other genomic Results/Methods,
  figure pixels, supplements and raw genomic or mass-spectrometry data were not reanalyzed.
  The native GO no-hit result is only an exact lexical query, not an exhaustive ontology
  absence claim.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User requests all uncovered records, including honest zero-finding reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
