# Mitochondrial outer membrane identity and source review

- Review: 20261022T023315Z-mitochondrial-outer-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:18:45Z
- Finished UTC: 2026-10-22T02:33:15Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

No concrete curation defect observed within the explicitly bounded scientific evidence scope.

## Scope And Provenance

Entire single target: identity, hierarchy, composition where present, taxonomy, canonical example, functions and every graph edge.

Selection: Target 7 of batch33 in strict uncovered path order from fresh origin/main f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005741 | data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml | maintained | mitochondrial outer membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0005741 | Focused native check passed; scientific scope assessed separately. |
| Native protein causal-graphs | passed | True | GO:0005741 | Focused native check passed; scientific scope assessed separately. |
| Focused native schema | passed | True | GO:0005741 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005741 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005741 | No expression-module or regulatory-module claim is assessed; direct structure and import/proteomics evidence is used. |
| Claim-level scientific review | passed | True | GO:0005741 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005741 | 14 of 14 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005741 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005741 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005741 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005741 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005741 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact structure and hierarchy

identity: supported. Targets: GO:0005741.

Exact native identity, synonyms where present, is_a hierarchy and membrane/lumen topology agree with the target. Containing mitochondrial compartments are distinguished from more specific constituent structures.

### Eukaryotic diversity and yeast example

scope: supported. Targets: GO:0005741.

The yeast example is supported by the actual purified-organelle study, with YPH499 growth and purification scope retained. Broad mitochondrial diversity is supported by GO mitochondrial context and the independently inspected Roger review. The target does not assert that all eukaryotes have identical mitochondrial architecture.

### Bilayer material and TOM localization

grounding: supported. Targets: GO:0005741.

The label-only LIPID row represents generic membrane material without grounding it to the entire membrane. TOM is supported as resident machinery and source-specific entry gate. Neither omission of a full TOM subunit inventory nor the representative Tom40 xref establishes a concrete defect.

### Defining membrane material

grounding: unknown. Targets: GO:0005741.

The lipid material is constitutional to the defined bilayer. The cited ontology and scoped papers do not experimentally test formation in its absence or establish universal necessity of a fixed lipid composition.

### Outer entry versus complete matrix import

scope: supported. Targets: GO:0005741.

The function description correctly limits the outer membrane contribution to precursor entry. Complete matrix translocation additionally requires inner-membrane and matrix machinery; that distinction is explicit in the source and target.

### Five descriptive edges and protein actor

graph: supported. Targets: GO:0005741.

Envelope parthood, cytoplasmic orientation, intermembrane-space boundary, TOM placement and the entry step all have narrow support. The graph remains NONMECHANISTIC and does not claim an untested complete pathway.

### Entire maintained record

completeness: supported. Targets: GO:0005741.

