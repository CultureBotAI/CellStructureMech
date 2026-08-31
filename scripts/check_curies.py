#!/usr/bin/env python3
"""Resolve every identifier in the corpus against the authority that issued it.

The dominant defect in this repository is a **pattern-valid identifier that
does not exist**. Four reached pull requests before something caught them: a
ComplexPortal accession (#2), a DOI pointing at a different paper (#4), a
download URL with tracking parameters (#34), and `CHEBI:50290`, which resolves
to sapphyrin PCI-2052 rather than magnetite (#62).

`validate_id_label_correspondence.py` closes part of this: it checks
`(grounding, label)` pairs against OAK for the handful of OBO ontologies with a
sqlite adapter. It says nothing about the 221 DOIs, 68 UniProt accessions, 66
taxon ids or 52 PMIDs in the corpus — the great majority of its identifiers.
This resolves all of them (#6).

Every check is a live lookup against the issuing authority, batched where the
API allows and cached under ``build/curie_cache.json`` so a re-run is nearly
free. A cache entry older than ``--max-age`` days is re-fetched; an identifier
is never trusted because it was fine once.

    python scripts/check_curies.py                 # resolve, print a summary
    python scripts/check_curies.py --check         # exit 1 on any unresolvable id
    python scripts/check_curies.py --report reports/curie_check.tsv
    python scripts/check_curies.py --offline       # cache only, no network

Prefixes with no resolver are reported as SKIPPED, never as OK: `traitmech:`
and `METPO:` live in a sibling repository (#11) and `cellstructuremech:` is
minted here.
"""

from __future__ import annotations

import argparse
import csv
import json
import re
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from collections import defaultdict
from datetime import date, datetime, timedelta
from pathlib import Path

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records

CACHE_PATH = REPO_ROOT / "build" / "curie_cache.json"
UA = {"User-Agent": "CellStructureMech/0.1 (mailto:noreply@anthropic.com; "
                    "https://github.com/CultureBotAI/CellStructureMech)"}
CURIE = re.compile(r"^[A-Za-z][A-Za-z0-9._-]*:\S+$")

# Prefixes we can resolve, and where. Anything else is SKIPPED with a reason.
OLS_ONTOLOGY = {"GO": "go", "CHEBI": "chebi", "SO": "so", "RO": "ro", "BFO": "bfo",
                "UO": "uo", "PATO": "pato", "NCBITaxon": "ncbitaxon", "MICRO": "micro",
                "NCIT": "ncit"}
NO_RESOLVER = {
    "traitmech": "sibling repository; covered by the cross-repo trait check (#11)",
    "METPO": "sibling ontology, not in the OLS set used here (#11)",
    "proteintraitsmech": "sibling repository",
    "cellstructuremech": "minted in this repository",
    "biolink": "model slot, not an ontology term",
    "rdfs": "RDF vocabulary",
    "dcterms": "Dublin Core vocabulary",
}


def _get(url: str, timeout: float = 30.0) -> tuple[int, bytes]:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as e:
        return e.code, b""
    except Exception:  # noqa: BLE001 — a transport failure is not a verdict
        return 0, b""


# ------------------------------------------------------------------ collect


def collect(records) -> dict[str, set[str]]:
    """Every CURIE-shaped string in the corpus, by prefix, with where it came from."""
    found: dict[str, set[str]] = defaultdict(set)

    def walk(node):
        if isinstance(node, dict):
            for value in node.values():
                walk(value)
        elif isinstance(node, list):
            for item in node:
                walk(item)
        elif isinstance(node, str) and CURIE.match(node) and not node.startswith(("http://", "https://")):
            found[node.split(":", 1)[0]].add(node)

    for _, doc in records:
        walk(doc)
    return found


# ------------------------------------------------------------------ resolvers


def _ols_search(curie: str) -> tuple[str, str] | None:
    """Global OLS search by exact obo_id. Some ontologies (RO, BFO) 404 on the
    per-ontology term endpoint but are indexed here."""
    url = ("https://www.ebi.ac.uk/ols4/api/search?exact=true&queryFields=obo_id&rows=5&q="
           + urllib.parse.quote(curie))
    status, body = _get(url)
    if status != 200:
        return None
    for doc in json.loads(body).get("response", {}).get("docs", []):
        if doc.get("obo_id") == curie:
            return ("OK", doc.get("label", ""))
    return None


