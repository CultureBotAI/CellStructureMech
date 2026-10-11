# Alfa filament: scientific record review

- Review: 20261011T071302Z-alfa_filament-audit
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-11T07:03:46Z
- Finished UTC: 2026-10-11T07:13:02Z
- Reviewer: Codex (self_review)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Entire native record assessed; concrete findings saved before separately authorized curation.

## Scope And Provenance

Entire native YAML: identity, synonyms, hierarchy, composition, taxonomy, functions, each causal edge, optional resources and provenance.

Selection: One resolved sequential target in the all-record goal; not a sampled verdict for other records.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: working_tree at Git base d9cea09379282886022064c57c012efe0db3beaf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:alfa_filament | data/structures/cytoskeleton/alfa_filament.yaml | maintained | AlfA filament |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| schema | passed | True | cellstructuremech:alfa_filament | Deterministic command passed; not scientific verification. |
| strict | passed | True | cellstructuremech:alfa_filament | Deterministic command passed; not scientific verification. |
| snippets | passed | True | cellstructuremech:alfa_filament | No verbatim snippets. This does not validate paraphrases. |
| history | passed | True | cellstructuremech:alfa_filament | Deterministic command passed; not scientific verification. |
| labels | passed | True | cellstructuremech:alfa_filament | id↔label correspondence summary:<br>          OK_CANONICAL: 3544<br>            OK_SYNONYM: 50<br>          OK_EXCEPTION: 6<br>    SKIPPED_NO_ADAPTER: 603<br><br>✅ All id↔label pairs correspond. |
| traits | passed | True | cellstructuremech:alfa_filament | Deterministic command passed; not scientific verification. |
| curies | passed | True | cellstructuremech:alfa_filament | resolver control: every resolver accepts a known id and rejects a fabricated one<br>resolving 6 CHEBI identifier(s)...<br>resolving 77 DOI identifier(s)...<br>resolving 30 GO identifier(s)...<br>resolving 1 InterPro identifier(s)...<br>resolving 12 NCBITaxon identifier(s)...<br>resolving 1 PMID identifier(s)...<br>resolving 2 uniprot.location identifier(s)...<br><br>identifier liveness summary:<br>  OK             4012<br>  SKIPPED         251<br><br>Every identifier resolves at its issuing authority. |
| reviews | passed | True | cellstructuremech:alfa_filament | Deterministic command passed; not scientific verification. |
| diff | passed | True | cellstructuremech:alfa_filament | Deterministic command passed; not scientific verification. |
| contract | passed | True | cellstructuremech:alfa_filament | Deterministic command passed; not scientific verification. |
| Exact-baseline authoritative CI QC | passed | True | cellstructuremech:alfa_filament | Full native QC passed on this exact unchanged input revision, including generated products; not newly run local full QC. |

## Scientific And Domain Assessments

### Filament versus whole cytoskeleton

identity: concern. Targets: cellstructuremech:alfa_filament.

Minted AlfA identity is retained, but a polymeric filament is not a subtype of the whole cytoskeletal framework. The identifier example in CURATION.md repeats that incorrect hierarchy convention.

### Composition, scope, function and each graph edge

evidence: supported. Targets: cellstructuremech:alfa_filament.

AlfA is the polymer constituent; AlfB-parN remains a graph-scoped regulator. B. subtilis variable plasmid-dependent occurrence and pBET131 example are scoped. The coarse polymerization/regulation/segregation graph is supported when the mistaken citation is corrected. No exact protein accession, raw dataset, image or numerical measurement is asserted.

### Prior history, omitted optional fields and review coverage

provenance: supported. Targets: cellstructuremech:alfa_filament.

Both history surfaces and previous issue fixes were read. No empty optional field or acknowledged unknown is counted as a finding. Ignored-inclusive canonical-review search found no exact-target predecessor; existing legacy reports remain historical. No claims of reviewing adjacent records are made.

## Findings

### F1: Replace the ParM DOI with the intended AlfA paper

major / open / confirmed; issue key: alfa-filament-parm-citation-mismatch.

Four AlfA claim sites cite DOI:10.1016/j.str.2009.07.008 while naming Polka et al. 2009 and their AlfA study. That DOI is a different ParM paper. The intended work is DOI:10.1128/JB.00676-09 in Journal of Bacteriology, whose inspected experiments support the AlfA claims.

