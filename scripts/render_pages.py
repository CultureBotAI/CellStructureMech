#!/usr/bin/env python3
"""Render the browsable site under pages/ from data/structures/.

Generated, committed, and served from `main`, matching the sibling Mech
repos. Regenerate with `just render`; `--check` fails when the committed
output is out of step with the corpus.

Usage:
    python scripts/render_pages.py
    python scripts/render_pages.py --out /tmp/site --check

GitHub Pages serves the whole repository from `main`, so the one page that
must sit outside pages/ -- the 404.html GitHub returns for every missing URL --
is written to the repository root by a default render and checked by `--check`.
"""

from __future__ import annotations

import argparse
import filecmp
import hashlib
import json
import re
import shutil
import sys
import tempfile
from collections import Counter, defaultdict
from collections.abc import Mapping
from pathlib import Path
from urllib.parse import quote, urlencode, urlsplit

from jinja2 import Environment, FileSystemLoader, pass_context, select_autoescape
from markupsafe import Markup, escape

try:
    from corpus import REPO_ROOT, SCHEMA_PATH, load_records
except ImportError:  # imported as scripts.render_pages, as the tests do
    from scripts.corpus import REPO_ROOT, SCHEMA_PATH, load_records

TEMPLATES_DIR = REPO_ROOT / "src" / "cellstructuremech" / "templates"
IMAGES_DIR = REPO_ROOT / "data" / "images"
EMBEDDINGS_DIR = REPO_ROOT / "data" / "embeddings"
PAGES_DIR = REPO_ROOT / "pages"
REFERENCES = REPO_ROOT / "data" / "website" / "references.json"
NOT_FOUND = "404.html"

GH_REPO = "https://github.com/CultureBotAI/CellStructureMech"
GH_BLOB = GH_REPO + "/blob/main"
# Where the published pages live: the full URL a reported issue cites, and the
# site-root path the root 404.html links with. GitHub serves that page at
# whatever missing address was asked for, so a relative link in it would
# resolve against an unknown depth.
SITE_PAGES = "https://culturebotai.github.io/CellStructureMech/pages/"
SITE_PATH = "/CellStructureMech/pages/"
# Projection names as their authors write them; the data file stores lowercase.
PROJECTION_NAMES = {"pacmap": "PaCMAP", "umap": "UMAP", "pca": "PCA", "tsne": "t-SNE"}

CATEGORY_BLURB = {
    "ENVELOPE": "Membranes, cell wall, S-layer, capsule, outer membrane, periplasm.",
    "APPENDAGE": "Flagella, archaella, pili, fimbriae, stalks, and their motors.",
    "CYTOSKELETON": "MreB, FtsZ, crescentin, ParM and other filament systems.",
    "MICROCOMPARTMENT": "Protein-shelled organelles — carboxysomes, metabolosomes, encapsulins.",
    "INCLUSION": "Storage and buoyancy bodies — PHA granules, polyphosphate, gas vesicles.",
    "MEMBRANE_ORGANELLE": "Lipid-bounded internal compartments — thylakoids, chlorosomes, magnetosomes.",
    "NUCLEOID": "The chromosome-organising structure and its condensation machinery.",
    "RIBONUCLEOPROTEIN": "Ribosome, RNA polymerase holoenzyme, SRP, degradosome.",
    "SECRETION_SYSTEM": "Type I–IX secretion systems and the Sec / Tat translocons.",
    "DIVISION_MACHINERY": "Divisome, Z ring, Min system, elongasome.",
    "ENERGY_COMPLEX": "ATP synthase, respiratory and photosynthetic complexes, nitrogenase.",
    "SPORE": "Endospore layers, exosporium, and spore-specific structures.",
    "OTHER": "Records that fit no other bucket.",
}

