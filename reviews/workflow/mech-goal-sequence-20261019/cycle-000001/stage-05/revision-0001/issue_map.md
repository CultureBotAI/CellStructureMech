# Cycle 1 Stage 5 Issue Map & Finding Dispositions

## Scope & Frozen Inputs

- **Run ID**: `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision**: Cycle `1`, Stage `5` (`resolve_review_findings`), Revision `1`
- **Scope Frozen At**: `2026-10-23T10:52:00Z`
- **Input Stage 4 Evidence Manifest**: `reviews/workflow/mech-goal-sequence-20261019/cycle-000001/stage-04/revision-0001/evidence.yaml` (SHA256 `e8bddc4fab1e4fec6f1f08b9a6add66e309ea063b53a5098ab2a6c032ad6707f`)
- **Carried-Forward Findings**: 9 open findings across 15 unique `CellStructureRecord` YAML files (16 record-group touches)
- **Fix Commit SHA**: `9dd9935ee1cf1d85454d42df0cec7da12f550a79`
- **Post-Remediation Structured Review Bundle**: `reviews/structured/20261023T114600Z-stage5-remediation-verification/review.yaml` (SHA256 `82cb13bad1f7c75c6de8c4a930c65a4b704a18b8981722e8a28f6b526422cb8e`, verdict `pass`, 0 open findings)

---

## Deduplication Against Open GitHub Issues

Swept the open GitHub issue queue (`gh issue list --repo CultureBotAI/CellStructureMech --state open --limit 100`, 55 open issues prior to Stage 5). None of the 55 existing open issues covered the 9 Stage 4 review findings. Four new grouped GitHub issues (`#2402`–`#2405`) were created by shared root cause and repair ownership.

---

## Issue Group Mapping

