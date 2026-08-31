# Schema guide

`src/cellstructuremech/schema/cellstructuremech.yaml` defines
**CellStructureRecord**, the single tree root. One YAML per record.

| Section | Class | What it holds |
|---|---|---|
| Identity | — | `identifier`, `label`, `definition`, `definition_source`, `synonyms`, `xrefs`, `structure_category` (filesystem bucket), `structure_kind` (what sort of physical thing) |
| Mereology | — | `parent_structures` (is-a), `part_of`, `has_part` — CURIEs of other records or GO terms |
| Canonical composition | `StructuralComponent` | Taxon-agnostic proteins, complexes, RNAs, lipids and polysaccharides; grounding, stoichiometry, essentiality, role, `protein_examples` (`ProteinExample`) |
| Source composition | `ComplexComposition` | A taxon-specific complex-database assertion with exact accession, source taxon, participants and copy numbers |
| Distribution | `TaxonomicScope` | Clade + `presence` (UNIVERSAL / COMMON / VARIABLE / RARE / ABSENT) |
| Exemplars | `CanonicalExample` | Reference organisms with citations |
| Function | `StructureFunction` | GO BP / MF with required evidence |
| Trait hand-off | `TraitLink` | TraitMech / METPO CURIE + relation (CONFERS, REQUIRED_FOR, DIAGNOSTIC_FOR, MODULATES, ASSOCIATED_WITH) + evidence for that relation |
| Measurements | `PhysicalProperty` | Dimension / count / mass with UO unit and citation |
| Mechanism | `CausalGraph` / `CausalNode` / `CausalEdge` | Same shape as TraitMech; `graph_kind`, `STRUCTURE` node type, `component_ref` |
| Discourse | `Discussion`, `Dataset` | From the vendored `mech_shared` module |
| Lifecycle | `CurationEvent` | `mapping_status` + append-only `curation_history` |

`mech_shared.yaml` and `history.yaml` are vendored byte-identically from
culturebotai-claw at the commit in `scripts/.vendored_canon_ref`, and compared
against it by `just vendored-check` in the `vendored-sync` workflow. Do not
edit them here — change them in claw and re-sync.

Regenerate Pydantic classes with `just gen-schema` (output is git-ignored).
