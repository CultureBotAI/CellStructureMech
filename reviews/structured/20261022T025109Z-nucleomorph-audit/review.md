# Scientific review of nucleomorph

- Review: 20261022T025109Z-nucleomorph-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:36:38Z
- Finished UTC: 2026-10-22T02:51:09Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact nucleomorph identity, lineage scope, retained chromosomes and G.theta replication example are supported. No concrete issue observed; individual assembly requirements and optional inventory remain unresolved.

## Scope And Provenance

Entire single maintained target at frozen f97b1abe; exact source identities, taxonomy, component/formation distinctions, function, evidence placement, completeness and all asserted graph/image fields.

Selection: Batch35 fixed strict path-order selection, position 8; one maintained record only. Initial focused inspect/schema/strict all passed before review.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0033009 | data/structures/membrane_organelle/nucleomorph.yaml | maintained | nucleomorph |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0033009 | Focused validator passed. |
| Focused native strict | passed | True | GO:0033009 | Focused validator passed. |
| Native focused graph protein-reference check | passed | True | GO:0033009 | Native check passed; all graph edges independently read. |
| Individual protein verification applicability | not_applicable | False | GO:0033009 | No structured individual protein example, gene-symbol field or UniProt protein accession is asserted. Named source proteins are checked against the actual primary passage; optional instance enrichment is not required. |
| Expression-module applicability | not_applicable | False | GO:0033009 | No expression-module/regulon claim or covered strain transcriptomic inference is made. |
| Claim-level scientific review | passed | True | GO:0033009 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0033009 | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0033009 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0033009 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0033009 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0033009 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0033009 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact nucleomorph and hierarchy

identity: supported. Targets: GO:0033009.

Native GO directly supports the vestigial nucleus identity, intracellular membrane-bounded class and plastid parthood. Related residual/remnant synonyms describe endosymbiont nuclei and do not confuse the nucleus with a genome alone.

### Algal lineages and canonical species

scope: supported. Targets: GO:0033009.

Native taxa match both classes and examples. Cited studies explicitly discuss nucleomorph retention in cryptophytes and chlorarachniophytes and directly study G.theta/B.natans or L.oceanica. COMMON is interpreted qualitatively as a characteristic retained structure, not a measured all-species census; no universal occurrence is claimed.

### Collective retained chromosome identity

grounding: supported. Targets: GO:0033009.

The DNA component is the residual endosymbiont genome, directly supported by genome sequencing. Three linear chromosomes are explicitly documented in L.oceanica. Reviewed-label-only avoids inventing a nucleomorph-specific chromosome CURIE; the target does not assert a particular gene's individual assembly requirement.

### Formation necessity distinguished from gene function

grounding: unknown. Targets: GO:0033009.

The retained chromosome complement is constitutive of this genome-containing vestigial nucleus, but the cited genome comparisons do not test removal of that complement or prove an individual chromosome/gene is required to build an envelope. ESSENTIAL must retain the schema's formation meaning; experimental formation necessity and exact individual requirements remain unknown, not inferred from essential-gene language.

### Genome retention and bounded replication example

evidence: supported. Targets: GO:0033009.

The source supports remnant genome retention and the G.theta cell-cycle replication example. The record's function and final edge explicitly name G.theta; graph scope_notes labels this as an example. No detailed envelope formation or replication machinery is asserted.

### All four NONMECHANISTIC edges

graph: supported. Targets: GO:0033009.

Chromosomes housed in nucleomorph, nucleomorph part of plastid, residual gene encoding and the explicitly G.theta replication edge agree with the authorities and primary studies. The graph is appropriately NONMECHANISTIC and its general description is read with the express example scope.

### Full record and acknowledged inventory boundaries

completeness: supported. Targets: GO:0033009.

