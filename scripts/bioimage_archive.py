#!/usr/bin/env python3
"""Ingest one licensed BioImage Archive dataset and representative image.

BioImage Archive is served through the BioStudies API. Licences are per
submission, so this adapter accepts only direct ``S-BIAD`` accessions carrying
an exact CC0 or CC BY 4.0 statement. A selected file must occur exactly once in
one of the study's declared file manifests and its downloaded byte count must
match the manifest.

Archive-native TIFFs are frequently multi-channel. The curator must select a
one-based channel whose name is present in the manifest; that exact TIFF plane
is exported losslessly as PNG. Dry-run is the default.
"""

from __future__ import annotations

import argparse
import datetime
import io
import re
import sys
import urllib.parse
from pathlib import Path, PurePosixPath

import yaml
from PIL import Image

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import (
    get_bytes,
    get_json,
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


API = "https://www.ebi.ac.uk/biostudies/api/v1/studies"
FILES = "https://www.ebi.ac.uk/biostudies/files"
LANDING = "https://www.ebi.ac.uk/biostudies/studies"
ACCESSION_RE = re.compile(r"^S-BIAD[1-9][0-9]*$")
MAX_SOURCE_BYTES = 64 * 1024 * 1024
MAX_HOSTED_BYTES = 2 * 1024 * 1024
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
    ("CC0", "/publicdomain/zero/1.0"): (
        "CC0",
        "https://creativecommons.org/publicdomain/zero/1.0/",
    ),
    ("CC0", "/publicdomain/zero/1.0/legalcode"): (
        "CC0",
        "https://creativecommons.org/publicdomain/zero/1.0/",
    ),
    ("CC BY 4.0", "/licenses/by/4.0"): (
        "CC_BY_4_0",
        "https://creativecommons.org/licenses/by/4.0/",
    ),
    ("CC BY 4.0", "/licenses/by/4.0/legalcode"): (
        "CC_BY_4_0",
        "https://creativecommons.org/licenses/by/4.0/",
    ),
}


def attr_values(node: dict, name: str) -> list[str]:
    return [
        str(item["value"]).strip()
        for item in node.get("attributes") or []
        if item.get("name") == name and item.get("value") not in {None, ""}
    ]


def unique_attr(node: dict, name: str) -> str:
    values = attr_values(node, name)
    if len(values) != 1:
        raise ValueError(f"expected exactly one {name!r} attribute; found {values}")
    return values[0]


def walk_sections(section: dict):
    yield section
    for child in section.get("subsections") or []:
        yield from walk_sections(child)


def licence(section: dict) -> tuple[str, str]:
    matches = [item for item in section.get("attributes") or [] if item.get("name") == "License"]
    if len(matches) != 1:
        raise ValueError(f"study must carry exactly one per-accession License; found {len(matches)}")
    item = matches[0]
    urls = [
        value["value"]
        for value in item.get("valqual") or []
        if value.get("name") == "URL" and value.get("value")
    ]
    if len(urls) != 1:
        raise ValueError(f"study License must carry exactly one URL; found {urls}")
    parsed = urllib.parse.urlsplit(urls[0])
    if parsed.scheme != "https" or parsed.netloc.lower() not in {
        "creativecommons.org",
        "www.creativecommons.org",
    }:
        raise ValueError(f"unrecognized BioImage Archive licence URL: {urls[0]!r}")
    key = (str(item.get("value", "")).strip(), parsed.path.rstrip("/"))
    try:
        return LICENCES[key]
    except KeyError as exc:
        raise ValueError(f"BioImage Archive licence is not accepted for hosting: {key!r}") from exc