### F2: Separate AlfA filament class from cytoskeleton parthood

major / open / confirmed; issue key: alfa-filament-hierarchy-parthood.

The record asserts AlfA filament is-a GO:0005856 cytoskeleton, the complete framework. GO:0099513 polymeric cytoskeletal fiber is the appropriate broader filament class and is itself part_of cytoskeleton. The identifier guidance incorrectly calls the whole cytoskeleton the parent of a minted filament and can reproduce the error.

### F3: Correct the Becker 2006 author attribution

minor / open / confirmed; issue key: alfa-becker-bibliographic-authors.

The bibliographic note names Becker, Moller-Jensen, Jensen and Gerdes. The inspected article author list instead names Becker, Herrera, Gunderson, Derman, Dance, Sims, Larsen and Pogliano. The DOI and biological claim are valid; the attached authors are not.

## Recommended Actions And Acceptance Checks

### A1

Replace the ParM DOI with the intended AlfA paper

- Replace all four mistaken DOI occurrences and correct the journal without changing the AlfA claim scope.
- Preserve discussion rationale, unresolved family grounding and the previously repaired AlfB-parN graph.
- Use guarded curation, append Codex curation and EDIT history, retain PROPOSED, previous histories/reviews and discussion rationale; regenerate affected products and pass focused tests plus native QC.

### A2

Separate AlfA filament class from cytoskeleton parthood

- Use GO:0099513 as the broader is-a parent and GO:0005856 as part_of, retaining cellstructuremech:alfa_filament identity.
- Correct the misleading filament identifier example in CURATION.md without rewriting or claiming review of other filament records.
- Use guarded curation, append Codex curation and EDIT history, retain PROPOSED, previous histories/reviews and discussion rationale; regenerate affected products and pass focused tests plus native QC.

### A3

Correct the Becker 2006 author attribution

- Replace the incorrect explicit author list with the verified list or Becker et al. 2006, retaining title, journal and DOI.
- Use guarded curation, append Codex curation and EDIT history, retain PROPOSED, previous histories/reviews and discussion rationale; regenerate affected products and pass focused tests plus native QC.

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| record | data/structures/cytoskeleton/alfa_filament.yaml | context_only | Full native YAML read and exact inputs captured before the formal assessment. Initial source leads preceded some captures. |
| rules | docs/CURATION.md | context_only | Requires claim-specific evidence, is-a versus parthood, constituent/machinery distinction and append-only rationale. |
| go | https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0001534,GO:0005737,GO:0005826,GO:0005856,GO:0005879,GO:0005885,GO:0005938,GO:0015629,GO:0030479,GO:0030864,GO:0036156,GO:0036157,GO:0061645,GO:0097545,GO:0097649,GO:0097650,GO:0099079,GO:0099513,GO:0110165,GO:0160111,GO:0160113,GO:0160114; Current native definitions, synonyms, obsolescence flags and typed child relationships | supports | Exact native GO identities and roles checked. Reverse child lists confirm is-a versus part_of; untyped ancestor reachability alone is not treated as an is-a assertion. |
| taxa | https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&amp;id=1423%2C284812%2C3055%2C4896%2C4932%2C559292; Top-level requested NCBI Taxon entries | supports | The six requested taxa and reference-strain names resolve. Taxonomy is not evidence of structure prevalence. |
| adapter | /private/tmp/csm-review-20261011T070221Z/adapter.log | context_only | Live 28-dataset inventory: no matching yeast or Chlamydomonas dataset. Bacillus searches are described separately; noncoverage is not negative biology. |
| becker | DOI:10.1038/sj.emboj.7601443; Author list, AlfA/AlfB Results, Figures 4-6 and Discussion | supports | AlfA forms dynamic filaments in B. subtilis and supports pBET131 segregation; AlfB is part of the partition system. Actual authors are Becker, Herrera, Gunderson, Derman, Dance, Sims, Larsen and Pogliano. |
| polka2009 | DOI:10.1128/JB.00676-09; Abstract, protein-purification/EM Methods and filament-assembly Results | supports | Polka, Kollman, Agard and Mullins study purified AlfA filaments in Journal of Bacteriology. ATP/GTP-dependent assembly and stable bundles are not ParM dynamic instability. |
| wrong-parm | DOI:10.1016/j.str.2009.07.008; Primary abstract and bibliographic metadata | supports | This DOI denotes Structural polymorphism of the ParM filament and dynamic instability, not the cited AlfA paper. |
| polka2014 | DOI:10.1073/pnas.1304127111; Abstract, in-vivo motion Results and AlfB/parN regulation Results with Figures 1-3 captions | supports | AlfB-parN nucleates and stabilizes AlfA; free AlfB has different effects. Graph-scoped centromere complex and nonmechanistic segregation support remain appropriate. |
| szewczak | DOI:10.1073/pnas.1716424115; Abstract, filament-reconstruction Results and Figure 1 caption | supports | Near-atomic cryo-EM of a nonbundling AlfA variant establishes filament architecture; the native record does not misrepresent it as in-situ wild-type reconstruction. |
| tanaka | DOI:10.1128/JB.01312-09; Abstract and Introduction | supports | Single-author Tanaka paper characterizes AlfB/parN and pBET131; the earlier corrected citation is valid. |
| go-search | https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=AlfA&amp;limit=100; Complete exact-name query response, two unrelated interferon-alpha hits | supports | No exact AlfA cellular-component identity was returned. Minted identity is retained; polymeric cytoskeletal fiber is only the broader class. |
| modulome-alfa | /private/tmp/csm-review-20261011T070221Z/adapter-modulome-alfA.log | context_only | B. subtilis structured adapter query returned no gene/module hits. This is not evidence against plasmid localization. |
| modulome-alfb | /private/tmp/csm-review-20261011T070221Z/adapter-modulome-alfB.log | context_only | B. subtilis structured adapter query returned no gene/module hits. This is not evidence against plasmid localization. |
| modulome-parn | /private/tmp/csm-review-20261011T070221Z/adapter-modulome-parN.log | context_only | B. subtilis structured adapter query returned no gene/module hits. This is not evidence against plasmid localization. |
| nicolas-alfa | /private/tmp/csm-review-20261011T070221Z/adapter-nicolas-alfA.log | context_only | B. subtilis structured adapter query returned no gene/module hits. This is not evidence against plasmid localization. |
| nicolas-alfb | /private/tmp/csm-review-20261011T070221Z/adapter-nicolas-alfB.log | context_only | B. subtilis structured adapter query returned no gene/module hits. This is not evidence against plasmid localization. |
| nicolas-parn | /private/tmp/csm-review-20261011T070221Z/adapter-nicolas-parN.log | context_only | B. subtilis structured adapter query returned no gene/module hits. This is not evidence against plasmid localization. |

