# Sinister fiber identity, localization and in-vitro assembly evidence review

- Review: 20261021T082245Z-sinister-fiber-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:09:07Z
- Finished UTC: 2026-10-21T08:22:45Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The sf-fiber identity, BAp95 example, native localization, strain bridge, link-only image and experimental assembly graph are supported. No concrete curation defect was established.

## Scope And Provenance

Entire target; native ontology/taxon/protein/strain authorities; full primary scientific body and visual inspection of Figures5,7,8.

Selection: Fifth unreviewed path in batch eleven, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:sinister_fiber | data/structures/cytoskeleton/sinister_fiber.yaml | maintained | sinister fiber |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:sinister_fiber | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:sinister_fiber | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:sinister_fiber | 6 identifiers OK; 1 transport/skipped residuals independently resolved. |
| Native UniProt causal-graphs | passed | True | cellstructuremech:sinister_fiber | Native read-only target check passed. |
| Native UniProt verify | passed | True | cellstructuremech:sinister_fiber | Native read-only target check passed. |
| Expression-module applicability | not_applicable | False | cellstructuremech:sinister_fiber | The target asserts a physical assembly and its bounded function, without an expression-module mechanism. |
| Claim-level scientific review | passed | True | cellstructuremech:sinister_fiber | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:sinister_fiber | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:sinister_fiber | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:sinister_fiber | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:sinister_fiber | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:sinister_fiber | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Native linker and adjacent assemblies

identity: supported. Targets: cellstructuremech:sinister_fiber.

The local identity, exact sf-fiber synonym and narrow1sf/2sf names agree with the primary description. Centrin fibers, SF-assemblin fibers, proximal plates, basal bodies and root microtubules are separate assemblies. Broad parent and cytoskeletal parthood are appropriate.

### Cloned antigen and native constituent

grounding: supported. Targets: cellstructuremech:sinister_fiber.

The specific anti-rec95 localization supports BAp95 membership, distinct from the two-band anti-p95 preparation. The834residue clone/accession bridge is correct. Native essentiality, complete inventory and stoichiometry are not established or claimed.

### Bounded family search and coiled-coil predictions

grounding: supported. Targets: cellstructuremech:sinister_fiber.

The current accession and three phrase searches returned204. Retaining a reviewed label-only family is justified within this search scope; predicted coiled-coil domains and weak general sequence similarities do not establish exact family identity.

### Species and culture-collection bridge

scope: supported. Targets: cellstructuremech:sinister_fiber.

Native taxonomy and SAG support the species and historical strain correspondence. Chlamydomonas antibody dots and negative cross-reactivity in other organisms are not used to infer exact sf-fiber identity or biological absence.

### Observed linkage versus proposed physiology

evidence: supported. Targets: cellstructuremech:sinister_fiber.

Native attachments and persistent1sf association after disintegration support the structural linkage function. Phototaxis, spindle positioning and cleavage placement remain proposals rather than direct perturbation-supported target functions.

### Two-edge experimental assembly graph

representation: supported. Targets: cellstructuremech:sinister_fiber.

Both edges are confined to purified recombinant protein and stepwise urea removal. Approximate98nm periodicity belongs to that assay. Concentration/tubing-dependent aggregates and proposed intermediates are excluded from native biogenesis claims.

### Native image, attribution and controls

provenance: supported. Targets: cellstructuremech:sinister_fiber.

The link-only image, nine-panel caption,200nm scale, species, article attribution and CC BY-NC-SA4.0 licence agree. The private fetched image is unmodified; no image is added to the repository.

### Explicit unresolved boundaries

completeness: supported. Targets: cellstructuremech:sinister_fiber.

