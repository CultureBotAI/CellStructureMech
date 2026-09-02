"""Offline contracts for exact RCSB PDB experimental-structure ingestion."""

from copy import deepcopy
from pathlib import Path

import pytest

from scripts import rcsb_pdb as rcsb


def responses(target: rcsb.Target) -> dict[str, dict]:
    entry = {
        "rcsb_id": target.pdb_id,
        "entry": {"id": target.pdb_id},
        "struct": {"title": target.title},
        "exptl": [{"method": target.method}],
        "em_experiment": {"reconstruction_method": target.reconstruction_method},
        "em_3d_reconstruction": [{"resolution": target.resolution}],
        "rcsb_entry_info": {
            "experimental_method": "EM",
            "structure_determination_methodology": "experimental",
            "resolution_combined": [target.resolution],
            "polymer_entity_count": len(target.entities),
            "polymer_entity_count_protein": len(target.entities),
        },
        "rcsb_entry_container_identifiers": {
            "entry_id": target.pdb_id,
            "rcsb_id": target.pdb_id,
            "assembly_ids": list(target.assembly_ids),
            "polymer_entity_ids": [item.entity_id for item in target.entities],
            "pubmed_id": target.pubmed_id,
            "emdb_ids": [target.emdb_id],
        },
        "rcsb_primary_citation": {
            "pdbx_database_id_DOI": target.doi,
            "pdbx_database_id_PubMed": target.pubmed_id,
        },
        "rcsb_accession_info": {
            "deposit_date": "2019-04-29T00:00:00.000+00:00",
            "initial_release_date": "2020-06-03T00:00:00.000+00:00",
            "revision_date": "2025-06-04T00:00:00.000+00:00",
            "status_code": "REL",
            "has_released_experimental_data": "Y",
        },
    }
    result = {f"{rcsb.DATA_API}/entry/{target.pdb_id}": entry}
    for expected in target.entities:
        result[f"{rcsb.DATA_API}/polymer_entity/{target.pdb_id}/{expected.entity_id}"] = {
            "rcsb_id": f"{target.pdb_id}_{expected.entity_id}",
            "rcsb_polymer_entity_container_identifiers": {
                "entity_id": expected.entity_id,
                "uniprot_ids": [expected.uniprot_id],
            },
            "rcsb_polymer_entity": {
                "pdbx_description": expected.description,
                "pdbx_number_of_molecules": expected.molecule_count,
            },
            "rcsb_entity_source_organism": [
                {"ncbi_taxonomy_id": target.taxon_id, "scientific_name": target.organism_name}
            ],
        }
    for assembly_id in target.assembly_ids:
        result[f"{rcsb.DATA_API}/assembly/{target.pdb_id}/{assembly_id}"] = {
            "rcsb_id": f"{target.pdb_id}-{assembly_id}",
            "pdbx_struct_assembly": {"id": assembly_id, "oligomeric_count": 22},
            "rcsb_assembly_info": {
                "entry_id": target.pdb_id,
                "assembly_id": assembly_id,
                "polymer_entity_count": len(target.entities),
                "polymer_entity_instance_count": sum(
                    entity.molecule_count for entity in target.entities
                ),
            },
            "rcsb_struct_symmetry": [
                {"kind": "Global Symmetry", "stoichiometry": ["A10", "B3"]},
                {"kind": "Pseudo Symmetry", "stoichiometry": ["A10", "B6"]},
                {"kind": "Local Symmetry", "stoichiometry": ["A10"]},
                {"kind": "Local Symmetry", "stoichiometry": ["B3"]},
            ],
        }
    return result


def fetcher(values: dict[str, dict]):
    def fetch(url: str) -> dict:
        return values[url]

    return fetch


def test_exact_6oqr_canary_resolves_and_normalizes_without_flattening():
    target = rcsb.TARGETS[0]
    source = responses(target)
    entry, entities, assemblies = rcsb.resolve(target, fetch=fetcher(source))
    value = rcsb.normalize(target, entry, entities, assemblies)
    assert value["accession"] == "PDB:6OQR"
    assert value["dataset_type"] == "EXPERIMENTAL_STRUCTURE"
    assert value["repository"] == "RCSB_PDB"
    assert value["organism"].startswith("NCBITaxon:562 ")
    assert value["publication"] == "DOI:10.1038/s41467-020-16387-2"
    assert "3.1 Å" in value["findings"]
    assert "PMID:32457314" in value["notes"]
    assert "alternate stoichiometries intentionally remain unflattened" in value["notes"]
    assert "not ingested as an image or counted as a micrograph" in value["notes"]
    assert "sample_count" not in value
    assert "A10" not in str(value)
    for expected in target.entities:
        assert f"UniProtKB:{expected.uniprot_id}" in value["notes"]
        assert f"/polymer_entity/6OQR/{expected.entity_id}" in value["notes"]
    assert "/assembly/6OQR/1" in value["notes"]


