# YAML Record Review: hyphal tip polarisome

- Repository: CultureBotAI/CellStructureMech
- Record: data/structures/other/hyphal_tip_polarisome.yaml
- Started UTC: 2026-09-28T20:55:40Z
- Finished UTC: 2026-09-28T20:57:21Z
- Verdict: needs curation

## Target

Reviewed `data/structures/other/hyphal_tip_polarisome.yaml`, a maintained
`CellStructureRecord` for `GO:0031562` / hyphal tip polarisome.

The record is a new `OTHER` / `MULTIPROTEIN_COMPLEX` draft with
`mapping_status: PROPOSED`, in-record creation, expansion, and graph-refinement
events, one repository history record under
`history/records/hyphal_tip_polarisome/`, and regenerated README, text-map, and
page artifacts.

## Validation

| Check | Result |
|---|---|
| `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/hyphal_tip_polarisome.yaml` | Passed. |
| `uv run python scripts/validate_strict.py --quiet data/structures/other/hyphal_tip_polarisome.yaml` | Passed. |
| `just validate-history history/records/hyphal_tip_polarisome` | Passed for 1 history record. |
| `uv run python scripts/build_text_embedding_map.py --check` | Passed for 676 records and 384 dimensions. |
| `uv run python scripts/render_pages.py --check` | Passed; `pages/` is current. |
| `uv run python scripts/check_docs.py --check` | Passed; the README corpus block is current. |
| `uv run python scripts/validate_strict.py --quiet` | Passed for 676 records. |
| `uv run python scripts/validate_history.py` | Passed for 1267 history records. |
| `uv run python scripts/fetch_snippets.py --verify --check` | Passed; 31 of 31 quotations found verbatim. |
| `uv run python scripts/check_trait_links.py --check` | Passed; 10 of 10 trait links resolved. |
| `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv` | Passed; every checked identifier resolved. |
| `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | Passed; all id/label pairs correspond. |
| `git diff --check` | Passed. |
| `just qc` | Passed locally; 567 tests passed and 3 skipped. |
| PR `vendored-sync` | Passed on PR #1739. |

## Identity and Grounding

The primary identity is sound. `GO:0031562` resolves to the exact Gene Ontology
cellular-component term for a hyphal tip polarisome; `GO:0000133` is the exact
broader polarisome term; and `GO:0001411` is the exact fungal hyphal tip parthood
target.

The component groundings are deliberately conservative. SPA-2, BUD-6, and BNI-1
are kept as `REVIEWED_LABEL_ONLY` Neurospora component rows with an open
discussion to resolve exact source-neutral family CURIEs later rather than
guessing broad InterPro, Pfam, or NCBIfam families.

## Evidence

Lichius et al. 2012 support the mature-tip topology for SPA-2, BUD-6, and BNI-1
in Neurospora hyphae. The record uses that paper conservatively for a localized
first pass: it records spatial occupancy at the mature hyphal tip without
asserting direct physical contacts among the three proteins.

One interpretation row is under-scoped relative to the same evidence. The record
correctly keeps septal-plug, cell-fusion, septation, and cytokinetic-ring
assemblies outside this `GO:0031562` record, but the resolved discussion attaches
only to BUD-6 and BNI-1 even though SPA-2 is the curated marker for the record
and Lichius et al. also reports non-tip septal-plug localization for the
polarisome proteins.

## Completeness

The new record includes exact GO identity, parentage, parthood, three
reviewed-label-only Neurospora component rows, a species-bounded distribution
and canonical example, a function, a nonmechanistic topology graph, and
appropriate grounding and boundary discussions.

The iModulonDB structured-source adapter was not applicable: this record
describes a filamentous-fungal cellular component and uses Neurospora polarity
genes rather than an iModulonDB-covered bacterial regulator, gene, locus, stress
response, or dataset.

Hidden/ignored-inclusive duplicate searches covered `data`, `history`,
`research`, `reports`, and `pages` for `GO:0031562`, `hyphal tip polarisome`,
obvious spelling variants, and `DOI:10.1371/journal.pone.0030372`. They found
the new draft, generated derivatives, and broader `polarisome` cross-references
but no pre-existing top-level `data/structures` record for `GO:0031562`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The non-tip boundary discussion omits SPA-2 while excluding septal plugging from the hyphal-tip polarisome. The record curates SPA-2 as the Neurospora marker for the mature hyphal-tip polarisome, and the prompt already makes septal plugging an excluded role; the discussion needs to attach to `components#spa2_scaffold` and state that SPA-2's septal-plug localization is outside the `GO:0031562` boundary. | `data/structures/other/hyphal_tip_polarisome.yaml` |

No blocker findings.

No minor findings.

## Recommended Edits

1. In `data/structures/other/hyphal_tip_polarisome.yaml`, add
   `components#spa2_scaffold` to the
   `exclude_polarisome_independent_roles.attaches_to` list.
2. Reword that discussion's rationale, resolution note, and evidence note so the
   boundary decision explicitly covers SPA-2 septal plugging as well as BUD-6
   and BNI-1 cell-fusion, septation, and cytokinetic-ring roles.
3. Append a `record_curation_event(..., llm_assisted=True)`, add a new
   append-only history record linked to the GitHub issue for this finding,
   regenerate pages, docs, and text embeddings, then rerun focused validation
   plus `just qc`.

## Follow-up Checks

Rerun:

- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/hyphal_tip_polarisome.yaml`
- `uv run python scripts/validate_strict.py --quiet data/structures/other/hyphal_tip_polarisome.yaml`
- `just validate-history history/records/hyphal_tip_polarisome`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `just qc`

## Additional Notes

The generated HTML, indexes, and text-map artifacts have no independent
ownership; they should update only by rerunning the relevant generators after
the maintained YAML is fixed.
