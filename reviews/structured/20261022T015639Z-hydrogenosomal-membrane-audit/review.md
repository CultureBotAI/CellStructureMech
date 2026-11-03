# Hydrogenosomal membrane identity, source scope and molecular-boundary review

- Review: 20261022T015639Z-hydrogenosomal-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:39:34Z
- Finished UTC: 2026-10-22T01:56:39Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The membrane identity, label-only collective lipid material, species context and descriptive topology are supported. One minor finding corrects the title attached to the valid Tachezy2022 review DOI.

## Scope And Provenance

Full single maintained target and frozen boundary neighbors; exact native identifiers, bibliography and claim-bearing primary/review scopes; no maintained record edits.

Selection: Target 9 of batch thirty in strict uncovered path order; fresh native inspect/schema/strict all passed at unchanged base f97b1abe before assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0046859 | data/structures/membrane_organelle/hydrogenosomal_membrane.yaml | maintained | hydrogenosomal membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0046859 | Focused validator passed. |
| Focused native strict | passed | True | GO:0046859 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0046859 | No expression-module membership, regulator or transcriptomic association is used in this organelle review. |
| Claim-level scientific review | passed | True | GO:0046859 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0046859 | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0046859 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0046859 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0046859 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0046859 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0046859 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact organelle and boundary hierarchy

identity: supported. Targets: GO:0046859.

Native GO and UniProt location identities match the target, synonym where present, and parent/parthood relations. The membrane, internal volume and whole organelle are kept distinct. Double-membrane context in T. vaginalis is directly supported by the primary source; a whole-membrane term is not thereby chemical lipid identity.

### Patchy eukaryotic occurrence and T. vaginalis model

scope: supported. Targets: GO:0046859.

Taxonomic IDs and the species model agree. Native authority and Schneider Introduction support patchy occurrence across anaerobic microbial eukaryotes; RARE is qualitative, not a measured frequency. Schneider Methods specifies T1 and separates fraction-associated proteins from validated localizations. Its proteome is not a universal complete matrix inventory across every hydrogenosome-bearing lineage.

### Incorrect title attached to the correct review DOI

evidence: concern. Targets: GO:0046859.

The exact DOI resolves to Tachezy, Makki and Hrdý2022, The hydrogenosome of Trichomonas vaginalis. The record instead gives Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes. This is a bibliographic provenance error; the DOI is correct and the actual review remains relevant.

### Collective bilayer with deliberately label-only grounding

grounding: supported. Targets: GO:0046859.

The component represents the collective lipid material of this membrane-only target and explicitly rejects the whole GO membrane term as an exact molecular grounding. No unique lipid species or chemical mixture is asserted. This differs from grounding a whole-organelle LIPID row to the complete membrane.

### Unmeasured individual chemical formation requirements

grounding: unknown. Targets: GO:0046859.

The complete constituting bilayer defines this membrane boundary, but the cited proteome and ontology do not establish removal/substitution requirements for individual lipid classes or molecular species. Experimental molecular formation necessities remain unknown; metabolic activity and membership do not substitute for them.

### Boundary function and two descriptive topology edges

graph: supported. Targets: GO:0046859.

Both edges express membrane parthood and enclosure of the matrix. Native definitions establish them and the primary study supplies the metabolic-compartment context. NONMECHANISTIC appropriately avoids importing the whole organelle enzyme/ISC/translocation pathway into this membrane-only record. The component_ref is to its collective constituting material with no asserted whole-membrane molecular grounding.

### Full target, evidence placement and bounded review

completeness: supported. Targets: GO:0046859.

Every maintained claim, evidence item, graph edge and discussion was inspected. Findings are limited to demonstrated identity/provenance/scope issues; optional inventory and inaccessible original bodies alone are not findings. No quantitative measurement field, maintained figure/licence asset or verbatim evidence snippet requires a separate check. Scientific status and history remain unchanged.

## Findings

### F1: Correct the title of the cited Tachezy2022 review

minor / open / confirmed; issue key: hydrogenosomal-membrane-tachezy-title.

