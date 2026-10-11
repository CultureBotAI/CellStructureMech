# Mastigoneme: scientific evidence review

- Review: 20261011T040606Z-mastigoneme-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T03:55:28Z
- Finished UTC: 2026-10-11T04:06:06Z
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
| GO:0097741 | data/structures/appendage/mastigoneme.yaml | maintained | mastigoneme |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097741 | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| strict | passed | True | GO:0097741 | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| snippets | passed | True | GO:0097741 | No quoted snippets present; successful exit performs no quotation matching. Scientific paraphrases inspected separately. |
| history | failed | False | GO:0097741 | Initial history invocation selected a missing pyenv Python via PATH; superseded by successful required history-venv-path rerun, not a native-record defect. |
| labels | passed | True | GO:0097741 | 3544 canonical labels, 50 synonyms and six exceptions accepted; 603 non-adapter pairs skipped. Relevant target authorities separately inspected. |
| traits | passed | True | GO:0097741 | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| curies | passed | True | GO:0097741 | 4009 identifiers OK, 251 skipped. BFO resolver controls were not exercised because its authority was unreachable. Neither skips nor unavailable controls certify those namespaces. Exact target GO/taxon authorities separately inspected. |
| reviews | passed | True | GO:0097741 | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| diff | passed | True | GO:0097741 | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| history-venv-path | passed | True | GO:0097741 | Command passed; shape, identifiers and quotations do not by themselves establish biological support. |
| Exact-baseline authoritative CI QC | passed | True | GO:0097741 | Authoritative full QC passed on the exact unchanged baseline, not a newly run local full QC. |
| Structured-source applicability | passed | False | GO:0097741 | iModulonDB dataset inventory has no applicable Haptophyta or Chlamydomonas dataset. No module query applied; lack of coverage is not negative biological evidence. |

## Scientific And Domain Assessments

### GO identity, definition, appendage category and cilium parthood

identity: supported. Targets: GO:0097741.

Exact GO structure retained; generic ontology definition is distinguished from species-specific experiments.

### Three components and assembly graph

grounding: supported. Targets: GO:0097741.

MST1/MST3 are constituents; PKD2 is associated machinery. All three assembly edges are supported at the stated granularity. Complete source-neutral protein-family grounding is openly deferred; no complete inventory or unmeasured PKD2/SIP stoichiometry is asserted.

### Distribution and canonical example

scope: supported. Targets: GO:0097741.

Species-scoped Chlamydomonas presence and PKD2-dependent organization example remain supported; no broader clade prevalence is guessed.

### Function claim and conflicting experimental results

evidence: concern. Targets: GO:0097741.

Unqualified motility contribution omits conflicting primary swimming/flow results. Different mutant lines and assay contexts prevent treating these as identical experiments or deciding that one universally refutes the other.

### Citations, optional fields, histories and native status

provenance: supported. Targets: GO:0097741.

Claim-local sources and bibliographic identities were checked at the access tiers stated. No trait links, image attributions, quantitative-property dataset, complex stoichiometry or protein examples are asserted. Past histories and PROPOSED status are preserved; absent optional fields are not defects.

## Findings

### F1: Qualify motility contribution with conflicting primary results

major / open / confirmed; issue key: mastigoneme-motility-evidence-conflict.

The sole function states that Chlamydomonas mastigonemes contribute to ciliary motility without context. Liu 2020 observed slower swimming in one mst1 line; Amador 2020 used another line and found no significant forward-speed, waveform or propulsive-flow benefit. Dai 2024, already cited by the record, acknowledges this conflict. The record should preserve these assay/strain-specific results rather than imply a settled general motility benefit.

## Recommended Actions And Acceptance Checks

### A1

Qualify the function and nearest evidence with both studies, exact mutant context and unresolved interpretation; retain the assembly graph and ontology definition.

