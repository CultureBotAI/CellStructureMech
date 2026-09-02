"""Offline contract tests for the narrow PSORTdb adapter."""

from __future__ import annotations

import csv
import hashlib
import io
import plistlib

import pytest

from scripts import psortdb


def target_row(**changes: str) -> dict[str, str]:
    row = dict.fromkeys(psortdb.EXPECTED_COLUMNS, "")
    row.update(
        {
            "SwissProt_ID": psortdb.TARGET.accession,
            "Experimental_Localization": psortdb.TARGET.experimental_localization,
            "Secondary_Localization": psortdb.TARGET.secondary_localization,
            "MultipleSCL": "0",
            "ProteinName": psortdb.TARGET.protein_name,
            "GeneName": psortdb.TARGET.gene_symbol,
            "TaxID": str(psortdb.TARGET.taxon_id),
            "Organism": psortdb.TARGET.taxon_label,
            "PMID": str(psortdb.TARGET.pmid),
            "ePSORTdbVersion": psortdb.TARGET.source_version,
        }
    )
    row.update(changes)
    return row


def archive_bytes(
    rows: list[dict[str, str]] | None = None,
    *,
    columns: tuple[str, ...] = psortdb.EXPECTED_COLUMNS,
    url: str = psortdb.DOWNLOAD_URL,
    mime: str = "text/tab-separated-values",
    encoding: str = "UTF-8",
    prefix: str = psortdb.HTML_PREFIX,
    suffix: str = psortdb.HTML_SUFFIX,
) -> bytes:
    stream = io.StringIO(newline="")
    writer = csv.DictWriter(stream, fieldnames=columns, delimiter="\t", extrasaction="ignore")
    writer.writeheader()
    writer.writerows(rows if rows is not None else [target_row()])
    wrapped = f"{prefix}{stream.getvalue()}{suffix}".encode()
    return plistlib.dumps(
        {
            "WebMainResource": {
                "WebResourceURL": url,
                "WebResourceMIMEType": mime,
                "WebResourceTextEncodingName": encoding,
                "WebResourceData": wrapped,
            }
        },
        fmt=plistlib.FMT_BINARY,
    )


def parse_fixture(payload: bytes, *, rows: int = 1) -> list[dict]:
    return psortdb.parse_download(
        payload,
        expected_sha256=hashlib.sha256(payload).hexdigest(),
        expected_row_count=rows,
    )


def uniprot_payload() -> dict:
    return {
        "primaryAccession": psortdb.TARGET.accession,
        "entryType": "UniProtKB reviewed (Swiss-Prot)",
        "organism": {"taxonId": psortdb.TARGET.taxon_id},
        "genes": [{"geneName": {"value": psortdb.TARGET.gene_symbol}}],
        "proteinDescription": {
            "recommendedName": {
                "fullName": {"value": "Spore coat morphogenetic protein CotE"}
            }
        },
    }


def pubmed_payload() -> dict:
    return {
        "result": {
            str(psortdb.TARGET.pmid): {
                "uid": str(psortdb.TARGET.pmid),
                "title": psortdb.TARGET.pubmed_title,
            }
        }
    }


def record() -> dict:
    return {
        "identifier": psortdb.TARGET.record_id,
        "canonical_examples": [],
        "components": [
            {
                "component_id": psortdb.TARGET.component_id,
                "label": "endospore coat proteins",
                "gene_symbols": [psortdb.TARGET.gene_symbol],
            }
        ],
    }


def test_webarchive_contract_and_exact_canary_are_accepted():
    payload = archive_bytes()
    rows = parse_fixture(payload)
    assert psortdb.select_target(rows)["PMID"] == str(psortdb.TARGET.pmid)


def test_artifact_hash_and_wrapper_contract_fail_closed():
    payload = archive_bytes()
    with pytest.raises(ValueError, match="SHA-256 changed"):
        psortdb.parse_download(payload, expected_sha256="0" * 64, expected_row_count=1)

    for changed, message in (
        ({"url": "https://example.org/export"}, "resource contract changed"),
        ({"mime": "text/html"}, "resource contract changed"),
        ({"encoding": "latin-1"}, "resource contract changed"),
        ({"prefix": "<pre>"}, "HTML envelope changed"),
    ):
        drifted = archive_bytes(**changed)
        with pytest.raises(ValueError, match=message):
            parse_fixture(drifted)


