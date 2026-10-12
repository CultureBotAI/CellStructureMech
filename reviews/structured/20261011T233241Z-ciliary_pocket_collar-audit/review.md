# ciliary pocket collar: evidence and structure review

- Review: 20261011T233241Z-ciliary_pocket_collar-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T23:26:06Z
- Finished UTC: 2026-10-11T23:32:41Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record assessed; observed issue(s) saved before any scientific mutation.

## Scope And Provenance

Whole native YAML including identity, typed relations, every component/function/graph edge, taxon/example, discussions and both history surfaces. Source access limitations retained per paper.

Selection: One exact record within the active 909-record goal; no batch sampling.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base 6b8e8880fd22415798fab889eacb8db10bddead2.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990900 | data/structures/cytoskeleton/ciliary_pocket_collar.yaml | maintained | ciliary pocket collar |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | GO:1990900 | Actual deterministic check passed; scientific support assessed separately. |
| strict | passed | True | GO:1990900 | Actual deterministic check passed; scientific support assessed separately. |
| snippets | passed | True | GO:1990900 | No verbatim snippets; paraphrases assessed separately against inspected text. |
| history | passed | True | GO:1990900 | Actual deterministic check passed; scientific support assessed separately. |
| labels | passed | True | GO:1990900 | id↔label correspondence summary:<br>          OK_CANONICAL: 3545<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | GO:1990900 | Actual deterministic check passed; scientific support assessed separately. |
| curies | passed | True | GO:1990900 | [not exercised] BFO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] CHEBI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] GO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] InterPro: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PATO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] PMID: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] RO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] SO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UO: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver was not exercised<br>  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355 was not exercised<br>resolver control: 14 resolver(s) could not be exercised because their authority was unreachable; the rest accept a known id and reject a fabricated one<br><br>identifier liveness summary:<br>  OK             4016<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | GO:1990900 | Actual deterministic check passed; scientific support assessed separately. |
| Exact-base native merge-group QC | passed | True | GO:1990900 | Exact 6b8e8880 baseline QC success verified from live run metadata and complete log. Not a fresh full local QC run. |

## Scientific And Domain Assessments

### Three constituents, three functions and seven assembly edges

evidence: supported. Targets: GO:1990900.

BILBO1 polymer scaffold and new-FPC/FP requirement are supported in tested procyclic cells. FPC4 binding and localizations are supported, not direct native bridging. BILBO2 binary-domain binding and tripartite interaction model do not assert resolved native stoichiometry. Historical broad-eukaryote distribution removal and split dimer/polymer edges remain correct; unasserted whole-family mappings are genuine unknowns.

### Attach the three-protein occurrence note to an appropriate source

evidence: concern. Targets: GO:1990900.

The T. brucei taxonomic note explicitly names BILBO1/FPC4/BILBO2 but cites the 2016 Perdomo review, which contains neither FPC4 nor BILBO2. The already-cited 2021 Isch primary study supports their T. brucei FPC localization/interaction context.

### Qualify the proposed native FPC4 connection

evidence: concern. Targets: GO:1990900.

FPC4 component.role still categorically says it links the collar to microtubule-associated elements. The primary studies directly establish binding and localization but describe native FPC/MtQ linking as proposed. Historical issue 295 corrected other fields, not this residual role text.

### Identity and structure relationships

grounding: supported. Targets: GO:1990900.

Exact GO structure identity, definition, category/kind and synonym evidence are supported. No single protein is substituted for a structure. Ciliary-pocket parthood is supported; T. brucei protein composition is not generalized to every organism in the GO definition.

### Discussions, optional surfaces and status

completeness: supported. Targets: GO:1990900.

All original inline/repository history and open scope/grounding discussions read. Missing optional stoichiometry, physical measurements, images, datasets, protein examples and trait/pathway links are not defects. PROPOSED is retained. This is a bounded review of represented claims and consequential gaps, not an exhaustive discovery of every later protein or publication.

## Findings

### F1: Attach the three-protein occurrence note to an appropriate source

minor / open / confirmed; issue key: pocket-collar-distribution-citation.

The T. brucei taxonomic note explicitly names BILBO1/FPC4/BILBO2 but cites the 2016 Perdomo review, which contains neither FPC4 nor BILBO2. The already-cited 2021 Isch primary study supports their T. brucei FPC localization/interaction context.

### F2: Qualify the proposed native FPC4 connection

minor / open / confirmed; issue key: pocket-collar-fpc4-linking-scope.

