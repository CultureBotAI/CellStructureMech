#!/usr/bin/env python3
"""UniProt Subcellular Location as a source (docs/SOURCE_QUEUE.md #3, issue #28).

Two things the SL vocabulary gives a CellStructureRecord:

* an ``xrefs`` entry ``uniprot.location:SL-NNNN`` — every SL term carries the
  GO CC id it corresponds to, so the mapping is read from ``subcell.txt``, not
  guessed;
* taxon-paired ``protein_examples`` on the record's components — reviewed
  UniProtKB entries annotated with the location in one of the record's
  canonical taxa, matched to a component by gene symbol, and carrying the
  ``ECO:0000269`` (experimental) PubMed evidence UniProt attaches to that
  localisation. Entries with no experimental citation, or with no
  unambiguous component, are reported but not written.

Dry-run by default; ``--apply`` writes through the validation gate and appends
a CurationEvent. Licence: CC BY 4.0 (footer of subcell.txt).

**Not every structure has an SL term, and that is left alone.** ``GO:0005840``
ribosome has none: UniProt classifies ribosomal proteins by keyword
(``KW-0689 Ribonucleoprotein``) rather than by subcellular location. Extending
this script to a keyword route was considered and declined (#42) — a keyword is
a *classification*, not a localisation, so the ``ECO:0000269``-per-localisation
evidence that makes these examples worth having does not transfer. The ribosome
gets its membership from Complex Portal instead (``CPX-3802`` 30S with 22
participants, ``CPX-3807`` 50S with 36), which states subunit composition
directly and carries CC BY terms.

    python scripts/uniprot_sl.py xrefs                       # dry run, all records
    python scripts/uniprot_sl.py xrefs --apply
    python scripts/uniprot_sl.py proteins --record data/structures/microcompartment/carboxysome.yaml
    python scripts/uniprot_sl.py proteins --record ... --taxon 1140 --apply
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

try:  # run as `python scripts/uniprot_sl.py` (scripts/ on sys.path) ...
    from corpus import REPO_ROOT, load_records
except ImportError:  # ... or imported by the tests as scripts.uniprot_sl
    from scripts.corpus import REPO_ROOT, load_records

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.validation.write_validated import ValidationFailedError, write_validated_structure

UA = {"User-Agent": "CellStructureMech/0.1 (https://github.com/CultureBotAI/CellStructureMech; curation bot)"}
SUBCELL_URL = "https://ftp.uniprot.org/pub/databases/uniprot/current_release/knowledgebase/complete/docs/subcell.txt"
REST = "https://rest.uniprot.org/uniprotkb/search"
CACHE = REPO_ROOT / "build" / "subcell.txt"
MAX_EVIDENCE = 3


def _get(url: str) -> bytes:
    with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=120) as r:
        return r.read()


def load_subcell(refresh: bool = False) -> dict[str, dict]:
    """GO CC id -> {sl, name, definition} parsed from subcell.txt (cached under build/)."""
    if refresh or not CACHE.exists():
        CACHE.parent.mkdir(parents=True, exist_ok=True)
        CACHE.write_bytes(_get(SUBCELL_URL))
    go_to_sl: dict[str, dict] = {}
    cur: dict = {}
    for line in CACHE.read_text(encoding="utf-8").splitlines():
        code, _, rest = line.partition("   ")
        rest = rest.strip()
        if code == "ID":
            cur = {"name": rest.rstrip(".")}
        elif code == "AC":
            cur["sl"] = rest
        elif code == "DE":
            cur["definition"] = (cur.get("definition", "") + " " + rest).strip()
        elif code == "GO":
            go_id = rest.split(";")[0].strip()
            go_to_sl[go_id] = dict(cur)
        elif code == "//":
            cur = {}
    return go_to_sl


# ---------------------------------------------------------------- xrefs


def plan_xrefs(records, go_to_sl):
    plan = []
    for path, doc in records:
        hit = go_to_sl.get(doc["identifier"])
        if not hit:
            continue
        curie = f"uniprot.location:{hit['sl']}"
        if curie in (doc.get("xrefs") or []):
            continue
        plan.append((path, doc, curie, hit["name"]))
    return plan


def cmd_xrefs(args) -> int:
    go_to_sl = load_subcell(args.refresh)
    plan = plan_xrefs(load_records(), go_to_sl)
    for path, doc, curie, name in plan:
        print(f"{path.relative_to(REPO_ROOT)}: {doc['identifier']} -> {curie} ({name})")
    if not plan:
        print("nothing to add")
        return 0
    if not args.apply:
        print(f"\ndry run: {len(plan)} xref(s) would be added; pass --apply")
        return 0
    for path, doc, curie, name in plan:
        doc.setdefault("xrefs", []).append(curie)
        record_curation_event(
            doc, curator="uniprot_sl", action="ADD_UNIPROT_SL_XREF", llm_assisted=False,
            changes=f"Added {curie} ({name}); mapping read from the GO line of UniProt subcell.txt.",
        )
        _write(doc, path)
    return 0


# ------------------------------------------------------------- proteins


def fetch_members(sl: str, taxon: int) -> list[dict]:
    q = f"(cc_scl_term:{sl}) AND (reviewed:true) AND (organism_id:{taxon})"
    url = REST + "?" + urllib.parse.urlencode({
        "query": q, "format": "json", "size": 500,
        "fields": "accession,gene_primary,protein_name,organism_name,organism_id,"
                  "cc_subcellular_location,reviewed",
    })
    return json.loads(_get(url)).get("results", [])


def localisation_pmids(entry: dict, sl: str) -> list[str]:
    pmids = []
    for c in entry.get("comments", []):
        if c.get("commentType") != "SUBCELLULAR LOCATION":
            continue
        for loc in c.get("subcellularLocations", []):
            if loc.get("location", {}).get("id") != sl:
                continue
            for ev in loc["location"].get("evidences", []):
                if ev.get("evidenceCode") == "ECO:0000269" and ev.get("source") == "PubMed":
                    pmids.append(ev["id"])
    return list(dict.fromkeys(pmids))


def match_component(doc: dict, gene: str | None) -> tuple[dict | None, str]:
    """A component whose gene_symbols contain the gene or a prefix of it (ccmK -> ccmK2)."""
    if not gene:
        return None, "no gene symbol"
    g = gene.lower()
    hits = [c for c in doc.get("components") or []
            if any(g == s.lower() or g.startswith(s.lower()) for s in c.get("gene_symbols") or [])]
    if len(hits) == 1:
        return hits[0], "ok"
    return None, "no matching component" if not hits else f"ambiguous: {[h['component_id'] for h in hits]}"


def plan_proteins(doc: dict, sl: str, taxon_id: int, taxon_label: str, today: str):
    rows = []
    for e in fetch_members(sl, taxon_id):
        acc = e["primaryAccession"]
        gene = (e.get("genes") or [{}])[0].get("geneName", {}).get("value")
        desc = e.get("proteinDescription", {})
        name = desc.get("recommendedName", {}).get("fullName", {}).get("value") or acc
        pmids = localisation_pmids(e, sl)
        comp, why = match_component(doc, gene)
        status = why if comp is None else ("ok" if pmids else "no ECO:0000269 PubMed evidence")
        example = None
        if status == "ok":
            already = {p["uniprot_id"] for p in comp.get("protein_examples") or []}
            if f"UniProtKB:{acc}" in already:
                status = "already present"
            else:
                example = {
                    "uniprot_id": f"UniProtKB:{acc}", "protein_label": name, "gene_symbol": gene,
                    "taxon_id": f"NCBITaxon:{taxon_id}", "taxon_label": taxon_label,
                    "entry_status": "REVIEWED", "retrieved_on": today,
                    "role": f"UniProt annotates this protein to {sl} ({doc['label']}); component role: "
                            f"{comp.get('role') or comp['label']}",
                    "evidence": [{"reference": f"PMID:{p}",
                                  "notes": f"ECO:0000269 experimental evidence for the {doc['label']} "
                                           f"localisation of {acc}, as cited by UniProt."}
                                 for p in pmids[:MAX_EVIDENCE]],
                }
        rows.append((acc, gene, name, comp["component_id"] if comp else "", len(pmids), status, example))
    return rows


def cmd_proteins(args) -> int:
    go_to_sl = load_subcell(args.refresh)
    path = Path(args.record).resolve()
    doc = yaml.safe_load(path.read_text(encoding="utf-8"))
    hit = go_to_sl.get(doc["identifier"])
    if not hit:
        print(f"{doc['identifier']} has no UniProt SL term in subcell.txt", file=sys.stderr)
        return 2
    sl = hit["sl"]
    taxa = [(t["taxon_id"], t["taxon_label"]) for t in doc.get("canonical_examples") or []]
    if args.taxon:
        taxa = [t for t in taxa if t[0] == f"NCBITaxon:{args.taxon}"]
        if not taxa:
            print(f"NCBITaxon:{args.taxon} is not a canonical example on this record; add it first "
                  "(image/protein taxa must be named on the record)", file=sys.stderr)
            return 2
    today = datetime.date.today().isoformat()
    added = 0
    for taxon_curie, taxon_label in taxa:
        taxon_id = int(taxon_curie.split(":")[1])
        rows = plan_proteins(doc, sl, taxon_id, taxon_label, today)
        print(f"\n{sl} x {taxon_label} (NCBITaxon:{taxon_id}): {len(rows)} reviewed entries")
        print("accession\tgene\tcomponent\tpmids\tstatus\tname")
        for acc, gene, name, comp_id, n, status, example in rows:
            print(f"{acc}\t{gene}\t{comp_id}\t{n}\t{status}\t{name}")
            if example and args.apply:
                comp = next(c for c in doc["components"] if c["component_id"] == comp_id)
                comp.setdefault("protein_examples", []).append(example)
                added += 1
    if not args.apply:
        print("\ndry run; pass --apply to write the rows marked ok")
        return 0
    if added:
        record_curation_event(
            doc, curator="uniprot_sl", action="SEED_PROTEIN_EXAMPLES", llm_assisted=False,
            changes=f"Added {added} taxon-paired protein example(s) from UniProtKB reviewed entries "
                    f"annotated to "
                    f"{sl} ({hit['name']}), matched to components by gene symbol, each carrying UniProt's "
                    f"ECO:0000269 PubMed evidence for the localisation.",
        )
        _write(doc, path)
        print(f"\nwrote {added} protein example(s) to {path.relative_to(REPO_ROOT)}")
    else:
        print("\nnothing to write")
    return 0


def _write(doc: dict, path: Path) -> None:
    try:
        write_validated_structure(doc, path)
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        raise SystemExit(1) from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--refresh", action="store_true", help="Re-download subcell.txt into build/.")
    sub = parser.add_subparsers(dest="cmd", required=True)
    x = sub.add_parser("xrefs", help="Add uniprot.location xrefs to GO-grounded records.")
    x.add_argument("--apply", action="store_true")
    x.set_defaults(func=cmd_xrefs)
    p = sub.add_parser("proteins", help="Seed components.protein_examples for one record.")
    p.add_argument("--record", required=True)
    p.add_argument("--taxon", type=int, help="Restrict to one canonical taxon id.")
    p.add_argument("--apply", action="store_true")
    p.set_defaults(func=cmd_proteins)
    args = parser.parse_args()
    return args.func(args)


if __name__ == "__main__":
    sys.exit(main())
