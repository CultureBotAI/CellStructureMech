# Adversarial YAML Record Review: GO:0110085

- PR: #1798
- Commit: aa4b9e8baa4aeb5a7e1ddf28cb21554fc1679c94
- Record: `data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml`
- Reviewed: 2026-09-29T22:33:41Z

## Findings

No concrete defects found.

## Checks

- Verified with ignored and hidden files included that no exact `GO:0110085`,
  `mitotic actomyosin contractile ring`, `mitotic contractile ring`,
  `PMID:27505246`, or `DOI:10.1016/j.cub.2016.06.071` record existed before
  this PR.
- Verified that `GO:0110085` is a current, unrestricted Gene Ontology cellular
  component with the preferred label `mitotic actomyosin contractile ring` and a
  definition/source payload matching the new record.
- Verified that the record uses `GO:0005826` only as the broader actomyosin-ring
  parent and keeps the narrower `GO:0000142` bud-neck contractile ring record
  separate.
- Verified that the record documents `GO:0110086` as the meiotic sibling class,
  rather than collapsing the mitotic and meiotic actomyosin-ring classes.
- Verified that the Schizosaccharomyces pombe distribution and canonical
  example are grounded only at species level in DOI:10.1083/jcb.200602032 and
  that no broader fungal distribution is asserted.
- Verified that the actin and myosin component rows use
  `REVIEWED_LABEL_ONLY` groundings and that no unverified InterPro, Pfam,
  NCBIfam, UniProtKB, or Complex Portal identifiers were guessed.
- Verified that the OPEN component-boundary TODO explicitly defers exact
  source-neutral actin/myosin groundings and myosin-associated accessory
  boundaries instead of modeling unreviewed fission-yeast node factors.
- Verified that rendered pages are current after PR creation and include the
  new cytoskeleton structure page, grounded index row, category row, and
  search index entry.

## Issues Filed

None.

## Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml`
- `uv run python scripts/validate_history.py history/records/mitotic_actomyosin_contractile_ring`
- `uv run --extra embeddings python scripts/build_text_embedding_map.py --refresh`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py`
- `uv run python scripts/check_docs.py --write`
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
