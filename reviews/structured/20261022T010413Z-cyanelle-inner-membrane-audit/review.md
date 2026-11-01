# Cyanelle inner membrane identity, topology and evidence review

- Review: 20261022T010413Z-cyanelle-inner-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-21T11:20:59Z
- Finished UTC: 2026-10-22T01:04:13Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact GO/SL identity, synonym scope, two parents, envelope parthood, bilayer material and all three topology edges are supported. No concrete curation defect was established.

## Scope And Provenance

Full target review: identity, definition/source, category/kind, synonym, hierarchy, component class/essentiality/grounding, distribution, canonical example, all graph edges, evidence, open discussion and history.

Selection: Resumed user-authorized all-record pass; batch25 index6 or7, one distinct maintained cyanelle substructure reviewed in full.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 9c0446c4c0dd4b458787c43a499e4ceab5e179a6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036012 | data/structures/membrane_organelle/cyanelle_inner_membrane.yaml | maintained | cyanelle inner membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Native protein verify | passed | True | GO:0036012 | Native check passed; the target has no named protein examples or GENE_OR_PROTEIN nodes. |
| Native protein causal-graphs | passed | True | GO:0036012 | Native check passed; the target has no named protein examples or GENE_OR_PROTEIN nodes. |
| Focused native schema | passed | True | GO:0036012 | Focused validator passed. |
| Focused native strict | passed | True | GO:0036012 | Focused validator passed. |
| Target resolver slice | passed | True | GO:0036012 | 11 identifiers OK; 0 transport/skipped residuals independently resolved. |
| Claim-level scientific review | passed | True | GO:0036012 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Full corpus QC | passed | True | GO:0036012 | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0036012 | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0036012 | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0036012 | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| Strict identifier resolver command | passed | True | GO:0036012 | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Scientific And Domain Assessments

### Maintained source and neighboring structure boundaries

ownership: supported. Targets: GO:0036012.

The target remains a PROPOSED maintained record. Native capture includes all six neighboring cyanelle records whose boundaries informed this review. Prior history and TODO discussions are provenance, not new independent experimental evidence. Future scientific edits would require the guarded writer, curation/history events and regenerated products.

### Canonical model and qualitative glaucophyte scope

scope: supported. Targets: GO:0036012.

Both taxon labels match their issuing authority. COMMON is interpreted as the stated cyanelle structural organization in the named glaucophyte context, not a surveyed percentage or a claim that each cell at every stage has identical molecular composition. The Cyanophora canonical example is matched to the actual model study.

### Exact inner membrane, synonyms and parentage

identity: supported. Targets: GO:0036012.

GO:0036012 and SL-0480 identify the same stroma-facing inner envelope bilayer. The exact inner-envelope synonym matches GO. Both recorded is_a parents and envelope part_of are supported. IMS, whole envelope and thylakoids remain distinct identities.

### Lipid material class and essentiality

representation: supported. Targets: GO:0036012.

The component represents the collective lipid bilayer material constituting this membrane. ESSENTIAL is constitutional to the membrane identity, not a measured requirement for a particular lipid species or protein. The record does not substitute a whole-membrane GO term for a chemical identity. Label-only status and its explicit TODO honestly retain the missing narrower material grounding.

### All three topology edges

graph: supported. Targets: GO:0036012.

Inner-membrane parthood in the envelope and the stroma/IMS boundaries follow the exact GO definitions and SL-0480. Giddings envelope observations independently establish separate inner/outer membranes with an intervening layer. NONMECHANISTIC scope appropriately excludes import machinery, channel inventory and photosynthetic mechanisms.

### Ultrastructure versus biochemical context

evidence: supported. Targets: GO:0036012.

The Cyanophora distribution and canonical note are confined to the distinct inner/outer envelope membranes actually studied. Pfanzagl is contextual support for the intervening PG layer, not evidence for a specific inner-membrane protein or lipid composition. No obsolete endosymbiont-status claim is inferred from Giddings.

## Findings