DOI:10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas vaginalis by Tachezy, Makki and Hrdý, not the title Hydrogenosomes and mitosomes: Mitochondria of anaerobic eukaryotes recorded in evidence.notes. The DOI and broad scientific relevance remain correct.

## Recommended Actions And Acceptance Checks

### A1

In a separately authorized curation change, replace the incorrect citation title and author attribution with the exact native bibliographic identity while retaining the correct DOI and review evidence tier.

- Verify DOI, exact title, three authors, year2022 and Journal of Eukaryotic Microbiology against the native metadata.
- Do not replace the correct DOI, claim that this review is a primary experiment, or generalize its T. vaginalis focus solely from the incorrect broad title.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/hydrogenosomal_membrane.yaml; Entire maintained YAML, including all components, taxonomy, examples, functions, graphs, evidence, discussions and history | context_only | The exact single target was fully read without maintained scientific edits or status promotion. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent lines391–446, molecular-grounding contract and essentiality; graph component_ref contract | context_only | A component is a molecular building block. The grounding contract distinguishes chemical lipid identity from GO sub-complex identity. Essentiality concerns formation without a component, not catalytic activity or inclusion in an intact inventory. |
| graph-policy | .claude/skills/curate-causal-graphs/SKILL.md; Graph source scope, component correspondence and causal versus descriptive representation | context_only | A correct descriptive topology does not establish molecular equivalence between the complete boundary and an asserted chemical constituent. |
| boundary-neighbor | data/structures/membrane_organelle/hydrogenosome_lumen.yaml; Entire frozen neighboring record, boundary context only | context_only | Whole hydrogenosome, enclosing membrane and enclosed lumen remain distinct; this neighbor is not a second review target. |
| paired-neighbor | data/structures/membrane_organelle/hydrogenosome.yaml; Entire frozen neighboring record, boundary context only | context_only | Whole hydrogenosome, enclosing membrane and enclosed lumen remain distinct; this neighbor is not a second review target. |
| hydrogenosome-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046859,GO:0042566,GO:0034492,GO:0016020,GO:0043231,GO:0005737; All six returned exact IDs, labels, definitions, synonyms and relevant child relations | supports | All six terms are active: hydrogenosome0042566, its membrane0046859 and lumen0034492, membrane0016020, intracellular membrane-bounded organelle0043231 and cytoplasm0005737. Explicit children establish hydrogenosome is_a0043231, part_of cytoplasm, and membrane/lumen parts. The membrane synonym is exact. |
| hydrogenosome-agent-SL-0144 | https://rest.uniprot.org/locations/SL-0144.json; Complete name, synonym, exact GO mapping, isA and partOf structures including embedded Hydrogenosome definition | supports | Hydrogenosome membrane SL0144 maps to GO0046859, is_a Membrane and part_of Hydrogenosome SL0145. The embedded whole-organelle entry describes unrelated anaerobic flagellate, fungal and ciliate lineages, with genome retention in some ciliates. |
| hydrogenosome-agent-SL-0335 | https://rest.uniprot.org/locations/SL-0335.json; Complete name, synonym, exact mapping and partOf | supports | Hydrogenosome lumen maps to GO0034492 and is part of Hydrogenosome SL0145. Its compartment definition supports boundary identity, not a protein or lipid constituent. |
| hydrogenosome-agent-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Exact taxId, scientificName, rank and lineage | supports | ENA2759 identifies Eukaryota at domain rank. Taxonomy alone does not establish prevalence, strain or experimental function. |
| hydrogenosome-agent-tax5722 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5722; Exact taxId, scientificName, rank and lineage | supports | ENA5722 identifies Trichomonas vaginalis at species rank. Taxonomy alone does not establish prevalence, strain or experimental function. |
| hydrogenosome-agent-tachezy2022-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1111/jeu.12922; Exact native bibliographic fields and complete abstract | supports | Native MED identifies The hydrogenosome of Trichomonas vaginalis. by Tachezy J, Makki A, Hrdý I. (2022), DOI 10.1111/jeu.12922, PMID 35567536. The complete returned abstract was read. This is review-tier context, not a new primary experiment. |
| hydrogenosome-agent-schneider2011-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1016/j.ijpara.2011.10.001; Exact native bibliographic fields and complete abstract | supports | Native MED identifies The Trichomonas vaginalis hydrogenosome proteome is highly reduced relative to mitochondria, yet complex compared with mitosomes. by Schneider RE, Brown MT, Shiflett AM, Dyall SD, Hayes RD, Xie Y, Loo JA, Johnson PJ. (2011), DOI 10.1016/j.ijpara.2011.10.001, PMID 22079833. The complete returned abstract was read. Detailed experimental claims use the separately inspected body where available. |
| hydrogenosome-agent-schneider2011-pmc | https://pmc.ncbi.nlm.nih.gov/articles/4437511/; Complete Introduction S1; Methods2.1–2.6 S3–S8 and2.7 S10, with only the opening of2.6.1 S9 inspected; Results3.1 S12 including Table1/Fig1–2 captions, complete3.5 S16 including3.5.1/3.5.2 andFig4–5 captions, complete3.7 S20 including3.7.1/3.7.2 andTable2, complete3.8 S23,3.9 S24 and concluding S25. Other Results, remaining2.6.1, image pixels and supplements not independently analyzed. | supports | T. vaginalis T1 hydrogenosome proteomics supports double membranes, pyruvate/ATP/hydrogen metabolism, ISC proteins and putative translocases. The569 identified proteins include external-surface proteins and possible contaminants; presence in a fraction is not proof every protein resides in matrix. Section3.8 explicitly recognizes targeting without an N-terminal presequence and incomplete motif predictions. The Introduction supports patchy fungal/ciliate/parabasalid occurrence; these are reviewed background statements within a primary proteomic study. |
| schema-result | just validate data/structures/membrane_organelle/hydrogenosomal_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/hydrogenosomal_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/hydrogenosomal_membrane.yaml --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/hydrogenosomal_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/hydrogenosomal_membrane.yaml --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/hydrogenosomal_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch30-20261022-frro2xh0/hydrogenosomal_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/hydrogenosomal_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 9 of 9 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Tachezy2022 is used as review-tier complete native abstract and exact bibliographic identity. Publisher HTML/PDF and author PDF requests returned403. An author manuscript was visible through the browser for its introductory historical pages, but no full-review-body scientific assessment or preserved body receipt is claimed here.
- Schneider2011 reading is limited to the explicitly enumerated Introduction, Methods and Results sections, Tables1–2 and specified captions. No figure pixels, supplementary tables, raw spectra or exhaustive proteome membership were independently analyzed.
- Qualitative RARE/COMMON scope is not a counted prevalence claim. The isolated hydrogenosome fraction contains surface-associated and possible contaminating proteins, and protein-family prediction is not equivalent to validated matrix localization.
- Exact membrane lipid chemistry, individual molecular formation requirements and complete localized cohort inventories remain unresolved; optional completeness is not a required missing field.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorization requires a validated review for every uncovered target; no finding is invented to satisfy the local issue-only output rule.
- Remote snapshots retain original URL, UTC access and raw SHA256. Reused de Zoysa and native sources retain their original batch29 receipts. Parent owns finalization and the five full-corpus gate integrations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T015639Z-hydrogenosomal-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Hydrogenosomal membrane identity, source scope and molecular-boundary review
started_at: '2026-10-22T01:39:34Z'
finished_at: '2026-10-22T01:56:39Z'
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
summary: The membrane identity, label-only collective lipid material, species context
  and descriptive topology are supported. One minor finding corrects the title attached
  to the valid Tachezy2022 review DOI.
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
  - path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    sha256: 7e389b3e00ef30e931b8415dcc2daf38b5022ba6849696387af283a6f9f7ab56
    role: target
  - path: data/structures/membrane_organelle/hydrogenosome.yaml
    sha256: cbe6ff879b7bc2477e475394c4361107d4d033bfeba79e4a85c03787b27b8b70
    role: context
  - path: data/structures/membrane_organelle/hydrogenosome_lumen.yaml
    sha256: 30c5139da8ac02b5d677b314f371d09b1a64fa10a6bb45352d3b8b76c298fd40
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
- target_id: GO:0046859
  path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  label: hydrogenosomal membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    role: maintained scientific record
