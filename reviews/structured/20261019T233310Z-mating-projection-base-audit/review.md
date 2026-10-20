# Mating projection base identity, topology and source review

- Review: 20261019T233310Z-mating-projection-base-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-19T07:43:47Z
- Finished UTC: 2026-10-19T23:33:10Z
- Reviewer: Codex scientific review agent (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The complete maintained record is supported at its stated regional scale. Exact GO identity, both narrow synonyms, is-a parent, projection parthood, all neighboring structure identifiers, species label, conditional taxonomic presence, canonical example and nonmechanistic graph were checked. No concrete curation defect was observed. The base is a defined anatomical region; the record does not invent a separate molecular complex or machinery assignment.

## Scope And Provenance

Full single-record assessment of every maintained field: definition, category/kind, two synonyms, parent and parthood, conditional distribution and example, all evidence, two graph nodes and one edge, resolved boundary discussion, status and available history. Seven unique GO terms, one NCBI taxon and the sole DOI were independently checked.

Selection: Tenth previously unreviewed target in the coordinating reviewer's ordered inventory: data/structures/appendage/mating_projection_base.yaml.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0001400 | data/structures/appendage/mating_projection_base.yaml | maintained | mating projection base |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema validation | passed | True | GO:0001400 | Focused LinkML validation returned No issues found. |
| strict validation | passed | True | GO:0001400 | Focused strict validation scanned one file and reported zero ERROR rows. |
| Stable identifiers and claim-level source inspection | passed | True | GO:0001400 | Inspected exact current GO definitions/relations, NCBI taxon identity and the sole primary paper as full text with relevant figure context. No material assertion depends on metadata alone. |
| Verbatim snippet applicability | not_applicable | False | GO:0001400 | The complete target has no snippet fields. No source quotation was added. |
| Protein and expression adapters applicability | not_applicable | False | GO:0001400 | No protein accession, gene assignment, regulator, expression module or transcriptomic dataset is asserted for this anatomical region. Such annotations would not establish its identity. |
| Target identifier coverage including resolver residuals | passed | True | GO:0001400 | All CURIE-shaped target values have issuing-authority or appropriate local/source-specific existence verification. Generic PMID HTTP414 failures and skipped namespaces were resolved by scoped receipts; biological mapping correctness is assessed separately. |
| Full corpus QC | passed | True | GO:0001400 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0001400 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0001400 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0001400 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0001400 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Base region and exact GO identity

identity: supported. Targets: GO:0001400.

GO:0001400 denotes the anatomical junction represented by the file. The definition, label, APPENDAGE category and SUBCELLULAR_REGION kind are compatible with that identity.

### Both narrow synonyms

nomenclature: supported. Targets: GO:0001400.

Both synonym strings and their NARROW scope exactly match the ontology. They do not broaden the record to the whole projection.

### Is-a parent versus parthood

grounding: supported. Targets: GO:0001400.

Cellular anatomical structure is the current asserted is-a parent; mating projection is the containing structure. QuickGO independently reproduces the ontology relations described as OLS-derived in the notes.

### Conditional species distribution and example

scope: supported. Targets: GO:0001400.

The taxon is correct. The projection-dependent base is consistent with the observed morphological response, and VARIABLE avoids treating the region as constitutively present.

### Regional composition scope

completeness: supported. Targets: GO:0001400.

No molecular components or fixed stoichiometry are asserted. For this regional record, leaving localized septin, polarisome and actin machinery with their owning structures avoids an unsupported component boundary.

### Single topological edge

graph: supported. Targets: GO:0001400.

The two node identities, edge direction and parthood description agree with GO. NONMECHANISTIC scope correctly limits the graph to topology; FUNCTION does not introduce a biochemical causal claim.

### Resolved neighboring-structure distinction

representation: supported. Targets: GO:0001400.

The base, whole projection, tip, membrane, septin ring and septin band are distinct ontology entities. The target does not assert that every neck has both septin morphologies, nor collapse a localized complex into the region.

### Optional function, measurement, image and dataset fields

completeness: not_applicable. Targets: GO:0001400.

No independent function, numerical property, image, licence or dataset claim is present. Their omission does not compromise this bounded anatomical record under the local checklist.

### Scientific status and available history

provenance: supported. Targets: GO:0001400.

Citations are attached at the relevant identity, scope, graph and discussion fields. The available history describes the maintained target, which remains PROPOSED. This review neither changes status nor substitutes for human sign-off.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/mating_projection_base.yaml; Entire target YAML; reread after resume | context_only | The target is a PROPOSED subcellular region with no molecular constituent, quantitative property or image assertion. Its sole graph edge is a regional parthood relation. Evidence and history retain distinct scope for neighboring projection structures. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0001400%2CGO%3A0110165%2CGO%3A0005937%2CGO%3A0043332%2CGO%3A0070250%2CGO%3A0032175%2CGO%3A0032162; All seven results: id/name/aspect/isObsolete/definition/synonyms; GO:0110165 and GO:0005937 children relations | supports | Every identifier is current and denotes the recorded cellular component. GO directly supports the base definition and narrow synonym scopes. The base is an is-a child of cellular anatomical structure and part of mating projection. Separate terms identify the tip, surrounding membrane, septin ring and diffuse septin band; both septin terms refer to neck localization. |
| taxonomy | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=4932; TaxaSet/Taxon: TaxId, ScientificName and Rank | supports | NCBITaxon:4932 resolves to species Saccharomyces cerevisiae, matching both distribution and example labels. |
| read-metadata | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1091/mbc.3.4.429&amp;format=json&amp;resultType=core; Core result DOI, title, author list, journal, year, PMID1498363 and PMC275593 | supports | The DOI resolves to Read, Okamura and Drubin 1992 in Molecular Biology of the Cell, volume 3, pages 429-444. The title and citation identity in the YAML match. This lookup verifies bibliographic identity separately from the paper-body inspection. |
| read-fulltext | https://europepmc.org/articles/PMC275593?pdf=render; DOI:10.1091/mbc.3.4.429; pp.429-432 Introduction, Table1, Methods and initial Results; Figure1 p.431 inspected visually | supports | The paper describes haploid mating-type cells and pheromone-induced projections. Wild-type DBY2055 and conditional mutants were assayed; the figure time course compares untreated cells with induced outgrowths continuous with the larger cell body. The text distinguishes pheromone doses that arrest cells from doses that induce morphology. This supports VARIABLE presence and the budding-yeast example. GO supplies the formal regional name. |
| read-author-copy | https://www.researchgate.net/profile/David-Drubin/publication/21658084_Actin-_and_tubulin-dependent_functions_during_Saccharomyces_cerevisiae_mating_projection_formation/links/09e4150fef1cec6344000000/Actin-and-tubulin-dependent-functions-during-Saccharomyces-cerevisiae-mating-projection-formation.pdf; Same 16-page primary article; first pages and methods/results compared with official PDF | supports | An author-uploaded copy independently exposed the full source text after publisher and PMC web failures. Bibliographic details and relevant biological content agree with the official Europe PMC snapshot. It is the same study, not independent experimental replication. |
| history | history/records/mating_projection_base/2026-09-30T213157Z-codex-b63c75.yaml; Whole CREATE event and target curation_history | context_only | The historical creation event identifies this GO term, maintained path, regional topology and boundary decision. Current status remains PROPOSED; no human review promotion is asserted. |
| siblings | data/structures/; Identity, parthood and discussions of mating_projection, mating_projection_membrane, mating_projection_tip, mating_projection_septin_ring and mating_projection_septin_band; exact paths and hashes in source.inputs | context_only | The neighboring structures have distinct maintained records, consistent with the target's resolved boundary decision. Their complete scientific correctness is outside this single-record review. Ring-versus-band qualifications in the sibling records are not overridden. |
| source-route-limits | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC275593/fullTextXML; Access attempts in source-access.json; successful official PDF metadata in mating-review/read-epmc-pdf.meta.json | context_only | Initial fullTextXML access failed, BioC was rate-limited and publisher PDF returned forbidden. Official Europe PMC PDF had already been retrieved successfully by the collaborating reviewer at 2026-10-19T07:44:14Z; its bytes, metadata and extracted text were inspected in this review. These failures did not leave a source-support gap. |
| schema-result | UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache just validate data/structures/appendage/mating_projection_base.yaml; Retained diagnostic log; actual process exit code 0, reread after resume | supports | Focused LinkML validation returned No issues found. |
| strict-result | UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache just validate-strict data/structures/appendage/mating_projection_base.yaml --out /private/tmp/cellstructure-record-reviews-UhRFh7/mating-projection-base/strict.tsv; Retained diagnostic log; actual process exit code 0, reread after resume | supports | Focused strict validation scanned one file and reported zero ERROR rows. |
| target-resolver-coverage | just check-curies-strict; data/structures/appendage/mating_projection_base.yaml; exact scripts/check_curies.py collect() scope; reports/curie_check.tsv | supports | This target contains 9 distinct CURIE-shaped scalar values: 9 OK, 0 transport-unreachable and 0 skipped in the global report. The attached scoped receipts resolve each non-OK identifier. HTTP URLs and prose are outside collect(); their content was inspected separately. Existence is not proof of correct biological mapping. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Read 1992 examines pheromone-induced projection formation and associated cytoskeletal changes. Its microscopy supports the projection-body junction morphologically; the formal identity of that junction as the mating projection base comes from GO. The review does not claim molecular demarcation or an exhaustive base-specific protein inventory.
- Some live publisher and PMC routes failed. The full primary paper was nevertheless inspected through an author-uploaded PDF and a separately retrieved official Europe PMC PDF, including source figures. No required biological claim remained inaccessible.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly requested one saved review per inspected record, including clean observations; this overrides the local issue-only persistence gate without creating a finding.
- No scientific record, generated page, curation history or external shared content was changed. This is a structured review observation.
- The review resumed after a session interruption. All repository input hashes were compared with the original inspection on 2026-10-19T23:29:30Z and were unchanged. Original provenance was preserved.
- No verbatim paper text is reproduced.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261019T233310Z-mating-projection-base-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Mating projection base identity, topology and source review
started_at: '2026-10-19T07:43:47Z'
finished_at: '2026-10-19T23:33:10Z'
reviewer:
  identity: Codex scientific review agent
  kind: agent
  independence: unknown
  independence_basis: A separate agent performed this read-only review; the existing
    record history names Codex, so independence from earlier authorship is not asserted.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: The complete maintained record is supported at its stated regional scale.
  Exact GO identity, both narrow synonyms, is-a parent, projection parthood, all neighboring
  structure identifiers, species label, conditional taxonomic presence, canonical
  example and nonmechanistic graph were checked. No concrete curation defect was observed.
  The base is a defined anatomical region; the record does not invent a separate molecular
  complex or machinery assignment.
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
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/appendage/mating_projection.yaml
    sha256: bab39726b1ad7003dbf3f66e8d48d088365fac303dcbfeef0aae4009b26cc1b0
    role: context
  - path: data/structures/appendage/mating_projection_base.yaml
    sha256: eddb868bc0a45a7cef478d5e4b0ea468fcb1ab65582b40b29863d41d36506d9d
    role: target
  - path: data/structures/appendage/mating_projection_membrane.yaml
    sha256: d1ed93a7c920c648dbb7ae5967579738c66ac620fa3f16513d465d18d75fd473
    role: context
  - path: data/structures/cytoskeleton/mating_projection_septin_band.yaml
    sha256: e68377ea65b5be456416810adb14479747220176a957b97f6d3ce3f5e731354d
    role: context
  - path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    sha256: 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6
    role: context
  - path: data/structures/other/mating_projection_tip.yaml
    sha256: ec2a7085e4d50080981c50bd9b523d8ffabf4de5739bbe1b696c382fddb7e1ad
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
  - path: history/records/mating_projection_base/2026-09-30T213157Z-codex-b63c75.yaml
    sha256: d932ee2b3e67584e1c85e5c388eaaa738433ad1c3b9b36af04055be0cb040b47
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
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0001400
  path: data/structures/appendage/mating_projection_base.yaml
  label: mating projection base
  record_class: CellStructureRecord
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/mating_projection_base.yaml
    role: maintained scientific record
scope:
  description: 'Full single-record assessment of every maintained field: definition,
    category/kind, two synonyms, parent and parthood, conditional distribution and
    example, all evidence, two graph nodes and one edge, resolved boundary discussion,
    status and available history. Seven unique GO terms, one NCBI taxon and the sole
    DOI were independently checked.'
  selection: 'Tenth previously unreviewed target in the coordinating reviewer''s ordered
    inventory: data/structures/appendage/mating_projection_base.yaml.'
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0001400
checks:
- check_id: schema
  name: schema validation
  status: passed
  required: true
  summary: Focused LinkML validation returned No issues found.
  target_ids:
  - GO:0001400
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/mating_projection_base.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - schema-result
  scope_note: The selected maintained target only.
- check_id: strict
  name: strict validation
  status: passed
  required: true
  summary: Focused strict validation scanned one file and reported zero ERROR rows.
  target_ids:
  - GO:0001400
  command: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/mating_projection_base.yaml --out
    /private/tmp/cellstructure-record-reviews-UhRFh7/mating-projection-base/strict.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - strict-result
  scope_note: The selected maintained target only.
- check_id: source-inspection
  name: Stable identifiers and claim-level source inspection
  status: passed
  required: true
  summary: Inspected exact current GO definitions/relations, NCBI taxon identity and
    the sole primary paper as full text with relevant figure context. No material
    assertion depends on metadata alone.
  target_ids:
  - GO:0001400
  evidence_ids:
  - go
  - taxonomy
  - read-metadata
  - read-fulltext
  - read-author-copy
- check_id: snippet-audit
  name: Verbatim snippet applicability
  status: not_applicable
  required: false
  summary: The complete target has no snippet fields. No source quotation was added.
  target_ids:
  - GO:0001400
  evidence_ids:
  - record
- check_id: protein-adapters
  name: Protein and expression adapters applicability
  status: not_applicable
  required: false
  summary: No protein accession, gene assignment, regulator, expression module or
    transcriptomic dataset is asserted for this anatomical region. Such annotations
    would not establish its identity.
  target_ids:
  - GO:0001400
  evidence_ids:
  - record
- check_id: target-identifier-coverage
  name: Target identifier coverage including resolver residuals
  status: passed
  required: true
  target_ids:
  - GO:0001400
  summary: All CURIE-shaped target values have issuing-authority or appropriate local/source-specific
    existence verification. Generic PMID HTTP414 failures and skipped namespaces were
    resolved by scoped receipts; biological mapping correctness is assessed separately.
  evidence_ids:
  - target-resolver-coverage
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0001400
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0001400
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0001400
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0001400
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0001400
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused across
    the batch because maintained scientific inputs are unchanged. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/mating_projection_base.yaml
  locator: Entire target YAML; reread after resume
  accessed_at: '2026-10-19T23:30:06Z'
  support: context_only
  summary: The target is a PROPOSED subcellular region with no molecular constituent,
    quantitative property or image assertion. Its sole graph edge is a regional parthood
    relation. Evidence and history retain distinct scope for neighboring projection
    structures.
  snapshot_sha256: eddb868bc0a45a7cef478d5e4b0ea468fcb1ab65582b40b29863d41d36506d9d
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0001400%2CGO%3A0110165%2CGO%3A0005937%2CGO%3A0043332%2CGO%3A0070250%2CGO%3A0032175%2CGO%3A0032162
  locator: 'All seven results: id/name/aspect/isObsolete/definition/synonyms; GO:0110165
    and GO:0005937 children relations'
  accessed_at: '2026-10-19T07:44:16Z'
  support: supports
  summary: Every identifier is current and denotes the recorded cellular component.
    GO directly supports the base definition and narrow synonym scopes. The base is
    an is-a child of cellular anatomical structure and part of mating projection.
    Separate terms identify the tip, surrounding membrane, septin ring and diffuse
    septin band; both septin terms refer to neck localization.
  snapshot_sha256: 8e13f4a687e4c6c572e6c1cecf521e4eda9648b34e33a3bda2e6248b42b8b6f2
- evidence_id: taxonomy
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=4932
  locator: 'TaxaSet/Taxon: TaxId, ScientificName and Rank'
  accessed_at: '2026-10-19T07:44:16Z'
  support: supports
  summary: NCBITaxon:4932 resolves to species Saccharomyces cerevisiae, matching both
    distribution and example labels.
  snapshot_sha256: da089959ea98b54a0b26b43b88037705e7aed37e969e5c789267f92803002124
- evidence_id: read-metadata
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1091/mbc.3.4.429&format=json&resultType=core
  locator: Core result DOI, title, author list, journal, year, PMID1498363 and PMC275593
  accessed_at: '2026-10-19T07:44:16Z'
  support: supports
  summary: The DOI resolves to Read, Okamura and Drubin 1992 in Molecular Biology
    of the Cell, volume 3, pages 429-444. The title and citation identity in the YAML
    match. This lookup verifies bibliographic identity separately from the paper-body
    inspection.
  snapshot_sha256: e40166f985fb75ad35a272b15e27fa6765dd6078753097cb0a2f2f4f12661b8f
- evidence_id: read-fulltext
  kind: primary_source
  reference: https://europepmc.org/articles/PMC275593?pdf=render
  locator: DOI:10.1091/mbc.3.4.429; pp.429-432 Introduction, Table1, Methods and initial
    Results; Figure1 p.431 inspected visually
  accessed_at: '2026-10-19T23:29:52Z'
  support: supports
  summary: The paper describes haploid mating-type cells and pheromone-induced projections.
    Wild-type DBY2055 and conditional mutants were assayed; the figure time course
    compares untreated cells with induced outgrowths continuous with the larger cell
    body. The text distinguishes pheromone doses that arrest cells from doses that
    induce morphology. This supports VARIABLE presence and the budding-yeast example.
    GO supplies the formal regional name.
  snapshot_sha256: 63d19679ef508f4c22b3a6a6428f2d78e1eefa32016310daac96f7753dc60377
- evidence_id: read-author-copy
  kind: primary_source
  reference: https://www.researchgate.net/profile/David-Drubin/publication/21658084_Actin-_and_tubulin-dependent_functions_during_Saccharomyces_cerevisiae_mating_projection_formation/links/09e4150fef1cec6344000000/Actin-and-tubulin-dependent-functions-during-Saccharomyces-cerevisiae-mating-projection-formation.pdf
  locator: Same 16-page primary article; first pages and methods/results compared
    with official PDF
  accessed_at: '2026-10-19T23:29:30Z'
  support: supports
  summary: An author-uploaded copy independently exposed the full source text after
    publisher and PMC web failures. Bibliographic details and relevant biological
    content agree with the official Europe PMC snapshot. It is the same study, not
    independent experimental replication.
- evidence_id: history
  kind: record_content
  reference: history/records/mating_projection_base/2026-09-30T213157Z-codex-b63c75.yaml
  locator: Whole CREATE event and target curation_history
  accessed_at: '2026-10-19T23:30:06Z'
  support: context_only
  summary: The historical creation event identifies this GO term, maintained path,
    regional topology and boundary decision. Current status remains PROPOSED; no human
    review promotion is asserted.
- evidence_id: siblings
  kind: record_content
  reference: data/structures/
  locator: Identity, parthood and discussions of mating_projection, mating_projection_membrane,
    mating_projection_tip, mating_projection_septin_ring and mating_projection_septin_band;
    exact paths and hashes in source.inputs
  accessed_at: '2026-10-19T23:30:56Z'
  support: context_only
  summary: The neighboring structures have distinct maintained records, consistent
    with the target's resolved boundary decision. Their complete scientific correctness
    is outside this single-record review. Ring-versus-band qualifications in the sibling
    records are not overridden.
- evidence_id: source-route-limits
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC275593/fullTextXML
  locator: Access attempts in source-access.json; successful official PDF metadata
    in mating-review/read-epmc-pdf.meta.json
  accessed_at: '2026-10-19T23:29:52Z'
  support: context_only
  summary: Initial fullTextXML access failed, BioC was rate-limited and publisher
    PDF returned forbidden. Official Europe PMC PDF had already been retrieved successfully
    by the collaborating reviewer at 2026-10-19T07:44:14Z; its bytes, metadata and
    extracted text were inspected in this review. These failures did not leave a source-support
    gap.
- evidence_id: schema-result
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate data/structures/appendage/mating_projection_base.yaml
  locator: Retained diagnostic log; actual process exit code 0, reread after resume
  accessed_at: '2026-10-19T23:29:30Z'
  support: supports
  summary: Focused LinkML validation returned No issues found.
  snapshot_sha256: 7e1299e7f9a3e43c124b4d3b8b012ebcdc4d6eba02e92b82bb35eae64f75d39c
- evidence_id: strict-result
  kind: validation
  reference: UV_CACHE_DIR=/private/tmp/cellstructure-record-reviews-UhRFh7/uv-cache
    just validate-strict data/structures/appendage/mating_projection_base.yaml --out
    /private/tmp/cellstructure-record-reviews-UhRFh7/mating-projection-base/strict.tsv
  locator: Retained diagnostic log; actual process exit code 0, reread after resume
  accessed_at: '2026-10-19T23:29:30Z'
  support: supports
  summary: Focused strict validation scanned one file and reported zero ERROR rows.
  snapshot_sha256: 24641bda8d035e064ff2ba5cd7c0dd10624911405a6df58bf61fe7052d1ff24b
- evidence_id: target-resolver-coverage
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/appendage/mating_projection_base.yaml; exact scripts/check_curies.py
    collect() scope; reports/curie_check.tsv
  accessed_at: '2026-10-19T23:32:25.400320Z'
  support: supports
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
  summary: 'This target contains 9 distinct CURIE-shaped scalar values: 9 OK, 0 transport-unreachable
    and 0 skipped in the global report. The attached scoped receipts resolve each
    non-OK identifier. HTTP URLs and prose are outside collect(); their content was
    inspected separately. Existence is not proof of correct biological mapping.'
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
  topic: Base region and exact GO identity
  outcome: supported
  summary: GO:0001400 denotes the anatomical junction represented by the file. The
    definition, label, APPENDAGE category and SUBCELLULAR_REGION kind are compatible
    with that identity.
  target_ids:
  - GO:0001400
  evidence_ids:
  - record
  - go
- assessment_id: synonyms
  area: nomenclature
  topic: Both narrow synonyms
  outcome: supported
  summary: Both synonym strings and their NARROW scope exactly match the ontology.
    They do not broaden the record to the whole projection.
  target_ids:
  - GO:0001400
  evidence_ids:
  - go
- assessment_id: hierarchy
  area: grounding
  topic: Is-a parent versus parthood
  outcome: supported
  summary: Cellular anatomical structure is the current asserted is-a parent; mating
    projection is the containing structure. QuickGO independently reproduces the ontology
    relations described as OLS-derived in the notes.
  target_ids:
  - GO:0001400
  evidence_ids:
  - go
  - record
- assessment_id: scope
  area: scope
  topic: Conditional species distribution and example
  outcome: supported
  summary: The taxon is correct. The projection-dependent base is consistent with
    the observed morphological response, and VARIABLE avoids treating the region as
    constitutively present.
  target_ids:
  - GO:0001400
  evidence_ids:
  - taxonomy
  - read-fulltext
  - go
  dimensions:
  - name: organism
    value: Saccharomyces cerevisiae; haploid mating-type strains
    definition: Experimental organism and mating context supporting the conditional
      example.
    evidence_ids:
    - taxonomy
    - read-fulltext
  - name: evidence_scale
    value: Source microscopy and morphological time course, with GO regional definition
    definition: The base is identified anatomically, without an inferred base-specific
      molecular inventory.
    evidence_ids:
    - read-fulltext
    - go
- assessment_id: components
  area: completeness
  topic: Regional composition scope
  outcome: supported
  summary: No molecular components or fixed stoichiometry are asserted. For this regional
    record, leaving localized septin, polarisome and actin machinery with their owning
    structures avoids an unsupported component boundary.
  target_ids:
  - GO:0001400
  evidence_ids:
  - record
  - go
  - siblings
- assessment_id: graph
  area: graph
  topic: Single topological edge
  outcome: supported
  summary: The two node identities, edge direction and parthood description agree
    with GO. NONMECHANISTIC scope correctly limits the graph to topology; FUNCTION
    does not introduce a biochemical causal claim.
  target_ids:
  - GO:0001400
  evidence_ids:
  - record
  - go
- assessment_id: boundary
  area: representation
  topic: Resolved neighboring-structure distinction
  outcome: supported
  summary: The base, whole projection, tip, membrane, septin ring and septin band
    are distinct ontology entities. The target does not assert that every neck has
    both septin morphologies, nor collapse a localized complex into the region.
  target_ids:
  - GO:0001400
  evidence_ids:
  - go
  - siblings
  - record
- assessment_id: functions-properties
  area: completeness
  topic: Optional function, measurement, image and dataset fields
  outcome: not_applicable
  summary: No independent function, numerical property, image, licence or dataset
    claim is present. Their omission does not compromise this bounded anatomical record
    under the local checklist.
  target_ids:
  - GO:0001400
  evidence_ids:
  - record
- assessment_id: provenance
  area: provenance
  topic: Scientific status and available history
  outcome: supported
  summary: Citations are attached at the relevant identity, scope, graph and discussion
    fields. The available history describes the maintained target, which remains PROPOSED.
    This review neither changes status nor substitutes for human sign-off.
  target_ids:
  - GO:0001400
  evidence_ids:
  - record
  - history
  - read-metadata
findings: []
actions: []
limitations:
- Read 1992 examines pheromone-induced projection formation and associated cytoskeletal
  changes. Its microscopy supports the projection-body junction morphologically; the
  formal identity of that junction as the mating projection base comes from GO. The
  review does not claim molecular demarcation or an exhaustive base-specific protein
  inventory.
- Some live publisher and PMC routes failed. The full primary paper was nevertheless
  inspected through an author-uploaded PDF and a separately retrieved official Europe
  PMC PDF, including source figures. No required biological claim remained inaccessible.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The user explicitly requested one saved review per inspected record, including clean
  observations; this overrides the local issue-only persistence gate without creating
  a finding.
- No scientific record, generated page, curation history or external shared content
  was changed. This is a structured review observation.
- The review resumed after a session interruption. All repository input hashes were
  compared with the original inspection on 2026-10-19T23:29:30Z and were unchanged.
  Original provenance was preserved.
- No verbatim paper text is reproduced.
```
