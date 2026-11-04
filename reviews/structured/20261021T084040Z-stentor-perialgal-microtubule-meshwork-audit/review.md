# Stentor perialgal microtubule meshwork identity and evidence review

- Review: 20261021T084040Z-stentor-perialgal-microtubule-meshwork-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:24:56Z
- Finished UTC: 2026-10-21T08:40:40Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The local structure identity, directly stained beta-tubulin family, host taxon, proposed positioning function and link-only image are supported. No concrete curation defect was established.

## Scope And Provenance

Entire target; native GO, taxonomy and family authorities; all source sections supporting anatomy, taxon boundary, microscopy and proposed positioning; native Figure3 visual inspection and PDF page6 caption.

Selection: Fourth unreviewed target in batch twelve, selected in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:stentor_perialgal_microtubule_meshwork | data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml | maintained | Stentor perialgal microtubule meshwork |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Focused validator passed. |
| Target resolver slice | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | 5 identifiers OK; 2 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | cellstructuremech:stentor_perialgal_microtubule_meshwork | The target is a physical cytoskeletal architecture and a qualified anatomical-function hypothesis, without an expression-module mechanism. |
| Claim-level scientific review | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | cellstructuremech:stentor_perialgal_microtubule_meshwork | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Host meshwork versus associated cells and neighboring fibers

identity: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

Definition and broad basket synonym preserve an irregular host cortical architecture. Symbiotic Chlorella, vacuole membranes, Km bundles and regular one-alga cages are excluded. Broad GO hierarchy is consistent with the observed location; local identity is not presented as exact GO mapping.

### Directly stained tubulin family

grounding: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

The beta-tubulin family grounding matches the Sigma T0198 immunofluorescence assay and native InterPro family. No specific Stentor paralog, assembly essentiality, complete constituent list or linker identity follows from the staining; the record retains those limits.

### Directly imaged host and separate algal symbiont

scope: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

The host species name and taxonomy agree. Morphological and18S characterization, together with isolation and separate culture of the algae, support keeping host cytoskeleton distinct from symbiont identity and organelle fixation. No genus-wide distribution or absence inference is asserted.

### Association and proposed cortical retention

evidence: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

Spatial association and recovery after bulk centrifugation support a hypothesis of cortical retention. They do not establish a selective requirement of this meshwork for anchoring, phototaxis, photosynthetic gain or gas exchange. The qualified function and explicit open discussion accurately preserve this distinction.

### Exact figure, source anchor and licence caveat

provenance: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

The image caption, source accession F3, PDF page6 anchor, species, attribution and link-only status agree with the source. CC BY4.0 follows the explicit copyright statement; the record correctly preserves the null metadata field and hosting guard. Expanded-image distances are not promoted to native measurements.

### Open inventory and experimental gaps

completeness: supported. Targets: cellstructuremech:stentor_perialgal_microtubule_meshwork.

