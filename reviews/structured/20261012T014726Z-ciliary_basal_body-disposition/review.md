# Ciliary basal body: supported finding dispositions

- Review: 20261012T014726Z-ciliary_basal_body-disposition
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T01:47:23Z
- Finished UTC: 2026-10-12T01:47:26Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Two exact saved major findings and the subsequent minor publication finding resolved; both original observations, source limits, histories and PROPOSED status retained.

## Scope And Provenance

Exact saved findings from both observations and preservation of surrounding claims reassessed; not another whole-record review.

Selection: 20261012T011544Z-ciliary_basal_body-audit and 20261012T012821Z-ciliary_basal_body-publication-audit
Coverage: partial; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 783280672fd1712576696ebe69de2fa4dd83bcaf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036064 | data/structures/cytoskeleton/ciliary_basal_body.yaml | maintained | ciliary basal body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| publication-post-focused | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| publication-post-strict | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| publication-post-history | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0036064 | id↔label correspondence summary:<br>          OK_CANONICAL: 3545<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| curies | passed | True | GO:0036064 | resolver control: every resolver accepts a known id and rejects a fabricated one<br>resolving 2 DOI identifier(s)...<br><br>identifier liveness summary:<br>  OK             4018<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| traits | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| ciliary_basal_body-snippets | passed | True | GO:0036064 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| release-qc | passed | True | GO:0036064 | Full local QC passed: 979 passed, 3 skipped in 650.95s (0:10:50). PR and native merge-group gates remain separate. |

## Scientific And Domain Assessments

### Use the verified microtubule-organizing-center parent

grounding: supported. Targets: GO:0036064.

The record now uses the verified GO0005815 microtubule-organizing-center is-a parent while retaining exact GO0036064 identity and cilium parthood.

### Qualify structural essentiality beyond normal architecture

evidence: supported. Targets: GO:0036064.

Triplet and cartwheel essentiality are UNKNOWN with source-local UNI3 and SAS6 evidence limits. The count and graph scope now explicitly describe wild-type architecture. No categorical dispensability or whole-cartwheel ablation is inferred; original constituent roles and graph relationships remain unchanged.

### Expose basal-body graph scope in the rendered description

evidence: supported. Targets: GO:0036064.

The displayed graph description retains its original text and appends the complete existing scope paragraph plus an explicit nonmechanistic qualifier. Original scope fields and graph relations are unchanged.

## Findings

### F1: Use the verified microtubule-organizing-center parent

major / resolved / confirmed; issue key: ciliary-basal-body-mtoc-parent.

The record now uses the verified GO0005815 microtubule-organizing-center is-a parent while retaining exact GO0036064 identity and cilium parthood.

Disposition: The record now uses the verified GO0005815 microtubule-organizing-center is-a parent while retaining exact GO0036064 identity and cilium parthood. Verified by source-native authority/primary evidence, bounded diff, red/green regressions and full local QC.

### F2: Qualify structural essentiality beyond normal architecture

major / resolved / confirmed; issue key: ciliary-basal-body-substructure-essentiality.

Triplet and cartwheel essentiality are UNKNOWN with source-local UNI3 and SAS6 evidence limits. The count and graph scope now explicitly describe wild-type architecture. No categorical dispensability or whole-cartwheel ablation is inferred; original constituent roles and graph relationships remain unchanged.

Disposition: Triplet and cartwheel essentiality are UNKNOWN with source-local UNI3 and SAS6 evidence limits. The count and graph scope now explicitly describe wild-type architecture. No categorical dispensability or whole-cartwheel ablation is inferred; original constituent roles and graph relationships remain unchanged. Verified by source-native authority/primary evidence, bounded diff, red/green regressions and full local QC.

### F3: Expose basal-body graph scope in the rendered description

minor / resolved / confirmed; issue key: ciliary-basal-body-published-graph-scope.

The displayed graph description retains its original text and appends the complete existing scope paragraph plus an explicit nonmechanistic qualifier. Original scope fields and graph relations are unchanged.

Disposition: The displayed graph description retains its original text and appends the complete existing scope paragraph plus an explicit nonmechanistic qualifier. Original scope fields and graph relations are unchanged. Two red regressions now pass, the visible generated text was inspected and final full local QC passed.

