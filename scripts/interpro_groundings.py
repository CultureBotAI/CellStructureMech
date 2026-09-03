#!/usr/bin/env python3
"""Apply a fixed, curator-reviewed set of InterPro family decisions.

The InterPro protein endpoint returns domains, sites, superfamilies and
families together.  This adapter keeps only integrated entries whose type is
exactly ``family`` and verifies that every source protein is a reviewed
UniProtKB entry.  It never searches labels or chooses the first result.

Mappings are an allow-list reviewed against component scope on 2026-09-01.
For combined components, additional alpha/beta-carboxysome or MamK/MamJ scope
examples are checked even when they are not stored as record examples.  A
family is written only when the exact family consensus is unambiguous across
that scope.  Otherwise the adapter records ``REVIEWED_LABEL_ONLY`` and why.
Dry-run is the default; pass ``--apply`` to write validated records.
"""

from __future__ import annotations

import argparse
import sys
from collections import defaultdict
from dataclasses import dataclass

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.ingest import get_json
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    write_validated_structure,
)

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records


API = "https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot"


@dataclass(frozen=True)
class ExpectedFamily:
    accession: str
    family: str
    label: str


@dataclass(frozen=True)
class Review:
    record_id: str
    record_label: str
    component_id: str
    component_label: str
    protein_examples: tuple[str, ...]
    scope_accessions: tuple[str, ...]
    expected_families: tuple[ExpectedFamily, ...]
    common_families: tuple[str, ...]
    grounding: str | None = None
    grounding_notes: str | None = None


