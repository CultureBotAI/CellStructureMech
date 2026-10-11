# Type i pilus: evidence and provenance review

- Review: 20261011T063133Z-type_i_pilus-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T06:24:07Z
- Finished UTC: 2026-10-11T06:31:33Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Concrete issues observed; save immutable findings before separately authorized curation.

## Scope And Provenance

Entire native YAML: identity, composition, taxonomy, functions, every graph edge, present resources and provenance.

Selection: One resolved sequential target in the all-record goal, not a sampled corpus verdict.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 617a24ae7989e21e482bb32d3d527b05d5b475b6.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0140621 | data/structures/appendage/type_i_pilus.yaml | maintained | type I pilus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0140621 | Deterministic command passed; scientific support assessed separately. |
| strict | passed | True | GO:0140621 | Deterministic command passed; scientific support assessed separately. |
| snippets | passed | True | GO:0140621 | No quoted snippets; success is not a test of paraphrase accuracy. |
| history | passed | True | GO:0140621 | Deterministic command passed; scientific support assessed separately. |
| labels | passed | True | GO:0140621 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0140621 | Deterministic command passed; scientific support assessed separately. |
| curies | passed | True | GO:0140621 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4011<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0140621 | Deterministic command passed; scientific support assessed separately. |
| diff | passed | True | GO:0140621 | Deterministic command passed; scientific support assessed separately. |
| contract | passed | True | GO:0140621 | Deterministic command passed; scientific support assessed separately. |
| Exact-baseline authoritative CI QC | passed | True | GO:0140621 | Full QC passed on this exact unchanged baseline, including generated products; not a newly run local full QC. |

## Scientific And Domain Assessments

### Definition and bacterial scope

identity: concern. Targets: GO:0140621.

Exact GO identity and mannose-sensitive adhesion are sound. The unqualified FimG-containing architecture in the opening definition conflates E. coli with all type I pili despite explicit Salmonella coverage.

### Five constituent rows and all eight assembly edges

grounding: supported. Targets: GO:0140621.

Supported for the E. coli model, including FimH-FimG-FimF-FimA order and FimI at the basal end. Existing exact-family TODO covers all rows; no guessed family accession or universal stoichiometry is needed.

### Assembly and adhesion source placement

evidence: concern. Targets: GO:0140621.

Mannose adhesion is supported. The local assembly-function citation is from 2018 when FimI termination remained a hypothesis, although the confirming 2025 source is correctly used elsewhere.

### History, discussions and optional slots

provenance: supported. Targets: GO:0140621.

Prior fixes, both history surfaces and PROPOSED status are intact. No empty optional field is a finding. No exact-target canonical predecessor was found by ignored-inclusive review-root search; adjacent Y-link grounding reviews concern the whole transition-zone record.

## Findings

### F1: Separate type I pilus identity from the E. coli subunit model

major / open / confirmed; issue key: type-i-pilus-ecoli-architecture-scope.

The opening definition requires a FimG/FimF tip for the entire GO type I pilus class, but the record also covers Salmonella. The cited 2018 review explicitly lists a different Salmonella gene inventory without FimG and cautions that its FimI is not the E. coli counterpart. GO itself scopes its FimH/FimG/FimF architecture to E. coli.

### F2: Attach the confirmed FimI termination source to the assembly function

minor / open / confirmed; issue key: type-i-pilus-termination-function-citation.

The assembly function includes a basal terminator but cites only the 2018 review, which explicitly says the FimI rod-terminator role remains unconfirmed. The inspected 2025 paper supports it and is cited elsewhere, so this is a local source-placement gap, not a false termination claim.

## Recommended Actions And Acceptance Checks

### A1

Separate type I pilus identity from the E. coli subunit model

- Define the broader mannose-sensitive CU pilus class, then explicitly introduce the E. coli Fim model.
- Scope constituent roles and the assembly graph to E. coli without deleting Salmonella from the supported broader distribution.
- Keep the correctly separated FimG and FimF rows and all exact-family discussion attachments.
- Use guarded curation, append Codex curation and EDIT history, retain PROPOSED and all earlier histories/reviews/discussion rationale, regenerate affected products, and pass focused tests plus native QC.

### A2

Attach the confirmed FimI termination source to the assembly function

