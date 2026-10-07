"""Pathway links must preserve target, organism, evidence and publication scope."""

from __future__ import annotations

import copy
import json
import subprocess
from pathlib import Path

import pytest
import yaml

from cellstructuremech.validation.write_validated import validate_structure
from scripts import run_qc
from scripts.check_pathway_links import SNAPSHOT, check_links, check_source
from scripts.corpus import REPO_ROOT, load_records
from scripts.validate_id_label_correspondence import iter_yaml


@pytest.fixture
def linked_record():
    path = REPO_ROOT / "data/structures/division_machinery/divisome_complex.yaml"
    return path, yaml.safe_load(path.read_text())


def test_committed_links_match_the_snapshot():
    assert not check_links(load_records(), json.loads(SNAPSHOT.read_text()))


def test_ontology_identity_scan_defers_pathway_links_to_the_pinned_checker(linked_record):
    path, doc = linked_record
    config = yaml.safe_load((REPO_ROOT / "conf/id_label_targets.yaml").read_text())
    target = next(row for row in config["targets"] if row["name"] == "record_identity")
    pairs = list(iter_yaml(path, target["pairs"], frozenset(target["exclude_keys"])))
    assert any(curie == doc["identifier"] and label == doc["label"]
               for _, curie, label, _, _ in pairs)
    assert not any(".related_records[" in locator for locator, *_ in pairs)
    assert not {"WikiPathways", "gomodel"}.intersection(config["ignored_prefixes"])

    # Deferring this surface to its own validator must not waive its labels.
    doc["related_records"][0]["label"] = "Incorrect pathway label"
    assert check_links([(path, doc)], json.loads(SNAPSHOT.read_text()))


@pytest.mark.parametrize("field,value", [
    ("identifier", "misspelled:structure"),
    ("label", "Incorrect structure label"),
])
def test_bad_root_identity_still_reaches_the_ontology_gate(linked_record, tmp_path, field, value):
    _, doc = linked_record
    doc[field] = value
    path = tmp_path / "structure.yaml"
    path.write_text(yaml.safe_dump(doc))
    config = yaml.safe_load((REPO_ROOT / "conf/id_label_targets.yaml").read_text())
    target = next(row for row in config["targets"] if row["name"] == "record_identity")
    pairs = list(iter_yaml(path, target["pairs"], frozenset(target["exclude_keys"])))
    assert ("structure.yaml.identifier", doc["identifier"], doc["label"], False, None) in pairs


@pytest.mark.parametrize("target_name", ["record_identity", "grounded_nodes"])
def test_pathway_routing_preserves_every_other_label_surface(linked_record, tmp_path, target_name):
    _, doc = linked_record
    # Exercise nested ontology pairs even when this particular curated record
    # names its components without ontology groundings.
    doc["components"].append({
        "grounding": "GO:1234567", "label": "Incorrect complex label",
        "protein_examples": [{"grounding": "GO:7654321", "label": "Incorrect protein function"}],
    })
    path = tmp_path / "structure.yaml"
    path.write_text(yaml.safe_dump(doc))
    config = yaml.safe_load((REPO_ROOT / "conf/id_label_targets.yaml").read_text())
    target = next(row for row in config["targets"] if row["name"] == target_name)
    excluded = frozenset(target["exclude_keys"])
    previous = list(iter_yaml(path, target["pairs"], excluded - {"related_records"}))
    actual = list(iter_yaml(path, target["pairs"], excluded))
    expected = [row for row in previous if ".related_records[" not in row[0]]
    assert actual == expected
    if target_name == "grounded_nodes":
        assert {"GO:1234567", "GO:7654321"} <= {row[1] for row in actual}


def test_required_qc_runs_pathway_validator_and_stops_on_its_failure(monkeypatch):
    calls = []

    def run(command, **kwargs):
        calls.append(command)
        code = 17 if "scripts/check_pathway_links.py" in command else 0
        return subprocess.CompletedProcess(command, code)

    monkeypatch.setattr(run_qc.subprocess, "run", run)
    assert run_qc.main() == 17
    assert calls[-1][1:] == ["scripts/check_pathway_links.py"]


@pytest.mark.parametrize("field,value", [
    ("identifier", "WikiPathways:WP999999"),
    ("label", "A different pathway"),
    ("source_version", "b" * 40),
    ("target_taxon_id", "NCBITaxon:9606"),
    ("corpus", "TraitMech"),
])
def test_same_label_or_identifier_cannot_hide_a_wrong_target(linked_record, field, value):
    path, doc = linked_record
    doc["related_records"][0][field] = value
    assert check_links([(path, doc)], json.loads(SNAPSHOT.read_text()))


@pytest.mark.parametrize("field", ["source_version", "scope_note", "evidence", "target_taxon_id"])
def test_pathway_links_require_version_scope_and_claim_evidence(linked_record, field):
    _, doc = linked_record
    del doc["related_records"][0][field]
    assert validate_structure(doc)


def test_schema_rejects_an_unreviewed_relation_or_short_pin(linked_record):
    _, doc = linked_record
    assert not validate_structure(doc)
    invalid = copy.deepcopy(doc)
    invalid["related_records"][0]["relation"] = "SAME_STRUCTURE"
    assert validate_structure(invalid)
    invalid = copy.deepcopy(doc)
    invalid["related_records"][0]["source_version"] = "d8ec2b69"
    assert validate_structure(invalid)


def test_a_missing_pinned_git_object_is_an_error(tmp_path):
    snapshot = json.loads(SNAPSHOT.read_text())
    assert check_source(tmp_path, snapshot)


def test_page_link_uses_the_actual_pathwaymech_record_contract():
    page = REPO_ROOT / "pages/structures/division_machinery/divisome_complex.html"
    assert (
        'href="https://culturebotai.github.io/PathwayMech/pages/records/WikiPathways_WP5060.html"'
    ) in page.read_text()


def test_snapshot_carries_distinct_pinned_sources_and_attribution():
    snapshot = json.loads(SNAPSHOT.read_text())
    assert len(snapshot["source_commit"]) == 40
    assert snapshot["license"] == "CC-BY-4.0"
    assert snapshot["attribution"]
    assert len({row["id"] for row in snapshot["records"]}) == len(snapshot["records"])
    for target in snapshot["records"]:
        assert len(target["sha256"]) == 64
        assert Path(target["path"]).suffix == ".yaml"
