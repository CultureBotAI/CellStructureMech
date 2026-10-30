# Category review of data/structures/ribonucleoprotein/ (88 records)

- Review: 20261030T082010Z-ribonucleoprotein-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-30T08:14:00Z
- Finished UTC: 2026-10-30T08:20:10Z
- Reviewer: antigravity-c4s4-record-review (independent)
- Completion: completed
- Verdict: needs_curation
- Scientific review: true

## Summary

Full cohort audit of all 88 RIBONUCLEOPROTEIN records in data/structures/ribonucleoprotein/. One major hierarchy/parthood conflation and one minor component_type/evidence-notes bundle were identified across 3 records: (F1) supraspliceosomal_complex.yaml (GO:0044530) lists GO:0005681 (spliceosomal complex) in parent_structures (is-a) while simultaneously modeling components[0] (spliceosomal_complex, grounding: GO:0005681, component_role: CONSTITUENT, stoichiometry: '4') as its tetrameric subunit without has_part: [GO:0005681]; and (F2) box_c_d_methylation_guide_snornp_complex.yaml (GO:0031428) types 4-subunit nop1_nop56_nop58_snu13_core ([NOP1, NOP56, NOP58, SNU13]) as PROTEIN instead of PROTEIN_COMPLEX, while box_c_d_rnp_complex.yaml (GO:0170049) components[1].protein_examples[2,3] evidence[0].notes still concatenate two paper citations on single-PMID EvidenceItem entries.

## Scope And Provenance

Full-cohort review of all 88 CellStructureRecord YAML files under data/structures/ribonucleoprotein/.

