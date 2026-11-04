# Cycle 1 Stage 4 (`record_review`) Validation Summary

All deterministic corpus, history, label-correspondence, UniProt, cross-link, page-render, structured-review, and pytest checks passed on frozen source revision `13c6b0d85338aa96d330b8d699587dfe270a21f9`.

| Check | Command | Exit Code | Output / Log SHA256 | Summary |
|---|---|---:|---|---|
| `strict` | `.venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv` | `0` | `b34bdc4f99ef4601161958120b45622535017214ba594a44bca249237869d704` | 978/978 records valid, 0 errors |
| `history` | `.venv/bin/python scripts/validate_history.py` | `0` | `58cd0a9db943ec58f980604094a2207f5c3d0da48b8cafbd4389e4e771cea1be` | 1903 history records valid |
| `labels` | `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | `0` | `b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e` | All id-label pairs correspond |
| `uniprot_verify` | `.venv/bin/python scripts/uniprot_genes.py --verify` | `0` | `3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289` | All UniProtKB protein_examples verified |
| `pathway_links` | `.venv/bin/python scripts/check_pathway_links.py` | `0` | `19688121d930c04c7ad1def60f0887d3c3afc1da1b02b8d237e4d9de925ed745` | 6 pathway links match target snapshot |
| `trait_links` | `.venv/bin/python scripts/check_trait_links.py --check` | `0` | `5d042eedc9a9bb981c3a2dad13cc7e00a5b5ab48823fa4f07cdd8220296a4501` | 10 trait links resolve with matching label |
| `curies_selftest` | `.venv/bin/python scripts/check_curies.py --self-test` | `0` | `ba50c23686d2293227babfda94464799e59dbec0ddc91c8693607bff4d0d7b01` | CURIE self-test passed |
| `render_pages_check` | `.venv/bin/python scripts/render_pages.py --check` | `0` | `b798d21a609b296cdc2aeb317f68fc259c4e86ee43942b4a3c5008b32b9bfa5e` | `pages/` is current |
| `record_review_check` | `.venv/bin/python scripts/record_review.py check --require-reviews --base HEAD` | `0` | `b3678b607378a0a58507564d8ea70082610c1051e9cee2056113dd54ecbcbb89` | All 262 structured review bundles valid and append-only |
| `pytest` | `.venv/bin/python -m pytest -q` | `0` | `57e2cec7616c46a7224caaf5814882cd476363e9b26485009acc14355a6f80eb` | 1053 passed, 3 skipped |
