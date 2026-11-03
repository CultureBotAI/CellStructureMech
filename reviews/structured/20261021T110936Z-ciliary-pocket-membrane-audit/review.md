# Ciliary pocket membrane identity, boundary and source review

- Review: 20261021T110936Z-ciliary-pocket-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T10:51:42Z
- Finished UTC: 2026-10-21T11:09:36Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No substantive issue was established. Native ontology and direct T. brucei studies support the exact membrane domain, species example, boundary function and nonmechanistic graph; molecular inventory and source-access limits remain explicit.

## Scope And Provenance

Entire maintained target; native GO and taxonomy; exact citation identities; scoped primary/review reading and frozen whole-pocket/collar boundary fields.

Selection: Ninth selected target in batch twenty-two, fixed maintained-path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0020018 | data/structures/membrane_organelle/ciliary_pocket_membrane.yaml | maintained | ciliary pocket membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0020018 | Focused validator passed. |
| Focused native strict | passed | True | GO:0020018 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0020018 | 9 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0020018 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0020018 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0020018 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0020018 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0020018 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0020018 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact membrane domain and topology

identity: supported. Targets: GO:0020018.

GO identity, the three exact synonyms, ciliary-membrane parentage and whole-pocket parthood are directly supported. The record consistently distinguishes the pocket membrane from the complete invagination and cytoskeletal collar.

### Collective membrane material and acknowledged inventory

grounding: supported. Targets: GO:0020018.

The lipid-bilayer row represents collective membrane material and does not assert an exact lipid species or resident protein family. The source-specific membrane domain is supported. The open inventory discussion does not justify importing the associated cytoskeletal collar or all pocket-trafficking factors as membrane constituents.

### Constitution versus empirical formation requirements

evidence: unknown. Targets: GO:0020018.

The ESSENTIAL row names the complete constituting lipid-bilayer material. No individual lipid species or protein is thereby shown necessary for membrane formation. The inspected studies do not establish a universal molecular assembly inventory, so empirical species-level formation requirements remain unknown.

### T. brucei occurrence and life-stage context

scope: supported. Targets: GO:0020018.

The native taxon response verifies T. brucei species identity. Direct bloodstream-form and procyclic studies support the qualitative COMMON occurrence and model example, without asserting a measured prevalence across strains or all trypanosomatids. The procyclic strain427 culture is not silently transferred to the separate bloodstream-form experiment.

### Boundary function and source placement

evidence: supported. Targets: GO:0020018.

The maintained function only describes lining the pocket invagination. It is supported by native GO and the accessible Field review abstract/Key Points, with direct primary boundary evidence. More detailed endocytosis, selective filtering or anchoring mechanisms are not asserted by this function.

### Explicitly nonmechanistic membrane topology

graph: supported. Targets: GO:0020018.

The graph separates a material component node from the complete membrane and whole pocket. The contributes-to and bounds edges consistently encode constitution and topology, and NONMECHANISTIC scope correctly avoids an unsupported molecular causal mechanism.

### Bounded clean review

completeness: supported. Targets: GO:0020018.

