# C2 axonemal microtubule identity and projection-scaffold review

- Review: 20261020T072458Z-c2-axonemal-microtubule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T07:24:02Z
- Finished UTC: 2026-10-20T07:24:58Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

C2 identity, hierarchy, Chlamydomonas scope, five projection attachments, two density-defined inner proteins and four nonmechanistic graph edges are supported. No concrete defect was found.

## Scope And Provenance

Entire maintained record; native GO/taxon entries and the2013 study’s relevant Results, Discussion and sample/processing Methods.

Selection: First remaining unreviewed path after four validated ten-record batches; fresh main at the identical base revision.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990720 | data/structures/cytoskeleton/c2_axonemal_microtubule.yaml | maintained | C2 axonemal microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990720 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990720 | Focused validator passed. |
| Target resolver slice | passed | True | GO:1990720 | 7 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:1990720 | No matched microbial expression dataset or expression-derived component mechanism is asserted. Primary structural and ontology evidence establish the reviewed relationships. |
| Claim-level scientific review | passed | True | GO:1990720 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:1990720 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990720 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990720 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990720 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:1990720 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact C2 singlet identity

identity: supported. Targets: GO:1990720.

Name, definition, filament kind and broad synonym match native GO and the primary source. C2 remains distinct from C1 and the complete central pair.

### Native is-a and part_of

grounding: supported. Targets: GO:1990720.

The axonemal microtubule parent and central-pair parthood match explicit native relations.

### Observed wild-type central-pair architecture

scope: supported. Targets: GO:1990720.

The Chlamydomonas example is directly supported across the selected strains. COMMON is a qualitative ordinary-architecture assertion, not a prevalence estimate or universal mutant/life-stage claim.

### Five projection attachments

evidence: supported. Targets: GO:1990720.

C2a-e, including the newly named2d/e densities, are explicit in the source. The broad scaffold role does not imply a tested signaling or force mechanism.

### Four spatial edges

graph: supported. Targets: GO:1990720.

C2 parthood, projection attachment and bridge contacts to C1/C2 are supported. NONMECHANISTIC correctly describes the graph’s level of explanation.

### Density labels without sequence assignment

evidence: supported. Targets: GO:1990720.

The two C2 MIPs are directly resolved in Chlamydomonas and remain density-defined in the cited source. Their mention in the open discussion does not claim named protein membership or cross-species conservation.

### Explicitly deferred molecular census

completeness: supported. Targets: GO:1990720.

The record names the unresolved wall/projection/MIP boundaries rather than implying complete composition. Optional molecular fields are not populated with unsupported identities.

### Ontology wording and reconstructed network

provenance: supported. Targets: GO:1990720.

The two-bridges note matches GO, while the paper resolves a more complex network; graph edges assert only connection. The parent GO definition currently says doublets, but this target correctly describes a singlet.

### Proposed broad record

completeness: supported. Targets: GO:1990720.

PROPOSED and the actionable molecular-boundary discussion agree with the limited curation. No concrete maintained-record defect was found.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| c1-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990719,GO:1990720,GO:1990717,GO:0005879,GO:0097540; Five native definitions, synonyms, aspects and child relations | supports | GO1990720 is active and names the exact C2 microtubule, with broad synonym C2 tubule. The axonemal-microtubule parent lists C2 as is_a, and central pair lists it as part_of. C1 and bridge identities match graph nodes. |
| bridge-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC3914236.1/PMC3914236.1.xml; C2 projection and C2 MIP Results, C1/C2 contact Results, bridge Discussion, sample and processing Methods | supports | C2 Results explicitly identify projections2a-e and distinguish their algal/sea-urchin morphology. The Chlamydomonas C2 lumen contains two density-defined MIPs called MIP-C2a/b; no sequence identity follows. Contact Results resolve the C1/C2 bridge network. Methods describe twelve axonemes from five strains with wild-type CPC and distinguish global from C2-focused alignment. |
| bridge-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1002/cm.21094&amp;format=json&amp;resultType=core; Exact bibliographic identity | supports | The DOI matches Carbajal-Gonzalez etal2013, Conserved structural motifs in the central pair complex of eukaryotic flagella. |
| sheath-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; Native taxonomy | supports | NCBITaxon3055 identifies Chlamydomonas reinhardtii. |
| record | data/structures/cytoskeleton/c2_axonemal_microtubule.yaml; Entire target, one function, five nodes/four edges and open composition discussion | context_only | The record preserves a broad C2 scaffold identity and labels its spatial graph NONMECHANISTIC. Wall constituents, projection boundaries, inner-protein identities and copy numbers remain explicitly deferred. |
| identity-search | data/structures/cytoskeleton/c2_axonemal_microtubule.yaml; Exact GO1990720 identifier search across data/structures including hidden and ignored files | context_only | Only the target declares this exact C2 identity. |
| schema-result | just validate data/structures/cytoskeleton/c2_axonemal_microtubule.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/c2_axonemal_microtubule.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/c2_axonemal_microtubule.yaml --out /private/tmp/cellstructure-batch5-20261020-aEelh1/c2_axonemal_microtubule-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/c2_axonemal_microtubule.yaml --out /private/tmp/cellstructure-batch5-20261020-aEelh1/c2_axonemal_microtubule-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch5-20261020-aEelh1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch5-20261020-aEelh1/c2_axonemal_microtubule-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/c2_axonemal_microtubule.yaml; exact collect() scope | supports | 7 of7 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Exact wall constituents, inner-protein identities, projection subcomplex boundaries and copy numbers remain uncurated.
- COMMON is not a prevalence measurement; reconstructed samples were selected for preserved central pairs.
- The native parent definition’s doublet wording is not adopted as morphology; primary data support singlet C2.
- Map volumes were not reprocessed and no newer molecular census was substituted for the stated record scope.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T072458Z-c2-axonemal-microtubule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: C2 axonemal microtubule identity and projection-scaffold review
started_at: '2026-10-20T07:24:02Z'
finished_at: '2026-10-20T07:24:58Z'
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
summary: C2 identity, hierarchy, Chlamydomonas scope, five projection attachments,
  two density-defined inner proteins and four nonmechanistic graph edges are supported.
  No concrete defect was found.
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
  - path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    sha256: 97c8666ddef318d146a2d902a225f8b0313468bcf54fa32d81d5f1d127798a44
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
- target_id: GO:1990720
  path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
  label: C2 axonemal microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    role: maintained scientific record
