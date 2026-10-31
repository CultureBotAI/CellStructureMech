# V-type ATPase identity, compartment scope and mechanism review

- Review: 20261021T100139Z-proton-transporting-v-type-atpase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T09:43:50Z
- Finished UTC: 2026-10-21T10:01:39Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The generic V-ATPase identity, yeast example and rotary pumping are supported. Two minor repairs concern unqualified vacuolar component scope and a descriptive graph labeled mechanistic.

## Scope And Provenance

Complete one-record claim audit with native ontology/citation identities and source reading limited to the explicit evidence locators.

Selection: Target 4 in batch seventeen; exact sorted uncovered path at the frozen fresh-main revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033176 | data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml | maintained | proton-transporting V-type ATPase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Concrete protein-example applicability | not_applicable | False | GO:0033176 | No maintained UniProt protein_examples or GENE_OR_PROTEIN graph nodes occur in this target. Yeast protein names in prose are source-context claims, not newly seeded accessions. |
| Expression-module applicability | not_applicable | False | GO:0033176 | No expression-module or transcriptomic inference is needed for these structural claims. |
| Focused native schema | passed | True | GO:0033176 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033176 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0033176 | 18 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0033176 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0033176 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033176 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033176 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033176 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0033176 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Generic complex or sector versus vacuolar subtype

identity: supported. Targets: GO:0033176.

The exact GO identifier, label and structural kind agree. Native parent and parthood relations preserve the distinction between a whole rotary ATPase and its V0/V1 sectors; a vacuolar example is a valid example of the broader class.

### Scoped budding-yeast reference example

scope: supported. Targets: GO:0033176.

The S.cerevisiae species identity and canonical vacuolar example are supported by the yeast review and structural source. COMMON is qualitative occurrence, not a measured frequency or a claim that every enzyme is assembled in every condition.

### Assembly necessity is distinct from pumping and physiological phenotypes

evidence: unknown. Targets: GO:0033176.

The presence and coupling of sectors are supported. A subunit knockout, inactive complex, independently assembled sector and loss of acidification are different endpoints. No universal necessity of each named protein or vacuolar isoform is inferred from the intact enzyme or the DDM preparation; no opposite dispensability claim is made.

### Class-level molecular detail without an obligatory inventory

completeness: supported. Targets: GO:0033176.

Subunit information in the definition and source context is evaluated, but a full component census, protein examples, family CURIEs, imported stoichiometry, images and numerical properties are optional. The source/taxon and graph defects below are independent of those optional slots.

### Vacuolar component subtypes are narrower than the target

scope: concern. Targets: GO:0033176.

Both component labels match their exact vacuolar GO terms, and the yeast example legitimately uses them. They are nevertheless the only unqualified ESSENTIAL constituent rows of a generic class that includes non-vacuolar and plasma-membrane complexes. The generic sector nodes already present in the graph should be distinguished from those compartment-specific examples.

### Core definition versus supplementary biological context

evidence: unknown. Targets: GO:0033176.

The native GO definition and exact synonym are sound. Kane explicitly acknowledges archaeal/bacterial functional versatility, so their mention is not automatically a wrong-family claim; yeast-specific organelle and isoform details should remain source-bound. The appended acidocalcisome phrase is not established by the listed sections and remains unverified rather than a categorical biological refutation.

### Coupled rotary pumping and scoped vacuolar acidification

evidence: supported. Targets: GO:0033176.

V1 hydrolysis drives rotor motion and membrane proton transfer. The corrected component prose properly distinguishes c-ring rotation from rotation of all V0. The function explicitly describes the vacuolar instance, so it is not read as a claim that bacterial enzymes possess vacuoles.

### Mechanistic prose is not yet a represented coupling path

graph: concern. Targets: GO:0033176.

The graph contains duplicate generic/vacuolar sector descriptions, parthood edges and whole-complex output edges. It does not represent hydrolysis-to-rotation-to-transport coupling even though the prose correctly explains it.

## Findings

### F1: Qualify compartment-specific sector examples within the generic complex

minor / open / confirmed; issue key: generic-v-atpase-vacuolar-component-scope.