No corrective issue was established. Exact molecular composition is an acknowledged unresolved inventory rather than a missing required slot. All maintained references have exact bibliographic identities; source access and body-read extents are recorded. No maintained images, protein accessions, snippets or quantitative structural measurements require separate checks.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/ciliary_pocket_membrane.yaml; Entire maintained YAML including definition/source, hierarchy, synonyms, component, functions if present, taxonomy, examples, every graph node/edge, discussions and history | context_only | The entire target was read against fresh native inspection. No scientific record, mapping status or history was changed. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent essentiality; CausalNode component_ref; docs/CURATION.md and native review checklist | context_only | Essentiality asks whether the structure forms without a component; observed membership and activity do not establish experimental formation necessity. component_ref identifies an own-component node. Optional slots are not mandatory. Reviewed-label-only collective lipid material is distinct from a whole membrane-bounded compartment. |
| pocket-membrane-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020016,GO:0020018,GO:0060170,GO:1990900; Complete GO0020018, GO0060170, GO0020016 and GO1990900 identities, definitions, synonyms, comments and relevant relationships | supports | GO0020018 exactly defines the plasma-membrane part in the ciliary/flagellar pocket, lists all three maintained synonyms as exact, and has direct is_a ciliary membrane and part_of ciliary pocket relationships. GO1990900 separately defines the cytoskeletal collar. |
| pocket-membrane-agent-tax-5691 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; Complete taxId, scientificName, rank, lineage and relevant synonyms | supports | This native ENA taxonomy response identifies Trypanosoma brucei, species. It verifies only this taxon identity and rank, not experimental occurrence or strain provenance. |
| pocket-membrane-agent-doi-10.1073_pnas.0909289106 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1073/pnas.0909289106; Complete returned bibliographic identity and abstract | supports | Exact native metadata identifies Membrane domains and flagellar pocket boundaries are influenced by the cytoskeleton in African trypanosomes. Authors: Gadelha C, Rothery S, Morphew M, McIntosh JR, Severs NJ, Gull K.; PMID 19805090; DOI 10.1073/pnas.0909289106. Bibliographic identity, publication type and available abstract were read; metadata is not a full-body substitute. |
| pocket-membrane-agent-doi-10.1242_jcs.045740 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1242/jcs.045740; Complete returned bibliographic identity and abstract | supports | Exact native metadata identifies Three-dimensional cellular architecture of the flagellar pocket and associated cytoskeleton in trypanosomes revealed by electron microscope tomography. Authors: Lacomble S, Vaughan S, Gadelha C, Morphew MK, Shaw MK, McIntosh JR, Gull K.; PMID 19299460; DOI 10.1242/jcs.045740. Bibliographic identity, publication type and available abstract were read; metadata is not a full-body substitute. |
| pocket-membrane-agent-doi-10.1038_nrmicro2221 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nrmicro2221; Complete returned bibliographic identity and abstract | supports | Exact native metadata identifies The trypanosome flagellar pocket. Authors: Field MC, Carrington M.; PMID 19806154; DOI 10.1038/nrmicro2221. Bibliographic identity, publication type and available abstract were read; metadata is not a full-body substitute. |
| pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.pt.2020.11.005; Complete returned bibliographic identity and abstract | supports | Exact native metadata identifies Trypanosomatid Flagellar Pocket from Structure to Function. Authors: Halliday C, de Castro-Neto A, Alcantara CL, Cunha-E-Silva NL, Vaughan S, Sunter JD.; PMID 33308952; DOI 10.1016/j.pt.2020.11.005. Bibliographic identity, publication type and available abstract were read; metadata is not a full-body substitute. |
| pocket-membrane-agent-pmc-PMC2755463 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2755463/; Unheaded Introduction paragraphs11-16; all Results sec2-sec6; all Discussion sec8-sec11; main Methods sec13-sec17; embedded Figures1-6 captions. Supplementary experimental detail and image pixels were not independently read. | supports | Gadelha2009 primary experiments distinguish continuous surface, neck, flagellar-pocket and flagellar membrane domains in bloodstream-form T. brucei. Freeze-fracture membrane-particle distributions and microscopy support a specialized pocket membrane and cytoskeleton-associated boundaries. Marker accumulation differs between cold and physiological conditions; membrane-domain boundaries are not simply equated with every cytoskeletal collar structure. Proposed channel/filter mechanisms remain qualified. |
| pocket-membrane-agent-pmc-PMC2714436 | https://pmc.ncbi.nlm.nih.gov/articles/PMC2714436/; Introduction sec1; Results sec3 Flagellar pocket architecture in procyclic trypanosomes and sec4 Flagellar pocket boundaries, including their captions; entire Discussion sec9; Cell culture sec11. Other Results and remaining Methods were not comprehensively audited; no tomography/image reanalysis. | supports | Lacomble2009 tomography directly describes the pocket as a bulbous plasma-membrane invagination, with cytoplasmic collar and basal flagellum-associated boundaries. The studied culture was procyclic T. brucei brucei strain427 at28 C. The paper distinguishes membrane domains from associated cytoskeletal structures; proposed trafficking or barrier mechanisms are not established universally. |
| pocket-membrane-agent-field2009-publisher | https://www.nature.com/articles/nrmicro2221; Publisher Abstract and complete Key Points only; full Main/body unavailable | supports | Field and Carrington2009 is review-tier context. Its accessible Abstract and Key Points describe a specialized plasma-membrane invagination with a distinct membrane-protein composition. These support the maintained boundary-only function. The publisher response does not expose the full review body. |
| pocket-membrane-agent-halliday2021-publisher | https://doi.org/10.1016/j.pt.2020.11.005; Actual response body and retrieval receipt | context_only | The HTTP200 response is a short Elsevier redirect/stub, not an article body. Halliday2021 was assessed from its separately preserved native abstract only. |
| boundary-0 | data/structures/membrane_organelle/flagellar_pocket.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | Only these boundary fields were read for context. This is not an additional full scientific review of the neighboring record. |
| boundary-1 | data/structures/cytoskeleton/ciliary_pocket_collar.yaml; Identifier, label, definition/source, synonyms, hierarchy/parthood and all discussions; frozen additional inspection input | context_only | Only these boundary fields were read for context. This is not an additional full scientific review of the neighboring record. |
| schema-result | just validate data/structures/membrane_organelle/ciliary_pocket_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/ciliary_pocket_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/ciliary_pocket_membrane.yaml --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/ciliary_pocket_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/ciliary_pocket_membrane.yaml --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/ciliary_pocket_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch22-20261021-xfifxerh/ciliary_pocket_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/ciliary_pocket_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 9 of9 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Field/Carrington2009 was read only at the publisher Abstract and Key Points; Halliday2021 only at the native metadata/abstract. Their full review bodies were not obtained. The Halliday publisher response was a stub despite HTTP200.
- Both2009 primary studies were available as genuine PMC HTML. Attempted version1 S3 JATS endpoints returned404; this does not imply that the primary bodies were unavailable. Gadelha main text was read at the recorded complete scope; Lacomble only at the explicitly named sections.
- No figure pixels, raw tomography volumes, movies, supplementary data or quantitative membrane-particle counts were independently reanalysed. Collective membrane constitution is supported, while formation necessity of individual lipids or proteins remains untested in this review.
- Neighboring whole-pocket and collar records were used only for the frozen boundary fields. This review does not certify their remaining claims or establish a complete membrane proteome.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T110936Z-ciliary-pocket-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Ciliary pocket membrane identity, boundary and source review
started_at: '2026-10-21T10:51:42Z'
finished_at: '2026-10-21T11:09:36Z'
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
summary: No substantive issue was established. Native ontology and direct T. brucei
  studies support the exact membrane domain, species example, boundary function and
  nonmechanistic graph; molecular inventory and source-access limits remain explicit.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    sha256: df0530c9582d0a40d8e0c646cdaa88cc0872d1e6e034cbdcd068b2a3f426ec3a
    role: context
  - path: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    sha256: acdf228c05817a740e627e5885200d543b8cb91f6ac94aefa4f5bf954255b3e0
    role: target
  - path: data/structures/membrane_organelle/flagellar_pocket.yaml
    sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
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
- target_id: GO:0020018
  path: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  label: ciliary pocket membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire maintained target; native GO and taxonomy; exact citation identities;
    scoped primary/review reading and frozen whole-pocket/collar boundary fields.
  selection: Ninth selected target in batch twenty-two, fixed maintained-path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0020018
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0020018
  command: just validate data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0020018
  command: just validate-strict data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/ciliary_pocket_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0020018
  summary: 9 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0020018
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - pocket-membrane-agent-go
  - pocket-membrane-agent-tax-5691
  - pocket-membrane-agent-doi-10.1073_pnas.0909289106
  - pocket-membrane-agent-doi-10.1242_jcs.045740
  - pocket-membrane-agent-doi-10.1038_nrmicro2221
  - pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005
  - pocket-membrane-agent-pmc-PMC2755463
  - pocket-membrane-agent-pmc-PMC2714436
  - pocket-membrane-agent-field2009-publisher
  - pocket-membrane-agent-halliday2021-publisher
  - boundary-0
  - boundary-1
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0020018
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
  - GO:0020018
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
  - GO:0020018
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
  - GO:0020018
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
  - GO:0020018
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
  reference: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  locator: Entire maintained YAML including definition/source, hierarchy, synonyms,
    component, functions if present, taxonomy, examples, every graph node/edge, discussions
    and history
  accessed_at: '2026-10-21T10:57:48Z'
  support: context_only
  summary: The entire target was read against fresh native inspection. No scientific
    record, mapping status or history was changed.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent essentiality; CausalNode component_ref; docs/CURATION.md
    and native review checklist
  accessed_at: '2026-10-21T10:57:48Z'
  support: context_only
  summary: Essentiality asks whether the structure forms without a component; observed
    membership and activity do not establish experimental formation necessity. component_ref
    identifies an own-component node. Optional slots are not mandatory. Reviewed-label-only
    collective lipid material is distinct from a whole membrane-bounded compartment.
