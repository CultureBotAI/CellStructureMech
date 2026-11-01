# Peroxisome scientific review

- Review: 20261022T031041Z-peroxisome-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:58:45Z
- Finished UTC: 2026-10-22T03:10:41Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Exact peroxisome identity, bounded yeast biology and pinned pathway link are supported; one major finding corrects whole-membrane LIPID grounding.

## Scope And Provenance

Entire single maintained target; two frozen adjacent records supply boundary context only.

Selection: Target 5 of batch37, the next uncovered record in strict path order at fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005777 | data/structures/membrane_organelle/peroxisome.yaml | maintained | peroxisome |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005777 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005777 | Focused validator passed. |
| Native graph protein-reference check | passed | True | GO:0005777 | Native command passed; source identity and biological support separately reviewed. |
| Pinned pathway-link checker | passed | True | GO:0005777 | Native command passed; source identity and biological support separately reviewed. |
| Expression-module applicability | not_applicable | False | GO:0005777 | No expression-module membership or regulator mechanism is asserted by this target. |
| Claim-level scientific review | passed | True | GO:0005777 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005777 | 8 of 9 collected target identifiers returned OK. gomodel:YeastPathways_YEAST-FAO-PWY: SKIPPED; Exact pinned PathwayMech revision bytes match local snapshot SHA256, identifier, label and S288C taxon. SITE_OF is bounded to the beta-oxidation segment; the generic resolver has no gomodel adapter. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005777 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005777 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005777 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005777 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005777 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Pinned, organism-scoped SITE_OF link

evidence: supported. Targets: GO:0005777.

The link matches the exact pinned pathway bytes and S288C identity. Its explicit beta-oxidation-segment restriction avoids assigning activation and auxiliary reactions to this compartment or presenting a new strain experiment.

### Single-membrane organelle with distinct parts

identity: supported. Targets: GO:0005777.

The exact GO identity and typed part relations support a peroxisome with a membrane and matrix volume. The historical removal of matrix volume from molecular components is retained appropriately.

### Whole membrane typed as a lipid

grounding: concern. Targets: GO:0005777.

The component labels and grounds the entire GO0005778 membrane while assigning LIPID; its graph node joins that row. This confuses anatomical membrane identity with a molecular constituent.

### Bounded yeast metabolism and import

evidence: supported. Targets: GO:0005777.

The review sources support the described yeast metabolic compartment and import process. The generic targeting-signal-bearing protein node intentionally describes a cargo class, so no unique accession is inferred or required by its broad label.

### Three descriptive edges with component correction

graph: supported. Targets: GO:0005777.

Matrix enclosure, cargo import and beta-oxidation compartmentalization have positive support at the stated descriptive scope. The membrane node component_ref shares the component-type defect; the graph does not assert complete import machinery.

### Species-bounded qualitative exemplar

scope: supported. Targets: GO:0005777.

The verified S.cerevisiae example and COMMON note are consistent with the stated yeast review context. They do not quantify prevalence across isolates, media or all eukaryotes.

### Complete maintained target

completeness: supported. Targets: GO:0005777.

All current fields, history, discussions and graph edges were assessed. Optional molecular inventory and quantitative measurements are not invented; historical curation events are not new source evidence.

## Findings

### F1: Separate whole membrane identity from lipid material

major / open / confirmed; issue key: peroxisome-whole-membrane-lipid-grounding.

The peroxisomal_membrane component has type LIPID but labels and grounds the whole anatomical membrane GO0005778. The structural graph node points to this component. A valid membrane parthood statement does not make that GO cellular component a chemical lipid.

## Recommended Actions And Acceptance Checks

### A1

Retain supported membrane parthood. Model a whole structural constituent with an appropriate type, or describe supported lipid material separately with chemical grounding or justified label-only status; align the component_ref.

