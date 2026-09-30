# Mating Projection Base YAML Record Review

- **PR:** #1842
- **Branch:** `add-mating-projection-base`
- **Reviewed head:** `8f83047c0965102643a3542323b432e670b8decc`
- **Record:** `data/structures/appendage/mating_projection_base.yaml`
- **Identifier:** `GO:0001400`
- **Reviewed at:** `2026-09-30T21:53:24Z`

## Scope

Reviewed the PR diff that adds the `GO:0001400` mating projection base record, the
generated static page, the embedding artifacts, README statistics, and the first
append-only history record for `mating_projection_base`.

## Duplicate Search

Re-ran hidden/ignored-inclusive searches for:

- `GO:0001400`
- `GO_0001400`
- `mating projection base`
- `base of shmoo tip`
- `conjugation tube base`
- `10.1091/mbc.3.4.429`

The broad search found the new record, its generated pages and embedding entries,
the `GO:0001400` resolver cache and CURIE report row, the existing
`mating_projection` record that already named `GO:0001400` as a child part, and
other mating-projection records that already cited the Read et al. 1992 DOI.

An anchored `data/structures` search for the exact identifier, label, and two GO
synonyms found only `data/structures/appendage/mating_projection_base.yaml`.
No pre-existing standalone mating-projection-base record or conflicting
identifier record was present.

## Evidence And Boundary Checks

- `GO:0001400` exactly denotes the basal region where a mating projection meets
  the cell body, rather than the whole `GO:0005937` mating projection, the
  `GO:0043332` projection tip, or the `GO:0070250` projection membrane.
- `structure_category: APPENDAGE` matches the existing `GO:0005937` mating
  projection and mating-projection membrane records.
- `structure_kind: SUBCELLULAR_REGION` matches the regional semantics already
  used for the neighboring `GO:0043332` mating projection tip record.
- `part_of: GO:0005937` reciprocates the existing parent record's
  `has_part: GO:0001400` and the causal graph limits itself to that GO-backed
  topological relation.
- The Saccharomyces cerevisiae distribution is kept species-level and `VARIABLE`
  because the cited Read et al. 1992 work supports pheromone-induced mating
  projections in budding yeast, not constitutive or broad fungal presence.
- No molecular components or functions were inferred for this basal region; the
  boundary discussion explicitly keeps tip-localized, membrane, septin, and
  whole-projection machinery on their own records.

## Validation Reviewed

Confirmed local green gates before this review:

- focused LinkML validation for `mating_projection_base.yaml`
- focused strict validation for `mating_projection_base.yaml`
- focused history validation for `history/records/mating_projection_base`
- embedding, rendered-page, and README drift checks
- full strict validation
- full history validation
- snippet verification
- TraitMech link validation
- CURIE liveness validation
- id/label correspondence validation
- `git diff --check`
- `just qc`

## Findings

No concrete defects found. No review issues were filed.