No findings recorded within this review's declared scope.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/cyanelle_inner_membrane.yaml; Entire maintained YAML, including every evidence item, graph edge, discussion and history entry | context_only | Full target read. This YAML owns any future scientific correction; no generated source table overrides it. No maintained scientific content or status was changed. |
| neighbors | data/structures/membrane_organelle; Native-captured seven-record cyanelle boundary neighborhood | context_only | Ignored-inclusive rg -l --no-ignore --hidden search under data/structures for GO:0036012, GO:0036014 and cyanelle peptidoglycan layer returned the seven captured cyanelle, envelope, generic membrane, inner membrane, outer membrane, IMS and stroma records. The two targets and envelope/outer/generic/stroma neighbors were read fully; cyanelle identity, hierarchy, components and discussions were read for context. Only this target receives a full scientific review here. |
| cyanelle-boundary-agent-parents-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528,GO:0009529,GO:0033112,GO:0033113,GO:0036012,GO:0036013,GO:0036014,GO:0034060; Eight exact terms: IDs, labels, definitions, synonyms and relevant child/relation fields | supports | Current nonobsolete GO terms distinguish inner and outer envelope membranes, the intervening space, the complete envelope and stroma. GO:0036012 has the exact inner-envelope synonym; GO:0036014 has exact envelope-lumen and periplasm synonyms. Direct child edges establish plastid-inner and generic-cyanelle-membrane parentage for the inner membrane, plastid-IMS parentage for IMS, and IMS parthood in the envelope. |
| cyanelle-agent-SL-0480 | https://rest.uniprot.org/locations/SL-0480.json; Exact name, GO mapping, definition, isA and partOf fields, including nested parent context | supports | SL-0480 maps exactly to GO:0036012, defines separation of stroma from IMS, gives cyanelle-membrane and plastid-inner-membrane parents and cyanelle-envelope parthood. Its generic parent SL-0083 has a broader fallback annotation scope; that does not broaden this exact inner-membrane entry. |
| cyanelle-agent-tax2762 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762; taxId, scientificName, rank, lineage and taxonomic synonyms | supports | NCBI-derived ENA taxonomy verifies 2762 as Cyanophora paradoxa, rank species, with Glaucocystophyceae in its lineage. This identity response alone does not establish structural frequency. |
| cyanelle-agent-tax38254 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254; taxId, scientificName, rank, lineage and taxonomic synonyms | supports | NCBI-derived ENA taxonomy verifies 38254 as Glaucocystophyceae, rank class, and lists Glaucophyta and Glaucophyceae as synonyms. This identity response alone does not establish structural frequency. |
| cyanelle-agent-doi-10.1104_pp.71.2.409 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1104/pp.71.2.409%22; PMID16662839; complete indexed abstract and citation metadata; source scans assessed separately | supports | Giddings, Wasmann and Staehelin1983 exact DOI/PMID/title metadata and complete abstract describe Cyanophora envelope freeze-fracture observations: inner membrane, adjacent presumptive peptidoglycan and an external layer with outer-membrane-like fracture faces. The paper supplies ultrastructural evidence, not a modern taxonomic-status decision or molecular essentiality assay. |
| cyanelle-agent-doi-10.1128_jb.178.2.332-339.1996 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&amp;resultType=core&amp;query=DOI%3A%2210.1128/jb.178.2.332-339.1996%22; PMID8550450; complete indexed abstract and citation metadata, not a claim to have read the scanned full paper | supports | Pfanzagl et al.1996 exact DOI/PMID/title and complete abstract characterize Cyanophora cyanelle peptidoglycan by muropeptide separation and mass spectrometry, including a chemical modification. This supports biochemical identification of envelope peptidoglycan; no detailed numerical composition or assembly requirement is imported into the target. |
| cyanelle-agent-giddings1983-page414 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/9d4d067999da/plntphys00558-0208.png; Original published page 414 PNG linked from PMC1066046; relevant envelope body paragraphs and captions directly visually read. No measurement or image-analysis re-estimation. | supports | Envelope Membranes Results identify an inner membrane and intervening wall-like layer in sections/fracture images. The caption identifies the inner envelope fracture face and cleavage-furrow wall layer. |
| cyanelle-agent-giddings1983-page416 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png; Original published page 416 PNG linked from PMC1066046; relevant envelope body paragraphs and captions directly visually read. No measurement or image-analysis re-estimation. | supports | Continuation of Envelope Membranes Results describes inner-adjacent presumptive peptidoglycan and E/P fracture faces of an outer membrane exterior to it, including outer-membrane lifting and exposure of the underlying layer. |
| cyanelle-agent-giddings1983-page417 | https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png; Original published page 417 PNG linked from PMC1066046; relevant envelope body paragraphs and captions directly visually read. No measurement or image-analysis re-estimation. | supports | Envelope Discussion separates the inner envelope membrane from thylakoids and interprets the exterior fracture plane as outer membrane. Fig16–18 captions identify inner/outer surfaces and PG exposure. Historical speculation about cyanelles being organelles versus endosymbionts is not adopted. |
| native-verify | /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml --verify; Original focused output for this exact target | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| native-causal-graphs | /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml --causal-graphs; Original focused output for this exact target | supports | causal_graphs GENE_OR_PROTEIN node summary:<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     0  total GENE_OR_PROTEIN causal nodes |
| cyanelle-boundary-agent-inner-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036012/ancestors?relations=is_a,part_of; GO:0036012 ancestry with relations=is_a,part_of | supports | The current GO mixed is_a/part_of closure contains plastid inner membrane, cyanelle membrane and cyanelle envelope. Relation types are separately checked against direct term edges and exact SL hierarchy; a mixed closure alone is not treated as a direct is_a assertion. |
| schema-result | just validate data/structures/membrane_organelle/cyanelle_inner_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/cyanelle_inner_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/cyanelle_inner_membrane.yaml --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_inner_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/cyanelle_inner_membrane.yaml --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_inner_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_inner_membrane-strict.tsv |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/cyanelle_inner_membrane.yaml; exact collect() scope; hash identifies the entire original resolver TSV | supports | 11 of11 collected target identifiers returned OK in this fresh base resolver run. Residuals: none. Source-native identity checked separately. |
| global-qc-result | just qc; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82 | supports | Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0 | supports | Exit 0. All 1828 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26 | supports | Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad | supports | Exit 0. Ten links checked against the 1130-entry trait index; zero missing or mislabelled links. |
| global-curies-result | just check-curies-strict; Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256 below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d | supports | Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE. Transport failures and skipped prefixes are not evidence of resolution. Exact target identifiers are assessed separately in this review. |

