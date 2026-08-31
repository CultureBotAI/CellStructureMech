#!/usr/bin/env python3
"""Ingest one hostable Cell Image Library preview from public item metadata.

The public API requires a key, but each item landing page exposes JSON-LD with
the stable CIL DOI, per-item licence, attribution, primary distribution and a
source-hosted JPEG preview. This adapter reads one landing page at a time; it
does not search or scrape the collection in bulk.

Only Public Domain and exact CC BY 3.0/4.0 licence URLs are accepted. CIL does
not expose an NCBI Taxonomy identifier in JSON-LD, so the curator supplies a
taxon already asserted by the target record. Dry-run is the default.
"""

from __future__ import annotations

import argparse
import datetime
import json
import re
import sys
import urllib.parse
from html.parser import HTMLParser
from pathlib import Path

import yaml

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import (
    get_bytes,
    require_record_taxon,
    sha256,
    upsert,
    write_image_with_validated_record,
)
from cellstructuremech.validation.write_validated import ValidationFailedError

try:
    from corpus import REPO_ROOT
except ImportError:
    from scripts.corpus import REPO_ROOT


LANDING_PAGE = "https://www.cellimagelibrary.org/images/{accession}"
DOI_PREFIX = "doi:10.7295/W9CIL"
MODALITIES = (
    "TEM",
    "SEM",
    "CRYO_EM",
    "CRYO_ET",
    "FLUORESCENCE",
    "LIGHT",
    "AFM",
    "SUPER_RESOLUTION",
    "OTHER",
)
LICENCES = {
    "/licenses/by/3.0": (
        "CC_BY_3_0",
        "https://creativecommons.org/licenses/by/3.0/",
    ),
    "/licenses/by/3.0/legalcode": (
        "CC_BY_3_0",
        "https://creativecommons.org/licenses/by/3.0/",
    ),
    "/licenses/by/4.0": (
        "CC_BY_4_0",
        "https://creativecommons.org/licenses/by/4.0/",
    ),
    "/licenses/by/4.0/legalcode": (
        "CC_BY_4_0",
        "https://creativecommons.org/licenses/by/4.0/",
    ),
    # CIL's legacy public-domain selector is the value emitted by its item
    # metadata. It is a public-domain dedication, not a CC0 claim. The URL now
    # returns 404, so do not replace it with a different modern legal tool.
    "/choose/publicdomain-3": (
        "PUBLIC_DOMAIN",
        None,
    ),
}


class JsonLdParser(HTMLParser):
    """Collect application/ld+json blocks without depending on an HTML library."""

    def __init__(self) -> None:
        super().__init__()
        self._in_json_ld = False
        self._chunks: list[str] = []
        self.blocks: list[str] = []

    def handle_starttag(self, tag: str, attrs: list[tuple[str, str | None]]) -> None:
        values = {key.lower(): (value or "") for key, value in attrs}
        if tag.lower() == "script" and values.get("type", "").lower() == "application/ld+json":
            self._in_json_ld = True
            self._chunks = []

    def handle_data(self, data: str) -> None:
        if self._in_json_ld:
            self._chunks.append(data)

    def handle_endtag(self, tag: str) -> None:
        if tag.lower() == "script" and self._in_json_ld:
            self.blocks.append("".join(self._chunks))
            self._in_json_ld = False
            self._chunks = []


def json_ld_datasets(html: bytes) -> list[dict]:
    parser = JsonLdParser()
    parser.feed(html.decode("utf-8"))
    datasets: list[dict] = []
    for block in parser.blocks:
        value = json.loads(block)
        values = value if isinstance(value, list) else [value]
        datasets.extend(item for item in values if isinstance(item, dict) and item.get("@type") == "Dataset")
    if not datasets:
        raise ValueError("landing page contains no Dataset JSON-LD")
    return datasets