def study_contract(payload: dict, accession: str) -> dict:
    if not ACCESSION_RE.fullmatch(accession):
        raise ValueError("accession must be an exact direct BioImage Archive S-BIAD identifier")
    if payload.get("accno") != accession or payload.get("type") != "submission":
        raise ValueError(f"study endpoint did not return submission {accession}")
    if unique_attr(payload, "AttachTo") != "BioImages":
        raise ValueError(f"{accession} is not attached to the BioImages collection")
    template = unique_attr(payload, "Template")
    if not template.startswith("BioImages."):
        raise ValueError(f"{accession} is not a direct BioImages-template submission: {template!r}")
    doi = unique_attr(payload, "DOI")
    if doi.upper() != f"10.6019/{accession}":
        raise ValueError(f"{accession} DOI mismatch: {doi!r}")

    section = payload.get("section") or {}
    if section.get("type") != "Study":
        raise ValueError(f"{accession} has no Study section")
    image_licence, licence_url = licence(section)
    sections = list(walk_sections(section))
    authors = []
    for item in sections:
        if str(item.get("type", "")).lower() == "author":
            for name in attr_values(item, "Name"):
                if name not in authors:
                    authors.append(name)
    if not authors:
        raise ValueError(f"{accession} has no named author")
    organisms = sorted(
        {
            value.strip()
            for item in sections
            if item.get("type") == "Biosample"
            for value in attr_values(item, "Organism")
        }
    )
    if not organisms:
        raise ValueError(f"{accession} has no Biosample Organism")
    manifests = sorted(
        {
            value
            for item in sections
            if item.get("type") == "Study Component"
            for value in attr_values(item, "File List")
        }
    )
    if not manifests:
        raise ValueError(f"{accession} has no Study Component file manifest")
    methods = []
    for item in sections:
        if item.get("type") == "Image acquisition":
            for value in attr_values(item, "Imaging method"):
                if value not in methods:
                    methods.append(value)
    return {
        "title": unique_attr(section, "Title"),
        "description": unique_attr(section, "Description"),
        "doi": doi,
        "licence": image_licence,
        "licence_url": licence_url,
        "authors": authors,
        "organisms": organisms,
        "manifests": manifests,
        "methods": methods,
    }


def safe_source_path(path: str) -> PurePosixPath:
    value = PurePosixPath(path)
    if not path or value.is_absolute() or ".." in value.parts or "\\" in path:
        raise ValueError(f"unsafe BioImage Archive source path: {path!r}")
    return value


def file_url(accession: str, path: str) -> str:
    safe_source_path(path)
    return f"{FILES}/{accession}/{urllib.parse.quote(path, safe='/')}"


def exact_file(manifests: list[list[dict]], path: str) -> tuple[dict, int]:
    safe_source_path(path)
    matches = [
        (item, len(manifest))
        for manifest in manifests
        for item in manifest
        if item.get("type") == "file" and item.get("path") == path
    ]
    if len(matches) != 1:
        raise ValueError(f"source path {path!r} matched {len(matches)} manifest files")
    item, manifest_count = matches[0]
    size = item.get("size")
    if not isinstance(size, int) or not 0 < size <= MAX_SOURCE_BYTES:
        raise ValueError(f"manifest size for {path!r} is invalid or over {MAX_SOURCE_BYTES} bytes: {size!r}")
    return item, manifest_count


def channel_attributes(file_item: dict) -> list[tuple[int, str]]:
    channels = []
    for item in file_item.get("attributes") or []:
        match = re.fullmatch(r"Channel ([1-9][0-9]*)", str(item.get("name", "")))
        if match and item.get("value"):
            channels.append((int(match.group(1)), str(item["value"]).strip()))
    channels.sort()
    numbers = [number for number, _ in channels]
    if numbers != list(range(1, len(channels) + 1)):
        raise ValueError(f"manifest channels must be unique and contiguous from 1: {channels}")
    return channels


