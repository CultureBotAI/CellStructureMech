#!/usr/bin/env python3
"""Seed ``components.protein_examples`` by gene symbol (issue #183).

``uniprot_sl.py proteins`` can only reach a component when the record's GO term
has a UniProt Subcellular Location mapping *and* a reviewed entry in one of the
record's canonical taxa carries that localisation. Run across the whole corpus
that route seeds five accessions. Most ``PROTEIN`` components are left with a
gene symbol and nothing resolvable, and ``interpro_groundings.py`` matches on
accessions, so the grounding backlog in #174 cannot move.

This is the other route #183 names, and the one the flagellum's accessions were
found by hand with::

    (gene_exact:<symbol>) AND (taxonomy_id:<taxon on the record>) AND (reviewed:true)

That is a query, not a guess: it returns a reviewed Swiss-Prot entry or nothing.

**The rule that makes it safe is "exactly one".** ``gene_exact:pilA`` in
*Pseudomonas aeruginosa* returns five reviewed pilin alleles; there is no honest
way to pick one, so the component is reported and skipped. Only a symbol that
resolves to a single reviewed entry in a taxon the record itself names is
written, and the returned entry's own gene names are re-checked against the
symbol before it is accepted -- the search is trusted to find candidates, never
to have understood the question.

The one tie-break allowed is by taxon node. ``taxonomy_id`` matches descendants,
so ``rodZ`` in *E. coli* K-12 returns the same protein three times, once per
sequenced sub-strain. When exactly one of those entries sits on the node the
record itself names, that is the record's own choice of organism rather than a
choice between equals, and it is taken. Anything else is skipped.

Every declared symbol is resolved, not just the first: a component labelled
"MreC and MreD" is two proteins, and one accession would present half of it as
the whole. Results are deduplicated by accession, because a component often
declares synonyms of one gene -- ``secY`` and ``prlA`` are the same entry -- and
accessions already on the component count, so a re-run fills gaps rather than
duplicating what a curator or the SL route already put there.

``taxon_label`` is NCBI's name for the taxon, not UniProt's organism string, so
that it corresponds to the ``NCBITaxon`` id beside it (#270).

What is written is an identifier, not a claim about the structure. The component
already asserts the gene symbol; this adds the accession UniProt gives that
symbol in that organism, and says so in ``role``. Where UniProt states a
subcellular location with ``ECO:0000269`` experimental evidence, those PubMed
citations are carried over and the note names *the location UniProt states* --
not the record's structure, which the entry says nothing about.

Dry-run by default; ``--apply`` writes through the validation gate and appends a
CurationEvent. Licence: UniProtKB is CC BY 4.0.

    python scripts/uniprot_genes.py                       # dry run, whole corpus
    python scripts/uniprot_genes.py --record data/structures/cytoskeleton/mreb_filament.yaml
    python scripts/uniprot_genes.py --record ... --apply
    python scripts/uniprot_genes.py --gaps                 # what is left, and why
"""

from __future__ import annotations

import argparse
import datetime
import json
import sys
import time
import urllib.error
import urllib.parse
import urllib.request
from pathlib import Path

import yaml

try:  # run as `python scripts/uniprot_genes.py` (scripts/ on sys.path) ...
    from corpus import REPO_ROOT, load_records
except ImportError:  # ... or imported by the tests as scripts.uniprot_genes
    from scripts.corpus import REPO_ROOT, load_records

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import ncbi_taxon_names, pubmed_citations
from cellstructuremech.validation.write_validated import ValidationFailedError, write_validated_structure

UA = {"User-Agent": "CellStructureMech/0.1 (https://github.com/CultureBotAI/CellStructureMech; curation bot)"}
REST = "https://rest.uniprot.org/uniprotkb/search"
ENTRY_URL = "https://www.uniprot.org/uniprotkb/{acc}"
FIELDS = ("accession,gene_primary,gene_names,protein_name,organism_name,organism_id,"
          "cc_subcellular_location,reviewed")
