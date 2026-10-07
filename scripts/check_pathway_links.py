#!/usr/bin/env python3
"""Validate PathwayMech links offline; optionally verify the pinned Git source."""

from __future__ import annotations

import argparse
import hashlib
import json
import subprocess
from pathlib import Path

import yaml

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records

SNAPSHOT = REPO_ROOT / "conf/pathwaymech_targets.json"


def check_links(records, snapshot: dict) -> list[str]:
    """A matching name alone is insufficient: identity, version and taxon bind it."""
    targets = {row["id"]: row for row in snapshot["records"]}
    if len(targets) != len(snapshot["records"]):
        return ["duplicate identifier in PathwayMech snapshot"]
    problems = []
    for path, doc in records:
        for link in doc.get("related_records") or []:
            target = targets.get(link.get("identifier"))
            prefix = f"{path}: {link.get('identifier')}"
            if not target:
                problems.append(f"{prefix}: target absent from pinned snapshot")
                continue
            if link.get("corpus") != "PathwayMech":
                problems.append(f"{prefix}: unsupported corpus")
            if link.get("source_version") != snapshot["source_commit"]:
                problems.append(f"{prefix}: source revision differs from snapshot")
            if link.get("label") != target["label"]:
                problems.append(f"{prefix}: target label differs from snapshot")
            if link.get("target_taxon_id") not in target["taxa"]:
                problems.append(f"{prefix}: target taxon differs from snapshot")
    return problems


def check_source(root: Path, snapshot: dict) -> list[str]:
    """Read committed objects, so an unrelated dirty worktree cannot alter proof."""
    problems = []
    for target in snapshot["records"]:
        result = subprocess.run(
            ["git", "-C", str(root), "show", f"{snapshot['source_commit']}:{target['path']}"],
            capture_output=True, check=False,
        )
        if result.returncode:
            problems.append(f"cannot read pinned target: {target['id']}")
            continue
        if hashlib.sha256(result.stdout).hexdigest() != target["sha256"]:
            problems.append(f"pinned target bytes differ: {target['id']}")
            continue
        doc = yaml.safe_load(result.stdout)
        if (doc["id"], doc["label"], sorted(t["id"] for t in doc.get("taxa") or [])) != (
            target["id"], target["label"], sorted(target["taxa"]),
        ):
            problems.append(f"snapshot metadata differs from target: {target['id']}")
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--pathwaymech-root", type=Path)
    args = parser.parse_args()
    snapshot = json.loads(SNAPSHOT.read_text(encoding="utf-8"))
    records = load_records()
    problems = check_links(records, snapshot)
    if args.pathwaymech_root:
        problems += check_source(args.pathwaymech_root, snapshot)
    if problems:
        print("\n".join(problems))
        return 1
    count = sum(len(doc.get("related_records") or []) for _, doc in records)
    print(f"OK: {count} pathway links match the pinned target snapshot")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
