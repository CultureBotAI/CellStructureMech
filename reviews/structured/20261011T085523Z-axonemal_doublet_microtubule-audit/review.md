# Axonemal doublet microtubule: scientific record review

- Review: 20261011T085523Z-axonemal_doublet_microtubule-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T08:43:44Z
- Finished UTC: 2026-10-11T08:55:23Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole native record reviewed; one minor discussion-provenance defect saved before separately authorized curation.

## Scope And Provenance

Whole native YAML, every causal edge, identity and typed hierarchy, composition, taxonomy, functions, optional resources, discussion lifecycle and both history surfaces.

Selection: One exact target in the 909-record review goal; adjacent records are supporting context, not additional certified reviews.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d01b9d412c3f5a0d08b0f2fab6d08b33a5fe88ab.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097545 | data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml | maintained | axonemal doublet microtubule |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0097545 | Deterministic validation passed; scientific claim assessment is separate. |
| strict | passed | True | GO:0097545 | Deterministic validation passed; scientific claim assessment is separate. |
| snippets | passed | True | GO:0097545 | No verbatim snippets asserted. Paraphrased claim support was inspected separately. |
| history | passed | True | GO:0097545 | Deterministic validation passed; scientific claim assessment is separate. |
| labels | passed | True | GO:0097545 | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0097545 | Deterministic validation passed; scientific claim assessment is separate. |
| curies | passed | True | GO:0097545 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4014<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0097545 | Deterministic validation passed; scientific claim assessment is separate. |
| diff | passed | True | GO:0097545 | Deterministic validation passed; scientific claim assessment is separate. |
| Exact-baseline CI full QC and review contract | passed | True | GO:0097545 | Full native QC (840 passed, 3 skipped) and review-contract gates passed on the exact captured baseline. This is a verified CI receipt, not a fresh local QC execution. |

## Scientific And Domain Assessments

### Identity, hierarchy, composition, species scope, functions and every graph edge

evidence: supported. Targets: GO:0097545.

GO:0097545 is the doublet scaffold, not a single tubulin protein or the entire axoneme. Six has_part links retain A/B tubules, inner sheath, both junctions and ribbon. The generic alpha/beta-tubulin class is conservatively label-only. Chlamydomonas nine-doublet and A13/B10 protofilament scope, both tubule parthood edges, tubulin polymerization, MIP-mediated stabilization and axoneme containment are supported. Owa measures B-lumen stabilization rather than every MIP in every species.

### Historical rationale and current task lifecycle

provenance: concern. Targets: GO:0097545.

The original rationale at 8b410f98 distinguished the coarse A/B scaffold from finer substructures. Four child additions at 1a6f7145, 5b2752fe, 8885f3fc and 16734f12 replaced it rather than appending. The current record loses the initial scope and intermediate decisions, contrary to the append-only rationale rule.

### Optional resources, conservative groundings and status

completeness: supported. Targets: GO:0097545.

No native images, quantitative property measurements, protein/dataset accessions or trait links require additional resource verification. Coarse label-only groups and acknowledged open molecular tasks are not invented defects. Native status remains PROPOSED.

## Findings

### F1: Restore the doublet-microtubule discussion rationale history

minor / open / confirmed; issue key: doublet-microtubule-discussion-rationale-preservation.

The original rationale at 8b410f98 distinguished the coarse A/B scaffold from finer substructures. Four child additions at 1a6f7145, 5b2752fe, 8885f3fc and 16734f12 replaced it rather than appending. The current record loses the initial scope and intermediate decisions, contrary to the append-only rationale rule.

## Recommended Actions And Acceptance Checks

### A1

Restore the doublet-microtubule discussion rationale history

