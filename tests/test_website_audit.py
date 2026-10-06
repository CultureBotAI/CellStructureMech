"""Website audit regressions for #2070–2081, using actual published records."""

import json
import re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"


def test_all_current_location_references_have_source_labels(records):
    references = json.loads((ROOT / "data/website/references.json").read_text())["references"]
    locations = {xref for _, record in records for xref in record.get("xrefs") or []
                 if xref.startswith("uniprot.location:")}
    assert len(locations) > 100
    for identifier in locations:
        entry = references[identifier]
        assert entry["label"]
        assert entry["url"] == "https://www.uniprot.org/locations/" + identifier.split(":")[1]
        assert entry["source"] == "subcell.txt"
    assert references["uniprot.location:SL-0021"]["label"] == "Attachment organelle membrane"


def test_published_reference_routes_and_local_relationships():
    for path, trait in (("envelope/s_layer", "s_layer"), ("membrane_organelle/magnetosome", "magnetosome"),
                        ("microcompartment/carboxysome", "carboxysome")):
        page = (PAGES / "structures" / (path + ".html")).read_text()
        assert f'https://culturebotai.github.io/TraitMech/pages/traits/morphology/{trait}.html' in page
        assert "https://w3id.org/traitmech/" not in page
    page = (PAGES / "structures/appendage/archaeal_type_flagellum_filament.html").read_text()
    assert 'href="../../structures/appendage/archaeal_type_flagellum.html"' in page
    assert "archaeal-type flagellum" in page
    assert "http://purl.obolibrary.org/obo/GO_0097589" in page
    for path, number in (("inclusion/gas_vesicle", "0000214"), ("membrane_organelle/magnetosome", "0000216")):
        page = (PAGES / "structures" / (path + ".html")).read_text()
        resolver = 'https://www.ebi.ac.uk/ols4/ontologies/micro/classes/'
        assert resolver + f'http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMICRO_{number}' in page
        assert f'href="http://purl.obolibrary.org/obo/MICRO_{number}"' not in page


def test_synonyms_and_readable_labels_reach_generated_catalogue():
    browse = (PAGES / "browse.html").read_text()
    assert re.search(r'data-synonyms="[^"]*archaeal flagellum', browse)
    assert "terminal organelle" in browse
    assert ">Division machinery<" in browse
    landing = (PAGES / "index.html").read_text()
    assert 'href="embedding-map.html">MiniLM / PCA text map' in landing
    assert "Division_machinery" not in landing
    category = (PAGES / "category/division_machinery.html").read_text()
    assert "<h1>Division machinery</h1>" in category


def test_local_relationship_index_does_not_invent_records(records):
    from html.parser import HTMLParser

    class Links(HTMLParser):
        def __init__(self):
            super().__init__()
            self.hrefs = []

        def handle_starttag(self, tag, attrs):
            if tag == "a":
                self.hrefs.append(dict(attrs).get("href", ""))

    for path, record in records:
        if not (record.get("part_of") or record.get("has_part")):
            continue
        page = PAGES / "structures" / path.relative_to(ROOT / "data/structures").with_suffix(".html")
        links = Links()
        links.feed(page.read_text())
        for href in links.hrefs:
            if "structures/" in href and not href.startswith("https:"):
                assert (page.parent / href).resolve().is_file(), (page, href)


def test_every_relationship_has_a_source_grounded_label(records):
    local = {record["identifier"] for _, record in records}
    references = json.loads((ROOT / "data/website/references.json").read_text())["references"]
    for _, record in records:
        for identifier in (record.get("part_of") or []) + (record.get("has_part") or []):
            assert identifier in local or references.get(identifier, {}).get("label"), identifier
    assert references["GO:0005737"]["label"] == "cytoplasm"
    assert references["GO:0005856"]["label"] == "cytoskeleton"
