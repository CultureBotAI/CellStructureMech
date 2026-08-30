"""Offline tests for scripts/uniprot_sl.py: parsing and matching, no network."""

from __future__ import annotations

from scripts import uniprot_sl

SUBCELL = """\
ID   Carboxysome.
AC   SL-0034
DE   A bacterial microcompartment that
DE   encapsulates RuBisCO.
HI   Bacterial microcompartment.
GO   GO:0031470; carboxysome
//
ID   Nowhere.
AC   SL-9999
//
"""


def test_subcell_parser_maps_go_to_sl(tmp_path, monkeypatch):
    cache = tmp_path / "subcell.txt"
    cache.write_text(SUBCELL)
    monkeypatch.setattr(uniprot_sl, "CACHE", cache)
    m = uniprot_sl.load_subcell()
    assert m["GO:0031470"]["sl"] == "SL-0034"
    assert m["GO:0031470"]["name"] == "Carboxysome"
    assert m["GO:0031470"]["definition"] == "A bacterial microcompartment that encapsulates RuBisCO."
    assert "SL-9999" not in {v["sl"] for v in m.values()}


DOC = {
    "label": "carboxysome",
    "components": [
        {"component_id": "bmc_h", "label": "shell hexamers", "gene_symbols": ["ccmK", "csoS1"]},
        {"component_id": "rubisco", "label": "RuBisCO", "gene_symbols": ["rbcL", "cbbL"]},
        {"component_id": "ca", "label": "carbonic anhydrase", "gene_symbols": ["ccaA"]},
    ],
}


def test_match_component_exact_and_prefix():
    assert uniprot_sl.match_component(DOC, "ccaA")[0]["component_id"] == "ca"
    assert uniprot_sl.match_component(DOC, "ccmK2")[0]["component_id"] == "bmc_h"


def test_match_component_rejects_unknown_and_missing():
    assert uniprot_sl.match_component(DOC, "ccmN") == (None, "no matching component")
    assert uniprot_sl.match_component(DOC, None) == (None, "no gene symbol")


def test_match_component_reports_ambiguity():
    doc = {"components": [
        {"component_id": "a", "gene_symbols": ["fli"]},
        {"component_id": "b", "gene_symbols": ["fliC"]},
    ]}
    comp, why = uniprot_sl.match_component(doc, "fliC")
    assert comp is None and why.startswith("ambiguous")


def test_localisation_pmids_only_experimental_for_that_term():
    entry = {"comments": [{"commentType": "SUBCELLULAR LOCATION", "subcellularLocations": [
        {"location": {"id": "SL-0034", "evidences": [
            {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "1"},
            {"evidenceCode": "ECO:0000255", "source": "HAMAP-Rule", "id": "MF_1"},
            {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "1"},
        ]}},
        {"location": {"id": "SL-0086", "evidences": [
            {"evidenceCode": "ECO:0000269", "source": "PubMed", "id": "2"}]}},
    ]}]}
    assert uniprot_sl.localisation_pmids(entry, "SL-0034") == ["1"]