Entire target and all evidence placements were read. No maintained image, numerical size claim, individual protein accession or gene-symbol instance is asserted. Envelope/pore/division machinery remains a bounded TODO; an empty optional inventory is not an observed defect. No exact cross-lineage chemical or chromosome mapping is invented.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/nucleomorph.yaml; Entire maintained target, including all history, graph nodes/edges, evidence notes and discussions | context_only | All target bytes read; no maintained scientific content changed. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent and grounding; ComponentTypeEnum; EssentialityEnum and PresenceEnum | context_only | OTHER is expressly allowed without a chemical description. LIPID groundings concern a molecular lipid identity; a whole anatomical membrane is a distinct entity. Essentiality means whether the structure forms without the constituent, not cell survival or catalytic function. |
| nucleomorph-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033009,GO:0043231,GO:0009536; All three complete QuickGO entries: definitions, names, obsolete flags and relation-labelled children | supports | The active nucleomorph term exactly matches the definition. GO0043231 returns nucleomorph as an is_a child; GO0009536 returns it as a part_of child. These distinct relations support intracellular membrane-bounded parentage and plastid parthood. |
| nucleomorph-agent-tax3027 | https://rest.uniprot.org/taxonomy/3027.json; Complete native taxonId, scientificName, active, rank, names and lineage | supports | Cryptophyceae is active class3027. Protein statistics are not a prevalence or constituent inventory. |
| nucleomorph-agent-tax29197 | https://rest.uniprot.org/taxonomy/29197.json; Complete native taxonId, scientificName, active, rank, names and lineage | supports | Chlorarachniophyceae is active class29197. Protein statistics are not a prevalence or constituent inventory. |
| nucleomorph-agent-tax55529 | https://rest.uniprot.org/taxonomy/55529.json; Complete native taxonId, scientificName, active, rank, names and lineage | supports | Guillardia theta is active species55529, with Cryptomonas phi synonym and Cryptophyceae lineage. Protein statistics are not a prevalence or constituent inventory. |
| nucleomorph-agent-tax227086 | https://rest.uniprot.org/taxonomy/227086.json; Complete native taxonId, scientificName, active, rank, names and lineage | supports | Bigelowiella natans is active species227086 in Chlorarachniophyceae; older alternative names do not change this identity. Protein statistics are not a prevalence or constituent inventory. |
| nucleomorph-agent-curtis2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/nature11681; Unique native bibliographic result and complete abstractText | supports | Exact DOI, PMID23201678, title, authors/year and complete abstract match the cited primary article. |
| nucleomorph-agent-onuma2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1038/s41598-017-02668-2; Unique native bibliographic result and complete abstractText | supports | Exact DOI, PMID28539635, title, authors/year and complete abstract match the cited primary article. |
| nucleomorph-agent-tanifuji2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A10.1186/1471-2164-15-374; Unique native bibliographic result and complete abstractText | supports | Exact DOI, PMID24885563, title, authors/year and complete abstract match the cited primary article. |
| nucleomorph-agent-curtis2012-publisher | https://doi.org/10.1038/nature11681; Abstract, Main and Fig1 caption; Why do nucleomorphs persist? complete section; Methods Summary; genuine publisher article body, no supplemental genome data or figure pixels | supports | The primary study compares G.theta and B.natans and interprets retained genes in remnant nuclei alongside a lack of recent nucleomorph-to-nucleus transfers. Its essential-gene inference concerns retained biological function, not a chromosome-removal test of organelle formation. |
| nucleomorph-agent-tanifuji2014-publisher | https://doi.org/10.1186/1471-2164-15-374; Background; Results and discussion Sec3 and first genome-comparison paragraphs; Fig1 caption and Table1 context; Methods Sec11–13; no uninspected supplements or raw sequence reanalysis | supports | Background places nucleomorphs in the PPC between plastid membrane pairs with independent red/green origins. Results directly resolve L.oceanica into three linear chromosomes, with repeat-copy/size uncertainty explicitly retained. Methods specify CCMP622 and enriched DNA sequencing/assembly verification. |
| nucleomorph-agent-onuma2017-publisher | https://doi.org/10.1038/s41598-017-02668-2; Abstract; Results Sec3–6 and Fig2–5 captions, specifically Sec5 EdU and cell-cycle paragraphs; Discussion Sec8–10; Methods Sec13–18; figures as text/captions, not pixels or supplements | supports | G.theta CCMP2712 cultures were synchronized by 8h-light/16h-dark cycles; roughly30% divided in that cycle. EdU timing places nucleomorph replication later and longer than host nuclear S-phase. This supports the expressly G.theta replication example; the paper discusses comparative regulation without resolving every lineage's machinery. |
| schema-result | just validate data/structures/membrane_organelle/nucleomorph.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/nucleomorph.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/nucleomorph.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/nucleomorph.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-strict.tsv |
| focused-causal | /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/nucleomorph.yaml; /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-agent/nucleomorph-causal.log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/nucleomorph.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Primary bodies were read only at the explicit locators; no raw genome/EdU reanalysis, source figure-pixel inspection or supplements were performed. Exact L.oceanica chromosomeI repeat number is unresolved in its source and is not generalized.
- COMMON is a qualitative lineage characterization, not a quantitative strain census. The G.theta synchronization experiment is not treated as a demonstrated universal replication mechanism.
- The chromosome complement is a defining collective constituent of the vestigial nucleus. The source does not experimentally establish organelle formation without that genome, nor individual chromosome/gene necessity; essential-gene retention and formation essentiality remain distinct.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025109Z-nucleomorph-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of nucleomorph
started_at: '2026-10-22T02:36:38Z'
finished_at: '2026-10-22T02:51:09Z'
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
summary: Exact nucleomorph identity, lineage scope, retained chromosomes and G.theta
  replication example are supported. No concrete issue observed; individual assembly
  requirements and optional inventory remain unresolved.
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
  - path: data/structures/membrane_organelle/nucleomorph.yaml
    sha256: 9653087b981991e28b537ec1eb809e442f5215f4ff4c994687106b74ed6338ad
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
- target_id: GO:0033009
  path: data/structures/membrane_organelle/nucleomorph.yaml
  label: nucleomorph
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nucleomorph.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target at frozen f97b1abe; exact source identities,
    taxonomy, component/formation distinctions, function, evidence placement, completeness
    and all asserted graph/image fields.
  selection: Batch35 fixed strict path-order selection, position 8; one maintained
    record only. Initial focused inspect/schema/strict all passed before review.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0033009
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: just validate data/structures/membrane_organelle/nucleomorph.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: just validate-strict data/structures/membrane_organelle/nucleomorph.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal
  name: Native focused graph protein-reference check
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/nucleomorph.yaml
  exit_code: 0
  summary: Native check passed; all graph edges independently read.
  evidence_ids:
  - focused-causal
