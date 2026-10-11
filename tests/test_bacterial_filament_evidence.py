"""Evidence boundaries identified in the bacterial-filament record review."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SLUGS = (
    "mreb_filament",
    "mamk_filament",
    "parm_filament",
    "bactofilin_filament",
    "crescentin_filament",
)


def record(slug):
    return yaml.safe_load(
        (ROOT / "data" / "structures" / "cytoskeleton" / f"{slug}.yaml").read_text()
    )


@pytest.mark.parametrize("slug", SLUGS)
def test_individual_filament_is_fiber_with_framework_parthood(slug):
    data = record(slug)
    assert data["parent_structures"] == ["GO:0099513"]
    assert data["part_of"] == ["GO:0005856"]
    assert {"GO:0099513", "GO:0005856"} <= {
        item["reference"] for item in data["evidence"]
    }


@pytest.mark.parametrize("slug", SLUGS)
def test_specific_identity_and_review_status_are_preserved(slug):
    data = record(slug)
    assert data["identifier"] == f"cellstructuremech:{slug}"
    assert data["mapping_status"] == "PROPOSED"
    assert data["structure_kind"] == "FILAMENT"


def test_mreb_occurrence_is_not_inferred_from_archaeal_actin_fold():
    data = record("mreb_filament")
    assert [row["taxon_id"] for row in data["taxonomic_distribution"]] == [
        "NCBITaxon:2"
    ]
    note = next(
        row for row in data["discussions"]
        if row["discussion_id"] == "archaeal_actin_fold_is_not_filament_occurrence"
    )
    assert "without asserting absence" in note["resolution_note"]
    assert "direct identity and assembly evidence" in note["resolution_note"]


def test_mreb_modern_definition_and_synthase_have_claim_local_support():
    data = record("mreb_filament")
    assert data["definition_source"] == "DOI:10.1016/j.cell.2018.02.050"
    graph = data["causal_graphs"][0]
    assert [(e["subject"], e["predicate"], e["object"]) for e in graph["edges"]] == [
        ("mreb", "polymerizes into", "mreb_filament"),
        ("rodz", "couples", "elongasome"),
        ("mreb_filament", "orients", "elongasome"),
        ("elongasome", "carries out", "sidewall_synthesis"),
        ("sidewall_synthesis", "maintains", "rod_shape"),
    ]
    assert {"DOI:10.1038/nrmicro2677", "DOI:10.1038/nmicrobiol.2016.172"} <= {
        e["reference"] for e in graph["edges"][3]["evidence"]
    }


def test_mreb_existing_trait_quotes_and_component_boundaries_remain():
    data = record("mreb_filament")
    assert [c["component_id"] for c in data["components"]] == [
        "mreb", "elongasome_link"
    ]
    assert data["components"][1]["component_role"] == "ASSOCIATED_MACHINERY"
    assert data["components"][1]["essentiality"] == "CONDITIONAL"
    quotes = [
        e["snippet"] for trait in data["associated_traits"] for e in trait["evidence"]
    ]
    assert len(quotes) == 3
    assert "Actinobacteria and Rhizobiales" in quotes[1]
    assert "MreB both senses and changes cell shape" in quotes[2]


def test_bactofilin_family_is_not_bacteria_exclusive():
    data = record("bactofilin_filament")
    assert "Bacteria-specific" not in data["components"][0]["role"]
    assert data["definition"].startswith("A cytoskeletal filament")
    assert data["definition_source"] == "DOI:10.1038/s41564-019-0544-0"


def test_pibac_in_vitro_support_does_not_become_native_occurrence():
    data = record("bactofilin_filament")
    note = next(
        row for row in data["discussions"]
        if row["discussion_id"] == "bactofilin_family_not_bacteria_exclusive"
    )
    assert "in vitro" in note["rationale"]
    assert "no native oomycete or archaeal occurrence is added" in note["resolution_note"]
    assert [row["taxon_id"] for row in data["taxonomic_distribution"]] == [
        "NCBITaxon:2", "NCBITaxon:155892"
    ]
    assert data["canonical_examples"][0]["taxon_id"] == "NCBITaxon:565050"
    assert len(data["causal_graphs"][0]["edges"]) == 4
    assert data["causal_graphs"][0]["scope_status"] == "NONMECHANISTIC"


@pytest.mark.parametrize("section", ["component", "function", "bibliography", "graph"])
def test_crescentin_active_citation_year_is_2017(section):
    data = record("crescentin_filament")
    evidence = {
        "component": data["components"][0]["evidence"][0],
        "function": data["functions"][0]["evidence"][0],
        "bibliography": data["evidence"][0],
        "graph": data["causal_graphs"][0]["edges"][2]["evidence"][0],
    }[section]
    assert evidence["reference"] == "DOI:10.1016/j.tim.2017.03.006"
    assert "Woldemeskel and Goley 2017" in evidence["notes"]


def test_crescentin_historical_year_typo_is_retained_and_explained():
    data = record("crescentin_filament")
    old = next(
        e for e in data["curation_history"]
        if e["action"] == "REPLACED_UNREADABLE_EVIDENCE"
    )
    assert "Woldemeskel and Goley 2018" in old["changes"]
    note = next(
        row for row in data["discussions"]
        if row["discussion_id"] == "woldemeskel_goley_2017_citation_date"
    )
    assert "Retain the original #1260 event unchanged" in note["resolution_note"]
    assert data["canonical_examples"][0]["taxon_id"] == "NCBITaxon:155892"