FPC4 component.role still categorically says it links the collar to microtubule-associated elements. The primary studies directly establish binding and localization but describe native FPC/MtQ linking as proposed. Historical issue 295 corrected other fields, not this residual role text.

## Recommended Actions And Acceptance Checks

### A1

Attach the three-protein occurrence note to an appropriate source

- Use the 2021 primary citation with a bounded T. brucei component-localization note, or narrow the note to the existing 2016 source.
- Preserve species occurrence and avoid universal strain/life-stage assembly claims.
- Guarded writer; append only actual Codex curation and EDIT history; preserve PROPOSED, all original events/discussions and historical bundles.
- Regenerate target products, pass focused regressions and native gates; save an exact-lineage successor.

### A2

Qualify the proposed native FPC4 connection

- State measured BILBO1 interaction/localization and mark the native linking role as proposed.
- Preserve the already-corrected function and graph evidence, rather than reopening their historical fix.
- Guarded writer; append only actual Codex curation and EDIT history; preserve PROPOSED, all original events/discussions and historical bundles.
- Regenerate target products, pass focused regressions and native gates; save an exact-lineage successor.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/ciliary_pocket_collar.yaml | context_only | Entire original native record read and unchanged captured bytes verified. |
| rules | docs/CURATION.md | context_only | Typed parthood, assertion-local evidence and assembly-only essentiality rules. |
| schema | src/cellstructuremech/schema/cellstructuremech.yaml | context_only | Essentiality concerns structure formation, possibly defectively; gene symbols are metadata, not component identity. |
| reading | /private/tmp/csm-review-20261011T232800Z/reading-checkpoint.json | context_only | Preserved source reading chronology and explicit abstract/full-text/visual limits. |
| predecessors | /private/tmp/csm-review-20261011T232800Z/predecessors.json | context_only | Ignored-inclusive canonical bundle scan; no exact-target predecessor. |
| go-relations | /private/tmp/csm-review-20261011T222903Z/next-go-relations.log | context_only | Source-native OAK typed relations inspected, independently consistent with QuickGO terms. |
| context | /private/tmp/csm-review-20261011T232800Z/context-search.log | context_only | Identifier/label/slug search includes ignored and hidden repository files, excluding Git internals and dependency trees. |
| adapter | /private/tmp/csm-review-20261011T222903Z/next-adapter.log | context_only | All 28 iModulonDB dataset rows inspected; no matching Trypanosoma dataset. Not negative biological evidence. |
| history-0 | history/records/ciliary_pocket_collar/2026-09-09T193650Z-codex-2ade5b.yaml | context_only | Entire original append-only history read; preserve historical actors and resolved issue scope. |
| history-1 | history/records/ciliary_pocket_collar/2026-09-10T013812Z-codex-d38ed3.yaml | context_only | Entire original append-only history read; preserve historical actors and resolved issue scope. |
| history-2 | history/records/ciliary_pocket_collar/2026-09-10T014219Z-codex-e70e45.yaml | context_only | Entire original append-only history read; preserve historical actors and resolved issue scope. |
| dedup-pocket-collar-distribution-citation | /private/tmp/csm-review-20261011T232800Z/dedup-pocket-collar-distribution-citation.log | context_only | All-state exact-key GitHub issue search checked before creation. Any earlier sandbox network failure remains in separate receipt. |
| dedup-pocket-collar-fpc4-linking-scope | /private/tmp/csm-review-20261011T232800Z/dedup-pocket-collar-fpc4-linking-scope.log | context_only | All-state exact-key GitHub issue search checked before creation. Any earlier sandbox network failure remains in separate receipt. |
| paper-3 | https://pmc.ncbi.nlm.nih.gov/articles/PMC4156054/; DOI:10.1074/jbc.M114.554659; Results, Discussion, Experimental Procedures, nine captions | supports | Purified BILBO1 domain analysis supports antiparallel dimers and leucine-zipper-dependent filament assembly. Molecular collar geometry remains a model; domain crystal/model distinctions retained. |
| paper-4 | https://pmc.ncbi.nlm.nih.gov/articles/PMC7008359/; DOI:10.1074/jbc.RA119.010768; Results, Discussion, Experimental Procedures, Table 1 and seven captions | supports | BILBO1 NTD crystal structure and purified-domain binding map FPC4 recognition; U2OS is heterologous. Native linkage to the microtubule quartet is proposed, not directly proven. |
| paper-11 | https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060105; DOI:10.1371/journal.pbio.0060105; Results, Discussion, Methods and seven captions | supports | BILBO1 RNAi blocks new FPC/FP assembly in tested procyclic cells while the old collar persists. Bloodstream lethality has a different morphology; genomic source strain is not every assay strain. |
| paper-12 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4379179/fullTextXML; DOI:10.1371/journal.ppat.1004654; abstract, author summary, all Results, Discussion, Methods, seven captions and five tables | supports | Purified calcium binding and coiled-coil-driven polymers are supported. Targeting assays retain endogenous BILBO1; dominant-negative mutants are not nulls and calcium regulation of native geometry remains a model. |
| paper-13 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5683654/fullTextXML; DOI:10.1371/journal.ppat.1006710; entire Results, Discussion, Methods and eight captions | supports | FPC4 binds BILBO1 domains and microtubules; endogenous localization, overexpression and heterologous assays differ. Physical bridging of the native MtQ is proposed. Partial RNAi and failed knockout attempts do not establish dispensability or essentiality. |
| paper-14 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8360560/fullTextXML; DOI:10.1371/journal.ppat.1009329; entire Results, Discussion, Conclusion, Methods, eight captions and Table 1 | supports | BILBO2/Tb927.6.3240 is a T. brucei FPC component and partner of BILBO1/FPC4. Binary-domain structure, interaction tests and heterologous coexpression support the tripartite model, not an atomic native whole-collar structure or universal stoichiometry. |
| paper-16 | https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4810094/fullTextXML; DOI:10.3390/cells5010009; abstract and all main sections/captions | supports | Review supports BILBO1 and collar architecture, but contains neither FPC4 nor BILBO2. It cannot support a claim explicitly naming those later-characterized proteins. This is a literature review, not a new primary experiment. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005856,GO%3A0020016,GO%3A0120119,GO%3A0120120,GO%3A0120269,GO%3A0140535,GO%3A1990900; Exact GO IDs, definitions, synonyms and child relation types | supports | Identity terms denote the requested structures; GO lexical synonymy is not an assertion that all historical protein cohorts are physically identical. |
| taxon | https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691; TaxId/name/rank | supports | T. brucei species identity verified; experiments remain limited to named laboratory forms/lines. |
| bilbo-domain | https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040747/; Accession/type/domain identity and representative BILBO2-FPC4 structure | supports | These are N-terminal domains, not exact whole BILBO protein families; label-only decisions remain appropriate. |
| bilbo-pfam | https://www.ebi.ac.uk/interpro/api/entry/pfam/PF18281/; Accession/type/domain identity and representative BILBO2-FPC4 structure | supports | These are N-terminal domains, not exact whole BILBO protein families; label-only decisions remain appropriate. |
| prior-295 | /private/tmp/csm-review-20261011T222903Z/next-issue-295.log | context_only | Closed issue narrowed FPC4 function/graph to binding and localization; current component role remains broader. |

