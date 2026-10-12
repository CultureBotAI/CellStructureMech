# Ciliary basal body: scientific structure review

- Review: 20261012T011544Z-ciliary_basal_body-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-12T01:08:30Z
- Finished UTC: 2026-10-12T01:15:44Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Whole native record reviewed; two major findings in typed parentage and categorical component essentiality saved before curation.

## Scope And Provenance

Whole native record, every component and graph edge, identity, taxa, function, physical property, discussion, optional surfaces and both histories.

Selection: One exact target in the909-record review goal; no sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 297b9f85ce552f6e07d75f3a086121e59161bb76.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0036064 | data/structures/cytoskeleton/ciliary_basal_body.yaml | maintained | ciliary basal body |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:0036064 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:0036064 | id↔label correspondence summary:<br>          OK_CANONICAL: 3545<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:0036064 | resolver control: every resolver accepts a known id and rejects a fabricated one<br><br>identifier liveness summary:<br>  OK             4016<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:0036064 | Actual deterministic check passed; scientific support assessed separately. |
| Exact-baseline native merge-group QC | passed | True | GO:0036064 | Live exact-base QC and complete log verified;967 tests passed and3 existing skips. Not a fresh full local QC run. |

## Scientific And Domain Assessments

### Exact identity, synonyms and organelle boundary

identity: supported. Targets: GO:0036064.

Exact GO0036064 identity is correct, including broad basal-body synonym and precise ciliary-body synonyms. OTHER avoids asserting one protein. The structure is not a bacterial basal body, the whole cilium or the entire cytoskeleton.

### Constituent roles, taxa, function and all three graph edges

evidence: supported. Targets: GO:0036064.

Triplet blades and cartwheel are supported normal structural constituents. Chlamydomonas occurrence/example and bounded cilium-assembly function are supported. Three NONMECHANISTIC graph edges describe normal cartwheel organization, wall formation and axoneme nucleation; none establishes absolute component essentiality. Taxonomy is not expanded beyond the existing species.

### Use the verified microtubule-organizing-center parent

grounding: concern. Targets: GO:0036064.

parent_structures currently asserts that a ciliary basal body is a GO:0005856 cytoskeleton, the whole cellular framework. The inspected typed OAK relationship and live QuickGO child relation instead give is_a GO:0005815 microtubule organizing center. Replace the incorrect class without changing exact GO0036064 identity or its cilium parthood.

### Qualify structural essentiality beyond normal architecture

evidence: concern. Targets: GO:0036064.

Both microtubule_triplets and cartwheel are marked ESSENTIAL, which the native schema defines as no structure formation without the component. Their cited normal morphology and Bld10 localization/null results do not establish that categorical whole-substructure requirement. UNI3 primary evidence retains mutant basal bodies with proximal doublets, while SAS6-null primary abstract retains variable-triplet centrioles after loss of the central cartwheel part. These findings warrant uncertainty, not a categorical opposite: complete absence of all triplet/cartwheel material in a functioning ciliary basal body is not demonstrated, and spoke tips can remain. Set both flags UNKNOWN with assertion-local source and boundary notes; explicitly scope the nine-triplet property and assembly graph to normal wild-type architecture.

### Optional resources, grounding TODO, histories and status

completeness: supported. Targets: GO:0036064.

Open source-neutral substructure grounding task remains legitimate; the local minted cartwheel does not prove an exact source-neutral identity. No optional image, dataset, trait or pathway link is fabricated. Original taxonomy correction and both histories remain intact; status stays PROPOSED.

## Findings

### F1: Use the verified microtubule-organizing-center parent

major / open / confirmed; issue key: ciliary-basal-body-mtoc-parent.

parent_structures currently asserts that a ciliary basal body is a GO:0005856 cytoskeleton, the whole cellular framework. The inspected typed OAK relationship and live QuickGO child relation instead give is_a GO:0005815 microtubule organizing center. Replace the incorrect class without changing exact GO0036064 identity or its cilium parthood.

### F2: Qualify structural essentiality beyond normal architecture

major / open / confirmed; issue key: ciliary-basal-body-substructure-essentiality.

Both microtubule_triplets and cartwheel are marked ESSENTIAL, which the native schema defines as no structure formation without the component. Their cited normal morphology and Bld10 localization/null results do not establish that categorical whole-substructure requirement. UNI3 primary evidence retains mutant basal bodies with proximal doublets, while SAS6-null primary abstract retains variable-triplet centrioles after loss of the central cartwheel part. These findings warrant uncertainty, not a categorical opposite: complete absence of all triplet/cartwheel material in a functioning ciliary basal body is not demonstrated, and spoke tips can remain. Set both flags UNKNOWN with assertion-local source and boundary notes; explicitly scope the nine-triplet property and assembly graph to normal wild-type architecture.

