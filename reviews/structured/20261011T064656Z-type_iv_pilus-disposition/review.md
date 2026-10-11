# Type iv pilus: finding dispositions

- Review: 20261011T064656Z-type_iv_pilus-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T06:37:00Z
- Finished UTC: 2026-10-11T06:46:56Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Exact predecessor findings resolved; source tiers and biological uncertainties remain explicit. No scientific status promotion.

## Scope And Provenance

Exact predecessor findings and changed fields, including append-only provenance; not a repeated whole-record scientific review.

Selection: 20261011T063139Z-type_iv_pilus-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 7214d5ae8dc9664472ed965a9bc8c0534a0c0bfd.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0044096 | data/structures/appendage/type_iv_pilus.yaml | maintained | type IV pilus |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0044096 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| strict | passed | True | GO:0044096 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| snippets | passed | True | GO:0044096 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| history | passed | True | GO:0044096 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| labels | passed | True | GO:0044096 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0044096 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| curies | passed | True | GO:0044096 | resolver control: every resolver accepts a known id and rejects a fabricated one<br>resolving 1 DOI identifier(s)...<br><br>identifier liveness summary:<br>  OK             4012<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| regressions | passed | True | GO:0044096 | .................................                                        [100%]<br>33 passed in 37.32s |
| reviews | passed | True | GO:0044096 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| diff | passed | True | GO:0044096 | Actual post-curation command passed. Empty quotation checks and resolver skips are not scientific proof. |
| release-qc | passed | True | GO:0044096 | Authoritative full local QC passed, including tests, all-record schema, histories and generated-product checks. PR and native merge-group checks are separate publication gates. |

## Scientific And Domain Assessments

### Keep cytoplasmic motors out of the pilus filament composition

scope: supported. Targets: GO:0044096.

PilB and PilT are no longer filament constituent rows or component references. Their evidenced motor nodes and all five edges remain in an explicitly type-IVa-scoped graph. A RESOLVED discussion records the boundary; major pilin and exact CryoET dataset provenance are unchanged.

## Findings

### F1: Keep cytoplasmic motors out of the pilus filament composition

major / resolved / confirmed; issue key: type-iv-pilus-filament-motor-boundary.

PilB and PilT are no longer filament constituent rows or component references. Their evidenced motor nodes and all five edges remain in an explicitly type-IVa-scoped graph. A RESOLVED discussion records the boundary; major pilin and exact CryoET dataset provenance are unchanged.