The partial composition and lack of causal graph are appropriate to current evidence. Selective disruption/rescue, attachment proteins, native paralogs, stoichiometry and assembly requirements remain open. Historical searches are not represented as newly exhaustive queries; the fresh perialgal search is bounded.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| perialgal-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863; Both term definitions and active flags | supports | Both terms are active: GO0005622 is intracellular anatomical structure and GO0030863 is the cortical cytoskeleton beneath the plasma membrane. They provide a broad parent and encompassing framework, respectively. |
| perialgal-prep-tax-2721102 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2721102; taxId, scientificName, rank and lineage | supports | Taxon2721102 is Stentor pyriformis at species rank, in Stentoridae/Heterotrichida. |
| perialgal-prep-IPR002453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; Entry accession, family type, name and hierarchy | supports | IPR002453 is the Beta tubulin family, distinguished from alpha and gamma tubulin in the family hierarchy. |
| perialgal-prep-go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=perialgal; numberOfHits, results and pageInfo | context_only | The current exact perialgal query returns zero hits. This is a bounded query result, not an exhaustive absence claim across ontology resources. |
| perialgal-prep-boudreau2025-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1091/mbc.E24-12-0571; Single DOI result bibliographic identity | supports | The exact DOI resolves to Boudreau et al.2025, PMID39937680/PMC12005096, on S.pyriformis cell biology and genome. |
| perialgal-prep-boudreau2025-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/PMC12005096.1.xml; Cell-anatomy, host/symbiont phylogeny and microtubule-basket Results; surface-association Discussion; culture, microscopy, expansion, algal-isolation and phylogeny Methods; Figure3 caption; copyright and licence elements | supports | Beta-tubulin staining and expansion microscopy distinguish irregular cortical meshwork from longitudinal Km fibers. The authors propose cortical retention and physiological benefits; centrifugation is not a selective meshwork perturbation. Host and isolated algal identities are distinguished. |
| perialgal-prep-figure3 | https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/mbc-36-ar44-g003.jpg; Native Figure3 A/B; image bytes unmodified | supports | Visual inspection confirms panelA chlorophyll and beta-tubulin images and panelB six sections through the expanded irregular meshwork. The native image MD5 matches the version1 package. |
| perialgal-prep-paper-pdf | https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/PMC12005096.1.pdf; PDF page6; pdftotext extraction checked against the separately inspected native Figure3 image | supports | PDF page6 contains the Figure3 caption and figure; its caption assigns chlorophyll to left panels and beta-tubulin to right panels inA, with six inward sections inB. The PDF MD5 matches the native package. |
| perialgal-prep-boudreau2025-package | https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC12005096.1.json; Version, identifiers, retraction/licence flags and three relevant file hashes | supports | Version1 metadata has matching DOI and PMID, is not marked retracted, and has null license_code. XML, PDF and Figure3 MD5 values match fetched bytes. The explicit JATS copyright statement grants CC BY4.0 while its licence element is a trademark notice. |
| record | data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml; Entire maintained YAML, including all four discussions and link-only image metadata | context_only | The local identity is PROPOSED. Beta tubulin is the sole, explicitly partial constituent; the positioning function is proposed. No exact protein accession, native paralog inventory, causal graph or hosted image is asserted. |
| schema-result | just validate data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/stentor_perialgal_microtubule_meshwork-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/stentor_perialgal_microtubule_meshwork-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch12-20261021-ipvr425j/stentor_perialgal_microtubule_meshwork-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 5 of 7 collected target identifiers returned OK at the unchanged base. Residuals: PMC12005096.1:F3: SKIPPED; resolved by evidence perialgal-prep-figure3; cellstructuremech:stentor_perialgal_microtubule_meshwork: SKIPPED; resolved by evidence record. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- No selective meshwork perturbation or rescue establishes an anchoring requirement. Physiological benefits remain hypotheses, as the record states.
- Beta-tubulin staining does not identify native paralogs, molecular linkers, full composition, stoichiometry or assembly essentiality.
- The primary sections needed for all maintained claims were read. Unrelated genomic, photosynthesis and phototaxis experiments, supplementary movies and raw data were not independently audited.
- The fresh ontology search is limited to the exact perialgal query. Earlier ignored-inclusive repository and broader authority searches remain historical notes, not newly repeated exhaustive searches.
- The article copyright explicitly grants CC BY4.0; the native structured licence code remains null. The image remains link-only and no hosting guard was changed.
- The separately fetched native Figure3 was visually inspected; PDF page6 caption and official PDF hash were checked. Expanded distances are not treated as native dimensions.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user goal requests saving qualified passes. No finding is invented to justify persistence; no primary article or image bytes are added to the repository.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T084040Z-stentor-perialgal-microtubule-meshwork-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Stentor perialgal microtubule meshwork identity and evidence review
started_at: '2026-10-21T08:24:56Z'
finished_at: '2026-10-21T08:40:40Z'
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
summary: The local structure identity, directly stained beta-tubulin family, host
  taxon, proposed positioning function and link-only image are supported. No concrete
  curation defect was established.
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
  - path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    sha256: 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf
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
- target_id: cellstructuremech:stentor_perialgal_microtubule_meshwork
  path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  label: Stentor perialgal microtubule meshwork
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    role: maintained scientific record
scope:
  description: Entire target; native GO, taxonomy and family authorities; all source
    sections supporting anatomy, taxon boundary, microscopy and proposed positioning;
    native Figure3 visual inspection and PDF page6 caption.
  selection: Fourth unreviewed target in batch twelve, selected in repository path
    order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just validate data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just validate-strict data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/stentor_perialgal_microtubule_meshwork-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: 5 identifiers OK; 2 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
  - record
  - perialgal-prep-figure3
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: The target is a physical cytoskeletal architecture and a qualified anatomical-function
    hypothesis, without an expression-module mechanism.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - perialgal-prep-go
  - perialgal-prep-tax-2721102
  - perialgal-prep-IPR002453
  - perialgal-prep-go-search
  - perialgal-prep-boudreau2025-meta
  - perialgal-prep-boudreau2025-jats
  - perialgal-prep-figure3
  - perialgal-prep-paper-pdf
  - perialgal-prep-boudreau2025-package
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:38:12Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1759 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:15Z to
    2026-10-19T07:29:37Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T07:32:39Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:17Z to
    2026-10-19T07:29:45Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE
    and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped
    prefixes are not evidence of resolution. Exact target identifiers are assessed
    separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-19T07:29:18Z to
    2026-10-19T08:04:01Z at 99692a3d5f16a7dcd6db7e3811344c299a977b81. Reused from
    batch1 isolated checkout because this fresh batch12 clone has the same base commit
    and unchanged maintained scientific inputs. This does not scientifically review
    non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: perialgal-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005622,GO:0030863
  locator: Both term definitions and active flags
  accessed_at: '2026-10-21T08:24:46.881484Z'
  support: supports
  summary: 'Both terms are active: GO0005622 is intracellular anatomical structure
    and GO0030863 is the cortical cytoskeleton beneath the plasma membrane. They provide
    a broad parent and encompassing framework, respectively.'
  snapshot_sha256: a51dafa11e7eafbaa411cc1af78225229343863c98b30dd927d782676aff3bdd
