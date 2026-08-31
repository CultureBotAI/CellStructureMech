from __future__ import annotations

import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(REPO / "scripts"))

import seed_foundational_structures as seed  # noqa: E402

from cellstructuremech.validation.write_validated import validate_structure  # noqa: E402


def test_seed_set_expands_four_records_to_ten_without_duplicate_ids():
    records = seed.prepared_records()
    assert len(records) == 6
    assert len({record["identifier"] for record in records}) == 6
    assert {record["identifier"] for record in records} == {
        "GO:0009274",
        "GO:0009276",
        "GO:0009279",
        "GO:0009295",
        "GO:0031411",
        "GO:0044096",
    }


def test_every_seed_is_proposed_cited_and_closed_schema_valid():
    for record in seed.prepared_records():
        assert record["mapping_status"] == "PROPOSED"
        assert record["evidence"]
        assert record["curation_history"][-1]["llm_assisted"] is True
        assert validate_structure(record) == []


def test_type_iv_pilus_uses_the_current_go_motility_term():
    pilus = next(
        record for record in seed.RECORDS if record["identifier"] == "GO:0044096"
    )
    function = pilus["functions"][0]
    assert function["grounding"] == "GO:0043107"
    assert function["label"] == "type IV pilus-dependent motility"