REVIEWS = (
    Review(
        "GO:0009288",
        "bacterial-type flagellum",
        "flagellin",
        "flagellin (FliC)",
        ("P02968",),
        ("P02968",),
        (ExpectedFamily("P02968", "IPR001492", "Flagellin"),),
        ("IPR001492",),
        grounding="InterPro:IPR001492",
    ),
    Review(
        "GO:0009288",
        "bacterial-type flagellum",
        "hook",
        "hook protein (FlgE)",
        (),
        ("P75937",),
        (ExpectedFamily("P75937", "IPR020013", "Flagellar hook-basal body protein, FlgE/F/G"),),
        ("IPR020013",),
        grounding_notes=(
            "FlgE's only integrated family, IPR020013, spans FlgE, FlgF and FlgG -- the hook "
            "and two of the rod proteins. It is broader than this component, and a broader "
            "term is not adopted as identity. No InterPro family denotes the hook alone."
        ),
    ),
    Review(
        "GO:0031470",
        "carboxysome",
        "bmc_h",
        "BMC-H shell hexamers (CcmK / CsoS1)",
        ("Q03511", "Q31RK2", "Q31RK3"),
        ("Q03511", "Q31RK2", "Q31RK3", "P45689", "P45688", "P45690"),
        (
            ExpectedFamily("Q03511", "IPR046380", "Carboxysome shell protein CcmK"),
            ExpectedFamily("Q31RK2", "IPR046380", "Carboxysome shell protein CcmK"),
            ExpectedFamily("Q31RK3", "IPR046380", "Carboxysome shell protein CcmK"),
            ExpectedFamily("P45689", "IPR050575", "Bacterial microcompartment shell"),
            ExpectedFamily("P45688", "IPR050575", "Bacterial microcompartment shell"),
            ExpectedFamily("P45690", "IPR050575", "Bacterial microcompartment shell"),
        ),
        ("IPR050575",),
        grounding_notes=(
            "IPR046380 exactly covers the reviewed CcmK examples, but alpha-carboxysome "
            "CsoS1 proteins lack it. Their only shared family, IPR050575, is the generic "
            "bacterial microcompartment shell family and also covers non-BMC-H proteins; "
            "no exact family denotes the combined CcmK / CsoS1 component."
        ),
    ),
    Review(
        "GO:0031470",
        "carboxysome",
        "bmc_p",
        "BMC-P shell pentamers (CcmL / CsoS4)",
        ("Q03512",),
        ("Q03512", "O85043", "O85044"),
        (
            ExpectedFamily("Q03512", "IPR046387", "Carboxysome shell vertex protein CcmL"),
            ExpectedFamily(
                "Q03512",
                "IPR004992",
                "Ethanolamine utilization protein EutN/carboxysome shell vertex protein CcmL",
            ),
            ExpectedFamily("O85043", "IPR014076", "Carboxysome shell vertex protein CsoS4A"),
            ExpectedFamily("O85044", "IPR014077", "Carboxysome shell vertex protein CsoS4B"),
        ),
        ("IPR004992",),
        grounding_notes=(
            "IPR046387 exactly covers CcmL, whereas CsoS4A and CsoS4B have the distinct "
            "IPR014076 and IPR014077 families. Their shared IPR004992 entry also includes "
            "the ethanolamine-utilization shell protein EutN, so no exact family denotes "
            "the combined carboxysome BMC-P component."
        ),
    ),
    Review(
        "GO:0031470",
        "carboxysome",
        "carbonic_anhydrase",
        "carboxysomal carbonic anhydrase (CcaA / CsoSCA)",
        ("P27134",),
        ("P27134", "O85042"),
        (
            ExpectedFamily("P27134", "IPR045066", "Beta carbonic anhydrases, cladeB"),
            ExpectedFamily("O85042", "IPR014074", "Carboxysome shell carbonic anhydrase"),
        ),
        (),
        grounding_notes=(
            "The beta-carboxysome CcaA example has IPR045066, while alpha-carboxysome "
            "CsoSCA has IPR014074; they share no integrated InterPro family, so neither "
            "lineage-specific family denotes the combined component."
        ),
    ),
    Review(
        "GO:0031470",
        "carboxysome",
        "scaffold",
        "cargo scaffold (CcmM / CsoS2)",
        ("Q03513",),
        ("Q03513", "O85041"),
        (
            ExpectedFamily("Q03513", "IPR017156", "Carboxysome assembly protein CcmM"),
            ExpectedFamily("O85041", "IPR020990", "Carboxysome assembly protein CsoS2/2B"),
        ),
        (),
        grounding_notes=(
            "The beta-carboxysome scaffold CcmM has IPR017156 and the alpha-carboxysome "
            "scaffold CsoS2 has IPR020990. They share no integrated InterPro family, so "
            "neither lineage-specific entry denotes the combined component."
        ),
    ),
    Review(
        "GO:0031470",
        "carboxysome",
        "assembly_adaptor",
        "assembly adaptor CcmN",
        ("P46204",),
        ("P46204",),
        (),
        (),
        grounding_notes=(
            "InterPro assigns only the fold-level LpxA-like homologous superfamily "
            "IPR011004 to CcmN; no integrated family denotes this component."
        ),
    ),
    Review(
        "GO:0031470",
        "carboxysome",
        "positioning",
        "carboxysome positioning system (McdB, with the McdA ATPase)",
        ("Q8GJM6",),
        ("Q8GJM6",),
        (),
        (),
        grounding_notes=(
            "InterPro assigns only the McdB C-terminal domain IPR063627 to this example; "
            "no integrated family denotes the complete McdB positioning component."
        ),
    ),
    Review(
        "GO:0110143",
        "magnetosome",
        "mamk_filament",
        "MamK actin-like filament",
        ("V6F519",),
        ("V6F519", "Q6NE59"),
        (
            ExpectedFamily("V6F519", "IPR060787", "Magnetosome protein MamJ"),
            ExpectedFamily("Q6NE59", "IPR056546", "MreB/MamK-like"),
        ),
        (),
        grounding_notes=(
            "The component combines MamK and its MamJ connector. The stored MamJ example "
            "has IPR060787, whereas reviewed MamK Q6NE59 has IPR056546; they share no "
            "integrated InterPro family, so a single grounding would conflate distinct roles."
        ),
    ),
)


def protein_url(accession: str) -> str:
    return f"{API}/{accession}/?page_size=200"