All target fields, causal graph edges, evidence placement, discussions and history were inspected. There are no record image assets, numerical properties or verbatim snippets. Optional inventory slots and acknowledged molecular-grounding unknowns do not become automatic findings.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml; Entire maintained target, all graph edges, evidence, discussions and history | context_only | The full target was read; scientific bytes and native status are unchanged. |
| policy | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, EssentialityEnum and causal node semantics | context_only | Collective membrane material is distinct from a complete protein-bearing membrane; constitutional composition does not by itself establish an experimental formation requirement. |
| root33-sources-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005759,GO:0070013,GO:0005739,GO:0005743,GO:0031966,GO:0016020,GO:0005740,GO:0005741,GO:0005758,GO:0031968,GO:0005742,GO:0005737,GO:0030150; Complete returned IDs, names, definitions, comments, synonyms and typed children | supports | All thirteen requested native GO terms are active, with exact definitions, synonym scopes and typed child relations inspected. Matrix is a mitochondrial lumen; generic membrane includes inner and outer bilayers. Mitochondrion comment explicitly distinguishes reduced mitochondrion-related organelles. TOM supplies entry to mitochondrial compartments; matrix import specifically uses TOM-TIM23-PAM. |
| root33-sources-GO0005741-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005741/ancestors?relations=is_a; Complete returned ancestor list requested with relations=is_a | supports | Exact is_a-only ancestors confirm the declared broader class or classes without substituting parthood for identity. |
| root33-sources-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; Complete taxId/scientificName/rank/lineage/otherNames | supports | Exact scientific name, rank and lineage verified. Taxonomy identity does not establish frequency or experimental genotype. |
| root33-sources-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId/scientificName/rank/lineage/otherNames | supports | Exact scientific name, rank and lineage verified. Taxonomy identity does not establish frequency or experimental genotype. |
| root33-sources-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId/scientificName/rank/lineage/otherNames | supports | Exact scientific name, rank and lineage verified. Taxonomy identity does not establish frequency or experimental genotype. |
| root33-sources-sickmann2003-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.2135385100&amp;format=json&amp;resultType=core; Exact MED identity and complete abstractText | supports | Exact native title, authors, DOI 10.1073/pnas.2135385100, PMID 14576278 and complete abstract inspected. Bibliography/abstract are distinct from the separately scoped body reading. |
| root33-sources-roger2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1016/j.cub.2017.09.015%22; Exact MED identity and complete abstractText | supports | Exact native title, authors, DOI 10.1016/j.cub.2017.09.015, PMID 29112874 and complete abstract inspected. Bibliography/abstract are distinct from the separately scoped body reading. |
| root33-sources-friedman2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature12985&amp;format=json&amp;resultType=core; Exact MED identity and complete abstractText | supports | Exact native title, authors, DOI 10.1038/nature12985, PMID 24429632 and complete abstract inspected. Bibliography/abstract are distinct from the separately scoped body reading. |
| root33-sources-chacinska2009-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016/j.cell.2009.08.005&amp;format=json&amp;resultType=core; Exact MED identity and complete abstractText | supports | Exact native title, authors, DOI 10.1016/j.cell.2009.08.005, PMID 19703392 and complete abstract inspected. Bibliography/abstract are distinct from the separately scoped body reading. |
| root33-sources-sickmann2003-pmc-exact | https://pmc.ncbi.nlm.nih.gov/articles/PMC263752/; Complete Materials and Methods sec1 and Results/Discussion sec2 with all embedded main figure captions; supplementary Tables1/2, raw spectra and figure pixels not inspected | supports | Genuine PMC263752 primary article. YPH499 yeast grown on glycerol was the main experimental strain; purification, MS and selected import assays recover matrix and membrane-associated machinery. The paper explicitly discusses contamination, dual localization and mistargeting by tags, and does not make bulk proteomics proof of every protein subcompartment or universal inventory. |
| root33-sources-roger2017-pdf | https://ecsolab.com/assets/pdf/roger_etal_2017.pdf; PDF first-page title/DOI/abstract; selected body paragraphs on printed R1184 and R1186: opening anaerobic-diversity paragraph, hydrogenosome/mitosome comparison and concluding reduction paragraph. Other body paragraphs, figure pixels and source experiments not independently certified read | supports | The exact review PDF supports multiple reduced mitochondrial forms in anaerobic lineages, including mitosomes and hydrogenosomes, and a functional continuum. This is secondary synthesis supporting broad diversity, not a new prevalence survey or proof that reduced organelles lack membranes. |
| root33-sources-friedman2014-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4075653.1/PMC4075653.1.xml; Complete body S5, Internal determinants of mitochondrial division; complete native abstract separately | supports | Review section describes distinct inner-boundary and crista regions, narrow connecting junctions, MICOS scaffold and ATP-synthase-stabilized ridges. Secondary synthesis is not treated as a new perturbation assay. |
| root33-sources-P23644 | https://rest.uniprot.org/uniprotkb/P23644.json; Exact primaryAccession, entryType, proteinDescription, genes, organism and complete comments | supports | Reviewed S288C TOM40 identity, gene aliases and native function/subunit/location comments verify one channel-forming member of TOM. The complex label and exact GO grounding preserve the whole actor identity; this member xref does not assert equality between the complete complex and one protein. |
| root33-sources-chacinska2009-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4099469.1/PMC4099469.1.xml; Complete body S1, S2, S7, S8 and S10. No figures, tables, other sections or cited primary experiments independently inspected | supports | Review describes TOM as the outer entry gate and Tom40 as its channel-forming member, followed by TIM23 and the matrix-exposed PAM motor for presequence matrix import. Proposed routes and dynamic-coupling models remain review synthesis; the target only asserts the bounded entry step. |
| native-verify | /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml --verify; Entire retained native focused log; successful network retry identified where applicable | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml --causal-graphs; Entire retained native focused log; successful network retry identified where applicable | supports | data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml  (GO:0005741)<br>  mitochondrial_outer_membrane_topology	tom_complex	UNANCHORED_WITH_UNIPROT	mitochondrial outer membrane translocase complex (UniProtKB:P23644)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     1  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     1  total GENE_OR_PROTEIN causal nodes |
| schema-result | just validate data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_outer_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_outer_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_outer_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 14 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- All occurrence labels are qualitative, not measured species-wide frequencies. No original source figure pixels, supplementary tables, raw spectra or primary data were inspected.
- Sickmann scope is the complete Methods and Results/Discussion with main captions, not its separate supplementary protein tables. Roger scope is the exact selected printed-page paragraphs stated in evidence; the remainder is not certified read.
- Historical authorship and issue dispositions were not independently recertified. This review does not promote status, change scientific records or regenerate pages.
- Friedman2014 scope is S5; Chacinska2009 scope is S1/S2/S7/S8/S10. These are secondary reviews, not newly inspected primary mechanism experiments.
- The initial optional UniProt verify attempt failed because sandbox DNS was unavailable. Its original failure log is retained; the same focused command succeeded with network access, and a separate native accession inspection agrees.
- GO0005741 alone does not establish taxonomic prevalence or all reduced-organelle diversity; the independent Roger review provides bounded biological context. No exact lipid-species grounding or universal formation requirement was established.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- The user explicitly authorizes one bundle for every uncovered record, including honest zero-finding reviews.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T023315Z-mitochondrial-outer-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Mitochondrial outer membrane identity and source review
started_at: '2026-10-22T02:18:45Z'
finished_at: '2026-10-22T02:33:15Z'
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
summary: No concrete curation defect observed within the explicitly bounded scientific
  evidence scope.
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
  - path: data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
    sha256: c65c2f350a175ad96c5b5fbb0128fef48a17ece11571fde4bbe898644599d78a
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
  - path: scripts/uniprot_genes.py
    sha256: feb9042b212bc639bc2603c186c6e328fa142c2641e93fc1418ad5a14e1d5faf
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
targets:
- target_id: GO:0005741
  path: data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
  label: mitochondrial outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
    role: maintained scientific record
