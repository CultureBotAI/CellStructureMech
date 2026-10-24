# Nuclear outer membrane scientific review

- Review: 20261022T025109Z-nuclear-outer-membrane-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-22T02:36:35Z
- Finished UTC: 2026-10-22T02:51:09Z
- Reviewer: Codex (unknown)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

The outer nuclear-membrane identity, label-only lipid material, source-scoped yeast function and verified protein references are supported. One minor finding concerns the OPEN discussion rationale that still treats existing verified accession links as pending.

## Scope And Provenance

Entire target within the four-record nuclear-envelope boundary set (target plus three neighbors); definitions, hierarchy, components, taxon/examples, functions, every directed edge, discussions, exact authorities and declared source body/supplement scopes.

Selection: Batch35 target 7; exact native inspection and focused schema/strict gates passed before assessment at unchanged f97b1abe.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base f97b1abe2d78971b6f66b9083087d7a94cf3c0cc.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0005640 | data/structures/membrane_organelle/nuclear_outer_membrane.yaml | maintained | nuclear outer membrane |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Focused native schema | passed | True | GO:0005640 | Focused validator passed. |
| Focused native strict | passed | True | GO:0005640 | Focused validator passed. |
| Expression-module applicability | not_applicable | False | GO:0005640 | No computational expression-module assertion is made; experimental gene interventions do not require expression-module evidence. |
| Native verify | passed | True | GO:0005640 | Read-only check passed; diagnostic coverage is assessed separately. |
| Native causal-graphs | passed | True | GO:0005640 | Read-only check passed; diagnostic coverage is assessed separately. |
| Claim-level scientific review | passed | True | GO:0005640 | All required claim-level inspections completed; findings and scope limitations are recorded separately. |
| Exact target resolver slice with scoped native residual resolution | passed | True | GO:0005640 | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| Full corpus QC | passed | True | GO:0005640 | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| Repository history validation | passed | True | GO:0005640 | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| Controlled vocabulary label validation | passed | True | GO:0005640 | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| Trait reference validation | passed | True | GO:0005640 | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| Strict identifier resolver command | passed | True | GO:0005640 | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Scientific And Domain Assessments

### Distinct outer nuclear membrane

identity: supported. Targets: GO:0005640.

The exact native definition, maintained synonym, nuclear-envelope parthood and organelle-membrane ancestry agree. The paired bilayer and intervening lumen remain distinct topology nodes, as stated by the resolved boundary discussion.

### Collective label-only lipid material

grounding: supported. Targets: GO:0005640.

The reviewed-label-only bilayer row has no whole-membrane GO chemical grounding. Its graph component_ref can identify constituting material without claiming exact chemical equivalence. Optional source-neutral lipid chemistry remains unresolved; no forced protein inventory is inferred.

### Individual molecular formation requirements unresolved

evidence: unknown. Targets: GO:0005640.

The collective bilayer is constitutive of this membrane. ESSENTIAL does not establish which individual lipid classes or proteins are required for membrane formation; the inspected targeting/contact studies do not test those global formation requirements.

### Yeast contact function and six coarse edges

graph: supported. Targets: GO:0005640.

The topology, Nvj1 localization, Vac8 vacuolar localization and interaction edges agree with Pan. The source combines binding/localization and perturbation evidence and interprets contact formation as mediated by the pair; its acknowledged remote indirect-binding possibility is retained as an assay limit. This does not imply either partner forms the entire outer membrane.

### Exact reference instances

grounding: supported. Targets: GO:0005640.

P38881 identifies NVJ1/YHR195W and P39968 identifies VAC8/YEL013W in reviewed S288C entries. They corroborate the named actors but do not recast the primary YEF473/L40 experimental backgrounds as S288C.

### Qualitative budding-yeast model

scope: supported. Targets: GO:0005640.

Species4932 is correct and the primary study establishes the named targeting/contact example. Reference accessions are not a claim that every experiment used S288C; COMMON is qualitative and supplies no universal percentage.

### Stale unresolved accession-verification rationale

provenance: concern. Targets: GO:0005640.

The OPEN discussion says protein nodes are left ungrounded until exact UniProt or family identifiers can be verified, but current node xrefs and the October history already record this accession work. The rationale should acknowledge verified instances and separate any genuinely remaining family or grouped-actor coverage rather than present all nodes as unverified.

### Source tier, currentness and review limits

evidence: supported. Targets: GO:0005640.

All target citation identities and native term/protein identities were checked. Relevant primary or review body passages were read within the declared locators. Historical discussions are interpreted in their recorded context, with only concrete current contradictions flagged. No scientific promotion or corpus edit is implied.

## Findings

### F1: Update the open protein-grounding rationale to acknowledge verified xrefs