Disposition: PilB and PilT are no longer filament constituent rows or component references. Their evidenced motor nodes and all five edges remain in an explicitly type-IVa-scoped graph. A RESOLVED discussion records the boundary; major pilin and exact CryoET dataset provenance are unchanged. Verified against inspected evidence, focused regressions and full QC.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/appendage/type_iv_pilus.yaml | context_only | Corrected native bytes reread against exact predecessor findings and the stated source tiers. |
| rules | docs/CURATION.md | context_only | Requires exact claim-level scope, constituent/machinery distinction and append-only discussion rationale. |
| go-0044096 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044096; Exact current QuickGO term | supports | Active exact term agrees with native identity, relation or process use. |
| go-0043107 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043107; Exact current QuickGO term | supports | Active exact term agrees with native identity, relation or process use. |
| go-0009289 | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0009289; Exact current QuickGO term | supports | Active exact term agrees with native identity, relation or process use. |
| taxon-2 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=2&amp;retmode=xml; Exact NCBI Taxonomy identity and names | supports | Taxon and current scientific name resolve; taxonomy is not evidence of prevalence. |
| taxon-287 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=287&amp;retmode=xml; Exact NCBI Taxonomy identity and names | supports | Taxon and current scientific name resolve; taxonomy is not evidence of prevalence. |
| taxon-264462 | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=264462&amp;retmode=xml; Exact NCBI Taxonomy identity and names | supports | Taxon and current scientific name resolve; taxonomy is not evidence of prevalence. |
| adapter-inventory | /private/tmp/csm-review-20261011T062301Z/adapter.log | context_only | Live 28-dataset iModulonDB inventory; no matching Caulobacter coverage. E. coli and P. aeruginosa searches were inspected. |
| hospenthal | DOI:10.1038/nrmicro.2017.40; Author manuscript pages 9-14: T4P biogenesis, machinery, filament and function | supports | Major/minor pilins form the filament. Cytoplasmic PilB/PilT belong to the motor subcomplex with PilC; the detailed motor account uses type IVa models. |
| skerker | DOI:10.1073/pnas.121171698; Abstract, Methods, Results and Discussion | supports | Direct Pseudomonas imaging supports extension, distal attachment, force and retraction-driven cell movement. |
| merz | DOI:10.1038/35024105; Primary abstract | supports | Neisseria optical-tweezer experiments establish PilT-dependent retraction and motility, not PilT filament membership. |
| bdellovibrio | DOI:10.1038/s41564-023-01401-2; Attack-phase results, Figure 1 caption, attachment results and Methods | supports | HD100 cryo-ET observes pili and distinguishes them from empty basal machines; uncertain non-piliated structures are not used as pilus identity proof. |
| cryo-dataset | /private/tmp/csm-review-20261011T062301Z/cryo-dataset.json | context_only | Exact official GraphQL metadata: dataset 10155, run 7978, annotation 30707 with eight GO:0044096 objects, manual IMOD labeling and both quality flags true. |
| cryo-run | /private/tmp/csm-review-20261011T062301Z/cryo-run.json | context_only | Exact official GraphQL metadata: dataset 10155, run 7978, annotation 30707 with eight GO:0044096 objects, manual IMOD labeling and both quality flags true. |
| cryo-annotation | /private/tmp/csm-review-20261011T062301Z/cryo-annotation.json | context_only | Exact official GraphQL metadata: dataset 10155, run 7978, annotation 30707 with eight GO:0044096 objects, manual IMOD labeling and both quality flags true. |
| pilB-adapter | /private/tmp/csm-review-20261011T062301Z/adapter-pilB.log | context_only | p_aeruginosa/precise364/PA4526 gene hit, no module hit; not composition proof. |
| pilT-adapter | /private/tmp/csm-review-20261011T062301Z/adapter-pilT.log | context_only | p_aeruginosa/precise364/PA0395 gene hit, no module hit; not composition proof. |
| predecessor | reviews/structured/20261011T063139Z-type_iv_pilus-audit/review.yaml | context_only | Immutable original observations committed before mutation. |
| preservation | /private/tmp/csm-review-20261011T062301Z/preservation.json | supports | Only four native records changed; 905 others and all prior histories, canonical reviews and legacy reports are byte-preserved. |
| embeddings | /private/tmp/csm-review-20261011T062301Z/embedding-refresh.json | supports | Only three pilus semantic vectors changed; the provenance-only stalk correction is outside the semantic projection. The other 906 vectors are preserved. |

## Limits And Additional Notes

- Same-agent review, not human sign-off or completion of the 909-record goal.
- Identifier resolver skips and label pairs without adapters are not certified. Exact target GO/taxon authorities were separately inspected for the scientific reviews.
- Merz 2000 was assessed at primary-abstract level. Hospenthal was reread from the authenticated author manuscript. CryoET assessment is metadata-only; raw volumes and annotation geometry were not inspected.
- Original source-access tiers and snapshot times are retained; no raw experimental reanalysis or independent approval is implied.
- Five focused tests failed against original inputs; the corrected focused/guarded-writer suite passes. A preliminary lint check required an explicit strict zip argument, corrected before QC.
- The scratch embedding refresh initially expected four semantic changes and refused before writing. Inspection of the maintained semantic projection showed the stalk rationale/history are excluded; only the three real semantic changes were refreshed.
- Disposition inputs are retained by review-base/pilus-scope-20261011. Final PR and merge-group results are verified separately.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T064656Z-type_iv_pilus-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Type iv pilus: finding dispositions'
started_at: '2026-10-11T06:37:00Z'
finished_at: '2026-10-11T06:46:56Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source-backed reassessment and separate adversarial
    diff inspection; not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Exact predecessor findings resolved; source tiers and biological uncertainties
  remain explicit. No scientific status promotion.
