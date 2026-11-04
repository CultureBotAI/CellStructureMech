# Nuclear microtubule identity and budding-yeast organization review

- Review: 20261021T074814Z-nuclear-microtubule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:36:44Z
- Finished UTC: 2026-10-21T07:48:14Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact nuclear microtubule identity, nuclear parthood and the bounded budding-yeast inner-plaque organization example are supported. No concrete correction established at the claimed scope.

## Scope And Provenance

Entire maintained target, native GO/taxon identifiers and relationships, cited review metadata and relevant author-manuscript body sections; focused validation and source/input hashes.

Selection: Seventh unreviewed path in batch nine, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005880 | data/structures/cytoskeleton/nuclear_microtubule.yaml | maintained | nuclear microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005880 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005880 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0005880 | 8 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0005880 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0005880 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005880 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005880 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005880 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0005880 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Nuclear microtubule class

identity: supported. Targets: GO:0005880.

Exact active GO identity, definition, is_a microtubule parent and part_of nucleus relationship are directly confirmed. FILAMENT/CYTOSKELETON treatment is compatible with a microtubule subtype.

### Location versus spindle membership

scope: supported. Targets: GO:0005880.

Cytoplasmic and nuclear location distinguish the two GO classes; spindle microtubule is defined by mitotic or meiotic spindle membership. The discussion does not require global disjointness, and the cited yeast nuclear microtubules can also be spindle microtubules.

### Budding-yeast example

scope: supported. Targets: GO:0005880.

Species4932 and the nuclear face of budding-yeast SPBs are supported. COMMON is read as normal occurrence in the cited model, not measured prevalence or universal eukaryotic organization. No strain equivalence or clade-wide distribution is inferred.

### Array organization at the inner plaque

evidence: supported. Targets: GO:0005880.

The record says nuclear arrays can be organized from sites such as the budding-yeast inner plaque. The review directly supplies this example, while GO supplies spatial class identity. The text does not generalize the yeast nucleation site to every nuclear microtubule.

### Nonmechanistic organizing-site graph

graph: supported. Targets: GO:0005880.

The subtype edge is directly supported by GO and the organizes edge by the cited review body. The graph is explicitly NONMECHANISTIC and does not turn a spatial association into a complete biochemical pathway or claim that plaque/nucleation proteins are tubulin polymer constituents.

### Deferred molecular inventory

completeness: supported. Targets: GO:0005880.

The class identity and alpha/beta polymer nature are supported by GO and the review. Taxon-specific motors, plus-end factors and gamma-tubulin nucleation machinery remain explicitly deferred. No exact molecular inventory is claimed; an empty optional component list is not by itself a demonstrated correction. Plaque anchors and nucleation complexes must remain distinct from the microtubule polymer.

### Citation identity and readable review body

provenance: supported. Targets: GO:0005880.

