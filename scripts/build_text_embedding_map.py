#!/usr/bin/env python3
"""Build the reproducible text-embedding map and nearest-neighbour index.

``--refresh`` runs a pinned sentence-transformers model locally; corpus text is
never sent to a service (the model weights may be downloaded on first use). The
committed vector cache makes PCA, neighbours, rendering, and CI checks offline.
A record is stale as soon as the SHA-256 of its deliberately narrow semantic
text projection changes.

Usage:
    python scripts/build_text_embedding_map.py --refresh
    python scripts/build_text_embedding_map.py
    python scripts/build_text_embedding_map.py --check
"""

from __future__ import annotations

import argparse
import datetime
import hashlib
import json
import math
import sys
from pathlib import Path

import numpy as np

try:
    from corpus import REPO_ROOT, load_records
except ImportError:
    from scripts.corpus import REPO_ROOT, load_records


MODEL = "sentence-transformers/all-MiniLM-L6-v2"
MODEL_REVISION = "c9745ed1d9f207416be6d2e6f8de32d1f16199bf"
MODEL_LICENSE = "Apache-2.0"
SENTENCE_TRANSFORMERS_VERSION = "6.0.0"
PROJECTION_VERSION = 1
EMBEDDINGS_PATH = REPO_ROOT / "data" / "embeddings" / "structure_text_embeddings.json"
MAP_PATH = REPO_ROOT / "data" / "embeddings" / "structure_text_map.json"
NEIGHBORS_PATH = REPO_ROOT / "data" / "embeddings" / "structure_text_neighbors.json"


def clean(value: object) -> str:
    return " ".join(str(value or "").split())


def semantic_text(record: dict) -> str:
    """Project a record to stable biological prose, excluding provenance noise.

    IDs, citations, images, curation history, source-specific complex assertions,
    and imported protein examples are intentionally absent. They describe how a
    record was curated, not what the structure is.
    """
    lines = [
        f"name: {clean(record['label'])}",
        f"definition: {clean(record.get('definition'))}",
        f"category: {clean(record.get('structure_category')).lower()}",
        f"kind: {clean(record.get('structure_kind')).lower()}",
    ]
    synonyms = [clean(item.get("synonym_text")) for item in record.get("synonyms") or []]
    if synonyms:
        lines.append("synonyms: " + "; ".join(synonyms))
    for item in record.get("components") or []:
        parts = [clean(item.get("label")), clean(item.get("role"))]
        lines.append("component: " + ". ".join(part for part in parts if part))
    for item in record.get("functions") or []:
        parts = [clean(item.get("label")), clean(item.get("description"))]
        lines.append("function: " + ". ".join(part for part in parts if part))
    for item in record.get("taxonomic_distribution") or []:
        label = clean(item.get("taxon_label"))
        presence = clean(item.get("presence")).lower()
        lines.append(f"taxonomic scope: {label} ({presence})")
    for item in record.get("physical_properties") or []:
        prop = clean(item.get("property")).lower().replace("_", " ")
        context = clean(item.get("context"))
        lines.append("physical property: " + "; ".join(part for part in (prop, context) if part))
    return "\n".join(line for line in lines if not line.endswith(": ")) + "\n"


def corpus_inputs() -> list[dict]:
    records = []
    for path, record in load_records():
        text = semantic_text(record)
        page = path.relative_to(REPO_ROOT / "data" / "structures").with_suffix(".html")
        records.append(
            {
                "identifier": record["identifier"],
                "label": record["label"],
                "category": record["structure_category"],
                "source_path": str(path.relative_to(REPO_ROOT)),
                "page": f"structures/{page.as_posix()}",
                "text": text,
                "text_sha256": hashlib.sha256(text.encode()).hexdigest(),
            }
        )
    return records


def local_embeddings(texts: list[str]) -> list[list[float]]:
    """Encode every semantic line locally, then mean-pool by record.

    The model truncates long inputs, so encoding the labelled projection one
    line at a time ensures later components and functions are not discarded.
    No corpus text leaves the machine.
    """
    try:
        import sentence_transformers
        from sentence_transformers import SentenceTransformer
    except ImportError as exc:
        raise ValueError(
            "--refresh requires the embeddings extra: uv sync --extra embeddings"
        ) from exc
    if sentence_transformers.__version__ != SENTENCE_TRANSFORMERS_VERSION:
        raise ValueError(
            "refresh requires sentence-transformers "
            f"{SENTENCE_TRANSFORMERS_VERSION}, found {sentence_transformers.__version__}"
        )
    model = SentenceTransformer(MODEL, revision=MODEL_REVISION, trust_remote_code=False)
    chunks = [[line for line in text.splitlines() if line] for text in texts]
    flat = [line for record_chunks in chunks for line in record_chunks]
    encoded = np.asarray(
        model.encode(flat, batch_size=32, normalize_embeddings=True, show_progress_bar=False),
        dtype=float,
    )
    vectors = []
    offset = 0
    for record_chunks in chunks:
        pooled = encoded[offset : offset + len(record_chunks)].mean(axis=0)
        norm = np.linalg.norm(pooled)
        if not norm:
            raise ValueError("local model produced an all-zero record embedding")
        vectors.append((pooled / norm).tolist())
        offset += len(record_chunks)
    return vectors


