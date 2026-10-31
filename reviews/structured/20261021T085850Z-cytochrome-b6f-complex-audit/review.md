# Cytochrome b6f whole-complex identity, electron-transfer scope and core inventory review

- Review: 20261021T085850Z-cytochrome-b6f-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:41:29Z
- Finished UTC: 2026-10-21T08:58:50Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact b6f identity, cyanobacterial example and bounded electron/proton-coupling graph are supported. One minor completeness finding separates established core composition from the unresolved family-grounding TODO.

## Scope And Provenance

Entire maintained target, five graph edges, taxonomy/discussion and native GO; complete primary Methods/Results/Discussion with tables/captions; inspected cited-review electron-transfer body excerpt.

Selection: Fifth target in batch thirteen; strict repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0009512 | data/structures/energy_complex/cytochrome_b6f_complex.yaml | maintained | cytochrome b6f complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0009512 | Focused validator passed. |
| Focused native strict | passed | True | GO:0009512 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0009512 | 8 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0009512 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0009512 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0009512 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0009512 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0009512 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0009512 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Exact complex and membrane parthood

identity: supported. Targets: GO:0009512.

GO identity, category and kind denote the whole b6f dimeric assembly. Thylakoid parthood is supported; PSI is a separate downstream complex and a soluble carrier is not silently included as a constitutive b6f subunit.

### Known core versus unresolved family identifiers

completeness: concern. Targets: GO:0009512.

The target defers all component rows until exact family identifiers are resolved. Native GO already identifies three catalytic core types and the cited primary paper directly identifies four large/four small Nostoc subunits. Family uncertainty need not block named label-only core constituents. This is a bounded consequential composition gap, not a requirement to fill every optional slot or generalize the full Nostoc inventory to every species.

### Qualitative cyanobacterial scope and strain

scope: supported. Targets: GO:0009512.

The names/ranks match and the primary culture is Nostoc PCC7120 grown in BG11 at30C. COMMON is qualitative, not a measured prevalence. Internal-thylakoid qualification avoids claiming that the membrane architecture is universal across all cyanobacteria.

### Transfer and proton coupling

evidence: supported. Targets: GO:0009512.

Native GO and inspected review text support the physiological function. The primary isolated-complex assay supports oxidoreductase activity under its detergent/substrate conditions; it is not separately cited as a complete proton-translocation or organism-level photosynthetic performance assay.

### All five physiological placement edges

graph: supported. Targets: GO:0009512.

The membrane location, reduced-quinone input, soluble downstream carrier and process/gradient contributions agree with the inspected sources. NONMECHANISTIC appropriately omits sites, relay chemistry, low-potential chain and carrier variants; it does not claim direct b6f-to-PSI electron contact or light absorption by b6f as its catalytic driver.

### Purification and inference limits

scope: supported. Targets: GO:0009512.

The crystal and MS data establish composition/architecture in isolated Nostoc complex. Partial PetC N-terminal acetylation is directly measured; suggested causes of extraction instability and protease involvement remain hypotheses. The record does not import these hypotheses or paper-caption PetA typo for Rieske into a component claim.

### Source-backed identity and actionable TODO

provenance: supported. Targets: GO:0009512.

Both exact citations resolve. The existing discussion is useful provenance, but known composition should be separated from unresolved family grounding/cofactor boundaries. Images, individual accessions, kinetic constants and full stoichiometry are optional and their absence is not independently a finding.

## Findings

### F1: Represent known core composition independently of family grounding

minor / open / confirmed; issue key: b6f-known-core-deferred-for-family-grounding.

The record has no components and its b6f_subunit_boundaries discussion explicitly defers adding subunit rows until source-neutral family groundings are resolved. GO0009512 identifies the catalytic core, and Baniulis2009 ESI-MS Table3 plus the crystal structure directly establish a named eight-subunit Nostoc inventory. Label-only rows can preserve known core composition while exact family identities remain open. The consequential gap is the blanket deferral of established constituents, not lack of every optional detail.

## Recommended Actions And Acceptance Checks

### A1

Add supported core constituent rows with primary evidence and unresolved grounding status where necessary. Scope additional Nostoc subunits to that experiment, and update discussion progress to distinguish known membership from exact family/cofactor uncertainty.

