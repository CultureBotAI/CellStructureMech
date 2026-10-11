"""Keep filament hierarchy, primary citations and retained components explicit."""

import hashlib
import json
from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(slug):
    return yaml.safe_load((ROOT / f"data/structures/cytoskeleton/{slug}.yaml").read_text())


def references(value):
    if isinstance(value, dict):
        if "reference" in value:
            yield value["reference"]
        for child in value.values():
            yield from references(child)
    elif isinstance(value, list):
        for child in value:
            yield from references(child)


def test_a_tubule_preserves_original_rationale_and_current_scope():
    doc = record("a_axonemal_microtubule")
    discussion = doc["discussions"][0]
    original = (
        "GO exactly identifies the A axonemal microtubule, but this pass curates "
        "only its coarse role in the outer doublet and leaves exact protofilament, MIP, "
        "radial-spoke and dynein-arm attachment placement unresolved."
    )
    assert discussion["rationale"].startswith(original)
    assert "Reassessment on" in discussion["rationale"]
    assert "GO:0160111 now captures" in discussion["rationale"]
    assert "non-inner-sheath" in discussion["prompt"]
    assert discussion["posed_date"] == "2026-09-23"
    assert discussion["status"] == "OPEN"
    assert "GO:0160111" in doc["has_part"]
    nodes = {n.get("grounding") for n in doc["causal_graphs"][0]["nodes"]}
    assert {"GO:0001534", "GO:0036156", "GO:0036157"} <= nodes


def test_patch_separates_is_a_from_cytoskeleton_parthood():
    doc = record("actin_cortical_patch")
    assert doc["parent_structures"] == ["GO:0061645"]
    assert {"GO:0030864", "GO:0005938"} <= set(doc["part_of"])
    assert {"GO:0061645", "GO:0030864"} <= set(references(doc["evidence"]))
    graph = doc["causal_graphs"][0]
    assert graph["graph_kind"] == "ASSEMBLY"
    assert "endocytic_internalization" not in {n["node_id"] for n in graph["nodes"]}
    arp = next(c for c in doc["components"] if c["component_id"] == "arp2_3_complex")
    assert "DOI:10.1371/journal.pbio.0060001" not in set(references(arp))


def test_ring_cdc12_is_a_retained_constituent():
    doc = record("actomyosin_contractile_ring")
    cdc12 = next(c for c in doc["components"] if c["component_id"] == "cdc12_formin_family")
    assert cdc12["component_role"] == "CONSTITUENT"
    assert "ring" in cdc12["role"]
    assert "DOI:10.1083/jcb.200602032" in set(references(cdc12))
    assert cdc12["gene_symbols"] == ["cdc12"]
    assert cdc12["grounding_status"] == "REVIEWED_LABEL_ONLY"
    assert "DOI:10.1016/S1534-5807(03)00324-1" in set(references(doc["functions"]))
    assert doc["discussions"][0]["status"] == "OPEN"


def test_alfa_sites_cite_the_alfA_study_not_parm():
    doc = record("alfa_filament")
    refs = list(references(doc))
    assert "DOI:10.1016/j.str.2009.07.008" not in refs
    intended = "DOI:10.1128/JB.00676-09"
    assert refs.count(intended) == 4
    for site in (doc["components"][0], doc["evidence"],
                 doc["causal_graphs"][0]["edges"][0], doc["discussions"][0]):
        assert intended in set(references(site))
    bibliographic = next(e for e in doc["evidence"] if e["reference"] == intended)
    assert "Journal of Bacteriology" in bibliographic["notes"]


def test_alfa_is_a_fiber_and_part_of_cytoskeleton():
    doc = record("alfa_filament")
    assert doc["identifier"] == "cellstructuremech:alfa_filament"
    assert doc["parent_structures"] == ["GO:0099513"]
    assert "GO:0005856" in doc["part_of"]
    assert {"GO:0099513", "GO:0005856"} <= set(references(doc["evidence"]))
    assert [c["component_id"] for c in doc["components"]] == ["alfa"]
    graph = doc["causal_graphs"][0]
    assert len(graph["edges"]) == 3
    assert any(n["node_id"] == "alfb_parn_complex" for n in graph["nodes"])


def test_alfa_becker_citation_does_not_invent_authors():
    doc = record("alfa_filament")
    note = next(e["notes"] for e in doc["evidence"]
                if e["reference"] == "DOI:10.1038/sj.emboj.7601443")
    assert "Becker et al. 2006" in note
    assert "Moller-Jensen" not in note
    assert "Gerdes" not in note


def test_new_hierarchy_labels_have_retained_authority_sources():
    from scripts.build_website_references import GO_RELATIONSHIP_TERMS

    snapshot = json.loads((ROOT / "data/website/references.json").read_text())
    expected = {
        "0030864": "cortical actin cytoskeleton",
        "0061645": "endocytic patch",
        "0099513": "polymeric cytoskeletal fiber",
    }
    for number, label in expected.items():
        assert number in GO_RELATIONSHIP_TERMS
        name = f"go-{number}.json"
        entry = snapshot["references"][f"GO:{number}"]
        assert entry["label"] == label
        assert entry["source"] == name
        source = next(s for s in snapshot["sources"] if s["file"] == name)
        path = ROOT / "reports/website_reference_sources/20261011-cytoskeleton" / name
        assert hashlib.sha256(path.read_bytes()).hexdigest() == source["sha256"]
        term, = json.loads(path.read_text())["_embedded"]["terms"]
        assert term["obo_id"] == f"GO:{number}"
        assert term["label"] == label
        assert term["is_obsolete"] is False
