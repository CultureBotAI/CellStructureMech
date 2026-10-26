"""X-Mech unified website features on the CellStructureMech site (wave 1, 2026-10-25).

The 2026-10-25 review left four features partial: references in free text and
URL references could not be followed (evidence), CURIEs naming this corpus's own
records were plain code (term_links), "Label (A-Z)" was not alphabetical
(sorting), and the Schema link opened raw YAML (schema_docs). It also found no
retry after a failed text-map load and a landing card naming the wrong
projection. The fleet catalogue candidates added here are a skip link, a
themed not-found page, a per-record report route and a curation notice; the
licence footer now links the licence files themselves.

Each test is driven by an input on which the old rendering and the new one
differ, and is scoped to the section it is about: a page-wide "the link exists"
passes when the same link appears elsewhere on the page.
"""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from functools import cache
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import parse_qs, urlsplit

import pytest
import yaml

from scripts.render_pages import (
    GH_REPO,
    PROJECTION_NAMES,
    SITE_PAGES,
    SITE_PATH,
    _root_files_differ,
    autolink,
    curie_url,
    issue_url,
    schema_reference,
    status_meanings,
    template_environment,
)

ROOT = Path(__file__).resolve().parents[1]
PAGES = ROOT / "pages"
SCHEMA_DIR = ROOT / "src" / "cellstructuremech" / "schema"
GH_BLOB = "https://github.com/CultureBotAI/CellStructureMech/blob/main"
LICENSE_LINKS = {f"{GH_BLOB}/LICENSE-DATA", f"{GH_BLOB}/LICENSE-CODE", f"{GH_BLOB}/LICENSE"}


class Page(HTMLParser):
    """Anchors with their text, the footer, element ids and the focus order."""

    FOCUSABLE = {"a", "button", "input", "select", "textarea"}

    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.anchors: list[tuple[dict, str]] = []
        self.footer_links: list[str] = []
        self.footer_text: list[str] = []
        self.text: list[str] = []
        self.ids: dict[str, str] = {}
        self.tags: list[tuple[str, dict]] = []
        self.focusable: list[tuple[str, dict]] = []
        self._open: list[tuple[dict, list[str]]] = []
        self._footer = 0
        self._skip = 0
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if attrs.get("id"):
            self.ids[attrs["id"]] = tag
        if tag in ("script", "style"):
            self._skip += 1
        if tag == "footer":
            self._footer += 1
        reachable = (tag in self.FOCUSABLE and (tag != "a" or "href" in attrs)) or "tabindex" in attrs
        if reachable and attrs.get("type") != "hidden" and attrs.get("tabindex") != "-1":
            self.focusable.append((tag, attrs))
        if tag == "a":
            self._open.append((attrs, []))
            if self._footer:
                self.footer_links.append(attrs.get("href", ""))

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self._skip -= 1
        if tag == "a" and self._open:
            attrs, text = self._open.pop()
            self.anchors.append((attrs, " ".join("".join(text).split())))
        if tag == "footer":
            self._footer -= 1

    def handle_data(self, data):
        if self._skip:
            return
        self.text.append(data)
        for _, text in self._open:
            text.append(data)
        if self._footer:
            self.footer_text.append(data)

    def hrefs(self) -> list[str]:
        return [attrs.get("href", "") for attrs, _ in self.anchors]

    def anchor(self, href: str) -> tuple[dict, str]:
        matches = [(attrs, text) for attrs, text in self.anchors if attrs.get("href") == href]
        assert matches, f"no anchor to {href}"
        return matches[0]

    def plain_text(self) -> str:
        return " ".join("".join(self.text).split())

    def footer(self) -> str:
        return " ".join("".join(self.footer_text).split())


def section(html: str, heading: str) -> str:
    """The markup from an <h2> to the next one: what a reader sees under that heading."""
    start = html.index(f"<h2>{heading}</h2>")
    end = html.find("<h2", start + 1)
    return html[start:end if end != -1 else len(html)]


RECORD_PAGE = "structures/other/example.html"


def render_record(record: dict, **context) -> str:
    """One record page through the renderer's own environment."""
    values = {
        "root": "../../", "source_path": "data/structures/other/example.yaml",
        "img_base": "../../../data/images/other/example/", "local_records": {},
        "report_url": issue_url(record.get("identifier", "x:1"), RECORD_PAGE), **context,
    }
    base = {"identifier": "cellstructuremech:example", "label": "example structure",
            "structure_category": "OTHER", "structure_kind": "OTHER", "mapping_status": "PROPOSED"}
    return template_environment().get_template("structure.html").render(r={**base, **record}, **values)


def committed(relative: str) -> str:
    return (ROOT / relative).read_text(encoding="utf-8")


# ---------------------------------------------------------------- evidence --

LINKED_TOKENS = [
    ("See PMID:40891913.", "https://pubmed.ncbi.nlm.nih.gov/40891913/", "PMID:40891913"),
    ("from PMID 22425159;", "https://pubmed.ncbi.nlm.nih.gov/22425159/", "PMID 22425159"),
    ("native PMC3382715.1 main text", "https://pmc.ncbi.nlm.nih.gov/articles/PMC3382715/", "PMC3382715"),
    ("Figure 4, The EMBO Journal (2012), DOI:10.1038/emboj.2011.460. Copyright",
     "https://doi.org/10.1038/emboj.2011.460", "DOI:10.1038/emboj.2011.460"),
    ("Cell (2025), Figure 3, DOI 10.1016/j.cell.2025.09.027.", "https://doi.org/10.1016/j.cell.2025.09.027",
     "DOI 10.1016/j.cell.2025.09.027"),
    ("(1987), doi:10.1083/jcb.105.2.903, via PubMed Central", "https://doi.org/10.1083/jcb.105.2.903",
     "doi:10.1083/jcb.105.2.903"),
    ("Accession 10.6084/m9.figshare.1505174.v1 here", "https://doi.org/10.6084/m9.figshare.1505174.v1",
     "10.6084/m9.figshare.1505174.v1"),
    ("Public submissions are CC0 (https://cryoetdataportal.czscience.com/data-submission-policy).",
     "https://cryoetdataportal.czscience.com/data-submission-policy",
     "https://cryoetdataportal.czscience.com/data-submission-policy"),
    ("(https://en.wikipedia.org/wiki/Foo_(bar))", "https://en.wikipedia.org/wiki/Foo_(bar)",
     "https://en.wikipedia.org/wiki/Foo_(bar)"),
    ("q https://example.org/?a=1&b=2 end", "https://example.org/?a=1&b=2", "https://example.org/?a=1&b=2"),
]


