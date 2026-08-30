---
name: source-queue
description: Triage and maintain CellStructureMech's prioritized data-source queue in curation/source_queue.tsv — rank candidate sources by the corpus gap they close, verify licence, per-item identifiers and taxon linkage before adoption, and fold in research findings. Use when asked what data source to add next, when evaluating a specific source, or after a research report lands; do not use as permission to fetch, seed, or adopt a source.
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 2.0.0
---

# Triage the data-source queue

`curation/source_queue.tsv` is the ranked list of data sources this corpus
draws on or might adopt. This skill keeps it honest and answers "what should
we add next?" with evidence rather than enthusiasm. Adapted from the
AntibioticMech skill of the same name; the ranking rule and the adoption gate
are theirs, the gaps and licence rules are this repository's.

## Read these first

- `curation/source_queue.tsv` — the queue; `docs/SOURCE_QUEUE.md` is its legend.
- `just source-queue` — the checker's verdict and its "next up" line.
- `just report` — which fields are actually empty, corpus-wide. A source that
  fills an empty column beats one that thickens a full one.
- `docs/CURATION.md` — the granularity contract, identifier policy and image
  rules; a source outside scope is a rejection, not a low priority.
- `conf/sources.yaml` — what the pipeline reads today.
- `research/` — the verified assessments behind the rows.

## The ranking rule

Rank by **what the corpus cannot currently assert**, not by how well known the
source is. In order:

1. **Does it close a stated gap?** Check `just report`. Today every record
   has components and an image; `protein_examples` exist on one record,
   `causal_graphs` on three, `physical_properties` are thin, and there are
   four records against a backlog of dozens (#12). A source that supplies
   *records* or *components with evidence* outranks one that supplies a
   second image.
2. **Can we redistribute it?** This is a hard gate. The corpus is CC0 and
   hosts image copies under `pages/`. `SEED` (copy into records or pages) is
   allowed only under `CC0_OK`, `ATTRIBUTION` or `SHARE_ALIKE`; `NONCOMMERCIAL`
   is `LINK_ONLY` at best (the Atlas); `RESTRICTED` is `CURATE_ONLY` (EcoCyc:
   cite, never copy); `UNVERIFIED` cannot be adopted. Record what the licence
   page says, not what it would take to make it work.

   The same tension AntibioticMech carries is open here: CC BY images and CC
   BY vocabularies sit inside a CC0 repository. Attribution is preserved per
   item (`images.attribution`, evidence notes), but a blanket CC0 dedication
   over CC BY content is not something we can grant. Judge candidates against
   the stricter reading.
3. **Does every item carry a citable identifier and a taxon?** The project
   brief requires both on images and protein examples. `item_id` and
   `taxon_link` say whether the source gives them or the curator must supply
   them; a `NO`/`NONE` source is a curation project, not an extraction.
4. **Bulk or API access over manual.** `data/` is committed and `just qc`
   runs offline; a per-item manual pull can never become `ADOPTED` (the
   checker requires a script), only `EVALUATING`.
5. **Effort, last.**

Two sources that close the same gap: adopt one, measure what it added, then
decide about the second (PMC OA vs Cell Image Library for micrographs).

## Verifying a source before it moves to ADOPTED

`redistribution` starts `UNVERIFIED` and is checked against the source's own
licence page — not a summary, not a memory, not another database's claim.
Record the date in `verified_on`. The checker refuses an `ADOPTED` row with
unverified terms, without a script, or absent from `conf/sources.yaml`.

Also establish, and write into `rationale`:

- **Coverage against this corpus**: which of our records would gain what.
  "6/6 test structures" (UniProt SL) is an answer; "thousands of images" is not.
- **Identifier joinability** — GO CC ids, NCBI taxids, UniProt accessions,
  DOIs. Name-only joining (Cell Image Library organisms) is curation work.
- **Machine-readable licence per item**, when the licence varies per item
  (Commons, CIL, BioImage Archive) — where in the API it is, quoted.
- **Known traps** this corpus has hit: pattern-valid identifiers that do not
  resolve (#2, #4, #34); tracking parameters in API-returned URLs (#34); a
  rendering presented as a micrograph (#35); a retired API still documented
  elsewhere (PMC OA service, Feb 2026); a site that resolves but refuses
  connections (ETDB-Caltech).
- **Whether an adopted source already closes it.** UniProt SL lists member
  proteins per structure; check it before adding a second components source.

A licence that cannot be reached is a result too: record the URLs tried and
what blocked them (SubtiWiki: nothing on site, bundle, Swagger or paper).

## Folding in a research report

When a research note lands, do not paste it into the queue. For each source
it covers: add or update the row; move `redistribution` off `UNVERIFIED` only
where the note quotes the licence page; put the specific finding in
`rationale`; keep the note's own "could not verify" as `UNVERIFIED`. Add a
**Sources** section to the note if it lacks one (#32).

## What this skill does not do

It does not fetch, seed, or adopt. Moving a source to `ADOPTED` means a
script under `scripts/` reads it, `conf/sources.yaml` lists it, the terms are
verified and dated, and `just qc` passes — that is a pull request with the
canary discipline in `CLAUDE.md` (one item end to end, side effects checked,
`just qc` run bare), not a row edit. Editing the row to say `ADOPTED` without
that work makes `just source-queue` fail, which is intended. Merging and
promoting records to `REVIEWED` stay the owner's calls.

## Output

Report: the top three candidates with the gap each closes and what is
unverified about it; anything whose status should change and why; any source
the corpus has outgrown. If the queue is already accurate, say so — a short
honest answer beats a reshuffle.