## Recommended Actions And Acceptance Checks

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/ciliary_basal_body.yaml | context_only | Whole corrected YAML reread; exact bounded mutation and appended event verified against baseline. |
| rules | docs/CURATION.md | context_only | Typed is-a/parthood and assertion-local evidence; essentiality concerns structure formation, not cell survival or normal function. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml | context_only | ESSENTIAL means the structure does not form without the component; UNKNOWN is not a dispensability claim. |
| history | history/records/ciliary_basal_body/2026-09-13T091320Z-codex-fca9e4.yaml | context_only | Original CREATE history and prior taxonomy correction inspected; preserve unchanged. |
| reading | /private/tmp/csm-review-20261012T010700Z/reading-checkpoint.json | context_only | Actual full-text/abstract/visual scope, source hashes and limitations retained. |
| predecessors | /private/tmp/csm-review-20261012T010700Z/predecessors.json | context_only | Ignored-inclusive canonical scan has no exact-target predecessor. |
| prior-issues | /private/tmp/csm-review-20261012T010700Z/prior-issues.log | context_only | Existing closed issue767 removed a clade-wide distribution row; not either new finding. |
| context | /private/tmp/csm-review-20261012T010700Z/context-search.log | context_only | Ignored/hidden-inclusive context search, excluding only Git/dependency trees. |
| go-relations | /private/tmp/csm-review-20261012T002200Z/read-ahead/go-relations.log | context_only | Complete OAK typed relation for GO0036064: is_a GO0005815 and part_of GO0005929; live QuickGO corroborates is_a. |
| adapter | /private/tmp/csm-review-20261012T010700Z/adapter.log | context_only | Structured iModulonDB coverage inspected separately; expression modules do not establish ultrastructural identity or essentiality. |
| cilium | data/structures/appendage/cilium.yaml | context_only | Whole containing-record context read; has_part GO0036064 agrees with ciliary parthood. Not a new scientific review of cilium. |
| neighbor | data/structures/cytoskeleton/basal_body_cartwheel.yaml | context_only | Whole local context read; minted cartwheel is not a source-neutral exact GO mapping. No inherited claim is used as independent primary evidence. |
| uni3-caveat | /private/tmp/csm-review-20261012T002200Z/read-ahead/uni3-functional-scope-caveat.json | context_only | Explicit source caution: no universal functional dispensability from proximal doublets; no paired single-cell nucleation/ultrastructure inference. |
| issue-dedup-0 | /private/tmp/csm-review-20261012T010700Z/dedup-ciliary-basal-body-mtoc-parent.log | context_only | All-state exact issue-key search before creation. |
| issue-dedup-1 | /private/tmp/csm-review-20261012T010700Z/dedup-ciliary-basal-body-substructure-essentiality.log | context_only | All-state exact issue-key search before creation. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005856,GO%3A0005929,GO%3A0005930,GO%3A0032053,GO%3A0035253,GO%3A0036064,GO%3A0043232,GO%3A0051647,GO%3A0060271,GO%3A0120103; Exact native GO definitions, synonym types, component/function identities | supports | Exact basal-body identity, ciliary parthood and assembly function supported; generic microtubule is broader than the triplet substructure. |
| mtoc | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005815,GO%3A0036064; GO0005815 definition and child GO0036064 is_a; GO0036064 definition and synonyms | supports | Direct is-a parent is microtubule organizing center, not whole cytoskeleton. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055; Species3055 names and rank | supports | Chlamydomonas reinhardtii identity verified; authority alone is not prevalence evidence. |
| bld10 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2172387/fullTextXML; Matsuura2004 complete scientific main, TableI and all8captions | supports | Bld10 cartwheel localization, null basal-body defect and rescue support a role in early normal assembly. They do not selectively remove the entire cartwheel while retaining every other Bld10 function. |
| uni3 | https://pmc.ncbi.nlm.nih.gov/articles/PMC25351/; Dutcher/Trabuco1998 relevant Methods; ultrastructure, deletion and rescue Results; complete Discussion; Figures1/4 visually inspected | supports | Proximal doublets occur in uni3-1 mutant basal bodies; population includes0/1/2flagella. Complete triplet material absence in every functional ciliary basal body is not demonstrated, and authors retain a nucleation caveat. |
| sas6 | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2007.11.046%22&amp;format=json&amp;resultType=core; Nakazawa2007 DOI10.1016/j.cub.2007.11.046; PMID18082404; full primary abstract only | supports | SAS6-null bld12 lacks the central cartwheel part and retains centrioles with variable triplet counts. This is not proof that all spoke-tip/cartwheel material was removed. |
| review2016 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4888484/fullTextXML; Dutcher/OToole2016 complete main and3captions; mutant paragraphs reread | context_only | Secondary review distinguishes normal triplets and cartwheel architecture from delta/epsilon-tubulin and SAS6 mutants; spoke tips can remain without SAS6. Not independent primary experimental evidence. |
| review2018 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6070942/fullTextXML; Wingfield/Lechtreck2018 complete main and5captions; Figure2 and mutant paragraphs reread | context_only | Secondary review explicitly separates wild-type nine-triplet/cartwheel architecture from uni3/bld12 variants, including residual flagella. No raw or paired-cell analysis performed. |
| silflow | https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1104%2Fpp.010807%22&amp;format=json&amp;resultType=core; Silflow/Lefebvre2001 DOI/PMID/title metadata only | supports | Publication identity verified. Full text inaccessible by attempted routes; immediate GO definition independently supports the bounded native nucleation function. |
| predecessor | reviews/structured/20261012T011544Z-ciliary_basal_body-audit/review.yaml | context_only | Original immutable observation committed before scientific edits. |
| red-tests | /private/tmp/csm-review-20261012T010700Z/regressions-red.log | context_only | Seven regressions fail before correction; three preservation controls pass. |
| green-tests | /private/tmp/csm-review-20261012T010700Z/publication-post-focused.log | context_only | All twelve regressions and guarded-writer tests pass after both corrections. |
| preservation | /private/tmp/csm-review-20261012T010700Z/publication-preservation.json | context_only | All908 other records,908 other vectors, prior histories/reviews/legacy files and three clean targets unchanged. |
| edit-history | history/records/ciliary_basal_body/2026-10-12T011949Z-codex-fb0531.yaml | context_only | Actual Codex EDIT links original review and both issues; changed sections derive from the exact native diff. |
| embedding | /private/tmp/csm-review-20261012T010700Z/embedding-refresh.json | context_only | Only the wild-type property-context correction changes semantic text; one vector regenerated with the pinned local model. |
| publication-predecessor | reviews/structured/20261012T012821Z-ciliary_basal_body-publication-audit/review.yaml | context_only | Scoped publication observation committed before the display-field correction. |
| publication-history | history/records/ciliary_basal_body/2026-10-12T012852Z-codex-e5f383.yaml | context_only | Second actual EDIT preserves the original graph introduction and appends its existing qualifiers. |
| publication-red | /private/tmp/csm-review-20261012T010700Z/publication-red.log | context_only | Both new description and visible-page assertions failed before the publication correction. |
| publication-page | pages/structures/cytoskeleton/ciliary_basal_body.html | context_only | Generated page now displays the complete existing scope paragraph and nonmechanistic qualifier. |

