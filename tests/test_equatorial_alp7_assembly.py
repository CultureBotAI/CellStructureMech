"""Keep equatorial formation distinct from Alp7-dependent maintenance."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]
SLUG = "equatorial_microtubule_organizing_center"
SOURCE = "DOI:10.1091/mbc.E05-08-0811"


def record():
    return yaml.safe_load(
        (ROOT / "data/structures/cytoskeleton" / f"{SLUG}.yaml").read_text()
    )


def test_alp7_residual_assembly_does_not_change_other_essentialities():
    components = {c["component_id"]: c for c in record()["components"]}
    assert components["alp7"]["essentiality"] == "DISPENSABLE"
    assert components["mto2"]["essentiality"] == "DISPENSABLE"
    assert components["rsp1"]["essentiality"] == "UNKNOWN"


@pytest.mark.parametrize("example", [False, True])
def test_deletion_evidence_is_local_and_preserves_maintenance_scope(example):
    alp7 = next(c for c in record()["components"] if c["component_id"] == "alp7")
    owner = alp7["protein_examples"][0] if example else alp7
    note = next(e["notes"] for e in owner["evidence"] if e["reference"] == SOURCE)
    assert "Figure 5C-E" in note
    assert "S. pombe mia1-deletion" in note
    assert "retained equatorial Mto1, Alp4 and Rsp1 markers" in note
    assert "not normal maintenance or all MTOCs" in note
    assert "Separate supplements and movies were not inspected" in note


def test_current_assembly_disposition_is_explained_and_published():
    discussion = next(
        d for d in record()["discussions"] if d["discussion_id"] == "residual_assembly"
    )
    assert "superseding its earlier UNKNOWN classification" in discussion["rationale"]
    assert "sustained nucleation-site use remains defective" in discussion["rationale"]
    assert any(e["reference"] == SOURCE for e in discussion["evidence"])
    page = (ROOT / "pages/structures/cytoskeleton" / f"{SLUG}.html").read_text()
    assert " ".join(discussion["rationale"].split()) in " ".join(page.split())
