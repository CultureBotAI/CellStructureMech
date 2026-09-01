#!/usr/bin/env python3
"""Add curator-reviewed MicrO identity xrefs to matching structure records.

MicrO is inactive and its scope mixes structures, whole cells, and qualities.
This adapter therefore does no label search and makes no inferred mappings. It
contains a deliberately small allow-list reviewed against the static source
release, then verifies each exact MicrO CURIE and label against OLS before
writing. Dry-run is the default.
"""

from __future__ import annotations

import argparse
import sys
import urllib.parse
from dataclasses import dataclass

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import get_json
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    write_validated_structure,
)

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records


OLS = "https://www.ebi.ac.uk/ols4/api/ontologies/micro/terms"


@dataclass(frozen=True)
class Mapping:
    record_id: str
    record_label: str
    micro_id: str
    micro_label: str


MAPPINGS = (
    Mapping("GO:0031411", "gas vesicle", "MICRO:0000214", "gas vacuole"),
    Mapping("GO:0110143", "magnetosome", "MICRO:0000216", "magnetosome"),
)


def term_url(curie: str) -> str:
    return OLS + "?" + urllib.parse.urlencode({"obo_id": curie})


def validate_term(payload: dict, mapping: Mapping) -> None:
    terms = (payload.get("_embedded") or {}).get("terms") or []
    if len(terms) != 1:
        raise ValueError(f"expected exactly one OLS term for {mapping.micro_id}; found {len(terms)}")
    term = terms[0]
    expected_iri = "http://purl.obolibrary.org/obo/" + mapping.micro_id.replace(":", "_")
    if (
        term.get("obo_id") != mapping.micro_id
        or term.get("iri") != expected_iri
        or term.get("ontology_name") != "micro"
        or term.get("label") != mapping.micro_label
        or term.get("is_obsolete") is not False
    ):
        raise ValueError(
            f"OLS term contract changed for {mapping.micro_id}: "
            f"id={term.get('obo_id')!r}, label={term.get('label')!r}, "
            f"ontology={term.get('ontology_name')!r}, obsolete={term.get('is_obsolete')!r}"
        )


def plan_xrefs(records, fetch=get_json):
    by_record = {mapping.record_id: mapping for mapping in MAPPINGS}
    plan = []
    for path, record in records:
        mapping = by_record.get(record.get("identifier"))
        if mapping is None or mapping.micro_id in (record.get("xrefs") or []):
            continue
        if record.get("label") != mapping.record_label:
            raise ValueError(
                f"record label changed for {mapping.record_id}: "
                f"expected {mapping.record_label!r}, found {record.get('label')!r}"
            )
        validate_term(fetch(term_url(mapping.micro_id)), mapping)
        plan.append((path, record, mapping))
    return plan


def run(*, apply: bool) -> int:
    plan = plan_xrefs(load_records())
    for path, record, mapping in plan:
        print(
            f"{path.relative_to(REPO_ROOT)}: {record['identifier']} ({record['label']}) "
            f"-> {mapping.micro_id} ({mapping.micro_label})"
        )
    if not plan:
        print("nothing to add")
        return 0
    if not apply:
        print(f"\ndry run: {len(plan)} curated xref(s) would be added; pass --apply")
        return 0

    for path, record, mapping in plan:
        record.setdefault("xrefs", []).append(mapping.micro_id)
        record_curation_event(
            record,
            curator="micro_xrefs",
            action="ADD_XREF",
            llm_assisted=False,
            changes=(
                f"Added {mapping.micro_id} ({mapping.micro_label}) as a curator-reviewed "
                "identity xref; exact non-obsolete MicrO id and label verified through OLS."
            ),
        )
        try:
            write_validated_structure(record, path)
        except ValidationFailedError as exc:
            print(exc.summary(), file=sys.stderr)
            return 1
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write records (default: dry run).")
    args = parser.parse_args()
    try:
        return run(apply=args.apply)
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"MicrO xref import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