scope:
  description: Full single maintained target and frozen boundary neighbors; exact
    native identifiers, bibliography and claim-bearing primary/review scopes; no maintained
    record edits.
  selection: Target 9 of batch thirty in strict uncovered path order; fresh native
    inspect/schema/strict all passed at unchanged base f97b1abe before assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0046859
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: just validate data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: just validate-strict data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/hydrogenosomal_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0046859
  summary: No expression-module membership, regulator or transcriptomic association
    is used in this organelle review.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0046859
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - graph-policy
  - boundary-neighbor
  - paired-neighbor
  - hydrogenosome-agent-go
  - hydrogenosome-agent-SL-0144
  - hydrogenosome-agent-SL-0335
  - hydrogenosome-agent-tax2759
  - hydrogenosome-agent-tax5722
  - hydrogenosome-agent-tachezy2022-meta
  - hydrogenosome-agent-schneider2011-meta
  - hydrogenosome-agent-schneider2011-pmc
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0046859
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0046859
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0046859
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
    and current batch30 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  locator: Entire maintained YAML, including all components, taxonomy, examples, functions,
    graphs, evidence, discussions and history
  accessed_at: '2026-10-22T01:47:25Z'
  support: context_only
  summary: The exact single target was fully read without maintained scientific edits
    or status promotion.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent lines391–446, molecular-grounding contract and essentiality;
    graph component_ref contract
  accessed_at: '2026-10-22T01:47:25Z'
  support: context_only
  summary: A component is a molecular building block. The grounding contract distinguishes
    chemical lipid identity from GO sub-complex identity. Essentiality concerns formation
    without a component, not catalytic activity or inclusion in an intact inventory.
