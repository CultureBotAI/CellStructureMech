# Gin4 complex identity, composition and mitotic assembly review

- Review: 20261021T070914Z-gin4-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:06:19Z
- Finished UTC: 2026-10-21T07:09:14Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact Gin4-complex identity, named composition, minimum Gin4 multiplicity and nonmechanistic mitotic assembly relations are supported by native authorities and the source study. No concrete curation defect was established.

## Scope And Provenance

Entire target, native GO/OLS/taxon identities, primary Methods/Results/Table1/Figure2 captions/Discussion and scoped complex/protein/family cross-checks.

Selection: First unreviewed path in batch seven, following the nine distinct paths reviewed in batch six; one record per bundle in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990317 | data/structures/cytoskeleton/gin4_complex.yaml | maintained | Gin4 complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:1990317 | Focused validator passed. |
| Focused native strict | passed | True | GO:1990317 | Focused validator passed. |
| Target resolver slice | passed | True | GO:1990317 | 5 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:1990317 | Named proteins are used for physical-complex identity and composition, with no expression-module or transcription-regulatory assertion. Native complex/protein records and purification experiments address those claims. |
| Claim-level scientific review | passed | True | GO:1990317 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:1990317 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:1990317 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:1990317 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:1990317 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:1990317 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Named kinase complex rather than ring or process

identity: supported. Targets: GO:1990317.

Exact GO identity, kinase-complex parent, ring parthood and process participation are supported by native QuickGO definitions and child relations. OLS independently confirms term identity and source. The target distinguishes a multiprotein assembly from the containing septin ring and the biological process.

### Eight identities and minimum Gin4 multiplicity

evidence: supported. Targets: GO:1990317.

Primary Results/Table1 support the named proteins; tagged coimmunoprecipitation supports at least two Gin4 molecules. Eight identities do not imply an eight-molecule complex, and no exact stoichiometry or direct Gin4-Gin4 contact is asserted.

### Species record with strain-specific source contexts

scope: supported. Targets: GO:1990317.

The species example is supported. Primary W303 experiments and native S288C database participants are kept separate. COMMON is qualitative occurrence in the model organism, not a measured cross-strain prevalence.

### Mitotic participation without recruitment sequence

graph: supported. Targets: GO:1990317.

Both graph edges are ontology-backed and consistent with cell-cycle-dependent experimental association. The record does not specify molecular order, treat regulatory dependencies as constituents or conflate persistent Gin4-Nap1 binding with full mitotic complex assembly.

### Accurate prose composition and acknowledged structured curation

completeness: supported. Targets: GO:1990317.

The component-grounding TODO is honest and no incorrect accession is asserted. Native sources make structured septin/NAP and taxon-paired complex composition enrichment feasible, but the record already accurately states the supported composition; an empty optional collection alone is not a defect. Exact full Bni5/Gin4 family mapping remains unresolved.

### Source behind ontology definition

provenance: supported. Targets: GO:1990317.