## Limits And Additional Notes

- Full coverage applies to the complete maintained target, not a systematic audit of every glaucophyte lineage or every envelope molecule. The named model and comparative studies do not establish numerical prevalence.
- Giddings1983 envelope Results/Discussion were read directly on original page scans414,416,417, with OCR context on409,410,412. This is not a claim of reading every page or independently remeasuring its micrographs. The historical endosymbiont-versus-organelle interpretation is not imported.
- Pfanzagl1996 primary-structure evidence was read as its complete indexed/PMC abstract; public HTML landing pages and challenged PDF requests are not full body text. No detailed glycan values, monomer counts or protein necessities were inferred from the abstract.
- No snippets, images, physical-property quantities, trait links, protein examples or GENE_OR_PROTEIN nodes occur in this target. Their absence does not require inventing a molecular inventory for this topology review.
- Existing label-only component-grounding TODOs remain open. No exact chemical or structural identifier is guessed, and no source response proves global absence of alternative ontology terms.
- Focused native checks and the exact current-base resolver slice are recorded. Root owns batch-wide final gates and immutable persistence; this author supplies unsaved drafts only.
- Shared corpus gates have bounded coverage: 617 label checks had no adapter; the identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific biological findings or proof that all corpus identifiers resolve.
- Only the review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T010413Z-cyanelle-inner-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Cyanelle inner membrane identity, topology and evidence review
started_at: '2026-10-21T11:20:59Z'
finished_at: '2026-10-22T01:04:13Z'
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
summary: Exact GO/SL identity, synonym scope, two parents, envelope parthood, bilayer
  material and all three topology edges are supported. No concrete curation defect
  was established.
