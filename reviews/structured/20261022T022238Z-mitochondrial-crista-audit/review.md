# Scientific review of mitochondrial crista

- Review: 20261022T022238Z-mitochondrial-crista-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:03:13Z
- Finished UTC: 2026-10-22T02:22:38Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Crista identity, topology and yeast architectural roles are supported; no concrete issue observed. General lineage scope and universal formation necessity remain bounded unknowns.

## Scope And Provenance

One complete maintained record; exact native identities, source contexts, molecular/graph representation and limitations.

Selection: Batch32 fixed strict path-order selection, one target only.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030061 | data/structures/membrane_organelle/mitochondrial_crista.yaml | maintained | mitochondrial crista |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0030061 | Focused validator passed. |
| Focused native strict | passed | True | GO:0030061 | Focused validator passed. |
| Native focused causal | passed | True | GO:0030061 | Focused native command completed successfully; scientific scope is assessed separately. |
| Expression-module applicability | not_applicable | False | GO:0030061 | No expression-module or transcriptomic-regulon claim; structural microscopy and perturbations do not require an expression-module lookup. |
| Claim-level scientific review | passed | True | GO:0030061 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0030061 | 14 of 14 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0030061 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0030061 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0030061 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0030061 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0030061 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact compartment and topology

identity: supported. Targets: GO:0030061.

Definition and identifier agree with native GO. Crista-junction connection to the inner boundary membrane is direct definition support; crista has_part junction is anatomical interpretation, not claimed as a returned native crista-child edge. Junction contact-site is_a and inner-membrane part_of are verified.

### Taxonomy and experimental context

scope: supported. Targets: GO:0030061.

Taxon identities and the budding-yeast canonical model are supported. COMMON describes the ordinary crista-bearing yeast context; mutant/respiratory-state differences do not establish species absence or a prevalence percentage. Yeast strain-specific results are not generalized to identical architecture across all Eukaryota.

### Limits of general Eukaryota statement

scope: unknown. Targets: GO:0030061.

Native term response does not contain explicit taxon-constraint data. The specific reduced-anaerobic-organelle explanation in the whole crista record is not established by the selected Friedman2014 passage; no exhaustive lineage survey was done. This bounded uncertainty is not evidence that the biological statement is false.

### Complex membership and architecture machinery

grounding: supported. Targets: GO:0030061.

MICOS is correctly associated architecture machinery; resident F-type ATP synthase is a constituent. GO complex abstractions are valid and avoid claiming a fixed species-independent subunit inventory. The seven-edge NONMECHANISTIC graph preserves topology, maintenance, ridge shaping and respiratory support without inventing a complete assembly sequence.

### Formation necessity

grounding: unknown. Targets: GO:0030061.

Both complex rows deliberately use UNKNOWN. Localization, altered morphology and individual mutant phenotypes do not establish universal necessity of every complex/member for any inward membrane fold.

### Bounded whole-record completeness

completeness: supported. Targets: GO:0030061.

