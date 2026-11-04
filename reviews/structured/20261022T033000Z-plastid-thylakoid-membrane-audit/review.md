# Source-backed review of plastid thylakoid membrane

- Review: 20261022T033000Z-plastid-thylakoid-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T03:14:04Z
- Finished UTC: 2026-10-22T03:30:00Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact identity, source-supported topology, taxon context and Chlamydomonas cryoET example are sound. No concrete curation defect was established within the explicit source limits.

## Scope And Provenance

Exactly one complete target; the two sibling thylakoid records and whole plastid are frozen boundary context. Exact native authorities, declared source passages, source placement, material identity, formation-necessity semantics, all graph fields and historical notes were assessed.

Selection: Batch39 fixed strict path order, index5; exactly one maintained record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0055035 | data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml | maintained | plastid thylakoid membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0055035 | Focused validator passed. |
| Focused native strict | passed | True | GO:0055035 | Focused validator passed. |
| Native focused graph check | passed | True | GO:0055035 | Read-only graph check passed; zero GENE_OR_PROTEIN nodes are asserted. |
| Claim-level scientific review | passed | True | GO:0055035 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0055035 | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0055035 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0055035 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0055035 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0055035 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0055035 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Exact identity and whole/part boundaries

identity: supported. Targets: GO:0055035.

GO0055035 exactly identifies the bilayer membrane, broader GO0042651 and whole-thylakoid parthood. Chloroplast and cyanelle membrane children are explicit native GO classes. The organellar chromatophore classification is separately supported by SL0356, not a fabricated native GO edge.

### Collective bilayer material and bounded label-only grounding

grounding: supported. Targets: GO:0055035.

The constituent explicitly denotes collective lipid material and deliberately avoids grounding it to the whole membrane GO term. The corresponding STRUCTURE graph node represents the membrane supported by that material. The open exact-material grounding task does not force an invented chemical species or ratio.

### Collective constitution versus individual formation necessity

grounding: unknown. Targets: GO:0055035.

A lipid bilayer is constitutional to this membrane-bounded class. Neither the primary mature-architecture study nor the secondary functional review establishes the formation necessity of any particular lipid species, photosystem, transporter or individual protein. Those individual requirements remain unknown; no depletion or assembly assay is inferred.

### Green-lineage and glaucophyte scope with exact imaging example

scope: supported. Targets: GO:0055035.

Native taxonomy verifies Viridiplantae, Glaucocystophyceae and C.reinhardtii identities. The secondary review supports photosynthetic plant/algal thylakoids, and native cyanelle identities support the glaucophyte subtype. COMMON is qualitative class context, not a measured prevalence census. Engel directly supports the Chlamydomonas imaging example in CC124(137c); no other strain or universal architecture is inferred.

### Target-specific topology and function

graph: supported. Targets: GO:0055035.

Two NONMECHANISTIC edges state lumen enclosure and support for light-reaction complexes. The oxygenic GO0019684 process matches photosynthetic plastids; no complete stoichiometric pathway or molecular assembly sequence is claimed.

### Entire record and bounded unresolved enrichment

completeness: supported. Targets: GO:0055035.

