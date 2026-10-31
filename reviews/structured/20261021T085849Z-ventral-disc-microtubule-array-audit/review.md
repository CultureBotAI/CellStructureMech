# Giardia ventral-disc microtubule scaffold and molecular-scope review

- Review: 20261021T085849Z-ventral-disc-microtubule-array-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T08:41:01Z
- Finished UTC: 2026-10-21T08:58:49Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The exact array identity, alpha/beta polymer scaffold, disc parthood and nonmechanistic graph are supported. Molecular density assignments and combined-family granularity remain explicitly unresolved. No concrete curation issue was established.

## Scope And Provenance

Entire target including all synonyms, hierarchy, component and graph claims; exact native GO/taxon/family candidates and primary3D structural/method evidence, with earlier source-specific handedness context.

Selection: Second selected target in batch thirteen, fixed repository path order.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097593 | data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml | maintained | ventral disc microtubule array |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097593 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097593 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0097593 | 6 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0097593 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0097593 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097593 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097593 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097593 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0097593 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Array identity and constituent microtubules

identity: supported. Targets: GO:0097593.

Exact GO identity, three synonym scopes, definition and filament-based nature agree. The array is an assembly of microtubules, not the generic protein tubulin, a single microribbon, the separate supernumerary fragment or the whole disc.

### Disc parthood, microtubule parts and microribbon base

scope: supported. Targets: GO:0097593.

Native GO supplies direct disc parthood; the definition and primary tomography support has_part GO:0005874 and the microribbon-base relationship. The array can contain microtubules without treating microtubule and array as synonyms or importing microribbon proteins into the tubulin component.

### Alpha/beta cohort and family granularity

grounding: supported. Targets: GO:0097593.

The alpha/beta polymer component is supported by native GO and the primary lattice analysis. Separately exact alpha and beta family entries are available, while IPR000217 is broader than the combined class. No one exact combined-class grounding was established by the inspected candidates; the acknowledged label-only cohort is defensible. Splitting into optional rows is not automatically required, and historical wording is not a claim that neither family exists.

### Species aliases and preparation

scope: supported. Targets: GO:0097593.

Giardia intestinalis, G.lamblia and native preferred G.duodenalis denote species5741. WBC6 trophozoites supply the experimental example. COMMON is qualitative characterized-species occurrence, without a numerical prevalence or universal stage/strain claim.

### Structural function and source-specific geometry

evidence: supported. Targets: GO:0097593.

Spiral microtubules form the scaffold and microribbon base as claimed. Schwartz2012 explicitly supports the target’s left-handed description; an opposite earlier background description is preserved as an unresolved source convention/discrepancy, not silently harmonized. No independent chirality reanalysis or force-generation assay is claimed.

### Three nonmechanistic structural edges

graph: supported. Targets: GO:0097593.

The component_ref is local and valid. Alpha/beta subunits make up the microtubule array, the array forms the microribbon base, and it is part of the disc. ASSEMBLY/NONMECHANISTIC avoids a temporal assembly order, recruitment cascade or a reconstituted Giardia polymerization pathway; the primary paper supplies static structure and native GO supplies generic polymer composition.

### Unassigned wall and interface densities

completeness: supported. Targets: GO:0097593.

The paper maps gMIPs, gMAPs, side-arms, paddles and an intra-complex bridge while noting that a named density may contain multiple proteins. The existing TODO properly preserves those unresolved boundaries and does not assign particular giardins or family CURIEs from morphology. Empty finer inventory is not automatically a defect.

### Native context versus extracted high-resolution map

scope: supported. Targets: GO:0097593.