## Limits And Additional Notes

- Same-agent assessment; no independent or human sign-off and no promotion of PROPOSED.
- Identifier check has 251 skipped identifiers; label check has 603 pairs without adapters. Exact target authorities were inspected separately; global skipped namespaces are not certified.
- Full QC uses the verified exact-baseline merge-group CI run. No raw experimental data or movies were reanalysed.
- Europe PMC fullTextXML failed for several sources; official PMC full HTML supplied the readable fallback. Access tiers are specified per source below.
- The broader AlfA filament query is a nonexhaustive 100-result lexical search; the exact AlfA query is complete. No claim that all ontology synonyms were exhaustively excluded. AlfA family grounding remains reviewed-label-only.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261011T071302Z-alfa_filament-audit
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Alfa filament: scientific record review'
started_at: '2026-10-11T07:03:46Z'
finished_at: '2026-10-11T07:13:02Z'
reviewer:
  identity: Codex
  kind: agent
  independence: self_review
  independence_basis: Same-agent review before curation, not independent human approval.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
scientific_review: true
summary: Entire native record assessed; concrete findings saved before separately
  authorized curation.
source:
  git_revision: d9cea09379282886022064c57c012efe0db3beaf
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
    sha256: 69d877184d26cad12996c067faf588ed2aae4c33518a904a75459cd8c80de62b
    role: context
  - path: data/structures/cytoskeleton/actin_body.yaml
    sha256: b0abd6f5cb40fec99ab2d5a23a56b7307041f4ac8eda2a32b9db8d57680f22ea
    role: context
  - path: data/structures/cytoskeleton/actin_cortical_patch.yaml
    sha256: fcbfc85680d23109790a85ffb36bc4741fd234d0b8ea0e08daeb3a968a83a98d
    role: context
  - path: data/structures/cytoskeleton/actomyosin_contractile_ring.yaml
    sha256: e5f2ff579535048e3d07b5b7b1284ce798cc61bc15f035a0bdf9eefad82af972
    role: context
  - path: data/structures/cytoskeleton/alfa_filament.yaml
    sha256: 0de91b02762d26df788d87897737eafac9de142277c77712ce4d2892c6156ffd
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
  - path: history/records/alfa_filament/2026-09-22T042634Z-codex-25f78a.yaml
    sha256: b1ccd139072f92280690d068ae556e95ca4b07634147abbb3866b2d9c37ed141
    role: context
  - path: history/records/alfa_filament/2026-09-22T070127Z-codex-75e31b.yaml
    sha256: a00d21a852a8cf2c4bd387cf5b3c2e3b49d65deeb054acfca5b42585e3651fc2
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
- target_id: cellstructuremech:alfa_filament
  path: data/structures/cytoskeleton/alfa_filament.yaml
  label: AlfA filament
  kind: maintained
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/alfa_filament.yaml
    role: maintained scientific record