Every field, evidence placement, graph node/edge, history and discussion was reviewed. No protein examples, image, direct quotation or quantitative dimensions are asserted. The label-only material task and absent optional molecular inventory do not create automatic findings. Historical source-access events are not judged false because newer access is available.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml; Entire maintained YAML, including every component, source note, graph, history and discussion | context_only | Complete target bytes were read. Historical events retain their original temporal scope. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent, ComponentTypeEnum, EssentialityEnum and graph semantics | context_only | Whole-membrane location identity is distinct from LIPID chemical material. Constitutional collective bilayer support does not establish each individual molecular formation requirement. |
| local-plastid | data/structures/membrane_organelle/plastid.yaml; Complete frozen boundary record; identity and component/graph context | context_only | The exact local boundary was read; neighboring experimental interpretations are not substituted for directly inspected sources. |
| local-plastid_thylakoid | data/structures/membrane_organelle/plastid_thylakoid.yaml; Complete frozen boundary record; identity and component/graph context | context_only | The exact local boundary was read; neighboring experimental interpretations are not substituted for directly inspected sources. |
| local-plastid_thylakoid_lumen | data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml; Complete frozen boundary record; identity and component/graph context | context_only | The exact local boundary was read; neighboring experimental interpretations are not substituted for directly inspected sources. |
| thylakoid-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031976,GO:0009579,GO:0009536,GO:0055035,GO:0031978,GO:0019684,GO:0009843,GO:0031977,GO:0033114,GO:0042651,GO:0033115,GO:0009535,GO:0070118; All13 complete entries: id/name/definition/isObsolete/synonyms/comments/typed children; exact relation directions retained. | supports | The13 active terms distinguish whole plastid thylakoid, membrane and enclosed lumen; their typed children support the stated generic parents, plastid parthood and cyanelle/chloroplast subclasses. GO0009579 explicitly distinguishes thylakoids from organelles. GO0019684 is oxygenic PSI/PSII light reactions. GO0070118 is returned under generic thylakoid membrane; this response does not expose a direct GO0055035-to-GO0070118 is_a edge. |
| thylakoid-agent-SL0278 | https://rest.uniprot.org/locations/SL-0278.json; Complete identity/definition/GO mapping and immediate isA/partOf hierarchy. | supports | SL0278 directly maps plastid thylakoid to GO0031976, with thylakoid isA and plastid partOf. Its definition and nested hierarchy describe compartment identity rather than a taxon-prevalence measurement. |
| thylakoid-agent-SL0082 | https://rest.uniprot.org/locations/SL-0082.json; Complete top-level cyanelle definition, GO mapping and isA plastid hierarchy. | supports | SL0082 identifies cyanelles as glaucocystophyte photosynthetic organelles with cyanobacteria-like thylakoids, a peptidoglycan-containing envelope and plastid classification. It supports the glaucophyte context, not a numerical prevalence census. |
| thylakoid-agent-SL0356 | https://rest.uniprot.org/locations/SL-0356.json; Complete SL0356 identity/definition, top-level isA SL0216 and its GO0055035 mapping, partOf SL0354. Original B36 bytes/time retained. | supports | SL0356 maps organellar chromatophore thylakoid membrane to GO0070118 and explicitly lists SL0216/GO0055035 as isA. This separate UniProt location hierarchy supports the broader plastid-thylakoid-membrane classification even though the inspected native GO response does not expose that direct edge. |
| thylakoid-agent-tax33090 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId33090 identifies Viridiplantae at rank kingdom; lineage and otherNames preserve the exact taxon and synonyms. This authority supplies identity, not experimental frequency or strain-specific phenotypes. |
| thylakoid-agent-tax38254 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId38254 identifies Glaucocystophyceae at rank class; lineage and otherNames preserve the exact taxon and synonyms. This authority supplies identity, not experimental frequency or strain-specific phenotypes. |
| thylakoid-agent-tax3055 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Complete taxId/scientificName/rank/lineage/otherNames. | supports | ENA taxId3055 identifies Chlamydomonas reinhardtii at rank species; lineage and otherNames preserve the exact taxon and synonyms. This authority supplies identity, not experimental frequency or strain-specific phenotypes. |
| thylakoid-agent-perez2024-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI and complete abstract. | supports | The exact MED38950450 record matches DOI10.1146/annurev-cellbio-120823-022747 and Evolution of Thylakoid Structural Diversity.. Complete abstract, authors/year and publication identity were read; metadata does not imply full-body access. |
| thylakoid-agent-engel2015-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554%2FeLife.04889&amp;format=json&amp;resultType=core; Unique MED identity/title/authors/year/DOI and complete abstract. | supports | The exact MED25584625 record matches DOI10.7554/elife.04889 and Native architecture of the Chlamydomonas chloroplast revealed by in situ cryo-electron tomography.. Complete abstract, authors/year and publication identity were read; metadata does not imply full-body access. |
| thylakoid-agent-perez2024-browser-introduction | https://doi.org/10.1146%2Fannurev-cellbio-120823-022747; Complete Introduction beginning “Since the dawn”, two paragraphs, and initial architecture paragraph within the captured publisher representation. Surrounding mixed retrieval content is not article body. | supports | The inspected secondary review Introduction describes thylakoids of plants/algae and cyanobacteria, with the lumen separated for proton-gradient-driven ATP synthesis. The retained mixed browser representation has status:null, not native HTTP200 full-paper access. |
| thylakoid-agent-perez2024-browser-search | https://doi.org/10.1146%2Fannurev-cellbio-120823-022747; JSON-encoded browser representation: full two paragraphs Electron Transport Chain Complexes and first Antenna Systems paragraph; status:null. | supports | The inspected secondary review subsection explains oxygenic PSII, plastoquinone, b6f, plastocyanin, PSI and ferredoxin/NADPH electron transfer and ATP-synthase use of the proton gradient. It supports the generic photosynthetic function, not necessity of each protein for membrane assembly. |
| thylakoid-agent-perez2024-publisher-new | https://www.annualreviews.org/content/journals/10.1146/annurev-cellbio-120823-022747?TRACK=RSS; HTTP status and exact challenge body. | context_only | The native publisher response is HTTP403 challenge HTML and supplies no article body. The separately retained browser excerpts have their own original timestamps and bounded reading scope. |
| thylakoid-agent-engel2015-jats-xml | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292175/fullTextXML; Genuine full JATS independently read: s1; complete s2-1/s2-2/s2-3 and their main captions; s3-1/s3-2; Methods s4-1 through s4-5. No figure/video pixels, supplements or raw tomograms analyzed. | supports | Engel2015 directly resolves native Chlamydomonas reinhardtii thylakoid membranes and lumen by in situ cryoFIB/cryoET. Methods use WT CC124(137c), TAP growth and specified illumination/aeration, vitrified cells, cryoFIB lamellae and tilt-series tomography. The study reports native networks and rare envelope-thylakoid connections but explicitly limits conclusions about universal compartment continuity and hypothesizes biogenesis/transport. The record claims the supported imaging example, not those unestablished mechanisms. |
| schema-result | just validate data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_thylakoid_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_thylakoid_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_thylakoid_membrane-strict.tsv |
| focused-causal | /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml; Complete focused read-only graph report | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 13 of 13 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Unchanged imports preserve original source URL, UTC access time and raw SHA256. The Perez review was read only in the complete abstract and named browser-extracted Introduction/electron-transport passages; its native publisher response is403. Browser representations have status:null, not HTTP200 full-body receipts.
- Engel primary sections and Methods listed in the evidence were read directly; figure captions were read but pixels, videos, supplements and raw tomography were not reanalyzed. CC124 growth/imaging context is preserved; universal continuity, detailed biogenesis mechanisms and prevalence counts are not inferred.
- Individual molecular formation necessity, exact lipid species/ratios and exhaustive taxon-neutral protein inventories remain unknown. The collective boundary is distinguished from those individual requirements.
- UniProt SL0356 supports the organellar chromatophore membrane classification; the inspected GO response does not expose the corresponding direct GO0055035 is_a edge. No missing native edge is silently invented.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User explicitly requests one review for every unreviewed record; no maintained scientific or history edits were made.
- iModulonDB is not applicable: these records assert physical compartment topology and photosynthesis rather than expression-module membership.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T033000Z-plastid-thylakoid-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Source-backed review of plastid thylakoid membrane
started_at: '2026-10-22T03:14:04Z'
finished_at: '2026-10-22T03:30:00Z'
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
summary: Exact identity, source-supported topology, taxon context and Chlamydomonas
  cryoET example are sound. No concrete curation defect was established within the
  explicit source limits.
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
  - path: data/structures/membrane_organelle/plastid.yaml
    sha256: 1be30ab06bc2fbae9294930ceaf74b20a2d43d8af60986aa9ed0e07b9645ae81
    role: context
  - path: data/structures/membrane_organelle/plastid_thylakoid.yaml
    sha256: ec3c74ee89bf25eea6a3a5682b3f7f73e0837465dccf2a8f2c0cce1550a4e3c8
    role: context
  - path: data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
    sha256: 7a75c5aee47a20bbae7da6351e07fc7f2d1dc418e7ca34e253d08e3a531ff4ee
    role: context
  - path: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    sha256: 51a2ece521e1b5c0b3b589fc7cf665be1c9544299257e0fda7fcf8352e7401c2
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
- target_id: GO:0055035
  path: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  label: plastid thylakoid membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    role: maintained scientific record
