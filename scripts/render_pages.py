#!/usr/bin/env python3
"""Render the browsable site under pages/ from data/structures/.

Generated, committed, and served from `main`, matching the sibling Mech
repos. Regenerate with `just render`; `--check` fails when the committed
output is out of step with the corpus.

Usage:
    python scripts/render_pages.py
    python scripts/render_pages.py --out /tmp/site --check
"""

from __future__ import annotations

import argparse
import filecmp
import json
import shutil
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

from corpus import REPO_ROOT, load_records
from jinja2 import Environment, FileSystemLoader, select_autoescape

TEMPLATES_DIR = REPO_ROOT / "src" / "cellstructuremech" / "templates"
IMAGES_DIR = REPO_ROOT / "data" / "images"
EMBEDDINGS_DIR = REPO_ROOT / "data" / "embeddings"
PAGES_DIR = REPO_ROOT / "pages"

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
    "InterPro": "https://www.ebi.ac.uk/interpro/entry/InterPro/",
    "Pfam": "https://www.ebi.ac.uk/interpro/entry/pfam/",
    "UniProtKB": "https://www.uniprot.org/uniprotkb/",
    "ComplexPortal": "https://www.ebi.ac.uk/complexportal/complex/",
    "RNAcentral": "https://rnacentral.org/rna/",
    "ECO": "http://purl.obolibrary.org/obo/ECO_",
    "PDB": "https://www.rcsb.org/structure/",
    "EMDB": "https://www.ebi.ac.uk/emdb/",
    "EMPIAR": "https://www.ebi.ac.uk/empiar/EMPIAR-",
    "CryoETDataPortal": "https://cryoetdataportal.czscience.com/datasets/",
    "PMID": "https://pubmed.ncbi.nlm.nih.gov/",
    "DOI": "https://doi.org/",
    "METPO": "https://w3id.org/metpo/",
    "traitmech": "https://w3id.org/traitmech/",
    "MICRO": "http://purl.obolibrary.org/obo/MICRO_",
}


def curie_url(curie: str) -> str | None:
    if ":" not in curie:
        return None
    prefix, local = curie.split(":", 1)
    base = PREFIX_URL.get(prefix)
    return f"{base}{local}" if base else None


def page_name(path: Path, records_root: Path) -> str:
    rel = path.relative_to(records_root).with_suffix("")
    return "/".join(rel.parts)


def render(out_dir: Path) -> None:
    env = Environment(
        loader=FileSystemLoader(str(TEMPLATES_DIR)),
        autoescape=select_autoescape(["html"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )
    env.filters["curie_url"] = curie_url

    records = load_records()
    records_root = REPO_ROOT / "data" / "structures"
    by_category: dict[str, list[dict]] = defaultdict(list)
    index = []
    for path, doc in records:
        name = page_name(path, records_root)
        entry = {
            "identifier": doc["identifier"],
            "label": doc["label"],
            "category": doc.get("structure_category"),
            "kind": doc.get("structure_kind"),
            "status": doc.get("mapping_status"),
            "page": f"structures/{name}.html",
            "definition": doc.get("definition", ""),
        }
        by_category[entry["category"]].append(entry)
        index.append(entry)

    out_dir.mkdir(parents=True, exist_ok=True)
    (out_dir / ".nojekyll").write_text("")
    shutil.copy(TEMPLATES_DIR / "style.css", out_dir / "style.css")
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
            categories=categories, total=len(index), grounded=grounded, root=""
        ),
        encoding="utf-8",
    )
    (out_dir / "browse.html").write_text(
        env.get_template("browse.html").render(records=index, root=""), encoding="utf-8"
    )
    (out_dir / "index.json").write_text(
        json.dumps(index, indent=1, ensure_ascii=False) + "\n", encoding="utf-8"
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
                r=doc, root=root, source_path=str(path.relative_to(REPO_ROOT)),
                img_base=img_base,
            ),
            encoding="utf-8",
        )


def _tree_differs(a: Path, b: Path) -> list[str]:
    diffs: list[str] = []

    def walk(cmp: filecmp.dircmp, prefix: str) -> None:
        diffs.extend(f"{prefix}{n}" for n in cmp.left_only + cmp.right_only + cmp.diff_files)
        for name, sub in cmp.subdirs.items():
            walk(sub, f"{prefix}{name}/")

    walk(filecmp.dircmp(a, b), "")
    return diffs


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--out", type=Path, default=PAGES_DIR)
    parser.add_argument("--check", action="store_true", help="Render to a temp dir and diff against --out.")
    args = parser.parse_args()

    if args.check:
        with tempfile.TemporaryDirectory() as tmp:
            render(Path(tmp))
            if not args.out.exists():
                print(f"{args.out} does not exist; run `just render`", file=sys.stderr)
                return 1
            diffs = _tree_differs(Path(tmp), args.out)
        if diffs:
            print(f"pages/ is stale ({len(diffs)} file(s) differ), e.g. {diffs[:5]}; run `just render`",
                  file=sys.stderr)
            return 1
        print("pages/ is current")
        return 0

    if args.out.exists():
        shutil.rmtree(args.out)
    render(args.out)
    print(f"rendered site under {args.out}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
