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

The shared `scripts/embedding_pipeline.py` will be installed from CLAW governance;
it is not copied from another Mech. Once installed, the planned commands are:

```bash
just text-map-inputs --output build/text-map/inputs.jsonl
uv run python scripts/embedding_pipeline.py inspect --input build/text-map/inputs.jsonl
uv run --extra embeddings python scripts/embedding_pipeline.py embed --input build/text-map/inputs.jsonl --cache build/text-map/vectors.sqlite --profile-output build/text-map/profile.json
uv run --extra embeddings python scripts/embedding_pipeline.py project --input build/text-map/inputs.jsonl --cache build/text-map/vectors.sqlite --profile build/text-map/profile.json --output data/text_map --title "Cell structure semantic text map"
uv run python scripts/embedding_pipeline.py check --output data/text_map --input build/text-map/inputs.jsonl
```

The common dependency extra must first be synchronized with the shared runtime;
the current legacy embeddings extra alone does not provide PaCMAP. No map is
claimed ready until the bundle is generated, validated against fresh full
inputs and enabled for publication. The renderer will stage its validated
current bundle at `pages/text-map/` and link it as a distinct semantic map,
while preserving the existing MiniLM view.


## Validated site publication

`conf/text_map.yaml` explicitly starts with `enabled: false`; no common map or
navigation link is claimed ready yet. After generating and reviewing the full
input-bound bundle under `data/text_map/`, set `enabled: true` and run `just render`.
The shared CLAW runtime must first be installed at `scripts/embedding_pipeline.py`.

When enabled, rendering exports fresh **full-corpus** JSONL and validates the
current pointer, artifact checksums, input coverage and pinned common BGE profile.
The runtime atomically stages the current bundle's `index.html`, `points.json`
and `manifest.json` at `pages/text-map/`. Only successful staging enables the
navigation link. Missing runtime/current pointer, stale inputs or invalid
checksums fail the build; they never silently hide an enabled map. The existing
published pages are retained if this preflight fails.

`just render --check` uses the same validation and staging inside its temporary
site. Ordinary checks do not download weights, encode text or fit PaCMAP.
The initial disabled setting is temporary rollout state, not a resolution of
the missing-map issue. Canaries must not be enabled as full-corpus publication.

Site staging binds the exact immutable bundle approved during preflight. If the
current pointer changes before staging, rendering fails instead of publishing a
different generation under the earlier encoder-policy approval (CLAW #429).
