# V1 sector boundary, coupling and subunit-completeness review

- Review: 20261021T091354Z-vacuolar-proton-transporting-v-type-atpase-v1-domain-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:50:58Z
- Finished UTC: 2026-10-21T09:13:54Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

V1 identity, hierarchy, yeast scope and intact-enzyme function graph are supported. One minor completeness issue remains: the cited known subunits are deferred solely pending family identifiers, despite available label-only representation.

## Scope And Provenance

Entire single target, native ontology/taxon/predicate scope and exact cited review identities; all maintained function/graph/discussion claims and known-subunit deferral assessed.

Selection: Ninth selected target in batch fourteen, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0000221 | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml | maintained | vacuolar proton-transporting V-type ATPase, V1 domain |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0000221 | Focused validator passed. |
| Focused native strict | passed | True | GO:0000221 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0000221 | 8 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0000221 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0000221 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0000221 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0000221 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0000221 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0000221 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### V1 sector versus whole enzyme

identity: supported. Targets: GO:0000221.

Exact GO identity, synonym, kind/category, generic is_a parent and whole-enzyme part_of placement are supported. V0 and V1 are distinct sectors of one rotary ATPase, not synonyms for the complete pump.

### Yeast vacuolar example

scope: supported. Targets: GO:0000221.

The S.cerevisiae canonical example and qualitative COMMON occurrence are supported by the cited review. This does not assert a population-frequency measurement or that every yeast V-ATPase isoform occupies the vacuole; Vph1/Stv1 localization distinctions remain relevant.

### Function within assembled enzyme

evidence: supported. Targets: GO:0000221.

The cytosolic V1 sector hydrolyzes ATP and drives rotation coupled to V0 in the intact enzyme. The record correctly avoids assigning the complete proton-pump molecular-function term to isolated V1; dissociated V1 activity is regulated and not assumed equivalent.

### Supported nonmechanistic topology and coupling

graph: supported. Targets: GO:0000221.

Both sectors are part_of the whole enzyme; V1 ATP hydrolysis and V1-to-V0 coupling are supported. The RO enables relation is compatible with catalysis wording. NONMECHANISTIC accurately limits this to sector function, not a complete molecular rotation/contact sequence.

### Known members deferred solely for family grounding

completeness: concern. Targets: GO:0000221.

The record has no component rows and explicitly says narrower family curation is needed before asserting subunit components. Kane already names A, B, C, D, E, F, G and H. Exact family CURIEs and copy numbers require their own checks, but the schema permits evidence-backed label-only constituents. Deferring every known member for this reason leaves a specific, resolvable composition gap.

### Composition does not prove assembly necessity

scope: supported. Targets: GO:0000221.

Source-supported constituent labels must not automatically receive ESSENTIAL. The schema asks whether the structure forms without the component. Kane distinguishes activity from assembly and reports an assembled inactive enzyme lacking H. Dedicated assembly factors are not final-sector constituents; freely dissociated sectors and whole-enzyme assembly are also separate scopes.

### Review-tier evidence and historical resolution

provenance: supported. Targets: GO:0000221.

The maintained Kane bibliography is exact and its relevant body is readable. The resolved sector-boundary discussion remains supported; the historical replacement of Zhao evidence is not undone. No literature-review synthesis is mislabeled as direct primary experimentation.

## Findings

### F1: Represent known V1 subunits without waiting for exact family CURIEs

minor / open / confirmed; issue key: v1-known-subunits-deferred-for-family-grounding.

The open v1_subunit_grounding_todo rationale makes family grounding a prerequisite to all subunit-level components. Yet the cited Kane2006 review explicitly identifies yeast V1 subunits A, B, C, D, E, F, G and H. Evidence-backed label-only component rows are allowed and can retain unresolved family identifiers and copy numbers. Revise the blanket deferral and represent at least the established core membership, preserving source/taxon boundaries. This finding concerns a concrete known inventory and the stated blocking rationale, not a general requirement to populate every optional field.

## Recommended Actions And Acceptance Checks

### A1

During authorized curation, add source-backed label-only V1 subunit components and narrow the TODO to unresolved family mappings/copy numbers.

