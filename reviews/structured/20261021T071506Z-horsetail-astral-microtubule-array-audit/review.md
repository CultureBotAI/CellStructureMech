# Horsetail astral array mechanism, image and protein-example review

- Review: 20261021T071506Z-horsetail-astral-microtubule-array-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T07:13:42Z
- Finished UTC: 2026-10-21T07:15:06Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Array identity, bounded mechanism, taxa, native identifiers and unchanged licensed figure are supported. Two minor inconsistencies remain in protein-example provenance prose.

## Scope And Provenance

Entire single target; all native identities; full relevant2012 main text, supplemental strain/method passages, complete Figure4 visual inspection and2005 abstract.

Selection: Fourth unreviewed path in batch seven, in repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0032117 | data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml | maintained | horsetail-astral microtubule array |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0032117 | Focused validator passed. |
| Focused native strict | passed | True | GO:0032117 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0032117 | 14 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0032117 | No expression-module or transcriptional-regulator assertion is used; the graph concerns physical organization. |
| Claim-level scientific review | passed | True | GO:0032117 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0032117 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0032117 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0032117 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0032117 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0032117 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Whole array and organizer boundary

identity: supported. Targets: GO:0032117.

Exact GO identity, hierarchy and parthood are supported. The whole array is distinct from an individual filament, the SPB core, the organizing center and the later spindle.

### Tubulin classes and sequence identity

grounding: concern. Targets: GO:0032117.

The alpha/beta family assignments and all three native accession identities are correct. Atb2 has direct imaging support; Nda2 and Nda3 examples explicitly supply sequence identity only. Their surrounding provenance prose needs reconciliation.

### Experimental and reference strains

scope: supported. Targets: GO:0032117.

The example correctly separates homothallic live imaging from synchronized engineered diploid ultrastructure and from the reference-sequence strain.

### Hrs1-dependent radial organization

graph: supported. Targets: GO:0032117.

The six edges preserve polymer composition and the organizing-center context. The record does not infer a purified physical bridge, universal copy counts, direct recombination outcomes or complete meiotic arrest.

### Image identity, licence and interpretation

provenance: supported. Targets: GO:0032117.

Tracked and fresh image hashes match; JATS explicitly states CC BY3.0. The complete multipanel figure and source caption support the fluorescence interpretation while identifying non-image panels separately.

## Findings

### F1: Nda2 example describes an undeclared component gene

minor / open / confirmed; issue key: horsetail-array-nda2-declared-symbol-provenance.

The P04688 role says its gene is declared on the component, but the alpha component lists only tub1, atb2 and alp2. Native UniProt establishes nda2 as a separate alpha-1 gene, not an alias of those names. This is a false description of the local gene list, not a wrong accession or demonstrated membership failure.

### F2: Nda3 withholding rationale conflicts with the present example

minor / open / confirmed; issue key: horsetail-array-nda3-stale-withholding-rationale.

The composition_limits discussion says an Nda3 example is not justified without an isoform-specific experiment, yet the beta component now contains a deliberately identity-only Nda3 example. Reconcile the record’s eligibility explanation; the new example does not itself claim an isoform-specific HAA experiment.

## Recommended Actions And Acceptance Checks

### A1

Reconcile the Nda2 example role with the actual declared-symbol scope; retain the explicit identity-only limitation.

- Do not present nda2 as an alias of tub1/atb2/alp2.
- Any expanded component gene declaration has appropriate class and taxon evidence.
- Run native schema, strict, label, history and generated-page checks after separately authorized curation.

### A2

Update the composition limitation to distinguish a reference-sequence example from experimentally established isoform membership, preserving the latter uncertainty.

