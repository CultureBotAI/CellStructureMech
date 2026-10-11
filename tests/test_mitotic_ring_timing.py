"""Keep budding-yeast precursor timing separate from the actomyosin ring."""

from pathlib import Path

import pytest
import yaml

RECORD = (
    Path(__file__).resolve().parents[1]
    / "data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml"
)
BI_REFERENCE = "DOI:10.1083/jcb.142.5.1301"


@pytest.fixture
def record():
    return yaml.safe_load(RECORD.read_text())


def test_budding_yeast_precursor_and_actin_have_distinct_timing(record):
    definition = record["definition"]
    assert "before mitosis" not in definition
    assert "Saccharomyces cerevisiae" in definition
    assert "Myo1" in definition and "before bud emergence" in definition
    assert "future bud site" in definition
    assert "actin joins" in definition and "near the end of anaphase" in definition


def test_timing_qualification_has_primary_evidence_and_source_conflict(record):
    assert any(e["reference"] == BI_REFERENCE for e in record["evidence"])
    discussion = next(
        d for d in record["discussions"]
        if d["discussion_id"] == "budding_yeast_mitotic_ring_timing"
    )
    assert discussion["kind"] == "INTERPRETATION"
    assert discussion["status"] == "RESOLVED"
    assert discussion["attaches_to"] == ["definition"]
    assert {e["reference"] for e in discussion["evidence"]} >= {
        "GO:0110085", BI_REFERENCE,
    }
    assert "before mitosis" in discussion["rationale"]
    assert "anaphase" in discussion["rationale"]
    assert "no upstream GO correction" in discussion["resolution_note"]


def test_budding_timing_does_not_replace_fission_yeast_model(record):
    assert record["identifier"] == record["definition_source"] == "GO:0110085"
    assert record["parent_structures"] == ["GO:0005826"]
    assert record["mapping_status"] == "PROPOSED"
    assert {e["taxon_id"] for e in record["canonical_examples"]} == {"NCBITaxon:4896"}
    assert record["canonical_examples"][0]["reference"] == "DOI:10.1083/jcb.200602032"
    graph = record["causal_graphs"][0]
    assert graph["graph_id"] == "fission_yeast_mitotic_ring_topology"
    assert graph["scope_status"] == "NONMECHANISTIC"
    assert {e["subject"] for e in graph["edges"]} == {"actin_filaments", "myosin_proteins"}
    assert all(e["predicate"] == "contributes to" for e in graph["edges"])
    assert "Myo1" not in yaml.safe_dump(graph)
