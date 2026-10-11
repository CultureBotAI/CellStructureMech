"""Keep quiescent-bundle qualifications visible and panel evidence precise."""

from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SLUGS = (
    "quiescent_cell_microtubule_bundle",
    "quiescent_nuclear_microtubule_bundle",
)


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


def record(slug):
    return yaml.safe_load(
        (ROOT / "data/structures/cytoskeleton" / f"{slug}.yaml").read_text()
    )


@pytest.mark.parametrize("slug", SLUGS)
def test_original_discussion_explanations_have_displayed_rationales(slug):
    discussions = record(slug)["discussions"]
    assert len(discussions) == 8
    for discussion in discussions:
        assert discussion["notes"]
        assert discussion.get("rationale") == discussion["notes"]


@pytest.mark.parametrize("slug", SLUGS)
def test_original_graph_scope_has_displayed_description(slug):
    graphs = record(slug)["causal_graphs"]
    assert len(graphs) == (2 if slug == SLUGS[1] else 1)
    for graph in graphs:
        assert graph["scope_notes"]
        assert graph.get("description") == graph["scope_notes"]


@pytest.mark.parametrize("slug", SLUGS)
@pytest.mark.parametrize(
    ("section", "field"), [("discussions", "notes"), ("causal_graphs", "scope_notes")]
)
def test_generated_page_exposes_complete_original_qualifications(slug, section, field):
    page = VisibleText()
    page.feed((ROOT / "pages/structures/cytoskeleton" / f"{slug}.html").read_text())
    visible = " ".join(" ".join(page.parts).split())
    for item in record(slug)[section]:
        assert " ".join(item[field].split()) in visible


def test_tub3_localization_uses_correct_panel_and_expansion_channel():
    tub3 = next(
        example
        for component in record(SLUGS[1])["components"]
        for example in component.get("protein_examples", [])
        if example["uniprot_id"] == "UniProtKB:P09734"
    )
    evidence = next(
        evidence
        for evidence in tub3["evidence"]
        if evidence["reference"] == "DOI:10.7554/eLife.89958"
    )
    note = evidence["notes"]
    assert "Figure 2A" in note
    assert "Figure 2B" not in note
    assert "Figure 2 supplement 1A" in note
    assert "Tub3-3GFP alongside alpha-tubulin by expansion microscopy" in note
