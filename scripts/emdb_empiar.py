#!/usr/bin/env python3
"""Ingest an EMPIAR dataset plus its linked EMDB representative image.

EMPIAR deliberately has no organism field. This importer therefore requires a
chosen EMDB cross-reference and obtains the NCBI taxon from that EMDB entry.
The raw EMPIAR dataset is recorded in ``datasets`` (CC0); the small,
depositor-supplied EMDB PNG is recorded in ``images`` (EMDB policy says these
figures are not subject to copyright restrictions). Imaging resolution stays
in image notes and is never misrepresented as a biological physical property.

Dry-run is the default. ``coverage`` measures how often an EMPIAR keyword
cohort has the EMDB bridge needed for taxon resolution.
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
import urllib.parse
from pathlib import Path

import yaml

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import (
    get_bytes,
    get_json,
    image_destination,
    require_record_taxon,
    sha256,
    upsert,
)
from cellstructuremech.validation.write_validated import ValidationFailedError, write_validated_structure

try:
    from corpus import REPO_ROOT
except ImportError:
    from scripts.corpus import REPO_ROOT


EMPIAR_API = "https://www.ebi.ac.uk/empiar/api/entry"
EMPIAR_SEARCH = "https://www.ebi.ac.uk/emdb/api/empiar/search"
EMDB_API = "https://www.ebi.ac.uk/emdb/api/entry"
EMDB_POLICY = "https://www.ebi.ac.uk/emdb/policies.html"
EMPIAR_POLICY = "https://www.ebi.ac.uk/empiar/policies/"
EMPIAR_RE = re.compile(r"^EMPIAR-[0-9]+$")
EMDB_RE = re.compile(r"^EMD-[0-9]+$")
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


def walk_objects(value):
    if isinstance(value, dict):
        yield value
        for child in value.values():
            yield from walk_objects(child)
    elif isinstance(value, list):
        for child in value:
            yield from walk_objects(child)


def emdb_taxa(payload: dict) -> dict[str, str]:
    taxa: dict[str, str] = {}
    for obj in walk_objects(payload):
        natural = obj.get("natural_source")
        values = natural if isinstance(natural, list) else [natural]
        for source in values:
            if not isinstance(source, dict):
                continue
            organism = source.get("organism") or {}
            if organism.get("ncbi") is not None:
                taxa[f"NCBITaxon:{organism['ncbi']}"] = organism.get("valueOf_") or "unknown"
    return taxa


def empiar_xrefs(payload: dict) -> set[str]:
    values = payload.get("cross_references") or []
    return {value if isinstance(value, str) else value.get("name") for value in values} - {None}


def emdb_resolution(payload: dict) -> str | None:
    for obj in walk_objects(payload):
        value = obj.get("resolution")
        values = value if isinstance(value, list) else [value]
        for item in values:
            if isinstance(item, dict) and item.get("valueOf_"):
                return f"{item['valueOf_']} {item.get('units', 'Å')}"
    return None


def emdb_authors(payload: dict) -> list[str]:
    values = payload.get("admin", {}).get("authors_list", {}).get("author", [])
    if isinstance(values, dict):
        values = [values]
    return [item["valueOf_"] for item in values if item.get("valueOf_")]


def linked_entry(empiar: str, payload: dict) -> dict:
    entry = payload.get(empiar)
    if not isinstance(entry, dict):
        raise ValueError(f"EMPIAR API did not return {empiar}")
    if entry.get("status") != "REL":
        raise ValueError(f"{empiar} status is {entry.get('status')!r}, not REL")
    return entry


def build_entries(
    empiar: str,
    empiar_entry: dict,
    emdb: str,
    emdb_entry: dict,
    *,
    taxon_id: str,
    modality: str,
    caption: str | None,
    image_bytes: bytes,
    filename: str,
    retrieved_on: str,
) -> tuple[dict, dict]:
    taxa = emdb_taxa(emdb_entry)
    if taxon_id not in taxa:
        raise ValueError(f"{emdb} does not assert {taxon_id}; available taxa: {sorted(taxa)}")
    title = emdb_entry.get("admin", {}).get("title") or empiar_entry.get("title") or emdb
    authors = emdb_authors(emdb_entry)
    citation = next((item for item in empiar_entry.get("citation") or [] if item.get("doi")), None)
    reference = f"DOI:{citation['doi']}" if citation else f"DOI:{empiar_entry['entry_doi']}"
    resolution = emdb_resolution(emdb_entry)
    raw_count = sum(
        int(imageset.get("num_images_or_tilt_series") or 0)
        for imageset in empiar_entry.get("imagesets") or []
    )
    dataset = {
        "accession": f"EMPIAR:{empiar.removeprefix('EMPIAR-')}",
        "title": empiar_entry.get("title") or empiar,
        "description": "Raw electron-microscopy image dataset linked to the selected EMDB entry.",
        "organism": f"{taxon_id} {taxa[taxon_id]}",
        "dataset_type": "OTHER",
        "repository": "OTHER",
        "sample_types": [
            item.get("category") or "electron microscopy images"
            for item in empiar_entry.get("imagesets") or []
        ],
        "sample_count": raw_count,
        "url": f"https://www.ebi.ac.uk/empiar/{empiar}/",
        "publication": reference,
        "notes": (
            f"EMPIAR dataset DOI {empiar_entry.get('entry_doi')}; CC0 ({EMPIAR_POLICY}). "
            f"Taxon is not present in EMPIAR and was resolved through linked {emdb}."
        ),
    }
    image = {
        "image_id": f"emdb_{emdb.lower().replace('-', '_')}",
        "file": filename,
        "file_sha256": sha256(image_bytes),
        "source": "EMDB",
        "source_accession": emdb,
        "source_url": f"https://www.ebi.ac.uk/emdb/{emdb}",
        "download_url": (
            f"https://ftp.ebi.ac.uk/pub/databases/emdb/structures/{emdb}/images/"
            f"emd_{emdb.removeprefix('EMD-')}.png"
        ),
        "licence": "PUBLIC_DOMAIN",
        "licence_url": EMDB_POLICY,
        "attribution": f"{', '.join(authors) or 'EMDB depositor(s)'}; {emdb} depositor image",
        "modality": modality,
        "caption": caption or f"Depositor-supplied representative image for {title}.",
        "taxon_id": taxon_id,
        "taxon_label": taxa[taxon_id],
        "reference": reference,
        "retrieved_on": retrieved_on,
        "notes": (
            f"EMDB representative figure linked from {empiar} (dataset DOI "
            f"{empiar_entry.get('entry_doi')}). Taxon read from EMDB natural_source."
            + (f" Reported reconstruction resolution: {resolution}." if resolution else "")
        ),
    }
    return dataset, image


def coverage(query: str, rows: int) -> int:
    url = f"{EMPIAR_SEARCH}/{urllib.parse.quote(query)}?rows={rows}"
    results = get_json(url)
    released = [entry for entry in results.values() if entry.get("status") == "REL"]
    linked = [entry for entry in released if empiar_xrefs(entry)]
    by_scale: dict[str, int] = {}
    for entry in released:
        scale = entry.get("scale") or "unspecified"
        by_scale[scale] = by_scale.get(scale, 0) + 1
    fraction = (100 * len(linked) / len(released)) if released else 0
    print(
        f"query={query!r}: {len(linked)}/{len(released)} released entries "
        f"({fraction:.1f}%) have >=1 EMDB cross-reference; scales={by_scale}"
    )
    if len(results) >= rows:
        print("warning: result reached --rows cap; rerun with a larger value", file=sys.stderr)
        return 2
    return 0


def ingest(args: argparse.Namespace) -> int:
    if not EMPIAR_RE.fullmatch(args.empiar) or not EMDB_RE.fullmatch(args.emdb):
        raise ValueError("accessions must be exact EMPIAR-N and EMD-N identifiers")
    empiar_payload = get_json(f"{EMPIAR_API}/{args.empiar}")
    empiar_entry = linked_entry(args.empiar, empiar_payload)
    if args.emdb not in empiar_xrefs(empiar_entry):
        raise ValueError(f"{args.emdb} is not among {args.empiar} cross-references")
    emdb_entry = get_json(f"{EMDB_API}/{args.emdb}")
    if emdb_entry.get("emdb_id") != args.emdb:
        raise ValueError(f"EMDB endpoint did not return {args.emdb}")
    image_url = (
        f"https://ftp.ebi.ac.uk/pub/databases/emdb/structures/{args.emdb}/images/"
        f"emd_{args.emdb.removeprefix('EMD-')}.png"
    )
    image_bytes = get_bytes(image_url)
    if not image_bytes.startswith(b"\x89PNG\r\n\x1a\n"):
        raise ValueError(f"{args.emdb} representative image is not a PNG")
    filename = f"emdb_{args.emdb.lower().replace('-', '_')}.png"
    today = datetime.date.today().isoformat()
    dataset, image = build_entries(
        args.empiar,
        empiar_entry,
        args.emdb,
        emdb_entry,
        taxon_id=args.taxon,
        modality=args.modality,
        caption=args.caption,
        image_bytes=image_bytes,
        filename=filename,
        retrieved_on=today,
    )
    record = yaml.safe_load(args.record.read_text(encoding="utf-8"))
    require_record_taxon(record, args.taxon)
    datasets, dataset_action = upsert(record.get("datasets"), "accession", dataset)
    images, image_action = upsert(record.get("images"), "image_id", image)
    if not args.apply:
        print(
            f"# dry run — would have {dataset_action} dataset and {image_action} image "
            f"on {args.record}\n"
        )
        print(yaml.safe_dump({"datasets": [dataset], "images": [image]}, sort_keys=False))
        return 0

    destination = image_destination(args.record, filename, REPO_ROOT)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(image_bytes)
    record["datasets"] = datasets
    record["images"] = images
    record_curation_event(
        record,
        curator="emdb_empiar",
        action="ADD_IMAGE",
        llm_assisted=False,
        changes=(
            f"Added {args.empiar} dataset and {args.emdb} representative image; "
            "EMPIAR→EMDB cross-reference and EMDB natural_source taxon verified at import."
        ),
    )
    try:
        write_validated_structure(record, args.record)
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    print(f"{dataset_action} {args.empiar}; {image_action} {args.emdb} on {args.record}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    subparsers = parser.add_subparsers(dest="command", required=True)
    coverage_parser = subparsers.add_parser("coverage")
    coverage_parser.add_argument("--query", default="bacteria")
    coverage_parser.add_argument("--rows", type=int, default=10000)

    image_parser = subparsers.add_parser("image")
    image_parser.add_argument("--empiar", required=True)
    image_parser.add_argument("--emdb", required=True)
    image_parser.add_argument("--record", required=True, type=Path)
    image_parser.add_argument("--taxon", required=True, help="NCBITaxon:NNN selected from EMDB.")
    image_parser.add_argument("--modality", required=True, choices=MODALITIES)
    image_parser.add_argument("--caption")
    image_parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    try:
        return coverage(args.query, args.rows) if args.command == "coverage" else ingest(args)
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"EMDB/EMPIAR import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