Whole-cell and resin-section tomography provide the overall disc geometry; the high-resolution cryo-ET grand average used extracted, flattened discs, selected five tomograms from four discs and excluded overlap/extreme-peripheral regions. The record does not universalize the average into a full-disc molecular map or assert measured mechanical stiffness.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml; Entire maintained YAML, all fields, graph edges and discussions | context_only | Complete target read; historical curation notes and native PROPOSED status remain unchanged. |
| policy | docs/record-review-profile.md; Governing review profile, checklist, evidence skill and schema captured by native inspect | context_only | Assess exact component/structure identity and evidential scope; optional inventories, images or protein examples are not automatic requirements. |
| disc-mt-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097593,GO:0097594,GO:0097597,GO:0005874; Complete four native results, all synonym scopes/status/definitions and parent children relations; has_part microtubule is assessed from definition/primary structure, not an invented native edge. | supports | Active GO:0097593 exactly defines the spiral microtubule array and microribbon base. GO:0097597 lists it as part_of; GO:0005874 defines polymeric alpha/beta tubulin microtubules; GO:0097594 defines the distinct microribbon. |
| disc-mt-agent-tax-5741 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741; Complete native taxon5741 result: scientificName, otherNames, rank and lineage; original receipt reused unchanged. | supports | Native species5741 is currently Giardia duodenalis, with Giardia intestinalis and Giardia lamblia explicitly included as synonyms. Species nomenclature is consistent with the target; experimental strain/stage are supplied by primary Methods. |
| disc-mt-agent-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.pone.0043783%22; Exact DOI/title/authors/year/PMID/PMC identity in native metadata. | supports | Exact cited DOI resolves to Schwartz, Heumann, Dawson and Hoenger2012, PMID22984443/PMC3439489. |
| disc-mt-agent-schwartz2012-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3439489/fullTextXML; Principal locators s2a (left-handed spiral and overlap), s2c–s2g (polarity, lattice, densities), s2h microribbon interface, Table1, s3a–s3c interpretation, s5 Methods; Native JATS PMC3439489: Introduction and Results s2a–s2h, Discussion s3a–s3e, Conclusions s4 and Methods s5a–s5f read across the unchanged batch12/13 snapshot; principal locators specified in summary. Claim-bearing captions/Table1 read; no figure pixels, videos or raw tomography reanalysis. | supports | Primary whole-cell/plastic-section tomography resolves a left-handed ventral-disc spiral and microribbons; isolated-disc cryo-ET resolves13-protofilament microtubules, alpha/beta lattice organization and associated unassigned densities. The paper does not identify molecular compositions of gMIP/gMAP/side-arm/paddle/bridge structures. |
| disc-mt-agent-IPR002452 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/; metadata accession/type/name, description and complete returned family hierarchy. | supports | Native IPR002452 is the Alpha tubulin family. It matches the alpha subset, not by itself the combined alpha-and-beta component class. |
| disc-mt-agent-IPR002453 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/; metadata accession/type/name, description and complete returned family hierarchy. | supports | Native IPR002453 is the Beta tubulin family. It matches the beta subset, not by itself the combined alpha-and-beta component class. |
| disc-mt-agent-IPR000217 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/; metadata accession/type/name, description and family hierarchy. | supports | Native IPR000217 is the broader Tubulin family with alpha, beta, gamma, delta, epsilon and zeta children; it does not exactly denote only the asserted alpha/beta pair. |
| disc-mt-agent-hagen2011-jats | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3243723/fullTextXML; Introduction paragraphs describing primary disc elements and supernumerary MTs; compared with Schwartz2012 s2a. Original primary-body receipt reused, but this background architectural claim is treated as secondary context. | context_only | The earlier paper’s Introduction uses right-handed for the main disc spiral and left-handed for the supernumerary array, opposite to Schwartz2012. This is a background account, not a new chirality measurement in the reviewed localization study; the discrepancy is retained without substituting it for the later cited3D study. |
| schema-result | just validate data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/ventral_disc_microtubule_array-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/ventral_disc_microtubule_array-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/ventral_disc_microtubule_array-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 6 of6 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The paper’s main Introduction/Results/Discussion/Conclusions/Methods and claim-bearing captions/Table1 were read from the same exact native JATS across batches12–13. Figure pixels, raw tomograms, videos and all supplements were not reanalyzed.
- The2012 left-handed main spiral is directly source-supported. Hagen2011 background prose uses the opposite main/supernumerary handedness labels; viewing-convention or historical correction was not independently resolved, and no new chirality measurement is claimed.
- The inspected native family entries cover alpha, beta and the broad tubulin family; this is not an exhaustive search for every possible combined-class identifier. Separate family availability does not itself require changing the existing component granularity.
- High-resolution densities describe an extracted-disc selected-region average, not every disc region, live assembly dynamics or exact molecular stoichiometry. gMIP/gMAP/side-arm/paddle/bridge protein identities remain unassigned in the cited source.
- No gene-specific accession, purified-protein reconstitution, universal essentiality, cyst-stage presence or numerical species prevalence is inferred.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- All12 native input hashes verified after inspect/schema/strict0. External snapshots retain actual original access times; no neighboring maintained YAML was needed.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261021T085849Z-ventral-disc-microtubule-array-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Giardia ventral-disc microtubule scaffold and molecular-scope review
started_at: '2026-10-21T08:41:01Z'
finished_at: '2026-10-21T08:58:49Z'
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
summary: The exact array identity, alpha/beta polymer scaffold, disc parthood and
  nonmechanistic graph are supported. Molecular density assignments and combined-family
  granularity remain explicitly unresolved. No concrete curation issue was established.
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
  - path: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
    sha256: 184540d5a0f41b8f04fa8e4cac937dc657481eaa999e5420ec315476801a07e3
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
- target_id: GO:0097593
  path: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
  label: ventral disc microtubule array
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
    role: maintained scientific record
