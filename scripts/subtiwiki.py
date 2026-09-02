#!/usr/bin/env python3
"""Add a curator-reviewed set of SubtiWiki flagellar protein examples.

SubtiWiki does not publish database redistribution terms.  This adapter is
therefore deliberately CURATE_ONLY: it reads one exact category and exact
gene-outlink endpoints, then stores only identifiers and a source link.  It
never copies descriptions, sequences, phenotypes, interaction text, or a bulk
export.  Protein labels, reviewed status, and the strain taxon are verified
independently against UniProtKB.

The allow-list is biological review, not a search result.  Dry-run is the
default; pass ``--apply`` to write the validated record.

    python scripts/subtiwiki.py \
      --record data/structures/appendage/bacterial_type_flagellum.yaml
    python scripts/subtiwiki.py \
      --record data/structures/appendage/bacterial_type_flagellum.yaml --apply
"""

from __future__ import annotations

import argparse
import datetime
import re
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import get_json, upsert
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    write_validated_structure,
)

API = "https://www.subtiwiki.uni-goettingen.de/v5/api"
UNIPROT_API = "https://rest.uniprot.org/uniprotkb"
CATEGORY_ID = 387
CATEGORY_NAME = "Flagellar proteins"
CATEGORY_DOT_NOTATION = "4.1.1.2"
RECORD_ID = "GO:0009288"
TAXON_ID = "NCBITaxon:224308"
TAXON_NUMBER = 224308
TAXON_LABEL = "Bacillus subtilis subsp. subtilis str. 168"
SOURCE_PAPER = "DOI:10.1093/nar/gkae957"
UNIPROT_ACCESSION = re.compile(r"^[A-Z0-9]+$")


@dataclass(frozen=True)
class Target:
    component_id: str
    gene_id: int
    gene_symbol: str
    uniprot_gene_symbol: str | None = None
    role_reference: str | None = None


# Exact membership reviewed against category 387 on 2026-09-01.  Candidates
# that are assembly factors rather than constituents (FliI/H/J/K/T/W, FlgD/N)
# and Gram-negative-only L/P rings are intentionally absent.
TARGETS = (
    Target("flagellin", 3732, "hag"),
    # SubtiWiki retains the historical flgE name for locus BSU_16290;
    # UniProt's current primary symbol is flgG and identifies it as distal rod.
    Target("rod", 1713, "flgE", "flgG"),
    Target("ms_ring", 1705, "fliF"),
    Target("c_ring", 1706, "fliG"),
    Target("c_ring", 1716, "fliM"),
    Target("c_ring", 1717, "fliY", None, "DOI:10.1128/JB.00626-18"),
    Target("stator", 1444, "motA"),
    Target("stator", 1443, "motB"),
    # SubtiWiki uses the functional aliases motP/motS; UniProt retains ytxD/ytxE
    # as the primary symbols for the second, sodium-coupled stator pair.
    Target("stator", 3153, "motP", "ytxD", "DOI:10.1016/j.jmb.2005.07.030"),
    Target("stator", 3152, "motS", "ytxE", "DOI:10.1016/j.jmb.2005.07.030"),
    Target("rod", 1702, "flgB"),
    Target("rod", 1703, "flgC"),
    Target("export_apparatus", 1724, "flhA"),
    Target("export_apparatus", 1723, "flhB"),
    Target("export_apparatus", 1720, "fliP"),
    Target("export_apparatus", 1721, "fliQ"),
    Target("export_apparatus", 1722, "fliR"),
)


def unwrap(payload: dict, label: str) -> dict:
    if payload.get("code") != 200 or payload.get("isSuccess") is not True:
        raise ValueError(f"{label} request was not successful")
    data = payload.get("data")
    if not isinstance(data, dict):
        raise ValueError(f"{label} response has no object data")
    return data