## Limits And Additional Notes

- Same-agent scientific review, not independent human approval or raw-data reanalysis.
- Original source access dates/hashes are retained from the read-ahead phase. Actual reading scope is recorded per source; separate supplements, movies and raw experiments were not reviewed.
- 2009 MORN1, 1999 FAZ assembly and 2011 CC2D remain primary-abstract-only for narrow supported claims; full-text inaccessibility is not asserted globally. Other material sources have the inspected main-text scope stated in evidence.
- The 2008 FAZ1 Figure 4 is visually inspected only for the FAZ review; other main figures were read as captions, not certified pixel-level reanalyses. No source media adopted.
- Exact baseline full QC is verified CI; fresh local schema/strict/history/label/reference/trait/review checks are separate. Existing identifier-policy/no-adapter and test skips remain explicit.
- No exact whole-family accession is invented and no absence from iModulonDB is biological evidence. Neighboring flagellar pocket and newer-publication leads are not counted as completed reviews.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T233241Z-ciliary_pocket_collar-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'ciliary pocket collar: evidence and structure review'
started_at: '2026-10-11T23:26:06Z'
finished_at: '2026-10-11T23:32:41Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent whole-record and primary-source assessment, not independent
    human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record assessed; observed issue(s) saved before any scientific
  mutation.