scope:
  description: 'Entire single target: identity, hierarchy, composition where present,
    taxonomy, canonical example, functions and every graph edge.'
  selection: Target 7 of batch33 in strict uncovered path order from fresh origin/main
    f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005741
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0005741
  command: /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
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
  - GO:0005741
  command: /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
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
  - GO:0005741
  command: just validate data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005741
  command: just validate-strict data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_outer_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005741
  summary: No expression-module or regulatory-module claim is assessed; direct structure
    and import/proteomics evidence is used.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005741
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - policy
  - root33-sources-go
  - root33-sources-GO0005741-isa
  - root33-sources-tax2759
  - root33-sources-tax4932
  - root33-sources-tax559292
  - root33-sources-sickmann2003-meta
  - root33-sources-roger2017-meta
  - root33-sources-friedman2014-meta
  - root33-sources-chacinska2009-meta
  - root33-sources-sickmann2003-pmc-exact
  - root33-sources-roger2017-pdf
  - root33-sources-friedman2014-jats
  - root33-sources-P23644
  - root33-sources-chacinska2009-jats
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005741
  summary: 14 of 14 collected target identifiers returned OK. No residuals. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.
  evidence_ids:
  - target-curies
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0005741
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
  - GO:0005741
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
  - GO:0005741
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
  - GO:0005741
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
  - GO:0005741
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
  reference: data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
  locator: Entire maintained target, all graph edges, evidence, discussions and history
  accessed_at: '2026-10-22T02:23:46Z'
  support: context_only
  summary: The full target was read; scientific bytes and native status are unchanged.