def licence_from_url(url: str) -> tuple[str, str | None]:
    parsed = urllib.parse.urlsplit(url)
    if parsed.scheme not in {"http", "https"} or parsed.netloc.lower() not in {
        "creativecommons.org",
        "www.creativecommons.org",
    }:
        raise ValueError(f"unrecognized CIL licence URL: {url!r}")
    key = parsed.path.rstrip("/")
    try:
        return LICENCES[key]
    except KeyError as exc:
        raise ValueError(f"CIL licence is not an accepted Public Domain or CC BY term: {url!r}") from exc


def _accession_name_matches(item: dict, accession: str) -> bool:
    return bool(re.search(rf"\bCIL:{re.escape(accession)}\b", str(item.get("name", ""))))


def item_metadata(html: bytes, accession: str) -> dict:
    datasets = json_ld_datasets(html)
    matching = [item for item in datasets if _accession_name_matches(item, accession)]
    if not matching:
        raise ValueError(f"JSON-LD does not identify CIL:{accession}")

    detailed = [item for item in matching if item.get("identifier")]
    if len(detailed) != 1:
        raise ValueError(f"expected one identified Dataset for CIL:{accession}; found {len(detailed)}")
    metadata = dict(detailed[0])
    expected_doi = f"{DOI_PREFIX}{accession}"
    if metadata.get("identifier") != expected_doi:
        raise ValueError(
            f"CIL:{accession} DOI mismatch: expected {expected_doi!r}, got {metadata.get('identifier')!r}"
        )

    image_urls = {
        item["image"]["url"]
        for item in matching
        if isinstance(item.get("image"), dict) and item["image"].get("url")
    }
    if len(image_urls) != 1:
        raise ValueError(f"expected one preview URL for CIL:{accession}; found {len(image_urls)}")
    metadata["preview_url"] = image_urls.pop()
    return metadata


def preview_url(metadata: dict, accession: str) -> tuple[str, str]:
    url = metadata["preview_url"]
    parsed = urllib.parse.urlsplit(url)
    expected_prefix = f"/media/thumbnail_display/{accession}/"
    if (
        parsed.scheme != "https"
        or parsed.netloc.lower() != "cildata.crbs.ucsd.edu"
        or not parsed.path.startswith(expected_prefix)
    ):
        raise ValueError(f"CIL preview URL is outside the expected source path: {url!r}")
    suffix = Path(parsed.path).suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        raise ValueError(f"unsupported CIL preview suffix: {suffix!r}")
    return url, suffix


def verify_image_format(data: bytes, suffix: str) -> None:
    """Refuse a 200 response containing an error page or unexpected file type."""
    signatures = {
        ".png": lambda value: value.startswith(b"\x89PNG\r\n\x1a\n"),
        ".jpg": lambda value: value.startswith(b"\xff\xd8\xff"),
        ".jpeg": lambda value: value.startswith(b"\xff\xd8\xff"),
        ".gif": lambda value: value.startswith((b"GIF87a", b"GIF89a")),
        ".webp": lambda value: len(value) >= 12 and value.startswith(b"RIFF") and value[8:12] == b"WEBP",
    }
    if not data or not signatures[suffix](data):
        raise ValueError(f"CIL preview bytes do not match the {suffix} filename")


def attribution(metadata: dict, accession: str) -> str:
    name = re.sub(r"\s+", " ", str(metadata.get("name", ""))).strip()
    match = re.match(rf"(.+?)\s+\([0-9]{{4}}\)\s+CIL:{re.escape(accession)}\b", name)
    if not match:
        raise ValueError("CIL JSON-LD name does not contain a named, dated attribution")
    return f"{match.group(1).strip()}; via Cell Image Library"