source:
  git_revision: 6b8e8880fd22415798fab889eacb8db10bddead2
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
  - path: data/structures/cytoskeleton/bilobe_structure.yaml
    sha256: 19e9083dd8c398e9ab49a74949bb53d0e0c0c16058d800c87619da78ebd0885f
    role: context
  - path: data/structures/cytoskeleton/ciliary_centrin_arm.yaml
    sha256: 076a14eebce9d80acada8668f1ff0c82f7d2949a7ce0a0ae76a5478fca4a1a96
    role: context
  - path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    sha256: abefa0652c7dfae6a06cd962f7c0805dd526c230f87180b35c408e076bd6a9b4
    role: target
  - path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    sha256: a3c88e9e9a6b27327238a732a4d6cdc4740ba50f26c581d251bfb5ad12f7dc0c
    role: context
  - path: data/structures/membrane_organelle/flagellar_pocket.yaml
    sha256: d67c465d104f21905f63ea994b6f4f526a51502cefccf79e9e732698f4971fa8
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
  - path: history/records/ciliary_pocket_collar/2026-09-09T193650Z-codex-2ade5b.yaml
    sha256: 40d52455f137443706f42f102500080c6f088a22b7488c78678e70a99586824f
    role: context
  - path: history/records/ciliary_pocket_collar/2026-09-10T013812Z-codex-d38ed3.yaml
    sha256: 0601374a8144e6966a1d08851d39b1bd00c05a586de878fa9375e893c4b1af5b
    role: context
  - path: history/records/ciliary_pocket_collar/2026-09-10T014219Z-codex-e70e45.yaml
    sha256: 3c80df02dfcfaf1c6351c3560c02ae08295c49abd1adac12d47f4d09ff2fee79
    role: context
  - path: justfile
    sha256: 634d060fd0c11a6ce8a3441a36341d03ac7c29bdeb50fb560ad9c4f77b190f4f
    role: context
  - path: pages/structures/cytoskeleton/ciliary_pocket_collar.html
    sha256: 511bb7cacd9932a4290aa4df741d00a1a463055eea34f083fa2316c66b29a9a4
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
- target_id: GO:1990900
  path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  label: ciliary pocket collar
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    role: maintained scientific record
scope:
  description: Whole native YAML including identity, typed relations, every component/function/graph
    edge, taxon/example, discussions and both history surfaces. Source access limitations
    retained per paper.
  selection: One exact record within the active 909-record goal; no batch sampling.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990900
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:26:58Z to 2026-10-11T23:27:00Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:27:00Z to 2026-10-11T23:27:04Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    --report /private/tmp/csm-review-20261011T232800Z/ciliary_pocket_collar-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets; paraphrases assessed separately against inspected
    text.
  scope_note: 2026-10-11T23:27:04Z to 2026-10-11T23:27:21Z; log SHA-256 8ab0e226e4a7798b5560bcfe3eaa39d55396d27e3164fd4c4459b189a4fd82d9
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:27:44Z to 2026-10-11T23:27:58Z; log SHA-256 e2ce523e6e88c9e5ea99c23750f1c095bb4476f6573aead8b46a1d5d8ff2e754
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3545\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T23:27:58Z to 2026-10-11T23:29:17Z; log SHA-256 459523b233cf29c593d6ebe49a38d5ed4484b1f98496dc47ea4fdc17be729286
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:32:04Z to 2026-10-11T23:32:30Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "[not exercised] BFO: the issuing authority was unreachable after 1 attempts,\
    \ so this resolver was not exercised\n  [not exercised] CHEBI: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] ComplexPortal: the issuing authority was unreachable after 1 attempts,\
    \ so this resolver was not exercised\n  [not exercised] DOI: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] GO: the issuing authority was unreachable after 1 attempts, so this\
    \ resolver was not exercised\n  [not exercised] InterPro: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] NCBITaxon: the issuing authority was unreachable after 1 attempts,\
    \ so this resolver was not exercised\n  [not exercised] PATO: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] PMID: the issuing authority was unreachable after 1 attempts, so\
    \ this resolver was not exercised\n  [not exercised] RO: the issuing authority\
    \ was unreachable after 1 attempts, so this resolver was not exercised\n  [not\
    \ exercised] SO: the issuing authority was unreachable after 1 attempts, so this\
    \ resolver was not exercised\n  [not exercised] UO: the issuing authority was\
    \ unreachable after 1 attempts, so this resolver was not exercised\n  [not exercised]\
    \ UniProtKB: the issuing authority was unreachable after 1 attempts, so this resolver\
    \ was not exercised\n  [not exercised] DOI: DataCite was unreachable, so DOI:10.22002/D1.1355\
    \ was not exercised\nresolver control: 14 resolver(s) could not be exercised because\
    \ their authority was unreachable; the rest accept a known id and reject a fabricated\
    \ one\n\nidentifier liveness summary:\n  OK             4016\n  SKIPPED      \
    \   251\n\nEvery identifier resolves at its issuing authority."
  scope_note: 2026-10-11T23:29:34Z to 2026-10-11T23:29:57Z; log SHA-256 fea3297b8556f2bc1f9b7053d2e57fa238f7e27121b7eab5396a9b3b27ec0c80
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Actual deterministic check passed; scientific support assessed separately.
  scope_note: 2026-10-11T23:29:57Z to 2026-10-11T23:31:27Z; log SHA-256 45a25fc1072d38a21fae9e79615ac64cf2ae2b52e40088ef081e2c6581728997
