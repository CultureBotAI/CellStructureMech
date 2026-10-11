# Haptonema: scientific evidence review

- Review: 20261011T040559Z-haptonema-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T03:55:21Z
- Finished UTC: 2026-10-11T04:05:59Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record assessed; one concrete evidence issue observed. Deferred molecular grounding and optional absent fields are not findings.

## Scope And Provenance

Entire native YAML, every present scientific claim and both history surfaces.

Selection: Sequential unassessed target in the all-909-record worklist; this observation covers one record.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7dc2dbb326ca4e7c2f6d8e9cc24859dd3afdbc23.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:haptonema | data/structures/appendage/haptonema.yaml | maintained | haptonema |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:haptonema | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| strict | passed | True | cellstructuremech:haptonema | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| snippets | passed | True | cellstructuremech:haptonema | No quoted snippets present; successful exit performs no quotation matching. Scientific paraphrases inspected separately. |
| history | failed | False | cellstructuremech:haptonema | Initial history invocation selected a missing pyenv Python via PATH; superseded by successful required history-venv-path rerun, not a native-record defect. |
| labels | passed | True | cellstructuremech:haptonema | 3544 canonical labels, 50 synonyms and six exceptions accepted; 603 non-adapter pairs skipped. Relevant target authorities separately inspected. |
| traits | passed | True | cellstructuremech:haptonema | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| curies | passed | True | cellstructuremech:haptonema | 4009 identifiers OK, 251 skipped. BFO resolver controls were not exercised because its authority was unreachable. Neither skips nor unavailable controls certify those namespaces. Exact target GO/taxon authorities separately inspected. |
| reviews | passed | True | cellstructuremech:haptonema | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| diff | passed | True | cellstructuremech:haptonema | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| history-venv-path | passed | True | cellstructuremech:haptonema | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| Exact-baseline authoritative CI QC | passed | True | cellstructuremech:haptonema | Authoritative full QC passed on the exact unchanged baseline, not a newly run local full QC. |
| Structured-source applicability | passed | False | cellstructuremech:haptonema | iModulonDB dataset inventory has no applicable Haptophyta or Chlamydomonas dataset. No module query applied; lack of coverage is not negative biological evidence. |

## Scientific And Domain Assessments

### Native identity, definition and appendage boundary

identity: supported. Targets: cellstructuremech:haptonema.

Membrane-bounded microtubule-supported haptophyte appendage, not a conventional flagellum or generic tubulin. No asserted parent/parthood needs correction.

### Scaffold constituent and deferred gene-level inventory

grounding: supported. Targets: cellstructuremech:haptonema.

Morphological singlet-microtubule bundle is supported; six-to-seven wording is attributed to prior ultrastructure rather than fixed universal stoichiometry. Exact linker/channel identities remain explicitly open.

### Distribution, name change and canonical example

scope: supported. Targets: cellstructuremech:haptonema.

VARIABLE clade presence and the Haptolina/Chrysochromulina hirta example are appropriately bounded.

### Both functions and four nonmechanistic edges

evidence: supported. Targets: cellstructuremech:haptonema.

Calcium-dependent coiling, microtubule scaffold and possible capture/delivery are supported. The graph explicitly defers motors and ion-channel mechanisms; the 1995 species-specific capture distinction is not erased by its bounded note.

### Experimental interpretation in calcium-edge note

evidence: concern. Targets: cellstructuremech:haptonema.

An observed calcium-dependent shape response after taxol is promoted to an unqualified finding that calcium influx was not prevented. The inspected Results and Methods do not measure influx directly.

### Citations, optional fields, histories and native status

provenance: supported. Targets: cellstructuremech:haptonema.

Claim-local sources and bibliographic identities were checked at the access tiers stated. No trait links, image attributions, quantitative-property dataset, complex stoichiometry or protein examples are asserted. Past histories and PROPOSED status are preserved; absent optional fields are not defects.

## Findings

### F1: Bound the taxol/calcium note to the measured shape response

minor / open / confirmed; issue key: haptonema-calcium-influx-overstatement.