scope:
  description: Entire target including all synonyms, hierarchy, component and graph
    claims; exact native GO/taxon/family candidates and primary3D structural/method
    evidence, with earlier source-specific handedness context.
  selection: Second selected target in batch thirteen, fixed repository path order.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097593
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097593
  command: just validate data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097593
  command: just validate-strict data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/ventral_disc_microtubule_array-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0097593
  summary: 6 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097593
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - disc-mt-agent-go
  - disc-mt-agent-tax-5741
  - disc-mt-agent-epmc
  - disc-mt-agent-schwartz2012-jats
  - disc-mt-agent-IPR002452
  - disc-mt-agent-IPR002453
  - disc-mt-agent-IPR000217
  - disc-mt-agent-hagen2011-jats
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097593
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
  - GO:0097593
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
  - GO:0097593
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
  - GO:0097593
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
  - GO:0097593
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
  reference: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
  locator: Entire maintained YAML, all fields, graph edges and discussions
  accessed_at: '2026-10-21T08:46:04Z'
  support: context_only
  summary: Complete target read; historical curation notes and native PROPOSED status
    remain unchanged.
- evidence_id: policy
  kind: record_content
  reference: docs/record-review-profile.md
  locator: Governing review profile, checklist, evidence skill and schema captured
    by native inspect
  accessed_at: '2026-10-21T08:46:04Z'
  support: context_only
  summary: Assess exact component/structure identity and evidential scope; optional
    inventories, images or protein examples are not automatic requirements.
- evidence_id: disc-mt-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097593,GO:0097594,GO:0097597,GO:0005874
  locator: Complete four native results, all synonym scopes/status/definitions and
    parent children relations; has_part microtubule is assessed from definition/primary
    structure, not an invented native edge.
  accessed_at: '2026-10-21T08:41:38.205951Z'
  support: supports
  summary: Active GO:0097593 exactly defines the spiral microtubule array and microribbon
    base. GO:0097597 lists it as part_of; GO:0005874 defines polymeric alpha/beta
    tubulin microtubules; GO:0097594 defines the distinct microribbon.
  snapshot_sha256: 3cc5a64324a5c78b42578653e338882a9e7fd7065a947abdd45c35bd5e9dd82b
- evidence_id: disc-mt-agent-tax-5741
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5741
  locator: 'Complete native taxon5741 result: scientificName, otherNames, rank and
    lineage; original receipt reused unchanged.'
  accessed_at: '2026-10-21T08:25:56.730800Z'
  support: supports
  summary: Native species5741 is currently Giardia duodenalis, with Giardia intestinalis
    and Giardia lamblia explicitly included as synonyms. Species nomenclature is consistent
    with the target; experimental strain/stage are supplied by primary Methods.
  snapshot_sha256: 1dcdc380972a71a0a24c80755d8bbacdcb0b6d9988bb5fb1e05ba43f50580dd3
- evidence_id: disc-mt-agent-epmc
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.pone.0043783%22
  locator: Exact DOI/title/authors/year/PMID/PMC identity in native metadata.
  accessed_at: '2026-10-21T08:25:57.030288Z'
  support: supports
  summary: Exact cited DOI resolves to Schwartz, Heumann, Dawson and Hoenger2012,
    PMID22984443/PMC3439489.
  snapshot_sha256: e57aa4be2b4da0e8c2fd4082e5f08d1cd50239a932a5c403924d3a2618bac654
- evidence_id: disc-mt-agent-schwartz2012-jats
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3439489/fullTextXML
  locator: 'Principal locators s2a (left-handed spiral and overlap), s2c–s2g (polarity,
    lattice, densities), s2h microribbon interface, Table1, s3a–s3c interpretation,
    s5 Methods; Native JATS PMC3439489: Introduction and Results s2a–s2h, Discussion
    s3a–s3e, Conclusions s4 and Methods s5a–s5f read across the unchanged batch12/13
    snapshot; principal locators specified in summary. Claim-bearing captions/Table1
    read; no figure pixels, videos or raw tomography reanalysis.'
  accessed_at: '2026-10-21T08:27:02.838620Z'
  support: supports
  summary: Primary whole-cell/plastic-section tomography resolves a left-handed ventral-disc
    spiral and microribbons; isolated-disc cryo-ET resolves13-protofilament microtubules,
    alpha/beta lattice organization and associated unassigned densities. The paper
    does not identify molecular compositions of gMIP/gMAP/side-arm/paddle/bridge structures.
  snapshot_sha256: df4cb13cb3b12c8be3df05f99f8b97cc44951dd61a2c00a168ed8e9aedb6f9d8