PREFIX_URL = {
    "GO": "http://purl.obolibrary.org/obo/GO_",
    "CHEBI": "http://purl.obolibrary.org/obo/CHEBI_",
    "NCBITaxon": "http://purl.obolibrary.org/obo/NCBITaxon_",
    "RO": "http://purl.obolibrary.org/obo/RO_",
    "BFO": "http://purl.obolibrary.org/obo/BFO_",
    "UO": "http://purl.obolibrary.org/obo/UO_",
    "SO": "http://purl.obolibrary.org/obo/SO_",
    "CL": "http://purl.obolibrary.org/obo/CL_",
    "UBERON": "http://purl.obolibrary.org/obo/UBERON_",
    "InterPro": "https://www.ebi.ac.uk/interpro/entry/InterPro/",
    "Pfam": "https://www.ebi.ac.uk/interpro/entry/pfam/",
    # The schema's own expansion; bioregistry.io answers 404 for these CURIEs.
    "NCBIfam": "https://www.ncbi.nlm.nih.gov/genome/annotation_prok/evidence/",
    "UniProtKB": "https://www.uniprot.org/uniprotkb/",
    "ComplexPortal": "https://www.ebi.ac.uk/complexportal/complex/",
    "RNAcentral": "https://rnacentral.org/rna/",
    "ECO": "http://purl.obolibrary.org/obo/ECO_",
    "PDB": "https://www.rcsb.org/structure/",
    "RCSB_PDB": "https://www.rcsb.org/structure/",
    "EMDB": "https://www.ebi.ac.uk/emdb/",
    "EMPIAR": "https://www.ebi.ac.uk/empiar/EMPIAR-",
    "CryoETDataPortal": "https://cryoetdataportal.czscience.com/datasets/",
    "PMID": "https://pubmed.ncbi.nlm.nih.gov/",
    "DOI": "https://doi.org/",
    "METPO": "https://w3id.org/metpo/",
    "uniprot.location": "https://www.uniprot.org/locations/",
}

# This repository's own namespace. No registry resolves it, so a
# cellstructuremech: CURIE is followable only through the record page it names;
# sending it to a registry fallback would just invent a dead end.
LOCAL_PREFIX = "cellstructuremech"
CURIE_SHAPE = re.compile(r"[A-Za-z][A-Za-z0-9_.-]*:[^\s<>\"'\\]+")
# What a DOI or URL token may contain. It ends at whitespace, markup and quote
# characters, and at the Markdown delimiters ] and ` that close a link label or
# a code span: "[10.1038/x](https://doi.org/10.1038/x)" is two tokens, and
# "`10.1146/z`" is one without its backticks. An unbalanced ) is trimmed after.
TOKEN_CHARS = r"[^\s<>\"'`\]\\]"
BARE_DOI = re.compile(r"10\.[0-9]{4,9}/" + TOKEN_CHARS + "+")


def safe_url(value: object) -> str | None:
    """An http(s) URL that is safe to put in an href, or None.

    Records cite web pages directly (1,300+ evidence references are UniProt,
    EBI or PDF URLs). Anything that is not a plain http(s) address with a host
    -- another scheme, embedded credentials, whitespace, markup characters, a
    malformed port -- stays text.
    """
    if not isinstance(value, str) or any(ord(ch) < 32 or ord(ch) == 127 for ch in value):
        return None
    text = value.strip()
    if any(ch.isspace() or ch in '\\<>"' for ch in text):
        return None
    try:
        parts = urlsplit(text)
        if (parts.scheme.lower() in {"http", "https"} and parts.hostname
                and parts.username is None and parts.password is None):
            _ = parts.port  # raises on a non-numeric port
            return text
    except ValueError:
        pass
    return None


def curie_url(curie: object) -> str | None:
    """The resolver for a displayed identifier, or None when there is none.

    A reference that is already a URL is its own resolver. Known prefixes use
    PREFIX_URL; any other well-formed CURIE falls back to bioregistry.io, which
    resolves or explains a registered prefix, so a displayed identifier is not a
    dead end. The local prefix never falls back: its resolver is a record page,
    which term_link() supplies.
    """
    if not isinstance(curie, str):
        return None
    value = curie.strip()
    if value.lower().startswith(("http://", "https://")):
        return safe_url(value)
    if BARE_DOI.fullmatch(value):
        # A dataset accession may be a DOI written without its prefix.
        return "https://doi.org/" + quote(value, safe="/():;")
    if ":" not in value:
        return None
    prefix, local = value.split(":", 1)
    if prefix == "MICRO" and re.fullmatch(r"[0-9]{7}", local):
        iri = "http://purl.obolibrary.org/obo/MICRO_" + local
        return "https://www.ebi.ac.uk/ols4/ontologies/micro/classes/" + quote(quote(iri, safe=""), safe="")
    if prefix == "uniprot.location" and not re.fullmatch(r"SL-[0-9]{4}", local):
        return None
    base = PREFIX_URL.get(prefix)
    if base:
        return f"{base}{local}"
    if prefix == LOCAL_PREFIX or not CURIE_SHAPE.fullmatch(value):
        return None
    return "https://bioregistry.io/" + quote(value, safe=":/")