The calcium-edge note says Nomura 2019 found taxol blocked coiling without preventing Ca2+ influx. Fig. 6 instead reports shape changes after calcium addition to taxol-treated cells. The inspected Results/Methods establish residual calcium responsiveness, not an unchanged influx measurement. This bounded source-attribution overstatement can be corrected without changing the supported nonmechanistic edge.

## Recommended Actions And Acceptance Checks

### A1

Replace the evidence note with the observed taxol inhibition and calcium-addition shape response; distinguish this from a direct calcium-influx measurement.

- Note describes taxol-blocked rapid coiling and the calcium-induced helix-to-planar-bend response.
- No claim of unchanged calcium influx or restoration of normal coiling is introduced.
- Other native claims, prior discussions, stable IDs and PROPOSED status are preserved.
- Guarded curation, append-only histories, affected generated artifacts and focused regression tests pass native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/haptonema.yaml; Entire native YAML and append-only histories | context_only | Native target assessed before edits; PROPOSED status and prior curation retained. |
| prior-search | reviews/structured/ and reports/yaml_record_review/; haptonema and exact identifier | context_only | No earlier exact-target review finding found in these bounded roots. Prior issues #773 and #775 concern canonical-example citation and clade presence respectively, not these new findings. |
| nomura | DOI:10.1242/bio.036590; Introduction, Results including Fig. 6, Discussion and Materials and Methods | supports | NIES-4122 microtubule architecture and rapid coiling support the scaffold and calcium-dependent behavior. Taxol inhibited normal coiling; adding CaCl2 after calcium-free taxol treatment converted a right-handed helix to planar bending. The inspected assay measures shape response, not unchanged calcium influx. |
| taxon-clade | https://rest.uniprot.org/taxonomy/2830.json; Exact taxonomy identity | supports | Haptophyta identity matches the VARIABLE distribution row. |
| taxon-example | https://rest.uniprot.org/taxonomy/35142.json; Name and synonyms | supports | Haptolina hirta includes the historical Chrysochromulina hirta name used in the feeding study. |
| go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=haptonema&amp;limit=100; Exact lexical query haptonema | context_only | No match in this bounded GO query; does not prove absence from every ontology. Native identity avoids substituting a broader microtubule term. |
| kawachi1991 | DOI:10.2216/i0031-8884-30-6-563.1; Author-uploaded primary abstract and figure captions on ResearchGate; not unavailable PDF preview | supports | Particles adhere to the C. hirta haptonema, aggregate and are delivered to the cell for phagocytosis. Supports capture and transport without assigning a molecular motor. |
| kawachi1995 | DOI:10.2216/i0031-8884-34-3-193.1; Author-uploaded primary abstract and figure captions on ResearchGate; body font encoding not reliably readable | supports | In C. spinifera spine scales capture particles and the haptonema delivers them. The native note only attributes a feeding role, not direct capture in this species. |
| andersen | DOI:10.3732/ajb.91.10.1508; Publisher review Introduction and flagellar-apparatus section; secondary synthesis | supports | Explicit secondary loss of haptonemata supports VARIABLE Haptophyta presence. This is review evidence, not a new experiment. |

## Limits And Additional Notes

- Nomura full main-text sections were inspected; supplemental movies or unseen assays are not claimed as reviewed. The finding is bounded to the inspected experiment.
- Kawachi papers were assessed from primary abstracts and captions on author-uploaded pages; publisher access was blocked and the 1995 body encoding was unreliable. Andersen is explicitly secondary synthesis.
- Same-agent assessment, not independent human sign-off or completion of the 909-record goal.
- Initial history PATH failure was superseded by a successful virtual-environment rerun. Exact-baseline CI supplies full QC; skipped resolver namespaces and unreachable BFO controls are not certified.
- No applicable iModulonDB dataset; this is not evidence of biological absence. No quotations were present to verify, so paraphrases required separate source inspection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T040559Z-haptonema-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Haptonema: scientific evidence review'
started_at: '2026-10-11T03:55:21Z'
finished_at: '2026-10-11T04:05:59Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source assessment before mutation; not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record assessed; one concrete evidence issue observed. Deferred
  molecular grounding and optional absent fields are not findings.