- check_id: baseline-qc
  name: Exact-base native merge-group QC
  status: passed
  required: true
  target_ids:
  - GO:1990900
  command: gh run view 38183517588 --repo CultureBotAI/CellStructureMech --log
  exit_code: 0
  summary: Exact 6b8e8880 baseline QC success verified from live run metadata and
    complete log. Not a fresh full local QC run.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38183517588;
    SHA-256 525a55d17a881a4c84dad779082212e22f4340030d6a86859c0b1702d026b789
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: abefa0652c7dfae6a06cd962f7c0805dd526c230f87180b35c408e076bd6a9b4
  support: context_only
  summary: Entire original native record read and unchanged captured bytes verified.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
  support: context_only
  summary: Typed parthood, assertion-local evidence and assembly-only essentiality
    rules.
- evidence_id: schema
  kind: record_content
  reference: src/cellstructuremech/schema/cellstructuremech.yaml
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
  support: context_only
  summary: Essentiality concerns structure formation, possibly defectively; gene symbols
    are metadata, not component identity.
- evidence_id: reading
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/reading-checkpoint.json
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: eacec47a4ec83f7aea2dc57abf00b895a6e216bf1d1c76ee2f5c9855606301c6
  support: context_only
  summary: Preserved source reading chronology and explicit abstract/full-text/visual
    limits.
- evidence_id: predecessors
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/predecessors.json
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 4f1c46b912fe671dcc64a5d99949cef6f94e3090587c5806a3ba5a876602b212
  support: context_only
  summary: Ignored-inclusive canonical bundle scan; no exact-target predecessor.
- evidence_id: go-relations
  kind: authority
  reference: /private/tmp/csm-review-20261011T222903Z/next-go-relations.log
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: a262339b1fbbc4277e13ac20c44b1875fd6042cc5209596e64eed932c6413396
  support: context_only
  summary: Source-native OAK typed relations inspected, independently consistent with
    QuickGO terms.
- evidence_id: context
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/context-search.log
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 1ba49870de1404b7f4c562c367b0563ca9ce248e3d0349886dd8ae944b8a267a
  support: context_only
  summary: Identifier/label/slug search includes ignored and hidden repository files,
    excluding Git internals and dependency trees.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T222903Z/next-adapter.log
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: All 28 iModulonDB dataset rows inspected; no matching Trypanosoma dataset.
    Not negative biological evidence.
- evidence_id: history-0
  kind: record_content
  reference: history/records/ciliary_pocket_collar/2026-09-09T193650Z-codex-2ade5b.yaml
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 40d52455f137443706f42f102500080c6f088a22b7488c78678e70a99586824f
  support: context_only
  summary: Entire original append-only history read; preserve historical actors and
    resolved issue scope.
- evidence_id: history-1
  kind: record_content
  reference: history/records/ciliary_pocket_collar/2026-09-10T013812Z-codex-d38ed3.yaml
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 0601374a8144e6966a1d08851d39b1bd00c05a586de878fa9375e893c4b1af5b
  support: context_only
  summary: Entire original append-only history read; preserve historical actors and
    resolved issue scope.
- evidence_id: history-2
  kind: record_content
  reference: history/records/ciliary_pocket_collar/2026-09-10T014219Z-codex-e70e45.yaml
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 3c80df02dfcfaf1c6351c3560c02ae08295c49abd1adac12d47f4d09ff2fee79
  support: context_only
  summary: Entire original append-only history read; preserve historical actors and
    resolved issue scope.
- evidence_id: dedup-pocket-collar-distribution-citation
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/dedup-pocket-collar-distribution-citation.log
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state exact-key GitHub issue search checked before creation. Any earlier
    sandbox network failure remains in separate receipt.
- evidence_id: dedup-pocket-collar-fpc4-linking-scope
  kind: validation
  reference: /private/tmp/csm-review-20261011T232800Z/dedup-pocket-collar-fpc4-linking-scope.log
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 37517e5f3dc66819f61f5a7bb8ace1921282415f10551d2defa5c3eb0985b570
  support: context_only
  summary: All-state exact-key GitHub issue search checked before creation. Any earlier
    sandbox network failure remains in separate receipt.
