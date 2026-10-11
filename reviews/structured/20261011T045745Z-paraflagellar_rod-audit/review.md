# Paraflagellar rod: scientific evidence review

- Review: 20261011T045745Z-paraflagellar_rod-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T04:48:07Z
- Finished UTC: 2026-10-11T04:57:45Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record assessed at the source access tiers stated; two concrete evidence issues observed. Optional empty fields and explicitly deferred molecular grounding are not findings.

## Scope And Provenance

Entire native YAML, present scientific claims, exact authorities and both history surfaces.

Selection: One sequential unassessed target from the all-909-record goal; not a sampled corpus verdict.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base fe0a41e4cd9c1bfa27f72ef427f045022df862c0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097740 | data/structures/appendage/paraflagellar_rod.yaml | maintained | paraflagellar rod |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097740 | Command passed; deterministic validity is not scientific support. |
| strict | passed | True | GO:0097740 | Command passed; deterministic validity is not scientific support. |
| snippets | passed | True | GO:0097740 | No quoted snippets present; the successful command did not test paraphrase accuracy. Paraphrases were inspected separately. |
| history | passed | True | GO:0097740 | Command passed; deterministic validity is not scientific support. |
| labels | passed | True | GO:0097740 | 3544 canonical labels, 50 synonyms and six exceptions accepted; 603 non-adapter pairs skipped. Exact relevant target authorities were separately inspected. |
| traits | passed | True | GO:0097740 | Command passed; deterministic validity is not scientific support. |
| curies | passed | True | GO:0097740 | 4010 identifiers resolved; 251 skipped. BFO controls were not exercised because its authority was unreachable. Skips and unexercised controls are not certified; relevant target authorities were separately inspected. |
| reviews | passed | True | GO:0097740 | Command passed; deterministic validity is not scientific support. |
| diff | passed | True | GO:0097740 | Command passed; deterministic validity is not scientific support. |
| contract | passed | True | GO:0097740 | Command passed; deterministic validity is not scientific support. |
| Exact-baseline authoritative CI QC | passed | True | GO:0097740 | Full QC passed on the exact unchanged baseline; not a newly run local full QC. |
| Structured-source applicability | passed | False | GO:0097740 | iModulonDB dataset inventory has no matching trypanosome, Leishmania or spirochete dataset. Not applicable; absence from the adapter is not biological absence. |

## Scientific And Domain Assessments

### GO identity, definition, parthood and synonym

identity: supported. Targets: GO:0097740.

Exact PFR term and 9+2 motile cilium parthood are supported; paraxial rod remains a related historical synonym.

### Paralogue families, examples and required composition

grounding: concern. Targets: GO:0097740.

Valid accessions are assigned to opposite consolidated families; PFR2 essentiality also exceeds the generic record scope that includes reduced PFRs.

### Distribution and examples

scope: supported. Targets: GO:0097740.

Rare protist distribution and variable kinetoplastid architecture are supported. Reduced PFRs remain in record scope.

### Three functions and assembly graph

evidence: concern. Targets: GO:0097740.

Motility, assembly-factor boundary and qualified signaling-platform descriptions are supported. The PFRA-tracking edge incorrectly calls PFRA PFR1; graph context must distinguish full-model assembly from reduced rods.

### Status, histories, optional fields and source access

provenance: supported. Targets: GO:0097740.

PROPOSED status and append-only histories remain unchanged. No asserted images, physical measurements, trait links or datasets require additional verification. Unpopulated optional fields are not defects.

## Findings

### F1: Reconcile PFR1/PFR2 orthology with historical PFRC/PFRA names

major / open / confirmed; issue key: paraflagellar-rod-pfr-family-conflation.

The record maps 69 kDa PFRA/PFRB (P22225) to PFR1 and 73 kDa PFRC/PFRD (Q26789) to PFR2 while importing Leishmania PFR1/PFR2 roles. Gadelha 2004 Table 1 and Fig. 1 explicitly consolidate PFRC as PFR1 and PFRA as PFR2. The tagged-PFRA edge is consequently assigned to the wrong modern family. Valid accessions and source labels do not make these orthology assignments valid.

### F2: Qualify PFR2 requirement for full versus reduced rods

major / open / confirmed; issue key: paraflagellar-rod-pfr2-essentiality-scope.

ESSENTIAL means the structure does not form without the component. The generic record explicitly includes cryptic/reduced PFRs, yet gives PFR2 unqualified ESSENTIAL status. Gadelha 2005 imaged a reduced Crithidia deanei rod and found no PFR2 with multiple techniques, retaining assay limitations. Leishmania loss experiments establish a requirement for full native architecture rather than all recognizable PFR material.