source:
  git_revision: 7214d5ae8dc9664472ed965a9bc8c0534a0c0bfd
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
    sha256: 34bb82ab5fe3599c02d673a2b8b80fe7ec12fa4228d504e1ad7cd028a61bca93
    role: context
  - path: data/structures/appendage/type_i_pilus.yaml
    sha256: 4c628643f9f8e5360cd1a8f1129ec9f5101978f37555e8e5005cd2ff18781cca
    role: context
  - path: data/structures/appendage/type_iv_pilus.yaml
    sha256: 21347bc455f18fe18d71eeb73a2f0a48d8a3ced0d8ff27e04ec6e844c2f52ca4
    role: target
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
  - path: history/records/type_iv_pilus/2026-08-30T193104Z-codex-e15285.yaml
    sha256: 3e70fe83ee675a8f5cb666489a783bd65d0c92634dc955288883b511a1abbaed
    role: context
  - path: history/records/type_iv_pilus/2026-08-30T203001Z-codex-9e92ab.yaml
    sha256: d993750541e3a1da1836d8f2b6e5b0cc19772e69fc86f8ee926d5eab3ba562d8
    role: context
  - path: history/records/type_iv_pilus/2026-09-04T005809Z-codex-a42bf8.yaml
    sha256: 2ea548e1e5f99a82a11cdfd312b92db6d70182f329bd51d59905d999c2565777
    role: context
  - path: history/records/type_iv_pilus/2026-10-11T063325Z-codex-7896f8.yaml
    sha256: 21a24185403af64bc2bdba3ab88d3902c792d61aacaf85210fb4572d20b1bc34
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: reports/evidence_readability.type_iv_pilus.tsv
    sha256: a076ddf9f62b8ddfe7c74fbb2d769dd2f32e46889110386214ca5dc26f293884
    role: context
  - path: reviews/structured/20261011T063139Z-type_iv_pilus-audit/review.yaml
    sha256: bebafec12e97edf62b9b8d774281fe2012a84241b40b6ad4adc7595a62e9635a
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: tests/test_pilus_scope_review.py
    sha256: 9c92e7a829bbbb6525bf63c3459e9957383cbe969e1a112f89a60ec5b30fa4d3
    role: context
targets:
- target_id: GO:0044096
  path: data/structures/appendage/type_iv_pilus.yaml
  label: type IV pilus
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/type_iv_pilus.yaml
    role: maintained scientific record
scope:
  description: Exact predecessor findings and changed fields, including append-only
    provenance; not a repeated whole-record scientific review.
  selection: 20261011T063139Z-type_iv_pilus-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0044096
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/appendage/type_iv_pilus.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T06:34:39Z to 2026-10-11T06:34:41Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python scripts/validate_strict.py data/structures/appendage/type_iv_pilus.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T06:34:41Z to 2026-10-11T06:34:44Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/appendage/type_iv_pilus.yaml
    --report /private/tmp/csm-review-20261011T062301Z/type_iv_pilus-post-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T06:34:44Z to 2026-10-11T06:35:01Z; log SHA-256 ea0b7017567ede828820d78f7473524f8b65c0c47b98b2794783eb5c77cff18f
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T06:35:26Z to 2026-10-11T06:35:47Z; log SHA-256 e836c3a60d88b76a8f3886dd6bf8d339fcbd2229409e99019ae17006c6c6f673
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T06:35:47Z to 2026-10-11T06:37:28Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T06:37:28Z to 2026-10-11T06:37:45Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\nresolving 1 DOI identifier(s)...\n\nidentifier liveness summary:\n  OK\
    \             4012\n  SKIPPED         251\n\nEvery identifier resolves at its\
    \ issuing authority."
  scope_note: 2026-10-11T06:37:45Z to 2026-10-11T06:38:37Z; log SHA-256 689f734e0d1a1d4dcd14294887e0791542956f43f22b8ac6ad2578c8e214e200
