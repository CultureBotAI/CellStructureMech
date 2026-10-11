"""Keep discussion provenance when axonemal child-record boundaries change."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"


def record(slug):
    return yaml.safe_load((ROOT / f"{slug}.yaml").read_text())


def test_doublet_retains_original_and_intermediate_rationales():
    doc = record("axonemal_doublet_microtubule")
    d = doc["discussions"][0]
    assert d["rationale"].startswith(
        "GO now identifies multiple named doublet substructures, and cryo-EM "
        "has mapped many Chlamydomonas MIPs, but this first GO:0097545 pass "
        "curates only the coarse A/B doublet scaffold."
    )
    for revision in ("1a6f714581ad", "5b2752fe91a2", "8885f3fcea2c", "16734f1265fe"):
        assert f"Historical reassessment at git {revision}:" in d["rationale"]
    assert "GO:0160115 ribbon now have child records" in d["rationale"]
    assert d["status"] == "OPEN" and d["posed_date"] == "2026-09-23"
    assert d["attaches_to"] == ["causal_graphs#chlamydomonas_doublet_scaffold"]
    assert d["prompt"] == (
        "Resolve exact source-neutral groundings for remaining doublet-specific "
        "accessory structures, and decide which ones need child records."
    )
    assert set(doc["has_part"]) == {
        "GO:0097649", "GO:0097650", "GO:0160110",
        "GO:0160113", "GO:0160114", "GO:0160115",
    }
    assert len(doc["causal_graphs"][0]["edges"]) == 5


def test_inner_sheath_keeps_resolved_split_and_original_ab_context():
    doc = record("axonemal_microtubule_doublet_inner_sheath")
    mip, split = doc["discussions"]
    assert split["rationale"].startswith(
        "GO exactly identifies the A- and B-tubule inner sheaths, but the present "
        "GO:0160110 record keeps them as child GO terms while their component "
        "boundaries and taxon-general MIP family identities remain unresolved."
    )
    assert "Historical reassessment at git d13891318477:" in split["rationale"]
    assert "GO exactly identifies the B-tubule inner sheath" in split["rationale"]
    assert "resolve_a_b_inner_sheath_children" in split["notes"]
    assert split["discussion_id"] == "resolve_b_inner_sheath_child_record"
    assert split["status"] == "RESOLVED"
    assert split["posed_date"] == split["resolved_date"] == "2026-09-23"
    assert split["resolution_note"] == (
        "GO:0160112 was promoted to its own axonemal B tubule inner sheath record "
        "and linked from the B axonemal microtubule parent. Exact B-lumen "
        "MIP-family groundings, positions and copy numbers remain open on the "
        "child record's resolve_b_tubule_inner_sheath_mips TODO."
    )
    assert mip["discussion_id"] == "resolve_inner_sheath_mip_groundings"
    assert mip["status"] == "OPEN" and mip["posed_date"] == "2026-09-23"
    assert doc["has_part"] == ["GO:0160111", "GO:0160112"]
    assert len(doc["causal_graphs"][0]["edges"]) == 4


def test_axoneme_retains_all_rationale_versions_and_live_scope():
    doc = record("axoneme")
    d = doc["discussions"][0]
    assert d["rationale"].startswith(
        "The Chlamydomonas axoneme has many named regulatory, projection, and "
        "microtubule-associated complexes. This first record curates coarse "
        "substructure classes until their exact complex-level boundaries can "
        "be reviewed."
    )
    for revision in (
        "0b7c77d1f1d0", "3304899aaa6f", "e7aa953abdb8",
        "7102642edca7", "9f7ca79bbf4d", "8b410f98eccd",
    ):
        assert f"Historical reassessment at git {revision}:" in d["rationale"]
    assert "axonemal nexin link now have GO-backed child-record boundaries" in d["rationale"]
    assert d["status"] == "OPEN" and d["posed_date"] == "2026-09-11"
    assert d["prompt"] == (
        "Resolve exact source-neutral groundings and boundaries for additional "
        "Chlamydomonas axoneme subcomplexes."
    )
    assert not d.get("attaches_to")
    assert len(doc["has_part"]) == 6
    assert len(doc["causal_graphs"][0]["edges"]) == 7
    assert "motile" not in doc["definition"].lower()
