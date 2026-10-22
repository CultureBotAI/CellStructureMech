# Microneme lumen boundary and source review

- Review: 20261022T022235Z-microneme-lumen-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:03:00Z
- Finished UTC: 2026-10-22T02:22:35Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

The microneme lumen identity, compartment boundary, cargo-storage context and descriptive topology are supported. No concrete curation finding was established.

## Scope And Provenance

Full target and two frozen boundary neighbors; exact native definitions/taxa, source bibliography, complete1997 primary main text and specified review sections.

Selection: Batch32 target4; initial inspect/schema/strict0 before assessment at immutable f97b1abe.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0034494 | data/structures/membrane_organelle/microneme_lumen.yaml | maintained | microneme lumen |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0034494 | Focused validator passed. |
| Focused native strict | passed | True | GO:0034494 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0034494 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Protein-example applicability | not_applicable | False | GO:0034494 | No protein_examples, gene symbols or GENE_OR_PROTEIN graph nodes occur in this boundary record; all graph nodes and references were manually checked. |
| Claim-level scientific review | passed | True | GO:0034494 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0034494 | 8 of 9 collected target identifiers returned OK. PMID:9208224: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID9208224 (no DOI returned in this native MED row) and Sequential protein secretion from three distinct organelles of Toxoplasma gondii accompanies invasion of human fibroblasts. Scientific scope remains limited to the separately documented inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0034494 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0034494 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0034494 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0034494 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0034494 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact boundary class and hierarchy

identity: supported. Targets: GO:0034494.

GO0034494 denotes only the enclosed volume; GO0043233 is a compatible broader lumen class. The microneme part relation is explicit in the returned whole-organelle child relations. No unsupported direct native edge is inferred from the broader-parent definition.

### Region without permanent cargo constituents

grounding: supported. Targets: GO:0034494.

The record leaves this spatial compartment without components and keeps the boundary membrane outside the lumen. Its generic storage statement concerns soluble cargo or luminal cargo portions, not a claim that every transmembrane adhesin or the entire MIC2–M2AP complex lies wholly in the lumen. The adjacent whole-record topology concern is not imported into this record.

### Apicomplexan occurrence and Toxoplasma example

scope: supported. Targets: GO:0034494.

The review supports qualitative COMMON occurrence with species and life-stage variation, including absent micronemes in Theileria zoites. The exact Toxoplasma example is supported by the RH/2F fibroblast-invasion study. Taxon identities are verified independently; no prevalence count or every-stage universality is claimed.

### Secretory cargo storage

evidence: supported. Targets: GO:0034494.

The enclosed secretory volume stores cargo before regulated discharge. Carruthers2008 describes lumenal contents and the1997 study demonstrates timed MIC2 redistribution; membrane-associated adhesins are not relabeled entirely soluble.

### Two descriptive topology edges

graph: supported. Targets: GO:0034494.

The two NONMECHANISTIC edges correctly place the lumen within the organelle and inside its bounding membrane. No molecular causal sequence or permanent cargo inventory is asserted.

### Bounded optional detail

completeness: supported. Targets: GO:0034494.

