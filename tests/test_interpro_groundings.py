"""Offline contract tests for exact InterPro family grounding decisions."""

from pathlib import Path

import pytest

from scripts import interpro_groundings as ip


def payload(accession: str, entries: list[tuple[str, str, str]], *, reviewed=True) -> dict:
    results = []
    for entry, label, entry_type in entries:
        results.append(
            {
                "metadata": {
                    "accession": entry,
                    "name": label,
                    "source_database": "interpro",
                    "type": entry_type,
                },
                "proteins": [
                    {
                        "accession": accession.lower(),
                        "source_database": "reviewed" if reviewed else "unreviewed",
                        "organism": "224308",
                    }
                ],
            }
        )
    return {"count": len(results), "next": None, "previous": None, "results": results}


@pytest.mark.parametrize(
    ("accession", "entry", "label"),
    [
        ("P02968", "IPR001492", "Flagellin"),
        ("Q03511", "IPR046380", "Carboxysome shell protein CcmK"),
        ("Q03512", "IPR046387", "Carboxysome shell vertex protein CcmL"),
        ("P27134", "IPR045066", "Beta carbonic anhydrases, cladeB"),
        ("Q03513", "IPR017156", "Carboxysome assembly protein CcmM"),
    ],
)
def test_positive_canaries_are_exact_integrated_families(accession, entry, label):
    result = ip.integrated_families(payload(accession, [(entry, label, "family")]), accession)
    assert result == {entry: label}


def test_domains_and_superfamilies_are_never_substituted_for_families():
    result = ip.integrated_families(
        payload(
            "P46204",
            [
                ("IPR011004", "Trimeric LpxA-like superfamily", "homologous_superfamily"),
                ("IPR063627", "McdB, C-terminal domain", "domain"),
            ],
        ),
        "P46204",
    )
    assert result == {}


@pytest.mark.parametrize("mutation", ["count", "next", "reviewed", "accession"])
def test_incomplete_or_unreviewed_responses_fail_closed(mutation):
    data = payload("P02968", [("IPR001492", "Flagellin", "family")])
    if mutation == "count":
        data["count"] = 2
    elif mutation == "next":
        data["next"] = "https://example.org/page/2"
    elif mutation == "reviewed":
        data["results"][0]["proteins"][0]["source_database"] = "unreviewed"
    else:
        data["results"][0]["proteins"][0]["accession"] = "wrong"
    with pytest.raises(ValueError):
        ip.integrated_families(data, "P02968")


def record_for(review: ip.Review, *, component_type="PROTEIN") -> dict:
    return {
        "identifier": review.record_id,
        "label": review.record_label,
        "components": [
            {
                "component_id": review.component_id,
                "label": review.component_label,
                "component_type": component_type,
                "protein_examples": [
                    {"uniprot_id": f"UniProtKB:{item}", "entry_status": "REVIEWED"}
                    for item in review.protein_examples
                ],
            }
        ],
    }


def fetch_for(review: ip.Review, *, extra_common: tuple[str, str] | None = None):
    expected: dict[str, list[tuple[str, str, str]]] = {accession: [] for accession in review.scope_accessions}
    labels = {item.family: item.label for item in review.expected_families}
    for item in review.expected_families:
        expected[item.accession].append((item.family, item.label, "family"))
    for family in review.common_families:
        label = labels.get(family, "Curated common family")
        for accession in review.scope_accessions:
            if family not in {item[0] for item in expected[accession]}:
                expected[accession].append((family, label, "family"))
    if extra_common:
        for accession in review.scope_accessions:
            expected[accession].append((*extra_common, "family"))

    def fetch(url: str) -> dict:
        accession = next(item for item in review.scope_accessions if f"/{item}/" in url)
        return payload(accession, expected[accession])

    return fetch


def test_exact_flagellin_consensus_is_planned_as_a_grounding():
    review = ip.REVIEWS[0]
    plan = ip.plan_reviews(
        [(Path("flagellum.yaml"), record_for(review))],
        reviews=(review,),
        fetch=fetch_for(review),
    )
    assert plan[0][3].grounding == "InterPro:IPR001492"
    assert plan[0][-1] == "ground"


def test_an_additional_common_family_is_ambiguous_and_refused():
    review = ip.REVIEWS[0]
    with pytest.raises(ValueError, match="consensus changed"):
        ip.validate_review(
            record_for(review),
            review,
            fetch=fetch_for(review, extra_common=("IPR999999", "Unexpected family")),
        )


def test_only_protein_components_can_receive_automatic_proposals():
    review = ip.REVIEWS[0]
    with pytest.raises(ValueError, match="only PROTEIN"):
        ip.validate_review(
            record_for(review, component_type="PROTEIN_COMPLEX"),
            review,
            fetch=pytest.fail,
        )


def test_changed_or_unreviewed_record_examples_are_refused_before_network():
    review = ip.REVIEWS[0]
    record = record_for(review)
    record["components"][0]["protein_examples"][0]["entry_status"] = "UNREVIEWED"
    with pytest.raises(ValueError, match="reviewed protein examples changed"):
        ip.validate_review(record, review, fetch=pytest.fail)


def test_bare_uniprot_accession_is_refused_before_network():
    review = ip.REVIEWS[0]
    record = record_for(review)
    record["components"][0]["protein_examples"][0]["uniprot_id"] = "P02968"
    with pytest.raises(ValueError, match="reviewed protein examples changed"):
        ip.validate_review(record, review, fetch=pytest.fail)


def test_label_only_review_never_removes_an_existing_grounding():
    review = next(item for item in ip.REVIEWS if item.component_id == "mamk_filament")
    record = record_for(review)
    record["components"][0]["grounding"] = "InterPro:IPR060787"
    with pytest.raises(ValueError, match="refusing to remove"):
        ip.validate_review(record, review, fetch=fetch_for(review))


@pytest.mark.parametrize("component_id", ["assembly_adaptor", "positioning", "mamk_filament"])
def test_negative_controls_produce_label_only_decisions(component_id):
    review = next(item for item in ip.REVIEWS if item.component_id == component_id)
    plan = ip.plan_reviews(
        [(Path("record.yaml"), record_for(review))],
        reviews=(review,),
        fetch=fetch_for(review),
    )
    assert plan[0][3].grounding is None
    assert plan[0][3].grounding_notes
    assert plan[0][-1] == "record label-only review"
