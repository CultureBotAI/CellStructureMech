"""Offline contract tests for the 2026 PMC OA S3 adapter."""

from __future__ import annotations

import hashlib

import pytest

from scripts import pmc_oa as pmc

XML = b"""<article xmlns:xlink="http://www.w3.org/1999/xlink">
<front><article-meta><permissions><license>
  <license-p>This is an open access article under the
    <ext-link xlink:href="https://creativecommons.org/licenses/by/3.0/">CC BY 3.0</ext-link>.
  </license-p>
</license></permissions><contrib-group>
  <contrib contrib-type="author"><name><surname>Ng</surname><given-names>A</given-names></name></contrib>
</contrib-group></article-meta></front>
<body>
  <fig id="F1"><label>Figure 1</label><caption><p>A transmission electron micrograph.</p></caption>
    <graphic xlink:href="fig1.jpg"/></fig>
  <fig id="F2"><label>Figure 2</label><caption><p>(A) Cells. (B) Detail.</p></caption>
    <graphic xlink:href="fig2.jpg"/></fig>
</body></article>"""
IMAGE = b"test-image"
METADATA = {
    "pmcid": "PMC123",
    "version": 2,
    "pmid": 456,
    "doi": "10.1000/pmc",
    "license_code": "CC BY",
    "is_retracted": False,
    "xml_url": "s3://pmc-oa-opendata/PMC123.2/PMC123.2.xml?md5=abc",
    "media_urls": [
        "s3://pmc-oa-opendata/PMC123.2/fig1.jpg?md5=" + hashlib.md5(IMAGE).hexdigest(),
        "s3://pmc-oa-opendata/PMC123.2/fig2.jpg?md5=def",
    ],
}


def test_latest_version_reads_current_metadata_prefix(monkeypatch):
    listing = b"""<ListBucketResult xmlns="http://s3.amazonaws.com/doc/2006-03-01/">
      <Contents><Key>metadata/PMC123.1.json</Key></Contents>
      <Contents><Key>metadata/PMC123.3.json</Key></Contents>
    </ListBucketResult>"""
    monkeypatch.setattr(pmc, "get_bytes", lambda _url: listing)
    assert pmc.latest_version("PMC123") == 3


def test_exact_figure_and_media_are_joined_by_source_ids_and_md5(monkeypatch):
    root = pmc.ET.fromstring(XML)
    monkeypatch.setattr(pmc, "get_bytes", lambda _url: IMAGE)
    image, data = pmc.build_image(
        METADATA,
        root,
        figure_id="F1",
        taxon_id="NCBITaxon:83333",
        taxon_label="Escherichia coli K-12",
        modality="TEM",
        caption_override=None,
        accept_multipanel=False,
        retrieved_on="2026-08-30",
    )

    assert data == IMAGE
    assert image["source_accession"] == "PMC123.2 F1"
    assert image["licence"] == "CC_BY_3_0"
    assert image["licence_url"] == "https://creativecommons.org/licenses/by/3.0/"
    assert image["attribution"].startswith("A Ng;")
    assert image["file_sha256"] == hashlib.sha256(IMAGE).hexdigest()


def test_multipanel_figure_requires_explicit_acknowledgement(monkeypatch):
    root = pmc.ET.fromstring(XML)
    monkeypatch.setattr(pmc, "get_bytes", lambda _url: IMAGE)
    with pytest.raises(ValueError, match="multi-panel"):
        pmc.build_image(
            METADATA,
            root,
            figure_id="F2",
            taxon_id="NCBITaxon:83333",
            taxon_label="Escherichia coli K-12",
            modality="TEM",
            caption_override=None,
            accept_multipanel=False,
            retrieved_on="2026-08-30",
        )


def test_unparenthesized_journal_panel_labels_are_detected():
    xml = pmc.ET.fromstring(
        b'<fig xmlns:xlink="http://www.w3.org/1999/xlink" id="F3">'
        b"<caption><p>Results.A and B, Cells. C, Quantification.</p></caption>"
        b'<graphic xlink:href="fig3.jpg"/></fig>'
    )
    root = pmc.ET.fromstring(b"<article/>" )
    root.append(xml)
    assert pmc.figure(root, "F3")[3] is True


def test_noncommercial_article_is_not_hostable(monkeypatch):
    metadata = dict(METADATA, license_code="CC BY-NC")
    monkeypatch.setattr(pmc, "get_json", lambda _url: metadata)
    with pytest.raises(ValueError, match="not CC BY or CC0"):
        pmc.article_metadata("PMC123", 2)


def test_cc_by_version_is_never_guessed_from_metadata_code():
    root = pmc.ET.fromstring(
        b'<article xmlns:xlink="http://www.w3.org/1999/xlink"><front><article-meta>'
        b'<permissions><license><ext-link xlink:href="https://creativecommons.org/licenses/by/4.0/"/>'
        b'</license></permissions></article-meta></front></article>'
    )
    assert pmc.article_license(root, "CC BY") == (
        "CC_BY_4_0",
        "https://creativecommons.org/licenses/by/4.0/",
    )


def test_missing_or_disagreeing_jats_licence_is_refused():
    with pytest.raises(ValueError, match="exactly one recognized"):
        pmc.article_license(pmc.ET.fromstring(b"<article/>"), "CC BY")
    cc0 = pmc.ET.fromstring(
        b'<article xmlns:xlink="http://www.w3.org/1999/xlink"><license>'
        b'<ext-link xlink:href="http://creativecommons.org/publicdomain/zero/1.0/"/>'
        b"</license></article>"
    )
    with pytest.raises(ValueError, match="disagrees"):
        pmc.article_license(cc0, "CC BY")