- Retain the stable function ID while making the label and description explicitly context-dependent.
- Keep the Liu slower-swimming result and add Amador no-enhancement evidence with distinct mutant lines.
- Do not generalize Amador into no motility phenotype at all or promote proposed sensory/drag mechanisms to established facts.
- Preserve prior discussions and add an evidence-linked OPEN interpretation of the conflict.
- Guarded curation, append-only histories, affected generated artifacts and focused regression tests pass native gates.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/mastigoneme.yaml; Entire native YAML and append-only histories | context_only | Native target assessed before edits; PROPOSED status and prior curation retained. |
| prior-search | reviews/structured/ and reports/yaml_record_review/; mastigoneme and exact identifier | context_only | No earlier exact-target review finding found in these bounded roots. Prior issues #773 and #775 concern canonical-example citation and clade presence respectively, not these new findings. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097741; Exact active GO term and definition | supports | Native identity and literal definition match active GO:0097741. Its broad may-assist wording is not a demonstrated Chlamydomonas hydrodynamic effect. |
| cilium | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030990,GO:0032991,GO:0005929,GO:0005930,GO:0060271; GO:0005929 only | supports | Cilium identity supports the part_of context; mastigonemes are surface hairs, not the whole cilium. |
| taxon | https://rest.uniprot.org/taxonomy/3055.json; Exact taxonomy identity | supports | Chlamydomonas reinhardtii matches the scoped distribution and example. |
| dai | DOI:10.1016/j.cell.2024.03.005; Introduction, structural Results and relevant Discussion | supports | Cryo-EM resolves an MST1 filament around a single MST3 and supports both structural constituents. A proposed PKD2/SIP anchoring model is not treated as directly measured stoichiometry. Introduction notes conflicting motility studies; mst3 mutants have a modest swimming phenotype in this experiment. |
| liu | DOI:10.1083/jcb.202001122; PKD2 organization and motility Results, Discussion and strain/motility Methods | supports | PKD2 loss and rescue establish ciliary mastigoneme organization. mst1 LMJ.RY0402.052413 swam about 15% slower under the tested conditions; pkd2 phenotypes and nonadditivity do not establish a universal drag mechanism. |
| amador | DOI:10.1016/j.bpj.2020.05.003; Materials and Methods, Results and Discussion, Conclusions | supports | Different mstg line LMJ.RY0402.136134, compared with cw15 and cc125, lacked mastigonemes by TEM but showed no significant mean/normalized-maximum speed, waveform or propulsive-flow advantage from mastigonemes. Increased turning was observed; this does not mean all motility phenotypes were absent. |
| chen | PMID:943397; Primary abstract and bibliographic identity only | supports | Ochromonas mastigoneme isolation and glycoprotein analysis match the background citation. No Chlamydomonas stoichiometry or broader distribution is inferred from it. |

## Limits And Additional Notes

- Both 2020 papers were inspected at full main-text Methods/Results level; Dai structural sections and its conflicting-motility discussion were read, not every supplemental dataset.
- Chen 1976 was inspected at primary-abstract level and is only background provenance here. No reanalysis of swimming data or experimental resolution of the conflict was performed.
- Same-agent assessment, not independent human sign-off or completion of the 909-record goal.
- Initial history PATH failure was superseded by a successful virtual-environment rerun. Exact-baseline CI supplies full QC; skipped resolver namespaces and unreachable BFO controls are not certified.
- No applicable iModulonDB dataset; this is not evidence of biological absence. No quotations were present to verify, so paraphrases required separate source inspection.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T040606Z-mastigoneme-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Mastigoneme: scientific evidence review'
started_at: '2026-10-11T03:55:28Z'
finished_at: '2026-10-11T04:06:06Z'
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
  - path: data/structures/appendage/mastigoneme.yaml
    sha256: 34c249d8d02bcd5f887ef084d415e744691305e6f2dc9e096bba8c2a3e72d31e
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
  - path: history/records/mastigoneme/2026-09-13T102018Z-codex-be2059.yaml
    sha256: 03eb6304dab2a50e474efa9a040a0fd89181c3968acc83a34dd6ec2b15152eb6
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
- target_id: GO:0097741
  path: data/structures/appendage/mastigoneme.yaml
  label: mastigoneme
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/mastigoneme.yaml
    role: maintained scientific record
scope:
  description: Entire native YAML, every present scientific claim and both history
    surfaces.
  selection: Sequential unassessed target in the all-909-record worklist; this observation
    covers one record.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097741
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0097741
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/mastigoneme.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; shape, identifiers and quotations do not by themselves
    establish biological support.
  scope_note: 2026-10-11T03:57:08Z to 2026-10-11T03:57:14Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097741
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/mastigoneme.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Command passed; shape, identifiers and quotations do not by themselves
    establish biological support.
  scope_note: 2026-10-11T03:57:14Z to 2026-10-11T03:57:26Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097741
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/mastigoneme.yaml
    --report /private/tmp/csm-review-20261011T035459Z/mastigoneme-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No quoted snippets present; successful exit performs no quotation matching.
    Scientific paraphrases inspected separately.
  scope_note: 2026-10-11T03:57:26Z to 2026-10-11T03:58:04Z; log SHA-256 4a688dfe5311e8e53e6b6d3107d7e4367146d2bfdef0635b78df791ed6ec924a
- check_id: history
  name: history
  status: failed
  required: false
  target_ids:
  - GO:0097741
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
  - GO:0097741
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
  - GO:0097741
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
  - GO:0097741
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
  - GO:0097741
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
  - GO:0097741
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
  - GO:0097741
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
  - GO:0097741
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
  - GO:0097741
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
  reference: data/structures/appendage/mastigoneme.yaml
  locator: Entire native YAML and append-only histories
  accessed_at: '2026-10-11T04:06:06Z'
  snapshot_sha256: 34c249d8d02bcd5f887ef084d415e744691305e6f2dc9e096bba8c2a3e72d31e
  support: context_only
  summary: Native target assessed before edits; PROPOSED status and prior curation
    retained.
