# Record review of primosome complex (GO:1990077): PMID:8663105 and PMID:21856207 bibliographic note misattributions and curation_history graph_id mismatch

- Review: 20261025T071002Z-primosome-complex-pmid-citation-misattribution
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T06:55:20Z
- Finished UTC: 2026-10-25T07:10:02Z
- Reviewer: antigravity-c3s4-record-review (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Primosome complex (GO:1990077, data/structures/other/primosome_complex.yaml) has accurate GO cellular-component identity, Escherichia coli K-12 DnaB/DnaG/DnaC and template DNA composition, and verified UniProtKB protein examples (P0ACB0, P0ABS5, P0AEF0). However, PMID:8663105 (which is Ng JY and Marians KJ 1996, 'The ordered assembly of the phiX174-type primosome. II. Preservation of primosome composition from assembly through replication', J Biol Chem 271(26):15649-15655, as cited in GO:1990077 and dnab_dnac_dnat_pria_prib_complex.yaml) is misattributed in notes across components[0].evidence[1], components[0].protein_examples[0].evidence[0], components[1].evidence[1], components[1].protein_examples[0].evidence[0], functions[0].evidence[1], evidence[2], causal_graphs[0].edges[2].evidence[0], and causal_graphs[0].edges[4].evidence[1] to 'Tougu K and Marians KJ 1996, The interaction between helicase and primase sets the replication fork clock'; and PMID:21856207 (Kaguni JM 2011, Curr Opin Chem Biol 15:606-613, DOI:10.1016/j.cbpa.2011.07.016) is misattributed in components[2].evidence[0].notes to 'Briggs et al. 2012 (and Marians 2000)'. Additionally, curation_history[1].changes cites graph_id 'primosome_assembly_and_priming' whereas causal_graphs[0].graph_id is 'primosome_primer_synthesis'.

## Scope And Provenance

Single-record audit of primosome complex (GO:1990077) covering identity, composition, evidence notes, causal graphs, and curation history.

Selection: Targeted single-record review of new Cycle 3 Stage 1 record data/structures/other/primosome_complex.yaml.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 83ec9d5184fb203d87d8c3bd7043792d385193bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990077 | data/structures/other/primosome_complex.yaml | maintained | primosome complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on primosome_complex.yaml | passed | True | GO:1990077 | No LinkML schema issues found for primosome_complex.yaml. |
| Strict instance validator on primosome_complex.yaml | passed | True | GO:1990077 | Zero strict validator errors on primosome_complex.yaml. |

## Scientific And Domain Assessments

### GO cellular-component identity and E. coli K-12 subunit composition of primosome complex (GO:1990077)

identity: supported. Targets: GO:1990077.

GO:1990077 identity, parent/part_of hierarchy, DnaB/DnaG/DnaC and template_dna components, and E. coli K-12 UniProtKB protein examples (P0ACB0, P0ABS5, P0AEF0) are accurately grounded.

### Bibliographic citation notes for PMID:8663105 and PMID:21856207 and curation_history causal_graph ID

evidence: concern. Targets: GO:1990077.

PMID:8663105 (Ng &amp; Marians 1996) is misattributed to Tougu &amp; Marians 1996, PMID:21856207 (Kaguni 2011) is misattributed to Briggs et al. 2012, and curation_history[1].changes cites primosome_assembly_and_priming instead of primosome_primer_synthesis.

## Findings

### F1: primosome_complex.yaml misattributes PMID:8663105 and PMID:21856207 in evidence notes and cites a mismatched graph_id in curation_history[1].changes

major / open / confirmed; issue key: primosome-complex-pmid-citation-and-graph-id.

In data/structures/other/primosome_complex.yaml (GO:1990077), PMID:8663105 (which is Ng JY and Marians KJ 1996, 'The ordered assembly of the phiX174-type primosome. II. Preservation of primosome composition from assembly through replication', J Biol Chem 271(26):15649-15655, the GO:1990077 definition reference also cited in dnab_dnac_dnat_pria_prib_complex.yaml) is misattributed in notes across components[0].evidence[1].notes, components[0].protein_examples[0].evidence[0].notes, components[1].evidence[1].notes, components[1].protein_examples[0].evidence[0].notes, functions[0].evidence[1].notes, evidence[2].notes, causal_graphs[0].edges[2].evidence[0].notes, and causal_graphs[0].edges[4].evidence[1].notes to 'Tougu K and Marians KJ 1996, The interaction between helicase and primase sets the replication fork clock'; and PMID:21856207 (Kaguni JM 2011, 'Replication initiation at the Escherichia coli chromosomal origin', Curr Opin Chem Biol 15(5):606-613, DOI:10.1016/j.cbpa.2011.07.016, the second GO:1990077 definition reference also cited in core_primosome_complex.yaml) is misattributed in components[2].evidence[0].notes to 'Briggs et al. 2012 (and Marians 2000)'. In addition, curation_history[1].changes (CURATED_CAUSAL_GRAPH) cites graph_id 'primosome_assembly_and_priming' whereas causal_graphs[0].graph_id is 'primosome_primer_synthesis'.

## Recommended Actions And Acceptance Checks

### A1

Update the bibliographic notes on PMID:8663105 (to Ng &amp; Marians 1996, J Biol Chem 271:15649-15655) and PMID:21856207 (to Kaguni 2011, Curr Opin Chem Biol 15:606-613) in data/structures/other/primosome_complex.yaml, align curation_history[1].changes to primosome_primer_synthesis, and record the update in history/records/primosome_complex/.

- .venv/bin/python scripts/validate_strict.py data/structures/other/primosome_complex.yaml --out /tmp/primosome_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_primosome_pmid_notes | data/structures/other/primosome_complex.yaml; evidence[2] (lines 161-163), components[0..2].evidence, functions[0].evidence[1], causal_graphs[0].edges[2,4], and curation_history[1].changes | supports | primosome_complex.yaml attributes PMID:8663105 (Ng &amp; Marians 1996) to Tougu &amp; Marians 1996 and PMID:21856207 (Kaguni 2011) to Briggs et al. 2012, and cites primosome_assembly_and_priming in curation_history[1].changes instead of primosome_primer_synthesis. |
| ev_schema_primosome | scripts/validate_strict.py; schema_primosome receipt | supports | linkml-validate exited 0 on primosome_complex.yaml. |
| ev_strict_primosome | scripts/validate_strict.py; strict_primosome receipt | supports | validate_strict.py exited 0 on primosome_complex.yaml. |

## Limits And Additional Notes

- Record edits are deferred to Cycle 3 Stage 5 (resolve_review_findings) per the Stage 4 review-only workflow contract.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T071002Z-primosome-complex-pmid-citation-misattribution
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Record review of primosome complex (GO:1990077): PMID:8663105 and PMID:21856207
  bibliographic note misattributions and curation_history graph_id mismatch'
started_at: '2026-10-25T06:55:20Z'
finished_at: '2026-10-25T07:10:02Z'
reviewer:
  identity: antigravity-c3s4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 3 Stage 4 record_review against committed
    git revision 83ec9d5184fb203d87d8c3bd7043792d385193bf without record edits in
    this stage.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: Primosome complex (GO:1990077, data/structures/other/primosome_complex.yaml)
  has accurate GO cellular-component identity, Escherichia coli K-12 DnaB/DnaG/DnaC
  and template DNA composition, and verified UniProtKB protein examples (P0ACB0, P0ABS5,
  P0AEF0). However, PMID:8663105 (which is Ng JY and Marians KJ 1996, 'The ordered
  assembly of the phiX174-type primosome. II. Preservation of primosome composition
  from assembly through replication', J Biol Chem 271(26):15649-15655, as cited in
  GO:1990077 and dnab_dnac_dnat_pria_prib_complex.yaml) is misattributed in notes
  across components[0].evidence[1], components[0].protein_examples[0].evidence[0],
  components[1].evidence[1], components[1].protein_examples[0].evidence[0], functions[0].evidence[1],
  evidence[2], causal_graphs[0].edges[2].evidence[0], and causal_graphs[0].edges[4].evidence[1]
  to 'Tougu K and Marians KJ 1996, The interaction between helicase and primase sets
  the replication fork clock'; and PMID:21856207 (Kaguni JM 2011, Curr Opin Chem Biol
  15:606-613, DOI:10.1016/j.cbpa.2011.07.016) is misattributed in components[2].evidence[0].notes
  to 'Briggs et al. 2012 (and Marians 2000)'. Additionally, curation_history[1].changes
  cites graph_id 'primosome_assembly_and_priming' whereas causal_graphs[0].graph_id
  is 'primosome_primer_synthesis'.