- Verify component type, identity and graph join against the exact source definition.
- After separately authorized curation, run schema, strict, graph and label checks.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/peroxisome.yaml; Entire maintained target, history, functions, each graph edge, discussions and related_records if present | context_only | Entire target read; scientific assertions and historical corrections assessed at their current scope. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum, graph node, xref and related-record contracts | context_only | An anatomical membrane differs from a chemical lipid; collective bilayer constitution differs from experimental necessity of an individual molecule. An accession used as an example does not identify an entire machinery cohort. |
| neighbor-peroxisomal_matrix | data/structures/membrane_organelle/peroxisomal_matrix.yaml; Complete adjacent maintained record | context_only | Whole organelle, matrix volume and membrane boundary read as distinct frozen local context; each has its own scientific review. |
| neighbor-peroxisomal_membrane | data/structures/membrane_organelle/peroxisomal_membrane.yaml; Complete adjacent maintained record | context_only | Whole organelle, matrix volume and membrane boundary read as distinct frozen local context; each has its own scientific review. |
| root37-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005782,GO:0005778,GO:0005777,GO:0031907,GO:0031903,GO:0006635; Complete native results GO0005777/78/82,0031903/07,0006635; definitions, synonym scopes and relation-labelled children | supports | Six active GO entries distinguish organelle, membrane and matrix; exact synonyms and typed is_a/part_of relations support the maintained identities. Beta-oxidation is a biological process, not the compartment. |
| root37-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId4932, scientificName, rank, lineage and names | supports | Native taxonomy identifies Saccharomyces cerevisiae at species rank. This identity is not a prevalence survey. |
| root37-sources-sibirny2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Ffemsyr%2Ffow038&amp;format=json&amp;resultType=core; Native MED bibliographic identity, publication type and entire abstractText; publisher body unavailable | supports | Exact DOI, title, author and PMID27189367 match. The complete abstract describes yeast peroxisomal metabolism including beta-oxidation, soluble matrix proteins and signal-dependent import. This is a secondary review, not a new strain experiment. |
| root37-sources-yuan2016-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.bbamcr.2015.09.008&amp;format=json&amp;resultType=core; Native MED bibliographic identity, publication type and entire abstractText; article body not retrieved | supports | Exact DOI, title, three authors, PMID26367802 and complete abstract verified. The review describes yeast mutant membrane remnants and discusses differences between experimental markers; it does not justify treating all biogenesis models as settled. |
| root37-sources-smith2013-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrm3700&amp;format=json&amp;resultType=core; Native MED identity, publication type, complete abstractText and full-text links | supports | Exact DOI, title, authors, PMID24263361 and PMCID4060825 verified; bibliographic source is explicitly a review. |
| root37-sources-smith2013-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC4060825/; Verified article title/PMCID; complete Box1, S5 Matrix protein import including Figure2 caption, S10 growth/fission and S11 de novo biogenesis. Other sections, pixels and raw experiments not certified read. | supports | The secondary review describes peroxisomal metabolism, targeting-signal-dependent matrix import and membrane-associated docking machinery. Its growth/fission and de novo models retain stated experimental uncertainties. |
| pathway-snapshot | conf/pathwaymech_targets.json; Complete six-field snapshot header and exact fatty-acid-oxidation record row | context_only | The local pinned identifier, label, S288C taxon, path and byte digest are preserved; no live-current pathway claim replaces the declared revision. |
| pathway-decision | research/cross_mech/2026-10-05-pathway-link-decisions.md; Complete decision note; peroxisome/matrix rows and source-read limitations | context_only | The original SITE_OF decision explicitly limits placement to the beta-oxidation segment and distinguishes S288C from species scope. |
| pathway-validator | scripts/check_pathway_links.py; Complete native check contract | context_only | The checker compares maintained links with the pinned snapshot; independent remote byte equality is checked separately. |
| root37-sources-pathway | https://raw.githubusercontent.com/CultureBotAI/PathwayMech/d8ec2b69f7a4c615aecddff80498fef1e1fab0ce/data/pathways/fatty-acid-oxidation-pathway.yaml; Pinned d8ec2b69f7a4c615aecddff80498fef1e1fab0ce YAML: id/label/description/pathway_type/taxa/references, all participant IDs/labels and all reaction IDs/labels; detailed mechanistic-edge evidence not audited | supports | At the exact source commit the linked record has the expected identifier, label and S288C taxon. Its bytes match the local SHA256. Identity, description, participants and reaction labels support the bounded link; their inclusion does not locate all activation or auxiliary reactions in the matrix. |
| root37-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId559292, scientificName, rank, lineage and names | supports | Native taxonomy identifies Saccharomyces cerevisiae S288C as a strain, narrower than the record species example. |
| schema-result | just validate data/structures/membrane_organelle/peroxisome.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/peroxisome.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/peroxisome.yaml --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/peroxisome-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/peroxisome.yaml --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/peroxisome-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch37-20261022-offjkz5m/peroxisome-strict.tsv |
| native-peroxisome-causal | /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/peroxisome.yaml; Complete captured native read-only command log | supports | <br>data/structures/membrane_organelle/peroxisome.yaml  (GO:0005777)<br>  peroxisomal_matrix_import	pts_matrix_proteins	UNANCHORED_NO_UNIPROT	peroxisomal targeting signal-bearing matrix proteins<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     1  total GENE_OR_PROTEIN causal nodes<br> |
| native-pathway-native | just check-pathway-links; Complete captured native read-only command log | supports | OK: 6 pathway links match the pinned target snapshot<br>uv run python scripts/check_pathway_links.py <br> |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/peroxisome.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 8 of 9 collected target identifiers returned OK. gomodel:YeastPathways_YEAST-FAO-PWY: SKIPPED; Exact pinned PathwayMech revision bytes match local snapshot SHA256, identifier, label and S288C taxon. SITE_OF is bounded to the beta-oxidation segment; the generic resolver has no gomodel adapter. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Sibirny2016 and Yuan2016 were read as complete native abstracts with verified bibliographic identities. The exact Sibirny publisher route returned HTTP403; Yuan DOI negotiation returned metadata rather than an article body. Smith2013 is a secondary review read only in the declared full sections. No primary experimental body or figure pixels were independently reanalyzed for this target.
- Qualitative yeast occurrence and function are source-supported; no isolate census, universal enzyme complement, exact molecular stoichiometry or quantitative physical measurement is inferred. No image asset or verbatim snippet is maintained.
- Pinned pathway identity and summarized biochemical segment were verified; the imported pathway graph, detailed quoted evidence and upstream GO-CAM model were not fully audited.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User authorizes an honest review bundle for every uncovered target, including zero-finding observations.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T031041Z-peroxisome-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Peroxisome scientific review
started_at: '2026-10-22T02:58:45Z'
finished_at: '2026-10-22T03:10:41Z'
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
summary: Exact peroxisome identity, bounded yeast biology and pinned pathway link
  are supported; one major finding corrects whole-membrane LIPID grounding.
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
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/pathwaymech_targets.json
    sha256: 625e474ce45903a482587deb9b26237088d1298d88a017920a69370c89db5dd0
    role: context
  - path: data/structures/membrane_organelle/peroxisomal_matrix.yaml
    sha256: 4fc4ffe0656f64952c9e1c0c88df647019381b19abe4201b321c5542297f6e23
    role: context
  - path: data/structures/membrane_organelle/peroxisomal_membrane.yaml
    sha256: 4c11f2dcb589eddf4948f8018d1008cfe30f7eb5e4edc3bbd020fa46fd3dcf87
    role: context
  - path: data/structures/membrane_organelle/peroxisome.yaml
    sha256: 63767bb1954d10e3237eec60b9541a916b6039d71f9afa374e8ff376a5066828
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
  - path: research/cross_mech/2026-10-05-pathway-link-decisions.md
    sha256: d209257e5c81e5189f4003b9aac347f8dbe7f3a6b59fb28f238db900d894fc73
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: scripts/check_pathway_links.py
    sha256: 054e0e3a5d7b8c8e7a9f661bcc1c096707aa4ee43e8537d60a9b1b6fd036b226
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0005777
  path: data/structures/membrane_organelle/peroxisome.yaml
  label: peroxisome
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/peroxisome.yaml
    role: maintained scientific record