@pytest.mark.parametrize("text,href,label", LINKED_TOKENS)
def test_autolink_links_reference_tokens_and_keeps_surrounding_text(text, href, label):
    page = Page(str(autolink(text)))
    _, anchor_text = page.anchor(href)
    assert anchor_text == label
    # The text a reader sees is unchanged: only the token became an anchor.
    assert page.plain_text() == " ".join(text.split())


UNLINKED_TEXT = [
    "javascript:alert(1)", "data:text/html,<b>x</b>", "https://user:pw@evil.example/",
    "https://", "version v10.1234/abc", "PMID:not-a-number", "PMID:..., DOI:..., or an opaque URL.",
    "ftp://example.org/file", "PMC12 is too short", "https://example.org:port/",
]


@pytest.mark.parametrize("text", UNLINKED_TEXT)
def test_autolink_leaves_unsafe_or_non_reference_text_unlinked(text):
    page = Page(str(autolink(text)))
    assert page.anchors == []
    assert page.plain_text() == " ".join(text.split())


MARKDOWN_AND_PUNCTUATION = [
    # A Markdown link: its label and its target are two tokens, neither
    # carrying the ](  between them (TraitMech#2022 linked .../x%5D(https://...).
    ("[10.1038/x](https://doi.org/10.1038/x)", ["https://doi.org/10.1038/x", "https://doi.org/10.1038/x"]),
    ("[site](https://example.org/a_(b))", ["https://example.org/a_(b)"]),
    ("**10.1099/y**", ["https://doi.org/10.1099/y"]),
    ("*https://example.org/italic*", ["https://example.org/italic"]),
    ("`10.1146/z`", ["https://doi.org/10.1146/z"]),
    ("`https://example.org/code`", ["https://example.org/code"]),
    ('"https://example.org/quoted"', ["https://example.org/quoted"]),
    ("'10.1000/single'", ["https://doi.org/10.1000/single"]),
    ("see https://example.org/a; and DOI:10.1000/b: then PMID:42.", [
        "https://example.org/a", "https://doi.org/10.1000/b", "https://pubmed.ncbi.nlm.nih.gov/42/"]),
    ("<https://example.org/angle>", ["https://example.org/angle"]),
    # A delimiter followed directly by more text: trimming the end cannot fix
    # these, so the token must stop at the delimiter itself.
    ("the `10.1146/z`-tagged entry", ["https://doi.org/10.1146/z"]),
    ("'https://example.org/q's page", ["https://example.org/q"]),
    # A ) that closes the reader's parenthesis ends the URL, and the next
    # reference may begin right after it (TraitMech#2033, DUFMech#377).
    ("(https://a.example/x)-(https://b.example/y)", ["https://a.example/x", "https://b.example/y"]),
    ("(DOI:10.1000/a)-(DOI:10.1000/b)", ["https://doi.org/10.1000/a", "https://doi.org/10.1000/b"]),
    ("see https://en.wikipedia.org/wiki/Foo_(bar) here", ["https://en.wikipedia.org/wiki/Foo_(bar)"]),
]


@pytest.mark.parametrize("text,hrefs", MARKDOWN_AND_PUNCTUATION)
def test_autolink_stops_at_markdown_and_punctuation(text, hrefs):
    page = Page(str(autolink(text)))
    assert page.hrefs() == hrefs
    assert not [href for href in page.hrefs() if re.search(r"%5[BD]|%2A|%60|%22|%27|[\]*`'\"]", href)]
    # Only the tokens became anchors: the Markdown a reader sees is unchanged.
    assert page.plain_text() == " ".join(text.split())


def test_autolink_escapes_markup_and_cannot_break_out_of_the_attribute():
    html = str(autolink('<script>alert(1)</script> https://example.org/x" onclick="alert(2) &'))
    page = Page(html)
    assert not any(tag == "script" for tag, _ in page.tags)
    assert page.hrefs() == ["https://example.org/x"]
    assert not any(key.startswith("on") for attrs, _ in page.anchors for key in attrs)
    assert "<script>alert(1)</script>" in page.plain_text()
    assert autolink(None) == "" and str(autolink(42)) == "42"


@pytest.mark.parametrize("reference,expected", [
    ("https://www.uniprot.org/uniprotkb/Q4J9K5", "https://www.uniprot.org/uniprotkb/Q4J9K5"),
    ("http://www.subtiwiki.uni-goettingen.de/v4/gene?id=x", "http://www.subtiwiki.uni-goettingen.de/v4/gene?id=x"),
    ("https://user:pw@evil.example/", None),
    ("https://exa mple.org/", None),
    ('https://example.org/"onmouseover=x', None),
])
def test_a_url_reference_is_its_own_resolver_when_it_is_safe(reference, expected):
    assert curie_url(reference) == expected


def test_free_text_references_link_in_every_record_context():
    """Each record surface the review found carrying plain-text references,
    with a distinct target per surface so one cannot stand in for another."""
    def url(name):
        return f"https://example.org/{name}"

    record = {
        "definition": f"Defined in {url('definition')}.",
        "images": [{"file": "a.png", "caption": f"Caption {url('caption')}", "modality": "TEM",
                    "taxon_id": "NCBITaxon:562", "taxon_label": "E. coli",
                    "attribution": "Figure 1, DOI:10.1000/attribution", "licence": "CC BY 4.0",
                    "source_url": "https://example.org/source", "source": "PMC", "source_accession": "x",
                    "reference": "DOI:10.1000/image-ref"}],
        "components": [{"label": "part", "component_type": "PROTEIN", "component_role": "CONSTITUENT",
                        "role": "Role per PMID:101", "evidence": [
                            {"reference": "PMID:1", "snippet": f"quote {url('snippet')}",
                             "notes": "Verbatim from PMC5161649."}],
                        "protein_examples": [{"uniprot_id": "UniProtKB:P0A6F5", "protein_label": "p",
                                              "taxon_id": "NCBITaxon:562", "taxon_label": "E. coli",
                                              "role": f"Example role {url('protein-role')}"}]}],
        "complex_compositions": [{"composition_id": "c1", "source_url": "https://example.org/cpx",
                                  "complex_label": "cpx", "source_accession": "CPX-1",
                                  "taxon_id": "NCBITaxon:562", "taxon_label": "E. coli",
                                  "retrieved_on": "2026-01-01", "participants": [],
                                  "notes": f"Composition {url('composition')}"}],
        "taxonomic_distribution": [{"taxon_id": "NCBITaxon:2", "taxon_label": "Bacteria",
                                    "presence": "COMMON", "note": f"Note {url('distribution')}"}],
        "canonical_examples": [{"taxon_id": "NCBITaxon:562", "taxon_label": "E. coli",
                                "note": f"Example {url('canonical')}"}],
        "functions": [{"label": "f", "description": f"Function {url('function')}"}],
        "associated_traits": [{"relation": "CONFERS", "trait_id": "METPO:1", "trait_label": "t",
                               "note": f"Trait {url('trait')}"}],
        "related_records": [{"identifier": "WikiPathways:WP1", "label": "pw", "relation": "SITE_OF",
                             "target_taxon_id": "NCBITaxon:562", "scope_note": f"Scope {url('scope')}",
                             "basis": f"Basis {url('basis')}", "source_version": "0" * 40, "evidence": []}],
        "physical_properties": [{"property": "LENGTH", "value": "1",
                                 "context": f"Context {url('property')}"}],
        "causal_graphs": [{"graph_id": "g1", "title": "graph", "description": f"Graph {url('graph')}",
                           "nodes": [], "edges": []}],
        "discussions": [{"kind": "OPEN_QUESTION", "status": "OPEN", "prompt": f"Prompt {url('prompt')}",
                         "rationale": f"Rationale {url('rationale')}"}],
        "datasets": [{"title": "d", "findings": f"Findings {url('findings')}",
                      "notes": f"Notes {url('dataset')}"}],
        "curation_history": [{"timestamp": "2026-10-01T00:00:00Z", "curator": "c", "action": "EDIT",
                              "changes": "Added PMID:40891913 as support."}],
    }
    hrefs = set(Page(render_record(record)).hrefs())
    expected = [url(name) for name in (
        "definition", "caption", "snippet", "protein-role", "composition", "distribution", "canonical",
        "function", "trait", "scope", "basis", "property", "graph", "prompt", "rationale", "findings",
        "dataset")] + [
        "https://doi.org/10.1000/attribution",                  # image attribution
        "https://pubmed.ncbi.nlm.nih.gov/101/",                 # component role
        "https://pmc.ncbi.nlm.nih.gov/articles/PMC5161649/",    # evidence notes
        "https://pubmed.ncbi.nlm.nih.gov/40891913/",            # curation history
    ]
    assert not [href for href in expected if href not in hrefs]