- Include at least source-supported cytochrome b6, cytochrome f and Rieske ISP identities without guessed family CURIEs.
- Keep small-subunit variability, cofactors, soluble carriers and universal essentiality distinct; use Table3/Results rather than the erroneous PetA label for Rieske in Figure3 caption.
- Use the guarded record writer, append curation/repository history, regenerate pages, and pass native schema/strict/products/history/qc gates in separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/energy_complex/cytochrome_b6f_complex.yaml; Entire maintained YAML including history, all component/protein/graph/evidence/discussion fields | context_only | Complete maintained record read; PROPOSED status and historical curation preserved. |
| policy | docs/CURATION.md; Components and evidence rules; exact review profile/checklist/schema captured in native inspect | context_only | Exact identifiers are required when assigned, but label-only constituent rows may retain unresolved family grounding; source-specific preparation and inference must be preserved. |
| b6f-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009512,GO:0009522,GO:0009767,GO:0042651; All four complete native term results: definitions, names, status, synonyms and available children | supports | Active GO0009512 exactly names the dimeric b6f complex and core cytochrome b, Rieske ISP and cytochrome f. GO0042651/0009767/0009522 support membrane/process/downstream-PSI identities. Species-variable additional subunits remain explicit. |
| b6f-prep-tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; Complete native identity fields and otherNames | supports | Native taxId/name/rank/lineage agree with Cyanobacteriota and Nostoc sp.PCC7120=FACHB-418; Nostoc/Anabaena PCC7120 aliases are explicit. |
| b6f-prep-tax-103690 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/103690; Complete native identity fields and otherNames | supports | Native taxId/name/rank/lineage agree with Cyanobacteriota and Nostoc sp.PCC7120=FACHB-418; Nostoc/Anabaena PCC7120 aliases are explicit. |
| b6f-prep-baniulis2009-pmc-html | https://pmc.ncbi.nlm.nih.gov/articles/PMC2665108/; PMC2665108 native full HTML: complete Experimental Procedures, Results and Discussion; Tables1–4 and Figure1–4 captions read. No figure pixels or raw MS/crystallographic data analysis. | supports | Primary Nostoc PCC7120 preparations produce an active detergent-isolated dimer. ESI-MS Table3 identifies eight subunits, and the3.0A crystal model supports the architecture. The Methods assay decyl-plastoquinol-to-plastocyanin oxidoreductase activity; no direct physiological proton-pumping measurement or universal necessity of all small subunits follows. |
| b6f-prep-baniulis2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1074/jbc.M809196200; Exact DOI/title/authors/year/PMID/PMC identity fields | supports | Exact DOI maps to Baniulis et al.2009, PMID19189962/PMC2665108, matching the read primary body. |
| b6f-prep-perez2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1146/annurev-cellbio-120823-022747; Exact article identity and abstract; metadata is not full-body evidence. | supports | Exact DOI maps to Perez-Boerema, Engel and Wietrzynski2024, PMID38950450, Evolution of Thylakoid Structural Diversity. |
| perez2024-body-excerpt | https://doi.org/10.1146%2Fannurev-cellbio-120823-022747; Browser-indexed publisher body: The Building Blocks of Thylakoid Membranes &gt; Electron Transport Chain Complexes; Introduction; no complete article or native HTTP200 claim. | supports | Inspected review text places b6f between PSII and PSI, with plastoquinol input, soluble plastocyanin output and proton transfer into the lumen. Its Introduction notes thylakoid-lacking Gloeobacter; the record explicitly bounds scope to cyanobacteria with internal thylakoids. |
| schema-result | just validate data/structures/energy_complex/cytochrome_b6f_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/energy_complex/cytochrome_b6f_complex.yaml |
| strict-result | just validate-strict data/structures/energy_complex/cytochrome_b6f_complex.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_b6f_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/energy_complex/cytochrome_b6f_complex.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_b6f_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_b6f_complex-strict.tsv |
| target-curies | just check-curies-strict; data/structures/energy_complex/cytochrome_b6f_complex.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 8 of8 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The Perez-Boerema2024 native publisher endpoints returned403; inspected publisher body passages were available through browser indexing. The saved raw response and capture-time/hash receipt identify that limited access, not a full-paper read.
- Baniulis2009 main claim-bearing sections/tables/captions were read; figure pixels, supplementary data and raw MS/crystallography were not reanalyzed.
- No exact subunit family or protein-accession inventory is newly assigned; additional species-variable subunits and stoichiometry require bounded curation.
- Purified-complex activity and3.0A architecture do not by themselves prove universal assembly necessity or direct physiological proton-coupling stoichiometry.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All12 native input hashes verified; no neighboring maintained-record dependency.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085850Z-cytochrome-b6f-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cytochrome b6f whole-complex identity, electron-transfer scope and core inventory
  review