def render_source_image(
    source_bytes: bytes,
    file_item: dict,
    *,
    channel: int | None,
) -> tuple[bytes, str, str]:
    path = str(file_item["path"])
    suffix = PurePosixPath(path).suffix.lower()
    if len(source_bytes) != file_item["size"]:
        raise ValueError(
            f"downloaded byte count for {path!r} is {len(source_bytes)}, manifest says {file_item['size']}"
        )
    if suffix in {".tif", ".tiff"}:
        channels = channel_attributes(file_item)
        channel_map = dict(channels)
        if channel is None:
            raise ValueError("multi-channel TIFF import requires an explicit one-based --channel")
        if channel not in channel_map:
            raise ValueError(f"channel {channel} is not named in the manifest: {channels}")
        with Image.open(io.BytesIO(source_bytes)) as image:
            if image.format != "TIFF" or image.n_frames != len(channels):
                raise ValueError(
                    f"TIFF frame count {image.n_frames} does not match {len(channels)} named channels"
                )
            image.seek(channel - 1)
            if image.mode not in {"1", "L", "I", "I;16", "RGB", "RGBA"}:
                raise ValueError(f"unsupported TIFF channel mode: {image.mode}")
            plane = image.copy()
        output = io.BytesIO()
        plane.save(output, format="PNG", optimize=True)
        rendered = output.getvalue()
        channel_name = channel_map[channel]
        output_suffix = ".png"
    elif suffix in {".png", ".jpg", ".jpeg", ".gif", ".webp"}:
        if channel is not None:
            raise ValueError("--channel is only valid for a TIFF source")
        with Image.open(io.BytesIO(source_bytes)) as image:
            expected_formats = {
                ".png": "PNG",
                ".jpg": "JPEG",
                ".jpeg": "JPEG",
                ".gif": "GIF",
                ".webp": "WEBP",
            }
            if image.format != expected_formats[suffix]:
                raise ValueError(
                    f"source bytes are {image.format}, not the format declared by {suffix}"
                )
            image.verify()
        rendered = source_bytes
        channel_name = "source image"
        output_suffix = suffix
    else:
        raise ValueError(f"unsupported BioImage Archive image suffix: {suffix!r}")
    if len(rendered) > MAX_HOSTED_BYTES:
        raise ValueError(
            f"rendered image is {len(rendered)} bytes, over the {MAX_HOSTED_BYTES}-byte hosted cap"
        )
    return rendered, output_suffix, channel_name


def local_key(accession: str, source_path: str, channel: int | None) -> str:
    stem = re.sub(r"[^a-z0-9]+", "_", PurePosixPath(source_path).stem.lower()).strip("_")
    digest = sha256(f"{source_path}#{channel}".encode())[:10]
    channel_part = f"_c{channel}" if channel is not None else ""
    return f"bia_{accession.lower().replace('-', '_')}_{stem}{channel_part}_{digest}"


def build_entries(
    contract: dict,
    file_item: dict,
    source_bytes: bytes,
    rendered_bytes: bytes,
    *,
    accession: str,
    source_path: str,
    channel: int | None,
    channel_name: str,
    output_suffix: str,
    manifest_count: int,
    taxon_id: str,
    taxon_label: str,
    source_organism: str,
    modality: str,
    caption: str,
    retrieved_on: str,
) -> tuple[dict, dict]:
    if source_organism not in contract["organisms"]:
        raise ValueError(
            f"source organism {source_organism!r} is not a Biosample Organism: {contract['organisms']}"
        )
    key = local_key(accession, source_path, channel)
    source_url = f"{LANDING}/{accession}"
    reference = f"DOI:{contract['doi']}"
    source_digest = sha256(source_bytes)
    dataset = {
        "accession": accession,
        "title": contract["title"],
        "description": contract["description"],
        "organism": f"{taxon_id} {taxon_label}",
        "dataset_type": "OTHER",
        "repository": "OTHER",
        "sample_types": contract["methods"] or ["bioimaging data"],
        "url": source_url,
        "publication": reference,
        "notes": (
            f"Direct BioImage Archive submission under {contract['licence']} "
            f"({contract['licence_url']}); per-accession terms verified on {retrieved_on}."
        ),
    }
    image = {
        "image_id": key,
        "file": f"{key}{output_suffix}",
        "file_sha256": sha256(rendered_bytes),
        "source": "BIOIMAGE_ARCHIVE",
        "source_accession": f"{accession}:{source_path}" + (f"#channel={channel}" if channel else ""),
        "source_url": source_url,
        "download_url": file_url(accession, source_path),
        "licence": contract["licence"],
        "licence_url": contract["licence_url"],
        "attribution": f"{', '.join(contract['authors'])}; via BioImage Archive",
        "modality": modality,
        "caption": caption,
        "taxon_id": taxon_id,
        "taxon_label": taxon_label,
        "reference": reference,
        "retrieved_on": retrieved_on,
        "notes": (
            f"Exact file matched in a {manifest_count}-file study-component manifest; source byte "
            f"count {file_item['size']} and SHA-256 {source_digest}. Source organism "
            f"{source_organism!r} mapped by the curator to {taxon_id}. "
            + (
                f"Named TIFF channel {channel} ({channel_name}) exported losslessly to PNG."
                if channel is not None
                else "Source image bytes retained without transcoding."
            )
        ),
    }
    return dataset, image