def resolve_ols(curies: list[str]) -> dict[str, tuple[str, str]]:
    """OLS4 per-ontology lookup, falling back to the global index."""
    out = {}
    for curie in curies:
        onto = OLS_ONTOLOGY[curie.split(":", 1)[0]]
        url = (f"https://www.ebi.ac.uk/ols4/api/ontologies/{onto}/terms?obo_id="
               + urllib.parse.quote(curie))
        status, body = _get(url)
        terms = json.loads(body).get("_embedded", {}).get("terms", []) if status == 200 else []
        if terms:
            term = terms[0]
            out[curie] = ("OBSOLETE", term.get("label", "")) if term.get("is_obsolete") \
                else ("OK", term.get("label", ""))
            continue
        if (hit := _ols_search(curie)) is not None:
            out[curie] = hit
        elif status not in (200, 404):
            out[curie] = ("UNREACHABLE", f"OLS returned {status}")
        else:
            out[curie] = ("NOT_FOUND", f"no such term in {onto} or the OLS index")
    return out


def resolve_doi(curies: list[str]) -> dict[str, tuple[str, str]]:
    out = {}
    for curie in curies:
        doi = curie.split(":", 1)[1]
        status, body = _get("https://api.crossref.org/works/" + urllib.parse.quote(doi))
        if status == 200:
            msg = json.loads(body).get("message", {})
            out[curie] = ("OK", (msg.get("title") or [""])[0][:90])
        else:
            # Not every DOI is a Crossref DOI: data repositories (CaltechDATA,
            # Zenodo, Dryad) register with DataCite, so a Crossref-only check
            # calls a perfectly good DOI missing (#81).
            dstatus, dbody = _get("https://api.datacite.org/dois/"
                                  + urllib.parse.quote(doi, safe=""))
            if dstatus == 200:
                attrs = json.loads(dbody).get("data", {}).get("attributes", {})
                titles = attrs.get("titles") or [{}]
                out[curie] = ("OK", (titles[0].get("title") or "")[:90])
            elif status == 404 and dstatus == 404:
                out[curie] = ("NOT_FOUND", "neither Crossref nor DataCite has this DOI")
            else:
                out[curie] = ("UNREACHABLE", f"Crossref {status}, DataCite {dstatus}")
        time.sleep(0.3)  # a modest rate, even on the polite pool
    return out


def resolve_pmid(curies: list[str]) -> dict[str, tuple[str, str]]:
    """NCBI esummary takes a batch, which keeps this to one request."""
    if not curies:
        return {}
    ids = [c.split(":", 1)[1] for c in curies]
    url = ("https://eutils.ncbi.nlm.nih.gov/entrez/eutils/esummary.fcgi?db=pubmed&retmode=json&id="
           + ",".join(ids))
    status, body = _get(url)
    if status != 200:
        return {c: ("UNREACHABLE", f"eutils returned {status}") for c in curies}
    result = json.loads(body).get("result", {})
    out = {}
    for curie, pmid in zip(curies, ids, strict=True):
        entry = result.get(pmid)
        if not entry or "error" in entry:
            out[curie] = ("NOT_FOUND", "PubMed has no such record")
        else:
            out[curie] = ("OK", (entry.get("title") or "")[:90])
    return out


def resolve_uniprot(curies: list[str]) -> dict[str, tuple[str, str]]:
    """UniProt resolves a batch of accessions in one request."""
    out = {}
    for start in range(0, len(curies), 100):
        chunk = curies[start:start + 100]
        accs = [c.split(":", 1)[1] for c in chunk]
        url = ("https://rest.uniprot.org/uniprotkb/accessions?format=json&fields=accession,id&accessions="
               + ",".join(accs))
        status, body = _get(url)
        if status != 200:
            out.update({c: ("UNREACHABLE", f"UniProt returned {status}") for c in chunk})
            continue
        got = {r["primaryAccession"] for r in json.loads(body).get("results", [])}
        for curie, acc in zip(chunk, accs, strict=True):
            out[curie] = ("OK", "") if acc in got else ("NOT_FOUND", "no such UniProtKB accession")
    return out


