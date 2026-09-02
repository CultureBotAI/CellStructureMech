#!/usr/bin/env python3
"""Ingest fixed, curator-reviewed RCSB PDB experimental structures.

The adapter resolves exact PDB entry, polymer-entity and biological-assembly
identifiers through the official RCSB Data API.  It stores lightweight
metadata and links only.  Alternate assembly symmetry/stoichiometry
annotations are checked but deliberately left at RCSB rather than flattened
into the source-neutral Dataset model.  RCSB molecular renders are not images
or micrographs for this corpus.  Dry-run is the default; pass ``--apply`` to
write validated records.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import get_json, require_record_taxon, upsert
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    write_validated_structure,
)

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records


DATA_API = "https://data.rcsb.org/rest/v1/core"
PORTAL = "https://www.rcsb.org/structure"
CC0_POLICY = "https://www.rcsb.org/pages/usage-policy"


@dataclass(frozen=True)
class Entity:
    entity_id: str
    uniprot_id: str
    description: str
    molecule_count: int


@dataclass(frozen=True)
class Target:
    record_id: str
    pdb_id: str
    title: str
    taxon_id: int
    organism_name: str
    doi: str
    pubmed_id: int
    method: str
    reconstruction_method: str
    resolution: float
    emdb_id: str
    assembly_ids: tuple[str, ...]
    entities: tuple[Entity, ...]


TARGETS = (
    Target(
        record_id="GO:0045259",
        pdb_id="6OQR",
        title="E. coli ATP Synthase ADP State 1a",
        taxon_id=562,
        organism_name="Escherichia coli",
        doi="10.1038/s41467-020-16387-2",
        pubmed_id=32457314,
        method="ELECTRON MICROSCOPY",
        reconstruction_method="SINGLE PARTICLE",
        resolution=3.1,
        emdb_id="EMD-20167",
        assembly_ids=("1",),
        entities=(
            Entity("1", "P0ABA4", "ATP synthase subunit delta", 1),
            Entity("2", "P0ABB0", "ATP synthase subunit alpha", 3),
            Entity("3", "P0ABA0", "ATP synthase subunit b", 2),
            Entity("4", "P0A6E6", "ATP synthase epsilon chain", 1),
            Entity("5", "P0ABA6", "ATP synthase gamma chain", 1),
            Entity("6", "P0ABB4", "ATP synthase subunit beta", 3),
            Entity("7", "P68699", "ATP synthase subunit c", 10),
            Entity("8", "P0AB98", "ATP synthase subunit a", 1),
        ),
    ),
)


def _changed(actual: dict, expected: dict) -> dict:
    return {
        key: (value, actual.get(key))
        for key, value in expected.items()
        if actual.get(key) != value
    }


def _object(value: object, label: str) -> dict:
    if not isinstance(value, dict):
        raise ValueError(f"PDB {label} is not an object")
    return value


def _objects(value: object, label: str) -> list[dict]:
    if not isinstance(value, list) or not all(isinstance(item, dict) for item in value):
        raise ValueError(f"PDB {label} is not a list of objects")
    return value


def resolve(target: Target, fetch=get_json) -> tuple[dict, list[dict], list[dict]]:
    """Resolve one exact entry and its explicitly enumerated child resources."""
    entry = _object(fetch(f"{DATA_API}/entry/{target.pdb_id}"), "entry response")
    ids = _object(entry.get("rcsb_entry_container_identifiers"), "entry identifiers")
    info = _object(entry.get("rcsb_entry_info"), "entry information")
    citation = _object(entry.get("rcsb_primary_citation"), "primary citation")
    accession = _object(entry.get("rcsb_accession_info"), "accession information")
    expected_entry = {
        "rcsb_id": target.pdb_id,
        "exptl": [{"method": target.method}],
    }
    changed = _changed(entry, expected_entry)
    if changed:
        raise ValueError(f"PDB entry identity or method contract changed: {changed!r}")
    entry_identity = _object(entry.get("entry"), "entry identity")
    structure = _object(entry.get("struct"), "structure metadata")
    if entry_identity.get("id") != target.pdb_id or structure.get("title") != target.title:
        raise ValueError("PDB entry identity or title contract changed")
    expected_ids = {
        "entry_id": target.pdb_id,
        "rcsb_id": target.pdb_id,
        "assembly_ids": list(target.assembly_ids),
        "polymer_entity_ids": [entity.entity_id for entity in target.entities],
        "pubmed_id": target.pubmed_id,
        "emdb_ids": [target.emdb_id],
    }
    changed = _changed(ids, expected_ids)
    if changed:
        raise ValueError(f"PDB entry child identifiers changed: {changed!r}")
    expected_info = {
        "experimental_method": "EM",
        "structure_determination_methodology": "experimental",
        "resolution_combined": [target.resolution],
        "polymer_entity_count": len(target.entities),
        "polymer_entity_count_protein": len(target.entities),
    }
    changed = _changed(info, expected_info)
    if changed:
        raise ValueError(f"PDB experimental structure contract changed: {changed!r}")
    experiment = _object(entry.get("em_experiment"), "EM experiment")
    if experiment.get("reconstruction_method") != target.reconstruction_method:
        raise ValueError("PDB reconstruction method changed")
    reconstructions = _objects(entry.get("em_3d_reconstruction"), "EM reconstructions")
    if len(reconstructions) != 1:
        raise ValueError("PDB EM resolution is missing or ambiguous")
    if reconstructions[0].get("resolution") != target.resolution:
        raise ValueError("PDB EM resolution changed")
    expected_citation = {
        "pdbx_database_id_DOI": target.doi,
        "pdbx_database_id_PubMed": target.pubmed_id,
    }
    changed = _changed(citation, expected_citation)
    if changed:
        raise ValueError(f"PDB primary citation changed: {changed!r}")
    if accession.get("status_code") != "REL" or (
        accession.get("has_released_experimental_data") != "Y"
    ):
        raise ValueError("PDB entry is not a released experimental-data record")

    entities = []
    for expected in target.entities:
        entity = _object(
            fetch(f"{DATA_API}/polymer_entity/{target.pdb_id}/{expected.entity_id}"),
            f"polymer entity {expected.entity_id} response",
        )
        container = _object(
            entity.get("rcsb_polymer_entity_container_identifiers"),
            f"polymer entity {expected.entity_id} identifiers",
        )
        polymer = _object(
            entity.get("rcsb_polymer_entity"),
            f"polymer entity {expected.entity_id} metadata",
        )
        expected_entity = {
            "rcsb_id": f"{target.pdb_id}_{expected.entity_id}",
        }
        changed = _changed(entity, expected_entity)
        if changed:
            raise ValueError(f"PDB polymer entity identity changed: {changed!r}")
        expected_container = {
            "entity_id": expected.entity_id,
            "uniprot_ids": [expected.uniprot_id],
        }
        changed = _changed(container, expected_container)
        if changed:
            raise ValueError(
                f"PDB polymer entity {expected.entity_id} linkage changed: {changed!r}"
            )
        expected_polymer = {
            "pdbx_description": expected.description,
            "pdbx_number_of_molecules": expected.molecule_count,
        }
        changed = _changed(polymer, expected_polymer)
        if changed:
            raise ValueError(
                f"PDB polymer entity {expected.entity_id} metadata changed: {changed!r}"
            )
        sources = _objects(
            entity.get("rcsb_entity_source_organism"),
            f"polymer entity {expected.entity_id} source organisms",
        )
        source_taxa = {source.get("ncbi_taxonomy_id") for source in sources}
        if source_taxa != {target.taxon_id}:
            raise ValueError(
                f"PDB polymer entity {expected.entity_id} source taxon changed: "
                f"{source_taxa!r}"
            )
        entities.append(entity)

    assemblies = []
    for assembly_id in target.assembly_ids:
        assembly = _object(
            fetch(f"{DATA_API}/assembly/{target.pdb_id}/{assembly_id}"),
            f"biological assembly {assembly_id} response",
        )
        assembly_def = _object(
            assembly.get("pdbx_struct_assembly"),
            f"biological assembly {assembly_id} definition",
        )
        assembly_info = _object(
            assembly.get("rcsb_assembly_info"),
            f"biological assembly {assembly_id} information",
        )
        if assembly.get("rcsb_id") != f"{target.pdb_id}-{assembly_id}" or (
            assembly_def.get("id") != assembly_id
        ):
            raise ValueError(f"PDB biological assembly {assembly_id} identity changed")
        expected_assembly_info = {
            "entry_id": target.pdb_id,
            "assembly_id": assembly_id,
            "polymer_entity_count": len(target.entities),
            "polymer_entity_instance_count": sum(
                entity.molecule_count for entity in target.entities
            ),
        }
        changed = _changed(assembly_info, expected_assembly_info)
        if changed:
            raise ValueError(f"PDB biological assembly contract changed: {changed!r}")
        expected_oligomeric_count = sum(entity.molecule_count for entity in target.entities)
        if assembly_def.get("oligomeric_count") != expected_oligomeric_count:
            raise ValueError("PDB biological assembly oligomeric count changed")
        symmetries = _objects(
            assembly.get("rcsb_struct_symmetry"),
            f"biological assembly {assembly_id} symmetry annotations",
        )
        if len(symmetries) < 2:
            raise ValueError("PDB assembly has no alternate symmetry annotations to retain")
        kinds = {item.get("kind") for item in symmetries}
        if kinds != {"Global Symmetry", "Pseudo Symmetry", "Local Symmetry"}:
            raise ValueError(f"PDB assembly symmetry kinds changed: {kinds!r}")
        stoichiometries = {
            tuple(item.get("stoichiometry") or ())
            for item in symmetries
        }
        if len(stoichiometries) < 2:
            raise ValueError("PDB assembly alternate stoichiometries became indistinguishable")
        assemblies.append(assembly)
    return entry, entities, assemblies


def normalize(target: Target, entry: dict, entities: list[dict], assemblies: list[dict]) -> dict:
    accession = entry["rcsb_accession_info"]
    entity_links = []
    for expected in target.entities:
        url = f"{DATA_API}/polymer_entity/{target.pdb_id}/{expected.entity_id}"
        entity_links.append(
            f"{target.pdb_id}_{expected.entity_id} ({expected.description}) = "
            f"UniProtKB:{expected.uniprot_id} [{url}]"
        )
    assembly_notes = []
    for assembly_id, assembly in zip(target.assembly_ids, assemblies, strict=True):
        symmetries = assembly["rcsb_struct_symmetry"]
        kinds = sorted({item["kind"] for item in symmetries})
        url = f"{DATA_API}/assembly/{target.pdb_id}/{assembly_id}"
        assembly_notes.append(
            f"assembly {assembly_id} has {len(symmetries)} RCSB symmetry annotations "
            f"({', '.join(kinds)}); alternate stoichiometries intentionally remain "
            f"unflattened at [{url}]"
        )
    notes = (
        f"RCSB polymer entity links: {'; '.join(entity_links)}. "
        f"Biological assembly provenance: {'; '.join(assembly_notes)}. "
        f"Deposited {accession.get('deposit_date')}; released "
        f"{accession.get('initial_release_date')}; revised {accession.get('revision_date')}; "
        f"primary PMID:{target.pubmed_id}; associated {target.emdb_id}. "
        f"PDB archive and API data are CC0 ({CC0_POLICY}). Metadata-only ingest: "
        "the RCSB molecular render is not ingested as an image or counted as a micrograph."
    )
    return {
        "accession": f"PDB:{target.pdb_id}",
        "title": target.title,
        "description": (
            f"Experimental atomic model of {target.organism_name} F1Fo ATP synthase "
            "in ADP state 1a."
        ),
        "organism": f"NCBITaxon:{target.taxon_id} {target.organism_name}",
        "dataset_type": "EXPERIMENTAL_STRUCTURE",
        "repository": "RCSB_PDB",
        "sample_types": ["recombinant protein complex"],
        "platform": "single-particle cryo-electron microscopy",
        "url": f"{PORTAL}/{target.pdb_id}",
        "publication": f"DOI:{target.doi}",
        "findings": (
            f"Released experimental {target.method.lower()} structure at "
            f"{target.resolution:.1f} Å resolution, with {len(entities)} protein entities "
            "linked to exact UniProt accessions."
        ),
        "evidence": [
            {
                "reference": f"DOI:{target.doi}",
                "supports": "SUPPORT",
                "evidence_source": "publication",
                "explanation": "Primary publication associated with the exact RCSB PDB entry.",
            }
        ],
        "notes": notes,
    }


def plan(records, targets=TARGETS, fetch=get_json):
    records_by_id = {record.get("identifier"): (path, record) for path, record in records}
    planned = []
    for target in targets:
        if target.record_id not in records_by_id:
            raise ValueError(f"target record is missing: {target.record_id}")
        path, record = records_by_id[target.record_id]
        require_record_taxon(record, f"NCBITaxon:{target.taxon_id}")
        entry, entities, assemblies = resolve(target, fetch=fetch)
        value = normalize(target, entry, entities, assemblies)
        existing = next(
            (item for item in record.get("datasets") or [] if item.get("url") == value["url"]),
            None,
        )
        action = "unchanged" if existing == value else ("updated" if existing else "added")
        planned.append((path, record, target, value, action))
    return planned


def run(*, apply: bool) -> int:
    planned = plan(load_records())
    changed = [item for item in planned if item[-1] != "unchanged"]
    for path, _record, target, _value, action in planned:
        print(f"{path.relative_to(REPO_ROOT)}\tPDB:{target.pdb_id}\t{action}")
    if not changed:
        print("nothing to write")
        return 0
    if not apply:
        print(f"\ndry run: {len(changed)} dataset reference(s) would be written; pass --apply")
        return 0

    for path, record, target, value, _action in changed:
        record["datasets"], _ = upsert(record.get("datasets"), "url", value)
        record_curation_event(
            record,
            curator="rcsb_pdb",
            action="ADD_STRUCTURAL_DATASET",
            llm_assisted=True,
            changes=(
                f"Added exact RCSB PDB:{target.pdb_id} experimental-structure metadata; "
                "required the record's pre-existing exact NCBI source taxon, retained DOI/PMID, "
                "method, resolution and polymer-entity links, and left alternate assembly "
                "stoichiometries unflattened at RCSB. No molecular render was ingested."
            ),
        )
        try:
            write_validated_structure(record, path)
        except ValidationFailedError as exc:
            print(exc.summary(), file=sys.stderr)
            return 1
    print(f"wrote {len(changed)} dataset reference(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write records (default: dry run).")
    args = parser.parse_args()
    try:
        return run(apply=args.apply)
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"RCSB PDB import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
