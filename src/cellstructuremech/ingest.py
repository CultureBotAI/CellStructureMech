"""Small, source-neutral helpers for curator-controlled ingestion scripts."""

from __future__ import annotations

import hashlib
import json
import re
import ssl
import urllib.parse
import urllib.request
from pathlib import Path

import truststore

from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    validate_structure,
    write_validated_structure,
)

USER_AGENT = {
    "User-Agent": (
        "CellStructureMech/0.1 "
        "(https://github.com/CultureBotAI/CellStructureMech; curation bot)"
    )
}
TLS_CONTEXT = truststore.SSLContext(ssl.PROTOCOL_TLS_CLIENT)


def get_bytes(url: str) -> bytes:
    """Read one public source URL with the repository's identifying User-Agent."""
    request = urllib.request.Request(url, headers=USER_AGENT)
    with urllib.request.urlopen(request, timeout=120, context=TLS_CONTEXT) as response:
        return response.read()


def get_json(url: str) -> dict:
    return json.loads(get_bytes(url))


def post_json(url: str, payload: dict) -> dict:
    """POST JSON to one public API with the repository's standard transport."""
    request = urllib.request.Request(
        url,
        data=json.dumps(payload).encode("utf-8"),
        headers={**USER_AGENT, "Content-Type": "application/json"},
        method="POST",
    )
    with urllib.request.urlopen(request, timeout=120, context=TLS_CONTEXT) as response:
        return json.loads(response.read())


def named_taxa(record: dict) -> set[str]:
    """Taxa a record already claims; importers may not silently broaden this set."""
    taxa = {item["taxon_id"] for item in record.get("taxonomic_distribution") or []}
    taxa |= {item["taxon_id"] for item in record.get("canonical_examples") or []}
    return taxa


def require_record_taxon(record: dict, taxon_id: str) -> None:
    if taxon_id not in named_taxa(record):
        raise ValueError(
            f"{taxon_id} is not in the record's taxonomic_distribution or canonical_examples"
        )


def upsert(items: list[dict] | None, key: str, value: dict) -> tuple[list[dict], str]:
    existing = items or []
    action = "updated" if any(item.get(key) == value[key] for item in existing) else "added"
    return [item for item in existing if item.get(key) != value[key]] + [value], action


def sha256(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def s3_https_url(uri: str) -> tuple[str, str | None]:
    """Convert the PMC dataset's s3:// URL to anonymous HTTPS and return its md5."""
    parsed = urllib.parse.urlsplit(uri)
    if parsed.scheme != "s3" or parsed.netloc != "pmc-oa-opendata":
        raise ValueError(f"unexpected PMC object URI: {uri}")
    query = urllib.parse.parse_qs(parsed.query)
    expected_md5 = query.get("md5", [None])[0]
    quoted_path = urllib.parse.quote(parsed.path.lstrip("/"), safe="/")
    return f"https://pmc-oa-opendata.s3.amazonaws.com/{quoted_path}", expected_md5


def verify_md5(data: bytes, expected: str | None, label: str) -> None:
    if expected is None:
        raise ValueError(f"{label} has no md5 in source metadata")
    actual = hashlib.md5(data).hexdigest()  # noqa: S324 — integrity, not cryptography
    if actual != expected:
        raise ValueError(f"{label} md5 mismatch: got {actual}, source says {expected}")


def image_destination(record_path: Path, filename: str, repo_root: Path) -> Path:
    if Path(filename).name != filename or not re.fullmatch(
        r"[a-z0-9][a-z0-9._-]*", filename
    ):
        raise ValueError(f"image filename must be a safe lowercase leaf name: {filename!r}")
    return repo_root / "data" / "images" / record_path.parent.name / record_path.stem / filename


def write_image_with_validated_record(
    record: dict,
    record_path: Path,
    filename: str,
    image_bytes: bytes,
    repo_root: Path,
) -> Path:
    """Validate the complete mutation before writing either record artifact."""
    errors = validate_structure(record)
    if errors:
        raise ValidationFailedError(record_path, errors)
    destination = image_destination(record_path, filename, repo_root)
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_bytes(image_bytes)
    write_validated_structure(record, record_path)
    return destination
