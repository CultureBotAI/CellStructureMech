"""Causal-graph scoring ranks the weakest mechanism records first."""

from __future__ import annotations

from pathlib import Path

from scripts.score_causal_graphs import score_record, score_records


def _doc(**extra):
    doc = {"identifier": "GO:1", "label": "test structure"}
    doc.update(extra)
    return doc


def test_record_without_graphs_scores_zero_and_ranks_first():
    no_graph = score_record(Path("no_graph.yaml"), _doc())
    thin_graph = score_record(
        Path("thin_graph.yaml"),
        _doc(
            causal_graphs=[
                {
                    "graph_id": "thin",
                    "graph_kind": "FUNCTION",
                    "scope_status": "MECHANISTIC",
                    "nodes": [
                        {"node_id": "a", "label": "A", "node_type": "STATE"},
                        {"node_id": "b", "label": "B", "node_type": "STATE"},
                    ],
                    "edges": [
                        {
                            "subject": "a",
                            "predicate": "causes",
                            "object": "b",
                            "evidence": [{"reference": "DOI:10.1/example", "notes": "Evidence."}],
                        }
                    ],
                }
            ]
        ),
    )

    ranked = score_records([
        (thin_graph.path, _doc(causal_graphs=[{"graph_id": "x"}])),
        (no_graph.path, _doc()),
    ])

    assert no_graph.score == 0
    assert "no_causal_graphs" in no_graph.improvement_flags
    assert ranked[0].path == no_graph.path


def test_rich_mechanistic_graph_outranks_review_needed_stub():
    review_needed = score_record(
        Path("review.yaml"),
        _doc(
            causal_graphs=[
                {
                    "graph_id": "review",
                    "graph_kind": "REGULATION",
                    "scope_status": "REVIEW_NEEDED",
                    "nodes": [
                        {"node_id": "a", "label": "A", "node_type": "STATE"},
                        {"node_id": "b", "label": "B", "node_type": "STATE"},
                    ],
                    "edges": [
                        {
                            "subject": "a",
                            "predicate": "regulates",
                            "object": "b",
                            "evidence": [{"reference": "DOI:10.1/example"}],
                        }
                    ],
                }
            ]
        ),
    )
    rich = score_record(
        Path("rich.yaml"),
        _doc(
            causal_graphs=[
                {
                    "graph_id": "assembly",
                    "graph_kind": "ASSEMBLY",
                    "scope_status": "MECHANISTIC",
                    "nodes": [
                        {
                            "node_id": "component",
                            "label": "component",
                            "node_type": "GENE_OR_PROTEIN",
                            "component_ref": "component",
                        },
                        {
                            "node_id": "structure",
                            "label": "structure",
                            "node_type": "STRUCTURE",
                            "grounding": "GO:2",
                        },
                    ],
                    "edges": [
                        {
                            "subject": "component",
                            "predicate": "self-assembles into",
                            "predicate_id": "RO:1",
                            "object": "structure",
                            "description": "Assembly edge.",
                            "evidence": [
                                {
                                    "reference": "PMID:1",
                                    "snippet": "Quote.",
                                    "notes": "Verbatim from the source.",
                                }
                            ],
                        },
                    ],
                }
            ]
        ),
    )

    assert rich.score > review_needed.score
    assert "nonmechanistic_or_review_needed_graphs" in review_needed.improvement_flags
    assert "thin_edge_evidence" in review_needed.improvement_flags