- evidence_id: prior-search
  kind: search
  reference: reviews/structured/ and reports/yaml_record_review/
  locator: mastigoneme and exact identifier
  accessed_at: '2026-10-11T04:06:06Z'
  support: context_only
  search_scope: rg --no-ignore --hidden in both review roots and the exact history
    directory included ignored files. GitHub all-state search for mastigoneme OR haptonema
    returned three earlier distinct, closed issues.
  summary: 'No earlier exact-target review finding found in these bounded roots. Prior
    issues #773 and #775 concern canonical-example citation and clade presence respectively,
    not these new findings.'
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0097741
  locator: Exact active GO term and definition
  accessed_at: '2026-10-11T03:59:37Z'
  snapshot_sha256: c451dc67bafe182c9a6d792bc1a2ddba13051be0573f457b7d5840ee1fd3857a
  support: supports
  summary: Native identity and literal definition match active GO:0097741. Its broad
    may-assist wording is not a demonstrated Chlamydomonas hydrodynamic effect.
- evidence_id: cilium
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0030990,GO:0032991,GO:0005929,GO:0005930,GO:0060271
  locator: GO:0005929 only
  accessed_at: '2026-10-11T03:58:11Z'
  snapshot_sha256: 9ce454502c5d2142bff87ef5e6a404ddd3ed1c217e42561118d11b0f50c9514a
  support: supports
  summary: Cilium identity supports the part_of context; mastigonemes are surface
    hairs, not the whole cilium.
- evidence_id: taxon
  kind: authority
  reference: https://rest.uniprot.org/taxonomy/3055.json
  locator: Exact taxonomy identity
  accessed_at: '2026-10-11T03:58:13Z'
  snapshot_sha256: 31e68163918c110c000e261d4edc5ae389b11e9992f43540ba3b89a9471ce850
  support: supports
  summary: Chlamydomonas reinhardtii matches the scoped distribution and example.
- evidence_id: dai
  kind: primary_source
  reference: DOI:10.1016/j.cell.2024.03.005
  locator: Introduction, structural Results and relevant Discussion
  accessed_at: '2026-10-11T03:59:14Z'
  snapshot_sha256: 318002363a183e30fd21030d7a9eee614044173ee614a578f00b62c62e3e7de2
  support: supports
  summary: Cryo-EM resolves an MST1 filament around a single MST3 and supports both
    structural constituents. A proposed PKD2/SIP anchoring model is not treated as
    directly measured stoichiometry. Introduction notes conflicting motility studies;
    mst3 mutants have a modest swimming phenotype in this experiment.
- evidence_id: liu
  kind: primary_source
  reference: DOI:10.1083/jcb.202001122
  locator: PKD2 organization and motility Results, Discussion and strain/motility
    Methods
  accessed_at: '2026-10-11T03:59:17Z'
  snapshot_sha256: 862f84b42b73f5a05c8b8904980229a1c49f22f8ef2c99586a1b112c5d9b4f9b
  support: supports
  summary: PKD2 loss and rescue establish ciliary mastigoneme organization. mst1 LMJ.RY0402.052413
    swam about 15% slower under the tested conditions; pkd2 phenotypes and nonadditivity
    do not establish a universal drag mechanism.
- evidence_id: amador
  kind: primary_source
  reference: DOI:10.1016/j.bpj.2020.05.003
  locator: Materials and Methods, Results and Discussion, Conclusions
  accessed_at: '2026-10-11T04:00:17Z'
  snapshot_sha256: 1355c58c828fd7e26de26ed2e36174bd1272d89f6bae4b13733ab6e78dd4fa2d
  support: supports
  summary: Different mstg line LMJ.RY0402.136134, compared with cw15 and cc125, lacked
    mastigonemes by TEM but showed no significant mean/normalized-maximum speed, waveform
    or propulsive-flow advantage from mastigonemes. Increased turning was observed;
    this does not mean all motility phenotypes were absent.
- evidence_id: chen
  kind: primary_source
  reference: PMID:943397
  locator: Primary abstract and bibliographic identity only
  accessed_at: '2026-10-11T03:59:17Z'
  snapshot_sha256: 066cf464fcfa83bab820c8db34f36ef34b2a9ad0a44df02b67f3540719692e2e
  support: supports
  summary: Ochromonas mastigoneme isolation and glycoprotein analysis match the background
    citation. No Chlamydomonas stoichiometry or broader distribution is inferred from
    it.
