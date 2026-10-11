# Stalk crossband: scientific evidence review

- Review: 20261011T055235Z-stalk_crossband-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T05:45:54Z
- Finished UTC: 2026-10-11T05:52:35Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record assessed at the source access tiers stated. Concrete evidence defects warrant curation; optional empty fields and explicitly deferred molecular grounding are not findings.

## Scope And Provenance

Entire native YAML, present scientific claims, exact authorities and both history surfaces.

Selection: One sequential unassessed target from the all-909-record goal; not a sampled corpus verdict.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base aa74419b62aaba390ab49cb40d430b394c933baa.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:stalk_crossband | data/structures/appendage/stalk_crossband.yaml | maintained | stalk crossband |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:stalk_crossband | Command passed; deterministic validity is not scientific support. |
| strict | passed | True | cellstructuremech:stalk_crossband | Command passed; deterministic validity is not scientific support. |
| snippets | passed | True | cellstructuremech:stalk_crossband | No quoted snippets present; this did not test paraphrase accuracy. Paraphrases were assessed against source text separately. |
| history | passed | True | cellstructuremech:stalk_crossband | Command passed; deterministic validity is not scientific support. |
| labels | passed | True | cellstructuremech:stalk_crossband | Full-corpus label check passed; unsupported adapter pairs are skipped, not certified. Exact target GO and taxonomy responses were separately inspected. |
| traits | passed | True | cellstructuremech:stalk_crossband | Command passed; deterministic validity is not scientific support. |
| curies | passed | True | cellstructuremech:stalk_crossband | Full-corpus identifier check passed with skipped non-resolvable namespaces and any unexercised authority controls retained in its log. All exact authorities used by these two records were separately inspected. |
| reviews | passed | True | cellstructuremech:stalk_crossband | Command passed; deterministic validity is not scientific support. |
| diff | passed | True | cellstructuremech:stalk_crossband | Command passed; deterministic validity is not scientific support. |
| contract | passed | True | cellstructuremech:stalk_crossband | Command passed; deterministic validity is not scientific support. |
| Exact-baseline authoritative CI QC | passed | True | cellstructuremech:stalk_crossband | Full QC passed on the exact unchanged baseline, including products; not a newly run local full QC. |
| Structured-source applicability | passed | False | cellstructuremech:stalk_crossband | The 28-row iModulonDB inventory has no Caulobacter, Brevundimonas or Asticcacaulis dataset. Not applicable; no biological absence inferred. |

## Scientific And Domain Assessments

### Definition, synonyms, parent and prostheca parthood

identity: supported. Targets: cellstructuremech:stalk_crossband.

Discrete proteinaceous crossband identity and Caulobacter functional definition are supported; it is a part of the envelope projection, not a synonym for that projection.

### Distribution and model example

scope: supported. Targets: cellstructuremech:stalk_crossband.

Caulobacter/Asticcacaulis observations support the qualified bacterial subset. Normal developmental formation does not assert barriers in swarmer cells or all stalk-bearing bacterial lineages. NA1000/CB15N names resolve.

### Stp cohort membership, structural essentiality and open identifiers

grounding: concern. Targets: cellstructuremech:stalk_crossband.

Membership is supported, but assigning all four proteins ESSENTIAL conflates scaffold formation with efficient barrier sealing. Reviewed labels remain appropriate; no exact family grounding was asserted.

### Diffusion function and all four assembly edges

evidence: concern. Targets: cellstructuremech:stalk_crossband.

WT crossband assembly, spanning, diffusion restriction and compartmentalization are supported. Assembly description should distinguish scaffold proteins from the barrier-tightening proteins to agree with mutant evidence.

### Status, prior issue fixes, histories and optional slots

provenance: supported. Targets: cellstructuremech:stalk_crossband.

PROPOSED and prior append-only histories remain intact. No asserted measurements, images, traits or datasets need additional evidence checks. Empty optional fields do not constitute issues.

## Findings

