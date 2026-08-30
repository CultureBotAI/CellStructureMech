"""Corpus-wide invariants that per-record validation cannot see."""

from __future__ import annotations

from collections import Counter

from cellstructuremech.validation.write_validated import validate_structure
from scripts.corpus import record_path


def test_identifiers_are_unique(records):
    dupes = [k for k, v in Counter(d["identifier"] for _, d in records).items() if v > 1]
    assert not dupes, f"duplicate identifiers: {dupes}"


def test_every_record_validates_closed(records):
    bad = {str(p): [e.message[:120] for e in errs] for p, d in records if (errs := validate_structure(d))}
    assert not bad, bad


def test_file_location_matches_category_and_label(records, repo_root):
    """`data/structures/<category>/<slug>.yaml` is derived from the record, so a
    moved or renamed file and its content cannot disagree."""
    wrong = []
    for path, doc in records:
        expected = record_path(doc["structure_category"], doc["label"])
        if path.resolve() != expected.resolve():
            wrong.append((str(path.relative_to(repo_root)), str(expected.relative_to(repo_root))))
    assert not wrong, f"records not at their derived path: {wrong}"


def test_graph_edges_reference_declared_nodes(records):
    bad = []
    for path, doc in records:
        for g in doc.get("causal_graphs") or []:
            ids = {n["node_id"] for n in g["nodes"]}
            for e in g["edges"]:
                for end in (e["subject"], e["object"]):
                    if end not in ids:
                        bad.append(f"{path.name}:{g['graph_id']}:{end}")
    assert not bad, f"edges referencing undeclared nodes: {bad}"


def test_graph_node_component_refs_resolve(records):
    bad = []
    for path, doc in records:
        comp_ids = {c["component_id"] for c in doc.get("components") or []}
        for g in doc.get("causal_graphs") or []:
            for n in g["nodes"]:
                ref = n.get("component_ref")
                if ref and ref not in comp_ids:
                    bad.append(f"{path.name}:{g['graph_id']}:{n['node_id']}->{ref}")
    assert not bad, f"component_ref pointing at no component: {bad}"


def test_local_ids_are_unique_within_record(records):
    bad = []
    for path, doc in records:
        for key, idk in (("components", "component_id"), ("functions", "function_id"),
                         ("causal_graphs", "graph_id"), ("discussions", "discussion_id")):
            ids = [x[idk] for x in doc.get(key) or []]
            if len(ids) != len(set(ids)):
                bad.append(f"{path.name}:{key}")
    assert not bad, f"duplicate local ids: {bad}"


def test_internal_part_links_resolve_or_are_go(records):
    """parent_structures / part_of / has_part either point at another record here or at a GO term
    a future record could adopt. Anything else is a typo."""
    known = {d["identifier"] for _, d in records}
    bad = []
    for path, doc in records:
        for key in ("parent_structures", "part_of", "has_part"):
            for c in doc.get(key) or []:
                if c not in known and not c.startswith("GO:"):
                    bad.append(f"{path.name}:{key}:{c}")
    assert not bad, bad


def test_discussion_anchors_resolve(records):
    """`attaches_to` uses `<section>#<local id>`; the id must exist in that section."""
    bad = []
    for path, doc in records:
        anchors = {
            "components": {c["component_id"] for c in doc.get("components") or []},
            "functions": {f["function_id"] for f in doc.get("functions") or []},
            "causal_graphs": {g["graph_id"] for g in doc.get("causal_graphs") or []},
        }
        for disc in doc.get("discussions") or []:
            for a in disc.get("attaches_to") or []:
                section, _, local = a.partition("#")
                if section in anchors and local not in anchors[section]:
                    bad.append(f"{path.name}:{disc['discussion_id']}:{a}")
    assert not bad, bad


def test_reviewed_records_carry_evidence_and_history(records):
    bad = []
    for path, doc in records:
        if doc.get("mapping_status") == "REVIEWED":
            if not (doc.get("evidence") or doc.get("definition_source")):
                bad.append(f"{path.name}: no evidence")
            if not doc.get("curation_history"):
                bad.append(f"{path.name}: no curation_history")
    assert not bad, bad