## Recommended Actions And Acceptance Checks

### A1

Reconcile PFR1/PFR2 orthology with historical PFRC/PFRA names

- Keep stable pfr1/pfr2 component IDs but align modern PFR1 with PFRC/PFRD and Q26789, and PFR2 with PFRA/PFRB and P22225.
- Move gene symbols, examples and experimental citations together; correct graph labels and the tagged-PFRA edge.
- Preserve source-native UniProt names and historical curation events; document the nomenclature crosswalk explicitly.
- Use the guarded writer, preserve prior histories and PROPOSED status, append EDIT provenance, regenerate affected products and pass focused tests plus authoritative QC.

### A2

Qualify PFR2 requirement for full versus reduced rods

- Use a lineage/context-qualified essentiality value and explain the full-native versus reduced-rod boundary.
- Retain the Leishmania native-assembly result and the reduced Crithidia observation with detection limits.
- Scope the assembly graph to the examined model lineages; do not claim an experimentally demonstrated universal gene absence.
- Use the guarded writer, preserve prior histories and PROPOSED status, append EDIT provenance, regenerate affected products and pass focused tests plus authoritative QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/paraflagellar_rod.yaml; Full native YAML and exact append-only record histories | context_only | Pre-mutation native record; original status and historical events retained. |
| prior | reviews/structured/ and reports/yaml_record_review/; Exact slugs and GO identifiers | context_only | No earlier exact-target saved review bundle found in these two roots. Closed issue #203 concerns introducing an active rotation node, not the static-versus-dynamic evidence mismatch; #293 concerns the PFR synonym citation, not family mapping. Earlier histories remain authoritative historical observations. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289,GO:0097740,GO:0097729,GO:0005930,GO:0055040,GO:0009288,GO:0120100,GO:0071973; Exact target term and asserted parent/parthood/function terms only | supports | Active GO identifiers and current relations match the native identity and hierarchy. Ontology wording is not experimental validation of uniform molecular architecture. |
| nomenclature | DOI:10.1016/j.molbiopara.2004.03.006; Pages 113-115, Table 1 and Fig. 1; page 114 table visually inspected | supports | The authors consolidate Trypanosoma PFRC into PFR1 and PFRA into PFR2 while keeping Leishmania PFR1/PFR2. Native rows combine these opposite families. |
| gadelha | DOI:10.1128/EC.4.3.516-525.2005; PCR/hybridization/protein Methods, Results including Fig. 4, Discussion | supports | Crithidia deanei has a reduced, recognizable PFR. Multiple assays found no evidence for PFR2; authors explicitly note individual assay limitations. This does not establish universal PFR2 essentiality. |
| maga | DOI:10.1242/jcs.112.16.2753; Primary abstract and bibliographic identity | supports | Leishmania PFR1 and PFR2 are both needed for native full PFR formation; attachment fibers assemble without the bulk PFR and PFR1 associates with them without PFR2. |
| bastin1999 | DOI:10.1128/MCB.19.12.8191; Abstract, tagged-PFRA assembly Results/Fig. 3-5 and Discussion | supports | Tagged PFRA incorporation occurs mostly at the distal tip plus minor incorporation along the PFR and in old flagella. The paper uses the pre-consolidation PFRA name. |
| alves | DOI:10.1242/jcs.242271; Abstract, AF1/AF2 Results, Discussion and Cell culture Methods | supports | Cytoplasmic AF1/AF2 deletions in TREU927 reduce PFR2 protein and impair complete PFR assembly. Proteins can still reach the flagellar tip; a specific direct preassembly/chaperone mechanism is not proved. |
| portman2009 | DOI:10.1074/jbc.M808859200; Primary abstract | supports | Twenty candidate PFR components from ablation proteomics; a subset localized by tagging; calcium/calmodulin links are inferred rather than direct biochemical proof. |
| portman2010 | DOI:10.1016/j.ijpara.2009.10.005; Review component-nomenclature, motility, signaling and assembly discussion; secondary synthesis | supports | Distinguishes historical PFRA naming from PFR2; discusses metabolic/signaling proteins and proposed regulatory functions, not a resolved universal pathway. |
| schlaeppi | DOI:10.1083/jcb.109.4.1695; Primary abstract and bibliographic identity only | supports | Helical major PFRA/PFRB protein and tandem genes; original one-protein interpretation was superseded by later work. |
| deflorin | PMID:7961827; Primary abstract and bibliographic identity only | supports | Distinct PFRA/PFRB and PFRC/PFRD products, not one family defined by their ordinal entry names. |
| santrich | PMID:9497035; Primary abstract and bibliographic identity only | supports | Leishmania PFR2 knockout leaves a residual structure and changes waveform/forward swimming. |
| farina | DOI:10.1111/j.1550-7408.1986.tb05661.x; Primary abstract and bibliographic identity only | supports | Publisher-deposited abstract uses paraxial rod for the trypanosomatid lattice and attachment fibers; synonym does not equate unrelated dinoflagellate structures. |
| bastin1998 | DOI:10.1038/35300; Publisher abstract at https://www.nature.com/articles/35300 | supports | Antisense ablation of the PFR causes paralysis; only the primary abstract, not the subscription body, was read. |
| P22225 | https://rest.uniprot.org/uniprotkb/P22225.json; Gene names, source protein name, taxonomy and family cross-references | supports | Accession/gene identity is valid; UniProt mnemonic numbering is not evidence of consolidated cross-species PFR orthology. |
| Q26789 | https://rest.uniprot.org/uniprotkb/Q26789.json; Gene names, source protein name, taxonomy and family cross-references | supports | Accession/gene identity is valid; UniProt mnemonic numbering is not evidence of consolidated cross-species PFR orthology. |
| interpro-IPR007824 | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007824/; Exact family metadata | supports | Broad PFR family rather than a single orthologous PFR1 or PFR2 subset. |
| pfam-PF05149 | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF05149/; Exact family metadata | supports | Broad PFR family rather than a single orthologous PFR1 or PFR2 subset. |
| taxon-5702 | https://rest.uniprot.org/taxonomy/5702.json; Exact taxonomy identity | supports | Taxon identity and rank match the native distribution/example at its stated scope. |
| taxon-5665 | https://rest.uniprot.org/taxonomy/5665.json; Exact taxonomy identity | supports | Taxon identity and rank match the native distribution/example at its stated scope. |
| taxon-2759 | https://rest.uniprot.org/taxonomy/2759.json; Exact taxonomy identity | supports | Taxon identity and rank match the native distribution/example at its stated scope. |
| taxon-33682 | https://rest.uniprot.org/taxonomy/33682.json; Exact taxonomy identity | supports | Taxon identity and rank match the native distribution/example at its stated scope. |

