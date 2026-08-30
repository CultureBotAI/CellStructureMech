---
name: source-queue
description: Work the prioritised data-source queue — pick the next source, canary one item, record the outcome, keep docs/SOURCE_QUEUE.md current. Use when asked what to ingest next, to add or re-rank a source, or to start pulling data from a source.
---

# Working the source queue

`docs/SOURCE_QUEUE.md` is the single ranked list of external sources and
their status. Everything else — research notes, issues, PRs — is evidence
for it. Never keep a private ranking in your head or in a chat reply.

## When asked "what next?"

1. Read `docs/SOURCE_QUEUE.md`. Answer from the table: the first `ACTIVE`
   row, else the first `READY` row. Quote its constraint and the issue.
2. Verify the status is still true with a live check before acting
   (`gh issue view`, a HEAD request to the source, `just report`). Notes go
   stale; a `BLOCKED` site may be back, a `READY` API may have been retired
   (PMC's OA service was, in Feb 2026).

## When starting on a source

1. Branch first. Open or reference the issue for it.
2. **Read the constraint column and honour it literally** — licence
   (hostable vs link-only, see docs/CURATION.md § Images), rate limits,
   User-Agent, "cite, do not redistribute".
3. **Canary one item end to end** on the same path the batch will use:
   fetch → read licence / taxon / identifier from the source's *machine-
   readable* metadata, not from a research note → write through
   `write_validated_structure` with a `record_curation_event` → `just render`
   → `just qc`. Confirm the side effects (file on disk, hash recorded, page
   renders, links resolve). Only then do more, one at a time or in a
   dry-run-first batch.
   Run `just qc` bare and read its exit code — never through a pipe
   (`| grep …` returns grep's status, and a failing suite was committed and
   pushed that way in PR #39).
4. **Never write a CURIE, accession or URL from memory.** Resolve it (OLS,
   Crossref, RCSB, the source API) in the same script that writes it. Three
   guessed identifiers reached PR #1 this way and one guessed download URL
   reached PR #33; the gate and review caught them, the rule is cheaper.
5. If the source's real behaviour differs from the queue row, fix the row in
   the same PR and say so in the PR body.

## When adding or re-ranking a source

1. Assess it first: licence (quote the wording), per-item identifier, taxon
   linkage, publication linkage, API, and two verified example items. Put the
   assessment in `research/<date>-<topic>.md` with a **Sources** section of
   URLs — a note without URLs was a review finding (#32).
2. Add the row with a status from the legend and a link to the note. Rank by
   the rule at the top of the queue file; a licence failure sinks a source
   regardless of everything else.
3. Open the tracking issue and link it from the row.

## When a source changes status

Edit the row, link the PR/issue that changed it, and mention it in the PR
body. `DONE` means the corpus uses it *and* a repeatable script exists —
a one-off hand pull is `READY`, not `DONE`.

## Do not

- Merge, or promote a record to `REVIEWED` — both are the owner's calls.
- Host anything under CC BY-NC / ND / unknown licence.
- Bulk-fetch before the canary, or scrape a site whose policy forbids it.