def resolve_interpro(curies: list[str]) -> dict[str, tuple[str, str]]:
    out = {}
    for curie in curies:
        acc = curie.split(":", 1)[1]
        status, body = _get(f"https://www.ebi.ac.uk/interpro/api/entry/interpro/{acc}")
        # InterPro answers an unknown accession with 204 No Content, not 404, so
        # a resolver keyed on 404 calls it a transport failure and lets it
        # through. The control caught this (#82).
        if status in (204, 404) or (status == 200 and not body.strip()):
            out[curie] = ("NOT_FOUND", "no such InterPro entry")
        elif status != 200:
            out[curie] = ("UNREACHABLE", f"InterPro returned {status}")
        else:
            out[curie] = ("OK", json.loads(body)["metadata"]["name"]["name"][:90])
    return out


def resolve_complexportal(curies: list[str]) -> dict[str, tuple[str, str]]:
    out = {}
    for curie in curies:
        acc = curie.split(":", 1)[1]
        # `details/{ac}` 404s for every accession, including ones the service's
        # own search returns, so it cannot distinguish a bad id from a good one
        # (#81). Exact-match the search index instead: a fabricated accession
        # returns zero elements.
        status, body = _get("https://www.ebi.ac.uk/intact/complex-ws/search/"
                            + urllib.parse.quote(acc))
        if status != 200:
            out[curie] = ("UNREACHABLE", f"Complex Portal returned {status}")
            continue
        elements = json.loads(body).get("elements", []) if body.strip() else []
        hit = next((e for e in elements if e.get("complexAC") == acc), None)
        out[curie] = ("OK", (hit.get("complexName") or "")[:90]) if hit \
            else ("NOT_FOUND", "no such Complex Portal accession")
    return out


def resolve_uniprot_location(curies: list[str]) -> dict[str, tuple[str, str]]:
    """SL ids come from the vendored subcell.txt, so this needs no network."""
    try:
        from uniprot_sl import load_subcell
    except ImportError:
        from scripts.uniprot_sl import load_subcell
    try:
        known = {hit["sl"]: hit["name"] for hit in load_subcell().values()}
    except Exception as exc:  # noqa: BLE001
        return {c: ("UNREACHABLE", f"subcell.txt unavailable: {exc}") for c in curies}
    return {c: (("OK", known[c.split(':', 1)[1]]) if c.split(":", 1)[1] in known
                else ("NOT_FOUND", "no such UniProt subcellular-location id"))
            for c in curies}


def resolve_obo_purl(curies: list[str]) -> dict[str, tuple[str, str]]:
    """Relation prefixes resolve at the OBO PURL, not through the OLS term index.

    BFO and RO relations are indexed by OLS as *properties* of `ro`, so
    `ontologies/bfo/terms?obo_id=` 404s for every one of them, and the global
    search finds a BFO relation only when some other ontology happens to import
    it — `BFO:0000050` (part of) is not found at all, while `BFO:0000066` is
    found three times over with the label `BFO_0000066` (#84). The PURL is the
    identifier's canonical location and answers 404 for a fabricated one.
    """
    out = {}
    for curie in curies:
        prefix, local = curie.split(":", 1)
        url = f"http://purl.obolibrary.org/obo/{prefix}_{local}"
        try:
            request = urllib.request.Request(url, headers=UA, method="HEAD")
            with urllib.request.urlopen(request, timeout=30) as response:
                out[curie] = ("OK", response.geturl()[:90]) if response.status == 200 \
                    else ("UNREACHABLE", f"PURL returned {response.status}")
        except urllib.error.HTTPError as exc:
            out[curie] = ("NOT_FOUND", "no such OBO term") if exc.code == 404 \
                else ("UNREACHABLE", f"PURL returned {exc.code}")
        except Exception as exc:  # noqa: BLE001
            out[curie] = ("UNREACHABLE", f"{type(exc).__name__}: {exc}")
    return out


RESOLVERS = {
    "DOI": resolve_doi,
    "PMID": resolve_pmid,
    "UniProtKB": resolve_uniprot,
    "InterPro": resolve_interpro,
    "ComplexPortal": resolve_complexportal,
    "uniprot.location": resolve_uniprot_location,
    # BFO only: the RO PURL namespace redirects a fabricated id to a generic
    # OLS page and answers 200, so it is not an authority for RO. RO resolves
    # correctly through the OLS global index, which returns no hit for a
    # fabricated id. The control is what separates these two cases (#84).
    "BFO": resolve_obo_purl,
}


