"""Shared fixtures: the corpus, loaded once per session. Tests treat it as read-only."""

from __future__ import annotations

from pathlib import Path

import pytest
import yaml

REPO_ROOT = Path(__file__).resolve().parents[1]
STRUCTURES_DIR = REPO_ROOT / "data" / "structures"
SCHEMA_PATH = REPO_ROOT / "src" / "cellstructuremech" / "schema" / "cellstructuremech.yaml"


@pytest.fixture(scope="session")
def repo_root() -> Path:
    return REPO_ROOT


@pytest.fixture(scope="session")
def schema_path() -> Path:
    return SCHEMA_PATH


@pytest.fixture(scope="session")
def records() -> list[tuple[Path, dict]]:
    """Every CellStructureRecord as (path, parsed doc)."""
    if not STRUCTURES_DIR.exists():
        pytest.skip(f"no corpus at {STRUCTURES_DIR}")
    out = []
    for path in sorted(STRUCTURES_DIR.rglob("*.yaml")):
        with path.open(encoding="utf-8") as fh:
            out.append((path, yaml.safe_load(fh)))
    if not out:
        pytest.skip(f"corpus at {STRUCTURES_DIR} is empty")
    return out
