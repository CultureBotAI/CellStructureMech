# YAML Record Review: curli_secretion_complex

- PR: #1764
- Issue: #1765
- Record: `data/structures/secretion_system/curli_secretion_complex.yaml`
- Related record: `data/structures/appendage/curli.yaml`
- Reviewed at: 2026-09-29T05:43:53Z
- Result: changes requested

## Scope

Adversarial review of the new `GO:0062155` curli secretion complex record, the
resolved `GO:0098774` curli boundary TODO, their append-only history entries,
and regenerated CellStructureMech pages, docs, and embedding artifacts in
PR #1764.

The review compared the new record with the live QuickGO `GO:0062155`
cellular-component term, its `GO:0032991` ancestor, the QuickGO
`GO:0098777` type VIII secretion process term, the NCBI metadata for the GO
definition paper PMID:25219853 / DOI:10.1038/nature13768, and adjacent
secretion-system records.

## Findings

### #1765: Resolved curli TODO still overstates the CsgE/F/G boundary

Severity: medium

PR #1764 correctly adds `GO:0062155` as a standalone secretion-system record and
keeps an open `csg_efg_component_boundary` TODO because the first pass verified
the GO term as a curli secretion channel but did not settle whether constituent
rows should model only CsgG or the broader CsgE/CsgF/CsgG machinery.

The resolved `curli_secretion_complex_boundary` discussion in the existing
`GO:0098774` curli record still says that GO has an exact curli secretion
complex term "for the CsgEFG machinery." That stale wording is stronger than
the verified GO definition and contradicts the new open component-boundary TODO.
The fix should keep the discussion resolved but soften the rationale so it only
claims that GO has an exact curli secretion complex term and that the Csg
secretion machinery is outside the extracellular amyloid-fiber boundary.

## Non-Findings

- The PR file list on GitHub matched the expected semantic records, history
  records, and generated artifact changes.
- `GO:0062155` is an exact cellular-component identifier for the new record.
- `GO:0062155` is current, unrestricted, and has `GO:0032991` as an ancestor.
- Hidden/ignored-inclusive duplicate searches found no pre-existing exact
  `GO:0062155` or `curli secretion complex` record.
- The first record leaves CsgE/F/G constituents out and tracks the component
  boundary explicitly rather than guessing family-level grounding.
- The existing `GO:0098774` curli appendage boundary remains separate from the
  secretion system that exports curli subunits.
