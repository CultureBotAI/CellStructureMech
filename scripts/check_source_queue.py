#!/usr/bin/env python3
"""Check curation/source_queue.tsv against the repository it describes.

The queue ranks data sources for the corpus. It is curator-owned prose in a
TSV, so nothing stops it drifting into wishful thinking: a source marked
ADOPTED that no script reads, a licence left UNVERIFIED under content the site
hosts, a gap named that no record field can carry.

Checks the claims that are checkable:

  * shape — known columns, known enum values, no duplicate ids
  * every gap named is a CellStructureRecord attribute or a corpus-level gap
  * ADOPTED means adopted: the source is in conf/sources.yaml, its `script`
    exists, its redistribution terms are verified and dated
  * every source conf/sources.yaml reads has an ADOPTED row
  * nothing is SEED-able (content copied into records or pages/) while its
    terms are UNVERIFIED, NONCOMMERCIAL or RESTRICTED — hosting is what the
    licence enum in the schema forbids, and this is the same rule one level up
  * LINK_ONLY is the only `use` allowed under NONCOMMERCIAL

    python scripts/check_source_queue.py
"""

from __future__ import annotations

import csv
import sys
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
QUEUE_PATH = REPO_ROOT / "curation" / "source_queue.tsv"
CONF_PATH = REPO_ROOT / "conf" / "sources.yaml"
SCHEMA_PATH = REPO_ROOT / "src" / "cellstructuremech" / "schema" / "cellstructuremech.yaml"

COLUMNS = ["source_id", "name", "closes_gap", "use", "redistribution", "taxon_link", "item_id",
           "access", "priority", "status", "verified_on", "script", "url", "rationale"]

USE = {"SEED", "LINK_ONLY", "CURATE_ONLY", "REFERENCE"}
REDISTRIBUTION = {"CC0_OK", "ATTRIBUTION", "SHARE_ALIKE", "NONCOMMERCIAL", "RESTRICTED", "UNVERIFIED"}
TAXON_LINK = {"YES", "PARTIAL", "NO", "UNVERIFIED"}
ITEM_ID = {"DOI", "CURIE", "ACCESSION", "URL", "NONE", "UNVERIFIED"}
ACCESS = {"BULK", "API", "BOTH", "MANUAL", "UNVERIFIED"}
STATUS = {"CANDIDATE", "EVALUATING", "ADOPTED", "REJECTED", "BLOCKED"}
# What LICENSE says may be copied into records or pages. SHARE_ALIKE is here
# rather than in the hostable set because share-alike propagates to consumers
# of this corpus, which a CC0 repository cannot promise (#93).
HOST_FORBIDDEN = {"UNVERIFIED", "NONCOMMERCIAL", "RESTRICTED", "SHARE_ALIKE"}

# Gaps that are not record fields: corpus-level things a source can close.
EXTRA_GAPS = {"identity", "evidence"}


def record_fields() -> set[str]:
    schema = yaml.safe_load(SCHEMA_PATH.read_text(encoding="utf-8"))
    return set(schema["classes"]["CellStructureRecord"]["attributes"])


def main() -> int:
    if not QUEUE_PATH.exists():
        print(f"missing {QUEUE_PATH}", file=sys.stderr)
        return 1
    with QUEUE_PATH.open(newline="", encoding="utf-8") as fh:
        reader = csv.DictReader(fh, delimiter="\t")
        if reader.fieldnames != COLUMNS:
            print(f"unexpected columns: {reader.fieldnames}", file=sys.stderr)
            return 1
        rows = list(reader)

    conf = yaml.safe_load(CONF_PATH.read_text(encoding="utf-8")) or {}
    pipeline_sources = {k for k, v in conf.items() if isinstance(v, dict)}
    allowed_gaps = record_fields() | EXTRA_GAPS

    problems: list[str] = []
    seen: set[str] = set()
    for row in rows:
        sid = row["source_id"]
        if sid in seen:
            problems.append(f"{sid}: duplicate row")
        seen.add(sid)
        for column, allowed in (("use", USE), ("redistribution", REDISTRIBUTION),
                                ("taxon_link", TAXON_LINK), ("item_id", ITEM_ID),
                                ("access", ACCESS), ("status", STATUS)):
            if row[column] not in allowed:
                problems.append(f"{sid}: {column}={row[column]!r} not one of {sorted(allowed)}")
        if row["closes_gap"] not in allowed_gaps:
            problems.append(f"{sid}: closes_gap={row['closes_gap']!r} is not a record field or corpus gap")
        if not row["priority"].isdigit() or not 1 <= int(row["priority"]) <= 5:
            problems.append(f"{sid}: priority={row['priority']!r} must be 1-5")
        if not row["rationale"].strip():
            problems.append(f"{sid}: no rationale — why this source, and why now?")
        if not row["url"].startswith("http"):
            problems.append(f"{sid}: url is not a URL")
        dated = {"ADOPTED", "BLOCKED", "REJECTED", "EVALUATING"}
        if row["status"] in dated and not row["verified_on"].startswith("20"):
            problems.append(f"{sid}: {row['status']} without a verification date")

        if row["status"] == "ADOPTED":
            if sid not in pipeline_sources:
                problems.append(f"{sid}: ADOPTED but conf/sources.yaml does not list it")
            if not row["script"]:
                problems.append(f"{sid}: ADOPTED without a script — a one-off pull is EVALUATING, "
                                f"not ADOPTED")
            elif not (REPO_ROOT / row["script"]).is_file():
                problems.append(f"{sid}: script {row['script']} does not exist")
            if row["redistribution"] == "UNVERIFIED":
                problems.append(f"{sid}: ADOPTED with unverified redistribution terms")

        if row["use"] == "SEED" and row["status"] == "ADOPTED" and row["redistribution"] in HOST_FORBIDDEN:
            problems.append(f"{sid}: SEED under {row['redistribution']} terms — content would be hosted "
                            f"or copied; use LINK_ONLY or CURATE_ONLY")
        nc_ok = {"LINK_ONLY", "CURATE_ONLY", "REFERENCE"}
        if row["redistribution"] == "NONCOMMERCIAL" and row["use"] not in nc_ok:
            problems.append(f"{sid}: NONCOMMERCIAL terms allow {sorted(nc_ok)}, not {row['use']}")

    adopted = {r["source_id"] for r in rows if r["status"] == "ADOPTED"}
    for source in sorted(pipeline_sources - adopted):
        problems.append(f"{source}: read by conf/sources.yaml but has no ADOPTED queue row")

    if problems:
        print("source queue check FAILED:", file=sys.stderr)
        print("\n".join(f"  {p}" for p in problems), file=sys.stderr)
        return 1

    by_status: dict[str, int] = {}
    for row in rows:
        by_status[row["status"]] = by_status.get(row["status"], 0) + 1
    nxt = sorted((r for r in rows if r["status"] in {"CANDIDATE", "EVALUATING"}),
                 key=lambda r: (int(r["priority"]), r["source_id"]))[:3]
    print(f"source queue OK: {len(rows)} sources — "
          + ", ".join(f"{n} {s.lower()}" for s, n in sorted(by_status.items())))
    if nxt:
        print("next up: " + ", ".join(f"{r['source_id']} (P{r['priority']}, {r['status'].lower()}, "
                                      f"{r['closes_gap']})" for r in nxt))
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
