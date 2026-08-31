#!/usr/bin/env python3
"""Import one verified Complex Portal composition assertion.

The importer only accepts an exact ``CPX-N`` accession and resolves it through
``complex-ws/complex/<accession>``. It never treats a search hit as an
equivalent xref: a 30S subunit may be relevant to the ribosome record without
being the whole ribosome. Taxon-specific participants live in
``complex_compositions`` rather than replacing taxon-agnostic ``components``.

Dry-run is the default. Example::

    python scripts/complex_portal.py --accession CPX-3802 \
      --record data/structures/ribonucleoprotein/ribosome.yaml \
      --taxon NCBITaxon:83333 \
      --scope-note "E. coli 30S subunit; not equivalent to the whole ribosome"
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from pathlib import Path

import yaml

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import get_json, require_record_taxon, upsert
from cellstructuremech.validation.write_validated import ValidationFailedError, write_validated_structure

API = "https://www.ebi.ac.uk/intact/complex-ws/complex"
ACCESSION = re.compile(r"^CPX-[0-9]+$")
STOICHIOMETRY = re.compile(
    r"^minValue:\s*([0-9]+(?:\.[0-9]+)?),\s*maxValue:\s*([0-9]+(?:\.[0-9]+)?)$"
)


def normalize_stoichiometry(value: str | None) -> str | None:
    if value is None:
        return None
    match = STOICHIOMETRY.fullmatch(value)
    if not match:
        raise ValueError(f"unrecognized Complex Portal stoichiometry: {value!r}")
    low, high = match.groups()
    return low if low == high else f"{low}-{high}"


def participant_curie(participant: dict) -> str:
    identifier = participant.get("identifier")
    if not identifier:
        raise ValueError("Complex Portal participant has no identifier")
    if ":" in identifier:
        return identifier
    if identifier.startswith("CPX-"):
        return f"ComplexPortal:{identifier}"
    if identifier.startswith("URS"):
        return f"RNAcentral:{identifier}"
    if participant.get("interactorType") == "protein":
        return f"UniProtKB:{identifier}"
    raise ValueError(
        f"cannot assign a CURIE prefix to {identifier!r} "
        f"({participant.get('interactorType')!r})"
    )


def normalize_participant(participant: dict) -> dict:
    entry = {
        "participant_id": participant_curie(participant),
        "label": participant.get("description") or participant.get("name") or participant["identifier"],
        "participant_type": participant.get("interactorType") or "unknown",
    }
    if participant.get("name"):
        entry["gene_symbol"] = participant["name"]
    stoichiometry = normalize_stoichiometry(participant.get("stochiometry"))
    if stoichiometry is not None:
        entry["stoichiometry"] = stoichiometry
    if participant.get("interactorAC"):
        entry["source_interactor_id"] = participant["interactorAC"]
    return entry


def normalize_entry(payload: dict, *, retrieved_on: str, scope_note: str) -> dict:
    accession = payload.get("complexAc")
    if not isinstance(accession, str) or not ACCESSION.fullmatch(accession):
        raise ValueError(f"source did not return a primary CPX accession: {accession!r}")
    species = payload.get("species", "")
    match = re.fullmatch(r"(.+);\s*([0-9]+)", species)
    if not match:
        raise ValueError(f"unrecognized Complex Portal species: {species!r}")
    taxon_label, taxon_number = match.groups()
    participants = [normalize_participant(item) for item in payload.get("participants") or []]
    if not participants:
        raise ValueError(f"{accession} has no participants")
    ids = [item["participant_id"] for item in participants]
    if len(ids) != len(set(ids)):
        raise ValueError(f"{accession} repeats a participant identifier; manual modeling is required")

    entry = {
        "composition_id": f"complex_portal_{accession.lower().replace('-', '_')}",
        "source": "COMPLEX_PORTAL",
        "source_accession": f"ComplexPortal:{accession}",
        "source_url": f"https://www.ebi.ac.uk/complexportal/complex/{accession}",
        "complex_label": payload.get("name") or accession,
        "taxon_id": f"NCBITaxon:{taxon_number}",
        "taxon_label": taxon_label.strip(),
    }
    assemblies = payload.get("complexAssemblies") or []
    if assemblies:
        entry["assembly"] = "; ".join(assemblies)
    evidence = payload.get("evidenceType") or {}
    if re.fullmatch(r"ECO:[0-9]+", evidence.get("identifier", "")):
        entry["evidence_code"] = evidence["identifier"]
    entry["participants"] = participants
    entry["retrieved_on"] = retrieved_on
    entry["notes"] = (
        f"Curator-scoped import: {scope_note}. Source evidence: "
        f"{evidence.get('description', 'not supplied')}. The accession was resolved through "
        "the Complex Portal accession endpoint; no equivalence xref was inferred."
    )
    return entry


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--accession", required=True)
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--taxon", required=True, help="Expected NCBITaxon:NNN from the source entry.")
    parser.add_argument(
        "--scope-note",
        required=True,
        help="How this source complex relates to the record; required to prevent silent equivalence claims.",
    )
    parser.add_argument("--apply", action="store_true", help="Write the record (default: dry run).")
    args = parser.parse_args()

    if not ACCESSION.fullmatch(args.accession):
        parser.error("--accession must be an exact CPX-N identifier")
    try:
        payload = get_json(f"{API}/{args.accession}")
        if payload.get("complexAc") != args.accession:
            raise ValueError(
                f"requested {args.accession}, accession endpoint returned {payload.get('complexAc')!r}"
            )
        entry = normalize_entry(
            payload, retrieved_on=datetime.date.today().isoformat(), scope_note=args.scope_note
        )
        if entry["taxon_id"] != args.taxon:
            raise ValueError(f"expected {args.taxon}, source entry is {entry['taxon_id']}")
        record = yaml.safe_load(args.record.read_text(encoding="utf-8"))
        require_record_taxon(record, entry["taxon_id"])
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"Complex Portal import refused: {exc}", file=sys.stderr)
        return 2

    compositions, action = upsert(
        record.get("complex_compositions"), "composition_id", entry
    )
    if not args.apply:
        print(f"# dry run — would have {action} this composition on {args.record}\n")
        print(yaml.safe_dump([entry], default_flow_style=False, sort_keys=False, allow_unicode=True))
        return 0

    record["complex_compositions"] = compositions
    record_curation_event(
        record,
        curator="complex_portal",
        action="ADD_EVIDENCE",
        llm_assisted=False,
        changes=(
            f"{action.capitalize()} taxon-specific composition {entry['source_accession']} "
            f"({len(entry['participants'])} participants); exact accession and taxon verified at import."
        ),
    )
    try:
        write_validated_structure(record, args.record)
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    print(f"{action} {entry['composition_id']} on {args.record}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