scope:
  description: 'Entire native YAML: identity, synonyms, hierarchy, composition, taxonomy,
    functions, each causal edge, optional resources and provenance.'
  selection: One resolved sequential target in the all-record goal; not a sampled
    verdict for other records.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - cellstructuremech:alfa_filament
checks:
- check_id: schema
  name: schema
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/cytoskeleton/alfa_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; not scientific verification.
  scope_note: 2026-10-11T07:05:05Z to 2026-10-11T07:05:07Z; log SHA-256 de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- check_id: strict
  name: strict
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/python scripts/validate_strict.py data/structures/cytoskeleton/alfa_filament.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; not scientific verification.
  scope_note: 2026-10-11T07:05:07Z to 2026-10-11T07:05:11Z; log SHA-256 a67df3fa0fed08c890b70f50cf5ad0c76ab853928d5a9088693d9f5a06605b1e
- check_id: snippets
  name: snippets
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/python scripts/fetch_snippets.py --verify --check --record data/structures/cytoskeleton/alfa_filament.yaml
    --report /private/tmp/csm-review-20261011T070221Z/alfa_filament-snippets.md
  exit_code: 0
  expected_exit_code: 0
  summary: No verbatim snippets. This does not validate paraphrases.
  scope_note: 2026-10-11T07:05:11Z to 2026-10-11T07:05:30Z; log SHA-256 19539338e3ec8ee46e88fd4402d57b05571ffa76495c7c8af6d9dcde78df854e
- check_id: history
  name: history
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; not scientific verification.
  scope_note: 2026-10-11T07:05:30Z to 2026-10-11T07:05:43Z; log SHA-256 e836c3a60d88b76a8f3886dd6bf8d339fcbd2229409e99019ae17006c6c6f673
- check_id: labels
  name: labels
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  summary: "id↔label correspondence summary:\n          OK_CANONICAL: 3544\n     \
    \       OK_SYNONYM: 50\n          OK_EXCEPTION: 6\n    SKIPPED_NO_ADAPTER: 603\n\
    \n✅ All id↔label pairs correspond."
  scope_note: 2026-10-11T07:05:43Z to 2026-10-11T07:07:05Z; log SHA-256 d423103555a6a5b538a7c811a73a29c24ed0e5a2eae00d1bb94715295f23f7cb
- check_id: traits
  name: traits
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/python scripts/check_trait_links.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; not scientific verification.
  scope_note: 2026-10-11T07:07:05Z to 2026-10-11T07:07:33Z; log SHA-256 c492eea742fc96aff67bb3d0570a24a4c3c20c30e436cedc85f2c3969114d31f
- check_id: curies
  name: curies
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/python scripts/check_curies.py --check
  exit_code: 0
  expected_exit_code: 0
  summary: "resolver control: every resolver accepts a known id and rejects a fabricated\
    \ one\nresolving 6 CHEBI identifier(s)...\nresolving 77 DOI identifier(s)...\n\
    resolving 30 GO identifier(s)...\nresolving 1 InterPro identifier(s)...\nresolving\
    \ 12 NCBITaxon identifier(s)...\nresolving 1 PMID identifier(s)...\nresolving\
    \ 2 uniprot.location identifier(s)...\n\nidentifier liveness summary:\n  OK  \
    \           4012\n  SKIPPED         251\n\nEvery identifier resolves at its issuing\
    \ authority."
  scope_note: 2026-10-11T07:07:33Z to 2026-10-11T07:09:55Z; log SHA-256 e06f3f324434626cb1076037e7014bae54ba5e379333ec2cb3f4ef1b0e8c9ee1