## Limits And Additional Notes

- Bastin 1998, Maga 1999, Santrich 1997, Deflorin 1994, Schlaeppi 1989 and Farina 1986 were assessed at primary-abstract level for their bounded native claims; unseen bodies and supplements are not claimed as reviewed.
- Gadelha 2004 nomenclature table was visually checked. Gadelha 2005, Bastin 1999 and Alves 2020 relevant main-text experiments were inspected; Portman 2010 is secondary synthesis and Portman 2009 was inspected at abstract level.
- Same-agent review, not independent human sign-off or completion of the 909-record goal.
- Exact-baseline CI supplies full QC; skipped namespaces, unexercised BFO controls and non-adapter label pairs are explicit limits.
- No relevant iModulonDB coverage. No quoted snippets to verify; identifier/label validation cannot establish scientific accuracy.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T045745Z-paraflagellar_rod-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Paraflagellar rod: scientific evidence review'
started_at: '2026-10-11T04:48:07Z'
finished_at: '2026-10-11T04:57:45Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source assessment before mutation, not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record assessed at the source access tiers stated; two concrete
  evidence issues observed. Optional empty fields and explicitly deferred molecular
  grounding are not findings.
source:
  git_revision: fe0a41e4cd9c1bfa27f72ef427f045022df862c0
  state: working_tree
  inputs:
  - path: .claude/skills/curate-yaml-record/references/review-checklist.md
    sha256: e6b9e4b16a58c54402bed7bbee2c8b94a91d37562e8b0ee8b94ff0c829184a70
    role: context
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: data/structures/appendage/bacterial_type_flagellum.yaml
    sha256: 4e3e6bf50835a3134d50e5a20a87cdfa86e1e37c21085757402df7dd628095e6
    role: context
  - path: data/structures/appendage/cilium.yaml
    sha256: 2536d421f9c482abf35c2d2bf026eb6158ddfec5c2df1f319ca80698cbb56bb8
    role: context
  - path: data/structures/appendage/p_pilus.yaml
    sha256: c9e8371a5cc6cda0a28d5264a6a2c2368a703670b3c285fc12f1aa58b6adafa9
    role: context
  - path: data/structures/appendage/paraflagellar_rod.yaml
    sha256: e6aac3ef5683759fa8ddc609e8768e2ad265b134bcbd4b1b6012458a713eccdf
    role: target
  - path: data/structures/appendage/periplasmic_flagellum.yaml
    sha256: 5ab5ca72079de286b8efd85459da9f3bb2851a22ce75caa658277a22b740c79b
    role: context
  - path: data/structures/appendage/pilus.yaml
    sha256: b82205e792d181aa2e2cb76eb56a2ecafdb3021302c7b86a5819c649528bc06b
    role: context
  - path: data/structures/appendage/type_i_pilus.yaml
    sha256: 35b161df2bab54d5b56efde936dc2ee7e5de57789ae583a26a8265b04dc17f00
    role: context
  - path: data/structures/appendage/type_iv_pilus.yaml
    sha256: 744f19aeb3b62c9f4d470fcbf47038056069904d998eb7c5e2b83f6821037d4e
    role: context
  - path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    sha256: a3c88e9e9a6b27327238a732a4d6cdc4740ba50f26c581d251bfb5ad12f7dc0c
    role: context
  - path: docs/CURATION.md
    sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
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
  - path: history/records/paraflagellar_rod/2026-09-09T191015Z-claude-code-f45c80.yaml
    sha256: 8b160cfa2417d8c30e4278b43507f692814121274c4bd76baf6c7f5563902598
    role: context
  - path: history/records/paraflagellar_rod/2026-09-09T191737Z-claude-code-c4e148.yaml
    sha256: 9265fdd54dd38667b24030afe5aed0fef1433f5e3336f18e1acd7e07cde31bd3
    role: context
  - path: history/records/paraflagellar_rod/2026-09-09T192302Z-claude-code-a25c34.yaml
    sha256: 75e693794ede48cb3bc8d8359587024411c87ea506d8bfd7988c0079980c8be3
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/evidence_readability.paraflagellar_rod.tsv
    sha256: 6f1fab50036d4d11d5097edaf3aaff8d79ac1428a605c936125f68ccb741ab40
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0097740
  path: data/structures/appendage/paraflagellar_rod.yaml
  label: paraflagellar rod
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/paraflagellar_rod.yaml
    role: maintained scientific record