The DOI resolves exactly and the claim-bearing review manuscript sections were read. This is an author-uploaded secondary review, not new primary experimental evidence or publisher-version byte attestation. Historical record evidence notes accurately identify it as a review.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| nuclear-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005880,GO:0005874,GO:0005634,GO:0005822,GO:0005881,GO:0005876; results[id=GO:0005880/GO:0005874/GO:0005634/GO:0005822/GO:0005881/GO:0005876], definitions and explicit children relation fields | supports | All six active identities and definitions match. GO:0005874 children explicitly give GO:0005880 is_a, and GO:0005634 children give it part_of. GO:0005822 denotes the inner plaque in the nucleus. Nuclear location and spindle membership are distinct criteria that can overlap in budding yeast. |
| nuclear-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName and rank | supports | 4932 denotes the species Saccharomyces cerevisiae. The record asserts a species example without assigning an experimental strain. |
| nuclear-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1146/annurev.cellbio.20.022003.114106%22; resultList.result[PMID15473833], DOI/title/authors/year/pubTypeList and abstractText | supports | Exact DOI query resolves Jaspersen and Winey 2004, PMID15473833, with matching title and review publication type. The full returned abstract was read; metadata alone is not the body evidence. |
| nuclear-agent-jaspersen-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author manuscript p5 Introduction/SPB Structure, browser lines187-218; pp8-9 Core SPB lines332-372. SHA256 is serialized browser extraction, not native publisher response bytes; no independent HTTP status attestation. | supports | Literature review, not a primary experiment. Author manuscript states that budding-yeast SPBs stay embedded in the nuclear envelope and organize nuclear and cytoplasmic microtubules; the inner plaque faces the nucleoplasm. The Spc110 discussion supplies the nuclear-face organizing context without making Spc110 part of the alpha/beta polymer. Public author upload dated2014-09-23. The reused original receipt retains its original access time; its inherited status200 field is not treated as verified HTTP response status because it explicitly describes browser-extracted text. |
| nuclear-agent-jaspersen-nucleation-browser | https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function; Author manuscript pp24-25 Microtubule Nucleation, browser lines978-1034; p26 Microtubule-Dependent SPB Functions lines1038-1073. SHA256 is exact JSON-encoded web.run browser response; tool supplies no HTTP status. | supports | Literature review, not a primary experiment. The nucleation section describes polarized alpha/beta-tubulin arrays extending from the SPB into cytoplasm and nucleoplasm. The following function section explicitly places nuclear microtubule origins at the inner plaque, with gamma-tubulin complex binding Spc110, and contrasts the cytoplasmic plaque/half-bridge. This supports the bounded organization claim and demonstrates that nuclear and spindle classes overlap in the cited model. |
| record | data/structures/cytoskeleton/nuclear_microtubule.yaml; Entire record, identity, taxa, functions, nonmechanistic graph, evidence and both discussions | context_only | The record defines a location-based microtubule subtype and uses budding yeast as one organizing example. It asserts no protein accession, exact nucleator composition, quantitative measurement, image or verbatim evidence snippet. The graph contains only native GO identifiers; no neighboring local record content informed this review. |
| schema-result | just validate data/structures/cytoskeleton/nuclear_microtubule.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/nuclear_microtubule.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/nuclear_microtubule.yaml --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/nuclear_microtubule-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/nuclear_microtubule.yaml --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/nuclear_microtubule-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch9-20261021-t98tzqpa/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch9-20261021-t98tzqpa/nuclear_microtubule-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/nuclear_microtubule.yaml; exact collect() scope; SHA256 identifies the entire original curie_check.tsv, not resolver-slice.json | supports | 8 of 8 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The cited literature is a secondary review. Relevant author-manuscript sections were inspected, not the entire article or every underlying primary experiment.
- Browser-extracted author manuscript text is not publisher-native PDF bytes. The original reused receipt is preserved, but its status200 field is not used as an HTTP attestation; the new extraction has no HTTP status.
- The budding-yeast inner-plaque example does not establish a universal nuclear nucleation site, clade prevalence, complete molecular inventory or experimental strain.
- Associated proteins and nucleation complexes remain explicit curation work. No exact family or protein mapping is asserted by this target.
- Distinct nuclear and spindle definitions do not imply disjoint structures; the yeast example includes nuclear spindle microtubules.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.
- Parent reviewed the full target, draft, claim-specific source packet, native input/source hashes and selected supporting source sections. Independent source collaborators checked remaining cited sections and source attribution. Parent accepts the bounded assessments before persistence.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T074814Z-nuclear-microtubule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Nuclear microtubule identity and budding-yeast organization review
started_at: '2026-10-21T07:36:44Z'
finished_at: '2026-10-21T07:48:14Z'
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
summary: Exact nuclear microtubule identity, nuclear parthood and the bounded budding-yeast
  inner-plaque organization example are supported. No concrete correction established
  at the claimed scope.
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
  - path: data/structures/cytoskeleton/nuclear_microtubule.yaml
    sha256: 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252
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
- target_id: GO:0005880
  path: data/structures/cytoskeleton/nuclear_microtubule.yaml
  label: nuclear microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/nuclear_microtubule.yaml
    role: maintained scientific record
scope:
  description: Entire maintained target, native GO/taxon identifiers and relationships,
    cited review metadata and relevant author-manuscript body sections; focused validation
    and source/input hashes.
  selection: Seventh unreviewed path in batch nine, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005880
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just validate data/structures/cytoskeleton/nuclear_microtubule.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just validate-strict data/structures/cytoskeleton/nuclear_microtubule.yaml
    --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/nuclear_microtubule-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0005880
  summary: 8 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005880
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - nuclear-agent-go
  - nuclear-agent-taxon
  - nuclear-agent-epmc
  - nuclear-agent-jaspersen-browser
  - nuclear-agent-jaspersen-nucleation-browser
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005880
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch9 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: nuclear-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005880,GO:0005874,GO:0005634,GO:0005822,GO:0005881,GO:0005876
  locator: results[id=GO:0005880/GO:0005874/GO:0005634/GO:0005822/GO:0005881/GO:0005876],
    definitions and explicit children relation fields
  accessed_at: '2026-10-21T07:43:25.790606Z'
  support: supports
  summary: All six active identities and definitions match. GO:0005874 children explicitly
    give GO:0005880 is_a, and GO:0005634 children give it part_of. GO:0005822 denotes
    the inner plaque in the nucleus. Nuclear location and spindle membership are distinct
    criteria that can overlap in budding yeast.
  snapshot_sha256: b38984db5ca7c25b8713102f88d7a26e1ea0a9c1ca9c312095f1f425ad84401d