No obligatory missing component or unverified exact mapping is established. The resolved boundary interpretation is correctly implemented; temporary cargo does not require constituent rows.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/microneme_lumen.yaml; Entire maintained target and every function, graph edge and discussion | context_only | The complete record was read without edits. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, grounding, essentiality and graph/component_ref contract | context_only | Constituting material and whole cellular structure are distinct; assembly necessity is not inferred from biochemical function. |
| whole-neighbor | data/structures/membrane_organelle/microneme.yaml; Entire frozen maintained neighbor | context_only | Read to resolve whole organelle, limiting membrane and lumen boundaries; maintained context is not independent experimental support. |
| boundary-neighbor | data/structures/membrane_organelle/microneme_membrane.yaml; Entire frozen maintained neighbor | context_only | Read to resolve whole organelle, limiting membrane and lumen boundaries; maintained context is not independent experimental support. |
| microneme-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020009,GO:0020007,GO:0033163,GO:0034494,GO:0043231,GO:0043233,GO:0031090; All seven complete labels/definitions/active flags, synonyms and returned relations | supports | Seven active native terms distinguish the microneme, its membrane, its lumen, apical complex and broader organelle classes. GO0020009 returns both membrane/lumen part_of children; GO0020007 returns microneme part_of; GO0043231 returns microneme is_a. Broader lumen/membrane parents are supported by definitions without asserting absent direct edges. |
| microneme-agent-tax5794 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794; Exact taxId/scientificName/rank and lineage | supports | ENA confirms Apicomplexa for taxon5794 with its native rank. The receipt establishes this identity, not organelle prevalence or experimental strain equivalence. |
| microneme-agent-tax5811 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811; Exact taxId/scientificName/rank and lineage | supports | ENA confirms Toxoplasma gondii for taxon5811 with its native rank. The receipt establishes this identity, not organelle prevalence or experimental strain equivalence. |
| microneme-agent-carruthers2008-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2F978-0-387-78267-6_2%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact MED DOI/title/authors/year/PMID and complete abstract | supports | Exact native bibliographic identity and complete abstract read for carruthers2008. Literature-review tier. |
| microneme-agent-dubois2019-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fcmi.13018%22&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact MED DOI/title/authors/year/PMID and complete abstract | supports | Exact native bibliographic identity and complete abstract read for dubois2019. Literature-review tier. |
| microneme-agent-pmid-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A%289208224+OR+11157983+OR+15684324+OR+18818666+OR+11083833+OR+11087913+OR+16102004%29+AND+SRC%3AMED&amp;format=json&amp;resultType=core&amp;pageSize=100; Exact requested MED result(s), identity and complete abstracts | supports | Exact MED PMID9208224 identifies Carruthers and Sibley1997 and its complete abstract. Only this result is used for this target; the bundled response also contains other microneme localization papers. |
| microneme-agent-carruthers1997-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC13475723/; Complete Introduction S1, Methods S2/S3–11, Results S12/S13–18 and Discussion S19, including Figures1–8 captions. No figure pixels or original kinetic data reanalysis. | supports | The recovered author manuscript reports RH/2F tachyzoites invading human fibroblasts. MIC2 secretion accompanies initial contact, before rhoptry and dense-granule release. It establishes the sequential-secretion model, not MIC2–M2AP perturbation or PKG signaling experiments. |
| microneme-agent-carruthers2008-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC2847500/; Complete Introduction S1, Oligomerization of MIC proteins S9 and Organization of MIC ligands within micronemes S10, including embedded Figure1 caption; no full review-body or pixel claim. | supports | The review describes stage/species variation, including Theileria zoites without micronemes; qualitative common occurrence is not universality. S9 distinguishes soluble M2AP from transmembrane MIC2 and its cytoplasmic targeting tail; S10 describes poorly resolved lumen organization and condensed contents. |
| microneme-agent-dubois2019-unige-pdf | https://access.archive-ouverte.unige.ch/access/metadata/8d9f50fe-0548-4e4f-bc29-4b05a43e7ddc/download; Accepted author manuscript: Abstract, Introduction, Microneme diversity/structure, Contents/conservation, Biogenesis/maturation/trafficking, Signaling cascade, Preparing for secretion, Fusion, Insights from other organisms and Concluding remarks. Table1 and figure pixels not comprehensively inspected. | supports | The accepted review manuscript supports varied microneme architecture, adhesin complexes, protein sorting and regulated exocytosis. It separates signaling evidence from speculative docking/fusion models and the unrelated exoneme/mononeme classes. It does not establish a universal lipid recipe or a complete fusion machinery. |
| schema-result | just validate data/structures/membrane_organelle/microneme_lumen.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/microneme_lumen.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/microneme_lumen.yaml --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/microneme_lumen-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/microneme_lumen.yaml --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/microneme_lumen-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch32-20261022-k96_2wx1/microneme_lumen-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/microneme_lumen.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 9 collected target identifiers returned OK. PMID:9208224: UNREACHABLE; The bulk transport returned414; the independently retrieved exact MED identity confirms PMID9208224 (no DOI returned in this native MED row) and Sequential protein secretion from three distinct organelles of Toxoplasma gondii accompanies invasion of human fibroblasts. Scientific scope remains limited to the separately documented inspections. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Carruthers2008 and Dubois2019 are review-tier. Only Carruthers S1/S9/S10 were read in full; Dubois accepted-manuscript scientific main text was inspected, without a comprehensive Table1 or image analysis. Publisher403 remains an access-route limit, not absence of the recovered accepted text.
- The1997 primary author manuscript was read through Introduction, Methods, Results and Discussion with captions, without image pixels or raw kinetic data reanalysis. It supports the RH/2F human-fibroblast context, not every apicomplexan species or stage.
- The native broader-parent definitions support the maintained hierarchy; no unreturned direct GO is_a edge is asserted. COMMON is qualitative, not measured prevalence.
- No complete cargo, fusion-machinery or lipid-species inventory is certified. Transmembrane adhesins have luminal and cytosolic domains; generic cargo storage does not imply entire membrane-spanning complexes are soluble lumen contents.
- Constitutive membrane identity and specific molecular formation necessity remain distinct; no individual lipid-removal requirement is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Original source URL, UTC access and SHA256 retained. No maintained scientific content changed; parent owns finalization.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T022235Z-microneme-lumen-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Microneme lumen boundary and source review
started_at: '2026-10-22T02:03:00Z'
finished_at: '2026-10-22T02:22:35Z'
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
summary: The microneme lumen identity, compartment boundary, cargo-storage context
  and descriptive topology are supported. No concrete curation finding was established.
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
  - path: data/structures/membrane_organelle/microneme.yaml
    sha256: 12358b0b6b393cc14973846c2d86f59e3716f1b9d3513ff2914c3e6b28193cc9
    role: context
  - path: data/structures/membrane_organelle/microneme_lumen.yaml
    sha256: c40d221eea42af12fcb06a6a5dbcc7d3592f289ad31f52a275acad4d6666af38
    role: target
  - path: data/structures/membrane_organelle/microneme_membrane.yaml
    sha256: f3c40aeb98a8d3eec6950ea6a3875db63372a5e72c66a75130e4ec821f0dc4ad
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
- target_id: GO:0034494
  path: data/structures/membrane_organelle/microneme_lumen.yaml
  label: microneme lumen
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/microneme_lumen.yaml
    role: maintained scientific record