started_at: '2026-10-21T08:41:29Z'
finished_at: '2026-10-21T08:58:50Z'
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
summary: Exact b6f identity, cyanobacterial example and bounded electron/proton-coupling
  graph are supported. One minor completeness finding separates established core composition
  from the unresolved family-grounding TODO.
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
  - path: data/structures/energy_complex/cytochrome_b6f_complex.yaml
    sha256: 6d228ab890a3a8f8f67e756ac5343896db16bc57dfc55d8250d2afd87851f7c3
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
- target_id: GO:0009512
  path: data/structures/energy_complex/cytochrome_b6f_complex.yaml
  label: cytochrome b6f complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/cytochrome_b6f_complex.yaml
    role: maintained scientific record
scope:
  description: Entire maintained target, five graph edges, taxonomy/discussion and
    native GO; complete primary Methods/Results/Discussion with tables/captions; inspected
    cited-review electron-transfer body excerpt.
  selection: Fifth target in batch thirteen; strict repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0009512
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0009512
  command: just validate data/structures/energy_complex/cytochrome_b6f_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0009512
  command: just validate-strict data/structures/energy_complex/cytochrome_b6f_complex.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_b6f_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0009512
  summary: 8 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0009512
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - b6f-prep-go
  - b6f-prep-tax-1117
  - b6f-prep-tax-103690
  - b6f-prep-baniulis2009-pmc-html
  - b6f-prep-baniulis2009-meta
  - b6f-prep-perez2024-meta
  - perez2024-body-excerpt
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0009512
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0009512
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0009512
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0009512
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0009512
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch13 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/energy_complex/cytochrome_b6f_complex.yaml
  locator: Entire maintained YAML including history, all component/protein/graph/evidence/discussion
    fields
  accessed_at: '2026-10-21T08:53:44Z'
  support: context_only
  summary: Complete maintained record read; PROPOSED status and historical curation
    preserved.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Components and evidence rules; exact review profile/checklist/schema captured
    in native inspect
  accessed_at: '2026-10-21T08:53:44Z'
  support: context_only
  summary: Exact identifiers are required when assigned, but label-only constituent
    rows may retain unresolved family grounding; source-specific preparation and inference
    must be preserved.
- evidence_id: b6f-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009512,GO:0009522,GO:0009767,GO:0042651
  locator: 'All four complete native term results: definitions, names, status, synonyms
    and available children'
  accessed_at: '2026-10-21T08:39:15.006441Z'
  support: supports
  summary: Active GO0009512 exactly names the dimeric b6f complex and core cytochrome
    b, Rieske ISP and cytochrome f. GO0042651/0009767/0009522 support membrane/process/downstream-PSI
    identities. Species-variable additional subunits remain explicit.
  snapshot_sha256: 90db9991db90483f31f7f79d784515b1665966e1919e61e8058310f44a73b8ca
- evidence_id: b6f-prep-tax-1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: Complete native identity fields and otherNames
  accessed_at: '2026-10-21T08:39:15.064546Z'
  support: supports
  summary: Native taxId/name/rank/lineage agree with Cyanobacteriota and Nostoc sp.PCC7120=FACHB-418;
    Nostoc/Anabaena PCC7120 aliases are explicit.
  snapshot_sha256: 0462d61ee879faf0de43deb3472da6e0fe29fdf63cc068591b0ca652eb921c4d
- evidence_id: b6f-prep-tax-103690
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/103690
  locator: Complete native identity fields and otherNames
  accessed_at: '2026-10-21T08:39:15.011565Z'
  support: supports
  summary: Native taxId/name/rank/lineage agree with Cyanobacteriota and Nostoc sp.PCC7120=FACHB-418;
    Nostoc/Anabaena PCC7120 aliases are explicit.
  snapshot_sha256: 807abd1968631ec3ee802bf72e180cfd5d7c74a5ae13cd97b8741b57e7342185
- evidence_id: b6f-prep-baniulis2009-pmc-html
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2665108/
  locator: 'PMC2665108 native full HTML: complete Experimental Procedures, Results
    and Discussion; Tables1–4 and Figure1–4 captions read. No figure pixels or raw
    MS/crystallographic data analysis.'
  accessed_at: '2026-10-21T08:42:01.419829Z'
  support: supports
  summary: Primary Nostoc PCC7120 preparations produce an active detergent-isolated
    dimer. ESI-MS Table3 identifies eight subunits, and the3.0A crystal model supports
    the architecture. The Methods assay decyl-plastoquinol-to-plastocyanin oxidoreductase
    activity; no direct physiological proton-pumping measurement or universal necessity
    of all small subunits follows.
  snapshot_sha256: 10711d2a7cdff876c3f901e69ac3764271aeda7af4fce0ee837ada8a6d28c862