assessments:
- assessment_id: identity
  area: identity
  topic: GO identity, definition, appendage category and cilium parthood
  outcome: supported
  target_ids:
  - GO:0097741
  evidence_ids:
  - record
  - go
  - cilium
  - dai
  - liu
  summary: Exact GO structure retained; generic ontology definition is distinguished
    from species-specific experiments.
- assessment_id: composition
  area: grounding
  topic: Three components and assembly graph
  outcome: supported
  target_ids:
  - GO:0097741
  evidence_ids:
  - dai
  - liu
  - record
  summary: MST1/MST3 are constituents; PKD2 is associated machinery. All three assembly
    edges are supported at the stated granularity. Complete source-neutral protein-family
    grounding is openly deferred; no complete inventory or unmeasured PKD2/SIP stoichiometry
    is asserted.
- assessment_id: scope
  area: scope
  topic: Distribution and canonical example
  outcome: supported
  target_ids:
  - GO:0097741
  evidence_ids:
  - taxon
  - dai
  - liu
  summary: Species-scoped Chlamydomonas presence and PKD2-dependent organization example
    remain supported; no broader clade prevalence is guessed.
- assessment_id: motility
  area: evidence
  topic: Function claim and conflicting experimental results
  outcome: concern
  target_ids:
  - GO:0097741
  evidence_ids:
  - record
  - liu
  - amador
  - dai
  summary: Unqualified motility contribution omits conflicting primary swimming/flow
    results. Different mutant lines and assay contexts prevent treating these as identical
    experiments or deciding that one universally refutes the other.
  dimensions:
  - name: strain_scope
    value: Liu MST1 LMJ.RY0402.052413 versus Amador mstg LMJ.RY0402.136134
    definition: Distinct mutant lines; no pooled or universal genotype-phenotype conclusion.
    evidence_ids:
    - liu
    - amador
- assessment_id: provenance
  area: provenance
  topic: Citations, optional fields, histories and native status
  outcome: supported
  target_ids:
  - GO:0097741
  evidence_ids:
  - record
  - liu
  - amador
  - dai
  summary: Claim-local sources and bibliographic identities were checked at the access
    tiers stated. No trait links, image attributions, quantitative-property dataset,
    complex stoichiometry or protein examples are asserted. Past histories and PROPOSED
    status are preserved; absent optional fields are not defects.
findings:
- finding_id: F1
  issue_key: mastigoneme-motility-evidence-conflict
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Qualify motility contribution with conflicting primary results
  description: The sole function states that Chlamydomonas mastigonemes contribute
    to ciliary motility without context. Liu 2020 observed slower swimming in one
    mst1 line; Amador 2020 used another line and found no significant forward-speed,
    waveform or propulsive-flow benefit. Dai 2024, already cited by the record, acknowledges
    this conflict. The record should preserve these assay/strain-specific results
    rather than imply a settled general motility benefit.
  target_ids:
  - GO:0097741
  field_paths:
  - functions[0].label
  - functions[0].description
  - functions[0].evidence
  evidence_ids:
  - record
  - liu
  - amador
  - dai
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/mastigoneme.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material scope inflation in the represented biological function;
    identity and assembly remain valid.
actions:
- action_id: A1
  description: Qualify the function and nearest evidence with both studies, exact
    mutant context and unresolved interpretation; retain the assembly graph and ontology
    definition.
  finding_ids:
  - F1
  target_ids:
  - GO:0097741
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/mastigoneme.yaml
    role: maintained scientific record
  acceptance_checks:
  - Retain the stable function ID while making the label and description explicitly
    context-dependent.
  - Keep the Liu slower-swimming result and add Amador no-enhancement evidence with
    distinct mutant lines.
  - Do not generalize Amador into no motility phenotype at all or promote proposed
    sensory/drag mechanisms to established facts.
  - Preserve prior discussions and add an evidence-linked OPEN interpretation of the
    conflict.
  - Guarded curation, append-only histories, affected generated artifacts and focused
    regression tests pass native gates.
limitations:
- Both 2020 papers were inspected at full main-text Methods/Results level; Dai structural
  sections and its conflicting-motility discussion were read, not every supplemental
  dataset.
- Chen 1976 was inspected at primary-abstract level and is only background provenance
  here. No reanalysis of swimming data or experimental resolution of the conflict
  was performed.
- Same-agent assessment, not independent human sign-off or completion of the 909-record
  goal.
- Initial history PATH failure was superseded by a successful virtual-environment
  rerun. Exact-baseline CI supplies full QC; skipped resolver namespaces and unreachable
  BFO controls are not certified.
- No applicable iModulonDB dataset; this is not evidence of biological absence. No
  quotations were present to verify, so paraphrases required separate source inspection.
```