@pass_context
def term_link(context, identifier: object, label: object = None, reference: bool = False) -> Markup:
    """A displayed identifier as a link, followed by its readable label.

    Where a CURIE names one of this corpus's records, the record page is the
    resolver -- 852 records take a GO term as their identity, so a GO-grounded
    graph node or component is usually a structure with a page here. Two
    exceptions keep the link meaningful:

    * ``reference=True`` marks a citation slot (an evidence reference, a
      definition source). There the identifier names the source a claim rests
      on -- most often the GO term whose definition is quoted -- so its external
      resolver wins, and a record page is used only when there is no other.
    * The page's own identifier would link the page to itself, so it resolves
      externally, or, for a minted cellstructuremech: identifier, to the YAML
      file that defines it.

    ``label`` is the name the record gives the target; otherwise the pinned
    reference label, if any, is shown, so a name is printed once (#2295).
    """
    if not isinstance(identifier, str) or not identifier.strip():
        return Markup("")
    value = identifier.strip()
    code = Markup("<code>{}</code>").format(value)
    routes = context.get("reference_urls") or {}
    external = routes[value] if value in routes else curie_url(value)
    record = context.get("r")
    own = record.get("identifier") if isinstance(record, Mapping) else None
    target = (context.get("local_records") or {}).get(value)
    href = external
    if target and value != own and (external is None or not reference):
        href = f"{context.get('root') or ''}{target['page']}"
    elif value == own and external is None and context.get("source_path"):
        href = f"{GH_BLOB}/{context.get('source_path')}"
    link = Markup('<a href="{}">{}</a>').format(href, code) if href else code
    shown = label or (context.get("reference_labels") or {}).get(value)
    return link + Markup(" — {}").format(shown) if shown else link


# Reference tokens inside free text. URLs come first so a DOI or PMCID inside a
# URL stays part of that URL. Matching runs on the raw string and every piece is
# escaped on the way out, so record text can never become markup.
AUTOLINK_TOKEN = re.compile(
    r"(?P<url>\b(?i:https?)://" + TOKEN_CHARS + "+)"
    r"|(?P<doi>(?:\b(?i:doi)(?::\s?|=|\s))?(?<![\w./])10\.[0-9]{4,9}/" + TOKEN_CHARS + "+)"
    r"|(?P<pmid>\b(?i:pmid)(?::\s?|\s)(?P<pmid_number>[0-9]{1,9})\b)"
    r"|(?P<pmcid>\bPMC[0-9]{4,9}\b)"
)
CLOSING = {")": "(", "]": "[", "}": "{"}
# Sentence punctuation, and Markdown emphasis or code marks, that end a token
# without belonging to it ("**10.1099/y**", "see https://example.org/a;").
TRAILING = ".,;:!?'\"*`"


def _close_token(token: str) -> str:
    """Cut a token at the first closer that closes nothing opened inside it.

    "(https://a.example/x)-(https://b.example/y)" matches as one run of URL
    characters; the ")" after x closes the reader's parenthesis, not one in
    the URL, so the first URL ends there. Balanced pairs stay inside one URL
    ("https://en.wikipedia.org/wiki/Foo_(bar)").
    """
    depth = dict.fromkeys(CLOSING.values(), 0)
    for index, char in enumerate(token):
        if char in depth:
            depth[char] += 1
        elif char in CLOSING:
            if not depth[CLOSING[char]]:
                return token[:index]
            depth[CLOSING[char]] -= 1
    return token