scope:
  description: Entire single maintained target; two frozen adjacent records supply
    boundary context only.
  selection: Target 5 of batch37, the next uncovered record in strict path order at
    fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005777
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005777
  command: just validate data/structures/membrane_organelle/peroxisome.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005777
  command: just validate-strict data/structures/membrane_organelle/peroxisome.yaml
    --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/peroxisome-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-peroxisome-causal
  name: Native graph protein-reference check
  status: passed
  required: true
  target_ids:
  - GO:0005777
  command: /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/peroxisome.yaml
  exit_code: 0
  summary: Native command passed; source identity and biological support separately
    reviewed.
  evidence_ids:
  - native-peroxisome-causal
- check_id: native-pathway-native
  name: Pinned pathway-link checker
  status: passed
  required: true
  target_ids:
  - GO:0005777
  command: just check-pathway-links
  exit_code: 0
  summary: Native command passed; source identity and biological support separately
    reviewed.
  evidence_ids:
  - native-pathway-native
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005777
  summary: No expression-module membership or regulator mechanism is asserted by this
    target.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005777
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-peroxisomal_matrix
  - neighbor-peroxisomal_membrane
  - root37-sources-go
  - root37-sources-tax4932
  - root37-sources-sibirny2016-meta
  - root37-sources-yuan2016-meta
  - root37-sources-smith2013-meta
  - root37-sources-smith2013-pmc
  - pathway-snapshot
  - pathway-decision
  - pathway-validator
  - root37-sources-pathway
  - root37-sources-tax559292
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005777
  summary: '8 of 9 collected target identifiers returned OK. gomodel:YeastPathways_YEAST-FAO-PWY:
    SKIPPED; Exact pinned PathwayMech revision bytes match local snapshot SHA256,
    identifier, label and S288C taxon. SITE_OF is bounded to the beta-oxidation segment;
    the generic resolver has no gomodel adapter. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root37-sources-pathway
  - pathway-snapshot
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005777
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005777
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005777
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005777
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005777
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
    and current batch37 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/peroxisome.yaml
  locator: Entire maintained target, history, functions, each graph edge, discussions
    and related_records if present
  accessed_at: '2026-10-22T03:03:54Z'
  support: context_only
  summary: Entire target read; scientific assertions and historical corrections assessed
    at their current scope.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum, graph node, xref and related-record
    contracts
  accessed_at: '2026-10-22T03:03:54Z'
  support: context_only
  summary: An anatomical membrane differs from a chemical lipid; collective bilayer
    constitution differs from experimental necessity of an individual molecule. An
    accession used as an example does not identify an entire machinery cohort.
