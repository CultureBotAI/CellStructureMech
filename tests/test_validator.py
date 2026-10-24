"""Unit tests for semantic record validation in validator.py (#2408, #2410, #2417)."""

from __future__ import annotations

import pytest

from cellstructuremech.validation.validator import (
    validate_causal_graphs,
    validate_component_protein_examples,
    validate_discussion_issue_links,
    validate_record_semantics,
)
from cellstructuremech.validation.write_validated import (
    ValidationFailedError,
    validate_structure,
    write_validated_structure,
)

BASE_RECORD = {
    "identifier": "GO:0005840",
    "label": "ribosome",
    "definition": "A ribonucleoprotein complex that translates messenger RNA.",
    "definition_source": "GO:0005840",
    "structure_category": "RIBONUCLEOPROTEIN",
    "structure_kind": "RIBONUCLEOPROTEIN_COMPLEX",
    "mapping_status": "PROPOSED",
}


def test_connected_graph_with_edge_descriptions_passes():
    doc = {
        **BASE_RECORD,
        "causal_graphs": [
            {
                "graph_id": "g1",
                "graph_kind": "FUNCTION",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {"node_id": "a", "label": "ribosome", "node_type": "STRUCTURE"},
                    {"node_id": "b", "label": "translation", "node_type": "BIOLOGICAL_PROCESS"},
                ],
                "edges": [
                    {
                        "subject": "a",
                        "predicate": "carries out",
                        "object": "b",
                        "description": (
                            "The assembled ribosome catalyzes mRNA-directed polypeptide synthesis."
                        ),
                        "evidence": [
                            {"reference": "PMID:12345678", "notes": "Supported by experimental assay."}
                        ],
                    }
                ],
            }
        ],
    }
    assert validate_causal_graphs(doc) == []
    assert validate_record_semantics(doc) == []
    assert validate_structure(doc) == []


def test_isolated_causal_node_is_flagged_and_blocks_write(tmp_path):
    doc = {
        **BASE_RECORD,
        "causal_graphs": [
            {
                "graph_id": "g1",
                "graph_kind": "ASSEMBLY",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {"node_id": "a", "label": "subunit A", "node_type": "GENE_OR_PROTEIN"},
                    {"node_id": "b", "label": "assembled complex", "node_type": "STRUCTURE"},
                    {"node_id": "orphan_node", "label": "orphan factor", "node_type": "GENE_OR_PROTEIN"},
                ],
                "edges": [
                    {
                        "subject": "a",
                        "predicate": "assembles into",
                        "object": "b",
                        "description": "Subunit A oligomerizes into the assembled complex.",
                        "evidence": [{"reference": "PMID:12345678", "notes": "Assembly assay."}],
                    }
                ],
            }
        ],
    }
    errors = validate_causal_graphs(doc)
    assert len(errors) == 1
    assert "isolated CausalNode 'orphan_node' has zero incident edges" in errors[0]
    with pytest.raises(ValidationFailedError, match="orphan_node"):
        write_validated_structure(doc, tmp_path / "orphan.yaml")


@pytest.mark.parametrize("bad_desc", [None, "", "   "])
def test_causal_edge_missing_or_blank_description_is_flagged(bad_desc):
    edge = {
        "subject": "a",
        "predicate": "carries out",
        "object": "b",
        "evidence": [{"reference": "PMID:12345678", "notes": "Supported by assay."}],
    }
    if bad_desc is not None:
        edge["description"] = bad_desc
    doc = {
        **BASE_RECORD,
        "causal_graphs": [
            {
                "graph_id": "g1",
                "graph_kind": "FUNCTION",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {"node_id": "a", "label": "ribosome", "node_type": "STRUCTURE"},
                    {"node_id": "b", "label": "translation", "node_type": "BIOLOGICAL_PROCESS"},
                ],
                "edges": [edge],
            }
        ],
    }
    errors = validate_causal_graphs(doc)
    assert len(errors) == 1
    assert "lacks a non-empty description" in errors[0]
    assert validate_structure(doc)


def test_discussion_referencing_issue_in_prose_requires_structured_issue_evidence():
    missing_link_doc = {
        **BASE_RECORD,
        "discussions": [
            {
                "discussion_id": "scope_note",
                "kind": "KNOWLEDGE_GAP",
                "status": "OPEN",
                "prompt": "Taxon pairing remains blocked pending #2052 and #2358.",
                "evidence": [
                    {
                        "reference": "https://github.com/CultureBotAI/CellStructureMech/issues/2052",
                        "notes": "Tracks #2052 only.",
                    }
                ],
            }
        ],
    }
    errors = validate_discussion_issue_links(missing_link_doc)
    assert len(errors) == 1
    assert "#2358" in errors[0]
    assert "#2052" not in errors[0]
    assert validate_structure(missing_link_doc)

    complete_link_doc = {
        **BASE_RECORD,
        "discussions": [
            {
                "discussion_id": "scope_note",
                "kind": "KNOWLEDGE_GAP",
                "status": "OPEN",
                "prompt": "Taxon pairing remains blocked pending #2052 and #2358.",
                "evidence": [
                    {
                        "reference": "https://github.com/CultureBotAI/CellStructureMech/issues/2052",
                        "notes": "Tracks #2052.",
                    },
                    {
                        "reference": "https://github.com/CultureBotAI/CellStructureMech/issues/2358",
                        "notes": "Tracks #2358.",
                    },
                ],
            }
        ],
    }
    assert validate_discussion_issue_links(complete_link_doc) == []
    assert validate_structure(complete_link_doc) == []