- check_id: regressions
  name: regressions
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python -m pytest -q tests/test_pilus_scope_review.py tests/test_stalk_evidence_review.py
    tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: '.................................                                        [100%]

    33 passed in 37.32s'
  scope_note: 2026-10-11T06:38:37Z to 2026-10-11T06:39:15Z; log SHA-256 d80be767bcfe8b26473cf122a106daa0d66b1522063250ed94a9e59a10a22c77
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python scripts/record_review.py check --base 617a24ae7989e21e482bb32d3d527b05d5b475b6
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T06:39:15Z to 2026-10-11T06:39:57Z; log SHA-256 6f78a061ae40b61bbe5427b44d8a84cfda7f9cb6dfca451b6a3a5cc0158fd313
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual post-curation command passed. Empty quotation checks and resolver
    skips are not scientific proof.
  scope_note: 2026-10-11T06:39:57Z to 2026-10-11T06:39:57Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - GO:0044096
  command: .venv/bin/python scripts/run_qc.py
  exit_code: 0
  expected_exit_code: 0
  summary: Authoritative full local QC passed, including tests, all-record schema,
    histories and generated-product checks. PR and native merge-group checks are separate
    publication gates.
  scope_note: 2026-10-11T06:36:52Z to 2026-10-11T06:46:42Z; log SHA-256 60e18bf851ba93585d294e573bda35d7743a0a5da277bed4d7aedc7d1ed6c861
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/appendage/type_iv_pilus.yaml
  accessed_at: '2026-10-11T06:46:56Z'
  snapshot_sha256: 21347bc455f18fe18d71eeb73a2f0a48d8a3ced0d8ff27e04ec6e844c2f52ca4
  support: context_only
  summary: Corrected native bytes reread against exact predecessor findings and the
    stated source tiers.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T06:31:39Z'
  snapshot_sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
  support: context_only
  summary: Requires exact claim-level scope, constituent/machinery distinction and
    append-only discussion rationale.
- evidence_id: go-0044096
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0044096
  locator: Exact current QuickGO term
  accessed_at: '2026-10-11T06:27:20Z'
  snapshot_sha256: 2d0550e159fe884cb3dbf4bfed109d00edab2a4ac93b6a5e5f1c13670fc37e3d
  support: supports
  summary: Active exact term agrees with native identity, relation or process use.
- evidence_id: go-0043107
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0043107
  locator: Exact current QuickGO term
  accessed_at: '2026-10-11T06:27:19Z'
  snapshot_sha256: f19c65bbfa350fd8d69a5e98977ba6a2f71254d285626b8d0bddb530c13bd88f
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
- evidence_id: taxon-287
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=287&retmode=xml
  locator: Exact NCBI Taxonomy identity and names
  accessed_at: '2026-10-11T06:27:28Z'
  snapshot_sha256: 8b8b55851c1c84bc3d3eb9cbc0e9dfc52d784a43b6c07d0f7aaa540be42697cf
  support: supports
  summary: Taxon and current scientific name resolve; taxonomy is not evidence of
    prevalence.
- evidence_id: taxon-264462
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=264462&retmode=xml
  locator: Exact NCBI Taxonomy identity and names
  accessed_at: '2026-10-11T06:27:28Z'
  snapshot_sha256: 2f4a3f21c9f8c729a4d9ab59be950742d7c1aa7dc6d45a33fe4290bdedbde2ca
  support: supports
  summary: Taxon and current scientific name resolve; taxonomy is not evidence of
    prevalence.
- evidence_id: adapter-inventory
  kind: validation
  reference: /private/tmp/csm-review-20261011T062301Z/adapter.log
  accessed_at: '2026-10-11T06:31:39Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Live 28-dataset iModulonDB inventory; no matching Caulobacter coverage.
    E. coli and P. aeruginosa searches were inspected.
- evidence_id: hospenthal
  kind: primary_source
  reference: DOI:10.1038/nrmicro.2017.40
  locator: 'Author manuscript pages 9-14: T4P biogenesis, machinery, filament and
    function'
  accessed_at: '2026-10-11T05:17:41Z'
  snapshot_sha256: 5c2dbbd1f8f92499fdda542390ccd97ce5e82ee7c2f785c61d7a118ee82a2a7d
  support: supports
  summary: Major/minor pilins form the filament. Cytoplasmic PilB/PilT belong to the
    motor subcomplex with PilC; the detailed motor account uses type IVa models.