minor / open / confirmed; issue key: nuclear-outer-membrane-stale-protein-grounding-rationale.

The rationale says the named protein nodes are left ungrounded until exact UniProt or family identifiers can be verified. Current graph nodes already carry verified accessions, and the October curation event records their addition. The remaining task needs to distinguish completed instance verification from any unresolved family or grouped-actor coverage.

## Recommended Actions And Acceptance Checks

### A1

Update discussion ground_nvj1p_and_vac8p to acknowledge the verified accession links and preserve its historical context. Retain OPEN only for a specifically stated remaining task; otherwise resolve the completed accession-verification subtask. Preserve correct xrefs and source-specific protein roles.

- The rationale no longer says all named nodes await UniProt verification when those links are already present.
- Any retained OPEN scope names an actual remaining task and does not imply that one representative accession identifies every member of a grouped system.
- Native schema, strict, read-only protein verification and history checks pass after authorized curation.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/membrane_organelle/nuclear_outer_membrane.yaml; Entire maintained YAML, including history, evidence, all directed edges and discussions | context_only | The complete target was independently read. Maintained scientific content and status remain unchanged. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml; StructuralComponent lines391–444; CausalNode lines843–875; component types1044–1057 | context_only | Molecular lipid identity differs from a complete membrane. GO can ground a protein subcomplex; CHEBI is the stated lipid grounding route. Essentiality denotes formation necessity. Node xrefs can link instances without claiming complete cohort coverage. |
| neighbor-nuclear_envelope | data/structures/membrane_organelle/nuclear_envelope.yaml; Complete maintained nuclear-envelope boundary neighbor | context_only | Exact adjacent record read and frozen for topology and representation context; maintained context is not independent experimental evidence. |
| neighbor-nuclear_envelope_lumen | data/structures/membrane_organelle/nuclear_envelope_lumen.yaml; Complete maintained nuclear-envelope boundary neighbor | context_only | Exact adjacent record read and frozen for topology and representation context; maintained context is not independent experimental evidence. |
| neighbor-nuclear_inner_membrane | data/structures/membrane_organelle/nuclear_inner_membrane.yaml; Complete maintained nuclear-envelope boundary neighbor | context_only | Exact adjacent record read and frozen for topology and representation context; maintained context is not independent experimental evidence. |
| nuclear-agent-go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005635,GO%3A0031967,GO%3A0005634,GO%3A0005637,GO%3A0005640,GO%3A0005641,GO%3A0005643,GO%3A0006913,GO%3A0006998,GO%3A0031970,GO%3A0005788,GO%3A0031090,GO%3A0005774; Complete13 requested native term results: exact IDs, definitions, synonyms, active flags and returned child relations | supports | All13 active native terms were inspected. The definitions distinguish envelope, nucleus, inner/outer bilayers, perinuclear lumen, NPC, ER lumen and vacuolar membrane. Returned children directly support envelope is_a organelle envelope, lumen is_a organelle envelope lumen, and envelope part_of nucleus. GO0005635 exactly supplies the maintained definition, including its20–40nm range and lamina clause; this is ontology wording, not a new universal measurement. |
| nuclear-agent-membrane-ancestors | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005637,GO%3A0005640/ancestors?relations=is_a; Exact relations=is_a ancestor lists for GO0005637 and GO0005640 | supports | The is_a-only ancestor response places both nuclear membrane terms below GO0031090 organelle membrane. It establishes ancestry, not necessarily an immediate parent edge. |
| nuclear-agent-tax4932 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932; Complete taxId, scientificName, rank and available lineage fields | supports | ENA confirms Saccharomyces cerevisiae4932 at species rank; this is not an experimental-strain attestation. |
| nuclear-agent-tax559292 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292; Complete taxId, scientificName, rank and available lineage fields | supports | ENA confirms Saccharomyces cerevisiae S288C559292 at strain rank, matching the protein reference entries; it is distinguished from the primary experimental backgrounds. |
| nuclear-agent-pan2000-meta | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&amp;format=json&amp;resultType=core; Unique MED result and complete abstract | supports | Exact DOI10.1091/mbc.11.7.2445/PMID10888680 authors/year/title and full abstract match the genuine primary body. |
| nuclear-agent-pan2000-pmc | https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/; PMC14931 Methods sec3–6,9; all Results sec11–17 and Discussion sec18 with embedded Figure1–9 captions. No image pixels or unlisted Methods inspected. | supports | Primary yeast study supports Nvj1 on the nuclear envelope, Vac8 on the vacuole and their role in contact formation using localization, two-hybrid, copurification, deletion/overexpression and thin-section TEM. It infers direct interaction while explicitly retaining a remote indirect-binding possibility. Methods use YEF473 backgrounds and L40, not a stated S288C experiment. Neither protein is thereby necessary for formation of the entire nuclear membrane. |
| nuclear-agent-protein-P38881 | https://rest.uniprot.org/uniprotkb/P38881.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Native primary accession P38881 identifies reviewed NVJ1/YHR195W in S288C559292. Gene/locus tokens, entry status and relevant location/interaction comments were read. This verifies this reference instance; the cited primary experiment supplies biological role and experimental background. |
| nuclear-agent-protein-P39968 | https://rest.uniprot.org/uniprotkb/P39968.json; primaryAccession, entryType, proteinDescription, genes, organism; relevant FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments | supports | Native primary accession P39968 identifies reviewed VAC8/YEL013W in S288C559292. Gene/locus tokens, entry status and relevant location/interaction comments were read. This verifies this reference instance; the cited primary experiment supplies biological role and experimental background. |
| schema-result | just validate data/structures/membrane_organelle/nuclear_outer_membrane.yaml; Captured focused validator log | supports | No issues found<br>uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml --target-class CellStructureRecord data/structures/membrane_organelle/nuclear_outer_membrane.yaml |
| strict-result | just validate-strict data/structures/membrane_organelle/nuclear_outer_membrane.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_outer_membrane-strict.tsv; Captured focused validator log | supports | uv run python scripts/validate_strict.py data/structures/membrane_organelle/nuclear_outer_membrane.yaml --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_outer_membrane-strict.tsv<br>Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml<br><br>=== validate-strict summary ===<br>  files scanned:      1<br>  files with ERROR:   0<br>  total ERROR rows:   0<br>  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_outer_membrane-strict.tsv |
| outer-verify | /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml; Complete native read-only log | supports | all UniProtKB protein_examples and causal_graphs xrefs verified ok |
| outer-causal-graphs | /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml; Complete native read-only log | supports | data/structures/membrane_organelle/nuclear_outer_membrane.yaml  (GO:0005640)<br>  yeast_nuclear_outer_membrane_contacts	nvj1p	UNANCHORED_WITH_UNIPROT	Nvj1p (UniProtKB:P38881)<br>  yeast_nuclear_outer_membrane_contacts	vac8p	UNANCHORED_WITH_UNIPROT	Vac8p (UniProtKB:P39968)<br><br>causal_graphs GENE_OR_PROTEIN node summary:<br>     2  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB grounding or xref<br>     0  COVERED                   component_ref target holds protein_examples covering all declared symbols<br>     0  PARTIAL_EXAMPLES          component_ref target holds protein_examples but has unrepresented symbols<br>     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols but holds no protein_examples<br>     0  NO_GENE_SYMBOLS           component_ref target declares no gene_symbols and holds no protein_examples<br>     0  DANGLING_COMPONENT_REF    component_ref names a component_id that does not exist on the record<br>     0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or xref on the node<br>     2  total GENE_OR_PROTEIN causal nodes |
| target-curies | just check-curies-strict; data/structures/membrane_organelle/nuclear_outer_membrane.yaml; native collect() exact identifier slice; SHA identifies full original TSV | supports | 10 of 10 collected target identifiers returned OK. No residuals. Native source checks are separately scoped; skipped or unreachable identifiers are not silently counted as resolved. |
| global-qc-result | just qc; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 f685f7bf909553282506f9f3c5a09594dcc8a5244d60910af9329e0d7b5514ae; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native QC passed: 1025 tests passed and 3 skipped, plus history, strict schema, generated-site consistency and corpus-report stages. |
| global-history-result | just validate-history; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 180c448609bee8b99e646da79e8b6c9e1300575374fe2ad823131d7624bf42d0; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. All 1888 history records validated; URI precheck reported zero invalid references. |
| global-products-result | just validate-products; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 ce990392d0edb5c173c58d7b9cf421a4ae36c746dfd2f7f1c0a31c07307b5c26; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Label results: 3982 canonical, 50 synonym, 6 exception and 659 SKIPPED_NO_ADAPTER. Skips are not successful authority verification. |
| global-traits-result | just check-trait-links --check; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 3551f69e0996e3a672a3da0defda6e3f541068fdc4d7af7440cd934a36e143ad; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. 10 trait links checked: 10 matching labels, 0 missing and 0 mislabelled. |
| global-curies-result | just check-curies-strict; Fresh batch26 full-corpus run at f97b1abe2d78971b6f66b9083087d7a94cf3c0cc; stdout hash below; stderr SHA256 68f69df12edee099457ef6e297b4fb63dc7514d16360a264452e73a6eff388a2; input manifest SHA256 a03d9f8e9f1ce967255422d8aaa6600a77e2460876c0a53aa335439f4e467c02 | supports | Exit0. Native resolver control: every resolver accepts a known id and rejects a fabricated one. Identifier results: 4848 OK, 252 SKIPPED, 822 UNREACHABLE. Transport failures and skipped prefixes are not proof of identifier resolution; exact target residuals are assessed separately. |

