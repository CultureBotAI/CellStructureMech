# Mitochondrial outer membrane translocase complex scientific review

- Review: 20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T08:17:33Z
- Finished UTC: 2026-10-22T08:48:10Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole TOM identity, topology and outer-entry function are supported. One minor corrects GIP from an exact to a narrower synonym; optional constituent-family expansion remains bounded follow-up.

## Scope And Provenance

Exactly one complete maintained target, frozen guidance/protein-example skill and, for Lon, its exact stored figure. Actual source-reading extents and original receipts are declared per evidence row.

Selection: Target 9 of batch60, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005742 | data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml | maintained | mitochondrial outer membrane translocase complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005742 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005742 | Focused validator passed. |
| Native causal-graphs | passed | True | GO:0005742 | Native focused check passed; scientific claims assessed separately. |
| Native verify | passed | True | GO:0005742 | Native focused check passed; scientific claims assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0005742 | No expression-module inference is used to establish this structure. |
| Claim-level scientific review | passed | True | GO:0005742 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005742 | 7 of 7 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005742 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005742 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005742 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005742 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005742 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Whole TOM and narrower GIP synonym

identity: concern. Targets: GO:0005742.

The exact whole-complex identity, outer-membrane parent/parthood and main synonym agree. GIP is explicitly a narrow GO synonym, and native Tom22 distinguishes docking of Tom20/Tom70 onto the general Tom40 import-pore complex; the current EXACT_SYNONYM typing overstates equivalence.

### Outer entry step without downstream conflation

graph: supported. Targets: GO:0005742.

The NONMECHANISTIC graph states outer-membrane location and entry for precursors continuing through TIM23/PAM. It does not assert that TOM alone completes matrix import or turn downstream machinery into TOM constituents.

### Verified candidates remain bounded follow-up

completeness: supported. Targets: GO:0005742.

The review and native entries identify seven yeast Tom constituents. Exact candidate families are now verified for Tom40/22/20/70/5/6/7, with fungal subfamilies distinguished from broader whole families. The pending discussion describes unasserted optional rows; it does not claim these terms are absent. No separate finding is manufactured from that pending inventory or the NONMECHANISTIC scope.

### Eukaryotic distribution and yeast context

scope: unknown. Targets: GO:0005742.

The review supports canonical eukaryotic mitochondrial TOM import and characterized yeast machinery. COMMON retains majority/losses-exception meaning, supported qualitatively rather than by a strain census. The exact lineage/strain prevalence underlying Eukaryota VARIABLE is not independently measured here and is retained as a limitation, not redefined as state-dependent visibility.

### No universal individual formation assertion

grounding: unknown. Targets: GO:0005742.

The current record does not assign individual component essentiality. Source-specific association/perturbation observations and positive constitutive identity are not automatically generalized to universal formation necessity.

### Whole maintained target and exact current source scope

completeness: supported. Targets: GO:0005742.

All maintained fields and current scientific assertions were compared with their nearest inspected sources. Historical read claims, optional enrichment and acknowledged unknowns alone do not create findings.

## Findings

### F1: Retain GIP as a narrower synonym

minor / open / confirmed; issue key: tom-gip-synonym-scope.

The current synonym row types GIP complex as EXACT_SYNONYM and attributes it to GO0005742. The native GO response marks GIP as narrow. The Tom22 authority independently distinguishes docking Tom20/Tom70 onto the general Tom40 import-pore complex, supporting the narrower-core boundary while preserving whole TOM identity.

## Recommended Actions And Acceptance Checks

### A1

Change only the GIP synonym scope to NARROW_SYNONYM or supply an explicitly scoped alternative supported by a direct source. Preserve the exact whole TOM identifier and the other exact synonym.