Open native assembly, essentiality, remaining inventory, direct functional perturbation and broader organism scope are warranted limits. None is silently replaced with a stronger biological claim. Historical repository/ontology searches are recorded as history, not rerun exhaustive absence findings.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| sinister-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0043232,GO:0120103; All three native active definitions and synonym scopes | supports | GO0043232 is the broad intracellular membraneless-organelle class and GO0005856 the cytoskeleton. GO0120103 specifies the mother-centriolar subdistal appendage, not both age-associated algal sf-fibers. |
| sinister-prep-tax-3192 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3192; taxId, scientificName, rank | supports | Taxon3192 is Spermatozopsis similis at species rank. |
| sinister-prep-O49944 | https://rest.uniprot.org/uniprotkb/O49944.json; Primary accession, entryType, organism, submitted protein name, gene absence, sequence length and EMBL crossreference | supports | Primary O49944 is unreviewed, names the 95kD basal apparatus protein in taxon3192, encodes834residues, has no gene-name tokens and links EMBL AJ001438/CAA04763.1. |
| sinister-prep-strain | https://sagdb.uni-goettingen.de/detailedList.php?str_number=1.85; Strain heading, taxonomy and complete sequence-information list | supports | SAG1.85 names S.similis and links AJ001438. Other sequence entries on that same strain page preserve SAG B1.85; this is a strain-name bridge, not a claim that the BAp95 sequence label itself includes the historical designation. |
| sinister-prep-geimer-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1083/jcb.140.5.1149; Single DOI result identity | supports | DOI10.1083/jcb.140.5.1149 resolves to the1998 primary paper and PMID9490727/PMC2132688. |
| sinister-prep-geimer-s3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/PMC2132688.1.xml; Entire Introduction, Methods, Results, Discussion; Fig2 accession AJ001438 and Figs5/7/8/9 captions; licence statement | supports | Native version1 JATS MD5 matches the record. Immunogold localizes the cloned antigen to1sf/2sf; recombinant reassembly is a separate assay. Native topology and proposed wider functions are distinguished. |
| sinister-prep-figure7 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f7.jpg; Native version1 Figure7 a-i; 200nm source scale; raw image unchanged | supports | All nine panels were visually inspected. Anti-rec95 and preimmune controls have the recorded panel assignment; the open arrow in a indicates a separate distal connecting fiber. Image MD5 matches the record. |
| sinister-prep-figure5 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f5.jpg; Native Figure5 a-g and caption, read with Methods and Results | supports | Visual inspection separates floating-membrane reassembly panelsa-e from the dense spindle-shaped aggregate conditionsf-g. The image does not prove an ordered sequence through the proposed rod/ladder intermediates. |
| sinister-prep-figure8 | https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f8.jpg; Native Figure8 a-e and caption | supports | Visual inspection supports distinct native attachment geometry:1sf on the older body,2sf proximal on the younger body, and retained1sf following mechanical disintegration. |
| interpro-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O49944/; Bounded native endpoint response; HTTP204 | context_only | No integrated entry returned by this exact accession/phrase query. This bounded result does not prove that no suitable family exists in any database. |
| interpro-family-search | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=BAp95; Bounded native endpoint response; HTTP204 | context_only | No integrated entry returned by this exact accession/phrase query. This bounded result does not prove that no suitable family exists in any database. |
| interpro-family-search-sinister | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=sinister%20fiber; Bounded native endpoint response; HTTP204 | context_only | No integrated entry returned by this exact accession/phrase query. This bounded result does not prove that no suitable family exists in any database. |
| interpro-family-search-basal | https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=basal%20apparatus%20protein; Bounded native endpoint response; HTTP204 | context_only | No integrated entry returned by this exact accession/phrase query. This bounded result does not prove that no suitable family exists in any database. |
| record | data/structures/cytoskeleton/sinister_fiber.yaml; Entire maintained YAML including both graph edges, image metadata and five discussions | context_only | The local identifier is an explicit corpus identity. BAp95 is a constituent with unknown native essentiality; the graph product is in-vitro fibers, deliberately not the native whole linker. No verbatim evidence snippets are stored. |
| schema-result | just validate data/structures/cytoskeleton/sinister_fiber.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/sinister_fiber.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/sinister_fiber.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../sinister_fiber-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/sinister_fiber.yaml --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../sinister_fiber-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../sinister_fiber-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/sinister_fiber.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 6 of 7 collected target identifiers returned OK at the unchanged base. Residuals: cellstructuremech:sinister_fiber: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| native-causal-graphs | /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sinister_fiber.yaml --causal-graphs; Entire captured native output | supports | data/structures/cytoskeleton/sinister_fiber.yaml  (cellstructuremech:sinister_fiber)<br>  bap95_in_vitro_fiber_assembly	recombinant_bap95	COVERED	-&gt;bap95_sf_fiber_proteins (UniProtKB:O49944)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/cytoskeleton/sinister_fiber.yaml --verify; Entire captured native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Native sf-fiber biogenesis, complete molecular inventory, stoichiometry and BAp95 essentiality remain unestablished. In-vitro reassembly does not establish native attachment sufficiency.
- Only the cited S.similis system is substantiated. Unshown cross-reactivity and negative antibody results do not establish exact structures or absence in other species.
- Four bounded InterPro endpoints returned204; no exhaustive absence claim across protein-family resources is made.
- The cited1998 body and relevant figures were read. Earlier ultrastructural papers cited inside it and raw experimental datasets were not independently audited.
- The current strain page has the historical B designation in other sequence entries and AJ001438 on the same record; this is not an identical historical text string on every accession.
- No stored verbatim snippet requires verification. The record historical search notes and earlier image-inspection event are not represented as fresh exhaustive search receipts.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Private source bytes were used for inspection only; the review adds no article or image copy.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T082245Z-sinister-fiber-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Sinister fiber identity, localization and in-vitro assembly evidence review
started_at: '2026-10-21T08:09:07Z'
finished_at: '2026-10-21T08:22:45Z'
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
summary: The sf-fiber identity, BAp95 example, native localization, strain bridge,
  link-only image and experimental assembly graph are supported. No concrete curation
  defect was established.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/cytoskeleton/sinister_fiber.yaml
    sha256: 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5
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
- target_id: cellstructuremech:sinister_fiber
  path: data/structures/cytoskeleton/sinister_fiber.yaml
  label: sinister fiber
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sinister_fiber.yaml
    role: maintained scientific record
