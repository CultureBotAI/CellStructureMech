# Source-backed review of dinoflagellate apical groove

- Review: 20261022T054302Z-dinoflagellate-apical-groove-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T05:30:52Z
- Finished UTC: 2026-10-22T05:43:02Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Qualified pass: apical-groove identity, direct structural topology and the Margalefidinium polykrikoides example are supported, with microscopy-abstract and taxonomic-transfer evidence kept distinct.

## Scope And Provenance

Exactly one entire target. All current definition, hierarchy/parthood, taxonomy, topology, evidence and discussion claims were assessed; neighboring identities are checked through native source relationships without importing a neighboring verdict.

Selection: Batch50 fixed strict path order, index 1; exactly one maintained target.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097685 | data/structures/other/dinoflagellate_apical_groove.yaml | maintained | dinoflagellate apical groove |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0097685 | Focused validator passed. |
| Focused native strict | passed | True | GO:0097685 | Focused validator passed. |
| Focused native graph check | passed | True | GO:0097685 | No GENE_OR_PROTEIN nodes are present. Structure-node identities and topology were checked against native GO separately. |
| Claim-level scientific review | passed | True | GO:0097685 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0097685 | 7 of 8 collected target identifiers returned OK. PMID:20561119: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0097685 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0097685 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0097685 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0097685 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0097685 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact apical-furrow class and current species name

identity: supported. Targets: GO:0097685.

The groove is a surface furrow on the apex within the epicone, distinct from either whole region or its flagellar apparatus. The2010 morphological observation and2017 nomenclatural change support different claims; native77300 bridges the old and current species labels.

### Class variability and species morphology

scope: supported. Targets: GO:0097685.

VARIABLE at Dinophyceae does not claim a groove in every dinoflagellate. COMMON at the named species is supported as an ordinary diagnostic morphology by the direct2010 abstract and formal2017 genus diagnosis, not a numerical prevalence census. The canonical example is the species studied, without inventing an experimental strain.

### Two directly typed structural relations

graph: supported. Targets: GO:0097685.

Both is-a surface-furrow and part-of epicone are explicitly present in the native ontology. The morphology citation supports the dorsal epicone location; the NONMECHANISTIC graph does not assert a molecular assembly order or physiological role.

### Separate microscopy support from taxonomic transfer

evidence: supported. Targets: GO:0097685.

The canonical example and morphology row cite Iwataki2010, while Gomez2017 supports record-level nomenclature. The latter paper has a formal U-shaped diagnosis despite not seeing that feature in its own obstructed specimens; the review preserves this observational limit.

### No unsupported molecular constituents

grounding: supported. Targets: GO:0097685.

No protein components or examples are asserted. The open discussion requests region-specific localization and exact family evidence. Generic whole-cell cellulose, membranes and proteins cannot populate these regional inventories without direct support.

### Molecular formation necessity remains unknown

grounding: unknown. Targets: GO:0097685.

Morphological location, taxon identity and structural classification do not establish molecular assembly requirements. There are no component essentiality values to reinterpret and no growth or localization phenotype is promoted to a formation requirement.

### All current fields reviewed without compulsory enrichment

completeness: supported. Targets: GO:0097685.

