"""Pin source labels and canonical website routes without changing structure records.

Download each URL in SOURCES to an input directory, then pass that directory to
this script. Rendering uses the committed snapshot offline. Source bodies and
their SHA-256 digests make a refresh reviewable before replacing the snapshot.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import re
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import urljoin

SOURCES = {
    "subcell.txt": "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/docs/subcell.txt",
    "trait-browse.html": "https://culturebotai.github.io/TraitMech/pages/browse.html",
    "micro-0000214.json": "https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000214",
    "micro-0000216.json": "https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms?obo_id=MICRO:0000216",
    "micro-ontology.json": "https://www.ebi.ac.uk/ols4/api/ontologies/micro",
}


# GO cellular-component targets represented in relationship lists but without
# a local structure record. Labels come from the declared OLS ontology source.
GO_RELATIONSHIP_TERMS = (
    '0000775', '0000781', '0000785', '0001411', '0005576', '0005618', '0005657',
    '0005737', '0005819', '0005829', '0005838', '0005856', '0012505', '0015629',
    '0015630', '0030140', '0030863', '0031522', '0032153', '0032156', '0032179',
    '0042764', '0043601', '0071944', '0097729', '0099115', '0120280',
)
SOURCES.update({
    "go-" + number + ".json": "https://www.ebi.ac.uk/ols4/api/ontologies/go/terms?obo_id=GO:" + number
    for number in GO_RELATIONSHIP_TERMS
})
SOURCES["go-ontology.json"] = "https://www.ebi.ac.uk/ols4/api/ontologies/go"


class TraitRoutes(HTMLParser):
    """Read each published row's identifier and actual record anchor together."""

    def __init__(self):
        super().__init__()
        self.routes = {}
        self.row = None
        self.capture = None

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        if tag == "tr":
            self.row = {}
        elif self.row is not None:
            if tag == "a" and attrs.get("href", "").startswith("traits/"):
                self.row["url"] = urljoin(SOURCES["trait-browse.html"], attrs["href"])
                self.capture = "label"
            elif tag == "code":
                self.capture = "identifier"

    def handle_data(self, text):
        if self.row is not None and self.capture:
            self.row[self.capture] = self.row.get(self.capture, "") + text

    def handle_endtag(self, tag):
        if tag in {"a", "code"}:
            self.capture = None
        if tag == "tr" and self.row is not None:
            identifier = self.row.get("identifier", "").strip()
            if identifier.startswith("traitmech:") and self.row.get("url"):
                self.routes[identifier] = {"label": self.row["label"].strip(), "url": self.row["url"],
                                           "source": "trait-browse.html"}
            self.row = None


def build(directory: Path, retrieved: str) -> dict:
    sources = [{"file": name, "url": url,
                "sha256": hashlib.sha256((directory / name).read_bytes()).hexdigest()}
               for name, url in SOURCES.items()]
    references = {}
    text = (directory / "subcell.txt").read_text()
    for block in text.split("\n//"):
        name = re.search(r"^(?:ID|IO|IT)   (.+)$", block, re.MULTILINE)
        accession = re.search(r"^AC   (SL-[0-9]{4})$", block, re.MULTILINE)
        if name and accession:
            identifier = accession[1]
            references["uniprot.location:" + identifier] = {
                "label": name[1].rstrip("."), "url": "https://www.uniprot.org/locations/" + identifier,
                "source": "subcell.txt",
            }
    browse = TraitRoutes()
    browse.feed((directory / "trait-browse.html").read_text())
    references.update(browse.routes)
    for number, label in (("0000214", "gas vacuole"), ("0000216", "magnetosome")):
        from render_pages import curie_url
        source = "micro-" + number + ".json"
        term, = json.loads((directory / source).read_text())["_embedded"]["terms"]
        identifier = "MICRO:" + number
        if term["obo_id"] != identifier or term["label"] != label or term["is_obsolete"] is not False:
            raise ValueError(f"Source identity changed for {identifier}; review the ontology before updating")
        references[identifier] = {"label": label, "url": curie_url(identifier), "source": source}
    for number in GO_RELATIONSHIP_TERMS:
        source = "go-" + number + ".json"
        term, = json.loads((directory / source).read_text())["_embedded"]["terms"]
        identifier = "GO:" + number
        expected_iri = "http://purl.obolibrary.org/obo/GO_" + number
        if term["obo_id"] != identifier or term["iri"] != expected_iri or term["is_obsolete"] is not False:
            raise ValueError(f"GO relationship identity changed: {identifier}")
        references[identifier] = {"label": term["label"], "url": expected_iri, "source": source}
    required = ("traitmech:" + n for n in ("000064", "000071", "000072"))
    if len(references) < 400 or not all(identifier in references for identifier in required):
        raise ValueError("Incomplete reference sources")
    return {"retrieved": retrieved, "sources": sources,
            "uniprot_release": re.search(r"^Release: +(.+)$", text, re.MULTILINE)[1],
            "uniprot_license": "CC-BY-4.0", "uniprot_attribution": "UniProt Consortium",
            "go_version": json.loads((directory / "go-ontology.json").read_text())["config"]["version"],
            "micro_version": json.loads((directory / "micro-ontology.json").read_text())["config"]["version"],
            "references": dict(sorted(references.items()))}


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input_dir", type=Path)
    parser.add_argument("--retrieved", required=True, help="Date the pinned source bodies were retrieved")
    parser.add_argument("--out", type=Path, default=Path("data/website/references.json"))
    args = parser.parse_args()
    snapshot = build(args.input_dir, args.retrieved)
    args.out.parent.mkdir(parents=True, exist_ok=True)
    args.out.write_text(json.dumps(snapshot, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