The native GO source is traceable to the inspected primary paper. Relevant body passages and figure captions were read rather than inferring experimental details from a title or metadata alone.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| gin4-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990317,GO:1902554,GO:0000144,GO:0000921; Native GO:1990317, GO:1902554, GO:0000144 and GO:0000921 definitions and child relations | supports | Exact active Gin4-complex definition names the eight proteins and at least two Gin4 molecules. The kinase-complex parent, bud-neck septin-ring parthood and septin-ring-assembly process participation match the record. |
| gin4-agent-ols | https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_1990317; OLS GO:1990317 native term record | supports | OLS confirms the exact Gin4 complex identity, definition and source PMID, and exposes traversal links for parthood and process-participation relations. This captured payload does not resolve their target IDs; those exact edges are established by the separately inspected native QuickGO child relations. |
| gin4-agent-taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; ENA scientificName, taxId and rank | supports | Native ENA taxonomy confirms Saccharomyces cerevisiae4932 at species rank. |
| gin4-agent-crossref-paper | https://api.crossref.org/works/10.1091/mbc.01-10-0500; Crossref title, authors and publication date | supports | DOI10.1091/mbc.01-10-0500 resolves to Mortensen, McDonald, Yates and Kellogg2002, Cell Cycle-dependent Assembly of a Gin4-Septin Complex. |
| gin4-agent-epmc-paper | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12058072%20AND%20SRC:MED&amp;format=json&amp;resultType=core; Europe PMC exact primary record and abstract | supports | Native PMID12058072/PMC117627 record and complete abstract agree on the Gin4 complex and provide the primary identity behind the GO definition. |
| gin4-browser-primary-body | https://pmc.ncbi.nlm.nih.gov/articles/PMC117627/; Methods: Strains and Culture Conditions; Results: Gin4 Is Found in a Complex with Itself during Mitosis; Figure 2; Results: Purification of Endogenous Gin4 Complexes by Immunoaffinity Chromatography; Table 1; Results: Assembly of the Gin4 Complex Occurs as Cells Enter Mitosis; Figure 4; saved tool-rendered primary-body passages, not publisher HTML or image pixels | supports | Methods place experiments in W303. Results/Table1 identify Gin4 and Cdc3/10/11/12, Shs1 (SEP7), Nap1 and Bni5 in specific immunoaffinity-purified complexes. Distinct tagged Gin4 copies coimmunoprecipitate in mitosis, supporting at least two molecules without an exact copy count or direct-contact proof. Results/Figure4 distinguish mitotic septin association from persistent Nap1 association. |
| gin4-browser-primary-discussion | https://pmc.ncbi.nlm.nih.gov/articles/PMC117627/; Discussion: Gin4 Assembles into a Multiprotein Complex as Cells Enter Mitosis; Table 2; Discussion: Mechanisms Leading to the Activation of Gin4 during Mitosis; saved tool-rendered primary-body passages, not publisher HTML or image pixels | supports | Discussion supports mitotic multiprotein assembly while leaving direct Gin4 self-contact, detailed recruitment/activation order and additional weak copurifying candidates unresolved. Regulatory dependencies are not automatically stable constituents. |
| gin4-agent-complex-portal | https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1712; Native complex name, systematicName, GO cross-reference, organism, participants and properties | supports | CPX-1712 independently identifies the Gin4 serine/threonine kinase complex, exact GO cross-reference and eight participants. Taxon is S288C; participant stoichiometries are null while prose states at least two Gin4. This corroborates identities without imposing database strain context on W303 experiments. |
| gin4-agent-uniprot | https://rest.uniprot.org/uniprotkb/search?query=organism_id:559292%20AND%20reviewed:true%20AND%20(gene_exact:BNI5%20OR%20gene_exact:CDC3%20OR%20gene_exact:CDC10%20OR%20gene_exact:CDC11%20OR%20gene_exact:CDC12%20OR%20gene_exact:GIN4%20OR%20gene_exact:NAP1%20OR%20gene_exact:SHS1)&amp;format=json&amp;size=50; Exact reviewed S288C gene query: BNI5, CDC3, CDC10, CDC11, CDC12, GIN4, NAP1 and SHS1 | supports | Native reviewed S288C entries resolve all eight named proteins and their Gin4-complex subunit annotations. These are possible taxon-paired curation examples, not accessions already asserted by the target or a substitute for primary composition evidence. |
| gin4-agent-taxon-strain | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Native strain name/rank | supports | ENA confirms S288C559292 is a strain distinct from the W303 source context. |
| gin4-agent-interpro-septin | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/; Native InterPro name/type and description | supports | IPR016491 is the Septin family, an exact family-level candidate for the generic septin class; the inspected UniProt examples carry it. |
| gin4-agent-interpro-nap | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002164/; Native InterPro name/type and description | supports | IPR002164 is the Nucleosome assembly protein family, a family-level candidate for Nap1; the inspected Nap1 entry carries it. |
| gin4-agent-interpro-bni5 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063385/; Native InterPro name/type and description | supports | IPR063385 is a BNI5 helical domain. Its domain type does not establish an exact whole-protein Bni5 family mapping. |
| gin4-agent-interpro-kinase | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000719/; Native InterPro name/type and description | supports | IPR000719 is the Protein kinase domain. It is broader than Gin4 and does not establish an exact full-Gin4 family identity. |
| record | data/structures/cytoskeleton/gin4_complex.yaml; Entire maintained YAML | context_only | The record remains PROPOSED and preserves all eight identities plus the minimum Gin4 multiplicity in its definition. Structured component grounding is explicitly deferred. The graph is NONMECHANISTIC and asserts only parthood and process participation. |
| schema-result | just validate data/structures/cytoskeleton/gin4_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/gin4_complex.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/gin4_complex.yaml --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/gin4_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/gin4_complex.yaml --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/gin4_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch7-20261021-dz9x5cv0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/gin4_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/gin4_complex.yaml; exact collect() scope | supports | 5 of5 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Primary body passages were read through the PMC browser rendering. Direct publisher/API/PDF routes returned403,500,404,429 or challenge pages; those responses are not treated as source text. Figure panels were not visually inspected.
- At least two Gin4 molecules is a lower bound inferred from tagged coimmunoprecipitation, not exact stoichiometry or proof of direct self-contact. Database participant counts remain unspecified.
- Primary W303 experiments and curated S288C records are distinct strain contexts. No database accession or strain is silently imported into the scientific record.
- Structured component enrichment remains open; verified septin/NAP families do not establish exact full Bni5/Gin4 family mappings or every weak copurifying candidate.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Explicit user instruction requires saving every reviewed target, including clean observations; no issue was invented.
- A read-only collaborator inspected primary passages and native sources. Root read the complete unchanged target and assessed it after batch-seven native input inspection.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T070914Z-gin4-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Gin4 complex identity, composition and mitotic assembly review
started_at: '2026-10-21T07:06:19Z'
finished_at: '2026-10-21T07:09:14Z'
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
summary: Exact Gin4-complex identity, named composition, minimum Gin4 multiplicity
  and nonmechanistic mitotic assembly relations are supported by native authorities
  and the source study. No concrete curation defect was established.
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
  - path: data/structures/cytoskeleton/gin4_complex.yaml
    sha256: 92702fe584fd086c30d5fee9fe8aaee5d8ec0e8938606710a09e6c2954428f43
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
- target_id: GO:1990317
  path: data/structures/cytoskeleton/gin4_complex.yaml
  label: Gin4 complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gin4_complex.yaml
    role: maintained scientific record
