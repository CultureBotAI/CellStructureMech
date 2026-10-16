# Phycobilisome core experimental-state and preparation-scope review

- Review: 20261012T093217Z-phycobilisome-core-source-scope
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T09:26:37Z
- Finished UTC: 2026-10-12T09:32:17Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole-record review completed with two major source-scope findings: unsupported photoprotected states under the2021 citation and an overstatement of intact core/rod reconstruction in the2022 example. The earlier PCC7002 taxon correction remains supported; identity, hierarchy, grouped components and coarse graph are otherwise supported within stated reading limits.

## Scope And Provenance

One entire native core record, all three components, both organism examples, all six graph edges, both histories and its exact legacy review; no sampling.

Selection: data/structures/energy_complex/phycobilisome_core.yaml
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e74d0c3e33df7e44348afbba1695b61c23262ab0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:phycobilisome_core | data/structures/energy_complex/phycobilisome_core.yaml | maintained | phycobilisome core |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:phycobilisome_core | Fresh target gate. Actual run: 2026-10-12T09:27:44Z to 2026-10-12T09:27:53Z. |
| strict | passed | True | cellstructuremech:phycobilisome_core | Fresh target gate. Actual run: 2026-10-12T09:27:53Z to 2026-10-12T09:28:00Z. |
| snippets | passed | True | cellstructuremech:phycobilisome_core | Fresh target gate. Zero of32 citations carries a snippet. Actual run: 2026-10-12T09:28:00Z to 2026-10-12T09:28:23Z. |
| reused-release-qc | passed | True | cellstructuremech:phycobilisome_core | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped, labels603 no-adapter skips and cached trait index. Actual run: 2026-10-12T06:33:07Z to 2026-10-12T06:45:16Z. |
| reused-release-labels | passed | True | cellstructuremech:phycobilisome_core | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped, labels603 no-adapter skips and cached trait index. Actual run: 2026-10-12T06:45:16Z to 2026-10-12T06:47:16Z. |
| reused-release-traits | passed | True | cellstructuremech:phycobilisome_core | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped, labels603 no-adapter skips and cached trait index. Actual run: 2026-10-12T06:48:15Z to 2026-10-12T06:48:52Z. |
| reused-curies-live | passed | True | cellstructuremech:phycobilisome_core | Verified result reuse: live CURIE4023OK/251skips, archive204valid, contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T07:05:41Z to 2026-10-12T07:10:58Z. |
| reused-post-save-archive | passed | True | cellstructuremech:phycobilisome_core | Verified result reuse: live CURIE4023OK/251skips, archive204valid, contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T09:22:18Z to 2026-10-12T09:23:49Z. |
| reused-post-save-contract | passed | True | cellstructuremech:phycobilisome_core | Verified result reuse: live CURIE4023OK/251skips, archive204valid, contract4passed. Fresh post-save checks follow. Actual run: 2026-10-12T09:23:49Z to 2026-10-12T09:25:18Z. |
| adapter-datasets | passed | False | cellstructuremech:phycobilisome_core | Fresh complete inventory; no exact organism dataset applies. Actual run: 2026-10-12T09:27:48Z to 2026-10-12T09:27:50Z. |

## Scientific And Domain Assessments

### Minted core identity and whole/part distinction

identity: supported. Targets: cellstructuremech:phycobilisome_core.

A named allophycocyanin-containing core is a valid light-harvesting subassembly, not the whole phycobilisome or a single protein. Parentage and parthood preserve that boundary. Coreless PBS alternatives do not invalidate this explicitly core-specific child record.

### All three constituent groups and rejected near matches

grounding: supported. Targets: cellstructuremech:phycobilisome_core.

ApcA/B core proteins, mixed ApcC/D/E/F linkers/emitters and bound bilins are supported coarse categories. The named InterPro exclusions are correct; deferred mixed-set grounding is not a claim that no narrower term exists. No universal exact stoichiometry or viability requirement is asserted for the mixed linker group.

### Qualitative cyanobacterial and red-algal occurrence

scope: supported. Targets: cellstructuremech:phycobilisome_core.

COMMON is qualitative occurrence of core-bearing PBS in these lineages, not proof that every cyanobacterium or every alternative antenna has a core. The primary comparison and review support the stated broad occurrence without measured prevalence.

### Canonical organisms and preparation context

provenance: concern. Targets: cellstructuremech:phycobilisome_core.

The PCC7002 replacement is supported, so the earlier taxon problem is no longer present in current bytes. Both current labels resolve correctly. The T.vulcanus example overstates the intactness of the reconstructed assembly.

### Core-linker state attribution and authors

evidence: concern. Targets: cellstructuremech:phycobilisome_core.