# ------------------------------------------------------------------ control

# Each resolver is exercised against an identifier known to exist and one known
# not to, before its verdicts about the corpus are believed. Without this a
# resolver pointed at a retired endpoint reports every identifier as missing —
# which is exactly what the first version of this script did (#82).
CONTROLS: dict[str, tuple[str, str]] = {
    # One per OLS ontology in use, not one for OLS: the ontologies are indexed
    # separately, so a control on GO says nothing about NCBI Taxonomy (#84).
    "GO": ("GO:0005840", "GO:9999999"),
    "CHEBI": ("CHEBI:46726", "CHEBI:99999999"),
    "SO": ("SO:0000650", "SO:9999999"),
    "RO": ("RO:0002327", "RO:9999999"),        # via the OLS global index
    "BFO": ("BFO:0000050", "BFO:9999999"),     # via the OBO PURL
    "UO": ("UO:0000018", "UO:9999999"),
    "PATO": ("PATO:0000051", "PATO:9999999"),
    "NCBITaxon": ("NCBITaxon:83333", "NCBITaxon:999999999"),
    "DOI": ("DOI:10.1038/nrmicro.2018.10", "DOI:10.9999/not-a-real-doi-zzq"),
    "PMID": ("PMID:17518518", "PMID:999999999"),
    "UniProtKB": ("UniProtKB:Q03511", "UniProtKB:X0X0X0"),
    "InterPro": ("InterPro:IPR001119", "InterPro:IPR999999"),
    "ComplexPortal": ("ComplexPortal:CPX-2244", "ComplexPortal:CPX-9999999"),
    "uniprot.location": ("uniprot.location:SL-0034", "uniprot.location:SL-9999"),
}
# A DataCite DOI as well: data repositories do not register with Crossref, and a
# Crossref-only resolver silently calls those missing (#82).
DATACITE_CONTROL = "DOI:10.22002/D1.1355"


def self_test() -> list[str]:
    """Return a list of failures; empty means every resolver is trustworthy."""
    failures = []
    for prefix, (good, bad) in sorted(CONTROLS.items()):
        resolver = RESOLVERS.get(prefix) or resolve_ols
        verdicts = resolver([good, bad])
        if verdicts.get(good, ("", ""))[0] != "OK":
            failures.append(f"{prefix}: known-good {good} did not resolve "
                            f"({verdicts.get(good, ('MISSING', ''))[0]}) — the resolver is broken, "
                            f"not the corpus")
        if verdicts.get(bad, ("", ""))[0] != "NOT_FOUND":
            failures.append(f"{prefix}: known-bad {bad} was not rejected "
                            f"({verdicts.get(bad, ('MISSING', ''))[0]}) — the resolver would pass anything")
    dc = resolve_doi([DATACITE_CONTROL]).get(DATACITE_CONTROL, ("MISSING", ""))
    if dc[0] != "OK":
        failures.append(f"DOI: DataCite control {DATACITE_CONTROL} did not resolve ({dc[0]})")
    return failures


# ------------------------------------------------------------------ cache


def load_cache() -> dict:
    if CACHE_PATH.exists():
        try:
            return json.loads(CACHE_PATH.read_text())
        except json.JSONDecodeError:
            return {}
    return {}


def save_cache(cache: dict) -> None:
    CACHE_PATH.parent.mkdir(parents=True, exist_ok=True)
    CACHE_PATH.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")


def fresh(entry: dict, max_age_days: int) -> bool:
    try:
        checked = datetime.fromisoformat(entry["checked_on"]).date()
    except (KeyError, ValueError):
        return False
    # An UNREACHABLE verdict is a transport failure, not an answer: never cache it.
    return entry.get("verdict") != "UNREACHABLE" and date.today() - checked <= timedelta(days=max_age_days)


