"""Offline contract tests for the linked EMPIAR/EMDB adapter."""

from __future__ import annotations

import pytest

from scripts import emdb_empiar as ee

EMPIAR = {
    "title": "ATP synthase raw micrographs",
    "status": "REL",
    "cross_references": ["EMD-1234"],
    "entry_doi": "10.6019/EMPIAR-10000",
    "imagesets": [{"category": "micrographs - multiframe", "num_images_or_tilt_series": 12}],
    "citation": [{"doi": "10.1000/example"}],
}
EMDB = {
    "emdb_id": "EMD-1234",
    "admin": {
        "title": "E. coli ATP synthase",
        "authors_list": {"author": [{"valueOf_": "Curator A"}, {"valueOf_": "Curator B"}]},
    },
    "sample": {
        "natural_source": {
            "organism": {"ncbi": 83333, "valueOf_": "Escherichia coli K-12"}
        }
    },
    "final_reconstruction": {"resolution": {"valueOf_": "3.2", "units": "Å"}},
}


def test_taxon_is_resolved_from_emdb_not_empiar():
    assert ee.emdb_taxa(EMDB) == {"NCBITaxon:83333": "Escherichia coli K-12"}
    assert ee.empiar_xrefs(EMPIAR) == {"EMD-1234"}


def test_only_exact_emdb_cross_references_count_as_taxon_bridges():
    mixed = {
        "cross_references": [
            "PDB:1ABC",
            {"name": "EMD-4321"},
            {"name": "EMD-not-a-number"},
            {"name": "PDB:2DEF"},
        ]
    }
    assert ee.empiar_xrefs(mixed) == {"EMD-4321"}
    assert ee.empiar_xrefs({"cross_references": ["PDB:1ABC"]}) == set()


def test_entries_preserve_raw_dataset_and_representative_image_separately():
    dataset, image = ee.build_entries(
        "EMPIAR-10000",
        EMPIAR,
        "EMD-1234",
        EMDB,
        taxon_id="NCBITaxon:83333",
        modality="CRYO_EM",
        caption=None,
        image_bytes=b"png",
        filename="emdb_emd_1234.png",
        retrieved_on="2026-08-30",
    )

    assert dataset["accession"] == "EMPIAR:10000"
    assert dataset["sample_count"] == 12
    assert dataset["repository"] == "OTHER"
    assert image["source"] == "EMDB"
    assert image["licence"] == "PUBLIC_DOMAIN"
    assert image["reference"] == "DOI:10.1000/example"
    assert "resolution: 3.2 Å" in image["notes"]
    assert "physical_properties" not in dataset and "physical_properties" not in image


def test_requested_taxon_must_be_asserted_by_emdb():
    with pytest.raises(ValueError, match="does not assert"):
        ee.build_entries(
            "EMPIAR-10000",
            EMPIAR,
            "EMD-1234",
            EMDB,
            taxon_id="NCBITaxon:2",
            modality="CRYO_EM",
            caption=None,
            image_bytes=b"png",
            filename="x.png",
            retrieved_on="2026-08-30",
        )
