#!/usr/bin/env python3
"""Add six literature-backed foundational structures through the validation gate.

This is a one-shot, reviewable corpus expansion. Dry-run by default; ``--apply``
writes only missing records and refuses to overwrite an existing path or identifier.
"""

from __future__ import annotations

import argparse
import sys
from pathlib import Path
from typing import Any

from corpus import load_records, record_path

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    emit_structure_yaml,
    write_validated_structure,
)

CURATION_TIMESTAMP = "2026-08-30T19:30:00Z"
PG_REVIEW = "DOI:10.1111/j.1574-6976.2007.00094.x"
ENVELOPE_REVIEW = "DOI:10.1101/cshperspect.a000414"
NUCLEOID_REVIEW = "DOI:10.1038/nrmicro2261"
PILUS_REVIEW = "DOI:10.1038/nrmicro.2017.40"
GAS_VESICLE_REVIEW = "PMID:8177173"


def evidence(reference: str, notes: str) -> list[dict[str, str]]:
    return [{"reference": reference, "notes": notes}]


RECORDS: tuple[dict[str, Any], ...] = (
    {
        "identifier": "GO:0009274",
        "label": "peptidoglycan-based cell wall",
        "definition": (
            "A protective, load-bearing structure outside the cytoplasmic membrane, "
            "built from glycan strands of alternating N-acetylglucosamine and "
            "N-acetylmuramic acid cross-linked by short peptides. The resulting "
            "murein sacculus surrounds the cell and resists turgor pressure."
        ),
        "definition_source": PG_REVIEW,
        "synonyms": [
            {"synonym_text": "murein sacculus", "synonym_type": "RELATED_SYNONYM", "source": PG_REVIEW}
        ],
        "structure_category": "ENVELOPE",
        "structure_kind": "ENVELOPE_LAYER",
        "components": [
            {
                "component_id": "peptidoglycan",
                "label": "peptidoglycan",
                "component_type": "PEPTIDOGLYCAN",
                "component_role": "CONSTITUENT",
                "essentiality": "ESSENTIAL",
                "role": "Forms the covalently closed, stress-bearing mesh around the cytoplasmic membrane.",
                "evidence": evidence(PG_REVIEW, "Vollmer et al. review sacculus chemistry and architecture."),
            }
        ],
        "taxonomic_distribution": [
            {
                "taxon_id": "NCBITaxon:2",
                "taxon_label": "Bacteria",
                "presence": "COMMON",
                "note": "Present in most bacteria; wall-less lineages and L-forms are exceptions.",
                "reference": PG_REVIEW,
            }
        ],
        "canonical_examples": [
            {
                "taxon_id": "NCBITaxon:562",
                "taxon_label": "Escherichia coli",
                "note": "Canonical Gram-negative murein sacculus model.",
                "reference": PG_REVIEW,
            }
        ],
        "functions": [
            {
                "function_id": "shape_and_osmotic_integrity",
                "label": "cell shape maintenance and resistance to turgor pressure",
                "description": "The cross-linked sacculus bears mechanical stress while permitting growth.",
                "evidence": evidence(PG_REVIEW, "Structural and physical roles of the sacculus."),
            }
        ],
        "evidence": evidence(PG_REVIEW, "Peptidoglycan structure and architecture."),
    },
    {
        "identifier": "GO:0009276",
        "label": "Gram-negative-bacterium-type cell wall",
        "definition": (
            "The relatively thin peptidoglycan layer of a Gram-negative cell envelope, "
            "located in the periplasm between the cytoplasmic and outer membranes and "
            "physically connected to the outer membrane by lipoproteins."
        ),
        "definition_source": ENVELOPE_REVIEW,
        "structure_category": "ENVELOPE",
        "structure_kind": "ENVELOPE_LAYER",
        "parent_structures": ["GO:0009274"],
        "components": [
            {
                "component_id": "thin_peptidoglycan",
                "label": "thin peptidoglycan sacculus",
                "component_type": "PEPTIDOGLYCAN",
                "component_role": "CONSTITUENT",
                "essentiality": "ESSENTIAL",
                "role": "Provides mechanical integrity within the periplasm.",
                "evidence": evidence(
                    ENVELOPE_REVIEW, "Silhavy et al. distinguish the thin wall from the outer membrane."
                ),
            },
            {
                "component_id": "outer_membrane_lipoprotein_links",
                "label": "peptidoglycan–outer-membrane lipoprotein links",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "essentiality": "CONDITIONAL",
                "role": "Couple the peptidoglycan layer mechanically to the outer membrane in many diderms.",
                "evidence": evidence(ENVELOPE_REVIEW, "Envelope review describes lipoprotein coupling."),
            },
        ],
        "taxonomic_distribution": [
            {
                "taxon_id": "NCBITaxon:1224",
                "taxon_label": "Pseudomonadota",
                "presence": "COMMON",
                "note": "Canonical diderm architecture; envelope variants occur across bacteria.",
                "reference": ENVELOPE_REVIEW,
            }
        ],
        "canonical_examples": [
            {
                "taxon_id": "NCBITaxon:562",
                "taxon_label": "Escherichia coli",
                "note": "Reference organism for Gram-negative envelope architecture.",
                "reference": ENVELOPE_REVIEW,
            }
        ],
        "functions": [
            {
                "function_id": "periplasmic_mechanical_integrity",
                "label": "cell-shape maintenance within a diderm envelope",
                "evidence": evidence(
                    ENVELOPE_REVIEW, "The peptidoglycan wall is the stress-bearing envelope layer."
                ),
            }
        ],
        "evidence": evidence(ENVELOPE_REVIEW, "The bacterial cell envelope."),
    },
    {
        "identifier": "GO:0009279",
        "label": "cell outer membrane",
        "definition": (
            "The outermost lipid bilayer of a diderm cell envelope. In canonical "
            "Gram-negative bacteria it is asymmetric, with phospholipid enriched in "
            "the inner leaflet and lipopolysaccharide enriched in the outer leaflet, "
            "and contains beta-barrel proteins that mediate transport and assembly."
        ),
        "definition_source": ENVELOPE_REVIEW,
        "synonyms": [
            {
                "synonym_text": "outer membrane of cell",
                "synonym_type": "EXACT_SYNONYM",
                "source": "GO:0009279",
            }
        ],
        "structure_category": "ENVELOPE",
        "structure_kind": "MEMBRANE",
        "parent_structures": ["GO:0016020"],
        "components": [
            {
                "component_id": "lipopolysaccharide",
                "label": "lipopolysaccharide-rich outer leaflet",
                "component_type": "LIPID",
                "component_role": "CONSTITUENT",
                "essentiality": "CONDITIONAL",
                "role": (
                    "Creates the characteristic asymmetric permeability barrier in "
                    "canonical Gram-negative bacteria."
                ),
                "evidence": evidence(
                    ENVELOPE_REVIEW, "Silhavy et al. describe outer-membrane lipid asymmetry."
                ),
            },
            {
                "component_id": "outer_membrane_beta_barrels",
                "label": "outer-membrane beta-barrel proteins",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "essentiality": "ESSENTIAL",
                "role": "Provide selective transport and envelope assembly functions.",
                "evidence": evidence(
                    ENVELOPE_REVIEW, "Porins and assembly proteins are core outer-membrane components."
                ),
            },
        ],
        "taxonomic_distribution": [
            {
                "taxon_id": "NCBITaxon:2",
                "taxon_label": "Bacteria",
                "presence": "VARIABLE",
                "note": "A diderm feature; monoderm bacteria lack an outer membrane.",
                "reference": ENVELOPE_REVIEW,
            }
        ],
        "canonical_examples": [
            {
                "taxon_id": "NCBITaxon:562",
                "taxon_label": "Escherichia coli",
                "note": "Canonical model for outer-membrane composition and biogenesis.",
                "reference": ENVELOPE_REVIEW,
            }
        ],
        "functions": [
            {
                "function_id": "selective_permeability_barrier",
                "label": "selective permeability barrier",
                "description": "Limits entry of harmful compounds while porins admit selected solutes.",
                "evidence": evidence(
                    ENVELOPE_REVIEW, "The outer membrane protects against environmental insults."
                ),
            }
        ],
        "evidence": evidence(ENVELOPE_REVIEW, "The bacterial cell envelope."),
    },
    {
        "identifier": "GO:0009295",
        "label": "nucleoid",
        "definition": (
            "The non-membrane-bounded subcellular region in which a bacterial "
            "chromosome is compacted and organized with nucleoid-associated proteins "
            "while remaining dynamically coupled to transcription and replication."
        ),
        "definition_source": NUCLEOID_REVIEW,
        "structure_category": "NUCLEOID",
        "structure_kind": "SUBCELLULAR_REGION",
        "components": [
            {
                "component_id": "chromosomal_dna",
                "label": "chromosomal DNA",
                "component_type": "DNA",
                "component_role": "CONSTITUENT",
                "essentiality": "ESSENTIAL",
                "role": "The genome polymer whose compaction and spatial organization define the nucleoid.",
                "evidence": evidence(
                    NUCLEOID_REVIEW, "Dorman reviews chromosome organization in the bacterial nucleoid."
                ),
            },
            {
                "component_id": "nucleoid_associated_proteins",
                "label": "nucleoid-associated proteins",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "essentiality": "CONDITIONAL",
                "role": (
                    "Bend, bridge, wrap, and constrain DNA and couple chromosome "
                    "structure to gene expression."
                ),
                "evidence": evidence(
                    NUCLEOID_REVIEW, "The review covers major NAP families and their regulatory roles."
                ),
            },
        ],
        "taxonomic_distribution": [
            {
                "taxon_id": "NCBITaxon:2",
                "taxon_label": "Bacteria",
                "presence": "UNIVERSAL",
                "note": "The chromosome occupies a nucleoid rather than a membrane-bounded nucleus.",
                "reference": NUCLEOID_REVIEW,
            }
        ],
        "canonical_examples": [
            {
                "taxon_id": "NCBITaxon:562",
                "taxon_label": "Escherichia coli",
                "note": "Best-characterized bacterial nucleoid and NAP system.",
                "reference": NUCLEOID_REVIEW,
            }
        ],
        "functions": [
            {
                "function_id": "chromosome_organization",
                "label": "chromosome organization",
                "grounding": "GO:0051276",
                "description": (
                    "Compacts and spatially organizes the chromosome while preserving "
                    "access to DNA."
                ),
                "evidence": evidence(
                    NUCLEOID_REVIEW, "Nucleoid architecture is integrated with gene expression."
                ),
            }
        ],
        "evidence": evidence(
            NUCLEOID_REVIEW, "Bacterial nucleoid-associated proteins, nucleoid structure and gene expression."
        ),
    },
    {
        "identifier": "GO:0044096",
        "label": "type IV pilus",
        "definition": (
            "A dynamic bacterial surface filament assembled from type IV pilins by an "
            "inner-membrane ATPase machinery. Reversible extension and retraction can "
            "generate force for twitching motility, adhesion, surface sensing, and DNA uptake."
        ),
        "definition_source": PILUS_REVIEW,
        "synonyms": [
            {"synonym_text": "type 4 pilus", "synonym_type": "EXACT_SYNONYM", "source": "GO:0044096"},
            {"synonym_text": "T4P", "synonym_type": "RELATED_SYNONYM", "source": PILUS_REVIEW},
        ],
        "structure_category": "APPENDAGE",
        "structure_kind": "APPENDAGE",
        "parent_structures": ["GO:0009289"],
        "components": [
            {
                "component_id": "major_pilin",
                "label": "major type IV pilin",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "essentiality": "ESSENTIAL",
                "role": "Polymerizes into the extracellular pilus filament.",
                "evidence": evidence(PILUS_REVIEW, "Hospenthal et al. review T4P filament architecture."),
            },
            {
                "component_id": "extension_atpase",
                "label": "PilB-family extension ATPase",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "essentiality": "ESSENTIAL",
                "role": "Powers pilin polymerization and filament extension.",
                "evidence": evidence(PILUS_REVIEW, "The cytoplasmic ATPase drives assembly."),
            },
            {
                "component_id": "retraction_atpase",
                "label": "PilT-family retraction ATPase",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "essentiality": "CONDITIONAL",
                "role": "Powers retraction in retractile type IV pilus systems.",
                "evidence": evidence(PILUS_REVIEW, "Retraction ATPases distinguish dynamic systems."),
            },
        ],
        "taxonomic_distribution": [
            {
                "taxon_id": "NCBITaxon:2",
                "taxon_label": "Bacteria",
                "presence": "VARIABLE",
                "note": "Widely distributed but absent from many lineages and strains.",
                "reference": PILUS_REVIEW,
            }
        ],
        "canonical_examples": [
            {
                "taxon_id": "NCBITaxon:287",
                "taxon_label": "Pseudomonas aeruginosa",
                "note": "Canonical retractile T4P model for twitching motility.",
                "reference": PILUS_REVIEW,
            }
        ],
        "functions": [
            {
                "function_id": "twitching_motility",
                "label": "type IV pilus-dependent motility",
                "grounding": "GO:0043107",
                "description": (
                    "Repeated extension, surface attachment, and retraction pull the "
                    "cell across a surface."
                ),
                "evidence": evidence(PILUS_REVIEW, "T4P dynamics generate motility and adhesion forces."),
            }
        ],
        "evidence": evidence(
            PILUS_REVIEW, "A comprehensive guide to pilus biogenesis in Gram-negative bacteria."
        ),
    },
    {
        "identifier": "GO:0031411",
        "label": "gas vesicle",
        "definition": (
            "A gas-filled, non-membrane-bounded protein organelle, usually shaped as "
            "a cylindrical shell with conical end caps. Its gas-permeable, water-excluding "
            "wall lowers cell density and enables buoyancy regulation in aquatic microbes."
        ),
        "definition_source": GAS_VESICLE_REVIEW,
        "synonyms": [
            {"synonym_text": "gas vacuole", "synonym_type": "RELATED_SYNONYM", "source": "GO:0031411"}
        ],
        "structure_category": "INCLUSION",
        "structure_kind": "PROTEIN_SHELLED_ORGANELLE",
        "components": [
            {
                "component_id": "gvpa",
                "label": "major gas vesicle protein GvpA",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "gene_symbols": ["gvpA"],
                "essentiality": "ESSENTIAL",
                "role": "Forms the ribbed, gas-permeable structural shell.",
                "evidence": evidence(
                    "PMID:22147705", "Solid-state NMR supports cross-beta assembly of the GvpA shell."
                ),
            },
            {
                "component_id": "gvpc",
                "label": "gas vesicle strengthening protein GvpC",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "gene_symbols": ["gvpC"],
                "essentiality": "CONDITIONAL",
                "role": "Strengthens the shell against collapse in characterized systems.",
                "evidence": evidence(GAS_VESICLE_REVIEW, "Walsby reviews GvpC-dependent strengthening."),
            },
        ],
        "taxonomic_distribution": [
            {
                "taxon_id": "NCBITaxon:2",
                "taxon_label": "Bacteria",
                "presence": "VARIABLE",
                "note": "Occurs in several bacterial phyla, especially aquatic phototrophs.",
                "reference": GAS_VESICLE_REVIEW,
            },
            {
                "taxon_id": "NCBITaxon:2157",
                "taxon_label": "Archaea",
                "presence": "VARIABLE",
                "note": "Also occurs in multiple archaeal groups, including haloarchaea.",
                "reference": GAS_VESICLE_REVIEW,
            },
        ],
        "functions": [
            {
                "function_id": "buoyancy_regulation",
                "label": "buoyancy regulation",
                "description": "Changing gas-vesicle content lets aquatic microbes alter vertical position.",
                "evidence": evidence(
                    GAS_VESICLE_REVIEW, "Gas vesicles provide buoyancy and enable vertical migration."
                ),
            }
        ],
        "evidence": [
            {"reference": GAS_VESICLE_REVIEW, "notes": "Walsby 1994 comprehensive review."},
            {
                "reference": "PMID:22147705",
                "notes": "Belenky et al. 2012 structural evidence for the GvpA shell.",
            },
        ],
    },
)


