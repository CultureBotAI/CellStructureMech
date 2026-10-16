# Plasma membrane-derived photosystem I source-organism review

- Review: 20261012T095015Z-plasma-membrane-psi-source-taxon
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T09:42:52Z
- Finished UTC: 2026-10-12T09:50:15Z
- Reviewer: Codex (self_review)
- Completion: partial
- Verdict: needs_curation
- Scientific review: true

## Summary

One confirmed major source-organism mismatch: Casella2017 directly studies PCC7942, while the canonical example and related graph/discussion attribute its PSI microscopy to PCC6803. Exact Perez-Boerema2024 distribution/electron-transfer attributions remain unverified because its body is inaccessible. No native record was changed.

## Scope And Provenance

Entire native record and append-only history read; identity, hierarchy, example and all four graph edges considered, with explicit incomplete review-body attribution checks; no sampling.

Selection: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base e74d0c3e33df7e44348afbba1695b61c23262ab0.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0030094 | data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml | maintained | plasma membrane-derived photosystem I |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0030094 | Fresh target gate. Actual run: 2026-10-12T09:43:03Z to 2026-10-12T09:43:05Z. |
| strict | passed | True | GO:0030094 | Fresh target gate. Actual run: 2026-10-12T09:43:05Z to 2026-10-12T09:43:08Z. |
| snippets | passed | True | GO:0030094 | Fresh target gate; snippets check found zero of16 citations with a snippet. Actual run: 2026-10-12T09:43:08Z to 2026-10-12T09:43:24Z. |
| reused-release-qc | passed | True | GO:0030094 | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; label603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:33:07Z to 2026-10-12T06:45:16Z. |
| reused-release-labels | passed | True | GO:0030094 | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; label603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:45:16Z to 2026-10-12T06:47:16Z. |
| reused-release-traits | passed | True | GO:0030094 | Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped; label603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:48:15Z to 2026-10-12T06:48:52Z. |
| reused-curies-live | passed | True | GO:0030094 | Preserved prior result: live CURIE4023OK/251skips; initial205 archive provenance check failed, explicit historical-commit recheck passed, full retry205valid and contract4passed. Failure cause not established; no input edits between failure/retry. Actual run: 2026-10-12T07:05:41Z to 2026-10-12T07:10:58Z. |
| reused-post-save-archive | failed | False | GO:0030094 | Preserved prior result: live CURIE4023OK/251skips; initial205 archive provenance check failed, explicit historical-commit recheck passed, full retry205valid and contract4passed. Failure cause not established; no input edits between failure/retry. Actual run: 2026-10-12T09:33:22Z to 2026-10-12T09:36:09Z. |
| reused-historical-git-recheck | passed | True | GO:0030094 | Preserved prior result: live CURIE4023OK/251skips; initial205 archive provenance check failed, explicit historical-commit recheck passed, full retry205valid and contract4passed. Failure cause not established; no input edits between failure/retry. Actual run: 2026-10-12T09:37:43Z to 2026-10-12T09:37:44Z. |
| reused-post-save-archive-retry | passed | True | GO:0030094 | Preserved prior result: live CURIE4023OK/251skips; initial205 archive provenance check failed, explicit historical-commit recheck passed, full retry205valid and contract4passed. Failure cause not established; no input edits between failure/retry. Actual run: 2026-10-12T09:39:53Z to 2026-10-12T09:41:13Z. |
| reused-post-save-contract | passed | True | GO:0030094 | Preserved prior result: live CURIE4023OK/251skips; initial205 archive provenance check failed, explicit historical-commit recheck passed, full retry205valid and contract4passed. Failure cause not established; no input edits between failure/retry. Actual run: 2026-10-12T09:36:09Z to 2026-10-12T09:38:31Z. |
| adapter-datasets | passed | False | GO:0030094 | Fresh full inventory; no exact native organism dataset. Actual run: 2026-10-12T09:43:07Z to 2026-10-12T09:43:07Z. |
| Cited-review body attribution | unavailable | True | GO:0030094 | Publisher body capture returned HTTP403; alternate web full-text/PDF opens were inaccessible. Abstract/metadata read, but exact distribution and b6f/PSI source attributions remain unverified. No exit code invented for this scientific reading check. |
| Initial draft validation | failed | False | GO:0030094 | Initial draft used uncertain/context instead of the contract enums unknown/context_only. Corrected without changing the scientific assessment. Actual run: 2026-10-12T09:49:26Z to 2026-10-12T09:49:29Z. |