## Limits And Additional Notes

- Same-agent whole-record assessment, not independent human approval or raw-data reanalysis.
- SAS6 source is primary abstract only; Silflow2001 has metadata/PMC landing only and attempted PDF returned HTML. UNI3 primary sections and two figures, Bld10 main/captions, and both full review main texts were inspected at the stated scopes.
- UNI3 may retain a functional nucleation requirement; SAS6 central-part loss is not demonstrated removal of all cartwheel material. UNKNOWN preserves these uncertainties and is not a dispensability conclusion.
- Bounded ontology searches do not prove global absence. Expression-module data cannot establish ultrastructural component necessity.
- The other three fiber records have separate review accounting; this issue-only bundle does not certify them.
- Full local QC passed with existing skips retained; PR and native merge-group checks remain separate publication gates.
- Same-agent scoped disposition, not a repeated whole-record review. Exact corrected inputs retained by review-base/basal-body-evidence-20261012.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T014726Z-ciliary_basal_body-disposition
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Ciliary basal body: supported finding dispositions'
started_at: '2026-10-12T01:47:23Z'
finished_at: '2026-10-12T01:47:26Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent whole-record and source review; not independent human
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: pass_with_limitations
scientific_review: true
summary: Two exact saved major findings and the subsequent minor publication finding
  resolved; both original observations, source limits, histories and PROPOSED status
  retained.
