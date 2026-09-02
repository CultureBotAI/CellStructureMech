#!/usr/bin/env python3
"""Ingest fixed, curator-reviewed CryoET Data Portal metadata canaries.

The adapter resolves exact dataset, run and (where selected) annotation ids
through the official GraphQL API. It accepts only an exact dataset-level GO
cell-component id or an exact annotation object id, and requires the dataset's
NCBI taxon to be present in the target record before any dataset is proposed.

Only lightweight metadata and landing-page links are queried and stored. The
queries deliberately omit S3/HTTPS data paths, and this script has no download
operation for tomograms or annotation volumes. Dry-run is the default; pass
``--apply`` to write validated records.
"""

from __future__ import annotations

import argparse
import sys
from dataclasses import dataclass

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import post_json, require_record_taxon, upsert
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    write_validated_structure,
)

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records


API = "https://graphql.cryoetdataportal.czscience.com/graphql"
PORTAL = "https://cryoetdataportal.czscience.com"
CC0_POLICY = f"{PORTAL}/data-submission-policy"

DATASET_QUERY = """query Dataset($id: Int!) {
  datasets(where: {id: {_eq: $id}}) {
    id title organismName organismTaxid cellStrainName cellStrainId sampleType
    cellComponentName cellComponentId datasetPublications relatedDatabaseEntries
    depositionDate releaseDate lastModifiedDate
    runsAggregate { aggregate { count } }
  }
}"""

RUN_QUERY = """query Run($id: Int!) {
  runs(where: {id: {_eq: $id}}) { id datasetId name }
}"""

ANNOTATION_QUERY = """query Annotation($id: Int!) {
  annotations(where: {id: {_eq: $id}}) {
    id runId depositionId annotationPublication annotationMethod annotationIngestId
    groundTruthStatus objectId objectName objectDescription objectState objectCount
    confidencePrecision confidenceRecall groundTruthUsed annotationSoftware
    isCuratorRecommended methodType depositionDate releaseDate lastModifiedDate
  }
}"""


@dataclass(frozen=True)
class Target:
    record_id: str
    dataset_id: int
    run_id: int
    taxon_id: int
    organism_name: str
    strain_name: str
    dataset_title: str
    run_name: str
    publication: str
    sample_type: str
    run_count: int
    dataset_component_id: str | None = None
    annotation_id: int | None = None
    annotation_count: int | None = None


TARGETS = (
    Target(
        record_id="GO:0031411",
        dataset_id=10014,
        run_id=14004,
        taxon_id=315271,
        organism_name="Dolichospermum flos-aquae",
        strain_name="CCAP 1403/13F",
        dataset_title="D. flos-aquae Ana GVs (WT)",
        run_name="pda2021-06-24-66",
        publication="10.1016/j.str.2023.03.011",
        sample_type="organelle",
        run_count=217,
        dataset_component_id="GO:0031411",
    ),
    Target(
        record_id="GO:0044096",
        dataset_id=10155,
        run_id=7978,
        annotation_id=30707,
        annotation_count=8,
        taxon_id=264462,
        organism_name="Bdellovibrio bacteriovorus",
        strain_name="HD100",
        dataset_title="Bdellovibrio attack-phase",
        run_name="ycw2012-11-14-17",
        publication="10.1038/s41564-023-01401-2",
        sample_type="primary_cell_culture",
        run_count=105,
    ),
)


def graphql(query: str, variables: dict) -> dict:
    payload = post_json(API, {"query": query, "variables": variables})
    if payload.get("errors"):
        raise ValueError(f"GraphQL returned errors: {payload['errors']!r}")
    data = payload.get("data")
    if not isinstance(data, dict):
        raise ValueError("GraphQL response has no data object")
    return data


def one(data: dict, field: str, expected_id: int) -> dict:
    items = data.get(field)
    if not isinstance(items, list) or len(items) != 1:
        count = len(items) if isinstance(items, list) else "non-list"
        raise ValueError(f"expected exactly one {field} result for {expected_id}; got {count}")
    item = items[0]
    if not isinstance(item, dict) or item.get("id") != expected_id:
        raise ValueError(f"{field} identity mismatch for {expected_id}: {item!r}")
    return item


