# Macronucleus identity, source and topology review

- Review: 20261022T021711Z-macronucleus-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T01:50:51Z
- Finished UTC: 2026-10-22T02:17:11Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed within the explicitly bounded source scope.

## Scope And Provenance

Entire single target: identity, hierarchy/parthood, material boundaries, source and taxonomic claims, examples, functions and every graph edge.

Selection: Target 7 of batch thirty-one in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0031039 | data/structures/membrane_organelle/macronucleus.yaml | maintained | macronucleus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0031039 | Focused native check passed; scientific scope assessed separately. |
| Native protein causal-graphs | passed | True | GO:0031039 | Focused native check passed; scientific scope assessed separately. |
| Focused native schema | passed | True | GO:0031039 | Focused validator passed. |
| Focused native strict | passed | True | GO:0031039 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0031039 | No expression-module claim or dataset is used. Genome preparation, compartment topology and direct recruitment sources apply. |
| Claim-level scientific review | passed | True | GO:0031039 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0031039 | 4 of 4 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0031039 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0031039 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0031039 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0031039 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0031039 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact structure and mereology

identity: supported. Targets: GO:0031039.

Native definitions and relations support macronucleus identity and nucleus ancestry, distinct from micronucleus and from DNA material.

### Molecular material versus whole compartment

grounding: supported. Targets: GO:0031039.

Macronuclear DNA explicitly denotes processed/amplified DNA rather than the complete GO nuclear chromosome. Label-only grounding and the open SO question preserve that distinction.

### Constitutive material versus experimental formation necessity

grounding: unknown. Targets: GO:0031039.

The DNA constituent is defining material of the macronucleus, and the inspected genome study supports its presence and processing. It does not experimentally test whether the macronucleus forms without this collective DNA component; chromosome sequencing and ontology definitions do not establish an assembly requirement.

### Taxon and actual experimental context

scope: supported. Targets: GO:0031039.

SB210 and purified-MAC shotgun preparation match the primary methods. Somatic expression is scoped to Tetrahymena asexual growth; no universal ciliate genome architecture is inferred.

### Bounded functional evidence

evidence: supported. Targets: GO:0031039.

GO and the primary Introduction support vegetative somatic gene expression; the genome paper is not a newly observed developmental perturbation assay.

### Every target graph edge

graph: supported. Targets: GO:0031039.

All three descriptive edges express DNA on chromosomes housed within MAC, DNA supporting somatic expression and MAC transcriptional function. The first predicate is read with its explicit description, which does not place DNA on the nuclear exterior. No developmental or pore mechanism is asserted.

### Unresolved inventories and evidence tiers

evidence: unknown. Targets: GO:0031039.

No complete molecular inventory, quantitative prevalence or isolated physical sufficiency experiment is established. Primary abstracts, selected primary-body sections and review synthesis retain distinct evidentiary roles.

### All maintained fields and native status

completeness: supported. Targets: GO:0031039.