Selection: Complete folder cohort data/structures/ribonucleoprotein/*.yaml in the frozen 1,001-record Cycle 4 Stage 4 inventory.
Coverage: full; 88 reviewed / 88 in the declared population.
Source: git_commit at Git base 5c642e4080ef3a0f026845843c559d3b46de8871.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0120259 | data/structures/ribonucleoprotein/7sk_snrnp.yaml | maintained | 7SK snRNP |
| GO:0030686 | data/structures/ribonucleoprotein/90s_preribosome.yaml | maintained | 90S preribosome |
| GO:1990061 | data/structures/ribonucleoprotein/bacterial_degradosome.yaml | maintained | bacterial degradosome |
| GO:0031428 | data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml | maintained | box C/D methylation guide snoRNP complex |
| GO:0170049 | data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml | maintained | box C/D RNP complex |
| GO:0072588 | data/structures/ribonucleoprotein/box_h_aca_rnp_complex.yaml | maintained | box H/ACA RNP complex |
| GO:0031429 | data/structures/ribonucleoprotein/box_h_aca_snornp_complex.yaml | maintained | box H/ACA snoRNP complex |
| GO:0015030 | data/structures/ribonucleoprotein/cajal_body.yaml | maintained | Cajal body |
| GO:0071012 | data/structures/ribonucleoprotein/catalytic_step_1_spliceosome.yaml | maintained | catalytic step 1 spliceosome |
| GO:0071013 | data/structures/ribonucleoprotein/catalytic_step_2_spliceosome.yaml | maintained | catalytic step 2 spliceosome |
| GO:0000243 | data/structures/ribonucleoprotein/commitment_complex.yaml | maintained | commitment complex |
| GO:0030679 | data/structures/ribonucleoprotein/cyanelle_ribonuclease_p_complex.yaml | maintained | cyanelle ribonuclease P complex |
| GO:0000177 | data/structures/ribonucleoprotein/cytoplasmic_exosome_rnase_complex.yaml | maintained | cytoplasmic exosome (RNase complex) |
| GO:0010494 | data/structures/ribonucleoprotein/cytoplasmic_stress_granule.yaml | maintained | cytoplasmic stress granule |
| GO:0030680 | data/structures/ribonucleoprotein/dimeric_ribonuclease_p_complex.yaml | maintained | dimeric ribonuclease P complex |
| GO:0000178 | data/structures/ribonucleoprotein/exosome_rnase_complex.yaml | maintained | exosome (RNase complex) |
| cellstructuremech:glycolytic_body | data/structures/ribonucleoprotein/glycolytic_body.yaml | maintained | glycolytic body |
| cellstructuremech:h_body | data/structures/ribonucleoprotein/h_body.yaml | maintained | H-body |
| GO:0035363 | data/structures/ribonucleoprotein/histone_locus_body.yaml | maintained | histone locus body |
| GO:0035061 | data/structures/ribonucleoprotein/interchromatin_granule.yaml | maintained | interchromatin granule |
| GO:0015934 | data/structures/ribonucleoprotein/large_ribosomal_subunit.yaml | maintained | large ribosomal subunit |
| GO:0120115 | data/structures/ribonucleoprotein/lsm2_8_complex.yaml | maintained | Lsm2-8 complex |
| GO:0030681 | data/structures/ribonucleoprotein/multimeric_ribonuclease_p_complex.yaml | maintained | multimeric ribonuclease P complex |
| GO:0010445 | data/structures/ribonucleoprotein/nuclear_dicing_body.yaml | maintained | nuclear dicing body |
| GO:0000176 | data/structures/ribonucleoprotein/nuclear_exosome_rnase_complex.yaml | maintained | nuclear exosome (RNase complex) |
| GO:0016607 | data/structures/ribonucleoprotein/nuclear_speck.yaml | maintained | nuclear speck |
| GO:0097165 | data/structures/ribonucleoprotein/nuclear_stress_granule.yaml | maintained | nuclear stress granule |
| GO:0101019 | data/structures/ribonucleoprotein/nucleolar_exosome_rnase_complex.yaml | maintained | nucleolar exosome (RNase complex) |
| GO:0005655 | data/structures/ribonucleoprotein/nucleolar_ribonuclease_p_complex.yaml | maintained | nucleolar ribonuclease P complex |
| GO:0035062 | data/structures/ribonucleoprotein/omega_speckle.yaml | maintained | omega speckle |
| GO:0000932 | data/structures/ribonucleoprotein/p_body.yaml | maintained | P-body |
| GO:0042382 | data/structures/ribonucleoprotein/paraspeckles.yaml | maintained | paraspeckles |
| GO:0071003 | data/structures/ribonucleoprotein/penta_snrnp_complex.yaml | maintained | penta-snRNP complex |
| GO:0097356 | data/structures/ribonucleoprotein/perinucleolar_compartment.yaml | maintained | perinucleolar compartment |
| GO:0071014 | data/structures/ribonucleoprotein/post_mrna_release_spliceosomal_complex.yaml | maintained | post-mRNA release spliceosomal complex |
| GO:0071020 | data/structures/ribonucleoprotein/post_spliceosomal_complex.yaml | maintained | post-spliceosomal complex |
| GO:0071011 | data/structures/ribonucleoprotein/precatalytic_spliceosome.yaml | maintained | precatalytic spliceosome |
| GO:0030684 | data/structures/ribonucleoprotein/preribosome.yaml | maintained | preribosome |
| GO:0030687 | data/structures/ribonucleoprotein/preribosome_large_subunit_precursor.yaml | maintained | preribosome, large subunit precursor |
| GO:0030688 | data/structures/ribonucleoprotein/preribosome_small_subunit_precursor.yaml | maintained | preribosome, small subunit precursor |
| GO:0071010 | data/structures/ribonucleoprotein/prespliceosome.yaml | maintained | prespliceosome |
| GO:0000172 | data/structures/ribonucleoprotein/ribonuclease_mrp_complex.yaml | maintained | ribonuclease MRP complex |
| GO:0030677 | data/structures/ribonucleoprotein/ribonuclease_p_complex.yaml | maintained | ribonuclease P complex |
| GO:0005840 | data/structures/ribonucleoprotein/ribosome.yaml | maintained | ribosome |
| GO:0140365 | data/structures/ribonucleoprotein/rnp_body.yaml | maintained | RNP body |
| GO:0048500 | data/structures/ribonucleoprotein/signal_recognition_particle.yaml | maintained | signal recognition particle |
| GO:0071024 | data/structures/ribonucleoprotein/sl_snrnp.yaml | maintained | SL snRNP |
| GO:0030532 | data/structures/ribonucleoprotein/small_nuclear_ribonucleoprotein_complex.yaml | maintained | small nuclear ribonucleoprotein complex |
| GO:0015935 | data/structures/ribonucleoprotein/small_ribosomal_subunit.yaml | maintained | small ribosomal subunit |
| GO:0032040 | data/structures/ribonucleoprotein/small_subunit_processome.yaml | maintained | small-subunit processome |
| GO:0005732 | data/structures/ribonucleoprotein/sno_s_rna_containing_ribonucleoprotein_complex.yaml | maintained | sno(s)RNA-containing ribonucleoprotein complex |
| GO:0071601 | data/structures/ribonucleoprotein/sphere_organelle.yaml | maintained | sphere organelle |
| GO:0005681 | data/structures/ribonucleoprotein/spliceosomal_complex.yaml | maintained | spliceosomal complex |
| GO:0097525 | data/structures/ribonucleoprotein/spliceosomal_snrnp_complex.yaml | maintained | spliceosomal snRNP complex |
| GO:0097526 | data/structures/ribonucleoprotein/spliceosomal_tri_snrnp_complex.yaml | maintained | spliceosomal tri-snRNP complex |
| GO:0044530 | data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml | maintained | supraspliceosomal complex |
| GO:0005697 | data/structures/ribonucleoprotein/telomerase_holoenzyme_complex.yaml | maintained | telomerase holoenzyme complex |
| cellstructuremech:tmar_condensate | data/structures/ribonucleoprotein/tmar_condensate.yaml | maintained | TmaR condensate |
| GO:0071023 | data/structures/ribonucleoprotein/trans_spliceosomal_complex.yaml | maintained | trans spliceosomal complex |
| GO:0005692 | data/structures/ribonucleoprotein/u11_snrnp.yaml | maintained | U11 snRNP |
| GO:0034693 | data/structures/ribonucleoprotein/u11_u12_snrnp.yaml | maintained | U11/U12 snRNP |
| GO:0005693 | data/structures/ribonucleoprotein/u12_snrnp.yaml | maintained | U12 snRNP |
| GO:0071017 | data/structures/ribonucleoprotein/u12_type_catalytic_step_1_spliceosome.yaml | maintained | U12-type catalytic step 1 spliceosome |
| GO:0071018 | data/structures/ribonucleoprotein/u12_type_catalytic_step_2_spliceosome.yaml | maintained | U12-type catalytic step 2 spliceosome |
| GO:0071019 | data/structures/ribonucleoprotein/u12_type_post_mrna_release_spliceosomal_complex.yaml | maintained | U12-type post-mRNA release spliceosomal complex |
| GO:0071022 | data/structures/ribonucleoprotein/u12_type_post_spliceosomal_complex.yaml | maintained | U12-type post-spliceosomal complex |
| GO:0071016 | data/structures/ribonucleoprotein/u12_type_precatalytic_spliceosome.yaml | maintained | U12-type precatalytic spliceosome |
| GO:0071015 | data/structures/ribonucleoprotein/u12_type_prespliceosome.yaml | maintained | U12-type prespliceosome |
| GO:0005689 | data/structures/ribonucleoprotein/u12_type_spliceosomal_complex.yaml | maintained | U12-type spliceosomal complex |
| GO:0005685 | data/structures/ribonucleoprotein/u1_snrnp.yaml | maintained | U1 snRNP |
| GO:0005686 | data/structures/ribonucleoprotein/u2_snrnp.yaml | maintained | U2 snRNP |
| GO:0071006 | data/structures/ribonucleoprotein/u2_type_catalytic_step_1_spliceosome.yaml | maintained | U2-type catalytic step 1 spliceosome |
| GO:0071007 | data/structures/ribonucleoprotein/u2_type_catalytic_step_2_spliceosome.yaml | maintained | U2-type catalytic step 2 spliceosome |
| GO:0071008 | data/structures/ribonucleoprotein/u2_type_post_mrna_release_spliceosomal_complex.yaml | maintained | U2-type post-mRNA release spliceosomal complex |
| GO:0071021 | data/structures/ribonucleoprotein/u2_type_post_spliceosomal_complex.yaml | maintained | U2-type post-spliceosomal complex |
| GO:0071005 | data/structures/ribonucleoprotein/u2_type_precatalytic_spliceosome.yaml | maintained | U2-type precatalytic spliceosome |
| GO:0071004 | data/structures/ribonucleoprotein/u2_type_prespliceosome.yaml | maintained | U2-type prespliceosome |
| GO:0005684 | data/structures/ribonucleoprotein/u2_type_spliceosomal_complex.yaml | maintained | U2-type spliceosomal complex |
| GO:0005687 | data/structures/ribonucleoprotein/u4_snrnp.yaml | maintained | U4 snRNP |
| GO:0071001 | data/structures/ribonucleoprotein/u4_u6_snrnp.yaml | maintained | U4/U6 snRNP |
| GO:0046540 | data/structures/ribonucleoprotein/u4_u6_x_u5_tri_snrnp_complex.yaml | maintained | U4/U6 x U5 tri-snRNP complex |
| GO:0005690 | data/structures/ribonucleoprotein/u4atac_snrnp.yaml | maintained | U4atac snRNP |
| GO:0071002 | data/structures/ribonucleoprotein/u4atac_u6atac_snrnp.yaml | maintained | U4atac/U6atac snRNP |
| GO:0071009 | data/structures/ribonucleoprotein/u4atac_u6atac_x_u5_tri_snrnp_complex.yaml | maintained | U4atac/U6atac x U5 tri-snRNP complex |
| GO:0005682 | data/structures/ribonucleoprotein/u5_snrnp.yaml | maintained | U5 snRNP |
| GO:0005688 | data/structures/ribonucleoprotein/u6_snrnp.yaml | maintained | U6 snRNP |
| GO:0005691 | data/structures/ribonucleoprotein/u6atac_snrnp.yaml | maintained | U6atac snRNP |
| GO:0005683 | data/structures/ribonucleoprotein/u7_snrnp.yaml | maintained | U7 snRNP |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering ribonucleoprotein cohort | passed | True | GO:0120259, GO:0030686, GO:1990061, GO:0031428, GO:0170049, GO:0072588, GO:0031429, GO:0015030, GO:0071012, GO:0071013, GO:0000243, GO:0030679, GO:0000177, GO:0010494, GO:0030680, GO:0000178, cellstructuremech:glycolytic_body, cellstructuremech:h_body, GO:0035363, GO:0035061, GO:0015934, GO:0120115, GO:0030681, GO:0010445, GO:0000176, GO:0016607, GO:0097165, GO:0101019, GO:0005655, GO:0035062, GO:0000932, GO:0042382, GO:0071003, GO:0097356, GO:0071014, GO:0071020, GO:0071011, GO:0030684, GO:0030687, GO:0030688, GO:0071010, GO:0000172, GO:0030677, GO:0005840, GO:0140365, GO:0048500, GO:0071024, GO:0030532, GO:0015935, GO:0032040, GO:0005732, GO:0071601, GO:0005681, GO:0097525, GO:0097526, GO:0044530, GO:0005697, cellstructuremech:tmar_condensate, GO:0071023, GO:0005692, GO:0034693, GO:0005693, GO:0071017, GO:0071018, GO:0071019, GO:0071022, GO:0071016, GO:0071015, GO:0005689, GO:0005685, GO:0005686, GO:0071006, GO:0071007, GO:0071008, GO:0071021, GO:0071005, GO:0071004, GO:0005684, GO:0005687, GO:0071001, GO:0046540, GO:0005690, GO:0071002, GO:0071009, GO:0005682, GO:0005688, GO:0005691, GO:0005683 | All 88 ribonucleoprotein records pass strict LinkML and semantic validation. |
| History ledger validation covering ribonucleoprotein cohort | passed | True | GO:0120259, GO:0030686, GO:1990061, GO:0031428, GO:0170049, GO:0072588, GO:0031429, GO:0015030, GO:0071012, GO:0071013, GO:0000243, GO:0030679, GO:0000177, GO:0010494, GO:0030680, GO:0000178, cellstructuremech:glycolytic_body, cellstructuremech:h_body, GO:0035363, GO:0035061, GO:0015934, GO:0120115, GO:0030681, GO:0010445, GO:0000176, GO:0016607, GO:0097165, GO:0101019, GO:0005655, GO:0035062, GO:0000932, GO:0042382, GO:0071003, GO:0097356, GO:0071014, GO:0071020, GO:0071011, GO:0030684, GO:0030687, GO:0030688, GO:0071010, GO:0000172, GO:0030677, GO:0005840, GO:0140365, GO:0048500, GO:0071024, GO:0030532, GO:0015935, GO:0032040, GO:0005732, GO:0071601, GO:0005681, GO:0097525, GO:0097526, GO:0044530, GO:0005697, cellstructuremech:tmar_condensate, GO:0071023, GO:0005692, GO:0034693, GO:0005693, GO:0071017, GO:0071018, GO:0071019, GO:0071022, GO:0071016, GO:0071015, GO:0005689, GO:0005685, GO:0005686, GO:0071006, GO:0071007, GO:0071008, GO:0071021, GO:0071005, GO:0071004, GO:0005684, GO:0005687, GO:0071001, GO:0046540, GO:0005690, GO:0071002, GO:0071009, GO:0005682, GO:0005688, GO:0005691, GO:0005683 | All history ledger records covering ribonucleoprotein validate cleanly. |

## Scientific And Domain Assessments

### Identity, boundaries, causal graphs, and ontology grounding across data/structures/ribonucleoprotein/

scope: supported. Targets: GO:0120259, GO:0030686, GO:1990061, GO:0031428, GO:0170049, GO:0072588, GO:0031429, GO:0015030, GO:0071012, GO:0071013, GO:0000243, GO:0030679, GO:0000177, GO:0010494, GO:0030680, GO:0000178, cellstructuremech:glycolytic_body, cellstructuremech:h_body, GO:0035363, GO:0035061, GO:0015934, GO:0120115, GO:0030681, GO:0010445, GO:0000176, GO:0016607, GO:0097165, GO:0101019, GO:0005655, GO:0035062, GO:0000932, GO:0042382, GO:0071003, GO:0097356, GO:0071014, GO:0071020, GO:0071011, GO:0030684, GO:0030687, GO:0030688, GO:0071010, GO:0000172, GO:0030677, GO:0005840, GO:0140365, GO:0048500, GO:0071024, GO:0030532, GO:0015935, GO:0032040, GO:0005732, GO:0071601, GO:0005681, GO:0097525, GO:0097526, GO:0044530, GO:0005697, cellstructuremech:tmar_condensate, GO:0071023, GO:0005692, GO:0034693, GO:0005693, GO:0071017, GO:0071018, GO:0071019, GO:0071022, GO:0071016, GO:0071015, GO:0005689, GO:0005685, GO:0005686, GO:0071006, GO:0071007, GO:0071008, GO:0071021, GO:0071005, GO:0071004, GO:0005684, GO:0005687, GO:0071001, GO:0046540, GO:0005690, GO:0071002, GO:0071009, GO:0005682, GO:0005688, GO:0005691, GO:0005683.

All 88 records in data/structures/ribonucleoprotein/ represent distinct microbial cell structures or subcomplexes with valid schema and history provenance.

### Disjointness of parent_structures (is-a) vs CONSTITUENT component/has_part (parthood) in supraspliceosomal_complex.yaml

representation: concern. Targets: GO:0044530.

supraspliceosomal_complex.yaml (GO:0044530) models GO:0005681 (spliceosomal complex) as both an is-a parent_structures entry and a stoichiometry-'4' CONSTITUENT component.

### Box C/D snoRNP core protein subcomplex typing and per-PMID evidence note attribution

representation: concern. Targets: GO:0031428, GO:0170049.

box_c_d_methylation_guide_snornp_complex.yaml types 4-protein core subcomplex as PROTEIN, and box_c_d_rnp_complex.yaml retains two semicolon-joined multi-paper notes on single-PMID EvidenceItem entries.

## Findings

### F1: supraspliceosomal_complex.yaml lists GO:0005681 (spliceosomal complex) in parent_structures while modeling GO:0005681 as a stoichiometry-'4' CONSTITUENT component without has_part

major / open / confirmed; issue key: ribonucleoprotein-supraspliceosomal-parent-constituent-conflation.

In data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml (GO:0044530), GO:0005681 (spliceosomal complex) is listed in parent_structures (lines 11-13) and simultaneously as components[0] (id: spliceosomal_complex, label: 'Native spliceosome monomer', component_type: PROTEIN_COMPLEX, component_role: CONSTITUENT, stoichiometry: '4', grounding: GO:0005681), while has_part is omitted. Because the supraspliceosome is a tetrameric assembly of four native spliceosomes alongside 5'-splice-site RNP factors (GO:1990904 ribonucleoprotein complex), GO:0005681 is a parthood constituent (has_part: [GO:0005681]) rather than simultaneously an is-a parent and a constituent part.

### F2: box_c_d_methylation_guide_snornp_complex.yaml types 4-subunit nop1_nop56_nop58_snu13_core as PROTEIN and box_c_d_rnp_complex.yaml retains two multi-paper notes on single-PMID EvidenceItem entries

minor / open / confirmed; issue key: ribonucleoprotein-box-cd-snornp-type-and-evidence-notes.

In data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml (GO:0031428), components[1] (nop1_nop56_nop58_snu13_core, 'Nop1/Nop56/Nop58/Snu13 core protein subcomplex', gene_symbols: [NOP1, NOP56, NOP58, SNU13]) is typed PROTEIN instead of PROTEIN_COMPLEX (unlike sibling box_c_d_rnp_complex.yaml, where nop1_nop56_nop58_snu13_core is typed PROTEIN_COMPLEX). Additionally, in data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml (GO:0170049), components[1].protein_examples[2].evidence[0].notes (PMID:9632712, Wu P et al. 1998) and components[1].protein_examples[3].evidence[0].notes (PMID:9372940, Watkins NJ et al. 2000 / Snu13) still concatenate 'Gautier T et al. 1997 (Mol Cell Biol) and Lafontaine DL &amp; Tollervey D 1999 (RNA); Wu P et al. 1998 (Genes Dev)' on single-PMID entries.

## Recommended Actions And Acceptance Checks

### A1

Move GO:0005681 from parent_structures to has_part in data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml (retaining parent_structures: [GO:1990904] and has_part: [GO:0005681]).

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

### A2

Update components[1].component_type from PROTEIN to PROTEIN_COMPLEX in box_c_d_methylation_guide_snornp_complex.yaml, and align components[1].protein_examples[2,3].evidence[0].notes in box_c_d_rnp_complex.yaml with their single cited PMIDs (PMID:9632712 and PMID:9372940).

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries

- retain: GO:0120259, GO:0030686, GO:1990061, GO:0031428, GO:0170049, GO:0072588, GO:0031429, GO:0015030, GO:0071012, GO:0071013, GO:0000243, GO:0030679, GO:0000177, GO:0010494, GO:0030680, GO:0000178, cellstructuremech:glycolytic_body, cellstructuremech:h_body, GO:0035363, GO:0035061, GO:0015934, GO:0120115, GO:0030681, GO:0010445, GO:0000176, GO:0016607, GO:0097165, GO:0101019, GO:0005655, GO:0035062, GO:0000932, GO:0042382, GO:0071003, GO:0097356, GO:0071014, GO:0071020, GO:0071011, GO:0030684, GO:0030687, GO:0030688, GO:0071010, GO:0000172, GO:0030677, GO:0005840, GO:0140365, GO:0048500, GO:0071024, GO:0030532, GO:0015935, GO:0032040, GO:0005732, GO:0071601, GO:0005681, GO:0097525, GO:0097526, GO:0044530, GO:0005697, cellstructuremech:tmar_condensate, GO:0071023, GO:0005692, GO:0034693, GO:0005693, GO:0071017, GO:0071018, GO:0071019, GO:0071022, GO:0071016, GO:0071015, GO:0005689, GO:0005685, GO:0005686, GO:0071006, GO:0071007, GO:0071008, GO:0071021, GO:0071005, GO:0071004, GO:0005684, GO:0005687, GO:0071001, GO:0046540, GO:0005690, GO:0071002, GO:0071009, GO:0005682, GO:0005688, GO:0005691, GO:0005683. All 88 ribonucleoprotein records denote distinct ribosomal, spliceosomal, snoRNP, CRISPR-Cas, or RNA-degradosome complexes.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_ribonucleoprotein | scripts/validate_strict.py; strict_all receipt | supports | validate_strict.py exited 0 across all 1,001 records including all 88 ribonucleoprotein records. |
| ev_history_ribonucleoprotein | scripts/validate_history.py; history_all receipt | supports | validate_history.py exited 0 across all 2,082 history records covering ribonucleoprotein. |
| ev_rnp_supraspliceosome | data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml; parent_structures (lines 11-13) and components[0] (lines 25-33) | supports | supraspliceosomal_complex.yaml lists GO:0005681 in parent_structures and also as CONSTITUENT component spliceosomal_complex (stoichiometry '4') without has_part. |
| ev_rnp_boxcd_guide | data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml; components[1] (lines 38-47) | supports | box_c_d_methylation_guide_snornp_complex.yaml types 4-subunit nop1_nop56_nop58_snu13_core ([NOP1, NOP56, NOP58, SNU13]) as PROTEIN. |
| ev_rnp_boxcd_notes | data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml; components[1].protein_examples[2,3].evidence[0] (lines 90-108) | supports | box_c_d_rnp_complex.yaml components[1].protein_examples[2,3].evidence[0].notes concatenate Gautier T et al. 1997 and Wu P et al. 1998 on single-PMID entries. |

## Limits And Additional Notes

- Record edits for ribonucleoprotein cohort findings are queued for Cycle 4 Stage 5 (resolve_review_findings).

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261030T082010Z-ribonucleoprotein-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: Category review of data/structures/ribonucleoprotein/ (88 records)
started_at: '2026-10-30T08:14:00Z'
finished_at: '2026-10-30T08:20:10Z'
reviewer:
  identity: antigravity-c4s4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 4 Stage 4 record_review against committed
    git revision 5c642e4080ef3a0f026845843c559d3b46de8871 without record edits in
    this stage.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: needs_curation
native_verdict: NEEDS_CURATION
scientific_review: true
summary: 'Full cohort audit of all 88 RIBONUCLEOPROTEIN records in data/structures/ribonucleoprotein/.
  One major hierarchy/parthood conflation and one minor component_type/evidence-notes
  bundle were identified across 3 records: (F1) supraspliceosomal_complex.yaml (GO:0044530)
  lists GO:0005681 (spliceosomal complex) in parent_structures (is-a) while simultaneously
  modeling components[0] (spliceosomal_complex, grounding: GO:0005681, component_role:
  CONSTITUENT, stoichiometry: ''4'') as its tetrameric subunit without has_part: [GO:0005681];
  and (F2) box_c_d_methylation_guide_snornp_complex.yaml (GO:0031428) types 4-subunit
  nop1_nop56_nop58_snu13_core ([NOP1, NOP56, NOP58, SNU13]) as PROTEIN instead of
  PROTEIN_COMPLEX, while box_c_d_rnp_complex.yaml (GO:0170049) components[1].protein_examples[2,3]
  evidence[0].notes still concatenate two paper citations on single-PMID EvidenceItem
  entries.'
source:
  git_revision: 5c642e4080ef3a0f026845843c559d3b46de8871
  state: git_commit
  inputs:
  - path: .claude/skills/review-yaml-category/SKILL.md
    sha256: 7a7ae411cf451ee7e634dfc65b6a466e5c52206e5d9111f090d3704832ddceae
    role: context
  - path: AGENTS.md
    sha256: ef74a980161b55cd24f1851e38d1c0b2e004fcf8837f1bc70da1874e4e8380f0
    role: context
  - path: conf/record_review.yaml
    sha256: d3334a12b8a616a7638f1195748085d2b543fba7df67ad4ff8fcc0ac18f2d3ee
    role: context
  - path: data/structures/ribonucleoprotein/7sk_snrnp.yaml
    sha256: e3e56d806c4898e643c8f3ece92713a862dbd259b953448b013da214abd871de
    role: target
  - path: data/structures/ribonucleoprotein/90s_preribosome.yaml
    sha256: 06478162f1faeddbd339eb1e0088e6fc785361d828d2fdd448a6ff26be802ff5
    role: target
  - path: data/structures/ribonucleoprotein/bacterial_degradosome.yaml
    sha256: 4c76d3ac120bdfbce44b60a77dd984ede075c6879e91687e92d288dc6500f479
    role: target
  - path: data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml
    sha256: 7d7114176d9060702b20554665e0fb1b701894343d82f8677ee85540cf058b9e
    role: target
  - path: data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml
    sha256: 8624ea357233062f8239ffc2ee70c3ea23fbba7f17b5904682222afeb350e0be
    role: target
  - path: data/structures/ribonucleoprotein/box_h_aca_rnp_complex.yaml
    sha256: 064d6e829c5501ab736b0861e4ebd51283a27f5fe17a38b35a865d4bb7bad270
    role: target
  - path: data/structures/ribonucleoprotein/box_h_aca_snornp_complex.yaml
    sha256: 24e6a6d9574daa7a7e34ee47cce2a1fe92dbf6b6996d958619f296682183c366
    role: target
  - path: data/structures/ribonucleoprotein/cajal_body.yaml
    sha256: daab37f660890e5620e3f5490467181fd97a224be590d36bbe55624531df7c3f
    role: target
  - path: data/structures/ribonucleoprotein/catalytic_step_1_spliceosome.yaml
    sha256: 54c5245e0f562f380523ac714124086cb2cb0cc1746ba42f8a909ef9dd3733df
    role: target
  - path: data/structures/ribonucleoprotein/catalytic_step_2_spliceosome.yaml
    sha256: 799f8a9a7d948a6e31e6d289f88640a45ce2f13645e2ec69636b9cab857289e7
    role: target
  - path: data/structures/ribonucleoprotein/commitment_complex.yaml
    sha256: 77021ed979ddf15c8e7e05b5f90be02c8df4639195042d01bde3bdc14bd06b1a
    role: target
  - path: data/structures/ribonucleoprotein/cyanelle_ribonuclease_p_complex.yaml
    sha256: 6655ae638092e29503e13c65d79e79aced5a1c672c91a72e869e8334b1605444
    role: target
  - path: data/structures/ribonucleoprotein/cytoplasmic_exosome_rnase_complex.yaml
    sha256: 0af441121ac03143ac16285b44b015fb162498c037d9dc96c0a50368d8069629
    role: target
  - path: data/structures/ribonucleoprotein/cytoplasmic_stress_granule.yaml
    sha256: 4a236f1a12607b22e150138452d8a9d86799c7a24ae9aa5e4727b3b48be357e8
    role: target
  - path: data/structures/ribonucleoprotein/dimeric_ribonuclease_p_complex.yaml
    sha256: 174351d3d9904c3981fbc5ada5b03d9e34c23b9aca766a4c908106c0e51dd961
    role: target
  - path: data/structures/ribonucleoprotein/exosome_rnase_complex.yaml
    sha256: 8124093402b98ea3265af77e84179c40aa533e5fc9509c60edee9d92cce19e67
    role: target
  - path: data/structures/ribonucleoprotein/glycolytic_body.yaml
    sha256: d4fe5fd2cf71a1011acf41f4e24899bff2fea1dc09090c10ef405bb38391896b
    role: target
  - path: data/structures/ribonucleoprotein/h_body.yaml
    sha256: 362c852cc05cb880426858ec3392ac9fc297ebe50e9fa6f818c01bf6c8a92b8a
    role: target
  - path: data/structures/ribonucleoprotein/histone_locus_body.yaml
    sha256: 9b0387ffb6129251d28ed46be210629c43b25eb2486ae714e10b26258191d8e0
    role: target
  - path: data/structures/ribonucleoprotein/interchromatin_granule.yaml
    sha256: 416cf9a474cbcccf75230ad3da54ba2f24f3c3a076632ca9f50dc5434a3c99bb
    role: target
  - path: data/structures/ribonucleoprotein/large_ribosomal_subunit.yaml
    sha256: 21451ec54d296110a99defcccba7b341b7480014048fae67809c7f3965c5d564
    role: target
  - path: data/structures/ribonucleoprotein/lsm2_8_complex.yaml
    sha256: 84a166a2bb93ed9365e0f069c82e3290da690eec3055650ed868aa53549d6f1b
    role: target
  - path: data/structures/ribonucleoprotein/multimeric_ribonuclease_p_complex.yaml
    sha256: 9171efac1c121e7b9fd678033e6cce6eb4dd114e83781dc30669f80e02e9cc19
    role: target
  - path: data/structures/ribonucleoprotein/nuclear_dicing_body.yaml
    sha256: 06830ecab9e03c85d10f25c0de56e6ecdc3673f049e60d5dd063faa66f96434e
    role: target
  - path: data/structures/ribonucleoprotein/nuclear_exosome_rnase_complex.yaml
    sha256: 33ae59bdd36575cfe9cc51a81ec5b34c5fc7b27fa3368f2974c14564397e4461
    role: target
  - path: data/structures/ribonucleoprotein/nuclear_speck.yaml
    sha256: 4092954bba31991b3315cf5938c98fc4471ec52e0d7b7c0521d7a2243c7129ac
    role: target
  - path: data/structures/ribonucleoprotein/nuclear_stress_granule.yaml
    sha256: 83a1831312d846e8262224b0e4335e3c0597f5c940315ef51f3b9984bb15ac28
    role: target
  - path: data/structures/ribonucleoprotein/nucleolar_exosome_rnase_complex.yaml
    sha256: e9ef3e0e63493d5acbf0a3af0aa1c67914fedc1c71518fc3e58e93635de32718
    role: target
  - path: data/structures/ribonucleoprotein/nucleolar_ribonuclease_p_complex.yaml
    sha256: e066dfd5e0124a6696331ce7df711f6fe1178468dccef6fc1a41cbc7fb83d78b
    role: target
  - path: data/structures/ribonucleoprotein/omega_speckle.yaml
    sha256: b72db9421c9894f2631b3ee331dbd0cf32ee9ec18fc91b73e2fec342603bfa08
    role: target
  - path: data/structures/ribonucleoprotein/p_body.yaml
    sha256: 8939b9aaf42fdfc6b830bbede49cbebd87e2e6cd0e9868106daa0384000ca023
    role: target
  - path: data/structures/ribonucleoprotein/paraspeckles.yaml
    sha256: 28e0a4a9d403de7625a74120c14af7f8338d7fffa0c888aee1f25527998a177a
    role: target
  - path: data/structures/ribonucleoprotein/penta_snrnp_complex.yaml
    sha256: db10e79fc00b6a9bd3816bab414cb52f2a907213c180ffcd0006e0a271a55234
    role: target
  - path: data/structures/ribonucleoprotein/perinucleolar_compartment.yaml
    sha256: 19a65c0778b0368ea57fc78fae1ade03533e521e393b98aa993ee7f5f1bc2fb8
    role: target
  - path: data/structures/ribonucleoprotein/post_mrna_release_spliceosomal_complex.yaml
    sha256: b62ba51e1189f520e920647fd1aa3e633c7fa8f0212d695978be549329e15c41
    role: target
  - path: data/structures/ribonucleoprotein/post_spliceosomal_complex.yaml
    sha256: d1c3b9dc9037f9fe1f2e8c404bf1dbe9921221c2af12d6d4c16547bbe4272b40
    role: target
  - path: data/structures/ribonucleoprotein/precatalytic_spliceosome.yaml
    sha256: b077a76493be17ddf78dd5855c002c7fadd2ed4babe64cccccacb2bd29ef5a54
    role: target
  - path: data/structures/ribonucleoprotein/preribosome.yaml
    sha256: a2eca4a8562a3134aa2c62272acd573cae73d50c3ad6a71622da67e651e2dffd
    role: target
  - path: data/structures/ribonucleoprotein/preribosome_large_subunit_precursor.yaml
    sha256: 451a0264fca33d0b98a6c1b868375910771ea34b0da27723d738ebb9cf4ad341
    role: target
  - path: data/structures/ribonucleoprotein/preribosome_small_subunit_precursor.yaml
    sha256: d40a26fbbbec983858aa7aed7a3e28bfe6c726e3114b8664e4c282808a06007d
    role: target
  - path: data/structures/ribonucleoprotein/prespliceosome.yaml
    sha256: 0f15b0e0cd5d851a1742abceb635f860ba3642be194b489205fc6055dd6cff8e
    role: target
  - path: data/structures/ribonucleoprotein/ribonuclease_mrp_complex.yaml
    sha256: cf134484a14d0ccda4ab8dfe3e1fcf5d400a4688a8a5fa97b4f6830c1f93d78a
    role: target
  - path: data/structures/ribonucleoprotein/ribonuclease_p_complex.yaml
    sha256: 8276f65cb590dba2616161fd698414906f749043e9da43d685ca3cbcbb2bf26f
    role: target
  - path: data/structures/ribonucleoprotein/ribosome.yaml
    sha256: c5eedf782372b48b8355ab5387fad6df558b0c2a11769b5a3d28dcc7a43d0169
    role: target
  - path: data/structures/ribonucleoprotein/rnp_body.yaml
    sha256: cf7350e280e7e49db17d9218704f5190dbe6266f01aec01a7272e07f1e73637e
    role: target
  - path: data/structures/ribonucleoprotein/signal_recognition_particle.yaml
    sha256: eeedb955e7f7e66a346344322e164ed188a2943652229f801a007bdb79f84965
    role: target
  - path: data/structures/ribonucleoprotein/sl_snrnp.yaml
    sha256: 63f2a5aa72a61288335992c9ad6619c29261b850c5b18041dbf8261c137d15c8
    role: target
  - path: data/structures/ribonucleoprotein/small_nuclear_ribonucleoprotein_complex.yaml
    sha256: bd6852e21130a2bc707f03268d9cf6a6ec41759af20c88bc6fc048e0982c3619
    role: target
  - path: data/structures/ribonucleoprotein/small_ribosomal_subunit.yaml
    sha256: c8f72042a86bbb414b49e4f5bedf6724daff1d61a4ddcbe6e78e5aafa487a51f
    role: target
  - path: data/structures/ribonucleoprotein/small_subunit_processome.yaml
    sha256: 69311bd666ee58989f766c229862df5b989ccb9f669c3b98405a4c2c6b534f67
    role: target
  - path: data/structures/ribonucleoprotein/sno_s_rna_containing_ribonucleoprotein_complex.yaml
    sha256: a6812f54c07d73a4f3c3f75a4dc963124753c9910727358c655daa7d0d2cb72f
    role: target
  - path: data/structures/ribonucleoprotein/sphere_organelle.yaml
    sha256: e7bc9b8f97fc95789c25578ab9922b982d4577a1d651b4a9268884ff6d19e614
    role: target
  - path: data/structures/ribonucleoprotein/spliceosomal_complex.yaml
    sha256: 94e7122c1b1170de14184fd66be7f823726640cdcbff5b1a939cd99f28fd3eb7
    role: target
  - path: data/structures/ribonucleoprotein/spliceosomal_snrnp_complex.yaml
    sha256: 3a2312afb128bbe2b549b69a2859a553f77384ac7e2e97747f5c4f916e87f787
    role: target
  - path: data/structures/ribonucleoprotein/spliceosomal_tri_snrnp_complex.yaml
    sha256: 2c43c4bf7fb3e8507986e9447a4d4e635b61ba32d9c81b97ff1c113f80120bb2
    role: target
  - path: data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml
    sha256: f6a171b986c156afe089e0c906e9342d97262d424781b84c8edb831f7fcbd4b1
    role: target
  - path: data/structures/ribonucleoprotein/telomerase_holoenzyme_complex.yaml
    sha256: 6dc02897f786de1e9abea233cdd3013c3e318cbf1e8a143de0c472d23c1b8b19
    role: target
  - path: data/structures/ribonucleoprotein/tmar_condensate.yaml
    sha256: a39523447310f91e4851a261c7d1802c8e1fae44df697edba61a9c5fcbb7115c
    role: target
  - path: data/structures/ribonucleoprotein/trans_spliceosomal_complex.yaml
    sha256: b01c080f6da33fa028e69e74331f76eee2b8960d83f54aa29c2dc6c3e9049314
    role: target
  - path: data/structures/ribonucleoprotein/u11_snrnp.yaml
    sha256: b0148f234cc1d6d0775be9586ea43665a87ca3e2ea2d77ded4c35d6eac2933b4
    role: target
  - path: data/structures/ribonucleoprotein/u11_u12_snrnp.yaml
    sha256: 6c0d8cadb5d666015f1df4e6f938c2a18c0a3f72a01a530d9facdbbbf2436367
    role: target
  - path: data/structures/ribonucleoprotein/u12_snrnp.yaml
    sha256: 4bb416f8dd3a2a3bc5bec30bcd988d9ca8f76fcebf06296de26d4ac99330e8b5
    role: target
  - path: data/structures/ribonucleoprotein/u12_type_catalytic_step_1_spliceosome.yaml
    sha256: da3723937069b544bf74dd5be22224ac5efa25fdf6ac2422f4d697cde6974465
    role: target
  - path: data/structures/ribonucleoprotein/u12_type_catalytic_step_2_spliceosome.yaml
    sha256: 8a6a9d9f7b34a23fdf5cd79a7c73477c19da4f394444b410672930234bb26680
    role: target
  - path: data/structures/ribonucleoprotein/u12_type_post_mrna_release_spliceosomal_complex.yaml
    sha256: cfd38ffcb127336e743f0c2d646f0622d768226f7ad1666018bb400ba597b8a4
    role: target
  - path: data/structures/ribonucleoprotein/u12_type_post_spliceosomal_complex.yaml
    sha256: 63336b79bcdfc9f342bf04b3887d5df3a4b6a4e44453a1d5aa71963cf08a40f1
    role: target
  - path: data/structures/ribonucleoprotein/u12_type_precatalytic_spliceosome.yaml
    sha256: 2291af60a266d95fa01cba12744488e289120031a0297ef38691b484e4f1ee1a
    role: target
  - path: data/structures/ribonucleoprotein/u12_type_prespliceosome.yaml
    sha256: 2a66f7f248c63092f03df1959c23b307f0927ba24d9fbd18eca873fbc3b8ce2d
    role: target
  - path: data/structures/ribonucleoprotein/u12_type_spliceosomal_complex.yaml
    sha256: a7403ff4f9b9abab7fcf87a80be9410ac0a476e283b2fb0d57c7bdeaef0952b7
    role: target
  - path: data/structures/ribonucleoprotein/u1_snrnp.yaml
    sha256: d3b8874a178556b7554272a274444958476efbef57080fe1d9116c63d4cc09e6
    role: target
  - path: data/structures/ribonucleoprotein/u2_snrnp.yaml
    sha256: 97572a5e9e26fc0f84d744b068d9e1fa41068980f4546d9a61fa92cc2101d787
    role: target
  - path: data/structures/ribonucleoprotein/u2_type_catalytic_step_1_spliceosome.yaml
    sha256: 4b728b8e81a09ab0e981dc64c6a15227b7738b7054d757701592f2099fad2c15
    role: target
  - path: data/structures/ribonucleoprotein/u2_type_catalytic_step_2_spliceosome.yaml
    sha256: 8d9c43d3ac430da899592a2b23d24ab92a85c35abe587fefa406362481362bc0
    role: target
  - path: data/structures/ribonucleoprotein/u2_type_post_mrna_release_spliceosomal_complex.yaml
    sha256: 56e36656f3e564fdf6280118e9c6cdd30cd66853e0172e2482450b842e16c990
    role: target
  - path: data/structures/ribonucleoprotein/u2_type_post_spliceosomal_complex.yaml
    sha256: 4bc54c73c0f2334db1a8574f547c50ce86699ac26dd398b711e1954c131494ef
    role: target
  - path: data/structures/ribonucleoprotein/u2_type_precatalytic_spliceosome.yaml
    sha256: d13661fa02d95ce8dd1824149f56673dd30da881d08c80d0e6c5ba1089471286
    role: target
  - path: data/structures/ribonucleoprotein/u2_type_prespliceosome.yaml
    sha256: 8544eab88c99409755eb2965397ec1178303d096562ccc21dcdaf047b48156a8
    role: target
  - path: data/structures/ribonucleoprotein/u2_type_spliceosomal_complex.yaml
    sha256: 4da7e8682e996ec6aa955bf99762904aed85b80718bac4d142dda8b82c993d5a
    role: target
  - path: data/structures/ribonucleoprotein/u4_snrnp.yaml
    sha256: 74bbb882bfa4bbc944e56f4470621ab2b416cb592c13108061e06ec10e4cfb4f
    role: target
  - path: data/structures/ribonucleoprotein/u4_u6_snrnp.yaml
    sha256: c1a0c276cf93bfef0873ce9a42e164fad8eb6ebd617730199406a904d596f351
    role: target
  - path: data/structures/ribonucleoprotein/u4_u6_x_u5_tri_snrnp_complex.yaml
    sha256: df18e621fa9aac1c1a33b57da6be2c12177dbc0ce516b61fdc1cccdab3acff42
    role: target
  - path: data/structures/ribonucleoprotein/u4atac_snrnp.yaml
    sha256: b7b38e9f5f030df36058b3b7345e577a66db646d28283f2fad17992b9f17e75e
    role: target
  - path: data/structures/ribonucleoprotein/u4atac_u6atac_snrnp.yaml
    sha256: 4885763b21e1fce2410621a80e2c82fbf55df14d768d954e6cc80d97f4c4e81e
    role: target
  - path: data/structures/ribonucleoprotein/u4atac_u6atac_x_u5_tri_snrnp_complex.yaml
    sha256: 6e9bc0e63e7ee7f66801c44e12bf2aa614818c46572d1a7161cbc9b44be1fb96
    role: target
  - path: data/structures/ribonucleoprotein/u5_snrnp.yaml
    sha256: 397c8d7855f291a1ea8de9c7e54f10444eb5e5939a89e1c84fb599c88c81474d
    role: target
  - path: data/structures/ribonucleoprotein/u6_snrnp.yaml
    sha256: 652a728e4330632752071e98e43c9311fa56c9742f9b6ae4bbeba487e41f7bd4
    role: target
  - path: data/structures/ribonucleoprotein/u6atac_snrnp.yaml
    sha256: 12fa2e55ee0e0eaae3601befd3802453e2506ce3c6176894a0d9b648b599a54a
    role: target
  - path: data/structures/ribonucleoprotein/u7_snrnp.yaml
    sha256: c8ed5c6a031e5baef522efc89d0389d2d11db93d366f529c4800a2abf4d6c72a
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
  description: Full-cohort review of all 88 CellStructureRecord YAML files under data/structures/ribonucleoprotein/.
  selection: Complete folder cohort data/structures/ribonucleoprotein/*.yaml in the
    frozen 1,001-record Cycle 4 Stage 4 inventory.
  coverage: full
  population_size: 88
  reviewed_target_ids:
  - GO:0120259
  - GO:0030686
  - GO:1990061
  - GO:0031428
  - GO:0170049
  - GO:0072588
  - GO:0031429
  - GO:0015030
  - GO:0071012
  - GO:0071013
  - GO:0000243
  - GO:0030679
  - GO:0000177
  - GO:0010494
  - GO:0030680
  - GO:0000178
  - cellstructuremech:glycolytic_body
  - cellstructuremech:h_body
  - GO:0035363
  - GO:0035061
  - GO:0015934
  - GO:0120115
  - GO:0030681
  - GO:0010445
  - GO:0000176
  - GO:0016607
  - GO:0097165
  - GO:0101019
  - GO:0005655
  - GO:0035062
  - GO:0000932
  - GO:0042382
  - GO:0071003
  - GO:0097356
  - GO:0071014
  - GO:0071020
  - GO:0071011
  - GO:0030684
  - GO:0030687
  - GO:0030688
  - GO:0071010
  - GO:0000172
  - GO:0030677
  - GO:0005840
  - GO:0140365
  - GO:0048500
  - GO:0071024
  - GO:0030532
  - GO:0015935
  - GO:0032040
  - GO:0005732
  - GO:0071601
  - GO:0005681
  - GO:0097525
  - GO:0097526
  - GO:0044530
  - GO:0005697
  - cellstructuremech:tmar_condensate
  - GO:0071023
  - GO:0005692
  - GO:0034693
  - GO:0005693
  - GO:0071017
  - GO:0071018
  - GO:0071019
  - GO:0071022
  - GO:0071016
  - GO:0071015
  - GO:0005689
  - GO:0005685
  - GO:0005686
  - GO:0071006
  - GO:0071007
  - GO:0071008
  - GO:0071021
  - GO:0071005
  - GO:0071004
  - GO:0005684
  - GO:0005687
  - GO:0071001
  - GO:0046540
  - GO:0005690
  - GO:0071002
  - GO:0071009
  - GO:0005682
  - GO:0005688
  - GO:0005691
  - GO:0005683
targets:
- target_id: GO:0120259
  path: data/structures/ribonucleoprotein/7sk_snrnp.yaml
  label: 7SK snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e3e56d806c4898e643c8f3ece92713a862dbd259b953448b013da214abd871de
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/7sk_snrnp.yaml
    role: maintained_record
- target_id: GO:0030686
  path: data/structures/ribonucleoprotein/90s_preribosome.yaml
  label: 90S preribosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 06478162f1faeddbd339eb1e0088e6fc785361d828d2fdd448a6ff26be802ff5
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/90s_preribosome.yaml
    role: maintained_record
- target_id: GO:1990061
  path: data/structures/ribonucleoprotein/bacterial_degradosome.yaml
  label: bacterial degradosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4c76d3ac120bdfbce44b60a77dd984ede075c6879e91687e92d288dc6500f479
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/bacterial_degradosome.yaml
    role: maintained_record
- target_id: GO:0031428
  path: data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml
  label: box C/D methylation guide snoRNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7d7114176d9060702b20554665e0fb1b701894343d82f8677ee85540cf058b9e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml
    role: maintained_record
- target_id: GO:0170049
  path: data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml
  label: box C/D RNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8624ea357233062f8239ffc2ee70c3ea23fbba7f17b5904682222afeb350e0be
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml
    role: maintained_record
- target_id: GO:0072588
  path: data/structures/ribonucleoprotein/box_h_aca_rnp_complex.yaml
  label: box H/ACA RNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 064d6e829c5501ab736b0861e4ebd51283a27f5fe17a38b35a865d4bb7bad270
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/box_h_aca_rnp_complex.yaml
    role: maintained_record
- target_id: GO:0031429
  path: data/structures/ribonucleoprotein/box_h_aca_snornp_complex.yaml
  label: box H/ACA snoRNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 24e6a6d9574daa7a7e34ee47cce2a1fe92dbf6b6996d958619f296682183c366
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/box_h_aca_snornp_complex.yaml
    role: maintained_record
- target_id: GO:0015030
  path: data/structures/ribonucleoprotein/cajal_body.yaml
  label: Cajal body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: daab37f660890e5620e3f5490467181fd97a224be590d36bbe55624531df7c3f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/cajal_body.yaml
    role: maintained_record
- target_id: GO:0071012
  path: data/structures/ribonucleoprotein/catalytic_step_1_spliceosome.yaml
  label: catalytic step 1 spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 54c5245e0f562f380523ac714124086cb2cb0cc1746ba42f8a909ef9dd3733df
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/catalytic_step_1_spliceosome.yaml
    role: maintained_record
- target_id: GO:0071013
  path: data/structures/ribonucleoprotein/catalytic_step_2_spliceosome.yaml
  label: catalytic step 2 spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 799f8a9a7d948a6e31e6d289f88640a45ce2f13645e2ec69636b9cab857289e7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/catalytic_step_2_spliceosome.yaml
    role: maintained_record
- target_id: GO:0000243
  path: data/structures/ribonucleoprotein/commitment_complex.yaml
  label: commitment complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 77021ed979ddf15c8e7e05b5f90be02c8df4639195042d01bde3bdc14bd06b1a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/commitment_complex.yaml
    role: maintained_record
- target_id: GO:0030679
  path: data/structures/ribonucleoprotein/cyanelle_ribonuclease_p_complex.yaml
  label: cyanelle ribonuclease P complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6655ae638092e29503e13c65d79e79aced5a1c672c91a72e869e8334b1605444
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/cyanelle_ribonuclease_p_complex.yaml
    role: maintained_record
- target_id: GO:0000177
  path: data/structures/ribonucleoprotein/cytoplasmic_exosome_rnase_complex.yaml
  label: cytoplasmic exosome (RNase complex)
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0af441121ac03143ac16285b44b015fb162498c037d9dc96c0a50368d8069629
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/cytoplasmic_exosome_rnase_complex.yaml
    role: maintained_record
- target_id: GO:0010494
  path: data/structures/ribonucleoprotein/cytoplasmic_stress_granule.yaml
  label: cytoplasmic stress granule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4a236f1a12607b22e150138452d8a9d86799c7a24ae9aa5e4727b3b48be357e8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/cytoplasmic_stress_granule.yaml
    role: maintained_record
- target_id: GO:0030680
  path: data/structures/ribonucleoprotein/dimeric_ribonuclease_p_complex.yaml
  label: dimeric ribonuclease P complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 174351d3d9904c3981fbc5ada5b03d9e34c23b9aca766a4c908106c0e51dd961
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/dimeric_ribonuclease_p_complex.yaml
    role: maintained_record
- target_id: GO:0000178
  path: data/structures/ribonucleoprotein/exosome_rnase_complex.yaml
  label: exosome (RNase complex)
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8124093402b98ea3265af77e84179c40aa533e5fc9509c60edee9d92cce19e67
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/exosome_rnase_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:glycolytic_body
  path: data/structures/ribonucleoprotein/glycolytic_body.yaml
  label: glycolytic body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d4fe5fd2cf71a1011acf41f4e24899bff2fea1dc09090c10ef405bb38391896b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/glycolytic_body.yaml
    role: maintained_record
- target_id: cellstructuremech:h_body
  path: data/structures/ribonucleoprotein/h_body.yaml
  label: H-body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 362c852cc05cb880426858ec3392ac9fc297ebe50e9fa6f818c01bf6c8a92b8a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/h_body.yaml
    role: maintained_record
- target_id: GO:0035363
  path: data/structures/ribonucleoprotein/histone_locus_body.yaml
  label: histone locus body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9b0387ffb6129251d28ed46be210629c43b25eb2486ae714e10b26258191d8e0
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/histone_locus_body.yaml
    role: maintained_record
- target_id: GO:0035061
  path: data/structures/ribonucleoprotein/interchromatin_granule.yaml
  label: interchromatin granule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 416cf9a474cbcccf75230ad3da54ba2f24f3c3a076632ca9f50dc5434a3c99bb
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/interchromatin_granule.yaml
    role: maintained_record
- target_id: GO:0015934
  path: data/structures/ribonucleoprotein/large_ribosomal_subunit.yaml
  label: large ribosomal subunit
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 21451ec54d296110a99defcccba7b341b7480014048fae67809c7f3965c5d564
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/large_ribosomal_subunit.yaml
    role: maintained_record
- target_id: GO:0120115
  path: data/structures/ribonucleoprotein/lsm2_8_complex.yaml
  label: Lsm2-8 complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 84a166a2bb93ed9365e0f069c82e3290da690eec3055650ed868aa53549d6f1b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/lsm2_8_complex.yaml
    role: maintained_record
- target_id: GO:0030681
  path: data/structures/ribonucleoprotein/multimeric_ribonuclease_p_complex.yaml
  label: multimeric ribonuclease P complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9171efac1c121e7b9fd678033e6cce6eb4dd114e83781dc30669f80e02e9cc19
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/multimeric_ribonuclease_p_complex.yaml
    role: maintained_record
- target_id: GO:0010445
  path: data/structures/ribonucleoprotein/nuclear_dicing_body.yaml
  label: nuclear dicing body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 06830ecab9e03c85d10f25c0de56e6ecdc3673f049e60d5dd063faa66f96434e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/nuclear_dicing_body.yaml
    role: maintained_record
- target_id: GO:0000176
  path: data/structures/ribonucleoprotein/nuclear_exosome_rnase_complex.yaml
  label: nuclear exosome (RNase complex)
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 33ae59bdd36575cfe9cc51a81ec5b34c5fc7b27fa3368f2974c14564397e4461
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/nuclear_exosome_rnase_complex.yaml
    role: maintained_record
- target_id: GO:0016607
  path: data/structures/ribonucleoprotein/nuclear_speck.yaml
  label: nuclear speck
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4092954bba31991b3315cf5938c98fc4471ec52e0d7b7c0521d7a2243c7129ac
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/nuclear_speck.yaml
    role: maintained_record
- target_id: GO:0097165
  path: data/structures/ribonucleoprotein/nuclear_stress_granule.yaml
  label: nuclear stress granule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 83a1831312d846e8262224b0e4335e3c0597f5c940315ef51f3b9984bb15ac28
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/nuclear_stress_granule.yaml
    role: maintained_record
- target_id: GO:0101019
  path: data/structures/ribonucleoprotein/nucleolar_exosome_rnase_complex.yaml
  label: nucleolar exosome (RNase complex)
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e9ef3e0e63493d5acbf0a3af0aa1c67914fedc1c71518fc3e58e93635de32718
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/nucleolar_exosome_rnase_complex.yaml
    role: maintained_record
- target_id: GO:0005655
  path: data/structures/ribonucleoprotein/nucleolar_ribonuclease_p_complex.yaml
  label: nucleolar ribonuclease P complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e066dfd5e0124a6696331ce7df711f6fe1178468dccef6fc1a41cbc7fb83d78b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/nucleolar_ribonuclease_p_complex.yaml
    role: maintained_record
- target_id: GO:0035062
  path: data/structures/ribonucleoprotein/omega_speckle.yaml
  label: omega speckle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b72db9421c9894f2631b3ee331dbd0cf32ee9ec18fc91b73e2fec342603bfa08
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/omega_speckle.yaml
    role: maintained_record
- target_id: GO:0000932
  path: data/structures/ribonucleoprotein/p_body.yaml
  label: P-body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8939b9aaf42fdfc6b830bbede49cbebd87e2e6cd0e9868106daa0384000ca023
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/p_body.yaml
    role: maintained_record
- target_id: GO:0042382
  path: data/structures/ribonucleoprotein/paraspeckles.yaml
  label: paraspeckles
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 28e0a4a9d403de7625a74120c14af7f8338d7fffa0c888aee1f25527998a177a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/paraspeckles.yaml
    role: maintained_record
- target_id: GO:0071003
  path: data/structures/ribonucleoprotein/penta_snrnp_complex.yaml
  label: penta-snRNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: db10e79fc00b6a9bd3816bab414cb52f2a907213c180ffcd0006e0a271a55234
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/penta_snrnp_complex.yaml
    role: maintained_record
- target_id: GO:0097356
  path: data/structures/ribonucleoprotein/perinucleolar_compartment.yaml
  label: perinucleolar compartment
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 19a65c0778b0368ea57fc78fae1ade03533e521e393b98aa993ee7f5f1bc2fb8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/perinucleolar_compartment.yaml
    role: maintained_record
- target_id: GO:0071014
  path: data/structures/ribonucleoprotein/post_mrna_release_spliceosomal_complex.yaml
  label: post-mRNA release spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b62ba51e1189f520e920647fd1aa3e633c7fa8f0212d695978be549329e15c41
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/post_mrna_release_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0071020
  path: data/structures/ribonucleoprotein/post_spliceosomal_complex.yaml
  label: post-spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d1c3b9dc9037f9fe1f2e8c404bf1dbe9921221c2af12d6d4c16547bbe4272b40
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/post_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0071011
  path: data/structures/ribonucleoprotein/precatalytic_spliceosome.yaml
  label: precatalytic spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b077a76493be17ddf78dd5855c002c7fadd2ed4babe64cccccacb2bd29ef5a54
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/precatalytic_spliceosome.yaml
    role: maintained_record
- target_id: GO:0030684
  path: data/structures/ribonucleoprotein/preribosome.yaml
  label: preribosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a2eca4a8562a3134aa2c62272acd573cae73d50c3ad6a71622da67e651e2dffd
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/preribosome.yaml
    role: maintained_record
- target_id: GO:0030687
  path: data/structures/ribonucleoprotein/preribosome_large_subunit_precursor.yaml
  label: preribosome, large subunit precursor
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 451a0264fca33d0b98a6c1b868375910771ea34b0da27723d738ebb9cf4ad341
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/preribosome_large_subunit_precursor.yaml
    role: maintained_record
- target_id: GO:0030688
  path: data/structures/ribonucleoprotein/preribosome_small_subunit_precursor.yaml
  label: preribosome, small subunit precursor
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d40a26fbbbec983858aa7aed7a3e28bfe6c726e3114b8664e4c282808a06007d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/preribosome_small_subunit_precursor.yaml
    role: maintained_record
- target_id: GO:0071010
  path: data/structures/ribonucleoprotein/prespliceosome.yaml
  label: prespliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0f15b0e0cd5d851a1742abceb635f860ba3642be194b489205fc6055dd6cff8e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/prespliceosome.yaml
    role: maintained_record
- target_id: GO:0000172
  path: data/structures/ribonucleoprotein/ribonuclease_mrp_complex.yaml
  label: ribonuclease MRP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: cf134484a14d0ccda4ab8dfe3e1fcf5d400a4688a8a5fa97b4f6830c1f93d78a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/ribonuclease_mrp_complex.yaml
    role: maintained_record
- target_id: GO:0030677
  path: data/structures/ribonucleoprotein/ribonuclease_p_complex.yaml
  label: ribonuclease P complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8276f65cb590dba2616161fd698414906f749043e9da43d685ca3cbcbb2bf26f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/ribonuclease_p_complex.yaml
    role: maintained_record
- target_id: GO:0005840
  path: data/structures/ribonucleoprotein/ribosome.yaml
  label: ribosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c5eedf782372b48b8355ab5387fad6df558b0c2a11769b5a3d28dcc7a43d0169
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/ribosome.yaml
    role: maintained_record
- target_id: GO:0140365
  path: data/structures/ribonucleoprotein/rnp_body.yaml
  label: RNP body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: cf7350e280e7e49db17d9218704f5190dbe6266f01aec01a7272e07f1e73637e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/rnp_body.yaml
    role: maintained_record
- target_id: GO:0048500
  path: data/structures/ribonucleoprotein/signal_recognition_particle.yaml
  label: signal recognition particle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: eeedb955e7f7e66a346344322e164ed188a2943652229f801a007bdb79f84965
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/signal_recognition_particle.yaml
    role: maintained_record
- target_id: GO:0071024
  path: data/structures/ribonucleoprotein/sl_snrnp.yaml
  label: SL snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 63f2a5aa72a61288335992c9ad6619c29261b850c5b18041dbf8261c137d15c8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/sl_snrnp.yaml
    role: maintained_record
- target_id: GO:0030532
  path: data/structures/ribonucleoprotein/small_nuclear_ribonucleoprotein_complex.yaml
  label: small nuclear ribonucleoprotein complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: bd6852e21130a2bc707f03268d9cf6a6ec41759af20c88bc6fc048e0982c3619
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/small_nuclear_ribonucleoprotein_complex.yaml
    role: maintained_record
- target_id: GO:0015935
  path: data/structures/ribonucleoprotein/small_ribosomal_subunit.yaml
  label: small ribosomal subunit
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c8f72042a86bbb414b49e4f5bedf6724daff1d61a4ddcbe6e78e5aafa487a51f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/small_ribosomal_subunit.yaml
    role: maintained_record
- target_id: GO:0032040
  path: data/structures/ribonucleoprotein/small_subunit_processome.yaml
  label: small-subunit processome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 69311bd666ee58989f766c229862df5b989ccb9f669c3b98405a4c2c6b534f67
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/small_subunit_processome.yaml
    role: maintained_record
- target_id: GO:0005732
  path: data/structures/ribonucleoprotein/sno_s_rna_containing_ribonucleoprotein_complex.yaml
  label: sno(s)RNA-containing ribonucleoprotein complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a6812f54c07d73a4f3c3f75a4dc963124753c9910727358c655daa7d0d2cb72f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/sno_s_rna_containing_ribonucleoprotein_complex.yaml
    role: maintained_record
- target_id: GO:0071601
  path: data/structures/ribonucleoprotein/sphere_organelle.yaml
  label: sphere organelle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e7bc9b8f97fc95789c25578ab9922b982d4577a1d651b4a9268884ff6d19e614
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/sphere_organelle.yaml
    role: maintained_record
- target_id: GO:0005681
  path: data/structures/ribonucleoprotein/spliceosomal_complex.yaml
  label: spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 94e7122c1b1170de14184fd66be7f823726640cdcbff5b1a939cd99f28fd3eb7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0097525
  path: data/structures/ribonucleoprotein/spliceosomal_snrnp_complex.yaml
  label: spliceosomal snRNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3a2312afb128bbe2b549b69a2859a553f77384ac7e2e97747f5c4f916e87f787
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/spliceosomal_snrnp_complex.yaml
    role: maintained_record
- target_id: GO:0097526
  path: data/structures/ribonucleoprotein/spliceosomal_tri_snrnp_complex.yaml
  label: spliceosomal tri-snRNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2c43c4bf7fb3e8507986e9447a4d4e635b61ba32d9c81b97ff1c113f80120bb2
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/spliceosomal_tri_snrnp_complex.yaml
    role: maintained_record
- target_id: GO:0044530
  path: data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml
  label: supraspliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f6a171b986c156afe089e0c906e9342d97262d424781b84c8edb831f7fcbd4b1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0005697
  path: data/structures/ribonucleoprotein/telomerase_holoenzyme_complex.yaml
  label: telomerase holoenzyme complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6dc02897f786de1e9abea233cdd3013c3e318cbf1e8a143de0c472d23c1b8b19
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/telomerase_holoenzyme_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:tmar_condensate
  path: data/structures/ribonucleoprotein/tmar_condensate.yaml
  label: TmaR condensate
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a39523447310f91e4851a261c7d1802c8e1fae44df697edba61a9c5fcbb7115c
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/tmar_condensate.yaml
    role: maintained_record
- target_id: GO:0071023
  path: data/structures/ribonucleoprotein/trans_spliceosomal_complex.yaml
  label: trans spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b01c080f6da33fa028e69e74331f76eee2b8960d83f54aa29c2dc6c3e9049314
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/trans_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0005692
  path: data/structures/ribonucleoprotein/u11_snrnp.yaml
  label: U11 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b0148f234cc1d6d0775be9586ea43665a87ca3e2ea2d77ded4c35d6eac2933b4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u11_snrnp.yaml
    role: maintained_record
- target_id: GO:0034693
  path: data/structures/ribonucleoprotein/u11_u12_snrnp.yaml
  label: U11/U12 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6c0d8cadb5d666015f1df4e6f938c2a18c0a3f72a01a530d9facdbbbf2436367
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u11_u12_snrnp.yaml
    role: maintained_record
- target_id: GO:0005693
  path: data/structures/ribonucleoprotein/u12_snrnp.yaml
  label: U12 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4bb416f8dd3a2a3bc5bec30bcd988d9ca8f76fcebf06296de26d4ac99330e8b5
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u12_snrnp.yaml
    role: maintained_record
- target_id: GO:0071017
  path: data/structures/ribonucleoprotein/u12_type_catalytic_step_1_spliceosome.yaml
  label: U12-type catalytic step 1 spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: da3723937069b544bf74dd5be22224ac5efa25fdf6ac2422f4d697cde6974465
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u12_type_catalytic_step_1_spliceosome.yaml
    role: maintained_record
- target_id: GO:0071018
  path: data/structures/ribonucleoprotein/u12_type_catalytic_step_2_spliceosome.yaml
  label: U12-type catalytic step 2 spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8a6a9d9f7b34a23fdf5cd79a7c73477c19da4f394444b410672930234bb26680
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u12_type_catalytic_step_2_spliceosome.yaml
    role: maintained_record
- target_id: GO:0071019
  path: data/structures/ribonucleoprotein/u12_type_post_mrna_release_spliceosomal_complex.yaml
  label: U12-type post-mRNA release spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: cfd38ffcb127336e743f0c2d646f0622d768226f7ad1666018bb400ba597b8a4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u12_type_post_mrna_release_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0071022
  path: data/structures/ribonucleoprotein/u12_type_post_spliceosomal_complex.yaml
  label: U12-type post-spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 63336b79bcdfc9f342bf04b3887d5df3a4b6a4e44453a1d5aa71963cf08a40f1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u12_type_post_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0071016
  path: data/structures/ribonucleoprotein/u12_type_precatalytic_spliceosome.yaml
  label: U12-type precatalytic spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2291af60a266d95fa01cba12744488e289120031a0297ef38691b484e4f1ee1a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u12_type_precatalytic_spliceosome.yaml
    role: maintained_record
- target_id: GO:0071015
  path: data/structures/ribonucleoprotein/u12_type_prespliceosome.yaml
  label: U12-type prespliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2a66f7f248c63092f03df1959c23b307f0927ba24d9fbd18eca873fbc3b8ce2d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u12_type_prespliceosome.yaml
    role: maintained_record
- target_id: GO:0005689
  path: data/structures/ribonucleoprotein/u12_type_spliceosomal_complex.yaml
  label: U12-type spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a7403ff4f9b9abab7fcf87a80be9410ac0a476e283b2fb0d57c7bdeaef0952b7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u12_type_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0005685
  path: data/structures/ribonucleoprotein/u1_snrnp.yaml
  label: U1 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d3b8874a178556b7554272a274444958476efbef57080fe1d9116c63d4cc09e6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u1_snrnp.yaml
    role: maintained_record
- target_id: GO:0005686
  path: data/structures/ribonucleoprotein/u2_snrnp.yaml
  label: U2 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 97572a5e9e26fc0f84d744b068d9e1fa41068980f4546d9a61fa92cc2101d787
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u2_snrnp.yaml
    role: maintained_record
- target_id: GO:0071006
  path: data/structures/ribonucleoprotein/u2_type_catalytic_step_1_spliceosome.yaml
  label: U2-type catalytic step 1 spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4b728b8e81a09ab0e981dc64c6a15227b7738b7054d757701592f2099fad2c15
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u2_type_catalytic_step_1_spliceosome.yaml
    role: maintained_record
- target_id: GO:0071007
  path: data/structures/ribonucleoprotein/u2_type_catalytic_step_2_spliceosome.yaml
  label: U2-type catalytic step 2 spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8d9c43d3ac430da899592a2b23d24ab92a85c35abe587fefa406362481362bc0
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u2_type_catalytic_step_2_spliceosome.yaml
    role: maintained_record
- target_id: GO:0071008
  path: data/structures/ribonucleoprotein/u2_type_post_mrna_release_spliceosomal_complex.yaml
  label: U2-type post-mRNA release spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 56e36656f3e564fdf6280118e9c6cdd30cd66853e0172e2482450b842e16c990
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u2_type_post_mrna_release_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0071021
  path: data/structures/ribonucleoprotein/u2_type_post_spliceosomal_complex.yaml
  label: U2-type post-spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4bc54c73c0f2334db1a8574f547c50ce86699ac26dd398b711e1954c131494ef
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u2_type_post_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0071005
  path: data/structures/ribonucleoprotein/u2_type_precatalytic_spliceosome.yaml
  label: U2-type precatalytic spliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d13661fa02d95ce8dd1824149f56673dd30da881d08c80d0e6c5ba1089471286
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u2_type_precatalytic_spliceosome.yaml
    role: maintained_record
- target_id: GO:0071004
  path: data/structures/ribonucleoprotein/u2_type_prespliceosome.yaml
  label: U2-type prespliceosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8544eab88c99409755eb2965397ec1178303d096562ccc21dcdaf047b48156a8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u2_type_prespliceosome.yaml
    role: maintained_record
- target_id: GO:0005684
  path: data/structures/ribonucleoprotein/u2_type_spliceosomal_complex.yaml
  label: U2-type spliceosomal complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4da7e8682e996ec6aa955bf99762904aed85b80718bac4d142dda8b82c993d5a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u2_type_spliceosomal_complex.yaml
    role: maintained_record
- target_id: GO:0005687
  path: data/structures/ribonucleoprotein/u4_snrnp.yaml
  label: U4 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 74bbb882bfa4bbc944e56f4470621ab2b416cb592c13108061e06ec10e4cfb4f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u4_snrnp.yaml
    role: maintained_record
- target_id: GO:0071001
  path: data/structures/ribonucleoprotein/u4_u6_snrnp.yaml
  label: U4/U6 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c1a0c276cf93bfef0873ce9a42e164fad8eb6ebd617730199406a904d596f351
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u4_u6_snrnp.yaml
    role: maintained_record
- target_id: GO:0046540
  path: data/structures/ribonucleoprotein/u4_u6_x_u5_tri_snrnp_complex.yaml
  label: U4/U6 x U5 tri-snRNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: df18e621fa9aac1c1a33b57da6be2c12177dbc0ce516b61fdc1cccdab3acff42
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u4_u6_x_u5_tri_snrnp_complex.yaml
    role: maintained_record
- target_id: GO:0005690
  path: data/structures/ribonucleoprotein/u4atac_snrnp.yaml
  label: U4atac snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b7b38e9f5f030df36058b3b7345e577a66db646d28283f2fad17992b9f17e75e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u4atac_snrnp.yaml
    role: maintained_record
- target_id: GO:0071002
  path: data/structures/ribonucleoprotein/u4atac_u6atac_snrnp.yaml
  label: U4atac/U6atac snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4885763b21e1fce2410621a80e2c82fbf55df14d768d954e6cc80d97f4c4e81e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u4atac_u6atac_snrnp.yaml
    role: maintained_record
- target_id: GO:0071009
  path: data/structures/ribonucleoprotein/u4atac_u6atac_x_u5_tri_snrnp_complex.yaml
  label: U4atac/U6atac x U5 tri-snRNP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6e9bc0e63e7ee7f66801c44e12bf2aa614818c46572d1a7161cbc9b44be1fb96
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u4atac_u6atac_x_u5_tri_snrnp_complex.yaml
    role: maintained_record
- target_id: GO:0005682
  path: data/structures/ribonucleoprotein/u5_snrnp.yaml
  label: U5 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 397c8d7855f291a1ea8de9c7e54f10444eb5e5939a89e1c84fb599c88c81474d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u5_snrnp.yaml
    role: maintained_record
- target_id: GO:0005688
  path: data/structures/ribonucleoprotein/u6_snrnp.yaml
  label: U6 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 652a728e4330632752071e98e43c9311fa56c9742f9b6ae4bbeba487e41f7bd4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u6_snrnp.yaml
    role: maintained_record
- target_id: GO:0005691
  path: data/structures/ribonucleoprotein/u6atac_snrnp.yaml
  label: U6atac snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 12fa2e55ee0e0eaae3601befd3802453e2506ce3c6176894a0d9b648b599a54a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u6atac_snrnp.yaml
    role: maintained_record
- target_id: GO:0005683
  path: data/structures/ribonucleoprotein/u7_snrnp.yaml
  label: U7 snRNP
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c8ed5c6a031e5baef522efc89d0389d2d11db93d366f529c4800a2abf4d6c72a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/u7_snrnp.yaml
    role: maintained_record
checks:
- check_id: strict_ribonucleoprotein
  name: Strict corpus validation covering ribonucleoprotein cohort
  status: passed
  required: true
  summary: All 88 ribonucleoprotein records pass strict LinkML and semantic validation.
  target_ids:
  - GO:0120259
  - GO:0030686
  - GO:1990061
  - GO:0031428
  - GO:0170049
  - GO:0072588
  - GO:0031429
  - GO:0015030
  - GO:0071012
  - GO:0071013
  - GO:0000243
  - GO:0030679
  - GO:0000177
  - GO:0010494
  - GO:0030680
  - GO:0000178
  - cellstructuremech:glycolytic_body
  - cellstructuremech:h_body
  - GO:0035363
  - GO:0035061
  - GO:0015934
  - GO:0120115
  - GO:0030681
  - GO:0010445
  - GO:0000176
  - GO:0016607
  - GO:0097165
  - GO:0101019
  - GO:0005655
  - GO:0035062
  - GO:0000932
  - GO:0042382
  - GO:0071003
  - GO:0097356
  - GO:0071014
  - GO:0071020
  - GO:0071011
  - GO:0030684
  - GO:0030687
  - GO:0030688
  - GO:0071010
  - GO:0000172
  - GO:0030677
  - GO:0005840
  - GO:0140365
  - GO:0048500
  - GO:0071024
  - GO:0030532
  - GO:0015935
  - GO:0032040
  - GO:0005732
  - GO:0071601
  - GO:0005681
  - GO:0097525
  - GO:0097526
  - GO:0044530
  - GO:0005697
  - cellstructuremech:tmar_condensate
  - GO:0071023
  - GO:0005692
  - GO:0034693
  - GO:0005693
  - GO:0071017
  - GO:0071018
  - GO:0071019
  - GO:0071022
  - GO:0071016
  - GO:0071015
  - GO:0005689
  - GO:0005685
  - GO:0005686
  - GO:0071006
  - GO:0071007
  - GO:0071008
  - GO:0071021
  - GO:0071005
  - GO:0071004
  - GO:0005684
  - GO:0005687
  - GO:0071001
  - GO:0046540
  - GO:0005690
  - GO:0071002
  - GO:0071009
  - GO:0005682
  - GO:0005688
  - GO:0005691
  - GO:0005683
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_ribonucleoprotein
- check_id: history_ribonucleoprotein
  name: History ledger validation covering ribonucleoprotein cohort
  status: passed
  required: true
  summary: All history ledger records covering ribonucleoprotein validate cleanly.
  target_ids:
  - GO:0120259
  - GO:0030686
  - GO:1990061
  - GO:0031428
  - GO:0170049
  - GO:0072588
  - GO:0031429
  - GO:0015030
  - GO:0071012
  - GO:0071013
  - GO:0000243
  - GO:0030679
  - GO:0000177
  - GO:0010494
  - GO:0030680
  - GO:0000178
  - cellstructuremech:glycolytic_body
  - cellstructuremech:h_body
  - GO:0035363
  - GO:0035061
  - GO:0015934
  - GO:0120115
  - GO:0030681
  - GO:0010445
  - GO:0000176
  - GO:0016607
  - GO:0097165
  - GO:0101019
  - GO:0005655
  - GO:0035062
  - GO:0000932
  - GO:0042382
  - GO:0071003
  - GO:0097356
  - GO:0071014
  - GO:0071020
  - GO:0071011
  - GO:0030684
  - GO:0030687
  - GO:0030688
  - GO:0071010
  - GO:0000172
  - GO:0030677
  - GO:0005840
  - GO:0140365
  - GO:0048500
  - GO:0071024
  - GO:0030532
  - GO:0015935
  - GO:0032040
  - GO:0005732
  - GO:0071601
  - GO:0005681
  - GO:0097525
  - GO:0097526
  - GO:0044530
  - GO:0005697
  - cellstructuremech:tmar_condensate
  - GO:0071023
  - GO:0005692
  - GO:0034693
  - GO:0005693
  - GO:0071017
  - GO:0071018
  - GO:0071019
  - GO:0071022
  - GO:0071016
  - GO:0071015
  - GO:0005689
  - GO:0005685
  - GO:0005686
  - GO:0071006
  - GO:0071007
  - GO:0071008
  - GO:0071021
  - GO:0071005
  - GO:0071004
  - GO:0005684
  - GO:0005687
  - GO:0071001
  - GO:0046540
  - GO:0005690
  - GO:0071002
  - GO:0071009
  - GO:0005682
  - GO:0005688
  - GO:0005691
  - GO:0005683
  command: .venv/bin/python scripts/validate_history.py
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_history_ribonucleoprotein
evidence:
- evidence_id: ev_strict_ribonucleoprotein
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict_all receipt
  accessed_at: '2026-10-30T08:20:10Z'
  support: supports
  summary: validate_strict.py exited 0 across all 1,001 records including all 88 ribonucleoprotein
    records.
  snapshot_sha256: 1ebf6e7daebc19797861570fcac0d3cf8b06c18f7f40abf3277d35ef5867f442
- evidence_id: ev_history_ribonucleoprotein
  kind: validation
  reference: scripts/validate_history.py
  locator: history_all receipt
  accessed_at: '2026-10-30T08:20:10Z'
  support: supports
  summary: validate_history.py exited 0 across all 2,082 history records covering
    ribonucleoprotein.
  snapshot_sha256: 8bcb91b216ec775bac08188426f9ef860888b78f91561be1e471ea4a2159ad3b
- evidence_id: ev_rnp_supraspliceosome
  kind: record_content
  reference: data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml
  locator: parent_structures (lines 11-13) and components[0] (lines 25-33)
  accessed_at: '2026-10-30T08:17:00Z'
  support: supports
  summary: supraspliceosomal_complex.yaml lists GO:0005681 in parent_structures and
    also as CONSTITUENT component spliceosomal_complex (stoichiometry '4') without
    has_part.
  quote: "parent_structures:\n- GO:0005681\n- GO:1990904\n...\n- id: spliceosomal_complex\n\
    \  label: Native spliceosome monomer\n  component_type: PROTEIN_COMPLEX\n  component_role:\
    \ CONSTITUENT\n  stoichiometry: '4'\n  grounding: GO:0005681"
  snapshot_sha256: f6a171b986c156afe089e0c906e9342d97262d424781b84c8edb831f7fcbd4b1
- evidence_id: ev_rnp_boxcd_guide
  kind: record_content
  reference: data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml
  locator: components[1] (lines 38-47)
  accessed_at: '2026-10-30T08:17:00Z'
  support: supports
  summary: box_c_d_methylation_guide_snornp_complex.yaml types 4-subunit nop1_nop56_nop58_snu13_core
    ([NOP1, NOP56, NOP58, SNU13]) as PROTEIN.
  quote: 'id: nop1_nop56_nop58_snu13_core

    label: Nop1/Nop56/Nop58/Snu13 core protein subcomplex

    component_type: PROTEIN

    component_role: CATALYTIC

    gene_symbols:

    - NOP1

    - NOP56

    - NOP58

    - SNU13'
  snapshot_sha256: 7d7114176d9060702b20554665e0fb1b701894343d82f8677ee85540cf058b9e
- evidence_id: ev_rnp_boxcd_notes
  kind: record_content
  reference: data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml
  locator: components[1].protein_examples[2,3].evidence[0] (lines 90-108)
  accessed_at: '2026-10-30T08:17:00Z'
  support: supports
  summary: box_c_d_rnp_complex.yaml components[1].protein_examples[2,3].evidence[0].notes
    concatenate Gautier T et al. 1997 and Wu P et al. 1998 on single-PMID entries.
  quote: "reference: PMID:9632712\nnotes: Gautier T et al. 1997 (Mol Cell Biol) and\
    \ Lafontaine DL & Tollervey D 1999\n  (RNA); Wu P et al. 1998 (Genes Dev)"
  snapshot_sha256: 8624ea357233062f8239ffc2ee70c3ea23fbba7f17b5904682222afeb350e0be
assessments:
- assessment_id: assess_ribonucleoprotein_cohort
  area: scope
  topic: Identity, boundaries, causal graphs, and ontology grounding across data/structures/ribonucleoprotein/
  outcome: supported
  summary: All 88 records in data/structures/ribonucleoprotein/ represent distinct
    microbial cell structures or subcomplexes with valid schema and history provenance.
  target_ids:
  - GO:0120259
  - GO:0030686
  - GO:1990061
  - GO:0031428
  - GO:0170049
  - GO:0072588
  - GO:0031429
  - GO:0015030
  - GO:0071012
  - GO:0071013
  - GO:0000243
  - GO:0030679
  - GO:0000177
  - GO:0010494
  - GO:0030680
  - GO:0000178
  - cellstructuremech:glycolytic_body
  - cellstructuremech:h_body
  - GO:0035363
  - GO:0035061
  - GO:0015934
  - GO:0120115
  - GO:0030681
  - GO:0010445
  - GO:0000176
  - GO:0016607
  - GO:0097165
  - GO:0101019
  - GO:0005655
  - GO:0035062
  - GO:0000932
  - GO:0042382
  - GO:0071003
  - GO:0097356
  - GO:0071014
  - GO:0071020
  - GO:0071011
  - GO:0030684
  - GO:0030687
  - GO:0030688
  - GO:0071010
  - GO:0000172
  - GO:0030677
  - GO:0005840
  - GO:0140365
  - GO:0048500
  - GO:0071024
  - GO:0030532
  - GO:0015935
  - GO:0032040
  - GO:0005732
  - GO:0071601
  - GO:0005681
  - GO:0097525
  - GO:0097526
  - GO:0044530
  - GO:0005697
  - cellstructuremech:tmar_condensate
  - GO:0071023
  - GO:0005692
  - GO:0034693
  - GO:0005693
  - GO:0071017
  - GO:0071018
  - GO:0071019
  - GO:0071022
  - GO:0071016
  - GO:0071015
  - GO:0005689
  - GO:0005685
  - GO:0005686
  - GO:0071006
  - GO:0071007
  - GO:0071008
  - GO:0071021
  - GO:0071005
  - GO:0071004
  - GO:0005684
  - GO:0005687
  - GO:0071001
  - GO:0046540
  - GO:0005690
  - GO:0071002
  - GO:0071009
  - GO:0005682
  - GO:0005688
  - GO:0005691
  - GO:0005683
  evidence_ids:
  - ev_strict_ribonucleoprotein
  - ev_history_ribonucleoprotein
- assessment_id: assess_rnp_supraspliceosome_hierarchy
  area: representation
  topic: Disjointness of parent_structures (is-a) vs CONSTITUENT component/has_part
    (parthood) in supraspliceosomal_complex.yaml
  outcome: concern
  summary: supraspliceosomal_complex.yaml (GO:0044530) models GO:0005681 (spliceosomal
    complex) as both an is-a parent_structures entry and a stoichiometry-'4' CONSTITUENT
    component.
  target_ids:
  - GO:0044530
  evidence_ids:
  - ev_rnp_supraspliceosome
- assessment_id: assess_rnp_boxcd_consistency
  area: representation
  topic: Box C/D snoRNP core protein subcomplex typing and per-PMID evidence note
    attribution
  outcome: concern
  summary: box_c_d_methylation_guide_snornp_complex.yaml types 4-protein core subcomplex
    as PROTEIN, and box_c_d_rnp_complex.yaml retains two semicolon-joined multi-paper
    notes on single-PMID EvidenceItem entries.
  target_ids:
  - GO:0031428
  - GO:0170049
  evidence_ids:
  - ev_rnp_boxcd_guide
  - ev_rnp_boxcd_notes
findings:
- finding_id: F1
  issue_key: ribonucleoprotein-supraspliceosomal-parent-constituent-conflation
  category: representation
  severity: major
  status: open
  certainty: confirmed
  title: supraspliceosomal_complex.yaml lists GO:0005681 (spliceosomal complex) in
    parent_structures while modeling GO:0005681 as a stoichiometry-'4' CONSTITUENT
    component without has_part
  description: 'In data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml
    (GO:0044530), GO:0005681 (spliceosomal complex) is listed in parent_structures
    (lines 11-13) and simultaneously as components[0] (id: spliceosomal_complex, label:
    ''Native spliceosome monomer'', component_type: PROTEIN_COMPLEX, component_role:
    CONSTITUENT, stoichiometry: ''4'', grounding: GO:0005681), while has_part is omitted.
    Because the supraspliceosome is a tetrameric assembly of four native spliceosomes
    alongside 5''-splice-site RNP factors (GO:1990904 ribonucleoprotein complex),
    GO:0005681 is a parthood constituent (has_part: [GO:0005681]) rather than simultaneously
    an is-a parent and a constituent part.'
  target_ids:
  - GO:0044530
  field_paths:
  - parent_structures
  - has_part
  - components[0].grounding
  evidence_ids:
  - ev_rnp_supraspliceosome
  rule_id: docs/CURATION.md:parent_structures-vs-part_of
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml
    role: maintained_record
  tags:
  - ribonucleoprotein
  - hierarchy
  - has-part
  - stage4-record-review
- finding_id: F2
  issue_key: ribonucleoprotein-box-cd-snornp-type-and-evidence-notes
  category: consistency
  severity: minor
  status: open
  certainty: confirmed
  title: box_c_d_methylation_guide_snornp_complex.yaml types 4-subunit nop1_nop56_nop58_snu13_core
    as PROTEIN and box_c_d_rnp_complex.yaml retains two multi-paper notes on single-PMID
    EvidenceItem entries
  description: 'In data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml
    (GO:0031428), components[1] (nop1_nop56_nop58_snu13_core, ''Nop1/Nop56/Nop58/Snu13
    core protein subcomplex'', gene_symbols: [NOP1, NOP56, NOP58, SNU13]) is typed
    PROTEIN instead of PROTEIN_COMPLEX (unlike sibling box_c_d_rnp_complex.yaml, where
    nop1_nop56_nop58_snu13_core is typed PROTEIN_COMPLEX). Additionally, in data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml
    (GO:0170049), components[1].protein_examples[2].evidence[0].notes (PMID:9632712,
    Wu P et al. 1998) and components[1].protein_examples[3].evidence[0].notes (PMID:9372940,
    Watkins NJ et al. 2000 / Snu13) still concatenate ''Gautier T et al. 1997 (Mol
    Cell Biol) and Lafontaine DL & Tollervey D 1999 (RNA); Wu P et al. 1998 (Genes
    Dev)'' on single-PMID entries.'
  target_ids:
  - GO:0031428
  - GO:0170049
  field_paths:
  - components[1].component_type
  - components[1].protein_examples[2].evidence[0].notes
  - components[1].protein_examples[3].evidence[0].notes
  evidence_ids:
  - ev_rnp_boxcd_guide
  - ev_rnp_boxcd_notes
  rule_id: docs/SCHEMA.md:ComponentTypeEnum.PROTEIN_COMPLEX-and-EvidenceItem
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml
    role: maintained_record
  tags:
  - ribonucleoprotein
  - component-type
  - evidence-hygiene
  - stage4-record-review
actions:
- action_id: A1
  description: 'Move GO:0005681 from parent_structures to has_part in data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml
    (retaining parent_structures: [GO:1990904] and has_part: [GO:0005681]).'
  finding_ids:
  - F1
  target_ids:
  - GO:0044530
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/supraspliceosomal_complex.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
- action_id: A2
  description: Update components[1].component_type from PROTEIN to PROTEIN_COMPLEX
    in box_c_d_methylation_guide_snornp_complex.yaml, and align components[1].protein_examples[2,3].evidence[0].notes
    in box_c_d_rnp_complex.yaml with their single cited PMIDs (PMID:9632712 and PMID:9372940).
  finding_ids:
  - F2
  target_ids:
  - GO:0031428
  - GO:0170049
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/box_c_d_methylation_guide_snornp_complex.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/ribonucleoprotein/box_c_d_rnp_complex.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
boundary_decisions:
- action: retain
  target_ids:
  - GO:0120259
  - GO:0030686
  - GO:1990061
  - GO:0031428
  - GO:0170049
  - GO:0072588
  - GO:0031429
  - GO:0015030
  - GO:0071012
  - GO:0071013
  - GO:0000243
  - GO:0030679
  - GO:0000177
  - GO:0010494
  - GO:0030680
  - GO:0000178
  - cellstructuremech:glycolytic_body
  - cellstructuremech:h_body
  - GO:0035363
  - GO:0035061
  - GO:0015934
  - GO:0120115
  - GO:0030681
  - GO:0010445
  - GO:0000176
  - GO:0016607
  - GO:0097165
  - GO:0101019
  - GO:0005655
  - GO:0035062
  - GO:0000932
  - GO:0042382
  - GO:0071003
  - GO:0097356
  - GO:0071014
  - GO:0071020
  - GO:0071011
  - GO:0030684
  - GO:0030687
  - GO:0030688
  - GO:0071010
  - GO:0000172
  - GO:0030677
  - GO:0005840
  - GO:0140365
  - GO:0048500
  - GO:0071024
  - GO:0030532
  - GO:0015935
  - GO:0032040
  - GO:0005732
  - GO:0071601
  - GO:0005681
  - GO:0097525
  - GO:0097526
  - GO:0044530
  - GO:0005697
  - cellstructuremech:tmar_condensate
  - GO:0071023
  - GO:0005692
  - GO:0034693
  - GO:0005693
  - GO:0071017
  - GO:0071018
  - GO:0071019
  - GO:0071022
  - GO:0071016
  - GO:0071015
  - GO:0005689
  - GO:0005685
  - GO:0005686
  - GO:0071006
  - GO:0071007
  - GO:0071008
  - GO:0071021
  - GO:0071005
  - GO:0071004
  - GO:0005684
  - GO:0005687
  - GO:0071001
  - GO:0046540
  - GO:0005690
  - GO:0071002
  - GO:0071009
  - GO:0005682
  - GO:0005688
  - GO:0005691
  - GO:0005683
  rationale: All 88 ribonucleoprotein records denote distinct ribosomal, spliceosomal,
    snoRNP, CRISPR-Cas, or RNA-degradosome complexes.
  evidence_ids:
  - ev_strict_ribonucleoprotein
  - ev_history_ribonucleoprotein
limitations:
- Record edits for ribonucleoprotein cohort findings are queued for Cycle 4 Stage
  5 (resolve_review_findings).
tags:
- stage4
- category-review
- ribonucleoprotein
```