- evidence_id: graph-policy
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Graph source scope, component correspondence and causal versus descriptive
    representation
  accessed_at: '2026-10-22T01:47:25Z'
  support: context_only
  summary: A correct descriptive topology does not establish molecular equivalence
    between the complete boundary and an asserted chemical constituent.
- evidence_id: boundary-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/hydrogenosome_lumen.yaml
  locator: Entire frozen neighboring record, boundary context only
  accessed_at: '2026-10-22T01:47:25Z'
  support: context_only
  summary: Whole hydrogenosome, enclosing membrane and enclosed lumen remain distinct;
    this neighbor is not a second review target.
- evidence_id: paired-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/hydrogenosome.yaml
  locator: Entire frozen neighboring record, boundary context only
  accessed_at: '2026-10-22T01:47:25Z'
  support: context_only
  summary: Whole hydrogenosome, enclosing membrane and enclosed lumen remain distinct;
    this neighbor is not a second review target.
- evidence_id: hydrogenosome-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0046859,GO:0042566,GO:0034492,GO:0016020,GO:0043231,GO:0005737
  locator: All six returned exact IDs, labels, definitions, synonyms and relevant
    child relations
  accessed_at: '2026-10-22T01:40:30.242260Z'
  support: supports
  summary: 'All six terms are active: hydrogenosome0042566, its membrane0046859 and
    lumen0034492, membrane0016020, intracellular membrane-bounded organelle0043231
    and cytoplasm0005737. Explicit children establish hydrogenosome is_a0043231, part_of
    cytoplasm, and membrane/lumen parts. The membrane synonym is exact.'
  snapshot_sha256: ba6172c903b6b820bc4dff5fb8cc9b28cf7dab7eab4ced81ad86446f84ec4ddb
- evidence_id: hydrogenosome-agent-SL-0144
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0144.json
  locator: Complete name, synonym, exact GO mapping, isA and partOf structures including
    embedded Hydrogenosome definition
  accessed_at: '2026-10-22T01:40:30.275157Z'
  support: supports
  summary: Hydrogenosome membrane SL0144 maps to GO0046859, is_a Membrane and part_of
    Hydrogenosome SL0145. The embedded whole-organelle entry describes unrelated anaerobic
    flagellate, fungal and ciliate lineages, with genome retention in some ciliates.
  snapshot_sha256: fccca371507283bd774e05a93feda2a3bc58eee39bb06c0b458c57786a80456a
