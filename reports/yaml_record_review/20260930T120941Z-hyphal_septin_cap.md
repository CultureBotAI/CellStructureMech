# YAML record review: hyphal_septin_cap

- PR: #1823
- Record: `data/structures/cytoskeleton/hyphal_septin_cap.yaml`
- Reviewed: 2026-09-30T12:09:42Z

## Findings

No concrete defects found.

## Non-findings

- The duplicate check used `rg --no-ignore --hidden` over `data/structures`;
  `GO:0032164`, `hyphal septin cap`, and `hyphal_septin_cap` are top-level
  values only in the new `data/structures/cytoskeleton/hyphal_septin_cap.yaml`.
  Pre-existing `GO:0032164` mentions were boundary evidence on the broader
  `septin_cap` record, not a duplicate structure record.
- OLS reports `GO:0032159` as the direct parent for `GO:0032164`, and the
  hyphal-cap OLS graph does not expose a direct `part_of` edge; the new record
  correctly uses only `GO:0032159` in `parent_structures`.
- The three `hyphal_septin_cap_topology` edges are supported directly by the
  `GO:0032164` definition: septins form the cap, the cap localizes to the
  hyphal leading edge, and the cap colocalizes with an ergosterol-rich
  plasma-membrane region.
- The `septin_proteins` component correctly remains `REVIEWED_LABEL_ONLY`; the
  record does not guess InterPro, Pfam, NCBIfam, UniProtKB, ComplexPortal,
  ChEBI, SO, or NCBITaxon groundings.
- The boundary discussion keeps the exact hyphal apical cap distinct from the
  generic `GO:0032159` septin cap, the `GO:0032171` germ-tube septin cap
  sibling, and the `GO:0032168` hyphal septation-site ring.
- The generated browse, cytoskeleton category, grounded, index, structure page,
  and embedding artifacts include `GO:0032164` and match the curated YAML.