scope:
  description: Entire target; native ontology/taxon/protein/strain authorities; full
    primary scientific body and visual inspection of Figures5,7,8.
  selection: Fifth unreviewed path in batch eleven, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:sinister_fiber
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just validate data/structures/cytoskeleton/sinister_fiber.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just validate-strict data/structures/cytoskeleton/sinister_fiber.yaml --out
    /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../sinister_fiber-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: 6 identifiers OK; 1 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - record
- check_id: native-causal-graphs
  name: Native UniProt causal-graphs
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/sinister_fiber.yaml
    --causal-graphs
  exit_code: 0
  summary: Native read-only target check passed.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native UniProt verify
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/sinister_fiber.yaml
    --verify
  exit_code: 0
  summary: Native read-only target check passed.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: The target asserts a physical assembly and its bounded function, without
    an expression-module mechanism.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - sinister-prep-go
  - sinister-prep-tax-3192
  - sinister-prep-O49944
  - sinister-prep-strain
  - sinister-prep-geimer-meta
  - sinister-prep-geimer-s3
  - sinister-prep-figure7
  - sinister-prep-figure5
  - sinister-prep-figure8
  - interpro-family
  - interpro-family-search
  - interpro-family-search-sinister
  - interpro-family-search-basal
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:sinister_fiber
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch11 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: sinister-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005856,GO:0043232,GO:0120103
  locator: All three native active definitions and synonym scopes
  accessed_at: '2026-10-21T08:13:09.835678Z'
  support: supports
  summary: GO0043232 is the broad intracellular membraneless-organelle class and GO0005856
    the cytoskeleton. GO0120103 specifies the mother-centriolar subdistal appendage,
    not both age-associated algal sf-fibers.
  snapshot_sha256: f31472cddab5dd37195121f9c780e76e466b7bade1da5116487beb7e51b629bd
- evidence_id: sinister-prep-tax-3192
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3192
  locator: taxId, scientificName, rank
  accessed_at: '2026-10-21T08:13:14.029409Z'
  support: supports
  summary: Taxon3192 is Spermatozopsis similis at species rank.
  snapshot_sha256: 05b70d411fc166a10f2823f9130f72b09e05c50d77bcbf846f78901d2adb23c7