scope:
  description: Entire native YAML, present scientific claims, exact authorities and
    both history surfaces.
  selection: One sequential unassessed target from the all-909-record goal; not a
    sampled corpus verdict.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097740
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/paraflagellar_rod.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T04:48:51Z to 2026-10-11T04:48:53Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/paraflagellar_rod.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T04:48:53Z to 2026-10-11T04:48:57Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/paraflagellar_rod.yaml
    --report /private/tmp/csm-review-20261011T044732Z/paraflagellar_rod-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No quoted snippets present; the successful command did not test paraphrase
    accuracy. Paraphrases were inspected separately.
  scope_note: 2026-10-11T04:48:57Z to 2026-10-11T04:49:26Z; log SHA-256 36ebcfabae32b464736106920d1d05d4f719d679ebac23fa4d31005ce761af66
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T04:50:08Z to 2026-10-11T04:50:28Z; log SHA-256 1681e9bb52c501d5ad826d30ec6540fee542dcf71d98302d7a1b47ebde38f150
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: 3544 canonical labels, 50 synonyms and six exceptions accepted; 603 non-adapter
    pairs skipped. Exact relevant target authorities were separately inspected.
  scope_note: 2026-10-11T04:50:28Z to 2026-10-11T04:52:22Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T04:52:22Z to 2026-10-11T04:52:46Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: 4010 identifiers resolved; 251 skipped. BFO controls were not exercised
    because its authority was unreachable. Skips and unexercised controls are not
    certified; relevant target authorities were separately inspected.
  scope_note: 2026-10-11T04:52:46Z to 2026-10-11T04:53:51Z; log SHA-256 3f7e468a7e37b80629f887d91075f58243b0dabfc8af4a9f34cc5da087b7fc49
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T04:53:51Z to 2026-10-11T04:54:47Z; log SHA-256 cc3452fe5ee816c2bdb2cc44d11e93bc3792f9eadd679e9158087b3c368811ce
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T04:54:47Z to 2026-10-11T04:54:47Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T04:53:39Z to 2026-10-11T04:54:39Z; log SHA-256 f9141701da44994bf8584f4d0678e4b743aa2c3a067ebfd12fc995df82c07678
- check_id: qc
  name: Exact-baseline authoritative CI QC
  status: passed
  required: true
  target_ids:
  - GO:0097740
  command: gh run view 38111375021 --json status,conclusion,headSha,event,name,url,jobs;
    gh run view 38111375021 --log
  exit_code: 0
  summary: Full QC passed on the exact unchanged baseline; not a newly run local full
    QC.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38111375021;
    full-log SHA-256 7b39c8b7ee34bf9650709933427d04ebd01fdb8fc544a5849b662860c5b8ccbe