Definition, hierarchy, source notes, distributions, graphs, discussions and history were read. Historical metadata limits remain explicit; optional protein inventories, dimensions, images, canonical species or mechanistic functions are not required solely to fill empty fields.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/other/dinoflagellate_apical_groove.yaml; Entire maintained YAML, including all topology edges, source notes, discussions and historical entries | context_only | The complete target was read; a cited authority is checked for biological consistency as well as verbatim identity. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; CellStructureRecord definition/definition_source; StructuralComponent; EssentialityEnum; taxonomic presence and graph scopes | context_only | A region is distinguished from an assembled molecular complex. Formation necessity is distinct from presence or function; no molecular requirement is inferred for an unspecified inventory. |
| curation | docs/CURATION.md; Exact identity and grounding, scope and evidence placement | context_only | Exact identifiers do not by themselves validate contradictory biological prose. Optional components are not filled with generic regional or whole-cell materials without specific support. |
| graph-rubric | .claude/skills/curate-causal-graphs/SKILL.md; Nonmechanistic structure topology and explicit edge-level evidence | context_only | Descriptive is-a, parthood and spatial relations can remain NONMECHANISTIC; they do not demonstrate formation or physiological causation. |
| root50-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685,GO:0097686,GO:0097611,GO:0097613,GO:0097683,GO:0097614,GO:0097610,GO:0110165; Eight native identities: complete definitions, status, synonyms/comments and relevant typed links; only relevant GO0110165 child links were scientifically assessed. | supports | Active GO0097685 identifies the apical furrow and broad synonym. Cell-surface furrow GO0097610 exposes its is-a child, and epicone GO0097613 exposes the groove as a part_of child. The typically looping definition does not require every species to have a closed circular groove. |
| root50-GO0097685-history | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685/history; Complete native history response. | supports | Dated native term/definition/relation/synonym entries agree with the maintained identity and typed relations. The history display has an uninformative taxon rendering; actual taxon constraints are checked separately. |
| root50-GO0097685-constraints | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685/constraints; Complete focal taxonConstraints array; identity fields also inspected. | supports | Native only_in_taxon constraint explicitly identifies NCBITaxon2864 Dinophyceae for this focal structure. This restricts the valid lineage without asserting occurrence in every member. |
| root50-tax2864 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864; Complete native ENA taxon name/rank/lineage/synonym fields; original receipt reused. | supports | Native class2864 is Dinophyceae with recognized dinoflagellate and Dinophyta/Dinoflagellata aliases. The identity authority does not supply a prevalence census. |
| root50-tol-orientation | https://tolweb.org/articles/?article_id=4756; Complete main orientation note and overview caption, authorship and licence; no image pixels; original receipt reused. | supports | Hoppenrath2008 defines the anterior episome and posterior hyposome relative to the cingulum, with naked/thecate terminology distinguished. Apex is at the anterior tip; apical grooves are possible features rather than a universal regional molecular inventory. |
| root50-iwataki2010-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1550-7408.2010.00491.x%22&amp;format=json&amp;resultType=core; Complete native authors/title/year/PMID/DOI and abstract; no full main body. | supports | Unique MED20561119 and DOI10.1111/j.1550-7408.2010.00491.x identify Iwataki et al.2010. The complete abstract directly describes the U-shaped groove connected to the anterior sulcal extension on the dorsal epicone of C.polykrikoides. Other flagellar/eyespot results are not recast as groove constituents. |
| root50-gomez2017-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.hal.2017.01.008%22&amp;format=json&amp;resultType=core; Complete native authors/title/year/PMID/DOI and abstract. | supports | Unique MED28366398 and DOI10.1016/j.hal.2017.01.008 identify Gomez, Richlen and Anderson2017. The complete abstract proposes Margalefidinium and the polykrikoides combination, separating it from C.strangulatum. |
| root50-gomez2017-legacy | https://pmc.ncbi.nlm.nih.gov/articles/PMC6276129/?report=xml; Complete Methods S3, Results S8 including nested molecular phylogeny S9 and Fig3/4 captions, S10 including Table1/all taxonomic subsections/Fig5 caption, and Conclusions S30; no pixels or supplements. | supports | The formal diagnosis and new combination establish Margalefidinium polykrikoides from Cochlodinium polykrikoides. Diagnosis/Table1 retain a U-shaped dorsal episomal groove. The authors could not resolve that groove in their own Puerto Rico light microscopy, and filamentous surface material obstructed detailed SEM; this source is not substituted for the2010 ultrastructural observation. |
| root50-tax77300 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/77300; Complete native taxon response. | supports | Native species77300 is Margalefidinium polykrikoides and explicitly lists Cochlodinium polykrikoides as a synonym, corroborating the current-name bridge. |
| root50-iwataki2010-publisher | https://onlinelibrary.wiley.com/doi/full/10.1111/j.1550-7408.2010.00491.x; Actual status/body readability limitation. | context_only | The Wiley full-article route returned403. The complete native abstract remains readable, but primary main-body methods and microscopy images were not inspected. |
| schema-result | just validate data/structures/other/dinoflagellate_apical_groove.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/other/dinoflagellate_apical_groove.yaml |
| strict-result | just validate-strict data/structures/other/dinoflagellate_apical_groove.yaml --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_apical_groove-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/other/dinoflagellate_apical_groove.yaml --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_apical_groove-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_apical_groove-strict.tsv |
| native-graphs | /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dinoflagellate_apical_groove.yaml; Complete focused read-only causal graph report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/other/dinoflagellate_apical_groove.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 7 of 8 collected target identifiers returned OK. PMID:20561119: UNREACHABLE; Exact native Europe PMC MED identifier, title and DOI were inspected after the bulk eutils414 transport failure. Identity resolution does not certify every attached biological claim; declared abstract/body reading scope remains in force. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- No figure pixels, microscopy datasets or supplemental videos were reanalyzed. Native GO, expert terminology, bibliographic metadata and inspected primary prose retain distinct evidence tiers.
- These are morphological regions, not molecular-complex inventories. No directly localized protein families, assembly-necessity assays or quantitative taxon-wide census were established.
- Iwataki2010 was read only at complete native metadata/abstract tier; the attempted publisher full-text route failed403. Gomez2017 body scope is explicitly listed and its own microscopy did not resolve the groove.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User expressly requests one review for every unreviewed record, including scientifically clean records.
- No protein examples or molecular graph actors occur in this target; protein-accession enrichment and iModulonDB do not apply to the present morphological topology claims.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T054302Z-dinoflagellate-apical-groove-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of dinoflagellate apical groove
started_at: '2026-10-22T05:30:52Z'
finished_at: '2026-10-22T05:43:02Z'
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
summary: 'Qualified pass: apical-groove identity, direct structural topology and the
  Margalefidinium polykrikoides example are supported, with microscopy-abstract and
  taxonomic-transfer evidence kept distinct.'
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
  - path: data/structures/other/dinoflagellate_apical_groove.yaml
    sha256: 7577f4358ce9bcc9753ec38e0295a7e496261827869f77353480ef2b130ad1f4
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
- target_id: GO:0097685
  path: data/structures/other/dinoflagellate_apical_groove.yaml
  label: dinoflagellate apical groove
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/dinoflagellate_apical_groove.yaml
    role: maintained scientific record