- evidence_id: b6f-prep-baniulis2009-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1074/jbc.M809196200
  locator: Exact DOI/title/authors/year/PMID/PMC identity fields
  accessed_at: '2026-10-21T08:39:18.475329Z'
  support: supports
  summary: Exact DOI maps to Baniulis et al.2009, PMID19189962/PMC2665108, matching
    the read primary body.
  snapshot_sha256: b8a27eadc119809309b29cab43f9e1f5b750a7976ce8daac1826acfcea9749c3
- evidence_id: b6f-prep-perez2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1146/annurev-cellbio-120823-022747
  locator: Exact article identity and abstract; metadata is not full-body evidence.
  accessed_at: '2026-10-21T08:39:18.846261Z'
  support: supports
  summary: Exact DOI maps to Perez-Boerema, Engel and Wietrzynski2024, PMID38950450,
    Evolution of Thylakoid Structural Diversity.
  snapshot_sha256: f9df3427bb3b35764922628c9e89cc9378fa7875a4a103bde71a75b130d54926
- evidence_id: perez2024-body-excerpt
  kind: authority
  reference: https://doi.org/10.1146%2Fannurev-cellbio-120823-022747
  locator: 'Browser-indexed publisher body: The Building Blocks of Thylakoid Membranes
    > Electron Transport Chain Complexes; Introduction; no complete article or native
    HTTP200 claim.'
  accessed_at: '2026-10-21T08:46:38.912004Z'
  support: supports
  summary: Inspected review text places b6f between PSII and PSI, with plastoquinol
    input, soluble plastocyanin output and proton transfer into the lumen. Its Introduction
    notes thylakoid-lacking Gloeobacter; the record explicitly bounds scope to cyanobacteria
    with internal thylakoids.
  snapshot_sha256: 1e2a20aee1043d6a8c9b511e909b825174d51fe9374f438c494e924d20992a0e
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/energy_complex/cytochrome_b6f_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:32Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/cytochrome_b6f_complex.yaml'
  snapshot_sha256: f9395ba121e4a2c80aaa4fdf40cc7e2e75e277e29ba49592944021cc0988e20d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/energy_complex/cytochrome_b6f_complex.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_b6f_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:34Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/energy_complex/cytochrome_b6f_complex.yaml\
    \ --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_b6f_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/cytochrome_b6f_complex-strict.tsv"
  snapshot_sha256: 55849e407e28a7fceb13996653e1691b4bc2fcbd027cab5b48e1dc0c086dab38
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/energy_complex/cytochrome_b6f_complex.yaml; exact collect()
    scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:53:44Z'
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
  topic: Exact complex and membrane parthood
  outcome: supported
  target_ids:
  - GO:0009512
  summary: GO identity, category and kind denote the whole b6f dimeric assembly. Thylakoid
    parthood is supported; PSI is a separate downstream complex and a soluble carrier
    is not silently included as a constitutive b6f subunit.
  evidence_ids:
  - b6f-prep-go
  - b6f-prep-baniulis2009-pmc-html
  - record
- assessment_id: inventory
  area: completeness
  topic: Known core versus unresolved family identifiers
  outcome: concern
  target_ids:
  - GO:0009512
  summary: The target defers all component rows until exact family identifiers are
    resolved. Native GO already identifies three catalytic core types and the cited
    primary paper directly identifies four large/four small Nostoc subunits. Family
    uncertainty need not block named label-only core constituents. This is a bounded
    consequential composition gap, not a requirement to fill every optional slot or
    generalize the full Nostoc inventory to every species.
  evidence_ids:
  - b6f-prep-go
  - b6f-prep-baniulis2009-pmc-html
  - policy
  - record
- assessment_id: taxon
  area: scope
  topic: Qualitative cyanobacterial scope and strain
  outcome: supported
  target_ids:
  - GO:0009512
  summary: The names/ranks match and the primary culture is Nostoc PCC7120 grown in
    BG11 at30C. COMMON is qualitative, not a measured prevalence. Internal-thylakoid
    qualification avoids claiming that the membrane architecture is universal across
    all cyanobacteria.
  evidence_ids:
  - b6f-prep-tax-1117
  - b6f-prep-tax-103690
  - b6f-prep-baniulis2009-pmc-html
  - perez2024-body-excerpt
  - record
- assessment_id: activity
  area: evidence
  topic: Transfer and proton coupling
  outcome: supported
  target_ids:
  - GO:0009512
  summary: Native GO and inspected review text support the physiological function.
    The primary isolated-complex assay supports oxidoreductase activity under its
    detergent/substrate conditions; it is not separately cited as a complete proton-translocation
    or organism-level photosynthetic performance assay.
  evidence_ids:
  - b6f-prep-go
  - b6f-prep-baniulis2009-pmc-html
  - perez2024-body-excerpt
  - record
