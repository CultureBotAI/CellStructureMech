# YAML Record Review: spindle_pole_body_duplication_plaque

- PR: #1780
- Record: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
- Identifier: cellstructuremech:spindle_pole_body_duplication_plaque
- Label: spindle pole body duplication plaque
- Reviewed at: 2026-09-29T11:50:15Z
- Result: one concrete defect found; filed as #1781.

## Scope

Reviewed the PR after publication against the new YAML record, its rendered
structure page, its generated index and category projections, and its repository
history.

## Checks

- Confirmed that PR #1780 only adds the SPB duplication plaque record, its
  append-only history entry, and regenerated README, embedding, index, and
  static-page artifacts.
- Rechecked the rendered structure page and generated indexes for
  `cellstructuremech:spindle_pole_body_duplication_plaque`,
  `SPB duplication plaque`, and `spb_duplication_plaque_transition`.
- Reviewed the boundary between the new duplication plaque record, the local
  SPB satellite record, and the mature `GO:0005816` spindle pole body record.
- Reviewed graph edge evidence against the prose claim it supports.

## Findings

### 1. The duplication plaque precursor edge cites evidence too generically

- Issue: #1781
- Severity: low
- Location: `causal_graphs[spb_duplication_plaque_transition].edges[duplication_plaque -> daughter_spindle_pole_body]`

The edge asserts that the duplication plaque is a transient plaque intermediate
before the daughter SPB is complete, but its only evidence note says that Adams
and Kilmartin localized core SPB components through daughter plaque stages. That
wording is broader than the edge and should directly support the
duplication-plaque-as-precursor claim.

Tighten the edge by adding or rewriting evidence so the note directly supports
the duplication-plaque transition.