- check_id: protein-verification
  name: Individual protein verification applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0033009
  summary: No structured individual protein example, gene-symbol field or UniProt
    protein accession is asserted. Named source proteins are checked against the actual
    primary passage; optional instance enrichment is not required.
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0033009
  summary: No expression-module/regulon claim or covered strain transcriptomic inference
    is made.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0033009
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - nucleomorph-agent-go
  - nucleomorph-agent-tax3027
  - nucleomorph-agent-tax29197
  - nucleomorph-agent-tax55529
  - nucleomorph-agent-tax227086
  - nucleomorph-agent-curtis2012-meta
  - nucleomorph-agent-onuma2017-meta
  - nucleomorph-agent-tanifuji2014-meta
  - nucleomorph-agent-curtis2012-publisher
  - nucleomorph-agent-tanifuji2014-publisher
  - nucleomorph-agent-onuma2017-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0033009
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0033009
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0033009
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
    and current batch35 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/nucleomorph.yaml
  locator: Entire maintained target, including all history, graph nodes/edges, evidence
    notes and discussions
  accessed_at: '2026-10-22T02:45:16Z'
  support: context_only
  summary: All target bytes read; no maintained scientific content changed.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent and grounding; ComponentTypeEnum; EssentialityEnum
    and PresenceEnum
  accessed_at: '2026-10-22T02:45:16Z'
  support: context_only
  summary: OTHER is expressly allowed without a chemical description. LIPID groundings
    concern a molecular lipid identity; a whole anatomical membrane is a distinct
    entity. Essentiality means whether the structure forms without the constituent,
    not cell survival or catalytic function.