scope:
  description: Exactly one entire target. All current definition, hierarchy/parthood,
    taxonomy, topology, evidence and discussion claims were assessed; neighboring
    identities are checked through native source relationships without importing a
    neighboring verdict.
  selection: Batch50 fixed strict path order, index 1; exactly one maintained target.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097685
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: just validate data/structures/other/dinoflagellate_apical_groove.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: just validate-strict data/structures/other/dinoflagellate_apical_groove.yaml
    --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_apical_groove-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: native-graphs
  name: Focused native graph check
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dinoflagellate_apical_groove.yaml
  exit_code: 0
  summary: No GENE_OR_PROTEIN nodes are present. Structure-node identities and topology
    were checked against native GO separately.
  evidence_ids:
  - native-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0097685
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - curation
  - graph-rubric
  - root50-go
  - root50-GO0097685-history
  - root50-GO0097685-constraints
  - root50-tax2864
  - root50-tol-orientation
  - root50-iwataki2010-meta
  - root50-gomez2017-meta
  - root50-gomez2017-legacy
  - root50-tax77300
  - root50-iwataki2010-publisher
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0097685
  summary: '7 of 8 collected target identifiers returned OK. PMID:20561119: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
  evidence_ids:
  - target-curies
  - root50-iwataki2010-meta
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0097685
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0097685
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
    and current batch50 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/other/dinoflagellate_apical_groove.yaml
  locator: Entire maintained YAML, including all topology edges, source notes, discussions
    and historical entries
  accessed_at: '2026-10-22T05:33:55Z'
  support: context_only
  summary: The complete target was read; a cited authority is checked for biological
    consistency as well as verbatim identity.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: CellStructureRecord definition/definition_source; StructuralComponent;
    EssentialityEnum; taxonomic presence and graph scopes
  accessed_at: '2026-10-22T05:33:55Z'
  support: context_only
  summary: A region is distinguished from an assembled molecular complex. Formation
    necessity is distinct from presence or function; no molecular requirement is inferred
    for an unspecified inventory.
