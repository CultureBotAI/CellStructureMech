# Mitochondrial inner membrane identity and experimental-source review

- Review: 20261022T023311Z-mitochondrial-inner-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:18:34Z
- Finished UTC: 2026-10-22T02:33:11Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Inner-membrane identity, collective lipid material, yeast biology and descriptive graph are supported. One minor finding corrects the canonical attribution of electron tomography to a section-TEM study.

## Scope And Provenance

Entire exact target and frozen boundary neighbors; all asserted native identifiers and citation identities; specified genuine source sections; molecular grounding, distribution, examples, functions and every graph edge.

Selection: Batch33 target3; complete initial native inspect/schema/strict gates0 at unchanged f97b1abe before scientific assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005743 | data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml | maintained | mitochondrial inner membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005743 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005743 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005743 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Organism-specific protein-example applicability | not_applicable | False | GO:0005743 | The target has no UniProt protein examples, gene-symbol assertions or GENE_OR_PROTEIN nodes requiring native protein verification. Component and graph identities were manually assessed. |
| Claim-level scientific review | passed | True | GO:0005743 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005743 | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005743 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005743 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005743 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005743 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005743 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Inner bilayer and exact hierarchy

identity: supported. Targets: GO:0005743.

The definition and all three exact synonyms match GO0005743. Both maintained parents are direct native is_a parents via their child lists; crista parthood and envelope topology are supported by native definitions/relations. Matrix and intermembrane space are distinct.

### Collective bilayer without false chemical grounding

grounding: supported. Targets: GO:0005743.

The sole LIPID row is explicitly reviewed-label-only constituting material, with no whole-membrane GO substituted for a molecular lipid. Its role correctly separates matrix and intermembrane space.

### Individual formation requirements remain unresolved

evidence: unknown. Targets: GO:0005743.

Collective membrane material is constitutive; the inspected studies do not establish experimental formation necessity of every lipid species. MICOS/respiratory phenotypes do not imply that a membrane cannot form, and ESSENTIAL is not a universal claim about all proteins or cardiolipin.

### Correct yeast example with method attribution concern

scope: concern. Targets: GO:0005743.

The organism and genetic/biochemical architecture context are supported. However, the canonical note calls the sole Friedman2015 citation electron-tomographic; its Methods specify ultrathin-section TEM. Its cell-extract immunopurification proteomics and isolated-mitochondrial assays should also remain distinct from the broad purified-mitochondrial inventory in Sickmann2003. Roger2017 independently supports the bounded reduced-organelle qualifier across anaerobic lineages; this is review-tier diversity context, not a prevalence census.

### Respiration and five descriptive topology edges

graph: supported. Targets: GO:0005743.

Native process definition and the primary recovered oxidative-phosphorylation machinery support the coarse ATP-synthesis function. All five NONMECHANISTIC edges preserve correct envelope/crista/matrix/intermembrane-space boundaries. No single respiratory complex, temporal assembly sequence or quantitative proton-gradient measurement is asserted.

### Optional lipid mapping

completeness: supported. Targets: GO:0005743.

The existing molecular-grounding TODO is candid. Absence of a detailed respiratory or lipid inventory alone is not a defect of this boundary record.

## Findings

### F1: Match the canonical microscopy method to Friedman2015

minor / open / confirmed; issue key: mitochondrial-inner-membrane-friedman-microscopy-attribution.

The canonical note says electron-tomographic studies but its sole citation describes resin sections examined by conventional transmission electron microscopy, together with genetics and fluorescence/biochemical assays. The organism and architecture research context remain correct.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, describe Friedman2015 as genetic and electron-microscopic analysis, or attach an independently inspected tomography source to any retained tomography assertion. Keep purified-proteome and interaction-proteomics contexts paired with their actual studies.

