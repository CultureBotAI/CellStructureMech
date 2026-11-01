# Axonemal doublet ribbon identity and evidence review

- Review: 20261020T035821Z-axonemal-microtubule-doublet-ribbon-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-20T03:55:24Z
- Finished UTC: 2026-10-20T03:58:21Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact ribbon identity, coarse composition, species context, two identity exemplars and four graph edges are supported. No observed defect within the record’s declared scope.

## Scope And Provenance

Entire record; all identifiers, three cited publications at claim-relevant passages, two exemplars and four edges.

Selection: Eighth unreviewed path of batch3.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 99692a3d5f16a7dcd6db7e3811344c299a977b81.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0160115 | data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml | maintained | axonemal microtubule doublet ribbon |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0160115 | Focused validator passed. |
| Focused native strict | passed | True | GO:0160115 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0160115 | 8 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Expression-module applicability | not_applicable | False | GO:0160115 | No expression dataset or transcriptional-regulation claim is used; structural and biochemical evidence determines this review. |
| Claim-level scientific review | passed | True | GO:0160115 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0160115 | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0160115 | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0160115 | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0160115 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0160115 | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### A11-A13 substructure

identity: supported. Targets: GO:0160115.

The record matches the exact GO cellular-component identity and parthood; it is distinct from the whole A-tubule and inner junction.

### Tubulin backbone and associated MIPs

evidence: supported. Targets: GO:0160115.

The backbone and associated-protein group are supported. RIB72 association is explicit in the2003 abstract; RIB43a association is explicit in the2018 source. Essentiality applies to the tubulin constituent class, not a demonstrated individual-gene knockout requirement.

### Two accession tuples

grounding: supported. Targets: GO:0160115.

Current names, genes, statuses and taxon labels match. Neither example is represented as independent localization evidence; the TUA2 fragment is an identity exemplar, not a complete structural model.

### Model species and older comparative biochemistry

scope: supported. Targets: GO:0160115.

The2003 primary abstract supports normal Chlamydomonas ribbon occurrence and its canonical example. Linck1976 concerns animal sperm and supports generic ribbon architecture; the record does not attribute those experiments to Chlamydomonas.

### Structural stabilization

evidence: supported. Targets: GO:0160115.

The GO definition supports stabilization of the ribbon protofilaments; Linck1976 supplies extraction-resistance evidence. The coarse role is supported without asserting a quantified mechanical effect or universal subunit mechanism.

### Four descriptive edges

graph: supported. Targets: GO:0160115.

Tubulin formation, MIP association, doublet parthood and stabilization have claim-level support. The NONMECHANISTIC label accurately bounds this architecture graph.

### Completeness and declared unknowns

provenance: supported. Targets: GO:0160115.

