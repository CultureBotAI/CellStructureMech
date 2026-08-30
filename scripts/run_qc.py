#!/usr/bin/env python3
"""Run the authoritative CellStructureMech quality gate locally and in CI."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent

COMMANDS = [
    (
        "lint",
        [sys.executable, "-m", "ruff", "check", "."],
        "Fail fast on syntax, import, and style defects before expensive corpus checks.",
    ),
    (
        "documentation",
        [sys.executable, "scripts/check_docs.py", "--check"],
        "The README's current-corpus block must match the corpus that generated it.",
    ),
    (
        "tests",
        [sys.executable, "-m", "pytest", "-q"],
        "Tests cover corpus-wide invariants that per-record validation cannot see.",
    ),
    (
        "schema validation",
        [sys.executable, "scripts/validate_strict.py", "--quiet"],
        "Closed-mode validation checks every record shape; quiet mode keeps the error summary visible.",
    ),
    (
        "generated site",
        [sys.executable, "scripts/render_pages.py", "--check"],
        "The committed, published site must not drift from the corpus that generated it.",
    ),
    (
        "corpus report",
        [sys.executable, "scripts/corpus_report.py"],
        "Exercise cross-corpus analyses and finish with the live curation summary.",
    ),
]


def main() -> int:
    for name, command, rationale in COMMANDS:
        print(f"\n=== qc: {name} ===", flush=True)
        print(f"why: {rationale}", flush=True)
        completed = subprocess.run(command, cwd=REPO_ROOT, check=False)
        if completed.returncode:
            print(f"qc stopped: {name} failed with exit code {completed.returncode}", file=sys.stderr)
            return completed.returncode
    print("\nAll CellStructureMech quality gates passed.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