- evidence_id: neighbor-peroxisomal_matrix
  kind: record_content
  reference: data/structures/membrane_organelle/peroxisomal_matrix.yaml
  locator: Complete adjacent maintained record
  accessed_at: '2026-10-22T03:03:54Z'
  support: context_only
  summary: Whole organelle, matrix volume and membrane boundary read as distinct frozen
    local context; each has its own scientific review.
- evidence_id: neighbor-peroxisomal_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/peroxisomal_membrane.yaml
  locator: Complete adjacent maintained record
  accessed_at: '2026-10-22T03:03:54Z'
  support: context_only
  summary: Whole organelle, matrix volume and membrane boundary read as distinct frozen
    local context; each has its own scientific review.
- evidence_id: root37-sources-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005782,GO:0005778,GO:0005777,GO:0031907,GO:0031903,GO:0006635
  locator: Complete native results GO0005777/78/82,0031903/07,0006635; definitions,
    synonym scopes and relation-labelled children
  accessed_at: '2026-10-22T02:59:25.328401Z'
  support: supports
  summary: Six active GO entries distinguish organelle, membrane and matrix; exact
    synonyms and typed is_a/part_of relations support the maintained identities. Beta-oxidation
    is a biological process, not the compartment.
  snapshot_sha256: bdca0c71b912962cf7e8c7339f43ce92105f098c16bc50a3306e6fe035723611
- evidence_id: root37-sources-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId4932, scientificName, rank, lineage and names
  accessed_at: '2026-10-22T02:59:25.329833Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae at species rank. This
    identity is not a prevalence survey.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root37-sources-sibirny2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093%2Ffemsyr%2Ffow038&format=json&resultType=core
  locator: Native MED bibliographic identity, publication type and entire abstractText;
    publisher body unavailable
  accessed_at: '2026-10-22T02:59:26.049568Z'
  support: supports
  summary: Exact DOI, title, author and PMID27189367 match. The complete abstract
    describes yeast peroxisomal metabolism including beta-oxidation, soluble matrix
    proteins and signal-dependent import. This is a secondary review, not a new strain
    experiment.
  snapshot_sha256: c888f15b79e011674af6ecf96004a577949ba9bd99e3d739efe4aa661420f878