## Limits And Additional Notes

- Source scope is limited to the exact body sections and captions stated per evidence row. No primary image pixels or quantitative reanalysis is claimed, and no maintained image or verbatim snippet requires reuse/licence verification here.
- Ontological topology and constitutive material identity do not establish individual molecular formation necessity. Optional exact lipid chemistry, stoichiometry and complete resident-protein inventories remain unresolved without invented findings.
- COMMON is qualitative occurrence; native taxon identities do not quantify prevalence or make every primary experimental background identical to a reference strain.
- Pan2000 direct interaction is the authors' interpretation of two-hybrid/copurification and cellular perturbation data; Resultssec11 explicitly leaves a remote indirect-binding possibility. No new purified minimal reconstitution or whole-membrane assembly necessity is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological findings. Exact target residuals were resolved only through the separately reviewed evidence mapping.
- User all-record goal authorizes clean drafts without inventing findings. Parent owns finalization and persistence; five same-base global gates are staged separately.
- Only this review bundle is intended for persistence. Maintained scientific content, native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver evidence. Earlier draft-stage statements that these checks were pending are superseded by the completed checks here; scientific access and assay limitations remain in force.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261022T025109Z-nuclear-outer-membrane-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: Nuclear outer membrane scientific review
started_at: '2026-10-22T02:36:35Z'
finished_at: '2026-10-22T02:51:09Z'
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
summary: The outer nuclear-membrane identity, label-only lipid material, source-scoped
  yeast function and verified protein references are supported. One minor finding
  concerns the OPEN discussion rationale that still treats existing verified accession
  links as pending.
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
  - path: data/structures/membrane_organelle/nuclear_envelope.yaml
    sha256: 226a12a5500d39f1afbc5baa0f3a81891d6ae4918f4d6c29e8ce05de0df9979a
    role: context
  - path: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
    sha256: 1c45350eaa4a19474f4689125aadc8aa93d1824d41303e3c4aaff1f7e1db6019
    role: context
  - path: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
    sha256: c0484a80c2b1568174ca7f9c96805a6ce2749a3ba27b700e21fb1de2aef4e4df
    role: context
  - path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    sha256: a760b04919cb0a80c89fd2eee5c1d4a0c940fc15a17b77b4b1810b9e1d2b2ffb
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
- target_id: GO:0005640
  path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  label: nuclear outer membrane
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    role: maintained scientific record
scope:
  description: Entire target within the four-record nuclear-envelope boundary set
    (target plus three neighbors); definitions, hierarchy, components, taxon/examples,
    functions, every directed edge, discussions, exact authorities and declared source
    body/supplement scopes.
  selection: Batch35 target 7; exact native inspection and focused schema/strict gates
    passed before assessment at unchanged f97b1abe.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0005640
