"""Offline contract tests for the BioImage Archive adapter."""

from __future__ import annotations

import io

import pytest
from PIL import Image

from scripts import bioimage_archive as bia

ACCESSION = "S-BIAD2294"
SOURCE_PATH = "Figure 3/Replicate 1/Series002_1.tif"
STUDY = {
    "accno": ACCESSION,
    "type": "submission",
    "attributes": [
        {"name": "Template", "value": "BioImages.v5"},
        {"name": "DOI", "value": f"10.6019/{ACCESSION}"},
        {"name": "AttachTo", "value": "BioImages"},
    ],
    "section": {
        "type": "Study",
        "attributes": [
            {"name": "Title", "value": "Peptidoglycan study"},
            {"name": "Description", "value": "HADA-labelled E. coli peptidoglycan."},
            {
                "name": "License",
                "value": "CC0",
                "valqual": [
                    {
                        "name": "URL",
                        "value": "https://creativecommons.org/publicdomain/zero/1.0/legalcode",
                    }
                ],
            },
        ],
        "subsections": [
            {
                "type": "Biosample",
                "attributes": [{"name": "Organism", "value": "Escherichia coli"}],
            },
            {
                "type": "Image acquisition",
                "attributes": [
                    {"name": "Imaging method", "value": "fluorescence microscopy"}
                ],
            },
            {
                "type": "Study Component",
                "attributes": [{"name": "File List", "value": "Figure 3.json"}],
            },
            {"type": "Author", "attributes": [{"name": "Name", "value": "A Researcher"}]},
        ],
    },
}


def tiff_bytes(frames: int = 3) -> bytes:
    images = [Image.new("L", (4, 3), color=10 + index) for index in range(frames)]
    output = io.BytesIO()
    images[0].save(output, format="TIFF", save_all=True, append_images=images[1:])
    return output.getvalue()


def manifest_item(source: bytes | None = None) -> dict:
    source = source if source is not None else tiff_bytes()
    return {
        "path": SOURCE_PATH,
        "size": len(source),
        "type": "file",
        "attributes": [
            {"name": "Channel 1", "value": "Phase-contrast"},
            {"name": "Channel 2", "value": "C9-AF647 (Y5)"},
            {"name": "Channel 3", "value": "HADA (CFP)"},
        ],
    }


def test_direct_study_contract_reads_per_accession_terms_and_metadata():
    contract = bia.study_contract(STUDY, ACCESSION)
    assert contract["doi"] == f"10.6019/{ACCESSION}"
    assert contract["licence"] == "CC0"
    assert contract["organisms"] == ["Escherichia coli"]
    assert contract["manifests"] == ["Figure 3.json"]
    assert contract["authors"] == ["A Researcher"]


def test_cc_by_4_0_is_normalized_for_the_record_schema():
    changed = {**STUDY, "section": {**STUDY["section"]}}
    attributes = [dict(item) for item in STUDY["section"]["attributes"]]
    attributes[2] = {
        "name": "License",
        "value": "CC BY 4.0",
        "valqual": [
            {
                "name": "URL",
                "value": "https://creativecommons.org/licenses/by/4.0/legalcode",
            }
        ],
    }
    changed["section"]["attributes"] = attributes

    contract = bia.study_contract(changed, ACCESSION)

    assert contract["licence"] == "CC_BY_4_0"
    assert contract["licence_url"] == "https://creativecommons.org/licenses/by/4.0/"


@pytest.mark.parametrize(
    ("name", "url"),
    [
        ("CC BY-NC 4.0", "https://creativecommons.org/licenses/by-nc/4.0/legalcode"),
        ("CC BY 3.0", "https://creativecommons.org/licenses/by/3.0/legalcode"),
        ("CC0", "https://example.org/terms"),
    ],
)
def test_unaccepted_or_unrecognized_licences_are_refused(name: str, url: str):
    changed = {**STUDY, "section": {**STUDY["section"]}}
    attributes = [dict(item) for item in STUDY["section"]["attributes"]]
    attributes[2] = {"name": "License", "value": name, "valqual": [{"name": "URL", "value": url}]}
    changed["section"]["attributes"] = attributes
    with pytest.raises(ValueError, match="licence"):
        bia.study_contract(changed, ACCESSION)


def test_only_direct_s_biad_bioimages_submissions_are_accepted():
    with pytest.raises(ValueError, match="direct BioImage Archive"):
        bia.study_contract({**STUDY, "accno": "S-BSST390"}, "S-BSST390")
    changed = {**STUDY, "attributes": [dict(item) for item in STUDY["attributes"]]}
    changed["attributes"][0]["value"] = "Default"
    with pytest.raises(ValueError, match="direct BioImages-template"):
        bia.study_contract(changed, ACCESSION)