source:
  git_revision: 9c0446c4c0dd4b458787c43a499e4ceab5e179a6
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
  - path: data/structures/membrane_organelle/cyanelle.yaml
    sha256: 24275c8050ca5d13c66d563c7aa697a4de65766f87499f876fc94c41cd2f0db7
    role: context
  - path: data/structures/membrane_organelle/cyanelle_envelope.yaml
    sha256: 4a25594b3a26541401976d3ab78f271bc8726951462af9073fafc0eff2389a67
    role: context
  - path: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    sha256: f10bb4f3ff44fb6d0b23e67379861768a590eb6d3da75686e296a0a5b3b26970
    role: target
  - path: data/structures/membrane_organelle/cyanelle_intermembrane_space.yaml
    sha256: aba8ad62f544ec82bea2f4767a8c79cc45d3fe117423163fc1ce1211a2527f8c
    role: context
  - path: data/structures/membrane_organelle/cyanelle_membrane.yaml
    sha256: b95c9fcb293bd9f434df3ccf9ecaa7c9bf04e1f83a95a2cd19673441a537a20b
    role: context
  - path: data/structures/membrane_organelle/cyanelle_outer_membrane.yaml
    sha256: 2f058b25ce3bf1b49d52bc03391ee46d6e26376860035469f037d27c52234047
    role: context
  - path: data/structures/membrane_organelle/cyanelle_stroma.yaml
    sha256: 13d83e3dadca9cafaa6550a7bf84cd8066bf1539ccaacd3627ec23aa5b08e118
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
- target_id: GO:0036012
  path: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  label: cyanelle inner membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    role: maintained scientific record
scope:
  description: 'Full target review: identity, definition/source, category/kind, synonym,
    hierarchy, component class/essentiality/grounding, distribution, canonical example,
    all graph edges, evidence, open discussion and history.'
  selection: Resumed user-authorized all-record pass; batch25 index6 or7, one distinct
    maintained cyanelle substructure reviewed in full.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0036012
checks:
- check_id: native-verify
  name: Native protein verify
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --verify
  exit_code: 0
  summary: Native check passed; the target has no named protein examples or GENE_OR_PROTEIN
    nodes.
  evidence_ids:
  - native-verify
- check_id: native-causal-graphs
  name: Native protein causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --causal-graphs
  exit_code: 0
  summary: Native check passed; the target has no named protein examples or GENE_OR_PROTEIN
    nodes.
  evidence_ids:
  - native-causal-graphs
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just validate data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just validate-strict data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_inner_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: target-curies
  name: Target resolver slice
  status: passed
  required: true
  target_ids:
  - GO:0036012
  summary: 11 identifiers OK; 0 transport/skipped residuals independently resolved.
  evidence_ids:
  - target-curies
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0036012
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - neighbors
  - cyanelle-boundary-agent-parents-go
  - cyanelle-agent-SL-0480
  - cyanelle-agent-tax2762
  - cyanelle-agent-tax38254
  - cyanelle-agent-doi-10.1104_pp.71.2.409
  - cyanelle-agent-doi-10.1128_jb.178.2.332-339.1996
  - cyanelle-agent-giddings1983-page414
  - cyanelle-agent-giddings1983-page416
  - cyanelle-agent-giddings1983-page417
  - cyanelle-boundary-agent-inner-ancestors
- check_id: global-qc
  name: Full corpus QC
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just qc
  exit_code: 0
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:12:21Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-qc-result
- check_id: global-history
  name: Repository history validation
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just validate-history
  exit_code: 0
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:53Z to
    2026-10-21T09:05:00Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-history-result
- check_id: global-products
  name: Controlled vocabulary label validation
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just validate-products
  exit_code: 0
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:46Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-products-result
- check_id: global-traits
  name: Trait reference validation
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just check-trait-links --check
  exit_code: 0
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:05:06Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-traits-result
- check_id: global-curies
  name: Strict identifier resolver command
  status: passed
  required: true
  target_ids:
  - GO:0036012
  command: just check-curies-strict
  exit_code: 0
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  scope_note: Full-corpus-only documented recipe, executed 2026-10-21T09:04:57Z to
    2026-10-21T09:45:43Z at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6. Executed in
    the fresh batch15 isolated checkout; any reuse is restricted to this identical
    base commit and unchanged maintained scientific inputs. This does not scientifically
    review non-target records.
  evidence_ids:
  - global-curies-result
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  locator: Entire maintained YAML, including every evidence item, graph edge, discussion
    and history entry
  accessed_at: '2026-10-22T00:55:16Z'
  support: context_only
  summary: Full target read. This YAML owns any future scientific correction; no generated
    source table overrides it. No maintained scientific content or status was changed.
- evidence_id: neighbors
  kind: record_content
  reference: data/structures/membrane_organelle
  locator: Native-captured seven-record cyanelle boundary neighborhood
  accessed_at: '2026-10-22T00:55:16Z'
  support: context_only
  summary: Ignored-inclusive rg -l --no-ignore --hidden search under data/structures
    for GO:0036012, GO:0036014 and cyanelle peptidoglycan layer returned the seven
    captured cyanelle, envelope, generic membrane, inner membrane, outer membrane,
    IMS and stroma records. The two targets and envelope/outer/generic/stroma neighbors
    were read fully; cyanelle identity, hierarchy, components and discussions were
    read for context. Only this target receives a full scientific review here.