scope:
  description: Full target and two frozen boundary neighbors; exact native definitions/taxa,
    source bibliography, complete1997 primary main text and specified review sections.
  selection: Batch32 target4; initial inspect/schema/strict0 before assessment at
    immutable f97b1abe.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0034494
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: just validate data/structures/membrane_organelle/microneme_lumen.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: just validate-strict data/structures/membrane_organelle/microneme_lumen.yaml
    --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/microneme_lumen-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0034494
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: protein-applicability
  name: Protein-example applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0034494
  summary: No protein_examples, gene symbols or GENE_OR_PROTEIN graph nodes occur
    in this boundary record; all graph nodes and references were manually checked.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0034494
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - whole-neighbor
  - boundary-neighbor
  - microneme-agent-go
  - microneme-agent-tax5794
  - microneme-agent-tax5811
  - microneme-agent-carruthers2008-meta
  - microneme-agent-dubois2019-meta
  - microneme-agent-pmid-meta
  - microneme-agent-carruthers1997-pmc
  - microneme-agent-carruthers2008-pmc
  - microneme-agent-dubois2019-unige-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0034494
  summary: '8 of 9 collected target identifiers returned OK. PMID:9208224: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID9208224 (no DOI returned in this native MED row) and Sequential protein
    secretion from three distinct organelles of Toxoplasma gondii accompanies invasion
    of human fibroblasts. Scientific scope remains limited to the separately documented
    inspections. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - microneme-agent-pmid-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0034494
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0034494
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
    and current batch32 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/microneme_lumen.yaml
  locator: Entire maintained target and every function, graph edge and discussion
  accessed_at: '2026-10-22T02:15:55Z'
  support: context_only
  summary: The complete record was read without edits.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, grounding, essentiality and graph/component_ref contract
  accessed_at: '2026-10-22T02:15:55Z'
  support: context_only
  summary: Constituting material and whole cellular structure are distinct; assembly
    necessity is not inferred from biochemical function.