- evidence_id: hydrogenosome-agent-SL-0335
  kind: database
  reference: https://rest.uniprot.org/locations/SL-0335.json
  locator: Complete name, synonym, exact mapping and partOf
  accessed_at: '2026-10-22T01:40:30.855391Z'
  support: supports
  summary: Hydrogenosome lumen maps to GO0034492 and is part of Hydrogenosome SL0145.
    Its compartment definition supports boundary identity, not a protein or lipid
    constituent.
  snapshot_sha256: 96793a2ae46ab05de07492a336d115179a5cf644697d96c5e5d3c4f4daf25c7d
- evidence_id: hydrogenosome-agent-tax2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Exact taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T01:40:30.254730Z'
  support: supports
  summary: ENA2759 identifies Eukaryota at domain rank. Taxonomy alone does not establish
    prevalence, strain or experimental function.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: hydrogenosome-agent-tax5722
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5722
  locator: Exact taxId, scientificName, rank and lineage
  accessed_at: '2026-10-22T01:40:30.265215Z'
  support: supports
  summary: ENA5722 identifies Trichomonas vaginalis at species rank. Taxonomy alone
    does not establish prevalence, strain or experimental function.
  snapshot_sha256: 187c33fcc8a5be0659d37aa99eb3c11f74b2e42cab385cd8ff38b2ba0175e47f
- evidence_id: hydrogenosome-agent-tachezy2022-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1111/jeu.12922
  locator: Exact native bibliographic fields and complete abstract
  accessed_at: '2026-10-22T01:40:29.609875Z'
  support: supports
  summary: Native MED identifies The hydrogenosome of Trichomonas vaginalis. by Tachezy
    J, Makki A, Hrdý I. (2022), DOI 10.1111/jeu.12922, PMID 35567536. The complete
    returned abstract was read. This is review-tier context, not a new primary experiment.
  snapshot_sha256: d04be05b15294eca215c38660eed08c45e0a78d2486043a183144b4682706944
- evidence_id: hydrogenosome-agent-schneider2011-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1016/j.ijpara.2011.10.001
  locator: Exact native bibliographic fields and complete abstract
  accessed_at: '2026-10-22T01:40:29.610134Z'
  support: supports
  summary: Native MED identifies The Trichomonas vaginalis hydrogenosome proteome
    is highly reduced relative to mitochondria, yet complex compared with mitosomes.
    by Schneider RE, Brown MT, Shiflett AM, Dyall SD, Hayes RD, Xie Y, Loo JA, Johnson
    PJ. (2011), DOI 10.1016/j.ijpara.2011.10.001, PMID 22079833. The complete returned
    abstract was read. Detailed experimental claims use the separately inspected body
    where available.
  snapshot_sha256: 8afe4787ba5f9cad8c1bc499491004290d1306b02a0114eafc7082afddcdc57a