- check_id: reviews
  name: reviews
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/python scripts/record_review.py check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; not scientific verification.
  scope_note: 2026-10-11T07:09:55Z to 2026-10-11T07:10:42Z; log SHA-256 c3d95a55b38dffd1274c02af55e2b3f708b154d2f63e072edb88aba988128971
- check_id: diff
  name: diff
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: git diff --check
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; not scientific verification.
  scope_note: 2026-10-11T07:10:42Z to 2026-10-11T07:10:42Z; log SHA-256 e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855
- check_id: contract
  name: contract
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: .venv/bin/python -m pytest -q tests/test_record_review_contract.py
  exit_code: 0
  expected_exit_code: 0
  summary: Deterministic command passed; not scientific verification.
  scope_note: 2026-10-11T07:03:13Z to 2026-10-11T07:04:12Z; log SHA-256 5ddb5253163bef2fb3581b178616966b159be8fb066c81fdfe022c6d78405a37
- check_id: qc
  name: Exact-baseline authoritative CI QC
  status: passed
  required: true
  target_ids:
  - cellstructuremech:alfa_filament
  command: gh run view 38119529229 --json status,conclusion,headSha,event,name,url,jobs;
    gh run view 38119529229 --log
  exit_code: 0
  summary: Full native QC passed on this exact unchanged input revision, including
    generated products; not newly run local full QC.
  scope_note: https://github.com/CultureBotAI/CellStructureMech/actions/runs/38119529229;
    full-log SHA-256 3fbc61430d4f984ff00dcdd8fea2fa5ca825a06e78e302342089a4fef8294c49
evidence:
- evidence_id: record
  kind: record_content
  reference: data/structures/cytoskeleton/alfa_filament.yaml
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: 0de91b02762d26df788d87897737eafac9de142277c77712ce4d2892c6156ffd
  support: context_only
  summary: Full native YAML read and exact inputs captured before the formal assessment.
    Initial source leads preceded some captures.
- evidence_id: rules
  kind: record_content
  reference: docs/CURATION.md
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: c3e482fbf381edcf0238e579648b779c3a8803a1d888b89397ad6fc8808dd07d
  support: context_only
  summary: Requires claim-specific evidence, is-a versus parthood, constituent/machinery
    distinction and append-only rationale.
- evidence_id: go
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0000147,GO:0001534,GO:0005737,GO:0005826,GO:0005856,GO:0005879,GO:0005885,GO:0005938,GO:0015629,GO:0030479,GO:0030864,GO:0036156,GO:0036157,GO:0061645,GO:0097545,GO:0097649,GO:0097650,GO:0099079,GO:0099513,GO:0110165,GO:0160111,GO:0160113,GO:0160114
  locator: Current native definitions, synonyms, obsolescence flags and typed child
    relationships
  accessed_at: '2026-10-11T07:04:57Z'
  snapshot_sha256: 71f14150527ed018024bb5682b4d3b88750c50919ca386ca9bac5766e8df4480
  support: supports
  summary: Exact native GO identities and roles checked. Reverse child lists confirm
    is-a versus part_of; untyped ancestor reachability alone is not treated as an
    is-a assertion.
- evidence_id: taxa
  kind: authority
  reference: https://eutils.ncbi.nlm.nih.gov/entrez/eutils/efetch.fcgi?db=taxonomy&id=1423%2C284812%2C3055%2C4896%2C4932%2C559292
  locator: Top-level requested NCBI Taxon entries
  accessed_at: '2026-10-11T07:05:02Z'
  snapshot_sha256: 785915aef9110dcf4728409ac02274f8c858aba27b08779ae5e3b0d2c5a37108
  support: supports
  summary: The six requested taxa and reference-strain names resolve. Taxonomy is
    not evidence of structure prevalence.
- evidence_id: adapter
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/adapter.log
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: 1e76828df39ff699ab7278c8586c1794b6bc23934d944644b00b88e8613c5549
  support: context_only
  summary: 'Live 28-dataset inventory: no matching yeast or Chlamydomonas dataset.
    Bacillus searches are described separately; noncoverage is not negative biology.'