- Attach the inspected 2025 structural evidence to the E. coli assembly function.
- Keep the older source for the claims it actually supports; do not represent its hypothesis as contemporaneous confirmation.
- Use guarded curation, append Codex curation and EDIT history, retain PROPOSED and all earlier histories/reviews/discussion rationale, regenerate affected products, and pass focused tests plus native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/type_i_pilus.yaml | context_only | Full native YAML read before findings; original status and histories captured. |
| rules | docs/CURATION.md | context_only | Requires exact claim-level scope, constituent/machinery distinction and append-only discussion rationale. |
| go-0140621 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140621; Exact current QuickGO term | supports | Active exact term agrees with native identity, relation or process use. |
| go-0140623 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140623; Exact current QuickGO term | supports | Active exact term agrees with native identity, relation or process use. |
| go-0009289 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289; Exact current QuickGO term | supports | Active exact term agrees with native identity, relation or process use. |
| taxon-2 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2&amp;retmode=xml; Exact NCBI Taxonomy identity and names | supports | Taxon and current scientific name resolve; taxonomy is not evidence of prevalence. |
| taxon-562 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=562&amp;retmode=xml; Exact NCBI Taxonomy identity and names | supports | Taxon and current scientific name resolve; taxonomy is not evidence of prevalence. |
| adapter-inventory | /private/tmp/csm-review-20261011T062301Z/adapter.log | context_only | Live 28-dataset iModulonDB inventory; no matching Caulobacter coverage. E. coli and P. aeruginosa searches were inspected. |
| cu2018 | DOI:10.1128/ecosalplus.ESP-0007-2017; Architecture, type 1 E. coli and Salmonella sections and assembly mechanism | supports | The E. coli FimH-FimG-FimF order differs from Salmonella, which has FimF but not FimG in the listed operon. FimI termination is still unconfirmed in this review. |
| bachmann | DOI:10.1038/s41467-025-60325-z; Introduction, FimA incorporation, tip-to-rod transition, FimI termination and Discussion; Figures 2-3 visually inspected | supports | E. coli FimH/FimG/FimF order, long FimA rod and single FimI terminator are supported; chaperone/usher machinery remains outside this filament record. |
| jones | DOI:10.1073/pnas.92.6.2081; Primary abstract | supports | Purified FimG-FimH fibrillae and mutant/complemented pili support tip architecture and mannose binding. |
| hospenthal | DOI:10.1038/nrmicro.2017.40; Author manuscript pages 3-14; assembly-platform/filament distinction | supports | CU chaperone and usher drive ordered assembly; the filament is distinct from its assembly platform. |
| fim-module | /private/tmp/csm-review-20261011T062301Z/adapter-fim-summary.log | context_only | e_coli/modulome/39 contains seven fim genes. Computational coexpression is not localization, stoichiometry or assembly evidence. |

## Limits And Additional Notes

- Same-agent review, not human sign-off or completion of the 909-record goal.
- Identifier resolver skips and label pairs without adapters are not certified. Exact target GO/taxon authorities were separately inspected for the scientific reviews.
- Full QC uses the verified exact-baseline CI run. No raw experimental data or movies were reanalysed.
- Jones 1995 was assessed at primary-abstract level. The 2018 review and 2017 author manuscript were reread from prior authenticated private snapshots, retaining original access times; current 2018 PMC access returned a challenge. No raw cryo-EM reanalysis.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T063133Z-type_i_pilus-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Type i pilus: evidence and provenance review'
started_at: '2026-10-11T06:24:07Z'
finished_at: '2026-10-11T06:31:33Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent review before mutation; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Concrete issues observed; save immutable findings before separately authorized
  curation.
source:
  git_revision: 617a24ae7989e21e482bb32d3d527b05d5b475b6
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
    sha256: 64862db2087298ae832b8a8410185349cc277151af31d88ce231e43201ab9440
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/appendage/p_pilus.yaml
    sha256: c9e8371a5cc6cda0a28d5264a6a2c2368a703670b3c285fc12f1aa58b6adafa9
    role: context
  - path: data/structures/appendage/pilus.yaml
    sha256: b82205e792d181aa2e2cb76eb56a2ecafdb3021302c7b86a5819c649528bc06b
    role: context
  - path: data/structures/appendage/suctorian_feeding_tentacle.yaml
    sha256: 6165bcfed6515881367eba4fe55aafd95e31be8c42f55d78179ceecb93f27400
    role: context
  - path: data/structures/appendage/tad_pilus.yaml
    sha256: ba94edab94e997876d50e0302b5b6b5055743f6c742da986b4b73b60dbcc89c1
    role: context
  - path: data/structures/appendage/type_i_pilus.yaml
    sha256: 35b161df2bab54d5b56efde936dc2ee7e5de57789ae583a26a8265b04dc17f00
    role: target
  - path: data/structures/appendage/type_iv_pilus.yaml
    sha256: 744f19aeb3b62c9f4d470fcbf47038056069904d998eb7c5e2b83f6821037d4e
    role: context
  - path: data/structures/appendage/y_shaped_link.yaml
    sha256: 89637052ba32ba24d695d33a540116783a09124de805feeaa9430f1f5c702841
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
  - path: history/records/type_i_pilus/2026-09-11T014721Z-codex-c18ff2.yaml
    sha256: a65f6a5acf556d397906d39b5360c97a94b69be59b2e96e9c244fdc6a80b32ff
    role: context
  - path: history/records/type_i_pilus/2026-09-11T015420Z-codex-d9fc51.yaml
    sha256: 649717a99709e25c52357666cf63db1d5196fab5523bee5619826a838f312b15
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/evidence_readability.type_i_pilus.tsv
    sha256: 1687fb0f76e818a9221287ed25a873de0d2e2dc743161f80f7e2dae2759d84dc
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
targets:
- target_id: GO:0140621
  path: data/structures/appendage/type_i_pilus.yaml
  label: type I pilus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/type_i_pilus.yaml
    role: maintained scientific record