source:
  git_revision: 783280672fd1712576696ebe69de2fa4dd83bcaf
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
    sha256: 3acb13884094f40c840ed3452a6209ee9a38b479ae16e4c0bca390c3c290828a
    role: context
  - path: curation/source_queue.tsv
    sha256: 55d8fe79b5edd7d6b42bf4ca9168fe4878240417716e2f4ba423489144b89284
    role: context
  - path: data/structures/appendage/cilium.yaml
    sha256: 2536d421f9c482abf35c2d2bf026eb6158ddfec5c2df1f319ca80698cbb56bb8
    role: context
  - path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    sha256: ad4e6fcf7639e0fffc00b553b0ab2e0e2a8eac5981b87ae9da1ee783ba942957
    role: context
  - path: data/structures/cytoskeleton/basal_body_triplet_base.yaml
    sha256: c88a6c10f311bce934e37d5583f122fee6cae6f45950117728cb6d1a7905e6f8
    role: context
  - path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    sha256: 46027bf3d3d8b3011803fa72d1229a892d34b7233d48ca290466b9afefb6b7ef
    role: target
  - path: data/structures/cytoskeleton/ciliary_rootlet.yaml
    sha256: 7e83f24e1bd10b9945a81a6f912aae66c8ca18a751aa4147a7d0a5bcf3fa88c9
    role: context
  - path: data/structures/cytoskeleton/distal_connecting_fiber.yaml
    sha256: 3fbecc2d7d51c4e4ea53cdbc4d6e49251a300430f23fc0d76d00a3412a2a8d79
    role: context
  - path: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
    sha256: 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d
    role: context
  - path: data/structures/cytoskeleton/sinister_fiber.yaml
    sha256: 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5
    role: context
  - path: docs/CURATION.md
    sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
    role: context
  - path: docs/SCHEMA.md
    sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
    role: context
  - path: docs/SOURCE_QUEUE.md
    sha256: 793e9a16435684b90b0d64b7be4bdfeffbba5ab6ac0ca99eadf25c8548e22729
    role: context
  - path: docs/record-review-profile.md
    sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: history/README.md
    sha256: 1636df44f28547f440242afcb4a05ac293b9714b4d7b809cecc30b975e44a522
    role: context
  - path: history/records/ciliary_basal_body/2026-09-13T091320Z-codex-fca9e4.yaml
    sha256: 0fe1f82ce8985d4dfc71d1868762bde7ae048fc5ec5daec339c7a9610a7b1989
    role: context
  - path: history/records/ciliary_basal_body/2026-10-12T011949Z-codex-fb0531.yaml
    sha256: f215b6327bb1f6f20c3fcdbefb1fa92cb9d1fb4155dd076e9ce74740d5528bdd
    role: context
  - path: history/records/ciliary_basal_body/2026-10-12T012852Z-codex-e5f383.yaml
    sha256: d4fa7b15ec5eeef5e1a65df40b690d0ef0438e30041eb207adb5f3a3f14f4750
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: pages/structures/cytoskeleton/ciliary_basal_body.html
    sha256: 66e4fc25168cc79350c5648f3663e315ab36bb937e92434cee279148d99490e6
    role: context
  - path: reviews/structured/20261012T011544Z-ciliary_basal_body-audit/review.yaml
    sha256: aca09fb429e058c4ccb0d46384f0a50f616a2828896cd33fff6de2c7a25ad12b
    role: context
  - path: reviews/structured/20261012T012821Z-ciliary_basal_body-publication-audit/review.yaml
    sha256: 62f42280be6b7622b7d25ef68b5de308e8e1bb8c804a9ee94a0e69a10439dda9
    role: context
  - path: scripts/render_pages.py
    sha256: b5be74a8a3a0f7190b63da47a86cd8b48cbce4bb955ea0896f29d24f214a9b22
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/mech_shared.yaml
    sha256: c2e7054fd32635e380c698282bd886a9105861009b9f0474f02bb1b80865e895
    role: context
  - path: src/cellstructuremech/templates/structure.html
    sha256: 417b020a6eda677a1e40ecd3d849bfd5063d83291d7496e1c52a1a3a321f35ed
    role: context
  - path: tests/test_basal_body_evidence_scope.py
    sha256: db5df16fc006ca93c461f0f0ad2534085e24a5eed2ba429d56447016affd29f2
    role: context
targets:
- target_id: GO:0036064
  path: data/structures/cytoskeleton/ciliary_basal_body.yaml
  label: ciliary basal body
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained scientific record
scope:
  description: Exact saved findings from both observations and preservation of surrounding
    claims reassessed; not another whole-record review.
  selection: 20261012T011544Z-ciliary_basal_body-audit and 20261012T012821Z-ciliary_basal_body-publication-audit
  coverage: partial
  population_size: 1
  reviewed_target_ids:
  - GO:0036064
checks:
- check_id: publication-post-focused
  name: publication-post-focused
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python -m pytest -q tests/test_basal_body_evidence_scope.py tests/test_write_validated.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T01:30:35Z to 2026-10-12T01:31:30Z; log SHA-256 e1ce8afcafb1ee6a7c480e7d89d52012ecafb3ef074bd992ddb6640cb442a053
- check_id: publication-post-strict
  name: publication-post-strict
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/ciliary_basal_body.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T01:31:30Z to 2026-10-12T01:31:36Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: publication-post-history
  name: publication-post-history
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T01:31:36Z to 2026-10-12T01:31:59Z; log SHA-256 18ccd1252becfd50c7b7b60bac6a12cbe7a48c66582a4bf9e60fd29e20d3a3ba
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3545\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-12T01:24:33Z to 2026-10-12T01:26:27Z; log SHA-256 459523b233cf29c593d6ebe49a38d5ed4484b1f98496dc47ea4fdc17be729286
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\nresolving 2 DOI identifier(s)...\n\nidentifier liveness summary:\n  OK\
    \             4018\n  SKIPPED         251\n\nEvery identifier resolves at its\
    \ issuing authority."
  scope_note: 2026-10-12T01:26:27Z to 2026-10-12T01:27:21Z; log SHA-256 cb1b3508df9e5c60d6d244aac4ed481014ce61053ce544472c6ee0c8acdeb6f9
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T01:27:21Z to 2026-10-12T01:27:38Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: ciliary_basal_body-snippets
  name: ciliary_basal_body-snippets
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/ciliary_basal_body.yaml
    --report /private/tmp/csm-review-20261012T010700Z/post-ciliary_basal_body-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-12T01:23:37Z to 2026-10-12T01:24:11Z; log SHA-256 3ecdbdb982e3fe85221f259f8617ccdbb4417c7fef9456ee6c312f16c0a5b092
