"""Keep septin wording aligned with the cited evidence and biological scope."""

from pathlib import Path

import yaml

ROOT = Path(__file__).resolve().parents[1] / "data/structures/cytoskeleton"
AN_REFERENCE = "DOI:10.1091/mbc.E04-07-0640"


def test_spn_copy_number_distinguishes_observation_from_model():
    record = yaml.safe_load((ROOT / "septin_complex.yaml").read_text())
    scope = record["taxonomic_distribution"][0]
    assert scope["taxon_id"] == "NCBITaxon:4896"
    assert scope["reference"] == AN_REFERENCE
    assert "at least two copies" in scope["note"]
    assert "proposed" in scope["note"] and "two-copy-per-subunit model" in scope["note"]
    assert "remained to be proven rigorously" in scope["note"]


def test_band_definition_uses_growth_without_changing_context():
    record = yaml.safe_load((ROOT / "septin_band.yaml").read_text())
    assert "polarized grown" not in record["definition"]
    assert "polarized growth" in record["definition"]
    assert "but not with cytokinesis" in record["definition"]
    assert "shmoo (mating projection) neck" in record["definition"]
    assert record["identifier"] == record["definition_source"] == "GO:0032158"


def test_complex_model_is_not_universalized_to_generic_graph():
    record = yaml.safe_load((ROOT / "septin_complex.yaml").read_text())
    assert record["identifier"] == record["definition_source"] == "GO:0031105"
    assert record["parent_structures"] == ["GO:0032991"]
    assert record["canonical_examples"][0]["reference"] == AN_REFERENCE
    graph = record["causal_graphs"][0]
    assert graph["scope_status"] == "NONMECHANISTIC"
    assert "without asserting a fixed subunit order, stoichiometry" in graph["scope_notes"]
    assert "two copies" not in yaml.safe_dump(graph)
