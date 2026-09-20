#!/usr/bin/env python3
"""Apply review-driven graph boundary fixes across existing records."""

from __future__ import annotations

import argparse
import sys
from collections.abc import Iterable
from dataclasses import dataclass, field
from pathlib import Path
from typing import Any

import yaml

from cellstructuremech.curate.curation_event import record_curation_event
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    write_validated_structure,
)

try:
    from corpus import REPO_ROOT
except ImportError:
    from scripts.corpus import REPO_ROOT


@dataclass(frozen=True)
class RecordFix:
    identifier: str
    graph_nodes: dict[str, tuple[str, ...]]
    changes: str
    localization_nodes: dict[str, tuple[str, ...]] = field(default_factory=dict)


FIXES: dict[Path, RecordFix] = {
    Path("data/structures/other/kinetochore.yaml"): RecordFix(
        identifier="GO:0000776",
        graph_nodes={
            "yeast_inner_outer_kinetochore_bridge": (
                "coma_complex",
                "mis12_mind_type_complex",
                "ndc80_complex",
            ),
        },
        changes=(
            "Retyped exact protein-complex graph nodes for COMA, MIS12/MIND, "
            "and Ndc80 from GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/other/nucleolus.yaml"): RecordFix(
        identifier="GO:0005730",
        graph_nodes={"yeast_nucleolar_ribosome_biogenesis": ("rna_polymerase_i_complex",)},
        changes="Retyped the RNA polymerase I complex graph node from GENE_OR_PROTEIN to STRUCTURE.",
    ),
    Path("data/structures/other/pyrenoid.yaml"): RecordFix(
        identifier="GO:1990732",
        graph_nodes={"epyc1_rubisco_pyrenoid_matrix_assembly": ("rubisco_holoenzyme",)},
        changes=(
            "Retyped the GO-grounded ribulose bisphosphate carboxylase complex "
            "graph node from GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/secretion_system/type_i_protein_secretion_system_complex.yaml"): RecordFix(
        identifier="GO:0030256",
        graph_nodes={"abc_mfp_tolc_one_step_export": ("outer_membrane_factor",)},
        changes="Retyped the TolC-family outer-membrane factor graph node from GENE_OR_PROTEIN to STRUCTURE.",
    ),
    Path("data/structures/secretion_system/type_ii_protein_secretion_system_complex.yaml"): RecordFix(
        identifier="GO:0015627",
        graph_nodes={
            "atpase_pseudopilus_secretin_export": (
                "inner_platform",
                "pseudopilus",
                "secretin",
            ),
        },
        changes=(
            "Retyped the T2SS inner platform, pseudopilus, and secretin graph "
            "nodes from GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml"): RecordFix(
        identifier="GO:0030257",
        graph_nodes={
            "export_gate_needle_translocon_injection": (
                "secretin",
                "inner_rings",
                "export_apparatus",
                "translocon",
            ),
        },
        changes=(
            "Retyped T3SS protein-complex subassembly graph nodes as STRUCTURE, "
            "removed the bacterial flagellum xref, and kept the flagellum "
            "homology discussion as the place to model shared ancestry."
        ),
    ),
    Path("data/structures/secretion_system/type_iv_secretion_system_complex.yaml"): RecordFix(
        identifier="GO:0043684",
        graph_nodes={
            "virb_vird4_substrate_transfer": (
                "core_complex",
                "inner_complex",
                "pilus",
            ),
        },
        changes=(
            "Retyped the T4SS core complex, inner complex, and extracellular "
            "pilus graph nodes from GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/secretion_system/type_ix_protein_secretion_system_complex.yaml"): RecordFix(
        identifier="cellstructuremech:type_ix_protein_secretion_system_complex",
        graph_nodes={
            "t9ss_outer_membrane_export": (
                "porl_porm_motor",
                "pork_porn_outer_membrane_ring",
            ),
        },
        changes=(
            "Retyped the PorL/PorM motor and PorK/PorN ring graph nodes from "
            "GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/secretion_system/type_vi_protein_secretion_system_complex.yaml"): RecordFix(
        identifier="GO:0033104",
        graph_nodes={
            "contractile_tube_injection": (
                "membrane",
                "baseplate",
                "sheath",
                "spike",
            ),
        },
        changes=(
            "Retyped the T6SS membrane, baseplate, contractile sheath, and "
            "spike graph nodes from GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_complex.yaml"): RecordFix(
        identifier="GO:0016471",
        graph_nodes={
            "yeast_v_atpase_rotary_acidification": (
                "v1_domain",
                "v0_domain",
            ),
        },
        changes="Retyped the vacuolar V-ATPase V1 and V0 domain graph nodes as STRUCTURE.",
    ),
    Path("data/structures/membrane_organelle/bacterial_thylakoid.yaml"): RecordFix(
        identifier="GO:0030075",
        graph_nodes={
            "cyanobacterial_thylakoid_topology": (
                "psii",
                "cytb6f",
                "psi",
                "atp_synthase",
            ),
        },
        changes=(
            "Retyped the PSII, cytochrome b6f, PSI, and ATP synthase graph "
            "nodes from GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/membrane_organelle/glycosome.yaml"): RecordFix(
        identifier="GO:0020015",
        graph_nodes={},
        changes="Retyped the glycosome lumen graph node as CELLULAR_LOCALIZATION.",
        localization_nodes={"pex14_glycolytic_import_compartmentation": ("glycosome_lumen",)},
    ),
    Path("data/structures/membrane_organelle/glycosome_membrane.yaml"): RecordFix(
        identifier="GO:0046860",
        graph_nodes={},
        changes="Retyped the glycosome lumen graph node as CELLULAR_LOCALIZATION.",
        localization_nodes={"glycosome_membrane_import_boundary": ("glycosome_lumen",)},
    ),
    Path("data/structures/membrane_organelle/hydrogenosome.yaml"): RecordFix(
        identifier="GO:0042566",
        graph_nodes={},
        changes="Retyped the hydrogenosome lumen graph node as CELLULAR_LOCALIZATION.",
        localization_nodes={
            "hydrogenosomal_pyruvate_to_atp_and_hydrogen": ("hydrogenosome_lumen",),
        },
    ),
    Path("data/structures/membrane_organelle/microneme.yaml"): RecordFix(
        identifier="GO:0020009",
        graph_nodes={},
        changes="Retyped the microneme lumen graph node as CELLULAR_LOCALIZATION.",
        localization_nodes={"microneme_exocytosis_host_invasion": ("microneme_lumen",)},
    ),
    Path("data/structures/membrane_organelle/microneme_membrane.yaml"): RecordFix(
        identifier="GO:0033163",
        graph_nodes={},
        changes="Retyped the microneme lumen graph node as CELLULAR_LOCALIZATION.",
        localization_nodes={"microneme_membrane_bounds_lumen": ("microneme_lumen",)},
    ),
    Path("data/structures/membrane_organelle/organellar_chromatophore_inner_membrane.yaml"): RecordFix(
        identifier="GO:0070113",
        graph_nodes={},
        changes=(
            "Retyped the organellar chromatophore intermembrane-space graph node "
            "as CELLULAR_LOCALIZATION."
        ),
        localization_nodes={
            "organellar_chromatophore_inner_membrane_topology": (
                "organellar_chromatophore_intermembrane_space",
            ),
        },
    ),
    Path("data/structures/membrane_organelle/chloroplast.yaml"): RecordFix(
        identifier="GO:0009507",
        graph_nodes={"chlamydomonas_chloroplast_envelope_and_import": ("toc_tic_supercomplex",)},
        changes="Retyped the chloroplast TOC-TIC import supercomplex graph node as STRUCTURE.",
    ),
    Path("data/structures/membrane_organelle/chloroplast_envelope.yaml"): RecordFix(
        identifier="GO:0009941",
        graph_nodes={
            "chlamydomonas_chloroplast_envelope_import": (
                "toc_complex",
                "tic_complex",
            ),
        },
        changes="Retyped the chloroplast Toc and Tic graph nodes as STRUCTURE.",
    ),
    Path("data/structures/membrane_organelle/mitochondrial_crista.yaml"): RecordFix(
        identifier="GO:0030061",
        graph_nodes={
            "yeast_mitochondrial_crista_architecture": (
                "micos_complex",
                "atp_synthase",
            ),
        },
        changes="Retyped the MICOS and ATP synthase graph nodes as STRUCTURE.",
    ),
    Path("data/structures/membrane_organelle/mitochondrial_envelope.yaml"): RecordFix(
        identifier="GO:0005740",
        graph_nodes={"yeast_mitochondrial_envelope_import": ("tom_complex",)},
        changes="Retyped the TOM complex graph node from GENE_OR_PROTEIN to STRUCTURE.",
    ),
    Path("data/structures/membrane_organelle/mitochondrion.yaml"): RecordFix(
        identifier="GO:0005739",
        graph_nodes={"yeast_mitochondrial_envelope_and_import": ("tom_complex",)},
        changes="Retyped the TOM complex graph node from GENE_OR_PROTEIN to STRUCTURE.",
    ),
    Path("data/structures/membrane_organelle/plasma_membrane_derived_chromatophore_membrane.yaml"): RecordFix(
        identifier="GO:0042717",
        graph_nodes={
            "chromatophore_photophosphorylation": (
                "rc_lh1_pufx",
                "cytochrome_bc1",
            ),
        },
        changes=(
            "Retyped the locally grounded RC-LH1-PufX and cytochrome bc1 "
            "complex graph nodes as STRUCTURE."
        ),
    ),
    Path("data/structures/membrane_organelle/plasma_membrane_derived_thylakoid_membrane.yaml"): RecordFix(
        identifier="GO:0031676",
        graph_nodes={
            "plasma_membrane_derived_thylakoid_membrane_topology": (
                "psii",
                "cytb6f",
                "psi",
            ),
        },
        changes=(
            "Retyped the PSII, cytochrome b6f, and PSI graph nodes from "
            "GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/membrane_organelle/rhoptry.yaml"): RecordFix(
        identifier="GO:0020008",
        graph_nodes={},
        changes="Retyped the rhoptry lumen graph node as CELLULAR_LOCALIZATION.",
        localization_nodes={"rhoptry_discharge_host_invasion": ("rhoptry_lumen",)},
    ),
    Path("data/structures/membrane_organelle/rhoptry_membrane.yaml"): RecordFix(
        identifier="GO:0033016",
        graph_nodes={},
        changes="Retyped the rhoptry lumen graph node as CELLULAR_LOCALIZATION.",
        localization_nodes={"rhoptry_membrane_bounds_lumen": ("rhoptry_lumen",)},
    ),
    Path("data/structures/membrane_organelle/thylakoid_membrane.yaml"): RecordFix(
        identifier="GO:0042651",
        graph_nodes={
            "linear_electron_transport_proton_gradient": (
                "psii",
                "cytb6f",
                "psi",
                "atp_synthase",
            ),
        },
        changes=(
            "Retyped the photosystem II, cytochrome b6f, photosystem I, and "
            "ATP synthase graph nodes from GENE_OR_PROTEIN to STRUCTURE."
        ),
    ),
    Path("data/structures/other/clathrin_coat_of_coated_pit.yaml"): RecordFix(
        identifier="GO:0030132",
        graph_nodes={"coated_pit_clathrin_coat_topology": ("ap2_adaptor_complex",)},
        changes="Retyped the AP-2 adaptor complex graph node as STRUCTURE.",
    ),
    Path("data/structures/spore/prospore_membrane.yaml"): RecordFix(
        identifier="GO:0005628",
        graph_nodes={"secretory_vesicles_build_prospore_membrane": ("lep_coat",)},
        changes="Retyped the prospore membrane leading-edge coat graph node as STRUCTURE.",
    ),
    Path("data/structures/spore/prospore_membrane_leading_edge.yaml"): RecordFix(
        identifier="GO:0070056",
        graph_nodes={
            "leading_edge_coat_marks_prospore_membrane_rim": (
                "leading_edge_protein_coat",
            ),
        },
        changes="Retyped the leading-edge protein coat graph node as STRUCTURE.",
    ),
    Path("data/structures/spore/endospore_external_encapsulating_structure.yaml"): RecordFix(
        identifier="GO:0043591",
        graph_nodes={},
        changes=(
            "Removed the endospore cortex graph node's component_ref so the "
            "GO:0043595 structure node no longer points at the narrower "
            "peptidoglycan component."
        ),
    ),
}


def get_one(items: Iterable[dict[str, Any]], key: str, value: str) -> dict[str, Any]:
    matches = [item for item in items if item.get(key) == value]
    if len(matches) != 1:
        raise ValueError(f"expected exactly one {key}={value!r}; found {len(matches)}")
    return matches[0]


def retype_node(record: dict[str, Any], graph_id: str, node_id: str) -> bool:
    graph = get_one(record.get("causal_graphs") or [], "graph_id", graph_id)
    node = get_one(graph.get("nodes") or [], "node_id", node_id)
    node_type = node.get("node_type")
    if node_type == "STRUCTURE":
        return False
    if node_type != "GENE_OR_PROTEIN":
        raise ValueError(f"{graph_id}#{node_id} has unexpected node_type {node_type!r}")
    if not node.get("component_ref"):
        raise ValueError(f"{graph_id}#{node_id} has no component_ref")
    node["node_type"] = "STRUCTURE"
    return True


def retype_localization_node(record: dict[str, Any], graph_id: str, node_id: str) -> bool:
    graph = get_one(record.get("causal_graphs") or [], "graph_id", graph_id)
    node = get_one(graph.get("nodes") or [], "node_id", node_id)
    node_type = node.get("node_type")
    if node_type == "CELLULAR_LOCALIZATION":
        return False
    if node_type != "STRUCTURE":
        raise ValueError(f"{graph_id}#{node_id} has unexpected node_type {node_type!r}")
    if not node.get("grounding"):
        raise ValueError(f"{graph_id}#{node_id} has no grounding")
    node["node_type"] = "CELLULAR_LOCALIZATION"
    return True


def remove_t3ss_flagellum_xref(record: dict[str, Any]) -> bool:
    changed = False
    xrefs = record.get("xrefs") or []
    if "GO:0009288" in xrefs:
        record["xrefs"] = [xref for xref in xrefs if xref != "GO:0009288"]
        if not record["xrefs"]:
            del record["xrefs"]
        changed = True

    discussion = get_one(record.get("discussions") or [], "discussion_id", "flagellum_homology")
    old_rationale = (
        "The two export apparatuses are homologous and the schema has no relation "
        "for 'evolutionarily related to'. GO:0009288 is recorded as an xref for now, "
        "which understates the relationship: an xref means equivalence elsewhere, "
        "not shared ancestry."
    )
    new_rationale = (
        "The injectisome export apparatus and flagellar fT3SS are homologous, "
        "but the schema has no relation for 'evolutionarily related to'. A plain "
        "xref would imply equivalence elsewhere, not shared ancestry."
    )
    rationale = discussion.get("rationale")
    if rationale == new_rationale:
        return changed
    if rationale != old_rationale:
        raise ValueError("flagellum_homology rationale no longer matches the expected review text")
    discussion["rationale"] = new_rationale
    return True


def remove_endospore_cortex_component_ref(record: dict[str, Any]) -> bool:
    graph = get_one(record.get("causal_graphs") or [], "graph_id", "cortex_coat_resistance")
    node = get_one(graph.get("nodes") or [], "node_id", "cortex")
    component_ref = node.get("component_ref")
    if component_ref is None:
        return False
    if component_ref != "cortex":
        raise ValueError(f"cortex node has unexpected component_ref {component_ref!r}")
    del node["component_ref"]
    return True


def mutate_record(path: Path, record: dict[str, Any]) -> bool:
    relative = path.relative_to(REPO_ROOT)
    fix = FIXES[relative]
    if record.get("identifier") != fix.identifier:
        raise ValueError(
            f"{relative} identifier changed: expected {fix.identifier!r}, "
            f"found {record.get('identifier')!r}"
        )

    changed = False
    for graph_id, node_ids in fix.graph_nodes.items():
        for node_id in node_ids:
            changed = retype_node(record, graph_id, node_id) or changed
    for graph_id, node_ids in fix.localization_nodes.items():
        for node_id in node_ids:
            changed = retype_localization_node(record, graph_id, node_id) or changed

    if relative == Path("data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml"):
        changed = remove_t3ss_flagellum_xref(record) or changed
    if relative == Path("data/structures/spore/endospore_external_encapsulating_structure.yaml"):
        changed = remove_endospore_cortex_component_ref(record) or changed

    return changed


def run(*, apply: bool) -> int:
    changed_paths = []
    for relative in FIXES:
        path = REPO_ROOT / relative
        record = yaml.safe_load(path.read_text(encoding="utf-8"))
        if not mutate_record(path, record):
            print(f"{relative}: unchanged")
            continue

        print(f"{relative}: changed")
        changed_paths.append(relative)
        if apply:
            record_curation_event(
                record,
                curator="codex",
                action="ADDRESSED_REVIEW",
                changes=FIXES[relative].changes,
                llm_assisted=True,
            )
            write_validated_structure(record, path)

    if changed_paths and not apply:
        print(f"\ndry run: {len(changed_paths)} record(s) would change; pass --apply")
    elif not changed_paths:
        print("\nno review node-type fixes needed")
    return 0


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--apply", action="store_true", help="Write records (default: dry run).")
    args = parser.parse_args()
    try:
        return run(apply=args.apply)
    except (OSError, KeyError, TypeError, ValueError, ValidationFailedError) as exc:
        print(f"review node-type fix refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