| Group ID | GitHub Issue | Finding IDs Covered | Target Records | Status | Fix Commit SHA |
| --- | --- | --- | --- | --- | --- |
| `history-ledger-completeness` | [#2402](https://github.com/CultureBotAI/CellStructureMech/issues/2402) | `woronin-body-missing-history` | `data/structures/membrane_organelle/woronin_body.yaml` | `resolved` | `9dd9935ee1cf1d85454d42df0cec7da12f550a79` |
| `chemoreceptor-array-phosphotransfer-narrative-sync` | [#2403](https://github.com/CultureBotAI/CellStructureMech/issues/2403) | `chemoreceptor-array-stale-unquotable-phosphotransfer-note` | `data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml` | `resolved` | `9dd9935ee1cf1d85454d42df0cec7da12f550a79` |
| `causal-graph-subcomplex-structure-node-typing` | [#2404](https://github.com/CultureBotAI/CellStructureMech/issues/2404) | `cilium-ift-particle-causal-node-type`, `cytoskeleton-go-subcomplex-causal-node-types`, `membrane-organelle-go-subcomplex-causal-node-types` | `cilium.yaml`, `actin_cortical_patch.yaml`, `equatorial_microtubule_organizing_center.yaml`, `interphase_microtubule_organizing_center.yaml`, `radial_spoke.yaml`, `telocentrosome.yaml`, `diazoplast.yaml`, `endoplasmic_reticulum.yaml` | `resolved` | `9dd9935ee1cf1d85454d42df0cec7da12f550a79` |
| `discussion-evidence-structured-issue-links` | [#2405](https://github.com/CultureBotAI/CellStructureMech/issues/2405) | `chemoreceptor-array-discussion-issue-evidence`, `cytoskeleton-discussion-prose-issue-links`, `division-machinery-discussion-prose-issue-links`, `t3ss-complex-discussion-issue-evidence` | `methyl_accepting_chemotaxis_protein_complex.yaml`, `crescentin_filament.yaml`, `mreb_filament.yaml`, `phuz_spindle.yaml`, `divisome_complex.yaml`, `elongasome.yaml`, `type_iii_protein_secretion_system_complex.yaml` | `resolved` | `9dd9935ee1cf1d85454d42df0cec7da12f550a79` |

---

## Per-Finding Dispositions

1. **`woronin-body-missing-history`** (`history-ledger-completeness`, [#2402](https://github.com/CultureBotAI/CellStructureMech/issues/2402))
   - **Status**: `resolved`
   - **Disposition**: Reconstructed `history/records/woronin_body/2026-09-10T103912Z-claude-90b0c5.yaml` and `history/records/woronin_body/2026-09-10T104642Z-claude-d2bf78.yaml` from git commit provenance (`90b0c505` and `d2bf78b0`) and recorded the Stage 5 audit in `history/records/woronin_body/2026-10-23T110200Z-claude-code-787f02.yaml` and `woronin_body.yaml` `curation_history`.

2. **`chemoreceptor-array-stale-unquotable-phosphotransfer-note`** (`chemoreceptor-array-phosphotransfer-narrative-sync`, [#2403](https://github.com/CultureBotAI/CellStructureMech/issues/2403))
   - **Status**: `resolved`
   - **Disposition**: Updated `causal_graphs[0].description` and `causal_graphs[0].edges[5].notes` in `data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml` to remove stale claims that CheA-to-CheY phosphotransfer is unquotable/omitted and instead reference the Stewart 1997 (`DOI:10.1021/bi962261k`) kinetic characterization on `edges[6]`.

3. **`cilium-ift-particle-causal-node-type`** (`causal-graph-subcomplex-structure-node-typing`, [#2404](https://github.com/CultureBotAI/CellStructureMech/issues/2404))
   - **Status**: `resolved`
   - **Disposition**: Updated `causal_graphs[0].nodes[0]` (`ift_particle`) in `data/structures/appendage/cilium.yaml` from `node_type: GENE_OR_PROTEIN` to `node_type: STRUCTURE` with `grounding: {id: GO:0030990, label: intraciliary transport particle}`.

4. **`cytoskeleton-go-subcomplex-causal-node-types`** (`causal-graph-subcomplex-structure-node-typing`, [#2404](https://github.com/CultureBotAI/CellStructureMech/issues/2404))
   - **Status**: `resolved`
   - **Disposition**: Updated 7 subcomplex causal-graph nodes across `actin_cortical_patch.yaml` (`arp2_3_complex`, `GO:0005885`), `equatorial_microtubule_organizing_center.yaml` (`gamma_turc`, `GO:0000930`), `interphase_microtubule_organizing_center.yaml` (`gamma_turc`, `GO:0000930`), `radial_spoke.yaml` (`radial_spoke_head` `GO:0001535`, `radial_spoke_neck` `GO:0120343`, `radial_spoke_stalk` `GO:0001536`), and `telocentrosome.yaml` (`gamma_turc`, `GO:0000930`) to `node_type: STRUCTURE` with canonical GO grounding.

5. **`membrane-organelle-go-subcomplex-causal-node-types`** (`causal-graph-subcomplex-structure-node-typing`, [#2404](https://github.com/CultureBotAI/CellStructureMech/issues/2404))
   - **Status**: `resolved`
   - **Disposition**: Updated `nitrogenase` (`GO:0016610`) in `diazoplast.yaml` and `sec61` (`GO:0005784`) in `endoplasmic_reticulum.yaml` from `node_type: GENE_OR_PROTEIN` to `node_type: STRUCTURE` with canonical GO grounding.

6. **`chemoreceptor-array-discussion-issue-evidence`** (`discussion-evidence-structured-issue-links`, [#2405](https://github.com/CultureBotAI/CellStructureMech/issues/2405))
   - **Status**: `resolved`
   - **Disposition**: Added structured `evidence` entries (`DOI:10.1021/bi962261k` and `https://github.com/CultureBotAI/CellStructureMech/issues/161`) to `discussions[0]` (`phosphotransfer_step_unquotable`) in `data/structures/other/methyl_accepting_chemotaxis_protein_complex.yaml`.

7. **`cytoskeleton-discussion-prose-issue-links`** (`discussion-evidence-structured-issue-links`, [#2405](https://github.com/CultureBotAI/CellStructureMech/issues/2405))
   - **Status**: `resolved`
   - **Disposition**: Added structured GitHub issue URLs to `discussions[0].evidence` in `crescentin_filament.yaml` (`#1260`), `mreb_filament.yaml` (`#119`), and `phuz_spindle.yaml` (`#481`, `#482`).

8. **`division-machinery-discussion-prose-issue-links`** (`discussion-evidence-structured-issue-links`, [#2405](https://github.com/CultureBotAI/CellStructureMech/issues/2405))
   - **Status**: `resolved`
   - **Disposition**: Added structured GitHub issue URLs to `discussions[0].evidence` (`ring_dimensions_unsourced`, `#65`, `#91`) in `divisome_complex.yaml` and to `discussions[0].evidence` (`mreb_diameter_primary_source_needed`, `#119`) and `discussions[1].evidence` (`rodz_mreb_linkage_edge_needs_snippet`, `#161`) in `elongasome.yaml`.

9. **`t3ss-complex-discussion-issue-evidence`** (`discussion-evidence-structured-issue-links`, [#2405](https://github.com/CultureBotAI/CellStructureMech/issues/2405))
   - **Status**: `resolved`
   - **Disposition**: Added structured GitHub issue URLs (`#65`, `#91`) to `discussions[0].evidence` (`needle_dimensions_unsourced`) in `data/structures/secretion_system/type_iii_protein_secretion_system_complex.yaml`.