- evidence_id: cyanelle-boundary-agent-parents-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009528,GO:0009529,GO:0033112,GO:0033113,GO:0036012,GO:0036013,GO:0036014,GO:0034060
  locator: 'Eight exact terms: IDs, labels, definitions, synonyms and relevant child/relation
    fields'
  accessed_at: '2026-10-22T00:53:18.483919Z'
  support: supports
  summary: Current nonobsolete GO terms distinguish inner and outer envelope membranes,
    the intervening space, the complete envelope and stroma. GO:0036012 has the exact
    inner-envelope synonym; GO:0036014 has exact envelope-lumen and periplasm synonyms.
    Direct child edges establish plastid-inner and generic-cyanelle-membrane parentage
    for the inner membrane, plastid-IMS parentage for IMS, and IMS parthood in the
    envelope.
  snapshot_sha256: 17a3ecbb85b1dba2def413e4918522db12758d85c4354f0cc3c8cfa00814c808
- evidence_id: cyanelle-agent-SL-0480
  kind: authority
  reference: https://rest.uniprot.org/locations/SL-0480.json
  locator: Exact name, GO mapping, definition, isA and partOf fields, including nested
    parent context
  accessed_at: '2026-10-21T11:21:45.924932Z'
  support: supports
  summary: SL-0480 maps exactly to GO:0036012, defines separation of stroma from IMS,
    gives cyanelle-membrane and plastid-inner-membrane parents and cyanelle-envelope
    parthood. Its generic parent SL-0083 has a broader fallback annotation scope;
    that does not broaden this exact inner-membrane entry.
  snapshot_sha256: b91c540680ba95ebee76012cbfcb23234f3ef6df3427a70bb85fcadd801933e9
- evidence_id: cyanelle-agent-tax2762
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2762
  locator: taxId, scientificName, rank, lineage and taxonomic synonyms
  accessed_at: '2026-10-21T11:21:45.924999Z'
  support: supports
  summary: NCBI-derived ENA taxonomy verifies 2762 as Cyanophora paradoxa, rank species,
    with Glaucocystophyceae in its lineage. This identity response alone does not
    establish structural frequency.
  snapshot_sha256: 285d213ba479ce1d232bf54aac3efda6f16d45546b5ce13284818fc16482408a
- evidence_id: cyanelle-agent-tax38254
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/38254
  locator: taxId, scientificName, rank, lineage and taxonomic synonyms
  accessed_at: '2026-10-21T11:21:46.530610Z'
  support: supports
  summary: NCBI-derived ENA taxonomy verifies 38254 as Glaucocystophyceae, rank class,
    and lists Glaucophyta and Glaucophyceae as synonyms. This identity response alone
    does not establish structural frequency.
  snapshot_sha256: 4b487eb0e34bcb4941fbb315aae5214c96ea6f60255d71a2aca172cd35844009
- evidence_id: cyanelle-agent-doi-10.1104_pp.71.2.409
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1104/pp.71.2.409%22
  locator: PMID16662839; complete indexed abstract and citation metadata; source scans
    assessed separately
  accessed_at: '2026-10-21T11:21:14.649813Z'
  support: supports
  summary: 'Giddings, Wasmann and Staehelin1983 exact DOI/PMID/title metadata and
    complete abstract describe Cyanophora envelope freeze-fracture observations: inner
    membrane, adjacent presumptive peptidoglycan and an external layer with outer-membrane-like
    fracture faces. The paper supplies ultrastructural evidence, not a modern taxonomic-status
    decision or molecular essentiality assay.'
  snapshot_sha256: 63e06e7891bc1f0bf83152a34ce823faa160c98bf984757e546f4acb00f202dc
- evidence_id: cyanelle-agent-doi-10.1128_jb.178.2.332-339.1996
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?format=json&resultType=core&query=DOI%3A%2210.1128/jb.178.2.332-339.1996%22
  locator: PMID8550450; complete indexed abstract and citation metadata, not a claim
    to have read the scanned full paper
  accessed_at: '2026-10-21T11:21:15.265478Z'
  support: supports
  summary: Pfanzagl et al.1996 exact DOI/PMID/title and complete abstract characterize
    Cyanophora cyanelle peptidoglycan by muropeptide separation and mass spectrometry,
    including a chemical modification. This supports biochemical identification of
    envelope peptidoglycan; no detailed numerical composition or assembly requirement
    is imported into the target.
  snapshot_sha256: 1f192e6160692da29293cf7e4a716b43fafe82d4c880157bed2a9a265ff1bd4a
