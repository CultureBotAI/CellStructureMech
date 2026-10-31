"""Unit tests for semantic record validation in validator.py
(#2408, #2410, #2417, #2428, #2457, #2472, #2486)."""

from __future__ import annotations

import pytest

from cellstructuremech.validation.validator import (
    validate_causal_graphs,
    validate_component_protein_examples,
    validate_curation_history,
    validate_discussion_issue_links,
    validate_hierarchy_relations,
    validate_record_semantics,
    validate_top_level_pmid_parity,
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


def test_causal_node_component_ref_requires_grounding_propagation():
    missing_grounding_doc = {
        **BASE_RECORD,
        "components": [
            {
                "component_id": "bam_b",
                "label": "BamB outer-membrane lipoprotein",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "grounding": "InterPro:IPR017688",
                "evidence": [{"reference": "PMID:12345678", "notes": "Component evidence."}],
            }
        ],
        "causal_graphs": [
            {
                "graph_id": "bam_assembly",
                "graph_kind": "ASSEMBLY",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {
                        "node_id": "bam_b",
                        "label": "BamB",
                        "node_type": "GENE_OR_PROTEIN",
                        "component_ref": "bam_b",
                    },
                    {"node_id": "bam_complex", "label": "BAM complex", "node_type": "STRUCTURE"},
                ],
                "edges": [
                    {
                        "subject": "bam_b",
                        "predicate": "part of",
                        "object": "bam_complex",
                        "description": "BamB associates with the BAM complex.",
                        "evidence": [{"reference": "PMID:12345678", "notes": "Assay."}],
                    }
                ],
            }
        ],
    }
    errors = validate_causal_graphs(missing_grounding_doc)
    assert len(errors) == 1
    assert "omits grounding 'InterPro:IPR017688' from referenced component" in errors[0]
    assert validate_structure(missing_grounding_doc)

    propagated_doc = {
        **missing_grounding_doc,
        "causal_graphs": [
            {
                **missing_grounding_doc["causal_graphs"][0],
                "nodes": [
                    {
                        **missing_grounding_doc["causal_graphs"][0]["nodes"][0],
                        "grounding": "InterPro:IPR017688",
                    },
                    missing_grounding_doc["causal_graphs"][0]["nodes"][1],
                ],
            }
        ],
    }
    assert validate_causal_graphs(propagated_doc) == []
    assert validate_structure(propagated_doc) == []


def test_curated_causal_graph_history_target_must_match_record_graph_id():
    bad_history_doc = {
        **BASE_RECORD,
        "causal_graphs": [
            {
                "graph_id": "static_microtubule_bundle_organization",
                "graph_kind": "ASSEMBLY",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {"node_id": "a", "label": "alpha-tubulin", "node_type": "GENE_OR_PROTEIN"},
                    {"node_id": "b", "label": "beta-tubulin", "node_type": "GENE_OR_PROTEIN"},
                ],
                "edges": [
                    {
                        "subject": "a",
                        "predicate": "heterodimerizes with",
                        "object": "b",
                        "description": "Alpha- and beta-tubulin form heterodimers.",
                        "evidence": [{"reference": "PMID:12345678", "notes": "Assay."}],
                    }
                ],
            }
        ],
        "curation_history": [
            {
                "timestamp": "2026-10-25T00:00:00Z",
                "curator": "curator",
                "action": "CURATED_CAUSAL_GRAPH",
                "changes": (
                    "Added alpha_tubulin -> beta_tubulin heterodimerization edge in "
                    "static_microtubule_bundle_assembly (PMID:12345678)."
                ),
            }
        ],
    }
    errors = validate_curation_history(bad_history_doc)
    assert len(errors) == 1
    assert "static_microtubule_bundle_assembly" in errors[0]
    assert validate_structure(bad_history_doc)

    good_history_doc = {
        **bad_history_doc,
        "curation_history": [
            {
                **bad_history_doc["curation_history"][0],
                "changes": (
                    "Added alpha_tubulin -> beta_tubulin heterodimerization edge in "
                    "static_microtubule_bundle_organization (PMID:12345678)."
                ),
            }
        ],
    }
    assert validate_curation_history(good_history_doc) == []
    assert validate_structure(good_history_doc) == []


