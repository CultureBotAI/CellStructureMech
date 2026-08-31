#!/usr/bin/env python3
"""Add a Wikimedia Commons image to a record, with its provenance read from the API.

Source queue row 2 (curation/source_queue.tsv). Four images reached the corpus
through one-off scripts before this existed (#45); every field they carry is
read here from Commons' own machine-readable metadata instead:

* **licence and attribution** from ``extmetadata`` (``LicenseShortName``,
  ``LicenseUrl``, ``Artist``, ``Credit``) — never from a research note;
* **taxon** from structured data ``P180`` (depicts) resolved through Wikidata
  ``P685`` (NCBI Taxonomy ID), so the taxon is the one Commons asserts;
* **integrity** by comparing the downloaded bytes' SHA-1 with ``imageinfo.sha1``
  before anything is written, and recording a SHA-256 for the corpus test.

A licence that does not permit hosting is refused rather than downloaded: the
record gets a link-only entry (no ``file``), which is what the schema and
``tests/test_corpus_integrity.py`` require. Dry-run by default.

    python scripts/fetch_commons_image.py --title "File:Carboxysomes_EM.jpg" \
        --record data/structures/microcompartment/carboxysome.yaml
    python scripts/fetch_commons_image.py ... --caption "..." --apply
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import re
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.validation.write_validated import ValidationFailedError, write_validated_structure

try:  # run as a script (scripts/ on sys.path) ...
    from corpus import REPO_ROOT
except ImportError:  # ... or imported by the tests
    from scripts.corpus import REPO_ROOT

# The Wikimedia User-Agent policy: "Scripts should use an informative
# User-Agent string with contact information, or they may be blocked."
UA = {"User-Agent": "CellStructureMech/0.1 (https://github.com/CultureBotAI/CellStructureMech; curation bot)"}
COMMONS_API = "https://commons.wikimedia.org/w/api.php"
WIKIDATA_API = "https://www.wikidata.org/w/api.php"
IMAGES_DIR = REPO_ROOT / "data" / "images"

# Commons' LicenseShortName -> our ImageLicenceEnum. Anything absent is refused
# rather than guessed: an unrecognised licence string is exactly when a human
# should look, and mapping it optimistically is how NC content gets hosted.
LICENCES = {
    "CC0": "CC0",
    "Public domain": "PUBLIC_DOMAIN",
    "CC BY 3.0": "CC_BY_3_0",
    "CC BY 4.0": "CC_BY_4_0",
    "CC BY-SA 3.0": "CC_BY_SA_3_0",
    "CC BY-SA 4.0": "CC_BY_SA_4_0",
    "CC BY-NC 4.0": "CC_BY_NC_4_0",
    "CC BY-NC-SA 4.0": "CC_BY_NC_SA_4_0",
    "CC BY-ND 4.0": "CC_BY_ND_4_0",
}
HOSTABLE = {"CC0", "PUBLIC_DOMAIN", "CC_BY_3_0", "CC_BY_4_0", "CC_BY_SA_3_0", "CC_BY_SA_4_0"}

MODALITIES = ("TEM", "SEM", "CRYO_EM", "CRYO_ET", "FLUORESCENCE", "LIGHT", "AFM", "SUPER_RESOLUTION", "OTHER")


def _get(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as response:
        return response.read()


def _json(api: str, **params) -> dict:
    params.setdefault("format", "json")
    return json.loads(_get(f"{api}?{urllib.parse.urlencode(params)}"))


def strip_tracking(url: str) -> str:
    """imageinfo.url carries utm_* parameters; the bare path is the stable URL (#34)."""
    return urllib.parse.urlunsplit(urllib.parse.urlsplit(url)._replace(query=""))


def slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "_", text.lower()).strip("_")