## Scientific And Domain Assessments

### Bacterial PSI complex boundary and hierarchy

identity: supported. Targets: GO:0030094.

Exact GO identity, complex kind, PSI parentage and bacterial-thylakoid parthood agree. Related cyanobacterial PSI synonym is compatible; no plastid PSI or whole-membrane identity is substituted.

### Deferred subunits and optional quantities

completeness: supported. Targets: GO:0030094.

The record makes no subunit stoichiometry, imaging measurement or protein-accession claim. Its explicit component-boundary TODO is a legitimate curation limit, not by itself a concrete defect. No optional row is required solely to generate a finding.

### Direct experimental organism

scope: concern. Targets: GO:0030094.

The nearest primary source directly maps localization/mobility in PCC7942, not PCC6803. Its background discussion of PCC6803 cannot be silently recast as the current experiment. The finding does not deny the biological occurrence of PSI in PCC6803.

### Cyanobacterial thylakoid occurrence and cited-review scope

evidence: unknown. Targets: GO:0030094.

GO and the inspected primary study support bacterial thylakoid PSI occurrence; the qualitative COMMON assertion is not a quantitative prevalence claim. Exact scope of the Perez-Boerema body passage supporting the native distribution note remains unverified.

### PSI downstream electron-input attribution

evidence: unknown. Targets: GO:0030094.

Generic PSI participation is compatible with GO and primary-paper context. The exact Perez-Boerema attribution for b6f-to-soluble-carrier-to-PSI remains unchecked because the body is unavailable; this is not proof that the biological chain or citation is wrong.

### All four nonmechanistic edges

graph: concern. Targets: GO:0030094.

Parthood is supported. The houses edge misattributes the source organism. Both process edges require the inaccessible review-body check. The b6f edge explicitly includes a downstream soluble carrier, so no false direct-contact finding is made.

### Actionable subunit-boundary discussion

provenance: concern. Targets: GO:0030094.

The discussion is relevant, but repeats the wrong source organism. Correct it alongside the canonical example and graph without forcing unrelated component expansion.

### Deterministic validation and stable identifiers

schema: supported. Targets: GO:0030094.

Native GO, taxonomy and DOI identities resolve. Author/title/year notes agree with metadata. Schema validation cannot establish organism-specific experimental support or replace the missing full-text check.

### Histories, status and retained observations

ownership: supported. Targets: GO:0030094.

Entire native YAML and append-only history were read. Maintained YAML owns future guarded corrections; no generated output or history is changed and PROPOSED remains. No canonical predecessor exists for this exact target, so no disposition is fabricated.

## Findings

### F1: Correct the organism attributed to Casella2017 PSI microscopy

major / open / confirmed; issue key: plasma-membrane-derived-psi-casella-taxon.

The record attributes Casella2017 PSI distribution and mobility experiments to Synechocystis PCC6803. Its methods and Results directly study Synechococcus elongatus PCC7942, including PsaE-eGFP imaging. Align the source-specific example, graph and discussion with that organism and experimental context, or retain PCC6803 using separately inspected primary evidence. The paper does mention earlier PCC6803 studies; the defect is conflating background with its direct experiment, not claiming the organism is absent from the article.

## Recommended Actions And Acceptance Checks

### A1

Correct all source-specific organism attributions consistently, preserving tagged-strain experimental context; alternatively inspect a PCC6803 primary source before retaining that example. Do not change the valid GO structure identity.