The2021 source supports structural core constituents but not the specific photoprotected-state claim in the linker evidence note. Repeated Sauer2021 author wording also conflicts with the DOI metadata. Correct scientific scope and bibliographic attribution together without undoing the valid taxon fix.

### Core-mediated light harvesting

evidence: supported. Targets: cellstructuremech:phycobilisome_core.

Absorption/transfer through bilins and terminal emitters is supported for this core-specific structure. GO0009765 is a compatible biological-process grounding. Proposed detailed energetic routes are not treated as measured trajectories.

### All six NONMECHANISTIC edges

graph: supported. Targets: cellstructuremech:phycobilisome_core.

Core proteins assemble; linkers stabilize/tune; bilins are bound; rods supply excitation; the core routes excitation toward photosystems and contributes to light harvesting. This is an explicitly coarse graph that excludes detailed excitonic and photoprotective rearrangements. Correct author notes without importing the unsupported component-state assertion into the graph.

### Grounding/boundary discussions and optional fields

completeness: supported. Targets: cellstructuremech:phycobilisome_core.

Both discussions are relevant and consistent with retained subassembly identity. No missing required image, physical quantity, protein example, trait or dataset slot was established. Do not force optional additions or infer absence from adapter coverage.

### Native gates and reference identity

schema: supported. Targets: cellstructuremech:phycobilisome_core.

All native stable GO, taxonomy, DOI and InterPro references resolve. Automatic validation does not establish organism/state-specific source support. Fresh target gates and verified reused wider gates are distinguished.

### Status, histories and review lineage

ownership: supported. Targets: cellstructuremech:phycobilisome_core.

Entire native file, both histories and exact legacy report read. Maintained YAML owns future guarded corrections; all earlier data/history/review bytes and PROPOSED status remain unchanged. The legacy taxon fix is acknowledged without inventing canonical finding lineage.

## Findings

### F1: Remove the unsupported photoprotected-state attribution and correct the2021 authors

major / open / confirmed; issue key: phycobilisome-core-photoprotected-source-conflation.

The core-linker evidence note says the cited2021 paper modeled light-harvesting and photoprotected PBS states. Its structural preparations were not light stressed and no OCP was observed. The DOI belongs to Zheng et al., not Sauer. Restrict the note to supported architecture/transfer claims and correct repeated author attribution. The already corrected PCC7002 example is supported and must not be reverted.

### F2: Distinguish separate core/rod structures from an intact resolved antenna

major / open / confirmed; issue key: phycobilisome-core-kawakami-preparation-scope.

The T.vulcanus canonical example says core and rods were resolved in an intact PBS. The cited study instead reconstructed separate core and dissociated rod preparations; limited residual rod density around the core was not modeled at the same detail. Qualify the example to match the inspected experimental preparation and reconstructed objects without denying intact starting material or residual rod density.

## Recommended Actions And Acceptance Checks

### A1

Correct2021 author notes and remove the unsupported photoprotected-state attribution, or add independently inspected, correctly scoped evidence for any retained state-specific claim. Preserve the PCC7002 correction.

- The linker note no longer claims that Zheng2021 resolved photoprotected structures.
- Every author/year note attached to the2021 DOI agrees with its bibliographic identity.
- The supported PCC7002 canonical example and coarse graph scope remain intact.
- Guarded curation/history, retained PROPOSED status, native gates and lineage-linked successor review.

### A2

Describe the T.vulcanus core and rod results as separate reconstructions with preparation context, rather than a jointly resolved intact PBS.