source:
  git_revision: 7dc2dbb326ca4e7c2f6d8e9cc24859dd3afdbc23
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
  - path: data/structures/appendage/haptonema.yaml
    sha256: b0d8436108c564a99bb634dd646c4e078934bfa2ac359336457557131b7f8ebb
    role: target
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
  - path: history/records/haptonema/2026-09-13T104036Z-codex-e4306d.yaml
    sha256: 2c41a2651c993ed0b02bfd855fa518789f753a2d63fc17a8751994b4e52a94fd
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: cellstructuremech:haptonema
  path: data/structures/appendage/haptonema.yaml
  label: haptonema
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/haptonema.yaml
    role: maintained scientific record
scope:
  description: Entire native YAML, every present scientific claim and both history
    surfaces.
  selection: Sequential unassessed target in the all-909-record worklist; this observation
    covers one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:haptonema
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/haptonema.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; shape, identifiers and quotations do not by themselves
    establish biological support.
  scope_note: 2026-10-11T03:55:39Z to 2026-10-11T03:55:42Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/haptonema.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; shape, identifiers and quotations do not by themselves
    establish biological support.
  scope_note: 2026-10-11T03:55:42Z to 2026-10-11T03:55:47Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/haptonema.yaml
    --report /private/tmp/csm-review-20261011T035459Z/haptonema-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No quoted snippets present; successful exit performs no quotation matching.
    Scientific paraphrases inspected separately.
  scope_note: 2026-10-11T03:55:47Z to 2026-10-11T03:56:13Z; log SHA-256 76a62fd5ec31e6ba130825b4a29c72af0af9ccf523b06b12b351759481bf488c
- check_id: history
  name: history
  status: failed
  required: false
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 1
  expected_exit_code: 0
  summary: Initial history invocation selected a missing pyenv Python via PATH; superseded
    by successful required history-venv-path rerun, not a native-record defect.
  scope_note: 2026-10-11T03:58:04Z to 2026-10-11T03:58:19Z; log SHA-256 7a5966a3b17af2f9351ff6ee03f3aea116e7f7f66b033d5a47ed829897e1cf73
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: 3544 canonical labels, 50 synonyms and six exceptions accepted; 603 non-adapter
    pairs skipped. Relevant target authorities separately inspected.
  scope_note: 2026-10-11T03:58:19Z to 2026-10-11T04:01:36Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; shape, identifiers and quotations do not by themselves
    establish biological support.
  scope_note: 2026-10-11T04:01:36Z to 2026-10-11T04:02:14Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/check_curies.py --check --report /private/tmp/csm-review-20261011T035459Z/curies.tsv
  exit_code: 0
  expected_exit_code: 0
  summary: 4009 identifiers OK, 251 skipped. BFO resolver controls were not exercised
    because its authority was unreachable. Neither skips nor unavailable controls
    certify those namespaces. Exact target GO/taxon authorities separately inspected.
  scope_note: 2026-10-11T04:02:14Z to 2026-10-11T04:03:23Z; log SHA-256 2e9bc07c9919e1e93c42cc1faaf08e9652ad00faacba05e189c139f5e1eb1afc
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; shape, identifiers and quotations do not by themselves
    establish biological support.
  scope_note: 2026-10-11T04:03:23Z to 2026-10-11T04:04:31Z; log SHA-256 707fa7427c86e537a7eeb10602a8b211cf38bc5a2ddac92233842df6a35c2fe3
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; shape, identifiers and quotations do not by themselves
    establish biological support.
  scope_note: 2026-10-11T04:04:31Z to 2026-10-11T04:04:32Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: history-venv-path
  name: history-venv-path
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: env PATH=/Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/Mechs/CellStructureMech/.venv/bin:/Users/marcin/.codex/packages/app-server-daemon/releases/0.162.1-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg0h2cTt3:/Users/marcin/.codex/tmp/arg0/codex-arg0Cl1Ll3:/Users/marcin/.codex/packages/app-server-daemon/releases/0.162.0-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg00NOnnV:/Users/marcin/.codex/packages/app-server-daemon/releases/0.161.0-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg0vMm3oW:/Users/marcin/.codex/packages/app-server-daemon/releases/0.160.1-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg0m0Bk6L:/Users/marcin/.codex/packages/app-server-daemon/releases/0.160.0-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg0TFYScl:/Users/marcin/.codex/packages/app-server-daemon/releases/0.159.3-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg0H4jslX:/Users/marcin/.codex/packages/app-server-daemon/releases/0.159.2-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg0CCBUVT:/Users/marcin/.codex/packages/app-server-daemon/releases/0.159.1-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg0apP4Kl:/Users/marcin/.codex/packages/app-server-daemon/releases/0.159.0-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg07qMB5c:/Users/marcin/.codex/packages/app-server-daemon/releases/0.158.0-x86_64-apple-darwin/codex-path:/Users/marcin/.codex/tmp/arg0/codex-arg0HRXmMN:/Users/marcin/.nvm/versions/node/v22.23.2/lib/node_modules/@openai/codex/node_modules/@openai/codex-darwin-x64/vendor/x86_64-apple-darwin/codex-path:/usr/local/Caskroom/miniforge/base/bin:/usr/local/Caskroom/miniforge/base/condabin:/Users/marcin/.nvm/versions/node/v22.23.2/bin:/Users/marcin/.local/bin:/Users/marcin/.poetry/bin:/Users/marcin/.cargo/bin:/Users/marcin/.pyenv/shims:/Users/marcin/.poetry/bin:/opt/local/bin:/opt/local/sbin:/usr/local/bin:/System/Cryptexes/App/usr/bin:/usr/bin:/bin:/usr/sbin:/sbin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/local/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/bin:/var/run/com.apple.security.cryptexd/codex.system/bootstrap/usr/appleinternal/bin:/pkg/env/global/bin:/opt/X11/bin:/Library/Apple/usr/bin:/usr/texbin:/usr/local/bin:/usr/local/mysql/bin:/Users/marcin/Documents/VIMSS/ontology/AIO/artificial-intelligence-ontology/relation-graph/cli/target/universal/stage/bin:/Users/marcin/Documents/VIMSS/ontology/OAK/ontology-access-kit/relation-graph/cli/target/universal/stage/bin
    .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; shape, identifiers and quotations do not by themselves
    establish biological support.
  scope_note: 2026-10-11T03:58:38Z to 2026-10-11T03:59:21Z; log SHA-256 b47bc6efbda2d1c9680d9da2a2742f00717dde852f867c5249e3dc3ea3710dd7