- Canonical example, graph and discussion consistently identify the actual directly studied strain and nearest source.
- No background citation or expression-module hit is substituted for inspected experimental evidence.
- Retain valid PSI hierarchy, carrier-qualified graph scope, PROPOSED status and append-only curation history.
- Run native validation and save a successor retaining this stable issue key; resolve the outstanding Perez-Boerema attribution check before claiming complete scientific review.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| native | data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml; Entire YAML and its one append-only history file | supports | The canonical PCC6803 example, graph description, membrane-houses-PSI edge and discussion attribute microscopy to Synechocystis. Components are explicitly deferred. The historical issue754 process-edge evidence fix is distinct from the present organism mismatch. |
| go | GO:0030094; GO:0009522; GO:0031676; GO:0030075; GO:0009767; GO:0009512; All six current GO entries, definitions, names and aspects | supports | Bacterial thylakoid PSI identity, generic PSI parent, bacterial membrane container and electron-transport process are compatible. The GO name is not independent proof of a particular membrane-biogenesis mechanism. |
| casella | https://doi.org/10.1016/j.molp.2017.09.019; Complete abstract and Introduction; Strains and Growth Conditions; Generation of Constructs; distribution and mobility Results sections | partial | The directly studied organism is Synechococcus elongatus PCC7942. PSI imaging used chromosomal PsaE-eGFP fusions in that strain. The article discusses earlier PCC6803 studies as background, but these are not its own organism-specific distribution/mobility experiments. |
| perez | https://doi.org/10.1146/annurev-cellbio-120823-022747; Complete abstract and bibliographic identity from Europe PMC, Crossref and publisher landing page; body unavailable | partial | Perez-Boerema, Engel and Wietrzynski2024 review thylakoid structural diversity across cyanobacteria and photosynthetic eukaryotes. The inspected abstract does not establish the exact b6f-to-carrier-to-PSI attribution in the native evidence notes. |
| access | https://www.annualreviews.org/deliver/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?itemId=/content/journals/10.1146/annurev-cellbio-120823-022747&amp;mimeType=html&amp;fmt=ahah; Recorded HTTP403 response, not article text | context_only | The publisher full-text request failed with HTTP403 and its bytes are retained as an access-failure artifact. Web opens of the full-text and Crossref-linked PDF endpoints were also inaccessible. The author-lab publication list only linked to PubMed. Search snippets were not treated as inspected source text. |
| adapter | https://imodulondb.org/; Fresh complete28-dataset inventory | supports | No exact PCC6803 dataset applies. PCC7942 is covered but is a possible source-specific correction, not the current native organism; no gene-level claim is made in this record and no expression module is substituted for microscopy evidence. |
| validation | /private/tmp/csm-review-20261012T094255Z-pmpsi/baseline-verification.json; Fresh target gates and hash-verified unchanged-input wider checks | supports | Schema and strict checks pass. Zero of16 citations carries a snippet. Wider QC987passed/3skipped and label/trait cache limits are retained; later live CURIE and205-bundle archive/contract checks are reused explicitly rather than reported as freshly executed. |
| search | reviews/structured/; Ignored-inclusive canonical and native/legacy searches | supports | Exact target has no canonical predecessor among205 bundles. No exact legacy report or occurrence of the new issue key was found in the searched local review/research/curation roots. This is not a remote issue-absence claim. |
| tax-1117 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117; Complete current taxonomy entry | supports | Native broad Cyanobacteriota label and ID agree. |
| tax-1148 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148; Complete current taxonomy entry | supports | PCC6803 resolves to the native Synechocystis label, but not the directly studied Casella strain. |
| tax-1140 | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140; Complete current taxonomy entry | supports | PCC7942 resolves to Synechococcus elongatus, the organism directly studied by Casella2017. |

## Limits And Additional Notes

- Same-agent review, not independent human sign-off, exhaustive literature/retraction search or raw experimental reanalysis.
- Casella primary evidence was read in the specified abstract/Introduction/Results/Methods sections, not every figure pixel, supplement or raw imaging dataset. Quantitative FRAP values are not added to this qualitative native record.
- Perez-Boerema metadata and complete abstract were inspected, but its full-text body remained inaccessible. The exact native distribution and process-edge attributions are unassessed; this partial result must not be counted as a completed review.
- Nine local HTTP captures returned200 and one publisher-body request returned403. Error HTML is retained as a failure artifact, not scientific evidence; search snippets and uninspected background papers were not promoted into proof.
- Fresh target checks and explicitly hash-verified wider-check reuse retain original skips/cache limits. Prior205-bundle archive failure and successful historical-commit recheck/full retry are both retained; the failure cause is unknown.
- No exact native iModulonDB dataset applies and no gene-level claim is present. Coverage of the possible correction strain is not itself support for localization or experimental phenotype.
- No native scientific edits, generated products, status/history changes or GitHub mutation. Remote historical issue754/PR753 status was not refreshed. Existing external-publication approval remains unanswered; no bypass or retry.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T095015Z-plasma-membrane-psi-source-taxon
kind: record
repository: CultureBotAI/CellStructureMech
title: Plasma membrane-derived photosystem I source-organism review
started_at: '2026-10-12T09:42:52Z'
finished_at: '2026-10-12T09:50:15Z'
reviewer:
  identity: Codex
  kind: agent
  model: GPT-5
  independence: self_review
  independence_basis: Same coding-agent context; no independent reviewer or human
    sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: partial
