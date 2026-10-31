# Cycle 5, Stage 4 Validation Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 5, Stage 4 (`record_review`)
- **Evaluated Commit**: `a94f6deb809dd50c8344fb03284de9801c0aa298`

## Validation Commands & Receipts

| Check | Command | Exit Code | Output SHA-256 | Summary |
|---|---|---|---|---|
| Strict validation (`validate_strict.py`) | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `329bb133ea2e12c21ccc1a052d09c48f3e848ddfb3fb3b49eea6c450c113025c` | `Strict validation passed: 1008 files, 0 errors.` |
| History validation (`validate_history.py`) | `.venv/bin/python scripts/validate_history.py` | `0` | `2e78c9efe24b4f187f74b59202639b36457409bff8485a4e23924569d89058e6` | `2140 history record(s) valid against src/cellstructuremech/schema/history.yaml` |
| Pathway links (`check_pathway_links.py`) | `.venv/bin/python scripts/check_pathway_links.py` | `0` | `19688121d930c04c7ad1def60f0887d3c3afc1da1b02b8d237e4d9de925ed745` | `OK: 6 pathway links match the pinned target snapshot` |
| Trait links (`check_trait_links.py --check`) | `.venv/bin/python scripts/check_trait_links.py --check` | `0` | `21b47315ec4c70c8d8f13a59de34eff37ad3131e5e89c46c4f05dbfa5aa26a2a` | `TraitMech index: 1130 traits from https://culturebotai.github.io/TraitMech/pages/data/trait_graph.json` |
| Source queue (`check_source_queue.py`) | `.venv/bin/python scripts/check_source_queue.py` | `0` | `85a8963cd339ac333ef76fcb1a713ff52ca0fdd42f21ac824e10b5ee57942061` | `next up: ncbifam (P1, candidate, components), pride_archive (P1, candidate, datasets), swissbiopics (P1, candidate, images)` |
| Docs stats check (`check_docs.py --check`) | `.venv/bin/python scripts/check_docs.py --check` | `0` | `4a94b906cdba02e2e8ced2fcb762b685ebd3095afb4efd580ddf8ccb228da626` | `README.md corpus block is current` |
| Text embedding map (`build_text_embedding_map.py --check`) | `.venv/bin/python scripts/build_text_embedding_map.py --check` | `0` | `9a94831b901d65a2b93f9b55f603203b419c659700825ca6c5169d926a8cc92d` | `text embedding map is current: 1008 records, 384 dimensions, sentence-transformers/all-MiniLM-L6-v2` |
| Rendered pages drift check (`render_pages.py --check`) | `.venv/bin/python scripts/render_pages.py --check` | `0` | `b798d21a609b296cdc2aeb317f68fc259c4e86ee43942b4a3c5008b32b9bfa5e` | `pages/ is current` |
| Structured review bundles (`record_review.py check`) | `.venv/bin/python scripts/record_review.py check --require-reviews --base main` | `0` | `d598f6dc4cf9c36a3c0e324a4c1eb23476cd8b41a188735b7fb34a2ca64d89dc` | `319 valid structured review bundles verified (including 5 new Cycle 5 Stage 4 review bundles covering 719 records + 289 clean cohort records across all 1,008 corpus records).` |