- evidence_id: curation
  kind: record_content
  reference: docs/CURATION.md
  locator: Exact identity and grounding, scope and evidence placement
  accessed_at: '2026-10-22T05:33:55Z'
  support: context_only
  summary: Exact identifiers do not by themselves validate contradictory biological
    prose. Optional components are not filled with generic regional or whole-cell
    materials without specific support.
- evidence_id: graph-rubric
  kind: record_content
  reference: .claude/skills/curate-causal-graphs/SKILL.md
  locator: Nonmechanistic structure topology and explicit edge-level evidence
  accessed_at: '2026-10-22T05:33:55Z'
  support: context_only
  summary: Descriptive is-a, parthood and spatial relations can remain NONMECHANISTIC;
    they do not demonstrate formation or physiological causation.
- evidence_id: root50-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685,GO:0097686,GO:0097611,GO:0097613,GO:0097683,GO:0097614,GO:0097610,GO:0110165
  locator: 'Eight native identities: complete definitions, status, synonyms/comments
    and relevant typed links; only relevant GO0110165 child links were scientifically
    assessed.'
  accessed_at: '2026-10-22T05:31:10.469605Z'
  support: supports
  summary: Active GO0097685 identifies the apical furrow and broad synonym. Cell-surface
    furrow GO0097610 exposes its is-a child, and epicone GO0097613 exposes the groove
    as a part_of child. The typically looping definition does not require every species
    to have a closed circular groove.
  snapshot_sha256: 728d23e8f48df235e1d286d42796040aeef04f727c1da32f3bab38c5d3285935
- evidence_id: root50-GO0097685-history
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685/history
  locator: Complete native history response.
  accessed_at: '2026-10-22T05:31:10.470151Z'
  support: supports
  summary: Dated native term/definition/relation/synonym entries agree with the maintained
    identity and typed relations. The history display has an uninformative taxon rendering;
    actual taxon constraints are checked separately.
  snapshot_sha256: aec2f55dd69f3539e73da407ce409741edae2b3cbd7f23d7b61131e2e1c6e875
- evidence_id: root50-GO0097685-constraints
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097685/constraints
  locator: Complete focal taxonConstraints array; identity fields also inspected.
  accessed_at: '2026-10-22T05:31:10.470058Z'
  support: supports
  summary: Native only_in_taxon constraint explicitly identifies NCBITaxon2864 Dinophyceae
    for this focal structure. This restricts the valid lineage without asserting occurrence
    in every member.
  snapshot_sha256: dd75a85b0ec0d3a82a85d6b6a5e23171598de4ecbc57b9dd7fa33ce71034f599
- evidence_id: root50-tax2864
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2864
  locator: Complete native ENA taxon name/rank/lineage/synonym fields; original receipt
    reused.
  accessed_at: '2026-10-22T05:16:46.025548Z'
  support: supports
  summary: Native class2864 is Dinophyceae with recognized dinoflagellate and Dinophyta/Dinoflagellata
    aliases. The identity authority does not supply a prevalence census.
  snapshot_sha256: da7d6dfa6d6784e4eb22bc3f3e05878f3aae5a281a4996ee25a2012d580f27d4
