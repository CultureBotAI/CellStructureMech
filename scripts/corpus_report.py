#!/usr/bin/env python3
"""Corpus report: records per category and status, grounding, and how much
of each record is filled in (components, functions, graphs, trait links).

Usage:
    python scripts/corpus_report.py
    python scripts/corpus_report.py --tsv reports/corpus.tsv
"""

from __future__ import annotations

import argparse
import csv
import sys
from collections import Counter
from pathlib import Path

from corpus import STRUCTURES_DIR, load_records


def summarize(records: list[tuple[Path, dict]]) -> dict:
    by_category = Counter(d.get("structure_category") for _, d in records)
    by_status = Counter(d.get("mapping_status") for _, d in records)
    go_grounded = sum(1 for _, d in records if d["identifier"].startswith("GO:"))
    minted = sum(1 for _, d in records if d["identifier"].startswith("cellstructuremech:"))
    with_components = sum(1 for _, d in records if d.get("components"))
    roles = Counter(c.get("component_role") for _, d in records for c in d.get("components") or [])
    with_graphs = sum(1 for _, d in records if d.get("causal_graphs"))
    with_traits = sum(1 for _, d in records if d.get("associated_traits"))
    with_functions = sum(1 for _, d in records if d.get("functions"))
    with_images = sum(1 for _, d in records if d.get("images"))
    edges = sum(len(g.get("edges") or []) for _, d in records for g in d.get("causal_graphs") or [])
    return {
        "total": len(records),
        "by_category": dict(by_category.most_common()),
        "by_status": dict(by_status.most_common()),
        "go_grounded": go_grounded,
        "minted": minted,
        "with_components": with_components,
        "with_functions": with_functions,
        "with_graphs": with_graphs,
        "with_traits": with_traits,
        "with_images": with_images,
        "component_roles": dict(roles.most_common()),
        "edges": edges,
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--tsv", type=Path, help="Also write a per-record TSV here.")
    args = parser.parse_args()

    records = load_records()
    if not records:
        print(f"No records under {STRUCTURES_DIR}", file=sys.stderr)
        return 0
    s = summarize(records)
    print(f"{s['total']} structure records")
    print("\nBy category:")
    for k, v in s["by_category"].items():
        print(f"  {k:22s} {v:5d}")
    print("\nBy status:")
    for k, v in s["by_status"].items():
        print(f"  {k:22s} {v:5d}")
    print(f"\nGrounded in GO: {s['go_grounded']}   minted cellstructuremech: {s['minted']}")
    if s["component_roles"]:
        parts = "   ".join(f"{role.lower()}: {n}" for role, n in s["component_roles"].items() if role)
        print(f"\nComponents by role: {parts}")
    print(
        f"With components: {s['with_components']}   functions: {s['with_functions']}   "
        f"causal graphs: {s['with_graphs']} ({s['edges']} edges)   trait links: {s['with_traits']}   "
        f"images: {s['with_images']}"
    )

    if args.tsv:
        args.tsv.parent.mkdir(parents=True, exist_ok=True)
        with args.tsv.open("w", newline="", encoding="utf-8") as fh:
            w = csv.writer(fh, delimiter="\t", lineterminator="\n")
            w.writerow(["identifier", "label", "category", "status", "components", "functions",
                        "graphs", "traits"])
            for _path, d in records:
                w.writerow([
                    d["identifier"], d["label"], d.get("structure_category"), d.get("mapping_status"),
                    len(d.get("components") or []), len(d.get("functions") or []),
                    len(d.get("causal_graphs") or []), len(d.get("associated_traits") or []),
                ])
    return 0


if __name__ == "__main__":
    sys.exit(main())