- check_id: qc
  name: Exact-baseline authoritative CI QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:haptonema
  command: gh run view 38107609075 --json status,conclusion,headSha,event,name,url,jobs;
    gh run view 38107609075 --log
  exit_code: 0
  summary: Authoritative full QC passed on the exact unchanged baseline, not a newly
    run local full QC.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38107609075;
    full log SHA-256 e14bdb51e92e65815b0cb7344279f2c8cded22cd86b265902bcd6c760022e937
- check_id: adapter
  name: Structured-source applicability
  status: passed
  required: false
  target_ids:
  - cellstructuremech:haptonema
  command: /Users/marcin/Documents/VIMSS/ontology/KG-Hub/KG-Microbe/culturebotai-claw/.venv/bin/kg-microbe-sources
    imodulondb datasets
  exit_code: 0
  summary: iModulonDB dataset inventory has no applicable Haptophyta or Chlamydomonas
    dataset. No module query applied; lack of coverage is not negative biological
    evidence.
  scope_note: 2026-10-11T03:57:18Z to 2026-10-11T03:57:20Z; log SHA-256 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/haptonema.yaml
  locator: Entire native YAML and append-only histories
  accessed_at: '2026-10-11T04:05:59Z'
  snapshot_sha256: b0d8436108c564a99bb634dd646c4e078934bfa2ac359336457557131b7f8ebb
  support: context_only
  summary: Native target assessed before edits; PROPOSED status and prior curation
    retained.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: haptonema and exact identifier
  accessed_at: '2026-10-11T04:05:59Z'
  support: context_only
  search_scope: rg --no-ignore --hidden in both review roots and the exact history
    directory included ignored files. GitHub all-state search for mastigoneme OR haptonema
    returned three earlier distinct, closed issues.
  summary: 'No earlier exact-target review finding found in these bounded roots. Prior
    issues #773 and #775 concern canonical-example citation and clade presence respectively,
    not these new findings.'