source:
  git_revision: 83ec9d5184fb203d87d8c3bd7043792d385193bf
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/other/primosome_complex.yaml
    sha256: 1db23064cd7e9ff602f2e3fc22f5b6af30896a20d962cfdc7d73c4291b4bfff8
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
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
scope:
  description: Single-record audit of primosome complex (GO:1990077) covering identity,
    composition, evidence notes, causal graphs, and curation history.
  selection: Targeted single-record review of new Cycle 3 Stage 1 record data/structures/other/primosome_complex.yaml.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990077
targets:
- target_id: GO:1990077
  path: data/structures/other/primosome_complex.yaml
  label: primosome complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1db23064cd7e9ff602f2e3fc22f5b6af30896a20d962cfdc7d73c4291b4bfff8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/primosome_complex.yaml
    role: maintained_record
checks:
- check_id: schema_primosome
  name: LinkML schema validation on primosome_complex.yaml
  status: passed
  required: true
  summary: No LinkML schema issues found for primosome_complex.yaml.
  target_ids:
  - GO:1990077
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/other/primosome_complex.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_schema_primosome
- check_id: strict_primosome
  name: Strict instance validator on primosome_complex.yaml
  status: passed
  required: true
  summary: Zero strict validator errors on primosome_complex.yaml.
  target_ids:
  - GO:1990077
  command: .venv/bin/python scripts/validate_strict.py data/structures/other/primosome_complex.yaml
    --out /tmp/primosome_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_primosome