- evidence_id: cyanelle-agent-giddings1983-page414
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/9d4d067999da/plntphys00558-0208.png
  locator: Original published page 414 PNG linked from PMC1066046; relevant envelope
    body paragraphs and captions directly visually read. No measurement or image-analysis
    re-estimation.
  accessed_at: '2026-10-22T00:53:33.927250Z'
  support: supports
  summary: Envelope Membranes Results identify an inner membrane and intervening wall-like
    layer in sections/fracture images. The caption identifies the inner envelope fracture
    face and cleavage-furrow wall layer.
  snapshot_sha256: 331f5f9fdd4e16e2a8cb67d9b5d45cca5467dc6554051cfa6696e34471e7bb82
- evidence_id: cyanelle-agent-giddings1983-page416
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/c329334d81e0/plntphys00558-0210.png
  locator: Original published page 416 PNG linked from PMC1066046; relevant envelope
    body paragraphs and captions directly visually read. No measurement or image-analysis
    re-estimation.
  accessed_at: '2026-10-22T00:53:34.247595Z'
  support: supports
  summary: Continuation of Envelope Membranes Results describes inner-adjacent presumptive
    peptidoglycan and E/P fracture faces of an outer membrane exterior to it, including
    outer-membrane lifting and exposure of the underlying layer.
  snapshot_sha256: 41f820c6bde6abc4318ac32baa45293634543bb4aceb0dc5129c3d25414e91ef
- evidence_id: cyanelle-agent-giddings1983-page417
  kind: primary_source
  reference: https://cdn.ncbi.nlm.nih.gov/pmc/blobs/4b1e/1066046/7694ed6a7a74/plntphys00558-0211.png
  locator: Original published page 417 PNG linked from PMC1066046; relevant envelope
    body paragraphs and captions directly visually read. No measurement or image-analysis
    re-estimation.
  accessed_at: '2026-10-22T00:53:34.248245Z'
  support: supports
  summary: Envelope Discussion separates the inner envelope membrane from thylakoids
    and interprets the exterior fracture plane as outer membrane. Fig16–18 captions
    identify inner/outer surfaces and PG exposure. Historical speculation about cyanelles
    being organelles versus endosymbionts is not adopted.
  snapshot_sha256: 276c1cb60d1a909200199f8e24495840d2caa5f5131c8a896d3f97d70e5bcf6f
- evidence_id: native-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --verify
  locator: Original focused output for this exact target
  accessed_at: '2026-10-22T00:53:25.806952Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: native-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/.venv/bin/python
    -B scripts/uniprot_genes.py --record data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --causal-graphs
  locator: Original focused output for this exact target
  accessed_at: '2026-10-22T00:53:26.217867Z'
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
- evidence_id: cyanelle-boundary-agent-inner-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0036012/ancestors?relations=is_a,part_of
  locator: GO:0036012 ancestry with relations=is_a,part_of
  accessed_at: '2026-10-22T00:53:19.700170Z'
  support: supports
  summary: The current GO mixed is_a/part_of closure contains plastid inner membrane,
    cyanelle membrane and cyanelle envelope. Relation types are separately checked
    against direct term edges and exact SL hierarchy; a mixed closure alone is not
    treated as a direct is_a assertion.
  snapshot_sha256: beaaffd44656b78e9eb06b4db38854596f6d9bbc0fb557510a957ad7d921bd2f
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:21:03Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/cyanelle_inner_membrane.yaml'
  snapshot_sha256: 91232b67cb2f2060d83cae6cae1096b9c5674a6c5d726e04243117ac961aee2e
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/cyanelle_inner_membrane.yaml
    --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_inner_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-21T11:21:04Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/cyanelle_inner_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_inner_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch25-20261021-9wf9f0wd/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch25-20261021-9wf9f0wd/cyanelle_inner_membrane-strict.tsv"
  snapshot_sha256: 22fad4216c044cbef85b61b84873641c8ef6a48ccb7bb55c79e03360c921fa82
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/cyanelle_inner_membrane.yaml; exact
    collect() scope; hash identifies the entire original resolver TSV
  accessed_at: '2026-10-22T00:55:16Z'
  support: supports
  summary: '11 of11 collected target identifiers returned OK in this fresh base resolver
    run. Residuals: none. Source-native identity checked separately.'
  snapshot_sha256: d428d95fd13ac608f3786bcf74a032c768ac80e494b9673013e1e4d27de9ad66
