# Parasitophorous vacuole scientific review

- Review: 20261022T030057Z-parasitophorous-vacuole-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:42:26Z
- Finished UTC: 2026-10-22T03:00:57Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The apicomplexan PV identity, broader GO parent, unique local boundaries, qualitative occurrence and niche function are supported. One major finding concerns a P. berghei BioID experiment misattributed to P. falciparum in the canonical example.

## Scope And Provenance

Entire single target and explicitly frozen boundary neighbors; exact identities, hierarchy, membership and formation-necessity scope where asserted, taxon/examples, functions, all directed edges, history/discussions and cited source tiers.

Selection: Batch36 target 9; exact native inspection and focused schema/strict gates passed before assessment on unchanged f97b1abe.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:parasitophorous_vacuole | data/structures/membrane_organelle/parasitophorous_vacuole.yaml | maintained | parasitophorous vacuole |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | cellstructuremech:parasitophorous_vacuole | Focused validator passed. |
| Focused native strict | passed | True | cellstructuremech:parasitophorous_vacuole | Focused validator passed. |
| Protein-instance applicability | not_applicable | False | cellstructuremech:parasitophorous_vacuole | This target asserts no individual protein example or GENE_OR_PROTEIN actor; molecular formation necessity is not asserted. |
| Expression-module applicability | not_applicable | False | cellstructuremech:parasitophorous_vacuole | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Claim-level scientific review | passed | True | cellstructuremech:parasitophorous_vacuole | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | cellstructuremech:parasitophorous_vacuole | 10 of 13 collected target identifiers returned OK. cellstructuremech:parasitophorous_vacuole: SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level identifier search; its maintained whole/space/membrane record is a frozen review input. This verifies local identity and preserves the distinct boundary scope, not external authority resolution.; cellstructuremech:parasitophorous_vacuole_lumen: SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level identifier search; its maintained whole/space/membrane record is a frozen review input. This verifies local identity and preserves the distinct boundary scope, not external authority resolution.; cellstructuremech:parasitophorous_vacuole_membrane: SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level identifier search; its maintained whole/space/membrane record is a frozen review input. This verifies local identity and preserves the distinct boundary scope, not external authority resolution. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | cellstructuremech:parasitophorous_vacuole | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | cellstructuremech:parasitophorous_vacuole | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | cellstructuremech:parasitophorous_vacuole | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | cellstructuremech:parasitophorous_vacuole | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | cellstructuremech:parasitophorous_vacuole | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact apicomplexan PV versus broader GO class

identity: supported. Targets: cellstructuremech:parasitophorous_vacuole.

The locally minted PV identity and SL0194 xref consistently represent the stated apicomplexan host-cell compartment. GO0020003 is broader by definition despite an exact lexical synonym, so retained parentage is defensible. The local identity and the two has_part links resolve uniquely.

### Whole vacuole and its membrane/lumen parts

graph: supported. Targets: cellstructuremech:parasitophorous_vacuole.

The one-edge NONMECHANISTIC graph correctly states that the PVM bounds the PV. Its exact local membrane link is distinct from a molecular LIPID grounding; the record has no molecular component or essentiality assertion. Both has_part targets and the resolved membrane-identity discussion agree with the frozen neighbors.

### Replicative host compartment and broad occurrence

scope: supported. Targets: cellstructuremech:parasitophorous_vacuole.

The PV niche function and qualitative Apicomplexa COMMON row are supported by the actual SL0194 definition and the complete Clough review abstract. The review supports the Toxoplasma example. No claim that all apicomplexan stages inhabit a PV or that the entire host-derived membrane is autonomous is inferred.

### BioID study assigned to wrong parasite species

evidence: concern. Targets: cellstructuremech:parasitophorous_vacuole.

The P. falciparum canonical example specifically attributes an intraerythrocytic BioID survey to Schnider2018. Its actual study organism is P. berghei, with ANKA background stated in Methods. Mentioned P. falciparum orthologs and earlier literature do not convert the performed survey into a P. falciparum experiment. This is a source-to-taxon error, not evidence that P. falciparum lacks PVs.

### Exact source tiers and unchanged scientific state

provenance: supported. Targets: cellstructuremech:parasitophorous_vacuole.

