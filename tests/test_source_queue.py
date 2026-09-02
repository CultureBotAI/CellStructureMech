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


def test_unverified_terms_block_seeding_but_not_reading(tmp_path, monkeypatch):
    """SEED copies content and needs verified terms; CURATE_ONLY copies nothing,
    so a source whose licence page does not exist can still inform curation —
    and UNVERIFIED is more honest there than a guessed RESTRICTED (#126)."""
    import scripts.check_source_queue as csq

    def queue(use: str):
        path = tmp_path / f"{use}.tsv"
        header = "\t".join(csq.COLUMNS)
        row = "\t".join(["x", "X", "components", use, "UNVERIFIED", "YES", "CURIE", "API", "1",
                         "ADOPTED", "2026-09-02", "scripts/check_source_queue.py", "https://x", "why"])
        path.write_text(header + "\n" + row + "\n")
        return path

    conf = tmp_path / "sources.yaml"
    conf.write_text("x:\n  name: X\n")
    monkeypatch.setattr(csq, "CONF_PATH", conf)
    monkeypatch.setattr(csq, "QUEUE_PATH", queue("SEED"))
    assert csq.main() == 1
    monkeypatch.setattr(csq, "QUEUE_PATH", queue("CURATE_ONLY"))
    assert csq.main() == 0


def test_a_curate_only_source_may_not_be_an_identity(tmp_path, monkeypatch):
    """CURATE_ONLY stores third-party identifiers. A record grounding to the
    source's own prefix would be that source's content under another name."""
    import scripts.check_source_queue as csq

    root = tmp_path / "repo"
    (root / "data" / "structures" / "other").mkdir(parents=True)
    (root / "data" / "structures" / "other" / "r.yaml").write_text(
        "identifier: GO:1\nlabel: x\nxrefs:\n- subtiwiki:BSU16290\n")
    monkeypatch.setattr(csq, "REPO_ROOT", root)
    rows = [{"source_id": "subtiwiki", "use": "CURATE_ONLY"}]
    problems = csq._curate_only_identities(rows)
    assert problems and "CURATE_ONLY source as identity" in problems[0]


def test_a_curate_only_source_that_stores_no_identity_passes(tmp_path, monkeypatch):
    import scripts.check_source_queue as csq

    root = tmp_path / "repo"
    (root / "data" / "structures" / "other").mkdir(parents=True)
    (root / "data" / "structures" / "other" / "r.yaml").write_text(
        "identifier: GO:1\nlabel: x\ncomponents:\n- component_id: c\n  grounding: InterPro:IPR1\n")
    monkeypatch.setattr(csq, "REPO_ROOT", root)
    assert csq._curate_only_identities([{"source_id": "subtiwiki", "use": "CURATE_ONLY"}]) == []