scope:
  description: Exactly one complete target; the two sibling thylakoid records and
    whole plastid are frozen boundary context. Exact native authorities, declared
    source passages, source placement, material identity, formation-necessity semantics,
    all graph fields and historical notes were assessed.
  selection: Batch39 fixed strict path order, index5; exactly one maintained record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0055035
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: just validate data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: just validate-strict data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_thylakoid_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: focused-causal
  name: Native focused graph check
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  exit_code: 0
  summary: Read-only graph check passed; zero GENE_OR_PROTEIN nodes are asserted.
  evidence_ids:
  - focused-causal
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0055035
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - local-plastid
  - local-plastid_thylakoid
  - local-plastid_thylakoid_lumen
  - thylakoid-agent-go
  - thylakoid-agent-SL0278
  - thylakoid-agent-SL0082
  - thylakoid-agent-SL0356
  - thylakoid-agent-tax33090
  - thylakoid-agent-tax38254
  - thylakoid-agent-tax3055
  - thylakoid-agent-perez2024-meta
  - thylakoid-agent-engel2015-meta
  - thylakoid-agent-perez2024-browser-introduction
  - thylakoid-agent-perez2024-browser-search
  - thylakoid-agent-perez2024-publisher-new
  - thylakoid-agent-engel2015-jats-xml
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0055035
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
  - GO:0055035
  command: just qc
  exit_code: 0
  summary: 'Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history,
    strict schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T01:05:35Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: just validate-history
  exit_code: 0
  summary: Exit0. All 1888 history records validated; URI precheck reported zero invalid
    references.
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:37Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: just validate-products
  exit_code: 0
  summary: 'Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:33Z to
    2026-10-22T00:59:14Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0055035
  command: just check-trait-links --check
  exit_code: 0
  summary: 'Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled.'
  scope_note: Full-corpus-only documented recipe executed 2026-10-22T00:58:32Z to
    2026-10-22T00:58:40Z in the original fresh batch26 checkout at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc;
    input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02.
    Same-base guards rechecked every manifested input in both the original batch26
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0055035
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
    and current batch39 checkouts. It is not a scientific review of other targets.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  locator: Entire maintained YAML, including every component, source note, graph,
    history and discussion
  accessed_at: '2026-10-22T03:26:22Z'
  support: context_only
  summary: Complete target bytes were read. Historical events retain their original
    temporal scope.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent, ComponentTypeEnum, EssentialityEnum and graph semantics
  accessed_at: '2026-10-22T03:26:22Z'
  support: context_only
  summary: Whole-membrane location identity is distinct from LIPID chemical material.
    Constitutional collective bilayer support does not establish each individual molecular
    formation requirement.