def validate_vectors(vectors: list[list[float]], expected_count: int) -> int:
    if len(vectors) != expected_count or not vectors:
        raise ValueError(f"expected {expected_count} non-empty vectors, found {len(vectors)}")
    if any(not isinstance(vector, list) for vector in vectors):
        raise ValueError("every embedding must be a JSON list")
    dimensions = {len(vector) for vector in vectors}
    if len(dimensions) != 1:
        raise ValueError("embedding vectors do not all have one shared dimension")
    dimension = dimensions.pop()
    if dimension < 2:
        raise ValueError(f"embedding dimension must be at least 2, found {dimension}")
    if any(not math.isfinite(float(value)) for vector in vectors for value in vector):
        raise ValueError("embedding vectors contain a non-finite value")
    if any(not any(float(value) for value in vector) for vector in vectors):
        raise ValueError("embedding vectors must not be all zero")
    return dimension


def normalized_matrix(vectors: list[list[float]]) -> np.ndarray:
    matrix = np.asarray(vectors, dtype=float)
    norms = np.linalg.norm(matrix, axis=1, keepdims=True)
    if np.any(norms == 0):
        raise ValueError("embedding vectors must not be all zero")
    return matrix / norms


def pca_coordinates(vectors: list[list[float]]) -> tuple[np.ndarray, list[float]]:
    """Project normalized vectors to two dimensions with stable axis signs."""
    matrix = normalized_matrix(vectors)
    centered = matrix - matrix.mean(axis=0)
    u, singular, _ = np.linalg.svd(centered, full_matrices=False)
    coordinates = np.zeros((len(vectors), 2), dtype=float)
    available = min(2, len(singular))
    coordinates[:, :available] = u[:, :available] * singular[:available]
    for column in range(2):
        anchor = int(np.argmax(np.abs(coordinates[:, column])))
        if coordinates[anchor, column] < 0:
            coordinates[:, column] *= -1
    variance = singular**2
    total = float(variance.sum())
    ratios = [float(value / total) if total else 0.0 for value in variance[:2]]
    ratios.extend([0.0] * (2 - len(ratios)))
    return coordinates, ratios


def derived_documents(artifact: dict, inputs: list[dict]) -> tuple[dict, dict]:
    vectors = [item["embedding"] for item in artifact["records"]]
    coordinates, ratios = pca_coordinates(vectors)
    normalized = normalized_matrix(vectors)
    similarities = normalized @ normalized.T
    map_records = []
    neighbor_records = []
    for index, item in enumerate(inputs):
        map_records.append(
            {
                "identifier": item["identifier"],
                "label": item["label"],
                "category": item["category"],
                "page": item["page"],
                "x": round(float(coordinates[index, 0]), 8),
                "y": round(float(coordinates[index, 1]), 8),
            }
        )
        others = sorted(
            (other for other in range(len(inputs)) if other != index),
            key=lambda other: (-float(similarities[index, other]), inputs[other]["identifier"]),
        )
        neighbor_records.append(
            {
                "identifier": item["identifier"],
                "label": item["label"],
                "neighbors": [
                    {
                        "identifier": inputs[other]["identifier"],
                        "label": inputs[other]["label"],
                        "cosine_similarity": round(float(similarities[index, other]), 8),
                    }
                    for other in others[: min(5, len(others))]
                ],
            }
        )
    common = {
        "format_version": 1,
        "source_embeddings": str(EMBEDDINGS_PATH.relative_to(REPO_ROOT)),
        "model": artifact["model"],
        "model_revision": artifact["model_revision"],
        "generator_library": artifact["generator_library"],
        "embedding_dimension": artifact["embedding_dimension"],
        "text_projection_version": artifact["text_projection_version"],
    }
    map_document = {
        **common,
        "projection": {
            "method": "PCA of unit-normalized embeddings",
            "dimensions": 2,
            "explained_variance_ratio": [round(value, 8) for value in ratios],
            "note": "Coordinates are exploratory; distances in two dimensions are lossy.",
        },
        "records": map_records,
    }
    neighbors_document = {
        **common,
        "similarity": "cosine",
        "records": neighbor_records,
    }
    return map_document, neighbors_document


