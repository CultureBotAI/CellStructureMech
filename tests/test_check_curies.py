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


def test_every_ols_ontology_has_its_own_control():
    """OLS indexes each ontology separately, so a control on GO says nothing
    about NCBI Taxonomy — 66 taxon references resolve through that path (#84)."""
    missing = sorted(set(cc.OLS_ONTOLOGY) - set(cc.CONTROLS) - {"MICRO", "NCIT"})
    assert not missing, f"OLS ontologies used by the corpus with no control: {missing}"


def test_interpro_treats_204_as_absent(monkeypatch):
    """InterPro answers an unknown accession with 204 No Content, not 404 (#82)."""
    monkeypatch.setattr(cc, "_get", lambda url, timeout=30.0: (204, b""))
    assert cc.resolve_interpro(["InterPro:IPR999999"])["InterPro:IPR999999"][0] == "NOT_FOUND"


def test_interpro_treats_404_as_unreachable(monkeypatch):
    """InterPro can emit a false 404 for an accession that normally resolves."""
    monkeypatch.setattr(cc, "_get", lambda url, timeout=30.0: (404, b""))

    assert cc.resolve_interpro(["InterPro:IPR001119"])["InterPro:IPR001119"][0] == "UNREACHABLE"


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


def test_get_uses_the_configured_default_timeout(monkeypatch):
    captured = {}

    class FakeResponse:
        status = 200

        def __enter__(self):
            return self

        def __exit__(self, *_):
            return None

        def read(self):
            return b"{}"

    def fake_urlopen(_request, timeout):
        captured["timeout"] = timeout
        return FakeResponse()

    monkeypatch.setattr(cc, "HTTP_TIMEOUT_SECONDS", 5.0)
    monkeypatch.setattr(cc.urllib.request, "urlopen", fake_urlopen)

    assert cc._get("https://example.org") == (200, b"{}")
    assert captured["timeout"] == 5.0


def test_control_verdicts_use_the_short_self_test_timeout(monkeypatch):
    seen = []

    def resolver(ids):
        seen.append(cc.HTTP_TIMEOUT_SECONDS)
        good, bad = ids
        return {good: ("OK", ""), bad: ("NOT_FOUND", "")}

    monkeypatch.setattr(cc, "HTTP_TIMEOUT_SECONDS", 30.0)
    monkeypatch.setattr(cc, "SELF_TEST_HTTP_TIMEOUT_SECONDS", 5.0)

    assert cc._control_verdicts(resolver, "GO:1", "GO:2") == {
        "GO:1": ("OK", ""),
        "GO:2": ("NOT_FOUND", ""),
    }
    assert seen == [5.0]
    assert cc.HTTP_TIMEOUT_SECONDS == 30.0


def test_obo_purl_treats_404_as_absent(monkeypatch):
    """BFO relations are OLS *properties*, not terms, so the term index 404s for
    all of them and the PURL is the authority. RO is deliberately NOT routed
    here: its PURL namespace answers 200 for a fabricated id (#84)."""
    import urllib.error

    def fake(request, timeout=30):
        raise urllib.error.HTTPError(request.full_url, 404, "Not Found", {}, None)

    monkeypatch.setattr(cc.urllib.request, "urlopen", fake)
    assert cc.resolve_obo_purl(["BFO:9999999"])["BFO:9999999"][0] == "NOT_FOUND"


def test_ro_is_not_routed_through_the_purl():
    """RO_9999999 redirects to a generic OLS page and answers 200, so the PURL
    cannot tell a real RO relation from a fabricated one (#84)."""
    assert cc.RESOLVERS.get("RO") is not cc.resolve_obo_purl
    assert cc.RESOLVERS.get("BFO") is cc.resolve_obo_purl


@pytest.mark.parametrize("prefix", sorted(cc.NO_RESOLVER))
def test_a_prefix_with_no_resolver_is_skipped_not_passed(prefix):
    """An identifier nothing can check must never be reported as OK."""
    assert cc.NO_RESOLVER[prefix], f"{prefix} is skipped without saying why"


def test_the_gate_refuses_to_pass_on_an_empty_corpus(monkeypatch, capsys):
    """A check that finds nothing must not report success — otherwise a moved
    directory or a broken loader reads as coverage (#87)."""
    monkeypatch.setattr(cc, "load_records", lambda *a, **k: [])
    monkeypatch.setattr(cc.sys, "argv", ["check_curies.py", "--check", "--offline"])
    assert cc.main() == 2
    assert "no records found" in capsys.readouterr().err