- The discussion and existing Nda3 example state compatible evidence requirements.
- No new experimental localization or essentiality claim is implied by the accession.
- Run native schema, strict, label, history and generated-page checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| horsetail-prep-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032117%2CGO%3A0005818%2CGO%3A0030981%2CGO%3A0030989%2CGO%3A0005874; All five returned terms; definitions and parent-term child edges | supports | Native GO verifies the exact HAA identity and synonym, aster parent, cortical microtubule cytoskeleton parthood, microtubule polymer definition and dynein-driven meiotic movement function. |
| horsetail-prep-alpha-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452; metadata accession, name, type and family hierarchy | supports | IPR002452 is the Alpha tubulin family. |
| horsetail-prep-beta-family | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453; metadata accession, name, type and family hierarchy | supports | IPR002453 is the Beta tubulin family. |
| horsetail-prep-taxon-4896 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896; taxId, scientificName and rank | supports | ENA verifies species Schizosaccharomyces pombe. |
| horsetail-prep-taxon-284812 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812; taxId, scientificName and rank | supports | ENA verifies reference strain Schizosaccharomyces pombe 972h-. |
| horsetail-prep-proteins | https://rest.uniprot.org/uniprotkb/search?query=(accession:P04689%20OR%20accession:P04688%20OR%20accession:P05219)&amp;format=json; All three accessions: entry status, recommended name, genes and organism | supports | Reviewed P04689 is tub1 with atb2/alp2 aliases; P04688 is the distinct nda2 alpha-1 gene; P05219 is nda3 beta tubulin. All three are reference-strain taxon 284812 identities, not proof of experimental-array membership. |
| horsetail-prep-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22425159%20OR%20EXT_ID:16111942&amp;format=json&amp;resultType=core; PMID22425159 and PMID16111942 bibliographic entries; 2005 abstract | supports | Native metadata verifies both cited DOI/PMID pairs. The complete readable 2005 abstract supports Hrs1-dependent array formation and nuclear motion, with ectopic HAA-like arrays distinguished from normal meiosis. |
| horsetail-prep-paper | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml; Full Introduction, Results, Discussion and Methods; Figure2 and Figure4 captions; JATS licence | supports | The 2012 body supports Hrs1-dependent rMTOC organization near the SPB, radial minus-end arrangement, loss of normal radial geometry after deletion, and regulated dissolution at meiosis I. It distinguishes residual microtubules from a normal array and proposed molecular bridging from demonstrated sufficiency. |
| horsetail-prep-supplement | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/mmc1.pdf; Supplement TableS1 p13 and experimental methods pp18–21; text inspected, no additional panel interpretation | supports | Table S1 identifies Figure4A strain KT2901 and separate engineered diploid EM strains. Methods specify high-pressure freezing, freeze substitution and resin sections; immunolabel timing says120min, unlike main-text80min. |
| horsetail-prep-figure4 | https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/gr4.jpg; Complete Figure4 image; compared with target caption and primary caption | supports | The retrieved complete Figure4 bytes match the tracked image and declared SHA256. Root visually inspected panels A–G: fluorescence time courses and distinct plots, blots and phosphorylation schematic match the caption. |
| record | data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml; Entire target including components, graphs, discussions and image metadata | context_only | The target has a bounded class-level polymer inventory, explicit experimental/reference strain distinctions and six source-bounded assembly edges. Two later protein examples coexist with older curation prose. |
| policy | docs/CURATION.md; Components and protein examples | context_only | Component class grounding and taxon-paired sequence examples have separate scopes; an accession identity alone is not experimental membership evidence. |
| schema-result | just validate data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/horsetail_astral_microtubule_array-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/horsetail_astral_microtubule_array-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch7-20261021-dz9x5cv0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/horsetail_astral_microtubule_array-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml; exact collect() scope; snapshot hash identifies the full original resolver TSV, not the extracted target slice | supports | 14 of14 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The2005 paper is assessed only through its complete readable abstract, not inaccessible full text or supplements.
- Movies, raw tomography data and most supplemental figure panels were not inspected; no quantitative reanalysis or reproduction was performed.
- Native sequence identity does not establish isoform-specific array membership. The exact inventory and physical nucleation/attachment mechanism remain explicitly unresolved.
- The primary source’s80min versus120min immunolabel timing conflict is retained as a limitation, not silently reconciled.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Source collaborator prepared native receipts; root read the entire target after native inspection and directly inspected the main body, relevant supplemental text and tracked figure.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T071506Z-horsetail-astral-microtubule-array-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Horsetail astral array mechanism, image and protein-example review
started_at: '2026-10-21T07:13:42Z'
finished_at: '2026-10-21T07:15:06Z'
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
summary: Array identity, bounded mechanism, taxa, native identifiers and unchanged
  licensed figure are supported. Two minor inconsistencies remain in protein-example
  provenance prose.
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
  - path: data/images/cytoskeleton/horsetail_astral_microtubule_array/pmc3382715_fig4.jpg
    sha256: 6a3cdc8e95796f27389e7bace40a6d68c1f30b810edf9a2bd9bc11dd17b2516c
    role: context
  - path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    sha256: 73abc8f115d095e86ee315409c2221a5a97b37fad16effdb8593c6b9655568de
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
- target_id: GO:0032117
  path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
  label: horsetail-astral microtubule array
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    role: maintained scientific record
scope:
  description: Entire single target; all native identities; full relevant2012 main
    text, supplemental strain/method passages, complete Figure4 visual inspection
    and2005 abstract.
  selection: Fourth unreviewed path in batch seven, in repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0032117
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0032117
  command: just validate data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0032117
  command: just validate-strict data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/horsetail_astral_microtubule_array-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0032117
  summary: 14 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0032117
  summary: No expression-module or transcriptional-regulator assertion is used; the
    graph concerns physical organization.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0032117
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - horsetail-prep-go
  - horsetail-prep-alpha-family
  - horsetail-prep-beta-family
  - horsetail-prep-taxon-4896
  - horsetail-prep-taxon-284812
  - horsetail-prep-proteins
  - horsetail-prep-epmc
  - horsetail-prep-paper
  - horsetail-prep-supplement
  - horsetail-prep-figure4
  - record
  - policy
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0032117
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
  - GO:0032117
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
  - GO:0032117
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
  - GO:0032117
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
  - GO:0032117
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
- evidence_id: horsetail-prep-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032117%2CGO%3A0005818%2CGO%3A0030981%2CGO%3A0030989%2CGO%3A0005874
  locator: All five returned terms; definitions and parent-term child edges
  accessed_at: '2026-10-21T07:08:04.056058Z'
  support: supports
  summary: Native GO verifies the exact HAA identity and synonym, aster parent, cortical
    microtubule cytoskeleton parthood, microtubule polymer definition and dynein-driven
    meiotic movement function.
  snapshot_sha256: babdfe397ac3a6e390fc580966790495926325a54192e57215af82d99b93ab5f