def plain(html: str) -> str:
    """Commons metadata is HTML. Tags become a space so adjacent words do not
    fuse, then the space before punctuation that leaves behind is removed —
    `<a>Tsai Y</a>, Sawaya MR` otherwise reads "Tsai Y , Sawaya MR"."""
    text = re.sub(r"\s+", " ", re.sub(r"<[^>]+>", " ", html or ""))
    return re.sub(r"\s+([,;.:])", r"\1", text).strip()


def file_page(title: str) -> dict:
    """imageinfo + extmetadata + the M-id for one File: title."""
    page = next(iter(_json(
        COMMONS_API, action="query", titles=title, prop="imageinfo",
        iiprop="url|extmetadata|sha1|size",
    )["query"]["pages"].values()))
    if "imageinfo" not in page:
        raise SystemExit(f"no such Commons file: {title}")
    return page


def depicted_taxon(pageid: int) -> tuple[str, str] | None:
    """SDC P180 (depicts) -> Wikidata item carrying P685 (NCBI Taxonomy ID)."""
    entity = _json(COMMONS_API, action="wbgetentities", ids=f"M{pageid}")["entities"][f"M{pageid}"]
    for claim in entity.get("statements", {}).get("P180", []):
        qid = claim["mainsnak"]["datavalue"]["value"]["id"]
        item = _json(WIKIDATA_API, action="wbgetentities", ids=qid, props="claims|labels",
                     languages="en")["entities"][qid]
        taxid = item.get("claims", {}).get("P685")
        if taxid:
            return f"NCBITaxon:{taxid[0]['mainsnak']['datavalue']['value']}", item["labels"]["en"]["value"]
    return None


