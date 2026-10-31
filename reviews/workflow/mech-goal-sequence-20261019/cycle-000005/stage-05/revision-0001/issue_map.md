# Cycle 5 Stage 5 — Issue Map and Grouped Finding Dispositions

- **Run ID:** `mech-goal-sequence-20261019`
- **Cycle / Stage / Revision:** Cycle `5`, Stage `5`, Revision `1`
- **Input Review Evidence:** `reviews/workflow/mech-goal-sequence-20261019/cycle-000005/stage-04/revision-0001/evidence.yaml` (`sha256: 008cce72cea1a120bfef359392a32f3930ae39fa3af2b47ef9f79bda7608df12`, frozen at `3fe670a67bd524b24acaa8b9158a82cf22974df4`)
- **Remediation Commit:** `c4a8f347c314b5601cad86c334497d5aca756640`
- **Post-Remediation Structured Review Bundle:** `reviews/structured/20261031T012000Z-c5-stage5-remediation-verification/review.yaml` (`sha256: 7058ca363b7d34269f3bd0993273db04445ed3369109a6cbe1d312d90dc04de9`, `verdict: pass`, `findings: []`)

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
| `post-anaphase-microtubule-array-emtoc-missing-gene-symbols` | `20261031T003001Z-post-anaphase-microtubule-array-emtoc-gene-symbols` (`F1`) | `spombe-uniprot-gene-symbols-and-strain-taxon-labels` | [#2475](https://github.com/CultureBotAI/CellStructureMech/issues/2475) | `resolved` — populated `gene_symbol: mto1` on `components[1].protein_examples[0]` (`UniProtKB:Q9P7F4`) and `causal_graphs[0].elements[0]` (`mto1_mto2`), and `gene_symbol: mto2` on `components[1].protein_examples[1]` (`UniProtKB:O94709`) in `post_anaphase_microtubule_array.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `cytoskeleton-spombe-p04689-primary-gene-symbol-tub1` | `20261031T003003Z-cytoskeleton-category-review` (`F1`) | `spombe-uniprot-gene-symbols-and-strain-taxon-labels` | [#2475](https://github.com/CultureBotAI/CellStructureMech/issues/2475) | `resolved` — updated `gene_symbol` from synonym `nda2` to UniProtKB primary gene name `tub1` on all `UniProtKB:P04689` `protein_examples` and `causal_graphs` elements in `cytoplasmic_microtubule_bundle.yaml`, `quiescent_cell_microtubule_bundle.yaml`, and `static_microtubule_bundle.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `other-eukaryotic-replisome-ncbitaxon-284812-strain-label` | `20261031T003005Z-other-category-review` (`F1`) | `spombe-uniprot-gene-symbols-and-strain-taxon-labels` | [#2475](https://github.com/CultureBotAI/CellStructureMech/issues/2475) | `resolved` — updated `organism.label` from species-level `Schizosaccharomyces pombe` to canonical strain-level `Schizosaccharomyces pombe 972h-` on all `NCBITaxon:284812` `protein_examples` in `cmg_complex.yaml`, `nuclear_replisome.yaml`, and `replisome.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `origin-recognition-complex-node-type-molecular-function` | `20261031T003002Z-origin-recognition-complex-node-type` (`F1`) | `go-grounding-causal-node-type-and-primosome-curation` | [#2476](https://github.com/CultureBotAI/CellStructureMech/issues/2476) | `resolved` — updated `causal_graphs[0].elements[1]` (`node_id: origin_dna_binding`, `GO:0003688` `DNA replication origin binding`) from `node_type: BIOLOGICAL_PROCESS` to `node_type: MOLECULAR_FUNCTION` in `origin_recognition_complex.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `autophagosome-macroautophagy-function-missing-go-grounding` | `20261031T003004Z-membrane-organelle-category-review` (`F1`) | `go-grounding-causal-node-type-and-primosome-curation` | [#2476](https://github.com/CultureBotAI/CellStructureMech/issues/2476) | `resolved` — added `grounding: {id: GO:0016236, label: macroautophagy}` to `functions[0]` (`macroautophagy`) in `autophagosome.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |
| `primosome-complex-dnac-protein-label-and-hierarchy-evidence` | `20261031T003005Z-other-category-review` (`F2`) | `go-grounding-causal-node-type-and-primosome-curation` | [#2476](https://github.com/CultureBotAI/CellStructureMech/issues/2476) | `resolved` — updated `components[2].protein_examples[0].protein.label` (`UniProtKB:P0AEF0`, `dnaC`) from `DNA replication protein DnaC` to UniProt recommended name `DnaC protein` and expanded the top-level `PMID:29024950` evidence note to explicitly cite `GO:0032991` (`protein-containing complex`) alongside `GO:1990077` in `primosome_complex.yaml`. | `20261031T012000Z-c5-stage5-remediation-verification` |

## Unresolved Blockers / Carry-Forward Findings

- **Carry-Forward Findings (`carry_forward_ids`):** `[]` (0 unresolved findings; all 6 Stage 4 findings resolved).
- **New Infrastructure Tasks (`infra_tasks`):** `[]` (no new Stage 5 writer or representation blockers encountered).