- evidence_id: disc-mt-agent-IPR002452
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002452/
  locator: metadata accession/type/name, description and complete returned family
    hierarchy.
  accessed_at: '2026-10-21T08:41:38.207087Z'
  support: supports
  summary: Native IPR002452 is the Alpha tubulin family. It matches the alpha subset,
    not by itself the combined alpha-and-beta component class.
  snapshot_sha256: ff28f4d004d8f82a804f7263ff1df3ab78d7bdbdeee755fa924a58e872602b5a
- evidence_id: disc-mt-agent-IPR002453
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002453/
  locator: metadata accession/type/name, description and complete returned family
    hierarchy.
  accessed_at: '2026-10-21T08:41:38.873716Z'
  support: supports
  summary: Native IPR002453 is the Beta tubulin family. It matches the beta subset,
    not by itself the combined alpha-and-beta component class.
  snapshot_sha256: edbfe5509d6e568069c7105eacc2b7e296e84e0790a16a63d836c45a094d20ef
- evidence_id: disc-mt-agent-IPR000217
  kind: database
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR000217/
  locator: metadata accession/type/name, description and family hierarchy.
  accessed_at: '2026-10-21T08:41:38.206229Z'
  support: supports
  summary: Native IPR000217 is the broader Tubulin family with alpha, beta, gamma,
    delta, epsilon and zeta children; it does not exactly denote only the asserted
    alpha/beta pair.
  snapshot_sha256: ddbf902c6495d576d69c82c85daf1bdf2bc9fea5894925a4efcd87dc45ea3170
- evidence_id: disc-mt-agent-hagen2011-jats
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC3243723/fullTextXML
  locator: Introduction paragraphs describing primary disc elements and supernumerary
    MTs; compared with Schwartz2012 s2a. Original primary-body receipt reused, but
    this background architectural claim is treated as secondary context.
  accessed_at: '2026-10-21T08:29:17.949589Z'
  support: context_only
  summary: The earlier paper’s Introduction uses right-handed for the main disc spiral
    and left-handed for the supernumerary array, opposite to Schwartz2012. This is
    a background account, not a new chirality measurement in the reviewed localization
    study; the discrepancy is retained without substituting it for the later cited3D
    study.
  snapshot_sha256: 4764e6ef8d323277737b63dbb374bbdb8011ff87153ed54603d74bd616b5e608
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:04Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml'
  snapshot_sha256: d1959d4ace8e993ce443536b46e9ed2ce7607b690d261e61efa7f8fc0ec7b133
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
    --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/ventral_disc_microtubule_array-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T08:41:08Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml\
    \ --out /private/tmp/cellstructure-batch13-20261021-vud60b4w/ventral_disc_microtubule_array-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch13-20261021-vud60b4w/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch13-20261021-vud60b4w/ventral_disc_microtubule_array-strict.tsv"
  snapshot_sha256: d7677dc7852fd1c6cf87825f1954e4844647ed08f738c7b69c88f694f115020d
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-21T08:46:04Z'
  support: supports
  summary: '6 of6 collected target identifiers returned OK at the unchanged base.
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
  topic: Array identity and constituent microtubules
  outcome: supported
  target_ids:
  - GO:0097593
  summary: Exact GO identity, three synonym scopes, definition and filament-based
    nature agree. The array is an assembly of microtubules, not the generic protein
    tubulin, a single microribbon, the separate supernumerary fragment or the whole
    disc.
  evidence_ids:
  - disc-mt-agent-go
  - disc-mt-agent-schwartz2012-jats
  - record
- assessment_id: relations
  area: scope
  topic: Disc parthood, microtubule parts and microribbon base
  outcome: supported
  target_ids:
  - GO:0097593
  summary: Native GO supplies direct disc parthood; the definition and primary tomography
    support has_part GO:0005874 and the microribbon-base relationship. The array can
    contain microtubules without treating microtubule and array as synonyms or importing
    microribbon proteins into the tubulin component.
  evidence_ids:
  - disc-mt-agent-go
  - disc-mt-agent-schwartz2012-jats
  - record
