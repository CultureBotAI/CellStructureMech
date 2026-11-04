# Cycle 2 Stage 5 — Issue Map and Grouped Finding Dispositions

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision:** Cycle `2`, Stage `5`, Revision `1`
- **Input Review Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000002/stage-04/revision-0001/evidence.yaml` (`sha256: d82e8d95fbabf37450deff6a3de9169f52b4e6b6af66536d101b5abf3673f945`, frozen at `af168704d9999acd544d1f9434c0e87e3fec349f`)
- **Remediation Commit:** `99e590eb7afb0e8251f6e81183e59ca1119987b9`
- **Post-Remediation Structured Review Bundle:** `reviews/structured/20261024T004000Z-c2-stage5-remediation-verification/review.yaml` (`verdict: pass`, `findings: []`)

## Open-Issue Deduplication Against `CultureBotAI/CellStructureMech`

Before creating issues, all open GitHub issues (`#2417`, `#2137`, `#2027`, `#2023`, `#2020`, `#1977`, `#1975`, `#1932`, `#1931`, `#1930`, `#1841`, `#1652`, `#1651`, `#1650`, `#1649`, `#1648`, `#1647`, `#1646`, `#1644`, `#1643`, `#1642`, `#1641`) were checked. None overlapped the 7 Cycle 2 Stage 4 record-level findings (`#2417` tracks the Stage 4 infrastructure task `cellstructuremech-infra-0005` for Stage 6). Three grouped GitHub issues (`#2419`, `#2420`, `#2421`) were created and closed upon verification.

## Grouped Issue Table

| Group ID | GitHub Issue | Findings Covered | Unique Records Modified | Status | Resolution Commit |
| --- | --- | --- | ---: | --- | --- |
| `causal-node-subcomplex-structure-typing` | [#2419](https://github.com/CultureBotAI/CellStructureMech/issues/2419) | `clathrin-coat-ap2-adaptor-causal-node-type`, `membrane-organelle-subcomplex-causal-node-types` | 5 | `resolved` (`closed`) | `99e590eb7afb0e8251f6e81183e59ca1119987b9` |
| `subcomplex-component-type-protein-complex` | [#2420](https://github.com/CultureBotAI/CellStructureMech/issues/2420) | `cytoskeleton-subcomplex-component-types`, `photosystem-reaction-center-core-component-types` | 8 | `resolved` (`closed`) | `99e590eb7afb0e8251f6e81183e59ca1119987b9` |
| `component-gene-symbols-protein-examples-sync` | [#2421](https://github.com/CultureBotAI/CellStructureMech/issues/2421) | `appendage-bacterial-flagellum-gene-symbol-mismatch`, `cytoskeleton-fission-yeast-nda2-gene-symbol-omission`, `carboxysome-bmc-h-paralogue-gene-symbols` | 6 | `resolved` (`closed`) | `99e590eb7afb0e8251f6e81183e59ca1119987b9` |

## Finding-by-Finding Disposition Table

| Finding ID | Source Review Bundle | Group ID | GitHub Issue | Disposition | Verification Bundle |
| --- | --- | --- | --- | --- | --- |
| `clathrin-coat-ap2-adaptor-causal-node-type` | `20261023T230501Z-clathrin-coat-ap2-causal-node-type` (`F1`) | `causal-node-subcomplex-structure-typing` | [#2419](https://github.com/CultureBotAI/CellStructureMech/issues/2419) | `resolved` — `ap2_adaptor_complex` (`GO:0030122`) changed to `node_type: STRUCTURE` in `clathrin_coat_of_endocytic_vesicle.yaml`. | `20261024T004000Z-c2-stage5-remediation-verification` |
| `membrane-organelle-subcomplex-causal-node-types` | `20261023T230505Z-membrane-organelle-category-review` (`F1`) | `causal-node-subcomplex-structure-typing` | [#2419](https://github.com/CultureBotAI/CellStructureMech/issues/2419) | `resolved` — `csma_baseplate` (`cellstructuremech:chlorosome_baseplate_antenna_complex`), `micos_complex` (`GO:0061617`), and `tom_complex` (`GO:0005742`) changed to `node_type: STRUCTURE` across 4 `membrane_organelle/` records. | `20261024T004000Z-c2-stage5-remediation-verification` |
| `cytoskeleton-subcomplex-component-types` | `20261023T230503Z-cytoskeleton-category-review` (`F1`) | `subcomplex-component-type-protein-complex` | [#2420](https://github.com/CultureBotAI/CellStructureMech/issues/2420) | `resolved` — 8 heterodimeric/multiprotein subcomplex components across 7 `cytoskeleton/` records changed to `component_type: PROTEIN_COMPLEX`. | `20261024T004000Z-c2-stage5-remediation-verification` |
| `photosystem-reaction-center-core-component-types` | `20261023T230504Z-energy-complex-category-review` (`F1`) | `subcomplex-component-type-protein-complex` | [#2420](https://github.com/CultureBotAI/CellStructureMech/issues/2420) | `resolved` — `type_i_reaction_center_core` and `type_ii_reaction_center_core` in `photosystem.yaml` changed to `component_type: PROTEIN_COMPLEX`. | `20261024T004000Z-c2-stage5-remediation-verification` |
| `appendage-bacterial-flagellum-gene-symbol-mismatch` | `20261023T230502Z-appendage-category-review` (`F1`) | `component-gene-symbols-protein-examples-sync` | [#2421](https://github.com/CultureBotAI/CellStructureMech/issues/2421) | `resolved` — added `hag` to `components#flagellin.gene_symbols` and `fliY` to `components#c_ring.gene_symbols` in `bacterial_type_flagellum.yaml`. | `20261024T004000Z-c2-stage5-remediation-verification` |
| `cytoskeleton-fission-yeast-nda2-gene-symbol-omission` | `20261023T230503Z-cytoskeleton-category-review` (`F2`) | `component-gene-symbols-protein-examples-sync` | [#2421](https://github.com/CultureBotAI/CellStructureMech/issues/2421) | `resolved` — added `nda2` to `components#alpha_tubulin.gene_symbols` across `aster.yaml`, `astral_microtubule.yaml`, `horsetail_astral_microtubule_array.yaml`, and `post_anaphase_microtubule_array.yaml`. | `20261024T004000Z-c2-stage5-remediation-verification` |
| `carboxysome-bmc-h-paralogue-gene-symbols` | `20261023T230506Z-microcompartment-category-review` (`F1`) | `component-gene-symbols-protein-examples-sync` | [#2421](https://github.com/CultureBotAI/CellStructureMech/issues/2421) | `resolved` — added `ccmK3` and `ccmK4` to `components#bmc_h.gene_symbols` in `carboxysome.yaml`. | `20261024T004000Z-c2-stage5-remediation-verification` |

## Unresolved Blockers / Carry-Forward Findings

- **Carry-Forward Findings (`carry_forward_ids`):** `[]` (0 unresolved findings; all 7 Stage 4 findings resolved).
- **New Infrastructure Tasks (`infra_tasks`):** `[]` (no new Stage 5 writer or representation blockers encountered; Stage 4 infrastructure task `cellstructuremech-infra-0005` / `#2417` remains queued in `INFRA_TASKS.md` for Stage 6).