def integrated_families(payload: dict, accession: str) -> dict[str, str]:
    """Return exact InterPro family ids and labels after validating the response."""
    results = payload.get("results")
    if not isinstance(results, list):
        raise ValueError(f"InterPro response for {accession} has no result list")
    if payload.get("count") != len(results) or payload.get("next") is not None:
        raise ValueError(
            f"InterPro response for {accession} is incomplete: "
            f"count={payload.get('count')!r}, results={len(results)}, next={payload.get('next')!r}"
        )

    families: dict[str, str] = {}
    seen: set[str] = set()
    for result in results:
        metadata = result.get("metadata") if isinstance(result, dict) else None
        if not isinstance(metadata, dict):
            raise ValueError(f"InterPro result for {accession} has no metadata")
        entry = metadata.get("accession")
        label = metadata.get("name")
        if (
            not isinstance(entry, str)
            or not entry.startswith("IPR")
            or not entry[3:].isdigit()
            or not isinstance(label, str)
            or not label.strip()
            or metadata.get("source_database") != "interpro"
        ):
            raise ValueError(f"invalid integrated InterPro metadata for {accession}: {metadata!r}")
        if entry in seen:
            raise ValueError(f"InterPro response for {accession} repeats {entry}")
        seen.add(entry)

        proteins = result.get("proteins")
        if not isinstance(proteins, list) or len(proteins) != 1:
            raise ValueError(f"InterPro result {entry} has ambiguous protein provenance")
        protein = proteins[0]
        if (
            str(protein.get("accession", "")).casefold() != accession.casefold()
            or protein.get("source_database") != "reviewed"
            or not str(protein.get("organism", "")).isdigit()
        ):
            raise ValueError(f"InterPro result {entry} is not for reviewed UniProtKB:{accession}")
        if metadata.get("type") == "family":
            families[entry] = label
    return families


def component_for_review(record: dict, review: Review) -> dict:
    if record.get("identifier") != review.record_id or record.get("label") != review.record_label:
        raise ValueError(f"record identity changed for {review.record_id}")
    matches = [
        component
        for component in record.get("components") or []
        if component.get("component_id") == review.component_id
    ]
    if len(matches) != 1:
        raise ValueError(
            f"expected one {review.record_id} component {review.component_id}; found {len(matches)}"
        )
    component = matches[0]
    if component.get("label") != review.component_label:
        raise ValueError(f"component label changed for {review.record_id}#{review.component_id}")
    if component.get("component_type") != "PROTEIN":
        raise ValueError(
            f"automatic InterPro review accepts only PROTEIN components; "
            f"{review.record_id}#{review.component_id} is {component.get('component_type')!r}"
        )
    examples = component.get("protein_examples") or []
    observed = tuple(str(example.get("uniprot_id", "")) for example in examples)
    expected = tuple(f"UniProtKB:{accession}" for accession in review.protein_examples)
    if observed != expected or any(example.get("entry_status") != "REVIEWED" for example in examples):
        raise ValueError(
            f"reviewed protein examples changed for {review.record_id}#{review.component_id}: "
            f"expected {expected!r}, found {observed!r}"
        )
    return component