def validate_category(payload: dict) -> None:
    data = unwrap(payload, "category")
    identity = (data.get("id"), data.get("name"), data.get("dot_notation"))
    expected = (CATEGORY_ID, CATEGORY_NAME, CATEGORY_DOT_NOTATION)
    if identity != expected:
        raise ValueError(f"category identity changed: expected {expected!r}, got {identity!r}")
    genes = data.get("genes")
    if not isinstance(genes, list):
        raise ValueError("category response has no gene list")
    observed = {(item.get("id"), item.get("name")) for item in genes}
    missing = [(target.gene_id, target.gene_symbol) for target in TARGETS
               if (target.gene_id, target.gene_symbol) not in observed]
    if missing:
        raise ValueError(f"curated category membership changed; missing {missing!r}")


def accession_from_outlink(payload: dict, target: Target) -> str:
    data = unwrap(payload, f"gene {target.gene_id} outlink")
    if data.get("gene_id") != target.gene_id:
        raise ValueError(
            f"gene outlink id changed: expected {target.gene_id}, got {data.get('gene_id')!r}"
        )
    accession = data.get("uniprot")
    if not isinstance(accession, str) or not UNIPROT_ACCESSION.fullmatch(accession):
        raise ValueError(f"gene {target.gene_symbol} has no valid UniProt accession")
    return accession


def normalize_example(
    target: Target, accession: str, uniprot: dict, component: dict, retrieved_on: str
) -> dict:
    if uniprot.get("primaryAccession") != accession:
        raise ValueError(
            f"UniProt accession mismatch for {target.gene_symbol}: "
            f"{uniprot.get('primaryAccession')!r}"
        )
    if uniprot.get("entryType") != "UniProtKB reviewed (Swiss-Prot)":
        raise ValueError(f"UniProtKB:{accession} is not reviewed")
    organism = uniprot.get("organism") or {}
    if organism.get("taxonId") != TAXON_NUMBER:
        raise ValueError(
            f"UniProtKB:{accession} has taxon {organism.get('taxonId')!r}, expected {TAXON_NUMBER}"
        )
    genes = uniprot.get("genes") or []
    primary_gene = (genes[0].get("geneName") or {}).get("value") if genes else None
    expected_gene = target.uniprot_gene_symbol or target.gene_symbol
    if primary_gene is None or primary_gene.casefold() != expected_gene.casefold():
        raise ValueError(
            f"UniProtKB:{accession} primary gene is {primary_gene!r}, "
            f"expected {expected_gene!r}"
        )
    description = uniprot.get("proteinDescription") or {}
    label = ((description.get("recommendedName") or {}).get("fullName") or {}).get("value")
    if not isinstance(label, str) or not label.strip():
        raise ValueError(f"UniProtKB:{accession} has no recommended protein name")

    source_url = f"https://www.subtiwiki.uni-goettingen.de/v5/gene/{target.gene_symbol}"
    evidence = [
        {
            "reference": source_url,
            "notes": (
                f"SubtiWiki category {CATEGORY_ID} lists {target.gene_symbol} among "
                f"B. subtilis flagellar proteins and links UniProtKB:{accession}"
                + (
                    f", whose current UniProt primary gene symbol is {expected_gene}."
                    if expected_gene != target.gene_symbol
                    else "."
                )
            ),
        }
    ]
    if target.role_reference:
        evidence.append(
            {
                "reference": target.role_reference,
                "notes": (
                    f"Independent experimental literature supports the curated placement of "
                    f"{target.gene_symbol} in the B. subtilis {component['label']} component."
                ),
            }
        )
    return {
        "uniprot_id": f"UniProtKB:{accession}",
        "protein_label": label,
        "gene_symbol": expected_gene,
        "taxon_id": TAXON_ID,
        "taxon_label": TAXON_LABEL,
        "entry_status": "REVIEWED",
        "retrieved_on": retrieved_on,
        "role": (
            f"Curator-mapped from SubtiWiki category {CATEGORY_ID} to the "
            f"{component['label']} component; identity and taxon independently verified in UniProtKB."
        ),
        "evidence": evidence,
    }