Known MICOS and ATP-synthase complexes already supply a meaningful molecular abstraction. Additional subunits, lipids and optional protein examples remain possible enrichment, without a consequential missing-inventory finding. No images, numerical properties or quotations are present.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/mitochondrial_crista.yaml; Entire maintained YAML including all components, graph edges, discussions and history | context_only | Complete target read; maintained scientific bytes remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; CausalNodeTypeEnum, StructuralComponent and essentiality | context_only | A GO cellular component has STRUCTURE node identity; constituent membership and formation necessity are distinct. |
| boundary | data/structures/membrane_organelle/mitochondrial_crista_junction.yaml; Entire frozen boundary neighbor | context_only | Read only to distinguish the whole crista, junction region and associated architecture machinery; not a second review target. |
| crista-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030061,GO:0005743,GO:0044284,GO:0097002,GO:0061617,GO:0045259,GO:0042407,GO:0006119,GO:0044232,GO:0007007; Complete ten returned entries; no inferred relation is represented as an unreturned native edge. | supports | All ten exact active terms, definitions, synonym scopes and returned child relations checked. Inner membrane explicitly lists crista/junction as part_of children; contact-site term lists junction as is_a child. MICOS is a six-subunit yeast complex; ATP synthase is a broader F-type complex. |
| crista-agent-GO0030061-isa | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030061/ancestors?relations=is_a; Complete ancestors list, requested relations=is_a | supports | Exact is_a-only response checked. Junction has organelle membrane contact site ancestry; crista has only general cellular-component ancestors in this response. |
| crista-agent-tax2759 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759; taxId, scientificName, rank; taxonomy identity only | supports | Native taxId/scientificName verifies Eukaryota at domain rank. |
| crista-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; taxId, scientificName, rank; taxonomy identity only | supports | Native taxId/scientificName verifies Saccharomyces cerevisiae at species rank; this is not a population survey. |
| crista-agent-friedman2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554/elife.07739&amp;format=json&amp;resultType=core; Complete resultList.result[0] identity and abstractText | supports | Complete native bibliographic identity and abstract inspected; DOI/title/authors/year/PMID and PMC identity agree with the cited paper. |
| crista-agent-friedman2014-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature12985&amp;format=json&amp;resultType=core; Complete resultList.result[0] identity and abstractText | supports | Complete native bibliographic identity and abstract inspected; DOI/title/authors/year/PMID and PMC identity agree with the cited paper. |
| crista-agent-davies2012-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.1204593109&amp;format=json&amp;resultType=core; Complete resultList.result[0] identity and abstractText | supports | Complete native bibliographic identity and abstract inspected; DOI/title/authors/year/PMID and PMC identity agree with the cited paper. |
| crista-agent-paumard2002-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/emboj/21.3.221&amp;format=json&amp;resultType=core; Complete resultList.result[0] identity and abstractText | supports | Complete native bibliographic identity and abstract inspected; DOI/title/authors/year/PMID and PMC identity agree with the cited paper. |
| crista-agent-friedman2015-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/PMC4434539.1.xml; Results s2-1 through s2-7 main prose, Discussion s3; Methods yeast growth, fluorescence microscopy and electron microscopy. Figures1-4/7 captions and associated embedded captions read; no pixels, raw data or supplemental tables reanalyzed. | supports | Yeast deletion/reconstitution, fluorescence, biochemical and thin-section TEM data support two MICOS subcomplexes and normal membrane organization. Junction positioning of Mic27/Mic60 is supported by crista-marker adjacency; direct junction immuno-EM was unsuccessful. Mic19 copy-number regulation remains a proposed explanation. |
| crista-agent-friedman2014-jats | https://pmc-oa-opendata.s3.amazonaws.com/PMC4075653.1/PMC4075653.1.xml; Body S5, paragraph beginning Mitochondrial skeletal structures; complete native abstract separately. Other main sections not certified read. | supports | Inspected review passage distinguishes inner boundary/crista regions, narrow junctions, MICOS scaffold and ATP-synthase-stabilized ridges. It is secondary synthesis, not an independent perturbation experiment. |
| crista-agent-davies2012-pmc | https://pmc.ncbi.nlm.nih.gov/articles/3427116/; Complete Results SEC1, Discussion SEC2, Conclusion SEC3; Methods sec12 strains and sec13 cryotomography; main captions. Other Methods, supplements and figure pixels not independently inspected. | supports | Genuine full primary HTML: yeast cryotomography resolves dimer rows along curved ridges; e/g/su4TM1 mutants lose dimers and typical lamellar cristae. Coarse-grained simulations propose membrane-energy-driven row assembly, distinct from the observed architecture. |
| crista-agent-paumard2002-pmc | https://pmc.ncbi.nlm.nih.gov/articles/125827/; Results sec3/TableI and sec7/TableII, Discussion sec8 including sec9 model, Methods sec10-14; associated captions. No raw microscopy pixels, earlier crosslinking Results or unseen supplement certified. | supports | Deletion of e/g produces altered onion-like/digitated inner membranes while rho+ mutant ATP-synthesis machinery can remain functional. Thin-section TEM and immunogold support morphology; the detailed dimer-association model is explicitly speculative. |
| schema-result | just validate data/structures/membrane_organelle/mitochondrial_crista.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/mitochondrial_crista.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/mitochondrial_crista.yaml --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/mitochondrial_crista-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitochondrial_crista.yaml --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/mitochondrial_crista-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch32-20261022-k96_2wx1/mitochondrial_crista-strict.tsv |
| focused-causal | /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitochondrial_crista.yaml; /private/tmp/cellstructure-batch32-20261022-k96_2wx1/crista-agent/mitochondrial_crista-causal.log | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/mitochondrial_crista.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 14 of 14 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Source reading is limited to the precise source-specific extents above. No raw microscopy image pixels or supplemental datasets were reanalyzed.
- GO definitions and native relations are distinguished from anatomy-based interpretations; quantitative prevalence and explicit GO taxon constraints were not independently established.
- The initial attempted score_causal_graphs.py --record invocation failed with argument error2 and was preserved; corrected native uniprot_genes.py --causal-graphs completed0. This was not a review-draft validation failure.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T022238Z-mitochondrial-crista-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Scientific review of mitochondrial crista
started_at: '2026-10-22T02:03:13Z'
finished_at: '2026-10-22T02:22:38Z'
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
summary: Crista identity, topology and yeast architectural roles are supported; no
  concrete issue observed. General lineage scope and universal formation necessity
  remain bounded unknowns.
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
  - path: .claude/skills/uniprot-protein-examples/SKILL.md
    sha256: 6462894c8257823bae2b175c34693cd42f11ff9269a3829c15b9286ba6d7c876
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/membrane_organelle/mitochondrial_crista.yaml
    sha256: d7f734bbcd5e5af1c899f0c2034d2bc72656eaeb71d5861cf185613c65f4bda6
    role: target
  - path: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
    sha256: fccd57bdf4448897c74fae433fbec5a596152571a8ad7e21034643d8d4379653
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
- target_id: GO:0030061
  path: data/structures/membrane_organelle/mitochondrial_crista.yaml
  label: mitochondrial crista
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/mitochondrial_crista.yaml
    role: maintained scientific record
