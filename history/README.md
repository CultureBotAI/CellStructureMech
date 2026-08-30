# Curation history

Append-only provenance for curation sessions. **One record per change** — per
target for hand curation, per *migration* for a bulk edit. Written once and
**never edited afterwards**; corrections go in a new record that references the
old one in its `details`.

```
history/<kind-dir>/<slug>/<TIMESTAMP>-<actor>-<shortid>.yaml
```

The schema (`src/cellstructuremech/schema/history.yaml`) and the scaffolder's
contract are vendored from culturebotai-claw; the conventions below are this
repository's.

## Why this exists

Per-record `curation_history` says what changed inside one record. It cannot
say that a source's licence was re-read at the source, that a gate was adopted
and what it found, or that a review deliberately changed nothing. Git says a
commit happened; it does not say which model, using which tool, changed what,
why, and under which issue. That gap matters more as agents do the changing.

## Why the layout looks like that

Directory-per-slug plus an unguessable `shortid`: two agents working the same
structure concurrently cannot write the same file, so this layer has **no
merge-conflict surface**. A shared changelog would conflict on every parallel PR.

## Writing a record

Do not hand-write the filename or timestamp — scaffold it:

```bash
just new-history --kind record --slug carboxysome \
  --target-root data/structures/microcompartment \
  --event EDIT --outcome changed \
  --sections components,images \
  --summary "Seed protein examples from UniProt SL and add the Commons micrograph" \
  --model claude-fable-5 --agent-tool claude-code \
  --issue https://github.com/CultureBotAI/CellStructureMech/issues/28 \
  --details "What was done, what evidence was used, how it was validated."
```

Omit `--details` and you get a TODO placeholder — `just validate-history`
**fails** while it is still there, so an unfilled record cannot slip through.
The command prints the record path as its final stdout line.

`--kind record` and `--kind schema` derive the target path from `--slug` plus
`--target-root`. Every other kind should pass an explicit `--path`: only those
two are reliably `.yaml` (a source-queue change is a `.tsv`, a research note an
`.md`, infrastructure a justfile or workflow).

Then validate and stage:

```bash
just validate-history history/records/carboxysome/<file>.yaml
git add history/
```

## The vocabulary

`event`: `CREATE` · `EDIT` · `REVIEW` · `AUDIT` · `GENERAL`

`outcome`: `changed` · `no_change` · `needs_followup` · `blocked`

Outcome is **orthogonal** to event on purpose. A `REVIEW` that found nothing is
`no_change` — a real result, because it says something was checked. An `EDIT`
that hit a wall is `blocked`, and `details` must say what the wall was so the
next session does not rediscover it.

`kind`: `record` · `schema` · `mapping` · `report` · `infrastructure` · `other`
(`other` requires an explicit `--path`).

## One record per CHANGE, not per file

For hand curation the session and the target coincide: one structure is
reasoned about and one record is written. For a mechanical change across many
records — a re-render, a bulk grounding fix, a schema migration — write **one
record for the migration**, with `--kind infrastructure` or `--kind schema` and
the script as the target. A record per touched file would bury the reasoning in
copies of itself.

| what happened | `--kind` | target |
|---|---|---|
| one structure, curated | `record` | that structure's YAML |
| a bulk edit across records | `infrastructure` | the script that made it |
| a schema change | `schema` | the schema file |
| a source adopted or re-ranked | `other` | `curation/source_queue.tsv` |
| a research note | `other` | the note under `research/` |

## What is checked

`just validate-history` (inside `just qc`) validates every record against the
vendored schema and checks that its links resolve to this repository. Records
are append-only by convention, not by a gate; a corrected record is a new
record that names the old one.