verdict: needs_curation
scientific_review: true
summary: 'One confirmed major source-organism mismatch: Casella2017 directly studies
  PCC7942, while the canonical example and related graph/discussion attribute its
  PSI microscopy to PCC6803. Exact Perez-Boerema2024 distribution/electron-transfer
  attributions remain unverified because its body is inaccessible. No native record
  was changed.'
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
  - path: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
    sha256: 43644bf79c44cc9c1674f8619a1cb977673a94b3bff2be2461eed104d03d0cdb
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
  - path: history/records/plasma_membrane_derived_photosystem_i/2026-09-13T053202Z-codex-722963.yaml
    sha256: f7fca8fde7082ee879d9260d1884fc30f3384754690aa6fe5c08720f1b9ef1ae
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
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0030094
  path: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
  label: plasma membrane-derived photosystem I
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
    role: maintained scientific record
scope:
  description: Entire native record and append-only history read; identity, hierarchy,
    example and all four graph edges considered, with explicit incomplete review-body
    attribution checks; no sampling.
  selection: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0030094
  exclusions:
  - target: taxonomic_distribution and function/graph evidence attributed to DOI:10.1146/annurev-cellbio-120823-022747
    reason: Exact cited-review body passage not accessible; abstract and metadata
      are insufficient for detailed attribution.
checks:
- check_id: schema
  name: schema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Actual run: 2026-10-12T09:43:03Z to 2026-10-12T09:43:05Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: strict
  name: strict
  command: .venv/bin/python scripts/validate_strict.py data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate. Actual run: 2026-10-12T09:43:05Z to 2026-10-12T09:43:08Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: snippets
  name: snippets
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
    --report /private/tmp/csm-review-20261012T094255Z-pmpsi/snippets.md
  exit_code: 0
  status: passed
  required: true
  summary: 'Fresh target gate; snippets check found zero of16 citations with a snippet.
    Actual run: 2026-10-12T09:43:08Z to 2026-10-12T09:43:24Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: reused-release-qc
  name: reused-release-qc
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    label603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:33:07Z
    to 2026-10-12T06:45:16Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: reused-release-labels
  name: reused-release-labels
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    label603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:45:16Z
    to 2026-10-12T06:47:16Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: reused-release-traits
  name: reused-release-traits
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Hash-verified unchanged-input reuse, not fresh execution. QC987passed/3skipped;
    label603 no-adapter skips; cached trait index. Actual run: 2026-10-12T06:48:15Z
    to 2026-10-12T06:48:52Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: reused-curies-live
  name: reused-curies-live
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  status: passed
  required: true
  summary: 'Preserved prior result: live CURIE4023OK/251skips; initial205 archive
    provenance check failed, explicit historical-commit recheck passed, full retry205valid
    and contract4passed. Failure cause not established; no input edits between failure/retry.
    Actual run: 2026-10-12T07:05:41Z to 2026-10-12T07:10:58Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: reused-post-save-archive
  name: reused-post-save-archive
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 1
  status: failed
  required: false
  summary: 'Preserved prior result: live CURIE4023OK/251skips; initial205 archive
    provenance check failed, explicit historical-commit recheck passed, full retry205valid
    and contract4passed. Failure cause not established; no input edits between failure/retry.
    Actual run: 2026-10-12T09:33:22Z to 2026-10-12T09:36:09Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: reused-historical-git-recheck
  name: reused-historical-git-recheck
  command: env GIT_NO_LAZY_FETCH=1 GIT_TERMINAL_PROMPT=0 git rev-parse --verify '4016cb9e19b3ec83f5d368f11b4741e2a74f2a5a^{commit}'
  exit_code: 0
  status: passed
  required: true
  summary: 'Preserved prior result: live CURIE4023OK/251skips; initial205 archive
    provenance check failed, explicit historical-commit recheck passed, full retry205valid
    and contract4passed. Failure cause not established; no input edits between failure/retry.
    Actual run: 2026-10-12T09:37:43Z to 2026-10-12T09:37:44Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: reused-post-save-archive-retry
  name: reused-post-save-archive-retry
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  status: passed
  required: true
  summary: 'Preserved prior result: live CURIE4023OK/251skips; initial205 archive
    provenance check failed, explicit historical-commit recheck passed, full retry205valid
    and contract4passed. Failure cause not established; no input edits between failure/retry.
    Actual run: 2026-10-12T09:39:53Z to 2026-10-12T09:41:13Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: reused-post-save-contract
  name: reused-post-save-contract
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  status: passed
  required: true
  summary: 'Preserved prior result: live CURIE4023OK/251skips; initial205 archive
    provenance check failed, explicit historical-commit recheck passed, full retry205valid
    and contract4passed. Failure cause not established; no input edits between failure/retry.
    Actual run: 2026-10-12T09:36:09Z to 2026-10-12T09:38:31Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