- check_id: release-qc
  name: release-qc
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: just qc
  exit_code: 0
  expected_exit_code: 0
  summary: 'Full local QC passed: 979 passed, 3 skipped in 650.95s (0:10:50). PR and
    native merge-group gates remain separate.'
  scope_note: 2026-10-12T01:31:59Z to 2026-10-12T01:47:04Z; log SHA-256 e044aced1648cece2c3edc051835cfbbe4eb27ea5a32a1985ad394d9d31b387c
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_basal_body.yaml
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: 46027bf3d3d8b3011803fa72d1229a892d34b7233d48ca290466b9afefb6b7ef
  support: context_only
  summary: Whole corrected YAML reread; exact bounded mutation and appended event
    verified against baseline.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Typed is-a/parthood and assertion-local evidence; essentiality concerns
    structure formation, not cell survival or normal function.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  support: context_only
  summary: ESSENTIAL means the structure does not form without the component; UNKNOWN
    is not a dispensability claim.
- evidence_id: history
  kind: record_content
  reference: history/records/ciliary_basal_body/2026-09-13T091320Z-codex-fca9e4.yaml
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 0fe1f82ce8985d4dfc71d1868762bde7ae048fc5ec5daec339c7a9610a7b1989
  support: context_only
  summary: Original CREATE history and prior taxonomy correction inspected; preserve
    unchanged.
- evidence_id: reading
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/reading-checkpoint.json
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: bcd2765afbd5b072c15e7a758f92fedf1ca715ca3105c4a07146fcb076e0fdba
  support: context_only
  summary: Actual full-text/abstract/visual scope, source hashes and limitations retained.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/predecessors.json
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 2b90d23c7b39dce8797b9b332eaaa9e0261a2a72407d265edcc879d67ef8f971
  support: context_only
  summary: Ignored-inclusive canonical scan has no exact-target predecessor.
- evidence_id: prior-issues
  kind: prior_review
  reference: /private/tmp/csm-review-20261012T010700Z/prior-issues.log
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: d9c89d528b8f27e03e267d4dbe7a05dae71bd54e7c859b25bda43d7b57d938c6
  support: context_only
  summary: Existing closed issue767 removed a clade-wide distribution row; not either
    new finding.
- evidence_id: context
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/context-search.log
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 3055f3c9438ce5bc66613a4de86b762e3c353925fc0ef1166c2415243e2ccf2b
  support: context_only
  summary: Ignored/hidden-inclusive context search, excluding only Git/dependency
    trees.
- evidence_id: go-relations
  kind: authority
  reference: /private/tmp/csm-review-20261012T002200Z/read-ahead/go-relations.log
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 958b4db5258f92b919bed8b2cd3bce2eef1054404ff2710cdac40e451f89eaa8
  support: context_only
  summary: 'Complete OAK typed relation for GO0036064: is_a GO0005815 and part_of
    GO0005929; live QuickGO corroborates is_a.'
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/adapter.log
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: Structured iModulonDB coverage inspected separately; expression modules
    do not establish ultrastructural identity or essentiality.
- evidence_id: cilium
  kind: record_content
  reference: data/structures/appendage/cilium.yaml
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 2536d421f9c482abf35c2d2bf026eb6158ddfec5c2df1f319ca80698cbb56bb8
  support: context_only
  summary: Whole containing-record context read; has_part GO0036064 agrees with ciliary
    parthood. Not a new scientific review of cilium.
- evidence_id: neighbor
  kind: record_content
  reference: data/structures/cytoskeleton/basal_body_cartwheel.yaml
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: ad4e6fcf7639e0fffc00b553b0ab2e0e2a8eac5981b87ae9da1ee783ba942957
  support: context_only
  summary: Whole local context read; minted cartwheel is not a source-neutral exact
    GO mapping. No inherited claim is used as independent primary evidence.
- evidence_id: uni3-caveat
  kind: validation
  reference: /private/tmp/csm-review-20261012T002200Z/read-ahead/uni3-functional-scope-caveat.json
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 48c7cdf2a1c1fbf02a73387efc5215300c58848569645e0cad98473de2ff331e
  support: context_only
  summary: 'Explicit source caution: no universal functional dispensability from proximal
    doublets; no paired single-cell nucleation/ultrastructure inference.'
- evidence_id: issue-dedup-0
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/dedup-ciliary-basal-body-mtoc-parent.log
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state exact issue-key search before creation.
- evidence_id: issue-dedup-1
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/dedup-ciliary-basal-body-substructure-essentiality.log
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state exact issue-key search before creation.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005856,GO%3A0005929,GO%3A0005930,GO%3A0032053,GO%3A0035253,GO%3A0036064,GO%3A0043232,GO%3A0051647,GO%3A0060271,GO%3A0120103
  locator: Exact native GO definitions, synonym types, component/function identities
  accessed_at: '2026-10-12T00:28:40Z'
  snapshot_sha256: 1b914b09e6e4115bcd9145a95917208de5d76f1d48862d5337fb9d1c16739e6a
  support: supports
  summary: Exact basal-body identity, ciliary parthood and assembly function supported;
    generic microtubule is broader than the triplet substructure.