def run_count(dataset: dict) -> int:
    aggregate = (dataset.get("runsAggregate") or {}).get("aggregate")
    if not isinstance(aggregate, list) or len(aggregate) != 1:
        raise ValueError("dataset run aggregate is missing or ambiguous")
    count = aggregate[0].get("count") if isinstance(aggregate[0], dict) else None
    if not isinstance(count, int) or count < 1:
        raise ValueError(f"dataset run count is invalid: {count!r}")
    return count


def resolve(target: Target, fetch=graphql) -> tuple[dict, dict, dict | None]:
    dataset = one(fetch(DATASET_QUERY, {"id": target.dataset_id}), "datasets", target.dataset_id)
    run = one(fetch(RUN_QUERY, {"id": target.run_id}), "runs", target.run_id)
    annotation = None
    if target.annotation_id is not None:
        annotation = one(
            fetch(ANNOTATION_QUERY, {"id": target.annotation_id}),
            "annotations",
            target.annotation_id,
        )

    expected_dataset = {
        "title": target.dataset_title,
        "organismName": target.organism_name,
        "organismTaxid": target.taxon_id,
        "cellStrainName": target.strain_name,
        "sampleType": target.sample_type,
        "datasetPublications": target.publication,
    }
    changed = {key: (expected, dataset.get(key)) for key, expected in expected_dataset.items()
               if dataset.get(key) != expected}
    if changed:
        raise ValueError(f"dataset {target.dataset_id} metadata contract changed: {changed!r}")
    if run_count(dataset) != target.run_count:
        raise ValueError(
            f"dataset {target.dataset_id} run count changed: "
            f"expected {target.run_count}, got {run_count(dataset)}"
        )
    if (run.get("datasetId"), run.get("name")) != (target.dataset_id, target.run_name):
        raise ValueError(f"run {target.run_id} no longer belongs to the curated dataset")

    if target.dataset_component_id is not None:
        if dataset.get("cellComponentId") != target.dataset_component_id:
            raise ValueError(
                f"dataset {target.dataset_id} component changed: "
                f"expected {target.dataset_component_id}, got {dataset.get('cellComponentId')!r}"
            )
        if annotation is not None:
            raise ValueError("a target must use one exact GO evidence path, not two")
    elif annotation is None:
        raise ValueError("target has neither an exact dataset component nor annotation")

    if annotation is not None:
        expected_annotation = {
            "runId": target.run_id,
            "objectId": target.record_id,
            "objectCount": target.annotation_count,
            "groundTruthStatus": True,
            "isCuratorRecommended": True,
            "methodType": "manual",
            "annotationMethod": "manual labeling.",
            "annotationSoftware": "IMOD",
        }
        changed = {
            key: (expected, annotation.get(key))
            for key, expected in expected_annotation.items()
            if annotation.get(key) != expected
        }
        if changed:
            raise ValueError(
                f"annotation {target.annotation_id} quality contract changed: {changed!r}"
            )
    return dataset, run, annotation


