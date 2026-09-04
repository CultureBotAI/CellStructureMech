#!/usr/bin/env python3
"""Score and rank records by causal-graph content and evidence quality.

Rank 1 is the poorest causal-graph record and the next curation target.
The score is deliberately about graph readiness, not overall record quality:
records with strong composition, imaging, or dataset metadata still score 0
until they carry at least one evidence-backed `causal_graphs` entry.
"""

from __future__ import annotations

import argparse
import csv
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    from corpus import REPO_ROOT, STRUCTURES_DIR, load_records
except ModuleNotFoundError:
    from scripts.corpus import REPO_ROOT, STRUCTURES_DIR, load_records

CORE_GRAPH_KINDS = {"ASSEMBLY", "FUNCTION", "REGULATION"}
SCORE_COLUMNS = [
    "rank",
    "score",
    "path",
    "identifier",
    "label",
    "graph_count",
    "graph_kinds",
    "mechanistic_graphs",
    "node_count",
    "anchored_nodes",
    "edge_count",
    "richly_evidenced_edges",
    "edges_with_predicate_id",
    "edges_with_description",
    "improvement_flags",
]


@dataclass(frozen=True)
class CausalGraphScore:
    score: int
    path: Path
    identifier: str
    label: str
    graph_count: int
    graph_kinds: tuple[str, ...]
    mechanistic_graphs: int
    node_count: int
    anchored_nodes: int
    edge_count: int
    richly_evidenced_edges: int
    edges_with_predicate_id: int
    edges_with_description: int
    improvement_flags: tuple[str, ...]

    def row(self, rank: int) -> dict[str, str | int]:
        return {
            "rank": rank,
            "score": self.score,
            "path": _display_path(self.path),
            "identifier": self.identifier,
            "label": self.label,
            "graph_count": self.graph_count,
            "graph_kinds": ",".join(self.graph_kinds),
            "mechanistic_graphs": self.mechanistic_graphs,
            "node_count": self.node_count,
            "anchored_nodes": self.anchored_nodes,
            "edge_count": self.edge_count,
            "richly_evidenced_edges": self.richly_evidenced_edges,
            "edges_with_predicate_id": self.edges_with_predicate_id,
            "edges_with_description": self.edges_with_description,
            "improvement_flags": ",".join(self.improvement_flags),
        }


def _display_path(path: Path) -> str:
    try:
        return path.relative_to(REPO_ROOT).as_posix()
    except ValueError:
        return path.as_posix()


def _fraction(numerator: int, denominator: int) -> float:
    return numerator / denominator if denominator else 0


def _has_rich_evidence(edge: dict[str, Any]) -> bool:
    return any(
        evidence.get("reference") and (evidence.get("snippet") or evidence.get("notes"))
        for evidence in edge.get("evidence") or []
    )


def score_record(path: Path, doc: dict[str, Any]) -> CausalGraphScore:
    graphs = doc.get("causal_graphs") or []
    nodes = [node for graph in graphs for node in graph.get("nodes") or []]
    edges = [edge for graph in graphs for edge in graph.get("edges") or []]

    graph_count = len(graphs)
    graph_kinds = tuple(sorted({graph.get("graph_kind", "") for graph in graphs if graph.get("graph_kind")}))
    mechanistic_graphs = sum(1 for graph in graphs if graph.get("scope_status") == "MECHANISTIC")
    anchored_nodes = sum(
        1
        for node in nodes
        if node.get("component_ref") or node.get("grounding") or node.get("xrefs")
    )
    richly_evidenced_edges = sum(1 for edge in edges if _has_rich_evidence(edge))
    edges_with_predicate_id = sum(1 for edge in edges if edge.get("predicate_id"))
    edges_with_description = sum(1 for edge in edges if edge.get("description"))

    raw_score = (
        10 * min(graph_count, 2) / 2
        + 12 * min(len(set(graph_kinds) & CORE_GRAPH_KINDS), len(CORE_GRAPH_KINDS)) / len(CORE_GRAPH_KINDS)
        + 14 * _fraction(mechanistic_graphs, graph_count)
        + 18 * min(len(edges), 5) / 5
        + 20 * _fraction(richly_evidenced_edges, len(edges))
        + 14 * _fraction(anchored_nodes, len(nodes))
        + 6 * _fraction(edges_with_predicate_id, len(edges))
        + 6 * _fraction(edges_with_description, len(edges))
    )

    flags = []
    if not graphs:
        flags.append("no_causal_graphs")
    if graph_count == 1:
        flags.append("single_causal_graph")
    if graphs and not set(graph_kinds) & {"ASSEMBLY", "FUNCTION"}:
        flags.append("missing_core_assembly_or_function_graph")
    if graph_count and mechanistic_graphs != graph_count:
        flags.append("nonmechanistic_or_review_needed_graphs")
    if len(edges) < 4:
        flags.append("thin_edge_count")
    if len(edges) and richly_evidenced_edges != len(edges):
        flags.append("thin_edge_evidence")
    if len(nodes) and anchored_nodes != len(nodes):
        flags.append("unanchored_nodes")
    if len(edges) and edges_with_predicate_id != len(edges):
        flags.append("edges_without_predicate_id")
    if len(edges) and edges_with_description != len(edges):
        flags.append("edges_without_description")

    return CausalGraphScore(
        score=round(raw_score),
        path=path,
        identifier=doc["identifier"],
        label=doc["label"],
        graph_count=graph_count,
        graph_kinds=graph_kinds,
        mechanistic_graphs=mechanistic_graphs,
        node_count=len(nodes),
        anchored_nodes=anchored_nodes,
        edge_count=len(edges),
        richly_evidenced_edges=richly_evidenced_edges,
        edges_with_predicate_id=edges_with_predicate_id,
        edges_with_description=edges_with_description,
        improvement_flags=tuple(flags),
    )


def score_records(records: list[tuple[Path, dict[str, Any]]]) -> list[CausalGraphScore]:
    return sorted(
        (score_record(path, doc) for path, doc in records),
        key=lambda item: (item.score, item.edge_count, item.graph_count, _display_path(item.path)),
    )


def write_scores(scores: list[CausalGraphScore], out) -> None:
    writer = csv.DictWriter(
        out,
        fieldnames=SCORE_COLUMNS,
        delimiter="\t",
        lineterminator="\n",
    )
    writer.writeheader()
    for rank, score in enumerate(scores, start=1):
        writer.writerow(score.row(rank))


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--root", type=Path, default=STRUCTURES_DIR,
                        help="Root containing CellStructureRecord YAML files.")
    parser.add_argument("--out", type=Path, help="Write the ranked TSV here instead of stdout.")
    parser.add_argument("--limit", type=int, help="Only emit the N lowest-scoring records.")
    args = parser.parse_args()

    records = load_records(args.root)
    if args.limit is not None and args.limit < 1:
        print("--limit must be positive", file=sys.stderr)
        return 2
    scores = score_records(records)
    if args.limit:
        scores = scores[: args.limit]

    if args.out:
        args.out.parent.mkdir(parents=True, exist_ok=True)
        with args.out.open("w", newline="", encoding="utf-8") as fh:
            write_scores(scores, fh)
    else:
        write_scores(scores, sys.stdout)
    return 0


if __name__ == "__main__":
    sys.exit(main())
