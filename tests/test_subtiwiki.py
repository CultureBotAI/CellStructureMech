"""Offline contract tests for the narrow SubtiWiki adapter."""

from __future__ import annotations

import pytest

from scripts import subtiwiki


def wrapped(data: dict) -> dict:
    return {"code": 200, "isSuccess": True, "data": data}


def category_payload() -> dict:
    return wrapped(
        {
            "id": subtiwiki.CATEGORY_ID,
            "name": subtiwiki.CATEGORY_NAME,
            "dot_notation": subtiwiki.CATEGORY_DOT_NOTATION,
            "genes": [
                {"id": target.gene_id, "name": target.gene_symbol}
                for target in subtiwiki.TARGETS
            ],
        }
    )


def test_category_contract_accepts_exact_reviewed_membership():
    subtiwiki.validate_category(category_payload())


def test_category_contract_refuses_identity_or_membership_drift():
    payload = category_payload()
    payload["data"]["name"] = "Flagella-ish"
    with pytest.raises(ValueError, match="identity changed"):
        subtiwiki.validate_category(payload)

    payload = category_payload()
    payload["data"]["genes"].pop()
    with pytest.raises(ValueError, match="membership changed"):
        subtiwiki.validate_category(payload)


def test_outlink_requires_exact_gene_and_uniprot_accession():
    target = subtiwiki.TARGETS[0]
    payload = wrapped({"gene_id": target.gene_id, "uniprot": "P02968"})
    assert subtiwiki.accession_from_outlink(payload, target) == "P02968"

    payload["data"]["gene_id"] = 999
    with pytest.raises(ValueError, match="id changed"):
        subtiwiki.accession_from_outlink(payload, target)


def test_normalize_example_checks_independent_uniprot_identity():
    target = subtiwiki.Target("ms_ring", 1705, "fliF")
    uniprot = {
        "primaryAccession": "P23447",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "organism": {"taxonId": subtiwiki.TAXON_NUMBER},
        "genes": [{"geneName": {"value": "fliF"}}],
        "proteinDescription": {"recommendedName": {"fullName": {"value": "Flagellar M-ring protein"}}},
    }
    result = subtiwiki.normalize_example(
        target, "P23447", uniprot, {"label": "MS ring (FliF)"}, "2026-09-01"
    )
    assert result["uniprot_id"] == "UniProtKB:P23447"
    assert result["taxon_id"] == "NCBITaxon:224308"
    assert result["entry_status"] == "REVIEWED"
    assert result["evidence"][0]["reference"].endswith("/gene/fliF")

    uniprot["organism"]["taxonId"] = 1423
    with pytest.raises(ValueError, match="has taxon"):
        subtiwiki.normalize_example(
            target, "P23447", uniprot, {"label": "MS ring"}, "2026-09-01"
        )


def test_historical_subtiwiki_symbol_must_match_curated_uniprot_primary_symbol():
    target = subtiwiki.Target("rod", 1713, "flgE", "flgG")
    uniprot = {
        "primaryAccession": "P23446",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "organism": {"taxonId": subtiwiki.TAXON_NUMBER},
        "genes": [{"geneName": {"value": "flgG"}}],
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": "Flagellar basal-body rod protein FlgG"}}
        },
    }
    result = subtiwiki.normalize_example(
        target, "P23446", uniprot, {"label": "rod"}, "2026-09-01"
    )
    assert result["gene_symbol"] == "flgG"
    assert "current UniProt primary gene symbol is flgG" in result["evidence"][0]["notes"]


def test_role_reference_adds_independent_evidence():
    target = subtiwiki.Target(
        "stator", 3153, "motP", "ytxD", "DOI:10.1016/j.jmb.2005.07.030"
    )
    uniprot = {
        "primaryAccession": "P39063",
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "organism": {"taxonId": subtiwiki.TAXON_NUMBER},
        "genes": [{"geneName": {"value": "ytxD"}}],
        "proteinDescription": {
            "recommendedName": {"fullName": {"value": "Uncharacterized protein YtxD"}}
        },
    }
    result = subtiwiki.normalize_example(
        target, "P39063", uniprot, {"label": "stator"}, "2026-09-01"
    )
    assert result["evidence"][1]["reference"] == "DOI:10.1016/j.jmb.2005.07.030"


def test_record_contract_refuses_other_records_and_missing_components():
    components = [
        {"component_id": component_id}
        for component_id in sorted({target.component_id for target in subtiwiki.TARGETS})
    ]
    record = {"identifier": subtiwiki.RECORD_ID, "components": components}
    assert set(subtiwiki.ensure_record_contract(record)) == {
        target.component_id for target in subtiwiki.TARGETS
    }

    record["identifier"] = "GO:0005840"
    with pytest.raises(ValueError, match="only accepts"):
        subtiwiki.ensure_record_contract(record)


def test_canonical_taxon_is_idempotent():
    record: dict = {"canonical_examples": []}
    assert subtiwiki.ensure_canonical_taxon(record) is True
    assert subtiwiki.ensure_canonical_taxon(record) is False
    assert record["canonical_examples"][0]["taxon_label"] == subtiwiki.TAXON_LABEL


def test_canonical_taxon_refuses_to_overwrite_curator_content():
    record = {
        "canonical_examples": [
            {"taxon_id": subtiwiki.TAXON_ID, "taxon_label": "curator-authored value"}
        ]
    }
    with pytest.raises(ValueError, match="refusing overwrite"):
        subtiwiki.ensure_canonical_taxon(record)