def test_source_path_is_encoded_and_confined():
    url = bia.file_url(ACCESSION, "Figure 3/Replicate 1 (date)/Series 1.tif")
    assert url.endswith("/Figure%203/Replicate%201%20%28date%29/Series%201.tif")
    for unsafe in ("../secret.tif", "/absolute.tif", "nested\\escape.tif", ""):
        with pytest.raises(ValueError, match="unsafe"):
            bia.file_url(ACCESSION, unsafe)


def test_exact_file_must_match_once_and_have_a_bounded_size():
    source = tiff_bytes()
    item = manifest_item(source)
    assert bia.exact_file([[item]], SOURCE_PATH) == (item, 1)
    with pytest.raises(ValueError, match="matched 2"):
        bia.exact_file([[item], [item]], SOURCE_PATH)
    with pytest.raises(ValueError, match="size"):
        bia.exact_file([[{**item, "size": bia.MAX_SOURCE_BYTES + 1}]], SOURCE_PATH)


def test_named_tiff_channel_is_exported_losslessly_to_png():
    source = tiff_bytes()
    rendered, suffix, channel_name = bia.render_source_image(
        source, manifest_item(source), channel=3
    )
    assert suffix == ".png"
    assert channel_name == "HADA (CFP)"
    with Image.open(io.BytesIO(rendered)) as image:
        assert image.format == "PNG"
        assert image.mode == "L"
        assert set(image.get_flattened_data()) == {12}


def test_tiff_channel_selection_is_never_implicit_or_ambiguous():
    source = tiff_bytes()
    with pytest.raises(ValueError, match="explicit"):
        bia.render_source_image(source, manifest_item(source), channel=None)
    with pytest.raises(ValueError, match="not named"):
        bia.render_source_image(source, manifest_item(source), channel=4)
    with pytest.raises(ValueError, match="frame count"):
        bia.render_source_image(tiff_bytes(2), manifest_item(tiff_bytes(2)), channel=2)

    duplicate = manifest_item(source)
    duplicate["attributes"][2]["name"] = "Channel 2"
    with pytest.raises(ValueError, match="unique and contiguous"):
        bia.render_source_image(source, duplicate, channel=2)


def test_source_byte_count_must_match_manifest():
    source = tiff_bytes()
    with pytest.raises(ValueError, match="byte count"):
        bia.render_source_image(source + b"x", manifest_item(source), channel=3)


def test_non_tiff_bytes_must_match_the_declared_suffix():
    output = io.BytesIO()
    Image.new("RGB", (2, 2)).save(output, format="PNG")
    source = output.getvalue()
    item = {"path": "image.jpg", "size": len(source), "type": "file"}
    with pytest.raises(ValueError, match="not the format declared"):
        bia.render_source_image(source, item, channel=None)


def test_supported_single_image_bytes_are_retained_without_transcoding():
    output = io.BytesIO()
    Image.new("RGB", (2, 2), color="red").save(output, format="PNG")
    source = output.getvalue()
    item = {"path": "image.png", "size": len(source), "type": "file"}

    rendered, suffix, channel_name = bia.render_source_image(source, item, channel=None)

    assert rendered == source
    assert suffix == ".png"
    assert channel_name == "source image"


def test_entries_preserve_dataset_and_exact_source_file_provenance():
    source = tiff_bytes()
    item = manifest_item(source)
    rendered, suffix, channel_name = bia.render_source_image(source, item, channel=3)
    dataset, image = bia.build_entries(
        bia.study_contract(STUDY, ACCESSION),
        item,
        source,
        rendered,
        accession=ACCESSION,
        source_path=SOURCE_PATH,
        channel=3,
        channel_name=channel_name,
        output_suffix=suffix,
        manifest_count=1,
        taxon_id="NCBITaxon:562",
        taxon_label="Escherichia coli",
        source_organism="Escherichia coli",
        modality="FLUORESCENCE",
        caption="HADA-labelled peptidoglycan.",
        retrieved_on="2026-09-01",
    )
    assert dataset["accession"] == ACCESSION
    assert dataset["publication"] == f"DOI:10.6019/{ACCESSION}"
    assert image["source"] == "BIOIMAGE_ARCHIVE"
    assert image["source_accession"].endswith("#channel=3")
    assert image["licence"] == "CC0"
    assert image["file"].endswith(".png")
    assert "HADA (CFP)" in image["notes"]


def test_source_organism_must_be_asserted_by_the_study():
    source = tiff_bytes()
    item = manifest_item(source)
    with pytest.raises(ValueError, match="not a Biosample Organism"):
        bia.build_entries(
            bia.study_contract(STUDY, ACCESSION),
            item,
            source,
            b"png",
            accession=ACCESSION,
            source_path=SOURCE_PATH,
            channel=3,
            channel_name="HADA (CFP)",
            output_suffix=".png",
            manifest_count=1,
            taxon_id="NCBITaxon:562",
            taxon_label="Escherichia coli",
            source_organism="Salmonella enterica",
            modality="FLUORESCENCE",
            caption="HADA-labelled peptidoglycan.",
            retrieved_on="2026-09-01",
        )