- check_id: adapter
  name: Structured-source applicability
  status: passed
  required: false
  target_ids:
  - GO:0097740
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  summary: iModulonDB dataset inventory has no matching trypanosome, Leishmania or
    spirochete dataset. Not applicable; absence from the adapter is not biological
    absence.
  scope_note: 2026-10-11T04:48:16Z to 2026-10-11T04:48:17Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/paraflagellar_rod.yaml
  locator: Full native YAML and exact append-only record histories
  accessed_at: '2026-10-11T04:57:45Z'
  snapshot_sha256: e6aac3ef5683759fa8ddc609e8768e2ad265b134bcbd4b1b6012458a713eccdf
  support: context_only
  summary: Pre-mutation native record; original status and historical events retained.
- evidence_id: prior
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: Exact slugs and GO identifiers
  accessed_at: '2026-10-11T04:57:45Z'
  support: context_only
  search_scope: rg --no-ignore --hidden across both review roots included ignored
    files. GitHub all-state bounded query paraflagellar OR periplasmic returned nine
    items, below the 100-result limit.
  summary: 'No earlier exact-target saved review bundle found in these two roots.
    Closed issue #203 concerns introducing an active rotation node, not the static-versus-dynamic
    evidence mismatch; #293 concerns the PFR synonym citation, not family mapping.
    Earlier histories remain authoritative historical observations.'
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289,GO:0097740,GO:0097729,GO:0005930,GO:0055040,GO:0009288,GO:0120100,GO:0071973
  locator: Exact target term and asserted parent/parthood/function terms only
  accessed_at: '2026-10-11T04:49:10Z'
  snapshot_sha256: 58999ee2fac67a7a971a451530f3a1fa4281636cf7762a139ead03851aa01c92
  support: supports
  summary: Active GO identifiers and current relations match the native identity and
    hierarchy. Ontology wording is not experimental validation of uniform molecular
    architecture.
- evidence_id: nomenclature
  kind: primary_source
  reference: DOI:10.1016/j.molbiopara.2004.03.006
  locator: Pages 113-115, Table 1 and Fig. 1; page 114 table visually inspected
  accessed_at: '2026-10-11T04:54:20Z'
  snapshot_sha256: 69f018b31f8a941fc8299e26b811408839e40aaa4d18ed93fbcc26946b8a5e61
  support: supports
  summary: The authors consolidate Trypanosoma PFRC into PFR1 and PFRA into PFR2 while
    keeping Leishmania PFR1/PFR2. Native rows combine these opposite families.
- evidence_id: gadelha
  kind: primary_source
  reference: DOI:10.1128/EC.4.3.516-525.2005
  locator: PCR/hybridization/protein Methods, Results including Fig. 4, Discussion
  accessed_at: '2026-10-11T04:49:46Z'
  snapshot_sha256: 2aa7db460bfb35cc694a11ebbb96bab0f617ce25241f0815bb05e83a09dde144
  support: supports
  summary: Crithidia deanei has a reduced, recognizable PFR. Multiple assays found
    no evidence for PFR2; authors explicitly note individual assay limitations. This
    does not establish universal PFR2 essentiality.
- evidence_id: maga
  kind: primary_source
  reference: DOI:10.1242/jcs.112.16.2753
  locator: Primary abstract and bibliographic identity
  accessed_at: '2026-10-11T04:49:01Z'
  snapshot_sha256: 2f7a51366c951e65437c5f15b351c172406a024b9cae15e4e9caef644e7871ec
  support: supports
  summary: Leishmania PFR1 and PFR2 are both needed for native full PFR formation;
    attachment fibers assemble without the bulk PFR and PFR1 associates with them
    without PFR2.
- evidence_id: bastin1999
  kind: primary_source
  reference: DOI:10.1128/MCB.19.12.8191
  locator: Abstract, tagged-PFRA assembly Results/Fig. 3-5 and Discussion
  accessed_at: '2026-10-11T04:49:46Z'
  snapshot_sha256: f19bf79dcc266852178468925bf656701464c2f645a607402ff9152a31f83ab1
  support: supports
  summary: Tagged PFRA incorporation occurs mostly at the distal tip plus minor incorporation
    along the PFR and in old flagella. The paper uses the pre-consolidation PFRA name.