- evidence_id: local-plastid
  kind: record_content
  reference: data/structures/membrane_organelle/plastid.yaml
  locator: Complete frozen boundary record; identity and component/graph context
  accessed_at: '2026-10-22T03:26:22Z'
  support: context_only
  summary: The exact local boundary was read; neighboring experimental interpretations
    are not substituted for directly inspected sources.
- evidence_id: local-plastid_thylakoid
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid.yaml
  locator: Complete frozen boundary record; identity and component/graph context
  accessed_at: '2026-10-22T03:26:22Z'
  support: context_only
  summary: The exact local boundary was read; neighboring experimental interpretations
    are not substituted for directly inspected sources.
- evidence_id: local-plastid_thylakoid_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/plastid_thylakoid_lumen.yaml
  locator: Complete frozen boundary record; identity and component/graph context
  accessed_at: '2026-10-22T03:26:22Z'
  support: context_only
  summary: The exact local boundary was read; neighboring experimental interpretations
    are not substituted for directly inspected sources.
- evidence_id: thylakoid-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0031976,GO:0009579,GO:0009536,GO:0055035,GO:0031978,GO:0019684,GO:0009843,GO:0031977,GO:0033114,GO:0042651,GO:0033115,GO:0009535,GO:0070118
  locator: 'All13 complete entries: id/name/definition/isObsolete/synonyms/comments/typed
    children; exact relation directions retained.'
  accessed_at: '2026-10-22T03:22:44.406059Z'
  support: supports
  summary: The13 active terms distinguish whole plastid thylakoid, membrane and enclosed
    lumen; their typed children support the stated generic parents, plastid parthood
    and cyanelle/chloroplast subclasses. GO0009579 explicitly distinguishes thylakoids
    from organelles. GO0019684 is oxygenic PSI/PSII light reactions. GO0070118 is
    returned under generic thylakoid membrane; this response does not expose a direct
    GO0055035-to-GO0070118 is_a edge.
  snapshot_sha256: de37d7d873c4473c1a0b7ffacb29ac80cdedd28189e940610323e2085cefe102