- evidence_id: paper-3
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC4156054/
  locator: DOI:10.1074/jbc.M114.554659; Results, Discussion, Experimental Procedures,
    nine captions
  accessed_at: '2026-10-11T22:54:49Z'
  snapshot_sha256: 9d686dd507f7aea408265e9599831288d454083983fef614b2186a24c683ce93
  support: supports
  summary: Purified BILBO1 domain analysis supports antiparallel dimers and leucine-zipper-dependent
    filament assembly. Molecular collar geometry remains a model; domain crystal/model
    distinctions retained.
- evidence_id: paper-4
  kind: primary_source
  reference: https://pmc.ncbi.nlm.nih.gov/articles/PMC7008359/
  locator: DOI:10.1074/jbc.RA119.010768; Results, Discussion, Experimental Procedures,
    Table 1 and seven captions
  accessed_at: '2026-10-11T22:54:49Z'
  snapshot_sha256: eec115a7d7c30831464ebfb05e0d0bcdbb012faec3861e1b7cdc3be67199d45a
  support: supports
  summary: BILBO1 NTD crystal structure and purified-domain binding map FPC4 recognition;
    U2OS is heterologous. Native linkage to the microtubule quartet is proposed, not
    directly proven.
- evidence_id: paper-11
  kind: primary_source
  reference: https://journals.plos.org/plosbiology/article?id=10.1371/journal.pbio.0060105
  locator: DOI:10.1371/journal.pbio.0060105; Results, Discussion, Methods and seven
    captions
  accessed_at: '2026-10-11T23:17:02Z'
  snapshot_sha256: 852d8bf17aad9264aff50beef94ebce15102b542b252cb3a77dc30714dd21084
  support: supports
  summary: BILBO1 RNAi blocks new FPC/FP assembly in tested procyclic cells while
    the old collar persists. Bloodstream lethality has a different morphology; genomic
    source strain is not every assay strain.
- evidence_id: paper-12
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4379179/fullTextXML
  locator: DOI:10.1371/journal.ppat.1004654; abstract, author summary, all Results,
    Discussion, Methods, seven captions and five tables
  accessed_at: '2026-10-11T22:54:20Z'
  snapshot_sha256: 629e3333f78e63bf0f1616488c04b018ebf143d9583f40d1aafe858a86c760a7
  support: supports
  summary: Purified calcium binding and coiled-coil-driven polymers are supported.
    Targeting assays retain endogenous BILBO1; dominant-negative mutants are not nulls
    and calcium regulation of native geometry remains a model.
- evidence_id: paper-13
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC5683654/fullTextXML
  locator: DOI:10.1371/journal.ppat.1006710; entire Results, Discussion, Methods and
    eight captions
  accessed_at: '2026-10-11T22:54:22Z'
  snapshot_sha256: a62fe459b845ca10b7934a02f20a2e0e70aeeb7350b436ce7b612e67a98d64a3
  support: supports
  summary: FPC4 binds BILBO1 domains and microtubules; endogenous localization, overexpression
    and heterologous assays differ. Physical bridging of the native MtQ is proposed.
    Partial RNAi and failed knockout attempts do not establish dispensability or essentiality.
- evidence_id: paper-14
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC8360560/fullTextXML
  locator: DOI:10.1371/journal.ppat.1009329; entire Results, Discussion, Conclusion,
    Methods, eight captions and Table 1
  accessed_at: '2026-10-11T22:54:25Z'
  snapshot_sha256: b71f84fb409ff564e93e7ea2f6c951218252ea667c7537b621eeb94155f357f6
  support: supports
  summary: BILBO2/Tb927.6.3240 is a T. brucei FPC component and partner of BILBO1/FPC4.
    Binary-domain structure, interaction tests and heterologous coexpression support
    the tripartite model, not an atomic native whole-collar structure or universal
    stoichiometry.
