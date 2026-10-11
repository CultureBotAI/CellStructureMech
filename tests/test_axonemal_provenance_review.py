"""Preserve axonemal discussion history and distinguish ontology source conflicts."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"


def record(slug):
    return yaml.safe_load((ROOT / f"{slug}.yaml").read_text())


def test_b_sheath_retains_biology_and_exposes_go_source_discrepancy():
    doc = record("axonemal_b_tubule_inner_sheath")
    assert doc["identifier"] == "GO:0160112"
    assert doc["part_of"] == ["GO:0160110", "GO:0097650"]
    note = next(e["notes"] for e in doc["evidence"] if e["reference"] == "GO:0097650")
    assert "not by its current typed GO parthood edge" in note
    conflict = next(d for d in doc["discussions"]
                    if d["discussion_id"] == "b_inner_sheath_go_relationship_discrepancy")
    assert conflict["status"] == "OPEN"
    assert "GO:0097649" in conflict["rationale"]
    assert "GO:0097650" in conflict["rationale"]
    assert "DOI:10.1016/j.cell.2019.09.030" in {e["reference"] for e in conflict["evidence"]}
    mip = next(d for d in doc["discussions"]
               if d["discussion_id"] == "resolve_b_tubule_inner_sheath_mips")
    assert mip["status"] == "OPEN" and mip["posed_date"] == "2026-09-23"
    graph = doc["causal_graphs"][0]
    assert graph["scope_status"] == "NONMECHANISTIC"
    assert [e["predicate"] for e in graph["edges"]] == ["is part of", "occupies lumen of", "stabilizes"]


def test_apparatus_preserves_rationale_versions_and_current_scope():
    doc = record("axonemal_central_apparatus")
    d = doc["discussions"][0]
    original = (
        "GO exactly identifies the axonemal central apparatus and the C1 and C2 "
        "axonemal microtubules, but no exact source-neutral term was verified for "
        "the broader central projection or bridge classes, central-pair caps, "
        "or named projection subcomplexes."
    )
    assert d["rationale"].startswith(original)
    assert "Historical reassessment at git 0f8108780c5c" in d["rationale"]
    assert "Historical reassessment at git 81057840432d" in d["rationale"]
    assert "Historical reassessment at git 11903e2fbf98" in d["rationale"]
    assert "GO exactly identifies the axonemal central pair, central bridge" in d["rationale"]
    assert d["posed_date"] == "2026-09-23" and d["status"] == "OPEN"
    assert d["prompt"] == (
        "Resolve exact source-neutral groundings for central-pair cap "
        "and named projection subcomplex classes."
    )
    assert d["attaches_to"] == ["causal_graphs#chlamydomonas_central_apparatus_architecture"]
    assert doc["has_part"] == ["GO:0097540", "GO:1990717", "GO:1990718"]
    assert all(e["predicate"] == "is part of" for e in doc["causal_graphs"][0]["edges"])


def test_central_pair_keeps_resolved_split_and_open_child_handoff():
    doc = record("axonemal_central_pair")
    d = next(d for d in doc.get("discussions", [])
             if d["discussion_id"] == "resolve_c1_c2_microtubule_children")
    original = (
        "GO exactly identifies the C1 and C2 axonemal microtubules, but this pass "
        "only curates their parent GO:0097540 central pair and leaves the "
        "individual asymmetric microtubules for later records."
    )
    assert d["rationale"].startswith(original)
    assert (
        "GO exactly identifies the C2 axonemal microtubule, "
        "but this pass leaves the second asymmetric microtubule"
    ) in d["rationale"]
    assert d["status"] == "RESOLVED" and d["posed_date"] == "2026-09-23"
    assert d["posed_by"] == "codex" and d["resolved_date"] >= "2026-10-11"
    assert "Only the child-record split is resolved" in d["resolution_note"]
    for child, discussion in (
        ("c1_axonemal_microtubule", "resolve_c1_projection_and_wall_boundaries"),
        ("c2_axonemal_microtubule", "resolve_c2_projection_mip_and_wall_boundaries"),
    ):
        assert discussion in d["resolution_note"]
        assert next(x for x in record(child)["discussions"]
                    if x["discussion_id"] == discussion)["status"] == "OPEN"
    assert "resolve_c2_microtubule_child" in d["notes"]
    assert doc["has_part"] == ["GO:1990719", "GO:1990720"]
    assert len(doc["causal_graphs"][0]["edges"]) == 6
