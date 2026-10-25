# Cycle 3, Stage 4 Validation Report (`record_review`)

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage**: Cycle 3, Stage 4 (`record_review`)
- **Evaluated Commit**: `83ec9d5184fb203d87d8c3bd7043792d385193bf`

## Validation Commands & Receipts

| Check | Command | Exit Code | Output SHA-256 | Summary |
|---|---|---|---|---|
| Strict validation (`validate_strict.py`) | `.venv/bin/python scripts/validate_strict.py` | `0` | `fc80872aed828ea24abbaf1ff66194605d09857b0bf0773189fc076d223594eb` | `Strict validation passed: 993 files.` |
| History validation (`validate_history.py`) | `.venv/bin/python scripts/validate_history.py` | `0` | `892f19c663d77d1f9857317328cf487684f291fbe34c6f7028e7e68585bed536` | `History validation passed: 993 files, 0 issues.` |
| Ontology ID-label correspondence (`check_id_label_correspondence.py`) | `.venv/bin/python scripts/check_id_label_correspondence.py` | `0` | `4bb207ccdd3216a741b1ca17643c1b57a2f2c68af02138decedfcd4fd19c8b3a` | `Checked 993 records across 7 ontology label prefixes; 0 errors, 0 unverified.` |
| UniProt protein examples (`uniprot_genes.py`) | `.venv/bin/python scripts/uniprot_genes.py --verify --check-examples` | `0` | `3cc17ed57cc5a954a982905916d4f0f66d781e2f4b51f2f7c77ada16c835d289` | `UniProt verification passed: 993 files, 2005 gene symbols, 4399 protein examples, 0 issues.` |
| Pathway links (`validate_pathway_links.py`) | `.venv/bin/python scripts/validate_pathway_links.py` | `0` | `19688121d930c04c7ad1def60f0887d3c3afc1da1b02b8d237e4d9de925ed745` | `Pathway link validation passed: 0 issues across 993 files.` |
| Trait links (`validate_trait_links.py`) | `.venv/bin/python scripts/validate_trait_links.py` | `0` | `5d042eedc9a9bb981c3a2dad13cc7e00a5b5ab48823fa4f07cdd8220296a4501` | `Trait link validation passed: 0 issues across 993 files.` |
| CURIE prefix self-test (`curies.py --selftest`) | `.venv/bin/python scripts/curies.py --selftest` | `0` | `ba50c23686d2293227babfda94464799e59dbec0ddc91c8693607bff4d0d7b01` | `curies self-test passed (40 prefix rules)` |
| Rendered pages drift check (`render_pages.py --check`) | `.venv/bin/python scripts/render_pages.py --check` | `0` | `b798d21a609b296cdc2aeb317f68fc259c4e86ee43942b4a3c5008b32b9bfa5e` | `Pages check passed: 993 structures.` |
| Structured review bundles (`record_review.py check`) | `.venv/bin/python scripts/record_review.py check --require-reviews --base HEAD` | `0` | `0abee4cd9d8f9b544170c6d78f2c9cbbe2e226580ca2dade95657dc5070158fb` | `293 valid structured review bundles verified (including 13 new Cycle 3 Stage 4 review bundles covering all 993 corpus records).` |
| Unit & corpus integrity test suite (`pytest`) | `.venv/bin/pytest` | `0` | `4e3ba24343b7776ffa69226195d3c38406d733390ba9409549aebf58c92c3a3f` | `204 passed in 88.62s (0:01:28)` |