def _trim_token(token: str) -> str:
    """Drop trailing punctuation, emphasis marks and unbalanced closers."""
    token = _close_token(token)
    while token:
        last = token[-1]
        if last in TRAILING or (last in CLOSING and token.count(last) > token.count(CLOSING[last])):
            token = token[:-1]
            continue
        break
    return token


def _token_url(kind: str, token: str, match: re.Match[str]) -> str | None:
    if kind == "url":
        return safe_url(token)
    if kind == "doi":
        doi = token[token.index("10."):]
        return "https://doi.org/" + quote(doi, safe="/():;") if BARE_DOI.fullmatch(doi) else None
    if kind == "pmid":
        return f"https://pubmed.ncbi.nlm.nih.gov/{match.group('pmid_number')}/"
    return f"https://pmc.ncbi.nlm.nih.gov/articles/{token}/"


def autolink(value: object) -> Markup:
    """Escape record prose and link the PMID, PMCID, DOI and http(s) URL tokens in it.

    Applied to record content only -- notes, snippets, roles, captions,
    attributions, change summaries -- so a citation is followable wherever it
    appears, not only in the structured ``reference`` slots. Only the token
    becomes the anchor; the text a reader sees is unchanged. Schema prose is
    left plain because its identifiers are format examples.
    """
    if value is None:
        return Markup("")
    if isinstance(value, Markup):
        return value
    text = str(value)
    out: list[str] = []
    position = 0
    # Not finditer: a token cut short gives the rest of its match back, and the
    # next reference may start inside it.
    match = AUTOLINK_TOKEN.search(text)
    while match:
        kind = match.lastgroup if match.lastgroup != "pmid_number" else "pmid"
        token = match.group(0)
        if kind in {"url", "doi"}:
            token = _trim_token(token)
        url = _token_url(kind, token, match) if token else None
        if not url:
            match = AUTOLINK_TOKEN.search(text, match.end())
            continue
        out.append(escape(text[position:match.start()]))
        out.append(Markup('<a href="{}">{}</a>').format(url, token))
        position = match.start() + len(token)
        match = AUTOLINK_TOKEN.search(text, position)
    out.append(escape(text[position:]))
    return Markup("").join(out)


def issue_url(identifier: str, page: str) -> str:
    """A new GitHub issue prefilled with the record it is about.

    An issue rather than an edit link: records are written only through the
    validated writer, which appends the curation event an edit made in the
    browser would skip.
    """
    return f"{GH_REPO}/issues/new?" + urlencode(
        {"title": f"Problem with {identifier}", "body": SITE_PAGES + page})


def template_environment(references: Mapping | None = None) -> Environment:
    """The Jinja environment every page is rendered with, filters included.

    Tests render single templates through this too, so a template can never
    depend on a filter only the full build registers.
    """
    if references is None:
        references = json.loads(REFERENCES.read_text(encoding="utf-8"))["references"]
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.globals["reference_labels"] = {key: item["label"] for key, item in references.items()}
    env.globals["reference_urls"] = {key: item["url"] for key, item in references.items()}
    env.globals["gh_blob"] = GH_BLOB
    env.globals["status_meanings"] = status_meanings()
    env.filters["curie_url"] = lambda identifier: (
        references[identifier]["url"] if identifier in references else curie_url(identifier))
    env.filters["term_link"] = term_link
    env.filters["autolink"] = autolink
    env.filters["projection_name"] = lambda method: PROJECTION_NAMES.get(
        str(method).lower(), str(method).upper())
    return env


def _shown_path(path: Path) -> str:
    """A file as the site names it: repository-relative, or its name if outside."""
    try:
        return path.resolve().relative_to(REPO_ROOT.resolve()).as_posix()
    except ValueError:
        return path.name


