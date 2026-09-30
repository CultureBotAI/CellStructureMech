# Adversarial review: mitotic septin complex

## Scope

- PR: #1835
- Record: `data/structures/cytoskeleton/mitotic_septin_complex.yaml`
- History: `history/records/mitotic_septin_complex/2026-09-30T174403Z-codex-6f6a32.yaml`

## Checks

- Re-read the GO:0032151 YAML and compared it to the broader `GO:0031105` septin complex record.
- Confirmed the PR file list contains only the new record, one history entry, one generated structure page, and regenerated README/site/embedding artifacts.
- Re-ran a hidden/ignored-inclusive search for `GO:0032151`, `GO_0032151`, `mitotic septin complex`, and `mitotic_septin_complex` across `data/structures`, `history`, `pages`, `reports`, and `README.md`.
- Checked that `parent_structures` uses the existing GO:0031105 septin-complex parent and does not point to higher-order septin-ring or septin-cytoskeleton records directly.
- Checked that the record stays generic to GO:0032151 and does not import the fission-yeast taxonomic distribution and canonical examples from the broader septin-complex record.
- Checked that no exact InterPro, Pfam, NCBIfam, or UniProt component groundings were guessed for the unresolved mitotic septin cohort.
- Re-ran `just qc`; it passed on 739 structure records.

## Findings

No defects found.

## Non-findings

- The record models GO:0032151 as the mitotic child of GO:0031105, not as a duplicate of the parent septin-complex class.
- The GO:0032152 meiotic septin complex is referenced only as a boundary comparator and is not collapsed into the mitotic record.
- The causal graph is limited to heterooligomeric complex formation and does not assert a fixed subunit stoichiometry, species-specific paralog set, or higher-order septin-ring polymerization.
- The function text only restates the GO definition's "acts during mitotic cell division" context and does not invent an exact mitotic-process CURIE.

## Validation

- `uv run linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/mitotic_septin_complex.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/mitotic_septin_complex.yaml`
- `uv run python scripts/validate_history.py history/records/mitotic_septin_complex`
- `uv run python scripts/validate_strict.py --quiet`
- `uv run python scripts/validate_history.py`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `just qc`
- `git diff --check`
