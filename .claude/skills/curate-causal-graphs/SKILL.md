---
name: curate-causal-graphs
description: Review and update CellStructureMech assembly and function causal graphs
  with source-backed components, roles and directed edges.
---

# CellStructureMech causal graphs

Read [curation](../../../docs/CURATION.md),
[the schema](../../../src/cellstructuremech/schema/cellstructuremech.yaml), and
[add-cell-structure](../add-cell-structure/SKILL.md) for the native graph contract.
Inventory `data/structures/**/*.yaml`, including all assembly/function graphs and
component references. A structure is not a single protein or a phenotype.

Review supported assembly/function paths, node identity, graph scope, component
membership and every directed edge. Keep source-specific stoichiometry, taxon,
experimental condition and physical composition separate from mechanism claims.
Use [uniprot-protein-examples](../uniprot-protein-examples/SKILL.md) for protein
instances: member nodes use `component_ref` and component examples; external
actors follow the documented xref route. Never make an external chaperone a
structural member just to give a graph node an example.

Apply narrow changes via
`cellstructuremech.curate.curation_event.record_curation_event` and
`cellstructuremech.validation.write_validated.write_validated_structure`, plus
append-only `just new-history`. Run `just validate-strict <record-path>`,
`just validate-history`, `just validate-products`, `just check-trait-links --check`,
`just render`, `just docs-stats`, evidence checks and `just qc` as applicable.
The native review profile has an issue-only persistence gate; preserve honest
coverage accounting for clean targets without inventing findings to save reports.
## Scope and completion

For one target, read the whole maintained record and its generated projection or
components. For a corpus goal, first freeze an inventory of record IDs, paths,
input hashes and applicable graph/protein elements; resume that ledger after an
interruption. Include hidden and ignored inputs when establishing absence.
Classify each target as checked, changed, evidence-limited, excluded, not
applicable or blocked, with reasons and inspected sources. A sample, a provider
report and a validator pass do not establish whole-corpus scientific completion.

Use [curate-yaml-record](../curate-yaml-record/SKILL.md) for the local evidence,
write, history and status contract; this adapter does not replace its managed
method. Record actual agent identity. Preserve scientific status rules and
unrelated edits. Use inspected primary evidence for mechanistic claims and exact
active identifiers for instances; never infer causality from association or
coverage from an empty query. A quotation is source text; interpretation belongs
in the native notes/explanation field.

Save final scientific assessments through
[review-yaml-record](../review-yaml-record/SKILL.md),
[record reviews](../../../docs/record-reviews.md), and the
[local profile](../../../docs/record-review-profile.md), including their native
persistence exceptions. Keep coverage/checkpoint accounting even when a clean
review should not produce a bundle. Unavailable prerequisites remain blocked;
a skipped target is not a completed enrichment. This skill authorizes no paid
provider call by itself.

After a completed goal, follow the user's authorized commit, push/PR,
adversarial review, issue/fix, merge and branch-cleanup sequence under the current
repository guidance. Carry forward existing authorization without asking again.
Use fresh required checks and native merge-queue rules. Verify actual merge and
landed content before deleting that feature branch or starting the next goal.
Only genuine review findings become issues; a no-diff goal needs a documented
no-op receipt rather than an artificial commit.