- The example preserves the distinction between intact starting material, dissociated preparations, residual density and detailed reconstructed models.
- Species identity and the supported core/rod result remain intact.
- Validate guarded native changes and save a successor retaining this stable issue key.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/energy_complex/phycobilisome_core.yaml; Entire YAML, two append-only history files and exact legacy review | supports | The core is explicitly distinct from whole PBS and rods. A prior edit corrected the canonical organism to PCC7002, but a core-linker note still attributes photoprotected states to the2021 study and all its author notes still say Sauer. The T.vulcanus example claims core and rods were resolved in an intact PBS. |
| go | GO:0030076; GO:0030089; GO:0009765; All three current terms, definitions, names and aspects | supports | Light-harvesting-complex parent, whole-phycobilisome container and light-harvesting process are compatible with a locally minted core subassembly. No whole-PBS GO ID is substituted for the core. |
| zheng | https://doi.org/10.1038/s41467-021-25813-y; Complete abstract and authors; overall/core structure, linkers, bilin-environment and strains/growth sections | partial | Zheng et al.2021 directly studied PCC7002/PCC7120 and reported no OCP in either structural preparation because cultures were not light stressed. The study supports core organization, terminal emitters and bounded energy-transfer interpretation, not the claimed photoprotected structural states. |
| kawakami | https://doi.org/10.1038/s41467-022-30962-9; Complete abstract; subunit composition, core purification/refinement, PC-rod structure and preparation sections; publisher text also inspected | partial | Kawakami et al.2022 used T.vulcanus NIES2134 and reconstructed the core and dissociated rods separately. Some rod density remains around the core, but its limited local resolution prevented a rod model there. Preparation and reconstruction must not be described as an intact, jointly resolved antenna. |
| sui | https://doi.org/10.1146/annurev-biophys-062920-063657; Fresh complete secondary-review abstract and bibliographic identity; not the full review | supports | Sui2021 summarizes phycobiliprotein/linker architecture and energy transfer in cyanobacteria and red algae. Its broad assertions are corroborated by the inspected primary papers and InterPro descriptions. A fresh author-PDF open timed out; no unread later passage is relied on. |
| ipr-broad | InterPro:IPR012128; Complete entry description, hierarchy and member signatures | supports | Family contains both rod and core alpha/beta phycobiliproteins; its use as a rejected near match for an allophycocyanin-only group is justified. |
| ipr-beta | InterPro:IPR006245; Complete entry description, hierarchy and member signatures | supports | This is the allophycocyanin beta-subunit branch, not the complete alpha/beta constituent set. |
| ipr-linker | InterPro:IPR011134; Complete entry description and member signatures | supports | The allophycocyanin-linker family does not represent the entire mixed ApcC/D/E/F core-linker and terminal-emitter set. |
| legacy | reports/yaml_record_review/2026-10-03T021514Z-phycobilisome_core.md; Entire historical report and its corresponding native history event | supports | The legacy report says issue1961 corrected the unsupported PCC6803 example to PCC7002. Current bytes and primary evidence corroborate that bounded correction. It is not a canonical predecessor, and this review neither reopens that taxon defect nor claims fresh remote issue/PR status. |
| adapter | https://imodulondb.org/; Fresh complete28-dataset inventory | supports | No exact PCC7002 or T.vulcanus dataset applies; S.elongatus coverage is not substituted. No applicable gene query and no biological absence inference. |
| validation | /private/tmp/csm-review-20261012T092625Z-core/baseline-verification.json; Fresh target gates and hash-verified unchanged-input wider checks | supports | Schema and strict checks pass; zero of32 citations carries a snippet. Reused QC987passed/3skipped, cached labels/traits, live CURIE4023OK/251skips and204-bundle archive/four contract tests retain their original scope. Fresh post-save archive checks follow. |
| search | reviews/structured/; Ignored-inclusive canonical and native/legacy searches | supports | Exact minted ID identifies one native target. No canonical predecessor among204 bundles and no existing occurrence of either new issue key. One exact historical report was read, not overwritten or promoted into a fabricated canonical predecessor. |
| tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; Complete current taxonomy entry | supports | Native identifier and label agree. PCC7002 includes historical Synechococcus naming; T.vulcanus includes historical Thermosynechococcus naming where relevant. |
| tax-2763 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2763; Complete current taxonomy entry | supports | Native identifier and label agree. PCC7002 includes historical Synechococcus naming; T.vulcanus includes historical Thermosynechococcus naming where relevant. |
| tax-32049 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32049; Complete current taxonomy entry | supports | Native identifier and label agree. PCC7002 includes historical Synechococcus naming; T.vulcanus includes historical Thermosynechococcus naming where relevant. |
| tax-32053 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053; Complete current taxonomy entry | supports | Native identifier and label agree. PCC7002 includes historical Synechococcus naming; T.vulcanus includes historical Thermosynechococcus naming where relevant. |

## Limits And Additional Notes