Entire target, all graph edges, source placements, discussions and history inspected. No maintained image asset, numeric physical property, trait link, protein example or verbatim snippet is asserted. PROPOSED remains unchanged; historic issue closures are not independently recertified.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/macronucleus.yaml; Entire maintained target, all sources, examples, graph edges, discussions and history | context_only | Full target read; no scientific record or native status changed. |
| policy | docs/CURATION.md; Exact identity, hierarchy versus parthood and narrow source support | context_only | Whole structures, enclosed volumes and molecular material remain distinct; optional inventories do not require speculative completion. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, graph nodes and essentiality | context_only | Constitutive boundary material is not a knockout assertion about every chemical species. A descriptive graph still needs support at each edge. |
| root31-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005770,GO:0005768,GO:0005771,GO:0010008,GO:0031904,GO:0031906,GO:0031902,GO:0071985,GO:0000813,GO:0000814,GO:0000815,GO:0031039,GO:0005634,GO:0000228; Complete names, definitions, synonyms, active flags and all returned child relations for fourteen identifiers | supports | All fourteen active native entries were read. GO0005770 is an endosome child with MVB as an is_a child. Exact membrane0031902 and lumen0031906 are late-endosome parts, with direct generic membrane/lumen parents. GO0071985 describes MVB luminal-vesicle cargo entry. ESCRT definitions match the sorting context. Macronucleus0031039 denotes the transcriptional polyploid ciliate compartment, distinct from nuclear chromosome0000228. |
| root31-sources-eisen2006-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1371/journal.pbio.0040286%22; Exact selected MED bibliography, ordered authors and complete abstractText | supports | Exact MED PMID16933976, DOI10.1371/journal.pbio.0040286, Macronuclear genome sequence of the ciliate Tetrahymena thermophila, a model eukaryote., Eisen JA, Coyne RS, Wu M, Wu D, Thiagarajan M, Wortman JR, Badger JH, Ren Q, Amedeo P, Jones KM, Tallon LJ, Delcher AL, Salzberg SL, Silva JC, Haas BJ, Majoros WH, Farzad M, Carlton JM, Smith RK, Garg J, Pearlman RE, Karrer KM, Sun L, Manning G, Elde NC, Turkewitz AP, Asai DJ, Wilkes DE, Wang Y, Cai H, Collins K, Stewart BA, Lee SR, Wilamowska K, Weinberg Z, Ruzzo WL, Wloga D, Gaertig J, Frankel J, Tsao CC, Gorovsky MA, Keeling PJ, Waller RF, Patron NJ, Cherry JM, Stover NA, Krieger CJ, del Toro C, Ryder HF, Williamson SC, Barbeau RA, Hamilton EP, Orias E.. The complete primary abstract describes the Tetrahymena somatic macronuclear genome and distinguishes its gene-expression role from the germline micronucleus. |
| root31-sources-tax5911 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911; Exact taxId, scientificName, rank, lineage and otherNames | supports | ENA5911 identifies Tetrahymena thermophila at species rank; the SB210 strain comes from the primary paper, not from inference based on this taxonomy entry. |
| root31-sources-macronucleus-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031039/ancestors?relations=is_a; Complete ancestors response, relations=is_a | supports | The native is_a-only ancestor list includes nucleus GO0005634. No parthood relation is substituted. |
| root31-sources-eisen2006-plos-xml | https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0040286&amp;type=manuscript; Publisher JATS complete sections s1, s2a1, s2a2, s2a5 and s3a, with embedded Fig1–4 captions where present; other sections, pixels, separate tables/supplements and raw reads not inspected | supports | Genuine publisher JATS Introduction, sequencing/assembly, assembly accuracy/completeness, copy-number analysis and cell-growth/DNA-isolation/library methods were read completely. The Introduction distinguishes somatic MAC expression from germline MIC and explains fragmentation, telomere addition and amplification. Results and methods explicitly identify SB210 and differential-sedimentation purification of macronuclei. Low MIC and mitochondrial contamination is acknowledged: purification does not imply absolute purity. DNA processing is established background here, not a newly tested developmental mechanism. |
| native-verify | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/macronucleus.yaml --verify; Entire retained focused native output | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/macronucleus.yaml --causal-graphs; Entire retained focused native output | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/macronucleus.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/macronucleus.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/macronucleus.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/macronucleus-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/macronucleus.yaml --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/macronucleus-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/macronucleus-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/macronucleus.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 4 of 4 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- COMMON is qualitative occurrence, not measured prevalence. Historical authorship and earlier issue dispositions are not independently recertified.
- Eisen2006 scope is complete abstract, Introduction, sequencing/assembly, accuracy/completeness, copy-number analysis and cell-growth/DNA-isolation/library methods. Remaining sections, pixels, supplementary tables and raw genome reads were not inspected. An initial numeric PMC request returned a challenge; genuine publisher JATS supplies the assessed body.
- The collective DNA ESSENTIAL row is interpreted at its constitutive material scope; experimental formation necessity was not established by the inspected sources.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes bundles for every uncovered record, including honest no-finding reviews. Scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T021711Z-macronucleus-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Macronucleus identity, source and topology review
started_at: '2026-10-22T01:50:51Z'
finished_at: '2026-10-22T02:17:11Z'
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
summary: No concrete curation defect observed within the explicitly bounded source
  scope.
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
  - path: data/structures/membrane_organelle/macronucleus.yaml
    sha256: 99c6a5a957b29cb3ee37f2f1c81b5e0c4a8e3e32462bbb5e33dc5134c04d38c2
    role: target
  - path: data/structures/membrane_organelle/micronucleus.yaml
    sha256: fe6086eb62e1499109082d20f9a25ff776a68482d0ab89253469f6f3bfcbb8c1
    role: context
  - path: data/structures/membrane_organelle/nucleus.yaml
    sha256: 889818b3c6a37074924a97bc81271f43ef236dc9112a871c5e521dae123e497d
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0031039
  path: data/structures/membrane_organelle/macronucleus.yaml
  label: macronucleus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/macronucleus.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target: identity, hierarchy/parthood, material boundaries,
    source and taxonomic claims, examples, functions and every graph edge.'
  selection: Target 7 of batch thirty-one in strict uncovered path order from fresh
    origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0031039
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0031039
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/macronucleus.yaml
    --verify
  exit_code: 0
  summary: Focused native check passed; scientific scope assessed separately.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0031039
  command: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/macronucleus.yaml
    --causal-graphs
  exit_code: 0
  summary: Focused native check passed; scientific scope assessed separately.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0031039
  command: just validate data/structures/membrane_organelle/macronucleus.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0031039
  command: just validate-strict data/structures/membrane_organelle/macronucleus.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/macronucleus-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0031039
  summary: No expression-module claim or dataset is used. Genome preparation, compartment
    topology and direct recruitment sources apply.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0031039
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - schema
  - root31-sources-go
  - root31-sources-eisen2006-meta
  - root31-sources-tax5911
  - root31-sources-macronucleus-ancestors
  - root31-sources-eisen2006-plos-xml
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0031039
  summary: 4 of 4 collected target identifiers returned OK. No residuals. Native source
    checks are separately scoped; skipped or unreachable identifiers are not silently
    counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0031039
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0031039
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0031039
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0031039
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0031039
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
    and current batch31 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/macronucleus.yaml
  locator: Entire maintained target, all sources, examples, graph edges, discussions
    and history
  accessed_at: '2026-10-22T02:01:25Z'
  support: context_only
  summary: Full target read; no scientific record or native status changed.