scope:
  description: One complete maintained record; exact native identities, source contexts,
    molecular/graph representation and limitations.
  selection: Batch32 fixed strict path-order selection, one target only.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0030061
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0030061
  command: just validate data/structures/membrane_organelle/mitochondrial_crista.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0030061
  command: just validate-strict data/structures/membrane_organelle/mitochondrial_crista.yaml
    --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/mitochondrial_crista-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal
  name: Native focused causal
  status: passed
  required: true
  target_ids:
  - GO:0030061
  command: /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitochondrial_crista.yaml
  exit_code: 0
  summary: Focused native command completed successfully; scientific scope is assessed
    separately.
  evidence_ids:
  - focused-causal
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0030061
  summary: No expression-module or transcriptomic-regulon claim; structural microscopy
    and perturbations do not require an expression-module lookup.
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0030061
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - boundary
  - crista-agent-go
  - crista-agent-GO0030061-isa
  - crista-agent-tax2759
  - crista-agent-tax4932
  - crista-agent-friedman2015-meta
  - crista-agent-friedman2014-meta
  - crista-agent-davies2012-meta
  - crista-agent-paumard2002-meta
  - crista-agent-friedman2015-jats
  - crista-agent-friedman2014-jats
  - crista-agent-davies2012-pmc
  - crista-agent-paumard2002-pmc
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0030061
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
  - GO:0030061
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
  - GO:0030061
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
  - GO:0030061
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
  - GO:0030061
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
  - GO:0030061
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
  reference: data/structures/membrane_organelle/mitochondrial_crista.yaml
  locator: Entire maintained YAML including all components, graph edges, discussions
    and history
  accessed_at: '2026-10-22T02:13:45Z'
  support: context_only
  summary: Complete target read; maintained scientific bytes remain unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: CausalNodeTypeEnum, StructuralComponent and essentiality
  accessed_at: '2026-10-22T02:13:45Z'
  support: context_only
  summary: A GO cellular component has STRUCTURE node identity; constituent membership
    and formation necessity are distinct.
- evidence_id: boundary
  kind: record_content
  reference: data/structures/membrane_organelle/mitochondrial_crista_junction.yaml
  locator: Entire frozen boundary neighbor
  accessed_at: '2026-10-22T02:13:45Z'
  support: context_only
  summary: Read only to distinguish the whole crista, junction region and associated
    architecture machinery; not a second review target.