def prepared_records() -> list[dict[str, Any]]:
    records: list[dict[str, Any]] = []
    for source in RECORDS:
        doc = dict(source)
        doc["mapping_status"] = "PROPOSED"
        record_curation_event(
            doc,
            curator="codex",
            action="CREATED_RECORD",
            changes=(
                "Added as a literature-backed foundational seed. Identity checked "
                "against the 2026-07-01 Gene Ontology release; requires human review."
            ),
            llm_assisted=True,
            timestamp=CURATION_TIMESTAMP,
        )
        records.append(doc)
    return records


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true")
    args = parser.parse_args(argv)
    existing = {doc["identifier"]: path for path, doc in load_records()}
    planned: list[tuple[Path, dict[str, Any]]] = []
    for doc in prepared_records():
        path = record_path(doc["structure_category"], doc["label"])
        if doc["identifier"] in existing:
            print(
                f"refusing duplicate identifier {doc['identifier']}: {existing[doc['identifier']]}",
                file=sys.stderr,
            )
            return 2
        if path.exists():
            print(f"refusing to overwrite {path}", file=sys.stderr)
            return 2
        planned.append((path, doc))

    if not args.apply:
        for path, doc in planned:
            print(f"# would write {path}\n{emit_structure_yaml(doc)}")
        return 0
    try:
        for path, doc in planned:
            write_validated_structure(doc, path)
            print(f"wrote {path}")
    except ValidationFailedError as exc:
        print(exc.summary(), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