- evidence_id: nuclear-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName and rank
  accessed_at: '2026-10-21T07:43:25.788893Z'
  support: supports
  summary: 4932 denotes the species Saccharomyces cerevisiae. The record asserts a
    species example without assigning an experimental strain.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: nuclear-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1146/annurev.cellbio.20.022003.114106%22
  locator: resultList.result[PMID15473833], DOI/title/authors/year/pubTypeList and
    abstractText
  accessed_at: '2026-10-21T07:43:25.868048Z'
  support: supports
  summary: Exact DOI query resolves Jaspersen and Winey 2004, PMID15473833, with matching
    title and review publication type. The full returned abstract was read; metadata
    alone is not the body evidence.
  snapshot_sha256: 8979c5d9e2c5cd8beecce7ff11b7ea31d5a4dbb6fb49886f3fffb6ecaa8c3a73
- evidence_id: nuclear-agent-jaspersen-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Author manuscript p5 Introduction/SPB Structure, browser lines187-218;
    pp8-9 Core SPB lines332-372. SHA256 is serialized browser extraction, not native
    publisher response bytes; no independent HTTP status attestation.
  accessed_at: '2026-10-21T07:24:18Z'
  support: supports
  summary: Literature review, not a primary experiment. Author manuscript states that
    budding-yeast SPBs stay embedded in the nuclear envelope and organize nuclear
    and cytoplasmic microtubules; the inner plaque faces the nucleoplasm. The Spc110
    discussion supplies the nuclear-face organizing context without making Spc110
    part of the alpha/beta polymer. Public author upload dated2014-09-23. The reused
    original receipt retains its original access time; its inherited status200 field
    is not treated as verified HTTP response status because it explicitly describes
    browser-extracted text.
  snapshot_sha256: 8aa2398ded5512b2450c936e832c11bc46d77ac317e4c01a2f7a6b9f1a4fce4e
- evidence_id: nuclear-agent-jaspersen-nucleation-browser
  kind: authority
  reference: https://www.researchgate.net/publication/8241691_THE_BUDDING_YEAST_SPINDLE_POLE_BODY_Structure_Duplication_and_Function
  locator: Author manuscript pp24-25 Microtubule Nucleation, browser lines978-1034;
    p26 Microtubule-Dependent SPB Functions lines1038-1073. SHA256 is exact JSON-encoded
    web.run browser response; tool supplies no HTTP status.
  accessed_at: '2026-10-21T07:43:49.372408Z'
  support: supports
  summary: Literature review, not a primary experiment. The nucleation section describes
    polarized alpha/beta-tubulin arrays extending from the SPB into cytoplasm and
    nucleoplasm. The following function section explicitly places nuclear microtubule
    origins at the inner plaque, with gamma-tubulin complex binding Spc110, and contrasts
    the cytoplasmic plaque/half-bridge. This supports the bounded organization claim
    and demonstrates that nuclear and spindle classes overlap in the cited model.
  snapshot_sha256: 5c038e01761413d522e0ea145ffefb28f289f6f2f5cc3b55c8deb377bf2aa0cf
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/nuclear_microtubule.yaml
  locator: Entire record, identity, taxa, functions, nonmechanistic graph, evidence
    and both discussions
  accessed_at: '2026-10-21T07:47:02Z'
  support: context_only
  summary: The record defines a location-based microtubule subtype and uses budding
    yeast as one organizing example. It asserts no protein accession, exact nucleator
    composition, quantitative measurement, image or verbatim evidence snippet. The
    graph contains only native GO identifiers; no neighboring local record content
    informed this review.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/nuclear_microtubule.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:36:48Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/nuclear_microtubule.yaml'
  snapshot_sha256: fb5c4d1b7ab0c3196078797b19ab43ee6fd36bbb037a8bd77e58a3555347a81a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/nuclear_microtubule.yaml
    --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/nuclear_microtubule-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:36:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/nuclear_microtubule.yaml\
    \ --out /private/tmp/cellstructure-batch9-20261021-t98tzqpa/nuclear_microtubule-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch9-20261021-t98tzqpa/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch9-20261021-t98tzqpa/nuclear_microtubule-strict.tsv"
  snapshot_sha256: 6bede8cef59feb1b78942c420697dd18e563b040cfd650e5a2bab47cf0e15b49
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/nuclear_microtubule.yaml; exact collect()
    scope; SHA256 identifies the entire original curie_check.tsv, not resolver-slice.json
  accessed_at: '2026-10-21T07:47:02Z'
  support: supports
  summary: '8 of 8 collected target identifiers returned OK at the unchanged base.
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
  topic: Nuclear microtubule class
  outcome: supported
  target_ids:
  - GO:0005880
  summary: Exact active GO identity, definition, is_a microtubule parent and part_of
    nucleus relationship are directly confirmed. FILAMENT/CYTOSKELETON treatment is
    compatible with a microtubule subtype.
  evidence_ids:
  - nuclear-agent-go
  - record