def test_discussion_referencing_doi_or_pmid_requires_structured_evidence():
    missing_citation_doc = {
        **BASE_RECORD,
        "discussions": [
            {
                "discussion_id": "cartwheel_note",
                "kind": "CONTROVERSY",
                "status": "OPEN",
                "prompt": "How is cartwheel symmetry maintained?",
                "notes": (
                    "Supported by DOI:10.1038/nsmb.2865 and PMID:18497260 in Chlamydomonas."
                ),
                "evidence": [
                    {
                        "reference": "DOI:10.1038/nsmb.2865",
                        "notes": "Guichard et al. 2014.",
                    }
                ],
            }
        ],
    }
    errors = validate_discussion_issue_links(missing_citation_doc)
    assert len(errors) == 1
    assert "PMID:18497260" in errors[0]
    assert "10.1038/nsmb.2865" not in errors[0]
    assert validate_structure(missing_citation_doc)

    complete_citation_doc = {
        **BASE_RECORD,
        "discussions": [
            {
                **missing_citation_doc["discussions"][0],
                "evidence": [
                    *missing_citation_doc["discussions"][0]["evidence"],
                    {
                        "reference": "PMID:18497260",
                        "notes": "Additional supporting study.",
                    },
                ],
            }
        ],
    }
    assert validate_discussion_issue_links(complete_citation_doc) == []
    assert validate_structure(complete_citation_doc) == []


def test_hierarchy_relation_disjointness():
    dup_parent_part_of_doc = {
        **BASE_RECORD,
        "parent_structures": ["GO:1990586"],
        "part_of": ["GO:1990586"],
    }
    errors = validate_hierarchy_relations(dup_parent_part_of_doc)
    assert len(errors) == 1
    assert "'GO:1990586' appears in both parent_structures (is-a) and part_of (parthood)" in errors[0]
    assert validate_structure(dup_parent_part_of_doc)

    dup_parent_component_doc = {
        **BASE_RECORD,
        "parent_structures": ["GO:0005681"],
        "components": [
            {
                "component_id": "spliceosomal_complex",
                "label": "spliceosomal complex",
                "component_type": "PROTEIN_COMPLEX",
                "component_role": "CONSTITUENT",
                "grounding": "GO:0005681",
                "evidence": [{"reference": "PMID:12345678", "notes": "Component evidence."}],
            }
        ],
    }
    comp_errors = validate_hierarchy_relations(dup_parent_component_doc)
    assert len(comp_errors) == 1
    assert "CONSTITUENT grounding 'GO:0005681' duplicates parent_structures (is-a)" in comp_errors[0]
    assert validate_structure(dup_parent_component_doc)

    disjoint_doc = {
        **BASE_RECORD,
        "parent_structures": ["GO:0032991"],
        "part_of": ["GO:1990586"],
        "has_part": ["GO:0015934"],
        "components": [
            {
                "component_id": "large_subunit",
                "label": "large ribosomal subunit",
                "component_type": "PROTEIN_COMPLEX",
                "component_role": "CONSTITUENT",
                "grounding": "GO:0015934",
                "evidence": [{"reference": "PMID:12345678", "notes": "Component evidence."}],
            }
        ],
    }
    assert validate_hierarchy_relations(disjoint_doc) == []
    assert validate_structure(disjoint_doc) == []