- The Friedman2015-linked note accurately identifies section TEM, not electron tomography.
- Any additional tomography or broad purified-mitochondrial inventory clause has its own inspected source; retain correct yeast identity and supported biology.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml; Entire maintained target, including history, all field-level evidence, graph and discussions | context_only | Complete record read without scientific changes. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent description, grounding, component_role and essentiality, lines388–444 | context_only | Components denote molecular building blocks; GO may identify a protein subcomplex, while lipid grounding is chemical. Essentiality denotes whether the structure forms without a component, not biochemical function. |
| neighbor-mitochondrial_crista | data/structures/membrane_organelle/mitochondrial_crista.yaml; Frozen maintained neighbor; complete boundary context read | context_only | The neighbor provides maintained boundary/parthood context, not independent experimental evidence or automatic endorsement of its other assertions. |
| neighbor-mitochondrial_envelope | data/structures/membrane_organelle/mitochondrial_envelope.yaml; Frozen maintained neighbor; complete boundary context read | context_only | The neighbor provides maintained boundary/parthood context, not independent experimental evidence or automatic endorsement of its other assertions. |
| neighbor-mitochondrial_intermembrane_space | data/structures/membrane_organelle/mitochondrial_intermembrane_space.yaml; Frozen maintained neighbor; complete boundary context read | context_only | The neighbor provides maintained boundary/parthood context, not independent experimental evidence or automatic endorsement of its other assertions. |
| neighbor-mitochondrial_matrix | data/structures/membrane_organelle/mitochondrial_matrix.yaml; Frozen maintained neighbor; complete boundary context read | context_only | The neighbor provides maintained boundary/parthood context, not independent experimental evidence or automatic endorsement of its other assertions. |
| mitochondrial-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005740,GO:0031967,GO:0005739,GO:0005741,GO:0005743,GO:0005758,GO:0005742,GO:0030150,GO:0006119,GO:0097002,GO:0030061,GO:0044284,GO:0007007,GO:0019866,GO:0031966,GO:0005759,GO:0031970; Exact requested term set in URL; complete labels, definitions, synonyms, active flags and returned child relations | supports | The17 active native GO identities, definitions, synonym scopes and returned child relations were read. The target identity, relevant topology and functions match the designated terms. Whole membrane classes remain distinct from molecular lipids. |
| mitochondrial-agent-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; taxId/scientificName/rank/lineage | supports | Native ENA confirms Eukaryota2759; taxonomic identity alone does not quantify organelle prevalence. |
| mitochondrial-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId/scientificName/rank/lineage | supports | Native ENA confirms Saccharomyces cerevisiae4932, distinct from any specific laboratory strain. |
| mitochondrial-agent-sickmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.2135385100&amp;format=json&amp;resultType=core; Exact native MED result and full abstract | supports | Exact DOI, PMID, title, authors, year and complete abstract inspected; primary experimental study. |
| mitochondrial-agent-sickmann2003-pmc-exact | https://pmc.ncbi.nlm.nih.gov/articles/PMC263752/; Complete abstract, unheaded Introduction, Materials and Methods, all Results and Discussion subsections, Figures1–5 captions. No figure pixels or separate supporting-table data reanalysis. | supports | Authentic yeast mitochondrial proteomics identifies known inner-membrane oxidative-phosphorylation components and matrix/outer-membrane proteins. Most experiments use YPH499 grown in glycerol; MR103 is used for tagged-Tom22 controls. The study explicitly discusses trace contamination, dual localization and limits to complete proteome coverage. |
| mitochondrial-agent-friedman2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554/elife.07739&amp;format=json&amp;resultType=core; Exact native MED result and full abstract | supports | Exact DOI, PMID, title, authors, year and complete abstract inspected; primary experimental study. |
| mitochondrial-agent-friedman2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/PMC4434539.1.xml; Complete Introduction s1, main Results prose s2-1–s2-7, Discussion s3 and all Methods s4-1–s4-9; Figure1/4/7 and their embedded supplement captions read. No pixels or separate source-data tables reanalysis. | supports | Primary W303-derived yeast genetics, microscopy and proteomic/biochemical assays support inner-boundary/crista organization. Electron microscopy Methods specify chemically fixed resin sections examined by TEM at100kV, not tomography. Proteomics uses immunopurifications from cell extracts, with separate isolated-mitochondrial assays. MICOS deletion affects normal morphology/function while membranes and respiratory complexes can persist. |
| mitochondrial-agent-friedman2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature12985&amp;format=json&amp;resultType=core; Exact native MED result and full abstract | supports | Exact DOI, PMID, title, authors, year and complete abstract inspected; literature review, not a primary experiment. |
| mitochondrial-agent-friedman2014-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4075653.1/PMC4075653.1.xml; Complete S5 Internal determinants of mitochondrial division; native complete abstract separately read. Other review sections and figure pixels not claimed. | supports | Review-tier context distinguishes the boundary region, crista invaginations and junctions, and discusses scaffold-based architecture without establishing a universal molecular formation requirement. |
| friedman-method-search | rg --no-ignore --hidden -n -i tomogra&#124;tomogram&#124;tilt.series /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial-agent/friedman2015-body.txt; Complete derived native JATS body prose and embedded captions; literal case-insensitive search | context_only | No tomogra, tomogram or tilt.series lexical matches in the complete article body/captions. Exit1 means no search match, not a validator failure. The positive Methods statement specifying TEM is the primary finding support. |
| schema-result | just validate data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_inner_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_inner_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_inner_membrane-strict.tsv |
| mitochondrial-agent-roger2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.cub.2017.09.015%22; Complete exact native MED result and abstract | supports | Exact DOI10.1016/j.cub.2017.09.015, title, authors, year and complete abstract confirm Roger, Munoz-Gomez and Kamikawa2017 as a literature review. |
| mitochondrial-agent-roger2017-pdf | https://ecsolab.com/assets/pdf/roger_etal_2017.pdf; First printed pageR1177 identity/abstract/Introduction; R1184 opening Diversity of Mitochondrial Functions in Anaerobic Eukaryotes paragraph; R1186 hydrogenosome/mitosome comparison and concluding reduction paragraph. Figures and remaining review not inspected. | supports | Review-tier evidence independently supports reduced/no cristae in anaerobic lineages and diversity including hydrogenosomes and mitosomes. It describes a continuum and evolutionary reductions; it supplies no population-frequency estimate. |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- COMMON and VARIABLE are qualitative distribution annotations, not measured prevalence. Native taxon records verify names only; the specific anaerobic-lineage exceptions are not comprehensively enumerated or independently surveyed here.
- Collective constitutive material, individual molecular formation necessity and biochemical function remain separate. No species-independent lipid composition, stoichiometry or obligatory complete protein inventory is inferred.
- No raw imaging, figure pixels, supporting-table datasets or quantitative reanalysis was performed. Native ontology definitions support topology; a biological relation is not described as a captured direct GO edge unless returned in the native response.
- The two numeric PMC routes returned HTML challenges, but genuine exact-prefix Sickmann HTML and Chacinska S3 JATS were recovered. Sickmann EuropePMC XML returned500. A longer-prefix S3 collision retrieved a different article and is explicitly excluded, with its diagnostic receipt preserved.
- Sickmann2003 complete main text/Methods/captions was read; separate supporting tables were not. YPH499/MR103 growth and purification context, possible contaminants and incomplete proteome coverage are preserved.
- Friedman2015 complete scientific main prose and Methods were read with selected captions; no separate source-data files or pixels were inspected. The2014 review is limited to complete S5 and its native abstract. Source copies retain their original B32 access times and hashes.
- Roger2017 review-tier context was subsequently read only in the exact evidence-locator scope. It supports general reduced-organelle diversity, not an exhaustive survey, individual membrane lipid necessity or measured prevalence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- No scientific content, history or status changed. Parent owns finalization and persistence; source URL/UTC/SHA provenance retained.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T023311Z-mitochondrial-inner-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Mitochondrial inner membrane identity and experimental-source review
started_at: '2026-10-22T02:18:34Z'
finished_at: '2026-10-22T02:33:11Z'
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
summary: Inner-membrane identity, collective lipid material, yeast biology and descriptive
  graph are supported. One minor finding corrects the canonical attribution of electron
  tomography to a section-TEM study.
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
  - path: data/structures/membrane_organelle/mitochondrial_crista.yaml
    sha256: d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6
    role: context
  - path: data/structures/membrane_organelle/mitochondrial_envelope.yaml
    sha256: e750843104d72fd05608a59a650410e8bc8103b02697f5a1add9fd5bd31e283f
    role: context
  - path: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
    sha256: 63301d7a679c30a2afadd331aa17b3559852b09c038e97dab14f53e40d34ed1f
    role: target
  - path: data/structures/membrane_organelle/mitochondrial_intermembrane_space.yaml
    sha256: 9b1d3fcf94d5a598d61810b56580265af6c9325890c673eab3532645e4cb48ea
    role: context
  - path: data/structures/membrane_organelle/mitochondrial_matrix.yaml
    sha256: a8348a52ab8d24234029023bee3b95b7bd8c42a618dad2822755c59b908a727a
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
- target_id: GO:0005743
  path: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
  label: mitochondrial inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire exact target and frozen boundary neighbors; all asserted native
    identifiers and citation identities; specified genuine source sections; molecular
    grounding, distribution, examples, functions and every graph edge.
  selection: Batch33 target3; complete initial native inspect/schema/strict gates0
    at unchanged f97b1abe before scientific assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005743
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005743
  command: just validate data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005743
  command: just validate-strict data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
    --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_inner_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005743
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: protein-applicability
  name: Organism-specific protein-example applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005743
  summary: The target has no UniProt protein examples, gene-symbol assertions or GENE_OR_PROTEIN
    nodes requiring native protein verification. Component and graph identities were
    manually assessed.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005743
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-mitochondrial_crista
  - neighbor-mitochondrial_envelope
  - neighbor-mitochondrial_intermembrane_space
  - neighbor-mitochondrial_matrix
  - mitochondrial-agent-go
  - mitochondrial-agent-tax2759
  - mitochondrial-agent-tax4932
  - mitochondrial-agent-sickmann2003-meta
  - mitochondrial-agent-sickmann2003-pmc-exact
  - mitochondrial-agent-friedman2015-meta
  - mitochondrial-agent-friedman2015-jats
  - mitochondrial-agent-friedman2014-meta
  - mitochondrial-agent-friedman2014-jats
  - friedman-method-search
  - mitochondrial-agent-roger2017-meta
  - mitochondrial-agent-roger2017-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005743
  summary: 13 of 13 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005743
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0005743
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0005743
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0005743
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0005743
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
    and current batch33 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
  locator: Entire maintained target, including history, all field-level evidence,
    graph and discussions
  accessed_at: '2026-10-22T02:24:38Z'
  support: context_only
  summary: Complete record read without scientific changes.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent description, grounding, component_role and essentiality,
    lines388–444
  accessed_at: '2026-10-22T02:24:38Z'
  support: context_only
  summary: Components denote molecular building blocks; GO may identify a protein
    subcomplex, while lipid grounding is chemical. Essentiality denotes whether the
    structure forms without a component, not biochemical function.
