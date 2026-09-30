# YAML record review: radial spoke head parent fix

- **Record:** `data/structures/cytoskeleton/radial_spoke_head.yaml`
- **Identifier:** `GO:0001535`
- **PR:** #1802
- **Issue:** #1801
- **Reviewer:** codex
- **Timestamp:** 2026-09-30T00:34:55Z

## Scope

Adversarially reviewed the focused radial spoke head parent-structure fix, its
append-only history entry, and the regenerated rendered radial spoke head page.

## Checks

- Verified that the live `parent_structures` value changed from the erroneous
  `GO:0140513` nuclear protein-containing-complex term to the generic
  `GO:0032991` protein-containing complex term.
- Verified the record-level GO parent evidence now cites `GO:0032991` and no
  longer describes `GO:0140513` as a generic protein-complex parent.
- Checked that remaining `GO:0140513` mentions in the PR diff are only
  historical audit prose in the new `FIX_PARENT_STRUCTURE` curation event, the
  rendered history line, and the issue-linked history record.
- Confirmed the new history record targets
  `data/structures/cytoskeleton/radial_spoke_head.yaml` and links issue `#1801`.
- Confirmed no stale temporary mutator remains in `scripts/`, including ignored
  files.
- Confirmed the rendered `pages/structures/cytoskeleton/radial_spoke_head.html`
  page was regenerated from the corrected source YAML.
- Confirmed embeddings and corpus-level pages did not drift after the parent
  evidence correction.

## Findings

No concrete defects found.

## Local Gates

- Focused LinkML validation passed for `radial_spoke_head.yaml`.
- Focused strict validation passed for `radial_spoke_head.yaml`.
- Focused history validation passed for `history/records/radial_spoke_head`.
- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check` passed.
- `uv run python scripts/render_pages.py --check` passed.
- `uv run python scripts/check_docs.py --check` passed.
- `uv run python scripts/validate_strict.py --quiet` passed for 716 records.
- `uv run python scripts/validate_history.py` passed for 1329 history records.
- `uv run python scripts/fetch_snippets.py --verify --check` passed.
- `uv run python scripts/check_trait_links.py --check` passed.
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv` passed.
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` passed.
- `just qc` passed.
- `git diff --check` passed.