MAX_EVIDENCE = 3
RETRIES = 3


def _get(url: str) -> bytes:
    last: Exception | None = None
    for attempt in range(RETRIES):
        try:
            with urllib.request.urlopen(urllib.request.Request(url, headers=UA), timeout=60) as fh:
                return fh.read()
        except urllib.error.HTTPError as exc:
            if exc.code < 500:  # a malformed query is not transient
                raise
            last = exc
            time.sleep(2 * (attempt + 1))
        except (urllib.error.URLError, TimeoutError) as exc:  # transient; UniProt rate-limits
            last = exc
            time.sleep(2 * (attempt + 1))
    raise RuntimeError(f"UniProt unreachable after {RETRIES} attempts: {last}")


def search_gene(symbol: str, taxon_id: int) -> list[dict]:
    """Reviewed entries whose gene name or synonym is exactly ``symbol``.

    ``taxonomy_id`` rather than ``organism_id``: a record names the species
    (*P. aeruginosa*, 287) while the reviewed entry often sits on a strain node
    below it (PAO1, 208964). The entry's own organism is what gets recorded.
    """
    q = f"(gene_exact:{symbol}) AND (taxonomy_id:{taxon_id}) AND (reviewed:true)"
    url = REST + "?" + urllib.parse.urlencode(
        {"query": q, "format": "json", "size": 25, "fields": FIELDS})
    return json.loads(_get(url)).get("results", [])


def entry_status(entry: dict) -> str | None:
    """What the entry says it is, or None when it does not say (#262, #271).

    ``search_gene`` filters ``reviewed:true``, so every entry reaching here is
    reviewed by contract and this is always REVIEWED today. Reading it off the
    entry is what keeps the field true if the query is ever widened. An entry
    with no ``entryType`` is a broken contract, not an unreviewed entry, so it
    returns None and the example is declined -- writing UNREVIEWED would be an
    assertion made from missing data, which is the one thing this adapter is
    otherwise careful never to do.
    """
    # "UniProtKB unreviewed (TrEMBL)" contains "reviewed"; test for the negative first.
    kind = (entry.get("entryType") or "").lower()
    if "unreviewed" in kind:
        return "UNREVIEWED"
    return "REVIEWED" if "reviewed" in kind else None


def gene_names(entry: dict) -> list[str]:
    """Every gene name and synonym UniProt lists on the entry."""
    names = []
    for gene in entry.get("genes") or []:
        value = (gene.get("geneName") or {}).get("value")
        if value:
            names.append(value)
        names += [s["value"] for s in gene.get("synonyms") or [] if s.get("value")]
    return names


def localisations(entry: dict) -> list[tuple[str, list[str]]]:
    """(location name, ECO:0000269 PubMed ids) for each stated subcellular location."""
    out = []
    for comment in entry.get("comments") or []:
        if comment.get("commentType") != "SUBCELLULAR LOCATION":
            continue
        for loc in comment.get("subcellularLocations") or []:
            location = loc.get("location") or {}
            name = location.get("value")
            if not name:
                continue
            pmids = [ev["id"] for ev in location.get("evidences") or []
                     if ev.get("evidenceCode") == "ECO:0000269" and ev.get("source") == "PubMed"]
            out.append((name, list(dict.fromkeys(pmids))))
    return out


def entry_note(acc: str, symbol: str, organism: str) -> str:
    """The fallback: what the database entry itself states, and nothing more."""
    return (f"UniProtKB reviewed (Swiss-Prot) entry {acc}, the single reviewed entry for gene "
            f"{symbol} in {organism}. Establishes the accession and gene identity only; the "
            f"component's membership in this structure rests on the record's own sources.")


def localisation_note(acc: str, location: str, citation: str | None) -> str:
    """A localisation note naming the location UniProt states, not this record's structure."""
    base = (f"ECO:0000269 experimental evidence cited by UniProt for the '{location}' "
            f"localisation of {acc}.")
    return f"{citation} {base}" if citation else base