def write_json(path: Path, document: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(document, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def load_artifact() -> dict:
    if not EMBEDDINGS_PATH.exists():
        raise ValueError(f"{EMBEDDINGS_PATH.relative_to(REPO_ROOT)} is missing; run with --refresh")
    return json.loads(EMBEDDINGS_PATH.read_text(encoding="utf-8"))


def validate_artifact(artifact: dict, inputs: list[dict]) -> None:
    expected_ids = [item["identifier"] for item in inputs]
    actual_records = artifact.get("records") or []
    actual_ids = [item.get("identifier") for item in actual_records]
    if artifact.get("format_version") != 1:
        raise ValueError("unsupported embedding artifact format_version")
    if artifact.get("provider") != "sentence-transformers":
        raise ValueError("embedding artifact provider must be sentence-transformers")
    if artifact.get("model") != MODEL:
        raise ValueError(f"embedding artifact model must be pinned to {MODEL}")
    if artifact.get("model_revision") != MODEL_REVISION:
        raise ValueError(f"embedding artifact model revision must be pinned to {MODEL_REVISION}")
    if artifact.get("model_license") != MODEL_LICENSE:
        raise ValueError(f"embedding artifact model licence must be {MODEL_LICENSE}")
    if artifact.get("generator_library") != f"sentence-transformers {SENTENCE_TRANSFORMERS_VERSION}":
        raise ValueError("embedding artifact generator library is not pinned")
    if artifact.get("text_projection_version") != PROJECTION_VERSION:
        raise ValueError("embedding artifact text projection version is stale")
    if actual_ids != expected_ids:
        raise ValueError(
            f"embedding record order/coverage differs: expected {expected_ids}, found {actual_ids}"
        )
    for actual, expected in zip(actual_records, inputs, strict=True):
        for field in ("source_path", "text_sha256"):
            if actual.get(field) != expected[field]:
                raise ValueError(f"{actual['identifier']} {field} is stale; run with --refresh")
    dimension = validate_vectors([item.get("embedding") for item in actual_records], len(inputs))
    if artifact.get("embedding_dimension") != dimension:
        raise ValueError("embedding_dimension does not match the cached vectors")


def refresh(inputs: list[dict]) -> dict:
    vectors = local_embeddings([item["text"] for item in inputs])
    dimension = validate_vectors(vectors, len(inputs))
    artifact = {
        "format_version": 1,
        "provider": "sentence-transformers",
        "model": MODEL,
        "model_revision": MODEL_REVISION,
        "model_license": MODEL_LICENSE,
        "generator_library": f"sentence-transformers {SENTENCE_TRANSFORMERS_VERSION}",
        "embedding_dimension": dimension,
        "aggregation": "mean of unit-normalized semantic-line embeddings, then unit-normalized",
        "text_projection_version": PROJECTION_VERSION,
        "generated_on": datetime.date.today().isoformat(),
        "records": [
            {
                "identifier": item["identifier"],
                "source_path": item["source_path"],
                "text_sha256": item["text_sha256"],
                "embedding": [float(value) for value in vector],
            }
            for item, vector in zip(inputs, vectors, strict=True)
        ],
    }
    write_json(EMBEDDINGS_PATH, artifact)
    return artifact


def documents_close(actual: object, expected: object) -> bool:
    """Compare generated JSON while tolerating cross-platform BLAS roundoff."""
    if isinstance(actual, float) and isinstance(expected, float):
        return math.isclose(actual, expected, rel_tol=1e-6, abs_tol=1e-6)
    if type(actual) is not type(expected):
        return False
    if isinstance(actual, dict):
        return actual.keys() == expected.keys() and all(
            documents_close(actual[key], expected[key]) for key in actual
        )
    if isinstance(actual, list):
        return len(actual) == len(expected) and all(
            documents_close(left, right) for left, right in zip(actual, expected, strict=True)
        )
    return actual == expected


def check_derived(expected_map: dict, expected_neighbors: dict) -> None:
    for path, expected in ((MAP_PATH, expected_map), (NEIGHBORS_PATH, expected_neighbors)):
        if not path.exists():
            raise ValueError(f"{path.relative_to(REPO_ROOT)} is missing; rebuild the map")
        actual = json.loads(path.read_text(encoding="utf-8"))
        if not documents_close(actual, expected):
            raise ValueError(f"{path.relative_to(REPO_ROOT)} is stale; rebuild the map")


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    mode = parser.add_mutually_exclusive_group()
    mode.add_argument(
        "--refresh", action="store_true", help="Run the pinned local model and replace cached vectors."
    )
    mode.add_argument(
        "--check", action="store_true", help="Verify vectors and derived files without writing."
    )
    args = parser.parse_args()
    try:
        inputs = corpus_inputs()
        artifact = refresh(inputs) if args.refresh else load_artifact()
        validate_artifact(artifact, inputs)
        map_document, neighbors_document = derived_documents(artifact, inputs)
        if args.check:
            check_derived(map_document, neighbors_document)
            print(
                f"text embedding map is current: {len(inputs)} records, "
                f"{artifact['embedding_dimension']} dimensions, {artifact['model']}"
            )
            return 0
        write_json(MAP_PATH, map_document)
        write_json(NEIGHBORS_PATH, neighbors_document)
        action = "refreshed" if args.refresh else "rebuilt"
        print(f"{action} text embedding map for {len(inputs)} records")
        return 0
    except (KeyError, OSError, TypeError, ValueError, json.JSONDecodeError) as exc:
        print(f"text embedding map refused: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