- evidence_id: neighbor-mitochondrial_crista
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_crista.yaml
  locator: Frozen maintained neighbor; complete boundary context read
  accessed_at: '2026-10-22T02:24:38Z'
  support: context_only
  summary: The neighbor provides maintained boundary/parthood context, not independent
    experimental evidence or automatic endorsement of its other assertions.
- evidence_id: neighbor-mitochondrial_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_envelope.yaml
  locator: Frozen maintained neighbor; complete boundary context read
  accessed_at: '2026-10-22T02:24:38Z'
  support: context_only
  summary: The neighbor provides maintained boundary/parthood context, not independent
    experimental evidence or automatic endorsement of its other assertions.
- evidence_id: neighbor-mitochondrial_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_intermembrane_space.yaml
  locator: Frozen maintained neighbor; complete boundary context read
  accessed_at: '2026-10-22T02:24:38Z'
  support: context_only
  summary: The neighbor provides maintained boundary/parthood context, not independent
    experimental evidence or automatic endorsement of its other assertions.
- evidence_id: neighbor-mitochondrial_matrix
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_matrix.yaml
  locator: Frozen maintained neighbor; complete boundary context read
  accessed_at: '2026-10-22T02:24:38Z'
  support: context_only
  summary: The neighbor provides maintained boundary/parthood context, not independent
    experimental evidence or automatic endorsement of its other assertions.