- evidence_id: policy
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity, hierarchy versus parthood and narrow source support
  accessed_at: '2026-10-22T02:01:25Z'
  support: context_only
  summary: Whole structures, enclosed volumes and molecular material remain distinct;
    optional inventories do not require speculative completion.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, graph nodes and essentiality
  accessed_at: '2026-10-22T02:01:25Z'
  support: context_only
  summary: Constitutive boundary material is not a knockout assertion about every
    chemical species. A descriptive graph still needs support at each edge.
- evidence_id: root31-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005770,GO:0005768,GO:0005771,GO:0010008,GO:0031904,GO:0031906,GO:0031902,GO:0071985,GO:0000813,GO:0000814,GO:0000815,GO:0031039,GO:0005634,GO:0000228
  locator: Complete names, definitions, synonyms, active flags and all returned child
    relations for fourteen identifiers
  accessed_at: '2026-10-22T01:51:20.292950Z'
  support: supports
  summary: All fourteen active native entries were read. GO0005770 is an endosome
    child with MVB as an is_a child. Exact membrane0031902 and lumen0031906 are late-endosome
    parts, with direct generic membrane/lumen parents. GO0071985 describes MVB luminal-vesicle
    cargo entry. ESCRT definitions match the sorting context. Macronucleus0031039
    denotes the transcriptional polyploid ciliate compartment, distinct from nuclear
    chromosome0000228.
  snapshot_sha256: 9247adc57897e68974e7ff5d2e137b8a39b0af19d4dbba94a647479312167c7a
- evidence_id: root31-sources-eisen2006-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1371/journal.pbio.0040286%22
  locator: Exact selected MED bibliography, ordered authors and complete abstractText
  accessed_at: '2026-10-22T01:51:20.293337Z'
  support: supports
  summary: Exact MED PMID16933976, DOI10.1371/journal.pbio.0040286, Macronuclear genome
    sequence of the ciliate Tetrahymena thermophila, a model eukaryote., Eisen JA,
    Coyne RS, Wu M, Wu D, Thiagarajan M, Wortman JR, Badger JH, Ren Q, Amedeo P, Jones
    KM, Tallon LJ, Delcher AL, Salzberg SL, Silva JC, Haas BJ, Majoros WH, Farzad
    M, Carlton JM, Smith RK, Garg J, Pearlman RE, Karrer KM, Sun L, Manning G, Elde
    NC, Turkewitz AP, Asai DJ, Wilkes DE, Wang Y, Cai H, Collins K, Stewart BA, Lee
    SR, Wilamowska K, Weinberg Z, Ruzzo WL, Wloga D, Gaertig J, Frankel J, Tsao CC,
    Gorovsky MA, Keeling PJ, Waller RF, Patron NJ, Cherry JM, Stover NA, Krieger CJ,
    del Toro C, Ryder HF, Williamson SC, Barbeau RA, Hamilton EP, Orias E.. The complete
    primary abstract describes the Tetrahymena somatic macronuclear genome and distinguishes
    its gene-expression role from the germline micronucleus.
  snapshot_sha256: 2d1fb0cfdee90a81dc9d9d9a752eb0012c7b6bf33d143ead4fcd0021e094b63e
