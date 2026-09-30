# YAML record review: septin filament array

- PR: #1825
- Record: `data/structures/cytoskeleton/septin_filament_array.yaml`
- Review timestamp: 20260930T131035Z

## Finding 1: remove unread PMID evidence

The record cites `PMID:16151244` in `canonical_examples`, top-level `evidence`,
and the history details, but this curation pass verified that PMID only as a GO
definition xref exposed by OLS. The GO term itself directly supports the
prospore- and chlamydospore-membrane example contexts, so the record should
cite `GO:0032160` for those claims unless the paper text is opened and reviewed.

## Scope reviewed

- Compared the new `GO:0032160` identity against hidden/ignored-inclusive
  `data/structures` searches for the GO CURIE and obvious labels.
- Rechecked the OLS definition, direct `GO:0032156` parent, direct
  `GO:0005856` `part_of` edge, and child terms `GO:0032165` and `GO:0032166`.
- Reviewed component grounding, taxon examples, graph nodes and edges,
  resolved boundary discussion, and open component-grounding TODO.