def build_image(
    metadata: dict,
    image_bytes: bytes,
    *,
    accession: str,
    taxon_id: str,
    taxon_label: str,
    modality: str,
    caption: str | None,
    reference: str | None,
    retrieved_on: str,
) -> dict:
    licence, licence_url = licence_from_url(metadata["license"])
    download_url, suffix = preview_url(metadata, accession)
    verify_image_format(image_bytes, suffix)
    entry = {
        "image_id": f"cil_{accession}",
        "file": f"cil_{accession}{suffix}",
        "file_sha256": sha256(image_bytes),
        "source": "CELL_IMAGE_LIBRARY",
        "source_accession": f"CIL:{accession}",
        "source_url": LANDING_PAGE.format(accession=accession),
        "download_url": download_url,
        "licence": licence,
        "attribution": attribution(metadata, accession),
        "modality": modality,
        "caption": caption or str(metadata.get("description", "")).strip(),
        "taxon_id": taxon_id,
        "taxon_label": taxon_label,
        "retrieved_on": retrieved_on,
        "notes": (
            "DOI, per-item licence, attribution and preview URL read from the landing-page JSON-LD. "
            "The source-served preview is used because CIL primary distributions may be TIFF or video. "
            "Taxon supplied by the curator because CIL exposes an organism name but no NCBI Taxonomy ID "
            "in its item JSON-LD."
        ),
    }
    if licence_url:
        entry["licence_url"] = licence_url
    if not entry["caption"]:
        entry.pop("caption")
    if reference:
        entry["reference"] = reference
    order = [
        "image_id",
        "file",
        "file_sha256",
        "source",
        "source_accession",
        "source_url",
        "download_url",
        "licence",
        "licence_url",
        "attribution",
        "modality",
        "caption",
        "taxon_id",
        "taxon_label",
        "reference",
        "retrieved_on",
        "notes",
    ]
    return {key: entry[key] for key in order if key in entry}


def ingest(args: argparse.Namespace) -> int:
    if not re.fullmatch(r"[1-9][0-9]*", args.accession):
        raise ValueError("--accession must be the numeric part of an exact CIL accession")
    if not re.fullmatch(r"NCBITaxon:[0-9]+", args.taxon):
        raise ValueError("--taxon must be NCBITaxon:NNN")
    if not args.taxon_label.strip():
        raise ValueError("--taxon-label must not be empty")
    if args.reference and not re.fullmatch(r"(?:DOI|PMID):.+", args.reference):
        raise ValueError("--reference must be DOI:... or PMID:...")

    record = yaml.safe_load(args.record.read_text(encoding="utf-8"))
    require_record_taxon(record, args.taxon)

    html = get_bytes(LANDING_PAGE.format(accession=args.accession))
    metadata = item_metadata(html, args.accession)
    # Refuse before fetching image bytes if the item is not hostable.
    licence_from_url(metadata["license"])
    download_url, _ = preview_url(metadata, args.accession)
    image_bytes = get_bytes(download_url)
    image = build_image(
        metadata,
        image_bytes,
        accession=args.accession,
        taxon_id=args.taxon,
        taxon_label=args.taxon_label,
        modality=args.modality,
        caption=args.caption,
        reference=args.reference,
        retrieved_on=datetime.date.today().isoformat(),
    )

    images, action = upsert(record.get("images"), "image_id", image)
    if not args.apply:
        print(f"# dry run — would have {action} this image on {args.record}\n")
        print(yaml.safe_dump([image], default_flow_style=False, sort_keys=False, allow_unicode=True))
        return 0

    record["images"] = images
    record_curation_event(
        record,
        curator="cell_image_library",
        action="ADD_IMAGE",
        llm_assisted=False,
        changes=(
            f"{action.capitalize()} CIL:{args.accession}; DOI, exact hostable licence, attribution "
            "and source-served preview URL verified from the item JSON-LD."
        ),
    )
    try:
        write_image_with_validated_record(
            record, args.record, image["file"], image_bytes, REPO_ROOT
        )
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    print(f"{action} {image['image_id']} on {args.record}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accession", required=True, help="Numeric CIL accession, e.g. 39991")
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--taxon", required=True)
    parser.add_argument("--taxon-label", required=True)
    parser.add_argument("--modality", required=True, choices=MODALITIES)
    parser.add_argument("--caption")
    parser.add_argument("--reference", help="DOI:... or PMID:... when a publication describes the image")
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        return ingest(args)
    except (OSError, UnicodeDecodeError, json.JSONDecodeError, KeyError, TypeError, ValueError) as exc:
        print(f"Cell Image Library import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