def missing_symbols(component: dict) -> list[str]:
    """Declared gene symbols with no protein example of their own yet."""
    have = {(e.get("gene_symbol") or "").lower()
            for e in component.get("protein_examples") or []}
    return [s for s in component.get("gene_symbols") or [] if s.lower() not in have]


def candidates(doc: dict) -> list[dict]:
    """Components this route could reach: PROTEIN, with a symbol still unrepresented."""
    return [c for c in doc.get("components") or []
            if c.get("component_type") == "PROTEIN" and missing_symbols(c)]


def per_taxon(symbol: str, taxa: list[tuple[int, str]]):
    """Yield ``(taxon_id, taxon_label, hits, exact)`` for one symbol, taxon by taxon.

    A generator so ``resolve_symbol`` can stop at the first taxon that answers
    while ``gap_report`` walks them all -- the two questions cost different
    numbers of requests and neither should pay for the other.
    """
    for taxon_id, taxon_label in taxa:
        hits = search_gene(symbol, taxon_id)
        exact = [e for e in hits
                 if any(n.lower() == symbol.lower() for n in gene_names(e))]
        yield taxon_id, taxon_label, hits, exact


def resolve_symbol(symbol: str, taxa: list[tuple[int, str]]) -> tuple[dict | None, str]:
    """The one reviewed entry for one symbol, or why there isn't one.

    Taxa are tried in the order the record lists them, so the curator's own
    ranking decides; a symbol that is ambiguous in one organism does not
    disqualify the next.
    """
    reasons = []
    for taxon_id, taxon_label, hits, exact in per_taxon(symbol, taxa):
        # Several reviewed entries for one symbol are usually the same protein in
        # sub-strains of the named taxon (rodZ in E. coli K-12: MG1655, BW2952,
        # DH10B). The entry sitting on the node the record actually names is the
        # one to take -- that is the record's own choice of organism, not a guess
        # between equals. at_node is a subset of exact, so narrowing to it can only
        # remove candidates: the "exactly one" test below still decides, and a
        # symbol that is ambiguous at the named node stays ambiguous.
        at_node = [e for e in exact if (e.get("organism") or {}).get("taxonId") == taxon_id]
        chosen = at_node or exact
        if len(chosen) == 1:
            return {"entry": chosen[0], "symbol": symbol, "taxon_label": taxon_label,
                    "narrowed": len(exact) > 1}, "ok"
        if len(exact) > 1:
            reasons.append(f"{taxon_id}: {len(exact)} reviewed entries")
        elif hits:
            reasons.append(f"{taxon_id}: {len(hits)} hit(s), none an exact gene match")
    return None, "; ".join(reasons) if reasons else "no reviewed entry"


def resolve(component: dict, taxa: list[tuple[int, str]]) -> tuple[list[dict], str]:
    """Every declared symbol that resolves, deduplicated by accession (#261).

    A component labelled "MreC and MreD" is two proteins, and returning only the
    first symbol's entry would present half of it as the whole. Deduplication is
    by accession because a component often declares synonyms of one gene --
    ``secY`` and ``prlA`` are the same entry, not two examples of it -- and
    accessions already on the component count, so re-running fills the gaps a
    curator or the SL route left rather than duplicating what is there.
    """
    seen = {(e.get("uniprot_id") or "").split(":")[-1]
            for e in component.get("protein_examples") or []}
    hits, reasons = [], []
    for symbol in missing_symbols(component):
        hit, why = resolve_symbol(symbol, taxa)
        if hit is None:
            reasons.append(f"{symbol}/{why}")
            continue
        acc = hit["entry"]["primaryAccession"]
        if acc in seen:
            continue
        seen.add(acc)
        hits.append(hit)
    return hits, "; ".join(reasons) if reasons else "nothing left to resolve"


# ------------------------------------------------------------------- gaps
#
# What is left after a seeding run is not one backlog. #183's tail is four
# different questions with four different answers, and reporting them as a
# single count of "components without an accession" hides which of them an
# adapter could ever close. These are the categories, in the order a curator
# can act on them.