- evidence_id: thylakoid-agent-SL0278
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0278.json
  locator: Complete identity/definition/GO mapping and immediate isA/partOf hierarchy.
  accessed_at: '2026-10-22T03:22:44.406260Z'
  support: supports
  summary: SL0278 directly maps plastid thylakoid to GO0031976, with thylakoid isA
    and plastid partOf. Its definition and nested hierarchy describe compartment identity
    rather than a taxon-prevalence measurement.
  snapshot_sha256: 45de8a98f24dded78cdf48ab6b0ca4812e1750b2ca31842e7dae26127d21c64e
- evidence_id: thylakoid-agent-SL0082
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0082.json
  locator: Complete top-level cyanelle definition, GO mapping and isA plastid hierarchy.
  accessed_at: '2026-10-22T03:23:31.453417Z'
  support: supports
  summary: SL0082 identifies cyanelles as glaucocystophyte photosynthetic organelles
    with cyanobacteria-like thylakoids, a peptidoglycan-containing envelope and plastid
    classification. It supports the glaucophyte context, not a numerical prevalence
    census.
  snapshot_sha256: ae0660e1e761b28504bbca0b97ea8b0cd6260df50fc514d37e4bcdb4afb2a3de
- evidence_id: thylakoid-agent-SL0356
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0356.json
  locator: Complete SL0356 identity/definition, top-level isA SL0216 and its GO0055035
    mapping, partOf SL0354. Original B36 bytes/time retained.
  accessed_at: '2026-10-22T02:44:36.279604Z'
  support: supports
  summary: SL0356 maps organellar chromatophore thylakoid membrane to GO0070118 and
    explicitly lists SL0216/GO0055035 as isA. This separate UniProt location hierarchy
    supports the broader plastid-thylakoid-membrane classification even though the
    inspected native GO response does not expose that direct edge.
  snapshot_sha256: fd631a05c9cdbdd6ee8bc4fa220ede8d59ad460cdaecbc15e98f38709d644934
- evidence_id: thylakoid-agent-tax33090
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/33090
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:09:41.837455Z'
  support: supports
  summary: ENA taxId33090 identifies Viridiplantae at rank kingdom; lineage and otherNames
    preserve the exact taxon and synonyms. This authority supplies identity, not experimental
    frequency or strain-specific phenotypes.
  snapshot_sha256: b1394e36c6896d7ec64cdb301a239f2bc49bc435a22cc21fdba8fdc6217e2d11