- evidence_id: alves
  kind: primary_source
  reference: DOI:10.1242/jcs.242271
  locator: Abstract, AF1/AF2 Results, Discussion and Cell culture Methods
  accessed_at: '2026-10-11T04:49:03Z'
  snapshot_sha256: 0299785232aa6f39ab7bc24f3a765d5178ad75ea8dac882ac39ff5a90fb11e5d
  support: supports
  summary: Cytoplasmic AF1/AF2 deletions in TREU927 reduce PFR2 protein and impair
    complete PFR assembly. Proteins can still reach the flagellar tip; a specific
    direct preassembly/chaperone mechanism is not proved.
- evidence_id: portman2009
  kind: primary_source
  reference: DOI:10.1074/jbc.M808859200
  locator: Primary abstract
  accessed_at: '2026-10-11T04:48:51Z'
  snapshot_sha256: 07ed2290ff3bd48c4a3d2c26021944209be57dcadbf6be2784a610ee79568507
  support: supports
  summary: Twenty candidate PFR components from ablation proteomics; a subset localized
    by tagging; calcium/calmodulin links are inferred rather than direct biochemical
    proof.
- evidence_id: portman2010
  kind: primary_source
  reference: DOI:10.1016/j.ijpara.2009.10.005
  locator: Review component-nomenclature, motility, signaling and assembly discussion;
    secondary synthesis
  accessed_at: '2026-10-11T04:48:43Z'
  snapshot_sha256: 0167f87520666792f8df0da2e74db5ccdd09361c4ff23817288a3c65e88bd701
  support: supports
  summary: Distinguishes historical PFRA naming from PFR2; discusses metabolic/signaling
    proteins and proposed regulatory functions, not a resolved universal pathway.
- evidence_id: schlaeppi
  kind: primary_source
  reference: DOI:10.1083/jcb.109.4.1695
  locator: Primary abstract and bibliographic identity only
  accessed_at: '2026-10-11T04:48:53Z'
  snapshot_sha256: 1970cc4c4bdbc5c867ee5cd19181605da78fec083554b7f3218c192a9ad966be
  support: supports
  summary: Helical major PFRA/PFRB protein and tandem genes; original one-protein
    interpretation was superseded by later work.
- evidence_id: deflorin
  kind: primary_source
  reference: PMID:7961827
  locator: Primary abstract and bibliographic identity only
  accessed_at: '2026-10-11T04:49:11Z'
  snapshot_sha256: 122a70a51c9d7c6aa63740eaa21e307441b6d15012d4fd4c0b0fcf1c41c91530
  support: supports
  summary: Distinct PFRA/PFRB and PFRC/PFRD products, not one family defined by their
    ordinal entry names.
- evidence_id: santrich
  kind: primary_source
  reference: PMID:9497035
  locator: Primary abstract and bibliographic identity only
  accessed_at: '2026-10-11T04:49:12Z'
  snapshot_sha256: b3ac8e47ba0be2627a6748b5720ab2dd680f02c7cc4554bd76721ea6724fda3a
  support: supports
  summary: Leishmania PFR2 knockout leaves a residual structure and changes waveform/forward
    swimming.
- evidence_id: farina
  kind: primary_source
  reference: DOI:10.1111/j.1550-7408.1986.tb05661.x
  locator: Primary abstract and bibliographic identity only
  accessed_at: '2026-10-11T04:52:08Z'
  snapshot_sha256: e1c7466c003646f4d42a9f028a3d087fc08a6b349cd7fb192d76275c91ea3fc9
  support: supports
  summary: Publisher-deposited abstract uses paraxial rod for the trypanosomatid lattice
    and attachment fibers; synonym does not equate unrelated dinoflagellate structures.
- evidence_id: bastin1998
  kind: primary_source
  reference: DOI:10.1038/35300
  locator: Publisher abstract at https://www.nature.com/articles/35300
  accessed_at: '2026-10-11T04:57:45Z'
  support: supports
  summary: Antisense ablation of the PFR causes paralysis; only the primary abstract,
    not the subscription body, was read.
- evidence_id: P22225
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/P22225.json
  locator: Gene names, source protein name, taxonomy and family cross-references
  accessed_at: '2026-10-11T04:49:02Z'
  snapshot_sha256: e9fd789dbe1615208b024eff8c4850050bd365de17a4bb4104f71185c8d4e3da
  support: supports
  summary: Accession/gene identity is valid; UniProt mnemonic numbering is not evidence
    of consolidated cross-species PFR orthology.