### F1: Separate structural scaffold requirements from barrier sealing

major / open / confirmed; issue key: stalk-crossband-assembly-barrier-essentiality.

The cohort gives StpA/B/C/D ESSENTIAL status and says all four are required to form crossbands. Schlimpert 2012 Results and Discussion distinguish loss of crossbands in StpAB-deficient cells from visible crossbands in StpC/D mutants; StpCD loss yields partial protein leakage. Native ESSENTIAL denotes formation of the structure, not full barrier function.

## Recommended Actions And Acceptance Checks

### A1

Separate structural scaffold requirements from barrier sealing

- Represent StpAB scaffold and StpCD sealing constituents separately with structural essentiality appropriate to each.
- Retain StpCD membership and requirement for efficient barrier sealing; do not call StpCD unnecessary for normal function.
- Update graph component references and grounding discussion attachments consistently, retaining all prior history.
- Use the guarded writer, preserve prior histories and PROPOSED status, append Codex EDIT provenance, regenerate affected products and pass focused tests plus authoritative QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/stalk_crossband.yaml; Full native YAML and both append-only record histories | context_only | Pre-mutation native record. Prior issue fixes and original status are retained. |
| prior | reviews/structured/ and reports/yaml_record_review/; Exact identifiers, labels and slugs | context_only | No prior exact-target review bundle found in these roots. Issues #399/#400 added the prostheca plasma membrane and typed the uptake process; #402/#403 removed age marking as a function and typed compartmentalization. These are not the present findings. |
| taxon-2 | https://rest.uniprot.org/taxonomy/2.json; Exact NCBI-derived taxon identity, synonym, parent and strain names | supports | Bacteria domain identity is valid; taxonomy metadata alone is not distribution evidence. |
| taxon-155892 | https://rest.uniprot.org/taxonomy/155892.json; Exact NCBI-derived taxon identity, synonym, parent and strain names | supports | Current authority recognizes C. vibrioides, historical C. crescentus nomenclature, and NA1000/CB15N at the asserted taxonomic levels. |
| taxon-565050 | https://rest.uniprot.org/taxonomy/565050.json; Exact NCBI-derived taxon identity, synonym, parent and strain names | supports | Current authority recognizes C. vibrioides, historical C. crescentus nomenclature, and NA1000/CB15N at the asserted taxonomic levels. |
| go-0032991 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032991; Exact QuickGO term | supports | Active term matches the asserted parent or part; no exact structure identity is inferred from a broader term. |
| go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=stalk+crossband&amp;limit=100; Bounded QuickGO search, limit 100 | supports | No exact bacterial structure match in this returned set. This is not an exhaustive assertion that no term exists in any ontology. |
| paper-0 | DOI:10.1016/j.cell.2012.10.046; Main-text Results, Figures 1-7 captions, Discussion and Methods | supports | StpAB deletion abolishes visible crossbands. StpC/D mutants retain crossbands with leaky barriers. StpAB provides the scaffold and StpC/D seals it. Protein trapping improves recovery from starvation. PstS cannot shuttle across mature crossbands; small-molecule routes remain possibilities, not established mechanisms. |
| paper-6 | DOI:10.1128/JB.178.13.3939-3948.1996; Primary abstract | supports | More than 7000 Caulobacter stalks and Asticcacaulis twin-stalk comparisons establish stalk bands in these genera and age correlations, not an active age-marking function. |
| paper-9 | PMID:4126821; Primary abstract | supports | Isolated Sk1 418 crossbands span the stalk width; the historical support hypothesis does not establish modern molecular composition. |

## Limits And Additional Notes

