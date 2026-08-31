"""Contracts for the committed semantic text map."""

from __future__ import annotations

import json

import numpy as np

from scripts import build_text_embedding_map as text_map


def test_semantic_projection_includes_biology_and_excludes_provenance():
    record = {
        "identifier": "GO:1",
        "label": "test structure",
        "definition": "A useful structure.",
        "definition_source": "DOI:secret",
        "structure_category": "OTHER",
        "structure_kind": "MULTIPROTEIN_COMPLEX",
        "synonyms": [{"synonym_text": "test body", "source": "PMID:1"}],
        "components": [
            {
                "label": "core protein",
                "role": "Builds the shell.",
                "evidence": [{"reference": "PMID:2"}],
                "protein_examples": [{"protein_label": "source-specific protein"}],
            }
        ],
        "complex_compositions": [{"label": "source-specific composition"}],
        "functions": [{"label": "transport", "description": "Moves cargo."}],
        "taxonomic_distribution": [{"taxon_label": "Bacteria", "presence": "COMMON"}],
        "images": [{"caption": "microscopy provenance"}],
        "curation_history": [{"changes": "agent prose"}],
    }
    projection = text_map.semantic_text(record)
    assert "test structure" in projection
    assert "core protein. Builds the shell." in projection
    assert "transport. Moves cargo." in projection
    assert "Bacteria (common)" in projection
    for excluded in (
        "GO:1",
        "DOI:secret",
        "PMID:1",
        "PMID:2",
        "source-specific protein",
        "source-specific composition",
        "microscopy provenance",
        "agent prose",
    ):
        assert excluded not in projection


def test_pca_projection_is_deterministic_across_input_order():
    vectors = [
        [1.0, 0.2, 0.1, 0.0],
        [0.1, 1.0, 0.3, 0.0],
        [0.2, 0.1, 1.0, 0.4],
        [0.7, 0.3, 0.2, 0.8],
    ]
    original, original_ratio = text_map.pca_coordinates(vectors)
    order = [2, 0, 3, 1]
    permuted, permuted_ratio = text_map.pca_coordinates([vectors[index] for index in order])
    restored = np.empty_like(permuted)
    for new_index, old_index in enumerate(order):
        restored[old_index] = permuted[new_index]
    assert np.allclose(original, restored)
    assert np.allclose(original_ratio, permuted_ratio)


def test_derived_comparison_allows_only_small_float_roundoff():
    expected = {"records": [{"identifier": "GO:1", "x": 0.12345678}]}
    assert text_map.documents_close(
        {"records": [{"identifier": "GO:1", "x": 0.12345718}]}, expected
    )
    assert not text_map.documents_close(
        {"records": [{"identifier": "GO:1", "x": 0.12445678}]}, expected
    )
    assert not text_map.documents_close(
        {"records": [{"identifier": "GO:2", "x": 0.12345678}]}, expected
    )


def test_committed_embedding_artifacts_cover_current_corpus():
    inputs = text_map.corpus_inputs()
    artifact = json.loads(text_map.EMBEDDINGS_PATH.read_text(encoding="utf-8"))
    text_map.validate_artifact(artifact, inputs)
    expected_map, expected_neighbors = text_map.derived_documents(artifact, inputs)
    text_map.check_derived(expected_map, expected_neighbors)
    assert len(expected_map["records"]) == len(inputs)
    assert all(len(item["neighbors"]) == len(inputs) - 1 for item in expected_neighbors["records"])
