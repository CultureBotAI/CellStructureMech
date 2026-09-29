# YAML record review: meiotic actomyosin contractile ring

- **Record:** `data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml`
- **Identifier:** `GO:0110086`
- **PR:** #1799
- **Reviewer:** codex
- **Timestamp:** 2026-09-29T23:10:19Z

## Scope

Adversarially reviewed the new meiotic actomyosin contractile ring record, its
append-only history entry, and regenerated README, embedding, and page artifacts.

## Checks

- Verified the new record uses the exact GO cellular-component identifier and
  label for `GO:0110086` and keeps the GO definition and `definition_source`
  aligned.
- Compared the parent and subtype boundary against the existing
  `GO:0005826` actomyosin contractile ring, `GO:0110085` mitotic actomyosin
  contractile ring, and `GO:0032157` prospore contractile ring records.
- Confirmed hidden/ignored-inclusive duplicate searches find the new
  `GO:0110086` record plus intentional sibling/child references, not a second
  exact meiotic actomyosin ring record.
- Reviewed the broad actin and myosin components for unverified accessions or
  guessed exact families; both are intentionally `REVIEWED_LABEL_ONLY`, and the
  unresolved accessory-protein boundary is captured as an open
  `CURATION_TODO`.
- Checked that the fission-yeast distribution, canonical example, and meiotic
  cytokinesis function are narrower than the GO term and tied to
  `DOI:10.1242/jcs.091561`.
- Checked the nonmechanistic topology graph for unsupported ordered assembly or
  species-specific accessory-factor assertions; it asserts only GO-backed actin
  and myosin membership.
- Confirmed the repository history entry targets the new YAML path and records
  the same curation scope as the PR.
- Confirmed generated embeddings, README corpus counts, index pages, category
  pages, and the rendered structure page were regenerated from the final YAML.

## Findings

No concrete defects found.

## Local Gates

- Focused LinkML validation passed for the new YAML record.
- Focused strict validation passed for the new YAML record.
- Focused history validation passed for `history/records/meiotic_actomyosin_contractile_ring`.
- `uv run --extra embeddings python scripts/build_text_embedding_map.py --check` passed.
- `uv run python scripts/render_pages.py --check` passed.
- `uv run python scripts/check_docs.py --check` passed.
- `uv run python scripts/validate_strict.py --quiet` passed for 715 records.
- `uv run python scripts/validate_history.py` passed for 1327 history records.
- `uv run python scripts/fetch_snippets.py --verify --check` passed.
- `uv run python scripts/check_trait_links.py --check` passed.
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv` passed.
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` passed.
- `just qc` passed.
- `git diff --check` passed.