The only component rows use vacuolar GO0000220/0000221 and are marked ESSENTIAL without an example scope, while the record identity includes organelle and plasma-membrane V-ATPases. Their labels and mappings are correct for vacuolar instances; the issue is their unqualified use as the broad class inventory.

### F2: Match graph scope to the represented coupling

minor / open / confirmed; issue key: generic-v-atpase-static-graph-scope.

Parthood and whole-complex activity edges do not encode the ATP-hydrolysis, rotor and translocation transitions described in prose. MECHANISTIC promises more than this graph represents.

## Recommended Actions And Acceptance Checks

### A1

Use the generic sector identities for a generic inventory or explicitly retain the vacuolar rows as scoped examples; reconcile duplicate generic/vacuolar graph nodes.

- Native GO must preserve generic-versus-vacuolar subtype relations.
- Yeast vacuolar evidence must not imply universal compartment-specific constituents.
- Any scientific change requires separate curation authorization, guarded writer, append-only history and native validation/rendering.

### A2

Classify the current graph as descriptive or add a bounded source-supported hydrolysis-to-rotation-to-proton-transport path.

- Retain correct distinction between rotor and stationary V0 elements.
- No invented molecular-detail quota or universal taxon mechanism.
- Any scientific change requires separate curation authorization, guarded writer, append-only history and native validation/rendering.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml; Entire maintained YAML including definition, hierarchy, components, functions, every graph edge and history | context_only | All fields were read; the intended generic structure is distinguished from its vacuolar subtype and yeast examples. |
| policy | docs/CURATION.md; Exact structure identity, claim-level evidence and frozen schema component-essentiality definition | context_only | Membership, assembly necessity and activity are separate endpoints. No optional molecular census is required. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Directed causal paths, scope and exact node identity | context_only | An explanatory graph must retain the physical identity of actors and distinguish parthood/function summaries from represented transitions. |
| vatp-agent-vatp-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0000221,GO:0005774,GO:0005775,GO:0007035,GO:0016469,GO:0016471,GO:0033176,GO:0033179,GO:0033180,GO:0046961,GO:0090533,GO:1904949; All terms returned for this target, with exact definitions, synonyms and relevant inverse child relations | supports | Exact returned native GO terms support the generic target, its three is_a parents (GO0016469, GO0090533 and GO1904949) and the V0/V1 part_of children, while vacuolar V0/V1 terms are compartment-specific subtypes. The source definition and synonym annotations are assessed separately from appended curator prose. |
| vatp-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Exact identity, scientific name and rank | supports | Native taxon4932 identifies Saccharomyces cerevisiae at species rank. It does not assign the JTY002 experimental stock to every yeast study. |
| vatp-agent-kane2006-legacy-html | https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1393255/; Abstract/Introduction; complete Structure and Mechanism paragraphs15–28 and Assembly/Transport paragraphs49–80 including Fig1/2captions; genuine legacy PMC HTML, no image-pixel audit | supports | Kane2006 is a yeast-focused review. It distinguishes Vph1 vacuolar and Stv1 Golgi/endosome isoforms, core and assembly factors, catalytic rotor and stator, and independently assembled or inactive partial complexes. Its older stalk models and assembly uncertainties are not silently replaced by later cryo-EM results. |
| vatp-agent-doi-MMBR_70_1_177-191_2006 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1128/MMBR.70.1.177-191.2006; Native citation and abstract fields | supports | Exact title, author, DOI and PMID identify Kane2006; bibliographic/abstract metadata is separate from the inspected review body. |
| vatp-agent-zhao2015-publisher | https://www.nature.com/articles/nature14365; Full Abstract, Main paragraphs17–31 and four main captions; complete Methods paragraphs33–34. No original-pixel, movie or extended-data reanalysis | supports | Zhao2015 resolves three rotational states of detergent-purified S.cerevisiae JTY002 V-ATPase without added nucleotide. The yeast c-ring accommodates ten proteolipids; peripheral stalks restrain whole-sector rotation while rotor/stator parts deform. Subunit e is absent from this DDM preparation. Proposed half-channel placement retains the stated resolution ambiguity. |
| vatp-agent-zhao2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nature14365; Bibliographic fields and primary abstract | supports | Native metadata verifies Zhao, Benlekbir and Rubinstein2015, DOI10.1038/nature14365 and PMID25971514. |
| vatp-agent-li2009-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC2906225.1/PMC2906225.1.xml; Entire acidification sectionS15–S18, including review discussion of V-ATPase, loss of acidification and regulation; not the entire article | supports | Li and Kane2009 supports ATP-driven yeast vacuolar acidification, compartment-specific isoforms and regulation. Loss of acidification and growth phenotypes are not complete-assembly tests; final pH also depends on counterions, exchangers and buffering. |
| vatp-agent-li2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.bbamcr.2008.08.003; Bibliographic identity and returned abstract | supports | Exact native citation identifies Li and Kane2009, DOI10.1016/j.bbamcr.2008.08.003 and PMID18786576. |
| vatp-agent-forgac2007-publisher | https://www.nature.com/articles/nrm2272; KeyPoints paragraphs9–14 and full abstract16 only | supports | Accessible Key Points and abstract describe ATP-driven proton pumping, central-rotor coupling, ER assembly factors and regulated disassembly. The subscription main text was not recovered from this HTTP200 page. |
| vatp-agent-doi-nrm2272 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrm2272; Bibliographic identity and abstract | supports | Native metadata verifies Forgac2007 DOI10.1038/nrm2272. |
| schema-result | just validate data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml |
| strict-result | just validate-strict data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/proton_transporting_v_type_atpase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/proton_transporting_v_type_atpase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch17-20261021-vub_b2nx/proton_transporting_v_type_atpase_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 18 of18 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Kane2006 is review-tier evidence, read at the listed sections. Its early assembly and stator models retain uncertainty and historical context; original figures were not visually reanalyzed.
- Zhao2015 is primary evidence from S.cerevisiae JTY002 after detergent purification and without added nucleotide. Three structural states do not directly measure rapid in vivo turnover or prove universal stoichiometry; subunit e was absent from this preparation, not shown universally dispensable.
- No full source-wide taxonomy survey, independent assembly-removal test, complete molecular inventory or new protein/family grounding is claimed.
- Li2009 was read only atS15–S18. Forgac2007 was read at KeyPoints/abstract scope only. Additional acidocalcisome-specific support was not established in these inspected sections.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The exact target slice comes from the completed fresh batch15 resolver at the identical9c0446 base; full-corpus gates are attached by root finalization. Scientific content and native status remain unchanged.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T100139Z-proton-transporting-v-type-atpase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: V-type ATPase identity, compartment scope and mechanism review
started_at: '2026-10-21T09:43:50Z'
finished_at: '2026-10-21T10:01:39Z'
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
summary: The generic V-ATPase identity, yeast example and rotary pumping are supported.
  Two minor repairs concern unqualified vacuolar component scope and a descriptive
  graph labeled mechanistic.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    sha256: 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4
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
- target_id: GO:0033176
  path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  label: proton-transporting V-type ATPase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