- evidence_id: paper-16
  kind: primary_source
  reference: https://www.ebi.ac.uk/europepmc/webservices/rest/PMC4810094/fullTextXML
  locator: DOI:10.3390/cells5010009; abstract and all main sections/captions
  accessed_at: '2026-10-11T22:54:29Z'
  snapshot_sha256: 86fc0f48497de67d50b384fe02e39cb1d7904dd1c5f200ee27f767b9f3b4c199
  support: supports
  summary: Review supports BILBO1 and collar architecture, but contains neither FPC4
    nor BILBO2. It cannot support a claim explicitly naming those later-characterized
    proteins. This is a literature review, not a new primary experiment.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO%3A0005856,GO%3A0020016,GO%3A0120119,GO%3A0120120,GO%3A0120269,GO%3A0140535,GO%3A1990900
  locator: Exact GO IDs, definitions, synonyms and child relation types
  accessed_at: '2026-10-11T22:57:55Z'
  snapshot_sha256: 2193158f92fafcc78c308b1ae6dcbcb7483113522fe12b201f3665c879e99c2e
  support: supports
  summary: Identity terms denote the requested structures; GO lexical synonymy is
    not an assertion that all historical protein cohorts are physically identical.
- evidence_id: taxon
  kind: authority
  reference: https://www.ebi.ac.uk/ena/taxonomy/rest/tax-id/5691
  locator: TaxId/name/rank
  accessed_at: '2026-10-11T22:57:55Z'
  snapshot_sha256: ba78ff6fe5de62b2654b61e249c2c87b239dca0208950b0e4ecf3ef2d81c99be
  support: supports
  summary: T. brucei species identity verified; experiments remain limited to named
    laboratory forms/lines.
- evidence_id: bilbo-domain
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/interpro/IPR040747/
  locator: Accession/type/domain identity and representative BILBO2-FPC4 structure
  accessed_at: '2026-10-11T23:20:18Z'
  snapshot_sha256: 2d292d9ea1b940dd62648024f3b1f10c5a73566bbd902170d164afbed3115731
  support: supports
  summary: These are N-terminal domains, not exact whole BILBO protein families; label-only
    decisions remain appropriate.
- evidence_id: bilbo-pfam
  kind: authority
  reference: https://www.ebi.ac.uk/interpro/api/entry/pfam/PF18281/
  locator: Accession/type/domain identity and representative BILBO2-FPC4 structure
  accessed_at: '2026-10-11T23:20:19Z'
  snapshot_sha256: 9155fdf7c6104cf7b94a59305105a759307f05033dddeeb355d602f36894fe26
  support: supports
  summary: These are N-terminal domains, not exact whole BILBO protein families; label-only
    decisions remain appropriate.
- evidence_id: prior-295
  kind: prior_review
  reference: /private/tmp/csm-review-20261011T222903Z/next-issue-295.log
  accessed_at: '2026-10-11T23:32:41Z'
  snapshot_sha256: 1a80214a26a976eef2d4fddb8f945887959af9a5e62bea6db72bfee2a59175dd
  support: context_only
  summary: Closed issue narrowed FPC4 function/graph to binding and localization;
    current component role remains broader.
assessments:
- assessment_id: biology
  area: evidence
  topic: Three constituents, three functions and seven assembly edges
  outcome: supported
  target_ids:
  - GO:1990900
  evidence_ids:
  - record
  - paper-3
  - paper-4
  - paper-11
  - paper-12
  - paper-13
  - paper-14
  - paper-16
  - bilbo-domain
  - bilbo-pfam
  summary: BILBO1 polymer scaffold and new-FPC/FP requirement are supported in tested
    procyclic cells. FPC4 binding and localizations are supported, not direct native
    bridging. BILBO2 binary-domain binding and tripartite interaction model do not
    assert resolved native stoichiometry. Historical broad-eukaryote distribution
    removal and split dimer/polymer edges remain correct; unasserted whole-family
    mappings are genuine unknowns.
- assessment_id: pocket-collar-distribution-citation
  area: evidence
  topic: Attach the three-protein occurrence note to an appropriate source
  outcome: concern
  target_ids:
  - GO:1990900
  evidence_ids:
  - record
  - paper-16
  - paper-14
  summary: The T. brucei taxonomic note explicitly names BILBO1/FPC4/BILBO2 but cites
    the 2016 Perdomo review, which contains neither FPC4 nor BILBO2. The already-cited
    2021 Isch primary study supports their T. brucei FPC localization/interaction
    context.
- assessment_id: pocket-collar-fpc4-linking-scope
  area: evidence
  topic: Qualify the proposed native FPC4 connection
  outcome: concern
  target_ids:
  - GO:1990900
  evidence_ids:
  - record
  - paper-13
  - paper-4
  - prior-295
  summary: FPC4 component.role still categorically says it links the collar to microtubule-associated
    elements. The primary studies directly establish binding and localization but
    describe native FPC/MtQ linking as proposed. Historical issue 295 corrected other
    fields, not this residual role text.
