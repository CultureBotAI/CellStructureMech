# YAML Record Review: cellular bud neck septin ring

- Repository: CultureBotAI/CellStructureMech
- Record: data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml
- Pull request: #1745
- Started UTC: 2026-09-28T23:06:51Z
- Finished UTC: 2026-09-28T23:07:22Z
- Verdict: needs curation

## Target

Reviewed `data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml`,
a new `CellStructureRecord` for `GO:0000144` / cellular bud neck septin ring.

The draft adds the exact Gene Ontology bud-neck septin-ring term, broader
septin-ring parentage, bud-neck parthood, one reviewed-label-only septin
component row, Saccharomyces cerevisiae distribution and canonical-example
claims, a future-bud-site scaffold function, a nonmechanistic ring-to-collar
topology graph, two curation discussions, one append-only history record, and
regenerated embedding, README, and static-page artifacts.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml` | Passed. |
| `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml` | Passed. |
| `just validate-history history/records/cellular_bud_neck_septin_ring` | Passed for 1 history record. |
| `uv run python scripts/build_text_embedding_map.py --check` | Passed for 679 records and 384 dimensions. |
| `uv run python scripts/render_pages.py --check` | Passed; `pages/` is current. |
| `uv run python scripts/check_docs.py --check` | Passed; the README corpus block is current. |
| `uv run python scripts/validate_strict.py --quiet` | Passed for 679 records. |
| `uv run python scripts/validate_history.py` | Passed for 1273 history records. |
| `uv run python scripts/fetch_snippets.py --verify --check` | Passed; 31 of 31 quotations found verbatim. |
| `uv run python scripts/check_trait_links.py --check` | Passed; 10 of 10 trait links resolved. |
| `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv` | Passed; every checked identifier resolved. |
| `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | Passed; all id/label pairs correspond. |
| `git diff --check` | Passed. |
| `just qc` | Passed locally; 567 tests passed and 3 skipped. |

## Identity and Grounding

The record identity is sound. `GO:0000144` is the exact Gene Ontology
cellular-component term for the cellular bud neck septin ring, `GO:0005940` is
the exact broader septin-ring term, and `GO:0005935` is the bud-neck parthood
target.

The septin-protein component is appropriately left as
`REVIEWED_LABEL_ONLY`: the record is scoped to the localized Saccharomyces
bud-neck ring, while exact source-neutral groundings for the complete septin
paralog cohort and GO-defined septin-associated proteins remain unresolved.

## Evidence

The Gene Ontology definition directly supports a ring-shaped structure in the
bud neck of a budding cell that contains septins and septin-associated
proteins. Kozubowski, Larson, and Tatchell 2005 directly support a
Saccharomyces transition in which septins form a ring-shaped scaffold at the
future budding site and then rearrange into a collar at the mother-bud neck
after budding.

The maintained claims are species-bounded and conservative: the broad
GO:0000144 identity is used for the record, while the non-GO distribution,
example, scaffold function, and ring-to-collar graph claims stay at
`NCBITaxon:4932`.

## Completeness

The record includes exact GO identity, parentage, parthood, a
reviewed-label-only septin component, species-bounded distribution and
canonical-example evidence, a function, a small nonmechanistic topology graph,
a ring/collar/split-ring boundary discussion, and an open TODO for exact
component boundaries.

Hidden/ignored-inclusive duplicate searches covered `data`, `history`,
`research`, `reports`, `pages`, `README.md`, `.github`, `.claude`, and
`scripts` for `GO:0000144`, `cellular bud neck septin ring`, future-bud-site
septin-ring text, and the derived `cellular_bud_neck_septin_ring` slug. They
found the existing bud-neck septin-collar topology node, the new draft, and
regenerated derivatives but no pre-existing top-level `data/structures` record
for `GO:0000144`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `resolve_bud_neck_ring_components` records a record-level component-boundary question because `GO:0000144` includes septin-associated proteins that are deliberately not curated yet, but `attaches_to` lists only `components#septin_proteins`. It should also attach to `record`, otherwise the open issue appears to concern only the curated septin row instead of the omitted GO-defined accessory constituents. | `data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml` |

No blocker findings.

No minor findings.

## Recommended Edits

1. Add `record` to
   `discussions[resolve_bud_neck_ring_components].attaches_to`.
2. Keep `components#septin_proteins` in the same attachment list so the TODO
   remains visible from the reviewed-label-only septin component.
3. Append a `record_curation_event(..., llm_assisted=True)`, add a new
   append-only history record linked to the GitHub issue for this finding,
   regenerate affected embedding/page/doc artifacts, and rerun focused
   validation plus `just qc`.

## Follow-up Checks

Rerun:

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml`
- `just validate-history history/records/cellular_bud_neck_septin_ring`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `just qc`

## Additional Notes

The generated HTML, indexes, and text-map artifacts have no independent
ownership; they should update only by rerunning the relevant generators after
the maintained YAML is fixed.
