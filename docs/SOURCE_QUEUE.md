# Data source queue

**The queue is `curation/source_queue.tsv`.** This page is its legend. It is
machine-checked by `scripts/check_source_queue.py` (`just source-queue`,
part of `just qc`), and triaged by the `source-queue` skill.

Ranking rule: what the corpus cannot currently assert (`just report`), then
whether we may redistribute it, then per-item identifiers and taxon linkage,
then bulk access, then effort. A licence failure sinks a source regardless of
everything else.

| Column | Values | Meaning |
|---|---|---|
| `closes_gap` | a `CellStructureRecord` field, or `identity` / `evidence` | What the source would fill. Check `just report` for what is actually empty. |
| `use` | `SEED` copy content into records or `pages/` · `LINK_ONLY` cite by URL/DOI, never host · `CURATE_ONLY` a curator may read it, nothing is copied · `REFERENCE` identifiers only | How the source may be used. |
| `redistribution` | `CC0_OK` · `ATTRIBUTION` (CC BY) · `SHARE_ALIKE` · `NONCOMMERCIAL` · `RESTRICTED` · `UNVERIFIED` | What the source's own licence page says. `SEED` is refused under the last three. |
| `taxon_link` | `YES` · `PARTIAL` · `NO` · `UNVERIFIED` | Does an item carry an NCBI Taxonomy id? |
| `item_id` | `DOI` · `CURIE` · `ACCESSION` · `URL` · `NONE` | The per-item citable identifier. |
| `access` | `BULK` · `API` · `BOTH` · `MANUAL` · `UNVERIFIED` | |
| `priority` | 1 (next) – 5 | |
| `status` | `CANDIDATE` · `EVALUATING` (used by hand, no repeatable script yet) · `ADOPTED` (in `conf/sources.yaml`, `script` exists, terms verified) · `BLOCKED` (reason in rationale) · `REJECTED` | |
| `verified_on` | date | When the licence was read at the source. |
| `script` | path | Required for `ADOPTED`; must exist. |

Research notes under `research/` are the evidence behind each row; issues
track the work. `ADOPTED` is earned by a pull request that adds the script and
passes `just qc`, not by editing the row.
