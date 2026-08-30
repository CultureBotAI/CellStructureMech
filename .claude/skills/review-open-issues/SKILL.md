---
name: review-open-issues
description: Sweep and triage the full open-issue queue for CellStructureMech. Fetches every open issue, checks each against main, the corpus, the source queue and the research notes, flags duplicates and already-fixed items, and assigns a priority tier (P0 silently wrong data or a licence breach, P1 real-but-schedulable, P2 process/doc, P3 backlog). Produces a short ranked report; only touches GitHub when asked. Use when asked to "review issues", "prioritize the backlog", "triage open issues", or after a review pass has filed a batch of new issues.
tools: Bash, Read
category: workflow
requires_database: false
requires_internet: true
version: 1.0.0
---

# Review & Prioritize Open Issues

Adapted from the `review-open-issues` skill in PFASCommunityAgents, which was
itself adapted from the Mech repos. The method and the read-only default are
unchanged; what a check consists of is specific to this repository: a small,
fully-committed, generated-and-gated knowledge base whose issues are about
records, identifiers, licences and pipeline gates rather than bench data.

## Overview

**Purpose**: an honest, current ranking of the whole open-issue queue.

**When NOT to use**: for choosing the next *data source* — that is the
`source-queue` skill and `docs/SOURCE_QUEUE.md`. This skill ranks issues; it
does not implement fixes, merge, or promote records.

## What makes this repo different

**1. Everything is on disk and checkable.** There is no hidden campaign data:
records, images, pages, research notes and the source queue are all committed.
So "cannot verify" is rarely honest here; the honest failure is *did not look*.
Every data-shaped verdict should cite the file, the `just report` line, or the
live lookup that established it.

**2. The dominant defect is a plausible identifier that does not resolve.**
Three CURIEs and one download URL written from memory reached PRs #1 and #33
before verification caught them. An issue that names a CURIE, DOI, accession
or URL is checked by *resolving it* (OLS, Crossref, RCSB, the source API), not
by reading it.

**3. Generated artifacts are gated, so drift is loud, not silent.** `pages/`,
the README statistics block and `reports/` are rebuilt by `just render`,
`just docs-stats` and `just report`; `just qc` fails on drift. An issue about a
stale page or count is usually already fixed by the next render — check
`just qc` before believing it.

**4. Records are `PROPOSED` until a human reads them.** Every record so far was
LLM-drafted. An issue alleging a wrong fact in a record is a candidate for
#7-style human review, not something to "fix" by a second LLM pass; say which.

**5. Licence is a hard constraint, not a severity.** Anything that would host a
CC BY-NC / ND / unlicensed image, or redistribute EcoCyc/SubtiWiki content, is
P0 regardless of how small the change is. `docs/SOURCE_QUEUE.md` holds the
constraint per source.

## Workflow

### Step 1 — Fetch the full open-issue queue

```bash
queue_file="${TMPDIR:-/tmp}/csm-open-issues.json"
gh issue list -R CultureBotAI/CellStructureMech --state open --limit 5000 \
  --json number,title,body,labels,comments,createdAt,updatedAt > "$queue_file"
jq -r '.[] | [.number, .createdAt[:10], (.labels|map(.name)|join(",")), .title] | @tsv' "$queue_file"
jq length "$queue_file"
```

`--limit` caps silently; print `jq length` and say whether coverage was
complete. Read bodies and comments from the JSON — a "fixed already" note is
usually a comment.

### Step 2 — Establish the state of the tree

Once, before checking anything:

```bash
git fetch origin main && git status -sb | head -1
just report                     # live counts; never quote a number from prose
just qc                         # run BARE — a pipe hides the exit code (PR #39)
```

If `just qc` fails on `main`, that is the first finding and every other verdict
is provisional until it is explained.

Then classify each issue:

- **Verifiable now** — about a file, record, identifier or page in the tree, or
  an identifier that can be resolved live.
- **Decision** — needs the owner (policy, licence interpretation, scope). Say
  what the options are; do not rank it as work.
- **Human review** — alleges a factual error in a `PROPOSED` record; belongs
  to the human-review track.