- evidence_id: root31-sources-tax5911
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5911
  locator: Exact taxId, scientificName, rank, lineage and otherNames
  accessed_at: '2026-10-22T01:51:20.293244Z'
  support: supports
  summary: ENA5911 identifies Tetrahymena thermophila at species rank; the SB210 strain
    comes from the primary paper, not from inference based on this taxonomy entry.
  snapshot_sha256: 42cc1d612d8aa31ffc6e484dfb7b846348bea7e26ca272eb4b5f4e7739df4ce6
- evidence_id: root31-sources-macronucleus-ancestors
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031039/ancestors?relations=is_a
  locator: Complete ancestors response, relations=is_a
  accessed_at: '2026-10-22T01:51:21.814911Z'
  support: supports
  summary: The native is_a-only ancestor list includes nucleus GO0005634. No parthood
    relation is substituted.
  snapshot_sha256: 73eee77f9c6e73d1323b86dbd2f6b44b0cc17858e94be5661597ccbb19d52c79
- evidence_id: root31-sources-eisen2006-plos-xml
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article/file?id=10.1371/journal.pbio.0040286&type=manuscript
  locator: Publisher JATS complete sections s1, s2a1, s2a2, s2a5 and s3a, with embedded
    Fig1–4 captions where present; other sections, pixels, separate tables/supplements
    and raw reads not inspected
  accessed_at: '2026-10-22T01:55:35.748654Z'
  support: supports
  summary: 'Genuine publisher JATS Introduction, sequencing/assembly, assembly accuracy/completeness,
    copy-number analysis and cell-growth/DNA-isolation/library methods were read completely.
    The Introduction distinguishes somatic MAC expression from germline MIC and explains
    fragmentation, telomere addition and amplification. Results and methods explicitly
    identify SB210 and differential-sedimentation purification of macronuclei. Low
    MIC and mitochondrial contamination is acknowledged: purification does not imply
    absolute purity. DNA processing is established background here, not a newly tested
    developmental mechanism.'
  snapshot_sha256: 024925187b37feef920b76eb39d59dd09190d33d393b65cb9c5e0f6e9ecfc55b
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/macronucleus.yaml
    --verify
  locator: Entire retained focused native output
  accessed_at: '2026-10-22T01:51:21.930105Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/macronucleus.yaml
    --causal-graphs
  locator: Entire retained focused native output
  accessed_at: '2026-10-22T01:51:22.377007Z'
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
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/macronucleus.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:50:52Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/macronucleus.yaml'
  snapshot_sha256: c2acbec59b3be180ed888173d9535716a6f078447aaba88f97b12ccd6293f414
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/macronucleus.yaml
    --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/macronucleus-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T01:50:53Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/macronucleus.yaml\
    \ --out /private/tmp/cellstructure-batch31-20261022-ag46a4d4/macronucleus-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch31-20261022-ag46a4d4/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch31-20261022-ag46a4d4/macronucleus-strict.tsv"
  snapshot_sha256: 2f36bb69e579dc0b7012b37eea37decf39bba0c286af1ad362537c95fd1d5a78
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/macronucleus.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 4 of 4 collected target identifiers returned OK. No residuals. Native source
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
  topic: Exact structure and mereology
  outcome: supported
  target_ids:
  - GO:0031039
  summary: Native definitions and relations support macronucleus identity and nucleus
    ancestry, distinct from micronucleus and from DNA material.
  evidence_ids:
  - record
  - policy
  - root31-sources-go
  - root31-sources-macronucleus-ancestors
  - root31-sources-eisen2006-plos-xml