def normalize(target: Target, dataset: dict, run: dict, annotation: dict | None) -> dict:
    related = dataset.get("relatedDatabaseEntries")
    dates = (
        f"deposited {dataset.get('depositionDate')}; released {dataset.get('releaseDate')}; "
        f"last modified {dataset.get('lastModifiedDate')}"
    )
    identity = (
        f"CryoET Data Portal dataset {target.dataset_id}; canary run {target.run_id} "
        f"({run['name']}), one of {target.run_count} portal runs"
    )
    if annotation is None:
        findings = (
            f"The portal identifies the dataset cell component exactly as {target.record_id} "
            f"({dataset['cellComponentName']}) across {target.run_count} runs."
        )
        quality = ""
    else:
        findings = (
            f"Run {target.run_id} annotation {target.annotation_id} identifies "
            f"{annotation['objectCount']} {annotation['objectId']} ({annotation['objectName']}) objects."
        )
        quality = (
            f"; annotation {target.annotation_id}: method_type={annotation['methodType']}, "
            f"annotation_method={annotation['annotationMethod']}, "
            f"annotation_software={annotation['annotationSoftware']}, "
            f"ground_truth_status={str(annotation['groundTruthStatus']).lower()}, "
            f"is_curator_recommended={str(annotation['isCuratorRecommended']).lower()}, "
            f"released {annotation.get('releaseDate')}"
        )
    notes = (
        f"{identity}{quality}; {dates}"
        + (f"; related entries: {related}" if related else "")
        + f". Public portal submissions are CC0 ({CC0_POLICY}). Metadata-only ingest: "
        "no tomogram or annotation volume was requested, downloaded or hosted."
    )
    return {
        "accession": f"CryoETDataPortal:{target.dataset_id}",
        "title": target.dataset_title,
        "description": (
            f"Cryo-electron tomography dataset for {target.organism_name} "
            f"{target.strain_name}, linked to {target.record_id}."
        ),
        "organism": (
            f"NCBITaxon:{target.taxon_id} {target.organism_name} {target.strain_name}"
        ),
        "dataset_type": "STRUCTURAL_IMAGING",
        "repository": "CRYOET_DATA_PORTAL",
        "sample_types": [target.sample_type.replace("_", " ")],
        "platform": "cryo-electron tomography",
        "url": f"{PORTAL}/datasets/{target.dataset_id}",
        "publication": f"DOI:{target.publication}",
        "findings": findings,
        "evidence": [
            {
                "reference": f"DOI:{target.publication}",
                "supports": "SUPPORT",
                "evidence_source": "publication",
                "explanation": "Associated primary publication for the selected CryoET dataset.",
            }
        ],
        "notes": notes,
    }


def plan(records, targets=TARGETS, fetch=graphql):
    records_by_id = {record.get("identifier"): (path, record) for path, record in records}
    planned = []
    for target in targets:
        if target.record_id not in records_by_id:
            raise ValueError(f"target record is missing: {target.record_id}")
        path, record = records_by_id[target.record_id]
        require_record_taxon(record, f"NCBITaxon:{target.taxon_id}")
        dataset, run, annotation = resolve(target, fetch=fetch)
        value = normalize(target, dataset, run, annotation)
        existing = next(
            (item for item in record.get("datasets") or [] if item.get("url") == value["url"]),
            None,
        )
        action = "unchanged" if existing == value else ("updated" if existing else "added")
        planned.append((path, record, target, value, action))
    return planned


def run(*, apply: bool) -> int:
    planned = plan(load_records())
    changed = [item for item in planned if item[-1] != "unchanged"]
    for path, _record, target, _value, action in planned:
        annotation = f" annotation {target.annotation_id}" if target.annotation_id else ""
        print(
            f"{path.relative_to(REPO_ROOT)}\tdataset {target.dataset_id}\t"
            f"run {target.run_id}{annotation}\t{action}"
        )
    if not changed:
        print("nothing to write")
        return 0
    if not apply:
        print(f"\ndry run: {len(changed)} dataset reference(s) would be written; pass --apply")
        return 0

    for path, record, target, value, _action in changed:
        # The landing URL is the migration key as well as a source identity:
        # it upgrades the pre-review accession spelling without leaving a duplicate.
        record["datasets"], _ = upsert(record.get("datasets"), "url", value)
        record_curation_event(
            record,
            curator="cryoet_data_portal",
            action="ADD_STRUCTURAL_DATASET",
            llm_assisted=True,
            changes=(
                f"Added CryoET Data Portal dataset {target.dataset_id} after exact GraphQL "
                f"resolution of run {target.run_id}"
                + (f" and annotation {target.annotation_id}" if target.annotation_id else "")
                + "; required the record's pre-existing exact NCBI taxon and exact GO identity, "
                "preserved annotation quality metadata, and stored no imaging volumes."
            ),
        )
        try:
            write_validated_structure(record, path)
        except ValidationFailedError as exc:
            print(exc.summary(), file=sys.stderr)
            return 1
    print(f"wrote {len(changed)} dataset reference(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write records (default: dry run).")
    args = parser.parse_args()
    try:
        return run(apply=args.apply)
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"CryoET Data Portal import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
