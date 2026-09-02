#!/usr/bin/env python3
"""Read the literature this corpus cites, and hold its evidence to it.

Every evidence item names a reference. Until now nothing read those references:
`check_curies.py` asks whether a DOI or PMID *exists*, never what it says, so
the corpus reached 344 evidence items with 0 verbatim snippets (#133) and one
claim that its own cited source contradicts.

Three modes, in the order they are useful:

``--audit`` (default)
    For every distinct reference, establish what can actually be read: open
    full text, abstract only, or nothing. Writes reports/evidence_readability.tsv.
    A claim with no snippet *and* no readable source is a claim nobody can
    check, and this makes those countable.

``--suggest --record PATH``
    Print candidate sentences from the readable text for each evidence item on
    that record, ranked by overlap with the claim the item is attached to. A
    curator picks; the tool never picks, because choosing which sentence
    supports a claim is the judgement the evidence exists to record.

``--verify``
    Every existing ``snippet`` must occur verbatim in the source's own text.
    This is the anti-fabrication gate: a quotation that is not in the paper is
    the worst defect this corpus can carry, and it is the one thing here that
    can be checked mechanically.

**Readability is established by trying, not by asking.** NCBI's ID converter
knows only PMC, so a paper absent from PMC looks absent from PubMed too — that
is how a real PMID (21047262) was recorded as "no PubMed record" (#133). Europe
PMC's `inEPMC` flag is no better: it says Y for PMC5433867, whose fullTextXML
404s. Every route is probed and the verdict is what came back.

    python scripts/fetch_snippets.py --audit
    python scripts/fetch_snippets.py --suggest --record data/structures/cytoskeleton/mreb_filament.yaml
    python scripts/fetch_snippets.py --verify
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
from datetime import date
from pathlib import Path

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records

UA = {"User-Agent": "CellStructureMech/0.1 (mailto:noreply@anthropic.com; "
                    "https://github.com/CultureBotAI/CellStructureMech)"}
CACHE_DIR = REPO_ROOT / "build" / "literature"
IDMAP_PATH = CACHE_DIR / "idmap.json"

EUROPE_PMC = "https://www.ebi.ac.uk/europepmc/webservices/rest"
EUTILS = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"
IDCONV = "https://www.ncbi.nlm.nih.gov/pmc/utils/idconv/v1.0/"

# What a reference turned out to be readable as, worst to best.
UNREADABLE, ABSTRACT, FULL_TEXT = "unreadable", "abstract", "full_text"

# Not literature at all: a database record, ontology term or deposited dataset.
# Asking whether these are "readable" is the wrong question — whether they
# resolve is, and check_curies.py already answers it. Counting them among the
# unreadable papers would inflate the one number this audit exists to report.
NOT_LITERATURE = "not_literature"
CROSSREF = "https://api.crossref.org/works/"
DATACITE = "https://api.datacite.org/dois/"
# Crossref types whose text a reader could expect to reach.
LITERATURE_TYPES = {"journal-article", "book-chapter", "proceedings-article",
                    "posted-content", "book", "monograph", "reference-entry", "report"}


def _get(url: str, timeout: float = 45.0) -> tuple[int, str]:
    try:
        with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=timeout) as r:
            return r.status, r.read().decode("utf-8", errors="replace")
    except urllib.error.HTTPError as exc:
        return exc.code, ""
    except Exception:  # noqa: BLE001 — a transport failure is not a verdict
        return 0, ""


def plain(xml: str) -> str:
    """XML/HTML to flowing text, keeping only what an author actually wrote.

    A JATS article carries the journal's own metadata in ``<front>`` and its
    bibliography in ``<back>``. Stripping tags across the whole document mixes
    both into the prose, and the ranker duly offered "Cell Cell 319 nihpa
    0413066 ... Article How to build a bacterial cell" as a candidate quotation.
    Neither is a claim anyone made, so both are dropped before ranking.
    """
    text = re.sub(r"<(?:script|style)[^>]*>.*?</(?:script|style)>", " ", xml, flags=re.S | re.I)
    body = re.search(r"<body[^>]*>(.*)</body>", text, re.S | re.I)
    if body:
        # The abstract sits in <front> beside the journal metadata, and is
        # author prose — keeping only <body> silently made every abstract
        # sentence unquotable, which --verify caught on a real snippet.
        abstracts = re.findall(r"<abstract[^>]*>(.*?)</abstract>", text, re.S | re.I)
        text = " ".join([*abstracts, body.group(1)])
    else:  # a PubMed abstract or plain page has no body element
        text = re.sub(r"<journal-meta[^>]*>.*?</journal-meta>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<(back|ref-list)[^>]*>.*?</\1>", " ", text, flags=re.S | re.I)
    text = re.sub(r"<[^>]+>", " ", text)
    text = text.replace("&amp;", "&").replace("&lt;", "<").replace("&gt;", ">").replace("&#x2013;", "-")
    return re.sub(r"\s+", " ", text).strip()


# ------------------------------------------------------------------ identity


def is_literature_shape(reference: str) -> bool:
    """A URL or a non-bibliographic CURIE is a record, not a paper."""
    return reference.startswith(("DOI:", "PMID:", "PMCID:"))


def classify_doi(doi: str) -> str:
    """Literature or deposited data, per the registration agency's own type."""
    status, body = _get(CROSSREF + urllib.parse.quote(doi))
    if status == 200:
        kind = (json.loads(body).get("message") or {}).get("type", "")
        return "literature" if kind in LITERATURE_TYPES else NOT_LITERATURE
    status, _ = _get(DATACITE + urllib.parse.quote(doi))
    return NOT_LITERATURE if status == 200 else "literature"