- evidence_id: pocket-membrane-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020016,GO:0020018,GO:0060170,GO:1990900
  locator: Complete GO0020018, GO0060170, GO0020016 and GO1990900 identities, definitions,
    synonyms, comments and relevant relationships
  accessed_at: '2026-10-21T10:51:30.561260Z'
  support: supports
  summary: GO0020018 exactly defines the plasma-membrane part in the ciliary/flagellar
    pocket, lists all three maintained synonyms as exact, and has direct is_a ciliary
    membrane and part_of ciliary pocket relationships. GO1990900 separately defines
    the cytoskeletal collar.
  snapshot_sha256: d86d3d966784eb15a91838b089711e2c7dce354317aa7a9d036376fb18b114d5
- evidence_id: pocket-membrane-agent-tax-5691
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: Complete taxId, scientificName, rank, lineage and relevant synonyms
  accessed_at: '2026-10-21T10:51:30.561607Z'
  support: supports
  summary: This native ENA taxonomy response identifies Trypanosoma brucei, species.
    It verifies only this taxon identity and rank, not experimental occurrence or
    strain provenance.
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
- evidence_id: pocket-membrane-agent-doi-10.1073_pnas.0909289106
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1073/pnas.0909289106
  locator: Complete returned bibliographic identity and abstract
  accessed_at: '2026-10-21T10:51:30.562007Z'
  support: supports
  summary: 'Exact native metadata identifies Membrane domains and flagellar pocket
    boundaries are influenced by the cytoskeleton in African trypanosomes. Authors:
    Gadelha C, Rothery S, Morphew M, McIntosh JR, Severs NJ, Gull K.; PMID 19805090;
    DOI 10.1073/pnas.0909289106. Bibliographic identity, publication type and available
    abstract were read; metadata is not a full-body substitute.'
  snapshot_sha256: 1e0d2e19103f1a6f98801b00012315427a396610d687351c10fecc37037093bb