- evidence_id: policy
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, EssentialityEnum and causal node semantics
  accessed_at: '2026-10-22T02:23:46Z'
  support: context_only
  summary: Collective membrane material is distinct from a complete protein-bearing
    membrane; constitutional composition does not by itself establish an experimental
    formation requirement.
- evidence_id: root33-sources-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005759,GO:0070013,GO:0005739,GO:0005743,GO:0031966,GO:0016020,GO:0005740,GO:0005741,GO:0005758,GO:0031968,GO:0005742,GO:0005737,GO:0030150
  locator: Complete returned IDs, names, definitions, comments, synonyms and typed
    children
  accessed_at: '2026-10-22T02:20:18.426796Z'
  support: supports
  summary: All thirteen requested native GO terms are active, with exact definitions,
    synonym scopes and typed child relations inspected. Matrix is a mitochondrial
    lumen; generic membrane includes inner and outer bilayers. Mitochondrion comment
    explicitly distinguishes reduced mitochondrion-related organelles. TOM supplies
    entry to mitochondrial compartments; matrix import specifically uses TOM-TIM23-PAM.
  snapshot_sha256: 231b4fe3bef31955a7fe0031fd8bea5ae33e2f644da9d41ab7b72c7c6ae426d0
- evidence_id: root33-sources-GO0005741-isa
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0005741/ancestors?relations=is_a
  locator: Complete returned ancestor list requested with relations=is_a
  accessed_at: '2026-10-22T02:20:18.427457Z'
  support: supports
  summary: Exact is_a-only ancestors confirm the declared broader class or classes
    without substituting parthood for identity.
  snapshot_sha256: 21010d1c860309497db26fb3a893cfc11dbea0b8c82109cb9919a54e863ed7eb
- evidence_id: root33-sources-tax2759
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: Complete taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-22T02:20:18.427689Z'
  support: supports
  summary: Exact scientific name, rank and lineage verified. Taxonomy identity does
    not establish frequency or experimental genotype.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: root33-sources-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-22T02:20:19.306481Z'
  support: supports
  summary: Exact scientific name, rank and lineage verified. Taxonomy identity does
    not establish frequency or experimental genotype.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: root33-sources-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId/scientificName/rank/lineage/otherNames
  accessed_at: '2026-10-22T02:20:19.310633Z'
  support: supports
  summary: Exact scientific name, rank and lineage verified. Taxonomy identity does
    not establish frequency or experimental genotype.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: root33-sources-sickmann2003-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.2135385100&format=json&resultType=core
  locator: Exact MED identity and complete abstractText
  accessed_at: '2026-10-22T02:20:26.034608Z'
  support: supports
  summary: Exact native title, authors, DOI 10.1073/pnas.2135385100, PMID 14576278
    and complete abstract inspected. Bibliography/abstract are distinct from the separately
    scoped body reading.
  snapshot_sha256: c5b3c15ca5f8b0e8cc638d016ec8f1a40c9392ddd1dda9230aa352066e331080
- evidence_id: root33-sources-roger2017-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1016/j.cub.2017.09.015%22
  locator: Exact MED identity and complete abstractText
  accessed_at: '2026-10-22T02:20:19.311159Z'
  support: supports
  summary: Exact native title, authors, DOI 10.1016/j.cub.2017.09.015, PMID 29112874
    and complete abstract inspected. Bibliography/abstract are distinct from the separately
    scoped body reading.
  snapshot_sha256: 79f51ae3193414033e9a85ac0cf692509624280a75f6e63345c2edf5389fef45
