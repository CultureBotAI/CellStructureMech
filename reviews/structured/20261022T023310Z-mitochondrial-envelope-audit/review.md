# Mitochondrial envelope molecular grounding and import review

- Review: 20261022T023310Z-mitochondrial-envelope-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:18:28Z
- Finished UTC: 2026-10-22T02:33:10Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Envelope identity, yeast scope, import and respiration context are supported. One major finding concerns two whole-membrane GO identifiers used as molecular lipid component groundings.

## Scope And Provenance

Entire exact target and frozen boundary neighbors; all asserted native identifiers and citation identities; specified genuine source sections; molecular grounding, distribution, examples, functions and every graph edge.

Selection: Batch33 target1; complete initial native inspect/schema/strict gates0 at unchanged f97b1abe before scientific assessment.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005740 | data/structures/membrane_organelle/mitochondrial_envelope.yaml | maintained | mitochondrial envelope |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005740 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005740 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005740 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Organism-specific protein-example applicability | not_applicable | False | GO:0005740 | The target has no UniProt protein examples, gene-symbol assertions or GENE_OR_PROTEIN nodes requiring native protein verification. Component and graph identities were manually assessed. |
| Claim-level scientific review | passed | True | GO:0005740 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005740 | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005740 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005740 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005740 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005740 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005740 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact double-envelope identity and topology

identity: supported. Targets: GO:0005740.

GO0005740 matches the whole definition including the intermembrane space. Native organelle-envelope is_a and mitochondrial part_of links agree; individual membranes and TOM are biological parts supported by the respective definitions and import review. This is not a single bilayer or the entire mitochondrial interior.

### Two lipid rows misuse whole membrane groundings

grounding: concern. Targets: GO:0005740.

Both LIPID constituents are named and grounded as complete mitochondrial membranes (GO0005741 and GO0005743), then equated to the corresponding graph nodes via component_ref. The schema requires molecular lipid identity in these rows. Correct membrane parthood does not make a whole membrane a molecular lipid. By contrast, the TOM PROTEIN_COMPLEX row correctly uses GO0005742.

### No assembly necessity inferred

evidence: unknown. Targets: GO:0005740.

UNKNOWN values are retained. The sources support material/complex presence and import activity, but do not establish formation necessity of every lipid species or each optional import subcomplex for the whole envelope. Functional dependence is not relabeled assembly necessity.

### Matrix import and oxidative phosphorylation

evidence: supported. Targets: GO:0005740.

TOM is correctly only the outer-membrane entry step for the specific TOM–TIM23–PAM matrix pathway, and inner-envelope oxidative phosphorylation is supported by native process definition and Sickmann coverage of the inner-membrane machinery. No claim that TOM alone translocates the inner membrane or that the outer bilayer alone performs respiration is made.

### Seven compartment-level edges

graph: concern. Targets: GO:0005740.

All seven NONMECHANISTIC topology/import/respiration descriptions are supported at their coarse scope. The two component_ref links inherit the molecular grounding concern; removing that conflation should preserve valid membrane nodes, enclosing topology and TOM entry.

### Yeast canonical example and qualified eukaryotic distribution

scope: supported. Targets: GO:0005740.

The purified yeast mitochondrial example and qualitative COMMON occurrence are supported. The primary experiments are predominantly YPH499, not a census of every Saccharomyces strain. VARIABLE restricts the broader row to canonical mitochondria; native taxonomy does not itself prove all anaerobic lineage details. Roger2017 independently supports the bounded reduced-organelle qualifier across anaerobic lineages; this is review-tier diversity context, not a prevalence census.

### Optional downstream complexes

completeness: supported. Targets: GO:0005740.

The open TIM/SAM/MIA/respiratory-complex follow-up does not claim those complexes are absent. It is not a missing required inventory; exact subcomplex rows remain a separate curation choice.

## Findings

### F1: Separate whole mitochondrial membranes from molecular lipid components

major / open / confirmed; issue key: mitochondrial-envelope-lipid-whole-membrane-grounding.