- evidence_id: becker
  kind: primary_source
  reference: DOI:10.1038/sj.emboj.7601443
  locator: Author list, AlfA/AlfB Results, Figures 4-6 and Discussion
  accessed_at: '2026-10-11T07:05:02Z'
  snapshot_sha256: e54d7e366d613615e1ea6046d4dd554195c2baab479a3c9d5d6c4caed5b55ba5
  support: supports
  summary: AlfA forms dynamic filaments in B. subtilis and supports pBET131 segregation;
    AlfB is part of the partition system. Actual authors are Becker, Herrera, Gunderson,
    Derman, Dance, Sims, Larsen and Pogliano.
- evidence_id: polka2009
  kind: primary_source
  reference: DOI:10.1128/JB.00676-09
  locator: Abstract, protein-purification/EM Methods and filament-assembly Results
  accessed_at: '2026-10-11T07:05:06Z'
  snapshot_sha256: 38e3194799870f08e9213176bd5fd349d54995871b52f02c5b1c8946e2cfe9f3
  support: supports
  summary: Polka, Kollman, Agard and Mullins study purified AlfA filaments in Journal
    of Bacteriology. ATP/GTP-dependent assembly and stable bundles are not ParM dynamic
    instability.
- evidence_id: wrong-parm
  kind: primary_source
  reference: DOI:10.1016/j.str.2009.07.008
  locator: Primary abstract and bibliographic metadata
  accessed_at: '2026-10-11T07:05:02Z'
  snapshot_sha256: 52188337181be37ef3c0fd7d751b184250c7ca3bac55f7a2496e34da1853195e
  support: supports
  summary: This DOI denotes Structural polymorphism of the ParM filament and dynamic
    instability, not the cited AlfA paper.
- evidence_id: polka2014
  kind: primary_source
  reference: DOI:10.1073/pnas.1304127111
  locator: Abstract, in-vivo motion Results and AlfB/parN regulation Results with
    Figures 1-3 captions
  accessed_at: '2026-10-11T07:05:02Z'
  snapshot_sha256: 8374efa31ef6582a77fea8c7897841f9cf9f607928fd762205a326f3682d978b
  support: supports
  summary: AlfB-parN nucleates and stabilizes AlfA; free AlfB has different effects.
    Graph-scoped centromere complex and nonmechanistic segregation support remain
    appropriate.
- evidence_id: szewczak
  kind: primary_source
  reference: DOI:10.1073/pnas.1716424115
  locator: Abstract, filament-reconstruction Results and Figure 1 caption
  accessed_at: '2026-10-11T07:05:03Z'
  snapshot_sha256: 44079e2855dadb59452576b405c2c9fa0cf39f42dce7422d82617af8c526a175
  support: supports
  summary: Near-atomic cryo-EM of a nonbundling AlfA variant establishes filament
    architecture; the native record does not misrepresent it as in-situ wild-type
    reconstruction.
- evidence_id: tanaka
  kind: primary_source
  reference: DOI:10.1128/JB.01312-09
  locator: Abstract and Introduction
  accessed_at: '2026-10-11T07:05:03Z'
  snapshot_sha256: bec32b7c640f7d4a16971a2ef4c37943d12dc4548e54af46481a8548c55deb32
  support: supports
  summary: Single-author Tanaka paper characterizes AlfB/parN and pBET131; the earlier
    corrected citation is valid.
- evidence_id: go-search
  kind: authority
  reference: https://www.ebi.ac.uk/QuickGO/services/ontology/go/search?query=AlfA&limit=100
  locator: Complete exact-name query response, two unrelated interferon-alpha hits
  accessed_at: '2026-10-11T07:10:57Z'
  snapshot_sha256: aa6e86dd9bffcc15cb5fdd07001747ed7240e916277fdb1ba1bea05c12db6bc4
  support: supports
  summary: No exact AlfA cellular-component identity was returned. Minted identity
    is retained; polymeric cytoskeletal fiber is only the broader class.
- evidence_id: modulome-alfa
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/adapter-modulome-alfA.log
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: d56b906358d6d9631453ea7b3159fbde817c3ce6117b37b77f509b52ec033393
  support: context_only
  summary: B. subtilis structured adapter query returned no gene/module hits. This
    is not evidence against plasmid localization.
