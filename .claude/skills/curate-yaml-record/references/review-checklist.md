# CellStructureRecord review checklist

Use this checklist for one microbial cell structure. It is not a requirement
to populate every optional slot or invent a causal graph.

## Evidence standard

- Put evidence on the narrowest component, composition, taxonomic, function,
  image, property, or causal assertion it supports.
- Verify stable IDs and inspect source-native records or source text.
- A protein annotation, predicted structure, or sequence hit does not alone
  establish assembly, localization, function, or taxonomic distribution.
- Snippets are short exact text; interpretation belongs in notes.
- Preserve conflicts and bounded “not found” results as uncertainty.

## Field-by-field audit

| Area | Verify | Complete enough when |
|---|---|---|
| Identity | ID, label, definition/source, category, and kind denote one structure or complex. | Protein, phenotype, broader system, and structure boundaries are explicit. |
| Hierarchy/parthood | Parents are is-a; `part_of` and `has_part` are real mereological relations. | Related structures are not forced into hierarchy or identity. |
| Components | Protein/family identity, role, stoichiometry, evidence, and source version agree. | Membership is distinguished from necessary composition and variable accessory parts. |
| Complex composition | Subcomplexes, counts, assembly context, and organism/condition scope agree. | A model from one species is not silently universalized. |
| Taxonomic distribution | Taxon/strain, presence/absence wording, method, and evidence agree. | Absence is asserted only from evidence capable of detecting the structure. |
| Functions/traits | Function, trait link, direction, organism/context, and evidence agree. | Association is not upgraded to mechanism or exclusivity. |
| Properties/images | Measurement, units, method, figure/repository accession, attribution, and license agree. | Visuals and values are traceable to the exact structure/context. |
| Causal graph | Scope, nodes, edges, direction, and edge-level evidence agree. | Every edge is supported and predictions remain labeled. |
| Discussions/datasets | Each item is relevant, durable, and actionable. | No placeholder or bibliography dump remains. |
| Status/audit | Mapping status and both history surfaces match the review performed. | Agent drafts stay PROPOSED; REVIEWED has human sign-off. |