- Restore the exact original rationale and every distinct later version, with revision-labelled historical context rather than current absence claims.
- Preserve current discussion IDs, narrowed prompts, live attachments, original posed dates and authors, statuses, all has_part links, all graph edges and earlier scientific scope corrections.
- Use the guarded writer, append Codex curation and EDIT history, preserve PROPOSED, prior history/reviews and unrelated records, regenerate pages, and pass focused regressions and native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml | context_only | Entire native YAML read; formal input capture preceded assessment, though initial reading preceded capture. |
| rules | docs/CURATION.md | context_only | Discussion rationale must be appended, not replaced; dates and resolved lifecycle must be preserved. |
| history | /private/tmp/csm-review-20261011T084242Z/axonemal_doublet_microtubule-discussion-history.json | context_only | All committed revisions of this target inspected, including full discussion objects and curation events. |
| context | /private/tmp/csm-review-20261011T084242Z/context-read.log | context_only | Maintained neighboring structures and append-only repository history inspected for current boundaries and earlier corrections. |
| predecessors | /private/tmp/csm-review-20261011T084242Z/exact-target-predecessors.json | context_only | Ignored-inclusive recursive structured-review target search found no exact-target predecessor; references to the term in another review are not target coverage. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001534,GO:0003352,GO:0005858,GO:0005879,GO:0005881,GO:0005930,GO:0005931,GO:0030286,GO:0036156,GO:0036157,GO:0051012,GO:0097540,GO:0097545,GO:0097649,GO:0097650,GO:0160110,GO:0160111,GO:0160112,GO:0160113,GO:0160114,GO:0160115,GO:1990716,GO:1990718,GO:1990719,GO:1990720; Exact term definitions, aspect, obsolescence, synonyms and typed reverse children for all 25 asserted GO identifiers in the ten-target selection | supports | Current GO supports these exact structure identities and typed parthood. Upstream central-pair doublets wording and B-sheath A-tubule relationship conflicts are not adopted as biological facts. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=3055%2C5911; Top-level taxa 3055 and 5911 | supports | Chlamydomonas reinhardtii and Tetrahymena thermophila identities resolve. Authority identity alone is not occurrence evidence. |
| adapter | /private/tmp/csm-review-20261011T084242Z/adapter.log | context_only | The live 28-dataset iModulonDB inventory includes neither reviewed organism. No applicable dataset search; absence is not negative biological evidence. |
| ma | DOI:10.1016/j.cell.2019.09.030; Results and captions: internal repeat, MIP network, luminal coating, ribbon and junctions; sample preparation and model-building Methods | supports | Primary Chlamydomonas cryo-EM resolves A/B tubules and interconnected luminal MIP networks; generic native structure-level claims do not assert exhaustive molecular composition. |
| owa | DOI:10.1038/s41467-019-09051-x; Results FAP45/FAP52 localization, mutant tomography, HS-AFM and FAP20 double-mutant tests; Figures 3-7 captions | supports | Primary Chlamydomonas experiments support B-lumen MIP localization and bounded doublet-stabilization claims, distinct from universal essentiality. |
| nicastro-abstract | DOI:10.1126/science.1128618; Exact DOI/PMID metadata and primary abstract | supports | The paper describes frozen Chlamydomonas and sea-urchin axoneme structures and proposes a dynein-sliding model. |
| nicastro-full | DOI:10.1126/science.1128618; Author-uploaded full text: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography ; introductory architecture, specimen preparation, mechanistic interpretation and Figures 1-5 captions | supports | Actual author-uploaded article text was read through the browser. Frozen, ATP-free Chlamydomonas architecture and the proposed force-generation interpretation support the coarse native structural model; no active-beating experiment is inferred. |

## Limits And Additional Notes