scope:
  description: Entire maintained record; native GO/taxon entries and the2013 study’s
    relevant Results, Discussion and sample/processing Methods.
  selection: First remaining unreviewed path after four validated ten-record batches;
    fresh main at the identical base revision.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990720
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990720
  command: just validate data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990720
  command: just validate-strict data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    --out /private/tmp/cellstructure-batch5-20261020-aEelh1/c2_axonemal_microtubule-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:1990720
  summary: 7 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990720
  summary: No matched microbial expression dataset or expression-derived component
    mechanism is asserted. Primary structural and ontology evidence establish the
    reviewed relationships.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990720
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - c1-go
  - bridge-paper
  - bridge-epmc
  - sheath-taxon
  - record
  - identity-search
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990720
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990720
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990720
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990720
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990720
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch3 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: c1-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990719,GO:1990720,GO:1990717,GO:0005879,GO:0097540
  locator: Five native definitions, synonyms, aspects and child relations
  accessed_at: '2026-10-20T07:17:58.776411Z'
  support: supports
  summary: GO1990720 is active and names the exact C2 microtubule, with broad synonym
    C2 tubule. The axonemal-microtubule parent lists C2 as is_a, and central pair
    lists it as part_of. C1 and bridge identities match graph nodes.
  snapshot_sha256: 0a3db616cf68ce6e2ac31888f639cbb1212fc889dbe354aa07916503058c3869
- evidence_id: bridge-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3914236.1/PMC3914236.1.xml
  locator: C2 projection and C2 MIP Results, C1/C2 contact Results, bridge Discussion,
    sample and processing Methods
  accessed_at: '2026-10-20T03:42:14.888078Z'
  support: supports
  summary: C2 Results explicitly identify projections2a-e and distinguish their algal/sea-urchin
    morphology. The Chlamydomonas C2 lumen contains two density-defined MIPs called
    MIP-C2a/b; no sequence identity follows. Contact Results resolve the C1/C2 bridge
    network. Methods describe twelve axonemes from five strains with wild-type CPC
    and distinguish global from C2-focused alignment.
  snapshot_sha256: 8ea6c2f20d7cecc7a071669f91afd2d6b2d2aa8681eefb5b001ef22c6b82a7d0
- evidence_id: bridge-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1002/cm.21094&format=json&resultType=core
  locator: Exact bibliographic identity
  accessed_at: '2026-10-20T03:41:58.165073Z'
  support: supports
  summary: The DOI matches Carbajal-Gonzalez etal2013, Conserved structural motifs
    in the central pair complex of eukaryotic flagella.
  snapshot_sha256: 99899baa950adcfa150e85483fd760d4addfbe5ff43e56e0aa5eb30f428dafd1
- evidence_id: sheath-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: Native taxonomy
  accessed_at: '2026-10-20T03:38:20.199537Z'
  support: supports
  summary: NCBITaxon3055 identifies Chlamydomonas reinhardtii.
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
  locator: Entire target, one function, five nodes/four edges and open composition
    discussion
  accessed_at: '2026-10-20T07:24:58Z'
  support: context_only
  summary: The record preserves a broad C2 scaffold identity and labels its spatial
    graph NONMECHANISTIC. Wall constituents, projection boundaries, inner-protein
    identities and copy numbers remain explicitly deferred.