def test_causal_node_component_ref_grounding_and_type_consistency():
    mismatch_doc = {
        **BASE_RECORD,
        "components": [
            {
                "component_id": "flagellin",
                "label": "flagellin",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "grounding": "InterPro:IPR001029",
                "evidence": [{"reference": "PMID:12345678", "notes": "Component evidence."}],
            }
        ],
        "causal_graphs": [
            {
                "graph_id": "flagellar_assembly",
                "graph_kind": "ASSEMBLY",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {
                        "node_id": "filament",
                        "label": "flagellar filament",
                        "node_type": "STRUCTURE",
                        "component_ref": "flagellin",
                        "grounding": "GO:0009420",
                    },
                    {"node_id": "hook", "label": "flagellar hook", "node_type": "STRUCTURE"},
                ],
                "edges": [
                    {
                        "subject": "hook",
                        "predicate": "nucleates",
                        "object": "filament",
                        "description": "The hook-filament junction nucleates flagellin polymerization.",
                        "evidence": [{"reference": "PMID:12345678", "notes": "Assay."}],
                    }
                ],
            }
        ],
    }
    errors = validate_causal_graphs(mismatch_doc)
    assert len(errors) == 2
    assert any("referencing PROTEIN component 'flagellin' (expected 'GENE_OR_PROTEIN')" in e for e in errors)
    assert any(
        "grounding 'GO:0009420' conflicting with referenced component grounding 'InterPro:IPR001029'"
        in e
        for e in errors
    )
    assert validate_structure(mismatch_doc)

    fixed_doc = {
        **mismatch_doc,
        "causal_graphs": [
            {
                **mismatch_doc["causal_graphs"][0],
                "nodes": [
                    {
                        "node_id": "flagellin_monomer",
                        "label": "flagellin",
                        "node_type": "GENE_OR_PROTEIN",
                        "component_ref": "flagellin",
                        "grounding": "InterPro:IPR001029",
                    },
                    {"node_id": "filament", "label": "flagellar filament", "node_type": "STRUCTURE"},
                ],
                "edges": [
                    {
                        "subject": "flagellin_monomer",
                        "predicate": "polymerizes into",
                        "object": "filament",
                        "description": "Flagellin monomers polymerize into the helical filament.",
                        "evidence": [{"reference": "PMID:12345678", "notes": "Assay."}],
                    }
                ],
            }
        ],
    }
    assert validate_causal_graphs(fixed_doc) == []
    assert validate_structure(fixed_doc) == []


def test_component_with_empty_gene_symbols_and_protein_example_is_flagged():
    bad_doc = {
        **BASE_RECORD,
        "components": [
            {
                "component_id": "emtoc",
                "label": "equatorial microtubule organizing center",
                "component_type": "PROTEIN_COMPLEX",
                "component_role": "CONSTITUENT",
                "grounding": "GO:0000923",
                "evidence": [{"reference": "PMID:12345678", "notes": "Component evidence."}],
                "protein_examples": [
                    {
                        "uniprot_id": "UniProtKB:O94488",
                        "protein_label": "Gamma tubulin complex adapter mto1",
                        "gene_symbol": "mto1",
                        "taxon_id": "NCBITaxon:284812",
                        "taxon_label": "Schizosaccharomyces pombe 972h-",
                        "entry_status": "REVIEWED",
                        "retrieved_on": "2026-10-17",
                        "role": (
                            "Representative reviewed UniProtKB entry for gene mto1 in "
                            "Schizosaccharomyces pombe 972h-. Identifier for the component's "
                            "declared gene symbol."
                        ),
                        "evidence": [
                            {
                                "reference": "PMID:15004232",
                                "notes": "Experimental localization.",
                            }
                        ],
                    }
                ],
            }
        ],
    }
    errors = validate_component_protein_examples(bad_doc)
    assert len(errors) == 1
    assert "declares gene_symbol 'mto1' on a component with empty gene_symbols" in errors[0]
    assert validate_structure(bad_doc)

    fixed_doc = {
        **BASE_RECORD,
        "components": [
            {
                **bad_doc["components"][0],
                "gene_symbols": ["mto1"],
            }
        ],
    }
    assert validate_component_protein_examples(fixed_doc) == []
    assert validate_structure(fixed_doc) == []