- evidence_id: whole-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/microneme.yaml
  locator: Entire frozen maintained neighbor
  accessed_at: '2026-10-22T02:15:55Z'
  support: context_only
  summary: Read to resolve whole organelle, limiting membrane and lumen boundaries;
    maintained context is not independent experimental support.
- evidence_id: boundary-neighbor
  kind: record_content
  reference: data/structures/membrane_organelle/microneme_membrane.yaml
  locator: Entire frozen maintained neighbor
  accessed_at: '2026-10-22T02:15:55Z'
  support: context_only
  summary: Read to resolve whole organelle, limiting membrane and lumen boundaries;
    maintained context is not independent experimental support.
- evidence_id: microneme-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0020009,GO:0020007,GO:0033163,GO:0034494,GO:0043231,GO:0043233,GO:0031090
  locator: All seven complete labels/definitions/active flags, synonyms and returned
    relations
  accessed_at: '2026-10-22T02:07:36.263194Z'
  support: supports
  summary: Seven active native terms distinguish the microneme, its membrane, its
    lumen, apical complex and broader organelle classes. GO0020009 returns both membrane/lumen
    part_of children; GO0020007 returns microneme part_of; GO0043231 returns microneme
    is_a. Broader lumen/membrane parents are supported by definitions without asserting
    absent direct edges.
  snapshot_sha256: 41bb647bbd29aa18675f16c8daab603b6517136475cef262993198eaf53b58bb
- evidence_id: microneme-agent-tax5794
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5794
  locator: Exact taxId/scientificName/rank and lineage
  accessed_at: '2026-10-22T02:07:37.806555Z'
  support: supports
  summary: ENA confirms Apicomplexa for taxon5794 with its native rank. The receipt
    establishes this identity, not organelle prevalence or experimental strain equivalence.
  snapshot_sha256: 71f50f7adf0b7ad8670573c6c6ac0e6df37a9cf467fdec2ab20d612db477bc53
- evidence_id: microneme-agent-tax5811
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5811
  locator: Exact taxId/scientificName/rank and lineage
  accessed_at: '2026-10-22T02:07:36.265008Z'
  support: supports
  summary: ENA confirms Toxoplasma gondii for taxon5811 with its native rank. The
    receipt establishes this identity, not organelle prevalence or experimental strain
    equivalence.
  snapshot_sha256: 11679825fa4d00b18d5848862450ab6b3770aaa47ad6676d1196d9df61124b16
- evidence_id: microneme-agent-carruthers2008-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1007%2F978-0-387-78267-6_2%22&format=json&resultType=core&pageSize=100
  locator: Exact MED DOI/title/authors/year/PMID and complete abstract
  accessed_at: '2026-10-22T02:07:41.322031Z'
  support: supports
  summary: Exact native bibliographic identity and complete abstract read for carruthers2008.
    Literature-review tier.
  snapshot_sha256: ab6fafa3d16039e85cba04114d282d8fd731080a98c01f6ad689923b03097773
- evidence_id: microneme-agent-dubois2019-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fcmi.13018%22&format=json&resultType=core&pageSize=100
  locator: Exact MED DOI/title/authors/year/PMID and complete abstract
  accessed_at: '2026-10-22T02:07:41.322440Z'
  support: supports
  summary: Exact native bibliographic identity and complete abstract read for dubois2019.
    Literature-review tier.
  snapshot_sha256: 1c775eb76c36272e9dd1bdd9d87ba8031e85698b78fa8a59ebc2ef240555a9be
- evidence_id: microneme-agent-pmid-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=EXT_ID%3A%289208224+OR+11157983+OR+15684324+OR+18818666+OR+11083833+OR+11087913+OR+16102004%29+AND+SRC%3AMED&format=json&resultType=core&pageSize=100
  locator: Exact requested MED result(s), identity and complete abstracts
  accessed_at: '2026-10-22T02:07:42.893923Z'
  support: supports
  summary: Exact MED PMID9208224 identifies Carruthers and Sibley1997 and its complete
    abstract. Only this result is used for this target; the bundled response also
    contains other microneme localization papers.
  snapshot_sha256: a718ae89432c8ce95186c3ec73eef8a97596738f94f2f1ecad65fa11385fd463
