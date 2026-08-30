"""Smoke tests for the CLI scripts against a temp corpus."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run(*args, cwd=REPO_ROOT):
    return subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, text=True, check=False)


def test_new_record_dry_run_writes_nothing(tmp_path, monkeypatch):
    out = _run("scripts/new_record.py", "--identifier", "cellstructuremech:TEST", "--label", "test thing",
               "--category", "OTHER")
    assert out.returncode == 0, out.stderr
    assert "dry run" in out.stdout
    assert not (REPO_ROOT / "data" / "structures" / "other" / "test_thing.yaml").exists()


def test_new_record_refuses_taken_identifier(records):
    ident = records[0][1]["identifier"]
    out = _run("scripts/new_record.py", "--identifier", ident, "--label", "dup",
               "--category", "OTHER", "--apply")
    assert out.returncode == 2
    assert "already used" in out.stderr


def test_validate_strict_passes_on_corpus(tmp_path):
    out = _run("scripts/validate_strict.py", "--quiet", "--out", str(tmp_path / "f.tsv"))
    assert out.returncode == 0, out.stderr


def test_render_check_is_current():
    out = _run("scripts/render_pages.py", "--check")
    assert out.returncode == 0, out.stderr


def test_corpus_report_runs():
    out = _run("scripts/corpus_report.py")
    assert out.returncode == 0, out.stderr
    assert "structure records" in out.stdout


def test_rendered_site_has_no_broken_local_links(tmp_path):
    """Every relative href/src in the rendered site must resolve to a file in
    the output tree. Caught #21, where record pages pointed one level too
    deep for their stylesheet and hosted images."""
    import re

    out = tmp_path / "site"
    res = _run("scripts/render_pages.py", "--out", str(out))
    assert res.returncode == 0, res.stderr
    broken = []
    for html in out.rglob("*.html"):
        for m in re.finditer(r'(?:href|src)="([^"#]+)"', html.read_text(encoding="utf-8")):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            if not (html.parent / url).resolve().exists():
                broken.append(f"{html.relative_to(out)}: {url}")
    assert not broken, broken
