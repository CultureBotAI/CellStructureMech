"""Offline contract tests for the Complex Portal adapter."""

from __future__ import annotations

import pytest

from scripts import complex_portal as cp

ENTRY = {
    "complexAc": "CPX-4022",
    "name": "ATP synthase complex",
    "species": "Escherichia coli (strain K12); 83333",
    "complexAssemblies": ["Hetero8-mer"],
    "evidenceType": {"identifier": "ECO:0005547", "description": "inferred by curator"},
    "participants": [
        {
            "identifier": "P68699",
            "interactorAC": "EBI-1121219",
            "name": "atpE",
            "description": "ATP synthase subunit c",
            "stochiometry": "minValue: 10, maxValue: 10",
            "interactorType": "protein",
        },
        {
            "identifier": "URS00005CADE5_83333",
            "interactorAC": "EBI-20767460",
            "name": "16s_rrna_ecoli",
            "description": "Ribosomal RNA 16S Escherichia coli",
            "stochiometry": "minValue: 1, maxValue: 2",
            "interactorType": "ribosomal rna",
        },
    ],
}


def test_normalize_entry_keeps_taxon_specific_participants_and_copy_numbers():
    result = cp.normalize_entry(ENTRY, retrieved_on="2026-08-30", scope_note="selected complex")

    assert result["source_accession"] == "ComplexPortal:CPX-4022"
    assert result["taxon_id"] == "NCBITaxon:83333"
    assert result["evidence_code"] == "ECO:0005547"
    assert result["participants"][0]["participant_id"] == "UniProtKB:P68699"
    assert result["participants"][0]["stoichiometry"] == "10"
    assert result["participants"][1]["participant_id"].startswith("RNAcentral:URS")
    assert result["participants"][1]["stoichiometry"] == "1-2"
    assert "equivalence xref was inferred" in result["notes"]


def test_unrecognized_stoichiometry_is_refused_instead_of_guessed():
    with pytest.raises(ValueError, match="unrecognized"):
        cp.normalize_stoichiometry("approximately 12")


def test_unknown_nonprotein_identifier_has_no_invented_prefix():
    with pytest.raises(ValueError, match="cannot assign a CURIE prefix"):
        cp.participant_curie({"identifier": "mystery", "interactorType": "other"})
