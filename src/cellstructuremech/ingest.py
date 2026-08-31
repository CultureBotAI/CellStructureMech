"""Small, source-neutral helpers for curator-controlled ingestion scripts."""

from __future__ import annotations

import hashlib
import json
import urllib.parse
import urllib.request
from pathlib import Path

USER_AGENT = {
    "User-Agent": (
        "CellStructureMech/0.1 "
        "(https://github.com/CultureBotAI/CellStructureMech; curation bot)"
    )
}


def get_bytes(url: str) -> bytes:
    """Read one public source URL with the repository's identifying User-Agent."""
    request = urllib.request.Request(url, headers=USER_AGENT)
    with urllib.request.urlopen(request, timeout=120) as response:
        return response.read()


def get_json(url: str) -> dict:
    return json.loads(get_bytes(url))


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
    return repo_root / "data" / "images" / record_path.parent.name / record_path.stem / filename