def resolve_identity(reference: str) -> dict:
    """PMID and PMCID for a reference, by every route, not just one.

    NCBI's converter is PMC-only: a paper that is not in PMC comes back empty,
    which reads identically to "not in PubMed either" and is how a real PMID was
    recorded as absent (#133). Europe PMC indexes both and is tried as well.
    """
    kind, _, value = reference.partition(":")
    out = {"reference": reference, "pmid": None, "pmcid": None, "doi": value if kind == "DOI" else None}
    if kind == "PMID":
        out["pmid"] = value

    if out["doi"]:
        status, body = _get(IDCONV + "?format=json&ids=" + urllib.parse.quote(out["doi"]))
        if status == 200:
            record = (json.loads(body).get("records") or [{}])[0]
            out["pmid"] = out["pmid"] or record.get("pmid")
            out["pmcid"] = out["pmcid"] or record.get("pmcid")

    if not (out["pmid"] and out["pmcid"]):
        query = f"DOI:{out['doi']}" if out["doi"] else f"EXT_ID:{out['pmid']}"
        status, body = _get(f"{EUROPE_PMC}/search?format=json&pageSize=1&query="
                            + urllib.parse.quote(query))
        if status == 200:
            hits = json.loads(body).get("resultList", {}).get("result", [])
            if hits:
                out["pmid"] = out["pmid"] or hits[0].get("pmid")
                out["pmcid"] = out["pmcid"] or hits[0].get("pmcid")
    return out


# ------------------------------------------------------------------ text


def fetch_text(identity: dict) -> tuple[str, str, str]:
    """(readability, source, text). Probes endpoints; never trusts a flag.

    Europe PMC reports ``inEPMC: Y`` for PMC5433867 while its fullTextXML
    returns 404, so availability is whatever an actual request returns.
    """
    pmcid = identity.get("pmcid")
    if pmcid:
        status, body = _get(f"{EUTILS}/efetch.fcgi?db=pmc&id={pmcid}&retmode=xml")
        if status == 200 and len(body) > 4000:
            return FULL_TEXT, f"PMC/{pmcid}", plain(body)
        status, body = _get(f"{EUROPE_PMC}/{pmcid}/fullTextXML")
        if status == 200 and len(body) > 4000:
            return FULL_TEXT, f"EuropePMC/{pmcid}", plain(body)

    if identity.get("not_literature"):
        return NOT_LITERATURE, "", ""

    pmid = identity.get("pmid")
    if pmid:
        status, body = _get(f"{EUTILS}/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml")
        if status == 200:
            match = re.search(r"<Abstract>(.*?)</Abstract>", body, re.S)
            if match:
                return ABSTRACT, f"PubMed/{pmid}", plain(match.group(1))
    return UNREADABLE, "", ""


# ------------------------------------------------------------------ evidence


def evidence_items(records) -> list[dict]:
    """Every evidence item, with the record and the claim it is attached to."""
    found: list[dict] = []

    def walk(node, path: str, record: str, claim: str):
        if isinstance(node, dict):
            if "reference" in node and isinstance(node["reference"], str):
                found.append({"record": record, "path": path, "claim": claim,
                              "reference": node["reference"], "snippet": node.get("snippet"),
                              "notes": node.get("notes", "")})
            label = node.get("label") or node.get("trait_label") or node.get("prompt") or claim
            for key, value in node.items():
                walk(value, f"{path}.{key}" if path else key, record, label)
        elif isinstance(node, list):
            for index, item in enumerate(node):
                walk(item, f"{path}[{index}]", record, claim)

    for path, doc in records:
        walk(doc, "", path.name, doc.get("label", ""))
    return found