def ensure_record_contract(record: dict) -> dict[str, dict]:
    if record.get("identifier") != RECORD_ID:
        raise ValueError(f"adapter only accepts {RECORD_ID}, got {record.get('identifier')!r}")
    components = {item.get("component_id"): item for item in record.get("components") or []}
    required = {target.component_id for target in TARGETS}
    missing = sorted(required - components.keys())
    if missing:
        raise ValueError(f"record is missing curated components: {missing!r}")
    return components


def ensure_canonical_taxon(record: dict) -> bool:
    examples = record.setdefault("canonical_examples", [])
    existing = next((item for item in examples if item.get("taxon_id") == TAXON_ID), None)
    value = {
        "taxon_id": TAXON_ID,
        "taxon_label": TAXON_LABEL,
        "note": "SubtiWiki's reference strain and a classical genetic model for flagellar assembly.",
        "reference": SOURCE_PAPER,
    }
    if existing == value:
        return False
    if existing is not None:
        raise ValueError(
            f"record already has a different curated {TAXON_ID} canonical example; refusing overwrite"
        )
    record["canonical_examples"].append(value)
    return True


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", required=True, type=Path)
    parser.add_argument("--apply", action="store_true", help="Write the record (default: dry run).")
    args = parser.parse_args()

    try:
        record = yaml.safe_load(args.record.read_text(encoding="utf-8"))
        components = ensure_record_contract(record)
        taxon_changed = ensure_canonical_taxon(record)
        category = get_json(f"{API}/gene-category/{CATEGORY_ID}")
        validate_category(category)
        retrieved_on = datetime.date.today().isoformat()
        planned: list[tuple[Target, dict]] = []
        for target in TARGETS:
            outlink = get_json(f"{API}/gene/{target.gene_id}/outlinks")
            accession = accession_from_outlink(outlink, target)
            uniprot = get_json(f"{UNIPROT_API}/{accession}.json")
            example = normalize_example(
                target, accession, uniprot, components[target.component_id], retrieved_on
            )
            planned.append((target, example))
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"SubtiWiki import refused: {exc}", file=sys.stderr)
        return 2

    changes = 0
    for target, example in planned:
        component = components[target.component_id]
        current_examples = component.get("protein_examples") or []
        current = next(
            (item for item in current_examples if item.get("uniprot_id") == example["uniprot_id"]),
            None,
        )
        if current == example:
            print(
                f"{target.gene_symbol}\t{example['uniprot_id']}\t"
                f"{target.component_id}\tunchanged"
            )
            continue
        examples, action = upsert(
            current_examples, "uniprot_id", example
        )
        changes += 1
        component["protein_examples"] = examples
        print(
            f"{target.gene_symbol}\t{example['uniprot_id']}\t{target.component_id}\t{action}"
        )
    if not args.apply:
        print(
            f"\ndry run: {changes} protein example(s), "
            f"canonical taxon {'updated' if taxon_changed else 'unchanged'}; pass --apply"
        )
        return 0
    if not changes and not taxon_changed:
        print("nothing to write")
        return 0

    record_curation_event(
        record,
        curator="subtiwiki",
        action="SEED_PROTEIN_EXAMPLES",
        llm_assisted=False,
        changes=(
            f"Added or refreshed {changes} curator-reviewed B. subtilis flagellar protein "
            f"examples from SubtiWiki category {CATEGORY_ID}; exact gene ids and UniProt outlinks "
            "were checked at SubtiWiki, then reviewed status, gene identity and taxon were checked "
            "independently at UniProtKB. No SubtiWiki prose, sequences or bulk export was copied."
        ),
    )
    try:
        write_validated_structure(record, args.record)
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    print(f"wrote {changes} protein examples to {args.record}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