def test_function_and_causal_node_go_grounding_and_aspect_consistency():
    bad_doc = {
        **BASE_RECORD,
        "functions": [
            {
                "function_id": "dna_replication_origin_binding",
                "label": "DNA replication origin binding",
                "grounding": "GO:0003688",
                "description": "Recognizes DNA replication origins in an ATP-dependent manner.",
                "evidence": [
                    {
                        "reference": "GO:0003688",
                        "notes": (
                            "GO:0003688 is the Gene Ontology molecular-function term for "
                            "DNA replication origin binding."
                        ),
                    }
                ],
            },
            {
                "function_id": "macroautophagy",
                "label": "macroautophagy",
                "description": "Delivers cytoplasmic cargo to the lytic vacuole.",
                "evidence": [
                    {
                        "reference": "GO:0016236",
                        "notes": "GO:0016236 defines macroautophagy.",
                    }
                ],
            },
        ],
        "causal_graphs": [
            {
                "graph_id": "func_graph",
                "graph_kind": "FUNCTION",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {"node_id": "complex", "label": "complex", "node_type": "STRUCTURE"},
                    {
                        "node_id": "dna_replication_origin_binding",
                        "label": "DNA replication origin binding",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0003688",
                    },
                    {
                        "node_id": "macroautophagy",
                        "label": "macroautophagy",
                        "node_type": "BIOLOGICAL_PROCESS",
                        "grounding": "GO:0016236",
                    },
                ],
                "edges": [
                    {
                        "subject": "complex",
                        "predicate": "mediates",
                        "object": "dna_replication_origin_binding",
                        "description": "The complex mediates DNA replication origin binding.",
                        "evidence": [{"reference": "GO:0003688", "notes": "MF term."}],
                    },
                    {
                        "subject": "complex",
                        "predicate": "supports",
                        "object": "macroautophagy",
                        "description": "The complex supports macroautophagy.",
                        "evidence": [{"reference": "GO:0016236", "notes": "BP term."}],
                    },
                ],
            }
        ],
    }
    errors = validate_causal_graphs(bad_doc)
    assert len(errors) == 2
    assert any(
        "has node_type 'BIOLOGICAL_PROCESS' contradicting molecular_function aspect on "
        "functions#dna_replication_origin_binding" in e
        for e in errors
    )
    assert any(
        "functions#macroautophagy: omits grounding 'GO:0016236' present on matching "
        "CausalNode 'macroautophagy'" in e
        for e in errors
    )
    assert validate_structure(bad_doc)

    fixed_doc = {
        **bad_doc,
        "functions": [
            bad_doc["functions"][0],
            {
                **bad_doc["functions"][1],
                "grounding": "GO:0016236",
            },
        ],
        "causal_graphs": [
            {
                **bad_doc["causal_graphs"][0],
                "nodes": [
                    bad_doc["causal_graphs"][0]["nodes"][0],
                    {
                        **bad_doc["causal_graphs"][0]["nodes"][1],
                        "node_type": "MOLECULAR_FUNCTION",
                    },
                    bad_doc["causal_graphs"][0]["nodes"][2],
                ],
            }
        ],
    }
    assert validate_causal_graphs(fixed_doc) == []
    assert validate_structure(fixed_doc) == []