- evidence_id: root37-sources-yuan2016-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016%2Fj.bbamcr.2015.09.008&format=json&resultType=core
  locator: Native MED bibliographic identity, publication type and entire abstractText;
    article body not retrieved
  accessed_at: '2026-10-22T02:59:26.076235Z'
  support: supports
  summary: Exact DOI, title, three authors, PMID26367802 and complete abstract verified.
    The review describes yeast mutant membrane remnants and discusses differences
    between experimental markers; it does not justify treating all biogenesis models
    as settled.
  snapshot_sha256: 81be8cc8b74ab8be98592d6439bd3a86a718e3e5cd8fafeb7cd9b896f0ac88e1
- evidence_id: root37-sources-smith2013-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038%2Fnrm3700&format=json&resultType=core
  locator: Native MED identity, publication type, complete abstractText and full-text
    links
  accessed_at: '2026-10-22T02:59:26.051789Z'
  support: supports
  summary: Exact DOI, title, authors, PMID24263361 and PMCID4060825 verified; bibliographic
    source is explicitly a review.
  snapshot_sha256: 8b90b38c8d12601010391d434816944a55e7f85b32934cf6ed954866394eefaa
- evidence_id: root37-sources-smith2013-pmc
  kind: authority
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4060825/
  locator: Verified article title/PMCID; complete Box1, S5 Matrix protein import including
    Figure2 caption, S10 growth/fission and S11 de novo biogenesis. Other sections,
    pixels and raw experiments not certified read.
  accessed_at: '2026-10-22T02:59:47.462836Z'
  support: supports
  summary: The secondary review describes peroxisomal metabolism, targeting-signal-dependent
    matrix import and membrane-associated docking machinery. Its growth/fission and
    de novo models retain stated experimental uncertainties.
  snapshot_sha256: 3b1e075027e000379c6b4c9729094f426c0d67d13375c589516074e31bed91d8
- evidence_id: pathway-snapshot
  kind: record_content
  reference: conf/pathwaymech_targets.json
  locator: Complete six-field snapshot header and exact fatty-acid-oxidation record
    row
  accessed_at: '2026-10-22T03:03:54Z'
  support: context_only
  summary: The local pinned identifier, label, S288C taxon, path and byte digest are
    preserved; no live-current pathway claim replaces the declared revision.
- evidence_id: pathway-decision
  kind: record_content
  reference: research/cross_mech/2026-10-05-pathway-link-decisions.md
  locator: Complete decision note; peroxisome/matrix rows and source-read limitations
  accessed_at: '2026-10-22T03:03:54Z'
  support: context_only
  summary: The original SITE_OF decision explicitly limits placement to the beta-oxidation
    segment and distinguishes S288C from species scope.
- evidence_id: pathway-validator
  kind: record_content
  reference: scripts/check_pathway_links.py
  locator: Complete native check contract
  accessed_at: '2026-10-22T03:03:54Z'
  support: context_only
  summary: The checker compares maintained links with the pinned snapshot; independent
    remote byte equality is checked separately.
- evidence_id: root37-sources-pathway
  kind: database
  reference: https://raw.githubusercontent.com/CultureBotAI/PathwayMech/d8ec2b69f7a4c615aecddff80498fef1e1fab0ce/data/pathways/fatty-acid-oxidation-pathway.yaml
  locator: 'Pinned d8ec2b69f7a4c615aecddff80498fef1e1fab0ce YAML: id/label/description/pathway_type/taxa/references,
    all participant IDs/labels and all reaction IDs/labels; detailed mechanistic-edge
    evidence not audited'
  accessed_at: '2026-10-22T02:59:47.464775Z'
  support: supports
  summary: At the exact source commit the linked record has the expected identifier,
    label and S288C taxon. Its bytes match the local SHA256. Identity, description,
    participants and reaction labels support the bounded link; their inclusion does
    not locate all activation or auxiliary reactions in the matrix.
  snapshot_sha256: e905337a760258df02ec780d5997a8fcc703587e11fe2d35a02d4950e22ac3dc