scope:
  description: Entire target, native GO/OLS/taxon identities, primary Methods/Results/Table1/Figure2
    captions/Discussion and scoped complex/protein/family cross-checks.
  selection: First unreviewed path in batch seven, following the nine distinct paths
    reviewed in batch six; one record per bundle in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990317
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:1990317
  command: just validate data/structures/cytoskeleton/gin4_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:1990317
  command: just validate-strict data/structures/cytoskeleton/gin4_complex.yaml --out
    /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/gin4_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:1990317
  summary: 5 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:1990317
  summary: Named proteins are used for physical-complex identity and composition,
    with no expression-module or transcription-regulatory assertion. Native complex/protein
    records and purification experiments address those claims.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:1990317
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - gin4-agent-go
  - gin4-agent-ols
  - gin4-agent-taxon
  - gin4-agent-crossref-paper
  - gin4-agent-epmc-paper
  - gin4-browser-primary-body
  - gin4-browser-primary-discussion
  - gin4-agent-complex-portal
  - gin4-agent-uniprot
  - gin4-agent-taxon-strain
  - gin4-agent-interpro-septin
  - gin4-agent-interpro-nap
  - gin4-agent-interpro-bni5
  - gin4-agent-interpro-kinase
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:1990317
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:1990317
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:1990317
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:1990317
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:1990317
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch7 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: gin4-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:1990317,GO:1902554,GO:0000144,GO:0000921
  locator: Native GO:1990317, GO:1902554, GO:0000144 and GO:0000921 definitions and
    child relations
  accessed_at: '2026-10-21T07:02:40.856749Z'
  support: supports
  summary: Exact active Gin4-complex definition names the eight proteins and at least
    two Gin4 molecules. The kinase-complex parent, bud-neck septin-ring parthood and
    septin-ring-assembly process participation match the record.
  snapshot_sha256: 30c510a74c963374ddf9b4b8ae23e523fb43d6d9ca380e1618f637c7f45a4779
- evidence_id: gin4-agent-ols
  kind: authority
  reference: https://www.ebi.ac.uk/ols4/api/ontologies/go/terms/http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FGO_1990317
  locator: OLS GO:1990317 native term record
  accessed_at: '2026-10-21T07:02:40.816980Z'
  support: supports
  summary: OLS confirms the exact Gin4 complex identity, definition and source PMID,
    and exposes traversal links for parthood and process-participation relations.
    This captured payload does not resolve their target IDs; those exact edges are
    established by the separately inspected native QuickGO child relations.
  snapshot_sha256: 1b9f2e4011c2d10fae15114421b3c7f90ffe8dbe4cb8ef172f0d87f1520c3c5f