def test_the_review_url_evidence_reference_is_linked_in_its_section():
    """archaeal-type flagellum's UniProt URL references printed as plain <code>.

    Scoped to the evidence lists: the accession UniProtKB:Q4J9K5 in the same
    table already links the same URL, so a section-wide check passes unfixed.
    """
    html = committed("pages/structures/appendage/archaeal_type_flagellum.html")
    examples = section(html, "Organism-specific protein examples")
    lists = "".join(re.findall(r'<ul class="evidence">.*?</ul>', examples, re.S))
    url = "https://www.uniprot.org/uniprotkb/Q4J9K5"
    assert (url, url) in [(attrs.get("href"), text) for attrs, text in Page(lists).anchors]


# ------------------------------------------- corpus-wide acceptance scans ---

REFERENCE_TOKEN = re.compile(
    r"(?<![\w/.])(?:PMID:\s?\d+|PMC\d{4,}|doi:\s?10\.\d{4,9}/[^\s<>\"']+|"
    r"(?<!doi\.org/)10\.\d{4,9}/[^\s<>\"',;)]+|https?://[^\s<>\"']+)", re.I)
CURIE_CODE = re.compile(r"^[A-Za-z][A-Za-z0-9_.-]*:\S+$")


class Scan(HTMLParser):
    """What a reader of a record page's content cannot follow (the review's scan)."""

    def __init__(self, html: str):
        super().__init__(convert_charrefs=True)
        self.links = 0
        self.skip = 0
        self.chrome = 0
        self.code: list[str] | None = None
        self.code_linked = False
        self.plain: list[str] = []
        self.unlinked_codes: list[str] = []
        self.hrefs: list[str] = []
        self.feed(html)

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag in ("script", "style"):
            self.skip += 1
        if tag in ("header", "footer"):
            self.chrome += 1
        if tag == "a" and attrs.get("href"):
            self.links += 1
            self.hrefs.append(attrs["href"])
        if tag == "code":
            self.code, self.code_linked = [], self.links > 0

    def handle_endtag(self, tag):
        if tag in ("script", "style"):
            self.skip -= 1
        if tag in ("header", "footer"):
            self.chrome -= 1
        if tag == "a" and self.links:
            self.links -= 1
        if tag == "code" and self.code is not None:
            value = "".join(self.code).strip()
            if not self.chrome and not self.code_linked and CURIE_CODE.match(value):
                self.unlinked_codes.append(value)
            self.code = None

    def handle_data(self, data):
        if self.skip:
            return
        if self.code is not None:
            self.code.append(data)
        if not self.chrome and not self.links:
            self.plain += [match.group(0) for match in REFERENCE_TOKEN.finditer(data)]


@cache
def record_scans() -> dict[str, Scan]:
    return {page.relative_to(PAGES).as_posix(): Scan(page.read_text(encoding="utf-8"))
            for page in sorted((PAGES / "structures").glob("*/*.html"))}


def test_no_record_page_shows_a_reference_outside_a_link():
    """The review's acceptance check: 1,173 URL references and 463 pages of
    plain PMIDs, DOIs and PMC IDs could not be followed."""
    plain = {page: scan.plain for page, scan in record_scans().items() if scan.plain}
    assert not plain, f"{len(plain)} record pages show unlinked references, e.g. {list(plain.items())[:3]}"


def test_no_record_page_shows_an_unlinked_curie():
    """379 cellstructuremech: graph groundings, 149 header identifiers and the
    NCBIfam and RCSB_PDB CURIEs were plain code."""
    unlinked = {page: scan.unlinked_codes for page, scan in record_scans().items() if scan.unlinked_codes}
    assert not unlinked, f"{len(unlinked)} record pages, e.g. {list(unlinked.items())[:3]}"
    assert not [href for scan in record_scans().values() for href in scan.hrefs if href in ("#", "")]


# -------------------------------------------------------------- term_links --

@pytest.mark.parametrize("curie,expected", [
    ("NCBIfam:TIGR00351", "https://www.ncbi.nlm.nih.gov/genome/annotation_prok/evidence/TIGR00351"),
    ("RCSB_PDB:2NN6", "https://www.rcsb.org/structure/2NN6"),
    ("NCIT:C12345", "https://bioregistry.io/NCIT:C12345"),
    ("WikiPathways:WP5060", "https://bioregistry.io/WikiPathways:WP5060"),
    ("GO:0005840", "http://purl.obolibrary.org/obo/GO_0005840"),
    ("MICRO:0000214", "https://www.ebi.ac.uk/ols4/ontologies/micro/classes/"
                      "http%253A%252F%252Fpurl.obolibrary.org%252Fobo%252FMICRO_0000214"),
    ("cellstructuremech:carboxysome", None),
    ("uniprot.location:not-an-sl", None),
    ("not a curie", None),
    ("X:<y>", None),
    ("", None),
])
def test_curie_resolver_map_with_registry_fallback(curie, expected):
    assert curie_url(curie) == expected


