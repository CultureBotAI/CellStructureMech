#!/usr/bin/env python3
"""Ingest one CC BY/CC0 PMC figure from the 2026 PMC Open Access S3 dataset.

The retired OA Web Service and legacy ``oa_comm`` prefixes are intentionally
not used. Article version, licence, JATS XML and media checksums all come from
the public ``pmc-oa-opendata`` bucket. PMC carries no NCBI organism identifier,
so a curator must supply a taxon already asserted by the target record.

Dry-run is the default. Multi-panel figures require an explicit
``--accept-multipanel`` acknowledgement. The ``coverage`` command reports
figure-level micrograph candidates, not merely article search hits.
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
import urllib.parse
import xml.etree.ElementTree as ET
from pathlib import Path

import yaml

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import (
    get_bytes,
    get_json,
    require_record_taxon,
    s3_https_url,
    sha256,
    upsert,
    verify_md5,
    write_image_with_validated_record,
)
from cellstructuremech.validation.write_validated import ValidationFailedError

try:
    from corpus import REPO_ROOT
except ImportError:
    from scripts.corpus import REPO_ROOT


BUCKET = "https://pmc-oa-opendata.s3.amazonaws.com"
ESEARCH = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esearch.fcgi"
PMC_RE = re.compile(r"^PMC[0-9]+$")
HOSTABLE_LICENSE_CODES = {"CC BY", "CC0"}
JATS_LICENSES = {
    "/licenses/by/3.0": ("CC BY", "CC_BY_3_0", "https://creativecommons.org/licenses/by/3.0/"),
    "/licenses/by/4.0": ("CC BY", "CC_BY_4_0", "https://creativecommons.org/licenses/by/4.0/"),
    "/publicdomain/zero/1.0": (
        "CC0",
        "CC0",
        "https://creativecommons.org/publicdomain/zero/1.0/",
    ),
}
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
MICROGRAPH = re.compile(
    r"\b(?:micrographs?|transmission electron microscopy images?|"
    r"scanning electron microscopy images?|electron microscopy images?)\b",
    re.IGNORECASE,
)
PANEL_MARKER = re.compile(
    r"(?:^|[\s;(])\(?[A-Ha-h]\)|(?:^|[.!?])\s*[A-Ha-h](?:\s*(?:,|and)\s*[A-Ha-h])*,"
)


def text_content(element: ET.Element | None) -> str:
    if element is None:
        return ""
    return re.sub(r"\s+", " ", "".join(element.itertext())).strip()


def latest_version(pmcid: str) -> int:
    query = urllib.parse.urlencode(
        {"list-type": "2", "prefix": f"metadata/{pmcid}.", "max-keys": "100"}
    )
    root = ET.fromstring(get_bytes(f"{BUCKET}/?{query}"))
    versions = []
    for key in root.findall("{*}Contents/{*}Key"):
        match = re.fullmatch(rf"metadata/{re.escape(pmcid)}\.([0-9]+)\.json", key.text or "")
        if match:
            versions.append(int(match.group(1)))
    if not versions:
        raise ValueError(f"{pmcid} has no metadata object in the current PMC OA S3 dataset")
    return max(versions)


def article_metadata(pmcid: str, version: int | None = None) -> dict:
    version = latest_version(pmcid) if version is None else version
    metadata = get_json(f"{BUCKET}/metadata/{pmcid}.{version}.json")
    if metadata.get("pmcid") != pmcid or metadata.get("version") != version:
        raise ValueError(f"metadata identity mismatch for {pmcid}.{version}")
    if metadata.get("is_retracted"):
        raise ValueError(f"{pmcid}.{version} is retracted")
    if metadata.get("license_code") not in HOSTABLE_LICENSE_CODES:
        raise ValueError(
            f"{pmcid}.{version} licence {metadata.get('license_code')!r} is not CC BY or CC0"
        )
    return metadata


def article_license(root: ET.Element, metadata_code: str) -> tuple[str, str]:
    """Return an exact schema licence from the article's JATS licence URL.

    PMC's metadata code says ``CC BY`` but does not encode the Creative Commons
    version. Treating every such article as CC BY 4.0 would silently alter the
    terms, so the version comes from the authoritative JATS ``<license>`` link.
    """
    hrefs: set[str] = set()
    for license_element in root.findall(".//{*}license"):
        for element in license_element.iter():
            href = element.get("{http://www.w3.org/1999/xlink}href")
            if href:
                hrefs.add(href)
    recognized = []
    for href in hrefs:
        parsed = urllib.parse.urlsplit(href)
        if parsed.netloc.lower() not in {"creativecommons.org", "www.creativecommons.org"}:
            continue
        key = parsed.path.rstrip("/")
        if key in JATS_LICENSES:
            recognized.append(JATS_LICENSES[key])
    if len(recognized) != 1:
        raise ValueError(
            f"JATS must contain exactly one recognized CC BY 3.0/4.0 or CC0 licence URL; "
            f"found {sorted(hrefs)}"
        )
    family, licence, canonical_url = recognized[0]
    if family != metadata_code:
        raise ValueError(
            f"PMC metadata licence {metadata_code!r} disagrees with JATS licence {family!r}"
        )
    return licence, canonical_url


def article_xml(metadata: dict) -> tuple[ET.Element, str]:
    xml_url, expected_md5 = s3_https_url(metadata["xml_url"])
    xml_bytes = get_bytes(xml_url)
    verify_md5(xml_bytes, expected_md5, f"{metadata['pmcid']} JATS XML")
    return ET.fromstring(xml_bytes), xml_url


def figure(root: ET.Element, figure_id: str) -> tuple[ET.Element, str, str, bool]:
    matches = [item for item in root.findall(".//{*}fig") if item.get("id") == figure_id]
    if len(matches) != 1:
        raise ValueError(f"figure id {figure_id!r} matched {len(matches)} JATS figures")
    item = matches[0]
    caption = text_content(item.find("{*}caption"))
    graphics = item.findall(".//{*}graphic")
    hrefs = [graphic.get("{http://www.w3.org/1999/xlink}href") for graphic in graphics]
    hrefs = [href for href in hrefs if href]
    if len(hrefs) != 1:
        raise ValueError(f"{figure_id} has {len(hrefs)} graphics; select a source with one graphic")
    label = text_content(item.find("{*}label")) or figure_id
    multipanel = bool(PANEL_MARKER.search(caption))
    return item, label, hrefs[0], multipanel


def article_authors(root: ET.Element) -> str:
    names = []
    for contrib in root.findall("./{*}front/{*}article-meta/{*}contrib-group/{*}contrib"):
        if contrib.get("contrib-type") not in {None, "author"}:
            continue
        name = contrib.find("{*}name")
        if name is not None:
            surname = text_content(name.find("{*}surname"))
            given = text_content(name.find("{*}given-names"))
            rendered = " ".join(part for part in (given, surname) if part)
        else:
            rendered = text_content(contrib.find("{*}collab"))
        if rendered and rendered not in names:
            names.append(rendered)
    if not names:
        return "PMC article author(s)"
    return ", ".join(names[:10]) + (", et al." if len(names) > 10 else "")


def media_object(metadata: dict, href: str) -> tuple[str, str | None]:
    target = Path(href).name
    matches = []
    for uri in metadata.get("media_urls") or []:
        url, expected_md5 = s3_https_url(uri)
        name = Path(urllib.parse.urlsplit(url).path).name
        if name == target or Path(name).stem == Path(target).stem:
            matches.append((url, expected_md5))
    if len(matches) != 1:
        raise ValueError(f"JATS graphic {href!r} matched {len(matches)} metadata media objects")
    return matches[0]


def local_figure_key(figure_id: str) -> str:
    """Make a stable safe key while retaining a hash for normalized source IDs."""
    key = re.sub(r"[^a-z0-9]+", "_", figure_id.lower()).strip("_")
    if not key:
        raise ValueError(f"figure id {figure_id!r} cannot form a local identifier")
    legacy_key = figure_id.lower().replace("-", "_")
    if key != legacy_key:
        key = f"{key}_{sha256(figure_id.encode())[:8]}"
    return key


def build_image(
    metadata: dict,
    root: ET.Element,
    *,
    figure_id: str,
    taxon_id: str,
    taxon_label: str,
    modality: str,
    caption_override: str | None,
    accept_multipanel: bool,
    retrieved_on: str,
) -> tuple[dict, bytes]:
    _, label, href, multipanel = figure(root, figure_id)
    if multipanel and not accept_multipanel:
        raise ValueError(
            f"{figure_id} appears multi-panel; inspect it and rerun with --accept-multipanel"
        )
    source_caption = text_content(
        next(item for item in root.findall(".//{*}fig") if item.get("id") == figure_id).find(
            "{*}caption"
        )
    )
    download_url, expected_md5 = media_object(metadata, href)
    image_bytes = get_bytes(download_url)
    verify_md5(image_bytes, expected_md5, f"{metadata['pmcid']} {figure_id}")
    suffix = Path(urllib.parse.urlsplit(download_url).path).suffix.lower()
    if suffix not in {".png", ".jpg", ".jpeg", ".gif", ".webp", ".svg"}:
        raise ValueError(f"unsupported PMC figure suffix: {suffix}")
    pmcid = metadata["pmcid"]
    version = metadata["version"]
    licence, licence_url = article_license(root, metadata["license_code"])
    doi = metadata.get("doi")
    pmid = metadata.get("pmid")
    if not doi and not pmid:
        raise ValueError(f"{pmcid}.{version} has neither DOI nor PMID")
    reference = f"DOI:{doi}" if doi else f"PMID:{pmid}"
    figure_key = local_figure_key(figure_id)
    filename = f"{pmcid.lower()}_{figure_key}{suffix}"
    image = {
        "image_id": f"pmc_{pmcid.lower()}_{figure_key}",
        "file": filename,
        "file_sha256": sha256(image_bytes),
        "source": "PMC",
        "source_accession": f"{pmcid}.{version} {figure_id}",
        "source_url": f"https://pmc.ncbi.nlm.nih.gov/articles/{pmcid}/",
        "download_url": download_url,
        "licence": licence,
        "licence_url": licence_url,
        "attribution": f"{article_authors(root)}; {metadata['license_code']}, via PubMed Central",
        "modality": modality,
        "caption": caption_override or source_caption,
        "taxon_id": taxon_id,
        "taxon_label": taxon_label,
        "reference": reference,
        "retrieved_on": retrieved_on,
        "notes": (
            f"{label} from article version {pmcid}.{version}; exact licence version read from "
            "JATS and media md5 read from the PMC OA S3 metadata. Taxon supplied by the curator "
            "because PMC has no taxon field."
            + (" Curator explicitly accepted the multi-panel figure." if multipanel else "")
        ),
    }
    return image, image_bytes


def coverage(term: str, limit: int) -> int:
    query = f'({term}) AND "cc by license"[filter]'
    url = f"{ESEARCH}?" + urllib.parse.urlencode(
        {"db": "pmc", "term": query, "retmode": "json", "retmax": limit, "sort": "relevance"}
    )
    result = get_json(url)["esearchresult"]
    ids = [f"PMC{value}" for value in result["idlist"]]
    scanned = unavailable = candidates = articles_with_candidates = 0
    candidate_ids: list[str] = []
    for pmcid in ids:
        try:
            metadata = article_metadata(pmcid)
            root, _ = article_xml(metadata)
        except (OSError, KeyError, ET.ParseError, TypeError, ValueError):
            unavailable += 1
            continue
        scanned += 1
        matching_figures = [
            item
            for item in root.findall(".//{*}fig")
            if MICROGRAPH.search(text_content(item.find("{*}caption")))
        ]
        count = len(matching_figures)
        candidate_ids.extend(
            f"{pmcid}.{metadata['version']}:{item.get('id')}" for item in matching_figures
        )
        candidates += count
        articles_with_candidates += bool(count)
    print(
        f"term={term!r}: {result['count']} CC BY article hits; scanned={scanned}/{len(ids)}, "
        f"unavailable={unavailable}, articles_with_micrograph_candidates="
        f"{articles_with_candidates}, figure_candidates={candidates}"
    )
    if int(result["count"]) > limit:
        print("coverage is a ranked sample; increase --limit for an exhaustive scan", file=sys.stderr)
    if candidate_ids:
        print("candidates: " + ", ".join(candidate_ids[:20]))
    return 0


def ingest(args: argparse.Namespace) -> int:
    if not PMC_RE.fullmatch(args.pmcid):
        raise ValueError("--pmcid must be an exact PMC accession")
    if not re.fullmatch(r"NCBITaxon:[0-9]+", args.taxon):
        raise ValueError("--taxon must be NCBITaxon:NNN")
    metadata = article_metadata(args.pmcid, args.version)
    root, _ = article_xml(metadata)
    image, image_bytes = build_image(
        metadata,
        root,
        figure_id=args.figure,
        taxon_id=args.taxon,
        taxon_label=args.taxon_label,
        modality=args.modality,
        caption_override=args.caption,
        accept_multipanel=args.accept_multipanel,
        retrieved_on=datetime.date.today().isoformat(),
    )
    record = yaml.safe_load(args.record.read_text(encoding="utf-8"))
    require_record_taxon(record, args.taxon)
    images, action = upsert(record.get("images"), "image_id", image)
    if not args.apply:
        print(f"# dry run — would have {action} this image on {args.record}\n")
        print(yaml.safe_dump([image], default_flow_style=False, sort_keys=False, allow_unicode=True))
        return 0
    record["images"] = images
    record_curation_event(
        record,
        curator="pmc_oa",
        action="ADD_IMAGE",
        llm_assisted=False,
        changes=(
            f"{action.capitalize()} {image['source_accession']}; version, CC licence, JATS figure "
            "identity and media md5 verified through the PMC OA S3 dataset."
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
    subparsers = parser.add_subparsers(dest="command", required=True)
    coverage_parser = subparsers.add_parser("coverage")
    coverage_parser.add_argument("--term", required=True, help="Entrez PMC query fragment.")
    coverage_parser.add_argument("--limit", type=int, default=100)

    image_parser = subparsers.add_parser("image")
    image_parser.add_argument("--pmcid", required=True)
    image_parser.add_argument("--version", type=int)
    image_parser.add_argument("--figure", required=True, help="Exact JATS fig/@id value.")
    image_parser.add_argument("--record", required=True, type=Path)
    image_parser.add_argument("--taxon", required=True)
    image_parser.add_argument("--taxon-label", required=True)
    image_parser.add_argument("--modality", required=True, choices=MODALITIES)
    image_parser.add_argument("--caption")
    image_parser.add_argument("--accept-multipanel", action="store_true")
    image_parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        return coverage(args.term, args.limit) if args.command == "coverage" else ingest(args)
    except (OSError, KeyError, ET.ParseError, TypeError, ValueError) as exc:
        print(f"PMC OA import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