def test_the_gate_refuses_when_records_carry_no_identifiers(monkeypatch, capsys):
    monkeypatch.setattr(cc, "load_records", lambda *a, **k: [(None, {"label": "x"})])
    monkeypatch.setattr(cc.sys, "argv", ["check_curies.py", "--check", "--offline"])
    assert cc.main() == 2
    assert "no identifiers found" in capsys.readouterr().err


def test_prose_dois_are_collected_and_normalised(tmp_path, monkeypatch):
    """research/ and curation/ cite papers in prose; a dead DOI there is the same
    defect as a dead DOI in a record (#85)."""
    (tmp_path / "research").mkdir()
    (tmp_path / "research" / "n.md").write_text(
        "See [the review](https://doi.org/10.1038/nrmicro.2018.10), and 10.1128/MMBR.00061-12.\n")
    monkeypatch.setattr(cc, "REPO_ROOT", tmp_path)
    got = cc.collect_prose(("research/*.md",))
    assert got["DOI"] == {"DOI:10.1038/nrmicro.2018.10", "DOI:10.1128/MMBR.00061-12"}


@pytest.mark.parametrize("template", [
    "10.6019/EMPIAR-XXXXX", "10.22002/D1.NNNN", "10.7295/W9CILNNNNN", "10.1234/{id}", "10.1234/<id>",
])
def test_a_documented_identifier_shape_is_not_treated_as_a_citation(tmp_path, monkeypatch, template):
    """Notes describe the form of an identifier as often as they cite one."""
    (tmp_path / "research").mkdir()
    (tmp_path / "research" / "n.md").write_text(f"Entries carry a DOI of the form `{template}`.\n")
    monkeypatch.setattr(cc, "REPO_ROOT", tmp_path)
    assert cc.collect_prose(("research/*.md",))["DOI"] == set()


# --- an unreachable authority is not a broken resolver (#173) ---

def test_an_unreachable_control_is_reported_separately_not_as_a_failure(monkeypatch):
    """CI failed a blocking gate with 'the resolver would pass anything' when the
    OBO PURL host was briefly unreachable. Nothing was asked, so nothing was
    learned -- and a gate that fails on an upstream blip teaches people to re-run
    gates instead of reading them."""
    monkeypatch.setattr(cc, "SELF_TEST_RETRIES", 1)
    monkeypatch.setattr(cc, "RESOLVERS",
                        dict.fromkeys(cc.CONTROLS, lambda ids: {i: ("UNREACHABLE", "") for i in ids}))
    monkeypatch.setattr(cc, "resolve_doi", lambda ids: {i: ("UNREACHABLE", "") for i in ids})
    failures, unreachable = cc.self_test()
    assert failures == []
    assert len(unreachable) == len(cc.CONTROLS) + 1
    assert "not exercised" not in " ".join(failures)


def test_a_resolver_that_accepts_a_fabricated_id_still_fails(monkeypatch):
    """The loosening must not have reached the thing the control exists for."""
    monkeypatch.setattr(cc, "SELF_TEST_RETRIES", 1)
    monkeypatch.setattr(cc, "RESOLVERS",
                        dict.fromkeys(cc.CONTROLS, lambda ids: {i: ("OK", "") for i in ids}))
    monkeypatch.setattr(cc, "resolve_doi", lambda ids: {i: ("OK", "") for i in ids})
    failures, unreachable = cc.self_test()
    assert unreachable == []
    assert failures and all("would pass anything" in f for f in failures)


def test_a_broken_known_good_still_fails(monkeypatch):
    monkeypatch.setattr(cc, "SELF_TEST_RETRIES", 1)
    monkeypatch.setattr(cc, "RESOLVERS",
                        dict.fromkeys(cc.CONTROLS, lambda ids: {i: ("NOT_FOUND", "") for i in ids}))
    monkeypatch.setattr(cc, "resolve_doi", lambda ids: {i: ("OK", "") for i in ids})
    failures, _ = cc.self_test()
    assert failures and any("resolver is broken" in f for f in failures)


