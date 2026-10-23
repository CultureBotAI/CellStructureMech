"""Semantic validation checks for CellStructureRecord documents (#2408, #2410).

Complements closed-schema LinkML validation (``write_validated.py``) with
cross-field and graph-completeness invariants that JSON Schema alone cannot
express:

- Every ``CausalEdge.subject`` and ``CausalEdge.object`` references a declared
  ``CausalNode.node_id`` in the same graph.
- Every ``CausalNode.component_ref`` resolves to a declared ``component_id`` on
  the record.
- Every declared ``CausalNode`` participates in at least one incident
  ``CausalEdge`` (no isolated nodes).
- Every ``CausalEdge`` carries a non-blank ``description``.
- Every ``#NNN`` GitHub issue mention in ``discussions`` prose (``prompt``,
  ``rationale``, ``resolution_note``) is backed by a full GitHub issue URL in
  that discussion's ``evidence`` list, and every ``attaches_to`` anchor
  resolves to a local ID on the record.
"""

from __future__ import annotations

import re
from typing import Any

DEFAULT_GITHUB_REPO = "CultureBotAI/CellStructureMech"
_PROSE_ISSUE_RE = re.compile(r"(?<![A-Za-z0-9_/])#([1-9]\d*)\b")


def validate_causal_graphs(doc: dict[str, Any]) -> list[str]:
    """Return semantic validation error strings for ``doc['causal_graphs']``."""
    errors: list[str] = []
    comp_ids = {
        c.get("component_id")
        for c in (doc.get("components") or [])
        if isinstance(c, dict) and c.get("component_id")
    }
    for graph in doc.get("causal_graphs") or []:
        if not isinstance(graph, dict):
            continue
        gid = graph.get("graph_id") or "<graph>"
        nodes = [n for n in (graph.get("nodes") or []) if isinstance(n, dict)]
        edges = [e for e in (graph.get("edges") or []) if isinstance(e, dict)]
        node_ids = {n.get("node_id") for n in nodes if n.get("node_id")}

        incident: set[str] = set()
        for idx, edge in enumerate(edges):
            subj = edge.get("subject")
            obj = edge.get("object")
            if subj not in node_ids:
                errors.append(
                    f"{gid}: edge[{idx}] subject {subj!r} is not a declared node_id"
                )
            else:
                incident.add(subj)
            if obj not in node_ids:
                errors.append(
                    f"{gid}: edge[{idx}] object {obj!r} is not a declared node_id"
                )
            else:
                incident.add(obj)
            desc = edge.get("description")
            if not isinstance(desc, str) or not desc.strip():
                errors.append(
                    f"{gid}: edge[{idx}] ({subj} -> {obj}) lacks a non-empty description"
                )

        for node in nodes:
            nid = node.get("node_id")
            cref = node.get("component_ref")
            if cref and cref not in comp_ids:
                errors.append(
                    f"{gid}: node {nid!r} component_ref {cref!r} does not resolve to a component"
                )
            if nid and nid not in incident:
                errors.append(
                    f"{gid}: isolated CausalNode {nid!r} has zero incident edges"
                )
    return errors


def validate_discussion_issue_links(
    doc: dict[str, Any],
    *,
    github_repo: str = DEFAULT_GITHUB_REPO,
) -> list[str]:
    """Return error strings for ``discussions`` anchor or ``#NNN`` issue-link defects."""
    errors: list[str] = []
    anchors = {
        "components": {
            c.get("component_id")
            for c in (doc.get("components") or [])
            if isinstance(c, dict) and c.get("component_id")
        },
        "functions": {
            f.get("function_id")
            for f in (doc.get("functions") or [])
            if isinstance(f, dict) and f.get("function_id")
        },
        "causal_graphs": {
            g.get("graph_id")
            for g in (doc.get("causal_graphs") or [])
            if isinstance(g, dict) and g.get("graph_id")
        },
    }
    issue_prefix = f"https://github.com/{github_repo}/issues/"
    for disc in doc.get("discussions") or []:
        if not isinstance(disc, dict):
            continue
        did = disc.get("discussion_id") or "<discussion>"
        for anchor in disc.get("attaches_to") or []:
            if not isinstance(anchor, str):
                continue
            section, _, local = anchor.partition("#")
            if section in anchors and local not in anchors[section]:
                errors.append(
                    f"{did}: attaches_to anchor {anchor!r} does not resolve"
                )
        ev_refs = {
            str(ev.get("reference") or "").strip()
            for ev in (disc.get("evidence") or [])
            if isinstance(ev, dict)
        }
        prose = " ".join(
            str(disc.get(field) or "")
            for field in ("prompt", "rationale", "resolution_note", "text")
        )
        seen_nums: set[str] = set()
        for match in _PROSE_ISSUE_RE.finditer(prose):
            num = match.group(1)
            if num in seen_nums:
                continue
            seen_nums.add(num)
            expected_url = f"{issue_prefix}{num}"
            if expected_url not in ev_refs:
                errors.append(
                    f"{did}: prose mentions #{num} without {expected_url!r} in discussion.evidence"
                )
    return errors


def validate_record_semantics(
    doc: dict[str, Any],
    *,
    github_repo: str = DEFAULT_GITHUB_REPO,
) -> list[str]:
    """Run all semantic record checks on ``doc``."""
    return [
        *validate_causal_graphs(doc),
        *validate_discussion_issue_links(doc, github_repo=github_repo),
    ]
