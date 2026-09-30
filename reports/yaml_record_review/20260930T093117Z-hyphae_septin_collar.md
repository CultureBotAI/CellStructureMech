# YAML record review: hyphae_septin_collar

- PR: #1817
- Record: `data/structures/cytoskeleton/hyphae_septin_collar.yaml`
- Reviewed: 2026-09-30T09:31:17Z

## Findings

### 1. The Pyricularia rows cite the septin-collar paper but only describe generic invasive-hyphae context

Severity: medium

Location: `data/structures/cytoskeleton/hyphae_septin_collar.yaml:48`

The `taxonomic_distribution` row says only that *Pyricularia oryzae* forms
invasive hyphae during plant cell-to-cell movement, and the `canonical_examples`
row says only that Sakulkoo et al. analyzed plant cell-to-cell invasion through
plasmodesmata. Those notes could support an invasive-hyphae model without
demonstrating the `GO:0062140` structure itself.

Sakulkoo et al. 2018 is the right primary reference: it directly describes
Sep5-GFP septin collars at rice cell wall crossing points in invasive hyphae and
shows that Pmk1 inhibition leaves Sep5-GFP in a disorganized mass instead of a
septin collar. The two *P. oryzae* rows should state that structure-level
evidence so the taxon and canonical-example claims are grounded in a primary
collar observation, not just a broader invasive-growth context.

Recommendation: update the `taxonomic_distribution` and `canonical_examples`
notes to say that *P. oryzae* invasive hyphae assemble Sep5-GFP septin collars at
plant cell wall crossing points, while retaining `DOI:10.1126/science.aaq0892`.

## Non-findings

- The existing-record check used `rg --no-ignore --hidden` over
  `data/structures`; it found `GO:0062140` only as child-term evidence on the
  broader septin-collar record, not as a top-level identifier, label, or synonym.
- `GO:0032173` is the exact is-a parent for `GO:0062140`, and the boundary note
  keeps the record distinct from the existing `GO:0032168` hyphal septin ring at
  future septation sites.
- The `septin_proteins` component is deliberately
  `REVIEWED_LABEL_ONLY`; the record does not guess InterPro, Pfam, NCBIfam,
  UniProtKB, ComplexPortal, ChEBI, SO, or NCBITaxon groundings.
- The generated browse, category, grounded, index, structure page, and embedding
  artifacts include `GO:0062140` and match the curated YAML.