- assessment_id: graph
  area: graph
  topic: All five physiological placement edges
  outcome: supported
  target_ids:
  - GO:0009512
  summary: The membrane location, reduced-quinone input, soluble downstream carrier
    and process/gradient contributions agree with the inspected sources. NONMECHANISTIC
    appropriately omits sites, relay chemistry, low-potential chain and carrier variants;
    it does not claim direct b6f-to-PSI electron contact or light absorption by b6f
    as its catalytic driver.
  evidence_ids:
  - b6f-prep-go
  - perez2024-body-excerpt
  - b6f-prep-baniulis2009-pmc-html
  - record
- assessment_id: experimental
  area: scope
  topic: Purification and inference limits
  outcome: supported
  target_ids:
  - GO:0009512
  summary: The crystal and MS data establish composition/architecture in isolated
    Nostoc complex. Partial PetC N-terminal acetylation is directly measured; suggested
    causes of extraction instability and protease involvement remain hypotheses. The
    record does not import these hypotheses or paper-caption PetA typo for Rieske
    into a component claim.
  evidence_ids:
  - b6f-prep-baniulis2009-pmc-html
  - record
- assessment_id: provenance
  area: provenance
  topic: Source-backed identity and actionable TODO
  outcome: supported
  target_ids:
  - GO:0009512
  summary: Both exact citations resolve. The existing discussion is useful provenance,
    but known composition should be separated from unresolved family grounding/cofactor
    boundaries. Images, individual accessions, kinetic constants and full stoichiometry
    are optional and their absence is not independently a finding.
  evidence_ids:
  - b6f-prep-baniulis2009-meta
  - b6f-prep-perez2024-meta
  - b6f-prep-baniulis2009-pmc-html
  - b6f-prep-go
  - record
  - policy
findings:
- finding_id: F1
  issue_key: b6f-known-core-deferred-for-family-grounding
  category: completeness
  severity: minor
  status: open
  certainty: confirmed
  title: Represent known core composition independently of family grounding
  description: The record has no components and its b6f_subunit_boundaries discussion
    explicitly defers adding subunit rows until source-neutral family groundings are
    resolved. GO0009512 identifies the catalytic core, and Baniulis2009 ESI-MS Table3
    plus the crystal structure directly establish a named eight-subunit Nostoc inventory.
    Label-only rows can preserve known core composition while exact family identities
    remain open. The consequential gap is the blanket deferral of established constituents,
    not lack of every optional detail.
  target_ids:
  - GO:0009512
  field_paths:
  - components
  - discussions[discussion_id=b6f_subunit_boundaries]
  evidence_ids:
  - b6f-prep-go
  - b6f-prep-baniulis2009-pmc-html
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/cytochrome_b6f_complex.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Non-blocking and resolvable core-composition gap; exact whole-complex
    identity and function remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0009512
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/cytochrome_b6f_complex.yaml
    role: maintained scientific record
  description: Add supported core constituent rows with primary evidence and unresolved
    grounding status where necessary. Scope additional Nostoc subunits to that experiment,
    and update discussion progress to distinguish known membership from exact family/cofactor
    uncertainty.
  acceptance_checks:
  - Include at least source-supported cytochrome b6, cytochrome f and Rieske ISP identities
    without guessed family CURIEs.
  - Keep small-subunit variability, cofactors, soluble carriers and universal essentiality
    distinct; use Table3/Results rather than the erroneous PetA label for Rieske in
    Figure3 caption.
  - Use the guarded record writer, append curation/repository history, regenerate
    pages, and pass native schema/strict/products/history/qc gates in separately authorized
    curation.
  generator: Maintained structure YAML; generated pages derive from it.
limitations:
- The Perez-Boerema2024 native publisher endpoints returned403; inspected publisher
  body passages were available through browser indexing. The saved raw response and
  capture-time/hash receipt identify that limited access, not a full-paper read.
- Baniulis2009 main claim-bearing sections/tables/captions were read; figure pixels,
  supplementary data and raw MS/crystallography were not reanalyzed.
- No exact subunit family or protein-accession inventory is newly assigned; additional
  species-variable subunits and stoichiometry require bounded curation.
- Purified-complex activity and3.0A architecture do not by themselves prove universal
  assembly necessity or direct physiological proton-coupling stoichiometry.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- All12 native input hashes verified; no neighboring maintained-record dependency.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