PROPOSED status and open composition grounding/copy-number discussion are consistent with the evidence. Optional image, trait and physical-property fields contain no claims requiring verification.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ribbon-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160115,GO:0097545; Exact two definitions and child relations | supports | Active GO0160115 specifies A11-A13, associated MIPs, luminal separation and stabilization. GO0097545 lists the ribbon through part_of. |
| ribbon-proteins | https://rest.uniprot.org/uniprotkb/search?query=accession:Q6SPP7%20OR%20accession:Q9M6B0&amp;format=json; Complete entries, genes, names, taxa, sequence flag | supports | Both unreviewed accessions, submitted protein names, gene symbols and species3055 match. Q6SPP7 is explicitly a fragment; the record uses it only as a gene-identity exemplar. |
| sheath-taxon | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055; Exact taxon | supports | NCBITaxon3055 is Chlamydomonas reinhardtii. |
| ribbon-epmc | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1242/jcs.20.2.405%20OR%20DOI:10.1074/jbc.M210751200%20OR%20DOI:10.1002/bies.201700209&amp;format=json&amp;resultType=core; All three exact results; complete abstracts | supports | Three DOI/title/author joins are correct. Linck1976 abstract directly describes resistant three-protofilament ribbons and axial repeats in animal sperm. Ikeda2003 abstract directly identifies Rib72 in the Chlamydomonas ribbon compartment. |
| review2018 | https://www.researchgate.net/publication/323127882_Microtubule_Inner_Proteins_A_Meshwork_of_Luminal_Proteins_Stabilizing_the_Doublet_Microtubule; Public article text; sections2-4, Figure2 and Table2; DOI10.1002/bies.201700209 | supports | The cited review explicitly assigns Rib43a and Rib72 to the ribbon. Table2 gives Q9M6B0 for Chlamydomonas Rib43a. Specific density assignments and mechanistic functions are qualified, whereas ribbon association is established. |
| record | data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml; Entire target, both components/examples, four edges and discussion | context_only | This is a coarse structural record with explicit uncertainty about MIP family identities and copy numbers. Examples assert identity only; no allele-specific localization or exact experimental sequence is claimed. |
| schema-result | just validate data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml |
| strict-result | just validate-strict data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule_doublet_ribbon-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule_doublet_ribbon-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch3-20261019-YKo4JU/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule_doublet_ribbon-strict.tsv |
| target-curies | just check-curies-strict; data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml; exact collect() scope | supports | 8 of8 collected target identifiers returned OK at the unchanged base. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 6c8c7d7abaf6a0a21b9e0eb879d48c56c28ac4e6078a53b7026927980af7bdec | supports | Exit 0. Native QC passed: 1017 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1759 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 a790911c34f0fcbf67057d508b1992332228d191b143cbc6ce4455c5424e36ad | supports | Exit 0. Label results: 3543 canonical, 50 synonym, 6 exception and 600 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 99692a3d5f16a7dcd6db7e3811344c299a977b81; stdout SHA-256 below, stderr SHA-256 64567a41acb57e09a332d91b914e0f757dff330c0e69e5fec5e0fe9f6034e3d4 | supports | Exit 0. Resolver controls passed; 4806 identifiers OK, 819 UNREACHABLE and 252 SKIPPED. Transport failures (including PMID batch HTTP 414) and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- The1976 and2003 primary papers were inspected through their complete source abstracts; the specific claims used here are explicit there. Full experimental protocols were not reviewed.
- The2018 review’s relevant full-text sections and Table2 were inspected; its historical density hypotheses are not promoted to resolved molecular assignments.
- The TUA2 accession is a sequence fragment and is suitable here only for the record’s explicitly restricted identity role.
- Exact MIP inventory, family groundings and copy numbers remain openly unresolved.
- Shared corpus gates have bounded coverage: 600 label checks had no adapter; the identifier command reported 819 transport-unreachable and 252 skipped identifiers. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- The user explicitly authorizes saving clean reviews.
- Only the review bundle is saved. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261020T035821Z-axonemal-microtubule-doublet-ribbon-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Axonemal doublet ribbon identity and evidence review
started_at: '2026-10-20T03:55:24Z'
finished_at: '2026-10-20T03:58:21Z'
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
summary: Exact ribbon identity, coarse composition, species context, two identity
  exemplars and four graph edges are supported. No observed defect within the record’s
  declared scope.
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
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
    sha256: 8966a4edaaa6f5f1645bded7428c44111b6213badd19bb0051e6473062dba3ce
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
- target_id: GO:0160115
  path: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
  label: axonemal microtubule doublet ribbon
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
    role: maintained scientific record
