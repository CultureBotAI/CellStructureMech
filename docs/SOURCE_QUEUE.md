# Data source queue

**The queue is `curation/source_queue.tsv`.** This page is its legend. It is
machine-checked by `scripts/check_source_queue.py` (`just source-queue`,
part of `just qc`), and triaged by the `source-queue` skill.

Ranking rule: what the corpus cannot currently assert (`just report`), then
whether we may redistribute it, then per-item identifiers and taxon linkage,
then bulk access, then effort. A licence failure sinks any source use that
copies or hosts source content; identifiers-only use must remain explicitly
bounded and keep the terms truthfully marked `UNVERIFIED`.

| Column | Values | Meaning |
|---|---|---|
| `closes_gap` | a `CellStructureRecord` field, or `identity` / `evidence` | What the source would fill. Check `just report` for what is actually empty. |
| `use` | `SEED` copy the source's content into records or `pages/` · `LINK_ONLY` cite by URL/DOI, never host · `CURATE_ONLY` read it and record **third-party identifiers it points to**, each verified at the issuing authority, plus a link back — never its own descriptions, sequences, measurements or a bulk export · `REFERENCE` identifiers only | How the source may be used. |
**Why `CURATE_ONLY` is not "nothing is copied".** It said that until #126, and
the corpus contradicted it: `scripts/subtiwiki.py` records UniProt accessions
that SubtiWiki's category page points to, each verified in UniProtKB, with a
link back for attribution. Nothing of SubtiWiki's own content is stored. The
distinction that matters is between a source's **expression** — which needs a
licence — and a **fact it asserts about a third-party identifier**, which the
identifier's own authority is the place to verify. `CURATE_ONLY` permits the
second and forbids the first.

**Terms may be `UNVERIFIED` when nothing is redistributed.** `SEED` requires
verified, redistributable terms because it copies content. `LINK_ONLY`,
`CURATE_ONLY` and `REFERENCE` copy nothing, so a source whose licence page
does not exist — SubtiWiki states terms nowhere on its site, bundle, Swagger
or paper — can still be used that way, and saying `UNVERIFIED` is more honest
than guessing `RESTRICTED`.

| `redistribution` | `CC0_OK` · `ATTRIBUTION` (CC BY) · `SHARE_ALIKE` · `NONCOMMERCIAL` · `RESTRICTED` · `UNVERIFIED` | What the source's own licence page says. `SEED` is refused under the last three. |
| `taxon_link` | `YES` · `PARTIAL` · `NO` · `UNVERIFIED` | Does an item carry an NCBI Taxonomy id? |
| `item_id` | `DOI` · `CURIE` · `ACCESSION` · `URL` · `NONE` | The per-item citable identifier. |
| `access` | `BULK` · `API` · `BOTH` · `MANUAL` · `UNVERIFIED` | |
| `priority` | 1 (next) – 5 | |
| `status` | `CANDIDATE` · `EVALUATING` (used by hand, no repeatable script yet) · `ADOPTED` (in `conf/sources.yaml`, script exists, and the permitted use boundary is documented) · `BLOCKED` (reason in rationale) · `REJECTED` | |
| `verified_on` | date | When the source, terms and stated use boundary were last checked. |
| `script` | path | Required for `ADOPTED`; must exist. |

Research notes under `research/` are the evidence behind each row; issues
track the work. `ADOPTED` is earned by a pull request that adds the script and
passes `just qc`, not by editing the row.