LOCAL = {
    "GO:0005930": {"identifier": "GO:0005930", "label": "axoneme",
                   "page": "structures/cytoskeleton/axoneme.html"},
    "cellstructuremech:prostheca": {"identifier": "cellstructuremech:prostheca", "label": "prostheca",
                                    "page": "structures/appendage/prostheca.html"},
    "cellstructuremech:example": {"identifier": "cellstructuremech:example", "label": "example structure",
                                  "page": RECORD_PAGE},
}


def graph_record(*groundings: str) -> dict:
    nodes = [{"node_id": f"n{i}", "label": f"node {i}", "grounding": grounding}
             for i, grounding in enumerate(groundings)]
    edges = [{"subject": f"n{i}", "predicate": "part of", "object": f"n{i}"} for i in range(len(groundings))]
    return {"causal_graphs": [{"graph_id": "g", "title": "graph", "nodes": nodes, "edges": edges}]}


def test_entity_groundings_naming_a_record_open_its_page():
    html = render_record(graph_record(
        "GO:0005930",                  # another record, GO identity
        "cellstructuremech:prostheca",  # another record, minted identity
        "cellstructuremech:example",   # the page itself, minted
        "GO:0005737",                  # a GO term with no record here
        "cellstructuremech:retired",   # names no record: stays text, never "#"
        "NCIT:C1",                     # unknown prefix
    ), local_records=LOCAL)
    graph = Page(section(html, "Mechanism graphs"))
    hrefs = graph.hrefs()
    assert "../../structures/cytoskeleton/axoneme.html" in hrefs
    assert "../../structures/appendage/prostheca.html" in hrefs
    assert f"{GH_BLOB}/data/structures/other/example.yaml" in hrefs
    assert "http://purl.obolibrary.org/obo/GO_0005737" in hrefs
    assert "https://bioregistry.io/NCIT:C1" in hrefs
    assert "http://purl.obolibrary.org/obo/GO_0005930" not in hrefs
    assert not any("retired" in href for href in hrefs) and "#" not in hrefs
    assert "<code>cellstructuremech:retired</code>" in html


def test_component_grounding_naming_a_record_opens_it():
    html = render_record({"components": [{"label": "axoneme", "component_type": "PROTEIN_COMPLEX",
                                          "component_role": "CONSTITUENT", "grounding": "GO:0005930"}]},
                         local_records=LOCAL)
    components = Page(section(html, "Components"))
    assert components.anchor("../../structures/cytoskeleton/axoneme.html")[1] == "GO:0005930"


def test_citation_slots_keep_the_cited_source():
    """A GO term cited as evidence is the definition being quoted, so it goes to
    GO even when a record here takes that term as its identity; a minted
    identifier has no other resolver and opens its record."""
    html = render_record({
        "definition": "A thing.", "definition_source": "GO:0005930",
        "evidence": [{"reference": "GO:0005930"}, {"reference": "cellstructuremech:prostheca"}],
    }, local_records=LOCAL)
    evidence = Page(section(html, "Evidence"))
    assert "http://purl.obolibrary.org/obo/GO_0005930" in evidence.hrefs()
    assert "../../structures/cytoskeleton/axoneme.html" not in evidence.hrefs()
    assert "../../structures/appendage/prostheca.html" in evidence.hrefs()
    definition = Page(re.search(r'<p class="definition">.*?</p>', html, re.S).group(0))
    assert definition.hrefs() == ["http://purl.obolibrary.org/obo/GO_0005930"]


def test_own_identifier_links_its_yaml_or_its_ontology_term():
    minted_html = render_record({}, local_records=LOCAL)
    minted = Page(re.search(r'<p class="meta">.*?</p>', minted_html, re.S).group(0))
    assert minted.hrefs()[0] == f"{GH_BLOB}/data/structures/other/example.yaml"
    grounded = render_record({"identifier": "GO:0005930"}, local_records=LOCAL)
    header = Page(re.search(r'<p class="meta">.*?</p>', grounded, re.S).group(0))
    assert header.hrefs()[0] == "http://purl.obolibrary.org/obo/GO_0005930"


def test_a_real_cross_record_graph_grounding_opens_that_record():
    html = committed("pages/structures/appendage/archaeal_type_flagellum_motor.html")
    graph = Page(section(html, "Mechanism graphs"))
    assert graph.anchor("../../structures/appendage/archaeal_type_flagellum_filament.html")[1] == (
        "cellstructuremech:archaeal_type_flagellum_filament")


def test_a_trait_name_is_printed_once():
    """#2295: the reference label and the record's trait label both printed."""
    html = render_record({"associated_traits": [
        {"relation": "CONFERS", "trait_id": "traitmech:000064", "trait_label": "S-layer"},
        {"relation": "CONFERS", "trait_id": "METPO:1000704", "trait_label": "flagellated"},
    ]})
    traits = Page(section(html, "Associated traits")).plain_text()
    assert traits.count("S-layer") == 1 and "CONFERS traitmech:000064 — S-layer" in traits
    assert "CONFERS METPO:1000704 — flagellated" in traits
    page = committed("pages/structures/envelope/s_layer.html")
    assert Page(section(page, "Associated traits")).plain_text().count("S-layer S-layer") == 0


# ----------------------------------------------------------------- sorting --

def test_sort_control_offers_a_true_label_order_and_names_the_default_honestly():
    html = template_environment().get_template("browse.html").render(records=[], root="")
    options = re.findall(r'<option value="([^"]*)">([^<]*)</option>',
                         re.search(r'<select id="record-sort".*?</select>', html, re.S).group(0))
    assert ("label-asc", "Label (A–Z)") in options
    default = dict(options)[""]
    assert "Label" not in default and "Category" in default