scope:
  description: Complete one-record claim audit with native ontology/citation identities
    and source reading limited to the explicit evidence locators.
  selection: Target 4 in batch seventeen; exact sorted uncovered path at the frozen
    fresh-main revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033176
checks:
- check_id: protein-examples
  name: Concrete protein-example applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0033176
  summary: No maintained UniProt protein_examples or GENE_OR_PROTEIN graph nodes occur
    in this target. Yeast protein names in prose are source-context claims, not newly
    seeded accessions.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0033176
  summary: No expression-module or transcriptomic inference is needed for these structural
    claims.
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033176
  command: just validate data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033176
  command: just validate-strict data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/proton_transporting_v_type_atpase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0033176
  summary: 18 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033176
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - vatp-agent-vatp-go
  - vatp-agent-tax-4932
  - vatp-agent-kane2006-legacy-html
  - vatp-agent-doi-MMBR_70_1_177-191_2006
  - vatp-agent-zhao2015-publisher
  - vatp-agent-zhao2015-meta
  - vatp-agent-li2009-jats
  - vatp-agent-li2009-meta
  - vatp-agent-forgac2007-publisher
  - vatp-agent-doi-nrm2272
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033176
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
  - GO:0033176
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
  - GO:0033176
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
  - GO:0033176
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
  - GO:0033176
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
  reference: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  locator: Entire maintained YAML including definition, hierarchy, components, functions,
    every graph edge and history
  accessed_at: '2026-10-21T09:53:06Z'
  support: context_only
  summary: All fields were read; the intended generic structure is distinguished from
    its vacuolar subtype and yeast examples.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact structure identity, claim-level evidence and frozen schema component-essentiality
    definition
  accessed_at: '2026-10-21T09:53:06Z'
  support: context_only
  summary: Membership, assembly necessity and activity are separate endpoints. No
    optional molecular census is required.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Directed causal paths, scope and exact node identity
  accessed_at: '2026-10-21T09:53:06Z'
  support: context_only
  summary: An explanatory graph must retain the physical identity of actors and distinguish
    parthood/function summaries from represented transitions.