scope:
  description: Entire record; all identifiers, three cited publications at claim-relevant
    passages, two exemplars and four edges.
  selection: Eighth unreviewed path of batch3.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0160115
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0160115
  command: just validate data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0160115
  command: just validate-strict data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
    --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule_doublet_ribbon-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0160115
  summary: 8 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0160115
  summary: No expression dataset or transcriptional-regulation claim is used; structural
    and biochemical evidence determines this review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0160115
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - ribbon-go
  - ribbon-proteins
  - sheath-taxon
  - ribbon-epmc
  - review2018
  - record
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0160115
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
  - GO:0160115
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
  - GO:0160115
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
  - GO:0160115
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
  - GO:0160115
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
- evidence_id: ribbon-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0160115,GO:0097545
  locator: Exact two definitions and child relations
  accessed_at: '2026-10-20T03:57:44.040099Z'
  support: supports
  summary: Active GO0160115 specifies A11-A13, associated MIPs, luminal separation
    and stabilization. GO0097545 lists the ribbon through part_of.
  snapshot_sha256: 4eedce15660a1ab5831d7a2218d211f83239619c3dc7631aa303641cc1477d6d
- evidence_id: ribbon-proteins
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/search?query=accession:Q6SPP7%20OR%20accession:Q9M6B0&format=json
  locator: Complete entries, genes, names, taxa, sequence flag
  accessed_at: '2026-10-20T03:57:43.971510Z'
  support: supports
  summary: Both unreviewed accessions, submitted protein names, gene symbols and species3055
    match. Q6SPP7 is explicitly a fragment; the record uses it only as a gene-identity
    exemplar.
  snapshot_sha256: b5cf2541a3e715ca168c5e5dfee3bbc2216ed418f80a340145f0dd9e00fa83b4
- evidence_id: sheath-taxon
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055
  locator: Exact taxon
  accessed_at: '2026-10-20T03:38:20.199537Z'
  support: supports
  summary: NCBITaxon3055 is Chlamydomonas reinhardtii.
  snapshot_sha256: a17bc1c97fea9112288574ef15727ed7e37c42787a430ef074ae5fc654547e6b
- evidence_id: ribbon-epmc
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.1242/jcs.20.2.405%20OR%20DOI:10.1074/jbc.M210751200%20OR%20DOI:10.1002/bies.201700209&format=json&resultType=core
  locator: All three exact results; complete abstracts
  accessed_at: '2026-10-20T03:57:44.032466Z'
  support: supports
  summary: Three DOI/title/author joins are correct. Linck1976 abstract directly describes
    resistant three-protofilament ribbons and axial repeats in animal sperm. Ikeda2003
    abstract directly identifies Rib72 in the Chlamydomonas ribbon compartment.
  snapshot_sha256: ceb6acbc876bb9e2272be5d708cce01e27f6a279e117bbcda9563bb8c3eb2f7f
- evidence_id: review2018
  kind: primary_source
  reference: https://www.researchgate.net/publication/323127882_Microtubule_Inner_Proteins_A_Meshwork_of_Luminal_Proteins_Stabilizing_the_Doublet_Microtubule
  locator: Public article text; sections2-4, Figure2 and Table2; DOI10.1002/bies.201700209
  accessed_at: '2026-10-20T03:58:21Z'
  support: supports
  summary: The cited review explicitly assigns Rib43a and Rib72 to the ribbon. Table2
    gives Q9M6B0 for Chlamydomonas Rib43a. Specific density assignments and mechanistic
    functions are qualified, whereas ribbon association is established.
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
  locator: Entire target, both components/examples, four edges and discussion
  accessed_at: '2026-10-20T03:58:21Z'
  support: context_only
  summary: This is a coarse structural record with explicit uncertainty about MIP
    family identities and copy numbers. Examples assert identity only; no allele-specific
    localization or exact experimental sequence is claimed.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-20T03:55:25Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml'
  snapshot_sha256: c77fec48c8a2066abdf4d4313315e05037a0e47f3ccf35d179d809c31ee911da
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
    --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule_doublet_ribbon-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-20T03:55:27Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml\
    \ --out /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule_doublet_ribbon-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch3-20261019-YKo4JU/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch3-20261019-YKo4JU/axonemal_microtubule_doublet_ribbon-strict.tsv"
  snapshot_sha256: eded63c2aa137e8b6ae842ce725d33c555f1f16793439ddb563123720eeab378
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml;
    exact collect() scope
  accessed_at: '2026-10-20T03:58:21Z'
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
  topic: A11-A13 substructure
  outcome: supported
  target_ids:
  - GO:0160115
  summary: The record matches the exact GO cellular-component identity and parthood;
    it is distinct from the whole A-tubule and inner junction.
  evidence_ids:
  - ribbon-go
  - record