Every maintained claim was assessed against the cited native identities and the declared source scope. Historical citations retain their genuine observations; concrete current contradictions are flagged separately. No corpus edit, scientific promotion or saved review is implied.

## Findings

### F1: Correct the species attached to the cited BioID canonical example

major / open / confirmed; issue key: parasitophorous-vacuole-bioid-canonical-species-misattribution.

canonical_examples[1] assigns the Schnider2018 BioID survey to Plasmodium falciparum5833. The cited primary paper performed that survey in P. berghei blood stages and states the ANKA mCherryHsp70 experimental background. Its comparisons with P. falciparum orthologs and previous studies do not support the maintained claim that this survey used P. falciparum.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, align this canonical example with the actual P. berghei study, using verified taxon5821 and the appropriate experimental background, or replace the citation and note with independently inspected P. falciparum-specific experimental evidence. Preserve the broader apicomplexan identity and valid Toxoplasma example.

- The taxon, note and cited experiment identify the same parasite species.
- P. berghei ANKA study data are not relabeled as P. falciparum data; orthology is distinguished from experimental provenance.
- PV identity, PVM/lumen boundary links and valid niche claims remain unchanged.
- Native schema, strict, taxon/identifier and history checks pass after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/parasitophorous_vacuole.yaml; Entire maintained YAML: definition, identity, components, history, distribution/examples, functions, every graph node/edge, evidence and discussions | context_only | The full maintained target was read. Proposed scientific status and maintained bytes remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent and ProteinExample definitions, lines391–475; graph scope and node contracts | context_only | Molecular grounding differs from whole-structure identity; a label-only collective lipid material need not assert an exact chemical species. Essentiality denotes formation necessity, separate from membership or function. Protein examples identify taxon-paired instances, not independent localization experiments. |
| pv-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020003,GO:0020004,GO:0020005; Complete three native definitions, synonyms, comments and direct child relations | supports | GO0020003,0020004 and0020005 are active broader symbiont-containing vacuole, intervening vacuolar space and membrane classes. Returned relations place space and membrane part_of the whole class. GO uses parasitophorous synonyms, but its definitions are not restricted to apicomplexans; lexical overlap alone does not force exact identity with the narrower maintained records. |
| pv-agent-SL0193 | https://rest.uniprot.org/locations/SL-0193.json; Complete native location entry: name/id/definition, synonyms, category, isA/partOf and GO mapping fields when present | supports | SL0193 exactly names the PVM, provides parasitophorous vacuolar membrane as a synonym, places it part_of SL0194 and maps it to broader GO0020005. |
| pv-agent-SL0194 | https://rest.uniprot.org/locations/SL-0194.json; Complete native location entry: name/id/definition, synonyms, category, isA/partOf and GO mapping fields when present | supports | SL0194 defines a host-cell vacuole where most apicomplexan parasites reside and develop, and describes membrane initiation during invasion. This is the maintained narrower scope; it maps to broader GO0020003. |
| pv-agent-SL0341 | https://rest.uniprot.org/locations/SL-0341.json; Complete native location entry: name/id/definition, synonyms, category, isA/partOf and GO mapping fields when present | supports | SL0341 exactly names parasitophorous vacuole lumen, supplies parasitophorous vacuolar lumen as a synonym, and explicitly places it part_of SL0194. Its response does not assert a separate direct GO map. |
| pv-agent-tax5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; Complete taxId, scientificName, rank and lineage | supports | ENA confirms Apicomplexa5794 at phylum rank. Qualitative occurrence derives from the cited location definition, not this taxonomy response. |
| neighbor-parasitophorous_vacuole_lumen | data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml; Entire maintained PV boundary neighbor | context_only | The complete adjacent whole/space/membrane record was read and frozen as maintained boundary context; it is not independent experimental evidence. |
| neighbor-parasitophorous_vacuole_membrane | data/structures/membrane_organelle/parasitophorous_vacuole_membrane.yaml; Entire maintained PV boundary neighbor | context_only | The complete adjacent whole/space/membrane record was read and frozen as maintained boundary context; it is not independent experimental evidence. |
| local-id-search | rg --no-ignore --hidden -n ^identifier: cellstructuremech:parasitophorous_vacuole(_lumen&#124;_membrane)?$ data/structures; Complete ignored-inclusive exact top-level identifier search | supports | Each of the three named local IDs occurs as exactly one top-level identifier in the full maintained data/structures universe, including hidden and ignored files. Those exact whole/lumen/membrane records are frozen inputs. |
| pv-agent-tax5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Complete native taxId, scientificName, rank and lineage | supports | ENA confirms Toxoplasma gondii5811 at species rank. |
| pv-agent-tax5833 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833; Complete native taxId, scientificName, rank and lineage | supports | ENA confirms Plasmodium falciparum5833 at species rank; this correctly names the current row but not the BioID experiment. |
| pv-agent-tax5821 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5821; Complete native taxId, scientificName, rank and lineage | supports | ENA confirms Plasmodium berghei5821 at species rank, the species used in the cited BioID study. |
| pv-agent-lingelbach1998-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1242/jcs.111.11.1467%22; Unique MED result and complete review abstract | supports | Exact DOI10.1242/jcs.111.11.1467/PMID9580555 title/authors/year identify a review of Plasmodium/Toxoplasma PVM formation, maintenance and function. Its complete abstract describes invasion-initiated membrane formation. This is secondary review evidence, not a newly read primary experiment. |
| pv-agent-clough2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.pt.2017.02.007%22; Unique MED result and complete review abstract | supports | Exact DOI10.1016/j.pt.2017.02.007/PMID28330745 identifies the Clough/Frickel review. Its complete abstract supports the Toxoplasma replicative niche and modified host–parasite interface. No detailed review body or quantitative measurement is claimed. |
| pv-agent-schnider2018-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1128/mSphere.00522-17%22; Unique MED result and complete primary abstract | supports | Exact DOI10.1128/mSphere.00522-17/PMID29404413/PMC5784244 identifies the primary BioID study; the full abstract explicitly states P. berghei blood-stage experiments. |
| pv-agent-schnider2018-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5784244/fullTextXML; Genuine PMC5784244 JATS: complete Introduction s0 and Results s1 with embedded main/supplement captions; Discussion s2; Methods s3.3–s3.11. No figure pixels, supplementary data files or raw proteomic reanalysis. | supports | The actual experiment uses P. berghei ANKA mCherryHsp70 parasites, EXP1-BirA*-V5 and18-hour biotin labeling of cultured blood-stage schizonts, followed by affinity purification and LC-MS/MS. Subsequent localizations distinguish PV, PVM and parasite plasma membrane and include liver-stage validation. P. falciparum orthologs and prior studies are discussed, but are not this study's BioID experimental organism. The body supports the general PV boundary while directly contradicting the canonical row's specific species attribution. |
| schema-result | just validate data/structures/membrane_organelle/parasitophorous_vacuole.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/parasitophorous_vacuole.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/parasitophorous_vacuole.yaml --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/parasitophorous_vacuole-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/parasitophorous_vacuole.yaml --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/parasitophorous_vacuole-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/parasitophorous_vacuole-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/parasitophorous_vacuole.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 13 collected target identifiers returned OK. cellstructuremech:parasitophorous_vacuole: SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level identifier search; its maintained whole/space/membrane record is a frozen review input. This verifies local identity and preserves the distinct boundary scope, not external authority resolution.; cellstructuremech:parasitophorous_vacuole_lumen: SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level identifier search; its maintained whole/space/membrane record is a frozen review input. This verifies local identity and preserves the distinct boundary scope, not external authority resolution.; cellstructuremech:parasitophorous_vacuole_membrane: SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level identifier search; its maintained whole/space/membrane record is a frozen review input. This verifies local identity and preserves the distinct boundary scope, not external authority resolution. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Lingelbach1998 and Clough2017 are secondary reviews read at complete native-abstract scope only. The Lingelbach publisher route returned403; the Clough DOI route failed TLS certificate verification (CERTIFICATE_VERIFY_FAILED). No primary mechanism, universal nutrient-permeability result or complete molecular inventory is certified from those abstracts.
- Schnider2018 body scope is explicit; its proximity-label list is not treated as proof that every candidate is a PVM constituent or that any candidate is required for whole-vacuole formation. No image pixels or supplementary datasets were reanalyzed.
- Local identifier uniqueness was checked over all data/structures, including ignored and hidden files, for only the three named PV boundary identities. This is not a comprehensive GO absence search or automatic validation of every neighboring scientific claim.
- The exact location vocabulary and broader GO definitions are distinct evidence surfaces; no exhaustive ontology-equivalence assertion or quantitative occurrence estimate is made.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes clean drafts without inventing findings. Parent owns finalization and persistence. Five same-base global gates are staged separately.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T030057Z-parasitophorous-vacuole-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Parasitophorous vacuole scientific review
started_at: '2026-10-22T02:42:26Z'
finished_at: '2026-10-22T03:00:57Z'
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
summary: The apicomplexan PV identity, broader GO parent, unique local boundaries,
  qualitative occurrence and niche function are supported. One major finding concerns
  a P. berghei BioID experiment misattributed to P. falciparum in the canonical example.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
  state: working_tree
  inputs:
  - path: .claude/skills/curate-causal-graphs/SKILL.md
    sha256: af43ca37f5ea03de1f0de815161ccee918b4b4b87d0b55f6a30a808884a7856b
    role: context
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
  - path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    sha256: bc5b288dc20d549717192249a6d0889856bdaf66fe33b61cd213b503f4d6f610
    role: target
  - path: data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
    sha256: 4a2a0820584215f4a76152f44d66e365ed67a663527da333d2e6c00d24bc244f
    role: context
  - path: data/structures/membrane_organelle/parasitophorous_vacuole_membrane.yaml
    sha256: fceffba04e82c2b88ce9fc1a9366c8931296169b4146291996ebe84f3dc213da
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
- target_id: cellstructuremech:parasitophorous_vacuole
  path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  label: parasitophorous vacuole
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    role: maintained scientific record
scope:
  description: Entire single target and explicitly frozen boundary neighbors; exact
    identities, hierarchy, membership and formation-necessity scope where asserted,
    taxon/examples, functions, all directed edges, history/discussions and cited source
    tiers.
  selection: Batch36 target 9; exact native inspection and focused schema/strict gates
    passed before assessment on unchanged f97b1abe.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:parasitophorous_vacuole
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just validate data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just validate-strict data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/parasitophorous_vacuole-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: protein-applicability
  name: Protein-instance applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: This target asserts no individual protein example or GENE_OR_PROTEIN actor;
    molecular formation necessity is not asserted.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - pv-agent-go
  - pv-agent-SL0193
  - pv-agent-SL0194
  - pv-agent-SL0341
  - pv-agent-tax5794
  - neighbor-parasitophorous_vacuole_lumen
  - neighbor-parasitophorous_vacuole_membrane
  - local-id-search
  - pv-agent-tax5811
  - pv-agent-tax5833
  - pv-agent-tax5821
  - pv-agent-lingelbach1998-meta
  - pv-agent-clough2017-meta
  - pv-agent-schnider2018-meta
  - pv-agent-schnider2018-xml
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: '10 of 13 collected target identifiers returned OK. cellstructuremech:parasitophorous_vacuole:
    SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level
    identifier search; its maintained whole/space/membrane record is a frozen review
    input. This verifies local identity and preserves the distinct boundary scope,
    not external authority resolution.; cellstructuremech:parasitophorous_vacuole_lumen:
    SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level
    identifier search; its maintained whole/space/membrane record is a frozen review
    input. This verifies local identity and preserves the distinct boundary scope,
    not external authority resolution.; cellstructuremech:parasitophorous_vacuole_membrane:
    SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level
    identifier search; its maintained whole/space/membrane record is a frozen review
    input. This verifies local identity and preserves the distinct boundary scope,
    not external authority resolution. Native source checks are separately scoped;
    skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - record
  - local-id-search
  - neighbor-parasitophorous_vacuole_lumen
  - neighbor-parasitophorous_vacuole_membrane
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  command: just check-curies-strict
  exit_code: 0
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:34Z to
    2026-10-22T01:34:04Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch36 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  locator: 'Entire maintained YAML: definition, identity, components, history, distribution/examples,
    functions, every graph node/edge, evidence and discussions'
  accessed_at: '2026-10-22T02:53:11Z'
  support: context_only
  summary: The full maintained target was read. Proposed scientific status and maintained
    bytes remain unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent and ProteinExample definitions, lines391–475; graph
    scope and node contracts
  accessed_at: '2026-10-22T02:53:11Z'
  support: context_only
  summary: Molecular grounding differs from whole-structure identity; a label-only
    collective lipid material need not assert an exact chemical species. Essentiality
    denotes formation necessity, separate from membership or function. Protein examples
    identify taxon-paired instances, not independent localization experiments.
- evidence_id: pv-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020003,GO:0020004,GO:0020005
  locator: Complete three native definitions, synonyms, comments and direct child
    relations
  accessed_at: '2026-10-22T02:47:24.900882Z'
  support: supports
  summary: GO0020003,0020004 and0020005 are active broader symbiont-containing vacuole,
    intervening vacuolar space and membrane classes. Returned relations place space
    and membrane part_of the whole class. GO uses parasitophorous synonyms, but its
    definitions are not restricted to apicomplexans; lexical overlap alone does not
    force exact identity with the narrower maintained records.
  snapshot_sha256: 0c5e6827975c9cf92d329fd907dd1635e5ab83f0608f42002ae34233bcb609c2
- evidence_id: pv-agent-SL0193
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0193.json
  locator: 'Complete native location entry: name/id/definition, synonyms, category,
    isA/partOf and GO mapping fields when present'
  accessed_at: '2026-10-22T02:47:24.901278Z'
  support: supports
  summary: SL0193 exactly names the PVM, provides parasitophorous vacuolar membrane
    as a synonym, places it part_of SL0194 and maps it to broader GO0020005.
  snapshot_sha256: cb9c8cc4e3f7cd3af9100ecc94eab5c05ba6eedd56c152d10301377e82642988
- evidence_id: pv-agent-SL0194
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0194.json
  locator: 'Complete native location entry: name/id/definition, synonyms, category,
    isA/partOf and GO mapping fields when present'
  accessed_at: '2026-10-22T02:47:24.901589Z'
  support: supports
  summary: SL0194 defines a host-cell vacuole where most apicomplexan parasites reside
    and develop, and describes membrane initiation during invasion. This is the maintained
    narrower scope; it maps to broader GO0020003.
  snapshot_sha256: 4bf6005753182d32a68bbb20ed4d7e75a92745c7f24d7ecdf19d78b23465fc28
- evidence_id: pv-agent-SL0341
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0341.json
  locator: 'Complete native location entry: name/id/definition, synonyms, category,
    isA/partOf and GO mapping fields when present'
  accessed_at: '2026-10-22T02:47:24.901412Z'
  support: supports
  summary: SL0341 exactly names parasitophorous vacuole lumen, supplies parasitophorous
    vacuolar lumen as a synonym, and explicitly places it part_of SL0194. Its response
    does not assert a separate direct GO map.
  snapshot_sha256: 9a3abc3189a97bf45ef3653b1ae2c96ac782aa6aa6dd896309db34c0137a3111
- evidence_id: pv-agent-tax5794
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: Complete taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T02:47:24.901531Z'
  support: supports
  summary: ENA confirms Apicomplexa5794 at phylum rank. Qualitative occurrence derives
    from the cited location definition, not this taxonomy response.
  snapshot_sha256: 617b42c27ae95a801b69abf63e1a545eff8565fd0af2f4a81be359d3fb6b3cbf
- evidence_id: neighbor-parasitophorous_vacuole_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/parasitophorous_vacuole_lumen.yaml
  locator: Entire maintained PV boundary neighbor
  accessed_at: '2026-10-22T02:53:11Z'
  support: context_only
  summary: The complete adjacent whole/space/membrane record was read and frozen as
    maintained boundary context; it is not independent experimental evidence.
- evidence_id: neighbor-parasitophorous_vacuole_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/parasitophorous_vacuole_membrane.yaml
  locator: Entire maintained PV boundary neighbor
  accessed_at: '2026-10-22T02:53:11Z'
  support: context_only
  summary: The complete adjacent whole/space/membrane record was read and frozen as
    maintained boundary context; it is not independent experimental evidence.
- evidence_id: local-id-search
  kind: search
  reference: 'rg --no-ignore --hidden -n ^identifier: cellstructuremech:parasitophorous_vacuole(_lumen|_membrane)?$
    data/structures'
  locator: Complete ignored-inclusive exact top-level identifier search
  accessed_at: '2026-10-22T02:51:09.045533Z'
  support: supports
  summary: Each of the three named local IDs occurs as exactly one top-level identifier
    in the full maintained data/structures universe, including hidden and ignored
    files. Those exact whole/lumen/membrane records are frozen inputs.
  snapshot_sha256: 51c79ef89ee1b16e362469081f9642c6a5fee31f95c5506f57cfa6aa3024f5e4
  search_scope: All data/structures files including hidden and ignored; exact top-level
    identifier lines for three named local IDs.
- evidence_id: pv-agent-tax5811
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: Complete native taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T02:47:25.631005Z'
  support: supports
  summary: ENA confirms Toxoplasma gondii5811 at species rank.
  snapshot_sha256: cbb209002c87051ce78d0a34bc169d2f6623f6bbfbb21edad170d43eb16d4032
- evidence_id: pv-agent-tax5833
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5833
  locator: Complete native taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T02:47:25.631195Z'
  support: supports
  summary: ENA confirms Plasmodium falciparum5833 at species rank; this correctly
    names the current row but not the BioID experiment.
  snapshot_sha256: 47c9da135299ea0515b9cbddde80166e0e7256bcf1daac4cdf87f8ae3e0ecd11
- evidence_id: pv-agent-tax5821
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5821
  locator: Complete native taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T02:50:18.419639Z'
  support: supports
  summary: ENA confirms Plasmodium berghei5821 at species rank, the species used in
    the cited BioID study.
  snapshot_sha256: b0491db442378c1d00975990420c6b2ac5d551752d1af21f2b02f199ddf3244e
- evidence_id: pv-agent-lingelbach1998-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1242/jcs.111.11.1467%22
  locator: Unique MED result and complete review abstract
  accessed_at: '2026-10-22T02:47:25.634592Z'
  support: supports
  summary: Exact DOI10.1242/jcs.111.11.1467/PMID9580555 title/authors/year identify
    a review of Plasmodium/Toxoplasma PVM formation, maintenance and function. Its
    complete abstract describes invasion-initiated membrane formation. This is secondary
    review evidence, not a newly read primary experiment.
  snapshot_sha256: 44fc4a33ed68a99e1bbc7a1c3ef2df29b9be6adef6c6f8ef4a401db83c4ba21a
- evidence_id: pv-agent-clough2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.pt.2017.02.007%22
  locator: Unique MED result and complete review abstract
  accessed_at: '2026-10-22T02:47:25.645245Z'
  support: supports
  summary: Exact DOI10.1016/j.pt.2017.02.007/PMID28330745 identifies the Clough/Frickel
    review. Its complete abstract supports the Toxoplasma replicative niche and modified
    host–parasite interface. No detailed review body or quantitative measurement is
    claimed.
  snapshot_sha256: 0b0685884bc32321186981725b894246b202c88ae06b607fac71e8139976d81a
- evidence_id: pv-agent-schnider2018-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1128/mSphere.00522-17%22
  locator: Unique MED result and complete primary abstract
  accessed_at: '2026-10-22T02:47:25.648509Z'
  support: supports
  summary: Exact DOI10.1128/mSphere.00522-17/PMID29404413/PMC5784244 identifies the
    primary BioID study; the full abstract explicitly states P. berghei blood-stage
    experiments.
  snapshot_sha256: 9900df2cc7121899912d85ef554c80cbd1fc7e720f48ae4b2b48701640468993
- evidence_id: pv-agent-schnider2018-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5784244/fullTextXML
  locator: 'Genuine PMC5784244 JATS: complete Introduction s0 and Results s1 with
    embedded main/supplement captions; Discussion s2; Methods s3.3–s3.11. No figure
    pixels, supplementary data files or raw proteomic reanalysis.'
  accessed_at: '2026-10-22T02:47:50.428241Z'
  support: supports
  summary: The actual experiment uses P. berghei ANKA mCherryHsp70 parasites, EXP1-BirA*-V5
    and18-hour biotin labeling of cultured blood-stage schizonts, followed by affinity
    purification and LC-MS/MS. Subsequent localizations distinguish PV, PVM and parasite
    plasma membrane and include liver-stage validation. P. falciparum orthologs and
    prior studies are discussed, but are not this study's BioID experimental organism.
    The body supports the general PV boundary while directly contradicting the canonical
    row's specific species attribution.
  snapshot_sha256: 24181a156e904a7981e409c7de955d57faa0e83d9ec437681077ecc43c4feb6b
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/parasitophorous_vacuole.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:42:27Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/parasitophorous_vacuole.yaml'
  snapshot_sha256: d71a3a564a91c12eb9486dbab9678ddadff386ac0b4f8374ee379605e73bc7e2
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/parasitophorous_vacuole-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:42:28Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/parasitophorous_vacuole.yaml\
    \ --out /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/parasitophorous_vacuole-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch36-20261022-i5iwb5rr/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch36-20261022-i5iwb5rr/parasitophorous_vacuole-strict.tsv"
  snapshot_sha256: 55ad98a85a43803c394faeee13fce269a89b0f474558d3d6c5ac742c0f1ef837
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/parasitophorous_vacuole.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '10 of 13 collected target identifiers returned OK. cellstructuremech:parasitophorous_vacuole:
    SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level
    identifier search; its maintained whole/space/membrane record is a frozen review
    input. This verifies local identity and preserves the distinct boundary scope,
    not external authority resolution.; cellstructuremech:parasitophorous_vacuole_lumen:
    SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level
    identifier search; its maintained whole/space/membrane record is a frozen review
    input. This verifies local identity and preserves the distinct boundary scope,
    not external authority resolution.; cellstructuremech:parasitophorous_vacuole_membrane:
    SKIPPED; Exact locally minted identifier occurs once in an ignored-inclusive top-level
    identifier search; its maintained whole/space/membrane record is a frozen review
    input. This verifies local identity and preserves the distinct boundary scope,
    not external authority resolution. Native source checks are separately scoped;
    skipped or unreachable identifiers are not silently counted as resolved.'
  snapshot_sha256: 173c367ec1621e2a96027e149b5cad9f4db0a86f0a3c916455ce192a9aa5f428
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:05:35Z'
  support: supports
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 8696c0d603149cee93ac200eaa3ed26c84320204285cd22cca542eb1ae7ba572
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:37Z'
  support: supports
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  snapshot_sha256: 98a7952c42add0416633f4dee73ff64331e5c6c4c4c8d707e98a152f04fc5b6d
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:59:14Z'
  support: supports
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T00:58:40Z'
  support: supports
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 'Exit0. Native resolver control: every resolver accepts a known id and
    rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE.
    Transport failures and skipped prefixes are not proof of identifier resolution;
    exact target residuals are assessed separately.'
  snapshot_sha256: 00cc5664a9143235d28fb9885fc5c43a8a78c9a9c9f47603b1232e1eddddeac1
assessments:
- assessment_id: identity
  area: identity
  topic: Exact apicomplexan PV versus broader GO class
  outcome: supported
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: The locally minted PV identity and SL0194 xref consistently represent the
    stated apicomplexan host-cell compartment. GO0020003 is broader by definition
    despite an exact lexical synonym, so retained parentage is defensible. The local
    identity and the two has_part links resolve uniquely.
  evidence_ids:
  - record
  - pv-agent-go
  - pv-agent-SL0194
  - local-id-search
- assessment_id: topology
  area: graph
  topic: Whole vacuole and its membrane/lumen parts
  outcome: supported
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: The one-edge NONMECHANISTIC graph correctly states that the PVM bounds
    the PV. Its exact local membrane link is distinct from a molecular LIPID grounding;
    the record has no molecular component or essentiality assertion. Both has_part
    targets and the resolved membrane-identity discussion agree with the frozen neighbors.
  evidence_ids:
  - record
  - pv-agent-go
  - pv-agent-SL0193
  - pv-agent-SL0341
  - local-id-search
- assessment_id: function
  area: scope
  topic: Replicative host compartment and broad occurrence
  outcome: supported
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: The PV niche function and qualitative Apicomplexa COMMON row are supported
    by the actual SL0194 definition and the complete Clough review abstract. The review
    supports the Toxoplasma example. No claim that all apicomplexan stages inhabit
    a PV or that the entire host-derived membrane is autonomous is inferred.
  evidence_ids:
  - record
  - pv-agent-SL0194
  - pv-agent-tax5794
  - pv-agent-tax5811
  - pv-agent-clough2017-meta
  - pv-agent-lingelbach1998-meta
  - pv-agent-schnider2018-xml
- assessment_id: example
  area: evidence
  topic: BioID study assigned to wrong parasite species
  outcome: concern
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: The P. falciparum canonical example specifically attributes an intraerythrocytic
    BioID survey to Schnider2018. Its actual study organism is P. berghei, with ANKA
    background stated in Methods. Mentioned P. falciparum orthologs and earlier literature
    do not convert the performed survey into a P. falciparum experiment. This is a
    source-to-taxon error, not evidence that P. falciparum lacks PVs.
  evidence_ids:
  - record
  - pv-agent-tax5833
  - pv-agent-tax5821
  - pv-agent-schnider2018-meta
  - pv-agent-schnider2018-xml
- assessment_id: review-boundaries
  area: provenance
  topic: Exact source tiers and unchanged scientific state
  outcome: supported
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  summary: Every maintained claim was assessed against the cited native identities
    and the declared source scope. Historical citations retain their genuine observations;
    concrete current contradictions are flagged separately. No corpus edit, scientific
    promotion or saved review is implied.
  evidence_ids:
  - record
  - pv-agent-go
  - pv-agent-SL0193
  - pv-agent-SL0194
  - pv-agent-SL0341
  - pv-agent-tax5794
  - pv-agent-tax5811
  - pv-agent-tax5833
  - pv-agent-tax5821
  - pv-agent-lingelbach1998-meta
  - pv-agent-clough2017-meta
  - pv-agent-schnider2018-meta
  - pv-agent-schnider2018-xml
findings:
- finding_id: F1
  issue_key: parasitophorous-vacuole-bioid-canonical-species-misattribution
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Correct the species attached to the cited BioID canonical example
  description: canonical_examples[1] assigns the Schnider2018 BioID survey to Plasmodium
    falciparum5833. The cited primary paper performed that survey in P. berghei blood
    stages and states the ANKA mCherryHsp70 experimental background. Its comparisons
    with P. falciparum orthologs and previous studies do not support the maintained
    claim that this survey used P. falciparum.
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  field_paths:
  - canonical_examples[1].taxon_id
  - canonical_examples[1].taxon_label
  - canonical_examples[1].note
  - canonical_examples[1].reference
  evidence_ids:
  - record
  - pv-agent-tax5833
  - pv-agent-tax5821
  - pv-agent-schnider2018-meta
  - pv-agent-schnider2018-xml
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    role: maintained scientific record
  rule_id: Source-specific claim support and biological scope
  native_severity: major
  normalization_reason: A concrete primary experiment is attached to the wrong taxon,
    materially corrupting the canonical species/evidence link. The broad PV identity
    and occurrence in both species remain valid, so major rather than blocker.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:parasitophorous_vacuole
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/parasitophorous_vacuole.yaml
    role: maintained scientific record
  description: In separately authorized curation, align this canonical example with
    the actual P. berghei study, using verified taxon5821 and the appropriate experimental
    background, or replace the citation and note with independently inspected P. falciparum-specific
    experimental evidence. Preserve the broader apicomplexan identity and valid Toxoplasma
    example.
  acceptance_checks:
  - The taxon, note and cited experiment identify the same parasite species.
  - P. berghei ANKA study data are not relabeled as P. falciparum data; orthology
    is distinguished from experimental provenance.
  - PV identity, PVM/lumen boundary links and valid niche claims remain unchanged.
  - Native schema, strict, taxon/identifier and history checks pass after authorized
    curation.
limitations:
- Lingelbach1998 and Clough2017 are secondary reviews read at complete native-abstract
  scope only. The Lingelbach publisher route returned403; the Clough DOI route failed
  TLS certificate verification (CERTIFICATE_VERIFY_FAILED). No primary mechanism,
  universal nutrient-permeability result or complete molecular inventory is certified
  from those abstracts.
- Schnider2018 body scope is explicit; its proximity-label list is not treated as
  proof that every candidate is a PVM constituent or that any candidate is required
  for whole-vacuole formation. No image pixels or supplementary datasets were reanalyzed.
- Local identifier uniqueness was checked over all data/structures, including ignored
  and hidden files, for only the three named PV boundary identities. This is not a
  comprehensive GO absence search or automatic validation of every neighboring scientific
  claim.
- The exact location vocabulary and broader GO definitions are distinct evidence surfaces;
  no exhaustive ontology-equivalence assertion or quantitative occurrence estimate
  is made.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes clean drafts without inventing findings. Parent
  owns finalization and persistence. Five same-base global gates are staged separately.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