- Recheck the native GO synonym type and retain the pore-core versus whole-complex distinction.
- Pass schema, strict and applicable identifier checks after separately authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml; Entire maintained record, including all evidence, graph edges, discussions, examples, datasets, images and history | context_only | Every maintained field was read. Historical source-inspection claims are not automatically adopted as current review evidence. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; Component, ProteinExample, EssentialityEnum, PresenceEnum and graph contracts | context_only | Membership and enzymatic activity differ from formation necessity. COMMON means most members with losses the exception; VARIABLE denotes lineage/strain patchiness, not cell state. |
| curation | docs/CURATION.md; Exact grounding, label-only classes and native validation contracts | context_only | Exact whole-protein families differ from domains or broader classes. Optional inventories and acknowledged unknowns do not alone establish defects. |
| complex60-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004176,GO:0005741,GO:0005742,GO:0005743,GO:0005759,GO:0007005,GO:0030150,GO:0035632,GO:0098799,GO:0098800,GO:1905368; Complete target-relevant native definitions, synonyms and typed relationships; unrelated combined entries excluded | supports | GO0005742 exactly identifies TOM and marks GIP complex as a narrow synonym. GO0098799 lists TOM as an is_a child; matrix import GO0030150 includes the downstream TOM-TIM23-PAM route. |
| complex60-agent-tax-2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete exact ENA taxonomy response | supports | Native taxon2759 is Eukaryota, rank domain. Its own names and lineage were read. |
| complex60-agent-tax-4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete exact ENA taxonomy response | supports | Native taxon4932 is Saccharomyces cerevisiae, rank species. Its own names and lineage were read. |
| complex60-agent-gene-TOM40 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM40+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete query result identity set and indicated returned-entry comments | supports | The exact reviewed S288C query returns P23644; all returned identities and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION and InterPro references were also read. |
| complex60-agent-gene-TOM22 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM22+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete query result identity set and indicated returned-entry comments | supports | The exact reviewed S288C query returns P49334; all returned identities and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION and InterPro references were also read. |
| complex60-agent-gene-TOM20 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM20+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete query result identity set and indicated returned-entry comments | supports | The exact reviewed S288C query returns P35180; all returned identities and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION and InterPro references were also read. |
| complex60-agent-gene-TOM70 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM70+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete query result identity set and indicated returned-entry comments | supports | The exact reviewed S288C query returns P07213; all returned identities and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION and InterPro references were also read. |
| complex60-agent-gene-TOM5 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM5+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete query result identity set and indicated returned-entry comments | supports | The exact reviewed S288C query returns P80967; all returned identities and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION and InterPro references were also read. |
| complex60-agent-gene-TOM6 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM6+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete query result identity set and indicated returned-entry comments | supports | The exact reviewed S288C query returns P33448; all returned identities and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION and InterPro references were also read. |
| complex60-agent-gene-TOM7 | https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM7+AND+organism_id%3A559292+AND+reviewed%3Atrue&amp;format=json&amp;size=500; Complete query result identity set and indicated returned-entry comments | supports | The exact reviewed S288C query returns P53507; all returned identities and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION and InterPro references were also read. |
| complex60-agent-doi-10.1016_j.cell.2009.08.005 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2009.08.005%22+AND+SRC%3AMED&amp;format=json&amp;resultType=core; Complete native bibliographic identity and available abstract | supports | Exact native identity: Importing mitochondrial proteins: machineries and mechanisms. Chacinska A, Koehler CM, Milenkovic D, Lithgow T, Pfanner N. (2009), PMID19703392. Complete available abstract read. |
| complex60-agent-go-0005742-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005742/ancestors?relations=is_a; Complete is_a-only native ancestor response | supports | The exact is_a-only ancestor closure includes the asserted mitochondrial membrane-protein-complex parent. It does not independently establish experimental mechanism or prevalence. |
| complex60-agent-chacinska2009-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4099469.1/PMC4099469.1.xml; Complete Introduction S1, TOM S2, TIM23 S7, PAM S8 and coupling S10; no table, figure pixels, supplements or cited primary bodies. Original imported source receipt retained. | supports | Chacinska2009 reviews the Tom40 channel, Tom20/Tom22/Tom70 receptors, small Tom5/6/7 subunits and downstream TIM23/PAM machinery. The whole TOM entry step is distinct from complete matrix translocation. This is secondary synthesis, not a newly inspected primary reconstitution. |
| complex60-agent-ipr-IPR037930 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037930/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR037930, Tom40, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| complex60-agent-ipr-IPR005686 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005686/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR005686, Mitochondrial import receptor subunit Tom40, fungi, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| complex60-agent-ipr-IPR005683 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005683/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR005683, Mitochondrial import receptor subunit Tom22, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| complex60-agent-ipr-IPR020951 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020951/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR020951, Mitochondrial import receptor subunit Tom22, fungi, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| complex60-agent-ipr-IPR002056 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002056/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR002056, Protein import receptor MAS20, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| complex60-agent-ipr-IPR005687 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005687/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR005687, Mitochondrial outer membrane translocase complex, subunit Tom70, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| complex60-agent-ipr-IPR019603 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019603/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR019603, Mitochondrial outer membrane translocase complex, subunit Tom5, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| complex60-agent-ipr-IPR020266 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020266/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR020266, Mitochondrial import receptor subunit Tom6, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| complex60-agent-ipr-IPR012621 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012621/; Complete family metadata, descriptions, signatures and quality flags | supports | Native family identity: IPR012621, Mitochondrial import receptor subunit TOM7, type family. Its complete description, signatures and quality flags were inspected; any protein membership is supported separately by the protein response. |
| schema-result | just validate data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml |
| strict-result | just validate-strict data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mitochondrial_outer_membrane_translocase_complex-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mitochondrial_outer_membrane_translocase_complex-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mitochondrial_outer_membrane_translocase_complex-strict.tsv |
| native-causal-graphs | /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml --causal-graphs; Complete native focused report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| native-verify | /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml --verify; Complete native focused report | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| target-curies | just check-curies-strict; data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 7 of 7 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five completed same-base batch26 global gates are integrated with exact manifest/input/log hashes verified; no fresh full-site QC is claimed from this sparse checkout.
- Only explicitly declared source sections and assets were inspected. No raw experimental data or atomic coordinates were reanalysed.
- Chacinska2009 is an inspected review, not independent verification of every primary experiment it cites. The seven family candidates are follow-up context; no required complete constituent inventory or universal per-subunit formation requirement is imposed.
- The eukaryotic VARIABLE occurrence assignment has no independently measured lineage-frequency census in this source scope.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The explicit all-record goal authorizes both qualified clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T084810Z-mitochondrial-outer-membrane-translocase-complex-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Mitochondrial outer membrane translocase complex scientific review
started_at: '2026-10-22T08:17:33Z'
finished_at: '2026-10-22T08:48:10Z'
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
summary: Whole TOM identity, topology and outer-entry function are supported. One
  minor corrects GIP from an exact to a narrower synonym; optional constituent-family
  expansion remains bounded follow-up.
