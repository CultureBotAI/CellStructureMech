#!/usr/bin/env python3
"""Ingest a fixed, curator-reviewed ePSORTdb experimental protein canary.

PSORTdb's v4 download is currently mislabeled: the URL and HTTP content type
say TSV, but its bytes are a Safari WebArchive containing an HTML ``pre``
wrapper around the table.  This adapter makes that defect an explicit,
fail-closed contract.  It pins the artifact hash, validates the plist resource
metadata and HTML envelope, then selects one exact experimental row.

PSORTdb's database-data licence is not stated precisely.  Per maintainer
direction, the source is integrated as CURATE_ONLY: only third-party
identifiers, source links and evidence metadata are stored.  The selected
protein's identity, reviewed status, gene and taxon are independently checked
at UniProtKB, and its PMID is independently resolved at NCBI.  cPSORTdb
predictions are never read.  Dry-run is the default; pass ``--apply`` to write.
"""

from __future__ import annotations

import argparse
import csv
import hashlib
import io
import plistlib
import sys
from dataclasses import dataclass
from pathlib import Path

import yaml

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import get_bytes, get_json, upsert
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    write_validated_structure,
)

try:
    from corpus import REPO_ROOT
except ImportError:
    from scripts.corpus import REPO_ROOT


DOWNLOAD_URL = "https://db.psort.org/static/downloads/Experimental-PSORTdb-v4.00.tsv"
SEARCH_URL = "https://db.psort.org/search/results?dataset=e&refseq=P14016&show_adjust=1"
UNIPROT_URL = "https://rest.uniprot.org/uniprotkb/P14016.json"
PUBMED_URL = (
    "https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi"
    "?db=pubmed&id=3139490&retmode=json"
)
EXPECTED_SHA256 = "4c4d28b3adde281b19465a850786529a400412aed5dc57679c0fd264d444db01"
EXPECTED_ROW_COUNT = 11781
RETRIEVED_ON = "2026-09-02"
RECORD_PATH = (
    REPO_ROOT / "data" / "structures" / "spore"
    / "endospore_external_encapsulating_structure.yaml"
)
HTML_PREFIX = (
    '<html><head></head><body><pre style="word-wrap: break-word; '
    'white-space: pre-wrap;">'
)
HTML_SUFFIX = "</pre></body></html>"
EXPECTED_COLUMNS = (
    "SwissProt_ID",
    "Refseq_Accession",
    "Other_Accession",
    "Experimental_Localization",
    "Secondary_Localization",
    "MultipleSCL",
    "ProteinName",
    "AltProteinName",
    "GeneName",
    "TaxID",
    "Organism",
    "Phylum",
    "Class",
    "GramStain",
    "Comments",
    "PMID",
    "RefSummary",
    "ePSORTdbVersion",
)


@dataclass(frozen=True)
class Target:
    record_id: str
    component_id: str
    accession: str
    gene_symbol: str
    protein_name: str
    taxon_id: int
    taxon_label: str
    pmid: int
    pubmed_title: str
    experimental_localization: str
    secondary_localization: str
    source_version: str


TARGET = Target(
    record_id="GO:0043591",
    component_id="coat",
    accession="P14016",
    gene_symbol="cotE",
    protein_name="Spore coat protein E",
    taxon_id=224308,
    taxon_label="Bacillus subtilis subsp. subtilis str. 168",
    pmid=3139490,
    pubmed_title=(
        "Gene encoding a morphogenic protein required in the assembly of the outer "
        "coat of the Bacillus subtilis endospore."
    ),
    experimental_localization="Extracellular",
    secondary_localization="Spore outer coat",
    source_version="3.00",
)


def parse_download(
    payload: bytes,
    expected_sha256: str = EXPECTED_SHA256,
    expected_row_count: int = EXPECTED_ROW_COUNT,
) -> list[dict]:
    actual_sha256 = hashlib.sha256(payload).hexdigest()
    if actual_sha256 != expected_sha256:
        raise ValueError(
            f"PSORTdb artifact SHA-256 changed: expected {expected_sha256}, got {actual_sha256}"
        )
    try:
        archive = plistlib.loads(payload)
    except plistlib.InvalidFileException as exc:
        raise ValueError("PSORTdb artifact is no longer a valid WebArchive plist") from exc
    if not isinstance(archive, dict):
        raise ValueError("PSORTdb WebArchive root is not an object")
    resource = archive.get("WebMainResource")
    if not isinstance(resource, dict):
        raise ValueError("PSORTdb WebArchive has no main resource object")
    expected_resource = {
        "WebResourceURL": DOWNLOAD_URL,
        "WebResourceMIMEType": "text/tab-separated-values",
        "WebResourceTextEncodingName": "UTF-8",
    }
    changed = {
        key: (expected, resource.get(key))
        for key, expected in expected_resource.items()
        if resource.get(key) != expected
    }
    if changed:
        raise ValueError(f"PSORTdb WebArchive resource contract changed: {changed!r}")
    data = resource.get("WebResourceData")
    if not isinstance(data, bytes):
        raise ValueError("PSORTdb WebArchive main resource has no byte payload")
    try:
        wrapped = data.decode("utf-8")
    except UnicodeDecodeError as exc:
        raise ValueError("PSORTdb embedded table is not UTF-8") from exc
    if not wrapped.startswith(HTML_PREFIX) or not wrapped.endswith(HTML_SUFFIX):
        raise ValueError("PSORTdb embedded table HTML envelope changed")
    table = wrapped[len(HTML_PREFIX) : -len(HTML_SUFFIX)]
    reader = csv.DictReader(io.StringIO(table), delimiter="\t")
    if tuple(reader.fieldnames or ()) != EXPECTED_COLUMNS:
        raise ValueError(f"PSORTdb table columns changed: {reader.fieldnames!r}")
    rows = list(reader)
    if len(rows) != expected_row_count:
        raise ValueError(
            f"PSORTdb table row count changed: expected {expected_row_count}, got {len(rows)}"
        )
    return rows