- Poindexter 1996 and Jones 1973 claims were assessed at primary-abstract level. Their scanned full article pages were not inspected; the bounded parthood/spanning claims also have Schlimpert main-text support.
- Schlimpert main-text HTML and figure captions were inspected after Europe PMC XML returned HTTP 500; raw tomograms, images and supplemental movies were not reanalysed.
- Same-agent assessment, not independent human sign-off or completion of the 909-record goal.
- Exact-baseline CI supplies full QC. Skipped namespaces and non-adapter label pairs are not certified by successful validators.
- No relevant iModulonDB coverage. No quoted snippets are present; snippet-check success is not paraphrase validation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T055235Z-stalk_crossband-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Stalk crossband: scientific evidence review'
started_at: '2026-10-11T05:45:54Z'
finished_at: '2026-10-11T05:52:35Z'
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
summary: Entire native record assessed at the source access tiers stated. Concrete
  evidence defects warrant curation; optional empty fields and explicitly deferred
  molecular grounding are not findings.
source:
  git_revision: aa74419b62aaba390ab49cb40d430b394c933baa
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
  - path: README.md
    sha256: 2e18c8ebf56445a45ddadbe3de7f7eb9b73bcfdc3be836fd8c8117ed5a8db6f4
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/appendage/prostheca.yaml
    sha256: 68fd613bc222f0d93985d761bb723b5b49bdb0cff30ae5c6f58e83820fc7396a
    role: context
  - path: data/structures/appendage/stalk_crossband.yaml
    sha256: 1a86dbf57b3ed4cecb2b5aed03eaf49f6408eff1b2a029a5516880b0ee1206d2
    role: target
  - path: data/structures/envelope/cell_outer_membrane.yaml
    sha256: 3becd0f494ef6cc70d352f21ea5f5231d70265edecde25c6f827a31b6c821dcf
    role: context
  - path: data/structures/envelope/gram_negative_bacterium_type_cell_wall.yaml
    sha256: 9c953c54e9f54eba9cbe7b658046a7910b2e9a42d41246d2ce3c2acf9693bef6
    role: context
  - path: data/structures/envelope/peptidoglycan_based_cell_wall.yaml
    sha256: 893883fe6827f7bd64eb8d07855e5592cedb0e1c0d368e8d42153521575a0911
    role: context
  - path: data/structures/envelope/plasma_membrane.yaml
    sha256: e8dcf1af1e9d5cf91056b26f09ed6bd95e092ced315abf7d4feca64f74ae819b
    role: context
  - path: data/structures/other/holdfast.yaml
    sha256: 6becc2beb9df3e1f8fe0c6384c2bed7191577a0f04fbb0de1c0086553e894f54
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
  - path: history/records/stalk_crossband/2026-09-11T033043Z-codex-c3a7c2.yaml
    sha256: 58f27cd1e0a5c7dafed30a5887dc40f9dd747ea23a8a8b90996f69f45a3b6b8b
    role: context
  - path: history/records/stalk_crossband/2026-09-11T033759Z-codex-f4cbcb.yaml
    sha256: 02f764cfd4948b17ea6d7407c3198c3911f82b3982cca440d6e44b1613566ae9
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/evidence_readability.stalk_crossband.tsv
    sha256: de3cebbf3dbe6db1d5d9dc19f404e417338128adb717c060e8f51a14d9f2d083
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: cellstructuremech:stalk_crossband
  path: data/structures/appendage/stalk_crossband.yaml
  label: stalk crossband
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/stalk_crossband.yaml
    role: maintained scientific record
