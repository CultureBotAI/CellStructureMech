"""2026-11-16: preserve PR #1069's graph change on the current CellStructure base.

Inputs: source snapshots from PR head 86977e21f86f902505c6f7061c097f662191b196,
verified against Git blob IDs; prepared isolated worktree at base 7a5ef9e.
Outputs: graph module/tests, minimal renderer/template hooks, and provenance.
No corpus writes. Regenerated pages are produced later by native `just render`.
Default is a dry run; --apply writes only the explicitly named files.
"""

import argparse
import hashlib
import json
import os
from pathlib import Path


def blob_sha(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--source", type=Path, required=True)
    parser.add_argument("--worktree", type=Path, required=True)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args()
    source, root = args.source.resolve(), args.worktree.resolve()
    pins = {
        "scripts/mechanism_graph.py": "17f992d0ebec98327f8844b02047f24277dc315b",
        "tests/test_mechanism_graph.py": "72801029851c497f124fc29ffa1e56bfc82766be",
    }
    writes = {}
    for name, expected in pins.items():
        data = (source / name).read_bytes()
        assert blob_sha(data) == expected, name
        assert not (root / name).exists(), name
        writes[name] = data
    renderer = root / "scripts/render_pages.py"
    data = renderer.read_text()
    assert blob_sha(data.encode()) == "652561c91f0bf05f637bc29da41b10fab66e8a02"
    needle = "from jinja2 import Environment, FileSystemLoader, select_autoescape\n"
    assert data.count(needle) == 1
    hook = (
        "\nif __package__:\n    from .mechanism_graph import graph_svg\n"
        "else:\n    from mechanism_graph import graph_svg\n"
    )
    data = data.replace(needle, needle + hook)
    needle = '    env.filters["curie_url"] = curie_url\n'
    assert data.count(needle) == 1
    data = data.replace(needle, '    env.filters["graph_svg"] = graph_svg\n' + needle)
    writes["scripts/render_pages.py"] = data.encode()
    template = root / "src/cellstructuremech/templates/structure.html"
    data = template.read_text()
    assert blob_sha(data.encode()) == "213873ab28b23ab80095b2b194104031923e32e6"
    needle = "{% if g.description %}<p>{{ g.description }}</p>{% endif %}\n"
    assert data.count(needle) == 1
    data = data.replace(needle, needle + "{{ g | graph_svg(loop.index) }}\n")
    writes["src/cellstructuremech/templates/structure.html"] = data.encode()
    provenance = {
        "date": "2026-11-16",
        "issue_or_pr": "https://github.com/CultureBotAI/CellStructureMech/pull/1069",
        "source_head": "86977e21f86f902505c6f7061c097f662191b196",
        "base_head": "7a5ef9e01fe8e8bc44f649d94b61b4b2bab5ef2b",
        "purpose": (
            "Port graph diagrams while preserving current-main page/reference enhancements; "
            "regenerate all pages to repair historical drift."
        ),
        "source_blob_ids": pins,
        "outputs_at_port_time": {
            name: hashlib.sha256(content).hexdigest() for name, content in writes.items()
        },
        "records_changed": False,
    }
    writes["scripts/adhoc/steward-graph-pr1069-20261116/port_graph_canary.py"] = Path(__file__).read_bytes()
    receipt = (json.dumps(provenance, indent=2) + "\n").encode()
    writes["scripts/adhoc/steward-graph-pr1069-20261116/provenance.json"] = receipt
    print(json.dumps({"apply": args.apply, "files": list(writes), "provenance": provenance}, indent=2))
    if args.apply:
        for name, content in writes.items():
            destination = root / name
            destination.parent.mkdir(parents=True, exist_ok=True)
            temporary = destination.with_name(destination.name + ".steward-new")
            with temporary.open("xb") as stream:
                stream.write(content)
            os.replace(temporary, destination)


if __name__ == "__main__":
    main()