checks:
- check_id: schema
  name: Focused native schema
  status: passed
  required: true
  target_ids:
  - GO:0005640
  command: just validate data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - schema-result
- check_id: strict
  name: Focused native strict
  status: passed
  required: true
  target_ids:
  - GO:0005640
  command: just validate-strict data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_outer_membrane-strict.tsv
  exit_code: 0
  summary: Focused validator passed.
  evidence_ids:
  - strict-result
- check_id: imodulondb
  name: Expression-module applicability
  status: not_applicable
  required: false
  target_ids:
  - GO:0005640
  summary: No computational expression-module assertion is made; experimental gene
    interventions do not require expression-module evidence.
- check_id: verify
  name: Native verify
  status: passed
  required: true
  target_ids:
  - GO:0005640
  command: /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python
    scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  exit_code: 0
  summary: Read-only check passed; diagnostic coverage is assessed separately.
  evidence_ids:
  - outer-verify
- check_id: causal-graphs
  name: Native causal-graphs
  status: passed
  required: true
  target_ids:
  - GO:0005640
  command: /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python
    scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  exit_code: 0
  summary: Read-only check passed; diagnostic coverage is assessed separately.
  evidence_ids:
  - outer-causal-graphs
- check_id: scientific-review
  name: Claim-level scientific review
  status: passed
  required: true
  target_ids:
  - GO:0005640
  summary: All required claim-level inspections completed; findings and scope limitations
    are recorded separately.
  evidence_ids:
  - record
  - schema
  - neighbor-nuclear_envelope
  - neighbor-nuclear_envelope_lumen
  - neighbor-nuclear_inner_membrane
  - nuclear-agent-go
  - nuclear-agent-membrane-ancestors
  - nuclear-agent-tax4932
  - nuclear-agent-tax559292
  - nuclear-agent-pan2000-meta
  - nuclear-agent-pan2000-pmc
  - nuclear-agent-protein-P38881
  - nuclear-agent-protein-P39968
