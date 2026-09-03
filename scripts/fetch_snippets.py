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
# No route answered. Neither readable nor unreadable — simply not established.
UNCHECKED = "unchecked"
CROSSREF = "https://api.crossref.org/works/"
DATACITE = "https://api.datacite.org/dois/"
# Crossref types whose text a reader could expect to reach.
LITERATURE_TYPES = {"journal-article", "book-chapter", "proceedings-article",
                    "posted-content", "book", "monograph", "reference-entry", "report"}


# Returned as the status when no answer was obtained at all. A server that says
# 404 has told us something; a socket that never opened has not, and the two must
# never reach the same conclusion — that conflation is the whole reason this
# script exists.
TRANSPORT_FAILURE = -1
RETRIES = 3


def _get(url: str, timeout: float = 45.0) -> tuple[int, str]:
    """(status, body). ``TRANSPORT_FAILURE`` means no answer, not a negative one."""
    for attempt in range(RETRIES):
        try:
            request = urllib.request.Request(url, headers=UA)
            with urllib.request.urlopen(request, timeout=timeout) as response:
                return response.status, response.read().decode("utf-8", errors="replace")
        except urllib.error.HTTPError as exc:
            return exc.code, ""  # the server answered; that is a verdict
        except Exception:  # noqa: BLE001 — transport; worth another try
            if attempt == RETRIES - 1:
                return TRANSPORT_FAILURE, ""
            time.sleep(1.5 * (attempt + 1))
    return TRANSPORT_FAILURE, ""


# Below this, a <body> holds a figure caption or a permissions notice rather than
# an article. PMC2761316 is 10 KB of XML with no <body> at all, and a length test
# on the raw response called it full text (#162).
MIN_BODY_PROSE = 1500


def body_text(payload: str) -> str | None:
    """The article's own prose, or None when the response carries no article.

    A response can be long and still not be full text: PMC holds metadata and an
    abstract for records whose publisher never deposited a body, and the author
    list alone runs to kilobytes. The tell is whether there is a ``<body>``, so
    that is what is asked -- not how big the response is.
    """
    if not re.search(r"<body[^>]*>", payload, re.I):
        return None
    text = plain(payload)
    return text if len(text) >= MIN_BODY_PROSE else None


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
    if status == TRANSPORT_FAILURE:
        return UNCHECKED
    if status == 200:
        kind = (json.loads(body).get("message") or {}).get("type", "")
        return "literature" if kind in LITERATURE_TYPES else NOT_LITERATURE
    status, _ = _get(DATACITE + urllib.parse.quote(doi))
    if status == TRANSPORT_FAILURE:
        return UNCHECKED
    return NOT_LITERATURE if status == 200 else "literature"