def ingest(args: argparse.Namespace) -> int:
    if not ACCESSION_RE.fullmatch(args.accession):
        raise ValueError("--accession must be an exact direct S-BIAD identifier")
    if not re.fullmatch(r"NCBITaxon:[0-9]+", args.taxon):
        raise ValueError("--taxon must be NCBITaxon:NNN")
    if not args.taxon_label.strip() or not args.caption.strip():
        raise ValueError("--taxon-label and --caption must not be empty")
    record = yaml.safe_load(args.record.read_text(encoding="utf-8"))
    require_record_taxon(record, args.taxon)

    payload = get_json(f"{API}/{args.accession}")
    contract = study_contract(payload, args.accession)
    manifests = [get_json(file_url(args.accession, name)) for name in contract["manifests"]]
    file_item, manifest_count = exact_file(manifests, args.source_file)
    source_bytes = get_bytes(file_url(args.accession, args.source_file))
    rendered, output_suffix, channel_name = render_source_image(
        source_bytes, file_item, channel=args.channel
    )
    today = datetime.date.today().isoformat()
    dataset, image = build_entries(
        contract,
        file_item,
        source_bytes,
        rendered,
        accession=args.accession,
        source_path=args.source_file,
        channel=args.channel,
        channel_name=channel_name,
        output_suffix=output_suffix,
        manifest_count=manifest_count,
        taxon_id=args.taxon,
        taxon_label=args.taxon_label,
        source_organism=args.source_organism,
        modality=args.modality,
        caption=args.caption,
        retrieved_on=today,
    )
    datasets, dataset_action = upsert(record.get("datasets"), "accession", dataset)
    images, image_action = upsert(record.get("images"), "image_id", image)
    if not args.apply:
        print(
            f"# dry run — would have {dataset_action} dataset and {image_action} image "
            f"on {args.record}\n"
        )
        print(yaml.safe_dump({"datasets": [dataset], "images": [image]}, sort_keys=False))
        return 0

    record["datasets"] = datasets
    record["images"] = images
    record_curation_event(
        record,
        curator="bioimage_archive",
        action="ADD_IMAGE",
        llm_assisted=False,
        changes=(
            f"{dataset_action.capitalize()} {args.accession} and {image_action} exact file "
            f"{args.source_file!r}, channel {args.channel}; per-accession licence, manifest "
            "identity, byte count and source taxon mapping verified at import."
        ),
    )
    try:
        write_image_with_validated_record(
            record, args.record, image["file"], rendered, REPO_ROOT
        )
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    print(f"{dataset_action} {args.accession}; {image_action} {image['image_id']} on {args.record}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accession", required=True)
    parser.add_argument("--source-file", required=True, help="Exact path from a declared file manifest.")
    parser.add_argument("--channel", type=int, help="One-based named TIFF channel.")
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--taxon", required=True)
    parser.add_argument("--taxon-label", required=True)
    parser.add_argument("--source-organism", required=True, help="Exact Biosample Organism value.")
    parser.add_argument("--modality", required=True, choices=MODALITIES)
    parser.add_argument("--caption", required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        return ingest(args)
    except (
        OSError,
        Image.DecompressionBombError,
        Image.UnidentifiedImageError,
        KeyError,
        TypeError,
        ValueError,
    ) as exc:
        print(f"BioImage Archive import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