- evidence_id: horsetail-prep-alpha-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452
  locator: metadata accession, name, type and family hierarchy
  accessed_at: '2026-10-21T07:08:04.089955Z'
  support: supports
  summary: IPR002452 is the Alpha tubulin family.
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
- evidence_id: horsetail-prep-beta-family
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453
  locator: metadata accession, name, type and family hierarchy
  accessed_at: '2026-10-21T07:08:04.085613Z'
  support: supports
  summary: IPR002453 is the Beta tubulin family.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: horsetail-prep-taxon-4896
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4896
  locator: taxId, scientificName and rank
  accessed_at: '2026-10-21T07:08:04.067112Z'
  support: supports
  summary: ENA verifies species Schizosaccharomyces pombe.
  snapshot_sha256: 42c5b7d3d99341137803612d6404cd3884e2d06ec8a740b1ad38163c678f6721
- evidence_id: horsetail-prep-taxon-284812
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/284812
  locator: taxId, scientificName and rank
  accessed_at: '2026-10-21T07:08:04.060512Z'
  support: supports
  summary: ENA verifies reference strain Schizosaccharomyces pombe 972h-.
  snapshot_sha256: 948c040cabf6c036dff451c7b6eac22605d0ed5d60a74f471e4431e63f82f721
- evidence_id: horsetail-prep-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=(accession:P04689%20OR%20accession:P04688%20OR%20accession:P05219)&format=json
  locator: 'All three accessions: entry status, recommended name, genes and organism'
  accessed_at: '2026-10-21T07:08:04.359288Z'
  support: supports
  summary: Reviewed P04689 is tub1 with atb2/alp2 aliases; P04688 is the distinct
    nda2 alpha-1 gene; P05219 is nda3 beta tubulin. All three are reference-strain
    taxon 284812 identities, not proof of experimental-array membership.
  snapshot_sha256: c788c6b01cefc6e248e3134f3d2a76c82dcd2653c1528bd7543ce3d6f973df22
- evidence_id: horsetail-prep-epmc
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID:22425159%20OR%20EXT_ID:16111942&format=json&resultType=core
  locator: PMID22425159 and PMID16111942 bibliographic entries; 2005 abstract
  accessed_at: '2026-10-21T07:08:04.154152Z'
  support: supports
  summary: Native metadata verifies both cited DOI/PMID pairs. The complete readable
    2005 abstract supports Hrs1-dependent array formation and nuclear motion, with
    ectopic HAA-like arrays distinguished from normal meiosis.
  snapshot_sha256: ee742075d85f9a68e32896cf1396fe5d0dfe201ab5785abdd883d7fd31bbe59a