The two LIPID components use GO0005741/GO0005743, which identify whole mitochondrial membranes, and graph component_ref links repeat those identities. This violates the molecular-building-block and lipid-grounding contract while leaving the envelope topology itself valid.

## Recommended Actions And Acceptance Checks

### A1

In separately authorized curation, retain the whole membranes in has_part and as topology nodes; represent genuinely molecular/collective lipid material with accurate label-only status unless an exact chemical grounding is verified. Remove or revise component_ref links that equate whole membranes to molecular lipids.

- Neither complete membrane GO term is used as the chemical identity of a LIPID component.
- The graph keeps correct whole-membrane topology without false molecular equivalence; TOM remains a correctly grounded protein subcomplex.
- Do not invent lipid species, stoichiometry or formation necessity to fill the revised rows.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/mitochondrial_envelope.yaml; Entire maintained target, including history, all field-level evidence, graph and discussions | context_only | Complete record read without scientific changes. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent description, grounding, component_role and essentiality, lines388–444 | context_only | Components denote molecular building blocks; GO may identify a protein subcomplex, while lipid grounding is chemical. Essentiality denotes whether the structure forms without a component, not biochemical function. |
| neighbor-mitochondrial_inner_membrane | data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml; Frozen maintained neighbor; complete boundary context read | context_only | The neighbor provides maintained boundary/parthood context, not independent experimental evidence or automatic endorsement of its other assertions. |
| neighbor-mitochondrial_intermembrane_space | data/structures/membrane_organelle/mitochondrial_intermembrane_space.yaml; Frozen maintained neighbor; complete boundary context read | context_only | The neighbor provides maintained boundary/parthood context, not independent experimental evidence or automatic endorsement of its other assertions. |
| neighbor-mitochondrial_outer_membrane | data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml; Frozen maintained neighbor; complete boundary context read | context_only | The neighbor provides maintained boundary/parthood context, not independent experimental evidence or automatic endorsement of its other assertions. |
| neighbor-mitochondrion | data/structures/membrane_organelle/mitochondrion.yaml; Frozen maintained neighbor; complete boundary context read | context_only | The neighbor provides maintained boundary/parthood context, not independent experimental evidence or automatic endorsement of its other assertions. |
| mitochondrial-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005740,GO:0031967,GO:0005739,GO:0005741,GO:0005743,GO:0005758,GO:0005742,GO:0030150,GO:0006119,GO:0097002,GO:0030061,GO:0044284,GO:0007007,GO:0019866,GO:0031966,GO:0005759,GO:0031970; Exact requested term set in URL; complete labels, definitions, synonyms, active flags and returned child relations | supports | The17 active native GO identities, definitions, synonym scopes and returned child relations were read. The target identity, relevant topology and functions match the designated terms. Whole membrane classes remain distinct from molecular lipids. |
| mitochondrial-agent-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; taxId/scientificName/rank/lineage | supports | Native ENA confirms Eukaryota2759; taxonomic identity alone does not quantify organelle prevalence. |
| mitochondrial-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId/scientificName/rank/lineage | supports | Native ENA confirms Saccharomyces cerevisiae4932, distinct from any specific laboratory strain. |
| mitochondrial-agent-sickmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.2135385100&amp;format=json&amp;resultType=core; Exact native MED result and full abstract | supports | Exact DOI, PMID, title, authors, year and complete abstract inspected; primary experimental study. |
| mitochondrial-agent-sickmann2003-pmc-exact | https://pmc.ncbi.nlm.nih.gov/articles/PMC263752/; Complete abstract, unheaded Introduction, Materials and Methods, all Results and Discussion subsections, Figures1–5 captions. No figure pixels or separate supporting-table data reanalysis. | supports | Authentic yeast mitochondrial proteomics identifies known inner-membrane oxidative-phosphorylation components and matrix/outer-membrane proteins. Most experiments use YPH499 grown in glycerol; MR103 is used for tagged-Tom22 controls. The study explicitly discusses trace contamination, dual localization and limits to complete proteome coverage. |
| mitochondrial-agent-chacinska2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016/j.cell.2009.08.005&amp;format=json&amp;resultType=core; Exact native MED result and full abstract | supports | Exact DOI, PMID, title, authors, year and complete abstract inspected; literature review, not a primary experiment. |
| mitochondrial-agent-chacinska2009-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4099469.1/PMC4099469.1.xml; Complete S1/S2/S6–S10/S12–S14/S16/S22/S23. Other sections, full tables and figure pixels not claimed as inspected. | supports | Review-tier synthesis supports TOM as the general entry machinery, downstream TIM23-PAM matrix import and the intermembrane-space carrier route. It distinguishes matrix import, inner-membrane sorting and MIA import; pathways and tentative mechanisms are not converted into a universal single route. |
| schema-result | just validate data/structures/membrane_organelle/mitochondrial_envelope.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/mitochondrial_envelope.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/mitochondrial_envelope.yaml --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_envelope-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitochondrial_envelope.yaml --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_envelope-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_envelope-strict.tsv |
| mitochondrial-agent-roger2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.cub.2017.09.015%22; Complete exact native MED result and abstract | supports | Exact DOI10.1016/j.cub.2017.09.015, title, authors, year and complete abstract confirm Roger, Munoz-Gomez and Kamikawa2017 as a literature review. |
| mitochondrial-agent-roger2017-pdf | https://ecsolab.com/assets/pdf/roger_etal_2017.pdf; First printed pageR1177 identity/abstract/Introduction; R1184 opening Diversity of Mitochondrial Functions in Anaerobic Eukaryotes paragraph; R1186 hydrogenosome/mitosome comparison and concluding reduction paragraph. Figures and remaining review not inspected. | supports | Review-tier evidence independently supports reduced/no cristae in anaerobic lineages and diversity including hydrogenosomes and mitosomes. It describes a continuum and evolutionary reductions; it supplies no population-frequency estimate. |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/mitochondrial_envelope.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
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
- Chacinska2009 is review-tier, read only in S1/S2/S6–S10/S12–S14/S16/S22/S23; it is not a new primary experiment and no access to the remaining sections, full tables or figure pixels is claimed.
- Sickmann2003 complete main text/Methods/captions was read; separate supporting tables were not. YPH499/MR103 growth and purification context, possible contaminants and incomplete proteome coverage are preserved.
- Roger2017 review-tier context was subsequently read only in the exact evidence-locator scope. It supports general reduced-organelle diversity, not an exhaustive survey, individual membrane lipid necessity or measured prevalence.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- No scientific content, history or status changed. Parent owns finalization and persistence; source URL/UTC/SHA provenance retained.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T023310Z-mitochondrial-envelope-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Mitochondrial envelope molecular grounding and import review
started_at: '2026-10-22T02:18:28Z'
finished_at: '2026-10-22T02:33:10Z'
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
summary: Envelope identity, yeast scope, import and respiration context are supported.
  One major finding concerns two whole-membrane GO identifiers used as molecular lipid
  component groundings.
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
  - path: data/structures/membrane_organelle/mitochondrial_envelope.yaml
    sha256: e750843104d72fd05608a59a650410e8bc8103b02697f5a1add9fd5bd31e283f
    role: target
  - path: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
    sha256: 63301d7a679c30a2afadd331aa17b3559852b09c038e97dab14f53e40d34ed1f
    role: context
  - path: data/structures/membrane_organelle/mitochondrial_intermembrane_space.yaml
    sha256: 9b1d3fcf94d5a598d61810b56580265af6c9325890c673eab3532645e4cb48ea
    role: context
  - path: data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
    sha256: c65c2f350a175ad96c5b5fbb0128fef48a17ece11571fde4bbe898644599d78a
    role: context
  - path: data/structures/membrane_organelle/mitochondrion.yaml
    sha256: 9152cb04bd6e1faf9f845187d723336a26136fa7d568d5cbb2b54070319aceac
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
- target_id: GO:0005740
  path: data/structures/membrane_organelle/mitochondrial_envelope.yaml
  label: mitochondrial envelope
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_envelope.yaml
    role: maintained scientific record
