"""Offline contract tests for the curated MicrO xref adapter."""

import urllib.parse
from pathlib import Path

import pytest

from scripts import micro_xrefs as mx


def payload(mapping: mx.Mapping) -> dict:
    return {
        "_embedded": {
            "terms": [
                {
                    "obo_id": mapping.micro_id,
                    "iri": "http://purl.obolibrary.org/obo/"
                    + mapping.micro_id.replace(":", "_"),
                    "ontology_name": "micro",
                    "label": mapping.micro_label,
                    "is_obsolete": False,
                }
            ]
        }
    }


def test_exact_non_obsolete_ols_contract_is_accepted():
    mapping = mx.MAPPINGS[0]
    mx.validate_term(payload(mapping), mapping)


@pytest.mark.parametrize("change", [{"label": "gas vesicle"}, {"is_obsolete": True}])
def test_changed_or_obsolete_term_is_refused(change: dict):
    mapping = mx.MAPPINGS[0]
    changed = payload(mapping)
    changed["_embedded"]["terms"][0].update(change)
    with pytest.raises(ValueError, match="contract changed"):
        mx.validate_term(changed, mapping)


def test_missing_or_ambiguous_term_is_refused():
    mapping = mx.MAPPINGS[0]
    with pytest.raises(ValueError, match="exactly one"):
        mx.validate_term({"_embedded": {"terms": []}}, mapping)
    term = payload(mapping)["_embedded"]["terms"][0]
    with pytest.raises(ValueError, match="exactly one"):
        mx.validate_term({"_embedded": {"terms": [term, term]}}, mapping)


def test_plan_uses_only_the_curated_identity_allow_list():
    records = [
        (Path("gas.yaml"), {"identifier": "GO:0031411", "label": "gas vesicle"}),
        (Path("mag.yaml"), {"identifier": "GO:0110143", "label": "magnetosome"}),
        (Path("flagellum.yaml"), {"identifier": "GO:0009288", "label": "bacterial-type flagellum"}),
    ]
    seen = []

    def fetch(url: str) -> dict:
        decoded_url = urllib.parse.unquote(url)
        mapping = next(mapping for mapping in mx.MAPPINGS if mapping.micro_id in decoded_url)
        seen.append(mapping.micro_id)
        return payload(mapping)

    plan = mx.plan_xrefs(records, fetch=fetch)

    assert [mapping.micro_id for _, _, mapping in plan] == ["MICRO:0000214", "MICRO:0000216"]
    assert seen == ["MICRO:0000214", "MICRO:0000216"]


def test_existing_xref_is_idempotently_skipped_without_network():
    mapping = mx.MAPPINGS[0]
    records = [
        (
            Path("gas.yaml"),
            {
                "identifier": mapping.record_id,
                "label": mapping.record_label,
                "xrefs": [mapping.micro_id],
            },
        )
    ]

    assert mx.plan_xrefs(records, fetch=lambda _: pytest.fail("unexpected fetch")) == []


def test_record_identity_drift_is_refused():
    mapping = mx.MAPPINGS[0]
    records = [(Path("gas.yaml"), {"identifier": mapping.record_id, "label": "wrong"})]
    with pytest.raises(ValueError, match="record label changed"):
        mx.plan_xrefs(records, fetch=lambda _: payload(mapping))
