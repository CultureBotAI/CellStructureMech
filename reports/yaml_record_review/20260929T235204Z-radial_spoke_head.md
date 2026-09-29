# YAML record review: radial spoke head

- **Record:** `data/structures/cytoskeleton/radial_spoke_head.yaml`
- **Identifier:** `GO:0001535`
- **PR:** #1800
- **Reviewer:** codex
- **Timestamp:** 2026-09-29T23:52:04Z

## Scope

Adversarially reviewed the new radial spoke head record, its append-only history
entry, and regenerated README, embedding, and page artifacts.

## Checks

- Verified the new record uses the exact GO cellular-component identifier and
  label for `GO:0001535` and keeps the GO definition and `definition_source`
  aligned.
- Compared the child-subcomplex boundary against the existing whole-radial-spoke
  `GO:0001534` record and its head, neck, and stalk component references.
- Confirmed hidden/ignored-inclusive duplicate searches find no second
  top-level radial spoke head record.
- Checked that `part_of: GO:0001534` is used for the whole radial spoke and that
  `GO:0140513` is used only as protein-complex parentage.
- Reviewed the radial-spoke-head protein constituent for unverified exact
  accessions; it is intentionally `REVIEWED_LABEL_ONLY`, and the unresolved RSP
  family and copy-number boundary is captured as an open `CURATION_TODO`.
- Checked that the Chlamydomonas distribution and canonical example stay at the
  species scope supported by the cited structural literature.
- Checked the nonmechanistic topology graph for unsupported ordered assembly,
  individual RSP assignments, or copy-number assertions; it asserts only coarse
  membership, whole-spoke parthood, and central-pair-facing orientation.
- Confirmed the repository history entry targets the new YAML path and records
  the same curation scope as the PR.
- Confirmed generated embeddings, README corpus counts, index pages, category
  pages, and the rendered structure page were regenerated from the final YAML.

## Findings

No concrete defects found.

## Local Gates

- Focused LinkML validation passed for the new YAML record.
- Focused strict validation passed for the new YAML record.
- Focused history validation passed for `history/records/radial_spoke_head`.
- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check` passed.
- `uv run python scripts/render_pages.py --check` passed.
- `uv run python scripts/check_docs.py --check` passed.
- `uv run python scripts/validate_strict.py --quiet` passed for 716 records.
- `uv run python scripts/validate_history.py` passed for 1328 history records.
- `uv run python scripts/fetch_snippets.py --verify --check` passed.
- `uv run python scripts/check_trait_links.py --check` passed.
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv` passed.
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` passed.
- `just qc` passed.
- `git diff --check` passed.