- evidence_id: root50-tol-orientation
  kind: authority
  reference: https://tolweb.org/articles/?article_id=4756
  locator: Complete main orientation note and overview caption, authorship and licence;
    no image pixels; original receipt reused.
  accessed_at: '2026-10-22T05:18:11.990831Z'
  support: supports
  summary: Hoppenrath2008 defines the anterior episome and posterior hyposome relative
    to the cingulum, with naked/thecate terminology distinguished. Apex is at the
    anterior tip; apical grooves are possible features rather than a universal regional
    molecular inventory.
  snapshot_sha256: 406916e9c83d51de4ec6f7dee8a7b129c6ab8e1781a65a3ec28d83734970370e
- evidence_id: root50-iwataki2010-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1111%2Fj.1550-7408.2010.00491.x%22&format=json&resultType=core
  locator: Complete native authors/title/year/PMID/DOI and abstract; no full main
    body.
  accessed_at: '2026-10-22T05:31:11.844760Z'
  support: supports
  summary: Unique MED20561119 and DOI10.1111/j.1550-7408.2010.00491.x identify Iwataki
    et al.2010. The complete abstract directly describes the U-shaped groove connected
    to the anterior sulcal extension on the dorsal epicone of C.polykrikoides. Other
    flagellar/eyespot results are not recast as groove constituents.
  snapshot_sha256: b418641cc79a313c5ac6965bcea52577cf505f259730019886d6e0baa4dac239
- evidence_id: root50-gomez2017-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.hal.2017.01.008%22&format=json&resultType=core
  locator: Complete native authors/title/year/PMID/DOI and abstract.
  accessed_at: '2026-10-22T05:31:11.955045Z'
  support: supports
  summary: Unique MED28366398 and DOI10.1016/j.hal.2017.01.008 identify Gomez, Richlen
    and Anderson2017. The complete abstract proposes Margalefidinium and the polykrikoides
    combination, separating it from C.strangulatum.
  snapshot_sha256: 2d4226e2377a9d7c5a498a540cedcd4384508373ae32732e547441e96d4352f9
- evidence_id: root50-gomez2017-legacy
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC6276129/?report=xml
  locator: Complete Methods S3, Results S8 including nested molecular phylogeny S9
    and Fig3/4 captions, S10 including Table1/all taxonomic subsections/Fig5 caption,
    and Conclusions S30; no pixels or supplements.
  accessed_at: '2026-10-22T05:31:12.401930Z'
  support: supports
  summary: The formal diagnosis and new combination establish Margalefidinium polykrikoides
    from Cochlodinium polykrikoides. Diagnosis/Table1 retain a U-shaped dorsal episomal
    groove. The authors could not resolve that groove in their own Puerto Rico light
    microscopy, and filamentous surface material obstructed detailed SEM; this source
    is not substituted for the2010 ultrastructural observation.
  snapshot_sha256: 8505575a2f756e4a4e7df55fe70b22fdbdb2a8554ee47bcb9130ca097825c4d9
- evidence_id: root50-tax77300
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/77300
  locator: Complete native taxon response.
  accessed_at: '2026-10-22T05:31:10.469974Z'
  support: supports
  summary: Native species77300 is Margalefidinium polykrikoides and explicitly lists
    Cochlodinium polykrikoides as a synonym, corroborating the current-name bridge.
  snapshot_sha256: 396e3ce6c4259f21145716995c5bc20dc469cf291b5941c925c0a258ae50ed35