- Use the cited review at its actual review evidence tier; retain yeast and vacuolar-isoform boundaries.
- Distinguish final constituents from dedicated assembly factors; do not assign ESSENTIAL from membership or catalytic activity.
- Leave unverified family CURIEs and numerical stoichiometry unresolved rather than borrowing broad domains or newer unsupported counts.
- Run the required focused schema, strict-reference and review validations.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml; Entire maintained YAML including all imported participants, component examples, functions, graph edges, discussions and history | context_only | All fields were read after fresh native inspection; the maintained target and PROPOSED state are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, CausalNode and source-specific ComplexComposition contracts; essentiality definition; docs/CURATION.md assembly-versus-function guidance and review checklist | context_only | Component family identity, concrete protein identity and source-specific assembly membership are separate. Essentiality asks whether the structure forms without the component; membership and activity do not establish it. Optional fields are not mandatory. CausalNode permits protein complexes; its xrefs contract does not inherit the top-level record equivalence restriction. |
| v1-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0000221,GO:0016471,GO:0033180,GO:0046961; All returned native GO term identities, definitions/comments, synonyms/status and hierarchy; obsolete whole-pump activity in history is not a current V1 function claim | supports | The active vacuolar V1 identity has the exact maintained synonym, generic sector is_a parent and part_of relation to vacuolar V-ATPase. Complementary sector and membrane/activity terms retain their own scopes. |
| v1-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete native taxon identity, rank and lineage | supports | Native taxonomy identifies Saccharomyces cerevisiae, species4932, exactly as maintained. |
| v1-agent-doi-MMBR_70_1_177-191_2006 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/MMBR.70.1.177-191.2006; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies The where, when, and how of organelle acidification by the yeast vacuolar H+-ATPase. Authors: Kane PM.; PMID 16524922; DOI 10.1128/mmbr.70.1.177-191.2006. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| v1-agent-kane2006-legacy-html | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1393255/; Genuine PMC1393255 HTML: Introduction sec1; Structure of the Yeast V-ATPase sec3/Figure1 caption; Catalytic Mechanism sec4; Assembly of Partial Complexes sec9; Early Steps in Biosynthesis/Assembly sec10/Figure2 caption; a-isoform roles sec11; Reversible Disassembly sec14/Figure3 caption. These listed sections were read; not all physiology/regulation sections. | supports | Kane2006 is a literature review, not a new defining experiment. It specifies yeast V1 subunitsA–H and V0 subunitsa,c,c-prime,c-double-prime,d,e; distinguishes vacuolar Vph1 from primarily Golgi/endosomal Stv1 and final constituents from dedicated Vma12/21/22 assembly factors. It describes coupled rotary transport and reversible dissociation. |
| v1-agent-doi-nrm2272 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrm2272; Exact bibliographic fields, article type and available abstract | supports | Native metadata identifies Vacuolar ATPases: rotary proton pumps in physiology and pathophysiology. Authors: Forgac M.; PMID 17912264; DOI 10.1038/nrm2272. Bibliographic identity and available abstract only; not a substitute for inspected article body. |
| v1-agent-forgac2007-publisher | https://www.nature.com/articles/nrm2272; Publisher article identity, complete Key Points and Abstract; remaining subscription-preview body not claimed read | supports | Forgac2007 is a review. Its publisher Key Points and Abstract explicitly place ATP hydrolysis in V1 and coupled rotary proton transport in V0. The accessible page is a preview, not the complete article body. |
| v1-agent-ro-native | https://raw.githubusercontent.com/oborel/obo-relations/master/ro.json; Exact RO0002327 object, label, definition and synonyms within native oborel ro.json snapshot | supports | RO0002327 is enables and has catalyzes/executes synonyms. The maintained catalyses predicate is consistent with that activity relation; it is not a binding assertion. |
| schema-result | just validate data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml |
| strict-result | just validate-strict data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/vacuolar_proton_transporting_v_type_atpase_v1_domain-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml --out /private/tmp/cellstructure-batch14-20261021-g0felisv/vacuolar_proton_transporting_v_type_atpase_v1_domain-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/vacuolar_proton_transporting_v_type_atpase_v1_domain-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 8 of8 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Kane2006 is review-tier synthesis. The listed claim-bearing sections and figure captions were read; underlying primary studies, figure pixels and every unrelated physiology/regulation section were not independently audited.
- The completeness action supports labels and membership, not automatically exact protein families, UniProt accessions, contemporary ring/stalk stoichiometry or assembly essentiality. These require bounded follow-up.
- Yeast a-subunit isoforms are compartment-specific; the canonical vacuolar example does not license assigning primarily Golgi/endosomal Stv1 to every vacuolar complex.
- Initial PMC routes included200 HTML challenge pages,500 JATS and404 S3 responses; a genuine legacy PMC full article was recovered and is the actual body evidence.
- Forgac2007 was read at publisher Key Points and Abstract level only. The apparent PDF route returned the same HTML preview. No full Forgac body or new primary rotation experiment is claimed.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Fresh native schema/strict gates0 and all12 inspection input hashes verified. No record edits, save or scientific-status promotion.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T091354Z-vacuolar-proton-transporting-v-type-atpase-v1-domain-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: V1 sector boundary, coupling and subunit-completeness review
started_at: '2026-10-21T08:50:58Z'
finished_at: '2026-10-21T09:13:54Z'
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
summary: 'V1 identity, hierarchy, yeast scope and intact-enzyme function graph are
  supported. One minor completeness issue remains: the cited known subunits are deferred
  solely pending family identifiers, despite available label-only representation.'
