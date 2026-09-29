# Adversarial YAML Record Review: GO:0160067

- PR: #1795
- Commit: b0969e6c23dc9157b56bf3cbaafc84e9f963de87
- Record: `data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml`
- Reviewed: 2026-09-29T20:26:42Z

## Findings

No concrete defects found.

## Checks

- Verified with ignored and hidden files included that no exact
  `GO:0160067`, `new spindle pole body SIN signaling complex`, or
  `new spindle pole body SIN signalling complex` record already exists in
  `data/structures`.
- Verified that `GO:0160067` is a current, unrestricted Gene Ontology cellular
  component term with `new spindle pole body SIN signaling complex` as its
  preferred label, `new spindle pole body SIN signalling complex` as its exact
  synonym, `GO:0160065` as its is-a parent, and a fungal taxon constraint.
- Verified that the new record keeps `GO:0160067` narrower than the broad
  `GO:0160065` SIN/MEN signaling complex and distinct from the sibling
  `GO:0160066` interphase SIN signaling complex and `GO:1990334` SIN/MEN
  two-component GAP complex.
- Verified that `GO:0071958` is cited only as the new mitotic spindle pole
  body named by the GO:0160067 definition, with no asserted `part_of` edge
  where GO only states association with that SPB.
- Verified that no ungrounded fission-yeast protein names were promoted to
  `components`; exact source-neutral family grounding is deferred in an OPEN
  `CURATION_TODO`.
- Verified that the new history record targets the new YAML path and records
  the same curated sections present in the record.
- Verified that rendered pages are current after PR creation and include the
  new cytoskeleton structure page and GO-grounded index row.

## Issues Filed

None.

## Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml`
- `uv run python scripts/validate_history.py history/records/new_spindle_pole_body_sin_signaling_complex/2026-09-29T201037Z-codex-6814bd.yaml`
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