- Same-agent whole-record review, not independent human sign-off, exhaustive literature/retraction search or raw experimental reanalysis.
- Primary papers were read in the selected abstract/Results/Methods sections identified in Evidence, not every figure pixel, supplementary item or raw map. Uncertain ApcD/CpcG assignments and inferred transfer paths are not upgraded to experimentally resolved specificity or motion.
- Sui2021 was freshly inspected as complete abstract and metadata; a renewed author-PDF request timed out. Broad architecture/energy-transfer claims are independently corroborated by the inspected primary papers and InterPro descriptions. No assertion about unread later review sections supports a finding.
- All17 local HTTP captures returned200, but the first Kawakami body URL used the wrong PMC ID and returned unrelated DOI10.1038/s41598-022-09654-3. Identity checking rejected it; the correct PMC9205905 article was fetched from the verified DOI metadata and used instead. The mismatched capture is retained, not treated as supporting evidence.
- The historical taxon correction is verified against current native bytes and literature; remote issue1961/PR1960 status was not refreshed, and no canonical predecessor or terminal disposition is invented.
- Fresh target checks plus checksum-verified wider-check reuse with original test/cache/no-adapter limitations. No exact iModulonDB dataset and no target trait links; absence from that inventory is not negative biological evidence.
- No native scientific edits, history/status changes, generated-product changes or GitHub mutation. Existing publication approval remains unanswered; no bypass or retry.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T093217Z-phycobilisome-core-source-scope
kind: record
repository: CultureBotAI/CellStructureMech
title: Phycobilisome core experimental-state and preparation-scope review
started_at: '2026-10-12T09:26:37Z'
finished_at: '2026-10-12T09:32:17Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same coding-agent context; no independent reviewer or human
    sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: 'Whole-record review completed with two major source-scope findings: unsupported
  photoprotected states under the2021 citation and an overstatement of intact core/rod
  reconstruction in the2022 example. The earlier PCC7002 taxon correction remains
  supported; identity, hierarchy, grouped components and coarse graph are otherwise
  supported within stated reading limits.'
source:
  git_revision: e74d0c3e33df7e44348afbba1695b61c23262ab0
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
  - path: data/structures/energy_complex/phycobilisome_core.yaml
    sha256: 486621e10b34c44f9682dfafaed1b1563fd632bd423e96d0c7e27702fae035fb
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
  - path: history/records/phycobilisome_core/2026-10-03T014904Z-codex-584101.yaml
    sha256: 8c23c2037987395f5b1b412fc21f2f2e2b29759bb39ce71e23c7efb885bdb17d
    role: context
  - path: history/records/phycobilisome_core/2026-10-03T020241Z-claude-code-9bde15.yaml
    sha256: eca88e2d618342e689d3499f02caa156d6f914958c37fcd0c2fcfd5dd53a6ed1
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/yaml_record_review/2026-10-03T021514Z-phycobilisome_core.md
    sha256: e3581255f6bf4b5b368b7a0bf37c06a400828e34d1f96a79cca30555d5588c51
    role: context
  - path: schema/record_review.yaml
    sha256: 229baf9b69118a1fe318e4c31085c0820e4e3d1365e7b04d6ace451b7c35f9bb
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: cellstructuremech:phycobilisome_core
  path: data/structures/energy_complex/phycobilisome_core.yaml
  label: phycobilisome core
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_core.yaml
    role: maintained scientific record
scope:
  description: One entire native core record, all three components, both organism
    examples, all six graph edges, both histories and its exact legacy review; no
    sampling.
  selection: data/structures/energy_complex/phycobilisome_core.yaml
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:phycobilisome_core
checks:
- check_id: schema
  name: schema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/phycobilisome_core.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Actual run: 2026-10-12T09:27:44Z to 2026-10-12T09:27:53Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  command: .venv/bin/python scripts/validate_strict.py data/structures/energy_complex/phycobilisome_core.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Actual run: 2026-10-12T09:27:53Z to 2026-10-12T09:28:00Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: snippets
  name: snippets
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/energy_complex/phycobilisome_core.yaml
    --report /private/tmp/csm-review-20261012T092625Z-core/snippets.md
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Zero of32 citations carries a snippet. Actual run:
    2026-10-12T09:28:00Z to 2026-10-12T09:28:23Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: reused-release-qc
  name: reused-release-qc
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped,
    labels603 no-adapter skips and cached trait index. Actual run: 2026-10-12T06:33:07Z
    to 2026-10-12T06:45:16Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: reused-release-labels
  name: reused-release-labels
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped,
    labels603 no-adapter skips and cached trait index. Actual run: 2026-10-12T06:45:16Z
    to 2026-10-12T06:47:16Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: reused-release-traits
  name: reused-release-traits
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped,
    labels603 no-adapter skips and cached trait index. Actual run: 2026-10-12T06:48:15Z
    to 2026-10-12T06:48:52Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: reused-curies-live
  name: reused-curies-live
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified result reuse: live CURIE4023OK/251skips, archive204valid, contract4passed.
    Fresh post-save checks follow. Actual run: 2026-10-12T07:05:41Z to 2026-10-12T07:10:58Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: reused-post-save-archive
  name: reused-post-save-archive
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified result reuse: live CURIE4023OK/251skips, archive204valid, contract4passed.
    Fresh post-save checks follow. Actual run: 2026-10-12T09:22:18Z to 2026-10-12T09:23:49Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: reused-post-save-contract
  name: reused-post-save-contract
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Verified result reuse: live CURIE4023OK/251skips, archive204valid, contract4passed.
    Fresh post-save checks follow. Actual run: 2026-10-12T09:23:49Z to 2026-10-12T09:25:18Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