- evidence_id: sinister-prep-O49944
  kind: database
  reference: https://rest.uniprot.org/uniprotkb/O49944.json
  locator: Primary accession, entryType, organism, submitted protein name, gene absence,
    sequence length and EMBL crossreference
  accessed_at: '2026-10-21T08:13:14.285937Z'
  support: supports
  summary: Primary O49944 is unreviewed, names the 95kD basal apparatus protein in
    taxon3192, encodes834residues, has no gene-name tokens and links EMBL AJ001438/CAA04763.1.
  snapshot_sha256: db6df16bdb9d2c0b88a960c7791bfbfd5e5ce4597ffa61ad825f1abb2a145554
- evidence_id: sinister-prep-strain
  kind: authority
  reference: https://sagdb.uni-goettingen.de/detailedList.php?str_number=1.85
  locator: Strain heading, taxonomy and complete sequence-information list
  accessed_at: '2026-10-21T08:13:16.219420Z'
  support: supports
  summary: SAG1.85 names S.similis and links AJ001438. Other sequence entries on that
    same strain page preserve SAG B1.85; this is a strain-name bridge, not a claim
    that the BAp95 sequence label itself includes the historical designation.
  snapshot_sha256: 917c9376c21f51f4c5f9fddd81df2456311452dfe38e4b89aab4df25d6c10cc8
- evidence_id: sinister-prep-geimer-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1083/jcb.140.5.1149
  locator: Single DOI result identity
  accessed_at: '2026-10-21T08:13:11.782411Z'
  support: supports
  summary: DOI10.1083/jcb.140.5.1149 resolves to the1998 primary paper and PMID9490727/PMC2132688.
  snapshot_sha256: 022732872e39901e6653f390126f77b031d97518ec5e931572371b6cdd3d6da8
- evidence_id: sinister-prep-geimer-s3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/PMC2132688.1.xml
  locator: Entire Introduction, Methods, Results, Discussion; Fig2 accession AJ001438
    and Figs5/7/8/9 captions; licence statement
  accessed_at: '2026-10-21T08:13:16.153778Z'
  support: supports
  summary: Native version1 JATS MD5 matches the record. Immunogold localizes the cloned
    antigen to1sf/2sf; recombinant reassembly is a separate assay. Native topology
    and proposed wider functions are distinguished.
  snapshot_sha256: 08fbbc9f099d1f64182b5dcb8cb683299836f01dc2300a093c290ed0156bcf41
- evidence_id: sinister-prep-figure7
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f7.jpg
  locator: Native version1 Figure7 a-i; 200nm source scale; raw image unchanged
  accessed_at: '2026-10-21T08:13:16.164735Z'
  support: supports
  summary: All nine panels were visually inspected. Anti-rec95 and preimmune controls
    have the recorded panel assignment; the open arrow in a indicates a separate distal
    connecting fiber. Image MD5 matches the record.
  snapshot_sha256: 363e493a65cb47436d260ffdeb373dd9f8ed7b77e4d3c4e48e16c773e338bd8a
- evidence_id: sinister-prep-figure5
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f5.jpg
  locator: Native Figure5 a-g and caption, read with Methods and Results
  accessed_at: '2026-10-21T08:15:59.948132Z'
  support: supports
  summary: Visual inspection separates floating-membrane reassembly panelsa-e from
    the dense spindle-shaped aggregate conditionsf-g. The image does not prove an
    ordered sequence through the proposed rod/ladder intermediates.
  snapshot_sha256: 1317f6975ea6f44f192719fcfae14f692b1caa24c902389bc369f7815284a640
- evidence_id: sinister-prep-figure8
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC2132688.1/JCB15053.f8.jpg
  locator: Native Figure8 a-e and caption
  accessed_at: '2026-10-21T08:16:00.061548Z'
  support: supports
  summary: Visual inspection supports distinct native attachment geometry:1sf on the
    older body,2sf proximal on the younger body, and retained1sf following mechanical
    disintegration.
  snapshot_sha256: 619df5c2da94e208089aa551df462aeae46dca28e8bc30c63217348d551d17b3