scope:
  description: 'Entire native YAML: identity, composition, taxonomy, functions, every
    graph edge, present resources and provenance.'
  selection: One resolved sequential target in the all-record goal, not a sampled
    corpus verdict.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0140621
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/type_i_pilus.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; scientific support assessed separately.
  scope_note: 2026-10-11T06:25:26Z to 2026-10-11T06:25:29Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/type_i_pilus.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; scientific support assessed separately.
  scope_note: 2026-10-11T06:25:29Z to 2026-10-11T06:25:33Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/type_i_pilus.yaml
    --report /private/tmp/csm-review-20261011T062301Z/type_i_pilus-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No quoted snippets; success is not a test of paraphrase accuracy.
  scope_note: 2026-10-11T06:25:33Z to 2026-10-11T06:25:54Z; log SHA-256 ce3f8b903c129e79d003c3769d89f364c4afeb3dcf52c486d926dbc4ede9f157
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; scientific support assessed separately.
  scope_note: 2026-10-11T06:26:53Z to 2026-10-11T06:27:08Z; log SHA-256 ec4802743686962e3e9ec0534e2a9fb4ca76e92b15ecc0cb7f607d8ce80a96a8
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T06:27:08Z to 2026-10-11T06:28:20Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; scientific support assessed separately.
  scope_note: 2026-10-11T06:28:20Z to 2026-10-11T06:28:37Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4011\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T06:28:37Z to 2026-10-11T06:29:27Z; log SHA-256 dc5ed8534cf356581f142af6232079d99cab71fde9815408309aac234b468667
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; scientific support assessed separately.
  scope_note: 2026-10-11T06:29:27Z to 2026-10-11T06:30:11Z; log SHA-256 5614362bbb86fa7e780a9ccce9e9eaced4fbf482469bd124dcd222da72633c46
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; scientific support assessed separately.
  scope_note: 2026-10-11T06:30:11Z to 2026-10-11T06:30:11Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; scientific support assessed separately.
  scope_note: 2026-10-11T06:24:22Z to 2026-10-11T06:25:22Z; log SHA-256 1bfa2c402d877089e25c6111113d3b329d85327841ca8ad98ce94631c2845de1
- check_id: qc
  name: Exact-baseline authoritative CI QC
  status: passed
  required: true
  target_ids:
  - GO:0140621
  command: gh run view 38117523970 --json status,conclusion,headSha,event,name,url,jobs;
    gh run view 38117523970 --log
  exit_code: 0
  summary: Full QC passed on this exact unchanged baseline, including generated products;
    not a newly run local full QC.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38117523970;
    full-log SHA-256 483d49589927059d90b64d291148e5e3c0461580ef9fffdf21fb2add7f56f4b3
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/type_i_pilus.yaml
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 35b161df2bab54d5b56efde936dc2ee7e5de57789ae583a26a8265b04dc17f00
  support: context_only
  summary: Full native YAML read before findings; original status and histories captured.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
  support: context_only
  summary: Requires exact claim-level scope, constituent/machinery distinction and
    append-only discussion rationale.
- evidence_id: go-0140621
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140621
  locator: Exact current QuickGO term
  accessed_at: '2026-10-11T06:27:24Z'
  snapshot_sha256: ca839e7e9bdf396cb9162f5036a959c36050545ad3bb1afb4011520df9a7dabb
  support: supports
  summary: Active exact term agrees with native identity, relation or process use.
- evidence_id: go-0140623
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140623
  locator: Exact current QuickGO term
  accessed_at: '2026-10-11T06:27:25Z'
  snapshot_sha256: 68a8c6ed61a488d6699914cae15550cba899b430a4e5acfccdbdd3bda1ea1242
  support: supports
  summary: Active exact term agrees with native identity, relation or process use.
