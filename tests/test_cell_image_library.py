"""Offline contract tests for the Cell Image Library adapter."""

from __future__ import annotations

import hashlib
import json

import pytest

from scripts import cell_image_library as cil

IMAGE = b"\xff\xd8\xffsource-served-preview"
HTML = b'''<!doctype html><html><head>
<script type="application/ld+json">
{"@context":"http://schema.org","@type":"Dataset",
 "name":"CIL:39991, Caulobacter crescentus CB15. CIL. Dataset",
 "image":{"@type":"ImageObject",
 "url":"https://cildata.crbs.ucsd.edu/media/thumbnail_display/39991/39991_thumbnailx512.jpg"}}
</script>
<script type="application/ld+json">
{"@context":"http://schema.org","@type":"Dataset",
 "name":"Lucy Shapiro, Harley McAdams (2012) CIL:39991, Caulobacter crescentus CB15. CIL. Dataset",
 "description":"A reconstructed tomographic data set.",
 "identifier":"doi:10.7295/W9CIL39991",
 "license":"http://creativecommons.org/licenses/by/3.0/legalcode",
 "distribution":{"@type":"DataDownload","contentUrl":"https://example.org/39991.tif"}}
</script></head></html>'''


def test_split_json_ld_is_joined_by_exact_accession():
    metadata = cil.item_metadata(HTML, "39991")
    assert metadata["identifier"] == "doi:10.7295/W9CIL39991"
    assert metadata["preview_url"].endswith("/39991_thumbnailx512.jpg")


def test_build_image_uses_per_item_terms_and_source_preview():
    metadata = cil.item_metadata(HTML, "39991")
    image = cil.build_image(
        metadata,
        IMAGE,
        accession="39991",
        taxon_id="NCBITaxon:190650",
        taxon_label="Caulobacter vibrioides CB15",
        modality="TEM",
        caption=None,
        reference=None,
        retrieved_on="2026-08-30",
    )
    assert image["source"] == "CELL_IMAGE_LIBRARY"
    assert image["source_accession"] == "CIL:39991"
    assert image["licence"] == "CC_BY_3_0"
    assert image["licence_url"] == "https://creativecommons.org/licenses/by/3.0/"
    assert image["attribution"] == "Lucy Shapiro, Harley McAdams; via Cell Image Library"
    assert image["download_url"].startswith("https://cildata.crbs.ucsd.edu/")
    assert image["file_sha256"] == hashlib.sha256(IMAGE).hexdigest()
    assert "Taxon supplied by the curator" in image["notes"]


def test_public_domain_is_not_misrepresented_as_cc0():
    licence, licence_url = cil.licence_from_url(
        "http://creativecommons.org/choose/publicdomain-3?title=x"
    )
    assert licence == "PUBLIC_DOMAIN"
    assert licence_url is None


def test_cc_by_landing_and_legalcode_urls_map_to_the_same_exact_terms():
    assert cil.licence_from_url("https://creativecommons.org/licenses/by/4.0/") == (
        "CC_BY_4_0",
        "https://creativecommons.org/licenses/by/4.0/",
    )


@pytest.mark.parametrize(
    "url",
    [
        "https://creativecommons.org/licenses/by-nc/4.0/legalcode",
        "https://creativecommons.org/licenses/by-nc-sa/4.0/legalcode",
        "https://example.org/license",
    ],
)
def test_non_hostable_or_unknown_licences_are_refused(url: str):
    with pytest.raises(ValueError, match="licence"):
        cil.licence_from_url(url)


def test_accession_and_doi_must_agree():
    with pytest.raises(ValueError, match="DOI mismatch"):
        cil.item_metadata(HTML.replace(b"W9CIL39991", b"W9CIL39992"), "39991")


def test_preview_download_is_confined_to_cil_media_host_and_accession():
    metadata = cil.item_metadata(HTML, "39991")
    for bad_url in (
        "https://example.org/media/thumbnail_display/39991/x.jpg",
        "https://cildata.crbs.ucsd.edu/media/thumbnail_display/39992/x.jpg",
        "http://cildata.crbs.ucsd.edu/media/thumbnail_display/39991/x.jpg",
    ):
        changed = dict(metadata, preview_url=bad_url)
        with pytest.raises(ValueError, match="outside the expected source path"):
            cil.preview_url(changed, "39991")


def test_duplicate_identified_datasets_are_refused():
    extra = (
        b'<script type="application/ld+json">'
        + json.dumps(cil.json_ld_datasets(HTML)[1]).encode()
        + b"</script>"
    )
    duplicate = HTML.replace(b"</head>", extra + b"</head>")
    with pytest.raises(ValueError, match="expected one identified Dataset"):
        cil.item_metadata(duplicate, "39991")


def test_preview_body_must_match_its_image_suffix():
    with pytest.raises(ValueError, match="do not match"):
        cil.verify_image_format(b"<html>temporary error</html>", ".jpg")