- evidence_id: nucleomorph-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0033009,GO:0043231,GO:0009536
  locator: 'All three complete QuickGO entries: definitions, names, obsolete flags
    and relation-labelled children'
  accessed_at: '2026-10-22T02:37:49.494023Z'
  support: supports
  summary: The active nucleomorph term exactly matches the definition. GO0043231 returns
    nucleomorph as an is_a child; GO0009536 returns it as a part_of child. These distinct
    relations support intracellular membrane-bounded parentage and plastid parthood.
  snapshot_sha256: fa62ce2f1dd74c24918af8eec74183c993358e73a9bac90bd22cf2bc1c5c9fd4
- evidence_id: nucleomorph-agent-tax3027
  kind: database
  reference: https://rest.uniprot.org/taxonomy/3027.json
  locator: Complete native taxonId, scientificName, active, rank, names and lineage
  accessed_at: '2026-10-22T02:37:49.871370Z'
  support: supports
  summary: Cryptophyceae is active class3027. Protein statistics are not a prevalence
    or constituent inventory.
  snapshot_sha256: 72a0682db96631ffc9f0b222e6bcace19f918d59866e3502ad92a9ba166292f5
- evidence_id: nucleomorph-agent-tax29197
  kind: database
  reference: https://rest.uniprot.org/taxonomy/29197.json
  locator: Complete native taxonId, scientificName, active, rank, names and lineage
  accessed_at: '2026-10-22T02:37:50.088860Z'
  support: supports
  summary: Chlorarachniophyceae is active class29197. Protein statistics are not a
    prevalence or constituent inventory.
  snapshot_sha256: 0947ed25a593cee9efd92ef0f889209a8f51e282940663b4ba775d61f1fe7dcf
- evidence_id: nucleomorph-agent-tax55529
  kind: database
  reference: https://rest.uniprot.org/taxonomy/55529.json
  locator: Complete native taxonId, scientificName, active, rank, names and lineage
  accessed_at: '2026-10-22T02:37:50.115230Z'
  support: supports
  summary: Guillardia theta is active species55529, with Cryptomonas phi synonym and
    Cryptophyceae lineage. Protein statistics are not a prevalence or constituent
    inventory.
  snapshot_sha256: 0c0ebfc3e6aeb0b277d2eec1eaa17b7b81ddfb09ba1ee6be5814826d943aad24
- evidence_id: nucleomorph-agent-tax227086
  kind: database
  reference: https://rest.uniprot.org/taxonomy/227086.json
  locator: Complete native taxonId, scientificName, active, rank, names and lineage
  accessed_at: '2026-10-22T02:37:50.145718Z'
  support: supports
  summary: Bigelowiella natans is active species227086 in Chlorarachniophyceae; older
    alternative names do not change this identity. Protein statistics are not a prevalence
    or constituent inventory.
  snapshot_sha256: bf5947b51ae6bd528dd7dc8630de62d8fa712f5dc95489505731dcff7bfd52ec
- evidence_id: nucleomorph-agent-curtis2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/nature11681
  locator: Unique native bibliographic result and complete abstractText
  accessed_at: '2026-10-22T02:37:46.050320Z'
  support: supports
  summary: Exact DOI, PMID23201678, title, authors/year and complete abstract match
    the cited primary article.
  snapshot_sha256: 187eeecf784d6521b01600f87a0d80a12bda612db852b4d9462bfc3aedffbf95
- evidence_id: nucleomorph-agent-onuma2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1038/s41598-017-02668-2
  locator: Unique native bibliographic result and complete abstractText
  accessed_at: '2026-10-22T02:37:46.503223Z'
  support: supports
  summary: Exact DOI, PMID28539635, title, authors/year and complete abstract match
    the cited primary article.
  snapshot_sha256: 91680ec1cb7b926740215827656f4a5b632d1687b208c16b5a82eea622176dc5
- evidence_id: nucleomorph-agent-tanifuji2014-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A10.1186/1471-2164-15-374
  locator: Unique native bibliographic result and complete abstractText
  accessed_at: '2026-10-22T02:37:46.757564Z'
  support: supports
  summary: Exact DOI, PMID24885563, title, authors/year and complete abstract match
    the cited primary article.
  snapshot_sha256: fc447dac178fc4a5e934ff0987fba3dcdbb0fb15c141a5b2ca0ccb41071231cb