source:
  git_revision: f97b1abe2d78971b6f66b9083087d7a94cf3c0cc
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
  - path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    sha256: a9facce19eda1794aefb3bef7b36fe07ba5c3a942220a4379c5569de4150022e
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
- target_id: GO:0005742
  path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  label: mitochondrial outer membrane translocase complex
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete maintained target, frozen guidance/protein-example
    skill and, for Lon, its exact stored figure. Actual source-reading extents and
    original receipts are declared per evidence row.
  selection: Target 9 of batch60, strict uncovered path order at unchanged f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005742
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: just validate data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: just validate-strict data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mitochondrial_outer_membrane_translocase_complex-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    --causal-graphs
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: native-verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    --verify
  exit_code: 0
  summary: Native focused check passed; scientific claims assessed separately.
  evidence_ids:
  - native-verify
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005742
  summary: No expression-module inference is used to establish this structure.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005742
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - complex60-agent-go
  - complex60-agent-tax-2759
  - complex60-agent-tax-4932
  - complex60-agent-gene-TOM40
  - complex60-agent-gene-TOM22
  - complex60-agent-gene-TOM20
  - complex60-agent-gene-TOM70
  - complex60-agent-gene-TOM5
  - complex60-agent-gene-TOM6
  - complex60-agent-gene-TOM7
  - complex60-agent-doi-10.1016_j.cell.2009.08.005
  - complex60-agent-go-0005742-ancestors
  - complex60-agent-chacinska2009-jats
  - complex60-agent-ipr-IPR037930
  - complex60-agent-ipr-IPR005686
  - complex60-agent-ipr-IPR005683
  - complex60-agent-ipr-IPR020951
  - complex60-agent-ipr-IPR002056
  - complex60-agent-ipr-IPR005687
  - complex60-agent-ipr-IPR019603
  - complex60-agent-ipr-IPR020266
  - complex60-agent-ipr-IPR012621
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005742
  summary: 7 of 7 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005742
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005742
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
    and current batch60 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  locator: Entire maintained record, including all evidence, graph edges, discussions,
    examples, datasets, images and history
  accessed_at: '2026-10-22T08:37:13Z'
  support: context_only
  summary: Every maintained field was read. Historical source-inspection claims are
    not automatically adopted as current review evidence.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: Component, ProteinExample, EssentialityEnum, PresenceEnum and graph contracts
  accessed_at: '2026-10-22T08:37:13Z'
  support: context_only
  summary: Membership and enzymatic activity differ from formation necessity. COMMON
    means most members with losses the exception; VARIABLE denotes lineage/strain
    patchiness, not cell state.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact grounding, label-only classes and native validation contracts
  accessed_at: '2026-10-22T08:37:13Z'
  support: context_only
  summary: Exact whole-protein families differ from domains or broader classes. Optional
    inventories and acknowledged unknowns do not alone establish defects.