def test_columns_row_count_and_target_identity_fail_closed():
    missing_column = tuple(c for c in psortdb.EXPECTED_COLUMNS if c != "PMID")
    with pytest.raises(ValueError, match="columns changed"):
        parse_fixture(archive_bytes(columns=missing_column))

    payload = archive_bytes()
    with pytest.raises(ValueError, match="row count changed"):
        psortdb.parse_download(
            payload,
            expected_sha256=hashlib.sha256(payload).hexdigest(),
            expected_row_count=2,
        )

    for rows, message in (
        ([], "got 0"),
        ([target_row(), target_row()], "got 2"),
        ([target_row(PMID="999")], "canary changed"),
        ([target_row(Secondary_Localization="Spore")], "canary changed"),
    ):
        with pytest.raises(ValueError, match=message):
            psortdb.select_target(rows)


def test_independent_authority_contracts_fail_closed():
    assert psortdb.validate_uniprot(uniprot_payload()) == (
        "Spore coat morphogenetic protein CotE"
    )
    psortdb.validate_pubmed(pubmed_payload())

    for path, value, message in (
        (("entryType",), "UniProtKB unreviewed (TrEMBL)", "not reviewed"),
        (("organism", "taxonId"), 1423, "taxon changed"),
        (("genes", 0, "geneName", "value"), "spoIVA", "primary gene changed"),
        (
            ("proteinDescription", "recommendedName", "fullName", "value"),
            "Other protein",
            "recommended name changed",
        ),
    ):
        payload = uniprot_payload()
        parent = payload
        for key in path[:-1]:
            parent = parent[key]
        parent[path[-1]] = value
        with pytest.raises(ValueError, match=message):
            psortdb.validate_uniprot(payload)

    payload = pubmed_payload()
    payload["result"][str(psortdb.TARGET.pmid)]["title"] = "Different paper"
    with pytest.raises(ValueError, match="identity or title changed"):
        psortdb.validate_pubmed(payload)


def test_record_and_canonical_taxon_contracts_are_exact_and_idempotent():
    doc = record()
    assert psortdb.ensure_record(doc)["component_id"] == psortdb.TARGET.component_id
    assert psortdb.ensure_canonical_taxon(doc) is True
    assert psortdb.ensure_canonical_taxon(doc) is False

    doc["canonical_examples"][0]["taxon_label"] = "conflicting curator value"
    with pytest.raises(ValueError, match="conflicting"):
        psortdb.ensure_canonical_taxon(doc)

    wrong = record()
    wrong["identifier"] = "GO:0000000"
    with pytest.raises(ValueError, match="only accepts"):
        psortdb.ensure_record(wrong)


def test_plan_uses_only_exact_endpoints_and_is_idempotent(monkeypatch):
    payload = archive_bytes()
    original_parse_download = psortdb.parse_download
    monkeypatch.setattr(
        psortdb,
        "parse_download",
        lambda value: original_parse_download(
            value,
            expected_sha256=hashlib.sha256(value).hexdigest(),
            expected_row_count=1,
        ),
    )
    requested: list[str] = []

    def fetch_bytes(url: str) -> bytes:
        requested.append(url)
        return payload

    def fetch_json(url: str) -> dict:
        requested.append(url)
        if url == psortdb.UNIPROT_URL:
            return uniprot_payload()
        if url == psortdb.PUBMED_URL:
            return pubmed_payload()
        raise AssertionError(f"unexpected endpoint: {url}")

    doc = record()
    value, taxon_changed, action = psortdb.plan(
        doc, fetch_bytes=fetch_bytes, fetch_json=fetch_json
    )
    assert (taxon_changed, action) == (True, "added")
    assert value["uniprot_id"] == "UniProtKB:P14016"
    assert requested == [psortdb.DOWNLOAD_URL, psortdb.UNIPROT_URL, psortdb.PUBMED_URL]
    assert all("cpsort" not in url.casefold() for url in requested)

    _, taxon_changed, action = psortdb.plan(
        doc, fetch_bytes=fetch_bytes, fetch_json=fetch_json
    )
    assert (taxon_changed, action) == (False, "unchanged")


def test_failed_plan_does_not_partially_mutate_the_record(monkeypatch):
    payload = archive_bytes()
    original_parse_download = psortdb.parse_download
    monkeypatch.setattr(
        psortdb,
        "parse_download",
        lambda value: original_parse_download(
            value,
            expected_sha256=hashlib.sha256(value).hexdigest(),
            expected_row_count=1,
        ),
    )
    doc = record()

    def failing_json(url: str) -> dict:
        if url == psortdb.UNIPROT_URL:
            invalid = uniprot_payload()
            invalid["entryType"] = "UniProtKB unreviewed (TrEMBL)"
            return invalid
        raise AssertionError("PubMed must not be requested after UniProt fails")

    with pytest.raises(ValueError, match="not reviewed"):
        psortdb.plan(doc, fetch_bytes=lambda _url: payload, fetch_json=failing_json)

    assert doc["canonical_examples"] == []
    assert "protein_examples" not in doc["components"][0]
