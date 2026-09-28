# YAML Record Review: cellular bud neck polarisome

- Repository: CultureBotAI/CellStructureMech
- Record: data/structures/other/cellular_bud_neck_polarisome.yaml
- Pull request: #1741
- Started UTC: 2026-09-28T21:39:28Z
- Finished UTC: 2026-09-28T21:39:35Z
- Verdict: needs curation

## Target

Reviewed `data/structures/other/cellular_bud_neck_polarisome.yaml`, a new
`CellStructureRecord` for `GO:0031560` / cellular bud neck polarisome.

The draft adds the exact Gene Ontology bud-neck polarisome term, broader
polarisome parentage, bud-neck parthood, one reviewed-label-only Spa2/Pea2
component row, Saccharomyces cerevisiae distribution and canonical-example
claims, a bud-neck polarity function, a nonmechanistic topology graph, two
curation TODOs, one append-only history record, and regenerated embedding,
README, and static-page artifacts.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/cellular_bud_neck_polarisome.yaml` | Passed. |
| `uv run python scripts/validate_strict.py --quiet data/structures/other/cellular_bud_neck_polarisome.yaml` | Passed. |
| `just validate-history history/records/cellular_bud_neck_polarisome` | Passed for 1 history record. |
| `uv run python scripts/build_text_embedding_map.py --check` | Passed for 677 records and 384 dimensions. |
| `uv run python scripts/render_pages.py --check` | Passed; `pages/` is current. |
| `uv run python scripts/check_docs.py --check` | Passed; the README corpus block is current. |
| `uv run python scripts/validate_strict.py --quiet` | Passed for 677 records. |
| `uv run python scripts/validate_history.py` | Passed for 1269 history records. |
| `uv run python scripts/fetch_snippets.py --verify --check` | Passed; 31 of 31 quotations found verbatim. |
| `uv run python scripts/check_trait_links.py --check` | Passed; 10 of 10 trait links resolved. |
| `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv` | Passed; every checked identifier resolved. |
| `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | Passed; all id/label pairs correspond. |
| `git diff --check` | Passed. |
| `just qc` | Passed locally; 567 tests passed and 3 skipped. |

## Identity and Grounding

The record identity is sound. `GO:0031560` is the exact Gene Ontology
cellular-component term for the cellular bud neck polarisome, `GO:0000133` is
the exact broader polarisome term, and `GO:0005935` is the bud-neck parthood
target.

The Spa2/Pea2 component is appropriately left as `REVIEWED_LABEL_ONLY`: the
opened literature supports Saccharomyces-specific SPA2/PEA2 localization and
functional coupling but does not provide an exact taxon-neutral family CURIE for
a fungal bud-neck scaffold cohort.

## Evidence

Valtz and Herskowitz 1996 directly support Pea2 staining at the neck between
mother and daughter cells after nuclear division and before cytokinesis, and
they report that the overall Pea2 localization pattern matches Spa2. The record
therefore has enough evidence for a conservative first-pass
Saccharomyces-localized bud-neck polarisome record.

One graph edge is over-specific relative to that evidence. The record annotates
`spa2_pea2_scaffold` as a protein constituent of `GO:0031560`, then adds a
`localizes to` edge from the scaffold back to the `GO:0031560` complex itself.
The paper directly localizes Pea2 and Spa2 to the mother-daughter neck, not to a
separately delimited bud-neck polarisome entity; GO provides the interpretation
that the bud-neck complex is a polarisome found at that neck site.

## Completeness

The record includes exact GO identity, parentage, parthood, a
reviewed-label-only Spa2/Pea2 component, species-bounded distribution and
canonical-example evidence, a function, a small nonmechanistic topology graph,
and open TODO discussions for component grounding and additional bud-neck
polarisome constituents.

Hidden/ignored-inclusive duplicate searches covered `data`, `history`,
`research`, `reports`, and `pages` for `GO:0031560`, `cellular bud neck
polarisome`, `bud neck polarisome`, the primary Valtz and Herskowitz DOI, and
the Sheu et al. DOI. They found broader `polarisome` cross-references, generated
derivatives, and the new draft but no pre-existing top-level
`data/structures` record for `GO:0031560`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | `bud_neck_polarisome_topology` points the Spa2/Pea2 scaffold at `cellular_bud_neck_polarisome`, even though the DOI evidence directly supports localization to the mother-daughter neck. The edge should terminate at `cellular_bud_neck` or be rewritten as a structural interpretation that combines GO identity with the staining paper. | `data/structures/other/cellular_bud_neck_polarisome.yaml` |

No blocker findings.

No minor findings.

## Recommended Edits

1. Retarget the `spa2_pea2_scaffold` localization edge to
   `cellular_bud_neck`, or rewrite it with a non-localization predicate that
   records the scaffold as part of the localized complex rather than pretending
   the Valtz staining paper separately recognized a bud-neck polarisome object.
2. Adjust the graph description and edge text so the DOI-backed statements say
   Spa2/Pea2 were seen at the mother-daughter neck, while the GO-backed
   statements identify the neck-localized complex as `GO:0031560`.
3. Append a `record_curation_event(..., llm_assisted=True)`, add a new
   append-only history record linked to the GitHub issue for this finding,
   regenerate affected embedding/page/doc artifacts, and rerun focused
   validation plus `just qc`.

## Follow-up Checks

Rerun:

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/cellular_bud_neck_polarisome.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/cellular_bud_neck_polarisome.yaml`
- `just validate-history history/records/cellular_bud_neck_polarisome`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `just qc`

## Additional Notes

The generated HTML, indexes, and text-map artifacts have no independent
ownership; they should update only by rerunning the relevant generators after
the maintained YAML is fixed.