- evidence_id: complex60-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0004176,GO:0005741,GO:0005742,GO:0005743,GO:0005759,GO:0007005,GO:0030150,GO:0035632,GO:0098799,GO:0098800,GO:1905368
  locator: Complete target-relevant native definitions, synonyms and typed relationships;
    unrelated combined entries excluded
  accessed_at: '2026-10-22T08:24:00.662524Z'
  support: supports
  summary: GO0005742 exactly identifies TOM and marks GIP complex as a narrow synonym.
    GO0098799 lists TOM as an is_a child; matrix import GO0030150 includes the downstream
    TOM-TIM23-PAM route.
  snapshot_sha256: e6a248305bc7752e1bb81d50f22d98da6c5bdd61dadb96af270f922128b26fb7
- evidence_id: complex60-agent-tax-2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete exact ENA taxonomy response
  accessed_at: '2026-10-22T08:24:03.464969Z'
  support: supports
  summary: Native taxon2759 is Eukaryota, rank domain. Its own names and lineage were
    read.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: complex60-agent-tax-4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete exact ENA taxonomy response
  accessed_at: '2026-10-22T08:24:03.593628Z'
  support: supports
  summary: Native taxon4932 is Saccharomyces cerevisiae, rank species. Its own names
    and lineage were read.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: complex60-agent-gene-TOM40
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM40+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete query result identity set and indicated returned-entry comments
  accessed_at: '2026-10-22T08:24:11.205735Z'
  support: supports
  summary: The exact reviewed S288C query returns P23644; all returned identities
    and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION
    and InterPro references were also read.
  snapshot_sha256: 38a89570647da9b92eb171e44ce611acce231f7eff964a9853885c001339e1da
  search_scope: Exact retained request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM40+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    all returned results inspected.
- evidence_id: complex60-agent-gene-TOM22
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM22+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete query result identity set and indicated returned-entry comments
  accessed_at: '2026-10-22T08:24:11.427030Z'
  support: supports
  summary: The exact reviewed S288C query returns P49334; all returned identities
    and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION
    and InterPro references were also read.
  snapshot_sha256: 030bd1eb366924304cd6982f6e66f24c56b381f24b9da59f9d8fc78c38f3caa4
  search_scope: Exact retained request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM22+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    all returned results inspected.
- evidence_id: complex60-agent-gene-TOM20
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM20+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete query result identity set and indicated returned-entry comments
  accessed_at: '2026-10-22T08:24:11.827171Z'
  support: supports
  summary: The exact reviewed S288C query returns P35180; all returned identities
    and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION
    and InterPro references were also read.
  snapshot_sha256: 0a186aed4a361f60d248c5a4cb95b1971b2bbe35d59f3a6a8a42cbb863005e90
  search_scope: Exact retained request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM20+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    all returned results inspected.
