# Common semantic text map

The existing `embedding-map.html` remains the pinned MiniLM/PCA view with cosine
neighbors. The common fleet view uses independently computed BGE 1,024D vectors
and PaCMAP. Shared biological text does not make the encoder spaces compatible;
the legacy 384D vectors must never be inserted into the BGE cache.

`just text-map-inputs` validates a full-corpus preview without model inference.
`just text-map-inputs --output build/text-map/inputs.jsonl` exports the exact
versioned fleet JSONL contract. `--limit 32` or repeated `--record` selects a
canary, explicitly labelled `subset` in the printed receipt. A subset is not
full map coverage. JSONL is published atomically after all selected inputs pass.

The biological projection is factored into `src/cellstructuremech/semantic_text.py`
and remains identical to the existing legacy builder's text. It includes
label, definition, category/kind, synonyms, components/roles, functions,
taxonomic scope and physical-property context, excluding citations, provenance,
images and imported protein examples. The adapter has its own
`cellstructuremech-semantic-v1` version, and links follow the source YAML path.

The installed CLAW runtime is `scripts/embedding_pipeline.py`; its separate
locked environment and exact build commands are in the [maintained runtime guide](../conf/embedding-runtime/README.md).
Normal rendering and verification do not install that model environment or run
inference. When record membership or selected semantic fields change, export
fresh full inputs, reuse the existing profile-bound vector cache to encode only
new or changed text, regenerate PaCMAP, and validate the complete bundle before
rendering. A stale bundle must be refreshed before publishing curated changes.

## Validated site publication

`conf/text_map.yaml` is enabled. The selected common bundle is recorded by
`data/text_map/current.json`; its `manifest.json` reports the input identity and
coverage counts. Rendering verifies freshness against the current corpus and
refuses a stale bundle until the cache-backed refresh is complete. The existing
MiniLM/PCA view remains distinct.

Rendering exports fresh **full-corpus** JSONL and validates the current pointer,
artifact checksums, complete input identity and pinned common BGE profile. The
runtime stages the selected `index.html`, `points.json` and `manifest.json` at
`pages/text-map/`; the site links to that view after successful staging. Missing
runtime or current pointer, stale inputs and invalid checksums fail an enabled
build. A failed preflight preserves the existing published pages.

`just render-check` uses the same validation and staging inside a temporary site.
These checks do not download weights, encode text or fit PaCMAP. A canary cannot
satisfy the full-corpus publication check.

Staging binds the exact immutable generation approved during preflight. A changed
current pointer or substituted generation fails validation before publication
(CLAW #429).