- evidence_id: thylakoid-agent-tax38254
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:22:44.406469Z'
  support: supports
  summary: ENA taxId38254 identifies Glaucocystophyceae at rank class; lineage and
    otherNames preserve the exact taxon and synonyms. This authority supplies identity,
    not experimental frequency or strain-specific phenotypes.
  snapshot_sha256: 4b487eb0e34bcb4941fbb315aae5214c96ea6f60255d71a2aca172cd35844009
- evidence_id: thylakoid-agent-tax3055
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Complete taxId/scientificName/rank/lineage/otherNames.
  accessed_at: '2026-10-22T03:09:41.892023Z'
  support: supports
  summary: ENA taxId3055 identifies Chlamydomonas reinhardtii at rank species; lineage
    and otherNames preserve the exact taxon and synonyms. This authority supplies
    identity, not experimental frequency or strain-specific phenotypes.
  snapshot_sha256: e3861fe6706cefe2e079e15c0178a65e95efaad3890f548f25e721553eaa93a0
- evidence_id: thylakoid-agent-perez2024-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.1146%2Fannurev-cellbio-120823-022747&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI and complete abstract.
  accessed_at: '2026-10-21T10:44:30.997805Z'
  support: supports
  summary: The exact MED38950450 record matches DOI10.1146/annurev-cellbio-120823-022747
    and Evolution of Thylakoid Structural Diversity.. Complete abstract, authors/year
    and publication identity were read; metadata does not imply full-body access.
  snapshot_sha256: f9df3427bb3b35764922628c9e89cc9378fa7875a4a103bde71a75b130d54926
- evidence_id: thylakoid-agent-engel2015-meta
  kind: database
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A10.7554%2FeLife.04889&format=json&resultType=core
  locator: Unique MED identity/title/authors/year/DOI and complete abstract.
  accessed_at: '2026-10-22T03:14:51.521865Z'
  support: supports
  summary: The exact MED25584625 record matches DOI10.7554/elife.04889 and Native
    architecture of the Chlamydomonas chloroplast revealed by in situ cryo-electron
    tomography.. Complete abstract, authors/year and publication identity were read;
    metadata does not imply full-body access.
  snapshot_sha256: e871243bee6520756b75290d986d9df20b09b14d80b6ba888a5a1048eeb85e9d
- evidence_id: thylakoid-agent-perez2024-browser-introduction
  kind: primary_source
  reference: https://doi.org/10.1146%2Fannurev-cellbio-120823-022747
  locator: Complete Introduction beginning “Since the dawn”, two paragraphs, and initial
    architecture paragraph within the captured publisher representation. Surrounding
    mixed retrieval content is not article body.
  accessed_at: '2026-10-21T10:46:36.113233Z'
  support: supports
  summary: The inspected secondary review Introduction describes thylakoids of plants/algae
    and cyanobacteria, with the lumen separated for proton-gradient-driven ATP synthesis.
    The retained mixed browser representation has status:null, not native HTTP200
    full-paper access.
  snapshot_sha256: 634c866a9cd76eae27d4820d7734d7e25ef595d42781bf95f8b816821065e9ba
- evidence_id: thylakoid-agent-perez2024-browser-search
  kind: primary_source
  reference: https://doi.org/10.1146%2Fannurev-cellbio-120823-022747
  locator: 'JSON-encoded browser representation: full two paragraphs Electron Transport
    Chain Complexes and first Antenna Systems paragraph; status:null.'
  accessed_at: '2026-10-21T08:46:38.912004Z'
  support: supports
  summary: The inspected secondary review subsection explains oxygenic PSII, plastoquinone,
    b6f, plastocyanin, PSI and ferredoxin/NADPH electron transfer and ATP-synthase
    use of the proton gradient. It supports the generic photosynthetic function, not
    necessity of each protein for membrane assembly.
  snapshot_sha256: 1e2a20aee1043d6a8c9b511e909b825174d51fe9374f438c494e924d20992a0e