- evidence_id: complex60-agent-gene-TOM70
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM70+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete query result identity set and indicated returned-entry comments
  accessed_at: '2026-10-22T08:24:12.135236Z'
  support: supports
  summary: The exact reviewed S288C query returns P07213; all returned identities
    and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION
    and InterPro references were also read.
  snapshot_sha256: a3686fc7de1c641fbfe919665059e83fe51cc74a2e90027670e8c140193720d4
  search_scope: Exact retained request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM70+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    all returned results inspected.
- evidence_id: complex60-agent-gene-TOM5
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM5+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete query result identity set and indicated returned-entry comments
  accessed_at: '2026-10-22T08:24:12.263420Z'
  support: supports
  summary: The exact reviewed S288C query returns P80967; all returned identities
    and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION
    and InterPro references were also read.
  snapshot_sha256: bb712a48d2dbc9ba523b214417f044c2a1dfc7e8c9cd6b0fb4e35f58ddea6e8d
  search_scope: Exact retained request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM5+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    all returned results inspected.
- evidence_id: complex60-agent-gene-TOM6
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM6+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete query result identity set and indicated returned-entry comments
  accessed_at: '2026-10-22T08:24:12.547128Z'
  support: supports
  summary: The exact reviewed S288C query returns P33448; all returned identities
    and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION
    and InterPro references were also read.
  snapshot_sha256: a57726ab1dad85fd4490629fc948822ef50f42e28941f771e729530b39f43ab5
  search_scope: Exact retained request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM6+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    all returned results inspected.
- evidence_id: complex60-agent-gene-TOM7
  kind: search
  reference: https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM7+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500
  locator: Complete query result identity set and indicated returned-entry comments
  accessed_at: '2026-10-22T08:24:12.980811Z'
  support: supports
  summary: The exact reviewed S288C query returns P53507; all returned identities
    and gene tokens were inspected. Returned full-entry FUNCTION/SUBUNIT/LOCATION
    and InterPro references were also read.
  snapshot_sha256: 4143829bd45a5ea07c1a0888fe01bc35992a7a9be13fd4c74d5e5ac95fd66267
  search_scope: Exact retained request https://rest.uniprot.org/uniprotkb/search?query=gene_exact%3ATOM7+AND+organism_id%3A559292+AND+reviewed%3Atrue&format=json&size=500;
    all returned results inspected.
- evidence_id: complex60-agent-doi-10.1016_j.cell.2009.08.005
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cell.2009.08.005%22+AND+SRC%3AMED&format=json&resultType=core
  locator: Complete native bibliographic identity and available abstract
  accessed_at: '2026-10-22T08:24:06.467439Z'
  support: supports
  summary: 'Exact native identity: Importing mitochondrial proteins: machineries and
    mechanisms. Chacinska A, Koehler CM, Milenkovic D, Lithgow T, Pfanner N. (2009),
    PMID19703392. Complete available abstract read.'
  snapshot_sha256: 6f9a4f9ac5d4cee38cb0e95c67e9d315a3b7c465d1716f117bdd4e8d5b9a2dd7
- evidence_id: complex60-agent-go-0005742-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005742/ancestors?relations=is_a
  locator: Complete is_a-only native ancestor response
  accessed_at: '2026-10-22T08:24:07.774567Z'
  support: supports
  summary: The exact is_a-only ancestor closure includes the asserted mitochondrial
    membrane-protein-complex parent. It does not independently establish experimental
    mechanism or prevalence.
  snapshot_sha256: 2997b2b57b236f7c9b169d20105062ee345a58809ef7ccd432e17a79db3ce91b
- evidence_id: complex60-agent-chacinska2009-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4099469.1/PMC4099469.1.xml
  locator: Complete Introduction S1, TOM S2, TIM23 S7, PAM S8 and coupling S10; no
    table, figure pixels, supplements or cited primary bodies. Original imported source
    receipt retained.
  accessed_at: '2026-10-22T02:21:09.775994Z'
  support: supports
  summary: Chacinska2009 reviews the Tom40 channel, Tom20/Tom22/Tom70 receptors, small
    Tom5/6/7 subunits and downstream TIM23/PAM machinery. The whole TOM entry step
    is distinct from complete matrix translocation. This is secondary synthesis, not
    a newly inspected primary reconstitution.
  snapshot_sha256: 010e4b847c377e924ee1635a33ce3479a86b63183d5e5b4524a6904ff555ceba