- evidence_id: root33-sources-friedman2014-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature12985&format=json&resultType=core
  locator: Exact MED identity and complete abstractText
  accessed_at: '2026-10-22T02:10:24.454595Z'
  support: supports
  summary: Exact native title, authors, DOI 10.1038/nature12985, PMID 24429632 and
    complete abstract inspected. Bibliography/abstract are distinct from the separately
    scoped body reading.
  snapshot_sha256: 390af3048cd69551f299e85c996efeab680b69e214c78b6d5d02bb24c0945d0a
- evidence_id: root33-sources-chacinska2009-meta
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1016/j.cell.2009.08.005&format=json&resultType=core
  locator: Exact MED identity and complete abstractText
  accessed_at: '2026-10-22T02:20:26.034500Z'
  support: supports
  summary: Exact native title, authors, DOI 10.1016/j.cell.2009.08.005, PMID 19703392
    and complete abstract inspected. Bibliography/abstract are distinct from the separately
    scoped body reading.
  snapshot_sha256: 7aa046f6810f431b585710c8f5a4867791023f1491928649449817119e305f59
- evidence_id: root33-sources-sickmann2003-pmc-exact
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC263752/
  locator: Complete Materials and Methods sec1 and Results/Discussion sec2 with all
    embedded main figure captions; supplementary Tables1/2, raw spectra and figure
    pixels not inspected
  accessed_at: '2026-10-22T02:21:23.144846Z'
  support: supports
  summary: Genuine PMC263752 primary article. YPH499 yeast grown on glycerol was the
    main experimental strain; purification, MS and selected import assays recover
    matrix and membrane-associated machinery. The paper explicitly discusses contamination,
    dual localization and mistargeting by tags, and does not make bulk proteomics
    proof of every protein subcompartment or universal inventory.
  snapshot_sha256: dbb60e1208e1203366064cd5220edfc437a809737bc245d1bb927b3c1c626fde
- evidence_id: root33-sources-roger2017-pdf
  kind: authority
  reference: https://ecsolab.com/assets/pdf/roger_etal_2017.pdf
  locator: 'PDF first-page title/DOI/abstract; selected body paragraphs on printed
    R1184 and R1186: opening anaerobic-diversity paragraph, hydrogenosome/mitosome
    comparison and concluding reduction paragraph. Other body paragraphs, figure pixels
    and source experiments not independently certified read'
  accessed_at: '2026-10-22T02:21:01.426006Z'
  support: supports
  summary: The exact review PDF supports multiple reduced mitochondrial forms in anaerobic
    lineages, including mitosomes and hydrogenosomes, and a functional continuum.
    This is secondary synthesis supporting broad diversity, not a new prevalence survey
    or proof that reduced organelles lack membranes.
  snapshot_sha256: b0ddb1d89fda3d1e929ef0d65c68b15864c0e602a5736305abbb08673010982e
- evidence_id: root33-sources-friedman2014-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4075653.1/PMC4075653.1.xml
  locator: Complete body S5, Internal determinants of mitochondrial division; complete
    native abstract separately
  accessed_at: '2026-10-22T02:10:55.342035Z'
  support: supports
  summary: Review section describes distinct inner-boundary and crista regions, narrow
    connecting junctions, MICOS scaffold and ATP-synthase-stabilized ridges. Secondary
    synthesis is not treated as a new perturbation assay.
  snapshot_sha256: 37cb298ab74e8ff5524164dcfa6563f44b3fc8f0833ce2049dad7d11f8e6ae97
- evidence_id: root33-sources-P23644
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P23644.json
  locator: Exact primaryAccession, entryType, proteinDescription, genes, organism
    and complete comments
  accessed_at: '2026-10-22T02:20:19.348727Z'
  support: supports
  summary: Reviewed S288C TOM40 identity, gene aliases and native function/subunit/location
    comments verify one channel-forming member of TOM. The complex label and exact
    GO grounding preserve the whole actor identity; this member xref does not assert
    equality between the complete complex and one protein.
  snapshot_sha256: 013d19f1318cc3529d32dd5ce2e6261a5d26a43ec41ae23c178d0f6bd25d042f
