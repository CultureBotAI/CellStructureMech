"""curation/source_queue.tsv is the operative ranking of data sources; the checker keeps it honest."""

from __future__ import annotations

import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def test_the_source_queue_is_consistent_with_the_repository():
    result = subprocess.run([sys.executable, "scripts/check_source_queue.py"], cwd=REPO_ROOT,
                            capture_output=True, text=True, check=False)
    assert result.returncode == 0, result.stderr
    assert "source queue OK" in result.stdout


def test_checker_rejects_adopted_without_script(tmp_path, monkeypatch):
    import scripts.check_source_queue as csq

    queue = tmp_path / "q.tsv"
    header = "\t".join(csq.COLUMNS)
    row = "\t".join(["x", "X", "images", "SEED", "CC0_OK", "YES", "DOI", "BULK", "1", "ADOPTED",
                     "2026-08-29", "", "https://x", "why"])
    queue.write_text(header + "\n" + row + "\n")
    conf = tmp_path / "sources.yaml"
    conf.write_text("x:\n  name: X\n")
    monkeypatch.setattr(csq, "QUEUE_PATH", queue)
    monkeypatch.setattr(csq, "CONF_PATH", conf)
    assert csq.main() == 1


def test_checker_rejects_seeding_noncommercial(tmp_path, monkeypatch, capsys):
    import scripts.check_source_queue as csq

    queue = tmp_path / "q.tsv"
    header = "\t".join(csq.COLUMNS)
    row = "\t".join(["x", "X", "images", "SEED", "NONCOMMERCIAL", "YES", "DOI", "BULK", "1", "CANDIDATE",
                     "2026-08-29", "", "https://x", "why"])
    queue.write_text(header + "\n" + row + "\n")
    conf = tmp_path / "sources.yaml"
    conf.write_text("")
    monkeypatch.setattr(csq, "QUEUE_PATH", queue)
    monkeypatch.setattr(csq, "CONF_PATH", conf)
    assert csq.main() == 1
    assert "NONCOMMERCIAL" in capsys.readouterr().err