## Recommended Actions And Acceptance Checks

### A1

Use the verified microtubule-organizing-center parent

- Set parent_structures to the verified GO:0005815 class and cite its typed relation; preserve part_of GO:0005929 and exact identity.
- Use guarded writer and actual Codex curation event; append one EDIT history with exact changed sections and both issue links.
- Preserve all old histories, discussions and PROPOSED status; do not change other native records.
- Add focused regressions, regenerate the changed semantic vector/products and pass full native gates; save exact-lineage supported dispositions.

### A2

Qualify structural essentiality beyond normal architecture

- Set the two essentiality fields UNKNOWN, not unsupported DISPENSABLE; attach inspected primary citations and exact mutant/partial-loss limitations to the relevant component.
- Keep normal constituent roles and all three graph relationships; make the count context and graph scope explicitly wild-type, without equating mutant morphology with demonstrated complete functional loss or normal function.
- Use guarded writer and actual Codex curation event; append one EDIT history with exact changed sections and both issue links.
- Preserve all old histories, discussions and PROPOSED status; do not change other native records.
- Add focused regressions, regenerate the changed semantic vector/products and pass full native gates; save exact-lineage supported dispositions.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/ciliary_basal_body.yaml | context_only | Whole native YAML reread and hash-verified before findings. |
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

## Limits And Additional Notes

- Same-agent whole-record assessment, not independent human approval or raw-data reanalysis.
- SAS6 source is primary abstract only; Silflow2001 has metadata/PMC landing only and attempted PDF returned HTML. UNI3 primary sections and two figures, Bld10 main/captions, and both full review main texts were inspected at the stated scopes.
- UNI3 may retain a functional nucleation requirement; SAS6 central-part loss is not demonstrated removal of all cartwheel material. UNKNOWN preserves these uncertainties and is not a dispensability conclusion.
- Exact-base QC is verified live native CI; fresh scoped/global checks run separately. Namespace/no-adapter and existing test skips remain explicit.
- Bounded ontology searches do not prove global absence. Expression-module data cannot establish ultrastructural component necessity.
- The other three fiber records have separate review accounting; this issue-only bundle does not certify them.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261012T011544Z-ciliary_basal_body-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Ciliary basal body: scientific structure review'
started_at: '2026-10-12T01:08:30Z'
finished_at: '2026-10-12T01:15:44Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent whole-record and source review; not independent human
    approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Whole native record reviewed; two major findings in typed parentage and categorical
  component essentiality saved before curation.
source:
  git_revision: 297b9f85ce552f6e07d75f3a086121e59161bb76
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
    sha256: 8f80489e9683ac36bb07ed5c1c435a1627df5e71c9458f1fcc1f842d65a93128
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
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: pages/structures/cytoskeleton/ciliary_basal_body.html
    sha256: 0d932c9c442d588d1b32b023a79494841fcf15ec2542906e0c2aa8c964207298
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
  description: Whole native record, every component and graph edge, identity, taxa,
    function, physical property, discussion, optional surfaces and both histories.
  selection: One exact target in the909-record review goal; no sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:0036064
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/ciliary_basal_body.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T01:08:44Z to 2026-10-12T01:08:46Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/ciliary_basal_body.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T01:08:46Z to 2026-10-12T01:08:50Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/ciliary_basal_body.yaml
    --report /private/tmp/csm-review-20261012T010700Z/ciliary_basal_body-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-12T01:08:50Z to 2026-10-12T01:09:07Z; log SHA-256 474e0a9301abb992e24f80b238f8b519692cfe989a846e70797ac9c3524c7e86
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T01:10:24Z to 2026-10-12T01:10:38Z; log SHA-256 366443aee9a0bb48ec439583d63f969bf2625f5f7c0147eecbb4e6bc03dab6b9
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
  scope_note: 2026-10-12T01:10:38Z to 2026-10-12T01:12:51Z; log SHA-256 459523b233cf29c593d6ebe49a38d5ed4484b1f98496dc47ea4fdc17be729286
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
  scope_note: 2026-10-12T01:12:51Z to 2026-10-12T01:13:15Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
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
    \ one\n\nidentifier liveness summary:\n  OK             4016\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-12T01:13:15Z to 2026-10-12T01:14:03Z; log SHA-256 f38fdf2889286b712ede050fc9d6de36ecb8830b57fbc4dfbf38421c176168c8
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-12T01:14:03Z to 2026-10-12T01:15:24Z; log SHA-256 7c64a24aaea378fb6f73c2890b64aa92b4e617e3afb8b864b8ee20fe9fed7a11
- check_id: baseline-qc
  name: Exact-baseline native merge-group QC
  status: passed
  required: true
  target_ids:
  - GO:0036064
  command: gh run view 38190063884 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  summary: Live exact-base QC and complete log verified;967 tests passed and3 existing
    skips. Not a fresh full local QC run.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38190063884;
    log SHA256 e046c82f65bae173205c7b64a398c77e9fb4677546aa047b182b9910a1de4c0b
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_basal_body.yaml
  accessed_at: '2026-10-12T01:15:44Z'
  snapshot_sha256: 8f80489e9683ac36bb07ed5c1c435a1627df5e71c9458f1fcc1f842d65a93128
  support: context_only
  summary: Whole native YAML reread and hash-verified before findings.
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
assessments:
- assessment_id: identity
  area: identity
  topic: Exact identity, synonyms and organelle boundary
  outcome: supported
  target_ids:
  - GO:0036064
  evidence_ids:
  - record
  - go
  - mtoc
  summary: Exact GO0036064 identity is correct, including broad basal-body synonym
    and precise ciliary-body synonyms. OTHER avoids asserting one protein. The structure
    is not a bacterial basal body, the whole cilium or the entire cytoskeleton.