- check_id: adapter-datasets
  name: adapter-datasets
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  status: passed
  required: false
  summary: 'Fresh full inventory; no exact native organism dataset. Actual run: 2026-10-12T09:43:07Z
    to 2026-10-12T09:43:07Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - adapter
- check_id: perez-claim-attribution
  name: Cited-review body attribution
  status: unavailable
  required: true
  summary: Publisher body capture returned HTTP403; alternate web full-text/PDF opens
    were inaccessible. Abstract/metadata read, but exact distribution and b6f/PSI
    source attributions remain unverified. No exit code invented for this scientific
    reading check.
  target_ids:
  - GO:0030094
  evidence_ids:
  - perez
  - access
- check_id: draft-contract-corrected
  name: Initial draft validation
  command: .venv/bin/python scripts/record_review.py validate /private/tmp/csm-review-20261012T094255Z-pmpsi/observation.yaml
  exit_code: 1
  status: failed
  required: false
  summary: 'Initial draft used uncertain/context instead of the contract enums unknown/context_only.
    Corrected without changing the scientific assessment. Actual run: 2026-10-12T09:49:26Z
    to 2026-10-12T09:49:29Z.'
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
evidence:
- evidence_id: native
  kind: record_content
  reference: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
  locator: Entire YAML and its one append-only history file
  summary: The canonical PCC6803 example, graph description, membrane-houses-PSI edge
    and discussion attribute microscopy to Synechocystis. Components are explicitly
    deferred. The historical issue754 process-edge evidence fix is distinct from the
    present organism mismatch.
  support: supports
  accessed_at: '2026-10-12T09:49:26Z'
  snapshot_sha256: 43644bf79c44cc9c1674f8619a1cb977673a94b3bff2be2461eed104d03d0cdb
- evidence_id: go
  kind: authority
  reference: GO:0030094; GO:0009522; GO:0031676; GO:0030075; GO:0009767; GO:0009512
  locator: All six current GO entries, definitions, names and aspects
  summary: Bacterial thylakoid PSI identity, generic PSI parent, bacterial membrane
    container and electron-transport process are compatible. The GO name is not independent
    proof of a particular membrane-biogenesis mechanism.
  support: supports
  accessed_at: '2026-10-12T09:42:56Z'
  snapshot_sha256: 069ed93a8da53b7f91f628bf3acffaa2a18a7ac9ae8403d43ac74369c95c74a5
- evidence_id: casella
  kind: primary_source
  reference: https://doi.org/10.1016/j.molp.2017.09.019
  locator: Complete abstract and Introduction; Strains and Growth Conditions; Generation
    of Constructs; distribution and mobility Results sections
  summary: The directly studied organism is Synechococcus elongatus PCC7942. PSI imaging
    used chromosomal PsaE-eGFP fusions in that strain. The article discusses earlier
    PCC6803 studies as background, but these are not its own organism-specific distribution/mobility
    experiments.
  support: partial
  accessed_at: '2026-10-12T09:43:44Z'
  snapshot_sha256: ea4b104ec579c77bad24b06160d8f9b512ba2a3746f4b899cbcc7878e212c224