- evidence_id: complex60-agent-ipr-IPR037930
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR037930/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:12.395237Z'
  support: supports
  summary: 'Native family identity: IPR037930, Tom40, type family. Its complete description,
    signatures and quality flags were inspected; any protein membership is supported
    separately by the protein response.'
  snapshot_sha256: 11b39b372584392de606846964e5df0135105e26ea6d933f7d39bd03a1cbbd71
- evidence_id: complex60-agent-ipr-IPR005686
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005686/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:12.694526Z'
  support: supports
  summary: 'Native family identity: IPR005686, Mitochondrial import receptor subunit
    Tom40, fungi, type family. Its complete description, signatures and quality flags
    were inspected; any protein membership is supported separately by the protein
    response.'
  snapshot_sha256: 4918743a6b99f2041f1891d7d44c74fb21f4ec9e47da25242c9d5c4d8e537427
- evidence_id: complex60-agent-ipr-IPR005683
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005683/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:11.796742Z'
  support: supports
  summary: 'Native family identity: IPR005683, Mitochondrial import receptor subunit
    Tom22, type family. Its complete description, signatures and quality flags were
    inspected; any protein membership is supported separately by the protein response.'
  snapshot_sha256: 5510c6aaedb6effa6107ed8e3ca400d2a1b91799038f0fc5eecfe55f949489e7
- evidence_id: complex60-agent-ipr-IPR020951
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020951/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:12.103838Z'
  support: supports
  summary: 'Native family identity: IPR020951, Mitochondrial import receptor subunit
    Tom22, fungi, type family. Its complete description, signatures and quality flags
    were inspected; any protein membership is supported separately by the protein
    response.'
  snapshot_sha256: c1867c085bab9a8bcb79c4ce73bfcc80f2fabdb6fa086566263dbcd386a627eb
- evidence_id: complex60-agent-ipr-IPR002056
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR002056/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:11.496556Z'
  support: supports
  summary: 'Native family identity: IPR002056, Protein import receptor MAS20, type
    family. Its complete description, signatures and quality flags were inspected;
    any protein membership is supported separately by the protein response.'
  snapshot_sha256: 39218d6b3819ff08bb08c779c694f86ee61a14c09413ec3ea3d82c033b45f4f7
- evidence_id: complex60-agent-ipr-IPR005687
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR005687/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:13.942836Z'
  support: supports
  summary: 'Native family identity: IPR005687, Mitochondrial outer membrane translocase
    complex, subunit Tom70, type family. Its complete description, signatures and
    quality flags were inspected; any protein membership is supported separately by
    the protein response.'
  snapshot_sha256: 61d5ce706787a28482fe55aa414e5103b36e8cabe5456cccfbdaf047703a2821
- evidence_id: complex60-agent-ipr-IPR019603
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR019603/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:12.992884Z'
  support: supports
  summary: 'Native family identity: IPR019603, Mitochondrial outer membrane translocase
    complex, subunit Tom5, type family. Its complete description, signatures and quality
    flags were inspected; any protein membership is supported separately by the protein
    response.'
  snapshot_sha256: 2c7a62970335a1447895f03c096ad456f4022f63957afeceea9c301b76668283
- evidence_id: complex60-agent-ipr-IPR020266
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR020266/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:13.301820Z'
  support: supports
  summary: 'Native family identity: IPR020266, Mitochondrial import receptor subunit
    Tom6, type family. Its complete description, signatures and quality flags were
    inspected; any protein membership is supported separately by the protein response.'
  snapshot_sha256: 1d842a377c7d730dbb2104c7284f2f4f11579968fc5122dbae8f807674d26775
