# Adversarial YAML Record Review: GO:1990334

- PR: #1796
- Commit: bf6aa5f4d127d854e63d25a26877d7e57b77595c
- Record: `data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml`
- Reviewed: 2026-09-29T21:07:29Z

## Findings

No concrete defects found.

## Checks

- Verified with ignored and hidden files included that no exact
  `GO:1990334`, `SIN/MEN two-component GAP complex`, `Bfa1-Bub2 complex`, or
  `Byr4-Cdc16 GAP complex` record already exists in `data/structures`.
- Verified that `GO:1990334` is a current, unrestricted Gene Ontology cellular
  component term with `SIN/MEN two-component GAP complex` as the current
  QuickGO preferred label and the Bfa1-Bub2 and Byr4-Cdc16 complex names as
  narrow synonyms.
- Verified that the targeted `GO:1990334` id/label exception documents a
  current QuickGO-vs-OAK snapshot label drift, where OAK still reports the
  older `Bfa1-Bub2 complex` label for the same GO term.
- Verified that the record uses only the GO-asserted `GO:1902773`
  GTPase-activator parent and `GO:0005816` spindle-pole-body parthood.
- Verified that the Saccharomyces cerevisiae taxonomic-distribution and
  canonical-example rows are grounded in DOI:10.1083/jcb.200507162 and that no
  unsupported broader fungal distribution is asserted.
- Verified that no unverified Bfa1, Bub2, Byr4, or Cdc16 component grounding was
  guessed; exact source-neutral family grounding is deferred in an OPEN
  `CURATION_TODO`.
- Verified that rendered pages are current after PR creation and include the
  new cytoskeleton structure page and GO-grounded index row.

## Issues Filed

None.

## Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml`
- `uv run python scripts/validate_history.py history/records/sin_men_two_component_gap_complex/2026-09-29T204726Z-codex-14256d.yaml`
- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `just qc`
- `git diff --check`