- check_id: adapter-datasets
  name: adapter-datasets
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh complete inventory; no exact organism dataset applies. Actual run:
    2026-10-12T09:27:48Z to 2026-10-12T09:27:50Z.'
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - adapter
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/energy_complex/phycobilisome_core.yaml
  locator: Entire YAML, two append-only history files and exact legacy review
  summary: The core is explicitly distinct from whole PBS and rods. A prior edit corrected
    the canonical organism to PCC7002, but a core-linker note still attributes photoprotected
    states to the2021 study and all its author notes still say Sauer. The T.vulcanus
    example claims core and rods were resolved in an intact PBS.
  support: supports
  accessed_at: '2026-10-12T09:32:17Z'
  snapshot_sha256: 486621e10b34c44f9682dfafaed1b1563fd632bd423e96d0c7e27702fae035fb
- evidence_id: go
  kind: authority
  reference: GO:0030076; GO:0030089; GO:0009765
  locator: All three current terms, definitions, names and aspects
  summary: Light-harvesting-complex parent, whole-phycobilisome container and light-harvesting
    process are compatible with a locally minted core subassembly. No whole-PBS GO
    ID is substituted for the core.
  support: supports
  accessed_at: '2026-10-12T09:27:23Z'
  snapshot_sha256: b4871465e93372dd482ee7d60e01d82de4f68e4c30c501145f24f31a738ea20f
- evidence_id: zheng
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-021-25813-y
  locator: Complete abstract and authors; overall/core structure, linkers, bilin-environment
    and strains/growth sections
  summary: Zheng et al.2021 directly studied PCC7002/PCC7120 and reported no OCP in
    either structural preparation because cultures were not light stressed. The study
    supports core organization, terminal emitters and bounded energy-transfer interpretation,
    not the claimed photoprotected structural states.
  support: partial
  accessed_at: '2026-10-12T09:28:16Z'
  snapshot_sha256: 1726fe18d49fc2e19a9fe0846a7d6879eb72b486b58cf84cd033d33794251ef1
- evidence_id: kawakami
  kind: primary_source
  reference: https://doi.org/10.1038/s41467-022-30962-9
  locator: Complete abstract; subunit composition, core purification/refinement, PC-rod
    structure and preparation sections; publisher text also inspected
  summary: Kawakami et al.2022 used T.vulcanus NIES2134 and reconstructed the core
    and dissociated rods separately. Some rod density remains around the core, but
    its limited local resolution prevented a rod model there. Preparation and reconstruction
    must not be described as an intact, jointly resolved antenna.
  support: partial
  accessed_at: '2026-10-12T09:28:49Z'
  snapshot_sha256: d428f0c1cc2ccea5b0e4e343d5841355b892f65e6cb694481ee1ff13c9087713
- evidence_id: sui
  kind: authority
  reference: https://doi.org/10.1146/annurev-biophys-062920-063657
  locator: Fresh complete secondary-review abstract and bibliographic identity; not
    the full review
  summary: Sui2021 summarizes phycobiliprotein/linker architecture and energy transfer
    in cyanobacteria and red algae. Its broad assertions are corroborated by the inspected
    primary papers and InterPro descriptions. A fresh author-PDF open timed out; no
    unread later passage is relied on.
  support: supports
  accessed_at: '2026-10-12T09:27:31Z'
  snapshot_sha256: 3b34576930f6587e4869a25f3956bb75a65884be66ad2fbd0c3b77cec53c2436
- evidence_id: ipr-broad
  kind: database
  reference: InterPro:IPR012128
  locator: Complete entry description, hierarchy and member signatures
  summary: Family contains both rod and core alpha/beta phycobiliproteins; its use
    as a rejected near match for an allophycocyanin-only group is justified.
  support: supports
  accessed_at: '2026-10-12T09:27:28Z'
  snapshot_sha256: 7de870a6ff5da7e35feb341d61ad7f902c7f7d78fcb8370e124adf8a85728c58
- evidence_id: ipr-beta
  kind: database
  reference: InterPro:IPR006245
  locator: Complete entry description, hierarchy and member signatures
  summary: This is the allophycocyanin beta-subunit branch, not the complete alpha/beta
    constituent set.
  support: supports
  accessed_at: '2026-10-12T09:27:29Z'
  snapshot_sha256: 16c1ecfc2c9ce37da9b04513aefbaf769ec70844fcc4cfbb84b418604c6c70ba