@pytest.mark.parametrize(
    "grounding",
    ["GO:0030122", "cellstructuremech:chlorosome_baseplate_antenna_complex"],
)
def test_gene_or_protein_causal_node_with_structure_grounding_is_flagged(grounding):
    doc = {
        **BASE_RECORD,
        "causal_graphs": [
            {
                "graph_id": "g1",
                "graph_kind": "FUNCTION",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {
                        "node_id": "complex_node",
                        "label": "AP-2 adaptor complex",
                        "node_type": "GENE_OR_PROTEIN",
                        "grounding": grounding,
                    },
                    {"node_id": "coat", "label": "clathrin coat", "node_type": "STRUCTURE"},
                ],
                "edges": [
                    {
                        "subject": "complex_node",
                        "predicate": "recruits",
                        "object": "coat",
                        "description": "The adaptor complex recruits clathrin to the pit.",
                        "evidence": [{"reference": "PMID:12345678", "notes": "Assay."}],
                    }
                ],
            }
        ],
    }
    errors = validate_causal_graphs(doc)
    assert len(errors) == 1
    assert "expected 'STRUCTURE'" in errors[0]
    assert validate_structure(doc)


def test_gene_or_protein_causal_node_referencing_grounded_protein_complex_is_flagged():
    doc = {
        **BASE_RECORD,
        "components": [
            {
                "component_id": "csma_baseplate",
                "label": "chlorosome baseplate antenna complex",
                "component_type": "PROTEIN_COMPLEX",
                "component_role": "CONSTITUENT",
                "grounding": "cellstructuremech:chlorosome_baseplate_antenna_complex",
            }
        ],
        "causal_graphs": [
            {
                "graph_id": "g1",
                "graph_kind": "FUNCTION",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {
                        "node_id": "csma_baseplate",
                        "label": "CsmA baseplate",
                        "node_type": "GENE_OR_PROTEIN",
                        "component_ref": "csma_baseplate",
                    },
                    {"node_id": "rc", "label": "reaction center", "node_type": "STRUCTURE"},
                ],
                "edges": [
                    {
                        "subject": "csma_baseplate",
                        "predicate": "transfers excitation energy to",
                        "object": "rc",
                        "description": "The CsmA baseplate funnels excitation energy to the reaction center.",
                        "evidence": [{"reference": "PMID:12345678", "notes": "Spectroscopy."}],
                    }
                ],
            }
        ],
    }
    errors = validate_causal_graphs(doc)
    assert len(errors) == 1
    assert "referencing grounded PROTEIN_COMPLEX component 'csma_baseplate'" in errors[0]
    assert validate_structure(doc)


def test_component_protein_examples_gene_symbol_consistency():
    bad_doc = {
        **BASE_RECORD,
        "components": [
            {
                "component_id": "flagellin",
                "label": "flagellin",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "gene_symbols": ["fliC", "fljB"],
                "evidence": [{"reference": "PMID:12345678", "notes": "Component evidence."}],
                "protein_examples": [
                    {
                        "uniprot_id": "UniProtKB:P02968",
                        "protein_label": "Flagellin",
                        "gene_symbol": "hag",
                        "taxon_id": "NCBITaxon:224308",
                        "taxon_label": "Bacillus subtilis subsp. subtilis str. 168",
                        "entry_status": "REVIEWED",
                        "retrieved_on": "2026-10-17",
                        "role": "Reviewed UniProtKB entry in Bacillus subtilis.",
                        "evidence": [
                            {
                                "reference": "https://www.uniprot.org/uniprotkb/P02968",
                                "notes": "Reviewed entry.",
                            }
                        ],
                    }
                ],
            }
        ],
    }
    errors = validate_component_protein_examples(bad_doc)
    assert len(errors) == 1
    assert "gene_symbol 'hag' is not in component.gene_symbols" in errors[0]
    assert validate_structure(bad_doc)

    # Disclosing the synonym in role or adding the symbol to gene_symbols resolves the error
    disclosed_doc = {
        **BASE_RECORD,
        "components": [
            {
                **bad_doc["components"][0],
                "protein_examples": [
                    {
                        **bad_doc["components"][0]["protein_examples"][0],
                        "role": (
                            "Reviewed entry in Bacillus subtilis (also declared as synonym fliC)."
                        ),
                    }
                ],
            }
        ],
    }
    assert validate_component_protein_examples(disclosed_doc) == []
    assert validate_structure(disclosed_doc) == []