scope:
  description: Entire exact target and frozen boundary neighbors; all asserted native
    identifiers and citation identities; specified genuine source sections; molecular
    grounding, distribution, examples, functions and every graph edge.
  selection: Batch33 target1; complete initial native inspect/schema/strict gates0
    at unchanged f97b1abe before scientific assessment.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005740
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005740
  command: just validate data/structures/membrane_organelle/mitochondrial_envelope.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005740
  command: just validate-strict data/structures/membrane_organelle/mitochondrial_envelope.yaml
    --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_envelope-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005740
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: protein-applicability
  name: Organism-specific protein-example applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005740
  summary: The target has no UniProt protein examples, gene-symbol assertions or GENE_OR_PROTEIN
    nodes requiring native protein verification. Component and graph identities were
    manually assessed.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005740
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-mitochondrial_inner_membrane
  - neighbor-mitochondrial_intermembrane_space
  - neighbor-mitochondrial_outer_membrane
  - neighbor-mitochondrion
  - mitochondrial-agent-go
  - mitochondrial-agent-tax2759
  - mitochondrial-agent-tax4932
  - mitochondrial-agent-sickmann2003-meta
  - mitochondrial-agent-sickmann2003-pmc-exact
  - mitochondrial-agent-chacinska2009-meta
  - mitochondrial-agent-chacinska2009-jats
  - mitochondrial-agent-roger2017-meta
  - mitochondrial-agent-roger2017-pdf
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005740
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
  - GO:0005740
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
  - GO:0005740
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
  - GO:0005740
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
  - GO:0005740
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
  - GO:0005740
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
  reference: data/structures/membrane_organelle/mitochondrial_envelope.yaml
  locator: Entire maintained target, including history, all field-level evidence,
    graph and discussions
  accessed_at: '2026-10-22T02:24:21Z'
  support: context_only
  summary: Complete record read without scientific changes.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent description, grounding, component_role and essentiality,
    lines388–444
  accessed_at: '2026-10-22T02:24:21Z'
  support: context_only
  summary: Components denote molecular building blocks; GO may identify a protein
    subcomplex, while lipid grounding is chemical. Essentiality denotes whether the
    structure forms without a component, not biochemical function.
