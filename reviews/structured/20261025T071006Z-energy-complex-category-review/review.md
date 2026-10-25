# Category review of data/structures/energy_complex/ (40 records): two-sector ATPase subcomplex types, curation_history graph IDs, and MCR node grounding

- Review: 20261025T071006Z-energy-complex-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-25T06:56:00Z
- Finished UTC: 2026-10-25T07:10:06Z
- Reviewer: antigravity-c3s4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full-coverage category review of all 40 records in data/structures/energy_complex/ (including the 2 new Cycle 3 Stage 1 two-sector ATPase domain records) verified distinct bioenergetic complex boundaries. Two minor cohort findings were identified across 3 records: (F1) in proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml (GO:0033178), heteromeric subcomplexes catalytic_hexamer_head (atpA/atpD/VMA1/VMA2) and central_rotational_stalk (atpG/atpC/VMA8/VMA7) are typed component_type: PROTEIN instead of PROTEIN_COMPLEX, and curation_history[1].changes in both GO:0033178 and sibling GO:0033177 cites stale causal_graph IDs; and (F2) in methyl_coenzyme_m_reductase_complex.yaml (GO:0044674), causal_graphs[0] nodes mcr_alpha_subunit, mcr_beta_subunit, and mcr_gamma_subunit (causal_graphs[0].nodes[1..3]) omit the verified InterPro: grounding declared on their referenced components[] entries.

## Scope And Provenance

Full-cohort review of all 40 CellStructureRecord YAML files under data/structures/energy_complex/.