- evidence_id: mitochondrial-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005740,GO:0031967,GO:0005739,GO:0005741,GO:0005743,GO:0005758,GO:0005742,GO:0030150,GO:0006119,GO:0097002,GO:0030061,GO:0044284,GO:0007007,GO:0019866,GO:0031966,GO:0005759,GO:0031970
  locator: Exact requested term set in URL; complete labels, definitions, synonyms,
    active flags and returned child relations
  accessed_at: '2026-10-22T02:20:26.033961Z'
  support: supports
  summary: The17 active native GO identities, definitions, synonym scopes and returned
    child relations were read. The target identity, relevant topology and functions
    match the designated terms. Whole membrane classes remain distinct from molecular
    lipids.
  snapshot_sha256: 2c72dffea60ae2bb60f90226c19d9b15830680253c902e5c1c8d717d304339a9
- evidence_id: mitochondrial-agent-tax2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: taxId/scientificName/rank/lineage
  accessed_at: '2026-10-22T02:20:26.034869Z'
  support: supports
  summary: Native ENA confirms Eukaryota2759; taxonomic identity alone does not quantify
    organelle prevalence.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: mitochondrial-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId/scientificName/rank/lineage
  accessed_at: '2026-10-22T02:20:26.781370Z'
  support: supports
  summary: Native ENA confirms Saccharomyces cerevisiae4932, distinct from any specific
    laboratory strain.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: mitochondrial-agent-sickmann2003-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.2135385100&format=json&resultType=core
  locator: Exact native MED result and full abstract
  accessed_at: '2026-10-22T02:20:26.034608Z'
  support: supports
  summary: Exact DOI, PMID, title, authors, year and complete abstract inspected;
    primary experimental study.
  snapshot_sha256: c5b3c15ca5f8b0e8cc638d016ec8f1a40c9392ddd1dda9230aa352066e331080