- evidence_id: identity-search
  kind: record_content
  reference: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
  locator: Exact GO1990720 identifier search across data/structures including hidden
    and ignored files
  accessed_at: '2026-10-20T07:24:58Z'
  support: context_only
  summary: Only the target declares this exact C2 identity.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T07:24:04Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/c2_axonemal_microtubule.yaml'
  snapshot_sha256: 193f892aa2644530cd0c72304d283d47a5af782da0ea074f4328e45a49a13a39
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    --out /private/tmp/cellstructure-batch5-20261020-aEelh1/c2_axonemal_microtubule-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T07:24:05Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/c2_axonemal_microtubule.yaml\
    \ --out /private/tmp/cellstructure-batch5-20261020-aEelh1/c2_axonemal_microtubule-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch5-20261020-aEelh1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch5-20261020-aEelh1/c2_axonemal_microtubule-strict.tsv"
  snapshot_sha256: d8e2e4186fcb5d6ec6059880f62b5eeac09c785d2e9737b52ed3907d6a7a7728
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml; exact collect()
    scope
  accessed_at: '2026-10-20T07:24:58Z'
  support: supports
  summary: '7 of7 collected target identifiers returned OK at the unchanged base.
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
  topic: Exact C2 singlet identity
  outcome: supported
  target_ids:
  - GO:1990720
  summary: Name, definition, filament kind and broad synonym match native GO and the
    primary source. C2 remains distinct from C1 and the complete central pair.
  evidence_ids:
  - c1-go
  - bridge-paper
  - record
- assessment_id: hierarchy
  area: grounding
  topic: Native is-a and part_of
  outcome: supported
  target_ids:
  - GO:1990720
  summary: The axonemal microtubule parent and central-pair parthood match explicit
    native relations.
  evidence_ids:
  - c1-go
  - record
- assessment_id: taxa
  area: scope
  topic: Observed wild-type central-pair architecture
  outcome: supported
  target_ids:
  - GO:1990720
  summary: The Chlamydomonas example is directly supported across the selected strains.
    COMMON is a qualitative ordinary-architecture assertion, not a prevalence estimate
    or universal mutant/life-stage claim.
  evidence_ids:
  - bridge-paper
  - sheath-taxon
  - record
- assessment_id: function
  area: evidence
  topic: Five projection attachments
  outcome: supported
  target_ids:
  - GO:1990720
  summary: C2a-e, including the newly named2d/e densities, are explicit in the source.
    The broad scaffold role does not imply a tested signaling or force mechanism.
  evidence_ids:
  - bridge-paper
  - c1-go
  - record
- assessment_id: graph
  area: graph
  topic: Four spatial edges
  outcome: supported
  target_ids:
  - GO:1990720
  summary: C2 parthood, projection attachment and bridge contacts to C1/C2 are supported.
    NONMECHANISTIC correctly describes the graph’s level of explanation.
  evidence_ids:
  - c1-go
  - bridge-paper
  - record
- assessment_id: inner-proteins
  area: evidence
  topic: Density labels without sequence assignment
  outcome: supported
  target_ids:
  - GO:1990720
  summary: The two C2 MIPs are directly resolved in Chlamydomonas and remain density-defined
    in the cited source. Their mention in the open discussion does not claim named
    protein membership or cross-species conservation.
  evidence_ids:
  - bridge-paper
  - record
- assessment_id: composition
  area: completeness
  topic: Explicitly deferred molecular census
  outcome: supported
  target_ids:
  - GO:1990720
  summary: The record names the unresolved wall/projection/MIP boundaries rather than
    implying complete composition. Optional molecular fields are not populated with
    unsupported identities.
  evidence_ids:
  - bridge-paper
  - record
- assessment_id: source-boundaries
  area: provenance
  topic: Ontology wording and reconstructed network
  outcome: supported
  target_ids:
  - GO:1990720
  summary: The two-bridges note matches GO, while the paper resolves a more complex
    network; graph edges assert only connection. The parent GO definition currently
    says doublets, but this target correctly describes a singlet.
  evidence_ids:
  - c1-go
  - bridge-paper
  - record
- assessment_id: status
  area: completeness
  topic: Proposed broad record
  outcome: supported
  target_ids:
  - GO:1990720
  summary: PROPOSED and the actionable molecular-boundary discussion agree with the
    limited curation. No concrete maintained-record defect was found.
  evidence_ids:
  - c1-go
  - bridge-paper
  - record
findings: []
actions: []
limitations:
- Exact wall constituents, inner-protein identities, projection subcomplex boundaries
  and copy numbers remain uncurated.
- COMMON is not a prevalence measurement; reconstructed samples were selected for
  preserved central pairs.
- The native parent definition’s doublet wording is not adopted as morphology; primary
  data support singlet C2.
- Map volumes were not reprocessed and no newer molecular census was substituted for
  the stated record scope.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