- check_id: target-curies
  name: Exact target resolver slice with scoped native residual resolution
  status: passed
  required: true
  target_ids:
  - GO:0005640
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
  - GO:0005640
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
  - GO:0005640
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
  - GO:0005640
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
  - GO:0005640
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
  - GO:0005640
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
  reference: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  locator: Entire maintained YAML, including history, evidence, all directed edges
    and discussions
  accessed_at: '2026-10-22T02:43:54Z'
  support: context_only
  summary: The complete target was independently read. Maintained scientific content
    and status remain unchanged.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  locator: StructuralComponent lines391–444; CausalNode lines843–875; component types1044–1057
  accessed_at: '2026-10-22T02:43:54Z'
  support: context_only
  summary: Molecular lipid identity differs from a complete membrane. GO can ground
    a protein subcomplex; CHEBI is the stated lipid grounding route. Essentiality
    denotes formation necessity. Node xrefs can link instances without claiming complete
    cohort coverage.
- evidence_id: neighbor-nuclear_envelope
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_envelope.yaml
  locator: Complete maintained nuclear-envelope boundary neighbor
  accessed_at: '2026-10-22T02:43:54Z'
  support: context_only
  summary: Exact adjacent record read and frozen for topology and representation context;
    maintained context is not independent experimental evidence.
- evidence_id: neighbor-nuclear_envelope_lumen
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_envelope_lumen.yaml
  locator: Complete maintained nuclear-envelope boundary neighbor
  accessed_at: '2026-10-22T02:43:54Z'
  support: context_only
  summary: Exact adjacent record read and frozen for topology and representation context;
    maintained context is not independent experimental evidence.
- evidence_id: neighbor-nuclear_inner_membrane
  kind: record_content
  reference: data/structures/membrane_organelle/nuclear_inner_membrane.yaml
  locator: Complete maintained nuclear-envelope boundary neighbor
  accessed_at: '2026-10-22T02:43:54Z'
  support: context_only
  summary: Exact adjacent record read and frozen for topology and representation context;
    maintained context is not independent experimental evidence.
- evidence_id: nuclear-agent-go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005635,GO%3A0031967,GO%3A0005634,GO%3A0005637,GO%3A0005640,GO%3A0005641,GO%3A0005643,GO%3A0006913,GO%3A0006998,GO%3A0031970,GO%3A0005788,GO%3A0031090,GO%3A0005774
  locator: 'Complete13 requested native term results: exact IDs, definitions, synonyms,
    active flags and returned child relations'
  accessed_at: '2026-10-22T02:39:01.002553Z'
  support: supports
  summary: All13 active native terms were inspected. The definitions distinguish envelope,
    nucleus, inner/outer bilayers, perinuclear lumen, NPC, ER lumen and vacuolar membrane.
    Returned children directly support envelope is_a organelle envelope, lumen is_a
    organelle envelope lumen, and envelope part_of nucleus. GO0005635 exactly supplies
    the maintained definition, including its20–40nm range and lamina clause; this
    is ontology wording, not a new universal measurement.
  snapshot_sha256: 18627a592c0f8bace3b7cf3d8847639aae864fec38a5ee52dbf84c4746d35298
- evidence_id: nuclear-agent-membrane-ancestors
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005637,GO%3A0005640/ancestors?relations=is_a
  locator: Exact relations=is_a ancestor lists for GO0005637 and GO0005640
  accessed_at: '2026-10-22T02:39:55.152921Z'
  support: supports
  summary: The is_a-only ancestor response places both nuclear membrane terms below
    GO0031090 organelle membrane. It establishes ancestry, not necessarily an immediate
    parent edge.
  snapshot_sha256: e57c228227ef0b047dd587cb5ac0fb2f89e7083e9d3d3cf43b21619398af3dc5
- evidence_id: nuclear-agent-tax4932
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/4932
  locator: Complete taxId, scientificName, rank and available lineage fields
  accessed_at: '2026-10-22T02:39:01.675509Z'
  support: supports
  summary: ENA confirms Saccharomyces cerevisiae4932 at species rank; this is not
    an experimental-strain attestation.
  snapshot_sha256: a9a5b093cf2c8ca6b29636297d91762ea2a8b790cf3979b09c50344bbaf6656e
- evidence_id: nuclear-agent-tax559292
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/559292
  locator: Complete taxId, scientificName, rank and available lineage fields
  accessed_at: '2026-10-22T02:39:01.682611Z'
  support: supports
  summary: ENA confirms Saccharomyces cerevisiae S288C559292 at strain rank, matching
    the protein reference entries; it is distinguished from the primary experimental
    backgrounds.
  snapshot_sha256: 940c60b7db761a4fda63338d466eed265e65607af672578413061e3c258095bb
