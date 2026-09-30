# YAML record review: cleavage apparatus septin structure

- PR: #1827
- Record: `data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml`
- Review timestamp: 20260930T135153Z

## Finding 1: type the septin cytoskeleton node as a structure

`causal_graphs[0].nodes#septin_cytoskeleton` is grounded to `GO:0032156`
septin cytoskeleton but typed as `CELLULAR_LOCALIZATION`. The graph uses an
`is part of` edge from the `GO:0032161` cleavage apparatus septin structure to
that node, and `GO:0032156` is a cellular-component structure, not a site label.
The node should be `STRUCTURE` to match its grounding and edge semantics.

## Scope reviewed

- Confirmed the new `GO:0032161` identifier and label are not duplicated under
  `data/structures`, including hidden and ignored paths.
- Rechecked the OLS definition, direct `GO:0110165` parent, direct `part_of`
  edges to `GO:0005938`, `GO:0032153`, and `GO:0032156`, and direct child
  terms used for boundary evidence.
- Reviewed component grounding, topology graph nodes and edges, the resolved
  child-term boundary discussion, and the open septin-associated-protein TODO.
