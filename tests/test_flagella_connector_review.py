"""Keep connector attachment geometry distinct from distal axonemal caps."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1]


def connector():
    return yaml.safe_load(
        (ROOT / "data/structures/appendage/flagella_connector.yaml").read_text()
    )


def test_connector_couples_new_tip_to_old_shaft_with_claim_specific_sources():
    doc = connector()
    functions = {f["function_id"]: f for f in doc["functions"]}
    assert "flank of the old flagellum" in functions["new_to_old_flagellum_linkage"]["description"]
    coupling = functions["distal_flagellar_tip_coupling"]
    assert coupling["label"] == "new-tip to old-shaft microtubule coupling"
    assert "extending microtubule tips in the assembling new flagellum" in coupling["description"]
    assert "lateral shaft of the mature old flagellum" in coupling["description"]
    sources = {e["reference"]: e["notes"] for e in coupling["evidence"]}
    assert "kinesin-15" in sources["DOI:10.1073/pnas.1703553114"]
    assert "does not place the old-side attachment at the old distal tip" in sources[
        "DOI:10.1073/pnas.1703553114"
    ]
    assert "lateral side of the old flagellum" in sources["DOI:10.1371/journal.pntd.0004312"]


def test_spatial_correction_does_not_claim_complete_molecular_identity():
    doc = connector()
    assert doc["identifier"] == "GO:0120118"
    assert doc["mapping_status"] == "PROPOSED"
    assert not doc.get("components")
    assert not doc.get("causal_graphs")
    discussions = {d["discussion_id"]: d for d in doc["discussions"]}
    inventory = discussions["curate_flagella_connector_components"]
    assert inventory["status"] == "OPEN"
    assert "seven flagella-connector constituents" in inventory["rationale"]
    assert "three axonemal-capping-structure constituents" in inventory["rationale"]
    assert discussions["resolve_connector_motility_mechanism"]["status"] == "OPEN"