def test_plan_requires_exact_source_taxon_before_any_api_request():
    target = rcsb.TARGETS[0]
    called = False

    def fetch(_url):
        nonlocal called
        called = True

    records = [(Path("atp.yaml"), {"identifier": target.record_id})]
    with pytest.raises(ValueError, match="NCBITaxon:562"):
        rcsb.plan(records, targets=(target,), fetch=fetch)
    assert called is False


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("entry_id", "identity or method"),
        ("method", "identity or method"),
        ("computed", "experimental structure"),
        ("resolution", "experimental structure"),
        ("citation", "primary citation"),
        ("entity_ids", "child identifiers"),
        ("uniprot", "linkage changed"),
        ("source_taxon", "source taxon changed"),
        ("assembly_id", "assembly 1 identity changed"),
        ("oligomeric_count", "oligomeric count changed"),
        ("instance_count", "assembly contract changed"),
        ("symmetry", "no alternate symmetry"),
    ],
)
def test_identity_provenance_entity_and_assembly_drift_fail_closed(mutation, message):
    target = rcsb.TARGETS[0]
    source = responses(target)
    entry_url = f"{rcsb.DATA_API}/entry/{target.pdb_id}"
    entity_url = f"{rcsb.DATA_API}/polymer_entity/{target.pdb_id}/1"
    assembly_url = f"{rcsb.DATA_API}/assembly/{target.pdb_id}/1"
    if mutation == "entry_id":
        source[entry_url]["rcsb_id"] = "6OQS"
    elif mutation == "method":
        source[entry_url]["exptl"] = [{"method": "X-RAY DIFFRACTION"}]
    elif mutation == "computed":
        source[entry_url]["rcsb_entry_info"]["structure_determination_methodology"] = "computational"
    elif mutation == "resolution":
        source[entry_url]["rcsb_entry_info"]["resolution_combined"] = [4.0]
    elif mutation == "citation":
        source[entry_url]["rcsb_primary_citation"]["pdbx_database_id_DOI"] = "10.0/drift"
    elif mutation == "entity_ids":
        source[entry_url]["rcsb_entry_container_identifiers"]["polymer_entity_ids"].pop()
    elif mutation == "uniprot":
        source[entity_url]["rcsb_polymer_entity_container_identifiers"]["uniprot_ids"] = []
    elif mutation == "source_taxon":
        source[entity_url]["rcsb_entity_source_organism"][0]["ncbi_taxonomy_id"] = 83333
    elif mutation == "assembly_id":
        source[assembly_url]["rcsb_id"] = "6OQR-2"
    elif mutation == "oligomeric_count":
        source[assembly_url]["pdbx_struct_assembly"]["oligomeric_count"] = 21
    elif mutation == "instance_count":
        source[assembly_url]["rcsb_assembly_info"]["polymer_entity_instance_count"] = 21
    else:
        source[assembly_url]["rcsb_struct_symmetry"] = [
            {"kind": "Global Symmetry", "stoichiometry": ["A10"]}
        ]
    with pytest.raises(ValueError, match=message):
        rcsb.resolve(target, fetch=fetcher(source))


def test_plan_is_idempotent_and_uses_exact_endpoint_urls_only():
    target = rcsb.TARGETS[0]
    source = responses(target)
    record = {
        "identifier": target.record_id,
        "canonical_examples": [{"taxon_id": "NCBITaxon:562"}],
    }
    planned = rcsb.plan([(Path("atp.yaml"), record)], fetch=fetcher(source))
    _path, _record, _target, value, action = planned[0]
    assert action == "added"
    record["datasets"] = [deepcopy(value)]
    planned = rcsb.plan([(Path("atp.yaml"), record)], fetch=fetcher(source))
    assert planned[0][-1] == "unchanged"
    expected_urls = {
        f"{rcsb.DATA_API}/entry/6OQR",
        f"{rcsb.DATA_API}/assembly/6OQR/1",
        *(f"{rcsb.DATA_API}/polymer_entity/6OQR/{i}" for i in range(1, 9)),
    }
    assert set(source) == expected_urls


@pytest.mark.parametrize(
    ("url_kind", "replacement", "message"),
    [
        ("entry", [], "entry response is not an object"),
        ("entity", [], "polymer entity 1 response is not an object"),
        ("sources", [None], "source organisms is not a list of objects"),
        ("symmetry", [None, {}], "symmetry annotations is not a list of objects"),
    ],
)
def test_malformed_api_shapes_fail_with_deterministic_refusal(url_kind, replacement, message):
    target = rcsb.TARGETS[0]
    source = responses(target)
    entry_url = f"{rcsb.DATA_API}/entry/{target.pdb_id}"
    entity_url = f"{rcsb.DATA_API}/polymer_entity/{target.pdb_id}/1"
    assembly_url = f"{rcsb.DATA_API}/assembly/{target.pdb_id}/1"
    if url_kind == "entry":
        source[entry_url] = replacement
    elif url_kind == "entity":
        source[entity_url] = replacement
    elif url_kind == "sources":
        source[entity_url]["rcsb_entity_source_organism"] = replacement
    else:
        source[assembly_url]["rcsb_struct_symmetry"] = replacement
    with pytest.raises(ValueError, match=message):
        rcsb.resolve(target, fetch=fetcher(source))
