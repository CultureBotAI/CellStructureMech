"""Exercise SVG integrity and safety independently of the record corpus."""

import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "scripts"))
from mechanism_graph import graph_svg

NS = {"s": "http://www.w3.org/2000/svg"}


def svg(graph, instance="one"):
    html = str(graph_svg(graph, instance))
    return ET.fromstring(html[html.index("<svg ") : html.index("</svg>") + 6])


def test_cycles_parallel_edges_isolated_and_unresolved_nodes_are_visible():
    graph = {
        "title": "Mechanism",
        "nodes": [
            {"node_id": "a", "label": "Source"},
            {"node_id": "b", "label": "Target"},
            {"node_id": "alone", "label": "Isolated"},
        ],
        "edges": [
            {"subject": "a", "object": "b", "predicate": "activates"},
            {"subject": "a", "object": "b", "predicate": "binds"},
            {"subject": "b", "object": "a", "predicate": "feedback"},
            {"subject": "b", "object": "b", "predicate": "self"},
            {"subject": "b", "object": "missing", "predicate": "causes"},
        ],
    }
    root = svg(graph)
    nodes = root.findall('.//s:g[@class="graph-node"]', NS)
    edges = root.findall('.//s:g[@class="graph-edge"]', NS)
    assert {n.attrib["data-node-id"] for n in nodes} == {"a", "b", "alone", "missing"}
    assert len(edges) == 5
    assert len({e.find("s:path", NS).attrib["d"] for e in edges}) == 5
    assert all(e.find("s:path", NS).attrib.get("marker-end") for e in edges)
    assert "UNRESOLVED" in "".join(root.itertext())
    assert graph["nodes"][-1]["node_id"] == "alone"  # source remains untouched


def test_labels_evidence_and_ids_are_escaped_and_keyboard_accessible():
    attack = '<script>alert("x")</script> & "quoted"'
    graph = {
        "title": attack,
        "nodes": [{"node_id": attack, "label": attack}],
        "edges": [
            {
                "subject": attack,
                "object": attack,
                "predicate": attack,
                "evidence": [{"reference": "PMID:123"}],
            }
        ],
    }
    root = svg(graph)
    assert root.find(".//s:script", NS) is None
    assert attack in "".join(root.itertext())
    assert "PMID:123" in "".join(root.itertext())
    assert all(g.attrib["tabindex"] == "0" for g in root.findall(".//s:g", NS))
    assert root.attrib["aria-labelledby"]


def test_multiple_graphs_have_distinct_markers_and_deterministic_output():
    graph = {"nodes": [{"node_id": "a", "label": "A"}], "edges": []}
    one, two = svg(graph, "one"), svg(graph, "two")
    assert one.find(".//s:marker", NS).attrib["id"] != two.find(".//s:marker", NS).attrib["id"]
    assert str(graph_svg(graph, "one")) == str(graph_svg(graph, "one"))
    assert "<svg" not in str(graph_svg({}))


def test_newer_golgi_record_renders_diagram_alongside_evidence(tmp_path, monkeypatch):
    """PR1069's old base missed this graph-bearing page; render current input."""
    import render_pages
    import yaml

    record = render_pages.REPO_ROOT / "data/structures/membrane_organelle/golgi_associated_vesicle.yaml"
    document = yaml.safe_load(record.read_text())
    assert document["causal_graphs"]
    monkeypatch.setattr(render_pages, "load_records", lambda: [(record, document)])
    render_pages.render(tmp_path / "site")
    page = (tmp_path / "site/structures/membrane_organelle/golgi_associated_vesicle.html").read_text()
    assert page.count('class="mechanism-svg"') == len(document["causal_graphs"])
    assert 'aria-label="Mechanism evidence:' in page
    assert "<th>Evidence</th>" in page
    assert document["causal_graphs"][0]["graph_kind"] in page
    assert "GO:0030660" in page


@pytest.mark.parametrize("case", ["self", "reverse", "same_column"])
def test_viewbox_contains_parallel_relationship_geometry(case):
    """PR1069/#3075: parallel paths and labels must remain within the viewport."""
    nodes = [{"node_id": node, "label": node.upper()} for node in "abc"]
    if case == "self":
        edges = [{"subject": "a", "object": "a", "predicate": f"self {i}"} for i in range(3)]
    elif case == "reverse":
        edges = [{"subject": "a", "object": "b", "predicate": "forward"}]
        edges += [{"subject": "b", "object": "a", "predicate": f"reverse {i}"} for i in range(12)]
    else:
        edges = [{"subject": "a", "object": node, "predicate": f"branch {node}"} for node in "bc"]
        edges += [{"subject": "b", "object": "c", "predicate": f"parallel {i}"} for i in range(12)]
    root = svg({"nodes": nodes, "edges": edges})
    left, top, width, height = map(float, root.attrib["viewBox"].split())
    right, bottom = left + width, top + height
    rendered_edges = root.findall('.//s:g[@class="graph-edge"]', NS)
    assert len(rendered_edges) == len(edges)
    for rendered in rendered_edges:
        coordinates = [
            float(n) for n in re.findall(r"-?\d+(?:\.\d+)?", rendered.find("s:path", NS).attrib["d"])
        ]
        assert all(left <= x <= right for x in coordinates[::2])
        assert all(top <= y <= bottom for y in coordinates[1::2])
        label = rendered.find("s:text", NS)
        assert left <= float(label.attrib["x"]) <= right
        assert top <= float(label.attrib["y"]) - 16
        assert float(label.attrib["y"]) + 6 <= bottom
    assert [edge.find("s:text", NS).text for edge in rendered_edges] == [edge["predicate"] for edge in edges]