- evidence_id: mtoc
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005815,GO%3A0036064
  locator: GO0005815 definition and child GO0036064 is_a; GO0036064 definition and
    synonyms
  accessed_at: '2026-10-12T01:08:48Z'
  snapshot_sha256: b15c76eea1a36d73da1170431bdfa22a7fb9e1d614dfbe7f6f6d82140ef382e9
  support: supports
  summary: Direct is-a parent is microtubule organizing center, not whole cytoskeleton.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/3055
  locator: Species3055 names and rank
  accessed_at: '2026-10-12T00:28:51Z'
  snapshot_sha256: a24c8f85014097148d9e865ea324b01b8d04f6bae27e893834f8abb5bd8b6a1f
  support: supports
  summary: Chlamydomonas reinhardtii identity verified; authority alone is not prevalence
    evidence.
- evidence_id: bld10
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC2172387/fullTextXML
  locator: Matsuura2004 complete scientific main, TableI and all8captions
  accessed_at: '2026-10-12T00:28:07Z'
  snapshot_sha256: 1b1eea71dfaaebd4da3d259e54a1831ed0c736f80e314bc50480160e0cf51d58
  support: supports
  summary: Bld10 cartwheel localization, null basal-body defect and rescue support
    a role in early normal assembly. They do not selectively remove the entire cartwheel
    while retaining every other Bld10 function.
- evidence_id: uni3
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC25351/
  locator: Dutcher/Trabuco1998 relevant Methods; ultrastructure, deletion and rescue
    Results; complete Discussion; Figures1/4 visually inspected
  accessed_at: '2026-10-12T00:41:48Z'
  snapshot_sha256: cf0ee4f04452cc38eb07b7ba8494171a98ee18f514b81de29128eede99ed3903
  support: supports
  summary: Proximal doublets occur in uni3-1 mutant basal bodies; population includes0/1/2flagella.
    Complete triplet material absence in every functional ciliary basal body is not
    demonstrated, and authors retain a nucleation caveat.
- evidence_id: sas6
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1016%2Fj.cub.2007.11.046%22&format=json&resultType=core
  locator: Nakazawa2007 DOI10.1016/j.cub.2007.11.046; PMID18082404; full primary abstract
    only
  accessed_at: '2026-10-12T00:41:49Z'
  snapshot_sha256: c95ffdddd73cb42392c57a364f75ebcb49a7f2e479dc1f7f3152e8b4c86e76db
  support: supports
  summary: SAS6-null bld12 lacks the central cartwheel part and retains centrioles
    with variable triplet counts. This is not proof that all spoke-tip/cartwheel material
    was removed.
- evidence_id: review2016
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4888484/fullTextXML
  locator: Dutcher/OToole2016 complete main and3captions; mutant paragraphs reread
  accessed_at: '2026-10-12T00:28:13Z'
  snapshot_sha256: 3cc29d2ea2e47d3bfd51742187c541299f3f7907998e7526d31bf26cd082537d
  support: context_only
  summary: Secondary review distinguishes normal triplets and cartwheel architecture
    from delta/epsilon-tubulin and SAS6 mutants; spoke tips can remain without SAS6.
    Not independent primary experimental evidence.
- evidence_id: review2018
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC6070942/fullTextXML
  locator: Wingfield/Lechtreck2018 complete main and5captions; Figure2 and mutant
    paragraphs reread
  accessed_at: '2026-10-12T00:28:16Z'
  snapshot_sha256: 32375e951e01d76c16ddfee275e90f1e94feb3aede6c06952b38f01ee009e079
  support: context_only
  summary: Secondary review explicitly separates wild-type nine-triplet/cartwheel
    architecture from uni3/bld12 variants, including residual flagella. No raw or
    paired-cell analysis performed.
- evidence_id: silflow
  kind: authority
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI%3A%2210.1104%2Fpp.010807%22&format=json&resultType=core
  locator: Silflow/Lefebvre2001 DOI/PMID/title metadata only
  accessed_at: '2026-10-12T00:28:10Z'
  snapshot_sha256: 179f0249d9770a482dfacbaae6f58062e342c6de0b371d990d7d7e31c7a33439
  support: supports
  summary: Publication identity verified. Full text inaccessible by attempted routes;
    immediate GO definition independently supports the bounded native nucleation function.
- evidence_id: predecessor
  kind: prior_review
  reference: reviews/structured/20261012T011544Z-ciliary_basal_body-audit/review.yaml
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: aca09fb429e058c4ccb0d46384f0a50f616a2828896cd33fff6de2c7a25ad12b
  support: context_only
  summary: Original immutable observation committed before scientific edits.
- evidence_id: red-tests
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/regressions-red.log
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: 645dd7d75e335e40d0ece53e7064d7d5c98d1668db7fab17e68ed9259eb86068
  support: context_only
  summary: Seven regressions fail before correction; three preservation controls pass.
