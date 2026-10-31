# Nucleus identity and source review

- Review: 20261022T025110Z-nucleus-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:36:40Z
- Finished UTC: 2026-10-22T02:51:10Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Nucleus identity and descriptive envelope/transport scope are supported. One minor finding corrects the Lu and Drubin bibliographic attribution.

## Scope And Provenance

Entire single record: identity, hierarchy, components, taxonomy, functions, every asserted graph edge, discussions and image provenance where present.

Selection: Target 9 of batch35 in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005634 | data/structures/membrane_organelle/nucleus.yaml | maintained | nucleus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005634 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005634 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005634 | No claimed expression-module membership or expression cluster used as mechanistic evidence. |
| Claim-level scientific review | passed | True | GO:0005634 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005634 | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005634 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005634 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005634 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005634 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005634 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact nucleus and parts

identity: supported. Targets: GO:0005634.

Native definition, exact synonym and is_a-only ancestry support the maintained nucleus. Envelope/lumen/pore parthood and the inner-membrane-enclosed volume remain distinct. The shortened definition is a bounded generic definition, not a new universal claim that every specialized nucleus replicates DNA.

### Exact pore-complex component

grounding: supported. Targets: GO:0005634.

GO0005643 explicitly denotes a protein complex; PROTEIN_COMPLEX is an appropriate component type. UNKNOWN formation essentiality does not equate transport function with necessity for forming the entire nucleus. No single organism protein instance is substituted for the whole NPC.

### Budding-yeast example

scope: supported. Targets: GO:0005634.

The canonical example and qualitative distribution note are specifically about nucleus–vacuole contacts in budding yeast. The primary source supports this bounded context, while neither native taxonomy nor this experiment supplies a measured species-wide prevalence.

### Four envelope and transport edges

graph: supported. Targets: GO:0005634.

Every NONMECHANISTIC edge is supported at its declared level: envelope bounds lumen/encloses nucleus, pore spans the envelope, and pore mediates exchange. No detailed molecular pore assembly pathway, energy-free whole transport claim or blanket NPC-protein inventory is asserted.

### Exact Lu and Drubin attribution

evidence: concern. Targets: GO:0005634.

The target bibliography misspells the first author and uses et al for a two-author paper. Native MED metadata and the genuine primary article independently identify Lu and Drubin. This is a bounded bibliographic error, not a wrong organelle or demonstrated false mechanism.

### Bounded nucleus inventory

completeness: supported. Targets: GO:0005634.

All maintained fields and the open molecular-cohort TODO were reviewed. The TODO does not claim a complete chromatin, nucleolar or nuclear-envelope inventory. No forced protein examples or unsupported molecular cohort grounding are added.

## Findings

### F1: Correct the Lu and Drubin citation attribution

minor / open / confirmed; issue key: nucleus-lu-drubin-attribution.

evidence[5].notes attributes DOI10.1080/21541248.2021.1993714 to Luo et al2022. Both native MED metadata and the primary article identify Michelle S Lu and David G Drubin as its two authors. The DOI, title and2022 volume year otherwise match.

## Recommended Actions And Acceptance Checks

### A1

Correct the evidence note to Lu and Drubin(2022), retaining the verified DOI/title and treating the article functional proposals as proposals.