- evidence_id: neighbor-mitochondrial_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_inner_membrane.yaml
  locator: Frozen maintained neighbor; complete boundary context read
  accessed_at: '2026-10-22T02:24:21Z'
  support: context_only
  summary: The neighbor provides maintained boundary/parthood context, not independent
    experimental evidence or automatic endorsement of its other assertions.
- evidence_id: neighbor-mitochondrial_intermembrane_space
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_intermembrane_space.yaml
  locator: Frozen maintained neighbor; complete boundary context read
  accessed_at: '2026-10-22T02:24:21Z'
  support: context_only
  summary: The neighbor provides maintained boundary/parthood context, not independent
    experimental evidence or automatic endorsement of its other assertions.
- evidence_id: neighbor-mitochondrial_outer_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
  locator: Frozen maintained neighbor; complete boundary context read
  accessed_at: '2026-10-22T02:24:21Z'
  support: context_only
  summary: The neighbor provides maintained boundary/parthood context, not independent
    experimental evidence or automatic endorsement of its other assertions.
- evidence_id: neighbor-mitochondrion
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrion.yaml
  locator: Frozen maintained neighbor; complete boundary context read
  accessed_at: '2026-10-22T02:24:21Z'
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
- evidence_id: mitochondrial-agent-chacinska2009-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016/j.cell.2009.08.005&format=json&resultType=core
  locator: Exact native MED result and full abstract
  accessed_at: '2026-10-22T02:20:26.034500Z'
  support: supports
  summary: Exact DOI, PMID, title, authors, year and complete abstract inspected;
    literature review, not a primary experiment.
  snapshot_sha256: 7aa046f6810f431b585710c8f5a4867791023f1491928649449817119e305f59