- evidence_id: nucleomorph-agent-curtis2012-publisher
  kind: primary_source
  reference: https://doi.org/10.1038/nature11681
  locator: Abstract, Main and Fig1 caption; Why do nucleomorphs persist? complete
    section; Methods Summary; genuine publisher article body, no supplemental genome
    data or figure pixels
  accessed_at: '2026-10-22T02:37:46.494651Z'
  support: supports
  summary: The primary study compares G.theta and B.natans and interprets retained
    genes in remnant nuclei alongside a lack of recent nucleomorph-to-nucleus transfers.
    Its essential-gene inference concerns retained biological function, not a chromosome-removal
    test of organelle formation.
  snapshot_sha256: 3c87b5b2a4b8b503b381777d2016f92a629b1c583fcfffd2ad764b653e74ffa2
- evidence_id: nucleomorph-agent-tanifuji2014-publisher
  kind: primary_source
  reference: https://doi.org/10.1186/1471-2164-15-374
  locator: Background; Results and discussion Sec3 and first genome-comparison paragraphs;
    Fig1 caption and Table1 context; Methods Sec11–13; no uninspected supplements
    or raw sequence reanalysis
  accessed_at: '2026-10-22T02:37:47.136535Z'
  support: supports
  summary: Background places nucleomorphs in the PPC between plastid membrane pairs
    with independent red/green origins. Results directly resolve L.oceanica into three
    linear chromosomes, with repeat-copy/size uncertainty explicitly retained. Methods
    specify CCMP622 and enriched DNA sequencing/assembly verification.
  snapshot_sha256: 9cdf863325574a5942c4cfab55d2a897f707d7e57ced94b3773eb11e5f7778bf
- evidence_id: nucleomorph-agent-onuma2017-publisher
  kind: primary_source
  reference: https://doi.org/10.1038/s41598-017-02668-2
  locator: Abstract; Results Sec3–6 and Fig2–5 captions, specifically Sec5 EdU and
    cell-cycle paragraphs; Discussion Sec8–10; Methods Sec13–18; figures as text/captions,
    not pixels or supplements
  accessed_at: '2026-10-22T02:37:46.545938Z'
  support: supports
  summary: G.theta CCMP2712 cultures were synchronized by 8h-light/16h-dark cycles;
    roughly30% divided in that cycle. EdU timing places nucleomorph replication later
    and longer than host nuclear S-phase. This supports the expressly G.theta replication
    example; the paper discusses comparative regulation without resolving every lineage's
    machinery.
  snapshot_sha256: 7f480d5d8f843218c398cf2d29de7c30ef0e7ac971c5fee70fd566f2553c5032
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/nucleomorph.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:39Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/nucleomorph.yaml'
  snapshot_sha256: ac25de6d18c96a94bd6c3d3618136397a43b59d4c9caf5cf8ba6cc7225b9328d
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/nucleomorph.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:40Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/nucleomorph.yaml\
    \ --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-strict.tsv"
  snapshot_sha256: 7b86ddc0f145efb76f5f0098b6a7f66930a9b46f6df4d4bbe5b8fbd95a9b2dd3
- evidence_id: focused-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/nucleomorph.yaml
  locator: /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nucleomorph-agent/nucleomorph-causal.log
  accessed_at: '2026-10-22T02:42:27.520093Z'
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
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/nucleomorph.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 10 of 10 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
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
  topic: Exact nucleomorph and hierarchy
  outcome: supported
  target_ids:
  - GO:0033009
  summary: Native GO directly supports the vestigial nucleus identity, intracellular
    membrane-bounded class and plastid parthood. Related residual/remnant synonyms
    describe endosymbiont nuclei and do not confuse the nucleus with a genome alone.
  evidence_ids:
  - nucleomorph-agent-go
  - nucleomorph-agent-curtis2012-publisher
  - nucleomorph-agent-tanifuji2014-publisher
- assessment_id: scope
  area: scope
  topic: Algal lineages and canonical species
  outcome: supported
  target_ids:
  - GO:0033009
  summary: Native taxa match both classes and examples. Cited studies explicitly discuss
    nucleomorph retention in cryptophytes and chlorarachniophytes and directly study
    G.theta/B.natans or L.oceanica. COMMON is interpreted qualitatively as a characteristic
    retained structure, not a measured all-species census; no universal occurrence
    is claimed.
  evidence_ids:
  - nucleomorph-agent-tax3027
  - nucleomorph-agent-tax29197
  - nucleomorph-agent-tax55529
  - nucleomorph-agent-tax227086
  - nucleomorph-agent-curtis2012-publisher
  - nucleomorph-agent-tanifuji2014-publisher
  - nucleomorph-agent-onuma2017-publisher