source:
  git_revision: 99692a3d5f16a7dcd6db7e3811344c299a977b81
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
  - path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    sha256: fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22
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
- target_id: GO:0000221
  path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  label: vacuolar proton-transporting V-type ATPase, V1 domain
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
scope:
  description: Entire single target, native ontology/taxon/predicate scope and exact
    cited review identities; all maintained function/graph/discussion claims and known-subunit
    deferral assessed.
  selection: Ninth selected target in batch fourteen, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0000221
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just validate data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just validate-strict data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/vacuolar_proton_transporting_v_type_atpase_v1_domain-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0000221
  summary: 8 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0000221
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - v1-agent-go
  - v1-agent-tax-4932
  - v1-agent-doi-MMBR_70_1_177-191_2006
  - v1-agent-kane2006-legacy-html
  - v1-agent-doi-nrm2272
  - v1-agent-forgac2007-publisher
  - v1-agent-ro-native
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0000221
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch14 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  locator: Entire maintained YAML including all imported participants, component examples,
    functions, graph edges, discussions and history
  accessed_at: '2026-10-21T09:12:55Z'
  support: context_only
  summary: All fields were read after fresh native inspection; the maintained target
    and PROPOSED state are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, CausalNode and source-specific ComplexComposition
    contracts; essentiality definition; docs/CURATION.md assembly-versus-function
    guidance and review checklist
  accessed_at: '2026-10-21T09:12:55Z'
  support: context_only
  summary: Component family identity, concrete protein identity and source-specific
    assembly membership are separate. Essentiality asks whether the structure forms
    without the component; membership and activity do not establish it. Optional fields
    are not mandatory. CausalNode permits protein complexes; its xrefs contract does
    not inherit the top-level record equivalence restriction.
- evidence_id: v1-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0000221,GO:0016471,GO:0033180,GO:0046961
  locator: All returned native GO term identities, definitions/comments, synonyms/status
    and hierarchy; obsolete whole-pump activity in history is not a current V1 function
    claim
  accessed_at: '2026-10-21T09:01:32.597312Z'
  support: supports
  summary: The active vacuolar V1 identity has the exact maintained synonym, generic
    sector is_a parent and part_of relation to vacuolar V-ATPase. Complementary sector
    and membrane/activity terms retain their own scopes.
  snapshot_sha256: 9bbbd96a8e65f44352a83fb48dce584787fddff024e8bea38675d1fa43435d75