- evidence_id: root33-sources-chacinska2009-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4099469.1/PMC4099469.1.xml
  locator: Complete body S1, S2, S7, S8 and S10. No figures, tables, other sections
    or cited primary experiments independently inspected
  accessed_at: '2026-10-22T02:21:09.775994Z'
  support: supports
  summary: Review describes TOM as the outer entry gate and Tom40 as its channel-forming
    member, followed by TIM23 and the matrix-exposed PAM motor for presequence matrix
    import. Proposed routes and dynamic-coupling models remain review synthesis; the
    target only asserts the bounded entry step.
  snapshot_sha256: 010e4b847c377e924ee1635a33ce3479a86b63183d5e5b4524a6904ff555ceba
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
    --verify
  locator: Entire retained native focused log; successful network retry identified
    where applicable
  accessed_at: '2026-10-22T02:21:22.063138Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/.venv/bin/python
    scripts/uniprot_genes.py --record data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
    --causal-graphs
  locator: Entire retained native focused log; successful network retry identified
    where applicable
  accessed_at: '2026-10-22T02:21:22.595342Z'
  support: supports
  summary: "data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml \
    \ (GO:0005741)\n  mitochondrial_outer_membrane_topology\ttom_complex\tUNANCHORED_WITH_UNIPROT\t\
    mitochondrial outer membrane translocase complex (UniProtKB:P23644)\n\ncausal_graphs\
    \ GENE_OR_PROTEIN node summary:\n     1  UNANCHORED_WITH_UNIPROT   no component_ref,\
    \ but node carries a UniProtKB grounding or xref\n     0  COVERED            \
    \       component_ref target holds protein_examples covering all declared symbols\n\
    \     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples\
    \ but has unrepresented symbols\n     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref\
    \ target declares gene_symbols but holds no protein_examples\n     0  NO_GENE_SYMBOLS\
    \           component_ref target declares no gene_symbols and holds no protein_examples\n\
    \     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does\
    \ not exist on the record\n     0  UNANCHORED_NO_UNIPROT     no component_ref\
    \ and no UniProtKB grounding or xref on the node\n     1  total GENE_OR_PROTEIN\
    \ causal nodes"
  snapshot_sha256: e624be73d7b2befb64d4aa4a5ade017e51cd70e949c26864159058531e0cb9ba
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:18:47Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml'
  snapshot_sha256: a7862597bfd77ce23d603cb94c3fe25bdf397178806ac4accaa2d54a2eec93dd
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_outer_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:18:48Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_outer_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch33-20261022-ohvln5r9/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch33-20261022-ohvln5r9/mitochondrial_outer_membrane-strict.tsv"
  snapshot_sha256: 7e6bd18916e784ee11d6f10966d510e26454db7b0db9ac6bb37b357d32cf4bd7
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/mitochondrial_outer_membrane.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: 14 of 14 collected target identifiers returned OK. No residuals. Native
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
  topic: Exact structure and hierarchy
  outcome: supported
  target_ids:
  - GO:0005741
  summary: Exact native identity, synonyms where present, is_a hierarchy and membrane/lumen
    topology agree with the target. Containing mitochondrial compartments are distinguished
    from more specific constituent structures.
  evidence_ids:
  - record
  - root33-sources-go
  - root33-sources-GO0005741-isa
  - root33-sources-sickmann2003-pmc-exact