def test_an_unreachable_control_is_retried_before_being_given_up_on(monkeypatch):
    calls = {"n": 0}

    def flaky(ids):
        calls["n"] += 1
        if calls["n"] < 3:
            return {i: ("UNREACHABLE", "") for i in ids}
        good, bad = sorted(ids)[0], sorted(ids)[1]
        return {good: ("OK", ""), bad: ("NOT_FOUND", "")}

    monkeypatch.setattr(cc, "SELF_TEST_RETRIES", 3)
    monkeypatch.setattr(cc.time, "sleep", lambda *_: None)
    prefix, (g, b) = sorted(cc.CONTROLS.items())[0]
    verdicts = cc._control_verdicts(flaky, g, b)
    assert "UNREACHABLE" not in {v[0] for v in verdicts.values()}


def _property_payload(**changes):
    hit = {"iri": "http://purl.obolibrary.org/obo/BFO_0000050", "ontology_name": "ro",
           "label": "part of", "is_obsolete": False, "obo_id": "RO:"}
    hit.update(changes)
    return {"_embedded": {"properties": [hit]}, "page": {"totalElements": 1}}


def _broken_property_browser(monkeypatch, final_url=None):
    iri = "http://purl.obolibrary.org/obo/BFO_0000050"
    final_url = final_url or "https://www.ebi.ac.uk/ols4/ontologies/ro/properties?iri=" + iri

    def fake(request, timeout):
        assert request.full_url == iri
        assert request.get_method() == "HEAD"
        assert timeout == cc.HTTP_TIMEOUT_SECONDS
        raise cc.urllib.error.HTTPError(final_url, 404, "Not Found", {}, None)

    monkeypatch.setattr(cc.urllib.request, "urlopen", fake)


@pytest.mark.parametrize("browser", ["ols", "ols4"])
def test_bfo_redirected_browser_404_uses_exact_property_api(monkeypatch, browser):
    """The observed browser 404 is not absence; GET to that browser also 404s."""
    iri = "http://purl.obolibrary.org/obo/BFO_0000050"
    _broken_property_browser(monkeypatch, f"https://www.ebi.ac.uk/{browser}/ontologies/ro/properties?iri={iri}")
    calls = []

    def get(url):
        calls.append(url)
        assert url == "https://www.ebi.ac.uk/ols4/api/ontologies/ro/properties?" + cc.urllib.parse.urlencode(
            {"iri": iri})
        return 200, json.dumps(_property_payload()).encode()

    monkeypatch.setattr(cc, "_get", get)
    assert cc.RESOLVERS["BFO"](["BFO:0000050"]) == {"BFO:0000050": ("OK", "part of")}
    assert len(calls) == 1


@pytest.mark.parametrize("final_url", [
    "https://unavailable.example/BFO_0000050",
    "https://www.ebi.ac.uk/ols4/ontologies/ro/properties?iri=http://purl.obolibrary.org/obo/BFO_9999999",
    "https://www.ebi.ac.uk/ols4/ontologies/bfo/terms?iri=http://purl.obolibrary.org/obo/BFO_0000050",
])
def test_bfo_other_redirected_404_is_unavailable_not_absent(monkeypatch, final_url):
    _broken_property_browser(monkeypatch, final_url)
    monkeypatch.setattr(cc, "_get", lambda *_: pytest.fail("unexpected property API call"))
    assert cc.resolve_obo_purl(["BFO:0000050"])["BFO:0000050"][0] == "UNREACHABLE"


@pytest.mark.parametrize("status", [0, 404, 429, 500])
def test_bfo_property_api_failure_is_unavailable_not_absent(monkeypatch, status):
    _broken_property_browser(monkeypatch)
    monkeypatch.setattr(cc, "_get", lambda *_: (status, b""))
    assert cc.resolve_obo_purl(["BFO:0000050"])["BFO:0000050"][0] == "UNREACHABLE"


@pytest.mark.parametrize("payload", [
    {}, [], {"page": {"totalElements": False}},
    {"page": {"totalElements": 1}},
    {"page": {"totalElements": 0}, "_embedded": {"properties": [{}]}},
    _property_payload(iri="http://purl.obolibrary.org/obo/BFO_9999999"),
    _property_payload(ontology_name="other"), _property_payload(is_obsolete="false"),
    _property_payload(label=""),
    {"_embedded": {"properties": _property_payload()["_embedded"]["properties"] * 2},
     "page": {"totalElements": 2}},
])
def test_bfo_property_api_requires_unambiguous_exact_identity(monkeypatch, payload):
    _broken_property_browser(monkeypatch)
    monkeypatch.setattr(cc, "_get", lambda *_: (200, json.dumps(payload).encode()))
    assert cc.resolve_obo_purl(["BFO:0000050"])["BFO:0000050"][0] == "UNREACHABLE"