- evidence_id: vatp-agent-vatp-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000220,GO:0000221,GO:0005774,GO:0005775,GO:0007035,GO:0016469,GO:0016471,GO:0033176,GO:0033179,GO:0033180,GO:0046961,GO:0090533,GO:1904949
  locator: All terms returned for this target, with exact definitions, synonyms and
    relevant inverse child relations
  accessed_at: '2026-10-21T09:45:54.802649Z'
  support: supports
  summary: Exact returned native GO terms support the generic target, its three is_a
    parents (GO0016469, GO0090533 and GO1904949) and the V0/V1 part_of children, while
    vacuolar V0/V1 terms are compartment-specific subtypes. The source definition
    and synonym annotations are assessed separately from appended curator prose.
  snapshot_sha256: dfcb0b766e3f6d96e765f9e5580c9dd1c7f39a05df8380ce18ca1e461dbfda7c
- evidence_id: vatp-agent-tax-4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Exact identity, scientific name and rank
  accessed_at: '2026-10-21T09:01:31.929795Z'
  support: supports
  summary: Native taxon4932 identifies Saccharomyces cerevisiae at species rank. It
    does not assign the JTY002 experimental stock to every yeast study.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: vatp-agent-kane2006-legacy-html
  kind: authority
  reference: https://www.ncbi.nlm.nih.gov/pmc/articles/PMC1393255/
  locator: Abstract/Introduction; complete Structure and Mechanism paragraphs15–28
    and Assembly/Transport paragraphs49–80 including Fig1/2captions; genuine legacy
    PMC HTML, no image-pixel audit
  accessed_at: '2026-10-21T09:03:55.796676Z'
  support: supports
  summary: Kane2006 is a yeast-focused review. It distinguishes Vph1 vacuolar and
    Stv1 Golgi/endosome isoforms, core and assembly factors, catalytic rotor and stator,
    and independently assembled or inactive partial complexes. Its older stalk models
    and assembly uncertainties are not silently replaced by later cryo-EM results.
  snapshot_sha256: 66b78d72bc8e0b5b730f8b79113808286406293c699ac59ba9631ec92151ccdc
- evidence_id: vatp-agent-doi-MMBR_70_1_177-191_2006
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1128/MMBR.70.1.177-191.2006
  locator: Native citation and abstract fields
  accessed_at: '2026-10-21T09:01:32.126757Z'
  support: supports
  summary: Exact title, author, DOI and PMID identify Kane2006; bibliographic/abstract
    metadata is separate from the inspected review body.
  snapshot_sha256: 8eac776a8869a547a37502fd79db9798cb0c58b42f84374f991ffb3f499e303e