- evidence_id: root37-sources-tax559292
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId559292, scientificName, rank, lineage and names
  accessed_at: '2026-10-22T02:59:26.049136Z'
  support: supports
  summary: Native taxonomy identifies Saccharomyces cerevisiae S288C as a strain,
    narrower than the record species example.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/peroxisome.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:58:46Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/peroxisome.yaml'
  snapshot_sha256: ac54dc0a6d6be6bb6289fa87398eacdd83a6b8e2ecfbcfc427a0ba55ca1da1bb
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/peroxisome.yaml
    --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/peroxisome-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:58:47Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/peroxisome.yaml\
    \ --out /private/tmp/cellstructure-batch37-20261022-offjkz5m/peroxisome-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch37-20261022-offjkz5m/peroxisome-strict.tsv"
  snapshot_sha256: 122312e59c9852d09eb970ccb06916ace00ff7433a8c8a9470aeb6d315e7b711
- evidence_id: native-peroxisome-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch37-20261022-offjkz5m/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/peroxisome.yaml
  locator: Complete captured native read-only command log
  accessed_at: '2026-10-22T03:01:47.770788Z'
  support: supports
  summary: "\ndata/structures/membrane_organelle/peroxisome.yaml  (GO:0005777)\n \
    \ peroxisomal_matrix_import\tpts_matrix_proteins\tUNANCHORED_NO_UNIPROT\tperoxisomal\
    \ targeting signal-bearing matrix proteins\n\ncausal_graphs GENE_OR_PROTEIN node\
    \ summary:\n     1  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB\
    \ grounding or xref on the node\n     0  COVERED                   component_ref\
    \ target holds protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES\
    \          component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     1  total GENE_OR_PROTEIN causal nodes\n"
  snapshot_sha256: bc989831a9f0e6b9c6e96c12ed5543938d7226aabb2a937281c771f930cbacf6
- evidence_id: native-pathway-native
  kind: validation
  reference: just check-pathway-links
  locator: Complete captured native read-only command log
  accessed_at: '2026-10-22T03:02:00.621781Z'
  support: supports
  summary: "OK: 6 pathway links match the pinned target snapshot\nuv run python scripts/check_pathway_links.py\
    \ \n"
  snapshot_sha256: e577945148147025534a959245514c512dcf70159ade5dd5cdcb6c1957df87b9
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/peroxisome.yaml; native collect() exact
    identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '8 of 9 collected target identifiers returned OK. gomodel:YeastPathways_YEAST-FAO-PWY:
    SKIPPED; Exact pinned PathwayMech revision bytes match local snapshot SHA256,
    identifier, label and S288C taxon. SITE_OF is bounded to the beta-oxidation segment;
    the generic resolver has no gomodel adapter. Native source checks are separately
    scoped; skipped or unreachable identifiers are not silently counted as resolved.'
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
- assessment_id: pathway
  area: evidence
  topic: Pinned, organism-scoped SITE_OF link
  outcome: supported
  target_ids:
  - GO:0005777
  summary: The link matches the exact pinned pathway bytes and S288C identity. Its
    explicit beta-oxidation-segment restriction avoids assigning activation and auxiliary
    reactions to this compartment or presenting a new strain experiment.
  evidence_ids:
  - record
  - pathway-snapshot
  - pathway-decision
  - root37-sources-pathway
  - root37-sources-tax559292
  - root37-sources-sibirny2016-meta
- assessment_id: identity
  area: identity
  topic: Single-membrane organelle with distinct parts
  outcome: supported
  target_ids:
  - GO:0005777
  summary: The exact GO identity and typed part relations support a peroxisome with
    a membrane and matrix volume. The historical removal of matrix volume from molecular
    components is retained appropriately.
  evidence_ids:
  - record
  - root37-sources-go
