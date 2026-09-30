# YAML Record Review: intraciliary_transport_particle

- PR: #1806
- Branch: add-intraciliary-transport-particle
- Commit reviewed: 37e1810d3de470b203a9b179cd6caf9ddbb141f5
- Record: `data/structures/appendage/intraciliary_transport_particle.yaml`
- Identifier: `GO:0030990`
- Review timestamp: 2026-09-30T03:27:19Z

## Findings

No concrete defects found.

## Adversarial Checks

- Duplicate search: searched `data/structures` with `rg --no-ignore --hidden` for `GO:0030990`, `intraciliary transport particle`, `intraflagellar transport particle`, and `IFT particle`, so ignored and hidden files were included.
- Duplicate judgment: the existing `cilium.yaml` record already references `GO:0030990` as associated IFT machinery, but no pre-existing top-level record owned `identifier: GO:0030990`, `label: intraciliary transport particle`, or `synonym_text: intraflagellar transport particle`.
- Scope: the record keeps the IFT particle distinct from the containing cilium, the axoneme track, and IFT motor complexes.
- Grounding: the GO cellular-component identifier exactly denotes the curated complex, broad GO structures are used only for hierarchy or evidence context, and the IFT protein cohort is intentionally `REVIEWED_LABEL_ONLY` with an open `CURATION_TODO` instead of guessed InterPro, Pfam, NCBIfam, UniProtKB, or motor-complex identifiers.
- Evidence: the non-GO claims are limited to the DOI-backed Chlamydomonas IFT model and coarse cargo-transport role.
- Rendering: the generated structure page reflects the new record, and shared rendered indexes include the new APPENDAGE entry.
- History: the append-only history entry targets the new record path and summarizes the creation event.

## Validation Reviewed

- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/appendage/intraciliary_transport_particle.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/appendage/intraciliary_transport_particle.yaml`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py history/records/intraciliary_transport_particle`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `git diff --check`
- `just qc`

No review issues were filed.