- evidence_id: green-tests
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/publication-post-focused.log
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: e1ce8afcafb1ee6a7c480e7d89d52012ecafb3ef074bd992ddb6640cb442a053
  support: context_only
  summary: All twelve regressions and guarded-writer tests pass after both corrections.
- evidence_id: preservation
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/publication-preservation.json
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: d0e7f223abe27d87c4448b6d50c7b2f87dfded849f122f8a57de1e8f91ec99ce
  support: context_only
  summary: All908 other records,908 other vectors, prior histories/reviews/legacy
    files and three clean targets unchanged.
- evidence_id: edit-history
  kind: record_content
  reference: history/records/ciliary_basal_body/2026-10-12T011949Z-codex-fb0531.yaml
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: f215b6327bb1f6f20c3fcdbefb1fa92cb9d1fb4155dd076e9ce74740d5528bdd
  support: context_only
  summary: Actual Codex EDIT links original review and both issues; changed sections
    derive from the exact native diff.
- evidence_id: embedding
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/embedding-refresh.json
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: 5cb7a8e117462451a85e85493c24b8939b021b6935658c91a7ac6a4fda6bf0a1
  support: context_only
  summary: Only the wild-type property-context correction changes semantic text; one
    vector regenerated with the pinned local model.
- evidence_id: publication-predecessor
  kind: prior_review
  reference: reviews/structured/20261012T012821Z-ciliary_basal_body-publication-audit/review.yaml
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: 62f42280be6b7622b7d25ef68b5de308e8e1bb8c804a9ee94a0e69a10439dda9
  support: context_only
  summary: Scoped publication observation committed before the display-field correction.
- evidence_id: publication-history
  kind: record_content
  reference: history/records/ciliary_basal_body/2026-10-12T012852Z-codex-e5f383.yaml
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: d4fa7b15ec5eeef5e1a65df40b690d0ef0438e30041eb207adb5f3a3f14f4750
  support: context_only
  summary: Second actual EDIT preserves the original graph introduction and appends
    its existing qualifiers.
- evidence_id: publication-red
  kind: validation
  reference: /private/tmp/csm-review-20261012T010700Z/publication-red.log
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: c8178ba15bb835f81cf6a2ddd0d15e12aaea69a66d0030099fab854cfae71b22
  support: context_only
  summary: Both new description and visible-page assertions failed before the publication
    correction.
- evidence_id: publication-page
  kind: record_content
  reference: pages/structures/cytoskeleton/ciliary_basal_body.html
  accessed_at: '2026-10-12T01:47:26Z'
  snapshot_sha256: 66e4fc25168cc79350c5648f3663e315ab36bb937e92434cee279148d99490e6
  support: context_only
  summary: Generated page now displays the complete existing scope paragraph and nonmechanistic
    qualifier.
assessments:
- assessment_id: resolved-f1
  area: grounding
  topic: Use the verified microtubule-organizing-center parent
  outcome: supported
  target_ids:
  - GO:0036064
  evidence_ids:
  - record
  - rules
  - go-relations
  - mtoc
  - predecessor
  - red-tests
  - green-tests
  - preservation
  - edit-history
  summary: The record now uses the verified GO0005815 microtubule-organizing-center
    is-a parent while retaining exact GO0036064 identity and cilium parthood.
- assessment_id: resolved-f2
  area: evidence
  topic: Qualify structural essentiality beyond normal architecture
  outcome: supported
  target_ids:
  - GO:0036064
  evidence_ids:
  - record
  - rules
  - schema
  - bld10
  - uni3
  - sas6
  - review2016
  - review2018
  - uni3-caveat
  - predecessor
  - red-tests
  - green-tests
  - preservation
  - edit-history
  summary: Triplet and cartwheel essentiality are UNKNOWN with source-local UNI3 and
    SAS6 evidence limits. The count and graph scope now explicitly describe wild-type
    architecture. No categorical dispensability or whole-cartwheel ablation is inferred;
    original constituent roles and graph relationships remain unchanged.
- assessment_id: resolved-f3
  area: evidence
  topic: Expose basal-body graph scope in the rendered description
  outcome: supported
  target_ids:
  - GO:0036064
  evidence_ids:
  - record
  - publication-predecessor
  - publication-history
  - publication-red
  - publication-page
  - green-tests
  - preservation
  summary: The displayed graph description retains its original text and appends the
    complete existing scope paragraph plus an explicit nonmechanistic qualifier. Original
    scope fields and graph relations are unchanged.
findings:
- finding_id: F1
  issue_key: ciliary-basal-body-mtoc-parent
  category: grounding
  severity: major
  status: resolved
  certainty: confirmed
  title: Use the verified microtubule-organizing-center parent
  description: The record now uses the verified GO0005815 microtubule-organizing-center
    is-a parent while retaining exact GO0036064 identity and cilium parthood.
  target_ids:
  - GO:0036064
  field_paths:
  - parent_structures
  - evidence
  evidence_ids:
  - record
  - rules
  - go-relations
  - mtoc
  - predecessor
  - red-tests
  - green-tests
  - preservation
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Wrong typed hierarchy or unsupported categorical assembly
    requirement changes structured scientific meaning; identity and normal constituent
    membership remain supported.
  disposition_reason: The record now uses the verified GO0005815 microtubule-organizing-center
    is-a parent while retaining exact GO0036064 identity and cilium parthood. Verified
    by source-native authority/primary evidence, bounded diff, red/green regressions
    and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261012T011544Z-ciliary_basal_body-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2275