- evidence_id: Q26789
  kind: authority
  reference: https://rest.uniprot.org/uniprotkb/Q26789.json
  locator: Gene names, source protein name, taxonomy and family cross-references
  accessed_at: '2026-10-11T04:49:03Z'
  snapshot_sha256: 740b985563ff51101f509560098d2d11ffebe123355e9dcabf6b6a34eb4e841e
  support: supports
  summary: Accession/gene identity is valid; UniProt mnemonic numbering is not evidence
    of consolidated cross-species PFR orthology.
- evidence_id: interpro-IPR007824
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR007824/
  locator: Exact family metadata
  accessed_at: '2026-10-11T04:52:09Z'
  snapshot_sha256: 251040399d98feb59cd5fe36028e0a59e5e8863503c1baaec69d60516e0b2c69
  support: supports
  summary: Broad PFR family rather than a single orthologous PFR1 or PFR2 subset.
- evidence_id: pfam-PF05149
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF05149/
  locator: Exact family metadata
  accessed_at: '2026-10-11T04:52:11Z'
  snapshot_sha256: d75646fb227cba1e9b75b8bfa0485fe84b53f3e6ebdc531b534d6671e60f3668
  support: supports
  summary: Broad PFR family rather than a single orthologous PFR1 or PFR2 subset.
- evidence_id: taxon-5702
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/5702.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T04:49:05Z'
  snapshot_sha256: c67df4b375befd0adb7824e405a17fdd005aa6b3def611b3f68c1f1f4f7bd3ae
  support: supports
  summary: Taxon identity and rank match the native distribution/example at its stated
    scope.
- evidence_id: taxon-5665
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/5665.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T04:49:07Z'
  snapshot_sha256: 7e2b33e45ecf627dbb40cc7bae5c9642493bd1aefdf8c7c97b2225ddda2fa76a
  support: supports
  summary: Taxon identity and rank match the native distribution/example at its stated
    scope.
- evidence_id: taxon-2759
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2759.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T04:49:06Z'
  snapshot_sha256: af5ba762219fdecb11d214126bb8184c0eb28fc6474d14777c4aaa7f7dd89369
  support: supports
  summary: Taxon identity and rank match the native distribution/example at its stated
    scope.
- evidence_id: taxon-33682
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/33682.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T04:49:06Z'
  snapshot_sha256: 95e0d436648994b80ea855704c8d985fa4cbc9f5a6284c12948dff363e3e8a9c
  support: supports
  summary: Taxon identity and rank match the native distribution/example at its stated
    scope.
assessments:
- assessment_id: identity
  area: identity
  topic: GO identity, definition, parthood and synonym
  outcome: supported
  target_ids:
  - GO:0097740
  evidence_ids:
  - record
  - go
  - farina
  summary: Exact PFR term and 9+2 motile cilium parthood are supported; paraxial rod
    remains a related historical synonym.
- assessment_id: components
  area: grounding
  topic: Paralogue families, examples and required composition
  outcome: concern
  target_ids:
  - GO:0097740
  evidence_ids:
  - nomenclature
  - P22225
  - Q26789
  - gadelha
  - maga
  - schlaeppi
  - deflorin
  summary: Valid accessions are assigned to opposite consolidated families; PFR2 essentiality
    also exceeds the generic record scope that includes reduced PFRs.
- assessment_id: scope
  area: scope
  topic: Distribution and examples
  outcome: supported
  target_ids:
  - GO:0097740
  evidence_ids:
  - gadelha
  - deflorin
  - alves
  - maga
  - taxon-5702
  - taxon-5665
  - taxon-2759
  - taxon-33682
  summary: Rare protist distribution and variable kinetoplastid architecture are supported.
    Reduced PFRs remain in record scope.
- assessment_id: functions
  area: evidence
  topic: Three functions and assembly graph
  outcome: concern
  target_ids:
  - GO:0097740
  evidence_ids:
  - bastin1998
  - santrich
  - bastin1999
  - alves
  - portman2009
  - portman2010
  - maga
  - nomenclature
  summary: Motility, assembly-factor boundary and qualified signaling-platform descriptions
    are supported. The PFRA-tracking edge incorrectly calls PFRA PFR1; graph context
    must distinguish full-model assembly from reduced rods.
- assessment_id: provenance
  area: provenance
  topic: Status, histories, optional fields and source access
  outcome: supported
  target_ids:
  - GO:0097740
  evidence_ids:
  - record
  summary: PROPOSED status and append-only histories remain unchanged. No asserted
    images, physical measurements, trait links or datasets require additional verification.
    Unpopulated optional fields are not defects.