- assessment_id: components
  area: evidence
  topic: Tubulin backbone and associated MIPs
  outcome: supported
  target_ids:
  - GO:0160115
  summary: The backbone and associated-protein group are supported. RIB72 association
    is explicit in the2003 abstract; RIB43a association is explicit in the2018 source.
    Essentiality applies to the tubulin constituent class, not a demonstrated individual-gene
    knockout requirement.
  evidence_ids:
  - ribbon-go
  - ribbon-epmc
  - review2018
  - record
- assessment_id: examples
  area: grounding
  topic: Two accession tuples
  outcome: supported
  target_ids:
  - GO:0160115
  summary: Current names, genes, statuses and taxon labels match. Neither example
    is represented as independent localization evidence; the TUA2 fragment is an identity
    exemplar, not a complete structural model.
  evidence_ids:
  - ribbon-proteins
  - sheath-taxon
  - record
- assessment_id: scope
  area: scope
  topic: Model species and older comparative biochemistry
  outcome: supported
  target_ids:
  - GO:0160115
  summary: The2003 primary abstract supports normal Chlamydomonas ribbon occurrence
    and its canonical example. Linck1976 concerns animal sperm and supports generic
    ribbon architecture; the record does not attribute those experiments to Chlamydomonas.
  evidence_ids:
  - ribbon-epmc
  - sheath-taxon
  - record
- assessment_id: function
  area: evidence
  topic: Structural stabilization
  outcome: supported
  target_ids:
  - GO:0160115
  summary: The GO definition supports stabilization of the ribbon protofilaments;
    Linck1976 supplies extraction-resistance evidence. The coarse role is supported
    without asserting a quantified mechanical effect or universal subunit mechanism.
  evidence_ids:
  - ribbon-go
  - ribbon-epmc
  - record
- assessment_id: graph
  area: graph
  topic: Four descriptive edges
  outcome: supported
  target_ids:
  - GO:0160115
  summary: Tubulin formation, MIP association, doublet parthood and stabilization
    have claim-level support. The NONMECHANISTIC label accurately bounds this architecture
    graph.
  evidence_ids:
  - ribbon-go
  - ribbon-epmc
  - review2018
  - record
- assessment_id: provenance
  area: provenance
  topic: Completeness and declared unknowns
  outcome: supported
  target_ids:
  - GO:0160115
  summary: PROPOSED status and open composition grounding/copy-number discussion are
    consistent with the evidence. Optional image, trait and physical-property fields
    contain no claims requiring verification.
  evidence_ids:
  - ribbon-go
  - ribbon-epmc
  - record
findings: []
actions: []
limitations:
- The1976 and2003 primary papers were inspected through their complete source abstracts;
  the specific claims used here are explicit there. Full experimental protocols were
  not reviewed.
- The2018 review’s relevant full-text sections and Table2 were inspected; its historical
  density hypotheses are not promoted to resolved molecular assignments.
- The TUA2 accession is a sequence fragment and is suitable here only for the record’s
  explicitly restricted identity role.
- Exact MIP inventory, family groundings and copy numbers remain openly unresolved.
- 'Shared corpus gates have bounded coverage: 600 label checks had no adapter; the
  identifier command reported 819 transport-unreachable and 252 skipped identifiers.
  These totals are not target-specific biological findings or proof that all corpus
  identifiers resolve.'
notes:
- The user explicitly authorizes saving clean reviews.
- Only the review bundle is saved. Maintained scientific content, native status, history
  and generated pages remain unchanged.
```
