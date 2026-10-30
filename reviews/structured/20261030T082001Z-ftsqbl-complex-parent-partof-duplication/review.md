# Record review of FtsQBL complex (GO:1990587): duplicate GO:1990586 in parent_structures and part_of

- Review: 20261030T082001Z-ftsqbl-complex-parent-partof-duplication
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-30T08:05:00Z
- Finished UTC: 2026-10-30T08:20:01Z
- Reviewer: antigravity-c4s4-record-review (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

FtsQBL complex (GO:1990587, data/structures/division_machinery/ftsqbl_complex.yaml) has accurate GO cellular-component identity, heterotrimeric FtsQ/DivIB-FtsB/DivIC-FtsL subunit composition (UniProtKB:P06136, P0A6S5, P0AEN4 in Escherichia coli K-12 and UniProtKB:P16655, P37471, Q06006 in Bacillus subtilis 168), and source-backed divisome allosteric regulation causal graph (PMID:15547266, PMID:29379009, PMID:37095708). However, GO:1990586 (divisome complex) is placed simultaneously in parent_structures (is-a) and part_of (parthood), whereas in Gene Ontology GO:1990587 is an is_a child of GO:1990586 (any protein complex involved in bacterial cell division) with no part_of edge to GO:1990586, matching sibling ftsbl_complex.yaml (GO:1990588).

## Scope And Provenance

Single-record audit of FtsQBL complex (GO:1990587) covering ontology identity, parent_structures/part_of/has_part hierarchy, subunit composition, protein examples, and causal graphs.

Selection: Targeted single-record review of new Cycle 4 Stage 1 record data/structures/division_machinery/ftsqbl_complex.yaml.
Coverage: full; 1 reviewed / 1 in the declared population.
Source: git_commit at Git base 5c642e4080ef3a0f026845843c559d3b46de8871.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:1990587 | data/structures/division_machinery/ftsqbl_complex.yaml | maintained | FtsQBL complex |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| LinkML schema validation on ftsqbl_complex.yaml | passed | True | GO:1990587 | No LinkML schema issues found for ftsqbl_complex.yaml. |
| Strict instance validator on ftsqbl_complex.yaml | passed | True | GO:1990587 | Zero strict validator errors on ftsqbl_complex.yaml. |

## Scientific And Domain Assessments

### GO:1990587 identity, FtsQ/FtsB/FtsL subunit composition, and FtsWI activation causal graph

representation: supported. Targets: GO:1990587.

GO:1990587 identity, FtsQ/DivIB, FtsB/DivIC, and FtsL subunit groundings (InterPro:IPR005548, IPR007157, IPR018190), E. coli and B. subtilis UniProtKB protein_examples, and PMID:15547266 / PMID:29379009 / PMID:37095708 citations are verified.

### Disjointness of parent_structures (is-a) and part_of (parthood) for GO:1990586

representation: concern. Targets: GO:1990587.

GO:1990586 (divisome complex) is listed in both parent_structures and part_of; in GO, GO:1990587 is an is_a child of GO:1990586 with no part_of edge.

## Findings

### F1: ftsqbl_complex.yaml lists GO:1990586 (divisome complex) in both parent_structures and part_of

major / open / confirmed; issue key: ftsqbl-complex-parent-partof-duplication.

In data/structures/division_machinery/ftsqbl_complex.yaml (GO:1990587, lines 12-16), GO:1990586 (divisome complex) is placed in both parent_structures (is-a) and part_of (parthood). In Gene Ontology, GO:1990587 (FtsQBL complex) is a direct rdfs:subClassOf (is_a) child of GO:1990586 ('Any protein complex involved in bacterial cell division') and has no BFO:0000050 (part_of) relationship to GO:1990586, matching sibling data/structures/division_machinery/ftsbl_complex.yaml (GO:1990588), which lists GO:1990586 only in parent_structures and GO:1990587 in part_of.

## Recommended Actions And Acceptance Checks

### A1

Remove part_of: [GO:1990586] from data/structures/division_machinery/ftsqbl_complex.yaml while retaining parent_structures: [GO:1990586, GO:0098797] and has_part: [GO:1990588], and record the curation event and history ledger entry.

- .venv/bin/python scripts/validate_strict.py data/structures/division_machinery/ftsqbl_complex.yaml --out /tmp/ftsqbl_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries


## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_ftsqbl_hierarchy_dup | data/structures/division_machinery/ftsqbl_complex.yaml; parent_structures and part_of (lines 12-16) | supports | ftsqbl_complex.yaml lists GO:1990586 (divisome complex) in both parent_structures and part_of. |
| ev_schema_ftsqbl | scripts/validate_strict.py; schema_ftsqbl receipt | supports | linkml-validate exited 0 on ftsqbl_complex.yaml. |
| ev_strict_ftsqbl | scripts/validate_strict.py; strict_ftsqbl receipt | supports | validate_strict.py exited 0 on ftsqbl_complex.yaml. |

## Limits And Additional Notes

- Record edits are deferred to Cycle 4 Stage 5 (resolve_review_findings) per the Stage 4 review-only workflow contract.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T082001Z-ftsqbl-complex-parent-partof-duplication
kind: record
repository: CultureBotAI/CellStructureMech
title: 'Record review of FtsQBL complex (GO:1990587): duplicate GO:1990586 in parent_structures
  and part_of'
started_at: '2026-10-30T08:05:00Z'
finished_at: '2026-10-30T08:20:01Z'
reviewer:
  identity: antigravity-c4s4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 4 Stage 4 record_review against committed
    git revision 5c642e4080ef3a0f026845843c559d3b46de8871 without record edits in
    this stage.
skill: .claude/skills/review-yaml-record/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: FtsQBL complex (GO:1990587, data/structures/division_machinery/ftsqbl_complex.yaml)
  has accurate GO cellular-component identity, heterotrimeric FtsQ/DivIB-FtsB/DivIC-FtsL
  subunit composition (UniProtKB:P06136, P0A6S5, P0AEN4 in Escherichia coli K-12 and
  UniProtKB:P16655, P37471, Q06006 in Bacillus subtilis 168), and source-backed divisome
  allosteric regulation causal graph (PMID:15547266, PMID:29379009, PMID:37095708).
  However, GO:1990586 (divisome complex) is placed simultaneously in parent_structures
  (is-a) and part_of (parthood), whereas in Gene Ontology GO:1990587 is an is_a child
  of GO:1990586 (any protein complex involved in bacterial cell division) with no
  part_of edge to GO:1990586, matching sibling ftsbl_complex.yaml (GO:1990588).
source:
  git_revision: 5c642e4080ef3a0f026845843c559d3b46de8871
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-record/SKILL.md
    sha256: 0d7a6cb0c6d72c42fc24335c8b587a15c12d5764ff27270112a814e2e0e3d550
    role: context
  - path: AGENTS.md
    sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/division_machinery/ftsqbl_complex.yaml
    sha256: c6563e47cef93b8807aaebfdd48e746d54d985e1b42f35b1ff42f0eab32e296a
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
  description: Single-record audit of FtsQBL complex (GO:1990587) covering ontology
    identity, parent_structures/part_of/has_part hierarchy, subunit composition, protein
    examples, and causal graphs.
  selection: Targeted single-record review of new Cycle 4 Stage 1 record data/structures/division_machinery/ftsqbl_complex.yaml.
  coverage: full
  population_size: 1
  reviewed_target_ids:
  - GO:1990587
targets:
- target_id: GO:1990587
  path: data/structures/division_machinery/ftsqbl_complex.yaml
  label: FtsQBL complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c6563e47cef93b8807aaebfdd48e746d54d985e1b42f35b1ff42f0eab32e296a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/ftsqbl_complex.yaml
    role: maintained_record
checks:
- check_id: schema_ftsqbl
  name: LinkML schema validation on ftsqbl_complex.yaml
  status: passed
  required: true
  summary: No LinkML schema issues found for ftsqbl_complex.yaml.
  target_ids:
  - GO:1990587
  command: .venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml
    --target-class CellStructureRecord data/structures/division_machinery/ftsqbl_complex.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_schema_ftsqbl
- check_id: strict_ftsqbl
  name: Strict instance validator on ftsqbl_complex.yaml
  status: passed
  required: true
  summary: Zero strict validator errors on ftsqbl_complex.yaml.
  target_ids:
  - GO:1990587
  command: .venv/bin/python scripts/validate_strict.py data/structures/division_machinery/ftsqbl_complex.yaml
    --out /tmp/ftsqbl_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_ftsqbl
evidence:
- evidence_id: ev_ftsqbl_hierarchy_dup
  kind: record_content
  reference: data/structures/division_machinery/ftsqbl_complex.yaml
  locator: parent_structures and part_of (lines 12-16)
  accessed_at: '2026-10-30T08:10:00Z'
  support: supports
  summary: ftsqbl_complex.yaml lists GO:1990586 (divisome complex) in both parent_structures
    and part_of.
  quote: 'parent_structures:

    - GO:1990586

    - GO:0098797

    part_of:

    - GO:1990586

    has_part:

    - GO:1990588'
  snapshot_sha256: c6563e47cef93b8807aaebfdd48e746d54d985e1b42f35b1ff42f0eab32e296a
- evidence_id: ev_schema_ftsqbl
  kind: validation
  reference: scripts/validate_strict.py
  locator: schema_ftsqbl receipt
  accessed_at: '2026-10-30T08:20:01Z'
  support: supports
  summary: linkml-validate exited 0 on ftsqbl_complex.yaml.
  snapshot_sha256: de6087f4be8c0adc015333597cd864406ad889bbde42d9ee20db0df5932bb2de
- evidence_id: ev_strict_ftsqbl
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict_ftsqbl receipt
  accessed_at: '2026-10-30T08:20:01Z'
  support: supports
  summary: validate_strict.py exited 0 on ftsqbl_complex.yaml.
  snapshot_sha256: 298cea07de69fca5249f132fc504b10be4e8c238680e452544c4bbf093408b42
assessments:
- assessment_id: assess_ftsqbl_composition
  area: representation
  topic: GO:1990587 identity, FtsQ/FtsB/FtsL subunit composition, and FtsWI activation
    causal graph
  outcome: supported
  summary: GO:1990587 identity, FtsQ/DivIB, FtsB/DivIC, and FtsL subunit groundings
    (InterPro:IPR005548, IPR007157, IPR018190), E. coli and B. subtilis UniProtKB
    protein_examples, and PMID:15547266 / PMID:29379009 / PMID:37095708 citations
    are verified.
  target_ids:
  - GO:1990587
  evidence_ids:
  - ev_schema_ftsqbl
  - ev_strict_ftsqbl
- assessment_id: assess_ftsqbl_hierarchy
  area: representation
  topic: Disjointness of parent_structures (is-a) and part_of (parthood) for GO:1990586
  outcome: concern
  summary: GO:1990586 (divisome complex) is listed in both parent_structures and part_of;
    in GO, GO:1990587 is an is_a child of GO:1990586 with no part_of edge.
  target_ids:
  - GO:1990587
  evidence_ids:
  - ev_ftsqbl_hierarchy_dup
findings:
- finding_id: F1
  issue_key: ftsqbl-complex-parent-partof-duplication
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: ftsqbl_complex.yaml lists GO:1990586 (divisome complex) in both parent_structures
    and part_of
  description: In data/structures/division_machinery/ftsqbl_complex.yaml (GO:1990587,
    lines 12-16), GO:1990586 (divisome complex) is placed in both parent_structures
    (is-a) and part_of (parthood). In Gene Ontology, GO:1990587 (FtsQBL complex) is
    a direct rdfs:subClassOf (is_a) child of GO:1990586 ('Any protein complex involved
    in bacterial cell division') and has no BFO:0000050 (part_of) relationship to
    GO:1990586, matching sibling data/structures/division_machinery/ftsbl_complex.yaml
    (GO:1990588), which lists GO:1990586 only in parent_structures and GO:1990587
    in part_of.
  target_ids:
  - GO:1990587
  field_paths:
  - parent_structures
  - part_of
  evidence_ids:
  - ev_ftsqbl_hierarchy_dup
  rule_id: docs/CURATION.md:parent_structures-vs-part_of
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/ftsqbl_complex.yaml
    role: maintained_record
  tags:
  - hierarchy
  - parent-structures
  - part-of
  - stage4-record-review
actions:
- action_id: A1
  description: 'Remove part_of: [GO:1990586] from data/structures/division_machinery/ftsqbl_complex.yaml
    while retaining parent_structures: [GO:1990586, GO:0098797] and has_part: [GO:1990588],
    and record the curation event and history ledger entry.'
  finding_ids:
  - F1
  target_ids:
  - GO:1990587
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/division_machinery/ftsqbl_complex.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py data/structures/division_machinery/ftsqbl_complex.yaml
    --out /tmp/ftsqbl_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
limitations:
- Record edits are deferred to Cycle 4 Stage 5 (resolve_review_findings) per the Stage
  4 review-only workflow contract.
tags:
- stage4
- record-review
- ftsqbl-complex
```