- evidence_id: perez
  kind: authority
  reference: https://doi.org/10.1146/annurev-cellbio-120823-022747
  locator: Complete abstract and bibliographic identity from Europe PMC, Crossref
    and publisher landing page; body unavailable
  summary: Perez-Boerema, Engel and Wietrzynski2024 review thylakoid structural diversity
    across cyanobacteria and photosynthetic eukaryotes. The inspected abstract does
    not establish the exact b6f-to-carrier-to-PSI attribution in the native evidence
    notes.
  support: partial
  accessed_at: '2026-10-12T09:42:59Z'
  snapshot_sha256: d2469ab1736b506b719d5c3ed200a00504885c61f22f4f60117405441d98ae72
- evidence_id: access
  kind: validation
  reference: https://www.annualreviews.org/deliver/fulltext/cellbio/40/1/annurev-cellbio-120823-022747.html?itemId=/content/journals/10.1146/annurev-cellbio-120823-022747&mimeType=html&fmt=ahah
  locator: Recorded HTTP403 response, not article text
  summary: The publisher full-text request failed with HTTP403 and its bytes are retained
    as an access-failure artifact. Web opens of the full-text and Crossref-linked
    PDF endpoints were also inaccessible. The author-lab publication list only linked
    to PubMed. Search snippets were not treated as inspected source text.
  support: context_only
  accessed_at: '2026-10-12T09:44:28Z'
  snapshot_sha256: d900d31ebbb7ad3e2d7c8447753d5d7072be800406998f42d32b219fbff0d5eb
- evidence_id: adapter
  kind: database
  reference: https://imodulondb.org/
  locator: Fresh complete28-dataset inventory
  summary: No exact PCC6803 dataset applies. PCC7942 is covered but is a possible
    source-specific correction, not the current native organism; no gene-level claim
    is made in this record and no expression module is substituted for microscopy
    evidence.
  support: supports
  accessed_at: '2026-10-12T09:49:26Z'
- evidence_id: validation
  kind: validation
  reference: /private/tmp/csm-review-20261012T094255Z-pmpsi/baseline-verification.json
  locator: Fresh target gates and hash-verified unchanged-input wider checks
  summary: Schema and strict checks pass. Zero of16 citations carries a snippet. Wider
    QC987passed/3skipped and label/trait cache limits are retained; later live CURIE
    and205-bundle archive/contract checks are reused explicitly rather than reported
    as freshly executed.
  support: supports
  accessed_at: '2026-10-12T09:49:26Z'
- evidence_id: search
  kind: search
  reference: reviews/structured/
  locator: Ignored-inclusive canonical and native/legacy searches
  summary: Exact target has no canonical predecessor among205 bundles. No exact legacy
    report or occurrence of the new issue key was found in the searched local review/research/curation
    roots. This is not a remote issue-absence claim.
  support: supports
  accessed_at: '2026-10-12T09:49:26Z'
  search_scope: Path.rglob included hidden/ignored canonical bundles; rg -uu searched
    target slug/identifier and issue key in data/structures, reviews, reports/yaml_record_review,
    history, research and curation.
- evidence_id: tax-1117
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1117
  locator: Complete current taxonomy entry
  summary: Native broad Cyanobacteriota label and ID agree.
  support: supports
  accessed_at: '2026-10-12T09:42:57Z'
  snapshot_sha256: 902dbbe6c250ccb733ac96b08f75a20556e8fbc50c444a8a05c354ff5296cddf
- evidence_id: tax-1148
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1148
  locator: Complete current taxonomy entry
  summary: PCC6803 resolves to the native Synechocystis label, but not the directly
    studied Casella strain.
  support: supports
  accessed_at: '2026-10-12T09:42:57Z'
  snapshot_sha256: 84c0a354189f6b736c57eb3886dc08090cd6edba80c6e35c1b92909c26f35ab4