NO_TAXON = "NO_CANONICAL_TAXON"
NO_SYMBOL = "NO_GENE_SYMBOL"
AMBIGUOUS = "AMBIGUOUS_SYMBOL"
NO_EXACT = "NO_EXACT_GENE_MATCH"
NO_ENTRY = "NO_REVIEWED_ENTRY"

GAP_MEANING = {
    NO_TAXON: "the record names no taxon, so nothing can be taxon-paired",
    NO_SYMBOL: "the component declares no gene symbol to resolve",
    AMBIGUOUS: "the symbol resolves to several reviewed entries; a curator must choose",
    NO_EXACT: "reviewed entries were found but none carries the symbol as a gene name",
    NO_ENTRY: "no reviewed entry for any declared symbol in any taxon the record names",
}


def gap_report(doc: dict) -> list[tuple[str, str, str]]:
    """``(component_id, category, detail)`` for every PROTEIN symbol still unresolved.

    A row per **component**, but candidacy is per **symbol**, matching
    ``candidates()``. A component holding one accession and four unrepresented
    symbols is not done, and reporting only components with zero accessions
    undercounts the work in the one place whose job is to state it (#298). The
    detail says how many accessions such a component already has.

    A symbol resolving to an accession the component already holds is covered,
    not missing -- ``secY`` and ``prlA`` are one entry -- so it produces no row.

    Only the AMBIGUOUS rows are ones more querying could ever settle, and settling
    them means choosing between reviewed entries, which is a curation decision.
    The detail names the candidates so that choice can be made from the record.
    """
    taxa = [(int(t["taxon_id"].split(":")[1]), t["taxon_label"])
            for t in doc.get("canonical_examples") or [] if t.get("taxon_id")]
    rows = []
    for component in doc.get("components") or []:
        if component.get("component_type") != "PROTEIN":
            continue
        held = len(component.get("protein_examples") or [])
        symbols = missing_symbols(component)
        if held and not symbols:
            continue
        cid = component["component_id"]
        prefix = f"[{held} already] " if held else ""
        if not component.get("gene_symbols"):
            rows.append((cid, NO_SYMBOL, prefix + (component.get("label") or "")))
            continue
        if not taxa:
            rows.append((cid, NO_TAXON, prefix + ", ".join(symbols)))
            continue
        # A symbol that resolves to an accession the component already holds is
        # covered, not missing: `secY` and `prlA` are one entry, and `resolve()`
        # drops the second by accession. Counting those as NO_REVIEWED_ENTRY would
        # inflate this report with the #266 synonym artefact.
        seen = {(e.get("uniprot_id") or "").split(":")[-1]
                for e in component.get("protein_examples") or []}
        ambiguous, inexact, unresolved = [], [], []
        for symbol in symbols:
            resolved = None
            for taxon_id, _label, hits, exact in per_taxon(symbol, taxa):
                if len(exact) == 1:
                    resolved = exact[0]["primaryAccession"]
                    break
                if len(exact) > 1:
                    accs = ", ".join(sorted(e["primaryAccession"] for e in exact))
                    ambiguous.append(f"{symbol}@{taxon_id}: {accs}")
                elif hits:
                    # Entries were found and then rejected by the exact-name
                    # recheck. That is a different fact from finding nothing, and
                    # it points at a different remedy -- the symbol may be one
                    # UniProt spells another way (#299).
                    inexact.append(f"{symbol}@{taxon_id}: {len(hits)} hit(s)")
            if resolved is None:
                unresolved.append(symbol)
            elif resolved not in seen:
                # Seeding would have taken this; only reachable on a corpus that
                # has not had --apply run over it.
                unresolved.append(f"{symbol} (seedable: {resolved})")
        if not (ambiguous or inexact or unresolved):
            continue
        if ambiguous:
            rows.append((cid, AMBIGUOUS, prefix + "; ".join(ambiguous)))
        elif inexact:
            rows.append((cid, NO_EXACT, prefix + "; ".join(inexact)))
        else:
            rows.append((cid, NO_ENTRY, prefix + ", ".join(unresolved)))
    return rows