- evidence_id: gin4-agent-taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: ENA scientificName, taxId and rank
  accessed_at: '2026-10-21T07:02:40.863990Z'
  support: supports
  summary: Native ENA taxonomy confirms Saccharomyces cerevisiae4932 at species rank.
  snapshot_sha256: be57b95543b586448f6bd2889db42e91038e90ae2d12e8f654050c92af5b9087
- evidence_id: gin4-agent-crossref-paper
  kind: authority
  reference: https://api.crossref.org/works/10.1091/mbc.01-10-0500
  locator: Crossref title, authors and publication date
  accessed_at: '2026-10-21T07:03:11.084787Z'
  support: supports
  summary: DOI10.1091/mbc.01-10-0500 resolves to Mortensen, McDonald, Yates and Kellogg2002,
    Cell Cycle-dependent Assembly of a Gin4-Septin Complex.
  snapshot_sha256: 8afb8420adb11c38eec10b7d41974bd6f3df5af22d561dab70c245bf3c6ea082
- evidence_id: gin4-agent-epmc-paper
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:12058072%20AND%20SRC:MED&format=json&resultType=core
  locator: Europe PMC exact primary record and abstract
  accessed_at: '2026-10-21T07:03:15.345694Z'
  support: supports
  summary: Native PMID12058072/PMC117627 record and complete abstract agree on the
    Gin4 complex and provide the primary identity behind the GO definition.
  snapshot_sha256: b82ad73baf6c55bf963c569cc6376e8c57fd8f58f21b7e892524e6ed3957c406
- evidence_id: gin4-browser-primary-body
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC117627/
  locator: 'Methods: Strains and Culture Conditions; Results: Gin4 Is Found in a Complex
    with Itself during Mitosis; Figure 2; Results: Purification of Endogenous Gin4
    Complexes by Immunoaffinity Chromatography; Table 1; Results: Assembly of the
    Gin4 Complex Occurs as Cells Enter Mitosis; Figure 4; saved tool-rendered primary-body
    passages, not publisher HTML or image pixels'
  accessed_at: '2026-10-21T07:06:00.781858Z'
  support: supports
  summary: Methods place experiments in W303. Results/Table1 identify Gin4 and Cdc3/10/11/12,
    Shs1 (SEP7), Nap1 and Bni5 in specific immunoaffinity-purified complexes. Distinct
    tagged Gin4 copies coimmunoprecipitate in mitosis, supporting at least two molecules
    without an exact copy count or direct-contact proof. Results/Figure4 distinguish
    mitotic septin association from persistent Nap1 association.
  snapshot_sha256: 7e3903eb954d2a26acc27bc3a3d939ec1c48777dd3824e57a7b618ca28312eaf
- evidence_id: gin4-browser-primary-discussion
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC117627/
  locator: 'Discussion: Gin4 Assembles into a Multiprotein Complex as Cells Enter
    Mitosis; Table 2; Discussion: Mechanisms Leading to the Activation of Gin4 during
    Mitosis; saved tool-rendered primary-body passages, not publisher HTML or image
    pixels'
  accessed_at: '2026-10-21T07:06:25.539423Z'
  support: supports
  summary: Discussion supports mitotic multiprotein assembly while leaving direct
    Gin4 self-contact, detailed recruitment/activation order and additional weak copurifying
    candidates unresolved. Regulatory dependencies are not automatically stable constituents.
  snapshot_sha256: 4b214478d95096ecc4fcb30cbd5214c0fbd9aa3eb64b508aabdb0801884468ae
- evidence_id: gin4-agent-complex-portal
  kind: database
  reference: https://www.ebi.ac.uk/intact/complex-ws/complex/CPX-1712
  locator: Native complex name, systematicName, GO cross-reference, organism, participants
    and properties
  accessed_at: '2026-10-21T07:05:51.260297Z'
  support: supports
  summary: CPX-1712 independently identifies the Gin4 serine/threonine kinase complex,
    exact GO cross-reference and eight participants. Taxon is S288C; participant stoichiometries
    are null while prose states at least two Gin4. This corroborates identities without
    imposing database strain context on W303 experiments.
  snapshot_sha256: a79af693780713b7d00f0ded35c4d5671be8bf98323c210c04b1bd38659035e8