def resolve_identity(reference: str) -> dict:
    """PMID and PMCID for a reference, by every route, not just one.

    NCBI's converter is PMC-only: a paper that is not in PMC comes back empty,
    which reads identically to "not in PubMed either" and is how a real PMID was
    recorded as absent (#133). Europe PMC indexes both and is tried as well.
    """
    kind, _, value = reference.partition(":")
    out = {"reference": reference, "pmid": None, "pmcid": None,
           "doi": value if kind == "DOI" else None, "unanswered": False}
    if kind == "PMID":
        out["pmid"] = value

    if out["doi"]:
        status, body = _get(IDCONV + "?format=json&ids=" + urllib.parse.quote(out["doi"]))
        out["unanswered"] = out["unanswered"] or status == TRANSPORT_FAILURE
        if status == 200:
            record = (json.loads(body).get("records") or [{}])[0]
            out["pmid"] = out["pmid"] or record.get("pmid")
            out["pmcid"] = out["pmcid"] or record.get("pmcid")

    if not (out["pmid"] and out["pmcid"]):
        query = f"DOI:{out['doi']}" if out["doi"] else f"EXT_ID:{out['pmid']}"
        status, body = _get(f"{EUROPE_PMC}/search?format=json&pageSize=1&query="
                            + urllib.parse.quote(query))
        out["unanswered"] = out["unanswered"] or status == TRANSPORT_FAILURE
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

    A route that never answered yields ``UNCHECKED``, not ``UNREADABLE``. The
    difference is the point of the script: a 404 is a verdict about the paper, a
    dead socket is a verdict about the network, and only the first belongs in a
    count of claims nobody can check.
    """
    if identity.get("not_literature"):
        return NOT_LITERATURE, "", ""

    unanswered = bool(identity.get("unanswered"))

    pmcid = identity.get("pmcid")
    if pmcid:
        for label, url in (("PMC", f"{EUTILS}/efetch.fcgi?db=pmc&id={pmcid}&retmode=xml"),
                           ("EuropePMC", f"{EUROPE_PMC}/{pmcid}/fullTextXML")):
            status, payload = _get(url)
            unanswered = unanswered or status == TRANSPORT_FAILURE
            if status != 200:
                continue
            text = body_text(payload)
            if text:
                return FULL_TEXT, f"{label}/{pmcid}", text

    pmid = identity.get("pmid")
    if pmid:
        status, body = _get(f"{EUTILS}/efetch.fcgi?db=pubmed&id={pmid}&retmode=xml")
        unanswered = unanswered or status == TRANSPORT_FAILURE
        if status == 200:
            match = re.search(r"<Abstract>(.*?)</Abstract>", body, re.S)
            if match:
                return ABSTRACT, f"PubMed/{pmid}", plain(match.group(1))

    return (UNCHECKED if unanswered else UNREADABLE), "", ""


# ------------------------------------------------------------------ evidence


def evidence_items(records) -> list[dict]:
    """Every evidence item, with the record and the claim it is attached to."""
    found: list[dict] = []

    def walk(node, path: str, record: str, claim: str):
        if isinstance(node, dict):
            if "reference" in node and isinstance(node["reference"], str):
                found.append({"record": record, "path": path, "claim": claim,
                              "reference": node["reference"], "snippet": node.get("snippet"),
                              "notes": node.get("notes", ""),
                              # An `evidence` list entry is an evidence item; a bare
                              # `reference` on a taxon note or image is a citation but
                              # not one. #133 counts the former, this tool both.
                              "in_evidence": "evidence[" in f"{path}."})
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


_QUOTES = {"\u201c": '"', "\u201d": '"', "\u201e": '"', "\u2018": "'", "\u2019": "'"}
_DASHES = {"\u2013": "-", "\u2014": "-", "\u2212": "-"}

# Tiers, strongest first. A match at EXACT or DESPACED is verbatim; a match only
# at LOOSE is not, and says so.
EXACT, DESPACED, LOOSE, ABSENT = "exact", "despaced", "loose", "absent"


def _exact(text: str) -> str:
    """Collapse whitespace runs. Everything else is significant."""
    return re.sub(r"\s+", " ", text.replace("\u00a0", " ")).strip()


def _despaced(text: str) -> str:
    """Drop whitespace entirely; keep hyphens, case and punctuation.

    Stripping ``<xref>`` tags out of JATS leaves spaces inside the punctuation
    that surrounded them — the printed "(Kruse et al., 2005)" arrives as
    "( Kruse et al., 2005 )". That is an extraction artefact, not a difference in
    the text, so a match here is still verbatim.

    Unlike the PDF equivalent this is modelled on, hyphens stay significant: a
    PDF line-break hyphen is indistinguishable from a compound hyphen, but JATS
    has no line breaks, so "rod-like" and "rodlike" really are different words.
    """
    return re.sub(r"\s+", "", text.replace("\u00a0", " "))


def _loose(text: str) -> str:
    """As ``_despaced``, and additionally unify case, quote and dash style.

    A curly-quote or en-dash mismatch IS a real difference — the record does not
    hold what the paper holds — so it is only normalised at the last tier, to
    separate "copied imprecisely" from "not in the paper at all".
    """
    for fancy, plain_char in {**_QUOTES, **_DASHES}.items():
        text = text.replace(fancy, plain_char)
    return _despaced(text).lower()


def describe_difference(snippet: str, source: str) -> str:
    """Which of the loose-tier allowances the match actually needed.

    ``_loose`` unifies case, quotes and dashes together, so reporting all three
    every time sends the curator looking for two things that are not there.
    """
    def unify(text: str, quotes: bool, dashes: bool, case: bool) -> str:
        mapping = {**(_QUOTES if quotes else {}), **(_DASHES if dashes else {})}
        for fancy, plain_char in mapping.items():
            text = text.replace(fancy, plain_char)
        text = _despaced(text)
        return text.lower() if case else text

    reasons = [label for label, flags in (("quote style", (True, False, False)),
                                          ("dash style", (False, True, False)),
                                          ("letter case", (False, False, True)))
               if unify(snippet, *flags) in unify(source, *flags)]
    return " or ".join(reasons) if reasons else "case, quote or dash style"


def match_tier(snippet: str, source: str) -> str:
    """The strongest tier at which ``snippet`` occurs in ``source``."""
    if not snippet.strip():
        return ABSENT
    if _exact(snippet) in _exact(source):
        return EXACT
    if _despaced(snippet) in _despaced(source):
        return DESPACED
    if _loose(snippet) in _loose(source):
        return LOOSE
    return ABSENT


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
                    kind = classify_doi(identity["doi"])
                    if kind == UNCHECKED:
                        identity["unanswered"] = True
                    else:
                        identity["not_literature"] = kind == NOT_LITERATURE
        # A resolution nothing answered would otherwise be cached forever, leaving
        # the paper permanently unreadable with nothing to say so.
        if not identity.get("unanswered"):
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
    parser.add_argument("--report", type=Path, default=None,
                        help="Default: reports/evidence_readability.tsv, or a scoped "
                             "filename when --record narrows the run.")
    parser.add_argument("--check", action="store_true", help="With --verify, exit 1 on any mismatch.")
    parser.add_argument("--strict", action="store_true",
                        help="With --verify --check, also fail on a snippet that is present but "
                             "not verbatim. Off by default: imprecise is not fabricated.")
    args = parser.parse_args()

    # A narrowed run must not overwrite the corpus-wide report with rows that
    # look complete and are not (#148).
    default_report = REPO_ROOT / "reports" / (
        f"evidence_readability.{args.record.stem}.tsv" if args.record
        else "evidence_readability.tsv")
    args.report = args.report or default_report

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
        print("no citations found — the collector is not seeing the fields it should",
              file=sys.stderr)
        return 2
    in_evidence = sum(1 for i in items if i["in_evidence"])

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
        quoted_evidence = sum(1 for i in quoted if i["in_evidence"])
        print(f"{len(quoted)} of {len(items)} citations carry a snippet; "
              f"{quoted_evidence} of those are evidence items "
              f"({len(items)} citations = {in_evidence} evidence items + "
              f"{len(items) - in_evidence} bare references)", file=sys.stderr)
        if not quoted:
            return 0
        texts = _load_texts(sorted({i["reference"] for i in quoted}), cache)
        IDMAP_PATH.write_text(json.dumps(cache, indent=1, sort_keys=True) + "\n")
        bad: list[str] = []
        imprecise: list[str] = []
        unchecked: list[str] = []
        for item in quoted:
            readability, source, text = texts[item["reference"]]
            if readability == UNCHECKED:
                unchecked.append(f"{item['record']}:{item['path']}: {item['reference']} — no route "
                                 f"answered, so this quotation was not checked either way")
            elif readability == UNREADABLE:
                bad.append(f"{item['record']}:{item['path']}: {item['reference']} cannot be read, so its "
                           f"quotation cannot be checked")
            elif readability == NOT_LITERATURE:
                bad.append(f"{item['record']}:{item['path']}: {item['reference']} is a database "
                           f"record, not a paper — a verbatim quotation cannot be checked against it")
            else:
                tier = match_tier(item["snippet"], text)
                if tier == ABSENT:
                    bad.append(f"{item['record']}:{item['path']}: quotation not found in {source} "
                               f"at any tier — {item['snippet'][:70]}...")
                elif tier == LOOSE:
                    imprecise.append(
                        f"{item['record']}:{item['path']}: present in {source} but not verbatim — "
                        f"differs in {describe_difference(item['snippet'], text)}. Re-copy the "
                        f"exact characters. {item['snippet'][:70]}...")
        for line in bad:
            print(f"  [ABSENT]      {line}", file=sys.stderr)
        for line in imprecise:
            print(f"  [not verbatim] {line}", file=sys.stderr)
        for line in unchecked:
            print(f"  [not checked] {line}", file=sys.stderr)
        verified = len(quoted) - len(bad) - len(imprecise) - len(unchecked)
        print(f"\n{verified} of {len(quoted)} quotations found verbatim in the source")
        if imprecise:
            print(f"{len(imprecise)} present but not verbatim — the text is in the paper, the "
                  f"record's copy of it is not exact")
        if unchecked:
            print(f"{len(unchecked)} could not be checked because no route answered — "
                  f"not a finding about the corpus")
        # Only a quotation absent from text we actually retrieved is a failure,
        # unless --strict also holds an imprecise copy to account.
        failing = bad + (imprecise if args.strict else [])
        return 1 if failing and args.check else 0

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
        scope = args.record.name if args.record else "whole corpus"
        writer.writerow(["scope", "reference", "pmid", "pmcid", "readability", "source",
                         "citations", "evidence_items", "quoted", "checked_on"])
        for reference in references:
            readability, source, _ = texts[reference]
            identity = cache.get(reference, {})
            claims = by_reference[reference]
            quoted = sum(1 for c in claims if c["snippet"])
            counts[readability] += 1
            # NOT_LITERATURE and UNCHECKED are excluded on purpose: one is not a
            # paper, the other is a question we failed to ask.
            if readability == UNREADABLE and quoted == 0:
                uncheckable += len(claims)
            writer.writerow([scope, reference, identity.get("pmid") or "", identity.get("pmcid") or "",
                             readability, source, len(claims),
                             sum(1 for c in claims if c["in_evidence"]), quoted,
                             date.today().isoformat()])

    print(f"\n{len(references)} distinct references across {len(items)} citations, "
          f"of which {in_evidence} are evidence items")
    for readability in (FULL_TEXT, ABSTRACT, UNREADABLE, NOT_LITERATURE, UNCHECKED):
        print(f"  {readability:14s} {counts[readability]:3d}")
    print(f"\n{uncheckable} claim(s) cite a paper with no reachable text and carry no quotation — "
          f"nobody can check those")
    try:
        shown = args.report.relative_to(REPO_ROOT)
    except ValueError:  # a path outside the repository is legitimate
        shown = args.report
    print(f"report: {shown}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