NODE_SORT = r"""
const fs = require('fs'), vm = require('vm'), assert = require('assert');
function run(search) {
  const events = {};
  const ctl = v => ({value: v});
  const query = ctl(''), category = ctl(''), kind = ctl(''), status = ctl(''), sort = ctl('');
  const form = {hidden: true, addEventListener: (n, fn) => events[n] = fn};
  const count = {textContent: ''}, empty = {hidden: true};
  const tbody = {order: [], appendChild(row) {
    this.order = this.order.filter(r => r !== row); this.order.push(row); }};
  const row = (label, cat) => ({textContent: label, hidden: false, parentNode: tbody,
    dataset: {label: label, id: label, category: cat, kind: '', status: '', synonyms: ''}});
  const rows = [row('y-shaped link', 'APPENDAGE'), row('a axonemal microtubule', 'CYTOSKELETON'),
                row('m filament', 'CYTOSKELETON')];
  tbody.order = rows.slice();
  const ids = {'record-filters': form, 'record-query': query, 'record-category': category,
    'record-kind': kind, 'record-status': status, 'record-sort': sort, 'record-count': count,
    'record-empty': empty};
  const document = {getElementById: id => ids[id], querySelectorAll: () => rows};
  const urls = [];
  const window = {addEventListener: () => {},
    location: {href: 'https://x/pages/browse.html' + search, search},
    history: {replaceState: (s, t, u) => urls.push(String(u))}};
  vm.runInNewContext(fs.readFileSync(process.argv[1], 'utf8'),
                     {document, window, URL, URLSearchParams, setTimeout: fn => fn()});
  const labels = () => tbody.order.map(r => r.dataset.label);
  return {events, sort, labels, urls};
}
let page = run('');
assert.deepStrictEqual(page.labels(), ['y-shaped link', 'a axonemal microtubule', 'm filament']);
page.sort.value = 'label-asc'; page.events.change();
assert.deepStrictEqual(page.labels(), ['a axonemal microtubule', 'm filament', 'y-shaped link']);
assert.match(page.urls[page.urls.length - 1], /[?&]sort=label-asc/);
page.sort.value = 'label-desc'; page.events.change();
assert.deepStrictEqual(page.labels(), ['y-shaped link', 'm filament', 'a axonemal microtubule']);
page.sort.value = ''; page.events.change();
assert.deepStrictEqual(page.labels(), ['y-shaped link', 'a axonemal microtubule', 'm filament']);
assert.doesNotMatch(page.urls[page.urls.length - 1], /sort=/);
// A cold load of a shared URL restores the order.
page = run('?sort=label-asc');
assert.deepStrictEqual(page.labels(), ['a axonemal microtubule', 'm filament', 'y-shaped link']);
"""


def node_or_skip() -> str:
    node = shutil.which("node")
    if not node:
        pytest.skip("Node is required for browser behaviour checks")
    return node


def test_label_sort_is_alphabetical_and_the_default_keeps_the_rendered_order():
    script = ROOT / "src/cellstructuremech/templates/record-browser.js"
    subprocess.run([node_or_skip(), "-e", NODE_SORT, str(script)], check=True)


# ------------------------------------------------------------- schema_docs --

def test_schema_reference_documents_every_class_slot_and_enum():
    raw = [yaml.safe_load((SCHEMA_DIR / name).read_text(encoding="utf-8"))
           for name in ("cellstructuremech.yaml", "mech_shared.yaml")]
    reference = schema_reference()
    classes = {cls["name"]: cls for cls in reference["classes"]}
    enums = {enum["name"]: enum for enum in reference["enums"]}
    for schema in raw:
        assert set(schema.get("classes") or {}) <= set(classes)
        for name, enum in (schema.get("enums") or {}).items():
            values = [value["text"] for value in enums[name]["permissible"]]
            assert values == list(enum.get("permissible_values") or {})
    record = {slot["name"]: slot for slot in classes["CellStructureRecord"]["slots"]}
    declared = raw[0]["classes"]["CellStructureRecord"]["attributes"]
    assert set(declared) <= set(record)
    assert record["identifier"]["identifier"] and record["identifier"]["required"]
    assert record["components"]["multivalued"]
    assert record["components"]["ranges"] == [{"name": "StructuralComponent", "kind": "class"}]
    assert record["mapping_status"]["ranges"] == [{"name": "MappingStatusEnum", "kind": "enum"}]


def test_an_identifier_slot_is_documented_as_required(tmp_path):
    """LinkML treats an identifier slot as required whether or not it says so.

    This schema's own identifier also says required: true, so it cannot tell
    the two rules apart; a slot that is only an identifier can.
    """
    schema = tmp_path / "mini.yaml"
    schema.write_text(
        "id: https://example.org/mini\nname: mini\n"
        "prefixes:\n  linkml: https://w3id.org/linkml/\n"
        "imports:\n  - linkml:types\ndefault_range: string\n"
        "classes:\n  Thing:\n    attributes:\n      id:\n        identifier: true\n      note: {}\n",
        encoding="utf-8")
    slots = {slot["name"]: slot for slot in schema_reference(schema)["classes"][0]["slots"]}
    assert slots["id"]["required"] and slots["id"]["identifier"]
    assert not slots["note"]["required"]


def test_schema_page_lists_every_class_and_enum_in_scrollable_regions():
    html = committed("pages/schema.html")
    page = Page(html)
    reference = schema_reference()
    for cls in reference["classes"]:
        assert page.ids.get(f"class-{cls['name']}") == "section"
    for enum in reference["enums"]:
        assert page.ids.get(f"enum-{enum['name']}") == "section"
    regions = re.findall(
        r'<div class="table-scroll" role="region" tabindex="0" aria-label="[^"]+ slots">', html)
    assert len(regions) == sum(1 for cls in reference["classes"] if cls["slots"])


def test_schema_prose_is_not_autolinked():
    """Schema descriptions carry format examples, which must not become links."""
    schema = {"title": "t", "description": "One record.", "license": "", "source": "s", "modules": [],
              "classes": [{"name": "C", "description": "Cite as PMID:12345678 or https://example.org/x",
                           "is_a": "", "source": "", "slots": []}], "enums": []}
    html = template_environment().get_template("schema.html").render(schema=schema, root="")
    hrefs = Page(html[html.index('id="class-C"'):]).hrefs()
    assert "https://pubmed.ncbi.nlm.nih.gov/12345678/" not in hrefs and "https://example.org/x" not in hrefs


def nav_links(html: str) -> dict[str, str]:
    """Link text -> href in the page header's navigation."""
    header = Page(re.search(r"<header.*?</header>", html, re.S).group(0))
    return {text: attrs["href"] for attrs, text in header.anchors}


def test_schema_link_opens_the_generated_page_everywhere():
    landing = committed("pages/index.html")
    assert nav_links(landing)["Schema"] == "schema.html"
    card = re.search(r'<div class="actions">\s*<a class="btn" href="corpus.json">.*?</div>', landing, re.S)
    card = Page(card.group(0))
    assert card.anchor("schema.html")[1] == "LinkML schema"
    record = committed("pages/structures/envelope/s_layer.html")
    assert nav_links(record)["Schema"] == "../../schema.html"
    footer = Page(record[record.index("<footer"):])
    assert footer.anchor("../../schema.html")[1] == "LinkML schema"


# ----------------------------------------------------------------- license --

PAGE_TYPES = [
    "pages/index.html", "pages/browse.html", "pages/grounded.html", "pages/category/envelope.html",
    "pages/structures/envelope/s_layer.html", "pages/embedding-map.html", "pages/sequence-map.html",
    "pages/schema.html", "404.html",
]