def schema_reference(schema_path: Path = SCHEMA_PATH) -> dict:
    """Readable documentation of the record schema, read from the schema itself.

    docs/SCHEMA.md is a hand-written field guide, so the site documents what
    LinkML resolves instead: every class with its induced slots (imports,
    attributes and slot_usage applied) and every enum with its permissible
    values. Declaration order, no clock: an unchanged schema renders
    byte-identically under `--check`.
    """
    from linkml_runtime.utils.schemaview import SchemaView

    view = SchemaView(str(schema_path))
    view.imports_closure()
    module_file = {}
    for name, schema in view.schema_map.items():
        source = schema_path.parent / f"{name}.yaml"
        if source.exists():
            module_file[schema.id] = _shown_path(source)
    classes = view.all_classes()
    enums = view.all_enums()
    local = list(view.all_classes(imports=False))
    ordered = local + [name for name in classes if name not in local]

    def range_kind(name: str | None) -> str:
        if name in classes:
            return "class"
        if name in enums:
            return "enum"
        return "type"

    def slot_row(slot) -> dict:
        names = [alt.range for alt in (slot.any_of or slot.exactly_one_of or []) if alt.range]
        ranges = names or [slot.range or view.schema.default_range or "string"]
        return {
            "name": slot.name,
            "ranges": [{"name": name, "kind": range_kind(name)} for name in ranges],
            # SchemaView already marks an identifier or key slot required.
            "required": bool(slot.required),
            "multivalued": bool(slot.multivalued),
            "identifier": bool(slot.identifier),
            "pattern": slot.pattern or "",
            "description": slot.description or "",
        }

    return {
        "title": view.schema.title or view.schema.name,
        "description": view.schema.description or "",
        "license": view.schema.license or "",
        "source": _shown_path(schema_path),
        "modules": sorted(set(module_file.values())),
        "classes": [{
            "name": name,
            "description": classes[name].description or "",
            "is_a": classes[name].is_a or "",
            "source": module_file.get(classes[name].from_schema, ""),
            "slots": [slot_row(slot) for slot in view.class_induced_slots(name)],
        } for name in ordered],
        "enums": [{
            "name": name,
            "description": enum.description or "",
            "source": module_file.get(enum.from_schema, ""),
            "permissible": [{"text": text, "description": value.description or "",
                             "meaning": value.meaning or ""}
                            for text, value in (enum.permissible_values or {}).items()],
        } for name, enum in enums.items()],
    }


def status_meanings(schema_path: Path = SCHEMA_PATH) -> dict[str, str]:
    """MappingStatusEnum value -> its schema description, quoted verbatim.

    What a status means is the schema's to say; the site repeats it rather than
    paraphrasing, so the two cannot drift.
    """
    import yaml

    schema = yaml.safe_load(schema_path.read_text(encoding="utf-8"))
    values = schema["enums"]["MappingStatusEnum"]["permissible_values"]
    return {name: (value or {}).get("description", "") for name, value in values.items()}


def page_name(path: Path, records_root: Path) -> str:
    rel = path.relative_to(records_root).with_suffix("")
    return "/".join(rel.parts)