- evidence_id: microneme-agent-carruthers1997-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC13475723/
  locator: Complete Introduction S1, Methods S2/S3–11, Results S12/S13–18 and Discussion
    S19, including Figures1–8 captions. No figure pixels or original kinetic data
    reanalysis.
  accessed_at: '2026-10-22T02:08:17.008565Z'
  support: supports
  summary: The recovered author manuscript reports RH/2F tachyzoites invading human
    fibroblasts. MIC2 secretion accompanies initial contact, before rhoptry and dense-granule
    release. It establishes the sequential-secretion model, not MIC2–M2AP perturbation
    or PKG signaling experiments.
  snapshot_sha256: 534e8dec49982ff6fc5f100019b7a67e32ce32ea3c0748d3172faa8fdda784b6
- evidence_id: microneme-agent-carruthers2008-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC2847500/
  locator: Complete Introduction S1, Oligomerization of MIC proteins S9 and Organization
    of MIC ligands within micronemes S10, including embedded Figure1 caption; no full
    review-body or pixel claim.
  accessed_at: '2026-10-22T02:08:17.005581Z'
  support: supports
  summary: The review describes stage/species variation, including Theileria zoites
    without micronemes; qualitative common occurrence is not universality. S9 distinguishes
    soluble M2AP from transmembrane MIC2 and its cytoplasmic targeting tail; S10 describes
    poorly resolved lumen organization and condensed contents.
  snapshot_sha256: f0962cd32d71c94fb036a77db99fd2a6a9343490b30c6f61fa2ffa43be841bdf
- evidence_id: microneme-agent-dubois2019-unige-pdf
  kind: authority
  reference: https://access.archive-ouverte.unige.ch/access/metadata/8d9f50fe-0548-4e4f-bc29-4b05a43e7ddc/download
  locator: 'Accepted author manuscript: Abstract, Introduction, Microneme diversity/structure,
    Contents/conservation, Biogenesis/maturation/trafficking, Signaling cascade, Preparing
    for secretion, Fusion, Insights from other organisms and Concluding remarks. Table1
    and figure pixels not comprehensively inspected.'
  accessed_at: '2026-10-22T02:09:12.638985Z'
  support: supports
  summary: The accepted review manuscript supports varied microneme architecture,
    adhesin complexes, protein sorting and regulated exocytosis. It separates signaling
    evidence from speculative docking/fusion models and the unrelated exoneme/mononeme
    classes. It does not establish a universal lipid recipe or a complete fusion machinery.
  snapshot_sha256: 32ce8f7b82f399bc5d27f4355f92b71e3a06f10487ce667af70f2d0810317e0c
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/microneme_lumen.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:03:02Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/microneme_lumen.yaml'
  snapshot_sha256: e7a42c1d98be182adfdd7b1df88ee6e92894c34e416f077aab38a1d0a5a3f4f3
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/microneme_lumen.yaml
    --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/microneme_lumen-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:03:03Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/microneme_lumen.yaml\
    \ --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/microneme_lumen-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch32-20261022-k96_2wx1/microneme_lumen-strict.tsv"
  snapshot_sha256: db6ff0f83c0d3397b757a337eb3b8ce0434098941de3e4144b4b6979bd32d3e6
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/microneme_lumen.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 9 collected target identifiers returned OK. PMID:9208224: UNREACHABLE;
    The bulk transport returned414; the independently retrieved exact MED identity
    confirms PMID9208224 (no DOI returned in this native MED row) and Sequential protein
    secretion from three distinct organelles of Toxoplasma gondii accompanies invasion
    of human fibroblasts. Scientific scope remains limited to the separately documented
    inspections. Native source checks are separately scoped; skipped or unreachable
    identifiers are not silently counted as resolved.'
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
  topic: Exact boundary class and hierarchy
  outcome: supported
  target_ids:
  - GO:0034494
  summary: GO0034494 denotes only the enclosed volume; GO0043233 is a compatible broader
    lumen class. The microneme part relation is explicit in the returned whole-organelle
    child relations. No unsupported direct native edge is inferred from the broader-parent
    definition.
  evidence_ids:
  - record
  - microneme-agent-go
  - whole-neighbor
  - boundary-neighbor