- evidence_id: skerker
  kind: primary_source
  reference: DOI:10.1073/pnas.121171698
  locator: Abstract, Methods, Results and Discussion
  accessed_at: '2026-10-11T06:27:04Z'
  snapshot_sha256: 9368e051d922e74cbddd61be6a8b85360d8a95ce36942611360ce254a64ecc5c
  support: supports
  summary: Direct Pseudomonas imaging supports extension, distal attachment, force
    and retraction-driven cell movement.
- evidence_id: merz
  kind: primary_source
  reference: DOI:10.1038/35024105
  locator: Primary abstract
  accessed_at: '2026-10-11T06:24:43Z'
  snapshot_sha256: 43b3fa6ad96295c0388aeb1d822465b265b335595a16acfc87f474909aabf43a
  support: supports
  summary: Neisseria optical-tweezer experiments establish PilT-dependent retraction
    and motility, not PilT filament membership.
- evidence_id: bdellovibrio
  kind: primary_source
  reference: DOI:10.1038/s41564-023-01401-2
  locator: Attack-phase results, Figure 1 caption, attachment results and Methods
  accessed_at: '2026-10-11T06:27:04Z'
  snapshot_sha256: 231e87b13effe61c6ef8151e91c3d886ee64c567f69f32144c92c0ffd223fc92
  support: supports
  summary: HD100 cryo-ET observes pili and distinguishes them from empty basal machines;
    uncertain non-piliated structures are not used as pilus identity proof.
- evidence_id: cryo-dataset
  kind: authority
  reference: /private/tmp/csm-review-20261011T062301Z/cryo-dataset.json
  accessed_at: '2026-10-11T06:31:39Z'
  snapshot_sha256: 33ecb09fd8d1440b3804f27f5ee682ebc061188e6ac58b1b5438a7949209707f
  support: context_only
  summary: 'Exact official GraphQL metadata: dataset 10155, run 7978, annotation 30707
    with eight GO:0044096 objects, manual IMOD labeling and both quality flags true.'
- evidence_id: cryo-run
  kind: authority
  reference: /private/tmp/csm-review-20261011T062301Z/cryo-run.json
  accessed_at: '2026-10-11T06:31:39Z'
  snapshot_sha256: f94da0f7220eb742a38647ba47cd85dcaebf36c39162df6957733e932224d293
  support: context_only
  summary: 'Exact official GraphQL metadata: dataset 10155, run 7978, annotation 30707
    with eight GO:0044096 objects, manual IMOD labeling and both quality flags true.'
- evidence_id: cryo-annotation
  kind: authority
  reference: /private/tmp/csm-review-20261011T062301Z/cryo-annotation.json
  accessed_at: '2026-10-11T06:31:39Z'
  snapshot_sha256: a92d6209e73fc7a22cc6aff7fb591958eda45e461f5da1da46f73557eeff200d
  support: context_only
  summary: 'Exact official GraphQL metadata: dataset 10155, run 7978, annotation 30707
    with eight GO:0044096 objects, manual IMOD labeling and both quality flags true.'
- evidence_id: pilB-adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T062301Z/adapter-pilB.log
  accessed_at: '2026-10-11T06:31:39Z'
  snapshot_sha256: b3ff8b47b8768c945c82d609f80fdee253e29c46f3a3afcebd36904d276a9e81
  support: context_only
  summary: p_aeruginosa/precise364/PA4526 gene hit, no module hit; not composition
    proof.