- evidence_id: interpro-family
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/O49944/
  locator: Bounded native endpoint response; HTTP204
  accessed_at: '2026-10-21T08:13:16.104033Z'
  support: context_only
  summary: No integrated entry returned by this exact accession/phrase query. This
    bounded result does not prove that no suitable family exists in any database.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: interpro-family-search
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=BAp95
  locator: Bounded native endpoint response; HTTP204
  accessed_at: '2026-10-21T08:13:16.504275Z'
  support: context_only
  summary: No integrated entry returned by this exact accession/phrase query. This
    bounded result does not prove that no suitable family exists in any database.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: interpro-family-search-sinister
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=sinister%20fiber
  locator: Bounded native endpoint response; HTTP204
  accessed_at: '2026-10-21T08:16:00.520959Z'
  support: context_only
  summary: No integrated entry returned by this exact accession/phrase query. This
    bounded result does not prove that no suitable family exists in any database.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: interpro-family-search-basal
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/?search=basal%20apparatus%20protein
  locator: Bounded native endpoint response; HTTP204
  accessed_at: '2026-10-21T08:16:00.501806Z'
  support: context_only
  summary: No integrated entry returned by this exact accession/phrase query. This
    bounded result does not prove that no suitable family exists in any database.
  snapshot_sha256: e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/sinister_fiber.yaml
  locator: Entire maintained YAML including both graph edges, image metadata and five
    discussions
  accessed_at: '2026-10-21T08:18:34Z'
  support: context_only
  summary: The local identifier is an explicit corpus identity. BAp95 is a constituent
    with unknown native essentiality; the graph product is in-vitro fibers, deliberately
    not the native whole linker. No verbatim evidence snippets are stored.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/sinister_fiber.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:09:11Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/sinister_fiber.yaml'
  snapshot_sha256: 6b26eb872083212300681a9ff50e65fb26bb9505f452cf2fc04561e06c1cd7b3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/sinister_fiber.yaml
    --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../sinister_fiber-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:09:15Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/sinister_fiber.yaml\
    \ --out /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../sinister_fiber-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/../sinister_fiber-strict.tsv"
  snapshot_sha256: c5307337be41a77f5bc408d1546326051351674afbfe5c8d77ba16327a18bd9b
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/sinister_fiber.yaml; exact collect() scope;
    hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:18:34Z'
  support: supports
  summary: '6 of 7 collected target identifiers returned OK at the unchanged base.
    Residuals: cellstructuremech:sinister_fiber: SKIPPED; resolved by evidence record.
    Source-native identity checked separately.'
  snapshot_sha256: 68d64e4e86437df228658f43be4d47b41054fe882fedf357e660293691a0a061
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/sinister_fiber.yaml
    --causal-graphs
  locator: Entire captured native output
  accessed_at: '2026-10-21T08:17:00.279881Z'
  support: supports
  summary: "data/structures/cytoskeleton/sinister_fiber.yaml  (cellstructuremech:sinister_fiber)\n\
    \  bap95_in_vitro_fiber_assembly\trecombinant_bap95\tCOVERED\t->bap95_sf_fiber_proteins\
    \ (UniProtKB:O49944)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n     1  COVERED\
    \                   component_ref target holds protein_examples covering all declared\
    \ symbols\n     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     1\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: a9342700e4abf3eb781ed81d9bfdbdbb7cf200c82b0e82e0433b58d16116fc41
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch11-20261021-bn_6pbpb/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/cytoskeleton/sinister_fiber.yaml
    --verify
  locator: Entire captured native output
  accessed_at: '2026-10-21T08:17:02.917393Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
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
  topic: Native linker and adjacent assemblies
  outcome: supported
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: The local identity, exact sf-fiber synonym and narrow1sf/2sf names agree
    with the primary description. Centrin fibers, SF-assemblin fibers, proximal plates,
    basal bodies and root microtubules are separate assemblies. Broad parent and cytoskeletal
    parthood are appropriate.
  evidence_ids:
  - sinister-prep-go
  - sinister-prep-geimer-s3
  - sinister-prep-figure8
  - record
