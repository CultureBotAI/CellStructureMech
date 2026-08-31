"""Offline tests for scripts/check_curies.py — no network."""

from __future__ import annotations

import json
from datetime import date, timedelta

import pytest

from scripts import check_curies as cc


def test_collect_finds_identifiers_in_every_nested_position():
    doc = {
        "identifier": "GO:1", "definition_source": "DOI:10.1/x",
        "components": [{"grounding": "InterPro:IPR1",
                        "protein_examples": [{"uniprot_id": "UniProtKB:P1", "taxon_id": "NCBITaxon:2"}]}],
        "causal_graphs": [{"edges": [{"predicate_id": "RO:1",
                                      "evidence": [{"reference": "PMID:9"}]}]}],
        "images": [{"source_url": "https://example.org/x", "licence": "CC0"}],
    }
    found = cc.collect([(None, doc)])
    assert found["GO"] == {"GO:1"} and found["DOI"] == {"DOI:10.1/x"}
    assert found["InterPro"] == {"InterPro:IPR1"} and found["UniProtKB"] == {"UniProtKB:P1"}
    assert found["NCBITaxon"] == {"NCBITaxon:2"} and found["RO"] == {"RO:1"} and found["PMID"] == {"PMID:9"}
    assert "https" not in found, "a URL is not a CURIE"


def test_a_transport_failure_is_never_cached():
    """UNREACHABLE is 'we could not ask', not 'the identifier is fine'. Caching
    it would turn one flaky request into a permanent pass."""
    entry = {"verdict": "UNREACHABLE", "checked_on": date.today().isoformat()}
    assert not cc.fresh(entry, 30)


def test_a_stale_entry_is_rechecked():
    old = (date.today() - timedelta(days=40)).isoformat()
    assert not cc.fresh({"verdict": "OK", "checked_on": old}, 30)
    assert cc.fresh({"verdict": "OK", "checked_on": date.today().isoformat()}, 30)


def test_every_resolver_has_a_control():
    """A resolver with no known-good/known-bad pair is a resolver nothing checks."""
    covered = set(cc.CONTROLS)
    assert set(cc.RESOLVERS) <= covered, f"no control for: {sorted(set(cc.RESOLVERS) - covered)}"
    assert "GO" in covered, "the OLS fallback resolver needs a control too"


def test_interpro_treats_204_as_absent(monkeypatch):
    """InterPro answers an unknown accession with 204 No Content, not 404 (#82)."""
    monkeypatch.setattr(cc, "_get", lambda url, timeout=30.0: (204, b""))
    assert cc.resolve_interpro(["InterPro:IPR999999"])["InterPro:IPR999999"][0] == "NOT_FOUND"


def test_complex_portal_requires_an_exact_accession_match(monkeypatch):
    """The search endpoint returns near matches; only complexAC equality counts."""
    payload = json.dumps({"elements": [{"complexAC": "CPX-2244", "complexName": "other"}]}).encode()
    monkeypatch.setattr(cc, "_get", lambda url, timeout=30.0: (200, payload))
    got = cc.resolve_complexportal(["ComplexPortal:CPX-3802"])
    assert got["ComplexPortal:CPX-3802"][0] == "NOT_FOUND"


def test_a_doi_missing_from_crossref_falls_back_to_datacite(monkeypatch):
    """Data repositories register with DataCite; a Crossref-only check would
    call a valid CaltechDATA or Zenodo DOI missing (#82)."""
    def fake(url, timeout=30.0):
        if "crossref" in url:
            return 404, b""
        return 200, json.dumps({"data": {"attributes": {"titles": [{"title": "A dataset"}]}}}).encode()
    monkeypatch.setattr(cc, "_get", fake)
    monkeypatch.setattr(cc.time, "sleep", lambda _s: None)
    got = cc.resolve_doi(["DOI:10.22002/D1.1355"])
    assert got["DOI:10.22002/D1.1355"] == ("OK", "A dataset")


def test_a_doi_absent_from_both_registries_is_not_found(monkeypatch):
    monkeypatch.setattr(cc, "_get", lambda url, timeout=30.0: (404, b""))
    monkeypatch.setattr(cc.time, "sleep", lambda _s: None)
    assert cc.resolve_doi(["DOI:10.9999/x"])["DOI:10.9999/x"][0] == "NOT_FOUND"


@pytest.mark.parametrize("prefix", sorted(cc.NO_RESOLVER))
def test_a_prefix_with_no_resolver_is_skipped_not_passed(prefix):
    """An identifier nothing can check must never be reported as OK."""
    assert cc.NO_RESOLVER[prefix], f"{prefix} is skipped without saying why"