- evidence_id: global-qc-result
  kind: validation
  reference: just qc
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 446dedbdf9d57d9a70b17a09a657b6aba2019ac5dd329007cfeb48bcb7d0bc82
  accessed_at: '2026-10-21T09:12:21Z'
  support: supports
  summary: 'Exit 0. Native QC passed: 1025 tests passed and 3 skipped, history, strict
    schema, generated-site consistency and corpus-report stages.'
  snapshot_sha256: 2cf77f0998cf42f98e103ee00a0f23cd610d5fcfd4814d7438d3e76bc9ef3d6d
- evidence_id: global-history-result
  kind: validation
  reference: just validate-history
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0
  accessed_at: '2026-10-21T09:05:00Z'
  support: supports
  summary: Exit 0. All 1828 history records validated; URI precheck reported zero
    invalid references.
  snapshot_sha256: 793664cc55dee807ad6725ace8cbdeb817e07c968f017af7ab0b5183a67b3df0
- evidence_id: global-products-result
  kind: validation
  reference: just validate-products
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26
  accessed_at: '2026-10-21T09:05:46Z'
  support: supports
  summary: 'Exit 0. Label results: 3952 canonical, 50 synonym, 6 exception and 617
    SKIPPED_NO_ADAPTER. Skips are not successful authority verification.'
  snapshot_sha256: dd07915effbb88aa88c56f6c102542b3cea4d9c70f381d943a664796a79c6917
- evidence_id: global-traits-result
  kind: validation
  reference: just check-trait-links --check
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad
  accessed_at: '2026-10-21T09:05:06Z'
  support: supports
  summary: Exit 0. Ten links checked against the 1130-entry trait index; zero missing
    or mislabelled links.
  snapshot_sha256: 6eab64b59433928ec8e0df9b0046dbccf479c84bb0911c315feebc344d536007
- evidence_id: global-curies-result
  kind: validation
  reference: just check-curies-strict
  locator: Full-corpus run at 9c0446c4c0dd4b458787c43a499e4ceab5e179a6; stdout SHA-256
    below, stderr SHA-256 896496da9422a4ccb4c14c2d29e2ed257c78edf6a3177f5c0fda61f1ff9b9f4d
  accessed_at: '2026-10-21T09:45:43Z'
  support: supports
  summary: Exit 0. Resolver controls passed; 4849 OK, 252 SKIPPED, 821 UNREACHABLE.
    Transport failures and skipped prefixes are not evidence of resolution. Exact
    target identifiers are assessed separately in this review.
  snapshot_sha256: 4b17ccc07b33ceab3eeb8631b1cf075f5f750c5a6f4820455b1930e3aa165286
assessments:
- assessment_id: ownership
  area: ownership
  topic: Maintained source and neighboring structure boundaries
  outcome: supported
  target_ids:
  - GO:0036012
  summary: The target remains a PROPOSED maintained record. Native capture includes
    all six neighboring cyanelle records whose boundaries informed this review. Prior
    history and TODO discussions are provenance, not new independent experimental
    evidence. Future scientific edits would require the guarded writer, curation/history
    events and regenerated products.
  evidence_ids:
  - record
  - neighbors
- assessment_id: taxa
  area: scope
  topic: Canonical model and qualitative glaucophyte scope
  outcome: supported
  target_ids:
  - GO:0036012
  summary: Both taxon labels match their issuing authority. COMMON is interpreted
    as the stated cyanelle structural organization in the named glaucophyte context,
    not a surveyed percentage or a claim that each cell at every stage has identical
    molecular composition. The Cyanophora canonical example is matched to the actual
    model study.
  evidence_ids:
  - cyanelle-agent-tax2762
  - cyanelle-agent-tax38254
  - cyanelle-agent-doi-10.1104_pp.71.2.409
  - cyanelle-agent-doi-10.1128_jb.178.2.332-339.1996