- evidence_id: vatp-agent-zhao2015-publisher
  kind: primary_source
  reference: https://www.nature.com/articles/nature14365
  locator: Full Abstract, Main paragraphs17–31 and four main captions; complete Methods
    paragraphs33–34. No original-pixel, movie or extended-data reanalysis
  accessed_at: '2026-10-21T09:45:56.414594Z'
  support: supports
  summary: Zhao2015 resolves three rotational states of detergent-purified S.cerevisiae
    JTY002 V-ATPase without added nucleotide. The yeast c-ring accommodates ten proteolipids;
    peripheral stalks restrain whole-sector rotation while rotor/stator parts deform.
    Subunit e is absent from this DDM preparation. Proposed half-channel placement
    retains the stated resolution ambiguity.
  snapshot_sha256: 6b78c6c52d53bf2fa64cb44c9d1d711205e7e9e6b95d79bea1638157ffba072f
- evidence_id: vatp-agent-zhao2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature14365
  locator: Bibliographic fields and primary abstract
  accessed_at: '2026-10-21T09:45:54.867635Z'
  support: supports
  summary: Native metadata verifies Zhao, Benlekbir and Rubinstein2015, DOI10.1038/nature14365
    and PMID25971514.
  snapshot_sha256: d1096176696622d0a2c23f9defeb60afd064f771bcddabb444365e9a8839c837
- evidence_id: vatp-agent-li2009-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2906225.1/PMC2906225.1.xml
  locator: Entire acidification sectionS15–S18, including review discussion of V-ATPase,
    loss of acidification and regulation; not the entire article
  accessed_at: '2026-10-21T09:45:55.403499Z'
  support: supports
  summary: Li and Kane2009 supports ATP-driven yeast vacuolar acidification, compartment-specific
    isoforms and regulation. Loss of acidification and growth phenotypes are not complete-assembly
    tests; final pH also depends on counterions, exchangers and buffering.
  snapshot_sha256: 13a3eb22e486987e2599a0e7c23b7677808cf35e07e8f558a3b559de5d6f86d4
- evidence_id: vatp-agent-li2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.bbamcr.2008.08.003
  locator: Bibliographic identity and returned abstract
  accessed_at: '2026-10-21T09:45:54.869634Z'
  support: supports
  summary: Exact native citation identifies Li and Kane2009, DOI10.1016/j.bbamcr.2008.08.003
    and PMID18786576.
  snapshot_sha256: bbe2bbf29e90cc7df492950e5d2d10f9fa92e0dfad3c359e6ced9189e4be81e9
- evidence_id: vatp-agent-forgac2007-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrm2272
  locator: KeyPoints paragraphs9–14 and full abstract16 only
  accessed_at: '2026-10-21T09:03:00.171816Z'
  support: supports
  summary: Accessible Key Points and abstract describe ATP-driven proton pumping,
    central-rotor coupling, ER assembly factors and regulated disassembly. The subscription
    main text was not recovered from this HTTP200 page.
  snapshot_sha256: f0ca31d8d16c2ad45ecaece0e5ecd6d3f62acdfa5a76f268be9c3de5d19bd902
- evidence_id: vatp-agent-doi-nrm2272
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrm2272
  locator: Bibliographic identity and abstract
  accessed_at: '2026-10-21T09:01:32.684552Z'
  support: supports
  summary: Native metadata verifies Forgac2007 DOI10.1038/nrm2272.
  snapshot_sha256: 55c0c1a8752adaa99a6255c1a99ee11cf7e2202a38e78c8fc936d05da82548f4
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:43:52Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml'
  snapshot_sha256: 7dfa90c01e0b299cbec51068d6a2cc444bd37cd6a87066474f34d49e3ac6ec2a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/proton_transporting_v_type_atpase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T09:43:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch17-20261021-vub_b2nx/proton_transporting_v_type_atpase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch17-20261021-vub_b2nx/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch17-20261021-vub_b2nx/proton_transporting_v_type_atpase_complex-strict.tsv"
  snapshot_sha256: 076abf73a7fc8e58d6413f3a7a53998db72ea8684a386a8bdd86bb3c41b0f491
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T09:53:06Z'
  support: supports
  summary: '18 of18 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
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
  topic: Generic complex or sector versus vacuolar subtype
  outcome: supported
  target_ids:
  - GO:0033176
  summary: The exact GO identifier, label and structural kind agree. Native parent
    and parthood relations preserve the distinction between a whole rotary ATPase
    and its V0/V1 sectors; a vacuolar example is a valid example of the broader class.
  evidence_ids:
  - vatp-agent-vatp-go
  - record