- assessment_id: composition
  area: grounding
  topic: Molecular material versus whole compartment
  outcome: supported
  target_ids:
  - GO:0031039
  summary: Macronuclear DNA explicitly denotes processed/amplified DNA rather than
    the complete GO nuclear chromosome. Label-only grounding and the open SO question
    preserve that distinction.
  evidence_ids:
  - record
  - schema
  - root31-sources-go
  - root31-sources-eisen2006-plos-xml
- assessment_id: formation-necessity
  area: grounding
  topic: Constitutive material versus experimental formation necessity
  outcome: unknown
  target_ids:
  - GO:0031039
  summary: The DNA constituent is defining material of the macronucleus, and the inspected
    genome study supports its presence and processing. It does not experimentally
    test whether the macronucleus forms without this collective DNA component; chromosome
    sequencing and ontology definitions do not establish an assembly requirement.
  evidence_ids:
  - record
  - schema
  - root31-sources-go
  - root31-sources-eisen2006-plos-xml
- assessment_id: scope
  area: scope
  topic: Taxon and actual experimental context
  outcome: supported
  target_ids:
  - GO:0031039
  summary: SB210 and purified-MAC shotgun preparation match the primary methods. Somatic
    expression is scoped to Tetrahymena asexual growth; no universal ciliate genome
    architecture is inferred.
  evidence_ids:
  - record
  - root31-sources-tax5911
  - root31-sources-eisen2006-meta
  - root31-sources-eisen2006-plos-xml
- assessment_id: function
  area: evidence
  topic: Bounded functional evidence
  outcome: supported
  target_ids:
  - GO:0031039
  summary: GO and the primary Introduction support vegetative somatic gene expression;
    the genome paper is not a newly observed developmental perturbation assay.
  evidence_ids:
  - record
  - root31-sources-go
  - root31-sources-eisen2006-meta
  - root31-sources-eisen2006-plos-xml
- assessment_id: graph
  area: graph
  topic: Every target graph edge
  outcome: supported
  target_ids:
  - GO:0031039
  summary: All three descriptive edges express DNA on chromosomes housed within MAC,
    DNA supporting somatic expression and MAC transcriptional function. The first
    predicate is read with its explicit description, which does not place DNA on the
    nuclear exterior. No developmental or pore mechanism is asserted.
  evidence_ids:
  - record
  - root31-sources-go
  - root31-sources-eisen2006-meta
  - root31-sources-eisen2006-plos-xml
  - root31-sources-macronucleus-ancestors
- assessment_id: limits
  area: evidence
  topic: Unresolved inventories and evidence tiers
  outcome: unknown
  target_ids:
  - GO:0031039
  summary: No complete molecular inventory, quantitative prevalence or isolated physical
    sufficiency experiment is established. Primary abstracts, selected primary-body
    sections and review synthesis retain distinct evidentiary roles.
  evidence_ids:
  - record
  - schema
  - root31-sources-go
  - root31-sources-eisen2006-meta
  - root31-sources-eisen2006-plos-xml
- assessment_id: coverage
  area: completeness
  topic: All maintained fields and native status
  outcome: supported
  target_ids:
  - GO:0031039
  summary: Entire target, all graph edges, source placements, discussions and history
    inspected. No maintained image asset, numeric physical property, trait link, protein
    example or verbatim snippet is asserted. PROPOSED remains unchanged; historic
    issue closures are not independently recertified.
  evidence_ids:
  - record
  - policy
  - root31-sources-go
  - root31-sources-eisen2006-meta
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- COMMON is qualitative occurrence, not measured prevalence. Historical authorship
  and earlier issue dispositions are not independently recertified.
- Eisen2006 scope is complete abstract, Introduction, sequencing/assembly, accuracy/completeness,
  copy-number analysis and cell-growth/DNA-isolation/library methods. Remaining sections,
  pixels, supplementary tables and raw genome reads were not inspected. An initial
  numeric PMC request returned a challenge; genuine publisher JATS supplies the assessed
  body.
- The collective DNA ESSENTIAL row is interpreted at its constitutive material scope;
  experimental formation necessity was not established by the inspected sources.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes bundles for every uncovered record, including honest
  no-finding reviews. Scientific content remains unchanged.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