evidence:
- evidence_id: ev_primosome_pmid_notes
  kind: record_content
  reference: data/structures/other/primosome_complex.yaml
  locator: evidence[2] (lines 161-163), components[0..2].evidence, functions[0].evidence[1],
    causal_graphs[0].edges[2,4], and curation_history[1].changes
  accessed_at: '2026-10-25T07:00:30Z'
  support: supports
  summary: primosome_complex.yaml attributes PMID:8663105 (Ng & Marians 1996) to Tougu
    & Marians 1996 and PMID:21856207 (Kaguni 2011) to Briggs et al. 2012, and cites
    primosome_assembly_and_priming in curation_history[1].changes instead of primosome_primer_synthesis.
  quote: "- reference: PMID:8663105\n  notes: Tougu K and Marians KJ 1996, 'The interaction\
    \ between helicase and primase\n    sets the replication fork clock.', J Biol\
    \ Chem."
  snapshot_sha256: 1db23064cd7e9ff602f2e3fc22f5b6af30896a20d962cfdc7d73c4291b4bfff8
- evidence_id: ev_schema_primosome
  kind: validation
  reference: scripts/validate_strict.py
  locator: schema_primosome receipt
  accessed_at: '2026-10-25T07:10:02Z'
  support: supports
  summary: linkml-validate exited 0 on primosome_complex.yaml.
  snapshot_sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- evidence_id: ev_strict_primosome
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict_primosome receipt
  accessed_at: '2026-10-25T07:10:02Z'
  support: supports
  summary: validate_strict.py exited 0 on primosome_complex.yaml.
  snapshot_sha256: 9decec6f9c3e08bc14595bd78798f05ec3e86b935d20ab3f20c8253a16bc611d
assessments:
- assessment_id: assess_primosome_identity
  area: identity
  topic: GO cellular-component identity and E. coli K-12 subunit composition of primosome
    complex (GO:1990077)
  outcome: supported
  summary: GO:1990077 identity, parent/part_of hierarchy, DnaB/DnaG/DnaC and template_dna
    components, and E. coli K-12 UniProtKB protein examples (P0ACB0, P0ABS5, P0AEF0)
    are accurately grounded.
  target_ids:
  - GO:1990077
  evidence_ids:
  - ev_schema_primosome
  - ev_strict_primosome