- evidence_id: root50-iwataki2010-publisher
  kind: database
  reference: https://onlinelibrary.wiley.com/doi/full/10.1111/j.1550-7408.2010.00491.x
  locator: Actual status/body readability limitation.
  accessed_at: '2026-10-22T05:31:12.422043Z'
  support: context_only
  summary: The Wiley full-article route returned403. The complete native abstract
    remains readable, but primary main-body methods and microscopy images were not
    inspected.
  snapshot_sha256: 792cc7833ab90870c2e3df1a8ab44e09ea0506fe4fe02c2542d238b991b4eda3
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/other/dinoflagellate_apical_groove.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:30:55Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/dinoflagellate_apical_groove.yaml'
  snapshot_sha256: 04327716a33d71a1ee36cfe6881ffa3ba9da901532496f862e54300b8d98ec29
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/other/dinoflagellate_apical_groove.yaml
    --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_apical_groove-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T05:30:57Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/other/dinoflagellate_apical_groove.yaml\
    \ --out /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_apical_groove-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/dinoflagellate_apical_groove-strict.tsv"
  snapshot_sha256: 6d7b73fa1944689960785d0d9165ae1336d54c8b6c1d29d7dff9d26f1a96dd55
- evidence_id: native-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch50-20261022-3ro2vlsx/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/other/dinoflagellate_apical_groove.yaml
  locator: Complete focused read-only causal graph report
  accessed_at: '2026-10-22T05:32:09.534082Z'
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
  locator: data/structures/other/dinoflagellate_apical_groove.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
  accessed_at: '2026-10-22T01:34:04Z'
  support: supports
  summary: '7 of 8 collected target identifiers returned OK. PMID:20561119: UNREACHABLE;
    Exact native Europe PMC MED identifier, title and DOI were inspected after the
    bulk eutils414 transport failure. Identity resolution does not certify every attached
    biological claim; declared abstract/body reading scope remains in force. Native
    source checks are separately scoped; skipped or unreachable identifiers are not
    silently counted as resolved.'
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
  topic: Exact apical-furrow class and current species name
  outcome: supported
  target_ids:
  - GO:0097685
  summary: The groove is a surface furrow on the apex within the epicone, distinct
    from either whole region or its flagellar apparatus. The2010 morphological observation
    and2017 nomenclatural change support different claims; native77300 bridges the
    old and current species labels.
  evidence_ids:
  - record
  - schema
  - root50-go
  - root50-GO0097685-history
  - root50-GO0097685-constraints
  - root50-tax2864
  - root50-tol-orientation
  - root50-iwataki2010-meta
  - root50-gomez2017-meta
  - root50-gomez2017-legacy
  - root50-tax77300
  - root50-iwataki2010-publisher
- assessment_id: taxonomic-scope
  area: scope
  topic: Class variability and species morphology
  outcome: supported
  target_ids:
  - GO:0097685
  summary: VARIABLE at Dinophyceae does not claim a groove in every dinoflagellate.
    COMMON at the named species is supported as an ordinary diagnostic morphology
    by the direct2010 abstract and formal2017 genus diagnosis, not a numerical prevalence
    census. The canonical example is the species studied, without inventing an experimental
    strain.
  evidence_ids:
  - record
  - schema
  - root50-go
  - root50-GO0097685-history
  - root50-GO0097685-constraints
  - root50-tax2864
  - root50-tol-orientation
  - root50-iwataki2010-meta
  - root50-gomez2017-meta
  - root50-gomez2017-legacy
  - root50-tax77300
  - root50-iwataki2010-publisher
- assessment_id: topology
  area: graph
  topic: Two directly typed structural relations
  outcome: supported
  target_ids:
  - GO:0097685
  summary: Both is-a surface-furrow and part-of epicone are explicitly present in
    the native ontology. The morphology citation supports the dorsal epicone location;
    the NONMECHANISTIC graph does not assert a molecular assembly order or physiological
    role.
  evidence_ids:
  - record
  - schema
  - root50-go
  - root50-GO0097685-history
  - root50-GO0097685-constraints
  - root50-tax2864
  - root50-tol-orientation
  - root50-iwataki2010-meta
  - root50-gomez2017-meta
  - root50-gomez2017-legacy
  - root50-tax77300
  - root50-iwataki2010-publisher
  - graph-rubric