- evidence_id: perialgal-prep-tax-2721102
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2721102
  locator: taxId, scientificName, rank and lineage
  accessed_at: '2026-10-21T08:24:46.896549Z'
  support: supports
  summary: Taxon2721102 is Stentor pyriformis at species rank, in Stentoridae/Heterotrichida.
  snapshot_sha256: cd3ca9f2bf6dc5cac38dc284b5275956c14cec0141ffb8c951383c90db5bd928
- evidence_id: perialgal-prep-IPR002453
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: Entry accession, family type, name and hierarchy
  accessed_at: '2026-10-21T08:24:46.909543Z'
  support: supports
  summary: IPR002453 is the Beta tubulin family, distinguished from alpha and gamma
    tubulin in the family hierarchy.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: perialgal-prep-go-search
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=perialgal
  locator: numberOfHits, results and pageInfo
  accessed_at: '2026-10-21T08:24:59.390879Z'
  support: context_only
  summary: The current exact perialgal query returns zero hits. This is a bounded
    query result, not an exhaustive absence claim across ontology resources.
  snapshot_sha256: 4f0027cdf6df79bb6d4e90297666e971eb23ca7cfa19fc11fb9c9931fd5f1004
- evidence_id: perialgal-prep-boudreau2025-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1091/mbc.E24-12-0571
  locator: Single DOI result bibliographic identity
  accessed_at: '2026-10-21T08:24:55.600761Z'
  support: supports
  summary: The exact DOI resolves to Boudreau et al.2025, PMID39937680/PMC12005096,
    on S.pyriformis cell biology and genome.
  snapshot_sha256: 8b44bf7372fbacbb6edf6c70ae75263d5d55c63032107f9f40e3e53cec868551