- evidence_id: nuclear-agent-pan2000-meta
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1091/mbc.11.7.2445%22&format=json&resultType=core
  locator: Unique MED result and complete abstract
  accessed_at: '2026-10-22T02:39:01.003242Z'
  support: supports
  summary: Exact DOI10.1091/mbc.11.7.2445/PMID10888680 authors/year/title and full
    abstract match the genuine primary body.
  snapshot_sha256: 8fd13375de562999edc00fab8fd5103111b6f6e00b90719774f0bf6f17fa1fe6
- evidence_id: nuclear-agent-pan2000-pmc
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC14931/
  locator: PMC14931 Methods sec3–6,9; all Results sec11–17 and Discussion sec18 with
    embedded Figure1–9 captions. No image pixels or unlisted Methods inspected.
  accessed_at: '2026-10-22T02:39:21.042109Z'
  support: supports
  summary: Primary yeast study supports Nvj1 on the nuclear envelope, Vac8 on the
    vacuole and their role in contact formation using localization, two-hybrid, copurification,
    deletion/overexpression and thin-section TEM. It infers direct interaction while
    explicitly retaining a remote indirect-binding possibility. Methods use YEF473
    backgrounds and L40, not a stated S288C experiment. Neither protein is thereby
    necessary for formation of the entire nuclear membrane.
  snapshot_sha256: 21ca47f90e10c08bef74688b1d99cb48079becd20b5613d7fc569a70de30001c
- evidence_id: nuclear-agent-protein-P38881
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P38881.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-22T02:39:02.269662Z'
  support: supports
  summary: Native primary accession P38881 identifies reviewed NVJ1/YHR195W in S288C559292.
    Gene/locus tokens, entry status and relevant location/interaction comments were
    read. This verifies this reference instance; the cited primary experiment supplies
    biological role and experimental background.
  snapshot_sha256: 4e3daf10d4a641ffad9c2e3c2850dd073e2a69da5e833626c484de0d5807b86b
- evidence_id: nuclear-agent-protein-P39968
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P39968.json
  locator: primaryAccession, entryType, proteinDescription, genes, organism; relevant
    FUNCTION/SUBUNIT/SUBCELLULAR LOCATION comments
  accessed_at: '2026-10-22T02:39:02.315473Z'
  support: supports
  summary: Native primary accession P39968 identifies reviewed VAC8/YEL013W in S288C559292.
    Gene/locus tokens, entry status and relevant location/interaction comments were
    read. This verifies this reference instance; the cited primary experiment supplies
    biological role and experimental background.
  snapshot_sha256: 8717485852a2be10a3d083ada88ed1cbbfbfe2a8ac02095c565a428ad14a6be8
- evidence_id: schema-result
  kind: validation
  reference: just validate data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:36Z'
  support: supports
  summary: 'No issues found

    uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/membrane_organelle/nuclear_outer_membrane.yaml'
  snapshot_sha256: c0583a69e372096cea05783579dddbe181b2e99dcf8851fe57bdc57b98070d1c
- evidence_id: strict-result
  kind: validation
  reference: just validate-strict data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_outer_membrane-strict.tsv
  locator: Captured focused validator log
  accessed_at: '2026-10-22T02:36:38Z'
  support: supports
  summary: "uv run python scripts/validate_strict.py data/structures/membrane_organelle/nuclear_outer_membrane.yaml\
    \ --out /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_outer_membrane-strict.tsv\n\
    Validating 1 files with 17 workers; schema=/private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/src/cellstructuremech/schema/cellstructuremech.yaml\n\
    \n=== validate-strict summary ===\n  files scanned:      1\n  files with ERROR:\
    \   0\n  total ERROR rows:   0\n  TSV:                /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/nuclear_outer_membrane-strict.tsv"
  snapshot_sha256: 682c35569a9e1365702c1143f1490e3e3ecfbdf4c428662329a34504ad25caf0
- evidence_id: outer-verify
  kind: validation
  reference: /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python
    scripts/uniprot_genes.py --verify --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T02:41:05.234225Z'
  support: supports
  summary: all UniProtKB protein_examples and causal_graphs xrefs verified ok
  snapshot_sha256: 3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289
