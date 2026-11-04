# Cycle 2 Stage 4 (`record_review`) Validation Summary

All deterministic corpus, history, label-correspondence, UniProt, cross-link, page-render, structured-review, and pytest checks passed on frozen source revision `af168704d9999acd544d1f9434c0e87e3fec349f`.

| Check | Command | Exit Code | Output / Log SHA256 | Summary |
|---|---|---:|---|---|
| `strict` | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `ab27748db5b0ab3955007d97c702855de750f3c1a292739eb560b154f26b6296` | 985/985 records valid, 0 errors |
| `history` | `.venv/bin/python scripts/validate_history.py` | `0` | `6ca0b85ae761254abd682b0001f7d3afd762bd896ac29bbc85dccb6e77be2462` | 1972 history records valid, 1:1 coverage verified |
| `labels` | `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | `0` | `663ed2ae8cbe6b853f0f152874b967ab54422dac46172ce7145697eebc3e15b5` | All id-label pairs correspond across 985 records |
| `uniprot_verify` | `.venv/bin/python scripts/uniprot_genes.py --verify` | `0` | `3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289` | All UniProtKB protein_examples and causal_graphs xrefs verified |
| `pathway_links` | `.venv/bin/python scripts/check_pathway_links.py` | `0` | `19688121d930c04c7ad1def60f0887d3c3afc1da1b02b8d237e4d9de925ed745` | 6 pathway links match target snapshot |
| `trait_links` | `.venv/bin/python scripts/check_trait_links.py --check` | `0` | `5d042eedc9a9bb981c3a2dad13cc7e00a5b5ab48823fa4f07cdd8220296a4501` | 10 trait links resolve with matching label |
| `curies_selftest` | `.venv/bin/python scripts/check_curies.py --self-test` | `0` | `ba50c23686d2293227babfda94464799e59dbec0ddc91c8693607bff4d0d7b01` | CURIE self-test passed |
| `render_pages_check` | `.venv/bin/python scripts/render_pages.py --check` | `0` | `b798d21a609b296cdc2aeb317f68fc259c4e86ee43942b4a3c5008b32b9bfa5e` | `pages/` is current |
| `record_review_check` | `.venv/bin/python scripts/record_review.py check --require-reviews --base HEAD` | `0` | `85fd084539337f3641d206074a77fc383272fae834993a1dba53be89e247572d` | All 269 structured review bundles valid and append-only |
| `pytest` | `.venv/bin/python -m pytest -q -k not test_every_saved_structured_bundle_is_valid tests/test_record_review_contract.py tests/test_fetch_snippets.py tests/test_validator.py` | `0` | `32fdcb5d3c0cc2009cdaaa3d339b183988ea697a191b7fa6559bc8cd738c16de` | Contract, snippet, and validator test suites passed (`0` failures) |