- evidence_id: pocket-membrane-agent-doi-10.1242_jcs.045740
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1242/jcs.045740
  locator: Complete returned bibliographic identity and abstract
  accessed_at: '2026-10-21T10:51:31.278446Z'
  support: supports
  summary: 'Exact native metadata identifies Three-dimensional cellular architecture
    of the flagellar pocket and associated cytoskeleton in trypanosomes revealed by
    electron microscope tomography. Authors: Lacomble S, Vaughan S, Gadelha C, Morphew
    MK, Shaw MK, McIntosh JR, Gull K.; PMID 19299460; DOI 10.1242/jcs.045740. Bibliographic
    identity, publication type and available abstract were read; metadata is not a
    full-body substitute.'
  snapshot_sha256: ab85e1b67afa139c3840f4cd1e58a0ecd9913aa645103352341a8824a397800b
- evidence_id: pocket-membrane-agent-doi-10.1038_nrmicro2221
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nrmicro2221
  locator: Complete returned bibliographic identity and abstract
  accessed_at: '2026-10-21T10:51:30.561895Z'
  support: supports
  summary: 'Exact native metadata identifies The trypanosome flagellar pocket. Authors:
    Field MC, Carrington M.; PMID 19806154; DOI 10.1038/nrmicro2221. Bibliographic
    identity, publication type and available abstract were read; metadata is not a
    full-body substitute.'
  snapshot_sha256: 90dfa2be054c3fe7a235ea43f9cfd9b82bca69f4cc6aaf5e8114e2364a46f55a