scope:
  description: Entire native YAML, present scientific claims, exact authorities and
    both history surfaces.
  selection: One sequential unassessed target from the all-909-record goal; not a
    sampled corpus verdict.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:stalk_crossband
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/stalk_crossband.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T05:46:47Z to 2026-10-11T05:46:50Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/stalk_crossband.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T05:46:50Z to 2026-10-11T05:46:55Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/stalk_crossband.yaml
    --report /private/tmp/csm-review-20261011T054444Z/stalk_crossband-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No quoted snippets present; this did not test paraphrase accuracy. Paraphrases
    were assessed against source text separately.
  scope_note: 2026-10-11T05:46:55Z to 2026-10-11T05:47:17Z; log SHA-256 d6f225b4d128d32d69af0f0dcf2a64afd9da9b41fabcafb7713c341de51cf125
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T05:47:17Z to 2026-10-11T05:47:30Z; log SHA-256 7d8379458f5adf9726b5df01dc5d6092c1500b8c1627b771ec131d9c4c3c3aaf
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Full-corpus label check passed; unsupported adapter pairs are skipped,
    not certified. Exact target GO and taxonomy responses were separately inspected.
  scope_note: 2026-10-11T05:47:30Z to 2026-10-11T05:48:51Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T05:48:51Z to 2026-10-11T05:49:10Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Full-corpus identifier check passed with skipped non-resolvable namespaces
    and any unexercised authority controls retained in its log. All exact authorities
    used by these two records were separately inspected.
  scope_note: 2026-10-11T05:49:10Z to 2026-10-11T05:49:54Z; log SHA-256 dc5ed8534cf356581f142af6232079d99cab71fde9815408309aac234b468667
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T05:49:54Z to 2026-10-11T05:50:31Z; log SHA-256 57c5e3051a144460c72ffefb748c3e497dc2f7275cc3974775fc158335f018db
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T05:50:31Z to 2026-10-11T05:50:31Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; deterministic validity is not scientific support.
  scope_note: 2026-10-11T05:46:09Z to 2026-10-11T05:47:10Z; log SHA-256 c9d49123f81747feace19afb3996a435ab8647c7ae3814dc5eb074f5e9fc8caa
- check_id: qc
  name: Exact-baseline authoritative CI QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:stalk_crossband
  command: gh run view 38115405450 --json status,conclusion,headSha,event,name,url,jobs;
    gh run view 38115405450 --log
  exit_code: 0
  summary: Full QC passed on the exact unchanged baseline, including products; not
    a newly run local full QC.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38115405450;
    full-log SHA-256 91e29548a308e23bb30138d3724a526c64c1fd0c5f8f2d415dbec65d7a95d485
- check_id: adapter
  name: Structured-source applicability
  status: passed
  required: false
  target_ids:
  - cellstructuremech:stalk_crossband
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  summary: The 28-row iModulonDB inventory has no Caulobacter, Brevundimonas or Asticcacaulis
    dataset. Not applicable; no biological absence inferred.
  scope_note: 2026-10-11T05:46:04Z to 2026-10-11T05:46:04Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/stalk_crossband.yaml
  locator: Full native YAML and both append-only record histories
  accessed_at: '2026-10-11T05:52:35Z'
  snapshot_sha256: 1a86dbf57b3ed4cecb2b5aed03eaf49f6408eff1b2a029a5516880b0ee1206d2
  support: context_only
  summary: Pre-mutation native record. Prior issue fixes and original status are retained.
- evidence_id: prior
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: Exact identifiers, labels and slugs
  accessed_at: '2026-10-11T05:52:35Z'
  support: context_only
  search_scope: rg --no-ignore --hidden across data/structures, history and both review
    roots included ignored files. GitHub all-state query prostheca OR crossband OR
    StpABCD returned four closed items, below the 100-result limit.
  summary: 'No prior exact-target review bundle found in these roots. Issues #399/#400
    added the prostheca plasma membrane and typed the uptake process; #402/#403 removed
    age marking as a function and typed compartmentalization. These are not the present
    findings.'
- evidence_id: taxon-2
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2.json
  locator: Exact NCBI-derived taxon identity, synonym, parent and strain names
  accessed_at: '2026-10-11T05:47:20Z'
  snapshot_sha256: 8074c9bcd59cd4da1da4bc9ec98c040bbecd52ef5c91c4c4bb9bed0f3a7cb5a9
  support: supports
  summary: Bacteria domain identity is valid; taxonomy metadata alone is not distribution
    evidence.