- evidence_id: ipr-linker
  kind: database
  reference: InterPro:IPR011134
  locator: Complete entry description and member signatures
  summary: The allophycocyanin-linker family does not represent the entire mixed ApcC/D/E/F
    core-linker and terminal-emitter set.
  support: supports
  accessed_at: '2026-10-12T09:27:30Z'
  snapshot_sha256: f88e7e1294e9efcd44a3ce7ef9a382f9802f95644f616ae8f44185d483a225a2
- evidence_id: legacy
  kind: prior_review
  reference: reports/yaml_record_review/2026-10-03T021514Z-phycobilisome_core.md
  locator: Entire historical report and its corresponding native history event
  summary: The legacy report says issue1961 corrected the unsupported PCC6803 example
    to PCC7002. Current bytes and primary evidence corroborate that bounded correction.
    It is not a canonical predecessor, and this review neither reopens that taxon
    defect nor claims fresh remote issue/PR status.
  support: supports
  accessed_at: '2026-10-12T09:32:17Z'
  snapshot_sha256: e3581255f6bf4b5b368b7a0bf37c06a400828e34d1f96a79cca30555d5588c51
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: Fresh complete28-dataset inventory
  summary: No exact PCC7002 or T.vulcanus dataset applies; S.elongatus coverage is
    not substituted. No applicable gene query and no biological absence inference.
  support: supports
  accessed_at: '2026-10-12T09:32:17Z'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/csm-review-20261012T092625Z-core/baseline-verification.json
  locator: Fresh target gates and hash-verified unchanged-input wider checks
  summary: Schema and strict checks pass; zero of32 citations carries a snippet. Reused
    QC987passed/3skipped, cached labels/traits, live CURIE4023OK/251skips and204-bundle
    archive/four contract tests retain their original scope. Fresh post-save archive
    checks follow.
  support: supports
  accessed_at: '2026-10-12T09:32:17Z'
- evidence_id: search
  kind: search
  reference: reviews/structured/
  locator: Ignored-inclusive canonical and native/legacy searches
  summary: Exact minted ID identifies one native target. No canonical predecessor
    among204 bundles and no existing occurrence of either new issue key. One exact
    historical report was read, not overwritten or promoted into a fabricated canonical
    predecessor.
  support: supports
  accessed_at: '2026-10-12T09:32:17Z'
  search_scope: Path.rglob includes hidden/ignored canonical bundles. rg -uu searched
    target slug, identifier and new issue keys across data/structures, reviews, reports/yaml_record_review,
    history, research and curation. No remote issue-absence claim.
- evidence_id: tax-1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: Complete current taxonomy entry
  summary: Native identifier and label agree. PCC7002 includes historical Synechococcus
    naming; T.vulcanus includes historical Thermosynechococcus naming where relevant.
  support: supports
  accessed_at: '2026-10-12T09:27:24Z'
  snapshot_sha256: 902dbbe6c250ccb733ac96b08f75a20556e8fbc50c444a8a05c354ff5296cddf
- evidence_id: tax-2763
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/2763
  locator: Complete current taxonomy entry
  summary: Native identifier and label agree. PCC7002 includes historical Synechococcus
    naming; T.vulcanus includes historical Thermosynechococcus naming where relevant.
  support: supports
  accessed_at: '2026-10-12T09:27:25Z'
  snapshot_sha256: 73c5fb9f4e663ee9f81162bbef7158f567879f7e39c91ee4823564289385434b
- evidence_id: tax-32049
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32049
  locator: Complete current taxonomy entry
  summary: Native identifier and label agree. PCC7002 includes historical Synechococcus
    naming; T.vulcanus includes historical Thermosynechococcus naming where relevant.
  support: supports
  accessed_at: '2026-10-12T09:27:26Z'
  snapshot_sha256: db9dcb971953c78f85dd40d12ea88152c3fc6aaaf022411c443f9cb666411f92
- evidence_id: tax-32053
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/32053
  locator: Complete current taxonomy entry
  summary: Native identifier and label agree. PCC7002 includes historical Synechococcus
    naming; T.vulcanus includes historical Thermosynechococcus naming where relevant.
  support: supports
  accessed_at: '2026-10-12T09:27:27Z'
  snapshot_sha256: fc530968cc8ae8239a8d2d36338d08aa9d41b347fa96df0ad41db960f4a7fbb9
assessments:
- assessment_id: identity
  area: identity
  topic: Minted core identity and whole/part distinction
  outcome: supported
  summary: A named allophycocyanin-containing core is a valid light-harvesting subassembly,
    not the whole phycobilisome or a single protein. Parentage and parthood preserve
    that boundary. Coreless PBS alternatives do not invalidate this explicitly core-specific
    child record.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - go
  - zheng
  - kawakami
