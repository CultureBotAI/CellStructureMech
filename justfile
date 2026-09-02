# CellStructureMech — microbial cell structure knowledge base

set positional-arguments := true

schema := "src/cellstructuremech/schema/cellstructuremech.yaml"
structures := "data/structures"

default:
    @just --list --unsorted

# Install package + dev tools
install:
    uv sync --extra dev

# Generate Pydantic classes from the LinkML schema
gen-schema:
    uv run gen-pydantic {{schema}} > src/cellstructuremech/schema/cellstructuremech_dataclasses.py

# Scaffold a new record (writes through the validation gate). Dry-run by default.
# `just new-record --category APPENDAGE --kind APPENDAGE --identifier GO:0009288 --label "bacterial-type flagellum" --definition "..." --definition-source GO:0009288 --apply`
new-record *args:
    uv run python scripts/new_record.py {{args}}

# One-shot, validated expansion from four seed records to ten. Dry-run by default.
seed-foundational-structures *args:
    uv run python scripts/seed_foundational_structures.py {{args}}

# Validate a single record YAML against the schema (open mode, quick check)
validate file:
    uv run linkml-validate -s {{schema}} --target-class CellStructureRecord {{file}}

# Validate every record. Delegates to validate-strict (closed mode: unknown
# fields are errors, not silently accepted as they are in linkml-validate's
# default open mode).
validate-all *args:
    @just validate-strict {{args}}

# Strict in-process validation in closed mode. Emits
# reports/instance_validation_failures.tsv and exits 1 on any ERROR.
validate-strict *args:
    uv run python scripts/validate_strict.py {{args}}

# Render the browsable site under pages/ from the corpus. Committed; `--check`
# fails when it has gone stale.
render *args:
    uv run python scripts/render_pages.py {{args}}

# Fail if pages/ is out of step with the corpus
render-check:
    uv run python scripts/render_pages.py --check

# Corpus report: records per category and status, grounding coverage,
# components / graphs / traits per record.
report *args:
    uv run python scripts/corpus_report.py {{args}}

# Refresh the generated current-corpus block in README.md.
docs-stats:
    uv run python scripts/check_docs.py --write

# Fail if README.md's current-corpus block is out of step with the corpus.
docs-check:
    uv run python scripts/check_docs.py --check

# Run the test suite
test *args:
    uv run pytest {{args}}

# Deep research for one structure. Dry-run by default; pass --apply for one
# real canary after `just deep-research-canary <provider>`.
research-cell-structure provider target *args="":
    uv run python scripts/research_cell_structure.py \
      --provider {{provider}} --target {{target}} {{args}}

research-entity provider target *args="":
    @just research-cell-structure {{provider}} {{target}} {{args}}

# Non-billing configuration/capability checks.
deep-research-canary provider="all" *args="":
    uv run python scripts/deep_research_contract.py {{provider}} \
      --client-command "uvx --python 3.12 --prerelease=allow --from deep-research-client[cyberian] deep-research-client" \
      {{args}}

# Lint
lint *args:
    uv run ruff check {{args}} .

# Auto-fix lint findings
lint-fix:
    uv run ruff check --fix .

# The prioritized data-source queue: what to adopt next, and what is still
# unverified about it. `.claude/skills/source-queue` triages it.
source-queue:
    uv run python scripts/check_source_queue.py

# The authoritative quality gate used both locally and in CI.
qc:
    uv run python scripts/run_qc.py

# UniProt Subcellular Location (source queue #3): add SL xrefs to GO-grounded records
uniprot-xrefs *args:
    uv run python scripts/uniprot_sl.py xrefs {{args}}

# Seed taxon-paired protein examples for ONE record from UniProt SL (dry-run by default).
# `just uniprot-proteins data/structures/microcompartment/carboxysome.yaml --taxon 1140 --apply`
uniprot-proteins record *args:
    uv run python scripts/uniprot_sl.py proteins --record {{record}} {{args}}

# --- claw-governed: curation history, vendored sync, id-label gate ---