- evidence_id: perialgal-prep-boudreau2025-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/PMC12005096.1.xml
  locator: Cell-anatomy, host/symbiont phylogeny and microtubule-basket Results; surface-association
    Discussion; culture, microscopy, expansion, algal-isolation and phylogeny Methods;
    Figure3 caption; copyright and licence elements
  accessed_at: '2026-10-21T08:24:58.439321Z'
  support: supports
  summary: Beta-tubulin staining and expansion microscopy distinguish irregular cortical
    meshwork from longitudinal Km fibers. The authors propose cortical retention and
    physiological benefits; centrifugation is not a selective meshwork perturbation.
    Host and isolated algal identities are distinguished.
  snapshot_sha256: d574ab2e03930539e6b30484f81004a46dfbf06dbfe787fb6cc9e883fd419794
- evidence_id: perialgal-prep-figure3
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/mbc-36-ar44-g003.jpg
  locator: Native Figure3 A/B; image bytes unmodified
  accessed_at: '2026-10-21T08:25:57.818580Z'
  support: supports
  summary: Visual inspection confirms panelA chlorophyll and beta-tubulin images and
    panelB six sections through the expanded irregular meshwork. The native image
    MD5 matches the version1 package.
  snapshot_sha256: d58c093705a97648409f47c19bd5d6cfd819b9c93d724eeda3210c14aa8563fb
- evidence_id: perialgal-prep-paper-pdf
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC12005096.1/PMC12005096.1.pdf
  locator: PDF page6; pdftotext extraction checked against the separately inspected
    native Figure3 image
  accessed_at: '2026-10-21T08:25:00.013965Z'
  support: supports
  summary: PDF page6 contains the Figure3 caption and figure; its caption assigns
    chlorophyll to left panels and beta-tubulin to right panels inA, with six inward
    sections inB. The PDF MD5 matches the native package.
  snapshot_sha256: 815a397a1a03146c11d70c648df6d9acdb8b2471622f2e28627d18e111d17487
- evidence_id: perialgal-prep-boudreau2025-package
  kind: database
  reference: https://pmc-oa-opendata.s3.amazonaws.com/metadata/PMC12005096.1.json
  locator: Version, identifiers, retraction/licence flags and three relevant file
    hashes
  accessed_at: '2026-10-21T08:24:58.247526Z'
  support: supports
  summary: Version1 metadata has matching DOI and PMID, is not marked retracted, and
    has null license_code. XML, PDF and Figure3 MD5 values match fetched bytes. The
    explicit JATS copyright statement grants CC BY4.0 while its licence element is
    a trademark notice.
  snapshot_sha256: 66e981d2ab672ea0dc47fe7c2b8a51a743100a2554f0e46e3da0b9e921e9a63d
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  locator: Entire maintained YAML, including all four discussions and link-only image
    metadata
  accessed_at: '2026-10-21T08:30:28Z'
  support: context_only
  summary: The local identity is PROPOSED. Beta tubulin is the sole, explicitly partial
    constituent; the positioning function is proposed. No exact protein accession,
    native paralog inventory, causal graph or hosted image is asserted.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:24:58Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml'
  snapshot_sha256: 2222931bf07cc48d27e051ce41f5ad47f4bfb33bea2f0306218b12c3992ab4c2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/stentor_perialgal_microtubule_meshwork-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:24:59Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml\
    \ --out /private/tmp/cellstructure-batch12-20261021-ipvr425j/stentor_perialgal_microtubule_meshwork-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch12-20261021-ipvr425j/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch12-20261021-ipvr425j/stentor_perialgal_microtubule_meshwork-strict.tsv"
  snapshot_sha256: b0eb93e37806bbf006f4c32e65b6039505ba8dfc4649dd27e68b3f06a4227f17
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml;
    exact collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:30:28Z'
  support: supports
  summary: '5 of 7 collected target identifiers returned OK at the unchanged base.
    Residuals: PMC12005096.1:F3: SKIPPED; resolved by evidence perialgal-prep-figure3;
    cellstructuremech:stentor_perialgal_microtubule_meshwork: SKIPPED; resolved by
    evidence record. Source-native identity checked separately.'
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
  topic: Host meshwork versus associated cells and neighboring fibers
  outcome: supported
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: Definition and broad basket synonym preserve an irregular host cortical
    architecture. Symbiotic Chlorella, vacuole membranes, Km bundles and regular one-alga
    cages are excluded. Broad GO hierarchy is consistent with the observed location;
    local identity is not presented as exact GO mapping.
  evidence_ids:
  - perialgal-prep-boudreau2025-jats
  - perialgal-prep-go
  - record
