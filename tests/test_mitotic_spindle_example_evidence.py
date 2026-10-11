"""Keep mitotic-spindle examples within their claim-local source evidence."""

from pathlib import Path

import pytest
import yaml

RECORD = (
    Path(__file__).resolve().parents[1]
    / "data/structures/cytoskeleton/mitotic_spindle.yaml"
)
WINEY = "DOI:10.1083/jcb.129.6.1601"
STRAIGHT = "DOI:10.1126/science.277.5325.574"


@pytest.fixture
def record():
    return yaml.safe_load(RECORD.read_text())


@pytest.mark.parametrize("section", ["taxonomic_distribution", "canonical_examples"])
def test_winey_only_example_describes_fixed_sample_reconstruction(record, section):
    example = record[section][0]
    assert example["taxon_id"] == "NCBITaxon:4932"
    assert example["reference"] == WINEY
    note = example["note"].lower()
    assert not any(phrase in note for phrase in ("living", "in vivo", "tracked"))
    assert "serial-section electron microscopy" in note
    assert "reconstructed" in note


def test_live_cell_evidence_remains_on_component_and_function(record):
    for section, key, identifier in (
        ("components", "component_id", "alpha_beta_tubulins"),
        ("functions", "function_id", "chromosome_segregation"),
    ):
        item = next(item for item in record[section] if item[key] == identifier)
        evidence = next(e for e in item["evidence"] if e["reference"] == STRAIGHT)
        assert "living" in evidence["notes"]