- assessment_id: components
  area: grounding
  topic: All three constituent groups and rejected near matches
  outcome: supported
  summary: ApcA/B core proteins, mixed ApcC/D/E/F linkers/emitters and bound bilins
    are supported coarse categories. The named InterPro exclusions are correct; deferred
    mixed-set grounding is not a claim that no narrower term exists. No universal
    exact stoichiometry or viability requirement is asserted for the mixed linker
    group.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - ipr-broad
  - ipr-beta
  - ipr-linker
  - zheng
  - kawakami
- assessment_id: distribution
  area: scope
  topic: Qualitative cyanobacterial and red-algal occurrence
  outcome: supported
  summary: COMMON is qualitative occurrence of core-bearing PBS in these lineages,
    not proof that every cyanobacterium or every alternative antenna has a core. The
    primary comparison and review support the stated broad occurrence without measured
    prevalence.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - sui
  - zheng
  - tax-1117
  - tax-2763
- assessment_id: examples
  area: provenance
  topic: Canonical organisms and preparation context
  outcome: concern
  summary: The PCC7002 replacement is supported, so the earlier taxon problem is no
    longer present in current bytes. Both current labels resolve correctly. The T.vulcanus
    example overstates the intactness of the reconstructed assembly.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - legacy
  - zheng
  - kawakami
  - tax-32049
  - tax-32053
  dimensions:
  - name: specimen
    value: Thermostichus vulcanus / historical Thermosynechococcus vulcanus NIES2134
    definition: Source organism agrees; the finding concerns specimen preparation
      and reconstruction, not taxonomic identity.
    evidence_ids:
    - tax-32053
    - kawakami
  - name: reconstruction_scope
    value: Separate core and dissociated rod reconstructions
    definition: Distinguishes detailed models from lower-resolution residual rod density
      around the core.
    evidence_ids:
    - kawakami
- assessment_id: states
  area: evidence
  topic: Core-linker state attribution and authors
  outcome: concern
  summary: The2021 source supports structural core constituents but not the specific
    photoprotected-state claim in the linker evidence note. Repeated Sauer2021 author
    wording also conflicts with the DOI metadata. Correct scientific scope and bibliographic
    attribution together without undoing the valid taxon fix.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - zheng
  - legacy
- assessment_id: function
  area: evidence
  topic: Core-mediated light harvesting
  outcome: supported
  summary: Absorption/transfer through bilins and terminal emitters is supported for
    this core-specific structure. GO0009765 is a compatible biological-process grounding.
    Proposed detailed energetic routes are not treated as measured trajectories.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - go
  - zheng
  - kawakami
- assessment_id: graph
  area: graph
  topic: All six NONMECHANISTIC edges
  outcome: supported
  summary: Core proteins assemble; linkers stabilize/tune; bilins are bound; rods
    supply excitation; the core routes excitation toward photosystems and contributes
    to light harvesting. This is an explicitly coarse graph that excludes detailed
    excitonic and photoprotective rearrangements. Correct author notes without importing
    the unsupported component-state assertion into the graph.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - go
  - zheng
  - kawakami
  - ipr-broad
- assessment_id: completeness
  area: completeness
  topic: Grounding/boundary discussions and optional fields
  outcome: supported
  summary: Both discussions are relevant and consistent with retained subassembly
    identity. No missing required image, physical quantity, protein example, trait
    or dataset slot was established. Do not force optional additions or infer absence
    from adapter coverage.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - go
  - adapter
  - ipr-broad
  - ipr-beta
  - ipr-linker
- assessment_id: checks
  area: schema
  topic: Native gates and reference identity
  outcome: supported
  summary: All native stable GO, taxonomy, DOI and InterPro references resolve. Automatic
    validation does not establish organism/state-specific source support. Fresh target
    gates and verified reused wider gates are distinguished.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - validation
  - go
  - zheng
  - ipr-broad
- assessment_id: ownership
  area: ownership
  topic: Status, histories and review lineage
  outcome: supported
  summary: Entire native file, both histories and exact legacy report read. Maintained
    YAML owns future guarded corrections; all earlier data/history/review bytes and
    PROPOSED status remain unchanged. The legacy taxon fix is acknowledged without
    inventing canonical finding lineage.
  target_ids:
  - cellstructuremech:phycobilisome_core
  evidence_ids:
  - native
  - legacy
  - search