- **External** — depends on a source being reachable or a licence being
  clarified (ETDB-Caltech, SubtiWiki). Re-check reachability now; sources have
  changed status during this project (PMC's OA service was retired Feb 2026).

### Step 3 — Group and dedupe

Issues filed from one review pass overlap. Group by PR reference, module, or
the same failure shape, and report a group as one item.

The recurring **families** here:

- **A guessed identifier** — a pattern-valid CURIE/URL that does not resolve
  (#2, #4, #34). Fix is always "resolve it in the same script that writes it".
- **A gate that does not see the failure** — validation passes but the site
  breaks or the fact is wrong (#21 broken links, #6 unresolvable CURIEs, #11
  cross-repo ids). Fix is a test, not a data edit.
- **Provenance a reader cannot follow** — a research note without URLs (#32),
  boilerplate evidence notes (#41), an image without its hash (#24).
- **Policy pushed into data** — a test forcing strain rows into
  `taxonomic_distribution` (#36), reference-required excluding public-domain
  images (#30). Fix is a schema/test decision, flag for the owner.
- **Image storage costs** — duplication (#31), size (#26).

### Step 4 — Check each issue against current reality

- **Already fixed on main?** This repo uses **merge commits**, so the PR number
  is in the merge subject and the fixing commit is a parent:
  `git log --oneline origin/main --perl-regexp --grep "#<N>\b"`. The `\b`
  matters (`#4` also matches `#40`). Do not use `--all`.
- **Closed by a merged PR but still open?** Happens here: GitHub honours only
  the first issue in `Closes #A, #B, #C` (#3–#5 and #18–#20 stayed open after
  their PRs merged). `gh issue view <N> --json closedByPullRequestsReferences`,
  then check `mergedAt`.
- **Identifier claims** — resolve them: OLS `api/ontologies/<onto>/terms?obo_id=`,
  Crossref `api.crossref.org/works/<doi>`, RCSB `data.rcsb.org/rest/v1/core/entry/`,
  Commons `action=query&prop=imageinfo&iiprop=extmetadata`.
- **Still reproducible?** If the issue cites a script, test or field, confirm
  it still exists in that shape — the schema has moved fast (`images`,
  `parent_structures`, `file_sha256` all arrived after PR #1).
- **Title still true?** Counts in titles drift; re-derive with `just report`.
- **Source status changed?** Cross-check against `docs/SOURCE_QUEUE.md`; an
  issue about a `BLOCKED` source may have become actionable, or vice versa.

### Step 5 — Assign priority

Labels are `P0`–`P3` plus `decision` and `human-review`. If the labels do not
exist yet, creating them is a write — ask first.

- **P0 — silently wrong data, or a licence breach.** A CURIE/DOI/taxon that
  resolves to the wrong thing, an image hosted under a licence that forbids
  it, a page that renders a claim the record does not make. Rare.
- **P1 — real, schedulable.** A gate gap that would let a P0 through (#6,
  #11), a missing test with a known failure, a content gap the tooling has
  surfaced (#40 unmatched proteins).
- **P2 — process or doc.** Drift, boilerplate, conventions, action pinning.
- **P3 — backlog.** Real but unscheduled.
- **`decision`** and **`human-review`** are orthogonal to severity; label them
  so nobody picks them up expecting to finish.

If more than ~10% land P0, recalibrate. An issue open a month that hurts
nobody is P3 however it is worded.

### Step 6 — Present the report

- Ranked list, P0 first, one line per issue or group: number, one-sentence why.
- Separate **fixed in code**, **needs a decision**, **needs a human reader**
  and **still open** — four different states.
- Issues recommended for closing, each with evidence: a commit, a merged PR,
  or a live lookup. Never "this looks done".
- **Top 2–3 to act on next**, with reasoning, and whether each is a branch of
  work or a source-queue item (hand those to `source-queue`).
- Count reviewed; state whether coverage was complete; state what `just qc`
  said on `main`.

### Step 7 — Act only when asked

Read-only by default. A general "yes" is not approval for an unattended close
loop.

- **Closing**: confirm the numbers first, then
  `gh issue close <N> -c "<evidence>"`, one at a time.
- **Relabelling**: batch it, say what changed.
- **Retitling** a drifted count: the comment says what it was and why it moved.

## Conventions this skill enforces

- **Full-queue coverage, not first-page sampling.** State the count.
- **Resolve, don't read.** Any identifier in an issue is checked live.
- **Evidence over vibes.** Every CLOSE / duplicate / fixed verdict cites a
  commit, PR, file, or lookup.
- **Licence findings are P0.**
- **Decisions and human review are labelled, not ranked as work.**
- **Read-only by default.**
- No @-mentions in comments without explicit per-mention authorization.

## Related

- `source-queue` — the ranked *data-source* queue; this skill hands source
  work to it.
- `just report`, `just qc` — Step 2 depends on both.
- `docs/CURATION.md` — what a correct record looks like; the yardstick for
  factual issues.
- `research/` — the evidence behind source-status claims.