- evidence_id: horsetail-prep-paper
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/PMC3382715.1.xml
  locator: Full Introduction, Results, Discussion and Methods; Figure2 and Figure4
    captions; JATS licence
  accessed_at: '2026-10-21T07:08:03.849693Z'
  support: supports
  summary: The 2012 body supports Hrs1-dependent rMTOC organization near the SPB,
    radial minus-end arrangement, loss of normal radial geometry after deletion, and
    regulated dissolution at meiosis I. It distinguishes residual microtubules from
    a normal array and proposed molecular bridging from demonstrated sufficiency.
  snapshot_sha256: 59f662c998abf622fbb9bccbabc3867cb5ffd3174943cc52cb6228b1e35cd93d
- evidence_id: horsetail-prep-supplement
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/mmc1.pdf
  locator: Supplement TableS1 p13 and experimental methods pp18–21; text inspected,
    no additional panel interpretation
  accessed_at: '2026-10-21T07:08:38.276610Z'
  support: supports
  summary: Table S1 identifies Figure4A strain KT2901 and separate engineered diploid
    EM strains. Methods specify high-pressure freezing, freeze substitution and resin
    sections; immunolabel timing says120min, unlike main-text80min.
  snapshot_sha256: 6dde9cc7999b0e3294aa95f3d3036a319c90b9390920d84bd7194c883dc213f9
- evidence_id: horsetail-prep-figure4
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC3382715.1/gr4.jpg
  locator: Complete Figure4 image; compared with target caption and primary caption
  accessed_at: '2026-10-21T07:08:38.011986Z'
  support: supports
  summary: 'The retrieved complete Figure4 bytes match the tracked image and declared
    SHA256. Root visually inspected panels A–G: fluorescence time courses and distinct
    plots, blots and phosphorylation schematic match the caption.'
  snapshot_sha256: 6a3cdc8e95796f27389e7bace40a6d68c1f30b810edf9a2bd9bc11dd17b2516c
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
  locator: Entire target including components, graphs, discussions and image metadata
  accessed_at: '2026-10-21T07:15:06Z'
  support: context_only
  summary: The target has a bounded class-level polymer inventory, explicit experimental/reference
    strain distinctions and six source-bounded assembly edges. Two later protein examples
    coexist with older curation prose.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Components and protein examples
  accessed_at: '2026-10-21T07:15:06Z'
  support: context_only
  summary: Component class grounding and taxon-paired sequence examples have separate
    scopes; an accession identity alone is not experimental membership evidence.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:13:44Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml'
  snapshot_sha256: 842dc104088e7528837638d4f36413562284f494aa94af9f3184d0711db00895
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/horsetail_astral_microtubule_array-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T07:13:46Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml\
    \ --out /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/horsetail_astral_microtubule_array-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch7-20261021-dz9x5cv0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch7-20261021-dz9x5cv0/horsetail_astral_microtubule_array-strict.tsv"
  snapshot_sha256: b81d8d8e9b4f2fb05bd90dce0e0cf82cc05437bde7a750d9c0c04cb8466fb7ed
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml; exact
    collect() scope; snapshot hash identifies the full original resolver TSV, not
    the extracted target slice
  accessed_at: '2026-10-21T07:15:06Z'
  support: supports
  summary: '14 of14 collected target identifiers returned OK at the unchanged base.
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
  topic: Whole array and organizer boundary
  outcome: supported
  target_ids:
  - GO:0032117
  summary: Exact GO identity, hierarchy and parthood are supported. The whole array
    is distinct from an individual filament, the SPB core, the organizing center and
    the later spindle.
  evidence_ids:
  - horsetail-prep-go
  - horsetail-prep-paper
  - record
- assessment_id: composition
  area: grounding
  topic: Tubulin classes and sequence identity
  outcome: concern
  target_ids:
  - GO:0032117
  summary: The alpha/beta family assignments and all three native accession identities
    are correct. Atb2 has direct imaging support; Nda2 and Nda3 examples explicitly
    supply sequence identity only. Their surrounding provenance prose needs reconciliation.
  evidence_ids:
  - horsetail-prep-alpha-family
  - horsetail-prep-beta-family
  - horsetail-prep-proteins
  - horsetail-prep-paper
  - record