findings:
- finding_id: F1
  issue_key: phycobilisome-core-photoprotected-source-conflation
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Remove the unsupported photoprotected-state attribution and correct the2021
    authors
  description: The core-linker evidence note says the cited2021 paper modeled light-harvesting
    and photoprotected PBS states. Its structural preparations were not light stressed
    and no OCP was observed. The DOI belongs to Zheng et al., not Sauer. Restrict
    the note to supported architecture/transfer claims and correct repeated author
    attribution. The already corrected PCC7002 example is supported and must not be
    reverted.
  target_ids:
  - cellstructuremech:phycobilisome_core
  field_paths:
  - components[core_linkers_and_terminal_emitters].evidence[reference=DOI:10.1038/s41467-021-25813-y].notes
  - components[allophycocyanin_core_phycobiliproteins].evidence
  - functions[allophycocyanin_core_energy_transfer].evidence
  - evidence[reference=DOI:10.1038/s41467-021-25813-y].notes
  - causal_graphs[phycobilisome_core_energy_transfer].edges.evidence
  evidence_ids:
  - native
  - zheng
  - legacy
  rule_id: review-checklist:exact-source-and-condition-scope
  native_severity: major
  normalization_reason: Specific unsupported structural-state evidence is material;
    this is more than a bibliographic typo. The core identity and earlier taxon correction
    remain valid.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_core.yaml
    role: maintained scientific record
- finding_id: F2
  issue_key: phycobilisome-core-kawakami-preparation-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Distinguish separate core/rod structures from an intact resolved antenna
  description: The T.vulcanus canonical example says core and rods were resolved in
    an intact PBS. The cited study instead reconstructed separate core and dissociated
    rod preparations; limited residual rod density around the core was not modeled
    at the same detail. Qualify the example to match the inspected experimental preparation
    and reconstructed objects without denying intact starting material or residual
    rod density.
  target_ids:
  - cellstructuremech:phycobilisome_core
  field_paths:
  - canonical_examples[taxon_id=NCBITaxon:32053].note
  evidence_ids:
  - native
  - kawakami
  rule_id: review-checklist:complex-composition-and-experimental-context
  native_severity: major
  normalization_reason: The statement materially overstates what assembled structural
    object was resolved. Correct organism and genuine core/rod structures do not make
    an intact-assembly claim supported.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_core.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Correct2021 author notes and remove the unsupported photoprotected-state
    attribution, or add independently inspected, correctly scoped evidence for any
    retained state-specific claim. Preserve the PCC7002 correction.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:phycobilisome_core
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_core.yaml
    role: maintained scientific record
  generator: Native guarded writer and documented generated-product workflow only
    after separately authorized curation.
  acceptance_checks:
  - The linker note no longer claims that Zheng2021 resolved photoprotected structures.
  - Every author/year note attached to the2021 DOI agrees with its bibliographic identity.
  - The supported PCC7002 canonical example and coarse graph scope remain intact.
  - Guarded curation/history, retained PROPOSED status, native gates and lineage-linked
    successor review.
- action_id: A2
  description: Describe the T.vulcanus core and rod results as separate reconstructions
    with preparation context, rather than a jointly resolved intact PBS.
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:phycobilisome_core
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_core.yaml
    role: maintained scientific record
  acceptance_checks:
  - The example preserves the distinction between intact starting material, dissociated
    preparations, residual density and detailed reconstructed models.
  - Species identity and the supported core/rod result remain intact.
  - Validate guarded native changes and save a successor retaining this stable issue
    key.
limitations:
- Same-agent whole-record review, not independent human sign-off, exhaustive literature/retraction
  search or raw experimental reanalysis.
- Primary papers were read in the selected abstract/Results/Methods sections identified
  in Evidence, not every figure pixel, supplementary item or raw map. Uncertain ApcD/CpcG
  assignments and inferred transfer paths are not upgraded to experimentally resolved
  specificity or motion.
- Sui2021 was freshly inspected as complete abstract and metadata; a renewed author-PDF
  request timed out. Broad architecture/energy-transfer claims are independently corroborated
  by the inspected primary papers and InterPro descriptions. No assertion about unread
  later review sections supports a finding.
- All17 local HTTP captures returned200, but the first Kawakami body URL used the
  wrong PMC ID and returned unrelated DOI10.1038/s41598-022-09654-3. Identity checking
  rejected it; the correct PMC9205905 article was fetched from the verified DOI metadata
  and used instead. The mismatched capture is retained, not treated as supporting
  evidence.
- The historical taxon correction is verified against current native bytes and literature;
  remote issue1961/PR1960 status was not refreshed, and no canonical predecessor or
  terminal disposition is invented.
- Fresh target checks plus checksum-verified wider-check reuse with original test/cache/no-adapter
  limitations. No exact iModulonDB dataset and no target trait links; absence from
  that inventory is not negative biological evidence.
- No native scientific edits, history/status changes, generated-product changes or
  GitHub mutation. Existing publication approval remains unanswered; no bypass or
  retry.
tags:
- scientific-review
- energy-complex
- experimental-scope
- major
```
