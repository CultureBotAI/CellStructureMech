# YAML record review: germ_tube_septin_cap

- PR: #1824
- Record: `data/structures/cytoskeleton/germ_tube_septin_cap.yaml`
- Reviewed: 2026-09-30T12:38:57Z

## Findings

No concrete defects found.

## Non-findings

- The duplicate check used `rg --no-ignore --hidden` over `data/structures`;
  `GO:0032171`, `germ tube septin cap`, and `germ_tube_septin_cap` are
  top-level values only in the new
  `data/structures/cytoskeleton/germ_tube_septin_cap.yaml`. Pre-existing
  `GO:0032171` mentions were sibling-boundary evidence on broader or adjacent
  septin-cap records, not duplicate structure records.
- OLS reports `GO:0032159` as the direct parent for `GO:0032171`, and the OLS
  graph reports `GO:0032171` as `part_of` `GO:0032179`; the new record carries
  those direct relations in `parent_structures` and `part_of`.
- The four `germ_tube_septin_cap_topology` edges are all GO-backed and every
  edge endpoint has a matching node, including the grounded `GO:0032179` germ
  tube node.
- The `septin_proteins` component correctly remains `REVIEWED_LABEL_ONLY`; the
  record does not guess InterPro, Pfam, NCBIfam, UniProtKB, ComplexPortal,
  ChEBI, SO, or NCBITaxon groundings.
- The boundary discussion keeps the exact germ-tube apical cap distinct from
  the generic `GO:0032159` septin cap, the `GO:0032164` hyphal septin cap
  sibling, and the `GO:0032172` germ-tube septation-site ring.
- The generated browse, cytoskeleton category, grounded, index, structure page,
  and embedding artifacts include `GO:0032171` and match the curated YAML.