- evidence_id: gin4-agent-uniprot
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=organism_id:559292%20AND%20reviewed:true%20AND%20(gene_exact:BNI5%20OR%20gene_exact:CDC3%20OR%20gene_exact:CDC10%20OR%20gene_exact:CDC11%20OR%20gene_exact:CDC12%20OR%20gene_exact:GIN4%20OR%20gene_exact:NAP1%20OR%20gene_exact:SHS1)&format=json&size=50
  locator: 'Exact reviewed S288C gene query: BNI5, CDC3, CDC10, CDC11, CDC12, GIN4,
    NAP1 and SHS1'
  accessed_at: '2026-10-21T07:02:41.555493Z'
  support: supports
  summary: Native reviewed S288C entries resolve all eight named proteins and their
    Gin4-complex subunit annotations. These are possible taxon-paired curation examples,
    not accessions already asserted by the target or a substitute for primary composition
    evidence.
  snapshot_sha256: dbc3dd1cd306437bfe0a243f4cda1b29154e55b424d7f717b4c6a8392782c39b
- evidence_id: gin4-agent-taxon-strain
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Native strain name/rank
  accessed_at: '2026-10-21T07:03:28.375633Z'
  support: supports
  summary: ENA confirms S288C559292 is a strain distinct from the W303 source context.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: gin4-agent-interpro-septin
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR016491/
  locator: Native InterPro name/type and description
  accessed_at: '2026-10-21T07:05:50.985912Z'
  support: supports
  summary: IPR016491 is the Septin family, an exact family-level candidate for the
    generic septin class; the inspected UniProt examples carry it.
  snapshot_sha256: 5797c626d192b641ed5b4b2231e729f9f179bfd6bb18f911689fa08253688c4a
- evidence_id: gin4-agent-interpro-nap
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002164/
  locator: Native InterPro name/type and description
  accessed_at: '2026-10-21T07:05:50.969116Z'
  support: supports
  summary: IPR002164 is the Nucleosome assembly protein family, a family-level candidate
    for Nap1; the inspected Nap1 entry carries it.
  snapshot_sha256: 1c410a4a211a9b67a45f8e2b564c2e92f08f6149101462ffeb7438b531f1a80b
- evidence_id: gin4-agent-interpro-bni5
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR063385/
  locator: Native InterPro name/type and description
  accessed_at: '2026-10-21T07:05:50.957456Z'
  support: supports
  summary: IPR063385 is a BNI5 helical domain. Its domain type does not establish
    an exact whole-protein Bni5 family mapping.
  snapshot_sha256: 60a13daadd643129f2e48c9c95439192651fe614194ade631b669d5091007e4d
- evidence_id: gin4-agent-interpro-kinase
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000719/
  locator: Native InterPro name/type and description
  accessed_at: '2026-10-21T07:05:51.073193Z'
  support: supports
  summary: IPR000719 is the Protein kinase domain. It is broader than Gin4 and does
    not establish an exact full-Gin4 family identity.
  snapshot_sha256: 8d9f1b1630c7c99ec11a01e67488bb8516c88934e645e65fdce915d316c67827
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/gin4_complex.yaml
  locator: Entire maintained YAML
  accessed_at: '2026-10-21T07:08:06Z'
  support: context_only
  summary: The record remains PROPOSED and preserves all eight identities plus the
    minimum Gin4 multiplicity in its definition. Structured component grounding is
    explicitly deferred. The graph is NONMECHANISTIC and asserts only parthood and
    process participation.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/gin4_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:06:21Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/gin4_complex.yaml'
  snapshot_sha256: 2dcbd5fc5361a300771ee87c7839d0e753c30f7036715958b83a742690eaf51c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/gin4_complex.yaml --out
    /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/gin4_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:06:23Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/gin4_complex.yaml\
    \ --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/gin4_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch7-20261021-dz9x5cv0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/gin4_complex-strict.tsv"
  snapshot_sha256: ce48014212cfbce30ac70f53068b10905d05ab908462e1b62ca1d925b84df784
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/gin4_complex.yaml; exact collect() scope
  accessed_at: '2026-10-21T07:08:06Z'
  support: supports
  summary: '5 of5 collected target identifiers returned OK at the unchanged base.
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
  topic: Named kinase complex rather than ring or process
  outcome: supported
  target_ids:
  - GO:1990317
  summary: Exact GO identity, kinase-complex parent, ring parthood and process participation
    are supported by native QuickGO definitions and child relations. OLS independently
    confirms term identity and source. The target distinguishes a multiprotein assembly
    from the containing septin ring and the biological process.
  evidence_ids:
  - gin4-agent-go
  - gin4-agent-ols
  - record