def validate_review(record: dict, review: Review, fetch=get_json) -> dict:
    """Validate one curated decision and return its target component."""
    component = component_for_review(record, review)
    family_sets: dict[str, dict[str, str]] = {}
    for accession in review.scope_accessions:
        family_sets[accession] = integrated_families(fetch(protein_url(accession)), accession)

    for expected in review.expected_families:
        actual = family_sets.get(expected.accession, {}).get(expected.family)
        if actual != expected.label:
            raise ValueError(
                f"InterPro family contract changed for {expected.accession}: "
                f"expected {expected.family} ({expected.label}), found {actual!r}"
            )

    common = set.intersection(*(set(items) for items in family_sets.values()))
    expected_common = set(review.common_families)
    if common != expected_common:
        raise ValueError(
            f"InterPro family consensus changed for {review.record_id}#{review.component_id}: "
            f"expected {sorted(expected_common)!r}, found {sorted(common)!r}"
        )
    if review.grounding is not None:
        expected_grounding = review.grounding.removeprefix("InterPro:")
        if common != {expected_grounding}:
            raise ValueError(
                f"grounding for {review.record_id}#{review.component_id} is missing or ambiguous"
            )
        if component.get("grounding") not in (None, review.grounding):
            raise ValueError(
                f"refusing to overwrite {component.get('grounding')} on "
                f"{review.record_id}#{review.component_id}"
            )
        if component.get("grounding_status") is not None:
            raise ValueError(f"{review.record_id}#{review.component_id} already has grounding_status")
    else:
        if component.get("grounding") is not None:
            raise ValueError(
                f"refusing to remove {component.get('grounding')} from "
                f"{review.record_id}#{review.component_id}"
            )
        if not review.grounding_notes:
            raise ValueError(f"label-only review for {review.component_id} has no explanation")
    return component


def plan_reviews(records, reviews=REVIEWS, fetch=get_json):
    records_by_id = {record.get("identifier"): (path, record) for path, record in records}
    plan = []
    for review in reviews:
        if review.record_id not in records_by_id:
            raise ValueError(f"curated record {review.record_id} is missing")
        path, record = records_by_id[review.record_id]
        component = validate_review(record, review, fetch=fetch)
        desired = (
            (review.grounding, None, None)
            if review.grounding
            else (None, "REVIEWED_LABEL_ONLY", review.grounding_notes)
        )
        current = (
            component.get("grounding"),
            component.get("grounding_status"),
            component.get("grounding_notes"),
        )
        action = (
            "unchanged"
            if current == desired
            else ("ground" if review.grounding else "record label-only review")
        )
        plan.append((path, record, component, review, action))
    return plan


def run(*, apply: bool) -> int:
    plan = plan_reviews(load_records())
    changed = [item for item in plan if item[-1] != "unchanged"]
    for path, _record, _component, review, action in plan:
        outcome = review.grounding or "REVIEWED_LABEL_ONLY"
        print(f"{path.relative_to(REPO_ROOT)}#{review.component_id}\t{outcome}\t{action}")
    if not changed:
        print("nothing to write")
        return 0
    if not apply:
        print(f"\ndry run: {len(changed)} component decision(s) would be written; pass --apply")
        return 0

    by_record = defaultdict(list)
    for item in changed:
        by_record[item[0]].append(item)
    for path, items in by_record.items():
        record = items[0][1]
        for _path, _record, component, review, _action in items:
            if review.grounding:
                component["grounding"] = review.grounding
                component.pop("grounding_status", None)
                component.pop("grounding_notes", None)
            else:
                component.pop("grounding", None)
                component["grounding_status"] = "REVIEWED_LABEL_ONLY"
                component["grounding_notes"] = review.grounding_notes
        grounded = [item[3].component_id for item in items if item[3].grounding]
        declined = [item[3].component_id for item in items if not item[3].grounding]
        grounded_text = ", ".join(grounded) or "none"
        declined_text = ", ".join(declined) or "none"
        record_curation_event(
            record,
            curator="interpro_groundings",
            action="GROUND_COMPONENTS",
            llm_assisted=True,
            changes=(
                f"Applied exact integrated InterPro family groundings to {grounded_text}; "
                f"recorded label-only decisions for {declined_text}. The fixed reviewed "
                "allow-list required exact component identity, reviewed UniProt examples, "
                "type=family entries, and unchanged family consensus across curated scope examples."
            ),
        )
        try:
            write_validated_structure(record, path)
        except ValidationFailedError as exc:
            print(exc.summary(), file=sys.stderr)
            return 1
    print(f"wrote {len(changed)} component decision(s) across {len(by_record)} record(s)")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write records (default: dry run).")
    args = parser.parse_args()
    try:
        return run(apply=args.apply)
    except (OSError, KeyError, TypeError, ValueError) as exc:
        print(f"InterPro grounding import refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