- Same-agent review, not independent human sign-off; no scientific-status promotion.
- Full baseline QC was verified in exact-revision CI; local scoped/global checks have their actual namespace and label skips retained. Automated validation is not scientific coverage.
- No raw micrograph, map, movie or experimental-data reanalysis; unresolved protein-family mappings and stoichiometries are not certified.
- Three Europe PMC XML requests returned errors; corresponding official PMC HTML was inspected. Nicastro full text was read through an author-uploaded browser page, not a downloaded publisher PDF.
- Current GO source conflicts affecting central-pair definition and B-inner-sheath typed placement are retained as authority limitations, not silently substituted for primary-supported native biology.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T085523Z-axonemal_doublet_microtubule-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Axonemal doublet microtubule: scientific record review'
started_at: '2026-10-11T08:43:44Z'
finished_at: '2026-10-11T08:55:23Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent source and record assessment; not independent human
    scientific sign-off.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole native record reviewed; one minor discussion-provenance defect saved
  before separately authorized curation.
source:
  git_revision: d01b9d412c3f5a0d08b0f2fab6d08b33a5fe88ab
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
  - path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
    sha256: ce35e4855b506178485b229b515c89a717ddee0a5a9d26fff88ba991fac5b06b
    role: context
  - path: data/structures/cytoskeleton/axonemal_central_pair_projection.yaml
    sha256: c13cdaf4797fb4905470b312cf1c024005f77aa311ab3d62dd4d59c0a6d9b916
    role: context
  - path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    sha256: 6a44e0a145c3ba58c9649ca75093614cd97001a451021dc2becf8c170824b270
    role: target
  - path: data/structures/cytoskeleton/axonemal_dynein_complex.yaml
    sha256: 9158b3b827892de2d3f14320353af5fbd6ef8ef3cfae114687b9e6725f7ce44e
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    sha256: 480cd29d1f2e87c07c19dd8d60e50768cdcce29223b28ce2df1d4c956dc46282
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_junction.yaml
    sha256: 1f4100cb6277d96af447d994d4f9749df7ae5038cd507dc5da3c833faf498013
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_sheath.yaml
    sha256: 2b964f29a3a4cd6b72ad12c06c411a2df5e19969033b52bfd27b33148b08576d
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_outer_junction.yaml
    sha256: b9147816869cf7d715ba4bbe9ae68ea2a2af15001c05ad83e539b74bbe2a7933
    role: context
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
    sha256: 68b8a96e0ef8454f126a22a7a5b3df710fec63ea67b6b7978ff7064852d5060d
    role: context
  - path: data/structures/cytoskeleton/axonemal_nexin_link.yaml
    sha256: 4415aab73c5b36e1ae80542d11995651b8b280dbba975dbb1d993cb2b5c6b90c
    role: context
  - path: data/structures/cytoskeleton/axoneme.yaml
    sha256: bed33d25739148035e6e753a535ec90e7d3f7c16f246d6d79a074609156c1536
    role: context
  - path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    sha256: 438f1274f334f407b89cb2f89c27796d3c909385e3535e57151f4d07fbe9c160
    role: context
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
  - path: history/records/axonemal_doublet_microtubule/2026-09-23T114752Z-codex-f4cd89.yaml
    sha256: a532ad52991a89a1cda741670bd9fab3b0a3ca034b4ea72cd21fc42b19833fa8
    role: context
  - path: history/records/axonemal_doublet_microtubule/2026-09-23T115733Z-codex-808f57.yaml
    sha256: cda5ee6650b99395efc49d61eabe189203766f353678400abdab94ae16ceb757
    role: context
  - path: history/records/axonemal_doublet_microtubule/2026-09-23T130217Z-codex-00d04c.yaml
    sha256: f8dd225939ead91563982843cfe411a9e3666500d55496dc09e80139cb7b431a
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
- target_id: GO:0097545
  path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
  label: axonemal doublet microtubule
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    role: maintained scientific record
scope:
  description: Whole native YAML, every causal edge, identity and typed hierarchy,
    composition, taxonomy, functions, optional resources, discussion lifecycle and
    both history surfaces.
  selection: One exact target in the 909-record review goal; adjacent records are
    supporting context, not additional certified reviews.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0097545
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic validation passed; scientific claim assessment is separate.
  scope_note: 2026-10-11T08:44:11Z to 2026-10-11T08:44:14Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic validation passed; scientific claim assessment is separate.
  scope_note: 2026-10-11T08:44:14Z to 2026-10-11T08:44:19Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    --report /private/tmp/csm-review-20261011T084242Z/axonemal_doublet_microtubule-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets asserted. Paraphrased claim support was inspected
    separately.
  scope_note: 2026-10-11T08:44:19Z to 2026-10-11T08:44:43Z; log SHA-256 8382e8c9525a451b2f9cdf0fb8e2fede4154cb09b7c7e823eaff9c5c31939116
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic validation passed; scientific claim assessment is separate.
  scope_note: 2026-10-11T08:49:13Z to 2026-10-11T08:49:32Z; log SHA-256 a334cb99b68bf9bff7dc6f7cbf42e376c52117e8773d42811c4f87cdf4e017da
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T08:49:32Z to 2026-10-11T08:51:19Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic validation passed; scientific claim assessment is separate.
  scope_note: 2026-10-11T08:51:19Z to 2026-10-11T08:51:43Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4014\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T08:51:43Z to 2026-10-11T08:52:40Z; log SHA-256 ee1c5f2e78a2d29fcb6781a8ecd722934376595042d2cc261b4465b361d19b79
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic validation passed; scientific claim assessment is separate.
  scope_note: 2026-10-11T08:52:40Z to 2026-10-11T08:54:22Z; log SHA-256 82b4ed449d60e1c91478d89ecc61151db2576619a6c70b3f993966645a35fdb6
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic validation passed; scientific claim assessment is separate.
  scope_note: 2026-10-11T08:54:22Z to 2026-10-11T08:54:22Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: qc
  name: Exact-baseline CI full QC and review contract
  status: passed
  required: true
  target_ids:
  - GO:0097545
  command: gh run view 38125277347 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  expected_exit_code: 0
  summary: Full native QC (840 passed, 3 skipped) and review-contract gates passed
    on the exact captured baseline. This is a verified CI receipt, not a fresh local
    QC execution.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38125277347;
    log SHA-256 81088c4381fa395d4cbe8386a0dc7e302d47e650bbac9dde14238e2dc869afc6
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
  accessed_at: '2026-10-11T08:55:23Z'
  snapshot_sha256: 6a44e0a145c3ba58c9649ca75093614cd97001a451021dc2becf8c170824b270
  support: context_only
  summary: Entire native YAML read; formal input capture preceded assessment, though
    initial reading preceded capture.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T08:55:23Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Discussion rationale must be appended, not replaced; dates and resolved
    lifecycle must be preserved.