def test_bfo_property_api_invalid_json_is_unavailable(monkeypatch):
    _broken_property_browser(monkeypatch)
    monkeypatch.setattr(cc, "_get", lambda *_: (200, b"not JSON"))
    assert cc.resolve_obo_purl(["BFO:0000050"])["BFO:0000050"][0] == "UNREACHABLE"


def test_bfo_property_api_empty_authoritative_result_is_absent(monkeypatch):
    _broken_property_browser(monkeypatch)
    monkeypatch.setattr(cc, "_get", lambda *_: (200, b'{"page":{"totalElements":0}}'))
    assert cc.resolve_obo_purl(["BFO:0000050"])["BFO:0000050"][0] == "NOT_FOUND"


def test_bfo_property_api_preserves_obsolete_verdict(monkeypatch):
    _broken_property_browser(monkeypatch)
    payload = json.dumps(_property_payload(is_obsolete=True)).encode()
    monkeypatch.setattr(cc, "_get", lambda *_: (200, payload))
    assert cc.resolve_obo_purl(["BFO:0000050"])["BFO:0000050"] == ("OBSOLETE", "part of")


@pytest.mark.parametrize("offline", [False, True])
def test_legacy_bfo_cache_needs_refresh_without_discarding_other_prefixes(tmp_path, monkeypatch, offline):
    """A successful control cannot make an old false corpus verdict trustworthy."""
    old_bfo = {"verdict": "NOT_FOUND", "detail": "no such OBO term", "checked_on": date.today().isoformat()}
    other = {"verdict": "OK", "detail": "ribosome", "checked_on": date.today().isoformat()}
    cache_path = tmp_path / "cache.json"
    cache_path.write_text(json.dumps({"BFO:0000050": old_bfo, "GO:0005840": other}))
    original_bytes = cache_path.read_bytes()
    monkeypatch.setattr(cc, "CACHE_PATH", cache_path)
    monkeypatch.setattr(cc, "load_records", lambda: [(None, {"part_of": "BFO:0000050",
                                                            "parent": "GO:0005840"})])
    monkeypatch.setattr(cc, "self_test", lambda: ([], []))
    calls = []

    def resolver(curies):
        calls.append(curies)
        return {"BFO:0000050": ("OK", "part of")}

    monkeypatch.setitem(cc.RESOLVERS, "BFO", resolver)
    monkeypatch.setattr(cc, "resolve_ols", lambda *_: pytest.fail("unrelated cached GO must not be fetched"))
    report = tmp_path / "report.tsv"
    argv = ["check_curies.py", "--check", "--records-only", "--report", str(report)]
    monkeypatch.setattr(cc.sys, "argv", argv + (["--offline"] if offline else []))
    assert cc.main() == 0
    cache = json.loads(cache_path.read_text())
    assert cache["GO:0005840"] == other
    if offline:
        assert calls == []
        assert cache_path.read_bytes() == original_bytes
        assert "BFO:0000050\tBFO\tSKIPPED\t" in report.read_text()
        assert "GO:0005840\tGO\tOK\t" in report.read_text()
    else:
        assert calls == [["BFO:0000050"]]
        assert cache["BFO:0000050"]["verdict"] == "OK"
        assert cache["BFO:0000050"]["resolver_version"] == cc.RESOLVER_CACHE_VERSIONS["BFO"]
        calls.clear()
        assert cc.main() == 0
        assert calls == [], "new compatible BFO cache must remain useful"


@pytest.mark.parametrize("version", [None, "older-version", "future-version"])
def test_bfo_cache_version_must_match_current_resolver(version):
    entry = {"verdict": "OK", "checked_on": date.today().isoformat()}
    if version is not None:
        entry["resolver_version"] = version
    assert not cc.fresh(entry, 30, cc.RESOLVER_CACHE_VERSIONS["BFO"])
    entry["resolver_version"] = cc.RESOLVER_CACHE_VERSIONS["BFO"]
    assert cc.fresh(entry, 30, cc.RESOLVER_CACHE_VERSIONS["BFO"])