- assessment_id: taxon
  area: scope
  topic: Scoped budding-yeast reference example
  outcome: supported
  target_ids:
  - GO:0033176
  summary: The S.cerevisiae species identity and canonical vacuolar example are supported
    by the yeast review and structural source. COMMON is qualitative occurrence, not
    a measured frequency or a claim that every enzyme is assembled in every condition.
  evidence_ids:
  - vatp-agent-tax-4932
  - vatp-agent-kane2006-legacy-html
  - vatp-agent-zhao2015-publisher
  - record
- assessment_id: necessity
  area: evidence
  topic: Assembly necessity is distinct from pumping and physiological phenotypes
  outcome: unknown
  target_ids:
  - GO:0033176
  summary: The presence and coupling of sectors are supported. A subunit knockout,
    inactive complex, independently assembled sector and loss of acidification are
    different endpoints. No universal necessity of each named protein or vacuolar
    isoform is inferred from the intact enzyme or the DDM preparation; no opposite
    dispensability claim is made.
  evidence_ids:
  - vatp-agent-kane2006-legacy-html
  - vatp-agent-zhao2015-publisher
  - policy
  - record
- assessment_id: completeness
  area: completeness
  topic: Class-level molecular detail without an obligatory inventory
  outcome: supported
  target_ids:
  - GO:0033176
  summary: Subunit information in the definition and source context is evaluated,
    but a full component census, protein examples, family CURIEs, imported stoichiometry,
    images and numerical properties are optional. The source/taxon and graph defects
    below are independent of those optional slots.
  evidence_ids:
  - vatp-agent-vatp-go
  - vatp-agent-kane2006-legacy-html
  - vatp-agent-zhao2015-publisher
  - policy
  - record
- assessment_id: composition
  area: scope
  topic: Vacuolar component subtypes are narrower than the target
  outcome: concern
  target_ids:
  - GO:0033176
  summary: Both component labels match their exact vacuolar GO terms, and the yeast
    example legitimately uses them. They are nevertheless the only unqualified ESSENTIAL
    constituent rows of a generic class that includes non-vacuolar and plasma-membrane
    complexes. The generic sector nodes already present in the graph should be distinguished
    from those compartment-specific examples.
  evidence_ids:
  - vatp-agent-vatp-go
  - vatp-agent-kane2006-legacy-html
  - vatp-agent-li2009-jats
  - record
- assessment_id: definition
  area: evidence
  topic: Core definition versus supplementary biological context
  outcome: unknown
  target_ids:
  - GO:0033176
  summary: The native GO definition and exact synonym are sound. Kane explicitly acknowledges
    archaeal/bacterial functional versatility, so their mention is not automatically
    a wrong-family claim; yeast-specific organelle and isoform details should remain
    source-bound. The appended acidocalcisome phrase is not established by the listed
    sections and remains unverified rather than a categorical biological refutation.
  evidence_ids:
  - vatp-agent-vatp-go
  - vatp-agent-kane2006-legacy-html
  - vatp-agent-li2009-jats
  - vatp-agent-forgac2007-publisher
  - vatp-agent-zhao2015-publisher
  - record
- assessment_id: function
  area: evidence
  topic: Coupled rotary pumping and scoped vacuolar acidification
  outcome: supported
  target_ids:
  - GO:0033176
  summary: V1 hydrolysis drives rotor motion and membrane proton transfer. The corrected
    component prose properly distinguishes c-ring rotation from rotation of all V0.
    The function explicitly describes the vacuolar instance, so it is not read as
    a claim that bacterial enzymes possess vacuoles.
  evidence_ids:
  - vatp-agent-vatp-go
  - vatp-agent-kane2006-legacy-html
  - vatp-agent-li2009-jats
  - vatp-agent-zhao2015-publisher
  - vatp-agent-forgac2007-publisher
  - record