- evidence_id: outer-causal-graphs
  kind: validation
  reference: /private/tmp/cellstructure-batch35-20261022-5cl5i1x7/repo/.venv/bin/python
    scripts/uniprot_genes.py --causal-graphs --record data/structures/membrane_organelle/nuclear_outer_membrane.yaml
  locator: Complete native read-only log
  accessed_at: '2026-10-22T02:41:05.713277Z'
  support: supports
  summary: "data/structures/membrane_organelle/nuclear_outer_membrane.yaml  (GO:0005640)\n\
    \  yeast_nuclear_outer_membrane_contacts\tnvj1p\tUNANCHORED_WITH_UNIPROT\tNvj1p\
    \ (UniProtKB:P38881)\n  yeast_nuclear_outer_membrane_contacts\tvac8p\tUNANCHORED_WITH_UNIPROT\t\
    Vac8p (UniProtKB:P39968)\n\ncausal_graphs GENE_OR_PROTEIN node summary:\n    \
    \ 2  UNANCHORED_WITH_UNIPROT   no component_ref, but node carries a UniProtKB\
    \ grounding or xref\n     0  COVERED                   component_ref target holds\
    \ protein_examples covering all declared symbols\n     0  PARTIAL_EXAMPLES   \
    \       component_ref target holds protein_examples but has unrepresented symbols\n\
    \     0  HAS_SYMBOLS_NO_EXAMPLES   component_ref target declares gene_symbols\
    \ but holds no protein_examples\n     0  NO_GENE_SYMBOLS           component_ref\
    \ target declares no gene_symbols and holds no protein_examples\n     0  DANGLING_COMPONENT_REF\
    \    component_ref names a component_id that does not exist on the record\n  \
    \   0  UNANCHORED_NO_UNIPROT     no component_ref and no UniProtKB grounding or\
    \ xref on the node\n     2  total GENE_OR_PROTEIN causal nodes"
  snapshot_sha256: 20ca030cdfeb1a45fdd86dc1db1c8361c2cd5f5569a0fd1e3468470442253e23
- evidence_id: target-curies
  kind: validation
  reference: just check-curies-strict
  locator: data/structures/membrane_organelle/nuclear_outer_membrane.yaml; native
    collect() exact identifier slice; SHA identifies full original TSV
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
  topic: Distinct outer nuclear membrane
  outcome: supported
  target_ids:
  - GO:0005640
  summary: The exact native definition, maintained synonym, nuclear-envelope parthood
    and organelle-membrane ancestry agree. The paired bilayer and intervening lumen
    remain distinct topology nodes, as stated by the resolved boundary discussion.
  evidence_ids:
  - record
  - nuclear-agent-go
  - nuclear-agent-membrane-ancestors
- assessment_id: components
  area: grounding
  topic: Collective label-only lipid material
  outcome: supported
  target_ids:
  - GO:0005640
  summary: The reviewed-label-only bilayer row has no whole-membrane GO chemical grounding.
    Its graph component_ref can identify constituting material without claiming exact
    chemical equivalence. Optional source-neutral lipid chemistry remains unresolved;
    no forced protein inventory is inferred.
  evidence_ids:
  - record
  - schema
  - nuclear-agent-go
- assessment_id: necessity
  area: evidence
  topic: Individual molecular formation requirements unresolved
  outcome: unknown
  target_ids:
  - GO:0005640
  summary: The collective bilayer is constitutive of this membrane. ESSENTIAL does
    not establish which individual lipid classes or proteins are required for membrane
    formation; the inspected targeting/contact studies do not test those global formation
    requirements.
  evidence_ids:
  - record
  - schema
  - nuclear-agent-go
  - nuclear-agent-pan2000-pmc
- assessment_id: functions-graph
  area: graph
  topic: Yeast contact function and six coarse edges
  outcome: supported
  target_ids:
  - GO:0005640
  summary: The topology, Nvj1 localization, Vac8 vacuolar localization and interaction
    edges agree with Pan. The source combines binding/localization and perturbation
    evidence and interprets contact formation as mediated by the pair; its acknowledged
    remote indirect-binding possibility is retained as an assay limit. This does not
    imply either partner forms the entire outer membrane.
  evidence_ids:
  - record
  - nuclear-agent-go
  - nuclear-agent-pan2000-pmc
  - nuclear-agent-protein-P38881
  - nuclear-agent-protein-P39968
- assessment_id: proteins
  area: grounding
  topic: Exact reference instances
  outcome: supported
  target_ids:
  - GO:0005640
  summary: P38881 identifies NVJ1/YHR195W and P39968 identifies VAC8/YEL013W in reviewed
    S288C entries. They corroborate the named actors but do not recast the primary
    YEF473/L40 experimental backgrounds as S288C.
  evidence_ids:
  - record
  - schema
  - nuclear-agent-tax559292
  - nuclear-agent-pan2000-pmc
  - nuclear-agent-protein-P38881
  - nuclear-agent-protein-P39968
- assessment_id: scope
  area: scope
  topic: Qualitative budding-yeast model
  outcome: supported
  target_ids:
  - GO:0005640
  summary: Species4932 is correct and the primary study establishes the named targeting/contact
    example. Reference accessions are not a claim that every experiment used S288C;
    COMMON is qualitative and supplies no universal percentage.
  evidence_ids:
  - record
  - nuclear-agent-tax4932
  - nuclear-agent-tax559292
  - nuclear-agent-pan2000-pmc