- evidence_id: history
  kind: record_content
  reference: /private/tmp/csm-review-20261011T084242Z/axonemal_doublet_microtubule-discussion-history.json
  accessed_at: '2026-10-11T08:55:23Z'
  snapshot_sha256: f75d34501145fe70be0464bb6742aec4e136896cf2eeed955bd6713409d4d69b
  support: context_only
  summary: All committed revisions of this target inspected, including full discussion
    objects and curation events.
- evidence_id: context
  kind: validation
  reference: /private/tmp/csm-review-20261011T084242Z/context-read.log
  accessed_at: '2026-10-11T08:55:23Z'
  snapshot_sha256: 8466ad636fabe3c2dbacb9d558bcf8c0c730dc79fbc31cba6398e99ab9912815
  support: context_only
  summary: Maintained neighboring structures and append-only repository history inspected
    for current boundaries and earlier corrections.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T084242Z/exact-target-predecessors.json
  accessed_at: '2026-10-11T08:55:23Z'
  snapshot_sha256: 19d6b776c97937ed352ae43a2425b13c15aafca39b6ff6d45cd3a74be34e1d1f
  support: context_only
  summary: Ignored-inclusive recursive structured-review target search found no exact-target
    predecessor; references to the term in another review are not target coverage.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0001534,GO:0003352,GO:0005858,GO:0005879,GO:0005881,GO:0005930,GO:0005931,GO:0030286,GO:0036156,GO:0036157,GO:0051012,GO:0097540,GO:0097545,GO:0097649,GO:0097650,GO:0160110,GO:0160111,GO:0160112,GO:0160113,GO:0160114,GO:0160115,GO:1990716,GO:1990718,GO:1990719,GO:1990720
  locator: Exact term definitions, aspect, obsolescence, synonyms and typed reverse
    children for all 25 asserted GO identifiers in the ten-target selection
  accessed_at: '2026-10-11T08:43:40Z'
  snapshot_sha256: 93097af320ac100c3e65e327a67a93a3c21ade82457eb1ad668d05cd6ab52345
  support: supports
  summary: Current GO supports these exact structure identities and typed parthood.
    Upstream central-pair doublets wording and B-sheath A-tubule relationship conflicts
    are not adopted as biological facts.
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=3055%2C5911
  locator: Top-level taxa 3055 and 5911
  accessed_at: '2026-10-11T08:43:41Z'
  snapshot_sha256: 8f418aa735d12049673dbd5bee57296b8ec2586d6d63ddb63c93e415ac0fe3d7
  support: supports
  summary: Chlamydomonas reinhardtii and Tetrahymena thermophila identities resolve.
    Authority identity alone is not occurrence evidence.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T084242Z/adapter.log
  accessed_at: '2026-10-11T08:55:23Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: The live 28-dataset iModulonDB inventory includes neither reviewed organism.
    No applicable dataset search; absence is not negative biological evidence.