- assessment_id: boundaries
  area: scope
  topic: Location versus spindle membership
  outcome: supported
  target_ids:
  - GO:0005880
  summary: Cytoplasmic and nuclear location distinguish the two GO classes; spindle
    microtubule is defined by mitotic or meiotic spindle membership. The discussion
    does not require global disjointness, and the cited yeast nuclear microtubules
    can also be spindle microtubules.
  evidence_ids:
  - nuclear-agent-go
  - nuclear-agent-jaspersen-nucleation-browser
  - record
- assessment_id: taxon
  area: scope
  topic: Budding-yeast example
  outcome: supported
  target_ids:
  - GO:0005880
  summary: Species4932 and the nuclear face of budding-yeast SPBs are supported. COMMON
    is read as normal occurrence in the cited model, not measured prevalence or universal
    eukaryotic organization. No strain equivalence or clade-wide distribution is inferred.
  evidence_ids:
  - nuclear-agent-taxon
  - nuclear-agent-jaspersen-browser
  - nuclear-agent-jaspersen-nucleation-browser
  - record
- assessment_id: function
  area: evidence
  topic: Array organization at the inner plaque
  outcome: supported
  target_ids:
  - GO:0005880
  summary: The record says nuclear arrays can be organized from sites such as the
    budding-yeast inner plaque. The review directly supplies this example, while GO
    supplies spatial class identity. The text does not generalize the yeast nucleation
    site to every nuclear microtubule.
  evidence_ids:
  - nuclear-agent-go
  - nuclear-agent-jaspersen-browser
  - nuclear-agent-jaspersen-nucleation-browser
  - record
- assessment_id: graph
  area: graph
  topic: Nonmechanistic organizing-site graph
  outcome: supported
  target_ids:
  - GO:0005880
  summary: The subtype edge is directly supported by GO and the organizes edge by
    the cited review body. The graph is explicitly NONMECHANISTIC and does not turn
    a spatial association into a complete biochemical pathway or claim that plaque/nucleation
    proteins are tubulin polymer constituents.
  evidence_ids:
  - nuclear-agent-go
  - nuclear-agent-jaspersen-browser
  - nuclear-agent-jaspersen-nucleation-browser
  - record
- assessment_id: composition
  area: completeness
  topic: Deferred molecular inventory
  outcome: supported
  target_ids:
  - GO:0005880
  summary: The class identity and alpha/beta polymer nature are supported by GO and
    the review. Taxon-specific motors, plus-end factors and gamma-tubulin nucleation
    machinery remain explicitly deferred. No exact molecular inventory is claimed;
    an empty optional component list is not by itself a demonstrated correction. Plaque
    anchors and nucleation complexes must remain distinct from the microtubule polymer.
  evidence_ids:
  - nuclear-agent-go
  - nuclear-agent-jaspersen-nucleation-browser
  - record
- assessment_id: source-tier
  area: provenance
  topic: Citation identity and readable review body
  outcome: supported
  target_ids:
  - GO:0005880
  summary: The DOI resolves exactly and the claim-bearing review manuscript sections
    were read. This is an author-uploaded secondary review, not new primary experimental
    evidence or publisher-version byte attestation. Historical record evidence notes
    accurately identify it as a review.
  evidence_ids:
  - nuclear-agent-epmc
  - nuclear-agent-jaspersen-browser
  - nuclear-agent-jaspersen-nucleation-browser
  - record
findings: []
actions: []
limitations:
- The cited literature is a secondary review. Relevant author-manuscript sections
  were inspected, not the entire article or every underlying primary experiment.
- Browser-extracted author manuscript text is not publisher-native PDF bytes. The
  original reused receipt is preserved, but its status200 field is not used as an
  HTTP attestation; the new extraction has no HTTP status.
- The budding-yeast inner-plaque example does not establish a universal nuclear nucleation
  site, clade prevalence, complete molecular inventory or experimental strain.
- Associated proteins and nucleation complexes remain explicit curation work. No exact
  family or protein mapping is asserted by this target.
- Distinct nuclear and spindle definitions do not imply disjoint structures; the yeast
  example includes nuclear spindle microtubules.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
- Parent reviewed the full target, draft, claim-specific source packet, native input/source
  hashes and selected supporting source sections. Independent source collaborators
  checked remaining cited sections and source attribution. Parent accepts the bounded
  assessments before persistence.
```