- evidence_id: v1-agent-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete native taxon identity, rank and lineage
  accessed_at: '2026-10-21T09:01:32.615220Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae, species4932, exactly
    as maintained.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: v1-agent-doi-MMBR_70_1_177-191_2006
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/MMBR.70.1.177-191.2006
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:32.811125Z'
  support: supports
  summary: 'Native metadata identifies The where, when, and how of organelle acidification
    by the yeast vacuolar H+-ATPase. Authors: Kane PM.; PMID 16524922; DOI 10.1128/mmbr.70.1.177-191.2006.
    Bibliographic identity and available abstract only; not a substitute for inspected
    article body.'
  snapshot_sha256: 8eac776a8869a547a37502fd79db9798cb0c58b42f84374f991ffb3f499e303e
- evidence_id: v1-agent-kane2006-legacy-html
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1393255/
  locator: 'Genuine PMC1393255 HTML: Introduction sec1; Structure of the Yeast V-ATPase
    sec3/Figure1 caption; Catalytic Mechanism sec4; Assembly of Partial Complexes
    sec9; Early Steps in Biosynthesis/Assembly sec10/Figure2 caption; a-isoform roles
    sec11; Reversible Disassembly sec14/Figure3 caption. These listed sections were
    read; not all physiology/regulation sections.'
  accessed_at: '2026-10-21T09:03:55.796676Z'
  support: supports
  summary: Kane2006 is a literature review, not a new defining experiment. It specifies
    yeast V1 subunitsA–H and V0 subunitsa,c,c-prime,c-double-prime,d,e; distinguishes
    vacuolar Vph1 from primarily Golgi/endosomal Stv1 and final constituents from
    dedicated Vma12/21/22 assembly factors. It describes coupled rotary transport
    and reversible dissociation.
  snapshot_sha256: 66b78d72bc8e0b5b730f8b79113808286406293c699ac59ba9631ec92151ccdc
- evidence_id: v1-agent-doi-nrm2272
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrm2272
  locator: Exact bibliographic fields, article type and available abstract
  accessed_at: '2026-10-21T09:01:32.684552Z'
  support: supports
  summary: 'Native metadata identifies Vacuolar ATPases: rotary proton pumps in physiology
    and pathophysiology. Authors: Forgac M.; PMID 17912264; DOI 10.1038/nrm2272. Bibliographic
    identity and available abstract only; not a substitute for inspected article body.'
  snapshot_sha256: 55c0c1a8752adaa99a6255c1a99ee11cf7e2202a38e78c8fc936d05da82548f4
- evidence_id: v1-agent-forgac2007-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrm2272
  locator: Publisher article identity, complete Key Points and Abstract; remaining
    subscription-preview body not claimed read
  accessed_at: '2026-10-21T09:03:00.171816Z'
  support: supports
  summary: Forgac2007 is a review. Its publisher Key Points and Abstract explicitly
    place ATP hydrolysis in V1 and coupled rotary proton transport in V0. The accessible
    page is a preview, not the complete article body.
  snapshot_sha256: f0ca31d8d16c2ad45ecaece0e5ecd6d3f62acdfa5a76f268be9c3de5d19bd902
