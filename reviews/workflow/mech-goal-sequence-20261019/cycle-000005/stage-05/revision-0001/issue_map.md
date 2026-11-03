# Cycle 5 Stage 5 — Issue Map and Grouped Finding Dispositions

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision:** Cycle `5`, Stage `5`, Revision `1`
- **Input Review Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml` (`sha256: 008cce72cea1a120bfef359392a32f3930ae39fa3af2b47ef9f79bda7608df12`, frozen at `a94f6deb809dd50c8344fb03284de9801c0aa298`)
- **Remediation Commit:** `c4a8f347c314b5601cad86c334497d5aca756640`
- **Post-Remediation Structured Review Bundle:** `reviews/structured/20261031T012000Z-c5-stage5-remediation-verification/review.yaml` (`sha256: efa019c67d498b88f74cd562b2e4a940166c9f49dec9116c2ba5bd99f6e05ead`, `verdict: pass`, `findings: []`)

## Open-Issue Deduplication Against `CultureBotAI/CellStructureMech`

Before creating issues, all open GitHub issues (`#2417`, `#2137`, `#2027`, `#2023`, `#2020`, `#1977`, `#1975`, `#1932`, `#1931`, `#1930`, `#1841`, `#1652`, `#1651`, `#1650`, `#1649`, `#1648`, `#1647`, `#1646`, `#1644`, `#1643`, `#1642`, `#1641`) were checked. None overlapped the 6 Cycle 5 Stage 4 record-level findings. Two grouped GitHub issues (`#2475`, `#2476`) were created by root cause and repair ownership across the 10 unique target records.

## Grouped Issue Table

| Group ID | GitHub Issue | Findings Covered | Unique Records Modified | Status | Resolution Commit |
| --- | --- | --- | ---: | --- | --- |
| `spombe-uniprot-gene-symbols-and-strain-taxon-labels` | [#2475](https://github.com/CultureBotAI/CellStructureMech/issues/2475) | `post-anaphase-microtubule-array-emtoc-missing-gene-symbols`, `cytoskeleton-spombe-p04689-primary-gene-symbol-tub1`, `other-eukaryotic-replisome-ncbitaxon-284812-strain-label` | 7 | `resolved` | `c4a8f347c314b5601cad86c334497d5aca756640` |
| `go-grounding-causal-node-type-and-primosome-curation` | [#2476](https://github.com/CultureBotAI/CellStructureMech/issues/2476) | `origin-recognition-complex-node-type-molecular-function`, `autophagosome-macroautophagy-function-missing-go-grounding`, `primosome-complex-dnac-protein-label-and-hierarchy-evidence` | 3 (0 shared with `#2475`) | `resolved` | `c4a8f347c314b5601cad86c334497d5aca756640` |

## Finding-by-Finding Disposition Table

| Finding ID | Source Review Bundle | Group ID | GitHub Issue | Disposition | Verification Bundle |
| --- | --- | --- | --- | --- | --- |
| `post-anaphase-microtubule-array-emtoc-missing-gene-symbols` | `20261030T222001Z-post-anaphase-microtubule-array-emtoc-missing-gene-symbols` (`F1`) | `spombe-uniprot-gene-symbols-and-strain-taxon-labels` | [#2475](https://github.com/CultureBotAI/CellStructureMech/issues/2475) | `resolved` — added `gene_symbols: [mto1, mto2]` on `components[3]` (`component_id: emtoc`, `GO:0000923`, equatorial microtubule organizing center) to match its existing reviewed `protein_examples` `UniProtKB:O94488` (`mto1`) and `UniProtKB:Q9USP7` (`mto2`) in `post_anaphase_microtubule_array.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `cytoskeleton-spombe-p04689-primary-gene-symbol-tub1` | `20261030T222003Z-cytoskeleton-category-review` (`F1`) | `spombe-uniprot-gene-symbols-and-strain-taxon-labels` | [#2475](https://github.com/CultureBotAI/CellStructureMech/issues/2475) | `resolved` — added `tub1` to `components[0].gene_symbols` (`[tub1, atb2]` in `cytoplasmic_microtubule_bundle.yaml` and `quiescent_cell_microtubule_bundle.yaml`; `[tub1, atb2, TUB1, TUB3]` in `static_microtubule_bundle.yaml`), updated `components[0].protein_examples[0].gene_symbol` (`UniProtKB:P04689`) from synonym `atb2` to primary symbol `tub1`, and noted `(also declared as synonym atb2)` in `components[0].protein_examples[0].role`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `other-eukaryotic-replisome-ncbitaxon-284812-strain-label` | `20261030T222005Z-other-category-review` (`F2`) | `spombe-uniprot-gene-symbols-and-strain-taxon-labels` | [#2475](https://github.com/CultureBotAI/CellStructureMech/issues/2475) | `resolved` — updated `taxon_label` from species-level `Schizosaccharomyces pombe` to canonical strain-level `Schizosaccharomyces pombe 972h-` on `components[2]` (`cdc45_protein`) `protein_examples[0]` (`UniProtKB:O74113`, `NCBITaxon:284812`) and on `canonical_examples[0]` (`NCBITaxon:284812`) in `cmg_complex.yaml`, `nuclear_replisome.yaml`, and `replisome.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `origin-recognition-complex-node-type-molecular-function` | `20261030T222002Z-origin-recognition-complex-node-type-molecular-function` (`F1`) | `go-grounding-causal-node-type-and-primosome-curation` | [#2476](https://github.com/CultureBotAI/CellStructureMech/issues/2476) | `resolved` — updated `causal_graphs[0].nodes[8]` (`node_id: dna_replication_origin_binding`, `GO:0003688` `DNA replication origin binding`) from `node_type: BIOLOGICAL_PROCESS` to `node_type: MOLECULAR_FUNCTION` in `origin_recognition_complex.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `autophagosome-macroautophagy-function-missing-go-grounding` | `20261030T222004Z-membrane-organelle-category-review` (`F1`) | `go-grounding-causal-node-type-and-primosome-curation` | [#2476](https://github.com/CultureBotAI/CellStructureMech/issues/2476) | `resolved` — added scalar `grounding: GO:0016236` to `functions[0]` (`macroautophagy`) in `autophagosome.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `primosome-complex-dnac-protein-label-and-hierarchy-evidence` | `20261030T222005Z-other-category-review` (`F1`) | `go-grounding-causal-node-type-and-primosome-curation` | [#2476](https://github.com/CultureBotAI/CellStructureMech/issues/2476) | `resolved` — updated `components[2].protein_examples[0].protein_label` (`UniProtKB:P0AEF0`, `dnaC`) from `DNA replication protein DnaC` to `Replicative helicase loader DnaC` (matching `causal_graphs[0].nodes[1]`) and added top-level `evidence` entries for `GO:0032993` (`parent_structures`) and `GO:0030894` (`part_of`) in `primosome_complex.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |

## Unresolved Blockers / Carry-Forward Findings

- **Carry-Forward Findings (`carry_forward_ids`):** `[]` (0 unresolved findings; all 6 Stage 4 findings resolved).
- **New Infrastructure Tasks (`infra_tasks`):** `[]` (no new Stage 5 writer or representation blockers encountered).