- evidence_id: pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.pt.2020.11.005
  locator: Complete returned bibliographic identity and abstract
  accessed_at: '2026-10-21T10:51:30.561764Z'
  support: supports
  summary: 'Exact native metadata identifies Trypanosomatid Flagellar Pocket from
    Structure to Function. Authors: Halliday C, de Castro-Neto A, Alcantara CL, Cunha-E-Silva
    NL, Vaughan S, Sunter JD.; PMID 33308952; DOI 10.1016/j.pt.2020.11.005. Bibliographic
    identity, publication type and available abstract were read; metadata is not a
    full-body substitute.'
  snapshot_sha256: 81206ea5842bd81a66c41534c2ee52ae977be1b7fa8ec29016b002c91d64d25b
- evidence_id: pocket-membrane-agent-pmc-PMC2755463
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2755463/
  locator: Unheaded Introduction paragraphs11-16; all Results sec2-sec6; all Discussion
    sec8-sec11; main Methods sec13-sec17; embedded Figures1-6 captions. Supplementary
    experimental detail and image pixels were not independently read.
  accessed_at: '2026-10-21T10:52:00.889584Z'
  support: supports
  summary: Gadelha2009 primary experiments distinguish continuous surface, neck, flagellar-pocket
    and flagellar membrane domains in bloodstream-form T. brucei. Freeze-fracture
    membrane-particle distributions and microscopy support a specialized pocket membrane
    and cytoskeleton-associated boundaries. Marker accumulation differs between cold
    and physiological conditions; membrane-domain boundaries are not simply equated
    with every cytoskeletal collar structure. Proposed channel/filter mechanisms remain
    qualified.
  snapshot_sha256: 487f14e3deacf17be235631744cc2845674dd5cfb332d08e44262f41a49fa850
- evidence_id: pocket-membrane-agent-pmc-PMC2714436
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2714436/
  locator: Introduction sec1; Results sec3 Flagellar pocket architecture in procyclic
    trypanosomes and sec4 Flagellar pocket boundaries, including their captions; entire
    Discussion sec9; Cell culture sec11. Other Results and remaining Methods were
    not comprehensively audited; no tomography/image reanalysis.
  accessed_at: '2026-10-21T10:52:00.889852Z'
  support: supports
  summary: Lacomble2009 tomography directly describes the pocket as a bulbous plasma-membrane
    invagination, with cytoplasmic collar and basal flagellum-associated boundaries.
    The studied culture was procyclic T. brucei brucei strain427 at28 C. The paper
    distinguishes membrane domains from associated cytoskeletal structures; proposed
    trafficking or barrier mechanisms are not established universally.
  snapshot_sha256: ca424ebc26ba0b12693d29556013e5f3d83fdbec74c99b4c23e48a459bb340b7
- evidence_id: pocket-membrane-agent-field2009-publisher
  kind: authority
  reference: https://www.nature.com/articles/nrmicro2221
  locator: Publisher Abstract and complete Key Points only; full Main/body unavailable
  accessed_at: '2026-10-21T10:52:01.215423Z'
  support: supports
  summary: Field and Carrington2009 is review-tier context. Its accessible Abstract
    and Key Points describe a specialized plasma-membrane invagination with a distinct
    membrane-protein composition. These support the maintained boundary-only function.
    The publisher response does not expose the full review body.
  snapshot_sha256: 7aa1da772a876400d8169216dd2ff1ced8635fb3e666afefd25f3effd4bd2144