def select_target(rows: list[dict], target: Target = TARGET) -> dict:
    matches = [row for row in rows if row.get("SwissProt_ID") == target.accession]
    if len(matches) != 1:
        raise ValueError(
            f"expected one exact ePSORTdb row for {target.accession}; got {len(matches)}"
        )
    row = matches[0]
    expected = {
        "Refseq_Accession": "",
        "Other_Accession": "",
        "Experimental_Localization": target.experimental_localization,
        "Secondary_Localization": target.secondary_localization,
        "MultipleSCL": "0",
        "ProteinName": target.protein_name,
        "GeneName": target.gene_symbol,
        "TaxID": str(target.taxon_id),
        "Organism": target.taxon_label,
        "PMID": str(target.pmid),
        "ePSORTdbVersion": target.source_version,
    }
    changed = {
        key: (value, row.get(key))
        for key, value in expected.items()
        if row.get(key) != value
    }
    if changed:
        raise ValueError(f"ePSORTdb {target.accession} canary changed: {changed!r}")
    return row


def validate_uniprot(payload: dict, target: Target = TARGET) -> str:
    if not isinstance(payload, dict):
        raise ValueError("UniProt response is not an object")
    if payload.get("primaryAccession") != target.accession:
        raise ValueError("UniProt accession identity changed")
    if payload.get("entryType") != "UniProtKB reviewed (Swiss-Prot)":
        raise ValueError(f"UniProtKB:{target.accession} is not reviewed")
    organism = payload.get("organism") or {}
    if not isinstance(organism, dict) or organism.get("taxonId") != target.taxon_id:
        raise ValueError(f"UniProtKB:{target.accession} taxon changed")
    genes = payload.get("genes") or []
    primary_gene = (
        ((genes[0].get("geneName") or {}).get("value"))
        if isinstance(genes, list) and genes and isinstance(genes[0], dict)
        else None
    )
    if primary_gene != target.gene_symbol:
        raise ValueError(f"UniProtKB:{target.accession} primary gene changed")
    description = payload.get("proteinDescription") or {}
    if not isinstance(description, dict):
        raise ValueError(f"UniProtKB:{target.accession} protein description changed")
    recommended_name = description.get("recommendedName") or {}
    if not isinstance(recommended_name, dict):
        raise ValueError(f"UniProtKB:{target.accession} recommended name changed")
    recommended = recommended_name.get("fullName") or {}
    if not isinstance(recommended, dict):
        raise ValueError(f"UniProtKB:{target.accession} recommended name changed")
    label = recommended.get("value")
    if label != "Spore coat morphogenetic protein CotE":
        raise ValueError(f"UniProtKB:{target.accession} recommended name changed")
    return label


def validate_pubmed(payload: dict, target: Target = TARGET) -> None:
    if not isinstance(payload, dict):
        raise ValueError("PubMed response is not an object")
    result = payload.get("result")
    item = result.get(str(target.pmid)) if isinstance(result, dict) else None
    if not isinstance(item, dict):
        raise ValueError(f"PMID:{target.pmid} did not resolve")
    if item.get("uid") != str(target.pmid) or item.get("title") != target.pubmed_title:
        raise ValueError(f"PMID:{target.pmid} identity or title changed")


def ensure_record(record: dict, target: Target = TARGET) -> dict:
    if record.get("identifier") != target.record_id:
        raise ValueError(f"adapter only accepts {target.record_id}")
    components = {
        component.get("component_id"): component
        for component in record.get("components") or []
        if isinstance(component, dict)
    }
    component = components.get(target.component_id)
    if not isinstance(component, dict):
        raise ValueError(f"record is missing component {target.component_id}")
    if target.gene_symbol not in (component.get("gene_symbols") or []):
        raise ValueError(
            f"component {target.component_id} does not already assert {target.gene_symbol}"
        )
    return component