# Abbreviations whose full stop does not end a sentence. "E. coli" split into
# "...absence of MreB." and "coli MreB forms..." — a fragment a curator could
# paste as a quotation, since it is still a literal substring of the source.
ABBREVIATIONS = frozenset({
    "al", "fig", "figs", "eq", "ref", "refs", "approx", "vs", "cf", "etc",
    "spp", "sp", "subsp", "str", "dr", "prof", "no", "pp", "ca", "i.e", "e.g",
})
_BREAK = re.compile(r"(?<=[.!?])\s+(?=[A-Z0-9\u201c(])")


def split_sentences(text: str) -> list[str]:
    """Split on sentence ends, not on every full stop.

    Python's ``re`` cannot express this as a lookbehind — the abbreviation list
    is variable-width — so candidate breaks are found first and then filtered by
    the token that precedes them.
    """
    sentences: list[str] = []
    start = 0
    for match in _BREAK.finditer(text):
        token = re.search(r"([\w.]+)\.$", text[start:match.start()].strip())
        word = token.group(1).lower().rstrip(".") if token else ""
        # A one-letter token is a genus initial or a middle initial, never a sentence.
        if word in ABBREVIATIONS or len(word) == 1:
            continue
        piece = text[start:match.start()].strip()
        if piece:
            sentences.append(piece)
        start = match.end()
    tail = text[start:].strip()
    if tail:
        sentences.append(tail)
    return sentences


def candidate_sentences(text: str, claim: str, notes: str, limit: int = 5) -> list[str]:
    """Sentences ranked by overlap with the claim's own words."""
    stop = {"the", "a", "an", "of", "and", "in", "to", "is", "for", "that", "this", "with", "as",
            "its", "it", "by", "on", "are", "be", "from", "which", "not", "at", "or", "than"}
    words = {w for w in re.findall(r"[a-z]{4,}", f"{claim} {notes}".lower()) if w not in stop}
    sentences = [s.strip() for s in split_sentences(text) if 40 < len(s.strip()) < 400]
    scored = sorted(sentences, key=lambda s: -len(words & set(re.findall(r"[a-z]{4,}", s.lower()))))
    return [s for s in scored[:limit] if words & set(re.findall(r"[a-z]{4,}", s.lower()))]


def normalise(text: str) -> str:
    """Reduce a quotation to what makes it *the same quotation*.

    Whitespace is dropped entirely rather than collapsed. Stripping ``<xref>``
    tags out of PMC's XML leaves spaces inside the punctuation that surrounded
    them — the printed "(Kruse et al., 2005)" arrives as "( Kruse et al., 2005 )"
    — so a whitespace-sensitive comparison rejects a quotation that is genuinely
    in the paper. A gate that fails on correct input is worse than no gate: it
    teaches the curator to ignore it. Case, dash style and curly quotes go the
    same way, for the same reason.

    What survives is the letters and punctuation in order, which is what a
    fabricated or silently reworded quotation still fails.
    """
    for fancy, plain_char in (("–", "-"), ("—", "-"), ("’", "'"),
                              ("“", '"'), ("”", '"'), ("\u00a0", " ")):
        text = text.replace(fancy, plain_char)
    return re.sub(r"\s+", "", text).lower()


# ------------------------------------------------------------------ modes