@pytest.mark.parametrize("relative", PAGE_TYPES)
def test_every_page_type_footer_links_the_licence_files(relative):
    page = Page(committed(relative))
    assert set(page.footer_links) >= LICENSE_LINKS
    footer = page.footer()
    assert "Project data: CC BY 4.0. Code: BSD-3-Clause." in footer
    assert "Third-party source material keeps its own terms (licence scope)." in footer
    assert "https://creativecommons.org/licenses/by/4.0/" not in page.footer_links


def test_footer_licences_are_what_the_licence_files_say():
    scope = committed("LICENSE")
    assert "Creative Commons Attribution 4.0\nInternational (CC-BY-4.0). See LICENSE-DATA." in scope
    assert "is licensed under BSD-3-Clause. See LICENSE-CODE." in scope
    assert "retain their own licenses and notices" in scope
    assert committed("LICENSE-DATA").startswith("Attribution 4.0 International")
    assert committed("LICENSE-CODE").startswith("BSD 3-Clause License")


# --------------------------------------------------------------- skip_link --

@pytest.mark.parametrize("relative", PAGE_TYPES)
def test_the_first_tab_stop_skips_to_main(relative):
    page = Page(committed(relative))
    tag, attrs = page.focusable[0]
    assert tag == "a" and attrs.get("href") == "#main" and "skip-link" in attrs.get("class", "")
    assert page.ids.get("main") == "main"


# ---------------------------------------------------------- not_found_page --

def test_the_root_not_found_page_works_at_any_depth():
    """GitHub serves the repository-root 404.html for every missing address, at
    whatever depth was requested, so its own links are site-root-absolute
    (/CellStructureMech/pages/...) and nothing in it is relative."""
    html = committed("404.html")
    page = Page(html)
    assert any(tag == "meta" and attrs.get("content") == "noindex, follow" for tag, attrs in page.tags)
    references = [attrs[key] for _, attrs in page.tags for key in ("href", "src", "action") if attrs.get(key)]
    relative = [ref for ref in references if not ref.startswith(("/CellStructureMech/", "https://", "#"))]
    assert not relative, relative
    assert not [ref for ref in references if ref.startswith("https://culturebotai.github.io/CellStructureMech/")]
    local = [ref for ref in references if ref.startswith(SITE_PATH)]
    missing = [ref for ref in local if not (PAGES / ref[len(SITE_PATH):].split("#")[0]).is_file()]
    assert len(local) >= 8 and not missing, missing
    assert {SITE_PATH + "style.css", SITE_PATH + "theme-toggle.js", SITE_PATH + "browse.html"} <= set(local)
    form = next(attrs for tag, attrs in page.tags if tag == "form")
    assert form["action"] == SITE_PATH + "browse.html" and form["method"] == "get"
    assert any(tag == "input" and attrs.get("name") == "q" for tag, attrs in page.tags)
    assert not (PAGES / "404.html").exists(), "under pages/ the absolute assets read as third-party loads"


def test_check_reports_a_stale_or_missing_root_not_found_page(tmp_path):
    fresh, published = tmp_path / "fresh", tmp_path / "published"
    fresh.mkdir(), published.mkdir()
    (fresh / "404.html").write_text("new")
    assert _root_files_differ(fresh, published) == ["../404.html"]
    (published / "404.html").write_text("old")
    assert _root_files_differ(fresh, published) == ["../404.html"]
    (published / "404.html").write_text("new")
    assert _root_files_differ(fresh, published) == []


# ---------------------------------------------------------- feedback_route --

def test_issue_url_names_the_record_and_its_page():
    url = urlsplit(issue_url("cellstructuremech:a&b c", "structures/other/a.html"))
    assert f"{url.scheme}://{url.netloc}{url.path}" == f"{GH_REPO}/issues/new"
    query = parse_qs(url.query)
    assert query == {"title": ["Problem with cellstructuremech:a&b c"],
                     "body": [SITE_PAGES + "structures/other/a.html"]}


def test_every_record_page_reports_against_its_own_record(records):
    wrong = []
    for path, record in records:
        page_path = path.relative_to(ROOT / "data" / "structures").with_suffix(".html").as_posix()
        html = (PAGES / "structures" / page_path).read_text(encoding="utf-8")
        source = Page(re.search(r'<p class="source">.*?</p>', html, re.S).group(0))
        report = [attrs["href"] for attrs, text in source.anchors
                  if text == "Report a problem with this record"]
        query = parse_qs(urlsplit(report[0]).query) if report else {}
        expected = {"title": [f"Problem with {record['identifier']}"],
                    "body": [SITE_PAGES + "structures/" + page_path]}
        if query != expected:
            wrong.append(page_path)
    assert not wrong, wrong[:5]


# --------------------------------------------------------- curation_notice --

def test_landing_states_how_records_are_made_and_what_each_status_means(records):
    html = committed("pages/index.html")
    block = html[html.index('id="curation"'):]
    block = block[:block.index("</section>")]
    rows = re.findall(r"<tr>\s*<td><code>(\w+)</code></td>\s*<td>(\d+)</td>\s*<td>([^<]*)</td>", block)
    meanings = status_meanings()
    assert [(name, meaning) for name, _, meaning in rows] == list(meanings.items())
    counts = {name: int(count) for name, count, _ in rows}
    assert sum(counts.values()) == len(records)
    assert counts["PROPOSED"] == sum(1 for _, r in records if r["mapping_status"] == "PROPOSED")
    flagged = sum(any(event.get("llm_assisted") is True for event in r.get("curation_history") or [])
                  for _, r in records)
    assert f"{flagged} of {len(records)} records carry at least one curation event" in " ".join(block.split())


@pytest.mark.parametrize("status", ["PROPOSED", "REVIEWED"])
def test_a_record_status_is_explained_by_the_schema(status):
    html = render_record({"mapping_status": status})
    note = Page(re.search(r'<small class="status-note">.*?</small>', html, re.S).group(0)).plain_text()
    assert note.startswith("— " + status_meanings()[status])
    assert "How records are made" in note


def test_curation_history_marks_llm_assisted_events():
    html = render_record({"curation_history": [
        {"timestamp": "2026-10-01T00:00:00Z", "curator": "codex", "action": "EDIT", "changes": "a",
         "llm_assisted": True},
        {"timestamp": "2026-10-02T00:00:00Z", "curator": "a person", "action": "REVIEW", "changes": "b"},
    ]})
    history = section(html, "Curation history")
    assert "1 of 2 events marked" in Page(history).plain_text()
    items = re.findall(r"<li>.*?</li>", history, re.S)
    assert ["LLM-assisted" in item for item in items] == [True, False]


# ------------------------------------------------------------ load_failure --