- evidence_id: ma
  kind: primary_source
  reference: DOI:10.1016/j.cell.2019.09.030
  locator: 'Results and captions: internal repeat, MIP network, luminal coating, ribbon
    and junctions; sample preparation and model-building Methods'
  accessed_at: '2026-10-11T08:44:05Z'
  snapshot_sha256: 17637049254d5327fcfb7760f454e09ae5ef5b19b94a0815af82e94055859b91
  support: supports
  summary: Primary Chlamydomonas cryo-EM resolves A/B tubules and interconnected luminal
    MIP networks; generic native structure-level claims do not assert exhaustive molecular
    composition.
- evidence_id: owa
  kind: primary_source
  reference: DOI:10.1038/s41467-019-09051-x
  locator: Results FAP45/FAP52 localization, mutant tomography, HS-AFM and FAP20 double-mutant
    tests; Figures 3-7 captions
  accessed_at: '2026-10-11T08:43:50Z'
  snapshot_sha256: 63663cccd58bd5988920296148f9d528b4311841c3be7033a6c442d94bb18aa1
  support: supports
  summary: Primary Chlamydomonas experiments support B-lumen MIP localization and
    bounded doublet-stabilization claims, distinct from universal essentiality.
- evidence_id: nicastro-abstract
  kind: primary_source
  reference: DOI:10.1126/science.1128618
  locator: Exact DOI/PMID metadata and primary abstract
  accessed_at: '2026-10-11T08:44:01Z'
  snapshot_sha256: dc5a628f1cfe67da937413ea897415a623f29682c4fcc83f9a7540d564467a27
  support: supports
  summary: The paper describes frozen Chlamydomonas and sea-urchin axoneme structures
    and proposes a dynein-sliding model.
- evidence_id: nicastro-full
  kind: primary_source
  reference: DOI:10.1126/science.1128618
  locator: 'Author-uploaded full text: https://www.researchgate.net/publication/6871150_The_Molecular_Architecture_of_Axonemes_Revealed_by_Cryoelectron_Tomography
    ; introductory architecture, specimen preparation, mechanistic interpretation
    and Figures 1-5 captions'
  accessed_at: '2026-10-11T08:55:23Z'
  support: supports
  summary: Actual author-uploaded article text was read through the browser. Frozen,
    ATP-free Chlamydomonas architecture and the proposed force-generation interpretation
    support the coarse native structural model; no active-beating experiment is inferred.
