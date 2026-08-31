# Text embedding map design (2026-08-30)

## Decision

CellStructureMech now follows the sibling Mech pattern of committed vectors,
two-dimensional coordinates, nearest-neighbour data, a generated interactive
page, and an offline staleness check. This map uses record text rather than a
knowledge-graph walk because the requested comparison is semantic content.

There are only four current records. UMAP and PaCMAP neighbourhood layouts are
not meaningful or stable at that size, so the display uses PCA over
unit-normalized vectors. The full 384-dimensional vectors remain authoritative
for cosine neighbours; the page calls the two-dimensional view exploratory.

## Model and privacy

- Model: `sentence-transformers/all-MiniLM-L6-v2`
- Revision: `c9745ed1d9f207416be6d2e6f8de32d1f16199bf`
- Licence: Apache-2.0
- Output: 384 dimensions
- Execution: local with `sentence-transformers==6.0.0` through the optional
  `embeddings` dependency

An authenticated CBorg embedding endpoint was considered, but using it would
transmit the projected record text. The implemented refresh instead runs the
already cached open model locally; no corpus text leaves the machine. The model
revision, licence, dimension, aggregation rule, generation date, record paths,
and text hashes are stored with the vectors.

The model card says inputs longer than 256 word pieces are truncated. To avoid
making early fields dominate, each labelled semantic-projection line is encoded
separately. Unit-normalized line vectors are averaged and normalized again to
form the record vector.

## Semantic projection

Included:

- label, definition, synonyms, category, and kind;
- canonical component labels and biological roles;
- function labels and descriptions;
- taxon labels with presence status;
- physical-property type and context.

Excluded:

- CURIEs and references;
- evidence notes, images, datasets, and curation history;
- source-specific Complex Portal compositions;
- imported organism-specific protein examples.

Those exclusions keep the map about what a structure is, rather than how much
source metadata or curation prose happens to be attached to it.

## Artifacts and gates

- `data/embeddings/structure_text_embeddings.json`: pinned vector cache.
- `data/embeddings/structure_text_map.json`: deterministic two-axis PCA data.
- `data/embeddings/structure_text_neighbors.json`: cosine-ranked neighbours.
- `pages/embedding-map.html`: interactive generated view.

`scripts/build_text_embedding_map.py --check` reconstructs the semantic text,
verifies every SHA-256 and vector invariant, derives the map and neighbours from
the cache, and compares them with the committed JSON. It performs no network or
model call and is part of the authoritative QC sequence.
