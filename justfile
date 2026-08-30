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
# `just new-record --category APPENDAGE --identifier GO:0009288 --label "bacterial-type flagellum" --apply`
new-record *args:
    uv run python scripts/new_record.py {{args}}

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