- assessment_id: scope
  area: scope
  topic: Experimental and reference strains
  outcome: supported
  target_ids:
  - GO:0032117
  summary: The example correctly separates homothallic live imaging from synchronized
    engineered diploid ultrastructure and from the reference-sequence strain.
  evidence_ids:
  - horsetail-prep-taxon-4896
  - horsetail-prep-taxon-284812
  - horsetail-prep-supplement
  - horsetail-prep-paper
- assessment_id: mechanism
  area: graph
  topic: Hrs1-dependent radial organization
  outcome: supported
  target_ids:
  - GO:0032117
  summary: The six edges preserve polymer composition and the organizing-center context.
    The record does not infer a purified physical bridge, universal copy counts, direct
    recombination outcomes or complete meiotic arrest.
  evidence_ids:
  - horsetail-prep-go
  - horsetail-prep-epmc
  - horsetail-prep-paper
  - record
- assessment_id: figure
  area: provenance
  topic: Image identity, licence and interpretation
  outcome: supported
  target_ids:
  - GO:0032117
  summary: Tracked and fresh image hashes match; JATS explicitly states CC BY3.0.
    The complete multipanel figure and source caption support the fluorescence interpretation
    while identifying non-image panels separately.
  evidence_ids:
  - horsetail-prep-figure4
  - horsetail-prep-paper
  - horsetail-prep-supplement
  - record
findings:
- finding_id: F1
  issue_key: horsetail-array-nda2-declared-symbol-provenance
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Nda2 example describes an undeclared component gene
  description: The P04688 role says its gene is declared on the component, but the
    alpha component lists only tub1, atb2 and alp2. Native UniProt establishes nda2
    as a separate alpha-1 gene, not an alias of those names. This is a false description
    of the local gene list, not a wrong accession or demonstrated membership failure.
  target_ids:
  - GO:0032117
  field_paths:
  - components[component_id=alpha_tubulin].gene_symbols
  - components[component_id=alpha_tubulin].protein_examples[uniprot_id=UniProtKB:P04688].role
  evidence_ids:
  - horsetail-prep-proteins
  - record
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Bounded provenance inconsistency; native protein identity
    and assembly identity remain supported.
- finding_id: F2
  issue_key: horsetail-array-nda3-stale-withholding-rationale
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Nda3 withholding rationale conflicts with the present example
  description: The composition_limits discussion says an Nda3 example is not justified
    without an isoform-specific experiment, yet the beta component now contains a
    deliberately identity-only Nda3 example. Reconcile the record’s eligibility explanation;
    the new example does not itself claim an isoform-specific HAA experiment.
  target_ids:
  - GO:0032117
  field_paths:
  - discussions[discussion_id=composition_limits].rationale
  - components[component_id=beta_tubulin].protein_examples
  evidence_ids:
  - horsetail-prep-proteins
  - record
  - policy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:Components
  native_severity: minor
  normalization_reason: Bounded provenance inconsistency; native protein identity
    and assembly identity remain supported.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0032117
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    role: maintained scientific record
  description: Reconcile the Nda2 example role with the actual declared-symbol scope;
    retain the explicit identity-only limitation.
  acceptance_checks:
  - Do not present nda2 as an alias of tub1/atb2/alp2.
  - Any expanded component gene declaration has appropriate class and taxon evidence.
  - Run native schema, strict, label, history and generated-page checks after separately
    authorized curation.
  generator: Maintained structure YAML; just render derives pages.
- action_id: A2
  finding_ids:
  - F2
  target_ids:
  - GO:0032117
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    role: maintained scientific record
  description: Update the composition limitation to distinguish a reference-sequence
    example from experimentally established isoform membership, preserving the latter
    uncertainty.
  acceptance_checks:
  - The discussion and existing Nda3 example state compatible evidence requirements.
  - No new experimental localization or essentiality claim is implied by the accession.
  - Run native schema, strict, label, history and generated-page checks after separately
    authorized curation.
  generator: Maintained structure YAML; just render derives pages.
limitations:
- The2005 paper is assessed only through its complete readable abstract, not inaccessible
  full text or supplements.
- Movies, raw tomography data and most supplemental figure panels were not inspected;
  no quantitative reanalysis or reproduction was performed.
- Native sequence identity does not establish isoform-specific array membership. The
  exact inventory and physical nucleation/attachment mechanism remain explicitly unresolved.
- The primary source’s80min versus120min immunolabel timing conflict is retained as
  a limitation, not silently reconciled.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- Source collaborator prepared native receipts; root read the entire target after
  native inspection and directly inspected the main body, relevant supplemental text
  and tracked figure.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