- evidence_id: modulome-alfb
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/adapter-modulome-alfB.log
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: f29a074a453390a3389a8547b5a5c4d5cd98deeb08b0fec3b936781c929f7356
  support: context_only
  summary: B. subtilis structured adapter query returned no gene/module hits. This
    is not evidence against plasmid localization.
- evidence_id: modulome-parn
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/adapter-modulome-parN.log
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: 61e296ecae9a9d65121a8780ac4dc873af5162799224abf5f6a0846cbe4832b6
  support: context_only
  summary: B. subtilis structured adapter query returned no gene/module hits. This
    is not evidence against plasmid localization.
- evidence_id: nicolas-alfa
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/adapter-nicolas-alfA.log
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: b7bd30afad89c9b46f2a58728aeb684e044ec95f5b3d20d0da6e51b9c6c3c13f
  support: context_only
  summary: B. subtilis structured adapter query returned no gene/module hits. This
    is not evidence against plasmid localization.
- evidence_id: nicolas-alfb
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/adapter-nicolas-alfB.log
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: b84b7693612711a6842fb7191cba54214332eb009d6853e6d96715ff94680b53
  support: context_only
  summary: B. subtilis structured adapter query returned no gene/module hits. This
    is not evidence against plasmid localization.
- evidence_id: nicolas-parn
  kind: validation
  reference: /private/tmp/csm-review-20261011T070221Z/adapter-nicolas-parN.log
  accessed_at: '2026-10-11T07:13:02Z'
  snapshot_sha256: a03cd523367b7a537b7c2379226caef74ca8c98e9508b8a8c0167b99a6819c59
  support: context_only
  summary: B. subtilis structured adapter query returned no gene/module hits. This
    is not evidence against plasmid localization.
assessments:
- assessment_id: identity
  area: identity
  topic: Filament versus whole cytoskeleton
  outcome: concern
  target_ids:
  - cellstructuremech:alfa_filament
  evidence_ids:
  - record
  - go
  - go-search
  - polka2009
  summary: Minted AlfA identity is retained, but a polymeric filament is not a subtype
    of the whole cytoskeletal framework. The identifier example in CURATION.md repeats
    that incorrect hierarchy convention.
- assessment_id: biology
  area: evidence
  topic: Composition, scope, function and each graph edge
  outcome: supported
  target_ids:
  - cellstructuremech:alfa_filament
  evidence_ids:
  - becker
  - polka2009
  - polka2014
  - szewczak
  - tanaka
  - taxa
  summary: AlfA is the polymer constituent; AlfB-parN remains a graph-scoped regulator.
    B. subtilis variable plasmid-dependent occurrence and pBET131 example are scoped.
    The coarse polymerization/regulation/segregation graph is supported when the mistaken
    citation is corrected. No exact protein accession, raw dataset, image or numerical
    measurement is asserted.
- assessment_id: resources-provenance
  area: provenance
  topic: Prior history, omitted optional fields and review coverage
  outcome: supported
  target_ids:
  - cellstructuremech:alfa_filament
  evidence_ids:
  - record
  - rules
  summary: Both history surfaces and previous issue fixes were read. No empty optional
    field or acknowledged unknown is counted as a finding. Ignored-inclusive canonical-review
    search found no exact-target predecessor; existing legacy reports remain historical.
    No claims of reviewing adjacent records are made.
findings:
- finding_id: F1
  issue_key: alfa-filament-parm-citation-mismatch
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: Replace the ParM DOI with the intended AlfA paper
  description: Four AlfA claim sites cite DOI:10.1016/j.str.2009.07.008 while naming
    Polka et al. 2009 and their AlfA study. That DOI is a different ParM paper. The
    intended work is DOI:10.1128/JB.00676-09 in Journal of Bacteriology, whose inspected
    experiments support the AlfA claims.
  target_ids:
  - cellstructuremech:alfa_filament
  field_paths:
  - components[0].evidence
  - evidence
  - causal_graphs[0].edges[0].evidence
  - discussions[0].evidence
  evidence_ids:
  - record
  - wrong-parm
  - polka2009
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/alfa_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Incorrect evidence identity, ontology relationship or structure
    composition.