- assessment_id: grounding
  area: grounding
  topic: Directly stained tubulin family
  outcome: supported
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: The beta-tubulin family grounding matches the Sigma T0198 immunofluorescence
    assay and native InterPro family. No specific Stentor paralog, assembly essentiality,
    complete constituent list or linker identity follows from the staining; the record
    retains those limits.
  evidence_ids:
  - perialgal-prep-boudreau2025-jats
  - perialgal-prep-IPR002453
  - record
- assessment_id: taxon
  area: scope
  topic: Directly imaged host and separate algal symbiont
  outcome: supported
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: The host species name and taxonomy agree. Morphological and18S characterization,
    together with isolation and separate culture of the algae, support keeping host
    cytoskeleton distinct from symbiont identity and organelle fixation. No genus-wide
    distribution or absence inference is asserted.
  evidence_ids:
  - perialgal-prep-boudreau2025-jats
  - perialgal-prep-tax-2721102
  - record
- assessment_id: function
  area: evidence
  topic: Association and proposed cortical retention
  outcome: supported
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: Spatial association and recovery after bulk centrifugation support a hypothesis
    of cortical retention. They do not establish a selective requirement of this meshwork
    for anchoring, phototaxis, photosynthetic gain or gas exchange. The qualified
    function and explicit open discussion accurately preserve this distinction.
  evidence_ids:
  - perialgal-prep-boudreau2025-jats
  - record
- assessment_id: image
  area: provenance
  topic: Exact figure, source anchor and licence caveat
  outcome: supported
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: The image caption, source accession F3, PDF page6 anchor, species, attribution
    and link-only status agree with the source. CC BY4.0 follows the explicit copyright
    statement; the record correctly preserves the null metadata field and hosting
    guard. Expanded-image distances are not promoted to native measurements.
  evidence_ids:
  - perialgal-prep-boudreau2025-jats
  - perialgal-prep-figure3
  - perialgal-prep-paper-pdf
  - perialgal-prep-boudreau2025-package
  - record
- assessment_id: completeness
  area: completeness
  topic: Open inventory and experimental gaps
  outcome: supported
  target_ids:
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  summary: The partial composition and lack of causal graph are appropriate to current
    evidence. Selective disruption/rescue, attachment proteins, native paralogs, stoichiometry
    and assembly requirements remain open. Historical searches are not represented
    as newly exhaustive queries; the fresh perialgal search is bounded.
  evidence_ids:
  - perialgal-prep-boudreau2025-jats
  - perialgal-prep-go-search
  - record
findings: []
actions: []
limitations:
- No selective meshwork perturbation or rescue establishes an anchoring requirement.
  Physiological benefits remain hypotheses, as the record states.
- Beta-tubulin staining does not identify native paralogs, molecular linkers, full
  composition, stoichiometry or assembly essentiality.
- The primary sections needed for all maintained claims were read. Unrelated genomic,
  photosynthesis and phototaxis experiments, supplementary movies and raw data were
  not independently audited.
- The fresh ontology search is limited to the exact perialgal query. Earlier ignored-inclusive
  repository and broader authority searches remain historical notes, not newly repeated
  exhaustive searches.
- The article copyright explicitly grants CC BY4.0; the native structured licence
  code remains null. The image remains link-only and no hosting guard was changed.
- The separately fetched native Figure3 was visually inspected; PDF page6 caption
  and official PDF hash were checked. Expanded distances are not treated as native
  dimensions.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The user goal requests saving qualified passes. No finding is invented to justify
  persistence; no primary article or image bytes are added to the repository.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