- assessment_id: component
  area: grounding
  topic: Whole membrane typed as a lipid
  outcome: concern
  target_ids:
  - GO:0005777
  summary: The component labels and grounds the entire GO0005778 membrane while assigning
    LIPID; its graph node joins that row. This confuses anatomical membrane identity
    with a molecular constituent.
  evidence_ids:
  - record
  - schema
  - root37-sources-go
- assessment_id: biology
  area: evidence
  topic: Bounded yeast metabolism and import
  outcome: supported
  target_ids:
  - GO:0005777
  summary: The review sources support the described yeast metabolic compartment and
    import process. The generic targeting-signal-bearing protein node intentionally
    describes a cargo class, so no unique accession is inferred or required by its
    broad label.
  evidence_ids:
  - record
  - root37-sources-sibirny2016-meta
  - root37-sources-yuan2016-meta
  - root37-sources-smith2013-pmc
- assessment_id: graph
  area: graph
  topic: Three descriptive edges with component correction
  outcome: supported
  target_ids:
  - GO:0005777
  summary: Matrix enclosure, cargo import and beta-oxidation compartmentalization
    have positive support at the stated descriptive scope. The membrane node component_ref
    shares the component-type defect; the graph does not assert complete import machinery.
  evidence_ids:
  - record
  - root37-sources-go
  - root37-sources-sibirny2016-meta
  - root37-sources-smith2013-pmc
- assessment_id: taxon
  area: scope
  topic: Species-bounded qualitative exemplar
  outcome: supported
  target_ids:
  - GO:0005777
  summary: The verified S.cerevisiae example and COMMON note are consistent with the
    stated yeast review context. They do not quantify prevalence across isolates,
    media or all eukaryotes.
  evidence_ids:
  - record
  - root37-sources-tax4932
  - root37-sources-sibirny2016-meta
  - root37-sources-yuan2016-meta
  - root37-sources-smith2013-pmc
- assessment_id: coverage
  area: completeness
  topic: Complete maintained target
  outcome: supported
  target_ids:
  - GO:0005777
  summary: All current fields, history, discussions and graph edges were assessed.
    Optional molecular inventory and quantitative measurements are not invented; historical
    curation events are not new source evidence.
  evidence_ids:
  - record
  - schema
  - root37-sources-go
findings:
- finding_id: F1
  issue_key: peroxisome-whole-membrane-lipid-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate whole membrane identity from lipid material
  description: The peroxisomal_membrane component has type LIPID but labels and grounds
    the whole anatomical membrane GO0005778. The structural graph node points to this
    component. A valid membrane parthood statement does not make that GO cellular
    component a chemical lipid.
  target_ids:
  - GO:0005777
  field_paths:
  - components[0].component_type
  - components[0].grounding
  - causal_graphs[0].nodes[0].component_ref
  evidence_ids:
  - record
  - schema
  - root37-sources-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/peroxisome.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md:component identity and molecular grounding
  native_severity: major
  normalization_reason: Whole-anatomical identity is materially mismatched to molecular
    lipid typing.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005777
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/peroxisome.yaml
    role: maintained scientific record
  description: Retain supported membrane parthood. Model a whole structural constituent
    with an appropriate type, or describe supported lipid material separately with
    chemical grounding or justified label-only status; align the component_ref.
  acceptance_checks:
  - Verify component type, identity and graph join against the exact source definition.
  - After separately authorized curation, run schema, strict, graph and label checks.
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Sibirny2016 and Yuan2016 were read as complete native abstracts with verified bibliographic
  identities. The exact Sibirny publisher route returned HTTP403; Yuan DOI negotiation
  returned metadata rather than an article body. Smith2013 is a secondary review read
  only in the declared full sections. No primary experimental body or figure pixels
  were independently reanalyzed for this target.
- Qualitative yeast occurrence and function are source-supported; no isolate census,
  universal enzyme complement, exact molecular stoichiometry or quantitative physical
  measurement is inferred. No image asset or verbatim snippet is maintained.
- Pinned pathway identity and summarized biochemical segment were verified; the imported
  pathway graph, detailed quoted evidence and upstream GO-CAM model were not fully
  audited.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User authorizes an honest review bundle for every uncovered target, including zero-finding
  observations.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