- assessment_id: evidence-placement
  area: evidence
  topic: Separate microscopy support from taxonomic transfer
  outcome: supported
  target_ids:
  - GO:0097685
  summary: The canonical example and morphology row cite Iwataki2010, while Gomez2017
    supports record-level nomenclature. The latter paper has a formal U-shaped diagnosis
    despite not seeing that feature in its own obstructed specimens; the review preserves
    this observational limit.
  evidence_ids:
  - record
  - schema
  - root50-go
  - root50-GO0097685-history
  - root50-GO0097685-constraints
  - root50-tax2864
  - root50-tol-orientation
  - root50-iwataki2010-meta
  - root50-gomez2017-meta
  - root50-gomez2017-legacy
  - root50-tax77300
  - root50-iwataki2010-publisher
- assessment_id: composition
  area: grounding
  topic: No unsupported molecular constituents
  outcome: supported
  target_ids:
  - GO:0097685
  summary: No protein components or examples are asserted. The open discussion requests
    region-specific localization and exact family evidence. Generic whole-cell cellulose,
    membranes and proteins cannot populate these regional inventories without direct
    support.
  evidence_ids:
  - record
  - schema
  - root50-go
  - root50-GO0097685-history
  - root50-GO0097685-constraints
  - root50-tax2864
  - root50-tol-orientation
  - root50-iwataki2010-meta
  - root50-gomez2017-meta
  - root50-gomez2017-legacy
  - root50-tax77300
  - root50-iwataki2010-publisher
  - curation
- assessment_id: necessity
  area: grounding
  topic: Molecular formation necessity remains unknown
  outcome: unknown
  target_ids:
  - GO:0097685
  summary: Morphological location, taxon identity and structural classification do
    not establish molecular assembly requirements. There are no component essentiality
    values to reinterpret and no growth or localization phenotype is promoted to a
    formation requirement.
  evidence_ids:
  - record
  - schema
  - root50-go
  - root50-GO0097685-history
  - root50-GO0097685-constraints
  - root50-tax2864
  - root50-tol-orientation
  - root50-iwataki2010-meta
  - root50-gomez2017-meta
  - root50-gomez2017-legacy
  - root50-tax77300
  - root50-iwataki2010-publisher
- assessment_id: coverage
  area: completeness
  topic: All current fields reviewed without compulsory enrichment
  outcome: supported
  target_ids:
  - GO:0097685
  summary: Definition, hierarchy, source notes, distributions, graphs, discussions
    and history were read. Historical metadata limits remain explicit; optional protein
    inventories, dimensions, images, canonical species or mechanistic functions are
    not required solely to fill empty fields.
  evidence_ids:
  - record
  - schema
  - root50-go
  - root50-GO0097685-history
  - root50-GO0097685-constraints
  - root50-tax2864
  - root50-tol-orientation
  - root50-iwataki2010-meta
  - root50-gomez2017-meta
  - root50-gomez2017-legacy
  - root50-tax77300
  - root50-iwataki2010-publisher
  - curation
findings: []
actions: []
limitations:
- No figure pixels, microscopy datasets or supplemental videos were reanalyzed. Native
  GO, expert terminology, bibliographic metadata and inspected primary prose retain
  distinct evidence tiers.
- These are morphological regions, not molecular-complex inventories. No directly
  localized protein families, assembly-necessity assays or quantitative taxon-wide
  census were established.
- Iwataki2010 was read only at complete native metadata/abstract tier; the attempted
  publisher full-text route failed403. Gomez2017 body scope is explicitly listed and
  its own microscopy did not resolve the groove.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User expressly requests one review for every unreviewed record, including scientifically
  clean records.
- No protein examples or molecular graph actors occur in this target; protein-accession
  enrichment and iModulonDB do not apply to the present morphological topology claims.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