- Verify exact authors/title/DOI against the native source.
- After separately authorized curation, run the focused schema and strict validation recipes.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/nucleus.yaml; Entire maintained target, every graph edge, component, discussion, image descriptor and historical event | context_only | Complete scientific target read; no scientific edits or status promotion. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent and ComponentTypeEnum/ComponentRoleEnum | context_only | Component identities, formation essentiality and constituent role are assessed separately. OTHER does not assert a chemical lipid category; exact named protein complexes have their own permitted type. |
| root35-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031981,GO:0070013,GO:0005634,GO:0005637,GO:0000228,GO:0005730,GO:0005622,GO:0005635,GO:0016020,GO:0044195,GO:0043231,GO:0005643,GO:0006913; Complete thirteen term entries; exact IDs in request URL, including all returned children and relation types | supports | All13 native active entries, definitions, synonym scopes and typed children were read. Nuclear lumen is enclosed by the inner membrane and contains nuclear chromosome/nucleolus parts; nucleus has the exact cell-nucleus synonym and organelle parent. Membrane includes embedded/attached proteins; the nuclear net is not equated with lamina-associated nucleoplasmic reticulum. |
| root35-sources-pan2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1091/mbc.11.7.2445%22; Complete native MED bibliographic identity and abstractText | supports | Exact DOI 10.1091/mbc.11.7.2445, PMID 10888680, title, authors, year and complete abstract checked. Native metadata and abstract scope are distinguished from the separately read full-text sections. |
| root35-sources-luo2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1080/21541248.2021.1993714%22; Complete native MED bibliographic identity and abstractText | supports | Exact DOI 10.1080/21541248.2021.1993714, PMID 34689711, title, authors, year and complete abstract checked. Native metadata and abstract scope are distinguished from the separately read full-text sections. |
| root35-sources-aitchison2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1534/genetics.111.127803%22; Complete native MED bibliographic identity and abstractText | supports | Exact DOI 10.1534/genetics.111.127803, PMID 22419078, title, authors, year and complete abstract checked. Native metadata and abstract scope are distinguished from the separately read full-text sections. |
| root35-sources-GO0005634-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005634/ancestors?relations=is_a; Complete result requested with relations=is_a | supports | The is_a-only ancestor list includes the declared parent. Parthood is supported separately by explicitly typed native term children. |
| root35-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxId, scientificName, rank, lineage and otherNames | supports | ENA confirms Saccharomyces cerevisiae4932 at species rank. This does not measure nuclear occurrence frequency or identify a particular experimental strain. |
| nuclear-agent-pan2000-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/; Verified title/DOI; complete Methods sec3/4, Results sec11/13/15 with embedded captions, Discussion sec19. Remaining sections, figures as pixels and supplements not certified read | supports | YEF473-derived strains and L40, two-hybrid/co-purification, C-terminal mapping and localization establish Nvj1/Vac8 association at nucleus–vacuole junctions. The authors infer direct interaction but explicitly acknowledge a remote indirect-interaction possibility; no purified binary reconstitution is claimed. The nucleus record cites only the bounded junction example, not a universal formation mechanism. |
| nuclear-agent-aitchison2012-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC3296253/; Verified title/DOI; complete s1 Structure/Composition, s2 Overall Composition and s10 Soluble Phase including embedded captions. Secondary review; source figure pixels and other sections not certified read | supports | The review distinguishes the NPC embedded in the nuclear envelope from soluble transport factors and explains regulated transport through its central channel. NPC architecture and transport support the target four descriptive edges, without asserting a complete nucleoporin inventory or specific assembly-essentiality test. |
| root35-sources-lu2022-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC9707532/; Verified title, DOI and citation_author metadata; complete Results s0002-s2002 including Fig2 caption and Discussion s0003 including Fig5 caption. Remaining Results/supplements/movies and figure pixels not certified read | supports | The article is by Michelle S Lu and David G Drubin, not Luo et al. Results use endogenous tagged Cdc42/Nvj1 imaging and report cell-cycle-dependent association; Discussion treats further functional roles as hypotheses. The target cites the paper bibliographically and does not add these unproven mechanisms. |
| schema-result | just validate data/structures/membrane_organelle/nucleus.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/nucleus.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/nucleus.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleus-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/nucleus.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleus-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleus-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/nucleus.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Source inspection is limited to the explicit locators. No supplementary datasets or raw experimental data were reanalyzed; a cited review remains secondary evidence.
- The Pan paper inferred direct association from two-hybrid/copurification and acknowledges a remote indirect possibility. Its qualitative junction example is not purified binary reconstitution or a nucleus-formation requirement. COMMON is not a quantified prevalence.
- Lu2022 XML returned HTTP500; the genuine PMC HTML was independently verified and the stated sections read. No source figure pixels, movies or supplements were inspected for this target.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes one bundle for every uncovered record, including honest zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025110Z-nucleus-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Nucleus identity and source review
started_at: '2026-10-22T02:36:40Z'
finished_at: '2026-10-22T02:51:10Z'
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
summary: Nucleus identity and descriptive envelope/transport scope are supported.
  One minor finding corrects the Lu and Drubin bibliographic attribution.
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
  - path: data/structures/membrane_organelle/nucleus.yaml
    sha256: 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d
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
- target_id: GO:0005634
  path: data/structures/membrane_organelle/nucleus.yaml
  label: nucleus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nucleus.yaml
    role: maintained scientific record
