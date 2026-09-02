"""Offline contracts for exact CryoET Data Portal dataset ingestion."""

from pathlib import Path

import pytest

from scripts import cryoet_data_portal as cryoet


def responses(target: cryoet.Target) -> dict[str, dict]:
    dataset = {
        "id": target.dataset_id,
        "title": target.dataset_title,
        "organismName": target.organism_name,
        "organismTaxid": target.taxon_id,
        "cellStrainName": target.strain_name,
        "cellStrainId": "not_reported",
        "sampleType": target.sample_type,
        "cellComponentName": "gas vesicle" if target.dataset_component_id else None,
        "cellComponentId": target.dataset_component_id,
        "datasetPublications": target.publication,
        "relatedDatabaseEntries": "EMD-29922" if target.dataset_component_id else None,
        "depositionDate": "2023-10-01T00:00:00+00:00",
        "releaseDate": "2023-12-01T00:00:00+00:00",
        "lastModifiedDate": "2023-12-01T00:00:00+00:00",
        "runsAggregate": {"aggregate": [{"count": target.run_count}]},
    }
    run = {"id": target.run_id, "datasetId": target.dataset_id, "name": target.run_name}
    annotation = None
    if target.annotation_id:
        annotation = {
            "id": target.annotation_id,
            "runId": target.run_id,
            "depositionId": 10305,
            "annotationPublication": None,
            "annotationMethod": "manual labeling.",
            "annotationIngestId": "type-iv-pilus-1",
            "groundTruthStatus": True,
            "objectId": target.record_id,
            "objectName": "type IV pilus",
            "objectDescription": None,
            "objectState": None,
            "objectCount": target.annotation_count,
            "confidencePrecision": None,
            "confidenceRecall": None,
            "groundTruthUsed": None,
            "annotationSoftware": "IMOD",
            "isCuratorRecommended": True,
            "methodType": "manual",
            "depositionDate": "2024-06-03T00:00:00+00:00",
            "releaseDate": "2024-06-03T00:00:00+00:00",
            "lastModifiedDate": "2024-06-03T00:00:00+00:00",
        }
    return {"datasets": dataset, "runs": run, "annotations": annotation}


def fetcher(values: dict[str, dict]):
    def fetch(query: str, variables: dict) -> dict:
        assert variables["id"] == values[
            "datasets" if query == cryoet.DATASET_QUERY else
            "runs" if query == cryoet.RUN_QUERY else "annotations"
        ]["id"]
        if query == cryoet.DATASET_QUERY:
            return {"datasets": [values["datasets"]]}
        if query == cryoet.RUN_QUERY:
            return {"runs": [values["runs"]]}
        return {"annotations": [values["annotations"]]}

    return fetch


@pytest.mark.parametrize("target", cryoet.TARGETS)
def test_exact_curated_canaries_resolve_and_normalize(target):
    source = responses(target)
    dataset, run, annotation = cryoet.resolve(target, fetch=fetcher(source))
    value = cryoet.normalize(target, dataset, run, annotation)
    assert value["accession"] == f"CryoETDataPortal:{target.dataset_id}"
    assert value["dataset_type"] == "STRUCTURAL_IMAGING"
    assert value["repository"] == "CRYOET_DATA_PORTAL"
    assert "sample_count" not in value
    assert str(target.run_count) in value["findings"] or str(target.run_count) in value["notes"]
    assert value["url"].endswith(f"/datasets/{target.dataset_id}")
    assert "no tomogram or annotation volume was requested" in value["notes"]
    if target.annotation_id:
        assert f"annotation {target.annotation_id}" in value["findings"]
        assert "method_type=manual" in value["notes"]
        assert "ground_truth_status=true" in value["notes"]
        assert "is_curator_recommended=true" in value["notes"]
    else:
        assert target.record_id in value["findings"]


def test_plan_requires_exact_taxon_before_it_fetches():
    target = cryoet.TARGETS[0]
    called = False

    def fetch(_query, _variables):
        nonlocal called
        called = True

    records = [(Path("gas.yaml"), {"identifier": target.record_id})]
    with pytest.raises(ValueError, match=f"NCBITaxon:{target.taxon_id}"):
        cryoet.plan(records, targets=(target,), fetch=fetch)
    assert called is False


@pytest.mark.parametrize(
    ("mutation", "message"),
    [
        ("dataset_go", "component changed"),
        ("run_dataset", "no longer belongs"),
        ("annotation_go", "quality contract changed"),
        ("ground_truth", "quality contract changed"),
        ("recommended", "quality contract changed"),
        ("method", "quality contract changed"),
        ("run_count", "run count changed"),
    ],
)
def test_identity_linkage_quality_and_completeness_drift_fail_closed(mutation, message):
    target = cryoet.TARGETS[1] if mutation in {
        "annotation_go", "ground_truth", "recommended", "method"
    } else cryoet.TARGETS[0]
    source = responses(target)
    if mutation == "dataset_go":
        source["datasets"]["cellComponentId"] = "GO:0000000"
    elif mutation == "run_dataset":
        source["runs"]["datasetId"] = 99999
    elif mutation == "annotation_go":
        source["annotations"]["objectId"] = "GO:0000000"
    elif mutation == "ground_truth":
        source["annotations"]["groundTruthStatus"] = False
    elif mutation == "recommended":
        source["annotations"]["isCuratorRecommended"] = False
    elif mutation == "method":
        source["annotations"]["methodType"] = "automated"
    else:
        source["datasets"]["runsAggregate"]["aggregate"][0]["count"] += 1
    with pytest.raises(ValueError, match=message):
        cryoet.resolve(target, fetch=fetcher(source))


def test_exact_queries_do_not_request_bulk_data_paths_or_files():
    queries = "\n".join(
        (cryoet.DATASET_QUERY, cryoet.RUN_QUERY, cryoet.ANNOTATION_QUERY)
    ).casefold()
    for forbidden in ("s3prefix", "httpsprefix", "annotationfiles", "tomograms"):
        assert forbidden not in queries


def test_plan_migrates_the_draft_accession_by_landing_url_without_duplication():
    target = cryoet.TARGETS[0]
    source = responses(target)
    record = {
        "identifier": target.record_id,
        "canonical_examples": [{"taxon_id": f"NCBITaxon:{target.taxon_id}"}],
        "datasets": [
            {
                "accession": f"CryoET Data Portal:{target.dataset_id}",
                "url": f"{cryoet.PORTAL}/datasets/{target.dataset_id}",
            }
        ],
    }
    planned = cryoet.plan(
        [(Path("gas.yaml"), record)], targets=(target,), fetch=fetcher(source)
    )
    _path, _record, _target, value, action = planned[0]
    assert action == "updated"
    migrated, _ = cryoet.upsert(record["datasets"], "url", value)
    assert [item["accession"] for item in migrated] == [
        f"CryoETDataPortal:{target.dataset_id}"
    ]


def test_graphql_errors_are_not_treated_as_empty_results(monkeypatch):
    monkeypatch.setattr(
        cryoet,
        "post_json",
        lambda *_args, **_kwargs: {"data": None, "errors": [{"message": "backend error"}]},
    )
    with pytest.raises(ValueError, match="GraphQL returned errors"):
        cryoet.graphql("query { datasets { id } }", {})
