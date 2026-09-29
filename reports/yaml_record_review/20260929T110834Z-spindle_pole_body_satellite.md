# YAML Record Review: spindle_pole_body_satellite

- PR: #1778
- Record: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
- Identifier: cellstructuremech:spindle_pole_body_satellite
- Label: spindle pole body satellite
- Reviewed at: 2026-09-29T11:08:34Z
- Result: one concrete defect found; filed as #1779.

## Scope

Reviewed the PR after publication against the new YAML record, its rendered
structure page, its generated index and category projections, its repository
history, and nearby spindle-pole-body records.

## Checks

- Confirmed that PR #1778 only adds the SPB satellite record, its append-only
  history entries, and regenerated README, embedding, index, and static-page
  artifacts.
- Rechecked the rendered structure page and generated indexes for
  `cellstructuremech:spindle_pole_body_satellite`, `SPB satellite`,
  `GO:0032991`, and `spb_satellite_precursor_assembly`.
- Reviewed the boundary between the new satellite record, the mature
  `GO:0005816` spindle pole body record, and the `GO:0005825` half-bridge
  record to verify that the satellite was minted as a local precursor rather
  than folded into either exact GO term.
- Reviewed the graph edge evidence against the prose claim it supports.

## Findings

### 1. The satellite precursor edge cites evidence too generically

- Issue: #1779
- Severity: low
- Location: `causal_graphs[spb_satellite_precursor_assembly].edges[spb_satellite -> daughter_spindle_pole_body]`

The edge asserts that the SPB satellite is a precursor of the daughter spindle
pole body, but its only evidence note says that Adams and Kilmartin localized
core SPB components during SPB duplication. That evidence note is broader than
the edge claim and does not explicitly connect the cited paper to the satellite
as a precursor intermediate.

Tighten the edge by adding or rewriting evidence so the note directly supports
the satellite-as-precursor claim.