- evidence_id: crista-agent-go
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030061,GO:0005743,GO:0044284,GO:0097002,GO:0061617,GO:0045259,GO:0042407,GO:0006119,GO:0044232,GO:0007007
  locator: Complete ten returned entries; no inferred relation is represented as an
    unreturned native edge.
  accessed_at: '2026-10-22T02:10:27.024416Z'
  support: supports
  summary: All ten exact active terms, definitions, synonym scopes and returned child
    relations checked. Inner membrane explicitly lists crista/junction as part_of
    children; contact-site term lists junction as is_a child. MICOS is a six-subunit
    yeast complex; ATP synthase is a broader F-type complex.
  snapshot_sha256: 2fc2451c5f30697ef017029eb4eb0653dde987bfcca2086d83b363aec4b63a5e
- evidence_id: crista-agent-GO0030061-isa
  kind: database
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030061/ancestors?relations=is_a
  locator: Complete ancestors list, requested relations=is_a
  accessed_at: '2026-10-22T02:10:28.569034Z'
  support: supports
  summary: Exact is_a-only response checked. Junction has organelle membrane contact
    site ancestry; crista has only general cellular-component ancestors in this response.
  snapshot_sha256: e045717e49d54f41d35c2dac4b0af09cf50374c0e6b7792086431f1adff22257
- evidence_id: crista-agent-tax2759
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2759
  locator: taxId, scientificName, rank; taxonomy identity only
  accessed_at: '2026-10-22T02:10:27.062961Z'
  support: supports
  summary: Native taxId/scientificName verifies Eukaryota at domain rank.
  snapshot_sha256: 47d02c524bbdc511eb1fc377bdedc484b5cb6d3504611b0cbc6c280a65f140b4
- evidence_id: crista-agent-tax4932
  kind: database
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: taxId, scientificName, rank; taxonomy identity only
  accessed_at: '2026-10-22T02:10:27.046142Z'
  support: supports
  summary: Native taxId/scientificName verifies Saccharomyces cerevisiae at species
    rank; this is not a population survey.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: crista-agent-friedman2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554/elife.07739&format=json&resultType=core
  locator: Complete resultList.result[0] identity and abstractText
  accessed_at: '2026-10-22T02:10:24.454393Z'
  support: supports
  summary: Complete native bibliographic identity and abstract inspected; DOI/title/authors/year/PMID
    and PMC identity agree with the cited paper.
  snapshot_sha256: c0346d49ef66ef89b48bcb0cda60019732342884dae87eaf75e9b0fe8e80f3a4
- evidence_id: crista-agent-friedman2014-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1038/nature12985&format=json&resultType=core
  locator: Complete resultList.result[0] identity and abstractText
  accessed_at: '2026-10-22T02:10:24.454595Z'
  support: supports
  summary: Complete native bibliographic identity and abstract inspected; DOI/title/authors/year/PMID
    and PMC identity agree with the cited paper.
  snapshot_sha256: 390af3048cd69551f299e85c996efeab680b69e214c78b6d5d02bb24c0945d0a
- evidence_id: crista-agent-davies2012-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1073/pnas.1204593109&format=json&resultType=core
  locator: Complete resultList.result[0] identity and abstractText
  accessed_at: '2026-10-22T02:10:24.454487Z'
  support: supports
  summary: Complete native bibliographic identity and abstract inspected; DOI/title/authors/year/PMID
    and PMC identity agree with the cited paper.
  snapshot_sha256: 6986a1e7d541d63c2c2c4edb9cd773a014026b1ac3ccf732291295f2eda56e49
- evidence_id: crista-agent-paumard2002-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1093/emboj/21.3.221&format=json&resultType=core
  locator: Complete resultList.result[0] identity and abstractText
  accessed_at: '2026-10-22T02:10:24.453998Z'
  support: supports
  summary: Complete native bibliographic identity and abstract inspected; DOI/title/authors/year/PMID
    and PMC identity agree with the cited paper.
  snapshot_sha256: fd960ff53fa221055f8814a0643d7c909aca15deca64173b50a1300e1b636b35