scope:
  description: 'Entire single record: identity, hierarchy, components, taxonomy, functions,
    every asserted graph edge, discussions and image provenance where present.'
  selection: Target 9 of batch35 in strict uncovered path order from fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005634
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005634
  command: just validate data/structures/membrane_organelle/nucleus.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005634
  command: just validate-strict data/structures/membrane_organelle/nucleus.yaml --out
    /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleus-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005634
  summary: No claimed expression-module membership or expression cluster used as mechanistic
    evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005634
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root35-sources-go
  - root35-sources-pan2000-meta
  - root35-sources-luo2022-meta
  - root35-sources-aitchison2012-meta
  - root35-sources-GO0005634-isa
  - root35-sources-tax4932
  - nuclear-agent-pan2000-pmc
  - nuclear-agent-aitchison2012-pmc
  - root35-sources-lu2022-pmc
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005634
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005634
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
  - GO:0005634
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
  - GO:0005634
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
  - GO:0005634
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
  - GO:0005634
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
  reference: data/structures/membrane_organelle/nucleus.yaml
  locator: Entire maintained target, every graph edge, component, discussion, image
    descriptor and historical event
  accessed_at: '2026-10-22T02:43:59Z'
  support: context_only
  summary: Complete scientific target read; no scientific edits or status promotion.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent and ComponentTypeEnum/ComponentRoleEnum
  accessed_at: '2026-10-22T02:43:59Z'
  support: context_only
  summary: Component identities, formation essentiality and constituent role are assessed
    separately. OTHER does not assert a chemical lipid category; exact named protein
    complexes have their own permitted type.
- evidence_id: root35-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031981,GO:0070013,GO:0005634,GO:0005637,GO:0000228,GO:0005730,GO:0005622,GO:0005635,GO:0016020,GO:0044195,GO:0043231,GO:0005643,GO:0006913
  locator: Complete thirteen term entries; exact IDs in request URL, including all
    returned children and relation types
  accessed_at: '2026-10-22T02:38:32.844110Z'
  support: supports
  summary: All13 native active entries, definitions, synonym scopes and typed children
    were read. Nuclear lumen is enclosed by the inner membrane and contains nuclear
    chromosome/nucleolus parts; nucleus has the exact cell-nucleus synonym and organelle
    parent. Membrane includes embedded/attached proteins; the nuclear net is not equated
    with lamina-associated nucleoplasmic reticulum.
  snapshot_sha256: eaa926192f182f2fc353a0d661c7992bf361c1f369fbf365387fef951f774c37
- evidence_id: root35-sources-pan2000-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1091/mbc.11.7.2445%22
  locator: Complete native MED bibliographic identity and abstractText
  accessed_at: '2026-10-22T02:38:33.743979Z'
  support: supports
  summary: Exact DOI 10.1091/mbc.11.7.2445, PMID 10888680, title, authors, year and
    complete abstract checked. Native metadata and abstract scope are distinguished
    from the separately read full-text sections.
  snapshot_sha256: 8fd13375de562999edc00fab8fd5103111b6f6e00b90719774f0bf6f17fa1fe6
- evidence_id: root35-sources-luo2022-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1080/21541248.2021.1993714%22
  locator: Complete native MED bibliographic identity and abstractText
  accessed_at: '2026-10-22T02:38:34.236659Z'
  support: supports
  summary: Exact DOI 10.1080/21541248.2021.1993714, PMID 34689711, title, authors,
    year and complete abstract checked. Native metadata and abstract scope are distinguished
    from the separately read full-text sections.
  snapshot_sha256: f83dac724f8ef7a9e79c1c7163244685a36273b4ed73176c66811108863d8e30
- evidence_id: root35-sources-aitchison2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1534/genetics.111.127803%22
  locator: Complete native MED bibliographic identity and abstractText
  accessed_at: '2026-10-22T02:38:34.266872Z'
  support: supports
  summary: Exact DOI 10.1534/genetics.111.127803, PMID 22419078, title, authors, year
    and complete abstract checked. Native metadata and abstract scope are distinguished
    from the separately read full-text sections.
  snapshot_sha256: 8e96fed817fa00c3a040951687f08a2de66b23f489467db85f87f9abbf43a13b
