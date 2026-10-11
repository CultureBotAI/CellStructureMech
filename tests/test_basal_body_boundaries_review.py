"""Preserve substructure classification and the B-tubule discussion history."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"


def record(slug):
    return yaml.safe_load((ROOT / f"{slug}.yaml").read_text())


def test_b_tubule_retains_original_and_narrowed_rationales():
    doc = record("b_axonemal_microtubule")
    discussion = doc["discussions"][0]
    assert discussion["rationale"].startswith(
        "GO exactly identifies the B axonemal microtubule, but this pass curates "
        "only its coarse role in the outer doublet and leaves exact protofilament "
        "and MIP placement unresolved."
    )
    assert "Historical reassessment at git 871db9b2b9d6:" in discussion["rationale"]
    assert "GO:0160112 now captures the B-tubule inner sheath" in discussion["rationale"]
    assert discussion["discussion_id"] == "resolve_b_tubule_protofilaments_and_mips"
    assert discussion["status"] == "OPEN"
    assert discussion["posed_date"] == "2026-09-23"
    assert "non-inner-sheath B-tubule" in discussion["prompt"]
    assert discussion["attaches_to"] == ["causal_graphs#chlamydomonas_b_tubule_doublet_scaffold"]
    assert doc["has_part"] == ["GO:0160112"]
    assert doc["parent_structures"] == ["GO:0005879"]
    assert doc["part_of"] == ["GO:0097545"]
    assert len(doc["causal_graphs"][0]["edges"]) == 4


@pytest.mark.parametrize(
    ("slug", "kind", "measurements"),
    [
        ("basal_body_c_tubule_hook", "OTHER", ["8"]),
        ("basal_body_c_tubule_luminal_filament", "FILAMENT", ["8", "13.6"]),
    ],
)
def test_c_tubule_parts_do_not_become_types_of_cytoskeleton(slug, kind, measurements):
    doc = record(slug)
    assert doc["identifier"] == f"cellstructuremech:{slug}"
    assert doc["parent_structures"] == ["GO:0005575"]
    assert doc["part_of"] == ["GO:0036064"]
    assert doc["structure_kind"] == kind
    assert not doc.get("components") and not doc.get("causal_graphs")
    assert [p["value"] for p in doc["physical_properties"]] == measurements
    assert {p["unit"] for p in doc["physical_properties"]} == {"UO:0000018"}
    assert doc["canonical_examples"][0]["taxon_id"] == "NCBITaxon:3055"
    assert doc["datasets"][0]["accession"] == "EMDB:EMD-5252"
    assert "Whole-triplet" in doc["datasets"][0]["description"]
    image = doc["images"][0]
    assert image["licence"] == "OTHER"
    assert image["licence_url"] == "https://creativecommons.org/licenses/by-nc-nd/3.0/"
    assert not {"file", "file_sha256", "download_url"} & image.keys()
    identity = doc["discussions"][0]
    assert identity["status"] == "RESOLVED"
    assert identity["posed_date"] == identity["resolved_date"] == "2026-10-04"
    assert "GO:0005575" in identity["notes"]
    assert "not an is-a parent" in identity["notes"]
    molecular_identity = next(d for d in doc["discussions"] if d["discussion_id"] == "molecular_identity")
    assert molecular_identity["status"] == "OPEN"
    assert doc["mapping_status"] == "PROPOSED"