- assessment_id: scope
  area: scope
  topic: Eukaryotic diversity and yeast example
  outcome: supported
  target_ids:
  - GO:0005741
  summary: The yeast example is supported by the actual purified-organelle study,
    with YPH499 growth and purification scope retained. Broad mitochondrial diversity
    is supported by GO mitochondrial context and the independently inspected Roger
    review. The target does not assert that all eukaryotes have identical mitochondrial
    architecture.
  evidence_ids:
  - record
  - root33-sources-go
  - root33-sources-tax2759
  - root33-sources-tax4932
  - root33-sources-tax559292
  - root33-sources-sickmann2003-pmc-exact
  - root33-sources-roger2017-pdf
- assessment_id: material
  area: grounding
  topic: Bilayer material and TOM localization
  outcome: supported
  target_ids:
  - GO:0005741
  summary: The label-only LIPID row represents generic membrane material without grounding
    it to the entire membrane. TOM is supported as resident machinery and source-specific
    entry gate. Neither omission of a full TOM subunit inventory nor the representative
    Tom40 xref establishes a concrete defect.
  evidence_ids:
  - record
  - policy
  - root33-sources-go
  - root33-sources-P23644
  - root33-sources-chacinska2009-jats
- assessment_id: formation-necessity
  area: grounding
  topic: Defining membrane material
  outcome: unknown
  target_ids:
  - GO:0005741
  summary: The lipid material is constitutional to the defined bilayer. The cited
    ontology and scoped papers do not experimentally test formation in its absence
    or establish universal necessity of a fixed lipid composition.
  evidence_ids:
  - record
  - policy
  - root33-sources-go
  - root33-sources-sickmann2003-pmc-exact
- assessment_id: function
  area: scope
  topic: Outer entry versus complete matrix import
  outcome: supported
  target_ids:
  - GO:0005741
  summary: The function description correctly limits the outer membrane contribution
    to precursor entry. Complete matrix translocation additionally requires inner-membrane
    and matrix machinery; that distinction is explicit in the source and target.
  evidence_ids:
  - record
  - root33-sources-go
  - root33-sources-chacinska2009-jats
- assessment_id: graph
  area: graph
  topic: Five descriptive edges and protein actor
  outcome: supported
  target_ids:
  - GO:0005741
  summary: Envelope parthood, cytoplasmic orientation, intermembrane-space boundary,
    TOM placement and the entry step all have narrow support. The graph remains NONMECHANISTIC
    and does not claim an untested complete pathway.
  evidence_ids:
  - record
  - root33-sources-go
  - root33-sources-chacinska2009-jats
  - root33-sources-P23644
  - root33-sources-friedman2014-jats
- assessment_id: coverage
  area: completeness
  topic: Entire maintained record
  outcome: supported
  target_ids:
  - GO:0005741
  summary: All target fields, causal graph edges, evidence placement, discussions
    and history were inspected. There are no record image assets, numerical properties
    or verbatim snippets. Optional inventory slots and acknowledged molecular-grounding
    unknowns do not become automatic findings.
  evidence_ids:
  - record
  - policy
  - root33-sources-go
  - root33-sources-sickmann2003-pmc-exact
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- All occurrence labels are qualitative, not measured species-wide frequencies. No
  original source figure pixels, supplementary tables, raw spectra or primary data
  were inspected.
- Sickmann scope is the complete Methods and Results/Discussion with main captions,
  not its separate supplementary protein tables. Roger scope is the exact selected
  printed-page paragraphs stated in evidence; the remainder is not certified read.
- Historical authorship and issue dispositions were not independently recertified.
  This review does not promote status, change scientific records or regenerate pages.
- Friedman2014 scope is S5; Chacinska2009 scope is S1/S2/S7/S8/S10. These are secondary
  reviews, not newly inspected primary mechanism experiments.
- The initial optional UniProt verify attempt failed because sandbox DNS was unavailable.
  Its original failure log is retained; the same focused command succeeded with network
  access, and a separate native accession inspection agrees.
- GO0005741 alone does not establish taxonomic prevalence or all reduced-organelle
  diversity; the independent Roger review provides bounded biological context. No
  exact lipid-species grounding or universal formation requirement was established.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- The user explicitly authorizes one bundle for every uncovered record, including
  honest zero-finding reviews.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