- evidence_id: root35-sources-GO0005634-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005634/ancestors?relations=is_a
  locator: Complete result requested with relations=is_a
  accessed_at: '2026-10-22T02:38:32.844787Z'
  support: supports
  summary: The is_a-only ancestor list includes the declared parent. Parthood is supported
    separately by explicitly typed native term children.
  snapshot_sha256: b91ce8b43246ceaa126f60dd5edb560810685ac917f2f27b9b8cd7bf34e91091
- evidence_id: root35-sources-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T02:38:32.844980Z'
  support: supports
  summary: ENA confirms Saccharomyces cerevisiae4932 at species rank. This does not
    measure nuclear occurrence frequency or identify a particular experimental strain.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: nuclear-agent-pan2000-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/
  locator: Verified title/DOI; complete Methods sec3/4, Results sec11/13/15 with embedded
    captions, Discussion sec19. Remaining sections, figures as pixels and supplements
    not certified read
  accessed_at: '2026-10-22T02:39:21.042109Z'
  support: supports
  summary: YEF473-derived strains and L40, two-hybrid/co-purification, C-terminal
    mapping and localization establish Nvj1/Vac8 association at nucleus–vacuole junctions.
    The authors infer direct interaction but explicitly acknowledge a remote indirect-interaction
    possibility; no purified binary reconstitution is claimed. The nucleus record
    cites only the bounded junction example, not a universal formation mechanism.
  snapshot_sha256: 21ca47f90e10c08bef74688b1d99cb48079becd20b5613d7fc569a70de30001c
- evidence_id: nuclear-agent-aitchison2012-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC3296253/
  locator: Verified title/DOI; complete s1 Structure/Composition, s2 Overall Composition
    and s10 Soluble Phase including embedded captions. Secondary review; source figure
    pixels and other sections not certified read
  accessed_at: '2026-10-22T02:39:20.762860Z'
  support: supports
  summary: The review distinguishes the NPC embedded in the nuclear envelope from
    soluble transport factors and explains regulated transport through its central
    channel. NPC architecture and transport support the target four descriptive edges,
    without asserting a complete nucleoporin inventory or specific assembly-essentiality
    test.
  snapshot_sha256: 1cb55823b5933be54b9daeab10063858f1cbc7e828492860416bca77af77bc5b
- evidence_id: root35-sources-lu2022-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC9707532/
  locator: Verified title, DOI and citation_author metadata; complete Results s0002-s2002
    including Fig2 caption and Discussion s0003 including Fig5 caption. Remaining
    Results/supplements/movies and figure pixels not certified read
  accessed_at: '2026-10-22T02:39:25.690417Z'
  support: supports
  summary: The article is by Michelle S Lu and David G Drubin, not Luo et al. Results
    use endogenous tagged Cdc42/Nvj1 imaging and report cell-cycle-dependent association;
    Discussion treats further functional roles as hypotheses. The target cites the
    paper bibliographically and does not add these unproven mechanisms.
  snapshot_sha256: ccdbc6c63f12ff9c10898bfc9bed0d899b8780a54b2d4b3af438e650d4633c4c
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/nucleus.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:42Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/nucleus.yaml'
  snapshot_sha256: 718391d460c3748473395ff41b810404b7bf529bd5a42d5d73848c73b05a0a73
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/nucleus.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleus-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:43Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/nucleus.yaml\
    \ --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleus-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleus-strict.tsv"
  snapshot_sha256: 74f156ae648d1d6e09f08970367d410346ef9f77d03b17cae6aea70fd499dd20
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/nucleus.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
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
  topic: Exact nucleus and parts
  outcome: supported
  target_ids:
  - GO:0005634
  summary: Native definition, exact synonym and is_a-only ancestry support the maintained
    nucleus. Envelope/lumen/pore parthood and the inner-membrane-enclosed volume remain
    distinct. The shortened definition is a bounded generic definition, not a new
    universal claim that every specialized nucleus replicates DNA.
  evidence_ids:
  - record
  - root35-sources-go
  - root35-sources-GO0005634-isa