- evidence_id: go-0009289
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289
  locator: Exact current QuickGO term
  accessed_at: '2026-10-11T06:27:16Z'
  snapshot_sha256: bc564119fe5e6d56127346948989278deecab0f5ad24cb75366edb2d3d6d63cb
  support: supports
  summary: Active exact term agrees with native identity, relation or process use.
- evidence_id: taxon-2
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=2&retmode=xml
  locator: Exact NCBI Taxonomy identity and names
  accessed_at: '2026-10-11T06:27:28Z'
  snapshot_sha256: d62facd350ac66acdd551e03af2eef6a55a96cd0d4c90e8d7e7205870896efa7
  support: supports
  summary: Taxon and current scientific name resolve; taxonomy is not evidence of
    prevalence.
- evidence_id: taxon-562
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=562&retmode=xml
  locator: Exact NCBI Taxonomy identity and names
  accessed_at: '2026-10-11T06:27:29Z'
  snapshot_sha256: 1d5618066f7d7b5fbf62b33b00b8928382362d9b9e017076caeb654151d980f8
  support: supports
  summary: Taxon and current scientific name resolve; taxonomy is not evidence of
    prevalence.
- evidence_id: adapter-inventory
  kind: validation
  reference: /private/tmp/csm-review-20261011T062301Z/adapter.log
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live 28-dataset iModulonDB inventory; no matching Caulobacter coverage.
    E. coli and P. aeruginosa searches were inspected.
- evidence_id: cu2018
  kind: primary_source
  reference: DOI:10.1128/ecosalplus.ESP-0007-2017
  locator: Architecture, type 1 E. coli and Salmonella sections and assembly mechanism
  accessed_at: '2026-10-11T04:49:47Z'
  snapshot_sha256: 52f625f1c984760f352c8e215786748c64dcbdf2523ff532164c810e958aabac
  support: supports
  summary: The E. coli FimH-FimG-FimF order differs from Salmonella, which has FimF
    but not FimG in the listed operon. FimI termination is still unconfirmed in this
    review.
- evidence_id: bachmann
  kind: primary_source
  reference: DOI:10.1038/s41467-025-60325-z
  locator: Introduction, FimA incorporation, tip-to-rod transition, FimI termination
    and Discussion; Figures 2-3 visually inspected
  accessed_at: '2026-10-11T06:24:48Z'
  snapshot_sha256: 7326486f3d7796d8498002c80e035c58504625da89b54054c5fd058ca009622d
  support: supports
  summary: E. coli FimH/FimG/FimF order, long FimA rod and single FimI terminator
    are supported; chaperone/usher machinery remains outside this filament record.
- evidence_id: jones
  kind: primary_source
  reference: DOI:10.1073/pnas.92.6.2081
  locator: Primary abstract
  accessed_at: '2026-10-11T06:24:52Z'
  snapshot_sha256: 61d225b9bd7d634614c8212176b22d322e129ebd2f9c2733132f9f8c0ca2559a
  support: supports
  summary: Purified FimG-FimH fibrillae and mutant/complemented pili support tip architecture
    and mannose binding.
- evidence_id: hospenthal
  kind: primary_source
  reference: DOI:10.1038/nrmicro.2017.40
  locator: Author manuscript pages 3-14; assembly-platform/filament distinction
  accessed_at: '2026-10-11T05:17:41Z'
  snapshot_sha256: 5c2dbbd1f8f92499fdda542390ccd97ce5e82ee7c2f785c61d7a118ee82a2a7d
  support: supports
  summary: CU chaperone and usher drive ordered assembly; the filament is distinct
    from its assembly platform.
- evidence_id: fim-module
  kind: validation
  reference: /private/tmp/csm-review-20261011T062301Z/adapter-fim-summary.log
  accessed_at: '2026-10-11T06:31:33Z'
  snapshot_sha256: 9918a3ccd92558dc215baaf1f9a4b87de08b623cfdd5bc70a1bc7e7f037c3111
  support: context_only
  summary: e_coli/modulome/39 contains seven fim genes. Computational coexpression
    is not localization, stoichiometry or assembly evidence.
assessments:
- assessment_id: identity
  area: identity
  topic: Definition and bacterial scope
  outcome: concern
  target_ids:
  - GO:0140621
  evidence_ids:
  - record
  - cu2018
  - go-0140621
  summary: Exact GO identity and mannose-sensitive adhesion are sound. The unqualified
    FimG-containing architecture in the opening definition conflates E. coli with
    all type I pili despite explicit Salmonella coverage.