- evidence_id: pocket-membrane-agent-halliday2021-publisher
  kind: authority
  reference: https://doi.org/10.1016/j.pt.2020.11.005
  locator: Actual response body and retrieval receipt
  accessed_at: '2026-10-21T10:52:01.216138Z'
  support: context_only
  summary: The HTTP200 response is a short Elsevier redirect/stub, not an article
    body. Halliday2021 was assessed from its separately preserved native abstract
    only.
  snapshot_sha256: c107afaf835af1937e35c50c624dc60406a92b24e67201ef2bb80803496b308c
- evidence_id: boundary-0
  kind: record_content
  reference: data/structures/membrane_organelle/flagellar_pocket.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:57:48Z'
  support: context_only
  summary: Only these boundary fields were read for context. This is not an additional
    full scientific review of the neighboring record.
- evidence_id: boundary-1
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  locator: Identifier, label, definition/source, synonyms, hierarchy/parthood and
    all discussions; frozen additional inspection input
  accessed_at: '2026-10-21T10:57:48Z'
  support: context_only
  summary: Only these boundary fields were read for context. This is not an additional
    full scientific review of the neighboring record.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:51:44Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/ciliary_pocket_membrane.yaml'
  snapshot_sha256: 0bc859bd26f39e24fbca6c09cf7346bfec2ef5b1d29a7e22f6424cf65d3a0c86
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/ciliary_pocket_membrane.yaml
    --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/ciliary_pocket_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T10:51:45Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/ciliary_pocket_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch22-20261021-xfifxerh/ciliary_pocket_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch22-20261021-xfifxerh/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch22-20261021-xfifxerh/ciliary_pocket_membrane-strict.tsv"
  snapshot_sha256: 9dc62f8a54a84c541cc55dcdcedc6b2c9e9de68122e6657e7794d3e52cfbea0c
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/ciliary_pocket_membrane.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T10:57:48Z'
  support: supports
  summary: '9 of9 collected target identifiers returned OK in this fresh base resolver
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
  topic: Exact membrane domain and topology
  outcome: supported
  target_ids:
  - GO:0020018
  summary: GO identity, the three exact synonyms, ciliary-membrane parentage and whole-pocket
    parthood are directly supported. The record consistently distinguishes the pocket
    membrane from the complete invagination and cytoskeletal collar.
  evidence_ids:
  - pocket-membrane-agent-go
  - pocket-membrane-agent-pmc-PMC2755463
  - pocket-membrane-agent-pmc-PMC2714436
  - boundary-0
  - boundary-1
  - record
- assessment_id: material
  area: grounding
  topic: Collective membrane material and acknowledged inventory
  outcome: supported
  target_ids:
  - GO:0020018
  summary: The lipid-bilayer row represents collective membrane material and does
    not assert an exact lipid species or resident protein family. The source-specific
    membrane domain is supported. The open inventory discussion does not justify importing
    the associated cytoskeletal collar or all pocket-trafficking factors as membrane
    constituents.
  evidence_ids:
  - pocket-membrane-agent-go
  - pocket-membrane-agent-pmc-PMC2755463
  - pocket-membrane-agent-pmc-PMC2714436
  - record
  - policy
- assessment_id: necessity
  area: evidence
  topic: Constitution versus empirical formation requirements
  outcome: unknown
  target_ids:
  - GO:0020018
  summary: The ESSENTIAL row names the complete constituting lipid-bilayer material.
    No individual lipid species or protein is thereby shown necessary for membrane
    formation. The inspected studies do not establish a universal molecular assembly
    inventory, so empirical species-level formation requirements remain unknown.
  evidence_ids:
  - pocket-membrane-agent-go
  - pocket-membrane-agent-pmc-PMC2755463
  - pocket-membrane-agent-pmc-PMC2714436
  - record
  - policy