- assessment_id: protein
  area: grounding
  topic: Cloned antigen and native constituent
  outcome: supported
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: The specific anti-rec95 localization supports BAp95 membership, distinct
    from the two-band anti-p95 preparation. The834residue clone/accession bridge is
    correct. Native essentiality, complete inventory and stoichiometry are not established
    or claimed.
  evidence_ids:
  - sinister-prep-O49944
  - sinister-prep-geimer-s3
  - sinister-prep-figure7
  - record
- assessment_id: family
  area: grounding
  topic: Bounded family search and coiled-coil predictions
  outcome: supported
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: The current accession and three phrase searches returned204. Retaining
    a reviewed label-only family is justified within this search scope; predicted
    coiled-coil domains and weak general sequence similarities do not establish exact
    family identity.
  evidence_ids:
  - interpro-family
  - interpro-family-search
  - interpro-family-search-sinister
  - interpro-family-search-basal
  - sinister-prep-geimer-s3
  - record
- assessment_id: taxon
  area: scope
  topic: Species and culture-collection bridge
  outcome: supported
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: Native taxonomy and SAG support the species and historical strain correspondence.
    Chlamydomonas antibody dots and negative cross-reactivity in other organisms are
    not used to infer exact sf-fiber identity or biological absence.
  evidence_ids:
  - sinister-prep-tax-3192
  - sinister-prep-strain
  - sinister-prep-geimer-s3
  - record
- assessment_id: function
  area: evidence
  topic: Observed linkage versus proposed physiology
  outcome: supported
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: Native attachments and persistent1sf association after disintegration support
    the structural linkage function. Phototaxis, spindle positioning and cleavage
    placement remain proposals rather than direct perturbation-supported target functions.
  evidence_ids:
  - sinister-prep-geimer-s3
  - sinister-prep-figure8
  - record
- assessment_id: mechanism
  area: representation
  topic: Two-edge experimental assembly graph
  outcome: supported
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: Both edges are confined to purified recombinant protein and stepwise urea
    removal. Approximate98nm periodicity belongs to that assay. Concentration/tubing-dependent
    aggregates and proposed intermediates are excluded from native biogenesis claims.
  evidence_ids:
  - sinister-prep-geimer-s3
  - sinister-prep-figure5
  - record
- assessment_id: image
  area: provenance
  topic: Native image, attribution and controls
  outcome: supported
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: The link-only image, nine-panel caption,200nm scale, species, article attribution
    and CC BY-NC-SA4.0 licence agree. The private fetched image is unmodified; no
    image is added to the repository.
  evidence_ids:
  - sinister-prep-geimer-s3
  - sinister-prep-figure7
  - record
- assessment_id: completeness
  area: completeness
  topic: Explicit unresolved boundaries
  outcome: supported
  target_ids:
  - cellstructuremech:sinister_fiber
  summary: Open native assembly, essentiality, remaining inventory, direct functional
    perturbation and broader organism scope are warranted limits. None is silently
    replaced with a stronger biological claim. Historical repository/ontology searches
    are recorded as history, not rerun exhaustive absence findings.
  evidence_ids:
  - sinister-prep-geimer-s3
  - sinister-prep-go
  - sinister-prep-O49944
  - record
findings: []
actions: []
limitations:
- Native sf-fiber biogenesis, complete molecular inventory, stoichiometry and BAp95
  essentiality remain unestablished. In-vitro reassembly does not establish native
  attachment sufficiency.
- Only the cited S.similis system is substantiated. Unshown cross-reactivity and negative
  antibody results do not establish exact structures or absence in other species.
- Four bounded InterPro endpoints returned204; no exhaustive absence claim across
  protein-family resources is made.
- The cited1998 body and relevant figures were read. Earlier ultrastructural papers
  cited inside it and raw experimental datasets were not independently audited.
- The current strain page has the historical B designation in other sequence entries
  and AJ001438 on the same record; this is not an identical historical text string
  on every accession.
- No stored verbatim snippet requires verification. The record historical search notes
  and earlier image-inspection event are not represented as fresh exhaustive search
  receipts.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Private source bytes were used for inspection only; the review adds no article or
  image copy.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
