# YAML Record Review: type_v_protein_secretion_system_complex

- PR: #1760
- Issue: #1761
- Record: `data/structures/secretion_system/type_v_protein_secretion_system_complex.yaml`
- Reviewed at: 2026-09-29T04:22:29Z
- Result: changes requested

## Scope

Adversarial review of the new `GO:0098046` type V protein secretion system
complex record, its append-only history entry, and regenerated CellStructureMech
pages, docs, and embedding artifacts in PR #1760.

The review compared the new record with the GO `GO:0098046` cellular-component
definition, the two PubMed references that cross-reference that GO definition,
and the deliberately open subtype-boundary TODOs that defer T5SS component and
process curation.

## Findings

### #1761: Component-boundary TODO overclaims later T5SS subtype scope

Severity: medium

The new `t5ss_subtype_component_boundary` discussion asks future curation to
resolve components for type Va autotransporters, type Vb two-partner systems,
trimeric autotransporters, and "later type V subfamilies" before adding
constituents to the generic `GO:0098046` record.

The record evidence only cites `GO:0098046`, PMID:15119822, and PMID:15590781.
That 2004 GO/literature envelope supports the Va/Vb/Vc boundary named in the GO
definition: autotransporters, two-partner secretion systems, and the Oca/type Vc
family. It does not support Vd/Ve/Vf or other later T5SS subfamilies. The TODO
should therefore name the supported type Vc/Oca trimeric-autotransporter scope
and avoid later-subfamily expansion unless modern evidence is added.

## Non-Findings

- The PR file list on GitHub matched the expected 14-file local change set.
- `GO:0098046` is an exact cellular-component identifier for the new generic
  record.
- The record deliberately omits components until subtype-specific Va/Vb/Vc
  family boundaries can be resolved.
- The record deliberately omits a function until the fit between broad
  `GO:0046819` type V secretion and the GO cellular-component scope is
  reviewed.