# Scaffold a repository-level history record (history/<kind>/<slug>/...). See
# history/README.md. "$@" not {{args}} — see `set positional-arguments`.
new-history *args:
    uv run python scripts/new_history_record.py "$@"

# Validate one history record, or a directory of them, against the VENDORED
# schema — works with no claw checkout, same as CI.
validate-history target="history":
    uv run python scripts/validate_history.py {{target}}

# Verify every claw-governed vendored file matches canon at scripts/.vendored_canon_ref (network).
vendored-check:
    bash scripts/check_vendored_sync.sh

# id<->label correspondence gate (vendored): every (grounding, label) pair in the
# records must match the ontology via OAK. Blocking in CI; downloads OAK sqlite
# ontologies on first run. Curator-accepted residuals live in conf/id_label_targets.yaml.
validate-products:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

# Same check, written to reports/label_drift.tsv without failing (CI triage artifact).
report-label-drift:
    uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml --report reports/label_drift.tsv || true

# Add a Wikimedia Commons image to a record, reading licence, attribution and
# taxon from the Commons/Wikidata APIs and verifying the file hash. Dry-run by
# default. `just commons-image --title "File:X.jpg" --record data/... --modality TEM --apply`
commons-image *args:
    uv run python scripts/fetch_commons_image.py "$@"

# Taxon-specific Complex Portal composition; exact CPX accession and dry-run by default.
complex-composition *args:
    uv run python scripts/complex_portal.py "$@"

# Linked EMPIAR dataset + EMDB representative image, or keyword coverage.
emdb-empiar *args:
    uv run python scripts/emdb_empiar.py "$@"

# Current-version PMC OA S3 figure ingest, or figure-level coverage.
pmc-image *args:
    uv run python scripts/pmc_oa.py "$@"

# Per-item CIL JSON-LD ingest; exact Public Domain/CC BY terms and dry-run by default.
cell-image-library *args:
    uv run python scripts/cell_image_library.py "$@"

# Direct S-BIAD dataset + exact file/channel ingest; per-study terms and dry-run by default.
bioimage-archive *args:
    uv run python scripts/bioimage_archive.py "$@"

# Curator-reviewed identity xrefs only; the inactive ontology is never label-searched.
micro-xrefs *args:
    uv run python scripts/micro_xrefs.py "$@"

# Fixed, curate-only B. subtilis flagellar examples; identifiers/links only.
subtiwiki *args:
    uv run python scripts/subtiwiki.py "$@"

# Refresh with the pinned local sentence-transformers model (no corpus text is
# transmitted), then rebuild the 2D PCA map and cosine-neighbour index.
text-embeddings-refresh:
    uv run --extra embeddings python scripts/build_text_embedding_map.py --refresh

# Rebuild derived map files from the committed vectors without network access.
text-map:
    uv run python scripts/build_text_embedding_map.py

# Fail when record text, cached vectors, map coordinates, or neighbours drift.
text-map-check:
    uv run python scripts/build_text_embedding_map.py --check

# Resolve every identifier in the corpus at its issuing authority (#6). Network;
# cached under build/curie_cache.json, so a re-run is nearly free. The resolvers
# are exercised against a known-good and known-bad id first, so a broken
# resolver fails loudly instead of condemning the corpus.
check-curies *args:
    uv run python scripts/check_curies.py {{args}}

# Fail if any identifier does not resolve. Blocking gate in CI.
check-curies-strict:
    uv run python scripts/check_curies.py --check --report reports/curie_check.tsv

# Only exercise the resolvers; says nothing about the corpus.
check-curies-self-test:
    uv run python scripts/check_curies.py --self-test

# Check every associated_traits link against TraitMech: the id must exist there
# and the label must still match (#11). Uses a local checkout when
# TRAITMECH_ROOT or conf/sources.yaml points at one, else TraitMech's published
# trait index. Network unless a checkout is present.
check-trait-links *args:
    uv run python scripts/check_trait_links.py {{args}}