- assessment_id: assess_primosome_pmid_notes
  area: evidence
  topic: Bibliographic citation notes for PMID:8663105 and PMID:21856207 and curation_history
    causal_graph ID
  outcome: concern
  summary: PMID:8663105 (Ng & Marians 1996) is misattributed to Tougu & Marians 1996,
    PMID:21856207 (Kaguni 2011) is misattributed to Briggs et al. 2012, and curation_history[1].changes
    cites primosome_assembly_and_priming instead of primosome_primer_synthesis.
  target_ids:
  - GO:1990077
  evidence_ids:
  - ev_primosome_pmid_notes
findings:
- finding_id: F1
  issue_key: primosome-complex-pmid-citation-and-graph-id
  category: evidence
  severity: major
  status: open
  certainty: confirmed
  title: primosome_complex.yaml misattributes PMID:8663105 and PMID:21856207 in evidence
    notes and cites a mismatched graph_id in curation_history[1].changes
  description: In data/structures/other/primosome_complex.yaml (GO:1990077), PMID:8663105
    (which is Ng JY and Marians KJ 1996, 'The ordered assembly of the phiX174-type
    primosome. II. Preservation of primosome composition from assembly through replication',
    J Biol Chem 271(26):15649-15655, the GO:1990077 definition reference also cited
    in dnab_dnac_dnat_pria_prib_complex.yaml) is misattributed in notes across components[0].evidence[1].notes,
    components[0].protein_examples[0].evidence[0].notes, components[1].evidence[1].notes,
    components[1].protein_examples[0].evidence[0].notes, functions[0].evidence[1].notes,
    evidence[2].notes, causal_graphs[0].edges[2].evidence[0].notes, and causal_graphs[0].edges[4].evidence[1].notes
    to 'Tougu K and Marians KJ 1996, The interaction between helicase and primase
    sets the replication fork clock'; and PMID:21856207 (Kaguni JM 2011, 'Replication
    initiation at the Escherichia coli chromosomal origin', Curr Opin Chem Biol 15(5):606-613,
    DOI:10.1016/j.cbpa.2011.07.016, the second GO:1990077 definition reference also
    cited in core_primosome_complex.yaml) is misattributed in components[2].evidence[0].notes
    to 'Briggs et al. 2012 (and Marians 2000)'. In addition, curation_history[1].changes
    (CURATED_CAUSAL_GRAPH) cites graph_id 'primosome_assembly_and_priming' whereas
    causal_graphs[0].graph_id is 'primosome_primer_synthesis'.
  target_ids:
  - GO:1990077
  field_paths:
  - components[0].evidence[1].notes
  - components[0].protein_examples[0].evidence[0].notes
  - components[1].evidence[1].notes
  - components[1].protein_examples[0].evidence[0].notes
  - components[2].evidence[0].notes
  - functions[0].evidence[1].notes
  - evidence[2].notes
  - causal_graphs[0].edges[2].evidence[0].notes
  - causal_graphs[0].edges[4].evidence[1].notes
  - curation_history[1].changes
  evidence_ids:
  - ev_primosome_pmid_notes
  rule_id: docs/CURATION.md:evidence-reference-accuracy
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/primosome_complex.yaml
    role: maintained_record
  tags:
  - evidence
  - reference-attribution
  - curation-history
  - stage4-record-review
actions:
- action_id: A1
  description: Update the bibliographic notes on PMID:8663105 (to Ng & Marians 1996,
    J Biol Chem 271:15649-15655) and PMID:21856207 (to Kaguni 2011, Curr Opin Chem
    Biol 15:606-613) in data/structures/other/primosome_complex.yaml, align curation_history[1].changes
    to primosome_primer_synthesis, and record the update in history/records/primosome_complex/.
  finding_ids:
  - F1
  target_ids:
  - GO:1990077
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/other/primosome_complex.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py data/structures/other/primosome_complex.yaml
    --out /tmp/primosome_failures.tsv
  - .venv/bin/python scripts/validate_history.py
limitations:
- Record edits are deferred to Cycle 3 Stage 5 (resolve_review_findings) per the Stage
  4 review-only workflow contract.
tags:
- stage4
- record-review
- primosome-complex
```