- evidence_id: v1-agent-ro-native
  kind: authority
  reference: https://raw.githubusercontent.com/oborel/obo-relations/master/ro.json
  locator: Exact RO0002327 object, label, definition and synonyms within native oborel
    ro.json snapshot
  accessed_at: '2026-10-21T09:05:16.603250Z'
  support: supports
  summary: RO0002327 is enables and has catalyzes/executes synonyms. The maintained
    catalyses predicate is consistent with that activity relation; it is not a binding
    assertion.
  snapshot_sha256: 17eab8be4f47c73d2905ba45752154ae8e2e7b0bf03ba3cc62a326b42a38e5a5
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:51:04Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml'
  snapshot_sha256: bac437eef296e12c629273c25d9b3ae7a88fe850edc61bc009ecd8cef6345d8a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    --out /private/tmp/cellstructure-batch14-20261021-g0felisv/vacuolar_proton_transporting_v_type_atpase_v1_domain-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:51:09Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml\
    \ --out /private/tmp/cellstructure-batch14-20261021-g0felisv/vacuolar_proton_transporting_v_type_atpase_v1_domain-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch14-20261021-g0felisv/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch14-20261021-g0felisv/vacuolar_proton_transporting_v_type_atpase_v1_domain-strict.tsv"
  snapshot_sha256: 7342cc981753555033eab7e2e9346d27f966f797e6a4fbdfe4291b5e4b8d643a
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:12:55Z'
  support: supports
  summary: '8 of8 collected target identifiers returned OK at the unchanged base.
    Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec
  accessed_at: '2026-10-19T07:38:12Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 7b6165ba8532d080a336f7a5a4c29b456fdf7182dd596410b700dfe60af61a06
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-19T07:29:37Z'
  support: supports
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: b98e3eecd58a81fa46033e6baca6977811a439f119b943fd5d9931964adb2680
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad
  accessed_at: '2026-10-19T07:32:39Z'
  support: supports
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: 2a1330c26aac5bd248a2fd3a3a7b9c882d2b3bb202365c555e5d6415d1c2203d
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-19T07:29:45Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256
    below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4
  accessed_at: '2026-10-19T08:04:01Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  snapshot_sha256: 7cb413edccc92ee6ce79a32cd2b96a59bc4da37f2cb7b326eaca51a64f723cfb
assessments:
- assessment_id: identity
  area: identity
  topic: V1 sector versus whole enzyme
  outcome: supported
  target_ids:
  - GO:0000221
  summary: Exact GO identity, synonym, kind/category, generic is_a parent and whole-enzyme
    part_of placement are supported. V0 and V1 are distinct sectors of one rotary
    ATPase, not synonyms for the complete pump.
  evidence_ids:
  - v1-agent-go
  - v1-agent-kane2006-legacy-html
  - record
- assessment_id: organism
  area: scope
  topic: Yeast vacuolar example
  outcome: supported
  target_ids:
  - GO:0000221
  summary: The S.cerevisiae canonical example and qualitative COMMON occurrence are
    supported by the cited review. This does not assert a population-frequency measurement
    or that every yeast V-ATPase isoform occupies the vacuole; Vph1/Stv1 localization
    distinctions remain relevant.
  evidence_ids:
  - v1-agent-tax-4932
  - v1-agent-kane2006-legacy-html
  - record
- assessment_id: function
  area: evidence
  topic: Function within assembled enzyme
  outcome: supported
  target_ids:
  - GO:0000221
  summary: The cytosolic V1 sector hydrolyzes ATP and drives rotation coupled to V0
    in the intact enzyme. The record correctly avoids assigning the complete proton-pump
    molecular-function term to isolated V1; dissociated V1 activity is regulated and
    not assumed equivalent.
  evidence_ids:
  - v1-agent-go
  - v1-agent-kane2006-legacy-html
  - v1-agent-doi-nrm2272
  - v1-agent-forgac2007-publisher
  - v1-agent-ro-native
  - record
- assessment_id: graph
  area: graph
  topic: Supported nonmechanistic topology and coupling
  outcome: supported
  target_ids:
  - GO:0000221
  summary: Both sectors are part_of the whole enzyme; V1 ATP hydrolysis and V1-to-V0
    coupling are supported. The RO enables relation is compatible with catalysis wording.
    NONMECHANISTIC accurately limits this to sector function, not a complete molecular
    rotation/contact sequence.
  evidence_ids:
  - v1-agent-go
  - v1-agent-kane2006-legacy-html
  - v1-agent-doi-nrm2272
  - v1-agent-forgac2007-publisher
  - v1-agent-ro-native
  - record
- assessment_id: known-components
  area: completeness
  topic: Known members deferred solely for family grounding
  outcome: concern
  target_ids:
  - GO:0000221
  summary: The record has no component rows and explicitly says narrower family curation
    is needed before asserting subunit components. Kane already names A, B, C, D,
    E, F, G and H. Exact family CURIEs and copy numbers require their own checks,
    but the schema permits evidence-backed label-only constituents. Deferring every
    known member for this reason leaves a specific, resolvable composition gap.
  evidence_ids:
  - v1-agent-kane2006-legacy-html
  - v1-agent-go
  - record
  - policy