def test_top_level_pmid_evidence_parity_is_enforced():
    bad_doc = {
        **BASE_RECORD,
        "evidence": [
            {
                "reference": "GO:0005840",
                "notes": "GO term definition.",
            },
            {
                "reference": "PMID:10985327",
                "notes": "Primary study.",
            },
        ],
        "components": [
            {
                "component_id": "sid2",
                "label": "Sid2 kinase",
                "component_type": "PROTEIN",
                "component_role": "CONSTITUENT",
                "gene_symbols": ["sid2"],
                "evidence": [
                    {"reference": "PMID:11069087", "notes": "Mob1-Sid2 complex assembly."}
                ],
            }
        ],
        "taxonomic_distribution": [
            {
                "taxon_id": "NCBITaxon:4896",
                "taxon_label": "Schizosaccharomyces pombe",
                "presence": "COMMON",
                "reference": "PMID:11069087",
                "note": "Demonstrated in fission yeast.",
            }
        ],
        "functions": [
            {
                "function_id": "sin_signaling",
                "label": "septation initiation signaling",
                "description": "Triggers medial ring constriction.",
                "evidence": [
                    {"reference": "PMID:11069087", "notes": "Required for cytokinesis."}
                ],
            }
        ],
        "causal_graphs": [
            {
                "graph_id": "sid2_mob1_assembly",
                "graph_kind": "ASSEMBLY",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {
                        "node_id": "sid2",
                        "label": "Sid2 kinase",
                        "node_type": "GENE_OR_PROTEIN",
                        "component_ref": "sid2",
                    },
                    {"node_id": "complex", "label": "Sid2-Mob1 complex", "node_type": "STRUCTURE"},
                ],
                "edges": [
                    {
                        "subject": "sid2",
                        "predicate": "assembles into",
                        "object": "complex",
                        "description": "Sid2 kinase associates with Mob1 to form the active complex.",
                        "evidence": [
                            {"reference": "PMID:11069087", "notes": "Co-immunoprecipitation."}
                        ],
                    }
                ],
            }
        ],
    }
    errors = validate_top_level_pmid_parity(bad_doc)
    assert len(errors) == 4
    assert any("components#sid2: cites 'PMID:11069087'" in e for e in errors)
    assert any("taxonomic_distribution#NCBITaxon:4896: cites 'PMID:11069087'" in e for e in errors)
    assert any("functions#sin_signaling: cites 'PMID:11069087'" in e for e in errors)
    assert any("causal_graphs#sid2_mob1_assembly.edges[0]: cites 'PMID:11069087'" in e for e in errors)
    assert validate_structure(bad_doc)

    fixed_doc = {
        **bad_doc,
        "evidence": [
            *bad_doc["evidence"],
            {
                "reference": "PMID:11069087",
                "notes": "Mob1-Sid2 complex assembly and cytokinesis requirement.",
            },
        ],
    }
    assert validate_top_level_pmid_parity(fixed_doc) == []
    assert validate_structure(fixed_doc) == []


def test_two_node_parthood_only_structure_causal_graph_marked_mechanistic_is_flagged():
    bad_doc = {
        **BASE_RECORD,
        "structure_category": "MEMBRANE_ORGANELLE",
        "structure_kind": "MEMBRANE",
        "causal_graphs": [
            {
                "graph_id": "reservosome_membrane_parthood",
                "graph_kind": "ASSEMBLY",
                "scope_status": "MECHANISTIC",
                "nodes": [
                    {
                        "node_id": "reservosome_membrane",
                        "label": "reservosome membrane",
                        "node_type": "STRUCTURE",
                        "grounding": "GO:0106126",
                    },
                    {
                        "node_id": "reservosome",
                        "label": "reservosome",
                        "node_type": "STRUCTURE",
                        "grounding": "GO:0033011",
                    },
                ],
                "edges": [
                    {
                        "subject": "reservosome_membrane",
                        "predicate": "is part of",
                        "object": "reservosome",
                        "description": "The reservosome membrane bounds the reservosome.",
                        "evidence": [{"reference": "GO:0106126", "notes": "GO parthood."}],
                    }
                ],
            }
        ],
    }
    errors = validate_causal_graphs(bad_doc)
    assert len(errors) == 1
    assert (
        "reservosome_membrane_parthood: 2-node 1-edge STRUCTURE graph with parthood-only "
        "predicate 'is part of' has scope_status 'MECHANISTIC' (expected 'NONMECHANISTIC' or 'INCOMPLETE')"
        in errors[0]
    )
    assert validate_structure(bad_doc)

    fixed_doc = {
        **bad_doc,
        "causal_graphs": [
            {
                **bad_doc["causal_graphs"][0],
                "scope_status": "NONMECHANISTIC",
            }
        ],
    }
    assert validate_causal_graphs(fixed_doc) == []
    assert validate_structure(fixed_doc) == []