# ------------------------------------------------------------------ main


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--check", action="store_true",
                        help="Exit 1 if any identifier is NOT_FOUND or OBSOLETE.")
    parser.add_argument("--report", type=Path, help="Write a TSV of every verdict here.")
    parser.add_argument("--max-age", type=int, default=30, help="Re-check a cached id older than N days.")
    parser.add_argument("--offline", action="store_true", help="Use the cache only; do not fetch.")
    parser.add_argument("--refresh", action="store_true", help="Ignore the cache and re-resolve everything.")
    parser.add_argument("--self-test", action="store_true",
                        help="Only exercise each resolver against a known-good and known-bad id.")
    args = parser.parse_args()

    if args.self_test or (args.check and not args.offline):
        failures = self_test()
        if failures:
            print("resolver control FAILED — verdicts about the corpus are not trustworthy:",
                  file=sys.stderr)
            for line in failures:
                print(f"  {line}", file=sys.stderr)
            return 2
        print("resolver control: every resolver accepts a known id and rejects a fabricated one",
              file=sys.stderr)
        if args.self_test:
            return 0

    records = load_records()
    found = collect(records)
    # A gate that finds nothing must not report success: if data/structures/
    # moves or the loader breaks, "every identifier resolves" would be true and
    # meaningless (#87).
    if not records:
        print("no records found — the corpus path or loader is wrong, not the corpus", file=sys.stderr)
        return 2
    if not found:
        print(f"{len(records)} record(s) but no identifiers found — the collector is not seeing "
              "the fields it should", file=sys.stderr)
        return 2
    cache = {} if args.refresh else load_cache()
    verdicts: dict[str, tuple[str, str]] = {}
    to_fetch: dict[str, list[str]] = defaultdict(list)

    for prefix, curies in sorted(found.items()):
        for curie in sorted(curies):
            if prefix in NO_RESOLVER:
                verdicts[curie] = ("SKIPPED", NO_RESOLVER[prefix])
            elif (entry := cache.get(curie)) and fresh(entry, args.max_age):
                verdicts[curie] = (entry["verdict"], entry.get("detail", ""))
            elif prefix in RESOLVERS or prefix in OLS_ONTOLOGY:
                to_fetch[prefix].append(curie)
            else:
                verdicts[curie] = ("SKIPPED", f"no resolver for the {prefix}: prefix")

    if args.offline:
        for curies in to_fetch.values():
            for curie in curies:
                verdicts[curie] = ("SKIPPED", "not cached and --offline")
    else:
        for prefix, curies in sorted(to_fetch.items()):
            print(f"resolving {len(curies)} {prefix} identifier(s)...", file=sys.stderr)
            resolver = RESOLVERS.get(prefix) or resolve_ols
            got = resolver(curies)
            verdicts.update(got)
            for curie, (verdict, detail) in got.items():
                cache[curie] = {"verdict": verdict, "detail": detail, "checked_on": date.today().isoformat()}
        save_cache(cache)

    by_verdict: dict[str, int] = defaultdict(int)
    for verdict, _ in verdicts.values():
        by_verdict[verdict] += 1

    if args.report:
        args.report.parent.mkdir(parents=True, exist_ok=True)
        with args.report.open("w", newline="", encoding="utf-8") as fh:
            writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
            writer.writerow(["identifier", "prefix", "verdict", "detail"])
            for curie in sorted(verdicts):
                verdict, detail = verdicts[curie]
                writer.writerow([curie, curie.split(":", 1)[0], verdict, detail])

    print("\nidentifier liveness summary:")
    for verdict in sorted(by_verdict, key=lambda v: -by_verdict[v]):
        print(f"  {verdict:14s} {by_verdict[verdict]:4d}")

    bad = {c: v for c, v in verdicts.items() if v[0] in {"NOT_FOUND", "OBSOLETE"}}
    unreachable = {c: v for c, v in verdicts.items() if v[0] == "UNREACHABLE"}
    if unreachable:
        print(f"\n{len(unreachable)} identifier(s) could not be reached — a transport failure, not a "
              f"verdict; they are not cached and will be retried:", file=sys.stderr)
        for curie, (_, detail) in sorted(unreachable.items())[:10]:
            print(f"  {curie}: {detail}", file=sys.stderr)
    if bad:
        print(f"\n{len(bad)} identifier(s) do not resolve:", file=sys.stderr)
        for curie, (verdict, detail) in sorted(bad.items()):
            print(f"  {verdict}: {curie} — {detail}", file=sys.stderr)
        if args.check:
            return 1
    elif args.check:
        print("\nEvery identifier resolves at its issuing authority.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