FAKE_DOM = r"""
const fs = require('fs'), vm = require('vm'), assert = require('assert');
const html = fs.readFileSync(process.argv[1], 'utf8');
const script = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).join('\n');
let focused = null;
class El {
  constructor(tag) {
    this.tagName = tag; this.children = []; this.attrs = {}; this.listeners = {}; this.open = false;
    this.dataset = {}; this.style = {}; this.text = ''; this.hidden = false; this.value = '';
  }
  get textContent() {
    return this.text + this.children.map(c => typeof c === 'string' ? c : c.textContent).join('');
  }
  set textContent(v) { this.children = []; this.text = String(v); }
  setAttribute(k, v) { this.attrs[k] = String(v); }
  append(...xs) { this.children.push(...xs); }
  appendChild(x) { this.children.push(x); return x; }
  replaceChildren(...xs) { this.children = xs; this.text = ''; }
  addEventListener(name, fn) { (this.listeners[name] = this.listeners[name] || []).push(fn); }
  fire(name) {
    (this.listeners[name] || []).forEach(fn => fn({preventDefault() {}}));
    if (this['on' + name]) this['on' + name]();
  }
  focus() { focused = this; }
  getContext() { return new Proxy({}, {get: () => () => {}}); }
  getBoundingClientRect() { return {width: 920, height: 580, left: 0, top: 0}; }
  all() { return this.children.filter(c => typeof c !== 'string').flatMap(c => [c, ...c.all()]); }
}
const ids = {};
const el = id => ids[id] || (ids[id] = new El('div'));
// A table's rows as [cell text, ...] plus each row's links.
const rows = body => body.children.map(tr => ({
  cells: tr.children.map(td => td.textContent),
  links: tr.all().filter(x => x.tagName === 'a').map(a => a.href)}));
"""

NODE_MAP = FAKE_DOM + r"""
for (const id of ['embedding-map', 'map-category', 'map-details', 'map-query', 'map-record',
                  'map-legend', 'map-count', 'map-table-body', 'map-table-caption']) el(id);
el('map-table').hidden = true;  // as rendered: shown only once the data has loaded
const document = {getElementById: id => ids[id], createElement: tag => new El(tag),
                  createElementNS: (ns, tag) => new El(tag)};
function Option(text, value) { const o = new El('option'); o.textContent = text; o.value = value; return o; }
const window = {location: {href: 'https://x/pages/embedding-map.html', search: ''},
                history: {replaceState() {}}};
const records = [
  {identifier: 'GO:1', label: 'one', category: 'APPENDAGE', x: 0, y: 0, page: 'structures/a.html'},
  {identifier: 'GO:2', label: 'two', category: 'ENVELOPE', x: 1, y: 1, page: 'structures/b.html'}];
const neighbours = records.map(r => ({identifier: r.identifier, neighbors: []}));
const bodies = {'data/structure_text_map.json': {records},
                'data/structure_text_neighbors.json': {records: neighbours}};
let mode = 'abort', calls = 0;
function fetch(url) {
  calls += 1;
  if (mode === 'abort') return Promise.reject(new Error('Failed to fetch'));
  const ok = mode !== 'missing';
  return Promise.resolve({ok, status: ok ? 200 : 404, json: () => Promise.resolve(bodies[url])});
}
const settle = async () => { for (let i = 0; i < 10; i++) await new Promise(r => setImmediate(r)); };
const plot = ids['embedding-map'];
const alertBox = () => plot.all().find(el => el.attrs.role === 'alert');
(async () => {
  vm.runInNewContext(script, {document, window, fetch, URL, URLSearchParams, Option, Promise, console});
  await settle();
  let box = alertBox();
  assert.ok(box, 'an aborted load shows an alert');
  assert.equal(ids['map-table'].hidden, true, 'no data table offered for a map that did not load');
  assert.match(box.textContent, /Could not load embedding artifacts: Failed to fetch/);
  let retry = box.all().find(el => el.tagName === 'button');
  assert.equal(retry.textContent, 'Retry');
  assert.equal(focused, retry);
  assert.ok(box.all().some(el => el.tagName === 'a' && el.href === 'browse.html'));
  // An HTTP error is a failure too, not an empty plot.
  mode = 'missing';
  retry.listeners.click.forEach(fn => fn());
  await settle();
  box = alertBox();
  assert.match(box.textContent, /HTTP 404/);
  // The retry redraws every point once the request succeeds.
  mode = 'ok';
  const before = calls;
  box.all().find(el => el.tagName === 'button').listeners.click.forEach(fn => fn());
  await settle();
  assert.ok(calls > before);
  assert.equal(alertBox(), undefined);
  const svg = plot.children.find(el => el.tagName === 'svg');
  assert.equal(svg.children.filter(el => el.tagName === 'a').length, 2);
  assert.equal(ids['map-count'].textContent, '2 of 2 structures shown');
  // visual_alternative: the disclosure lists what the plot shows, each row linking its record.
  const table = ids['map-table'], body = ids['map-table-body'];
  assert.equal(table.hidden, false);
  assert.equal(body.children.length, 0, 'rows are built only when the disclosure opens');
  table.open = true; table.fire('toggle');
  assert.deepStrictEqual(rows(body), [
    {cells: ['one', 'GO:1', 'appendage', '0.000', '0.000'], links: ['structures/a.html']},
    {cells: ['two', 'GO:2', 'envelope', '1.000', '1.000'], links: ['structures/b.html']}]);
  assert.equal(ids['map-table-caption'].textContent, '2 of 2 structures plotted');
  ids['map-category'].value = 'ENVELOPE'; ids['map-category'].fire('change');
  assert.deepStrictEqual(rows(body).map(r => r.links), [['structures/b.html']]);
  assert.equal(ids['map-table-caption'].textContent, '1 of 2 structures plotted');
})().catch(error => { console.error(error); process.exit(1); });
"""