- assessment_id: biology
  area: evidence
  topic: Constituent roles, taxa, function and all three graph edges
  outcome: supported
  target_ids:
  - GO:0036064
  evidence_ids:
  - record
  - go
  - taxon
  - bld10
  - review2016
  - review2018
  summary: Triplet blades and cartwheel are supported normal structural constituents.
    Chlamydomonas occurrence/example and bounded cilium-assembly function are supported.
    Three NONMECHANISTIC graph edges describe normal cartwheel organization, wall
    formation and axoneme nucleation; none establishes absolute component essentiality.
    Taxonomy is not expanded beyond the existing species.
  dimensions:
  - name: evidence-tier
    value: Primary Bld10 full text; UNI3 relevant full text; SAS6 primary abstract;
      secondary reviews
    definition: Different source tiers and mutant-specific boundaries remain explicit;
      no primary full-text claim for SAS6/Silflow.
    evidence_ids:
    - bld10
    - uni3
    - sas6
    - review2016
    - review2018
  - name: experimental-boundary
    value: Normal architecture versus mutant formation versus functional nucleation
    definition: Malformed structures, partial substructure loss and organismal viability
      do not establish universal essentiality or dispensability.
    evidence_ids:
    - uni3
    - uni3-caveat
    - sas6
    - schema
- assessment_id: finding-1
  area: grounding
  topic: Use the verified microtubule-organizing-center parent
  outcome: concern
  target_ids:
  - GO:0036064
  evidence_ids:
  - record
  - rules
  - go-relations
  - mtoc
  summary: parent_structures currently asserts that a ciliary basal body is a GO:0005856
    cytoskeleton, the whole cellular framework. The inspected typed OAK relationship
    and live QuickGO child relation instead give is_a GO:0005815 microtubule organizing
    center. Replace the incorrect class without changing exact GO0036064 identity
    or its cilium parthood.
- assessment_id: finding-2
  area: evidence
  topic: Qualify structural essentiality beyond normal architecture
  outcome: concern
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
  summary: 'Both microtubule_triplets and cartwheel are marked ESSENTIAL, which the
    native schema defines as no structure formation without the component. Their cited
    normal morphology and Bld10 localization/null results do not establish that categorical
    whole-substructure requirement. UNI3 primary evidence retains mutant basal bodies
    with proximal doublets, while SAS6-null primary abstract retains variable-triplet
    centrioles after loss of the central cartwheel part. These findings warrant uncertainty,
    not a categorical opposite: complete absence of all triplet/cartwheel material
    in a functioning ciliary basal body is not demonstrated, and spoke tips can remain.
    Set both flags UNKNOWN with assertion-local source and boundary notes; explicitly
    scope the nine-triplet property and assembly graph to normal wild-type architecture.'
