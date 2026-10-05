"""Real record tables remain accessible within named keyboard-scroll regions."""
from html.parser import HTMLParser
from pathlib import Path

import pytest
import yaml
from jinja2 import Environment, FileSystemLoader, select_autoescape

ROOT = Path(__file__).resolve().parents[1]
TEMPLATES = ROOT / "src/cellstructuremech/templates"


class Tables(HTMLParser):
    def __init__(self, markup):
        super().__init__()
        self.divs = []
        self.regions = []
        self.feed(markup)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "div":
            self.divs.append(attrs)
        if tag == "table":
            self.regions.append(next((d for d in reversed(self.divs)
                                      if "table-scroll" in d.get("class", "").split()), {}))

    def handle_endtag(self, tag):
        if tag == "div":
            self.divs.pop()


def render_record(relative):
    record = yaml.safe_load((ROOT / "data/structures" / relative).read_text())
    env = Environment(loader=FileSystemLoader(TEMPLATES), autoescape=select_autoescape(["html"]))
    env.filters["curie_url"] = lambda _curie: None
    return env.get_template("structure.html").render(
        r=record, root="../../", source_path="data/structures/" + relative, img_base="../../../data/images/"
    )


@pytest.mark.parametrize("record", ["appendage/archaeal_cannula.yaml", "ribonucleoprotein/ribosome.yaml",
                                 "secretion_system/type_iii_protein_secretion_system_complex.yaml"])
def test_every_real_record_table_has_named_focusable_scroll_region(record):
    markup = render_record(record)
    tables = Tables(markup)
    assert len(tables.regions) >= 2
    for region in tables.regions:
        assert region.get("role") == "region"
        assert region.get("tabindex") == "0"
        assert region.get("aria-label")
    assert f"CellStructureMech/blob/main/data/structures/{record}" in markup


def test_source_composition_names_are_not_presented_as_genes():
    markup = render_record("other/i_aaa_complex.yaml")
    composition_table = markup.split('aria-label="Source composition: i-AAA complex"', 1)[1]
    composition_table = composition_table.split("</table>", 1)[0]
    assert "<th>Source name</th>" in composition_table
    assert "<th>Gene</th>" not in composition_table
    assert "<td>zinc(2+)</td>" in composition_table
    assert "<td>YME1</td>" in composition_table