- evidence_id: mitochondrial-agent-sickmann2003-pmc-exact
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC263752/
  locator: Complete abstract, unheaded Introduction, Materials and Methods, all Results
    and Discussion subsections, Figures1–5 captions. No figure pixels or separate
    supporting-table data reanalysis.
  accessed_at: '2026-10-22T02:21:23.144846Z'
  support: supports
  summary: Authentic yeast mitochondrial proteomics identifies known inner-membrane
    oxidative-phosphorylation components and matrix/outer-membrane proteins. Most
    experiments use YPH499 grown in glycerol; MR103 is used for tagged-Tom22 controls.
    The study explicitly discusses trace contamination, dual localization and limits
    to complete proteome coverage.
  snapshot_sha256: dbb60e1208e1203366064cd5220edfc437a809737bc245d1bb927b3c1c626fde
- evidence_id: mitochondrial-agent-friedman2015-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554/elife.07739&format=json&resultType=core
  locator: Exact native MED result and full abstract
  accessed_at: '2026-10-22T02:10:24.454393Z'
  support: supports
  summary: Exact DOI, PMID, title, authors, year and complete abstract inspected;
    primary experimental study.
  snapshot_sha256: c0346d49ef66ef89b48bcb0cda60019732342884dae87eaf75e9b0fe8e80f3a4