def _load_texts(references: list[str], cache: dict) -> dict[str, tuple[str, str, str]]:
    texts = {}
    for reference in references:
        identity = cache.get(reference)
        if identity is None:
            if not is_literature_shape(reference):
                identity = {"reference": reference, "not_literature": True}
            else:
                identity = resolve_identity(reference)
                if identity["doi"] and not (identity["pmid"] or identity["pmcid"]):
                    identity["not_literature"] = classify_doi(identity["doi"]) == NOT_LITERATURE
        cache[reference] = identity
        readability, source, text = fetch_text(identity)
        texts[reference] = (readability, source, text)
        time.sleep(0.4)  # NCBI asks for a modest rate without an API key
    return texts


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--audit", action="store_true", help="Report what each reference can be read as.")
    mode.add_argument("--suggest", action="store_true", help="Candidate sentences for one record's claims.")
    mode.add_argument("--verify", action="store_true", help="Every snippet must occur in its source.")
    parser.add_argument("--record", type=Path, help="Restrict to one record (required by --suggest).")
    parser.add_argument("--report", type=Path, default=REPO_ROOT / "reports" / "evidence_readability.tsv")
    parser.add_argument("--check", action="store_true", help="With --verify, exit 1 on any mismatch.")
    args = parser.parse_args()

    records = load_records()
    if not records:
        print("no records found — the corpus path or loader is wrong, not the corpus", file=sys.stderr)
        return 2
    if args.record:
        records = [(p, d) for p, d in records if p.name == args.record.name]
        if not records:
            print(f"no record named {args.record.name}", file=sys.stderr)
            return 2

    items = evidence_items(records)
    if not items:
        print("no evidence items found — the collector is not seeing the fields it should", file=sys.stderr)
        return 2

    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    cache = json.loads(IDMAP_PATH.read_text()) if IDMAP_PATH.exists() else {}

    if args.suggest:
        if not args.record:
            print("--suggest needs --record", file=sys.stderr)
            return 2
        texts = _load_texts(sorted({i["reference"] for i in items}), cache)
        IDMAP_PATH.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")
        for item in items:
            readability, source, text = texts[item["reference"]]
            print(f"\n=== {item['path']}\n    claim: {item['claim']}\n    ref:   {item['reference']} "
                  f"[{readability}{' via ' + source if source else ''}]")
            if item["snippet"]:
                print("    already quoted; nothing to suggest")
                continue
            if readability == UNREADABLE:
                print("    nothing readable — say so rather than paraphrasing a title")
                continue
            for n, sentence in enumerate(candidate_sentences(text, item["claim"], item["notes"]), 1):
                print(f"      [{n}] {sentence}")
        return 0

    if args.verify:
        quoted = [i for i in items if i["snippet"]]
        print(f"{len(quoted)} of {len(items)} evidence items carry a snippet", file=sys.stderr)
        if not quoted:
            return 0
        texts = _load_texts(sorted({i["reference"] for i in quoted}), cache)
        IDMAP_PATH.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")
        bad = []
        for item in quoted:
            readability, source, text = texts[item["reference"]]
            if readability == UNREADABLE:
                bad.append(f"{item['record']}:{item['path']}: {item['reference']} cannot be read, so its "
                           f"quotation cannot be checked")
            elif readability == NOT_LITERATURE:
                bad.append(f"{item['record']}:{item['path']}: {item['reference']} is a database "
                           f"record, not a paper — a verbatim quotation cannot be checked against it")
            elif normalise(item["snippet"]) not in normalise(text):
                bad.append(f"{item['record']}:{item['path']}: quotation not found in {source} — "
                           f"{item['snippet'][:70]}...")
        for line in bad:
            print(f"  {line}", file=sys.stderr)
        print(f"\n{len(quoted) - len(bad)} of {len(quoted)} quotations verified against the source")
        return 1 if bad and args.check else 0

    # --audit (default)
    references = sorted({i["reference"] for i in items})
    texts = _load_texts(references, cache)
    IDMAP_PATH.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")
    by_reference = defaultdict(list)
    for item in items:
        by_reference[item["reference"]].append(item)

    args.report.parent.mkdir(parents=True, exist_ok=True)
    counts: dict[str, int] = defaultdict(int)
    uncheckable = 0
    with args.report.open("w", newline="", encoding="utf-8") as fh:
        writer = csv.writer(fh, delimiter="\t", lineterminator="\n")
        writer.writerow(["reference", "pmid", "pmcid", "readability", "source",
                         "claims", "quoted", "checked_on"])
        for reference in references:
            readability, source, _ = texts[reference]
            identity = cache.get(reference, {})
            claims = by_reference[reference]
            quoted = sum(1 for c in claims if c["snippet"])
            counts[readability] += 1
            if readability == UNREADABLE and quoted == 0:  # NOT_LITERATURE excluded on purpose
                uncheckable += len(claims)
            writer.writerow([reference, identity.get("pmid") or "", identity.get("pmcid") or "",
                             readability, source, len(claims), quoted, date.today().isoformat()])

    print(f"\n{len(references)} distinct references across {len(items)} evidence items")
    for readability in (FULL_TEXT, ABSTRACT, UNREADABLE, NOT_LITERATURE):
        print(f"  {readability:14s} {counts[readability]:3d}")
    print(f"\n{uncheckable} claim(s) cite a paper with no reachable text and carry no quotation — "
          f"nobody can check those")
    print(f"report: {args.report.relative_to(REPO_ROOT)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