- evidence_id: mitochondrial-agent-chacinska2009-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4099469.1/PMC4099469.1.xml
  locator: Complete S1/S2/S6–S10/S12–S14/S16/S22/S23. Other sections, full tables
    and figure pixels not claimed as inspected.
  accessed_at: '2026-10-22T02:21:09.775994Z'
  support: supports
  summary: Review-tier synthesis supports TOM as the general entry machinery, downstream
    TIM23-PAM matrix import and the intermembrane-space carrier route. It distinguishes
    matrix import, inner-membrane sorting and MIA import; pathways and tentative mechanisms
    are not converted into a universal single route.
  snapshot_sha256: 010e4b847c377e924ee1635a33ce3479a86b63183d5e5b4524a6904ff555ceba
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/mitochondrial_envelope.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:18:30Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/mitochondrial_envelope.yaml'
  snapshot_sha256: 3d7b4f6c609c6f47ca962163e2eecd64e1cc600c291875e607f6ad55149c0391
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/mitochondrial_envelope.yaml
    --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_envelope-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:18:31Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitochondrial_envelope.yaml\
    \ --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_envelope-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_envelope-strict.tsv"
  snapshot_sha256: 7904399d0880cdc76e9aa68489fdf885832dc4494a15a8144b739382bb610165
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
  locator: data/structures/membrane_organelle/mitochondrial_envelope.yaml; native
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
  topic: Exact double-envelope identity and topology
  outcome: supported
  target_ids:
  - GO:0005740
  summary: GO0005740 matches the whole definition including the intermembrane space.
    Native organelle-envelope is_a and mitochondrial part_of links agree; individual
    membranes and TOM are biological parts supported by the respective definitions
    and import review. This is not a single bilayer or the entire mitochondrial interior.
  evidence_ids:
  - record
  - mitochondrial-agent-go
  - mitochondrial-agent-chacinska2009-jats
- assessment_id: components
  area: grounding
  topic: Two lipid rows misuse whole membrane groundings
  outcome: concern
  target_ids:
  - GO:0005740
  summary: Both LIPID constituents are named and grounded as complete mitochondrial
    membranes (GO0005741 and GO0005743), then equated to the corresponding graph nodes
    via component_ref. The schema requires molecular lipid identity in these rows.
    Correct membrane parthood does not make a whole membrane a molecular lipid. By
    contrast, the TOM PROTEIN_COMPLEX row correctly uses GO0005742.
  evidence_ids:
  - record
  - schema
  - mitochondrial-agent-go
  - mitochondrial-agent-chacinska2009-jats
- assessment_id: necessity
  area: evidence
  topic: No assembly necessity inferred
  outcome: unknown
  target_ids:
  - GO:0005740
  summary: UNKNOWN values are retained. The sources support material/complex presence
    and import activity, but do not establish formation necessity of every lipid species
    or each optional import subcomplex for the whole envelope. Functional dependence
    is not relabeled assembly necessity.
  evidence_ids:
  - record
  - schema
  - mitochondrial-agent-sickmann2003-pmc-exact
  - mitochondrial-agent-chacinska2009-jats
- assessment_id: functions
  area: evidence
  topic: Matrix import and oxidative phosphorylation
  outcome: supported
  target_ids:
  - GO:0005740
  summary: TOM is correctly only the outer-membrane entry step for the specific TOM–TIM23–PAM
    matrix pathway, and inner-envelope oxidative phosphorylation is supported by native
    process definition and Sickmann coverage of the inner-membrane machinery. No claim
    that TOM alone translocates the inner membrane or that the outer bilayer alone
    performs respiration is made.
  evidence_ids:
  - record
  - mitochondrial-agent-go
  - mitochondrial-agent-chacinska2009-jats
  - mitochondrial-agent-sickmann2003-pmc-exact