- evidence_id: tax-1140
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/1140
  locator: Complete current taxonomy entry
  summary: PCC7942 resolves to Synechococcus elongatus, the organism directly studied
    by Casella2017.
  support: supports
  accessed_at: '2026-10-12T09:43:45Z'
  snapshot_sha256: 70bf02b8ca783e9afbd060d6c098a79cec71954ea2d64a270fc130481a63cb2b
assessments:
- assessment_id: identity
  area: identity
  topic: Bacterial PSI complex boundary and hierarchy
  outcome: supported
  summary: Exact GO identity, complex kind, PSI parentage and bacterial-thylakoid
    parthood agree. Related cyanobacterial PSI synonym is compatible; no plastid PSI
    or whole-membrane identity is substituted.
  target_ids:
  - GO:0030094
  evidence_ids:
  - native
  - go
  - casella
- assessment_id: composition
  area: completeness
  topic: Deferred subunits and optional quantities
  outcome: supported
  summary: The record makes no subunit stoichiometry, imaging measurement or protein-accession
    claim. Its explicit component-boundary TODO is a legitimate curation limit, not
    by itself a concrete defect. No optional row is required solely to generate a
    finding.
  target_ids:
  - GO:0030094
  evidence_ids:
  - native
  - go
  - casella
- assessment_id: example
  area: scope
  topic: Direct experimental organism
  outcome: concern
  summary: The nearest primary source directly maps localization/mobility in PCC7942,
    not PCC6803. Its background discussion of PCC6803 cannot be silently recast as
    the current experiment. The finding does not deny the biological occurrence of
    PSI in PCC6803.
  target_ids:
  - GO:0030094
  evidence_ids:
  - native
  - casella
  - tax-1148
  - tax-1140
  dimensions:
  - name: native_organism
    value: Synechocystis sp. PCC6803 / NCBITaxon:1148
    definition: Current canonical example and graph organism.
    evidence_ids:
    - native
    - tax-1148
  - name: experimental_organism
    value: Synechococcus elongatus PCC7942 / NCBITaxon:1140
    definition: Direct experimental organism in the cited primary study; PsaE-eGFP
      imaging must retain tagged-strain context.
    evidence_ids:
    - casella
    - tax-1140
- assessment_id: distribution
  area: evidence
  topic: Cyanobacterial thylakoid occurrence and cited-review scope
  outcome: unknown
  summary: GO and the inspected primary study support bacterial thylakoid PSI occurrence;
    the qualitative COMMON assertion is not a quantitative prevalence claim. Exact
    scope of the Perez-Boerema body passage supporting the native distribution note
    remains unverified.
  target_ids:
  - GO:0030094
  evidence_ids:
  - native
  - go
  - casella
  - perez
  - tax-1117
- assessment_id: function
  area: evidence
  topic: PSI downstream electron-input attribution
  outcome: unknown
  summary: Generic PSI participation is compatible with GO and primary-paper context.
    The exact Perez-Boerema attribution for b6f-to-soluble-carrier-to-PSI remains
    unchecked because the body is unavailable; this is not proof that the biological
    chain or citation is wrong.
  target_ids:
  - GO:0030094
  evidence_ids:
  - native
  - go
  - casella
  - perez
  - access
- assessment_id: graph
  area: graph
  topic: All four nonmechanistic edges
  outcome: concern
  summary: Parthood is supported. The houses edge misattributes the source organism.
    Both process edges require the inaccessible review-body check. The b6f edge explicitly
    includes a downstream soluble carrier, so no false direct-contact finding is made.
  target_ids:
  - GO:0030094
  evidence_ids:
  - native
  - go
  - casella
  - perez
  - access
- assessment_id: discussion
  area: provenance
  topic: Actionable subunit-boundary discussion
  outcome: concern
  summary: The discussion is relevant, but repeats the wrong source organism. Correct
    it alongside the canonical example and graph without forcing unrelated component
    expansion.
  target_ids:
  - GO:0030094
  evidence_ids:
  - native
  - casella
- assessment_id: checks
  area: schema
  topic: Deterministic validation and stable identifiers
  outcome: supported
  summary: Native GO, taxonomy and DOI identities resolve. Author/title/year notes
    agree with metadata. Schema validation cannot establish organism-specific experimental
    support or replace the missing full-text check.
  target_ids:
  - GO:0030094
  evidence_ids:
  - validation
  - go
  - casella
  - perez
  - tax-1148