- assessment_id: component
  area: grounding
  topic: Exact pore-complex component
  outcome: supported
  target_ids:
  - GO:0005634
  summary: GO0005643 explicitly denotes a protein complex; PROTEIN_COMPLEX is an appropriate
    component type. UNKNOWN formation essentiality does not equate transport function
    with necessity for forming the entire nucleus. No single organism protein instance
    is substituted for the whole NPC.
  evidence_ids:
  - record
  - policy
  - root35-sources-go
  - nuclear-agent-aitchison2012-pmc
- assessment_id: scope
  area: scope
  topic: Budding-yeast example
  outcome: supported
  target_ids:
  - GO:0005634
  summary: The canonical example and qualitative distribution note are specifically
    about nucleus–vacuole contacts in budding yeast. The primary source supports this
    bounded context, while neither native taxonomy nor this experiment supplies a
    measured species-wide prevalence.
  evidence_ids:
  - record
  - root35-sources-tax4932
  - nuclear-agent-pan2000-pmc
- assessment_id: graph
  area: graph
  topic: Four envelope and transport edges
  outcome: supported
  target_ids:
  - GO:0005634
  summary: 'Every NONMECHANISTIC edge is supported at its declared level: envelope
    bounds lumen/encloses nucleus, pore spans the envelope, and pore mediates exchange.
    No detailed molecular pore assembly pathway, energy-free whole transport claim
    or blanket NPC-protein inventory is asserted.'
  evidence_ids:
  - record
  - root35-sources-go
  - nuclear-agent-aitchison2012-pmc
- assessment_id: bibliography
  area: evidence
  topic: Exact Lu and Drubin attribution
  outcome: concern
  target_ids:
  - GO:0005634
  summary: The target bibliography misspells the first author and uses et al for a
    two-author paper. Native MED metadata and the genuine primary article independently
    identify Lu and Drubin. This is a bounded bibliographic error, not a wrong organelle
    or demonstrated false mechanism.
  evidence_ids:
  - record
  - root35-sources-luo2022-meta
  - root35-sources-lu2022-pmc
- assessment_id: coverage
  area: completeness
  topic: Bounded nucleus inventory
  outcome: supported
  target_ids:
  - GO:0005634
  summary: All maintained fields and the open molecular-cohort TODO were reviewed.
    The TODO does not claim a complete chromatin, nucleolar or nuclear-envelope inventory.
    No forced protein examples or unsupported molecular cohort grounding are added.
  evidence_ids:
  - record
  - root35-sources-go
  - nuclear-agent-aitchison2012-pmc
  - root35-sources-lu2022-pmc
findings:
- finding_id: F1
  issue_key: nucleus-lu-drubin-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the Lu and Drubin citation attribution
  description: evidence[5].notes attributes DOI10.1080/21541248.2021.1993714 to Luo
    et al2022. Both native MED metadata and the primary article identify Michelle
    S Lu and David G Drubin as its two authors. The DOI, title and2022 volume year
    otherwise match.
  target_ids:
  - GO:0005634
  field_paths:
  - evidence[5].notes
  evidence_ids:
  - record
  - root35-sources-luo2022-meta
  - root35-sources-lu2022-pmc
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nucleus.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact source identity
  native_severity: minor
  normalization_reason: Minor bounded bibliographic attribution correction; organelle
    identity and cited biological scope remain sound.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005634
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nucleus.yaml
    role: maintained scientific record
  description: Correct the evidence note to Lu and Drubin(2022), retaining the verified
    DOI/title and treating the article functional proposals as proposals.
  acceptance_checks:
  - Verify exact authors/title/DOI against the native source.
  - After separately authorized curation, run the focused schema and strict validation
    recipes.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Source inspection is limited to the explicit locators. No supplementary datasets
  or raw experimental data were reanalyzed; a cited review remains secondary evidence.
- The Pan paper inferred direct association from two-hybrid/copurification and acknowledges
  a remote indirect possibility. Its qualitative junction example is not purified
  binary reconstitution or a nucleus-formation requirement. COMMON is not a quantified
  prevalence.
- Lu2022 XML returned HTTP500; the genuine PMC HTML was independently verified and
  the stated sections read. No source figure pixels, movies or supplements were inspected
  for this target.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes one bundle for every uncovered record, including
  honest zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
