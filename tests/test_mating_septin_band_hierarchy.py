"""Keep the diffuse shmoo-neck band distinct from its containing framework."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"


def test_mating_band_uses_the_generic_band_as_its_is_a_parent():
    record = yaml.safe_load((ROOT / "mating_projection_septin_band.yaml").read_text())
    assert record["parent_structures"] == ["GO:0032158"]
    assert any(e["reference"] == "GO:0032158" for e in record["evidence"])


def test_mating_band_retains_projection_and_cytoskeleton_parthood():
    record = yaml.safe_load((ROOT / "mating_projection_septin_band.yaml").read_text())
    assert set(record["part_of"]) == {"GO:0005937", "GO:0032156"}
    assert len(record["part_of"]) == 2
    assert "GO:0032156" not in record["parent_structures"]


def test_mating_band_and_ring_remain_distinct_structures():
    band = yaml.safe_load((ROOT / "mating_projection_septin_band.yaml").read_text())
    ring = yaml.safe_load((ROOT / "mating_projection_septin_ring.yaml").read_text())
    assert band["identifier"] == band["definition_source"] == "GO:0032162"
    assert ring["identifier"] == ring["definition_source"] == "GO:0032175"
    assert ring["parent_structures"] == ["GO:0005940"]
    assert band["causal_graphs"][0]["scope_status"] == "NONMECHANISTIC"