- assessment_id: identity
  area: grounding
  topic: Identity and structure relationships
  outcome: supported
  target_ids:
  - GO:1990900
  evidence_ids:
  - record
  - go
  - go-relations
  summary: Exact GO structure identity, definition, category/kind and synonym evidence
    are supported. No single protein is substituted for a structure. Ciliary-pocket
    parthood is supported; T. brucei protein composition is not generalized to every
    organism in the GO definition.
- assessment_id: provenance
  area: completeness
  topic: Discussions, optional surfaces and status
  outcome: supported
  target_ids:
  - GO:1990900
  evidence_ids:
  - record
  - rules
  - reading
  - context
  summary: All original inline/repository history and open scope/grounding discussions
    read. Missing optional stoichiometry, physical measurements, images, datasets,
    protein examples and trait/pathway links are not defects. PROPOSED is retained.
    This is a bounded review of represented claims and consequential gaps, not an
    exhaustive discovery of every later protein or publication.
findings:
- finding_id: F1
  issue_key: pocket-collar-distribution-citation
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Attach the three-protein occurrence note to an appropriate source
  description: The T. brucei taxonomic note explicitly names BILBO1/FPC4/BILBO2 but
    cites the 2016 Perdomo review, which contains neither FPC4 nor BILBO2. The already-cited
    2021 Isch primary study supports their T. brucei FPC localization/interaction
    context.
  target_ids:
  - GO:1990900
  field_paths:
  - taxonomic_distribution[0].reference
  - taxonomic_distribution[0].note
  evidence_ids:
  - record
  - paper-16
  - paper-14
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded evidence-note, citation or role wording defect; structure
    identity and occurrence remain supported.
- finding_id: F2
  issue_key: pocket-collar-fpc4-linking-scope
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: Qualify the proposed native FPC4 connection
  description: FPC4 component.role still categorically says it links the collar to
    microtubule-associated elements. The primary studies directly establish binding
    and localization but describe native FPC/MtQ linking as proposed. Historical issue
    295 corrected other fields, not this residual role text.
  target_ids:
  - GO:1990900
  field_paths:
  - components[1].role
  evidence_ids:
  - record
  - paper-13
  - paper-4
  - prior-295
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded evidence-note, citation or role wording defect; structure
    identity and occurrence remain supported.
actions:
- action_id: A1
  description: Attach the three-protein occurrence note to an appropriate source
  finding_ids:
  - F1
  target_ids:
  - GO:1990900
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    role: maintained scientific record
  acceptance_checks:
  - Use the 2021 primary citation with a bounded T. brucei component-localization
    note, or narrow the note to the existing 2016 source.
  - Preserve species occurrence and avoid universal strain/life-stage assembly claims.
  - Guarded writer; append only actual Codex curation and EDIT history; preserve PROPOSED,
    all original events/discussions and historical bundles.
  - Regenerate target products, pass focused regressions and native gates; save an
    exact-lineage successor.
- action_id: A2
  description: Qualify the proposed native FPC4 connection
  finding_ids:
  - F2
  target_ids:
  - GO:1990900
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    role: maintained scientific record
  acceptance_checks:
  - State measured BILBO1 interaction/localization and mark the native linking role
    as proposed.
  - Preserve the already-corrected function and graph evidence, rather than reopening
    their historical fix.
  - Guarded writer; append only actual Codex curation and EDIT history; preserve PROPOSED,
    all original events/discussions and historical bundles.
  - Regenerate target products, pass focused regressions and native gates; save an
    exact-lineage successor.
limitations:
- Same-agent scientific review, not independent human approval or raw-data reanalysis.
- Original source access dates/hashes are retained from the read-ahead phase. Actual
  reading scope is recorded per source; separate supplements, movies and raw experiments
  were not reviewed.
- 2009 MORN1, 1999 FAZ assembly and 2011 CC2D remain primary-abstract-only for narrow
  supported claims; full-text inaccessibility is not asserted globally. Other material
  sources have the inspected main-text scope stated in evidence.
- The 2008 FAZ1 Figure 4 is visually inspected only for the FAZ review; other main
  figures were read as captions, not certified pixel-level reanalyses. No source media
  adopted.
- Exact baseline full QC is verified CI; fresh local schema/strict/history/label/reference/trait/review
  checks are separate. Existing identifier-policy/no-adapter and test skips remain
  explicit.
- No exact whole-family accession is invented and no absence from iModulonDB is biological
  evidence. Neighboring flagellar pocket and newer-publication leads are not counted
  as completed reviews.
```
