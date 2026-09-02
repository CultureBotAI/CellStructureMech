"""Smoke tests for the CLI scripts against a temp corpus."""

from __future__ import annotations

import json
import subprocess
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[1]


def _run(*args, cwd=REPO_ROOT):
    return subprocess.run([sys.executable, *args], cwd=cwd, capture_output=True, text=True, check=False)


def test_new_record_dry_run_writes_nothing(tmp_path, monkeypatch):
    out = _run("scripts/new_record.py", "--identifier", "cellstructuremech:TEST", "--label", "test thing",
               "--category", "OTHER", "--kind", "OTHER", "--definition", "A test structure.",
               "--definition-source", "DOI:10.0000/example")
    assert out.returncode == 0, out.stderr
    assert "dry run" in out.stdout
    assert not (REPO_ROOT / "data" / "structures" / "other" / "test_thing.yaml").exists()


def test_new_record_refuses_taken_identifier(records):
    ident = records[0][1]["identifier"]
    out = _run("scripts/new_record.py", "--identifier", ident, "--label", "dup",
               "--category", "OTHER", "--kind", "OTHER", "--definition", "A duplicate.",
               "--definition-source", "DOI:10.0000/example", "--apply")
    assert out.returncode == 2
    assert "already used" in out.stderr


def test_validate_strict_passes_on_corpus(tmp_path):
    out = _run("scripts/validate_strict.py", "--quiet", "--out", str(tmp_path / "f.tsv"))
    assert out.returncode == 0, out.stderr


def test_render_check_is_current():
    out = _run("scripts/render_pages.py", "--check")
    assert out.returncode == 0, out.stderr


def test_rendered_cryoet_datasets_are_public_and_resolvable(tmp_path):
    out = tmp_path / "site"
    result = _run("scripts/render_pages.py", "--out", str(out))
    assert result.returncode == 0, result.stderr
    gas = (out / "structures" / "inclusion" / "gas_vesicle.html").read_text()
    pilus = (out / "structures" / "appendage" / "type_iv_pilus.html").read_text()
    assert "<h2>Datasets</h2>" in gas
    assert "https://cryoetdataportal.czscience.com/datasets/10014" in gas
    assert "CryoETDataPortal:10014" in gas
    assert "across 217 runs" in gas
    assert "https://cryoetdataportal.czscience.com/datasets/10155" in pilus
    assert "annotation 30707" in pilus
    assert "ground_truth_status=true" in pilus
    assert "is_curator_recommended=true" in pilus


def test_text_embedding_map_check_is_current():
    out = _run("scripts/build_text_embedding_map.py", "--check")
    assert out.returncode == 0, out.stderr


def test_readme_public_map_link_matches_root_based_pages_layout():
    readme = (REPO_ROOT / "README.md").read_text(encoding="utf-8")
    assert "https://culturebotai.github.io/CellStructureMech/pages/embedding-map.html" in readme
    assert "https://culturebotai.github.io/CellStructureMech/embedding-map.html" not in readme


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
        # The site is published from the repository root, so a page at
        # pages/a/b.html can legitimately reference ../../data/images/... —
        # hosted images are served where they are committed rather than copied
        # into the page tree (#31). Resolve every link from where the page will
        # actually live, not from the temporary output directory.
        published_dir = REPO_ROOT / "pages" / html.parent.relative_to(out)
        for m in re.finditer(r'(?:href|src)="([^"#]+)"', html.read_text(encoding="utf-8")):
            url = m.group(1)
            if url.startswith(("http://", "https://", "mailto:")):
                continue
            target = (published_dir / url).resolve()
            # A generated page may not exist yet in the committed tree, so fall
            # back to the freshly rendered copy for anything inside pages/.
            if target.exists():
                continue
            if not (html.parent / url).resolve().exists():
                broken.append(f"{html.relative_to(out)}: {url}")
    assert not broken, broken


def test_a_hosted_image_link_points_at_the_committed_file(tmp_path):
    """The published page must reach the image where it is committed; if the
    renderer ever copies images again, this keeps the reference honest (#31)."""
    import yaml

    out = tmp_path / "site"
    assert _run("scripts/render_pages.py", "--out", str(out)).returncode == 0
    checked = 0
    for record in sorted((REPO_ROOT / "data" / "structures").rglob("*.yaml")):
        doc = yaml.safe_load(record.read_text(encoding="utf-8"))
        for image in doc.get("images") or []:
            if not image.get("file"):
                continue
            page = out / "structures" / record.parent.name / f"{record.stem}.html"
            html = page.read_text(encoding="utf-8")
            assert f'/data/images/{record.parent.name}/{record.stem}/{image["file"]}"' in html, page
            checked += 1
    assert checked, "no hosted image found to check"
    map_data = json.loads((out / "data" / "structure_text_map.json").read_text())
    assert (out / "embedding-map.html").exists()
    assert all((out / item["page"]).exists() for item in map_data["records"])


def test_the_site_root_opts_out_of_jekyll():
    """Pages publishes this repository from `/`, and record pages reference
    images under `data/` — outside the directory that carries pages/.nojekyll.
    Jekyll silently drops paths it considers special, and the failure mode is a
    404 for a file that is present in the repository, which no local check
    reproduces (#105)."""
    assert (REPO_ROOT / ".nojekyll").exists(), (
        "add an empty .nojekyll at the repository root: the published site now "
        "depends on data/images/, which is outside pages/"
    )
