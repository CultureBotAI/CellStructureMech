# Adversarial review: intermediate_layer_of_spindle_pole_body

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1776
- Commit reviewed: a42c030e
- Record: `data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml`
- Review timestamp: 2026-09-29T09:56:28Z

## Scope

Reviewed the new `GO:0005821` record, its repository history record,
regenerated README statistics, regenerated text embedding artifacts, and the
rendered site/index outputs added in PR #1776.

Focused checks:

- exact identity of `GO:0005821` as the intermediate layer of the spindle pole
  body
- hidden/ignored-inclusive duplicate search coverage before record creation
- `part_of: GO:0005816` for spindle-pole-body parthood
- narrow `Saccharomyces cerevisiae` taxonomic scope
- no guessed InterPro, Pfam, NCBIfam, UniProtKB, or Complex Portal component
  groundings
- use of a nonmechanistic ASSEMBLY graph for central/intermediate/outer plaque
  topology
- explicit boundary discussion separating `GO:0005821` from the central
  `GO:0005823` and outer `GO:0005824` plaque terms
- rendered page and browse/index placement under `CYTOSKELETON`
- embedding-map and README count regeneration
- focused and full schema/history validation results

## Findings

No concrete defects found.

## Notes

The graph intentionally records only topology: the intermediate layer is part
of the SPB and positioned between the central and outer plaques. It does not
try to infer an ordered assembly path or exact molecular component boundary.

The component boundary remains intentionally unresolved. The new
`resolve_intermediate_layer_components` `CURATION_TODO` tracks exact
source-neutral family grounding work for SPB intermediate-layer constituents
rather than guessing accessions in the first GO-backed record.

## Local gates observed

- `just text-map-check`
- `just render-check`
- `just docs-check`
- `just validate data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml`
- `just validate-strict data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml`
- `just validate-history history/records/intermediate_layer_of_spindle_pole_body`
- `just validate-strict`
- `just validate-history`
- `uv run python scripts/fetch_snippets.py --verify --check`
- `uv run python scripts/check_trait_links.py --check`
- `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `just qc`
- `git diff --check`
