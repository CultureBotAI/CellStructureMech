#!/usr/bin/env python3
"""Scaffold a new CellStructureRecord through the validation gate.

Dry-run by default: prints the YAML that would be written. Pass --apply to
write it. Refuses to overwrite an existing file or reuse an identifier.

    python scripts/new_record.py --category APPENDAGE --identifier GO:0009288 \
        --label "bacterial-type flagellum" --kind APPENDAGE --curator jane --apply
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path

from corpus import load_records, record_path

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    emit_structure_yaml,
    write_validated_structure,
)


def build_doc(args: argparse.Namespace) -> dict:
    doc: dict = {
        "identifier": args.identifier,
        "label": args.label,
        "structure_category": args.category,
    }
    if args.kind:
        doc["structure_kind"] = args.kind
    if args.definition:
        doc["definition"] = args.definition
    if args.definition_source:
        doc["definition_source"] = args.definition_source
    doc["mapping_status"] = "PROPOSED"
    record_curation_event(
        doc,
        curator=args.curator,
        action="CREATED_RECORD",
        changes="Scaffolded by scripts/new_record.py",
        llm_assisted=args.llm_assisted,
    )
    return doc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--identifier", required=True, help="GO:... or cellstructuremech:...")
    parser.add_argument("--label", required=True)
    parser.add_argument("--category", required=True, help="StructureCategoryEnum value")
    parser.add_argument("--kind", help="StructureKindEnum value")
    parser.add_argument("--definition")
    parser.add_argument("--definition-source")
    parser.add_argument("--curator", default="unknown")
    parser.add_argument("--llm-assisted", action="store_true")
    parser.add_argument("--apply", action="store_true", help="Write the file (default: dry run).")
    args = parser.parse_args()

    doc = build_doc(args)
    path: Path = record_path(args.category, args.label)

    taken = {d["identifier"]: p for p, d in load_records()}
    if args.identifier in taken:
        print(f"identifier {args.identifier} already used by {taken[args.identifier]}", file=sys.stderr)
        return 2
    if path.exists():
        print(f"refusing to overwrite {path}", file=sys.stderr)
        return 2

    if not args.apply:
        print(f"# dry run — would write {path}\n")
        print(emit_structure_yaml(doc))
        return 0
    try:
        write_validated_structure(doc, path)
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    print(f"wrote {path}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
