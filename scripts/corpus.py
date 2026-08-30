"""Shared corpus loading for the scripts: one place that knows where the
records live and how a record maps to a page slug."""

from __future__ import annotations

import re
from pathlib import Path

import yaml

REPO_ROOT = Path(__file__).resolve().parent.parent
STRUCTURES_DIR = REPO_ROOT / "data" / "structures"
SCHEMA_PATH = REPO_ROOT / "src" / "cellstructuremech" / "schema" / "cellstructuremech.yaml"


def load_records(root: Path = STRUCTURES_DIR) -> list[tuple[Path, dict]]:
    """Every record as (path, parsed doc), sorted by path."""
    out = []
    for path in sorted(root.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            out.append((path, yaml.safe_load(fh)))
    return out


def slugify(label: str) -> str:
    slug = re.sub(r"[^a-z0-9]+", "_", label.lower()).strip("_")
    return slug or "record"


def record_path(category: str, label: str, root: Path = STRUCTURES_DIR) -> Path:
    return root / category.lower() / f"{slugify(label)}.yaml"