def cmd_gaps(records) -> int:
    counts: dict[str, int] = dict.fromkeys(GAP_MEANING, 0)
    partial = 0
    for path, doc in records:
        rows = gap_report(doc)
        if not rows:
            continue
        print(f"\n{path.relative_to(REPO_ROOT)}  ({doc['identifier']})")
        for cid, category, detail in rows:
            counts[category] += 1
            partial += detail.startswith("[")
            print(f"  {cid}\t{category}\t{detail}")
    print("\nPROTEIN components with an unresolved gene symbol:")
    for category, n in sorted(counts.items(), key=lambda kv: -kv[1]):
        print(f"  {n:3}  {category:20} {GAP_MEANING[category]}")
    total = sum(counts.values())
    print(f"  {total:3}  total, of which {partial} already hold at least one accession")
    return 0


def build_example(hit: dict, today: str, citations: dict[str, str],
                  taxon_names: dict[str, str], record_labels: dict[str, str] | None = None) -> dict | None:
    """The example to write, or None when it cannot be stated honestly.

    Declined when the entry carries no organism taxon (#263), when NCBI will not
    name that taxon (#270), or when the entry does not say whether it is reviewed
    (#271). Every accession here is paired to the organism it was found in, and a
    pair that cannot be completed is reported rather than filled in.

    ``taxon_label`` never comes from UniProt: the id is an ``NCBITaxon`` CURIE,
    and UniProt's house string beside it would be a pair that does not correspond
    -- one the id/label gate cannot catch, because ``conf/id_label_targets.yaml``
    skips the prefix (#270). A taxon the record itself names keeps the record's
    own label, which is what ``uniprot_sl.py`` writes, so one id does not end up
    with two labels in one corpus; a strain node below it takes NCBI's name.
    """
    entry = hit["entry"]
    acc = entry["primaryAccession"]
    organism = entry.get("organism") or {}
    taxon = organism.get("taxonId")
    status = entry_status(entry)
    if not taxon or status is None:
        return None
    organism_name = (record_labels or {}).get(str(taxon)) or taxon_names.get(str(taxon))
    if not organism_name:
        return None
    primary = (entry.get("genes") or [{}])[0].get("geneName", {}).get("value") or hit["symbol"]
    desc = entry.get("proteinDescription") or {}
    label = ((desc.get("recommendedName") or {}).get("fullName") or {}).get("value") or acc

    evidence = []
    for location, pmids in localisations(entry):
        for pmid in pmids[:MAX_EVIDENCE]:
            evidence.append({"reference": f"PMID:{pmid}",
                             "notes": localisation_note(acc, location, citations.get(str(pmid)))})
    seen, unique = set(), []
    for item in evidence:
        if item["reference"] not in seen:
            seen.add(item["reference"])
            unique.append(item)
    if not unique:
        unique = [{"reference": ENTRY_URL.format(acc=acc),
                   "notes": entry_note(acc, hit["symbol"], organism_name)}]

    narrowed = ("; other reviewed entries for this symbol exist on sub-strain nodes and this "
                "is the one at the taxon the record names" if hit.get("narrowed") else "")
    # rodA and mrdB are one gene; say so rather than leaving the record's symbol and
    # UniProt's primary name looking like two different things.
    named = (f"gene {hit['symbol']}, which UniProt lists under the primary name {primary},"
             if primary.lower() != hit["symbol"].lower() else f"gene {hit['symbol']}")
    role = (f"The single reviewed UniProtKB entry for {named} in "
            f"{organism_name}, a taxon this record names{narrowed}. Identifier for the "
            f"component's declared gene symbol; it is not itself evidence that the protein "
            f"is part of this structure.")
    return {
        "uniprot_id": f"UniProtKB:{acc}", "protein_label": label, "gene_symbol": primary,
        "taxon_id": f"NCBITaxon:{organism.get('taxonId')}", "taxon_label": organism_name,
        "entry_status": status, "retrieved_on": today, "role": role,
        "evidence": unique[:MAX_EVIDENCE],
    }