- evidence_id: hydrogenosome-agent-schneider2011-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/4437511/
  locator: Complete Introduction S1; Methods2.1–2.6 S3–S8 and2.7 S10, with only the
    opening of2.6.1 S9 inspected; Results3.1 S12 including Table1/Fig1–2 captions,
    complete3.5 S16 including3.5.1/3.5.2 andFig4–5 captions, complete3.7 S20 including3.7.1/3.7.2
    andTable2, complete3.8 S23,3.9 S24 and concluding S25. Other Results, remaining2.6.1,
    image pixels and supplements not independently analyzed.
  accessed_at: '2026-10-22T01:40:30.865625Z'
  support: supports
  summary: T. vaginalis T1 hydrogenosome proteomics supports double membranes, pyruvate/ATP/hydrogen
    metabolism, ISC proteins and putative translocases. The569 identified proteins
    include external-surface proteins and possible contaminants; presence in a fraction
    is not proof every protein resides in matrix. Section3.8 explicitly recognizes
    targeting without an N-terminal presequence and incomplete motif predictions.
    The Introduction supports patchy fungal/ciliate/parabasalid occurrence; these
    are reviewed background statements within a primary proteomic study.
  snapshot_sha256: 71f42aec9b7990c668899689fea0c650181de68fa7ed8c2e0c5a953a4aaf5ea9
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:39:35Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/hydrogenosomal_membrane.yaml'
  snapshot_sha256: e8371b32227bd92e98d90b575c55b9d375d963f988d3a1aa4aa1097990844a7c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/hydrogenosomal_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:39:36Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/hydrogenosomal_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch30-20261022-frro2xh0/hydrogenosomal_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch30-20261022-frro2xh0/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch30-20261022-frro2xh0/hydrogenosomal_membrane-strict.tsv"
  snapshot_sha256: 9fd8db10d8dabaa66a8d9cafc2c22a7bdd6390ee527d391a7da641cfe29708bb
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 9 of 9 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
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
  topic: Exact organelle and boundary hierarchy
  outcome: supported
  target_ids:
  - GO:0046859
  summary: Native GO and UniProt location identities match the target, synonym where
    present, and parent/parthood relations. The membrane, internal volume and whole
    organelle are kept distinct. Double-membrane context in T. vaginalis is directly
    supported by the primary source; a whole-membrane term is not thereby chemical
    lipid identity.
  evidence_ids:
  - record
  - boundary-neighbor
  - paired-neighbor
  - hydrogenosome-agent-go
  - hydrogenosome-agent-SL-0144
  - hydrogenosome-agent-SL-0335
  - hydrogenosome-agent-schneider2011-pmc
- assessment_id: scope
  area: scope
  topic: Patchy eukaryotic occurrence and T. vaginalis model
  outcome: supported
  target_ids:
  - GO:0046859
  summary: Taxonomic IDs and the species model agree. Native authority and Schneider
    Introduction support patchy occurrence across anaerobic microbial eukaryotes;
    RARE is qualitative, not a measured frequency. Schneider Methods specifies T1
    and separates fraction-associated proteins from validated localizations. Its proteome
    is not a universal complete matrix inventory across every hydrogenosome-bearing
    lineage.
  evidence_ids:
  - record
  - hydrogenosome-agent-go
  - hydrogenosome-agent-SL-0144
  - hydrogenosome-agent-tachezy2022-meta
  - hydrogenosome-agent-schneider2011-meta
  - hydrogenosome-agent-schneider2011-pmc
  - hydrogenosome-agent-tax2759
  - hydrogenosome-agent-tax5722
- assessment_id: citation
  area: evidence
  topic: Incorrect title attached to the correct review DOI
  outcome: concern
  target_ids:
  - GO:0046859
  summary: 'The exact DOI resolves to Tachezy, Makki and Hrdý2022, The hydrogenosome
    of Trichomonas vaginalis. The record instead gives Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes. This is a bibliographic provenance error;
    the DOI is correct and the actual review remains relevant.'
  evidence_ids:
  - record
  - hydrogenosome-agent-tachezy2022-meta
- assessment_id: material
  area: grounding
  topic: Collective bilayer with deliberately label-only grounding
  outcome: supported
  target_ids:
  - GO:0046859
  summary: The component represents the collective lipid material of this membrane-only
    target and explicitly rejects the whole GO membrane term as an exact molecular
    grounding. No unique lipid species or chemical mixture is asserted. This differs
    from grounding a whole-organelle LIPID row to the complete membrane.
  evidence_ids:
  - record
  - policy
  - hydrogenosome-agent-go
  - hydrogenosome-agent-SL-0144
  - hydrogenosome-agent-schneider2011-pmc
- assessment_id: necessity
  area: grounding
  topic: Unmeasured individual chemical formation requirements
  outcome: unknown
  target_ids:
  - GO:0046859
  summary: The complete constituting bilayer defines this membrane boundary, but the
    cited proteome and ontology do not establish removal/substitution requirements
    for individual lipid classes or molecular species. Experimental molecular formation
    necessities remain unknown; metabolic activity and membership do not substitute
    for them.
  evidence_ids:
  - record
  - policy
  - hydrogenosome-agent-go
  - hydrogenosome-agent-schneider2011-pmc
