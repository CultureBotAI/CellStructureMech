"""Every claim-bearing section of a record must reach its published page.

`protein_examples` held 31 accessions, taxa, roles and PubMed citations that the
site never rendered (#157). Validation passed, `just render` passed, the
drift check passed — nothing compared what a record *holds* against what its
page *shows*, so the omission was invisible to every gate.

This is that comparison. It does not check how a field is rendered, only that a
record carrying content in a field produces a page that mentions it somewhere.
"""

from __future__ import annotations

import html
import re
from functools import cache
from pathlib import Path

import pytest

from scripts.corpus import REPO_ROOT, load_records

PAGES = REPO_ROOT / "pages" / "structures"

# Section -> a probe that must appear on the page of any record carrying it.
# The probe is a value out of the record, not a template string, so a section
# rendered under any heading passes and a section not rendered at all fails.
PROBES = {
    "components": lambda r: [c["label"] for c in r["components"]],
    "protein_examples": lambda r: [p["uniprot_id"].split(":")[-1]
                                   for c in r.get("components") or []
                                   for p in c.get("protein_examples") or []],
    "functions": lambda r: [f.get("label") or f.get("function_id") for f in r["functions"]],
    "taxonomic_distribution": lambda r: [t["taxon_label"] for t in r["taxonomic_distribution"]],
    "canonical_examples": lambda r: [t["taxon_label"] for t in r["canonical_examples"]],
    "associated_traits": lambda r: [t["trait_id"] for t in r["associated_traits"]],
    "physical_properties": lambda r: [p.get("property_label") or p.get("property_id")
                                      for p in r["physical_properties"]],
    "images": lambda r: [i.get("caption") or i.get("image_id") for i in r["images"]],
    "complex_compositions": lambda r: [c["source_accession"] for c in r["complex_compositions"]],
    "datasets": lambda r: [d.get("accession") or d.get("dataset_id") for d in r["datasets"]],
    # The page shows the prompt, not the id; the probe must name what a reader sees.
    "discussions": lambda r: [d["prompt"] for d in r["discussions"]],
}


@cache
def _records():
    """Parsed once; the parametrised tests would otherwise re-read the corpus
    eleven times and add five seconds to `just qc`."""
    return load_records()


@cache
def _page_text(path: Path) -> str:
    page = PAGES / path.parent.name / (path.stem + ".html")
    assert page.exists(), f"no rendered page for {path.name}"
    # Unescape first: a prompt containing an apostrophe reaches the page as
    # &#39; and would look absent to a naive substring test.
    return re.sub(r"\s+", " ", html.unescape(page.read_text(encoding="utf-8")))


@pytest.mark.parametrize("section", sorted(PROBES))
def test_every_populated_section_reaches_the_page(section):
    missing = []
    for path, record in _records():
        if section == "protein_examples":
            values = PROBES[section](record)
        elif not record.get(section):
            continue
        else:
            values = PROBES[section](record)
        if not values:
            continue
        text = _page_text(path)
        for value in values:
            if value and str(value) not in text:
                missing.append(f"{path.name}: {section} value {value!r} is absent from the page")
    assert not missing, "record content that no reader can see:\n  " + "\n  ".join(missing[:12])


def test_the_probe_set_covers_every_list_section_the_schema_defines():
    """A new section added to the schema must be added here too, or it could go
    unrendered exactly the way protein_examples did."""
    covered = set(PROBES) | {
        # Rendered as prose or metadata rather than as a listed section.
        "identifier", "label", "definition", "definition_source", "structure_category",
        "structure_kind", "mapping_status", "synonyms", "xrefs", "parent_structures",
        "part_of", "has_part", "curation_history", "causal_graphs", "grounding_status", "notes",
        "evidence", "external_links", "size_range", "abbreviations",
    }
    seen = {key for _, record in _records() for key in record}
    assert not (seen - covered), (
        f"record fields with no page-coverage probe: {sorted(seen - covered)}"
    )
