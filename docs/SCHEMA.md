# Schema guide

`src/cellstructuremech/schema/cellstructuremech.yaml` defines
**CellStructureRecord**, the single tree root. One YAML per record.

| Section | Class | What it holds |
|---|---|---|
| Identity | — | `identifier`, `label`, `definition`, `definition_source`, `synonyms`, `xrefs`, `structure_category` (filesystem bucket), `structure_kind` (what sort of physical thing) |
| Mereology | — | `parent_structures` (is-a), `part_of`, `has_part` — CURIEs of other records or GO terms |
| Composition | `StructuralComponent` | Proteins, complexes, RNAs, lipids, polysaccharides; grounding, stoichiometry, essentiality, role, `protein_examples` (`ProteinExample`) |
| Distribution | `TaxonomicScope` | Clade + `presence` (UNIVERSAL / COMMON / VARIABLE / RARE / ABSENT) |
| Exemplars | `CanonicalExample` | Reference organisms with citations |
| Function | `StructureFunction` | GO BP / MF with required evidence |
| Trait hand-off | `TraitLink` | TraitMech / METPO CURIE + relation (CONFERS, REQUIRED_FOR, DIAGNOSTIC_FOR, MODULATES, ASSOCIATED_WITH) |
| Measurements | `PhysicalProperty` | Dimension / count / mass with UO unit and citation |
| Mechanism | `CausalGraph` / `CausalNode` / `CausalEdge` | Same shape as TraitMech; `graph_kind`, `STRUCTURE` node type, `component_ref` |
| Discourse | `Discussion`, `Dataset` | From the vendored `mech_shared` module |
| Lifecycle | `CurationEvent` | `mapping_status` + append-only `curation_history` |

`mech_shared.yaml` is vendored byte-identically across the Mech repos and
sha-pinned by `tests/test_schema.py`. Do not edit it here.

Regenerate Pydantic classes with `just gen-schema` (output is git-ignored).