- assessment_id: composition
  area: grounding
  topic: Region without permanent cargo constituents
  outcome: supported
  target_ids:
  - GO:0034494
  summary: The record leaves this spatial compartment without components and keeps
    the boundary membrane outside the lumen. Its generic storage statement concerns
    soluble cargo or luminal cargo portions, not a claim that every transmembrane
    adhesin or the entire MIC2–M2AP complex lies wholly in the lumen. The adjacent
    whole-record topology concern is not imported into this record.
  evidence_ids:
  - record
  - schema
  - microneme-agent-go
  - microneme-agent-carruthers2008-pmc
  - microneme-agent-dubois2019-unige-pdf
  - whole-neighbor
  - boundary-neighbor
- assessment_id: scope
  area: scope
  topic: Apicomplexan occurrence and Toxoplasma example
  outcome: supported
  target_ids:
  - GO:0034494
  summary: The review supports qualitative COMMON occurrence with species and life-stage
    variation, including absent micronemes in Theileria zoites. The exact Toxoplasma
    example is supported by the RH/2F fibroblast-invasion study. Taxon identities
    are verified independently; no prevalence count or every-stage universality is
    claimed.
  evidence_ids:
  - record
  - microneme-agent-carruthers2008-pmc
  - microneme-agent-dubois2019-unige-pdf
  - microneme-agent-carruthers1997-pmc
  - microneme-agent-tax5794
  - microneme-agent-tax5811
- assessment_id: function
  area: evidence
  topic: Secretory cargo storage
  outcome: supported
  target_ids:
  - GO:0034494
  summary: The enclosed secretory volume stores cargo before regulated discharge.
    Carruthers2008 describes lumenal contents and the1997 study demonstrates timed
    MIC2 redistribution; membrane-associated adhesins are not relabeled entirely soluble.
  evidence_ids:
  - record
  - microneme-agent-go
  - microneme-agent-carruthers2008-pmc
  - microneme-agent-dubois2019-unige-pdf
  - microneme-agent-carruthers1997-pmc
- assessment_id: graph
  area: graph
  topic: Two descriptive topology edges
  outcome: supported
  target_ids:
  - GO:0034494
  summary: The two NONMECHANISTIC edges correctly place the lumen within the organelle
    and inside its bounding membrane. No molecular causal sequence or permanent cargo
    inventory is asserted.
  evidence_ids:
  - record
  - microneme-agent-go
  - microneme-agent-carruthers1997-pmc
  - microneme-agent-dubois2019-unige-pdf
- assessment_id: completeness
  area: completeness
  topic: Bounded optional detail
  outcome: supported
  target_ids:
  - GO:0034494
  summary: No obligatory missing component or unverified exact mapping is established.
    The resolved boundary interpretation is correctly implemented; temporary cargo
    does not require constituent rows.
  evidence_ids:
  - record
  - schema
  - microneme-agent-go
  - microneme-agent-dubois2019-unige-pdf
findings: []
actions: []
limitations:
- Carruthers2008 and Dubois2019 are review-tier. Only Carruthers S1/S9/S10 were read
  in full; Dubois accepted-manuscript scientific main text was inspected, without
  a comprehensive Table1 or image analysis. Publisher403 remains an access-route limit,
  not absence of the recovered accepted text.
- The1997 primary author manuscript was read through Introduction, Methods, Results
  and Discussion with captions, without image pixels or raw kinetic data reanalysis.
  It supports the RH/2F human-fibroblast context, not every apicomplexan species or
  stage.
- The native broader-parent definitions support the maintained hierarchy; no unreturned
  direct GO is_a edge is asserted. COMMON is qualitative, not measured prevalence.
- No complete cargo, fusion-machinery or lipid-species inventory is certified. Transmembrane
  adhesins have luminal and cytosolic domains; generic cargo storage does not imply
  entire membrane-spanning complexes are soluble lumen contents.
- Constitutive membrane identity and specific molecular formation necessity remain
  distinct; no individual lipid-removal requirement is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- Original source URL, UTC access and SHA256 retained. No maintained scientific content
  changed; parent owns finalization.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