- evidence_id: mitochondrial-agent-friedman2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/PMC4434539.1.xml
  locator: Complete Introduction s1, main Results prose s2-1–s2-7, Discussion s3 and
    all Methods s4-1–s4-9; Figure1/4/7 and their embedded supplement captions read.
    No pixels or separate source-data tables reanalysis.
  accessed_at: '2026-10-22T02:10:55.341589Z'
  support: supports
  summary: Primary W303-derived yeast genetics, microscopy and proteomic/biochemical
    assays support inner-boundary/crista organization. Electron microscopy Methods
    specify chemically fixed resin sections examined by TEM at100kV, not tomography.
    Proteomics uses immunopurifications from cell extracts, with separate isolated-mitochondrial
    assays. MICOS deletion affects normal morphology/function while membranes and
    respiratory complexes can persist.
  snapshot_sha256: 8d1082e98a558176fbd86c80851d3467e7bf41c986f38b8dfe00810c3903a345
- evidence_id: mitochondrial-agent-friedman2014-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature12985&format=json&resultType=core
  locator: Exact native MED result and full abstract
  accessed_at: '2026-10-22T02:10:24.454595Z'
  support: supports
  summary: Exact DOI, PMID, title, authors, year and complete abstract inspected;
    literature review, not a primary experiment.
  snapshot_sha256: 390af3048cd69551f299e85c996efeab680b69e214c78b6d5d02bb24c0945d0a
- evidence_id: mitochondrial-agent-friedman2014-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4075653.1/PMC4075653.1.xml
  locator: Complete S5 Internal determinants of mitochondrial division; native complete
    abstract separately read. Other review sections and figure pixels not claimed.
  accessed_at: '2026-10-22T02:10:55.342035Z'
  support: supports
  summary: Review-tier context distinguishes the boundary region, crista invaginations
    and junctions, and discusses scaffold-based architecture without establishing
    a universal molecular formation requirement.
  snapshot_sha256: 37cb298ab74e8ff5524164dcfa6563f44b3fc8f0833ce2049dad7d11f8e6ae97
- evidence_id: friedman-method-search
  kind: search
  reference: rg --no-ignore --hidden -n -i tomogra|tomogram|tilt.series /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial-agent/friedman2015-body.txt
  locator: Complete derived native JATS body prose and embedded captions; literal
    case-insensitive search
  accessed_at: '2026-10-22T02:22:21.897710Z'
  support: context_only
  summary: No tomogra, tomogram or tilt.series lexical matches in the complete article
    body/captions. Exit1 means no search match, not a validator failure. The positive
    Methods statement specifying TEM is the primary finding support.
  snapshot_sha256: 8a48f227ca91ea3da4a772f2e98d57c401fff06717a63ac63e3008e74f854a59
  search_scope: Ignored-file-inclusive rg on the exact complete native JATS body/caption
    text derivative; separate supplementary raw files not included.
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:18:36Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml'
  snapshot_sha256: a38ccdec3f092a339b78800f141f5bc286c8ca9bd876d71c309c69a6567d7c16
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
    --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_inner_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:18:37Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_inner_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_inner_membrane-strict.tsv"
  snapshot_sha256: 2abe50c301f3013c32227d5365bae9091682e3f7685a6cfa299a348f6de80a9d
- evidence_id: mitochondrial-agent-roger2017-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.cub.2017.09.015%22
  locator: Complete exact native MED result and abstract
  accessed_at: '2026-10-22T02:20:19.311159Z'
  support: supports
  summary: Exact DOI10.1016/j.cub.2017.09.015, title, authors, year and complete abstract
    confirm Roger, Munoz-Gomez and Kamikawa2017 as a literature review.
  snapshot_sha256: 79f51ae3193414033e9a85ac0cf692509624280a75f6e63345c2edf5389fef45