- evidence_id: pilT-adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T062301Z/adapter-pilT.log
  accessed_at: '2026-10-11T06:31:39Z'
  snapshot_sha256: d9490e1a2c4e3f28618a3e87e44a384fa37558ffaeffc38cfa08b9a9e60471c6
  support: context_only
  summary: p_aeruginosa/precise364/PA0395 gene hit, no module hit; not composition
    proof.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261011T063139Z-type_iv_pilus-audit/review.yaml
  accessed_at: '2026-10-11T06:46:56Z'
  snapshot_sha256: bebafec12e97edf62b9b8d774281fe2012a84241b40b6ad4adc7595a62e9635a
  support: context_only
  summary: Immutable original observations committed before mutation.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261011T062301Z/preservation.json
  accessed_at: '2026-10-11T06:46:56Z'
  snapshot_sha256: beb90d8207e154d1bac8a0082ae7d81f39f3648695308b74264174304ef4b19c
  support: supports
  summary: Only four native records changed; 905 others and all prior histories, canonical
    reviews and legacy reports are byte-preserved.
- evidence_id: embeddings
  kind: validation
  reference: /private/tmp/csm-review-20261011T062301Z/embedding-refresh.json
  accessed_at: '2026-10-11T06:46:56Z'
  snapshot_sha256: a2e2b42849fa18abdffd855d2ee91e221053532cfb740760f8c14ee9d34175a9
  support: supports
  summary: Only three pilus semantic vectors changed; the provenance-only stalk correction
    is outside the semantic projection. The other 906 vectors are preserved.
assessments:
- assessment_id: resolved-f1
  area: scope
  topic: Keep cytoplasmic motors out of the pilus filament composition
  outcome: supported
  target_ids:
  - GO:0044096
  evidence_ids:
  - record
  - hospenthal
  - merz
  - rules
  - predecessor
  - preservation
  summary: PilB and PilT are no longer filament constituent rows or component references.
    Their evidenced motor nodes and all five edges remain in an explicitly type-IVa-scoped
    graph. A RESOLVED discussion records the boundary; major pilin and exact CryoET
    dataset provenance are unchanged.
findings:
- finding_id: F1
  issue_key: type-iv-pilus-filament-motor-boundary
  category: scope
  severity: major
  status: resolved
  certainty: confirmed
  title: Keep cytoplasmic motors out of the pilus filament composition
  description: PilB and PilT are no longer filament constituent rows or component
    references. Their evidenced motor nodes and all five edges remain in an explicitly
    type-IVa-scoped graph. A RESOLVED discussion records the boundary; major pilin
    and exact CryoET dataset provenance are unchanged.
  target_ids:
  - GO:0044096
  field_paths:
  - components[1]
  - components[2]
  - causal_graphs[0]
  evidence_ids:
  - record
  - hospenthal
  - merz
  - rules
  - predecessor
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/appendage/type_iv_pilus.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Material model-to-class scope or composition-boundary defect.
  disposition_reason: PilB and PilT are no longer filament constituent rows or component
    references. Their evidenced motor nodes and all five edges remain in an explicitly
    type-IVa-scoped graph. A RESOLVED discussion records the boundary; major pilin
    and exact CryoET dataset provenance are unchanged. Verified against inspected
    evidence, focused regressions and full QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261011T063139Z-type_iv_pilus-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2184
actions: []
limitations:
- Same-agent review, not human sign-off or completion of the 909-record goal.
- Identifier resolver skips and label pairs without adapters are not certified. Exact
  target GO/taxon authorities were separately inspected for the scientific reviews.
- Merz 2000 was assessed at primary-abstract level. Hospenthal was reread from the
  authenticated author manuscript. CryoET assessment is metadata-only; raw volumes
  and annotation geometry were not inspected.
- Original source-access tiers and snapshot times are retained; no raw experimental
  reanalysis or independent approval is implied.
- Five focused tests failed against original inputs; the corrected focused/guarded-writer
  suite passes. A preliminary lint check required an explicit strict zip argument,
  corrected before QC.
- The scratch embedding refresh initially expected four semantic changes and refused
  before writing. Inspection of the maintained semantic projection showed the stalk
  rationale/history are excluded; only the three real semantic changes were refreshed.
- Disposition inputs are retained by review-base/pilus-scope-20261011. Final PR and
  merge-group results are verified separately.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2184
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261011T063139Z-type_iv_pilus-audit
  relationship: Resolves exact predecessor findings without rewriting the original
    observation.
```