- evidence_id: thylakoid-agent-perez2024-publisher-new
  kind: primary_source
  reference: https://www.annualreviews.org/content/journals/10.1146/annurev-cellbio-120823-022747?TRACK=RSS
  locator: HTTP status and exact challenge body.
  accessed_at: '2026-10-21T10:45:06.747552Z'
  support: context_only
  summary: The native publisher response is HTTP403 challenge HTML and supplies no
    article body. The separately retained browser excerpts have their own original
    timestamps and bounded reading scope.
  snapshot_sha256: 28b3b2a15fff24403298d4f0339c20ef6edbfd1dbda58b10de440a95e03e26fd
- evidence_id: thylakoid-agent-engel2015-jats-xml
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4292175/fullTextXML
  locator: 'Genuine full JATS independently read: s1; complete s2-1/s2-2/s2-3 and
    their main captions; s3-1/s3-2; Methods s4-1 through s4-5. No figure/video pixels,
    supplements or raw tomograms analyzed.'
  accessed_at: '2026-10-22T03:15:30.275769Z'
  support: supports
  summary: Engel2015 directly resolves native Chlamydomonas reinhardtii thylakoid
    membranes and lumen by in situ cryoFIB/cryoET. Methods use WT CC124(137c), TAP
    growth and specified illumination/aeration, vitrified cells, cryoFIB lamellae
    and tilt-series tomography. The study reports native networks and rare envelope-thylakoid
    connections but explicitly limits conclusions about universal compartment continuity
    and hypothesizes biogenesis/transport. The record claims the supported imaging
    example, not those unestablished mechanisms.
  snapshot_sha256: 5d5e176465dc54f9a8b7a3b0faace8d7ccfa56ee57bece00723d4b451ff68026
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:14:05Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml'
  snapshot_sha256: e61ff63f375f348f54652addb8e628404741685be96cc9b0c0aeb71fd31c5aca
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
    --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_thylakoid_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T03:14:07Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_thylakoid_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch39-20261022-9ejlvnby/plastid_thylakoid_membrane-strict.tsv"
  snapshot_sha256: 9ee2719cfeea129f6eea968e7324149b2481939c987aa85a57d08ca118f004d4
- evidence_id: focused-causal
  kind: validation
  reference: /private/tmp/cellstructure-batch39-20261022-9ejlvnby/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml
  locator: Complete focused read-only graph report
  accessed_at: '2026-10-22T03:23:28.893209Z'
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
  locator: data/structures/membrane_organelle/plastid_thylakoid_membrane.yaml; native
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
  topic: Exact identity and whole/part boundaries
  outcome: supported
  target_ids:
  - GO:0055035
  summary: GO0055035 exactly identifies the bilayer membrane, broader GO0042651 and
    whole-thylakoid parthood. Chloroplast and cyanelle membrane children are explicit
    native GO classes. The organellar chromatophore classification is separately supported
    by SL0356, not a fabricated native GO edge.
  evidence_ids:
  - record
  - thylakoid-agent-go
  - thylakoid-agent-SL0278
  - thylakoid-agent-SL0082
  - thylakoid-agent-SL0356
- assessment_id: composition
  area: grounding
  topic: Collective bilayer material and bounded label-only grounding
  outcome: supported
  target_ids:
  - GO:0055035
  summary: The constituent explicitly denotes collective lipid material and deliberately
    avoids grounding it to the whole membrane GO term. The corresponding STRUCTURE
    graph node represents the membrane supported by that material. The open exact-material
    grounding task does not force an invented chemical species or ratio.
  evidence_ids:
  - record
  - schema
  - thylakoid-agent-go
  - thylakoid-agent-perez2024-browser-introduction