- evidence_id: nomura
  kind: primary_source
  reference: DOI:10.1242/bio.036590
  locator: Introduction, Results including Fig. 6, Discussion and Materials and Methods
  accessed_at: '2026-10-11T03:57:07Z'
  snapshot_sha256: b01fa9e239c67f2e3130906f6b144243dcdf63ae2b3f7fd3d36099c7b0fe1559
  support: supports
  summary: NIES-4122 microtubule architecture and rapid coiling support the scaffold
    and calcium-dependent behavior. Taxol inhibited normal coiling; adding CaCl2 after
    calcium-free taxol treatment converted a right-handed helix to planar bending.
    The inspected assay measures shape response, not unchanged calcium influx.
- evidence_id: taxon-clade
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/2830.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T03:57:22Z'
  snapshot_sha256: 5c1967ec75f6ec3db677bb2f29619d984b218e777dadfa53ca0af5ffda543e66
  support: supports
  summary: Haptophyta identity matches the VARIABLE distribution row.
- evidence_id: taxon-example
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/35142.json
  locator: Name and synonyms
  accessed_at: '2026-10-11T03:57:23Z'
  snapshot_sha256: e51f95793844c6030c1454334ec2780bbe3b7782578d0bf1d33815d4dd176a99
  support: supports
  summary: Haptolina hirta includes the historical Chrysochromulina hirta name used
    in the feeding study.
- evidence_id: go-search
  kind: search
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=haptonema&limit=100
  locator: Exact lexical query haptonema
  accessed_at: '2026-10-11T03:57:20Z'
  snapshot_sha256: f3a7dae9b1e9335291e3940cdf0e5f8dadf9335da7b9547710606b5106c63f86
  support: context_only
  summary: No match in this bounded GO query; does not prove absence from every ontology.
    Native identity avoids substituting a broader microtubule term.
  search_scope: Exact lexical query haptonema; only the recorded QuickGO service query,
    not an exhaustive ontology or repository absence search.
- evidence_id: kawachi1991
  kind: primary_source
  reference: DOI:10.2216/i0031-8884-30-6-563.1
  locator: Author-uploaded primary abstract and figure captions on ResearchGate; not
    unavailable PDF preview
  accessed_at: '2026-10-11T04:05:59Z'
  support: supports
  summary: Particles adhere to the C. hirta haptonema, aggregate and are delivered
    to the cell for phagocytosis. Supports capture and transport without assigning
    a molecular motor.
- evidence_id: kawachi1995
  kind: primary_source
  reference: DOI:10.2216/i0031-8884-34-3-193.1
  locator: Author-uploaded primary abstract and figure captions on ResearchGate; body
    font encoding not reliably readable
  accessed_at: '2026-10-11T04:05:59Z'
  support: supports
  summary: In C. spinifera spine scales capture particles and the haptonema delivers
    them. The native note only attributes a feeding role, not direct capture in this
    species.
- evidence_id: andersen
  kind: primary_source
  reference: DOI:10.3732/ajb.91.10.1508
  locator: Publisher review Introduction and flagellar-apparatus section; secondary
    synthesis
  accessed_at: '2026-10-11T04:05:59Z'
  support: supports
  summary: Explicit secondary loss of haptonemata supports VARIABLE Haptophyta presence.
    This is review evidence, not a new experiment.
assessments:
- assessment_id: identity
  area: identity
  topic: Native identity, definition and appendage boundary
  outcome: supported
  target_ids:
  - cellstructuremech:haptonema
  evidence_ids:
  - record
  - nomura
  - go-search
  summary: Membrane-bounded microtubule-supported haptophyte appendage, not a conventional
    flagellum or generic tubulin. No asserted parent/parthood needs correction.
- assessment_id: composition
  area: grounding
  topic: Scaffold constituent and deferred gene-level inventory
  outcome: supported
  target_ids:
  - cellstructuremech:haptonema
  evidence_ids:
  - record
  - nomura
  summary: Morphological singlet-microtubule bundle is supported; six-to-seven wording
    is attributed to prior ultrastructure rather than fixed universal stoichiometry.
    Exact linker/channel identities remain explicitly open.