- evidence_id: mitochondrial-agent-roger2017-pdf
  kind: authority
  reference: https://ecsolab.com/assets/pdf/roger_etal_2017.pdf
  locator: First printed pageR1177 identity/abstract/Introduction; R1184 opening Diversity
    of Mitochondrial Functions in Anaerobic Eukaryotes paragraph; R1186 hydrogenosome/mitosome
    comparison and concluding reduction paragraph. Figures and remaining review not
    inspected.
  accessed_at: '2026-10-22T02:21:01.426006Z'
  support: supports
  summary: Review-tier evidence independently supports reduced/no cristae in anaerobic
    lineages and diversity including hydrogenosomes and mitosomes. It describes a
    continuum and evolutionary reductions; it supplies no population-frequency estimate.
  snapshot_sha256: b0ddb1d89fda3d1e929ef0d65c68b15864c0e602a5736305abbb08673010982e
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 13 of 13 collected target identifiers returned OK. No residuals. Native
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
  topic: Inner bilayer and exact hierarchy
  outcome: supported
  target_ids:
  - GO:0005743
  summary: The definition and all three exact synonyms match GO0005743. Both maintained
    parents are direct native is_a parents via their child lists; crista parthood
    and envelope topology are supported by native definitions/relations. Matrix and
    intermembrane space are distinct.
  evidence_ids:
  - record
  - mitochondrial-agent-go
- assessment_id: composition
  area: grounding
  topic: Collective bilayer without false chemical grounding
  outcome: supported
  target_ids:
  - GO:0005743
  summary: The sole LIPID row is explicitly reviewed-label-only constituting material,
    with no whole-membrane GO substituted for a molecular lipid. Its role correctly
    separates matrix and intermembrane space.
  evidence_ids:
  - record
  - schema
  - mitochondrial-agent-go
  - mitochondrial-agent-friedman2015-jats
- assessment_id: necessity
  area: evidence
  topic: Individual formation requirements remain unresolved
  outcome: unknown
  target_ids:
  - GO:0005743
  summary: Collective membrane material is constitutive; the inspected studies do
    not establish experimental formation necessity of every lipid species. MICOS/respiratory
    phenotypes do not imply that a membrane cannot form, and ESSENTIAL is not a universal
    claim about all proteins or cardiolipin.
  evidence_ids:
  - record
  - schema
  - mitochondrial-agent-go
  - mitochondrial-agent-friedman2015-jats
- assessment_id: scope
  area: scope
  topic: Correct yeast example with method attribution concern
  outcome: concern
  target_ids:
  - GO:0005743
  summary: The organism and genetic/biochemical architecture context are supported.
    However, the canonical note calls the sole Friedman2015 citation electron-tomographic;
    its Methods specify ultrathin-section TEM. Its cell-extract immunopurification
    proteomics and isolated-mitochondrial assays should also remain distinct from
    the broad purified-mitochondrial inventory in Sickmann2003. Roger2017 independently
    supports the bounded reduced-organelle qualifier across anaerobic lineages; this
    is review-tier diversity context, not a prevalence census.
  evidence_ids:
  - record
  - mitochondrial-agent-sickmann2003-pmc-exact
  - mitochondrial-agent-friedman2015-jats
  - mitochondrial-agent-tax2759
  - mitochondrial-agent-tax4932
  - mitochondrial-agent-roger2017-meta
  - mitochondrial-agent-roger2017-pdf