- assessment_id: discussion
  area: provenance
  topic: Stale unresolved accession-verification rationale
  outcome: concern
  target_ids:
  - GO:0005640
  summary: The OPEN discussion says protein nodes are left ungrounded until exact
    UniProt or family identifiers can be verified, but current node xrefs and the
    October history already record this accession work. The rationale should acknowledge
    verified instances and separate any genuinely remaining family or grouped-actor
    coverage rather than present all nodes as unverified.
  evidence_ids:
  - record
  - nuclear-agent-protein-P38881
  - nuclear-agent-protein-P39968
- assessment_id: access-completeness
  area: evidence
  topic: Source tier, currentness and review limits
  outcome: supported
  target_ids:
  - GO:0005640
  summary: All target citation identities and native term/protein identities were
    checked. Relevant primary or review body passages were read within the declared
    locators. Historical discussions are interpreted in their recorded context, with
    only concrete current contradictions flagged. No scientific promotion or corpus
    edit is implied.
  evidence_ids:
  - record
  - nuclear-agent-go
  - nuclear-agent-membrane-ancestors
  - nuclear-agent-tax4932
  - nuclear-agent-tax559292
  - nuclear-agent-pan2000-meta
  - nuclear-agent-pan2000-pmc
  - nuclear-agent-protein-P38881
  - nuclear-agent-protein-P39968
findings:
- finding_id: F1
  issue_key: nuclear-outer-membrane-stale-protein-grounding-rationale
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Update the open protein-grounding rationale to acknowledge verified xrefs
  description: The rationale says the named protein nodes are left ungrounded until
    exact UniProt or family identifiers can be verified. Current graph nodes already
    carry verified accessions, and the October curation event records their addition.
    The remaining task needs to distinguish completed instance verification from any
    unresolved family or grouped-actor coverage.
  target_ids:
  - GO:0005640
  field_paths:
  - discussions[1].rationale
  - discussions[1].status
  evidence_ids:
  - record
  - nuclear-agent-protein-P38881
  - nuclear-agent-protein-P39968
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    role: maintained scientific record
  rule_id: Evidence placement and current discussion provenance
  native_severity: minor
  normalization_reason: This is bounded stale task provenance. Protein identities
    and biological claims remain supported; an optional missing family or complete
    grouped-actor accession inventory is not independently treated as a defect.
actions:
- action_id: A1
  finding_ids:
  - F1
  target_ids:
  - GO:0005640
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/membrane_organelle/nuclear_outer_membrane.yaml
    role: maintained scientific record
  description: Update discussion ground_nvj1p_and_vac8p to acknowledge the verified
    accession links and preserve its historical context. Retain OPEN only for a specifically
    stated remaining task; otherwise resolve the completed accession-verification
    subtask. Preserve correct xrefs and source-specific protein roles.
  acceptance_checks:
  - The rationale no longer says all named nodes await UniProt verification when those
    links are already present.
  - Any retained OPEN scope names an actual remaining task and does not imply that
    one representative accession identifies every member of a grouped system.
  - Native schema, strict, read-only protein verification and history checks pass
    after authorized curation.
limitations:
- Source scope is limited to the exact body sections and captions stated per evidence
  row. No primary image pixels or quantitative reanalysis is claimed, and no maintained
  image or verbatim snippet requires reuse/licence verification here.
- Ontological topology and constitutive material identity do not establish individual
  molecular formation necessity. Optional exact lipid chemistry, stoichiometry and
  complete resident-protein inventories remain unresolved without invented findings.
- COMMON is qualitative occurrence; native taxon identities do not quantify prevalence
  or make every primary experimental background identical to a reference strain.
- Pan2000 direct interaction is the authors' interpretation of two-hybrid/copurification
  and cellular perturbation data; Resultssec11 explicitly leaves a remote indirect-binding
  possibility. No new purified minimal reconstitution or whole-membrane assembly necessity
  is inferred.
- Fresh corpus checks have bounded coverage:659 label checks had no adapter; resolver
  totals 252 SKIPPED, 822 UNREACHABLE. These totals are not target-specific biological
  findings. Exact target residuals were resolved only through the separately reviewed
  evidence mapping.
notes:
- User all-record goal authorizes clean drafts without inventing findings. Parent
  owns finalization and persistence; five same-base global gates are staged separately.
- Only this review bundle is intended for persistence. Maintained scientific content,
  native status, history and generated pages remain unchanged.
- Fresh26 finalization integrated all five actual corpus gates and exact target resolver
  evidence. Earlier draft-stage statements that these checks were pending are superseded
  by the completed checks here; scientific access and assay limitations remain in
  force.
```
