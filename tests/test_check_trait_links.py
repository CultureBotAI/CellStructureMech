"""Offline tests for scripts/check_trait_links.py — no network, no sibling checkout."""

from __future__ import annotations

import json

import pytest

from scripts import check_trait_links as ctl


def _corpus(links):
    class P:
        name = "rec.yaml"
    return [(P(), {"associated_traits": links})]


def test_trait_links_are_collected_with_their_record():
    got = ctl.trait_links(_corpus([{"trait_id": "METPO:1", "trait_label": "motile"}]))
    assert got == [("rec.yaml", "METPO:1", "motile")]


def test_a_record_without_trait_links_contributes_nothing():
    assert ctl.trait_links([(type("P", (), {"name": "r.yaml"})(), {})]) == []


def test_an_empty_index_refuses_rather_than_passing(monkeypatch, capsys):
    """An index that failed to load must not read as a clean corpus (#87)."""
    monkeypatch.setattr(ctl, "load_index", lambda offline=False: ({}, "nowhere"))
    monkeypatch.setattr(ctl.sys, "argv", ["check_trait_links.py", "--check"])
    assert ctl.main() == 2
    assert "index is empty" in capsys.readouterr().err


def test_an_index_failing_its_control_refuses(monkeypatch, capsys):
    """A well-formed index that lacks a trait everyone has, or contains a
    fabricated one, is not the index it claims to be (#82)."""
    monkeypatch.setattr(ctl, "load_index", lambda offline=False: ({"traitmech:1": "x"}, "somewhere"))
    monkeypatch.setattr(ctl.sys, "argv", ["check_trait_links.py", "--check"])
    assert ctl.main() == 2
    assert "control failed" in capsys.readouterr().err


def _index():
    return {ctl.CONTROL_GOOD: "motile", "traitmech:000071": "magnetosome"}


@pytest.mark.parametrize(("links", "expected"), [
    ([{"trait_id": "traitmech:000071", "trait_label": "magnetosome"}], 0),
    ([{"trait_id": "traitmech:000071", "trait_label": "Magnetosome"}], 0),   # case-insensitive
    ([{"trait_id": "traitmech:999999", "trait_label": "ghost"}], 1),          # not a TraitMech record
    ([{"trait_id": "traitmech:000071", "trait_label": "gas vesicle"}], 1),    # label drifted
])
def test_check_verdicts(monkeypatch, links, expected):
    monkeypatch.setattr(ctl, "load_index", lambda offline=False: (_index(), "fixture"))
    monkeypatch.setattr(ctl, "load_records", lambda *a, **k: _corpus(links))
    monkeypatch.setattr(ctl.sys, "argv", ["check_trait_links.py", "--check"])
    assert ctl.main() == expected


def test_published_index_is_parsed_into_id_to_label(monkeypatch, tmp_path):
    payload = json.dumps([{"id": "METPO:1", "label": "motile"}, {"label": "no id"}]).encode()

    class R:
        def read(self):
            return payload
        def __enter__(self):
            return self
        def __exit__(self, *a):
            return False

    monkeypatch.setattr(ctl.urllib.request, "urlopen", lambda *a, **k: R())
    monkeypatch.setattr(ctl, "CACHE_PATH", tmp_path / "idx.json")
    assert ctl.index_from_published() == {"METPO:1": "motile"}
