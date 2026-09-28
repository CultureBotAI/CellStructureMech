# YAML Record Review: cellular bud tip polarisome

- Repository: CultureBotAI/CellStructureMech
- Record: data/structures/other/cellular_bud_tip_polarisome.yaml
- Started UTC: 2026-09-28T19:55:09Z
- Finished UTC: 2026-09-28T19:56:27Z
- Verdict: needs curation

## Target

Reviewed `data/structures/other/cellular_bud_tip_polarisome.yaml`, a maintained
`CellStructureRecord` for `GO:0031561` / cellular bud tip polarisome.

The record is a new `OTHER` / `MULTIPROTEIN_COMPLEX` draft with
`mapping_status: PROPOSED`, in-record creation and expansion events, one
repository history record under `history/records/cellular_bud_tip_polarisome/`,
and regenerated README, text-map, and page artifacts.

## Validation

| Check | Result |
|---|---|
| `uv run python scripts/validate_strict.py --quiet` | Passed for 675 records. |
| `uv run python scripts/validate_history.py` | Passed for 1265 history records. |
| `uv run python scripts/fetch_snippets.py --verify --check` | Passed; 31 of 31 quotations found verbatim. |
| `uv run python scripts/check_trait_links.py --check` | Passed; 10 of 10 trait links resolved. |
| `uv run python scripts/build_text_embedding_map.py --check` | Passed for 675 records and 384 dimensions. |
| `uv run python scripts/render_pages.py --check` | Passed; `pages/` is current. |
| `uv run python scripts/check_docs.py --check` | Passed; the README corpus block is current. |
| `just qc` | Passed locally; 567 tests passed, 3 skipped, 2 warnings. |
| PR `identifier-liveness` | Passed on PR #1737. |
| PR `label-correspondence` | Passed on PR #1737. |
| PR `vendored-sync` | Passed on PR #1737. |

## Identity and Grounding

The primary identity is sound. `GO:0031561` resolves to the exact Gene Ontology
cellular-component term for the cellular bud tip polarisome, the term is under
the broader `GO:0000133` polarisome identity, and `GO:0005934` is the exact
cellular bud tip parthood target.

The component boundary is mostly sound: the record correctly keeps the exocyst
and MAPK pathway proteins out of the 12S polarisome itself, and it explicitly
defers candidate Bni1, Aip5, and Myo2 relationships until direct localized
component evidence is curated.

## Evidence

Valtz and Herskowitz 1996 support the Spa2/Pea2 polarized-growth-site cohort in
budding and mating `Saccharomyces cerevisiae` cells. Sheu et al. 1998 support
direct Spa2-Pea2 association and support Bud6/Aip3 as a weaker 12S polarisome
member that cosediments with Spa2 and Pea2. `GO:0031561` supports the exact
bud-tip-localized identity.

One component label is over-specific relative to the evidence attached in this
localized first pass: the record labels Bud6/Aip3 as an actin
nucleation-promoting factor, but the cited Sheu et al. source directly supports
an actin-associated polarity protein cosedimenting in the 12S polarisome.
Because this same record deliberately defers the later Bni1/Aip5
actin-polymerization module, the Bud6 label should not import that narrower
module without its supporting literature.

## Completeness

The new record includes exact GO identity, parentage, parthood, two
reviewed-label-only Saccharomyces component rows, a Saccharomyces distribution
and canonical example, a function, a nonmechanistic topology graph, and two
relevant discussions.

The iModulonDB structured-source adapter was not applicable: this record
describes a fungal cellular component and uses Saccharomyces polarity genes
rather than an iModulonDB-covered bacterial regulator, gene, locus, stress
response, or dataset.

A gitignore-independent duplicate search covered `data/structures`, `history`,
`pages`, `reports`, `README.md`, `.github`, `.claude`, and `scripts` for
`GO:0031561`, `cellular bud tip polarisome`, and
`cellular_bud_tip_polarisome`. It found the new draft, generated derivatives,
and broader-record cross-references but no pre-existing top-level
`data/structures` record.

## Findings

| Severity | Finding | Maintained owner |
|---|---|---|
| Major | The `bud6_actin_nucleation_factor` component and graph node overstate the reviewed evidence by naming Bud6/Aip3 as an actin nucleation-promoting factor while this record cites only Sheu et al. 1998 for the localized 12S polarisome claim and explicitly defers the Bni1/Aip5 actin-polymerization module. The directly cited evidence supports renaming this row to an actin-associated polarity protein. | `data/structures/other/cellular_bud_tip_polarisome.yaml` |

No blocker findings.

No minor findings.

## Recommended Edits

1. In `data/structures/other/cellular_bud_tip_polarisome.yaml`, rename
   `bud6_actin_nucleation_factor` and its graph node from
   `Bud6/Aip3 actin nucleation-promoting factor` to `Bud6/Aip3 actin-associated
   polarity protein`.
2. Keep the curation TODO and Bni1/Aip5/Myo2/exocyst/MAPK boundary decision in
   place, append a `record_curation_event(..., llm_assisted=True)`, and add a
   new append-only history record linked to the GitHub issue for this finding.

## Follow-up Checks

Rerun:

- `just validate-history history/records/cellular_bud_tip_polarisome`
- `uv run python scripts/validate_strict.py data/structures/other/cellular_bud_tip_polarisome.yaml`
- `uv run python scripts/build_text_embedding_map.py --check`
- `uv run python scripts/render_pages.py --check`
- `uv run python scripts/check_docs.py --check`
- `just qc`

## Additional Notes

The generated HTML, indexes, and text-map artifacts have no independent
ownership; they should update only by rerunning the relevant generators after
the maintained YAML is fixed.