- assessment_id: provenance
  area: completeness
  topic: Optional resources, grounding TODO, histories and status
  outcome: supported
  target_ids:
  - GO:0036064
  evidence_ids:
  - record
  - rules
  - history
  - reading
  - neighbor
  summary: Open source-neutral substructure grounding task remains legitimate; the
    local minted cartwheel does not prove an exact source-neutral identity. No optional
    image, dataset, trait or pathway link is fabricated. Original taxonomy correction
    and both histories remain intact; status stays PROPOSED.
findings:
- finding_id: F1
  issue_key: ciliary-basal-body-mtoc-parent
  category: grounding
  severity: major
  status: open
  certainty: confirmed
  title: Use the verified microtubule-organizing-center parent
  description: parent_structures currently asserts that a ciliary basal body is a
    GO:0005856 cytoskeleton, the whole cellular framework. The inspected typed OAK
    relationship and live QuickGO child relation instead give is_a GO:0005815 microtubule
    organizing center. Replace the incorrect class without changing exact GO0036064
    identity or its cilium parthood.
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
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Wrong typed hierarchy or unsupported categorical assembly
    requirement changes structured scientific meaning; identity and normal constituent
    membership remain supported.
- finding_id: F2
  issue_key: ciliary-basal-body-substructure-essentiality
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Qualify structural essentiality beyond normal architecture
  description: 'Both microtubule_triplets and cartwheel are marked ESSENTIAL, which
    the native schema defines as no structure formation without the component. Their
    cited normal morphology and Bld10 localization/null results do not establish that
    categorical whole-substructure requirement. UNI3 primary evidence retains mutant
    basal bodies with proximal doublets, while SAS6-null primary abstract retains
    variable-triplet centrioles after loss of the central cartwheel part. These findings
    warrant uncertainty, not a categorical opposite: complete absence of all triplet/cartwheel
    material in a functioning ciliary basal body is not demonstrated, and spoke tips
    can remain. Set both flags UNKNOWN with assertion-local source and boundary notes;
    explicitly scope the nine-triplet property and assembly graph to normal wild-type
    architecture.'
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
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Wrong typed hierarchy or unsupported categorical assembly
    requirement changes structured scientific meaning; identity and normal constituent
    membership remain supported.
actions:
- action_id: A1
  description: Use the verified microtubule-organizing-center parent
  finding_ids:
  - F1
  target_ids:
  - GO:0036064
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained scientific record
  acceptance_checks:
  - Set parent_structures to the verified GO:0005815 class and cite its typed relation;
    preserve part_of GO:0005929 and exact identity.
  - Use guarded writer and actual Codex curation event; append one EDIT history with
    exact changed sections and both issue links.
  - Preserve all old histories, discussions and PROPOSED status; do not change other
    native records.
  - Add focused regressions, regenerate the changed semantic vector/products and pass
    full native gates; save exact-lineage supported dispositions.
- action_id: A2
  description: Qualify structural essentiality beyond normal architecture
  finding_ids:
  - F2
  target_ids:
  - GO:0036064
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained scientific record
  acceptance_checks:
  - Set the two essentiality fields UNKNOWN, not unsupported DISPENSABLE; attach inspected
    primary citations and exact mutant/partial-loss limitations to the relevant component.
  - Keep normal constituent roles and all three graph relationships; make the count
    context and graph scope explicitly wild-type, without equating mutant morphology
    with demonstrated complete functional loss or normal function.
  - Use guarded writer and actual Codex curation event; append one EDIT history with
    exact changed sections and both issue links.
  - Preserve all old histories, discussions and PROPOSED status; do not change other
    native records.
  - Add focused regressions, regenerate the changed semantic vector/products and pass
    full native gates; save exact-lineage supported dispositions.
limitations:
- Same-agent whole-record assessment, not independent human approval or raw-data reanalysis.
- SAS6 source is primary abstract only; Silflow2001 has metadata/PMC landing only
  and attempted PDF returned HTML. UNI3 primary sections and two figures, Bld10 main/captions,
  and both full review main texts were inspected at the stated scopes.
- UNI3 may retain a functional nucleation requirement; SAS6 central-part loss is not
  demonstrated removal of all cartwheel material. UNKNOWN preserves these uncertainties
  and is not a dispensability conclusion.
- Exact-base QC is verified live native CI; fresh scoped/global checks run separately.
  Namespace/no-adapter and existing test skips remain explicit.
- Bounded ontology searches do not prove global absence. Expression-module data cannot
  establish ultrastructural component necessity.
- The other three fiber records have separate review accounting; this issue-only bundle
  does not certify them.
```