- assessment_id: scope
  area: scope
  topic: Distribution, name change and canonical example
  outcome: supported
  target_ids:
  - cellstructuremech:haptonema
  evidence_ids:
  - taxon-clade
  - taxon-example
  - andersen
  - kawachi1991
  summary: VARIABLE clade presence and the Haptolina/Chrysochromulina hirta example
    are appropriately bounded.
- assessment_id: functions
  area: evidence
  topic: Both functions and four nonmechanistic edges
  outcome: supported
  target_ids:
  - cellstructuremech:haptonema
  evidence_ids:
  - nomura
  - kawachi1991
  - kawachi1995
  summary: Calcium-dependent coiling, microtubule scaffold and possible capture/delivery
    are supported. The graph explicitly defers motors and ion-channel mechanisms;
    the 1995 species-specific capture distinction is not erased by its bounded note.
- assessment_id: influx-note
  area: evidence
  topic: Experimental interpretation in calcium-edge note
  outcome: concern
  target_ids:
  - cellstructuremech:haptonema
  evidence_ids:
  - record
  - nomura
  summary: An observed calcium-dependent shape response after taxol is promoted to
    an unqualified finding that calcium influx was not prevented. The inspected Results
    and Methods do not measure influx directly.
- assessment_id: provenance
  area: provenance
  topic: Citations, optional fields, histories and native status
  outcome: supported
  target_ids:
  - cellstructuremech:haptonema
  evidence_ids:
  - record
  - nomura
  summary: Claim-local sources and bibliographic identities were checked at the access
    tiers stated. No trait links, image attributions, quantitative-property dataset,
    complex stoichiometry or protein examples are asserted. Past histories and PROPOSED
    status are preserved; absent optional fields are not defects.
findings:
- finding_id: F1
  issue_key: haptonema-calcium-influx-overstatement
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Bound the taxol/calcium note to the measured shape response
  description: The calcium-edge note says Nomura 2019 found taxol blocked coiling
    without preventing Ca2+ influx. Fig. 6 instead reports shape changes after calcium
    addition to taxol-treated cells. The inspected Results/Methods establish residual
    calcium responsiveness, not an unchanged influx measurement. This bounded source-attribution
    overstatement can be corrected without changing the supported nonmechanistic edge.
  target_ids:
  - cellstructuremech:haptonema
  field_paths:
  - causal_graphs[0].edges[1].evidence[0].notes
  evidence_ids:
  - record
  - nomura
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/haptonema.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded experimental-detail overstatement; the supported coarse
    edge remains valid.
actions:
- action_id: A1
  description: Replace the evidence note with the observed taxol inhibition and calcium-addition
    shape response; distinguish this from a direct calcium-influx measurement.
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:haptonema
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/haptonema.yaml
    role: maintained scientific record
  acceptance_checks:
  - Note describes taxol-blocked rapid coiling and the calcium-induced helix-to-planar-bend
    response.
  - No claim of unchanged calcium influx or restoration of normal coiling is introduced.
  - Other native claims, prior discussions, stable IDs and PROPOSED status are preserved.
  - Guarded curation, append-only histories, affected generated artifacts and focused
    regression tests pass native gates.
limitations:
- Nomura full main-text sections were inspected; supplemental movies or unseen assays
  are not claimed as reviewed. The finding is bounded to the inspected experiment.
- Kawachi papers were assessed from primary abstracts and captions on author-uploaded
  pages; publisher access was blocked and the 1995 body encoding was unreliable. Andersen
  is explicitly secondary synthesis.
- Same-agent assessment, not independent human sign-off or completion of the 909-record
  goal.
- Initial history PATH failure was superseded by a successful virtual-environment
  rerun. Exact-baseline CI supplies full QC; skipped resolver namespaces and unreachable
  BFO controls are not certified.
- No applicable iModulonDB dataset; this is not evidence of biological absence. No
  quotations were present to verify, so paraphrases required separate source inspection.
```