- finding_id: F2
  issue_key: alfa-filament-hierarchy-parthood
  category: identity
  severity: major
  status: open
  certainty: confirmed
  title: Separate AlfA filament class from cytoskeleton parthood
  description: The record asserts AlfA filament is-a GO:0005856 cytoskeleton, the
    complete framework. GO:0099513 polymeric cytoskeletal fiber is the appropriate
    broader filament class and is itself part_of cytoskeleton. The identifier guidance
    incorrectly calls the whole cytoskeleton the parent of a minted filament and can
    reproduce the error.
  target_ids:
  - cellstructuremech:alfa_filament
  field_paths:
  - parent_structures
  - part_of
  - evidence
  - docs/CURATION.md#identifiers
  evidence_ids:
  - record
  - go
  - polka2009
  - rules
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/alfa_filament.yaml
    role: maintained scientific record
  - repository: CultureBotAI/CellStructureMech
    path: docs/CURATION.md
    role: maintained identifier and hierarchy guidance
  rule_id: docs/CURATION.md
  native_severity: major
  normalization_reason: Incorrect evidence identity, ontology relationship or structure
    composition.
- finding_id: F3
  issue_key: alfa-becker-bibliographic-authors
  category: provenance
  severity: minor
  status: open
  certainty: confirmed
  title: Correct the Becker 2006 author attribution
  description: The bibliographic note names Becker, Moller-Jensen, Jensen and Gerdes.
    The inspected article author list instead names Becker, Herrera, Gunderson, Derman,
    Dance, Sims, Larsen and Pogliano. The DOI and biological claim are valid; the
    attached authors are not.
  target_ids:
  - cellstructuremech:alfa_filament
  field_paths:
  - evidence[0].notes
  evidence_ids:
  - record
  - becker
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/alfa_filament.yaml
    role: maintained scientific record
  rule_id: docs/CURATION.md
  native_severity: minor
  normalization_reason: Bounded bibliographic or append-only provenance defect; biological
    identity remains valid.
actions:
- action_id: A1
  description: Replace the ParM DOI with the intended AlfA paper
  finding_ids:
  - F1
  target_ids:
  - cellstructuremech:alfa_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/alfa_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Replace all four mistaken DOI occurrences and correct the journal without changing
    the AlfA claim scope.
  - Preserve discussion rationale, unresolved family grounding and the previously
    repaired AlfB-parN graph.
  - Use guarded curation, append Codex curation and EDIT history, retain PROPOSED,
    previous histories/reviews and discussion rationale; regenerate affected products
    and pass focused tests plus native QC.
- action_id: A2
  description: Separate AlfA filament class from cytoskeleton parthood
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:alfa_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/alfa_filament.yaml
    role: maintained scientific record
  - repository: CultureBotAI/CellStructureMech
    path: docs/CURATION.md
    role: maintained identifier and hierarchy guidance
  acceptance_checks:
  - Use GO:0099513 as the broader is-a parent and GO:0005856 as part_of, retaining
    cellstructuremech:alfa_filament identity.
  - Correct the misleading filament identifier example in CURATION.md without rewriting
    or claiming review of other filament records.
  - Use guarded curation, append Codex curation and EDIT history, retain PROPOSED,
    previous histories/reviews and discussion rationale; regenerate affected products
    and pass focused tests plus native QC.
- action_id: A3
  description: Correct the Becker 2006 author attribution
  finding_ids:
  - F3
  target_ids:
  - cellstructuremech:alfa_filament
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/alfa_filament.yaml
    role: maintained scientific record
  acceptance_checks:
  - Replace the incorrect explicit author list with the verified list or Becker et
    al. 2006, retaining title, journal and DOI.
  - Use guarded curation, append Codex curation and EDIT history, retain PROPOSED,
    previous histories/reviews and discussion rationale; regenerate affected products
    and pass focused tests plus native QC.
limitations:
- Same-agent assessment; no independent or human sign-off and no promotion of PROPOSED.
- Identifier check has 251 skipped identifiers; label check has 603 pairs without
  adapters. Exact target authorities were inspected separately; global skipped namespaces
  are not certified.
- Full QC uses the verified exact-baseline merge-group CI run. No raw experimental
  data or movies were reanalysed.
- Europe PMC fullTextXML failed for several sources; official PMC full HTML supplied
  the readable fallback. Access tiers are specified per source below.
- The broader AlfA filament query is a nonexhaustive 100-result lexical search; the
  exact AlfA query is complete. No claim that all ontology synonyms were exhaustively
  excluded. AlfA family grounding remains reviewed-label-only.
```