- evidence_id: crista-agent-friedman2015-jats
  kind: primary_source
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4434539.1/PMC4434539.1.xml
  locator: Results s2-1 through s2-7 main prose, Discussion s3; Methods yeast growth,
    fluorescence microscopy and electron microscopy. Figures1-4/7 captions and associated
    embedded captions read; no pixels, raw data or supplemental tables reanalyzed.
  accessed_at: '2026-10-22T02:10:55.341589Z'
  support: supports
  summary: Yeast deletion/reconstitution, fluorescence, biochemical and thin-section
    TEM data support two MICOS subcomplexes and normal membrane organization. Junction
    positioning of Mic27/Mic60 is supported by crista-marker adjacency; direct junction
    immuno-EM was unsuccessful. Mic19 copy-number regulation remains a proposed explanation.
  snapshot_sha256: 8d1082e98a558176fbd86c80851d3467e7bf41c986f38b8dfe00810c3903a345
- evidence_id: crista-agent-friedman2014-jats
  kind: authority
  reference: https://pmc-oa-opendata.s3.amazonaws.com/PMC4075653.1/PMC4075653.1.xml
  locator: Body S5, paragraph beginning Mitochondrial skeletal structures; complete
    native abstract separately. Other main sections not certified read.
  accessed_at: '2026-10-22T02:10:55.342035Z'
  support: supports
  summary: Inspected review passage distinguishes inner boundary/crista regions, narrow
    junctions, MICOS scaffold and ATP-synthase-stabilized ridges. It is secondary
    synthesis, not an independent perturbation experiment.
  snapshot_sha256: 37cb298ab74e8ff5524164dcfa6563f44b3fc8f0833ce2049dad7d11f8e6ae97
- evidence_id: crista-agent-davies2012-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/3427116/
  locator: Complete Results SEC1, Discussion SEC2, Conclusion SEC3; Methods sec12
    strains and sec13 cryotomography; main captions. Other Methods, supplements and
    figure pixels not independently inspected.
  accessed_at: '2026-10-22T02:11:43.022308Z'
  support: supports
  summary: 'Genuine full primary HTML: yeast cryotomography resolves dimer rows along
    curved ridges; e/g/su4TM1 mutants lose dimers and typical lamellar cristae. Coarse-grained
    simulations propose membrane-energy-driven row assembly, distinct from the observed
    architecture.'
  snapshot_sha256: 70354780b5d7e88115d57130c1212085c663c1d0f01bbc051eb4d7d4c3edf9f7
- evidence_id: crista-agent-paumard2002-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/125827/
  locator: Results sec3/TableI and sec7/TableII, Discussion sec8 including sec9 model,
    Methods sec10-14; associated captions. No raw microscopy pixels, earlier crosslinking
    Results or unseen supplement certified.
  accessed_at: '2026-10-22T02:11:43.021981Z'
  support: supports
  summary: Deletion of e/g produces altered onion-like/digitated inner membranes while
    rho+ mutant ATP-synthesis machinery can remain functional. Thin-section TEM and
    immunogold support morphology; the detailed dimer-association model is explicitly
    speculative.
  snapshot_sha256: f4cb30d8cbf66c8425cbafa5456368e43025874fbb1cf949bc8ee8b8dc2364b8
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/mitochondrial_crista.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:03:14Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/mitochondrial_crista.yaml'
  snapshot_sha256: c5381d07cf0cfe1b417ccc81f4289e9af9c6f88db082082f99ba9d6db7a28e60
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/mitochondrial_crista.yaml
    --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/mitochondrial_crista-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:03:15Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/mitochondrial_crista.yaml\
    \ --out /private/tmp/cellstructure-batch32-20261022-k96_2wx1/mitochondrial_crista-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch32-20261022-k96_2wx1/mitochondrial_crista-strict.tsv"
  snapshot_sha256: 1c7c604bc37b98a72cadc595650bab176bf4549861cb1957c9858188f02c54a9