- finding_id: F2
  issue_key: ciliary-basal-body-substructure-essentiality
  category: evidence
  severity: major
  status: resolved
  certainty: confirmed
  title: Qualify structural essentiality beyond normal architecture
  description: Triplet and cartwheel essentiality are UNKNOWN with source-local UNI3
    and SAS6 evidence limits. The count and graph scope now explicitly describe wild-type
    architecture. No categorical dispensability or whole-cartwheel ablation is inferred;
    original constituent roles and graph relationships remain unchanged.
  target_ids:
  - GO:0036064
  field_paths:
  - components[0].essentiality
  - components[0].evidence
  - components[1].essentiality
  - components[1].evidence
  - physical_properties[0].context
  - causal_graphs[0].scope_notes
  evidence_ids:
  - record
  - rules
  - schema
  - bld10
  - uni3
  - sas6
  - review2016
  - review2018
  - uni3-caveat
  - predecessor
  - red-tests
  - green-tests
  - preservation
  - edit-history
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Wrong typed hierarchy or unsupported categorical assembly
    requirement changes structured scientific meaning; identity and normal constituent
    membership remain supported.
  disposition_reason: Triplet and cartwheel essentiality are UNKNOWN with source-local
    UNI3 and SAS6 evidence limits. The count and graph scope now explicitly describe
    wild-type architecture. No categorical dispensability or whole-cartwheel ablation
    is inferred; original constituent roles and graph relationships remain unchanged.
    Verified by source-native authority/primary evidence, bounded diff, red/green
    regressions and full local QC.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261012T011544Z-ciliary_basal_body-audit
    finding_id: F2
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2276
- finding_id: F3
  issue_key: ciliary-basal-body-published-graph-scope
  category: evidence
  severity: minor
  status: resolved
  certainty: confirmed
  title: Expose basal-body graph scope in the rendered description
  description: The displayed graph description retains its original text and appends
    the complete existing scope paragraph plus an explicit nonmechanistic qualifier.
    Original scope fields and graph relations are unchanged.
  target_ids:
  - GO:0036064
  field_paths:
  - causal_graphs[0].description
  evidence_ids:
  - record
  - publication-predecessor
  - publication-history
  - publication-red
  - publication-page
  - green-tests
  - preservation
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded rendered-publication omission; native scope and nearby
    caveats already exist.
  disposition_reason: The displayed graph description retains its original text and
    appends the complete existing scope paragraph plus an explicit nonmechanistic
    qualifier. Original scope fields and graph relations are unchanged. Two red regressions
    now pass, the visible generated text was inspected and final full local QC passed.
  previous_occurrences:
  - repository: CultureBotAI/CellStructureMech
    review_id: 20261012T012821Z-ciliary_basal_body-publication-audit
    finding_id: F1
  external_issues:
  - https://github.com/CultureBotAI/CellStructureMech/issues/2277
actions: []
limitations:
- Same-agent whole-record assessment, not independent human approval or raw-data reanalysis.
- SAS6 source is primary abstract only; Silflow2001 has metadata/PMC landing only
  and attempted PDF returned HTML. UNI3 primary sections and two figures, Bld10 main/captions,
  and both full review main texts were inspected at the stated scopes.
- UNI3 may retain a functional nucleation requirement; SAS6 central-part loss is not
  demonstrated removal of all cartwheel material. UNKNOWN preserves these uncertainties
  and is not a dispensability conclusion.
- Bounded ontology searches do not prove global absence. Expression-module data cannot
  establish ultrastructural component necessity.
- The other three fiber records have separate review accounting; this issue-only bundle
  does not certify them.
- Full local QC passed with existing skips retained; PR and native merge-group checks
  remain separate publication gates.
- Same-agent scoped disposition, not a repeated whole-record review. Exact corrected
  inputs retained by review-base/basal-body-evidence-20261012.
links:
- https://github.com/CultureBotAI/CellStructureMech/issues/2275
- https://github.com/CultureBotAI/CellStructureMech/issues/2276
- https://github.com/CultureBotAI/CellStructureMech/issues/2277
related_reviews:
- repository: CultureBotAI/CellStructureMech
  review_id: 20261012T011544Z-ciliary_basal_body-audit
  relationship: Resolves both exact original finding occurrences without replacing
    the bundle.
- repository: CultureBotAI/CellStructureMech
  review_id: 20261012T012821Z-ciliary_basal_body-publication-audit
  relationship: Resolves the exact scoped publication finding without replacing its
    bundle.
```