- evidence_id: taxon-155892
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/155892.json
  locator: Exact NCBI-derived taxon identity, synonym, parent and strain names
  accessed_at: '2026-10-11T05:47:21Z'
  snapshot_sha256: bb62df49943694589f201ba87a84dc3f34fb5a96c8577bd005914f695df7cd0e
  support: supports
  summary: Current authority recognizes C. vibrioides, historical C. crescentus nomenclature,
    and NA1000/CB15N at the asserted taxonomic levels.
- evidence_id: taxon-565050
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/565050.json
  locator: Exact NCBI-derived taxon identity, synonym, parent and strain names
  accessed_at: '2026-10-11T05:47:22Z'
  snapshot_sha256: f82c9e5906404b4e68229cdde10bd11dda11c16be678086d1a104f651a852683
  support: supports
  summary: Current authority recognizes C. vibrioides, historical C. crescentus nomenclature,
    and NA1000/CB15N at the asserted taxonomic levels.
- evidence_id: go-0032991
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0032991
  locator: Exact QuickGO term
  accessed_at: '2026-10-11T05:47:14Z'
  snapshot_sha256: 480165003b2c8a406006ff17c4cfe836fc000541ad5dac1ca0f585ed30c02e87
  support: supports
  summary: Active term matches the asserted parent or part; no exact structure identity
    is inferred from a broader term.
- evidence_id: go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=stalk+crossband&limit=100
  locator: Bounded QuickGO search, limit 100
  accessed_at: '2026-10-11T05:47:18Z'
  snapshot_sha256: f83b272c1f2e980580e7fac68cf969183f99d3ec225c30f0599630fa5d76575b
  support: supports
  summary: No exact bacterial structure match in this returned set. This is not an
    exhaustive assertion that no term exists in any ontology.
  search_scope: Bounded QuickGO search, limit 100; https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=stalk+crossband&limit=100
- evidence_id: paper-0
  kind: primary_source
  reference: DOI:10.1016/j.cell.2012.10.046
  locator: Main-text Results, Figures 1-7 captions, Discussion and Methods
  accessed_at: '2026-10-11T05:47:09Z'
  snapshot_sha256: d44137d5f9c67b54f59fe54840fe7b1d0b82bf3734641c1b540d55b7e6d52681
  support: supports
  summary: StpAB deletion abolishes visible crossbands. StpC/D mutants retain crossbands
    with leaky barriers. StpAB provides the scaffold and StpC/D seals it. Protein
    trapping improves recovery from starvation. PstS cannot shuttle across mature
    crossbands; small-molecule routes remain possibilities, not established mechanisms.
- evidence_id: paper-6
  kind: primary_source
  reference: DOI:10.1128/JB.178.13.3939-3948.1996
  locator: Primary abstract
  accessed_at: '2026-10-11T05:46:24Z'
  snapshot_sha256: 29b0d99ff99c8507f9b15f397a423b2d9e43bf5241f4538e286e0e726d4b6c43
  support: supports
  summary: More than 7000 Caulobacter stalks and Asticcacaulis twin-stalk comparisons
    establish stalk bands in these genera and age correlations, not an active age-marking
    function.
- evidence_id: paper-9
  kind: primary_source
  reference: PMID:4126821
  locator: Primary abstract
  accessed_at: '2026-10-11T05:46:31Z'
  snapshot_sha256: adf1fb5d390f040b10bf04323f6aeb749da3cc6e2e8989d781083b5290abdd0b
  support: supports
  summary: Isolated Sk1 418 crossbands span the stalk width; the historical support
    hypothesis does not establish modern molecular composition.
assessments:
- assessment_id: identity
  area: identity
  topic: Definition, synonyms, parent and prostheca parthood
  outcome: supported
  target_ids:
  - cellstructuremech:stalk_crossband
  evidence_ids:
  - record
  - paper-0
  - paper-6
  - paper-9
  - go-0032991
  summary: Discrete proteinaceous crossband identity and Caulobacter functional definition
    are supported; it is a part of the envelope projection, not a synonym for that
    projection.
