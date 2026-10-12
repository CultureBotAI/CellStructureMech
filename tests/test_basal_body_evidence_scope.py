"""Keep normal basal-body architecture distinct from absolute assembly requirements."""

from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml

PATH = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton/ciliary_basal_body.yaml"


@pytest.fixture
def record():
    return yaml.safe_load(PATH.read_text())


def test_basal_body_has_the_typed_organizing_center_parent(record):
    assert record["parent_structures"] == ["GO:0005815"]


@pytest.mark.parametrize("component_id", ["microtubule_triplets", "cartwheel"])
def test_component_essentiality_retains_partial_loss_uncertainty(record, component_id):
    component = next(c for c in record["components"] if c["component_id"] == component_id)
    assert component["essentiality"] == "UNKNOWN"


@pytest.mark.parametrize(
    ("component_id", "reference", "boundary"),
    [
        ("microtubule_triplets", "DOI:10.1091/mbc.9.6.1293", "nucleation"),
        ("cartwheel", "DOI:10.1016/j.cub.2007.11.046", "central"),
    ],
)
def test_primary_mutant_evidence_is_attached_to_the_component(
    record, component_id, reference, boundary
):
    component = next(c for c in record["components"] if c["component_id"] == component_id)
    evidence = next((e for e in component["evidence"] if e["reference"] == reference), None)
    assert evidence is not None
    assert boundary in evidence["notes"].lower()
    assert "UNKNOWN" in evidence["notes"]


def test_triplet_count_is_scoped_to_wild_type(record):
    prop = record["physical_properties"][0]
    assert prop["value"] == "9"
    assert "wild-type" in prop["context"]


def test_graph_scope_is_normal_architecture(record):
    graph = record["causal_graphs"][0]
    assert "wild-type" in graph["scope_notes"]
    assert graph["scope_status"] == "NONMECHANISTIC"


def test_graph_description_exposes_its_complete_scope(record):
    graph = record["causal_graphs"][0]
    assert graph["scope_notes"] in graph["description"]
    assert "nonmechanistic" in graph["description"]


def test_generated_page_exposes_graph_qualifications(record):
    class VisibleText(HTMLParser):
        def __init__(self):
            super().__init__()
            self.parts = []
            self.hidden = 0

        def handle_starttag(self, tag, attrs):
            if tag in {"script", "style"}:
                self.hidden += 1

        def handle_endtag(self, tag):
            if tag in {"script", "style"}:
                self.hidden -= 1

        def handle_data(self, data):
            if not self.hidden:
                self.parts.append(data)

    page = PATH.parents[3] / "pages/structures/cytoskeleton/ciliary_basal_body.html"
    parser = VisibleText()
    parser.feed(page.read_text())
    visible = " ".join(" ".join(parser.parts).split())
    graph = record["causal_graphs"][0]
    assert " ".join(graph["scope_notes"].split()) in visible
    assert "nonmechanistic" in visible


def test_ciliary_identity_and_parthood_are_preserved(record):
    assert record["identifier"] == "GO:0036064"
    assert record["part_of"] == ["GO:0005929"]


def test_normal_architecture_relationships_are_preserved(record):
    edges = record["causal_graphs"][0]["edges"]
    assert [(e["subject"], e["predicate"], e["object"]) for e in edges] == [
        ("cartwheel", "organizes", "microtubule_triplets"),
        ("microtubule_triplets", "form wall of", "ciliary_basal_body"),
        ("ciliary_basal_body", "nucleates", "axoneme"),
    ]


def test_source_neutral_grounding_task_and_agent_status_are_preserved(record):
    assert record["mapping_status"] == "PROPOSED"
    assert record["discussions"][0]["discussion_id"] == "ground_cartwheel_and_triplet_substructures"
    assert record["discussions"][0]["status"] == "OPEN"
