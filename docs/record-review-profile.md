# CellStructureMech review profile

New record reviews follow [the shared contract](record-reviews.md), with
authoritative YAML and derived Markdown under
`reviews/structured/<YYYYMMDDTHHMMSSZ>-<slug>/`. Historical ad hoc reports remain
historical evidence and need no migration. `conf/record_review.yaml` lists the
active routes and local rubrics.

## Routes and output

- `.claude/skills/review-yaml-record/SKILL.md`: one resolved record.
- `.claude/skills/review-yaml-category/SKILL.md`: a coherent category with
  explicit lump/split/retain/defer decisions; sampled coverage keeps its method,
  denominator, inspected members and limitations. Explicit batches use `kind: batch`.
- `.claude/skills/curate-yaml-record/SKILL.md`: the audit-only route uses the
  same output contract and retains the native scientific checklist.
- `.claude/skills/literature-evidence/SKILL.md`: source accessibility and
  quotation/claim evidence audits save their scoped final assessments.

Run from the repository root using its own Python environment (LinkML,
linkml-runtime, jsonschema and PyYAML; pytest in the dev extra):

```bash
uv run python scripts/record_review.py inspect --targets /tmp/review-targets.yaml
just review-validate /tmp/completed-review.yaml
just review-save /tmp/completed-review.yaml
just review-check
```

Use session-unique temporary inputs and add `--input <path>` to inspect for each
additional rubric/schema/source/overlay used. Retain the captured Git revision
and hashes. Checks record actual commands and exit codes, never invented
success. New observations are immutable; link both saved files in the final
response. Missing dependencies or required checks are an explicit blocked output
step or partial assessment, not permission to save unvalidated prose.

## Native questions and ownership

Review maintained `data/structures/` records for structure versus protein or
phenotype identity, GO cellular-component grounding, is-a versus parthood,
components and stoichiometry, taxonomic scope, functions/traits, imaging and
physical measurements, and edge-level causal evidence. Use
`docs/CURATION.md`, `docs/SCHEMA.md`, and the local checklist; retain experimental
context and evidence type in assessment dimensions.

The maintained structure YAML owns scientific changes; generated `pages/` does
not. Any later mutation uses `write_validated_structure`, a curation event and
the append-only repository history. Agent-authored records remain PROPOSED;
only a human curator can mark them REVIEWED. A saved review neither promotes
that status nor appends either history surface.

## Native checks

```bash
just validate <record-path>
just validate-strict <record-path>
just validate-products
just check-trait-links --check
just validate-history
just qc
```

Ontology and sibling checks may require their documented caches/network; record
unavailable checks explicitly. Literature readability scans and research notes
are inspection inputs, not completed scientific review. The native
`literature-evidence` workflow establishes access, source readability and
claim-level quotation support. Its final assessment uses the shared saver;
the record/category route covers the broader biological verdict.

## Validation and ownership of the contract

`schema/record_review.yaml`, `scripts/record_review.py`,
`docs/record-reviews.md`, and `tests/test_record_review_contract.py` are copied
byte-identically from CLAW. Canonical marked skill regions are rendered with
the native sections preserved. Edit the shared contract upstream and re-adopt;
the local profile, rubrics and scientific status gates remain repository-owned.
`just review-check` validates retained bundles and runs the profile/roundtrip
contract tests. The existing PR and merge-group quality workflow also runs the
contract test alongside its unchanged native checks. Zero structured reviews
means missing coverage, not a scientific pass. The new path is Git-visible
without opening ignored legacy report directories.

CI fetches full history and sets `RECORD_REVIEW_BASE` from the trusted PR base,
merge-group base, or push-before SHA. It requires that commit to exist before
running the canonical test, which rejects changes or deletions to previously
saved bundles. Local `just review-check` defaults to HEAD; set
`RECORD_REVIEW_BASE=<base-commit>` when checking a branch's committed changes.
There is no automatic CI fallback to an already modified HEAD.
