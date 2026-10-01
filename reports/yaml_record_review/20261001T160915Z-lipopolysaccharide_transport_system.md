# YAML Record Review: lipopolysaccharide transport system

- PR: #1877
- Record: `data/structures/other/lipopolysaccharide_transport_system.yaml`
- Identifier: `GO:0062051`
- Reviewed at: `2026-10-01T16:09:15Z`
- Reviewer: `codex`
- Result: no concrete defects found; no GitHub issues filed

## Scope Reviewed

- Verified the PR diff contains one new `GO:0062051` record, one append-only
  history record, one rendered structure page, and deterministic
  README/embedding/index updates.
- Rechecked the hidden/ignored-inclusive duplicate search results for the GO
  CURIE, exact label, Lpt naming, and primary DOI/PMID strings; no pre-existing
  record or history entry conflicts with the new Lpt record.
- Reviewed the emitted YAML and rendered
  `pages/structures/other/lipopolysaccharide_transport_system.html` for broken
  discussion anchors, missing evidence, and display of reviewed-label-only Lpt
  components.
- Cross-checked every new DOI, `GO:0062051`, and `GO:1990351` in
  `reports/curie_check.tsv`; all resolve at their issuing authorities.

## Adversarial Findings

No issue-grade defects found.

The main boundary risk is MsbA: the record correctly keeps MsbA out of the
LptA-G transport system because MsbA flips nascent LPS across the inner
membrane before Lpt-mediated extraction and periplasmic transport. The second
modelling risk is over-grounding individual Lpt components: the record leaves
LptA, LptB, LptC, LptD, LptE, LptF, and LptG as `REVIEWED_LABEL_ONLY` with an
open `CURATION_TODO` rather than mapping them to broad ABC-transporter,
beta-jellyroll, beta-barrel, or lipoprotein families.

## Local Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/lipopolysaccharide_transport_system.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/lipopolysaccharide_transport_system.yaml`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py history/records/lipopolysaccharide_transport_system/2026-10-01T155518Z-codex-f94cac.yaml`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `uv run pytest tests/test_corpus_integrity.py::test_discussion_anchors_resolve`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `uv run python scripts/run_qc.py`
- `git diff --check`