def ensure_canonical_taxon(record: dict, target: Target = TARGET) -> bool:
    examples = record.setdefault("canonical_examples", [])
    value = {
        "taxon_id": f"NCBITaxon:{target.taxon_id}",
        "taxon_label": target.taxon_label,
        "note": "Experimental reference strain for CotE-dependent outer spore-coat assembly.",
        "reference": f"PMID:{target.pmid}",
    }
    existing = next(
        (item for item in examples if item.get("taxon_id") == value["taxon_id"]), None
    )
    if existing == value:
        return False
    if existing is not None:
        raise ValueError(f"record has conflicting {value['taxon_id']} canonical-example content")
    examples.append(value)
    return True


def normalize_example(label: str, target: Target = TARGET) -> dict:
    return {
        "uniprot_id": f"UniProtKB:{target.accession}",
        "protein_label": label,
        "gene_symbol": target.gene_symbol,
        "taxon_id": f"NCBITaxon:{target.taxon_id}",
        "taxon_label": target.taxon_label,
        "entry_status": "REVIEWED",
        "retrieved_on": RETRIEVED_ON,
        "role": (
            f"Exact ePSORTdb experimental canary: {target.accession} is assigned to "
            f"{target.secondary_localization}; current protein identity and taxon were "
            "independently verified in UniProtKB."
        ),
        "evidence": [
            {
                "reference": SEARCH_URL,
                "notes": (
                    f"The exact ePSORTdb result links {target.accession} ({target.protein_name}) "
                    f"from taxon {target.taxon_id} to secondary localization "
                    f"'{target.secondary_localization}' and PMID:{target.pmid}."
                ),
            },
            {
                "reference": f"PMID:{target.pmid}",
                "notes": (
                    "Zheng et al. identify CotE as a morphogenetic protein required to "
                    "assemble the outer Bacillus subtilis endospore coat."
                ),
            },
        ],
    }


def plan(
    record: dict,
    *,
    fetch_bytes=get_bytes,
    fetch_json=get_json,
    target: Target = TARGET,
) -> tuple[dict, bool, str]:
    component = ensure_record(record, target)
    rows = parse_download(fetch_bytes(DOWNLOAD_URL))
    select_target(rows, target)
    label = validate_uniprot(fetch_json(UNIPROT_URL), target)
    validate_pubmed(fetch_json(PUBMED_URL), target)
    value = normalize_example(label, target)
    # Do not mutate the caller-owned document until every external contract has
    # passed.  This matters to library callers even though the CLI never writes
    # a failed plan.
    taxon_changed = ensure_canonical_taxon(record, target)
    current_examples = component.get("protein_examples") or []
    current = next(
        (item for item in current_examples if item.get("uniprot_id") == value["uniprot_id"]),
        None,
    )
    if current == value:
        action = "unchanged"
    else:
        examples, action = upsert(current_examples, "uniprot_id", value)
        component["protein_examples"] = examples
    return value, taxon_changed, action


def run(record_path: Path, *, apply: bool) -> int:
    record = yaml.safe_load(record_path.read_text(encoding="utf-8"))
    value, taxon_changed, action = plan(record)
    print(
        f"{record_path.relative_to(REPO_ROOT)}\t{value['uniprot_id']}\t"
        f"{TARGET.component_id}\t{action}"
    )
    changed = action != "unchanged" or taxon_changed
    if not changed:
        print("nothing to write")
        return 0
    if not apply:
        print(
            f"\ndry run: protein example {action}; canonical taxon "
            f"{'added' if taxon_changed else 'unchanged'}; pass --apply"
        )
        return 0
    record_curation_event(
        record,
        curator="psortdb",
        action="SEED_PROTEIN_EXAMPLE",
        llm_assisted=True,
        changes=(
            "Added exact ePSORTdb experimental P14016/CotE spore-outer-coat example "
            "with PMID:3139490; validated the pinned WebArchive-wrapped v4 artifact, "
            "then independently verified reviewed protein identity, gene and strain taxon "
            "at UniProtKB and the PMID at NCBI. Source licensing responsibility was "
            "accepted by the maintainer; no cPSORTdb predictions or bulk prose were stored."
        ),
    )
    try:
        write_validated_structure(record, record_path)
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    print(f"wrote {value['uniprot_id']} to {record_path}")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--record", type=Path, default=RECORD_PATH)
    parser.add_argument("--apply", action="store_true", help="Write the record (default: dry run).")
    args = parser.parse_args()
    try:
        return run(args.record, apply=args.apply)
    except (OSError, KeyError, TypeError, ValueError, plistlib.InvalidFileException) as exc:
        print(f"PSORTdb import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