- assessment_id: function-graph
  area: graph
  topic: Boundary function and two descriptive topology edges
  outcome: supported
  target_ids:
  - GO:0046859
  summary: Both edges express membrane parthood and enclosure of the matrix. Native
    definitions establish them and the primary study supplies the metabolic-compartment
    context. NONMECHANISTIC appropriately avoids importing the whole organelle enzyme/ISC/translocation
    pathway into this membrane-only record. The component_ref is to its collective
    constituting material with no asserted whole-membrane molecular grounding.
  evidence_ids:
  - record
  - graph-policy
  - hydrogenosome-agent-go
  - hydrogenosome-agent-SL-0144
  - hydrogenosome-agent-SL-0335
  - hydrogenosome-agent-schneider2011-pmc
- assessment_id: coverage
  area: completeness
  topic: Full target, evidence placement and bounded review
  outcome: supported
  target_ids:
  - GO:0046859
  summary: Every maintained claim, evidence item, graph edge and discussion was inspected.
    Findings are limited to demonstrated identity/provenance/scope issues; optional
    inventory and inaccessible original bodies alone are not findings. No quantitative
    measurement field, maintained figure/licence asset or verbatim evidence snippet
    requires a separate check. Scientific status and history remain unchanged.
  evidence_ids:
  - record
  - policy
findings:
- finding_id: F1
  issue_key: hydrogenosomal-membrane-tachezy-title
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the title of the cited Tachezy2022 review
  description: 'DOI:10.1111/jeu.12922 resolves to The hydrogenosome of Trichomonas
    vaginalis by Tachezy, Makki and Hrdý, not the title Hydrogenosomes and mitosomes:
    Mitochondria of anaerobic eukaryotes recorded in evidence.notes. The DOI and broad
    scientific relevance remain correct.'
  target_ids:
  - GO:0046859
  field_paths:
  - evidence[reference=DOI:10.1111/jeu.12922].notes
  evidence_ids:
  - record
  - hydrogenosome-agent-tachezy2022-meta
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:exact identity, scoped evidence
    and severity rubric
  native_severity: minor
  normalization_reason: 'Minor bibliographic provenance error: the resolvable source
    identifier and relevant organelle topic are correct; no wrong organelle identity
    follows from the title correction.'
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0046859
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/hydrogenosomal_membrane.yaml
    role: maintained scientific record
  description: In a separately authorized curation change, replace the incorrect citation
    title and author attribution with the exact native bibliographic identity while
    retaining the correct DOI and review evidence tier.
  acceptance_checks:
  - Verify DOI, exact title, three authors, year2022 and Journal of Eukaryotic Microbiology
    against the native metadata.
  - Do not replace the correct DOI, claim that this review is a primary experiment,
    or generalize its T. vaginalis focus solely from the incorrect broad title.
limitations:
- Tachezy2022 is used as review-tier complete native abstract and exact bibliographic
  identity. Publisher HTML/PDF and author PDF requests returned403. An author manuscript
  was visible through the browser for its introductory historical pages, but no full-review-body
  scientific assessment or preserved body receipt is claimed here.
- Schneider2011 reading is limited to the explicitly enumerated Introduction, Methods
  and Results sections, Tables1–2 and specified captions. No figure pixels, supplementary
  tables, raw spectra or exhaustive proteome membership were independently analyzed.
- Qualitative RARE/COMMON scope is not a counted prevalence claim. The isolated hydrogenosome
  fraction contains surface-associated and possible contaminating proteins, and protein-family
  prediction is not equivalent to validated matrix localization.
- Exact membrane lipid chemistry, individual molecular formation requirements and
  complete localized cohort inventories remain unresolved; optional completeness is
  not a required missing field.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorization requires a validated review for every uncovered target; no finding
  is invented to satisfy the local issue-only output rule.
- Remote snapshots retain original URL, UTC access and raw SHA256. Reused de Zoysa
  and native sources retain their original batch29 receipts. Parent owns finalization
  and the five full-corpus gate integrations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