def render(out_dir: Path, root_dir: Path | None = None) -> None:
    """Render pages/ into ``out_dir``; with ``root_dir``, also the files GitHub
    Pages needs at the published root (404.html)."""
    env = template_environment()

    records = load_records()
    records_root = REPO_ROOT / "data" / "structures"
    by_category: dict[str, list[dict]] = defaultdict(list)
    index = []
    timestamps: list[str] = []
    llm_assisted_records = 0
    for path, doc in records:
        name = page_name(path, records_root)
        events = doc.get("curation_history") or []
        llm_assisted_records += any(ev.get("llm_assisted") is True for ev in events)
        for ev in events:
            if ts := ev.get("timestamp"):
                timestamps.append(str(ts))
        entry = {
            "identifier": doc["identifier"],
            "label": doc["label"],
            "category": doc.get("structure_category"),
            "kind": doc.get("structure_kind"),
            "status": doc.get("mapping_status"),
            "page": f"structures/{name}.html",
            "definition": doc.get("definition", ""),
            "synonyms": " ".join(s["synonym_text"] for s in doc.get("synonyms") or []),
        }
        by_category[entry["category"]].append(entry)
        index.append(entry)

    latest_ts = max(timestamps) if timestamps else "unknown"
    corpus_date = latest_ts.replace("T", " ").replace("Z", " UTC") if "T" in latest_ts else latest_ts
    corpus_digest = hashlib.sha256(
        json.dumps([doc for _, doc in records], sort_keys=True, ensure_ascii=False).encode("utf-8")
    ).hexdigest()[:12]
    env.globals["local_records"] = {entry["identifier"]: entry for entry in index}
    env.globals["corpus_date"] = corpus_date
    env.globals["corpus_digest"] = corpus_digest
    env.globals["total_records"] = len(index)
    meanings = env.globals["status_meanings"]
    status_counts = Counter(entry["status"] for entry in index)
    # Every schema status, in the schema's order, with how many records hold it.
    # A status with no records is listed too: what REVIEWED would mean is part
    # of what PROPOSED does not.
    curation = {
        "statuses": [{"name": name, "meaning": meaning, "count": status_counts.get(name, 0)}
                     for name, meaning in meanings.items()],
        "llm_assisted_records": llm_assisted_records,
    }
    seq_map_path = EMBEDDINGS_DIR / "sequence_map.json"
    seq_method = (json.loads(seq_map_path.read_text(encoding="utf-8")).get("method")
                  if seq_map_path.exists() else None)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ".nojekyll").write_text("")
    shutil.copy(TEMPLATES_DIR / "style.css", out_dir / "style.css")
    shutil.copy(TEMPLATES_DIR / "record-browser.js", out_dir / "record-browser.js")
    # Vendored byte-identical across all seven Mech sites: reads localStorage
    # "mech-theme", sets data-theme before paint, injects the toggle button.
    shutil.copy(TEMPLATES_DIR / "theme-toggle.js", out_dir / "theme-toggle.js")

    categories = [
        {"name": c, "count": len(v), "blurb": CATEGORY_BLURB.get(c, ""), "page": f"category/{c.lower()}.html"}
        for c, v in sorted(by_category.items())
    ]
    grounded = sum(1 for e in index if str(e["identifier"]).startswith("GO:"))
    (out_dir / "index.html").write_text(
        env.get_template("index.html").render(
            categories=categories, total=len(index), grounded=grounded, root="",
            curation=curation, seq_method=seq_method,
        ),
        encoding="utf-8",
    )
    (out_dir / "schema.html").write_text(
        env.get_template("schema.html").render(schema=schema_reference(), root=""),
        encoding="utf-8",
    )
    (out_dir / "browse.html").write_text(
        env.get_template("browse.html").render(records=index, root=""), encoding="utf-8"
    )
    grounded_records = [
        entry for entry in index if str(entry["identifier"]).startswith("GO:")
    ]
    (out_dir / "grounded.html").write_text(
        env.get_template("browse.html").render(
            records=grounded_records,
            root="",
            page_title="GO-grounded structures",
            heading="GO-grounded structures",
            lede=(
                f"{len(grounded_records)} structures use an exact Gene Ontology "
                "cellular-component identifier."
            ),
        ),
        encoding="utf-8",
    )
    (out_dir / "index.json").write_text(
        json.dumps(index, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    (out_dir / "corpus.json").write_text(
        json.dumps(
            {
                "corpus": "CellStructureMech",
                "record_count": len(records),
                "corpus_updated": corpus_date,
                "corpus_digest": corpus_digest,
                "schema": "https://github.com/CultureBotAI/CellStructureMech/blob/main/src/cellstructuremech/schema/cellstructuremech.yaml",
                "records": [doc for _, doc in records],
            },
            indent=1,
            ensure_ascii=False,
        )
        + "\n",
        encoding="utf-8",
    )
    embedding_map = json.loads((EMBEDDINGS_DIR / "structure_text_map.json").read_text())
    data_dir = out_dir / "data"
    data_dir.mkdir(exist_ok=True)
    for name in ("structure_text_map.json", "structure_text_neighbors.json"):
        shutil.copy(EMBEDDINGS_DIR / name, data_dir / name)
    (out_dir / "embedding-map.html").write_text(
        env.get_template("embedding_map.html").render(
            root="", model=embedding_map["model"]
        ),
        encoding="utf-8",
    )
    if seq_map_path.exists():
        seq_map = json.loads(seq_map_path.read_text(encoding="utf-8"))
        shutil.copy(seq_map_path, data_dir / "sequence_map.json")
        (out_dir / "sequence-map.html").write_text(
            env.get_template("sequence_map.html").render(
                root="",
                seq_map=seq_map,
                seq_map_json=json.dumps(seq_map, separators=(",", ":"))
                .replace("<", "\\u003c")
                .replace("\u2028", "\\u2028")
                .replace("\u2029", "\\u2029"),
            ),
            encoding="utf-8",
        )

    for cat in categories:
        p = out_dir / cat["page"]
        p.parent.mkdir(parents=True, exist_ok=True)
        p.write_text(
            env.get_template("category.html").render(
                category=cat, records=by_category[cat["name"]], root="../"
            ),
            encoding="utf-8",
        )

    for path, doc in records:
        name = page_name(path, records_root)
        p = out_dir / "structures" / f"{name}.html"
        p.parent.mkdir(parents=True, exist_ok=True)
        # The page sits at structures/<category>/<slug>.html: the directories
        # below pages/ are structures/ plus every part of `name` except the
        # file itself, i.e. exactly len(parts). Getting this wrong (#21) sent
        # every record page one level too deep for its stylesheet and images.
        depth = len(Path(name).parts)
        # Hosted images are served from data/images/ where they are committed,
        # not copied into the page tree: GitHub Pages publishes the repository
        # root, so one copy is reachable and two were 1.3 MB of duplication
        # (#31). The page sits `depth` levels below pages/, and pages/ is one
        # below the root.
        root = "../" * depth
        img_base = f"{root}../data/images/{path.parent.name}/{path.stem}/"
        p.write_text(
            env.get_template("structure.html").render(
                r=doc, root=root, source_path=path.relative_to(REPO_ROOT).as_posix(),
                img_base=img_base, report_url=issue_url(doc["identifier"], f"structures/{name}.html"),
            ),
            encoding="utf-8",
        )

    if root_dir is not None:
        # GitHub Pages answers every missing address on the site with the
        # repository-root 404.html, at whatever depth was asked for, so its
        # links and assets are site-root-absolute (/CellStructureMech/pages/...).
        root_dir.mkdir(parents=True, exist_ok=True)
        (root_dir / NOT_FOUND).write_text(
            env.get_template("not_found.html").render(root=SITE_PATH), encoding="utf-8"
        )


def _tree_differs(a: Path, b: Path) -> list[str]:
    diffs: list[str] = []

    def walk(cmp: filecmp.dircmp, prefix: str) -> None:
        diffs.extend(f"{prefix}{n}" for n in cmp.left_only + cmp.right_only + cmp.diff_files)
        for name, sub in cmp.subdirs.items():
            walk(sub, f"{prefix}{name}/")

    walk(filecmp.dircmp(a, b), "")
    return diffs


def _root_files_differ(fresh_root: Path, published_root: Path) -> list[str]:
    """Root-level files a fresh render made that the published root lacks or holds stale."""
    committed = published_root / NOT_FOUND
    fresh = fresh_root / NOT_FOUND
    if committed.is_file() and committed.read_bytes() == fresh.read_bytes():
        return []
    return [f"../{NOT_FOUND}"]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument("--check", action="store_true", help="Render to a temp dir and diff against --out.")
    args = parser.parse_args()
    # Root files belong to the published site, not to an arbitrary --out.
    publishes_root = args.out.resolve() == PAGES_DIR.resolve()

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            fresh = Path(tmp) / "pages"
            render(fresh, root_dir=Path(tmp))
            if not args.out.exists():
                print(f"{args.out} does not exist; run `just render`", file=sys.stderr)
                return 1
            diffs = _tree_differs(fresh, args.out)
            if publishes_root:
                diffs += _root_files_differ(Path(tmp), REPO_ROOT)
        if diffs:
            print(f"pages/ is stale ({len(diffs)} file(s) differ), e.g. {diffs[:5]}; run `just render`",
                  file=sys.stderr)
            return 1
        print("pages/ is current")
        return 0

    if args.out.exists():
        shutil.rmtree(args.out)
    render(args.out, root_dir=REPO_ROOT if publishes_root else None)
    print(f"rendered site under {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