NODE_SEQ = FAKE_DOM + r"""
const data = JSON.parse(html.match(/<script id="seq-data" type="application\/json">([\s\S]*?)<\/script>/)[1]);
const main = [...html.matchAll(/<script>([\s\S]*?)<\/script>/g)].map(m => m[1]).join('\n');
for (const id of ['seq-form', 'seq-q', 'seq-color', 'seq-cat', 'seq-role', 'seq-channel', 'seq-length',
                  'seq-status', 'seq-legend', 'seq-details', 'seq-table-body', 'seq-table-caption',
                  'seq-tip']) el(id);
el('seq-table').hidden = true;
el('seq-data').textContent = JSON.stringify(data);
const canvas = el('seq-canvas');
canvas.parentElement = new El('div');
const document = {getElementById: id => ids[id], createElement: tag => new El(tag),
                  createTextNode: text => String(text)};
const window = {location: {href: 'https://x/pages/sequence-map.html', search: ''}, devicePixelRatio: 1,
                history: {replaceState() {}}, addEventListener() {}};
vm.runInNewContext(main, {document, window, URL, URLSearchParams, setTimeout});
const table = ids['seq-table'], body = ids['seq-table-body'];
assert.equal(table.hidden, false);
assert.equal(body.children.length, 0, 'rows are built only when the disclosure opens');
table.open = true; table.fire('toggle');
const all = rows(body);
assert.equal(all.length, data.proteins.length);
const total = data.proteins.length;
assert.equal(ids['seq-table-caption'].textContent, `${total} of ${total} proteins shown`);
// Each row names its protein and links its UniProt entry and every structure record it comes from.
data.proteins.forEach((p, i) => {
  const entry = p.id.startsWith('UniProtKB:')
    ? ['https://www.uniprot.org/uniprotkb/' + p.id.slice('UniProtKB:'.length) + '/entry'] : [];
  assert.equal(all[i].cells[0], p.label);
  assert.deepStrictEqual(all[i].links, [...entry, ...(p.records || []).map(r => r.page)]);
});
assert.ok(all.every(r => r.links.length > 1), 'every row links at least one structure record');
// The table follows the filters, as the status line does.
const group = data.groups[0];
ids['seq-cat'].value = group; ids['seq-cat'].fire('change');
const expected = data.proteins.filter(p => (p.groups || []).includes(group)).length;
assert.ok(expected > 0 && expected < data.proteins.length);
assert.equal(rows(body).length, expected);
assert.equal(ids['seq-status'].textContent, `${expected} of ${data.proteins.length} proteins shown`);
"""


def test_a_failed_text_map_load_offers_a_retry_that_redraws():
    """Also drives the text map's data table once the retried load succeeds."""
    subprocess.run([node_or_skip(), "-e", NODE_MAP, str(PAGES / "embedding-map.html")], check=True)


# ------------------------------------------------------- visual_alternative --

@pytest.mark.parametrize("relative,prefix,noun", [
    ("pages/embedding-map.html", "map", "structures"),
    ("pages/sequence-map.html", "seq", "proteins"),
])
def test_each_map_offers_a_keyboard_reachable_data_table(relative, prefix, noun):
    """The ids the scripts fill exist, behind a native disclosure, in a named
    focusable scroll region; without JavaScript the page points to Browse."""
    html = committed(relative)
    assert {f"{prefix}-table", f"{prefix}-table-body", f"{prefix}-table-caption"} <= set(Page(html).ids)
    assert re.search(
        rf'<details id="{prefix}-table" class="map-table" hidden>\s*<summary>View data as table</summary>\s*'
        rf'<div class="table-scroll" role="region" tabindex="0" aria-label="Plotted {noun}">', html)
    noscript = html[html.index("<noscript>"):html.index("</noscript>")]
    assert 'href="browse.html"' in noscript


def test_the_narrow_layout_track_cannot_grow_to_its_content():
    """A bare 1fr track grows to its widest item, so an opened data table could
    widen the page at 390 px; minmax(0, 1fr) keeps it to the viewport."""
    css = (ROOT / "src/cellstructuremech/templates/style.css").read_text(encoding="utf-8")
    narrow = re.search(r"@media \(max-width: 860px\) \{(.*?)\n\}", css, re.S).group(1)
    columns = re.search(r"\.page-with-sidebar \{[^}]*grid-template-columns:\s*([^;]+);", narrow).group(1)
    assert "1fr" in columns and "1fr" not in re.sub(r"minmax\(0,\s*1fr\)", "", columns)


def test_the_text_map_table_comes_before_its_focusable_points():
    """Every text-map point is a link; after the plot, the table would sit
    behind 1,001 Tab presses."""
    html = committed("pages/embedding-map.html")
    assert html.index('<details id="map-table"') < html.index('<div id="embedding-map"')


def test_the_sequence_map_table_lists_what_the_canvas_shows():
    subprocess.run([node_or_skip(), "-e", NODE_SEQ, str(PAGES / "sequence-map.html")], check=True)


# ------------------------------------------------------------- domain_view --

def test_landing_and_map_page_name_the_same_projection():
    method = json.loads(committed("data/embeddings/sequence_map.json"))["method"]
    expected = f"2D {PROJECTION_NAMES[method]} projection"
    landing = committed("pages/index.html")
    card = re.search(r"<h2>Sequence map \(pLM\)</h2>\s*<p>(.*?)</p>", landing, re.S).group(1)
    assert " ".join(card.split()).startswith(expected)
    assert expected in committed("pages/sequence-map.html")


# ------------------------------------------- cross_mech_links (repair) ---

# Verified routes (fleet route table, 2026-10-25) plus the record routes this
# site emits: PathwayMech's records/<Source>_<id>.html, and the TraitMech record
# pages data/website/references.json pins from TraitMech's own published browse.
SIBLING_PREFIXES = (
    "https://culturebotai.github.io/PathwayMech/pages/records/",
    "https://culturebotai.github.io/TraitMech/pages/traits/",
    "https://culturebotai.github.io/TraitMech/pages/browse.html?q=",
    "https://culturebotai.github.io/CultureMech/app/browser.html?q=",
    "https://culturebotai.github.io/MediaIngredientMech/browser.html?q=",
    "https://culturebotai.github.io/CommunityMech/browser.html?q=",
    "https://culturebotai.github.io/proteintraitsmech/browse.html?q=",
    "https://culturebotai.github.io/AntibioticMech/pages/browse.html?q=",
    "https://culturebotai.github.io/HabitatMech/pages/browse.html?q=",
    "https://culturebotai.github.io/NaturalProductMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/browse.html?q=",
    "https://culturebotai.github.io/TaxonMech/pages/taxon.html?id=NCBITaxon:",
    "https://culturebotai.github.io/PathwayMech/pages/browse.html?q=",
    "https://culturebotai.github.io/DUFMech/index.html?q=",
    "https://culturebotai.github.io/CMMMech/pages/browse.html?q=",
    "https://culturebotai.github.io/AIMech/pages/browse.html?q=",
)
SITE_ROOTS = {f"https://culturebotai.github.io/{name}/" for name in (
    "mechs", "CultureMech", "MediaIngredientMech", "CommunityMech", "TraitMech", "proteintraitsmech",
    "AntibioticMech")}


def test_every_sibling_url_uses_a_verified_route():
    hrefs = set()
    for page in [*PAGES.rglob("*.html"), ROOT / "404.html"]:
        html = page.read_text(encoding="utf-8")
        hrefs |= set(re.findall(r'href="(https://culturebotai\.github\.io/[^"]*)"', html))
    sibling = {href for href in hrefs if not href.startswith("https://culturebotai.github.io/CellStructureMech/")}
    unverified = sorted(href for href in sibling
                        if href not in SITE_ROOTS and not href.startswith(SIBLING_PREFIXES))
    assert not unverified, unverified[:10]
    assert any(href.startswith(SIBLING_PREFIXES[0]) for href in sibling)
    assert any(href.startswith(SIBLING_PREFIXES[1]) for href in sibling)