- assessment_id: graph
  area: graph
  topic: Seven compartment-level edges
  outcome: concern
  target_ids:
  - GO:0005740
  summary: All seven NONMECHANISTIC topology/import/respiration descriptions are supported
    at their coarse scope. The two component_ref links inherit the molecular grounding
    concern; removing that conflation should preserve valid membrane nodes, enclosing
    topology and TOM entry.
  evidence_ids:
  - record
  - mitochondrial-agent-go
  - mitochondrial-agent-chacinska2009-jats
  - mitochondrial-agent-sickmann2003-pmc-exact
- assessment_id: scope
  area: scope
  topic: Yeast canonical example and qualified eukaryotic distribution
  outcome: supported
  target_ids:
  - GO:0005740
  summary: The purified yeast mitochondrial example and qualitative COMMON occurrence
    are supported. The primary experiments are predominantly YPH499, not a census
    of every Saccharomyces strain. VARIABLE restricts the broader row to canonical
    mitochondria; native taxonomy does not itself prove all anaerobic lineage details.
    Roger2017 independently supports the bounded reduced-organelle qualifier across
    anaerobic lineages; this is review-tier diversity context, not a prevalence census.
  evidence_ids:
  - record
  - mitochondrial-agent-go
  - mitochondrial-agent-sickmann2003-pmc-exact
  - mitochondrial-agent-chacinska2009-jats
  - mitochondrial-agent-tax2759
  - mitochondrial-agent-tax4932
  - mitochondrial-agent-roger2017-meta
  - mitochondrial-agent-roger2017-pdf
- assessment_id: completeness
  area: completeness
  topic: Optional downstream complexes
  outcome: supported
  target_ids:
  - GO:0005740
  summary: The open TIM/SAM/MIA/respiratory-complex follow-up does not claim those
    complexes are absent. It is not a missing required inventory; exact subcomplex
    rows remain a separate curation choice.
  evidence_ids:
  - record
  - schema
  - mitochondrial-agent-chacinska2009-jats
findings:
- finding_id: F1
  issue_key: mitochondrial-envelope-lipid-whole-membrane-grounding
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Separate whole mitochondrial membranes from molecular lipid components
  description: The two LIPID components use GO0005741/GO0005743, which identify whole
    mitochondrial membranes, and graph component_ref links repeat those identities.
    This violates the molecular-building-block and lipid-grounding contract while
    leaving the envelope topology itself valid.
  target_ids:
  - GO:0005740
  field_paths:
  - components[0]
  - components[1]
  - causal_graphs[0].nodes[2].component_ref
  - causal_graphs[0].nodes[3].component_ref
  evidence_ids:
  - record
  - schema
  - mitochondrial-agent-go
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_envelope.yaml
    role: maintained scientific record
  rule_id: src/cellstructuremech/schema/cellstructuremech.yaml:StructuralComponent.grounding
  native_severity: major
  normalization_reason: Wrong molecular ontology grounding is major under the local
    rubric. The finding is limited to the two lipid rows and their equivalence links;
    it does not reject membrane parthood, the whole-envelope identity or TOM.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005740
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_envelope.yaml
    role: maintained scientific record
  description: In separately authorized curation, retain the whole membranes in has_part
    and as topology nodes; represent genuinely molecular/collective lipid material
    with accurate label-only status unless an exact chemical grounding is verified.
    Remove or revise component_ref links that equate whole membranes to molecular
    lipids.
  acceptance_checks:
  - Neither complete membrane GO term is used as the chemical identity of a LIPID
    component.
  - The graph keeps correct whole-membrane topology without false molecular equivalence;
    TOM remains a correctly grounded protein subcomplex.
  - Do not invent lipid species, stoichiometry or formation necessity to fill the
    revised rows.
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
- Chacinska2009 is review-tier, read only in S1/S2/S6–S10/S12–S14/S16/S22/S23; it
  is not a new primary experiment and no access to the remaining sections, full tables
  or figure pixels is claimed.
- Sickmann2003 complete main text/Methods/captions was read; separate supporting tables
  were not. YPH499/MR103 growth and purification context, possible contaminants and
  incomplete proteome coverage are preserved.
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