- evidence_id: complex60-agent-ipr-IPR012621
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR012621/
  locator: Complete family metadata, descriptions, signatures and quality flags
  accessed_at: '2026-10-22T08:25:13.719429Z'
  support: supports
  summary: 'Native family identity: IPR012621, Mitochondrial import receptor subunit
    TOM7, type family. Its complete description, signatures and quality flags were
    inspected; any protein membership is supported separately by the protein response.'
  snapshot_sha256: 0c2ffdc1819b020bbb2e36f27dbf9256c9d95a8ee587dc890f896f372b8ae5de
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:17:34Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml'
  snapshot_sha256: adbbd755ca0e8b6e26a03eaf3fea9679ca5366fe616fbd3e8ededb82f55b989a
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mitochondrial_outer_membrane_translocase_complex-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T08:17:35Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml\
    \ --out /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mitochondrial_outer_membrane_translocase_complex-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch60-20261022-hg31t4fv/mitochondrial_outer_membrane_translocase_complex-strict.tsv"
  snapshot_sha256: 679c367d25cb525e1f9d448d382456f01e744825e6ec73ff960d59c1406c1ad2
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    --causal-graphs
  locator: Complete native focused report
  accessed_at: '2026-10-22T08:25:14.139959Z'
  support: supports
  summary: "causal_graphs GENE_OR_PROTEIN node summary:\n     0  COVERED         \
    \          component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  UNANCHORED_NO_UNIPROT\
    \     no component_ref and no UniProtKB grounding or xref on the node\n     0\
    \  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 76713306e77e0692d57177510568a0e633849a0a594c55b30edcd9a5e375e6a5
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch60-20261022-hg31t4fv/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    --verify
  locator: Complete native focused report
  accessed_at: '2026-10-22T08:25:14.521183Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml;
    native collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 7 of 7 collected target identifiers returned OK. No residuals. Native source
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
  topic: Whole TOM and narrower GIP synonym
  outcome: concern
  target_ids:
  - GO:0005742
  summary: The exact whole-complex identity, outer-membrane parent/parthood and main
    synonym agree. GIP is explicitly a narrow GO synonym, and native Tom22 distinguishes
    docking of Tom20/Tom70 onto the general Tom40 import-pore complex; the current
    EXACT_SYNONYM typing overstates equivalence.
  evidence_ids:
  - record
  - complex60-agent-go
  - complex60-agent-go-0005742-ancestors
  - complex60-agent-chacinska2009-jats
  - complex60-agent-gene-TOM40
  - complex60-agent-gene-TOM22
  - complex60-agent-gene-TOM20
  - complex60-agent-gene-TOM70
  - complex60-agent-gene-TOM5
  - complex60-agent-gene-TOM6
  - complex60-agent-gene-TOM7
- assessment_id: graph
  area: graph
  topic: Outer entry step without downstream conflation
  outcome: supported
  target_ids:
  - GO:0005742
  summary: The NONMECHANISTIC graph states outer-membrane location and entry for precursors
    continuing through TIM23/PAM. It does not assert that TOM alone completes matrix
    import or turn downstream machinery into TOM constituents.
  evidence_ids:
  - record
  - complex60-agent-go
  - complex60-agent-go-0005742-ancestors
  - complex60-agent-chacinska2009-jats
- assessment_id: inventory
  area: completeness
  topic: Verified candidates remain bounded follow-up
  outcome: supported
  target_ids:
  - GO:0005742
  summary: The review and native entries identify seven yeast Tom constituents. Exact
    candidate families are now verified for Tom40/22/20/70/5/6/7, with fungal subfamilies
    distinguished from broader whole families. The pending discussion describes unasserted
    optional rows; it does not claim these terms are absent. No separate finding is
    manufactured from that pending inventory or the NONMECHANISTIC scope.
  evidence_ids:
  - record
  - curation
  - complex60-agent-chacinska2009-jats
  - complex60-agent-gene-TOM40
  - complex60-agent-gene-TOM22
  - complex60-agent-gene-TOM20
  - complex60-agent-gene-TOM70
  - complex60-agent-gene-TOM5
  - complex60-agent-gene-TOM6
  - complex60-agent-gene-TOM7
  - complex60-agent-ipr-IPR037930
  - complex60-agent-ipr-IPR005686
  - complex60-agent-ipr-IPR005683
  - complex60-agent-ipr-IPR020951
  - complex60-agent-ipr-IPR002056
  - complex60-agent-ipr-IPR005687
  - complex60-agent-ipr-IPR019603
  - complex60-agent-ipr-IPR020266
  - complex60-agent-ipr-IPR012621