- assessment_id: scope
  area: scope
  topic: Distribution and model example
  outcome: supported
  target_ids:
  - cellstructuremech:stalk_crossband
  evidence_ids:
  - paper-0
  - paper-6
  - taxon-2
  - taxon-155892
  - taxon-565050
  summary: Caulobacter/Asticcacaulis observations support the qualified bacterial
    subset. Normal developmental formation does not assert barriers in swarmer cells
    or all stalk-bearing bacterial lineages. NA1000/CB15N names resolve.
- assessment_id: composition
  area: grounding
  topic: Stp cohort membership, structural essentiality and open identifiers
  outcome: concern
  target_ids:
  - cellstructuremech:stalk_crossband
  evidence_ids:
  - record
  - paper-0
  summary: Membership is supported, but assigning all four proteins ESSENTIAL conflates
    scaffold formation with efficient barrier sealing. Reviewed labels remain appropriate;
    no exact family grounding was asserted.
- assessment_id: functions
  area: evidence
  topic: Diffusion function and all four assembly edges
  outcome: concern
  target_ids:
  - cellstructuremech:stalk_crossband
  evidence_ids:
  - record
  - paper-0
  - paper-9
  summary: WT crossband assembly, spanning, diffusion restriction and compartmentalization
    are supported. Assembly description should distinguish scaffold proteins from
    the barrier-tightening proteins to agree with mutant evidence.
- assessment_id: provenance
  area: provenance
  topic: Status, prior issue fixes, histories and optional slots
  outcome: supported
  target_ids:
  - cellstructuremech:stalk_crossband
  evidence_ids:
  - record
  - prior
  summary: PROPOSED and prior append-only histories remain intact. No asserted measurements,
    images, traits or datasets need additional evidence checks. Empty optional fields
    do not constitute issues.
findings:
- finding_id: F1
  issue_key: stalk-crossband-assembly-barrier-essentiality
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Separate structural scaffold requirements from barrier sealing
  description: The cohort gives StpA/B/C/D ESSENTIAL status and says all four are
    required to form crossbands. Schlimpert 2012 Results and Discussion distinguish
    loss of crossbands in StpAB-deficient cells from visible crossbands in StpC/D
    mutants; StpCD loss yields partial protein leakage. Native ESSENTIAL denotes formation
    of the structure, not full barrier function.
  target_ids:
  - cellstructuremech:stalk_crossband
  field_paths:
  - components[0]
  - causal_graphs[0].description
  - causal_graphs[0].nodes[0]
  - causal_graphs[0].edges[0]
  - discussions[0]
  evidence_ids:
  - record
  - paper-0
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/stalk_crossband.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material scientific scope or component-essentiality defect.
actions:
- action_id: A1
  description: Separate structural scaffold requirements from barrier sealing
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:stalk_crossband
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/stalk_crossband.yaml
    role: maintained scientific record
  acceptance_checks:
  - Represent StpAB scaffold and StpCD sealing constituents separately with structural
    essentiality appropriate to each.
  - Retain StpCD membership and requirement for efficient barrier sealing; do not
    call StpCD unnecessary for normal function.
  - Update graph component references and grounding discussion attachments consistently,
    retaining all prior history.
  - Use the guarded writer, preserve prior histories and PROPOSED status, append Codex
    EDIT provenance, regenerate affected products and pass focused tests plus authoritative
    QC.
limitations:
- Poindexter 1996 and Jones 1973 claims were assessed at primary-abstract level. Their
  scanned full article pages were not inspected; the bounded parthood/spanning claims
  also have Schlimpert main-text support.
- Schlimpert main-text HTML and figure captions were inspected after Europe PMC XML
  returned HTTP 500; raw tomograms, images and supplemental movies were not reanalysed.
- Same-agent assessment, not independent human sign-off or completion of the 909-record
  goal.
- Exact-baseline CI supplies full QC. Skipped namespaces and non-adapter label pairs
  are not certified by successful validators.
- No relevant iModulonDB coverage. No quoted snippets are present; snippet-check success
  is not paraphrase validation.
```
