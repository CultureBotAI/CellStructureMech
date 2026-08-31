"""Offline tests for scripts/fetch_commons_image.py — no network."""

from __future__ import annotations

from scripts import fetch_commons_image as fci

PAGE = {
    "pageid": 4508748,
    "imageinfo": [{
        "url": "https://upload.wikimedia.org/wikipedia/commons/f/f5/X.jpg?utm_source=commons&utm_content=original",
        "sha1": "deadbeef",
        "extmetadata": {
            "LicenseShortName": {"value": "CC BY 3.0"},
            "LicenseUrl": {"value": "https://creativecommons.org/licenses/by/3.0"},
            "Artist": {"value": "<a href='#'>Tsai Y</a>, Sawaya MR"},
            "Credit": {"value": "<i>PLoS biology</i> - Tsai Y et al"},
        },
    }],
}


def test_tracking_parameters_are_stripped():
    """imageinfo.url gained utm_* parameters; the bare path is the stable URL (#34)."""
    assert fci.strip_tracking(PAGE["imageinfo"][0]["url"]) == \
        "https://upload.wikimedia.org/wikipedia/commons/f/f5/X.jpg"


def test_html_is_reduced_to_plain_attribution_text():
    assert fci.plain("<a href='#'>Tsai Y</a>,  Sawaya MR") == "Tsai Y, Sawaya MR"


def test_hostable_licences_are_exactly_the_redistributable_ones():
    """The schema and tests/test_corpus_integrity.py enforce the same set; if these
    drift apart the script would download something the corpus must not host."""
    assert {"CC0", "PUBLIC_DOMAIN", "CC_BY_3_0", "CC_BY_4_0",
                            "CC_BY_SA_3_0", "CC_BY_SA_4_0"} == fci.HOSTABLE
    assert set(fci.LICENCES.values()) >= fci.HOSTABLE
    for nc in ("CC BY-NC 4.0", "CC BY-NC-SA 4.0", "CC BY-ND 4.0"):
        assert fci.LICENCES[nc] not in fci.HOSTABLE


def test_an_unmapped_licence_string_has_no_mapping():
    """Refusing beats guessing: an unrecognised licence must not resolve."""
    assert fci.LICENCES.get("CC BY-SA 2.5 fr") is None
    assert fci.LICENCES.get("Copyrighted free use") is None


def test_build_image_reads_licence_attribution_and_hash_from_the_api():
    entry = fci.build_image(PAGE, "File:X.jpg", modality="TEM", caption="a cell",
                            taxon=("NCBITaxon:927", "Halothiobacillus neapolitanus"),
                            licence="CC_BY_3_0", image_id="x", today="2026-08-30",
                            file_name="x.jpg", sha256="a" * 64)
    assert entry["licence"] == "CC_BY_3_0"
    assert entry["attribution"] == "Tsai Y, Sawaya MR; CC BY 3.0, via Wikimedia Commons"
    assert entry["download_url"].endswith("/X.jpg")
    assert entry["file_sha256"] == "a" * 64
    assert entry["taxon_id"] == "NCBITaxon:927"
    assert "PLoS biology" in entry["notes"]


def test_source_credit_is_not_silently_truncated():
    page = {"pageid": 1, "imageinfo": [{
        "url": "https://upload.wikimedia.org/x.jpg", "sha1": "d",
        "extmetadata": {
            "LicenseShortName": {"value": "CC BY 3.0"},
            "Artist": {"value": "Example Author"},
            "Credit": {"value": "complete provenance " + "x" * 220},
        },
    }]}
    entry = fci.build_image(
        page, "File:X.jpg", modality="TEM", caption=None,
        taxon=("NCBITaxon:1", "root"), licence="CC_BY_3_0", image_id="x",
        today="2026-08-30", file_name="x.jpg", sha256="a" * 64,
    )
    assert entry["notes"].endswith("x" * 220)


def test_missing_licence_url_is_omitted_not_empty():
    """Commons omits LicenseUrl for public-domain files; '' is not a uri and the
    write gate rejects it — caught while adding the CDC flagellum image."""
    page = {"pageid": 1, "imageinfo": [{
        "url": "https://upload.wikimedia.org/x.png", "sha1": "d",
        "extmetadata": {"LicenseShortName": {"value": "Public domain"}, "Artist": {"value": "CDC"}},
    }]}
    entry = fci.build_image(page, "File:X.png", modality="TEM", caption=None,
                            taxon=("NCBITaxon:83334", "Escherichia coli O157:H7"),
                            licence="PUBLIC_DOMAIN", image_id="x", today="2026-08-30",
                            file_name="x.png", sha256="b" * 64)
    assert "licence_url" not in entry


def test_a_link_only_entry_carries_no_file():
    entry = fci.build_image(PAGE, "File:X.jpg", modality="CRYO_ET", caption=None,
                            taxon=("NCBITaxon:1", "root"), licence="CC_BY_NC_4_0",
                            image_id="x", today="2026-08-30", file_name=None, sha256=None)
    assert "file" not in entry and "file_sha256" not in entry


def test_slug_is_filesystem_safe():
    assert fci.slug("P. urativorans 70S ribosome with Balon and RaiA") == \
        "p_urativorans_70s_ribosome_with_balon_and_raia"
