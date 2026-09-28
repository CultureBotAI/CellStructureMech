# YAML Record Review: cellular bud neck septin collar

- Repository: CultureBotAI/CellStructureMech
- Record: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
- Pull request: #1743
- Started UTC: 2026-09-28T22:22:14Z
- Finished UTC: 2026-09-28T22:22:48Z
- Verdict: needs curation

## Target

Reviewed `data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml`,
a new `CellStructureRecord` for `GO:0032174` / cellular bud neck septin
collar.

The draft adds the exact Gene Ontology bud-neck septin-collar term, the
broader septin-collar parent, bud-neck parthood, one reviewed-label-only septin
component row, Saccharomyces cerevisiae distribution and canonical-example
claims, a bud-neck scaffold function, a nonmechanistic ring-to-collar topology
graph, two curation discussions, one append-only history record, and
regenerated embedding, README, and static-page artifacts.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml` | Passed. |
| `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml` | Passed. |
| `just validate-history history/records/cellular_bud_neck_septin_collar` | Passed for 1 history record. |
| `uv run python scripts/build_text_embedding_map.py --check` | Passed for 678 records and 384 dimensions. |
| `uv run python scripts/render_pages.py --check` | Passed; `pages/` is current. |
| `uv run python scripts/check_docs.py --check` | Passed; the README corpus block is current. |
| `uv run python scripts/validate_strict.py --quiet` | Passed for 678 records. |
| `uv run python scripts/validate_history.py` | Passed for 1271 history records. |
| `uv run python scripts/fetch_snippets.py --verify --check` | Passed; 31 of 31 quotations found verbatim. |
| `uv run python scripts/check_trait_links.py --check` | Passed; 10 of 10 trait links resolved. |
| `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv` | Passed; every checked identifier resolved. |
| `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | Passed; all id/label pairs correspond. |
| `git diff --check` | Passed. |
| `just qc` | Passed locally; 567 tests passed and 3 skipped. |

## Identity and Grounding

The record identity is sound. `GO:0032174` is the exact Gene Ontology
cellular-component term for the cellular bud neck septin collar, `GO:0032173`
is the exact broader septin-collar term, and `GO:0005935` is the bud-neck
parthood target.

The septin component is appropriately left as `REVIEWED_LABEL_ONLY`: the
opened literature supports a Saccharomyces bud-neck cohort of multiple septin
GTPases but does not provide an exact source-neutral family CURIE for all
fungal septins that build this localized collar.

## Evidence

The Gene Ontology definition directly supports an hourglass-shaped, highly
ordered septin-filament collar at the budding-cell neck. Kozubowski, Larson,
and Tatchell 2005 directly support a budding-yeast transition in which the
initial septin ring rearranges into a collar at the mother-bud neck after
budding. Versele and Thorner 2005 directly support budding-yeast septin
polymerization as a prerequisite for septin-collar assembly.

One function sentence is over-specific relative to that evidence. The collar is
located at the bud neck throughout most of the Saccharomyces cell cycle, and
the draft already distinguishes `GO:0032174` from `GO:0032177` split rings
formed at cytokinesis. Its scaffold function should therefore describe
organizing bud-neck-associated proteins at the collar rather than narrowing
the structure's scaffold role to cytokinesis.

## Completeness

The record includes exact GO identity, parentage, parthood, a
reviewed-label-only septin component, species-bounded distribution and
canonical-example evidence, a function, a small nonmechanistic topology graph,
a ring/collar/split-ring boundary discussion, and an open TODO for exact
septin-family groundings.

Hidden/ignored-inclusive duplicate searches covered `data`, `history`,
`research`, `reports`, `pages`, `README.md`, `.github`, `.claude`, and
`scripts` for `GO:0032174`, `GO:0032173`, `GO:0032177`, `GO:0062140`,
`cellular bud neck septin ring`, `cellular bud neck septin collar`, `cellular
bud neck split septin rings`, `split septin rings`, `septin collar`, `septin
hourglass`, and the primary PMID/DOI values. They found one broader
`cellular_bud_neck` note about not asserting septin-collar splitting order, the
new draft, and regenerated derivatives but no pre-existing top-level
`data/structures` record for `GO:0032174`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The `bud_neck_scaffold` function narrows the cellular bud neck septin collar to organizing bud-neck-associated proteins "during budding-yeast cytokinesis". `GO:0032174` defines the collar as fixed at the bud neck throughout most of the cell cycle, Kozubowski et al. describe the ring-to-collar transition after budding, and the record separately excludes the `GO:0032177` cytokinetic split rings. The function should be broadened to cover the persistent bud-neck collar state. | `data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml` |

No blocker findings.

No minor findings.

## Recommended Edits

1. Reword the `bud_neck_scaffold` description so it says the hourglass-shaped
   septin collar organizes proteins that function at the Saccharomyces
   mother-bud neck, without restricting the claim to cytokinesis.
2. Keep the ring/collar/split-ring boundary discussion intact so the broader
   function remains explicitly bounded away from `GO:0032177`.
3. Append a `record_curation_event(..., llm_assisted=True)`, add a new
   append-only history record linked to the GitHub issue for this finding,
   regenerate affected embedding/page/doc artifacts, and rerun focused
   validation plus `just qc`.

## Follow-up Checks

Rerun:

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml`
- `just validate-history history/records/cellular_bud_neck_septin_collar`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `just qc`

## Additional Notes

The generated HTML, indexes, and text-map artifacts have no independent
ownership; they should update only by rerunning the relevant generators after
the maintained YAML is fixed.
