#!/usr/bin/env python3
"""Check every `associated_traits` link against TraitMech (#11).

A trait link is the corpus's one claim about another repository: it asserts
that `traitmech:000071` exists there and is called "magnetosome". Nothing
verified that. `check_curies.py` deliberately skips the `traitmech:` and
`METPO:` prefixes for exactly this reason — they are not resolvable at any
public ontology service, only in the sibling repository.

Source of truth, in order:

1. a local TraitMech checkout (``TRAITMECH_ROOT``, or ``local_path`` under
   ``traitmech`` in ``conf/sources.yaml``) — read from ``data/traits``;
2. the published ``pages/data/trait_graph.json``, which carries the id and
   label of every trait record and needs no credentials.

Both the id and the label are checked. A label that has drifted is the
cross-repo form of the defect the id-label gate catches inside this corpus: the
CURIE still resolves, and the record says something the other repository no
longer says.

    python scripts/check_trait_links.py            # report
    python scripts/check_trait_links.py --check    # exit 1 on any bad link
    python scripts/check_trait_links.py --self-test
"""

from __future__ import annotations

import argparse
import json
import os
import sys
import urllib.request
from pathlib import Path

import yaml

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records

UA = {"User-Agent": "CellStructureMech/0.1 (https://github.com/CultureBotAI/CellStructureMech)"}
PUBLISHED_INDEX = "https://culturebotai.github.io/TraitMech/pages/data/trait_graph.json"
CACHE_PATH = REPO_ROOT / "build" / "traitmech_index.json"

# A trait known to exist, and one that cannot: the control that separates "the
# corpus is wrong" from "the index did not load" (#82).
CONTROL_GOOD = "METPO:1000702"
CONTROL_BAD = "traitmech:999999"


def local_root() -> Path | None:
    if (env := os.environ.get("TRAITMECH_ROOT", "").strip()):
        return Path(env).expanduser()
    conf = REPO_ROOT / "conf" / "sources.yaml"
    if conf.exists():
        entry = (yaml.safe_load(conf.read_text(encoding="utf-8")) or {}).get("traitmech") or {}
        if entry.get("local_path"):
            return Path(entry["local_path"]).expanduser()
    return None


def index_from_checkout(root: Path) -> dict[str, str]:
    traits = root / "data" / "traits"
    if not traits.is_dir():
        return {}
    out = {}
    for path in traits.rglob("*.yaml"):
        doc = yaml.safe_load(path.read_text(encoding="utf-8")) or {}
        if doc.get("identifier"):
            out[doc["identifier"]] = doc.get("label", "")
    return out


def index_from_published(offline: bool = False) -> dict[str, str]:
    if offline:
        return json.loads(CACHE_PATH.read_text()) if CACHE_PATH.exists() else {}
    try:
        with urllib.request.urlopen(urllib.request.Request(PUBLISHED_INDEX, headers=UA), timeout=60) as r:
            nodes = json.loads(r.read())
    except Exception as exc:  # noqa: BLE001
        print(f"could not fetch TraitMech's published index: {exc}", file=sys.stderr)
        return json.loads(CACHE_PATH.read_text()) if CACHE_PATH.exists() else {}
    out = {n["id"]: n.get("label", "") for n in nodes if n.get("id")}
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(out, indent=1, sort_keys=True) + "\n")
    return out


def load_index(offline: bool = False) -> tuple[dict[str, str], str]:
    root = local_root()
    if root and (index := index_from_checkout(root)):
        return index, f"local checkout {root}"
    return index_from_published(offline), PUBLISHED_INDEX


SIBLING_PREFIXES = ("traitmech:", "METPO:")


def trait_links(records) -> list[tuple[str, str, str]]:
    """(record file, trait id, claimed label) for every sibling-repository CURIE.

    Trait links carry a label to check; a sibling CURIE anywhere else — an
    `xrefs` entry, a `parent_structures` entry, a causal-node grounding — has
    no label, and is checked for existence alone. Walking the whole record
    matters because `check_curies.py` skips these prefixes on the grounds that
    this script covers them; a field neither one walks is checked by nothing
    (#89).
    """
    def sibling_curies(node, seen: set[str], found: list[str]) -> None:
        if isinstance(node, dict):
            for value in node.values():
                sibling_curies(value, seen, found)
        elif isinstance(node, list):
            for item in node:
                sibling_curies(item, seen, found)
        elif isinstance(node, str) and node.startswith(SIBLING_PREFIXES) and node not in seen:
            seen.add(node)
            found.append(node)

    out = []
    for path, doc in records:
        seen: set[str] = set()
        for link in doc.get("associated_traits") or []:
            out.append((path.name, link["trait_id"], link.get("trait_label", "")))
            seen.add(link["trait_id"])
        elsewhere: list[str] = []
        sibling_curies(doc, seen, elsewhere)
        out.extend((path.name, curie, "") for curie in elsewhere)
    return out


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 on any unresolvable or mislabelled link.")
    parser.add_argument("--offline", action="store_true", help="Use the cached index; do not fetch.")
    parser.add_argument("--self-test", action="store_true", help="Only check the index itself is usable.")
    args = parser.parse_args()

    index, source = load_index(args.offline)
    # An empty index means the source failed, not that the corpus is clean (#87).
    if not index:
        print("TraitMech index is empty — the checkout path or the published index is wrong, "
              "not the corpus", file=sys.stderr)
        return 2
    if CONTROL_GOOD not in index or CONTROL_BAD in index:
        print(f"index control failed against {source}: {CONTROL_GOOD} must be present and "
              f"{CONTROL_BAD} must not — the index is not what it claims to be", file=sys.stderr)
        return 2
    print(f"TraitMech index: {len(index)} traits from {source}", file=sys.stderr)
    if args.self_test:
        return 0

    links = trait_links(load_records())
    missing, mislabelled = [], []
    for record, trait_id, trait_label in links:
        if trait_id not in index:
            missing.append(f"{record}: {trait_id} is not a TraitMech record")
        elif trait_label and index[trait_id].strip().lower() != trait_label.strip().lower():
            mislabelled.append(f"{record}: {trait_id} is '{index[trait_id]}' in TraitMech, "
                               f"not '{trait_label}'")

    print(f"\n{len(links)} trait link(s): {len(links) - len(missing) - len(mislabelled)} resolve with a "
          f"matching label, {len(missing)} missing, {len(mislabelled)} mislabelled")
    for line in missing + mislabelled:
        print(f"  {line}", file=sys.stderr)
    if (missing or mislabelled) and args.check:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