- assessment_id: taxa
  area: scope
  topic: T. brucei occurrence and life-stage context
  outcome: supported
  target_ids:
  - GO:0020018
  summary: The native taxon response verifies T. brucei species identity. Direct bloodstream-form
    and procyclic studies support the qualitative COMMON occurrence and model example,
    without asserting a measured prevalence across strains or all trypanosomatids.
    The procyclic strain427 culture is not silently transferred to the separate bloodstream-form
    experiment.
  evidence_ids:
  - pocket-membrane-agent-tax-5691
  - pocket-membrane-agent-pmc-PMC2755463
  - pocket-membrane-agent-pmc-PMC2714436
  - pocket-membrane-agent-doi-10.1073_pnas.0909289106
  - pocket-membrane-agent-doi-10.1242_jcs.045740
  - pocket-membrane-agent-doi-10.1038_nrmicro2221
  - pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005
  - record
- assessment_id: function
  area: evidence
  topic: Boundary function and source placement
  outcome: supported
  target_ids:
  - GO:0020018
  summary: The maintained function only describes lining the pocket invagination.
    It is supported by native GO and the accessible Field review abstract/Key Points,
    with direct primary boundary evidence. More detailed endocytosis, selective filtering
    or anchoring mechanisms are not asserted by this function.
  evidence_ids:
  - pocket-membrane-agent-go
  - pocket-membrane-agent-field2009-publisher
  - pocket-membrane-agent-pmc-PMC2755463
  - pocket-membrane-agent-pmc-PMC2714436
  - record
- assessment_id: graph
  area: graph
  topic: Explicitly nonmechanistic membrane topology
  outcome: supported
  target_ids:
  - GO:0020018
  summary: The graph separates a material component node from the complete membrane
    and whole pocket. The contributes-to and bounds edges consistently encode constitution
    and topology, and NONMECHANISTIC scope correctly avoids an unsupported molecular
    causal mechanism.
  evidence_ids:
  - pocket-membrane-agent-go
  - pocket-membrane-agent-pmc-PMC2755463
  - pocket-membrane-agent-pmc-PMC2714436
  - pocket-membrane-agent-field2009-publisher
  - record
  - policy
- assessment_id: completeness
  area: completeness
  topic: Bounded clean review
  outcome: supported
  target_ids:
  - GO:0020018
  summary: No corrective issue was established. Exact molecular composition is an
    acknowledged unresolved inventory rather than a missing required slot. All maintained
    references have exact bibliographic identities; source access and body-read extents
    are recorded. No maintained images, protein accessions, snippets or quantitative
    structural measurements require separate checks.
  evidence_ids:
  - pocket-membrane-agent-go
  - pocket-membrane-agent-doi-10.1073_pnas.0909289106
  - pocket-membrane-agent-doi-10.1242_jcs.045740
  - pocket-membrane-agent-doi-10.1038_nrmicro2221
  - pocket-membrane-agent-doi-10.1016_j.pt.2020.11.005
  - pocket-membrane-agent-pmc-PMC2755463
  - pocket-membrane-agent-pmc-PMC2714436
  - pocket-membrane-agent-field2009-publisher
  - record
  - policy
findings: []
actions: []
limitations:
- Field/Carrington2009 was read only at the publisher Abstract and Key Points; Halliday2021
  only at the native metadata/abstract. Their full review bodies were not obtained.
  The Halliday publisher response was a stub despite HTTP200.
- Both2009 primary studies were available as genuine PMC HTML. Attempted version1
  S3 JATS endpoints returned404; this does not imply that the primary bodies were
  unavailable. Gadelha main text was read at the recorded complete scope; Lacomble
  only at the explicitly named sections.
- No figure pixels, raw tomography volumes, movies, supplementary data or quantitative
  membrane-particle counts were independently reanalysed. Collective membrane constitution
  is supported, while formation necessity of individual lipids or proteins remains
  untested in this review.
- Neighboring whole-pocket and collar records were used only for the frozen boundary
  fields. This review does not certify their remaining claims or establish a complete
  membrane proteome.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