def build_image(page: dict, title: str, *, modality: str, caption: str | None,
                taxon: tuple[str, str], licence: str, image_id: str, today: str,
                file_name: str | None, sha256: str | None) -> dict:
    info = page["imageinfo"][0]
    meta = info["extmetadata"]
    artist = plain(meta.get("Artist", {}).get("value", "")) or "unknown"
    short_name = plain(meta.get("LicenseShortName", {}).get("value", ""))
    credit = plain(meta.get("Credit", {}).get("value", ""))
    entry = {
        "image_id": image_id,
        "source": "WIKIMEDIA_COMMONS",
        "source_accession": f"{title} (M{page['pageid']})",
        "source_url": "https://commons.wikimedia.org/wiki/" + urllib.parse.quote(title.replace(" ", "_")),
        "download_url": strip_tracking(info["url"]),
        "licence": licence,
        "attribution": f"{artist}; {short_name}, via Wikimedia Commons",
        "modality": modality,
        "taxon_id": taxon[0],
        "taxon_label": taxon[1],
        "retrieved_on": today,
        "notes": (f"Licence, attribution and depicted taxon read from the Commons API "
                  f"(extmetadata + structured data P180 -> Wikidata P685) on {today}; "
                  f"file sha1 verified against imageinfo."
                  # Commons credits run to full citations and template text; notes is
                  # prose a reader scans, so keep the bound (#71).
                  + (f" Source credit: {credit[:300]}" if credit else "")),
    }
    # Commons omits LicenseUrl for public-domain files; an empty string is not a
    # uri and the write gate rejects it, so the optional field is simply absent.
    licence_url = meta.get("LicenseUrl", {}).get("value", "")
    if licence_url:
        entry["licence_url"] = licence_url
    if caption:
        entry["caption"] = caption
    if file_name:
        entry["file"] = file_name
        entry["file_sha256"] = sha256
    # Field order follows the schema so the emitted YAML reads top-down.
    order = ["image_id", "file", "file_sha256", "source", "source_accession", "source_url",
             "download_url", "licence", "licence_url", "attribution", "modality", "caption",
             "taxon_id", "taxon_label", "reference", "retrieved_on", "notes"]
    return {k: entry[k] for k in order if k in entry}


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--title", required=True, help='Commons file title, e.g. "File:Carboxysomes_EM.jpg"')
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--modality", required=True, choices=MODALITIES)
    parser.add_argument("--caption")
    parser.add_argument("--reference", help="DOI:... or PMID:... when the image comes from a publication")
    parser.add_argument("--image-id", help="Local id; defaults to a slug of the file title.")
    parser.add_argument("--taxon", help="NCBITaxon:NNN override when Commons has no P180 depicts statement.")
    parser.add_argument("--taxon-label", help="Required with --taxon.")
    parser.add_argument("--apply", action="store_true",
                        help="Write the file and the record (default: dry run).")
    args = parser.parse_args()

    page = file_page(args.title)
    info = page["imageinfo"][0]
    short = plain(info["extmetadata"].get("LicenseShortName", {}).get("value", ""))
    licence = LICENCES.get(short)
    if licence is None:
        print(f"unmapped Commons licence {short!r} — add it to LICENCES only after reading the terms",
              file=sys.stderr)
        return 2

    taxon = (args.taxon, args.taxon_label) if args.taxon else depicted_taxon(page["pageid"])
    if not taxon or not taxon[1]:
        print("no taxon: Commons has no P180 depicts statement with an NCBI id; pass --taxon/--taxon-label "
              "after checking the file page", file=sys.stderr)
        return 2

    doc = yaml.safe_load(args.record.read_text(encoding="utf-8"))
    named = {t["taxon_id"] for t in doc.get("taxonomic_distribution") or []}
    named |= {t["taxon_id"] for t in doc.get("canonical_examples") or []}
    if taxon[0] not in named:
        print(f"{taxon[0]} is not in the record's taxonomic_distribution or canonical_examples; "
              "add the taxon to the record first — an image of a taxon the record does not claim is "
              "evidence for nothing", file=sys.stderr)
        return 2

    image_id = args.image_id or slug(args.title.removeprefix("File:"))
    hostable = licence in HOSTABLE
    today = datetime.date.today().isoformat()
    file_name = sha256 = None
    data = None

    if hostable:
        data = _get(strip_tracking(info["url"]))
        actual = hashlib.sha1(data).hexdigest()
        if actual != info["sha1"]:
            print(f"sha1 mismatch: got {actual}, Commons says {info['sha1']}", file=sys.stderr)
            return 1
        suffix = Path(urllib.parse.urlparse(info["url"]).path).suffix.lower()
        file_name = slug(Path(args.title.removeprefix("File:")).stem) + suffix
        sha256 = hashlib.sha256(data).hexdigest()

    entry = build_image(page, args.title, modality=args.modality, caption=args.caption, taxon=taxon,
                        licence=licence, image_id=image_id, today=today, file_name=file_name, sha256=sha256)
    if args.reference:
        entry["reference"] = args.reference

    existing = {i["image_id"]: i for i in doc.get("images") or []}
    action = "updated" if image_id in existing else "added"
    if not args.apply:
        print(f"# dry run — would have {action} this image on {args.record}\n")
        print(yaml.safe_dump([entry], default_flow_style=False, sort_keys=False, allow_unicode=True))
        print(f"# licence {licence} ({'hosted copy' if hostable else 'LINK-ONLY: licence forbids hosting'})")
        return 0

    if data is not None:
        dest = IMAGES_DIR / args.record.parent.name / args.record.stem / file_name
        dest.parent.mkdir(parents=True, exist_ok=True)
        dest.write_bytes(data)
    images = [i for i in doc.get("images") or [] if i["image_id"] != image_id]
    doc["images"] = images + [entry]
    record_curation_event(
        doc, curator="fetch_commons_image", action="ADD_IMAGE", llm_assisted=False,
        changes=f"{action.capitalize()} Commons image {args.title} ({licence}, {taxon[1]}); licence, "
                f"attribution and taxon read from the Commons and Wikidata APIs at retrieval.",
    )
    try:
        write_validated_structure(doc, args.record)
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    print(f"{action} {image_id} on {args.record}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
