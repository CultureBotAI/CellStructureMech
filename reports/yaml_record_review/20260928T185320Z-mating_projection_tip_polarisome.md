# YAML Record Review: mating projection tip polarisome

- Repository: CultureBotAI/CellStructureMech
- Record: data/structures/other/mating_projection_tip_polarisome.yaml
- Started UTC: 2026-09-28T18:52:52Z
- Finished UTC: 2026-09-28T18:53:20Z
- Verdict: needs curation

## Target

Reviewed `data/structures/other/mating_projection_tip_polarisome.yaml`, a maintained
`CellStructureRecord` for `GO:0031563` / mating projection tip polarisome.

The record is a new `OTHER` / `MULTIPROTEIN_COMPLEX` draft with `mapping_status:
PROPOSED`, in-record curation events, two repository history records under
`history/records/mating_projection_tip_polarisome/`, and regenerated pages and
embedding artifacts.

## Validation

| Check | Result |
|---|---|
| `uv run python scripts/validate_strict.py --quiet` | Passed for 674 records. |
| `uv run python scripts/validate_history.py` | Passed for 1263 history records. |
| `uv run python scripts/fetch_snippets.py --verify --check` | Passed; 31 of 31 quotations found verbatim. |
| `uv run python scripts/check_trait_links.py --check` | Passed; 10 of 10 trait links resolved. |
| `uv run python scripts/check_curies.py --check --report reports/curie_check.tsv` | Passed; `GO:0031563`, `GO:0000133`, `GO:0043332`, `GO:0031382`, and both DOI references resolve. |
| `uv run python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml` | Passed; all id/label pairs correspond. |
| `uv run python scripts/build_text_embedding_map.py --check` | Passed for 674 records and 384 dimensions. |
| `uv run python scripts/render_pages.py --check` | Passed; `pages/` is current. |
| `uv run python scripts/check_docs.py --check` | Passed; the README corpus block is current. |
| `just validate-all` | Passed. |
| `just qc` | Passed; 567 tests passed, 3 skipped, 2 warnings. |

## Identity and Grounding

The primary identity is sound. `GO:0031563` resolves to the exact Gene Ontology
cellular-component term for a mating projection tip polarisome; `GO:0000133` is
the exact broader polarisome term; and `GO:0043332` is the exact mating projection
tip partonomy target. The record correctly leaves Cdc24, Bem3, Fus1, and Fus2
outside the component list because Bidlingmaier and Snyder 2004 treat them as
Cdc42 regulators or fusion proteins that affect projection cycles, not as
polarisome constituents.

## Evidence

Bidlingmaier and Snyder 2004 support a Saccharomyces pheromone-response context
and support Spa2, Pea2, and Bni1 roles in the frequency or termination of periodic
mating-projection growth. Valtz and Herskowitz 1996 support Pea2/Spa2
co-localization at polarized-growth sites in mating cells. The GO parent term
supports Bni1 as a named Saccharomyces polarisome protein.

One boundary claim is under-explained: Bidlingmaier and Snyder 2004 also mention
Bud6/Aip3 as another known polarisome component and explicitly tested `bud6`
deletion during periodic projection formation. The new record omits Bud6 without
a `components#...` entry, a resolved interpretation, or an open discussion item
explaining whether Bud6 is outside the localized `GO:0031563` boundary or was only
deferred.

## Completeness

The new record includes identity, parentage, parthood, reviewed-label-only
components for Spa2/Pea2 and Bni1, a bounded Saccharomyces taxonomic example,
a function, a nonmechanistic graph, and two relevant discussions. The
consequential gap is the missing Bud6/Aip3 boundary treatment described above.

The iModulonDB structured-source adapter was not applicable: this record describes
a fungal cellular component and uses Saccharomyces polarity genes rather than an
iModulonDB-covered bacterial regulator, gene, locus, stress response, or dataset.

A gitignore-independent search covered `data`, `history`, `pages`, `reports`,
`README.md`, `.github`, and `.claude` for `Bud6`, `BUD6`, and
`component_id: bud6`; it found the existing broader `polarisome` record and
generated derivatives but no Bud6 treatment in
`mating_projection_tip_polarisome.yaml`.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The Saccharomyces component boundary drops Bud6/Aip3 without an explicit curation decision. The broader `GO:0000133` polarisome record curates Bud6 as a canonical Saccharomyces constituent, and Bidlingmaier and Snyder 2004 identify Bud6 as a known polarisome component while reporting that `bud6Δ` did not change the periodic mating-projection phenotypes. This needs either a Bud6 component supported by exact localized evidence or a discussion that deliberately excludes or defers Bud6 for this tip-localized record. | `data/structures/other/mating_projection_tip_polarisome.yaml` |

No blocker findings.

No minor findings.

## Recommended Edits

1. In `data/structures/other/mating_projection_tip_polarisome.yaml`, add an
   explicit Bud6/Aip3 boundary decision. Prefer a `bud6_actin_nucleation_factor`
   component if exact mating-projection-tip polarisome evidence is available;
   otherwise add an open or resolved discussion explaining why the canonical
   polarisome Bud6 constituent is omitted from this localized first pass.
2. Attach the decision to concrete component or graph anchors, append a
   `record_curation_event(..., llm_assisted=True)`, and add a new
   append-only history record for the review fix.

## Follow-up Checks

Rerun:

- `just validate-history history/records/mating_projection_tip_polarisome`
- `uv run python scripts/validate_strict.py data/structures/other/mating_projection_tip_polarisome.yaml`
- `uv run python scripts/render_pages.py && uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --write && uv run python scripts/check_docs.py --check`
- `just validate-all`
- `just qc`

## Additional Notes

The generated HTML has no independent ownership; it should update only by
rerunning `scripts/render_pages.py` after the maintained YAML is fixed.
