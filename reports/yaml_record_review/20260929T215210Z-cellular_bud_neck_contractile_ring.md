# Adversarial YAML Record Review: GO:0000142

- PR: #1797
- Commit: ea13a5622eb38b10e2d7e9da76d07975e8689759
- Record: `data/structures/cytoskeleton/cellular_bud_neck_contractile_ring.yaml`
- Reviewed: 2026-09-29T21:52:10Z

## Findings

No concrete defects found.

## Checks

- Verified with ignored and hidden files included that no exact `GO:0000142`,
  `cellular bud neck contractile ring`, `neck ring`,
  DOI:10.1083/jcb.142.5.1301, or PMID:9732290 record existed before this PR.
- Verified that `GO:0000142` is a current, unrestricted Gene Ontology cellular
  component with the preferred label `cellular bud neck contractile ring`, the
  exact synonym `neck ring`, and definition/source payload matching the new
  record.
- Verified that the broader `GO:0110085` `mitotic actomyosin contractile ring`
  relation and the `GO:0005935` cellular-bud-neck placement are represented as
  parentage and parthood instead of being collapsed into the exact record
  identifier.
- Verified that the record stays distinct from the generic `GO:0005826`
  `actomyosin contractile ring` record and the bud-neck septin-ring and
  septin-collar records.
- Verified that the Saccharomyces cerevisiae distribution and canonical example
  are grounded only at species level in DOI:10.1083/jcb.142.5.1301 and that no
  broader fungal distribution is asserted.
- Verified that the actin and Myo1 component rows use
  `REVIEWED_LABEL_ONLY` groundings and that no unverified InterPro, Pfam,
  NCBIfam, UniProtKB, or Complex Portal identifiers were guessed.
- Verified that rendered pages are current after PR creation and include the
  new cytoskeleton structure page, grounded index row, category row, and
  search index entry.

## Issues Filed

None.

## Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/cellular_bud_neck_contractile_ring.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/cellular_bud_neck_contractile_ring.yaml`
- `uv run python scripts/validate_history.py history/records/cellular_bud_neck_contractile_ring/2026-09-29T213316Z-codex-c2ac04.yaml`
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