- assessment_id: function-graph
  area: graph
  topic: Respiration and five descriptive topology edges
  outcome: supported
  target_ids:
  - GO:0005743
  summary: Native process definition and the primary recovered oxidative-phosphorylation
    machinery support the coarse ATP-synthesis function. All five NONMECHANISTIC edges
    preserve correct envelope/crista/matrix/intermembrane-space boundaries. No single
    respiratory complex, temporal assembly sequence or quantitative proton-gradient
    measurement is asserted.
  evidence_ids:
  - record
  - mitochondrial-agent-go
  - mitochondrial-agent-sickmann2003-pmc-exact
  - mitochondrial-agent-friedman2015-jats
  - mitochondrial-agent-friedman2014-jats
- assessment_id: completeness
  area: completeness
  topic: Optional lipid mapping
  outcome: supported
  target_ids:
  - GO:0005743
  summary: The existing molecular-grounding TODO is candid. Absence of a detailed
    respiratory or lipid inventory alone is not a defect of this boundary record.
  evidence_ids:
  - record
  - schema
  - mitochondrial-agent-go
findings:
- finding_id: F1
  issue_key: mitochondrial-inner-membrane-friedman-microscopy-attribution
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Match the canonical microscopy method to Friedman2015
  description: The canonical note says electron-tomographic studies but its sole citation
    describes resin sections examined by conventional transmission electron microscopy,
    together with genetics and fluorescence/biochemical assays. The organism and architecture
    research context remain correct.
  target_ids:
  - GO:0005743
  field_paths:
  - canonical_examples[0].note
  - canonical_examples[0].reference
  evidence_ids:
  - record
  - mitochondrial-agent-friedman2015-jats
  - friedman-method-search
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
    role: maintained scientific record
  rule_id: .claude/skills/review-yaml-record/SKILL.md:claim-level evidence placement
  native_severity: minor
  normalization_reason: This is bounded experimental-method provenance precision.
    It does not invalidate the membrane identity, yeast occurrence, actual genetic/EM
    architecture evidence or respiratory function.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005743
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
    role: maintained scientific record
  description: In separately authorized curation, describe Friedman2015 as genetic
    and electron-microscopic analysis, or attach an independently inspected tomography
    source to any retained tomography assertion. Keep purified-proteome and interaction-proteomics
    contexts paired with their actual studies.
  acceptance_checks:
  - The Friedman2015-linked note accurately identifies section TEM, not electron tomography.
  - Any additional tomography or broad purified-mitochondrial inventory clause has
    its own inspected source; retain correct yeast identity and supported biology.
limitations:
- COMMON and VARIABLE are qualitative distribution annotations, not measured prevalence.
  Native taxon records verify names only; the specific anaerobic-lineage exceptions
  are not comprehensively enumerated or independently surveyed here.
- Collective constitutive material, individual molecular formation necessity and biochemical
  function remain separate. No species-independent lipid composition, stoichiometry
  or obligatory complete protein inventory is inferred.
- No raw imaging, figure pixels, supporting-table datasets or quantitative reanalysis
  was performed. Native ontology definitions support topology; a biological relation
  is not described as a captured direct GO edge unless returned in the native response.
- The two numeric PMC routes returned HTML challenges, but genuine exact-prefix Sickmann
  HTML and Chacinska S3 JATS were recovered. Sickmann EuropePMC XML returned500. A
  longer-prefix S3 collision retrieved a different article and is explicitly excluded,
  with its diagnostic receipt preserved.
- Sickmann2003 complete main text/Methods/captions was read; separate supporting tables
  were not. YPH499/MR103 growth and purification context, possible contaminants and
  incomplete proteome coverage are preserved.
- Friedman2015 complete scientific main prose and Methods were read with selected
  captions; no separate source-data files or pixels were inspected. The2014 review
  is limited to complete S5 and its native abstract. Source copies retain their original
  B32 access times and hashes.
- Roger2017 review-tier context was subsequently read only in the exact evidence-locator
  scope. It supports general reduced-organelle diversity, not an exhaustive survey,
  individual membrane lipid necessity or measured prevalence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- No scientific content, history or status changed. Parent owns finalization and persistence;
  source URL/UTC/SHA provenance retained.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