- assessment_id: scope
  area: scope
  topic: Eukaryotic distribution and yeast context
  outcome: unknown
  target_ids:
  - GO:0005742
  summary: The review supports canonical eukaryotic mitochondrial TOM import and characterized
    yeast machinery. COMMON retains majority/losses-exception meaning, supported qualitatively
    rather than by a strain census. The exact lineage/strain prevalence underlying
    Eukaryota VARIABLE is not independently measured here and is retained as a limitation,
    not redefined as state-dependent visibility.
  evidence_ids:
  - record
  - schema
  - complex60-agent-chacinska2009-jats
  - complex60-agent-tax-2759
  - complex60-agent-tax-4932
- assessment_id: formation
  area: grounding
  topic: No universal individual formation assertion
  outcome: unknown
  target_ids:
  - GO:0005742
  summary: The current record does not assign individual component essentiality. Source-specific
    association/perturbation observations and positive constitutive identity are not
    automatically generalized to universal formation necessity.
  evidence_ids:
  - record
  - schema
  - complex60-agent-chacinska2009-jats
- assessment_id: coverage
  area: completeness
  topic: Whole maintained target and exact current source scope
  outcome: supported
  target_ids:
  - GO:0005742
  summary: All maintained fields and current scientific assertions were compared with
    their nearest inspected sources. Historical read claims, optional enrichment and
    acknowledged unknowns alone do not create findings.
  evidence_ids:
  - record
  - schema
  - curation
  - complex60-agent-go
findings:
- finding_id: F1
  issue_key: tom-gip-synonym-scope
  category: identity
  severity: minor
  status: open
  certainty: confirmed
  title: Retain GIP as a narrower synonym
  description: The current synonym row types GIP complex as EXACT_SYNONYM and attributes
    it to GO0005742. The native GO response marks GIP as narrow. The Tom22 authority
    independently distinguishes docking Tom20/Tom70 onto the general Tom40 import-pore
    complex, supporting the narrower-core boundary while preserving whole TOM identity.
  target_ids:
  - GO:0005742
  field_paths:
  - synonyms[0].synonym_type
  evidence_ids:
  - record
  - complex60-agent-go
  - complex60-agent-gene-TOM40
  - complex60-agent-gene-TOM22
  - complex60-agent-gene-TOM20
  - complex60-agent-gene-TOM70
  - complex60-agent-gene-TOM5
  - complex60-agent-gene-TOM6
  - complex60-agent-gene-TOM7
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    role: maintained scientific record
  rule_id: Exact synonym and structure-boundary correspondence
  native_severity: minor
  normalization_reason: A bounded synonym-scope correction preserves the supported
    whole-complex identity, location and import function.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005742
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/mitochondrial_outer_membrane_translocase_complex.yaml
    role: maintained scientific record
  description: Change only the GIP synonym scope to NARROW_SYNONYM or supply an explicitly
    scoped alternative supported by a direct source. Preserve the exact whole TOM
    identifier and the other exact synonym.
  acceptance_checks:
  - Recheck the native GO synonym type and retain the pore-core versus whole-complex
    distinction.
  - Pass schema, strict and applicable identifier checks after separately authorized
    curation.
limitations:
- All five completed same-base batch26 global gates are integrated with exact manifest/input/log
  hashes verified; no fresh full-site QC is claimed from this sparse checkout.
- Only explicitly declared source sections and assets were inspected. No raw experimental
  data or atomic coordinates were reanalysed.
- Chacinska2009 is an inspected review, not independent verification of every primary
  experiment it cites. The seven family candidates are follow-up context; no required
  complete constituent inventory or universal per-subunit formation requirement is
  imposed.
- The eukaryotic VARIABLE occurrence assignment has no independently measured lineage-frequency
  census in this source scope.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The explicit all-record goal authorizes both qualified clean and issue-bearing reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
