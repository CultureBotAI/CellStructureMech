"""Pathway links must preserve target, organism, evidence and publication scope."""

from __future__ import annotations

import copy
import json
from pathlib import Path

import pytest
import yaml

from cellstructuremech.validation.write_validated import validate_structure
from scripts.check_pathway_links import SNAPSHOT, check_links, check_source
from scripts.corpus import REPO_ROOT, load_records


@pytest.fixture
def linked_record():
    path = REPO_ROOT / "data/structures/division_machinery/divisome_complex.yaml"
    return path, yaml.safe_load(path.read_text())


def test_committed_links_match_the_snapshot():
    assert not check_links(load_records(), json.loads(SNAPSHOT.read_text()))


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