- assessment_id: identity
  area: identity
  topic: Exact inner membrane, synonyms and parentage
  outcome: supported
  target_ids:
  - GO:0036012
  summary: GO:0036012 and SL-0480 identify the same stroma-facing inner envelope bilayer.
    The exact inner-envelope synonym matches GO. Both recorded is_a parents and envelope
    part_of are supported. IMS, whole envelope and thylakoids remain distinct identities.
  evidence_ids:
  - cyanelle-boundary-agent-parents-go
  - cyanelle-agent-SL-0480
  - cyanelle-boundary-agent-inner-ancestors
  - record
  - neighbors
- assessment_id: component
  area: representation
  topic: Lipid material class and essentiality
  outcome: supported
  target_ids:
  - GO:0036012
  summary: The component represents the collective lipid bilayer material constituting
    this membrane. ESSENTIAL is constitutional to the membrane identity, not a measured
    requirement for a particular lipid species or protein. The record does not substitute
    a whole-membrane GO term for a chemical identity. Label-only status and its explicit
    TODO honestly retain the missing narrower material grounding.
  evidence_ids:
  - cyanelle-boundary-agent-parents-go
  - cyanelle-agent-SL-0480
  - record
- assessment_id: graph
  area: graph
  topic: All three topology edges
  outcome: supported
  target_ids:
  - GO:0036012
  summary: Inner-membrane parthood in the envelope and the stroma/IMS boundaries follow
    the exact GO definitions and SL-0480. Giddings envelope observations independently
    establish separate inner/outer membranes with an intervening layer. NONMECHANISTIC
    scope appropriately excludes import machinery, channel inventory and photosynthetic
    mechanisms.
  evidence_ids:
  - cyanelle-boundary-agent-parents-go
  - cyanelle-agent-SL-0480
  - cyanelle-agent-doi-10.1104_pp.71.2.409
  - cyanelle-agent-giddings1983-page414
  - cyanelle-agent-giddings1983-page416
  - cyanelle-agent-giddings1983-page417
  - record
- assessment_id: sources
  area: evidence
  topic: Ultrastructure versus biochemical context
  outcome: supported
  target_ids:
  - GO:0036012
  summary: The Cyanophora distribution and canonical note are confined to the distinct
    inner/outer envelope membranes actually studied. Pfanzagl is contextual support
    for the intervening PG layer, not evidence for a specific inner-membrane protein
    or lipid composition. No obsolete endosymbiont-status claim is inferred from Giddings.
  evidence_ids:
  - cyanelle-agent-doi-10.1104_pp.71.2.409
  - cyanelle-agent-doi-10.1128_jb.178.2.332-339.1996
  - cyanelle-agent-giddings1983-page414
  - cyanelle-agent-giddings1983-page416
  - cyanelle-agent-giddings1983-page417
  - cyanelle-agent-tax2762
  - cyanelle-agent-tax38254
findings: []
actions: []
limitations:
- Full coverage applies to the complete maintained target, not a systematic audit
  of every glaucophyte lineage or every envelope molecule. The named model and comparative
  studies do not establish numerical prevalence.
- Giddings1983 envelope Results/Discussion were read directly on original page scans414,416,417,
  with OCR context on409,410,412. This is not a claim of reading every page or independently
  remeasuring its micrographs. The historical endosymbiont-versus-organelle interpretation
  is not imported.
- Pfanzagl1996 primary-structure evidence was read as its complete indexed/PMC abstract;
  public HTML landing pages and challenged PDF requests are not full body text. No
  detailed glycan values, monomer counts or protein necessities were inferred from
  the abstract.
- No snippets, images, physical-property quantities, trait links, protein examples
  or GENE_OR_PROTEIN nodes occur in this target. Their absence does not require inventing
  a molecular inventory for this topology review.
- Existing label-only component-grounding TODOs remain open. No exact chemical or
  structural identifier is guessed, and no source response proves global absence of
  alternative ontology terms.
- Focused native checks and the exact current-base resolver slice are recorded. Root
  owns batch-wide final gates and immutable persistence; this author supplies unsaved
  drafts only.
- 'Shared corpus gates have bounded coverage: 617 label checks had no adapter; the
  identifier command reported 252 SKIPPED, 821 UNREACHABLE. These totals are not target-specific
  biological findings or proof that all corpus identifiers resolve.'
notes:
- Only the review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
```