assessments:
- assessment_id: biology
  area: evidence
  topic: Identity, hierarchy, composition, species scope, functions and every graph
    edge
  outcome: supported
  target_ids:
  - GO:0097545
  evidence_ids:
  - record
  - go
  - taxa
  - ma
  - owa
  - nicastro-full
  summary: GO:0097545 is the doublet scaffold, not a single tubulin protein or the
    entire axoneme. Six has_part links retain A/B tubules, inner sheath, both junctions
    and ribbon. The generic alpha/beta-tubulin class is conservatively label-only.
    Chlamydomonas nine-doublet and A13/B10 protofilament scope, both tubule parthood
    edges, tubulin polymerization, MIP-mediated stabilization and axoneme containment
    are supported. Owa measures B-lumen stabilization rather than every MIP in every
    species.
- assessment_id: provenance
  area: provenance
  topic: Historical rationale and current task lifecycle
  outcome: concern
  target_ids:
  - GO:0097545
  evidence_ids:
  - record
  - history
  - rules
  - context
  summary: The original rationale at 8b410f98 distinguished the coarse A/B scaffold
    from finer substructures. Four child additions at 1a6f7145, 5b2752fe, 8885f3fc
    and 16734f12 replaced it rather than appending. The current record loses the initial
    scope and intermediate decisions, contrary to the append-only rationale rule.
- assessment_id: resources
  area: completeness
  topic: Optional resources, conservative groundings and status
  outcome: supported
  target_ids:
  - GO:0097545
  evidence_ids:
  - record
  - rules
  summary: No native images, quantitative property measurements, protein/dataset accessions
    or trait links require additional resource verification. Coarse label-only groups
    and acknowledged open molecular tasks are not invented defects. Native status
    remains PROPOSED.
findings:
- finding_id: F1
  issue_key: doublet-microtubule-discussion-rationale-preservation
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Restore the doublet-microtubule discussion rationale history
  description: The original rationale at 8b410f98 distinguished the coarse A/B scaffold
    from finer substructures. Four child additions at 1a6f7145, 5b2752fe, 8885f3fc
    and 16734f12 replaced it rather than appending. The current record loses the initial
    scope and intermediate decisions, contrary to the append-only rationale rule.
  target_ids:
  - GO:0097545
  field_paths:
  - discussions[0].rationale
  evidence_ids:
  - record
  - history
  - rules
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: A bounded source-attribution or discussion-provenance defect;
    the biological identity and structure boundaries remain supported.
actions:
- action_id: A1
  description: Restore the doublet-microtubule discussion rationale history
  finding_ids:
  - F1
  target_ids:
  - GO:0097545
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    role: maintained scientific record
  acceptance_checks:
  - Restore the exact original rationale and every distinct later version, with revision-labelled
    historical context rather than current absence claims.
  - Preserve current discussion IDs, narrowed prompts, live attachments, original
    posed dates and authors, statuses, all has_part links, all graph edges and earlier
    scientific scope corrections.
  - Use the guarded writer, append Codex curation and EDIT history, preserve PROPOSED,
    prior history/reviews and unrelated records, regenerate pages, and pass focused
    regressions and native QC.
limitations:
- Same-agent review, not independent human sign-off; no scientific-status promotion.
- Full baseline QC was verified in exact-revision CI; local scoped/global checks have
  their actual namespace and label skips retained. Automated validation is not scientific
  coverage.
- No raw micrograph, map, movie or experimental-data reanalysis; unresolved protein-family
  mappings and stoichiometries are not certified.
- Three Europe PMC XML requests returned errors; corresponding official PMC HTML was
  inspected. Nicastro full text was read through an author-uploaded browser page,
  not a downloaded publisher PDF.
- Current GO source conflicts affecting central-pair definition and B-inner-sheath
  typed placement are retained as authority limitations, not silently substituted
  for primary-supported native biology.
```