- assessment_id: graph
  area: graph
  topic: Mechanistic prose is not yet a represented coupling path
  outcome: concern
  target_ids:
  - GO:0033176
  summary: The graph contains duplicate generic/vacuolar sector descriptions, parthood
    edges and whole-complex output edges. It does not represent hydrolysis-to-rotation-to-transport
    coupling even though the prose correctly explains it.
  evidence_ids:
  - vatp-agent-vatp-go
  - vatp-agent-zhao2015-publisher
  - vatp-agent-kane2006-legacy-html
  - graph-policy
  - record
findings:
- finding_id: F1
  issue_key: generic-v-atpase-vacuolar-component-scope
  category: scope
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify compartment-specific sector examples within the generic complex
  description: The only component rows use vacuolar GO0000220/0000221 and are marked
    ESSENTIAL without an example scope, while the record identity includes organelle
    and plasma-membrane V-ATPases. Their labels and mappings are correct for vacuolar
    instances; the issue is their unqualified use as the broad class inventory.
  target_ids:
  - GO:0033176
  field_paths:
  - components[component_id=v0_domain]
  - components[component_id=v1_domain]
  evidence_ids:
  - vatp-agent-vatp-go
  - vatp-agent-kane2006-legacy-html
  - vatp-agent-li2009-jats
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The basic biology is supported; the defect is bounded compartment/source
    attribution or graph representation.
- finding_id: F2
  issue_key: generic-v-atpase-static-graph-scope
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Match graph scope to the represented coupling
  description: Parthood and whole-complex activity edges do not encode the ATP-hydrolysis,
    rotor and translocation transitions described in prose. MECHANISTIC promises more
    than this graph represents.
  target_ids:
  - GO:0033176
  field_paths:
  - causal_graphs[graph_id=proton_transporting_v_type_atpase_complex_mechanism].scope_status
  - causal_graphs[graph_id=proton_transporting_v_type_atpase_complex_mechanism].edges
  evidence_ids:
  - vatp-agent-zhao2015-publisher
  - vatp-agent-kane2006-legacy-html
  - graph-policy
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
  rule_id: .claude/skills/curate-yaml-record/references/review-checklist.md:Evidence
    and claim scope
  native_severity: minor
  normalization_reason: The basic biology is supported; the defect is bounded compartment/source
    attribution or graph representation.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0033176
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
  description: Use the generic sector identities for a generic inventory or explicitly
    retain the vacuolar rows as scoped examples; reconcile duplicate generic/vacuolar
    graph nodes.
  acceptance_checks:
  - Native GO must preserve generic-versus-vacuolar subtype relations.
  - Yeast vacuolar evidence must not imply universal compartment-specific constituents.
  - Any scientific change requires separate curation authorization, guarded writer,
    append-only history and native validation/rendering.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0033176
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained scientific record
  description: Classify the current graph as descriptive or add a bounded source-supported
    hydrolysis-to-rotation-to-proton-transport path.
  acceptance_checks:
  - Retain correct distinction between rotor and stationary V0 elements.
  - No invented molecular-detail quota or universal taxon mechanism.
  - Any scientific change requires separate curation authorization, guarded writer,
    append-only history and native validation/rendering.
limitations:
- Kane2006 is review-tier evidence, read at the listed sections. Its early assembly
  and stator models retain uncertainty and historical context; original figures were
  not visually reanalyzed.
- Zhao2015 is primary evidence from S.cerevisiae JTY002 after detergent purification
  and without added nucleotide. Three structural states do not directly measure rapid
  in vivo turnover or prove universal stoichiometry; subunit e was absent from this
  preparation, not shown universally dispensable.
- No full source-wide taxonomy survey, independent assembly-removal test, complete
  molecular inventory or new protein/family grounding is claimed.
- Li2009 was read only atS15–S18. Forgac2007 was read at KeyPoints/abstract scope
  only. Additional acidocalcisome-specific support was not established in these inspected
  sections.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- The exact target slice comes from the completed fresh batch15 resolver at the identical9c0446
  base; full-corpus gates are attached by root finalization. Scientific content and
  native status remain unchanged.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