- evidence_id: focused-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch32-20261022-k96_2wx1/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/mitochondrial_crista.yaml
  locator: /private/tmp/cellstructure-batch32-20261022-k96_2wx1/crista-agent/mitochondrial_crista-causal.log
  accessed_at: '2026-10-22T02:11:39.791698Z'
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
  locator: data/structures/membrane_organelle/mitochondrial_crista.yaml; native collect()
    exact identifier slice; SHA identifies full original TSV
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
  topic: Exact compartment and topology
  outcome: supported
  target_ids:
  - GO:0030061
  summary: Definition and identifier agree with native GO. Crista-junction connection
    to the inner boundary membrane is direct definition support; crista has_part junction
    is anatomical interpretation, not claimed as a returned native crista-child edge.
    Junction contact-site is_a and inner-membrane part_of are verified.
  evidence_ids:
  - crista-agent-go
  - crista-agent-GO0030061-isa
  - record
  - boundary
- assessment_id: scope
  area: scope
  topic: Taxonomy and experimental context
  outcome: supported
  target_ids:
  - GO:0030061
  summary: Taxon identities and the budding-yeast canonical model are supported. COMMON
    describes the ordinary crista-bearing yeast context; mutant/respiratory-state
    differences do not establish species absence or a prevalence percentage. Yeast
    strain-specific results are not generalized to identical architecture across all
    Eukaryota.
  evidence_ids:
  - crista-agent-tax2759
  - crista-agent-tax4932
  - crista-agent-friedman2015-jats
- assessment_id: taxon-limit
  area: scope
  topic: Limits of general Eukaryota statement
  outcome: unknown
  target_ids:
  - GO:0030061
  summary: Native term response does not contain explicit taxon-constraint data. The
    specific reduced-anaerobic-organelle explanation in the whole crista record is
    not established by the selected Friedman2014 passage; no exhaustive lineage survey
    was done. This bounded uncertainty is not evidence that the biological statement
    is false.
  evidence_ids:
  - crista-agent-friedman2014-jats
  - crista-agent-go
- assessment_id: membership
  area: grounding
  topic: Complex membership and architecture machinery
  outcome: supported
  target_ids:
  - GO:0030061
  summary: MICOS is correctly associated architecture machinery; resident F-type ATP
    synthase is a constituent. GO complex abstractions are valid and avoid claiming
    a fixed species-independent subunit inventory. The seven-edge NONMECHANISTIC graph
    preserves topology, maintenance, ridge shaping and respiratory support without
    inventing a complete assembly sequence.
  evidence_ids:
  - crista-agent-go
  - crista-agent-friedman2015-jats
  - crista-agent-davies2012-pmc
  - crista-agent-paumard2002-pmc
  - schema
- assessment_id: necessity
  area: grounding
  topic: Formation necessity
  outcome: unknown
  target_ids:
  - GO:0030061
  summary: Both complex rows deliberately use UNKNOWN. Localization, altered morphology
    and individual mutant phenotypes do not establish universal necessity of every
    complex/member for any inward membrane fold.
  evidence_ids:
  - crista-agent-friedman2015-jats
  - crista-agent-davies2012-pmc
  - crista-agent-paumard2002-pmc
  - schema
- assessment_id: completeness
  area: completeness
  topic: Bounded whole-record completeness
  outcome: supported
  target_ids:
  - GO:0030061
  summary: Known MICOS and ATP-synthase complexes already supply a meaningful molecular
    abstraction. Additional subunits, lipids and optional protein examples remain
    possible enrichment, without a consequential missing-inventory finding. No images,
    numerical properties or quotations are present.
  evidence_ids:
  - crista-agent-go
  - crista-agent-GO0030061-isa
  - crista-agent-tax2759
  - crista-agent-tax4932
  - crista-agent-friedman2015-meta
  - crista-agent-friedman2014-meta
  - crista-agent-davies2012-meta
  - crista-agent-paumard2002-meta
  - crista-agent-friedman2015-jats
  - crista-agent-friedman2014-jats
  - crista-agent-davies2012-pmc
  - crista-agent-paumard2002-pmc
findings: []
actions: []
limitations:
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Source reading is limited to the precise source-specific extents above. No raw microscopy
  image pixels or supplemental datasets were reanalyzed.
- GO definitions and native relations are distinguished from anatomy-based interpretations;
  quantitative prevalence and explicit GO taxon constraints were not independently
  established.
- The initial attempted score_causal_graphs.py --record invocation failed with argument
  error2 and was preserved; corrected native uniprot_genes.py --causal-graphs completed0.
  This was not a review-draft validation failure.
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