- assessment_id: composition
  area: grounding
  topic: Five constituent rows and all eight assembly edges
  outcome: supported
  target_ids:
  - GO:0140621
  evidence_ids:
  - bachmann
  - jones
  - hospenthal
  summary: Supported for the E. coli model, including FimH-FimG-FimF-FimA order and
    FimI at the basal end. Existing exact-family TODO covers all rows; no guessed
    family accession or universal stoichiometry is needed.
- assessment_id: functions
  area: evidence
  topic: Assembly and adhesion source placement
  outcome: concern
  target_ids:
  - GO:0140621
  evidence_ids:
  - cu2018
  - bachmann
  - jones
  summary: Mannose adhesion is supported. The local assembly-function citation is
    from 2018 when FimI termination remained a hypothesis, although the confirming
    2025 source is correctly used elsewhere.
- assessment_id: provenance
  area: provenance
  topic: History, discussions and optional slots
  outcome: supported
  target_ids:
  - GO:0140621
  evidence_ids:
  - record
  - rules
  summary: Prior fixes, both history surfaces and PROPOSED status are intact. No empty
    optional field is a finding. No exact-target canonical predecessor was found by
    ignored-inclusive review-root search; adjacent Y-link grounding reviews concern
    the whole transition-zone record.
findings:
- finding_id: F1
  issue_key: type-i-pilus-ecoli-architecture-scope
  category: scope
  severity: major
  status: open
  certainty: confirmed
  title: Separate type I pilus identity from the E. coli subunit model
  description: The opening definition requires a FimG/FimF tip for the entire GO type
    I pilus class, but the record also covers Salmonella. The cited 2018 review explicitly
    lists a different Salmonella gene inventory without FimG and cautions that its
    FimI is not the E. coli counterpart. GO itself scopes its FimH/FimG/FimF architecture
    to E. coli.
  target_ids:
  - GO:0140621
  field_paths:
  - definition
  - components
  - causal_graphs[0]
  evidence_ids:
  - record
  - cu2018
  - bachmann
  - go-0140621
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/type_i_pilus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material model-to-class scope or composition-boundary defect.
- finding_id: F2
  issue_key: type-i-pilus-termination-function-citation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach the confirmed FimI termination source to the assembly function
  description: The assembly function includes a basal terminator but cites only the
    2018 review, which explicitly says the FimI rod-terminator role remains unconfirmed.
    The inspected 2025 paper supports it and is cited elsewhere, so this is a local
    source-placement gap, not a false termination claim.
  target_ids:
  - GO:0140621
  field_paths:
  - functions[0].evidence
  evidence_ids:
  - record
  - cu2018
  - bachmann
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/type_i_pilus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded citation or append-only provenance defect; biological
    identity remains valid.
actions:
- action_id: A1
  description: Separate type I pilus identity from the E. coli subunit model
  finding_ids:
  - F1
  target_ids:
  - GO:0140621
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/type_i_pilus.yaml
    role: maintained scientific record
  acceptance_checks:
  - Define the broader mannose-sensitive CU pilus class, then explicitly introduce
    the E. coli Fim model.
  - Scope constituent roles and the assembly graph to E. coli without deleting Salmonella
    from the supported broader distribution.
  - Keep the correctly separated FimG and FimF rows and all exact-family discussion
    attachments.
  - Use guarded curation, append Codex curation and EDIT history, retain PROPOSED
    and all earlier histories/reviews/discussion rationale, regenerate affected products,
    and pass focused tests plus native QC.
- action_id: A2
  description: Attach the confirmed FimI termination source to the assembly function
  finding_ids:
  - F2
  target_ids:
  - GO:0140621
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/type_i_pilus.yaml
    role: maintained scientific record
  acceptance_checks:
  - Attach the inspected 2025 structural evidence to the E. coli assembly function.
  - Keep the older source for the claims it actually supports; do not represent its
    hypothesis as contemporaneous confirmation.
  - Use guarded curation, append Codex curation and EDIT history, retain PROPOSED
    and all earlier histories/reviews/discussion rationale, regenerate affected products,
    and pass focused tests plus native QC.
limitations:
- Same-agent review, not human sign-off or completion of the 909-record goal.
- Identifier resolver skips and label pairs without adapters are not certified. Exact
  target GO/taxon authorities were separately inspected for the scientific reviews.
- Full QC uses the verified exact-baseline CI run. No raw experimental data or movies
  were reanalysed.
- Jones 1995 was assessed at primary-abstract level. The 2018 review and 2017 author
  manuscript were reread from prior authenticated private snapshots, retaining original
  access times; current 2018 PMC access returned a challenge. No raw cryo-EM reanalysis.
```