- assessment_id: assembly-boundaries
  area: scope
  topic: Composition does not prove assembly necessity
  outcome: supported
  target_ids:
  - GO:0000221
  summary: Source-supported constituent labels must not automatically receive ESSENTIAL.
    The schema asks whether the structure forms without the component. Kane distinguishes
    activity from assembly and reports an assembled inactive enzyme lacking H. Dedicated
    assembly factors are not final-sector constituents; freely dissociated sectors
    and whole-enzyme assembly are also separate scopes.
  evidence_ids:
  - v1-agent-kane2006-legacy-html
  - policy
  - record
- assessment_id: source-state
  area: provenance
  topic: Review-tier evidence and historical resolution
  outcome: supported
  target_ids:
  - GO:0000221
  summary: The maintained Kane bibliography is exact and its relevant body is readable.
    The resolved sector-boundary discussion remains supported; the historical replacement
    of Zhao evidence is not undone. No literature-review synthesis is mislabeled as
    direct primary experimentation.
  evidence_ids:
  - v1-agent-doi-MMBR_70_1_177-191_2006
  - v1-agent-kane2006-legacy-html
  - v1-agent-doi-nrm2272
  - v1-agent-forgac2007-publisher
  - v1-agent-ro-native
  - record
findings:
- finding_id: F1
  issue_key: v1-known-subunits-deferred-for-family-grounding
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Represent known V1 subunits without waiting for exact family CURIEs
  description: The open v1_subunit_grounding_todo rationale makes family grounding
    a prerequisite to all subunit-level components. Yet the cited Kane2006 review
    explicitly identifies yeast V1 subunits A, B, C, D, E, F, G and H. Evidence-backed
    label-only component rows are allowed and can retain unresolved family identifiers
    and copy numbers. Revise the blanket deferral and represent at least the established
    core membership, preserving source/taxon boundaries. This finding concerns a concrete
    known inventory and the stated blocking rationale, not a general requirement to
    populate every optional field.
  target_ids:
  - GO:0000221
  field_paths:
  - components
  - discussions[discussion_id=v1_subunit_grounding_todo].rationale
  evidence_ids:
  - v1-agent-kane2006-legacy-html
  - v1-agent-go
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Composition
    and completeness
  native_severity: minor
  normalization_reason: The sector identity, topology and functions are correct. This
    is a non-blocking recoverable composition gap caused by an unnecessary grounding
    prerequisite, not wrong structure identity or a demand for exact stoichiometry.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0000221
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained scientific record
  description: During authorized curation, add source-backed label-only V1 subunit
    components and narrow the TODO to unresolved family mappings/copy numbers.
  acceptance_checks:
  - Use the cited review at its actual review evidence tier; retain yeast and vacuolar-isoform
    boundaries.
  - Distinguish final constituents from dedicated assembly factors; do not assign
    ESSENTIAL from membership or catalytic activity.
  - Leave unverified family CURIEs and numerical stoichiometry unresolved rather than
    borrowing broad domains or newer unsupported counts.
  - Run the required focused schema, strict-reference and review validations.
limitations:
- Kane2006 is review-tier synthesis. The listed claim-bearing sections and figure
  captions were read; underlying primary studies, figure pixels and every unrelated
  physiology/regulation section were not independently audited.
- The completeness action supports labels and membership, not automatically exact
  protein families, UniProt accessions, contemporary ring/stalk stoichiometry or assembly
  essentiality. These require bounded follow-up.
- Yeast a-subunit isoforms are compartment-specific; the canonical vacuolar example
  does not license assigning primarily Golgi/endosomal Stv1 to every vacuolar complex.
- Initial PMC routes included200 HTML challenge pages,500 JATS and404 S3 responses;
  a genuine legacy PMC full article was recovered and is the actual body evidence.
- Forgac2007 was read at publisher Key Points and Abstract level only. The apparent
  PDF route returned the same HTML preview. No full Forgac body or new primary rotation
  experiment is claimed.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Fresh native schema/strict gates0 and all12 inspection input hashes verified. No
  record edits, save or scientific-status promotion.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