- assessment_id: composition
  area: grounding
  topic: Alpha/beta cohort and family granularity
  outcome: supported
  target_ids:
  - GO:0097593
  summary: The alpha/beta polymer component is supported by native GO and the primary
    lattice analysis. Separately exact alpha and beta family entries are available,
    while IPR000217 is broader than the combined class. No one exact combined-class
    grounding was established by the inspected candidates; the acknowledged label-only
    cohort is defensible. Splitting into optional rows is not automatically required,
    and historical wording is not a claim that neither family exists.
  evidence_ids:
  - disc-mt-agent-go
  - disc-mt-agent-schwartz2012-jats
  - disc-mt-agent-IPR002452
  - disc-mt-agent-IPR002453
  - disc-mt-agent-IPR000217
  - record
  - policy
- assessment_id: taxon
  area: scope
  topic: Species aliases and preparation
  outcome: supported
  target_ids:
  - GO:0097593
  summary: Giardia intestinalis, G.lamblia and native preferred G.duodenalis denote
    species5741. WBC6 trophozoites supply the experimental example. COMMON is qualitative
    characterized-species occurrence, without a numerical prevalence or universal
    stage/strain claim.
  evidence_ids:
  - disc-mt-agent-tax-5741
  - disc-mt-agent-schwartz2012-jats
  - record
- assessment_id: scaffold
  area: evidence
  topic: Structural function and source-specific geometry
  outcome: supported
  target_ids:
  - GO:0097593
  summary: Spiral microtubules form the scaffold and microribbon base as claimed.
    Schwartz2012 explicitly supports the target’s left-handed description; an opposite
    earlier background description is preserved as an unresolved source convention/discrepancy,
    not silently harmonized. No independent chirality reanalysis or force-generation
    assay is claimed.
  evidence_ids:
  - disc-mt-agent-go
  - disc-mt-agent-schwartz2012-jats
  - disc-mt-agent-hagen2011-jats
  - record
- assessment_id: graph
  area: graph
  topic: Three nonmechanistic structural edges
  outcome: supported
  target_ids:
  - GO:0097593
  summary: The component_ref is local and valid. Alpha/beta subunits make up the microtubule
    array, the array forms the microribbon base, and it is part of the disc. ASSEMBLY/NONMECHANISTIC
    avoids a temporal assembly order, recruitment cascade or a reconstituted Giardia
    polymerization pathway; the primary paper supplies static structure and native
    GO supplies generic polymer composition.
  evidence_ids:
  - disc-mt-agent-go
  - disc-mt-agent-schwartz2012-jats
  - record
- assessment_id: density-boundary
  area: completeness
  topic: Unassigned wall and interface densities
  outcome: supported
  target_ids:
  - GO:0097593
  summary: The paper maps gMIPs, gMAPs, side-arms, paddles and an intra-complex bridge
    while noting that a named density may contain multiple proteins. The existing
    TODO properly preserves those unresolved boundaries and does not assign particular
    giardins or family CURIEs from morphology. Empty finer inventory is not automatically
    a defect.
  evidence_ids:
  - disc-mt-agent-schwartz2012-jats
  - record
  - policy
- assessment_id: preparation
  area: scope
  topic: Native context versus extracted high-resolution map
  outcome: supported
  target_ids:
  - GO:0097593
  summary: Whole-cell and resin-section tomography provide the overall disc geometry;
    the high-resolution cryo-ET grand average used extracted, flattened discs, selected
    five tomograms from four discs and excluded overlap/extreme-peripheral regions.
    The record does not universalize the average into a full-disc molecular map or
    assert measured mechanical stiffness.
  evidence_ids:
  - disc-mt-agent-schwartz2012-jats
  - record
findings: []
actions: []
limitations:
- The paper’s main Introduction/Results/Discussion/Conclusions/Methods and claim-bearing
  captions/Table1 were read from the same exact native JATS across batches12–13. Figure
  pixels, raw tomograms, videos and all supplements were not reanalyzed.
- The2012 left-handed main spiral is directly source-supported. Hagen2011 background
  prose uses the opposite main/supernumerary handedness labels; viewing-convention
  or historical correction was not independently resolved, and no new chirality measurement
  is claimed.
- The inspected native family entries cover alpha, beta and the broad tubulin family;
  this is not an exhaustive search for every possible combined-class identifier. Separate
  family availability does not itself require changing the existing component granularity.
- High-resolution densities describe an extracted-disc selected-region average, not
  every disc region, live assembly dynamics or exact molecular stoichiometry. gMIP/gMAP/side-arm/paddle/bridge
  protein identities remain unassigned in the cited source.
- No gene-specific accession, purified-protein reconstitution, universal essentiality,
  cyst-stage presence or numerical species prevalence is inferred.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- All12 native input hashes verified after inspect/schema/strict0. External snapshots
  retain actual original access times; no neighboring maintained YAML was needed.
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
