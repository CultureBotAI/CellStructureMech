"""docs/SOURCE_QUEUE.md is the operative ranking of data sources; keep it well-formed."""

from __future__ import annotations

import re
from pathlib import Path

QUEUE = Path(__file__).resolve().parents[1] / "docs" / "SOURCE_QUEUE.md"
STATUSES = {"DONE", "ACTIVE", "READY", "CAUTION", "BLOCKED", "SKIP"}


def _rows():
    rows = []
    for line in QUEUE.read_text(encoding="utf-8").splitlines():
        m = re.match(r"^\|\s*(\d+)\s*\|(.*)\|\s*$", line)
        if m:
            cells = [c.strip() for c in m.group(2).split("|")]
            rows.append((int(m.group(1)), cells))
    return rows


def test_queue_has_rows():
    assert len(_rows()) >= 10


def test_ranks_are_contiguous_from_one():
    ranks = [r for r, _ in _rows()]
    assert ranks == list(range(1, len(ranks) + 1)), ranks


def test_statuses_come_from_the_legend():
    bad = [(r, c[2]) for r, c in _rows() if c[2] not in STATUSES]
    assert not bad, f"statuses not in {sorted(STATUSES)}: {bad}"


def test_every_row_has_a_constraint_and_evidence():
    bad = [(r, c[0]) for r, c in _rows() if not c[3] or not c[4]]
    assert not bad, f"rows missing constraint or evidence: {bad}"


def test_at_most_one_active_source():
    """ACTIVE means 'next up'; two of them is a queue without an order."""
    active = [c[0] for _, c in _rows() if c[2] == "ACTIVE"]
    assert len(active) <= 1, active