- assessment_id: composition
  area: evidence
  topic: Eight identities and minimum Gin4 multiplicity
  outcome: supported
  target_ids:
  - GO:1990317
  summary: Primary Results/Table1 support the named proteins; tagged coimmunoprecipitation
    supports at least two Gin4 molecules. Eight identities do not imply an eight-molecule
    complex, and no exact stoichiometry or direct Gin4-Gin4 contact is asserted.
  evidence_ids:
  - gin4-browser-primary-body
  - gin4-browser-primary-discussion
  - gin4-agent-go
  - gin4-agent-complex-portal
- assessment_id: scope
  area: scope
  topic: Species record with strain-specific source contexts
  outcome: supported
  target_ids:
  - GO:1990317
  summary: The species example is supported. Primary W303 experiments and native S288C
    database participants are kept separate. COMMON is qualitative occurrence in the
    model organism, not a measured cross-strain prevalence.
  evidence_ids:
  - gin4-agent-taxon
  - gin4-agent-taxon-strain
  - gin4-agent-complex-portal
  - gin4-agent-uniprot
  - gin4-browser-primary-body
  - gin4-browser-primary-discussion
- assessment_id: graph
  area: graph
  topic: Mitotic participation without recruitment sequence
  outcome: supported
  target_ids:
  - GO:1990317
  summary: Both graph edges are ontology-backed and consistent with cell-cycle-dependent
    experimental association. The record does not specify molecular order, treat regulatory
    dependencies as constituents or conflate persistent Gin4-Nap1 binding with full
    mitotic complex assembly.
  evidence_ids:
  - gin4-agent-go
  - gin4-browser-primary-body
  - gin4-browser-primary-discussion
- assessment_id: completeness
  area: completeness
  topic: Accurate prose composition and acknowledged structured curation
  outcome: supported
  target_ids:
  - GO:1990317
  summary: The component-grounding TODO is honest and no incorrect accession is asserted.
    Native sources make structured septin/NAP and taxon-paired complex composition
    enrichment feasible, but the record already accurately states the supported composition;
    an empty optional collection alone is not a defect. Exact full Bni5/Gin4 family
    mapping remains unresolved.
  evidence_ids:
  - gin4-agent-go
  - gin4-agent-complex-portal
  - gin4-agent-uniprot
  - record
  - gin4-agent-interpro-septin
  - gin4-agent-interpro-nap
  - gin4-agent-interpro-bni5
  - gin4-agent-interpro-kinase
- assessment_id: provenance
  area: provenance
  topic: Source behind ontology definition
  outcome: supported
  target_ids:
  - GO:1990317
  summary: The native GO source is traceable to the inspected primary paper. Relevant
    body passages and figure captions were read rather than inferring experimental
    details from a title or metadata alone.
  evidence_ids:
  - gin4-agent-go
  - gin4-agent-crossref-paper
  - gin4-agent-epmc-paper
  - gin4-browser-primary-body
  - gin4-browser-primary-discussion
findings: []
actions: []
limitations:
- Primary body passages were read through the PMC browser rendering. Direct publisher/API/PDF
  routes returned403,500,404,429 or challenge pages; those responses are not treated
  as source text. Figure panels were not visually inspected.
- At least two Gin4 molecules is a lower bound inferred from tagged coimmunoprecipitation,
  not exact stoichiometry or proof of direct self-contact. Database participant counts
  remain unspecified.
- Primary W303 experiments and curated S288C records are distinct strain contexts.
  No database accession or strain is silently imported into the scientific record.
- Structured component enrichment remains open; verified septin/NAP families do not
  establish exact full Bni5/Gin4 family mappings or every weak copurifying candidate.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Explicit user instruction requires saving every reviewed target, including clean
  observations; no issue was invented.
- A read-only collaborator inspected primary passages and native sources. Root read
  the complete unchanged target and assessed it after batch-seven native input inspection.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