- assessment_id: composition
  area: grounding
  topic: Collective retained chromosome identity
  outcome: supported
  target_ids:
  - GO:0033009
  summary: The DNA component is the residual endosymbiont genome, directly supported
    by genome sequencing. Three linear chromosomes are explicitly documented in L.oceanica.
    Reviewed-label-only avoids inventing a nucleomorph-specific chromosome CURIE;
    the target does not assert a particular gene's individual assembly requirement.
  evidence_ids:
  - nucleomorph-agent-curtis2012-publisher
  - nucleomorph-agent-tanifuji2014-publisher
  - record
  - schema
- assessment_id: formation
  area: grounding
  topic: Formation necessity distinguished from gene function
  outcome: unknown
  target_ids:
  - GO:0033009
  summary: The retained chromosome complement is constitutive of this genome-containing
    vestigial nucleus, but the cited genome comparisons do not test removal of that
    complement or prove an individual chromosome/gene is required to build an envelope.
    ESSENTIAL must retain the schema's formation meaning; experimental formation necessity
    and exact individual requirements remain unknown, not inferred from essential-gene
    language.
  evidence_ids:
  - nucleomorph-agent-curtis2012-publisher
  - nucleomorph-agent-tanifuji2014-publisher
  - schema
  - record
- assessment_id: functions
  area: evidence
  topic: Genome retention and bounded replication example
  outcome: supported
  target_ids:
  - GO:0033009
  summary: The source supports remnant genome retention and the G.theta cell-cycle
    replication example. The record's function and final edge explicitly name G.theta;
    graph scope_notes labels this as an example. No detailed envelope formation or
    replication machinery is asserted.
  evidence_ids:
  - nucleomorph-agent-curtis2012-publisher
  - nucleomorph-agent-onuma2017-publisher
  - nucleomorph-agent-tanifuji2014-publisher
- assessment_id: graph
  area: graph
  topic: All four NONMECHANISTIC edges
  outcome: supported
  target_ids:
  - GO:0033009
  summary: Chromosomes housed in nucleomorph, nucleomorph part of plastid, residual
    gene encoding and the explicitly G.theta replication edge agree with the authorities
    and primary studies. The graph is appropriately NONMECHANISTIC and its general
    description is read with the express example scope.
  evidence_ids:
  - nucleomorph-agent-go
  - nucleomorph-agent-tanifuji2014-publisher
  - nucleomorph-agent-curtis2012-publisher
  - nucleomorph-agent-onuma2017-publisher
  - record
- assessment_id: coverage
  area: completeness
  topic: Full record and acknowledged inventory boundaries
  outcome: supported
  target_ids:
  - GO:0033009
  summary: Entire target and all evidence placements were read. No maintained image,
    numerical size claim, individual protein accession or gene-symbol instance is
    asserted. Envelope/pore/division machinery remains a bounded TODO; an empty optional
    inventory is not an observed defect. No exact cross-lineage chemical or chromosome
    mapping is invented.
  evidence_ids:
  - record
  - schema
  - nucleomorph-agent-go
  - nucleomorph-agent-curtis2012-publisher
  - nucleomorph-agent-tanifuji2014-publisher
  - nucleomorph-agent-onuma2017-publisher
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Primary bodies were read only at the explicit locators; no raw genome/EdU reanalysis,
  source figure-pixel inspection or supplements were performed. Exact L.oceanica chromosomeI
  repeat number is unresolved in its source and is not generalized.
- COMMON is a qualitative lineage characterization, not a quantitative strain census.
  The G.theta synchronization experiment is not treated as a demonstrated universal
  replication mechanism.
- The chromosome complement is a defining collective constituent of the vestigial
  nucleus. The source does not experimentally establish organelle formation without
  that genome, nor individual chromosome/gene necessity; essential-gene retention
  and formation essentiality remain distinct.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