- assessment_id: ownership
  area: ownership
  topic: Histories, status and retained observations
  outcome: supported
  summary: Entire native YAML and append-only history were read. Maintained YAML owns
    future guarded corrections; no generated output or history is changed and PROPOSED
    remains. No canonical predecessor exists for this exact target, so no disposition
    is fabricated.
  target_ids:
  - GO:0030094
  evidence_ids:
  - native
  - search
findings:
- finding_id: F1
  issue_key: plasma-membrane-derived-psi-casella-taxon
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Correct the organism attributed to Casella2017 PSI microscopy
  description: The record attributes Casella2017 PSI distribution and mobility experiments
    to Synechocystis PCC6803. Its methods and Results directly study Synechococcus
    elongatus PCC7942, including PsaE-eGFP imaging. Align the source-specific example,
    graph and discussion with that organism and experimental context, or retain PCC6803
    using separately inspected primary evidence. The paper does mention earlier PCC6803
    studies; the defect is conflating background with its direct experiment, not claiming
    the organism is absent from the article.
  target_ids:
  - GO:0030094
  field_paths:
  - canonical_examples[taxon_id=NCBITaxon:1148]
  - causal_graphs[cyanobacterial_psi_electron_input].description
  - causal_graphs[cyanobacterial_psi_electron_input].edges[subject=thylakoid_membrane,object=psi].description
  - causal_graphs[cyanobacterial_psi_electron_input].edges[subject=thylakoid_membrane,object=psi].evidence
  - discussions[psi_subunit_boundaries].evidence
  evidence_ids:
  - native
  - casella
  - tax-1148
  - tax-1140
  rule_id: review-checklist:taxon-strain-and-experimental-evidence-scope
  native_severity: major
  normalization_reason: Multiple scientific claims are attributed to the wrong experimental
    organism; a valid taxon ID and generic PSI occurrence do not repair nearest-source
    support.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
    role: maintained scientific record
actions:
- action_id: A1
  description: Correct all source-specific organism attributions consistently, preserving
    tagged-strain experimental context; alternatively inspect a PCC6803 primary source
    before retaining that example. Do not change the valid GO structure identity.
  finding_ids:
  - F1
  target_ids:
  - GO:0030094
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
    role: maintained scientific record
  generator: Native guarded writer and documented product workflow after separately
    authorized curation.
  acceptance_checks:
  - Canonical example, graph and discussion consistently identify the actual directly
    studied strain and nearest source.
  - No background citation or expression-module hit is substituted for inspected experimental
    evidence.
  - Retain valid PSI hierarchy, carrier-qualified graph scope, PROPOSED status and
    append-only curation history.
  - Run native validation and save a successor retaining this stable issue key; resolve
    the outstanding Perez-Boerema attribution check before claiming complete scientific
    review.
limitations:
- Same-agent review, not independent human sign-off, exhaustive literature/retraction
  search or raw experimental reanalysis.
- Casella primary evidence was read in the specified abstract/Introduction/Results/Methods
  sections, not every figure pixel, supplement or raw imaging dataset. Quantitative
  FRAP values are not added to this qualitative native record.
- Perez-Boerema metadata and complete abstract were inspected, but its full-text body
  remained inaccessible. The exact native distribution and process-edge attributions
  are unassessed; this partial result must not be counted as a completed review.
- Nine local HTTP captures returned200 and one publisher-body request returned403.
  Error HTML is retained as a failure artifact, not scientific evidence; search snippets
  and uninspected background papers were not promoted into proof.
- Fresh target checks and explicitly hash-verified wider-check reuse retain original
  skips/cache limits. Prior205-bundle archive failure and successful historical-commit
  recheck/full retry are both retained; the failure cause is unknown.
- No exact native iModulonDB dataset applies and no gene-level claim is present. Coverage
  of the possible correction strain is not itself support for localization or experimental
  phenotype.
- No native scientific edits, generated products, status/history changes or GitHub
  mutation. Remote historical issue754/PR753 status was not refreshed. Existing external-publication
  approval remains unanswered; no bypass or retry.
tags:
- scientific-review
- energy-complex
- taxon-scope
- major
- partial
```