Selection: Complete folder cohort data/structures/energy_complex/*.yaml in the frozen 993-record Cycle 3 Stage 4 inventory.
Coverage: full; 40 reviewed / 40 in the declared population.
Source: git_commit at Git base 83ec9d5184fb203d87d8c3bd7043792d385193bf.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| cellstructuremech:chlorosome_baseplate_antenna_complex | data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml | maintained | chlorosome baseplate antenna complex |
| cellstructuremech:chromatophore_cytochrome_bc1_complex | data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml | maintained | chromatophore cytochrome bc1 complex |
| GO:0009512 | data/structures/energy_complex/cytochrome_b6f_complex.yaml | maintained | cytochrome b6f complex |
| cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex | data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml | maintained | cytochrome bd-I ubiquinol oxidase complex |
| GO:0009319 | data/structures/energy_complex/cytochrome_o_ubiquinol_oxidase_complex.yaml | maintained | cytochrome o ubiquinol oxidase complex |
| GO:0009390 | data/structures/energy_complex/dimethyl_sulfoxide_reductase_complex.yaml | maintained | dimethyl sulfoxide reductase complex |
| GO:0009326 | data/structures/energy_complex/formate_dehydrogenase_complex.yaml | maintained | formate dehydrogenase complex |
| cellstructuremech:formate_dehydrogenase_n_complex | data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml | maintained | formate dehydrogenase N complex |
| cellstructuremech:formate_hydrogenlyase_complex | data/structures/energy_complex/formate_hydrogenlyase_complex.yaml | maintained | formate hydrogenlyase complex |
| GO:0045283 | data/structures/energy_complex/fumarate_reductase_complex.yaml | maintained | fumarate reductase complex |
| cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex | data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml | maintained | LH2 peripheral light-harvesting antenna complex |
| GO:0030076 | data/structures/energy_complex/light_harvesting_complex.yaml | maintained | light-harvesting complex |
| GO:0044674 | data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml | maintained | methyl coenzyme M reductase complex |
| GO:0044799 | data/structures/energy_complex/narghi_complex.yaml | maintained | NarGHI complex |
| GO:0009325 | data/structures/energy_complex/nitrate_reductase_complex.yaml | maintained | nitrate reductase complex |
| GO:0016610 | data/structures/energy_complex/nitrogenase_complex.yaml | maintained | nitrogenase complex |
| GO:0009521 | data/structures/energy_complex/photosystem.yaml | maintained | photosystem |
| GO:0009522 | data/structures/energy_complex/photosystem_i.yaml | maintained | photosystem I |
| GO:0009523 | data/structures/energy_complex/photosystem_ii.yaml | maintained | photosystem II |
| GO:0030089 | data/structures/energy_complex/phycobilisome.yaml | maintained | phycobilisome |
| cellstructuremech:phycobilisome_core | data/structures/energy_complex/phycobilisome_core.yaml | maintained | phycobilisome core |
| cellstructuremech:phycobilisome_rod | data/structures/energy_complex/phycobilisome_rod.yaml | maintained | phycobilisome rod |
| GO:0030094 | data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml | maintained | plasma membrane-derived photosystem I |
| GO:0030096 | data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml | maintained | plasma membrane-derived thylakoid photosystem II |
| GO:0045259 | data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml | maintained | proton-transporting ATP synthase complex |
| GO:0016469 | data/structures/energy_complex/proton_transporting_two_sector_atpase_complex.yaml | maintained | proton-transporting two-sector ATPase complex |
| GO:0033178 | data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml | maintained | proton-transporting two-sector ATPase complex, catalytic domain |
| GO:0033177 | data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_proton_transporting_domain.yaml | maintained | proton-transporting two-sector ATPase complex, proton-transporting domain |
| GO:0033176 | data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml | maintained | proton-transporting V-type ATPase complex |
| GO:0033179 | data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml | maintained | proton-transporting V-type ATPase, V0 domain |
| GO:0033180 | data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml | maintained | proton-transporting V-type ATPase, V1 domain |
| cellstructuremech:rc_lh1_pufx_core_complex | data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml | maintained | RC-LH1-PufX core complex |
| GO:0045271 | data/structures/energy_complex/respiratory_chain_complex_i.yaml | maintained | respiratory chain complex I |
| GO:0045273 | data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml | maintained | respiratory chain complex II (succinate dehydrogenase) |
| GO:0045275 | data/structures/energy_complex/respiratory_chain_complex_iii.yaml | maintained | respiratory chain complex III |
| GO:0045277 | data/structures/energy_complex/respiratory_chain_complex_iv.yaml | maintained | respiratory chain complex IV |
| GO:0160292 | data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml | maintained | sodium-translocating NADH:quinone reductase complex |
| GO:0016471 | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_complex.yaml | maintained | vacuolar proton-transporting V-type ATPase complex |
| GO:0000220 | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml | maintained | vacuolar proton-transporting V-type ATPase, V0 domain |
| GO:0000221 | data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml | maintained | vacuolar proton-transporting V-type ATPase, V1 domain |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering energy_complex cohort | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex, cellstructuremech:chromatophore_cytochrome_bc1_complex, GO:0009512, cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex, GO:0009319, GO:0009390, GO:0009326, cellstructuremech:formate_dehydrogenase_n_complex, cellstructuremech:formate_hydrogenlyase_complex, GO:0045283, cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex, GO:0030076, GO:0044674, GO:0044799, GO:0009325, GO:0016610, GO:0009521, GO:0009522, GO:0009523, GO:0030089, cellstructuremech:phycobilisome_core, cellstructuremech:phycobilisome_rod, GO:0030094, GO:0030096, GO:0045259, GO:0016469, GO:0033178, GO:0033177, GO:0033176, GO:0033179, GO:0033180, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0045275, GO:0045277, GO:0160292, GO:0016471, GO:0000220, GO:0000221 | All 40 energy_complex records pass strict LinkML and semantic validation. |
| ID-label correspondence across energy_complex cohort | passed | True | cellstructuremech:chlorosome_baseplate_antenna_complex, cellstructuremech:chromatophore_cytochrome_bc1_complex, GO:0009512, cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex, GO:0009319, GO:0009390, GO:0009326, cellstructuremech:formate_dehydrogenase_n_complex, cellstructuremech:formate_hydrogenlyase_complex, GO:0045283, cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex, GO:0030076, GO:0044674, GO:0044799, GO:0009325, GO:0016610, GO:0009521, GO:0009522, GO:0009523, GO:0030089, cellstructuremech:phycobilisome_core, cellstructuremech:phycobilisome_rod, GO:0030094, GO:0030096, GO:0045259, GO:0016469, GO:0033178, GO:0033177, GO:0033176, GO:0033179, GO:0033180, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0045275, GO:0045277, GO:0160292, GO:0016471, GO:0000220, GO:0000221 | All ontology ID-label pairs in energy_complex records correspond to canonical labels. |

## Scientific And Domain Assessments

### Identity, boundaries, causal graphs, and ontology grounding across data/structures/energy_complex/

scope: supported. Targets: cellstructuremech:chlorosome_baseplate_antenna_complex, cellstructuremech:chromatophore_cytochrome_bc1_complex, GO:0009512, cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex, GO:0009319, GO:0009390, GO:0009326, cellstructuremech:formate_dehydrogenase_n_complex, cellstructuremech:formate_hydrogenlyase_complex, GO:0045283, cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex, GO:0030076, GO:0044674, GO:0044799, GO:0009325, GO:0016610, GO:0009521, GO:0009522, GO:0009523, GO:0030089, cellstructuremech:phycobilisome_core, cellstructuremech:phycobilisome_rod, GO:0030094, GO:0030096, GO:0045259, GO:0016469, GO:0033178, GO:0033177, GO:0033176, GO:0033179, GO:0033180, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0045275, GO:0045277, GO:0160292, GO:0016471, GO:0000220, GO:0000221.

All 40 records in data/structures/energy_complex/ represent distinct microbial cell structures or subcomplexes with valid hierarchy links and verified UniProtKB protein examples.

### Subcomplex component_type and curation_history causal_graph IDs in two-sector ATPase domain records

consistency: concern. Targets: GO:0033178, GO:0033177.

GO:0033178 types heteromeric subcomplexes catalytic_hexamer_head and central_rotational_stalk as PROTEIN, and GO:0033178 and GO:0033177 cite stale graph_ids in curation_history[1].changes.

### Causal-graph component_ref grounding propagation in methyl_coenzyme_m_reductase_complex.yaml

graph: concern. Targets: GO:0044674.

Three component_ref causal_graphs nodes in methyl_coenzyme_m_reductase_complex.yaml omit verified InterPro: groundings from components[].

## Findings

### F1: Two-sector ATPase domain records type heteromeric F1/V1 subcomplexes as PROTEIN and cite mismatched causal_graph IDs in curation_history[1].changes

minor / open / confirmed; issue key: energy-complex-atpase-subcomplex-types-and-history-graph-ids.

In data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml (GO:0033178), heteromeric multiprotein subcomplex components catalytic_hexamer_head (atpA/atpD/VMA1/VMA2, alpha3-beta3 hexamer) and central_rotational_stalk (atpG/atpC/VMA8/VMA7, gamma-epsilon / D-F stalk) are typed component_type: PROTEIN instead of PROTEIN_COMPLEX, and curation_history[1].changes cites graph_id 'catalytic_sector_rotary_catalysis' instead of causal_graphs[0].graph_id 'catalytic_domain_rotary_mechanism'. In sibling proton_transporting_two_sector_atpase_complex_proton_transporting_domain.yaml (GO:0033177), curation_history[1].changes cites graph_id 'proton_sector_rotary_conduction' instead of causal_graphs[0].graph_id 'proton_transporting_domain_mechanism'.

### F2: methyl_coenzyme_m_reductase_complex.yaml causal_graphs[0] subunit nodes omit verified InterPro: groundings from components[]

minor / open / confirmed; issue key: energy-complex-mcr-causal-node-component-ref-grounding.

In data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml (GO:0044674), causal_graphs[0] nodes mcr_alpha_subunit (nodes[1]), mcr_beta_subunit (nodes[2]), and mcr_gamma_subunit (nodes[3]) reference components[0..2] via component_ref but omit their verified InterPro: groundings (InterPro:IPR016212, InterPro:IPR003179, InterPro:IPR003178).

## Recommended Actions And Acceptance Checks

### A1

Update catalytic_hexamer_head and central_rotational_stalk in GO:0033178 to component_type: PROTEIN_COMPLEX, align curation_history[1].changes in GO:0033178 and GO:0033177 to their actual causal_graphs[0].graph_id values, and record the updates in history/records/.

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

### A2

Propagate InterPro:IPR016212, InterPro:IPR003179, and InterPro:IPR003178 to causal_graphs[0].nodes[1..3] in methyl_coenzyme_m_reductase_complex.yaml and record the update in history/records/methyl_coenzyme_m_reductase_complex/.

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

## Category Boundaries

- retain: cellstructuremech:chlorosome_baseplate_antenna_complex, cellstructuremech:chromatophore_cytochrome_bc1_complex, GO:0009512, cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex, GO:0009319, GO:0009390, GO:0009326, cellstructuremech:formate_dehydrogenase_n_complex, cellstructuremech:formate_hydrogenlyase_complex, GO:0045283, cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex, GO:0030076, GO:0044674, GO:0044799, GO:0009325, GO:0016610, GO:0009521, GO:0009522, GO:0009523, GO:0030089, cellstructuremech:phycobilisome_core, cellstructuremech:phycobilisome_rod, GO:0030094, GO:0030096, GO:0045259, GO:0016469, GO:0033178, GO:0033177, GO:0033176, GO:0033179, GO:0033180, cellstructuremech:rc_lh1_pufx_core_complex, GO:0045271, GO:0045273, GO:0045275, GO:0045277, GO:0160292, GO:0016471, GO:0000220, GO:0000221. All 40 records in data/structures/energy_complex/ represent distinct respiratory, photosynthetic, methanogenic, or rotary ATPase complexes and subcomplexes.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_energycomplex | scripts/validate_strict.py; strict receipt | supports | validate_strict.py exited 0 across all 993 records including all 40 energy_complex records. |
| ev_labels_energycomplex | scripts/validate_id_label_correspondence.py; labels receipt | supports | validate_id_label_correspondence.py exited 0 across all ontology targets. |
| ev_ec_atpase_subcomplex_and_history | data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml; components[0..1] (lines 16-66) and curation_history[1].changes (lines 259-264) in GO:0033178 and curation_history[1].changes (lines 255-260) in GO:0033177 | supports | GO:0033178 types heteromeric subcomplexes catalytic_hexamer_head and central_rotational_stalk as PROTEIN instead of PROTEIN_COMPLEX, and both GO:0033178 and GO:0033177 cite mismatched graph_ids in curation_history[1].changes. |
| ev_ec_mcr_grounding | data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml; components[0..2] vs causal_graphs[0].nodes[1..3] (lines 226-240) | supports | methyl_coenzyme_m_reductase_complex.yaml causal_graphs[0] nodes mcr_alpha_subunit, mcr_beta_subunit, and mcr_gamma_subunit omit InterPro:IPR016212, InterPro:IPR003179, and InterPro:IPR003178. |

## Limits And Additional Notes

- Record edits for energy_complex cohort findings are queued for Cycle 3 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261025T071006Z-energy-complex-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: 'Category review of data/structures/energy_complex/ (40 records): two-sector
  ATPase subcomplex types, curation_history graph IDs, and MCR node grounding'
started_at: '2026-10-25T06:56:00Z'
finished_at: '2026-10-25T07:10:06Z'
reviewer:
  identity: antigravity-c3s4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 3 Stage 4 record_review against committed
    git revision 83ec9d5184fb203d87d8c3bd7043792d385193bf without record edits in
    this stage.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: PASS_WITH_FOLLOW_UP
scientific_review: true
summary: 'Full-coverage category review of all 40 records in data/structures/energy_complex/
  (including the 2 new Cycle 3 Stage 1 two-sector ATPase domain records) verified
  distinct bioenergetic complex boundaries. Two minor cohort findings were identified
  across 3 records: (F1) in proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml
  (GO:0033178), heteromeric subcomplexes catalytic_hexamer_head (atpA/atpD/VMA1/VMA2)
  and central_rotational_stalk (atpG/atpC/VMA8/VMA7) are typed component_type: PROTEIN
  instead of PROTEIN_COMPLEX, and curation_history[1].changes in both GO:0033178 and
  sibling GO:0033177 cites stale causal_graph IDs; and (F2) in methyl_coenzyme_m_reductase_complex.yaml
  (GO:0044674), causal_graphs[0] nodes mcr_alpha_subunit, mcr_beta_subunit, and mcr_gamma_subunit
  (causal_graphs[0].nodes[1..3]) omit the verified InterPro: grounding declared on
  their referenced components[] entries.'
source:
  git_revision: 83ec9d5184fb203d87d8c3bd7043792d385193bf
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 7a7ae411cf451ee7e634dfc65b6a466e5c52206e5d9111f090d3704832ddceae
    role: context
  - path: CLAUDE.md
    sha256: c587a437d59a8babb39169ebc7250982c73d5a23a88d6f5bb15104624ddf33f6
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    sha256: 7ea00dedcd0998fc477737d6d2e8301e4e57a08e57378d19efe5e32a6ea8c92d
    role: target
  - path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    sha256: 7f6582722d2f5376262287856929ec073f8550493eee88c6cb92dfc7624ec7ed
    role: target
  - path: data/structures/energy_complex/cytochrome_b6f_complex.yaml
    sha256: 6d228ab890a3a8f8f67e756ac5343896db16bc57dfc55d8250d2afd87851f7c3
    role: target
  - path: data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
    sha256: 1a71d5c7e8f417d2e943dfea2657d5be85bebad9786cccc4fee4fa39fa66f825
    role: target
  - path: data/structures/energy_complex/cytochrome_o_ubiquinol_oxidase_complex.yaml
    sha256: 0afaecc355f783a9a89789e5b765680d3bb22aa0617c80eaf6b279d3096e6bc7
    role: target
  - path: data/structures/energy_complex/dimethyl_sulfoxide_reductase_complex.yaml
    sha256: 2422ae4303bcaafc3a0c60fa5bb3ac71cde37b650a4352868c91e32437c6308d
    role: target
  - path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    sha256: 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e
    role: target
  - path: data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    sha256: ef7276f6532db0b7be7eac0564d02687a9661839dd9181aa89374ff24a6afe62
    role: target
  - path: data/structures/energy_complex/formate_hydrogenlyase_complex.yaml
    sha256: 2fc61b025a3a5b49936cb08e6e58ae7a6aba385f953b1535e5ba27859602a99b
    role: target
  - path: data/structures/energy_complex/fumarate_reductase_complex.yaml
    sha256: e823d8ddaac1348ad816503190e4a0c020e4b115c80831dcc6383e44346c7c6f
    role: target
  - path: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
    sha256: 4bb84c48c2bb27f1a8dded06f479771b494070977ef26e0b14f0708bc446a7ce
    role: target
  - path: data/structures/energy_complex/light_harvesting_complex.yaml
    sha256: 4454f3c667f5536bb3c39e9be2ef6aee5cb38e9842dda50f55e19ddf79bb2bdd
    role: target
  - path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    sha256: ef43ab9df3e0a3d8ed86e0347c9801db59ced9efd1d0313f8ab2a9b3b1420338
    role: target
  - path: data/structures/energy_complex/narghi_complex.yaml
    sha256: 3820651a5a9e3aed9a74bb663caa00f4e428c344d0bfc432ab343f171f30aabb
    role: target
  - path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    sha256: ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459
    role: target
  - path: data/structures/energy_complex/nitrogenase_complex.yaml
    sha256: 530365fc81d15c00b907873712c418eb8b4dd14e7e0ce2cca4f6796862186026
    role: target
  - path: data/structures/energy_complex/photosystem.yaml
    sha256: c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8
    role: target
  - path: data/structures/energy_complex/photosystem_i.yaml
    sha256: fc0a444867219721d503382db2682e2146969c65bbc777c8bf86581f6524ef0e
    role: target
  - path: data/structures/energy_complex/photosystem_ii.yaml
    sha256: fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16
    role: target
  - path: data/structures/energy_complex/phycobilisome.yaml
    sha256: b05c823a9d1bea4fb41a69a9ab7361be702d0b0d0a60f6536c73eb08c0ec9b40
    role: target
  - path: data/structures/energy_complex/phycobilisome_core.yaml
    sha256: 34cca2a846f5b2b84b95c6c2db929370814b4e2898eee052f3e2cbfecafde554
    role: target
  - path: data/structures/energy_complex/phycobilisome_rod.yaml
    sha256: f610a707b8f8fea3edfd28574b996a315eaf1e2d245de7efce9edf96b49943d1
    role: target
  - path: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
    sha256: 8fec8764bc49e21960bbfc6d95eb30247aab5158ef852d45ad4d7cec2aa9eff6
    role: target
  - path: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
    sha256: 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef
    role: target
  - path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    sha256: ab93b5ffa055615dfc9de1edfb137773e1098b4f7e9eefdda9d0ea00961af4fb
    role: target
  - path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex.yaml
    sha256: 4a1a6f78af3ec95c4ce56ab37996344566f78a38a95263d34ba386cd681ca26a
    role: target
  - path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml
    sha256: ffe0962a1a4efb660e02c185cce1f37ded89481634a7f12f217863e6ab7569e1
    role: target
  - path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_proton_transporting_domain.yaml
    sha256: 73fcc564b341e9dbeaa5634126d6b1a25dc8ac6a0a5193c626fc0485d463b6b8
    role: target
  - path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    sha256: 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4
    role: target
  - path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    sha256: f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c
    role: target
  - path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    sha256: a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300
    role: target
  - path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
    role: target
  - path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
    sha256: 412f85b2aeb446f9635a89f69cef1dc90c124dbade5bc41f1c5b568461a31e4a
    role: target
  - path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    sha256: 9660cbd309d7c81353bf0b1fe1a3cd5a883f6ec574e3a0d9e990166dd861de0f
    role: target
  - path: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
    sha256: 6b28f37858f010707aa5590ba7c607b83fc68c2dc02e74daaee810ed3107e4ca
    role: target
  - path: data/structures/energy_complex/respiratory_chain_complex_iv.yaml
    sha256: bbc04be6b11b9dd836132063ee51e13b8fe7bdde56bb21ba50940236e002e98c
    role: target
  - path: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
    sha256: 89b0850ee7b37bbb07768671a1a5b2d42855e9cf3c440276373aacaf9ba3c53c
    role: target
  - path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_complex.yaml
    sha256: 83ab28fcc2eb9d96345865559c437e573f0d03797ea43682fa5be32b3c220f1d
    role: target
  - path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
    sha256: b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48
    role: target
  - path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    sha256: fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22
    role: target
  - path: docs/CURATION.md
    sha256: 097a600e001c28cb1749faa2f1cc5e75b678a459df9b348aa3ef599a6405cbe4
    role: context
  - path: docs/SCHEMA.md
    sha256: 07b8f936a553a45cc6e8dba924c21e6af48c81b3866725efeb00c8183f0c75a2
    role: context
  - path: docs/record-review-profile.md
    sha256: 6a49c8d35f0a94082a9ad0b8bd8c6a929d85de8339141955f3779bd7ab0eb7e4
    role: context
  - path: docs/record-reviews.md
    sha256: 452a19ab688276747b7c4308523a14d4d99c1c39ef6909ae8a90b85b7a9b3e9b
    role: context
  - path: src/cellstructuremech/schema/cellstructuremech.yaml
    sha256: adbf5dfc7dc2eb87cfbc8c827b0a5a9f4346e9b7724fea93f7b294569e759944
    role: context
  - path: src/cellstructuremech/schema/history.yaml
    sha256: b01b06f1b9a37db205c26c31ec0fd910690848507c7e1bfb73b424ac0829c52d
    role: context
scope:
  description: Full-cohort review of all 40 CellStructureRecord YAML files under data/structures/energy_complex/.
  selection: Complete folder cohort data/structures/energy_complex/*.yaml in the frozen
    993-record Cycle 3 Stage 4 inventory.
  coverage: full
  population_size: 40
  reviewed_target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  - GO:0009512
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  - GO:0009319
  - GO:0009390
  - GO:0009326
  - cellstructuremech:formate_dehydrogenase_n_complex
  - cellstructuremech:formate_hydrogenlyase_complex
  - GO:0045283
  - cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex
  - GO:0030076
  - GO:0044674
  - GO:0044799
  - GO:0009325
  - GO:0016610
  - GO:0009521
  - GO:0009522
  - GO:0009523
  - GO:0030089
  - cellstructuremech:phycobilisome_core
  - cellstructuremech:phycobilisome_rod
  - GO:0030094
  - GO:0030096
  - GO:0045259
  - GO:0016469
  - GO:0033178
  - GO:0033177
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0045275
  - GO:0045277
  - GO:0160292
  - GO:0016471
  - GO:0000220
  - GO:0000221
targets:
- target_id: cellstructuremech:chlorosome_baseplate_antenna_complex
  path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
  label: chlorosome baseplate antenna complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7ea00dedcd0998fc477737d6d2e8301e4e57a08e57378d19efe5e32a6ea8c92d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/chlorosome_baseplate_antenna_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:chromatophore_cytochrome_bc1_complex
  path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
  label: chromatophore cytochrome bc1 complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7f6582722d2f5376262287856929ec073f8550493eee88c6cb92dfc7624ec7ed
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/chromatophore_cytochrome_bc1_complex.yaml
    role: maintained_record
- target_id: GO:0009512
  path: data/structures/energy_complex/cytochrome_b6f_complex.yaml
  label: cytochrome b6f complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6d228ab890a3a8f8f67e756ac5343896db16bc57dfc55d8250d2afd87851f7c3
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/cytochrome_b6f_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  path: data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
  label: cytochrome bd-I ubiquinol oxidase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1a71d5c7e8f417d2e943dfea2657d5be85bebad9786cccc4fee4fa39fa66f825
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/cytochrome_bd_i_ubiquinol_oxidase_complex.yaml
    role: maintained_record
- target_id: GO:0009319
  path: data/structures/energy_complex/cytochrome_o_ubiquinol_oxidase_complex.yaml
  label: cytochrome o ubiquinol oxidase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0afaecc355f783a9a89789e5b765680d3bb22aa0617c80eaf6b279d3096e6bc7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/cytochrome_o_ubiquinol_oxidase_complex.yaml
    role: maintained_record
- target_id: GO:0009390
  path: data/structures/energy_complex/dimethyl_sulfoxide_reductase_complex.yaml
  label: dimethyl sulfoxide reductase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2422ae4303bcaafc3a0c60fa5bb3ac71cde37b650a4352868c91e32437c6308d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/dimethyl_sulfoxide_reductase_complex.yaml
    role: maintained_record
- target_id: GO:0009326
  path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
  label: formate dehydrogenase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5972b09d4e2e8884aa9b7c2974a3c568227fdcfcb768bf68ee0d366ec0345b4e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:formate_dehydrogenase_n_complex
  path: data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
  label: formate dehydrogenase N complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ef7276f6532db0b7be7eac0564d02687a9661839dd9181aa89374ff24a6afe62
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_dehydrogenase_n_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:formate_hydrogenlyase_complex
  path: data/structures/energy_complex/formate_hydrogenlyase_complex.yaml
  label: formate hydrogenlyase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2fc61b025a3a5b49936cb08e6e58ae7a6aba385f953b1535e5ba27859602a99b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/formate_hydrogenlyase_complex.yaml
    role: maintained_record
- target_id: GO:0045283
  path: data/structures/energy_complex/fumarate_reductase_complex.yaml
  label: fumarate reductase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e823d8ddaac1348ad816503190e4a0c020e4b115c80831dcc6383e44346c7c6f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/fumarate_reductase_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex
  path: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
  label: LH2 peripheral light-harvesting antenna complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4bb84c48c2bb27f1a8dded06f479771b494070977ef26e0b14f0708bc446a7ce
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/lh2_peripheral_light_harvesting_antenna_complex.yaml
    role: maintained_record
- target_id: GO:0030076
  path: data/structures/energy_complex/light_harvesting_complex.yaml
  label: light-harvesting complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4454f3c667f5536bb3c39e9be2ef6aee5cb38e9842dda50f55e19ddf79bb2bdd
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/light_harvesting_complex.yaml
    role: maintained_record
- target_id: GO:0044674
  path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
  label: methyl coenzyme M reductase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ef43ab9df3e0a3d8ed86e0347c9801db59ced9efd1d0313f8ab2a9b3b1420338
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    role: maintained_record
- target_id: GO:0044799
  path: data/structures/energy_complex/narghi_complex.yaml
  label: NarGHI complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3820651a5a9e3aed9a74bb663caa00f4e428c344d0bfc432ab343f171f30aabb
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/narghi_complex.yaml
    role: maintained_record
- target_id: GO:0009325
  path: data/structures/energy_complex/nitrate_reductase_complex.yaml
  label: nitrate reductase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ad431e98375e475d6f38365d314b04bb0eb3643d39f289a879d5496ad1ce3459
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrate_reductase_complex.yaml
    role: maintained_record
- target_id: GO:0016610
  path: data/structures/energy_complex/nitrogenase_complex.yaml
  label: nitrogenase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 530365fc81d15c00b907873712c418eb8b4dd14e7e0ce2cca4f6796862186026
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/nitrogenase_complex.yaml
    role: maintained_record
- target_id: GO:0009521
  path: data/structures/energy_complex/photosystem.yaml
  label: photosystem
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c2bcf25948fb2eac1930736513012c4c177df4e0138ef971209ffed798ef3da8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem.yaml
    role: maintained_record
- target_id: GO:0009522
  path: data/structures/energy_complex/photosystem_i.yaml
  label: photosystem I
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: fc0a444867219721d503382db2682e2146969c65bbc777c8bf86581f6524ef0e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem_i.yaml
    role: maintained_record
- target_id: GO:0009523
  path: data/structures/energy_complex/photosystem_ii.yaml
  label: photosystem II
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: fc05496451f76ed16643edb2ca590803fd07569abfe432111e31314375687a16
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/photosystem_ii.yaml
    role: maintained_record
- target_id: GO:0030089
  path: data/structures/energy_complex/phycobilisome.yaml
  label: phycobilisome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b05c823a9d1bea4fb41a69a9ab7361be702d0b0d0a60f6536c73eb08c0ec9b40
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome.yaml
    role: maintained_record
- target_id: cellstructuremech:phycobilisome_core
  path: data/structures/energy_complex/phycobilisome_core.yaml
  label: phycobilisome core
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 34cca2a846f5b2b84b95c6c2db929370814b4e2898eee052f3e2cbfecafde554
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_core.yaml
    role: maintained_record
- target_id: cellstructuremech:phycobilisome_rod
  path: data/structures/energy_complex/phycobilisome_rod.yaml
  label: phycobilisome rod
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f610a707b8f8fea3edfd28574b996a315eaf1e2d245de7efce9edf96b49943d1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/phycobilisome_rod.yaml
    role: maintained_record
- target_id: GO:0030094
  path: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
  label: plasma membrane-derived photosystem I
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8fec8764bc49e21960bbfc6d95eb30247aab5158ef852d45ad4d7cec2aa9eff6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/plasma_membrane_derived_photosystem_i.yaml
    role: maintained_record
- target_id: GO:0030096
  path: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
  label: plasma membrane-derived thylakoid photosystem II
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7629a2480ce3d823e87431d0c26be93c45101095021fd60087301f5f1d9a58ef
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/plasma_membrane_derived_thylakoid_photosystem_ii.yaml
    role: maintained_record
- target_id: GO:0045259
  path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
  label: proton-transporting ATP synthase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ab93b5ffa055615dfc9de1edfb137773e1098b4f7e9eefdda9d0ea00961af4fb
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_atp_synthase_complex.yaml
    role: maintained_record
- target_id: GO:0016469
  path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex.yaml
  label: proton-transporting two-sector ATPase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4a1a6f78af3ec95c4ce56ab37996344566f78a38a95263d34ba386cd681ca26a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex.yaml
    role: maintained_record
- target_id: GO:0033178
  path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml
  label: proton-transporting two-sector ATPase complex, catalytic domain
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ffe0962a1a4efb660e02c185cce1f37ded89481634a7f12f217863e6ab7569e1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml
    role: maintained_record
- target_id: GO:0033177
  path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_proton_transporting_domain.yaml
  label: proton-transporting two-sector ATPase complex, proton-transporting domain
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 73fcc564b341e9dbeaa5634126d6b1a25dc8ac6a0a5193c626fc0485d463b6b8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_proton_transporting_domain.yaml
    role: maintained_record
- target_id: GO:0033176
  path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
  label: proton-transporting V-type ATPase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 664368c78b89064e89426ced374c86cef839457112601cf3413372319ff369d4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_complex.yaml
    role: maintained_record
- target_id: GO:0033179
  path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
  label: proton-transporting V-type ATPase, V0 domain
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f5955010d84445f4d57d44c34a72e35489c6c7b9f44315d9a24cad4c80320c6c
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained_record
- target_id: GO:0033180
  path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
  label: proton-transporting V-type ATPase, V1 domain
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a9096f4ff8a763caea7625663f9ac36a376c00ca1b7d64f51d2dd7fd75456300
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained_record
- target_id: cellstructuremech:rc_lh1_pufx_core_complex
  path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
  label: RC-LH1-PufX core complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0a3a6fcfe54b7a355fd2903992f521fb2fc293ce984d4ede356dbc8460071824
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/rc_lh1_pufx_core_complex.yaml
    role: maintained_record
- target_id: GO:0045271
  path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
  label: respiratory chain complex I
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 412f85b2aeb446f9635a89f69cef1dc90c124dbade5bc41f1c5b568461a31e4a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_i.yaml
    role: maintained_record
- target_id: GO:0045273
  path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
  label: respiratory chain complex II (succinate dehydrogenase)
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9660cbd309d7c81353bf0b1fe1a3cd5a883f6ec574e3a0d9e990166dd861de0f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_ii_succinate_dehydrogenase.yaml
    role: maintained_record
- target_id: GO:0045275
  path: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
  label: respiratory chain complex III
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6b28f37858f010707aa5590ba7c607b83fc68c2dc02e74daaee810ed3107e4ca
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_iii.yaml
    role: maintained_record
- target_id: GO:0045277
  path: data/structures/energy_complex/respiratory_chain_complex_iv.yaml
  label: respiratory chain complex IV
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: bbc04be6b11b9dd836132063ee51e13b8fe7bdde56bb21ba50940236e002e98c
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/respiratory_chain_complex_iv.yaml
    role: maintained_record
- target_id: GO:0160292
  path: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
  label: sodium-translocating NADH:quinone reductase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 89b0850ee7b37bbb07768671a1a5b2d42855e9cf3c440276373aacaf9ba3c53c
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/sodium_translocating_nadh_quinone_reductase_complex.yaml
    role: maintained_record
- target_id: GO:0016471
  path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_complex.yaml
  label: vacuolar proton-transporting V-type ATPase complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 83ab28fcc2eb9d96345865559c437e573f0d03797ea43682fa5be32b3c220f1d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_complex.yaml
    role: maintained_record
- target_id: GO:0000220
  path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
  label: vacuolar proton-transporting V-type ATPase, V0 domain
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b76891f7e50630db7612669a25299babae68eb2e480724de8209094cc1953c48
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v0_domain.yaml
    role: maintained_record
- target_id: GO:0000221
  path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
  label: vacuolar proton-transporting V-type ATPase, V1 domain
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: fabfca0b7f5ff5ee1340a6874918e4505c242d7939734a2e9ef8f3df5ebeeb22
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/vacuolar_proton_transporting_v_type_atpase_v1_domain.yaml
    role: maintained_record
checks:
- check_id: strict_energy_complex
  name: Strict corpus validation covering energy_complex cohort
  status: passed
  required: true
  summary: All 40 energy_complex records pass strict LinkML and semantic validation.
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  - GO:0009512
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  - GO:0009319
  - GO:0009390
  - GO:0009326
  - cellstructuremech:formate_dehydrogenase_n_complex
  - cellstructuremech:formate_hydrogenlyase_complex
  - GO:0045283
  - cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex
  - GO:0030076
  - GO:0044674
  - GO:0044799
  - GO:0009325
  - GO:0016610
  - GO:0009521
  - GO:0009522
  - GO:0009523
  - GO:0030089
  - cellstructuremech:phycobilisome_core
  - cellstructuremech:phycobilisome_rod
  - GO:0030094
  - GO:0030096
  - GO:0045259
  - GO:0016469
  - GO:0033178
  - GO:0033177
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0045275
  - GO:0045277
  - GO:0160292
  - GO:0016471
  - GO:0000220
  - GO:0000221
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_energycomplex
- check_id: labels_energy_complex
  name: ID-label correspondence across energy_complex cohort
  status: passed
  required: true
  summary: All ontology ID-label pairs in energy_complex records correspond to canonical
    labels.
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  - GO:0009512
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  - GO:0009319
  - GO:0009390
  - GO:0009326
  - cellstructuremech:formate_dehydrogenase_n_complex
  - cellstructuremech:formate_hydrogenlyase_complex
  - GO:0045283
  - cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex
  - GO:0030076
  - GO:0044674
  - GO:0044799
  - GO:0009325
  - GO:0016610
  - GO:0009521
  - GO:0009522
  - GO:0009523
  - GO:0030089
  - cellstructuremech:phycobilisome_core
  - cellstructuremech:phycobilisome_rod
  - GO:0030094
  - GO:0030096
  - GO:0045259
  - GO:0016469
  - GO:0033178
  - GO:0033177
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0045275
  - GO:0045277
  - GO:0160292
  - GO:0016471
  - GO:0000220
  - GO:0000221
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_labels_energycomplex
evidence:
- evidence_id: ev_strict_energycomplex
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict receipt
  accessed_at: '2026-10-25T07:10:06Z'
  support: supports
  summary: validate_strict.py exited 0 across all 993 records including all 40 energy_complex
    records.
  snapshot_sha256: fc80872aed828ea24abbaf1ff66194605d09857b0bf0773189fc076d223594eb
- evidence_id: ev_labels_energycomplex
  kind: validation
  reference: scripts/validate_id_label_correspondence.py
  locator: labels receipt
  accessed_at: '2026-10-25T07:10:06Z'
  support: supports
  summary: validate_id_label_correspondence.py exited 0 across all ontology targets.
  snapshot_sha256: 4bb207ccdd3216a741b1ca17643c1b57a2f2c68af02138decedfcd4fd19c8b3a
- evidence_id: ev_ec_atpase_subcomplex_and_history
  kind: record_content
  reference: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml
  locator: components[0..1] (lines 16-66) and curation_history[1].changes (lines 259-264)
    in GO:0033178 and curation_history[1].changes (lines 255-260) in GO:0033177
  accessed_at: '2026-10-25T07:02:30Z'
  support: supports
  summary: GO:0033178 types heteromeric subcomplexes catalytic_hexamer_head and central_rotational_stalk
    as PROTEIN instead of PROTEIN_COMPLEX, and both GO:0033178 and GO:0033177 cite
    mismatched graph_ids in curation_history[1].changes.
  quote: "- component_id: catalytic_hexamer_head\n  label: catalytic hexameric head\
    \ subunits\n  component_type: PROTEIN\n  component_role: CONSTITUENT"
  snapshot_sha256: ffe0962a1a4efb660e02c185cce1f37ded89481634a7f12f217863e6ab7569e1
- evidence_id: ev_ec_mcr_grounding
  kind: record_content
  reference: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
  locator: components[0..2] vs causal_graphs[0].nodes[1..3] (lines 226-240)
  accessed_at: '2026-10-25T07:02:45Z'
  support: supports
  summary: methyl_coenzyme_m_reductase_complex.yaml causal_graphs[0] nodes mcr_alpha_subunit,
    mcr_beta_subunit, and mcr_gamma_subunit omit InterPro:IPR016212, InterPro:IPR003179,
    and InterPro:IPR003178.
  quote: "  - node_id: mcr_alpha_subunit\n    label: Methyl coenzyme M reductase,\
    \ alpha subunit\n    node_type: GENE_OR_PROTEIN\n    component_ref: mcr_alpha_subunit"
  snapshot_sha256: ef43ab9df3e0a3d8ed86e0347c9801db59ced9efd1d0313f8ab2a9b3b1420338
assessments:
- assessment_id: assess_energycomplex_cohort
  area: scope
  topic: Identity, boundaries, causal graphs, and ontology grounding across data/structures/energy_complex/
  outcome: supported
  summary: All 40 records in data/structures/energy_complex/ represent distinct microbial
    cell structures or subcomplexes with valid hierarchy links and verified UniProtKB
    protein examples.
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  - GO:0009512
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  - GO:0009319
  - GO:0009390
  - GO:0009326
  - cellstructuremech:formate_dehydrogenase_n_complex
  - cellstructuremech:formate_hydrogenlyase_complex
  - GO:0045283
  - cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex
  - GO:0030076
  - GO:0044674
  - GO:0044799
  - GO:0009325
  - GO:0016610
  - GO:0009521
  - GO:0009522
  - GO:0009523
  - GO:0030089
  - cellstructuremech:phycobilisome_core
  - cellstructuremech:phycobilisome_rod
  - GO:0030094
  - GO:0030096
  - GO:0045259
  - GO:0016469
  - GO:0033178
  - GO:0033177
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0045275
  - GO:0045277
  - GO:0160292
  - GO:0016471
  - GO:0000220
  - GO:0000221
  evidence_ids:
  - ev_strict_energycomplex
  - ev_labels_energycomplex
- assessment_id: assess_ec_atpase
  area: consistency
  topic: Subcomplex component_type and curation_history causal_graph IDs in two-sector
    ATPase domain records
  outcome: concern
  summary: GO:0033178 types heteromeric subcomplexes catalytic_hexamer_head and central_rotational_stalk
    as PROTEIN, and GO:0033178 and GO:0033177 cite stale graph_ids in curation_history[1].changes.
  target_ids:
  - GO:0033178
  - GO:0033177
  evidence_ids:
  - ev_ec_atpase_subcomplex_and_history
- assessment_id: assess_ec_mcr
  area: graph
  topic: Causal-graph component_ref grounding propagation in methyl_coenzyme_m_reductase_complex.yaml
  outcome: concern
  summary: 'Three component_ref causal_graphs nodes in methyl_coenzyme_m_reductase_complex.yaml
    omit verified InterPro: groundings from components[].'
  target_ids:
  - GO:0044674
  evidence_ids:
  - ev_ec_mcr_grounding
findings:
- finding_id: F1
  issue_key: energy-complex-atpase-subcomplex-types-and-history-graph-ids
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: Two-sector ATPase domain records type heteromeric F1/V1 subcomplexes as PROTEIN
    and cite mismatched causal_graph IDs in curation_history[1].changes
  description: 'In data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml
    (GO:0033178), heteromeric multiprotein subcomplex components catalytic_hexamer_head
    (atpA/atpD/VMA1/VMA2, alpha3-beta3 hexamer) and central_rotational_stalk (atpG/atpC/VMA8/VMA7,
    gamma-epsilon / D-F stalk) are typed component_type: PROTEIN instead of PROTEIN_COMPLEX,
    and curation_history[1].changes cites graph_id ''catalytic_sector_rotary_catalysis''
    instead of causal_graphs[0].graph_id ''catalytic_domain_rotary_mechanism''. In
    sibling proton_transporting_two_sector_atpase_complex_proton_transporting_domain.yaml
    (GO:0033177), curation_history[1].changes cites graph_id ''proton_sector_rotary_conduction''
    instead of causal_graphs[0].graph_id ''proton_transporting_domain_mechanism''.'
  target_ids:
  - GO:0033178
  - GO:0033177
  field_paths:
  - components[0].component_type
  - components[1].component_type
  - curation_history[1].changes
  evidence_ids:
  - ev_ec_atpase_subcomplex_and_history
  rule_id: docs/SCHEMA.md:ComponentTypeEnum
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_proton_transporting_domain.yaml
    role: maintained_record
  tags:
  - components
  - component-type
  - curation-history
  - stage4-record-review
- finding_id: F2
  issue_key: energy-complex-mcr-causal-node-component-ref-grounding
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: 'methyl_coenzyme_m_reductase_complex.yaml causal_graphs[0] subunit nodes
    omit verified InterPro: groundings from components[]'
  description: 'In data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    (GO:0044674), causal_graphs[0] nodes mcr_alpha_subunit (nodes[1]), mcr_beta_subunit
    (nodes[2]), and mcr_gamma_subunit (nodes[3]) reference components[0..2] via component_ref
    but omit their verified InterPro: groundings (InterPro:IPR016212, InterPro:IPR003179,
    InterPro:IPR003178).'
  target_ids:
  - GO:0044674
  field_paths:
  - causal_graphs[0].nodes[1].grounding
  - causal_graphs[0].nodes[2].grounding
  - causal_graphs[0].nodes[3].grounding
  evidence_ids:
  - ev_ec_mcr_grounding
  rule_id: docs/SCHEMA.md:CausalNode-grounding
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    role: maintained_record
  tags:
  - causal-graphs
  - grounding
  - component-ref
  - stage4-record-review
actions:
- action_id: A1
  description: 'Update catalytic_hexamer_head and central_rotational_stalk in GO:0033178
    to component_type: PROTEIN_COMPLEX, align curation_history[1].changes in GO:0033178
    and GO:0033177 to their actual causal_graphs[0].graph_id values, and record the
    updates in history/records/.'
  finding_ids:
  - F1
  target_ids:
  - GO:0033178
  - GO:0033177
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_catalytic_domain.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/proton_transporting_two_sector_atpase_complex_proton_transporting_domain.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
- action_id: A2
  description: Propagate InterPro:IPR016212, InterPro:IPR003179, and InterPro:IPR003178
    to causal_graphs[0].nodes[1..3] in methyl_coenzyme_m_reductase_complex.yaml and
    record the update in history/records/methyl_coenzyme_m_reductase_complex/.
  finding_ids:
  - F2
  target_ids:
  - GO:0044674
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/energy_complex/methyl_coenzyme_m_reductase_complex.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
boundary_decisions:
- action: retain
  target_ids:
  - cellstructuremech:chlorosome_baseplate_antenna_complex
  - cellstructuremech:chromatophore_cytochrome_bc1_complex
  - GO:0009512
  - cellstructuremech:cytochrome_bd_i_ubiquinol_oxidase_complex
  - GO:0009319
  - GO:0009390
  - GO:0009326
  - cellstructuremech:formate_dehydrogenase_n_complex
  - cellstructuremech:formate_hydrogenlyase_complex
  - GO:0045283
  - cellstructuremech:lh2_peripheral_light_harvesting_antenna_complex
  - GO:0030076
  - GO:0044674
  - GO:0044799
  - GO:0009325
  - GO:0016610
  - GO:0009521
  - GO:0009522
  - GO:0009523
  - GO:0030089
  - cellstructuremech:phycobilisome_core
  - cellstructuremech:phycobilisome_rod
  - GO:0030094
  - GO:0030096
  - GO:0045259
  - GO:0016469
  - GO:0033178
  - GO:0033177
  - GO:0033176
  - GO:0033179
  - GO:0033180
  - cellstructuremech:rc_lh1_pufx_core_complex
  - GO:0045271
  - GO:0045273
  - GO:0045275
  - GO:0045277
  - GO:0160292
  - GO:0016471
  - GO:0000220
  - GO:0000221
  rationale: All 40 records in data/structures/energy_complex/ represent distinct
    respiratory, photosynthetic, methanogenic, or rotary ATPase complexes and subcomplexes.
  evidence_ids:
  - ev_strict_energycomplex
  - ev_labels_energycomplex
limitations:
- Record edits for energy_complex cohort findings are queued for Cycle 3 Stage 5 (resolve_review_findings).
tags:
- stage4
- category-review
- energy-complex
```