findings:
- finding_id: F1
  issue_key: paraflagellar-rod-pfr-family-conflation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Reconcile PFR1/PFR2 orthology with historical PFRC/PFRA names
  description: The record maps 69 kDa PFRA/PFRB (P22225) to PFR1 and 73 kDa PFRC/PFRD
    (Q26789) to PFR2 while importing Leishmania PFR1/PFR2 roles. Gadelha 2004 Table
    1 and Fig. 1 explicitly consolidate PFRC as PFR1 and PFRA as PFR2. The tagged-PFRA
    edge is consequently assigned to the wrong modern family. Valid accessions and
    source labels do not make these orthology assignments valid.
  target_ids:
  - GO:0097740
  field_paths:
  - components[0]
  - components[1]
  - causal_graphs[0].nodes
  - causal_graphs[0].edges[0]
  evidence_ids:
  - record
  - nomenclature
  - P22225
  - Q26789
  - bastin1999
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/paraflagellar_rod.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material component identity, scope or edge-evidence defect;
    the structure record itself retains valid identity.
- finding_id: F2
  issue_key: paraflagellar-rod-pfr2-essentiality-scope
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Qualify PFR2 requirement for full versus reduced rods
  description: ESSENTIAL means the structure does not form without the component.
    The generic record explicitly includes cryptic/reduced PFRs, yet gives PFR2 unqualified
    ESSENTIAL status. Gadelha 2005 imaged a reduced Crithidia deanei rod and found
    no PFR2 with multiple techniques, retaining assay limitations. Leishmania loss
    experiments establish a requirement for full native architecture rather than all
    recognizable PFR material.
  target_ids:
  - GO:0097740
  field_paths:
  - components[1].essentiality
  - components[1].role
  - causal_graphs[0].description
  - causal_graphs[0].edges[1]
  evidence_ids:
  - record
  - gadelha
  - maga
  - santrich
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/paraflagellar_rod.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material component identity, scope or edge-evidence defect;
    the structure record itself retains valid identity.
actions:
- action_id: A1
  description: Reconcile PFR1/PFR2 orthology with historical PFRC/PFRA names
  finding_ids:
  - F1
  target_ids:
  - GO:0097740
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/paraflagellar_rod.yaml
    role: maintained scientific record
  acceptance_checks:
  - Keep stable pfr1/pfr2 component IDs but align modern PFR1 with PFRC/PFRD and Q26789,
    and PFR2 with PFRA/PFRB and P22225.
  - Move gene symbols, examples and experimental citations together; correct graph
    labels and the tagged-PFRA edge.
  - Preserve source-native UniProt names and historical curation events; document
    the nomenclature crosswalk explicitly.
  - Use the guarded writer, preserve prior histories and PROPOSED status, append EDIT
    provenance, regenerate affected products and pass focused tests plus authoritative
    QC.
- action_id: A2
  description: Qualify PFR2 requirement for full versus reduced rods
  finding_ids:
  - F2
  target_ids:
  - GO:0097740
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/paraflagellar_rod.yaml
    role: maintained scientific record
  acceptance_checks:
  - Use a lineage/context-qualified essentiality value and explain the full-native
    versus reduced-rod boundary.
  - Retain the Leishmania native-assembly result and the reduced Crithidia observation
    with detection limits.
  - Scope the assembly graph to the examined model lineages; do not claim an experimentally
    demonstrated universal gene absence.
  - Use the guarded writer, preserve prior histories and PROPOSED status, append EDIT
    provenance, regenerate affected products and pass focused tests plus authoritative
    QC.
limitations:
- Bastin 1998, Maga 1999, Santrich 1997, Deflorin 1994, Schlaeppi 1989 and Farina
  1986 were assessed at primary-abstract level for their bounded native claims; unseen
  bodies and supplements are not claimed as reviewed.
- Gadelha 2004 nomenclature table was visually checked. Gadelha 2005, Bastin 1999
  and Alves 2020 relevant main-text experiments were inspected; Portman 2010 is secondary
  synthesis and Portman 2009 was inspected at abstract level.
- Same-agent review, not independent human sign-off or completion of the 909-record
  goal.
- Exact-baseline CI supplies full QC; skipped namespaces, unexercised BFO controls
  and non-adapter label pairs are explicit limits.
- No relevant iModulonDB coverage. No quoted snippets to verify; identifier/label
  validation cannot establish scientific accuracy.
```