def plan_record(doc: dict, today: str) -> list[tuple[str, str, list[dict]]]:
    taxa = [(int(t["taxon_id"].split(":")[1]), t["taxon_label"])
            for t in doc.get("canonical_examples") or [] if t.get("taxon_id")]
    if not taxa:
        return [(c["component_id"], "no canonical taxon on the record", [])
                for c in candidates(doc)]
    resolved = [(component, *resolve(component, taxa)) for component in candidates(doc)]
    citations = pubmed_citations(
        [p for _, hits, _ in resolved for hit in hits
         for _, pmids in localisations(hit["entry"]) for p in pmids[:MAX_EVIDENCE]])
    taxon_names = ncbi_taxon_names(
        [str((hit["entry"].get("organism") or {}).get("taxonId"))
         for _, hits, _ in resolved for hit in hits
         if (hit["entry"].get("organism") or {}).get("taxonId")])
    record_labels = {t["taxon_id"].split(":")[1]: t["taxon_label"]
                     for t in doc.get("canonical_examples") or []
                     if t.get("taxon_id") and t.get("taxon_label")}
    rows = []
    for component, hits, why in resolved:
        examples = [e for e in
                    (build_example(h, today, citations, taxon_names, record_labels) for h in hits) if e]
        declined = len(hits) - len(examples)
        if declined:
            why = f"{why}; {declined} entry(s) not statable (no taxon, unnamed taxon, or no entryType)"
        rows.append((component["component_id"], why, examples))
    return rows


def _write(doc: dict, path: Path) -> None:
    try:
        write_validated_structure(doc, path)
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        raise SystemExit(1) from exc


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--record", help="One record; default is every record.")
    # --gaps reads and --apply writes; asking for both is a contradiction to
    # reject, not one to resolve by precedence (#300).
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument("--apply", action="store_true")
    mode.add_argument("--gaps", action="store_true",
                      help="Report what is left and why, instead of seeding. Read-only.")
    args = parser.parse_args()

    if args.record:
        path = Path(args.record).resolve()
        records = [(path, yaml.safe_load(path.read_text(encoding="utf-8")))]
    else:
        records = load_records()

    if args.gaps:
        return cmd_gaps(records)

    today = datetime.date.today().isoformat()
    total = 0
    for path, doc in records:
        rows = plan_record(doc, today)
        if not rows:
            continue
        print(f"\n{path.relative_to(REPO_ROOT)}  ({doc['identifier']})")
        added = 0
        for component_id, why, examples in rows:
            for example in examples:
                print(f"  {component_id}\t{example['uniprot_id']}\t{example['taxon_label']}"
                      f"\t{len(example['evidence'])} evidence\t{example['protein_label']}")
            if not examples:
                print(f"  {component_id}\t-\t{why}")
            if examples and args.apply:
                component = next(c for c in doc["components"] if c["component_id"] == component_id)
                component.setdefault("protein_examples", []).extend(examples)
                added += len(examples)
        if added:
            record_curation_event(
                doc, curator="uniprot_genes", action="SEED_PROTEIN_EXAMPLES", llm_assisted=False,
                changes=f"#183: added {added} protein example(s) by resolving each of the component's "
                        f"declared gene symbols to the single reviewed UniProtKB entry for that symbol "
                        f"in a taxon this record names, deduplicated by accession. Symbols resolving to "
                        f"more than one reviewed entry were skipped rather than chosen between.",
            )
            _write(doc, path)
            print(f"  wrote {added} protein example(s)")
            total += added
    if not args.apply:
        print("\ndry run; pass --apply to write the rows with an accession")
    else:
        print(f"\nwrote {total} protein example(s)")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