- assessment_id: necessity
  area: grounding
  topic: Collective constitution versus individual formation necessity
  outcome: unknown
  target_ids:
  - GO:0055035
  summary: A lipid bilayer is constitutional to this membrane-bounded class. Neither
    the primary mature-architecture study nor the secondary functional review establishes
    the formation necessity of any particular lipid species, photosystem, transporter
    or individual protein. Those individual requirements remain unknown; no depletion
    or assembly assay is inferred.
  evidence_ids:
  - record
  - schema
  - thylakoid-agent-go
  - thylakoid-agent-perez2024-browser-introduction
  - thylakoid-agent-engel2015-jats-xml
- assessment_id: taxon
  area: scope
  topic: Green-lineage and glaucophyte scope with exact imaging example
  outcome: supported
  target_ids:
  - GO:0055035
  summary: Native taxonomy verifies Viridiplantae, Glaucocystophyceae and C.reinhardtii
    identities. The secondary review supports photosynthetic plant/algal thylakoids,
    and native cyanelle identities support the glaucophyte subtype. COMMON is qualitative
    class context, not a measured prevalence census. Engel directly supports the Chlamydomonas
    imaging example in CC124(137c); no other strain or universal architecture is inferred.
  evidence_ids:
  - record
  - thylakoid-agent-go
  - thylakoid-agent-SL0278
  - thylakoid-agent-SL0082
  - thylakoid-agent-SL0356
  - thylakoid-agent-perez2024-browser-introduction
  - thylakoid-agent-engel2015-jats-xml
  - thylakoid-agent-tax33090
  - thylakoid-agent-tax38254
  - thylakoid-agent-tax3055
- assessment_id: graph
  area: graph
  topic: Target-specific topology and function
  outcome: supported
  target_ids:
  - GO:0055035
  summary: Two NONMECHANISTIC edges state lumen enclosure and support for light-reaction
    complexes. The oxygenic GO0019684 process matches photosynthetic plastids; no
    complete stoichiometric pathway or molecular assembly sequence is claimed.
  evidence_ids:
  - record
  - thylakoid-agent-go
  - thylakoid-agent-SL0278
  - thylakoid-agent-SL0082
  - thylakoid-agent-SL0356
  - thylakoid-agent-perez2024-browser-introduction
  - thylakoid-agent-perez2024-browser-search
  - thylakoid-agent-engel2015-jats-xml
- assessment_id: coverage
  area: completeness
  topic: Entire record and bounded unresolved enrichment
  outcome: supported
  target_ids:
  - GO:0055035
  summary: Every field, evidence placement, graph node/edge, history and discussion
    was reviewed. No protein examples, image, direct quotation or quantitative dimensions
    are asserted. The label-only material task and absent optional molecular inventory
    do not create automatic findings. Historical source-access events are not judged
    false because newer access is available.
  evidence_ids:
  - record
  - schema
  - thylakoid-agent-go
  - thylakoid-agent-perez2024-browser-introduction
  - thylakoid-agent-engel2015-jats-xml
findings: []
actions: []
limitations:
- Unchanged imports preserve original source URL, UTC access time and raw SHA256.
  The Perez review was read only in the complete abstract and named browser-extracted
  Introduction/electron-transport passages; its native publisher response is403. Browser
  representations have status:null, not HTTP200 full-body receipts.
- Engel primary sections and Methods listed in the evidence were read directly; figure
  captions were read but pixels, videos, supplements and raw tomography were not reanalyzed.
  CC124 growth/imaging context is preserved; universal continuity, detailed biogenesis
  mechanisms and prevalence counts are not inferred.
- Individual molecular formation necessity, exact lipid species/ratios and exhaustive
  taxon-neutral protein inventories remain unknown. The collective boundary is distinguished
  from those individual requirements.
- UniProt SL0356 supports the organellar chromatophore membrane classification; the
  inspected GO response does not expose the corresponding direct GO0055035 is_a edge.
  No missing native edge is silently invented.
- All five fresh-base batch26 corpus gates and exact target resolver rows are integrated
  here; every manifested source input is identical at the shared base.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User explicitly requests one review for every unreviewed record; no maintained scientific
  or history edits were made.
- 'iModulonDB is not applicable: these records assert physical compartment topology
  and photosynthesis rather than expression-module membership.'
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
