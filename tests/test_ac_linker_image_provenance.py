"""Keep source-denoised tomography distinct from raw image data."""

import hashlib
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]
SLUG = "basal_body_a_c_linker"


def image_metadata():
    path = ROOT / "data/structures/cytoskeleton" / f"{SLUG}.yaml"
    return yaml.safe_load(path.read_text())["images"][0]


def test_caption_discloses_source_denoising():
    image = image_metadata()
    assert "denoised" in image["caption"]
    assert "raw in-situ" not in image["caption"]
    assert "DeepDeWedge" in image["notes"]
    assert "source" in image["notes"].lower()


def test_processing_description_does_not_replace_the_source_figure():
    image = image_metadata()
    path = ROOT / "data/images/cytoskeleton" / SLUG / image["file"]
    original_hash = "fe0ce1a1e2152db5441413b3f999800bb60903ecfd8664ddcb78b352d3d995ad"
    assert hashlib.sha256(path.read_bytes()).hexdigest() == original_hash
    assert image["file_sha256"] == original_hash
    assert image["source_accession"] == "PMC12506977.1 F1"
    assert image["reference"] == "DOI:10.1126/sciadv.ady3689"
    assert image["licence"] == "CC_BY_4_0"
    assert "Cai" in image["attribution"]
    assert "D is the isolation schematic" in image["caption"]
    assert "SDS-PAGE" in image["caption"]
    assert "Scale bars: A, 200 nm; B-C and F-G, 100 nm." in image["caption"]
