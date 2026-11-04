# Category review of data/structures/cytoskeleton/ (173 records): GO subcomplex causal-node types and discussion issue evidence links

- Review: 20261023T091804Z-cytoskeleton-category-review
- Repository: CultureBotAI/CellStructureMech
- Started UTC: 2026-10-23T09:10:15Z
- Finished UTC: 2026-10-23T09:18:04Z
- Reviewer: antigravity-stage4-record-review (independent)
- Completion: completed
- Verdict: pass_with_limitations
- Scientific review: true

## Summary

Full-coverage category review of all 173 records in data/structures/cytoskeleton/ verified distinct filament, MTOC, septin, eisosome, and motor-complex boundaries. Two minor cohort patterns were identified across 8 records: (F1) 7 causal-graph nodes across 5 records reference GO-grounded PROTEIN_COMPLEX subcomplex components (Arp2/3 complex GO:0005885, gamma-tubulin complex GO:0000930, radial spoke head/neck/stalk GO:0001535/GO:0120343/GO:0001536) but are typed GENE_OR_PROTEIN without grounding instead of STRUCTURE; and (F2) 3 records (crescentin_filament.yaml, mreb_filament.yaml, phuz_spindle.yaml) cite repository issues (#1260, #119, #481, #482) in discussions prose without structured evidence links.

## Scope And Provenance

Full-cohort review of all 173 CellStructureRecord YAML files under data/structures/cytoskeleton/.

Selection: Complete folder cohort data/structures/cytoskeleton/*.yaml in the frozen 978-record Stage 4 inventory.
Coverage: full; 173 reviewed / 173 in the declared population.
Source: git_commit at Git base 13c6b0d85338aa96d330b8d699587dfe270a21f9.
Working-tree hashes do not imply those bytes were committed.

| Target | Path / selector | Kind | Label |
| --- | --- | --- | --- |
| GO:0097649 | data/structures/cytoskeleton/a_axonemal_microtubule.yaml | maintained | A axonemal microtubule |
| GO:0099079 | data/structures/cytoskeleton/actin_body.yaml | maintained | actin body |
| GO:0030479 | data/structures/cytoskeleton/actin_cortical_patch.yaml | maintained | actin cortical patch |
| GO:0005826 | data/structures/cytoskeleton/actomyosin_contractile_ring.yaml | maintained | actomyosin contractile ring |
| cellstructuremech:alfa_filament | data/structures/cytoskeleton/alfa_filament.yaml | maintained | AlfA filament |
| GO:0005885 | data/structures/cytoskeleton/arp2_3_protein_complex.yaml | maintained | Arp2/3 protein complex |
| GO:0005818 | data/structures/cytoskeleton/aster.yaml | maintained | aster |
| GO:0000235 | data/structures/cytoskeleton/astral_microtubule.yaml | maintained | astral microtubule |
| GO:0160111 | data/structures/cytoskeleton/axonemal_a_tubule_inner_sheath.yaml | maintained | axonemal A tubule inner sheath |
| GO:0160112 | data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml | maintained | axonemal B tubule inner sheath |
| GO:1990716 | data/structures/cytoskeleton/axonemal_central_apparatus.yaml | maintained | axonemal central apparatus |
| GO:1990717 | data/structures/cytoskeleton/axonemal_central_bridge.yaml | maintained | axonemal central bridge |
| GO:0097540 | data/structures/cytoskeleton/axonemal_central_pair.yaml | maintained | axonemal central pair |
| GO:1990718 | data/structures/cytoskeleton/axonemal_central_pair_projection.yaml | maintained | axonemal central pair projection |
| GO:0097545 | data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml | maintained | axonemal doublet microtubule |
| GO:0005858 | data/structures/cytoskeleton/axonemal_dynein_complex.yaml | maintained | axonemal dynein complex |
| GO:0005879 | data/structures/cytoskeleton/axonemal_microtubule.yaml | maintained | axonemal microtubule |
| GO:0160113 | data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_junction.yaml | maintained | axonemal microtubule doublet inner junction |
| GO:0160110 | data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_sheath.yaml | maintained | axonemal microtubule doublet inner sheath |
| GO:0160114 | data/structures/cytoskeleton/axonemal_microtubule_doublet_outer_junction.yaml | maintained | axonemal microtubule doublet outer junction |
| GO:0160115 | data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml | maintained | axonemal microtubule doublet ribbon |
| GO:0005931 | data/structures/cytoskeleton/axonemal_nexin_link.yaml | maintained | axonemal nexin link |
| GO:0005930 | data/structures/cytoskeleton/axoneme.yaml | maintained | axoneme |
| GO:0097650 | data/structures/cytoskeleton/b_axonemal_microtubule.yaml | maintained | B axonemal microtubule |
| cellstructuremech:bactofilin_filament | data/structures/cytoskeleton/bactofilin_filament.yaml | maintained | bactofilin filament |
| cellstructuremech:basal_body_a_b_inner_junction | data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml | maintained | basal body A-B inner junction |
| cellstructuremech:basal_body_a_c_linker | data/structures/cytoskeleton/basal_body_a_c_linker.yaml | maintained | basal body A-C linker |
| cellstructuremech:basal_body_a_tusk | data/structures/cytoskeleton/basal_body_a_tusk.yaml | maintained | basal body A-tusk |
| cellstructuremech:basal_body_b_c_inner_junction | data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml | maintained | basal body B-C inner junction |
| cellstructuremech:basal_body_c_tubule_hook | data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml | maintained | basal body C-tubule hook |
| cellstructuremech:basal_body_c_tubule_luminal_filament | data/structures/cytoskeleton/basal_body_c_tubule_luminal_filament.yaml | maintained | basal body C-tubule luminal filament |
| cellstructuremech:basal_body_cartwheel | data/structures/cytoskeleton/basal_body_cartwheel.yaml | maintained | basal body cartwheel |
| cellstructuremech:basal_body_cartwheel_inner_density | data/structures/cytoskeleton/basal_body_cartwheel_inner_density.yaml | maintained | basal body cartwheel inner density |
| cellstructuremech:basal_body_d2_rod | data/structures/cytoskeleton/basal_body_d2_rod.yaml | maintained | basal body D2-rod |
| cellstructuremech:basal_body_filamentous_cartwheel_inner_density | data/structures/cytoskeleton/basal_body_filamentous_cartwheel_inner_density.yaml | maintained | basal body filamentous cartwheel inner density |
| cellstructuremech:basal_body_inner_scaffold | data/structures/cytoskeleton/basal_body_inner_scaffold.yaml | maintained | basal body inner scaffold |
| cellstructuremech:basal_body_pinhead | data/structures/cytoskeleton/basal_body_pinhead.yaml | maintained | basal body pinhead |
| cellstructuremech:basal_body_triplet_base | data/structures/cytoskeleton/basal_body_triplet_base.yaml | maintained | basal body triplet base |
| GO:0020032 | data/structures/cytoskeleton/basal_ring_of_apical_complex.yaml | maintained | basal ring of apical complex |
| GO:0120120 | data/structures/cytoskeleton/bilobe_structure.yaml | maintained | bilobe structure |
| cellstructuremech:btubab_bacterial_microtubule | data/structures/cytoskeleton/btubab_bacterial_microtubule.yaml | maintained | BtubAB bacterial microtubule |
| GO:1990719 | data/structures/cytoskeleton/c1_axonemal_microtubule.yaml | maintained | C1 axonemal microtubule |
| GO:1990720 | data/structures/cytoskeleton/c2_axonemal_microtubule.yaml | maintained | C2 axonemal microtubule |
| GO:0000142 | data/structures/cytoskeleton/cellular_bud_neck_contractile_ring.yaml | maintained | cellular bud neck contractile ring |
| GO:0032174 | data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml | maintained | cellular bud neck septin collar |
| GO:0000144 | data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml | maintained | cellular bud neck septin ring |
| GO:0032177 | data/structures/cytoskeleton/cellular_bud_neck_split_septin_rings.yaml | maintained | cellular bud neck split septin rings |
| GO:0061493 | data/structures/cytoskeleton/central_plaque_of_mitotic_spindle_pole_body.yaml | maintained | central plaque of mitotic spindle pole body |
| GO:0005823 | data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml | maintained | central plaque of spindle pole body |
| cellstructuremech:cetz_filament | data/structures/cytoskeleton/cetz_filament.yaml | maintained | CetZ filament |
| GO:0032166 | data/structures/cytoskeleton/chlamydospore_septin_filament_array.yaml | maintained | chlamydospore septin filament array |
| GO:0036064 | data/structures/cytoskeleton/ciliary_basal_body.yaml | maintained | ciliary basal body |
| GO:0120269 | data/structures/cytoskeleton/ciliary_centrin_arm.yaml | maintained | ciliary centrin arm |
| GO:1990900 | data/structures/cytoskeleton/ciliary_pocket_collar.yaml | maintained | ciliary pocket collar |
| GO:0120280 | data/structures/cytoskeleton/ciliary_pro_basal_body.yaml | maintained | ciliary pro-basal body |
| GO:0035253 | data/structures/cytoskeleton/ciliary_rootlet.yaml | maintained | ciliary rootlet |
| GO:0032161 | data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml | maintained | cleavage apparatus septin structure |
| GO:0020010 | data/structures/cytoskeleton/conoid.yaml | maintained | conoid |
| cellstructuremech:crescentin_filament | data/structures/cytoskeleton/crescentin_filament.yaml | maintained | crescentin filament |
| cellstructuremech:cryptophyte_cortical_centrin_network | data/structures/cytoskeleton/cryptophyte_cortical_centrin_network.yaml | maintained | cryptophyte cortical centrin network |
| GO:0097268 | data/structures/cytoskeleton/cytoophidium.yaml | maintained | cytoophidium |
| GO:0005881 | data/structures/cytoskeleton/cytoplasmic_microtubule.yaml | maintained | cytoplasmic microtubule |
| cellstructuremech:cytostomal_cord | data/structures/cytoskeleton/cytostomal_cord.yaml | maintained | cytostomal cord |
| GO:0032123 | data/structures/cytoskeleton/deep_fiber.yaml | maintained | deep fiber |
| cellstructuremech:distal_connecting_fiber | data/structures/cytoskeleton/distal_connecting_fiber.yaml | maintained | distal connecting fiber |
| GO:0036286 | data/structures/cytoskeleton/eisosome_filament.yaml | maintained | eisosome filament |
| GO:0061645 | data/structures/cytoskeleton/endocytic_patch.yaml | maintained | endocytic patch |
| cellstructuremech:entodiniomorphid_subkinetal_myoneme_system | data/structures/cytoskeleton/entodiniomorphid_subkinetal_myoneme_system.yaml | maintained | Entodiniomorphid subkinetal myoneme system |
| GO:0000923 | data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml | maintained | equatorial microtubule organizing center |
| GO:0120119 | data/structures/cytoskeleton/flagellum_attachment_zone.yaml | maintained | flagellum attachment zone |
| cellstructuremech:funis | data/structures/cytoskeleton/funis.yaml | maintained | funis |
| GO:0000930 | data/structures/cytoskeleton/gamma_tubulin_complex.yaml | maintained | gamma-tubulin complex |
| GO:0000931 | data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml | maintained | gamma-tubulin ring complex |
| GO:0008275 | data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml | maintained | gamma-tubulin small complex |
| GO:0032171 | data/structures/cytoskeleton/germ_tube_septin_cap.yaml | maintained | germ tube septin cap |
| GO:0032172 | data/structures/cytoskeleton/germ_tube_septin_ring.yaml | maintained | germ tube septin ring |
| GO:1990317 | data/structures/cytoskeleton/gin4_complex.yaml | maintained | Gin4 complex |
| GO:0061496 | data/structures/cytoskeleton/half_bridge_of_mitotic_spindle_pole_body.yaml | maintained | half bridge of mitotic spindle pole body |
| GO:0005825 | data/structures/cytoskeleton/half_bridge_of_spindle_pole_body.yaml | maintained | half bridge of spindle pole body |
| GO:0032117 | data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml | maintained | horsetail-astral microtubule array |
| GO:0062140 | data/structures/cytoskeleton/hyphae_septin_collar.yaml | maintained | hyphae septin collar |
| GO:0032163 | data/structures/cytoskeleton/hyphal_septin_band.yaml | maintained | hyphal septin band |
| GO:0032164 | data/structures/cytoskeleton/hyphal_septin_cap.yaml | maintained | hyphal septin cap |
| GO:0032168 | data/structures/cytoskeleton/hyphal_septin_ring.yaml | maintained | hyphal septin ring |
| cellstructuremech:icl1e_complex | data/structures/cytoskeleton/icl1e_complex.yaml | maintained | ICL1e complex |
| cellstructuremech:infraciliary_lattice | data/structures/cytoskeleton/infraciliary_lattice.yaml | maintained | infraciliary lattice |
| GO:0036156 | data/structures/cytoskeleton/inner_dynein_arm.yaml | maintained | inner dynein arm |
| GO:0061497 | data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml | maintained | inner plaque of mitotic spindle pole body |
| GO:0005822 | data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml | maintained | inner plaque of spindle pole body |
| GO:0061498 | data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml | maintained | intermediate layer of mitotic spindle pole body |
| GO:0005821 | data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml | maintained | intermediate layer of spindle pole body |
| GO:0031021 | data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml | maintained | interphase microtubule organizing center |
| GO:0160066 | data/structures/cytoskeleton/interphase_sin_signaling_complex.yaml | maintained | interphase SIN signaling complex |
| GO:0033289 | data/structures/cytoskeleton/intraconoid_microtubule.yaml | maintained | intraconoid microtubule |
| cellstructuremech:mamk_filament | data/structures/cytoskeleton/mamk_filament.yaml | maintained | MamK filament |
| GO:1990819 | data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml | maintained | mating projection actin fusion focus |
| GO:0032162 | data/structures/cytoskeleton/mating_projection_septin_band.yaml | maintained | mating projection septin band |
| GO:0032175 | data/structures/cytoskeleton/mating_projection_septin_ring.yaml | maintained | mating projection septin ring |
| GO:0036391 | data/structures/cytoskeleton/medial_cortex_septin_ring.yaml | maintained | medial cortex septin ring |
| GO:0097568 | data/structures/cytoskeleton/median_body.yaml | maintained | median body |
| GO:0110086 | data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml | maintained | meiotic actomyosin contractile ring |
| GO:0034993 | data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml | maintained | meiotic nuclear membrane microtubule tethering complex |
| cellstructuremech:meiotic_outer_plaque | data/structures/cytoskeleton/meiotic_outer_plaque.yaml | maintained | meiotic outer plaque |
| GO:0032152 | data/structures/cytoskeleton/meiotic_septin_complex.yaml | maintained | meiotic septin complex |
| GO:0035974 | data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml | maintained | meiotic spindle pole body |
| GO:0005874 | data/structures/cytoskeleton/microtubule.yaml | maintained | microtubule |
| GO:0110085 | data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml | maintained | mitotic actomyosin contractile ring |
| GO:0032151 | data/structures/cytoskeleton/mitotic_septin_complex.yaml | maintained | mitotic septin complex |
| GO:0072686 | data/structures/cytoskeleton/mitotic_spindle.yaml | maintained | mitotic spindle |
| GO:0044732 | data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml | maintained | mitotic spindle pole body |
| cellstructuremech:mreb_filament | data/structures/cytoskeleton/mreb_filament.yaml | maintained | MreB filament |
| GO:0071958 | data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml | maintained | new mitotic spindle pole body |
| GO:0160067 | data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml | maintained | new spindle pole body SIN signaling complex |
| GO:0005880 | data/structures/cytoskeleton/nuclear_microtubule.yaml | maintained | nuclear microtubule |
| cellstructuremech:nucleus_basal_body_connector | data/structures/cytoskeleton/nucleus_basal_body_connector.yaml | maintained | nucleus-basal body connector |
| GO:0071957 | data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml | maintained | old mitotic spindle pole body |
| GO:0036157 | data/structures/cytoskeleton/outer_dynein_arm.yaml | maintained | outer dynein arm |
| GO:0061499 | data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml | maintained | outer plaque of mitotic spindle pole body |
| GO:0005824 | data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml | maintained | outer plaque of spindle pole body |
| cellstructuremech:parm_filament | data/structures/cytoskeleton/parm_filament.yaml | maintained | ParM filament |
| cellstructuremech:peritrich_body_myoneme_system | data/structures/cytoskeleton/peritrich_body_myoneme_system.yaml | maintained | Peritrich body myoneme system |
| cellstructuremech:phuz_spindle | data/structures/cytoskeleton/phuz_spindle.yaml | maintained | PhuZ spindle |
| GO:0020031 | data/structures/cytoskeleton/polar_ring_of_apical_complex.yaml | maintained | polar ring of apical complex |
| GO:1990295 | data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml | maintained | post-anaphase microtubule array |
| GO:0032157 | data/structures/cytoskeleton/prospore_contractile_ring.yaml | maintained | prospore contractile ring |
| GO:0032165 | data/structures/cytoskeleton/prospore_septin_filament_array.yaml | maintained | prospore septin filament array |
| GO:0032169 | data/structures/cytoskeleton/prospore_septin_ring.yaml | maintained | prospore septin ring |
| GO:0032170 | data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml | maintained | pseudohyphal septin ring |
| cellstructuremech:quiescent_cell_microtubule_bundle | data/structures/cytoskeleton/quiescent_cell_microtubule_bundle.yaml | maintained | quiescent cell microtubule bundle |
| cellstructuremech:quiescent_nuclear_microtubule_bundle | data/structures/cytoskeleton/quiescent_nuclear_microtubule_bundle.yaml | maintained | quiescent nuclear microtubule bundle |
| cellstructuremech:radial_microtubule_organizing_center | data/structures/cytoskeleton/radial_microtubule_organizing_center.yaml | maintained | radial microtubule organizing center |
| GO:0001534 | data/structures/cytoskeleton/radial_spoke.yaml | maintained | radial spoke |
| GO:0001535 | data/structures/cytoskeleton/radial_spoke_head.yaml | maintained | radial spoke head |
| GO:0120343 | data/structures/cytoskeleton/radial_spoke_neck.yaml | maintained | radial spoke neck |
| GO:0001536 | data/structures/cytoskeleton/radial_spoke_stalk.yaml | maintained | radial spoke stalk |
| GO:1990612 | data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml | maintained | Sad1-Kms1 LINC complex |
| GO:0032158 | data/structures/cytoskeleton/septin_band.yaml | maintained | septin band |
| GO:0032159 | data/structures/cytoskeleton/septin_cap.yaml | maintained | septin cap |
| GO:0032173 | data/structures/cytoskeleton/septin_collar.yaml | maintained | septin collar |
| GO:0031105 | data/structures/cytoskeleton/septin_complex.yaml | maintained | septin complex |
| GO:0032156 | data/structures/cytoskeleton/septin_cytoskeleton.yaml | maintained | septin cytoskeleton |
| GO:0032160 | data/structures/cytoskeleton/septin_filament_array.yaml | maintained | septin filament array |
| GO:0005940 | data/structures/cytoskeleton/septin_ring.yaml | maintained | septin ring |
| GO:0160065 | data/structures/cytoskeleton/sin_men_signaling_complex.yaml | maintained | SIN/MEN signaling complex |
| GO:1990334 | data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml | maintained | SIN/MEN two-component GAP complex |
| cellstructuremech:sinister_fiber | data/structures/cytoskeleton/sinister_fiber.yaml | maintained | sinister fiber |
| GO:0005819 | data/structures/cytoskeleton/spindle.yaml | maintained | spindle |
| GO:0005876 | data/structures/cytoskeleton/spindle_microtubule.yaml | maintained | spindle microtubule |
| GO:0051233 | data/structures/cytoskeleton/spindle_midzone.yaml | maintained | spindle midzone |
| GO:0000922 | data/structures/cytoskeleton/spindle_pole.yaml | maintained | spindle pole |
| GO:0005816 | data/structures/cytoskeleton/spindle_pole_body.yaml | maintained | spindle pole body |
| cellstructuremech:spindle_pole_body_duplication_plaque | data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml | maintained | spindle pole body duplication plaque |
| cellstructuremech:spindle_pole_body_satellite | data/structures/cytoskeleton/spindle_pole_body_satellite.yaml | maintained | spindle pole body satellite |
| cellstructuremech:spirostomum_myoneme_fishnet | data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml | maintained | Spirostomum myoneme fishnet |
| GO:0032176 | data/structures/cytoskeleton/split_septin_rings.yaml | maintained | split septin rings |
| cellstructuremech:stalk_spasmoneme | data/structures/cytoskeleton/stalk_spasmoneme.yaml | maintained | Stalk spasmoneme |
| cellstructuremech:stentor_km_fiber | data/structures/cytoskeleton/stentor_km_fiber.yaml | maintained | Stentor Km fiber |
| cellstructuremech:stentor_myoneme_system | data/structures/cytoskeleton/stentor_myoneme_system.yaml | maintained | Stentor myoneme system |
| cellstructuremech:stentor_perialgal_microtubule_meshwork | data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml | maintained | Stentor perialgal microtubule meshwork |
| GO:0020025 | data/structures/cytoskeleton/subpellicular_microtubule.yaml | maintained | subpellicular microtubule |
| GO:0070850 | data/structures/cytoskeleton/tacc_tog_complex.yaml | maintained | TACC/TOG complex |
| cellstructuremech:telocentrosome | data/structures/cytoskeleton/telocentrosome.yaml | maintained | telocentrosome |
| cellstructuremech:transition_zone_stellate_fiber_system | data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml | maintained | transition zone stellate fiber system |
| GO:0120121 | data/structures/cytoskeleton/tripartite_attachment_complex.yaml | maintained | tripartite attachment complex |
| cellstructuremech:tubulin_spool | data/structures/cytoskeleton/tubulin_spool.yaml | maintained | tubulin spool |
| cellstructuremech:tubz_filament | data/structures/cytoskeleton/tubz_filament.yaml | maintained | TubZ filament |
| GO:0097597 | data/structures/cytoskeleton/ventral_disc.yaml | maintained | ventral disc |
| GO:0097595 | data/structures/cytoskeleton/ventral_disc_crossbridge.yaml | maintained | ventral disc crossbridge |
| GO:0097594 | data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml | maintained | ventral disc dorsal microribbon |
| GO:0097591 | data/structures/cytoskeleton/ventral_disc_lateral_crest.yaml | maintained | ventral disc lateral crest |
| GO:0097593 | data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml | maintained | ventral disc microtubule array |
| GO:0097592 | data/structures/cytoskeleton/ventral_disc_overlap_zone.yaml | maintained | ventral disc overlap zone |
| GO:0097596 | data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml | maintained | ventral disc supernumerary microtubule array |

## Validation

| Check | Status | Required | Targets | Result |
| --- | --- | --- | --- | --- |
| Strict corpus validation covering cytoskeleton cohort | passed | True | GO:0097649, GO:0099079, GO:0030479, GO:0005826, cellstructuremech:alfa_filament, GO:0005885, GO:0005818, GO:0000235, GO:0160111, GO:0160112, GO:1990716, GO:1990717, GO:0097540, GO:1990718, GO:0097545, GO:0005858, GO:0005879, GO:0160113, GO:0160110, GO:0160114, GO:0160115, GO:0005931, GO:0005930, GO:0097650, cellstructuremech:bactofilin_filament, cellstructuremech:basal_body_a_b_inner_junction, cellstructuremech:basal_body_a_c_linker, cellstructuremech:basal_body_a_tusk, cellstructuremech:basal_body_b_c_inner_junction, cellstructuremech:basal_body_c_tubule_hook, cellstructuremech:basal_body_c_tubule_luminal_filament, cellstructuremech:basal_body_cartwheel, cellstructuremech:basal_body_cartwheel_inner_density, cellstructuremech:basal_body_d2_rod, cellstructuremech:basal_body_filamentous_cartwheel_inner_density, cellstructuremech:basal_body_inner_scaffold, cellstructuremech:basal_body_pinhead, cellstructuremech:basal_body_triplet_base, GO:0020032, GO:0120120, cellstructuremech:btubab_bacterial_microtubule, GO:1990719, GO:1990720, GO:0000142, GO:0032174, GO:0000144, GO:0032177, GO:0061493, GO:0005823, cellstructuremech:cetz_filament, GO:0032166, GO:0036064, GO:0120269, GO:1990900, GO:0120280, GO:0035253, GO:0032161, GO:0020010, cellstructuremech:crescentin_filament, cellstructuremech:cryptophyte_cortical_centrin_network, GO:0097268, GO:0005881, cellstructuremech:cytostomal_cord, GO:0032123, cellstructuremech:distal_connecting_fiber, GO:0036286, GO:0061645, cellstructuremech:entodiniomorphid_subkinetal_myoneme_system, GO:0000923, GO:0120119, cellstructuremech:funis, GO:0000930, GO:0000931, GO:0008275, GO:0032171, GO:0032172, GO:1990317, GO:0061496, GO:0005825, GO:0032117, GO:0062140, GO:0032163, GO:0032164, GO:0032168, cellstructuremech:icl1e_complex, cellstructuremech:infraciliary_lattice, GO:0036156, GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:0160066, GO:0033289, cellstructuremech:mamk_filament, GO:1990819, GO:0032162, GO:0032175, GO:0036391, GO:0097568, GO:0110086, GO:0034993, cellstructuremech:meiotic_outer_plaque, GO:0032152, GO:0035974, GO:0005874, GO:0110085, GO:0032151, GO:0072686, GO:0044732, cellstructuremech:mreb_filament, GO:0071958, GO:0160067, GO:0005880, cellstructuremech:nucleus_basal_body_connector, GO:0071957, GO:0036157, GO:0061499, GO:0005824, cellstructuremech:parm_filament, cellstructuremech:peritrich_body_myoneme_system, cellstructuremech:phuz_spindle, GO:0020031, GO:1990295, GO:0032157, GO:0032165, GO:0032169, GO:0032170, cellstructuremech:quiescent_cell_microtubule_bundle, cellstructuremech:quiescent_nuclear_microtubule_bundle, cellstructuremech:radial_microtubule_organizing_center, GO:0001534, GO:0001535, GO:0120343, GO:0001536, GO:1990612, GO:0032158, GO:0032159, GO:0032173, GO:0031105, GO:0032156, GO:0032160, GO:0005940, GO:0160065, GO:1990334, cellstructuremech:sinister_fiber, GO:0005819, GO:0005876, GO:0051233, GO:0000922, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet, GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_myoneme_system, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0020025, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, GO:0120121, cellstructuremech:tubulin_spool, cellstructuremech:tubz_filament, GO:0097597, GO:0097595, GO:0097594, GO:0097591, GO:0097593, GO:0097592, GO:0097596 | All 173 cytoskeleton records pass strict LinkML and semantic validation. |
| ID-label correspondence across cytoskeleton cohort | passed | True | GO:0097649, GO:0099079, GO:0030479, GO:0005826, cellstructuremech:alfa_filament, GO:0005885, GO:0005818, GO:0000235, GO:0160111, GO:0160112, GO:1990716, GO:1990717, GO:0097540, GO:1990718, GO:0097545, GO:0005858, GO:0005879, GO:0160113, GO:0160110, GO:0160114, GO:0160115, GO:0005931, GO:0005930, GO:0097650, cellstructuremech:bactofilin_filament, cellstructuremech:basal_body_a_b_inner_junction, cellstructuremech:basal_body_a_c_linker, cellstructuremech:basal_body_a_tusk, cellstructuremech:basal_body_b_c_inner_junction, cellstructuremech:basal_body_c_tubule_hook, cellstructuremech:basal_body_c_tubule_luminal_filament, cellstructuremech:basal_body_cartwheel, cellstructuremech:basal_body_cartwheel_inner_density, cellstructuremech:basal_body_d2_rod, cellstructuremech:basal_body_filamentous_cartwheel_inner_density, cellstructuremech:basal_body_inner_scaffold, cellstructuremech:basal_body_pinhead, cellstructuremech:basal_body_triplet_base, GO:0020032, GO:0120120, cellstructuremech:btubab_bacterial_microtubule, GO:1990719, GO:1990720, GO:0000142, GO:0032174, GO:0000144, GO:0032177, GO:0061493, GO:0005823, cellstructuremech:cetz_filament, GO:0032166, GO:0036064, GO:0120269, GO:1990900, GO:0120280, GO:0035253, GO:0032161, GO:0020010, cellstructuremech:crescentin_filament, cellstructuremech:cryptophyte_cortical_centrin_network, GO:0097268, GO:0005881, cellstructuremech:cytostomal_cord, GO:0032123, cellstructuremech:distal_connecting_fiber, GO:0036286, GO:0061645, cellstructuremech:entodiniomorphid_subkinetal_myoneme_system, GO:0000923, GO:0120119, cellstructuremech:funis, GO:0000930, GO:0000931, GO:0008275, GO:0032171, GO:0032172, GO:1990317, GO:0061496, GO:0005825, GO:0032117, GO:0062140, GO:0032163, GO:0032164, GO:0032168, cellstructuremech:icl1e_complex, cellstructuremech:infraciliary_lattice, GO:0036156, GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:0160066, GO:0033289, cellstructuremech:mamk_filament, GO:1990819, GO:0032162, GO:0032175, GO:0036391, GO:0097568, GO:0110086, GO:0034993, cellstructuremech:meiotic_outer_plaque, GO:0032152, GO:0035974, GO:0005874, GO:0110085, GO:0032151, GO:0072686, GO:0044732, cellstructuremech:mreb_filament, GO:0071958, GO:0160067, GO:0005880, cellstructuremech:nucleus_basal_body_connector, GO:0071957, GO:0036157, GO:0061499, GO:0005824, cellstructuremech:parm_filament, cellstructuremech:peritrich_body_myoneme_system, cellstructuremech:phuz_spindle, GO:0020031, GO:1990295, GO:0032157, GO:0032165, GO:0032169, GO:0032170, cellstructuremech:quiescent_cell_microtubule_bundle, cellstructuremech:quiescent_nuclear_microtubule_bundle, cellstructuremech:radial_microtubule_organizing_center, GO:0001534, GO:0001535, GO:0120343, GO:0001536, GO:1990612, GO:0032158, GO:0032159, GO:0032173, GO:0031105, GO:0032156, GO:0032160, GO:0005940, GO:0160065, GO:1990334, cellstructuremech:sinister_fiber, GO:0005819, GO:0005876, GO:0051233, GO:0000922, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet, GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_myoneme_system, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0020025, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, GO:0120121, cellstructuremech:tubulin_spool, cellstructuremech:tubz_filament, GO:0097597, GO:0097595, GO:0097594, GO:0097591, GO:0097593, GO:0097592, GO:0097596 | All ontology ID-label pairs in cytoskeleton records correspond to canonical labels. |

## Scientific And Domain Assessments

### Boundary discipline, identity, composition, and evidence across all 173 cytoskeleton records

identity: supported. Targets: GO:0097649, GO:0099079, GO:0030479, GO:0005826, cellstructuremech:alfa_filament, GO:0005885, GO:0005818, GO:0000235, GO:0160111, GO:0160112, GO:1990716, GO:1990717, GO:0097540, GO:1990718, GO:0097545, GO:0005858, GO:0005879, GO:0160113, GO:0160110, GO:0160114, GO:0160115, GO:0005931, GO:0005930, GO:0097650, cellstructuremech:bactofilin_filament, cellstructuremech:basal_body_a_b_inner_junction, cellstructuremech:basal_body_a_c_linker, cellstructuremech:basal_body_a_tusk, cellstructuremech:basal_body_b_c_inner_junction, cellstructuremech:basal_body_c_tubule_hook, cellstructuremech:basal_body_c_tubule_luminal_filament, cellstructuremech:basal_body_cartwheel, cellstructuremech:basal_body_cartwheel_inner_density, cellstructuremech:basal_body_d2_rod, cellstructuremech:basal_body_filamentous_cartwheel_inner_density, cellstructuremech:basal_body_inner_scaffold, cellstructuremech:basal_body_pinhead, cellstructuremech:basal_body_triplet_base, GO:0020032, GO:0120120, cellstructuremech:btubab_bacterial_microtubule, GO:1990719, GO:1990720, GO:0000142, GO:0032174, GO:0000144, GO:0032177, GO:0061493, GO:0005823, cellstructuremech:cetz_filament, GO:0032166, GO:0036064, GO:0120269, GO:1990900, GO:0120280, GO:0035253, GO:0032161, GO:0020010, cellstructuremech:crescentin_filament, cellstructuremech:cryptophyte_cortical_centrin_network, GO:0097268, GO:0005881, cellstructuremech:cytostomal_cord, GO:0032123, cellstructuremech:distal_connecting_fiber, GO:0036286, GO:0061645, cellstructuremech:entodiniomorphid_subkinetal_myoneme_system, GO:0000923, GO:0120119, cellstructuremech:funis, GO:0000930, GO:0000931, GO:0008275, GO:0032171, GO:0032172, GO:1990317, GO:0061496, GO:0005825, GO:0032117, GO:0062140, GO:0032163, GO:0032164, GO:0032168, cellstructuremech:icl1e_complex, cellstructuremech:infraciliary_lattice, GO:0036156, GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:0160066, GO:0033289, cellstructuremech:mamk_filament, GO:1990819, GO:0032162, GO:0032175, GO:0036391, GO:0097568, GO:0110086, GO:0034993, cellstructuremech:meiotic_outer_plaque, GO:0032152, GO:0035974, GO:0005874, GO:0110085, GO:0032151, GO:0072686, GO:0044732, cellstructuremech:mreb_filament, GO:0071958, GO:0160067, GO:0005880, cellstructuremech:nucleus_basal_body_connector, GO:0071957, GO:0036157, GO:0061499, GO:0005824, cellstructuremech:parm_filament, cellstructuremech:peritrich_body_myoneme_system, cellstructuremech:phuz_spindle, GO:0020031, GO:1990295, GO:0032157, GO:0032165, GO:0032169, GO:0032170, cellstructuremech:quiescent_cell_microtubule_bundle, cellstructuremech:quiescent_nuclear_microtubule_bundle, cellstructuremech:radial_microtubule_organizing_center, GO:0001534, GO:0001535, GO:0120343, GO:0001536, GO:1990612, GO:0032158, GO:0032159, GO:0032173, GO:0031105, GO:0032156, GO:0032160, GO:0005940, GO:0160065, GO:1990334, cellstructuremech:sinister_fiber, GO:0005819, GO:0005876, GO:0051233, GO:0000922, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet, GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_myoneme_system, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0020025, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, GO:0120121, cellstructuremech:tubulin_spool, cellstructuremech:tubz_filament, GO:0097597, GO:0097595, GO:0097594, GO:0097591, GO:0097593, GO:0097592, GO:0097596.

All 173 cytoskeleton records have distinct GO/CSM identities, valid ontology label correspondence, and clear boundaries between polymers, organizing centers, and subcomplexes.

### Causal-graph node typing for GO-grounded PROTEIN_COMPLEX subcomplex components

graph: concern. Targets: GO:0030479, GO:0000923, GO:0031021, GO:0001534, cellstructuremech:telocentrosome.

Seven causal-graph nodes across 5 cytoskeleton records reference GO-grounded multiprotein subcomplex components using node_type: GENE_OR_PROTEIN without grounding instead of node_type: STRUCTURE.

### Structured GitHub issue URLs for #NNN mentions in discussions prose

evidence: concern. Targets: cellstructuremech:crescentin_filament, cellstructuremech:mreb_filament, cellstructuremech:phuz_spindle.

Three cytoskeleton records mention repository issues (#1260, #119, #481, #482) in discussions prose without corresponding GitHub issue URLs in evidence.

## Findings

### F1: Seven causal-graph nodes across 5 cytoskeleton records type GO-grounded PROTEIN_COMPLEX subcomplexes as GENE_OR_PROTEIN without grounding

minor / open / confirmed; issue key: cytoskeleton-go-subcomplex-causal-node-types.

Across 5 records in data/structures/cytoskeleton/ — actin_cortical_patch.yaml (node arp2_3_complex -&gt; GO:0005885), equatorial_microtubule_organizing_center.yaml (node gamma_tuc -&gt; GO:0000930), interphase_microtubule_organizing_center.yaml (node gamma_tuc -&gt; GO:0000930), radial_spoke.yaml (nodes radial_spoke_head -&gt; GO:0001535, radial_spoke_neck -&gt; GO:0120343, radial_spoke_stalk -&gt; GO:0001536), and telocentrosome.yaml (node gamma_tuc -&gt; GO:0000930) — causal-graph nodes referencing GO-grounded PROTEIN_COMPLEX components are typed GENE_OR_PROTEIN without grounding instead of STRUCTURE with their GO cellular-component grounding.

### F2: Three cytoskeleton records cite repository issues (#1260, #119, #481, #482) in discussions prose without structured evidence links

minor / open / confirmed; issue key: cytoskeleton-discussion-prose-issue-links.

In crescentin_filament.yaml (discussions[1] resolve_filament_architecture_and_dimensions, citing #1260), mreb_filament.yaml (discussions[0] resolve_filament_width_and_protofilament_number, citing #119), and phuz_spindle.yaml (discussions[0] dynamic_instability_parameters_unsourced citing #481 and discussions[1] spindle_centering_mechanism_details citing #482), discussions prose cites #NNN issue numbers without structured GitHub issue URLs in that discussion's evidence list.

## Recommended Actions And Acceptance Checks

### A1

Update the 7 subcomplex causal-graph nodes across actin_cortical_patch.yaml, equatorial_microtubule_organizing_center.yaml, interphase_microtubule_organizing_center.yaml, radial_spoke.yaml, and telocentrosome.yaml to node_type: STRUCTURE with their canonical GO labels and groundings.

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml

### A2

Add structured GitHub issue URLs (and cited source references) to the discussions[].evidence lists in crescentin_filament.yaml (#1260), mreb_filament.yaml (#119), and phuz_spindle.yaml (#481, #482).

- .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
- .venv/bin/python scripts/validate_history.py

## Category Boundaries

- retain: GO:0097649, GO:0099079, GO:0030479, GO:0005826, cellstructuremech:alfa_filament, GO:0005885, GO:0005818, GO:0000235, GO:0160111, GO:0160112, GO:1990716, GO:1990717, GO:0097540, GO:1990718, GO:0097545, GO:0005858, GO:0005879, GO:0160113, GO:0160110, GO:0160114, GO:0160115, GO:0005931, GO:0005930, GO:0097650, cellstructuremech:bactofilin_filament, cellstructuremech:basal_body_a_b_inner_junction, cellstructuremech:basal_body_a_c_linker, cellstructuremech:basal_body_a_tusk, cellstructuremech:basal_body_b_c_inner_junction, cellstructuremech:basal_body_c_tubule_hook, cellstructuremech:basal_body_c_tubule_luminal_filament, cellstructuremech:basal_body_cartwheel, cellstructuremech:basal_body_cartwheel_inner_density, cellstructuremech:basal_body_d2_rod, cellstructuremech:basal_body_filamentous_cartwheel_inner_density, cellstructuremech:basal_body_inner_scaffold, cellstructuremech:basal_body_pinhead, cellstructuremech:basal_body_triplet_base, GO:0020032, GO:0120120, cellstructuremech:btubab_bacterial_microtubule, GO:1990719, GO:1990720, GO:0000142, GO:0032174, GO:0000144, GO:0032177, GO:0061493, GO:0005823, cellstructuremech:cetz_filament, GO:0032166, GO:0036064, GO:0120269, GO:1990900, GO:0120280, GO:0035253, GO:0032161, GO:0020010, cellstructuremech:crescentin_filament, cellstructuremech:cryptophyte_cortical_centrin_network, GO:0097268, GO:0005881, cellstructuremech:cytostomal_cord, GO:0032123, cellstructuremech:distal_connecting_fiber, GO:0036286, GO:0061645, cellstructuremech:entodiniomorphid_subkinetal_myoneme_system, GO:0000923, GO:0120119, cellstructuremech:funis, GO:0000930, GO:0000931, GO:0008275, GO:0032171, GO:0032172, GO:1990317, GO:0061496, GO:0005825, GO:0032117, GO:0062140, GO:0032163, GO:0032164, GO:0032168, cellstructuremech:icl1e_complex, cellstructuremech:infraciliary_lattice, GO:0036156, GO:0061497, GO:0005822, GO:0061498, GO:0005821, GO:0031021, GO:0160066, GO:0033289, cellstructuremech:mamk_filament, GO:1990819, GO:0032162, GO:0032175, GO:0036391, GO:0097568, GO:0110086, GO:0034993, cellstructuremech:meiotic_outer_plaque, GO:0032152, GO:0035974, GO:0005874, GO:0110085, GO:0032151, GO:0072686, GO:0044732, cellstructuremech:mreb_filament, GO:0071958, GO:0160067, GO:0005880, cellstructuremech:nucleus_basal_body_connector, GO:0071957, GO:0036157, GO:0061499, GO:0005824, cellstructuremech:parm_filament, cellstructuremech:peritrich_body_myoneme_system, cellstructuremech:phuz_spindle, GO:0020031, GO:1990295, GO:0032157, GO:0032165, GO:0032169, GO:0032170, cellstructuremech:quiescent_cell_microtubule_bundle, cellstructuremech:quiescent_nuclear_microtubule_bundle, cellstructuremech:radial_microtubule_organizing_center, GO:0001534, GO:0001535, GO:0120343, GO:0001536, GO:1990612, GO:0032158, GO:0032159, GO:0032173, GO:0031105, GO:0032156, GO:0032160, GO:0005940, GO:0160065, GO:1990334, cellstructuremech:sinister_fiber, GO:0005819, GO:0005876, GO:0051233, GO:0000922, GO:0005816, cellstructuremech:spindle_pole_body_duplication_plaque, cellstructuremech:spindle_pole_body_satellite, cellstructuremech:spirostomum_myoneme_fishnet, GO:0032176, cellstructuremech:stalk_spasmoneme, cellstructuremech:stentor_km_fiber, cellstructuremech:stentor_myoneme_system, cellstructuremech:stentor_perialgal_microtubule_meshwork, GO:0020025, GO:0070850, cellstructuremech:telocentrosome, cellstructuremech:transition_zone_stellate_fiber_system, GO:0120121, cellstructuremech:tubulin_spool, cellstructuremech:tubz_filament, GO:0097597, GO:0097595, GO:0097594, GO:0097591, GO:0097593, GO:0097592, GO:0097596. All 173 records in data/structures/cytoskeleton/ represent distinct cytoskeletal filaments, MTOCs, septin assemblies, eisosome/MCC complexes, or motor/adaptor subcomplexes.

## Evidence

| Evidence | Reference / locator | Support | Observation |
| --- | --- | --- | --- |
| ev_strict_cyto | scripts/validate_strict.py; strict receipt | supports | validate_strict.py exited 0 across all 978 records including all 173 cytoskeleton records. |
| ev_labels_cyto | scripts/validate_id_label_correspondence.py; labels receipt | supports | validate_id_label_correspondence.py exited 0 across all ontology targets. |
| ev_cyto_subcomplex_nodes | data/structures/cytoskeleton/actin_cortical_patch.yaml; actin_cortical_patch.yaml (arp2_3_complex), equatorial/interphase_microtubule_organizing_center.yaml &amp; telocentrosome.yaml (gamma_tuc), radial_spoke.yaml (radial_spoke_head/neck/stalk) | supports | Seven causal_graphs nodes across 5 cytoskeleton records reference GO-grounded PROTEIN_COMPLEX components (GO:0005885, GO:0000930, GO:0001535, GO:0120343, GO:0001536) but carry node_type: GENE_OR_PROTEIN without grounding instead of node_type: STRUCTURE. |
| ev_cyto_discussion_issues | data/structures/cytoskeleton/crescentin_filament.yaml; crescentin_filament.yaml discussions[1] (#1260), mreb_filament.yaml discussions[0] (#119), phuz_spindle.yaml discussions[0..1] (#481, #482) | supports | Four discussions entries across crescentin_filament.yaml, mreb_filament.yaml, and phuz_spindle.yaml mention repository issues (#1260, #119, #481, #482) in prose without structured GitHub issue URLs in their evidence lists. |

## Limits And Additional Notes

- Two minor cohort findings across 8 cytoskeleton records are queued for Stage 5 remediation.

## Complete Structured Record

The sibling review.yaml is authoritative.

```yaml
schema_version: 1.0.0
review_id: 20261023T091804Z-cytoskeleton-category-review
kind: category
repository: CultureBotAI/CellStructureMech
title: 'Category review of data/structures/cytoskeleton/ (173 records): GO subcomplex
  causal-node types and discussion issue evidence links'
started_at: '2026-10-23T09:10:15Z'
finished_at: '2026-10-23T09:18:04Z'
reviewer:
  identity: antigravity-stage4-record-review
  kind: agent
  model: claude-opus-4-6
  independence: independent
  independence_basis: Reviewed in Cycle 1 Stage 4 record_review against committed
    git revision 13c6b0d85338aa96d330b8d699587dfe270a21f9 without record edits in
    this stage.
skill: .claude/skills/review-yaml-category/SKILL.md
completion: completed
verdict: pass_with_limitations
native_verdict: PASS_WITH_FOLLOW_UP
scientific_review: true
summary: 'Full-coverage category review of all 173 records in data/structures/cytoskeleton/
  verified distinct filament, MTOC, septin, eisosome, and motor-complex boundaries.
  Two minor cohort patterns were identified across 8 records: (F1) 7 causal-graph
  nodes across 5 records reference GO-grounded PROTEIN_COMPLEX subcomplex components
  (Arp2/3 complex GO:0005885, gamma-tubulin complex GO:0000930, radial spoke head/neck/stalk
  GO:0001535/GO:0120343/GO:0001536) but are typed GENE_OR_PROTEIN without grounding
  instead of STRUCTURE; and (F2) 3 records (crescentin_filament.yaml, mreb_filament.yaml,
  phuz_spindle.yaml) cite repository issues (#1260, #119, #481, #482) in discussions
  prose without structured evidence links.'
source:
  git_revision: 13c6b0d85338aa96d330b8d699587dfe270a21f9
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
  - path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
    sha256: ce35e4855b506178485b229b515c89a717ddee0a5a9d26fff88ba991fac5b06b
    role: target
  - path: data/structures/cytoskeleton/actin_body.yaml
    sha256: b0abd6f5cb40fec99ab2d5a23a56b7307041f4ac8eda2a32b9db8d57680f22ea
    role: target
  - path: data/structures/cytoskeleton/actin_cortical_patch.yaml
    sha256: 4b005ca985e36cdca47ff20271c2b31cc00b47a080e1da614265469d6adaaf8a
    role: target
  - path: data/structures/cytoskeleton/actomyosin_contractile_ring.yaml
    sha256: 8876e95f0d7f8046d816cde2038818cced5d3b5996858dfb564d41b4ecac47ff
    role: target
  - path: data/structures/cytoskeleton/alfa_filament.yaml
    sha256: 9869708619647267114ce2cb97912536765e482595c4026025d6307f849e02ba
    role: target
  - path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    sha256: a612b062735844ba209722df0054d084db27ef18e8a243dc32d6d180303fd44b
    role: target
  - path: data/structures/cytoskeleton/aster.yaml
    sha256: ed329cc165c49478a9cad71b9a56809631bed2891dd09a46d8a4cce1523f3ae7
    role: target
  - path: data/structures/cytoskeleton/astral_microtubule.yaml
    sha256: 7c5c19cbf7cc39406dcc7d8bf376e4fcff12dcf7c71f702cf8058e766138be1f
    role: target
  - path: data/structures/cytoskeleton/axonemal_a_tubule_inner_sheath.yaml
    sha256: 23bcdab335f1f6b6f39da802471c2336ab47ed2083b4986133b9558f42d4f7c0
    role: target
  - path: data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml
    sha256: d1b0e481219c8b248e22e069aaa333074857a9ef8cae74d159e9a9e1f33a733e
    role: target
  - path: data/structures/cytoskeleton/axonemal_central_apparatus.yaml
    sha256: 74e419f358ba3717a764cd93cb5c0e4e892c7015094ed6457518994526ee1899
    role: target
  - path: data/structures/cytoskeleton/axonemal_central_bridge.yaml
    sha256: 488bf49e662fd058a77ae30e822399a25c8079ea423dc663a8523f364de07e71
    role: target
  - path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    sha256: 5e6d9301edf395d718469728f33d6fd7aad90d01bea8bf84b31ba6a742e7cf75
    role: target
  - path: data/structures/cytoskeleton/axonemal_central_pair_projection.yaml
    sha256: 3474d5bb5742dd4f8064e544f426f6fc79c552c808f444d536ca258d2479581a
    role: target
  - path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    sha256: 8ca9df0aa3b658a662383c2f1b4489b029699d011828f35b4e2d82ecb2fa40b6
    role: target
  - path: data/structures/cytoskeleton/axonemal_dynein_complex.yaml
    sha256: 9158b3b827892de2d3f14320353af5fbd6ef8ef3cfae114687b9e6725f7ce44e
    role: target
  - path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    sha256: 480cd29d1f2e87c07c19dd8d60e50768cdcce29223b28ce2df1d4c956dc46282
    role: target
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_junction.yaml
    sha256: b2b8871710df39db8cea586df9f0ad41f852297f6061e0efb6a6e33bd39b5adf
    role: target
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_sheath.yaml
    sha256: 9e9be5e7f27009254e123e548fe1c5bbfd4bbacb87f856eec8f868fb605c0f9e
    role: target
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_outer_junction.yaml
    sha256: 226a02455cd0afbaedc49a3c74a986e5f6bab41d60e1240d98249ee656e5ac10
    role: target
  - path: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
    sha256: 8966a4edaaa6f5f1645bded7428c44111b6213badd19bb0051e6473062dba3ce
    role: target
  - path: data/structures/cytoskeleton/axonemal_nexin_link.yaml
    sha256: d55ca69b76b3b435e76e88185ee89256f4133ce7a0da1e819c5f3a18e5264188
    role: target
  - path: data/structures/cytoskeleton/axoneme.yaml
    sha256: 0b91b4cd41d1a34bdc3883d988f31009effc74347b881cdc5c9b66014704e223
    role: target
  - path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    sha256: 14dc7bee2d7f4dbaf766868cb49cb2e0145765a5de184a80452664871a7db50f
    role: target
  - path: data/structures/cytoskeleton/bactofilin_filament.yaml
    sha256: 622cf3533ca2672077d567c9fc018232e73a2638b40d4ed56ad6db296c535cfd
    role: target
  - path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    sha256: 6ca65191f50d079b7e7b0d807e6df7e2b1651eed1671d8a55029b7241bc80be4
    role: target
  - path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
    sha256: 3af66e82de4894039af1d1592b40a3d2e9f4e4fa331d27223d0344f16e9ee7f6
    role: target
  - path: data/structures/cytoskeleton/basal_body_a_tusk.yaml
    sha256: f82923b0febf504980e0c7e006d03d72c9cfdd2b38e225b6ad82adaac4d754c1
    role: target
  - path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    sha256: 9c4967f2edcd2ccc044157dd3bc03ed3f066d5bcd7205e2f5cc30da20e858ea1
    role: target
  - path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
    sha256: 492ed1f70c96fec1ccf2f5eb0efbb7ed4950b46f69031242a1869c9c820ee383
    role: target
  - path: data/structures/cytoskeleton/basal_body_c_tubule_luminal_filament.yaml
    sha256: a7abec342419ed1f405caf67d4fbaf85d1ce7587db5391a73bfeb136509aa1b1
    role: target
  - path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    sha256: ad4e6fcf7639e0fffc00b553b0ab2e0e2a8eac5981b87ae9da1ee783ba942957
    role: target
  - path: data/structures/cytoskeleton/basal_body_cartwheel_inner_density.yaml
    sha256: cc7469f2607b02f62b092c115aac1669dd80865e82be6462c10e3dec866dfc00
    role: target
  - path: data/structures/cytoskeleton/basal_body_d2_rod.yaml
    sha256: acd457cb1d0121248e5d11bdebc1d70a815a42f240f31e02eaa556bc54e7bc27
    role: target
  - path: data/structures/cytoskeleton/basal_body_filamentous_cartwheel_inner_density.yaml
    sha256: 5fc268e1a3493fde87ab6856fae60c61025633bdbc9c7d29c08c794c5678d8df
    role: target
  - path: data/structures/cytoskeleton/basal_body_inner_scaffold.yaml
    sha256: 40a6d03ee9aefd5eab50c48f90976e90aedb1e9be33ac13aceccbcc6b5fb6c0e
    role: target
  - path: data/structures/cytoskeleton/basal_body_pinhead.yaml
    sha256: ef3da1eee8d7e92150c0bf3ab1c6e2c67a410aa366416ab03454e3929e25bff2
    role: target
  - path: data/structures/cytoskeleton/basal_body_triplet_base.yaml
    sha256: c88a6c10f311bce934e37d5583f122fee6cae6f45950117728cb6d1a7905e6f8
    role: target
  - path: data/structures/cytoskeleton/basal_ring_of_apical_complex.yaml
    sha256: 72cfdcad53fe8d4a31deb6bfcab9454b8ef840b5ea6aebefb35256140e4fc649
    role: target
  - path: data/structures/cytoskeleton/bilobe_structure.yaml
    sha256: e9773e92e7c1414e2124d38c525927487c6fe03a7efd44440f00e19755de8a63
    role: target
  - path: data/structures/cytoskeleton/btubab_bacterial_microtubule.yaml
    sha256: cfd4cb0c8ba5958bda186e8eb4bc395c85461a3337bfd947b622c7d4e04ef4bf
    role: target
  - path: data/structures/cytoskeleton/c1_axonemal_microtubule.yaml
    sha256: 2f4f420d4958d3133a60a7b072e517361d7c2c4908acb4e307bd2033095f18f4
    role: target
  - path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    sha256: 97c8666ddef318d146a2d902a225f8b0313468bcf54fa32d81d5f1d127798a44
    role: target
  - path: data/structures/cytoskeleton/cellular_bud_neck_contractile_ring.yaml
    sha256: 98f13751880cb87993310078d3409a400df4ccbaad0f9499f9b76a2be4538280
    role: target
  - path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    sha256: 2901b13c5e8db9e171b7c1f93caf816991d0e58ba9456339c5db7f7f3716ae0e
    role: target
  - path: data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml
    sha256: 6ef4f3536140aa328f20854cf2ef1db86b5508676f475e9a3282f932819546d1
    role: target
  - path: data/structures/cytoskeleton/cellular_bud_neck_split_septin_rings.yaml
    sha256: c76ed8c617acf9966daa42ca587f49cc352795bc3e2b9fe702359075c49a9cff
    role: target
  - path: data/structures/cytoskeleton/central_plaque_of_mitotic_spindle_pole_body.yaml
    sha256: 7276a4205e01b2df88459ebd1d3dcd58ddf53677cd21be367e0d9e3667db70f5
    role: target
  - path: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
    sha256: b81ebcb1048c0454cde531ad51c3b0df92769b6c7236e07012ce9e3cef369527
    role: target
  - path: data/structures/cytoskeleton/cetz_filament.yaml
    sha256: 63215aac67bf4bbcdb4d43b73b27c0fef9420bca2eedda06d78cceacf63f253e
    role: target
  - path: data/structures/cytoskeleton/chlamydospore_septin_filament_array.yaml
    sha256: 716764f6ed0bcbbb41f86d89e51272e96c0ac83ca56ef41c71dd5ff23f7a3481
    role: target
  - path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    sha256: 46027bf3d3d8b3011803fa72d1229a892d34b7233d48ca290466b9afefb6b7ef
    role: target
  - path: data/structures/cytoskeleton/ciliary_centrin_arm.yaml
    sha256: 459a2b5ece1620d7d617ef459cca0bd2a1020441201b80e83ecaa09c78299ec6
    role: target
  - path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    sha256: df0530c9582d0a40d8e0c646cdaa88cc0872d1e6e034cbdcd068b2a3f426ec3a
    role: target
  - path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
    sha256: 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4
    role: target
  - path: data/structures/cytoskeleton/ciliary_rootlet.yaml
    sha256: a4ce875de28c94730588bfb1549dd6dc38b28658e3f3d66b8cb6fe66859433b3
    role: target
  - path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    sha256: 07dd82a0f5ad6f6a473e9305c85bf0de6ca336f573878668664e2ee44dbc90e1
    role: target
  - path: data/structures/cytoskeleton/conoid.yaml
    sha256: f45c77a22694ab07d2abdf0954141d0a99579150924d64e605387e067cf0a501
    role: target
  - path: data/structures/cytoskeleton/crescentin_filament.yaml
    sha256: 8a7528bc96ddf0c0d8935ba4a308d49e7390262d09de979fe5138dbf1fcd2f0a
    role: target
  - path: data/structures/cytoskeleton/cryptophyte_cortical_centrin_network.yaml
    sha256: cb0d5b64a7ea83ca03ae0ec91abad982f682314b29d0e89fe0f62cbaa2072819
    role: target
  - path: data/structures/cytoskeleton/cytoophidium.yaml
    sha256: 4e75070209f20d340a776a5ea708588484f39dc1f0a8859a0f0520ba2acda553
    role: target
  - path: data/structures/cytoskeleton/cytoplasmic_microtubule.yaml
    sha256: 23b89e56b6a009464465814315eaa0f663df8429a15f78dc62bcc79711b82005
    role: target
  - path: data/structures/cytoskeleton/cytostomal_cord.yaml
    sha256: 24269590b15ed4830dc083638b561e5b79f141d7d36b3b6199602a1a4ae633dd
    role: target
  - path: data/structures/cytoskeleton/deep_fiber.yaml
    sha256: 7868013c7bf3ce1c327c9106136b716f305afebe4efe5d49412e69278d26d702
    role: target
  - path: data/structures/cytoskeleton/distal_connecting_fiber.yaml
    sha256: 3fbecc2d7d51c4e4ea53cdbc4d6e49251a300430f23fc0d76d00a3412a2a8d79
    role: target
  - path: data/structures/cytoskeleton/eisosome_filament.yaml
    sha256: dba11b89f8cc8d874eae359238715f5fdb0d8a3da2ff551cc43b58b8aacd156b
    role: target
  - path: data/structures/cytoskeleton/endocytic_patch.yaml
    sha256: 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd
    role: target
  - path: data/structures/cytoskeleton/entodiniomorphid_subkinetal_myoneme_system.yaml
    sha256: d2a4795123a8de62db9e270237cc7e5c1b3f2fb29655f4d3af6f158e6d0ebaeb
    role: target
  - path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    sha256: a8621a1fd05b6f1b997635eb62c3f743083f09c1b9e696fe0e0281ac384b9b7e
    role: target
  - path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    sha256: 1477cd38547a428f9625e08f7bf061c7a3f320b5710cfe736a7d722700221b8f
    role: target
  - path: data/structures/cytoskeleton/funis.yaml
    sha256: f4410ba245ffdd163c6cbff4adf7292cb348b39ff2952c7484091aaeed4aa9be
    role: target
  - path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    sha256: c8f46fb3cb6d1a5a9c2ebdc657cc357bba4a05d8904b005c1836dadffe906182
    role: target
  - path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    sha256: 411a47cbbdad6599e88f4328dc0d8e745a05a46c4815177adaf73e2c3e89f728
    role: target
  - path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    sha256: 4a9e3e657b2e17962527694dd078c1a74dbed1e83ffb32752675a25332754468
    role: target
  - path: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
    sha256: 2b38e6f9051b64b36fe4bb52206122b35d060e5146d548622573303fe0378732
    role: target
  - path: data/structures/cytoskeleton/germ_tube_septin_ring.yaml
    sha256: f1420625e020c7842cf281f96450b246edd350c32060c3d3186130d45ec012a0
    role: target
  - path: data/structures/cytoskeleton/gin4_complex.yaml
    sha256: 92702fe584fd086c30d5fee9fe8aaee5d8ec0e8938606710a09e6c2954428f43
    role: target
  - path: data/structures/cytoskeleton/half_bridge_of_mitotic_spindle_pole_body.yaml
    sha256: 774a31a26d3323f1395c6db0de2a0f68cdeaa17d1d68b97900e364455c3b43d4
    role: target
  - path: data/structures/cytoskeleton/half_bridge_of_spindle_pole_body.yaml
    sha256: c9420adeab4b1029037608be6b66ee738a0d5b6b1559fd7aa8742b256ce4f3bb
    role: target
  - path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    sha256: 73abc8f115d095e86ee315409c2221a5a97b37fad16effdb8593c6b9655568de
    role: target
  - path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
    sha256: 9e143ed6218b251660020e57fd99c4758ea02e5ce91e6cf8de3133f626d08f26
    role: target
  - path: data/structures/cytoskeleton/hyphal_septin_band.yaml
    sha256: ca28b60ce59664d282f0379709392c10f211dbc1be34fc1bab90840285a429d7
    role: target
  - path: data/structures/cytoskeleton/hyphal_septin_cap.yaml
    sha256: ca2f4c8585ae8b00261d85983033efe1b63fc690a5f316d4b0506200927a9d2f
    role: target
  - path: data/structures/cytoskeleton/hyphal_septin_ring.yaml
    sha256: 9b8a399ed470a314cf73b6a4df6c4e14bf8d2cda618eb091f7c02f557c5252cf
    role: target
  - path: data/structures/cytoskeleton/icl1e_complex.yaml
    sha256: 1c27b35fb37f183dd5aa251395e359541721525d3a76f76263664d0d09a379e0
    role: target
  - path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    sha256: 40b4b68e4354201ceabd0605deeafc8ce5a71c14e6457d075e5a6fe0d082cf9e
    role: target
  - path: data/structures/cytoskeleton/inner_dynein_arm.yaml
    sha256: 30f955bace0501cfaac21cf19540023e78ddd2acddb1107a78412c6debdc7da3
    role: target
  - path: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
    sha256: c7d1f6c1fa0f5928a0d3bc67d245eb0d3e655798fc62e719990248707765aff8
    role: target
  - path: data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
    sha256: 663b2ccb7bf2a427807d0156bb33feb5c96ce978649f091ed5a9a2b4723a0dba
    role: target
  - path: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
    sha256: 6babc40661cf4080adb6b1c5e18c42a78c7b1cffddae612a3288fee4926c98e5
    role: target
  - path: data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
    sha256: 3c889767d96b20dae86ccb3327892d5d33a5892591133cd4dcea4ad17a4b07c0
    role: target
  - path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
    sha256: e16c54c5053f30b3da52fae3a7b2eeb0afb18d2580bff4e95d3b69071160b7ca
    role: target
  - path: data/structures/cytoskeleton/interphase_sin_signaling_complex.yaml
    sha256: b3a359eac1e3973709e48eea87d5b9b7ecdc16ad1372d573b15bcc88ad91ef40
    role: target
  - path: data/structures/cytoskeleton/intraconoid_microtubule.yaml
    sha256: 6744611709c76a74cc30a2ca22fe118e1b87cc3aeabb5199df81a210b2fced41
    role: target
  - path: data/structures/cytoskeleton/mamk_filament.yaml
    sha256: fb273942dd11b99a71c61834f5ca331829a340b6a271e0f73e050c1b0128ca64
    role: target
  - path: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
    sha256: e0b5696c74beabb751e5334fd04492a057d4b3fceeedf87f7b1c59978e172b1e
    role: target
  - path: data/structures/cytoskeleton/mating_projection_septin_band.yaml
    sha256: e68377ea65b5be456416810adb14479747220176a957b97f6d3ce3f5e731354d
    role: target
  - path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    sha256: 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6
    role: target
  - path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    sha256: 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6
    role: target
  - path: data/structures/cytoskeleton/median_body.yaml
    sha256: d8acb0b396e2f02d12854bfcef95a7a2bc67b6be648058230971e38d1b7e757f
    role: target
  - path: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
    sha256: 482e30c182b04c65329ec8652cc472449ece53ac9c60657f1ae6bb6ceface019
    role: target
  - path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    sha256: 1edc92bdba11eec4c3da00ba06bd5cae3bd2593f5ba94be9d545c52a9da86049
    role: target
  - path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    sha256: 5482b05be175efef27e7e2acd73c2a7fb6cddbd69ebe7c430ed0adc3f858bfe9
    role: target
  - path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
    sha256: 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9
    role: target
  - path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    sha256: 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75
    role: target
  - path: data/structures/cytoskeleton/microtubule.yaml
    sha256: 06773fdcef54b61e7ed2a8a4c1066dfed8ba71dce8050eb39a879fab702b7498
    role: target
  - path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
    sha256: d74335a45d6c7037868c200e25a7fe12bc73121536cd32e68be983a3ebf6e9ac
    role: target
  - path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
    sha256: 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e
    role: target
  - path: data/structures/cytoskeleton/mitotic_spindle.yaml
    sha256: 85b2e3d0b8037dec88990c0d95901bd9005766e7d01067c5744c46894ec3d1a6
    role: target
  - path: data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
    sha256: 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329
    role: target
  - path: data/structures/cytoskeleton/mreb_filament.yaml
    sha256: b27d315ff07c11f2aa9eb1f1c1f4c65203ba62509fe6999c7804397e76ab9711
    role: target
  - path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    sha256: 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82
    role: target
  - path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    sha256: 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae
    role: target
  - path: data/structures/cytoskeleton/nuclear_microtubule.yaml
    sha256: 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252
    role: target
  - path: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
    sha256: 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d
    role: target
  - path: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
    sha256: 84c9dc88c397f90a6c90dc61031b9f5334baa65580eaecc16cc851cacc54840b
    role: target
  - path: data/structures/cytoskeleton/outer_dynein_arm.yaml
    sha256: b394df130fce9a7cfd91a9d76a0c7be847e89f5bc471827f7836dbf988413fa8
    role: target
  - path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
    sha256: 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226
    role: target
  - path: data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
    sha256: 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142
    role: target
  - path: data/structures/cytoskeleton/parm_filament.yaml
    sha256: d021bb88e2999e696f67403cff71a22b39801ad248f2c1aa86d8e9360a33024b
    role: target
  - path: data/structures/cytoskeleton/peritrich_body_myoneme_system.yaml
    sha256: 85563af4f17c846111f087a0c6bd31b6480a9b5fff05df9a3eff79e0b25418f9
    role: target
  - path: data/structures/cytoskeleton/phuz_spindle.yaml
    sha256: 335a29b8efc518b066fdc5b44c9e6f4c777e2c1f5458f977a3b68595d9c13013
    role: target
  - path: data/structures/cytoskeleton/polar_ring_of_apical_complex.yaml
    sha256: ec70822af034fd9e33585bf8fa8894a6fd97cf8c2127fb6e29d91d842efd278b
    role: target
  - path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    sha256: f8b698394b595d435b10633cac0cef969d32aae261b770d3ea60b974e5c4cd15
    role: target
  - path: data/structures/cytoskeleton/prospore_contractile_ring.yaml
    sha256: 86ff161d77dbd6b182aab5d48cf4fa4376ad69ec739305c9b3c25c8aef103e51
    role: target
  - path: data/structures/cytoskeleton/prospore_septin_filament_array.yaml
    sha256: 39df294524bcae01b5a3c70410172ac4d19c6fb936a7bf970fda23a043220bfa
    role: target
  - path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    sha256: 56b764eb06dde6d49e5ad5135ab577218f765b63791ffe0483147d4186498da5
    role: target
  - path: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
    sha256: 725c892c096cf75b48bb0a26a1aad5d657d9e5e716851f07211b161ba4d04533
    role: target
  - path: data/structures/cytoskeleton/quiescent_cell_microtubule_bundle.yaml
    sha256: 6228e65ead4750033cd105250a703ffce6dfba328d05e94de0d26ae06b100bc8
    role: target
  - path: data/structures/cytoskeleton/quiescent_nuclear_microtubule_bundle.yaml
    sha256: 87b29df8262cfbc32a1bae44f4777edb2ba44663fe0bee22733cc95bc78400ea
    role: target
  - path: data/structures/cytoskeleton/radial_microtubule_organizing_center.yaml
    sha256: a6a2e4d87b3159afe989f1f838da6988395c5c2b0fc1b24bf1cde154f2dbc364
    role: target
  - path: data/structures/cytoskeleton/radial_spoke.yaml
    sha256: fdfeccafa1a5892150fe6a0da6971348e06ce6ca7123d69564ac70844f7f9993
    role: target
  - path: data/structures/cytoskeleton/radial_spoke_head.yaml
    sha256: bec66030c7916b9cf537e93d924b97e92b7590e049547920896e39108b19adaa
    role: target
  - path: data/structures/cytoskeleton/radial_spoke_neck.yaml
    sha256: 856f1fc78aecde5a603330227e494ac20ee930f25e04deca0ceb98d286c12418
    role: target
  - path: data/structures/cytoskeleton/radial_spoke_stalk.yaml
    sha256: 8747c08b214590fd435efacd64ee8fb09e56cf9e693fa193df256716c2703936
    role: target
  - path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    sha256: 2dc179231cae9404e022e417327a94b550b75c47872ef2e467330ea79d5cdf17
    role: target
  - path: data/structures/cytoskeleton/septin_band.yaml
    sha256: 41d269f0b9bd3a3814d8fd2bb5e3e26e933763e1b06c42a30e8b13e20f2865da
    role: target
  - path: data/structures/cytoskeleton/septin_cap.yaml
    sha256: 5dccebc18f9349148bd4ef1e64e29e42648d4df485e0f407c989be0d1b13f8ba
    role: target
  - path: data/structures/cytoskeleton/septin_collar.yaml
    sha256: c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9
    role: target
  - path: data/structures/cytoskeleton/septin_complex.yaml
    sha256: 4de023faea51c1ea084592fda0f5db6a95ae91f1a8de69de44a208099fcd8373
    role: target
  - path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    sha256: a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e
    role: target
  - path: data/structures/cytoskeleton/septin_filament_array.yaml
    sha256: 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0
    role: target
  - path: data/structures/cytoskeleton/septin_ring.yaml
    sha256: a29add3311f4b53bf4b50c2ec527d5ef450cfff625eadd312324d625b8790b93
    role: target
  - path: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
    sha256: 59f188a29d48dab89d1c7a36aee3bd8f67efe3110c7c981bbac7b60df20d8f4b
    role: target
  - path: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
    sha256: 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd
    role: target
  - path: data/structures/cytoskeleton/sinister_fiber.yaml
    sha256: 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5
    role: target
  - path: data/structures/cytoskeleton/spindle.yaml
    sha256: da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e
    role: target
  - path: data/structures/cytoskeleton/spindle_microtubule.yaml
    sha256: bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9
    role: target
  - path: data/structures/cytoskeleton/spindle_midzone.yaml
    sha256: 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661
    role: target
  - path: data/structures/cytoskeleton/spindle_pole.yaml
    sha256: c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204
    role: target
  - path: data/structures/cytoskeleton/spindle_pole_body.yaml
    sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
    role: target
  - path: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
    sha256: e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3
    role: target
  - path: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
    sha256: a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3
    role: target
  - path: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
    sha256: 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af
    role: target
  - path: data/structures/cytoskeleton/split_septin_rings.yaml
    sha256: 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff
    role: target
  - path: data/structures/cytoskeleton/stalk_spasmoneme.yaml
    sha256: a3de4646f57551323b08c225176359cf3737eff71eaab9da598131d646920bdb
    role: target
  - path: data/structures/cytoskeleton/stentor_km_fiber.yaml
    sha256: 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6
    role: target
  - path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
    sha256: 8396ff930730d215b773b9b9f40d5b0a4444e3e2c6581cde72dbd47358570941
    role: target
  - path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    sha256: 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf
    role: target
  - path: data/structures/cytoskeleton/subpellicular_microtubule.yaml
    sha256: 8fb4caeb1617731d37c9ae70ea44bcea84be14499211b86922bade11cdd6af83
    role: target
  - path: data/structures/cytoskeleton/tacc_tog_complex.yaml
    sha256: 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787
    role: target
  - path: data/structures/cytoskeleton/telocentrosome.yaml
    sha256: 05d5a42ee4b63bd62b3e8c6c0137e2268964980fcc00f27769e29498cf67dca7
    role: target
  - path: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
    sha256: ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36
    role: target
  - path: data/structures/cytoskeleton/tripartite_attachment_complex.yaml
    sha256: 4b20e1ac242cf6e988ee0ec52eefb537bdd7b1270c1c32c238183baa66c7dd52
    role: target
  - path: data/structures/cytoskeleton/tubulin_spool.yaml
    sha256: 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072
    role: target
  - path: data/structures/cytoskeleton/tubz_filament.yaml
    sha256: 0399b1e1569592d6be671444cb03e37d481ca5022d52a476dd3a75f21337355e
    role: target
  - path: data/structures/cytoskeleton/ventral_disc.yaml
    sha256: da4539d720be1cfa7e1e1b5ca12d86f57ededaebc6a869bdd2fc4bf13fb5680b
    role: target
  - path: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
    sha256: bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b
    role: target
  - path: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
    sha256: 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425
    role: target
  - path: data/structures/cytoskeleton/ventral_disc_lateral_crest.yaml
    sha256: 6a8127a748d9dcdb2e429d05d817626c02ffed35eb545eb501c0b101758db32b
    role: target
  - path: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
    sha256: 184540d5a0f41b8f04fa8e4cac937dc657481eaa999e5420ec315476801a07e3
    role: target
  - path: data/structures/cytoskeleton/ventral_disc_overlap_zone.yaml
    sha256: 983f27caa2fde019c9ab576e64c54bd354b6528a65e0f9ef9cdfbb87abb365ce
    role: target
  - path: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
    sha256: 54772643689f75f239cddf783180ab3eb0443695ea60080d966cbeb2fb0efe1f
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
  description: Full-cohort review of all 173 CellStructureRecord YAML files under
    data/structures/cytoskeleton/.
  selection: Complete folder cohort data/structures/cytoskeleton/*.yaml in the frozen
    978-record Stage 4 inventory.
  coverage: full
  population_size: 173
  reviewed_target_ids:
  - GO:0097649
  - GO:0099079
  - GO:0030479
  - GO:0005826
  - cellstructuremech:alfa_filament
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0160111
  - GO:0160112
  - GO:1990716
  - GO:1990717
  - GO:0097540
  - GO:1990718
  - GO:0097545
  - GO:0005858
  - GO:0005879
  - GO:0160113
  - GO:0160110
  - GO:0160114
  - GO:0160115
  - GO:0005931
  - GO:0005930
  - GO:0097650
  - cellstructuremech:bactofilin_filament
  - cellstructuremech:basal_body_a_b_inner_junction
  - cellstructuremech:basal_body_a_c_linker
  - cellstructuremech:basal_body_a_tusk
  - cellstructuremech:basal_body_b_c_inner_junction
  - cellstructuremech:basal_body_c_tubule_hook
  - cellstructuremech:basal_body_c_tubule_luminal_filament
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:basal_body_cartwheel_inner_density
  - cellstructuremech:basal_body_d2_rod
  - cellstructuremech:basal_body_filamentous_cartwheel_inner_density
  - cellstructuremech:basal_body_inner_scaffold
  - cellstructuremech:basal_body_pinhead
  - cellstructuremech:basal_body_triplet_base
  - GO:0020032
  - GO:0120120
  - cellstructuremech:btubab_bacterial_microtubule
  - GO:1990719
  - GO:1990720
  - GO:0000142
  - GO:0032174
  - GO:0000144
  - GO:0032177
  - GO:0061493
  - GO:0005823
  - cellstructuremech:cetz_filament
  - GO:0032166
  - GO:0036064
  - GO:0120269
  - GO:1990900
  - GO:0120280
  - GO:0035253
  - GO:0032161
  - GO:0020010
  - cellstructuremech:crescentin_filament
  - cellstructuremech:cryptophyte_cortical_centrin_network
  - GO:0097268
  - GO:0005881
  - cellstructuremech:cytostomal_cord
  - GO:0032123
  - cellstructuremech:distal_connecting_fiber
  - GO:0036286
  - GO:0061645
  - cellstructuremech:entodiniomorphid_subkinetal_myoneme_system
  - GO:0000923
  - GO:0120119
  - cellstructuremech:funis
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0032171
  - GO:0032172
  - GO:1990317
  - GO:0061496
  - GO:0005825
  - GO:0032117
  - GO:0062140
  - GO:0032163
  - GO:0032164
  - GO:0032168
  - cellstructuremech:icl1e_complex
  - cellstructuremech:infraciliary_lattice
  - GO:0036156
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:0160066
  - GO:0033289
  - cellstructuremech:mamk_filament
  - GO:1990819
  - GO:0032162
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0110086
  - GO:0034993
  - cellstructuremech:meiotic_outer_plaque
  - GO:0032152
  - GO:0035974
  - GO:0005874
  - GO:0110085
  - GO:0032151
  - GO:0072686
  - GO:0044732
  - cellstructuremech:mreb_filament
  - GO:0071958
  - GO:0160067
  - GO:0005880
  - cellstructuremech:nucleus_basal_body_connector
  - GO:0071957
  - GO:0036157
  - GO:0061499
  - GO:0005824
  - cellstructuremech:parm_filament
  - cellstructuremech:peritrich_body_myoneme_system
  - cellstructuremech:phuz_spindle
  - GO:0020031
  - GO:1990295
  - GO:0032157
  - GO:0032165
  - GO:0032169
  - GO:0032170
  - cellstructuremech:quiescent_cell_microtubule_bundle
  - cellstructuremech:quiescent_nuclear_microtubule_bundle
  - cellstructuremech:radial_microtubule_organizing_center
  - GO:0001534
  - GO:0001535
  - GO:0120343
  - GO:0001536
  - GO:1990612
  - GO:0032158
  - GO:0032159
  - GO:0032173
  - GO:0031105
  - GO:0032156
  - GO:0032160
  - GO:0005940
  - GO:0160065
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005819
  - GO:0005876
  - GO:0051233
  - GO:0000922
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_myoneme_system
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0020025
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - GO:0120121
  - cellstructuremech:tubulin_spool
  - cellstructuremech:tubz_filament
  - GO:0097597
  - GO:0097595
  - GO:0097594
  - GO:0097591
  - GO:0097593
  - GO:0097592
  - GO:0097596
targets:
- target_id: GO:0097649
  path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
  label: A axonemal microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ce35e4855b506178485b229b515c89a717ddee0a5a9d26fff88ba991fac5b06b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/a_axonemal_microtubule.yaml
    role: maintained_record
- target_id: GO:0099079
  path: data/structures/cytoskeleton/actin_body.yaml
  label: actin body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b0abd6f5cb40fec99ab2d5a23a56b7307041f4ac8eda2a32b9db8d57680f22ea
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/actin_body.yaml
    role: maintained_record
- target_id: GO:0030479
  path: data/structures/cytoskeleton/actin_cortical_patch.yaml
  label: actin cortical patch
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4b005ca985e36cdca47ff20271c2b31cc00b47a080e1da614265469d6adaaf8a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/actin_cortical_patch.yaml
    role: maintained_record
- target_id: GO:0005826
  path: data/structures/cytoskeleton/actomyosin_contractile_ring.yaml
  label: actomyosin contractile ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8876e95f0d7f8046d816cde2038818cced5d3b5996858dfb564d41b4ecac47ff
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/actomyosin_contractile_ring.yaml
    role: maintained_record
- target_id: cellstructuremech:alfa_filament
  path: data/structures/cytoskeleton/alfa_filament.yaml
  label: AlfA filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9869708619647267114ce2cb97912536765e482595c4026025d6307f849e02ba
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/alfa_filament.yaml
    role: maintained_record
- target_id: GO:0005885
  path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
  label: Arp2/3 protein complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a612b062735844ba209722df0054d084db27ef18e8a243dc32d6d180303fd44b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/arp2_3_protein_complex.yaml
    role: maintained_record
- target_id: GO:0005818
  path: data/structures/cytoskeleton/aster.yaml
  label: aster
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ed329cc165c49478a9cad71b9a56809631bed2891dd09a46d8a4cce1523f3ae7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/aster.yaml
    role: maintained_record
- target_id: GO:0000235
  path: data/structures/cytoskeleton/astral_microtubule.yaml
  label: astral microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7c5c19cbf7cc39406dcc7d8bf376e4fcff12dcf7c71f702cf8058e766138be1f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/astral_microtubule.yaml
    role: maintained_record
- target_id: GO:0160111
  path: data/structures/cytoskeleton/axonemal_a_tubule_inner_sheath.yaml
  label: axonemal A tubule inner sheath
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 23bcdab335f1f6b6f39da802471c2336ab47ed2083b4986133b9558f42d4f7c0
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_a_tubule_inner_sheath.yaml
    role: maintained_record
- target_id: GO:0160112
  path: data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml
  label: axonemal B tubule inner sheath
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d1b0e481219c8b248e22e069aaa333074857a9ef8cae74d159e9a9e1f33a733e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_b_tubule_inner_sheath.yaml
    role: maintained_record
- target_id: GO:1990716
  path: data/structures/cytoskeleton/axonemal_central_apparatus.yaml
  label: axonemal central apparatus
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 74e419f358ba3717a764cd93cb5c0e4e892c7015094ed6457518994526ee1899
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_apparatus.yaml
    role: maintained_record
- target_id: GO:1990717
  path: data/structures/cytoskeleton/axonemal_central_bridge.yaml
  label: axonemal central bridge
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 488bf49e662fd058a77ae30e822399a25c8079ea423dc663a8523f364de07e71
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_bridge.yaml
    role: maintained_record
- target_id: GO:0097540
  path: data/structures/cytoskeleton/axonemal_central_pair.yaml
  label: axonemal central pair
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5e6d9301edf395d718469728f33d6fd7aad90d01bea8bf84b31ba6a742e7cf75
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_pair.yaml
    role: maintained_record
- target_id: GO:1990718
  path: data/structures/cytoskeleton/axonemal_central_pair_projection.yaml
  label: axonemal central pair projection
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3474d5bb5742dd4f8064e544f426f6fc79c552c808f444d536ca258d2479581a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_central_pair_projection.yaml
    role: maintained_record
- target_id: GO:0097545
  path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
  label: axonemal doublet microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8ca9df0aa3b658a662383c2f1b4489b029699d011828f35b4e2d82ecb2fa40b6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_doublet_microtubule.yaml
    role: maintained_record
- target_id: GO:0005858
  path: data/structures/cytoskeleton/axonemal_dynein_complex.yaml
  label: axonemal dynein complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9158b3b827892de2d3f14320353af5fbd6ef8ef3cfae114687b9e6725f7ce44e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_dynein_complex.yaml
    role: maintained_record
- target_id: GO:0005879
  path: data/structures/cytoskeleton/axonemal_microtubule.yaml
  label: axonemal microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 480cd29d1f2e87c07c19dd8d60e50768cdcce29223b28ce2df1d4c956dc46282
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule.yaml
    role: maintained_record
- target_id: GO:0160113
  path: data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_junction.yaml
  label: axonemal microtubule doublet inner junction
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b2b8871710df39db8cea586df9f0ad41f852297f6061e0efb6a6e33bd39b5adf
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_junction.yaml
    role: maintained_record
- target_id: GO:0160110
  path: data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_sheath.yaml
  label: axonemal microtubule doublet inner sheath
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9e9be5e7f27009254e123e548fe1c5bbfd4bbacb87f856eec8f868fb605c0f9e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule_doublet_inner_sheath.yaml
    role: maintained_record
- target_id: GO:0160114
  path: data/structures/cytoskeleton/axonemal_microtubule_doublet_outer_junction.yaml
  label: axonemal microtubule doublet outer junction
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 226a02455cd0afbaedc49a3c74a986e5f6bab41d60e1240d98249ee656e5ac10
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule_doublet_outer_junction.yaml
    role: maintained_record
- target_id: GO:0160115
  path: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
  label: axonemal microtubule doublet ribbon
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8966a4edaaa6f5f1645bded7428c44111b6213badd19bb0051e6473062dba3ce
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_microtubule_doublet_ribbon.yaml
    role: maintained_record
- target_id: GO:0005931
  path: data/structures/cytoskeleton/axonemal_nexin_link.yaml
  label: axonemal nexin link
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d55ca69b76b3b435e76e88185ee89256f4133ce7a0da1e819c5f3a18e5264188
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axonemal_nexin_link.yaml
    role: maintained_record
- target_id: GO:0005930
  path: data/structures/cytoskeleton/axoneme.yaml
  label: axoneme
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0b91b4cd41d1a34bdc3883d988f31009effc74347b881cdc5c9b66014704e223
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/axoneme.yaml
    role: maintained_record
- target_id: GO:0097650
  path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
  label: B axonemal microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 14dc7bee2d7f4dbaf766868cb49cb2e0145765a5de184a80452664871a7db50f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/b_axonemal_microtubule.yaml
    role: maintained_record
- target_id: cellstructuremech:bactofilin_filament
  path: data/structures/cytoskeleton/bactofilin_filament.yaml
  label: bactofilin filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 622cf3533ca2672077d567c9fc018232e73a2638b40d4ed56ad6db296c535cfd
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/bactofilin_filament.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_a_b_inner_junction
  path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
  label: basal body A-B inner junction
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6ca65191f50d079b7e7b0d807e6df7e2b1651eed1671d8a55029b7241bc80be4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_b_inner_junction.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_a_c_linker
  path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
  label: basal body A-C linker
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3af66e82de4894039af1d1592b40a3d2e9f4e4fa331d27223d0344f16e9ee7f6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_c_linker.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_a_tusk
  path: data/structures/cytoskeleton/basal_body_a_tusk.yaml
  label: basal body A-tusk
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f82923b0febf504980e0c7e006d03d72c9cfdd2b38e225b6ad82adaac4d754c1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_a_tusk.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_b_c_inner_junction
  path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
  label: basal body B-C inner junction
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9c4967f2edcd2ccc044157dd3bc03ed3f066d5bcd7205e2f5cc30da20e858ea1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_b_c_inner_junction.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_c_tubule_hook
  path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
  label: basal body C-tubule hook
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 492ed1f70c96fec1ccf2f5eb0efbb7ed4950b46f69031242a1869c9c820ee383
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_c_tubule_hook.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_c_tubule_luminal_filament
  path: data/structures/cytoskeleton/basal_body_c_tubule_luminal_filament.yaml
  label: basal body C-tubule luminal filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a7abec342419ed1f405caf67d4fbaf85d1ce7587db5391a73bfeb136509aa1b1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_c_tubule_luminal_filament.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_cartwheel
  path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
  label: basal body cartwheel
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ad4e6fcf7639e0fffc00b553b0ab2e0e2a8eac5981b87ae9da1ee783ba942957
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_cartwheel.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_cartwheel_inner_density
  path: data/structures/cytoskeleton/basal_body_cartwheel_inner_density.yaml
  label: basal body cartwheel inner density
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: cc7469f2607b02f62b092c115aac1669dd80865e82be6462c10e3dec866dfc00
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_cartwheel_inner_density.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_d2_rod
  path: data/structures/cytoskeleton/basal_body_d2_rod.yaml
  label: basal body D2-rod
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: acd457cb1d0121248e5d11bdebc1d70a815a42f240f31e02eaa556bc54e7bc27
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_d2_rod.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_filamentous_cartwheel_inner_density
  path: data/structures/cytoskeleton/basal_body_filamentous_cartwheel_inner_density.yaml
  label: basal body filamentous cartwheel inner density
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5fc268e1a3493fde87ab6856fae60c61025633bdbc9c7d29c08c794c5678d8df
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_filamentous_cartwheel_inner_density.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_inner_scaffold
  path: data/structures/cytoskeleton/basal_body_inner_scaffold.yaml
  label: basal body inner scaffold
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 40a6d03ee9aefd5eab50c48f90976e90aedb1e9be33ac13aceccbcc6b5fb6c0e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_inner_scaffold.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_pinhead
  path: data/structures/cytoskeleton/basal_body_pinhead.yaml
  label: basal body pinhead
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ef3da1eee8d7e92150c0bf3ab1c6e2c67a410aa366416ab03454e3929e25bff2
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_pinhead.yaml
    role: maintained_record
- target_id: cellstructuremech:basal_body_triplet_base
  path: data/structures/cytoskeleton/basal_body_triplet_base.yaml
  label: basal body triplet base
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c88a6c10f311bce934e37d5583f122fee6cae6f45950117728cb6d1a7905e6f8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_body_triplet_base.yaml
    role: maintained_record
- target_id: GO:0020032
  path: data/structures/cytoskeleton/basal_ring_of_apical_complex.yaml
  label: basal ring of apical complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 72cfdcad53fe8d4a31deb6bfcab9454b8ef840b5ea6aebefb35256140e4fc649
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/basal_ring_of_apical_complex.yaml
    role: maintained_record
- target_id: GO:0120120
  path: data/structures/cytoskeleton/bilobe_structure.yaml
  label: bilobe structure
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e9773e92e7c1414e2124d38c525927487c6fe03a7efd44440f00e19755de8a63
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/bilobe_structure.yaml
    role: maintained_record
- target_id: cellstructuremech:btubab_bacterial_microtubule
  path: data/structures/cytoskeleton/btubab_bacterial_microtubule.yaml
  label: BtubAB bacterial microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: cfd4cb0c8ba5958bda186e8eb4bc395c85461a3337bfd947b622c7d4e04ef4bf
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/btubab_bacterial_microtubule.yaml
    role: maintained_record
- target_id: GO:1990719
  path: data/structures/cytoskeleton/c1_axonemal_microtubule.yaml
  label: C1 axonemal microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2f4f420d4958d3133a60a7b072e517361d7c2c4908acb4e307bd2033095f18f4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/c1_axonemal_microtubule.yaml
    role: maintained_record
- target_id: GO:1990720
  path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
  label: C2 axonemal microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 97c8666ddef318d146a2d902a225f8b0313468bcf54fa32d81d5f1d127798a44
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/c2_axonemal_microtubule.yaml
    role: maintained_record
- target_id: GO:0000142
  path: data/structures/cytoskeleton/cellular_bud_neck_contractile_ring.yaml
  label: cellular bud neck contractile ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 98f13751880cb87993310078d3409a400df4ccbaad0f9499f9b76a2be4538280
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cellular_bud_neck_contractile_ring.yaml
    role: maintained_record
- target_id: GO:0032174
  path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
  label: cellular bud neck septin collar
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2901b13c5e8db9e171b7c1f93caf816991d0e58ba9456339c5db7f7f3716ae0e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cellular_bud_neck_septin_collar.yaml
    role: maintained_record
- target_id: GO:0000144
  path: data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml
  label: cellular bud neck septin ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6ef4f3536140aa328f20854cf2ef1db86b5508676f475e9a3282f932819546d1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cellular_bud_neck_septin_ring.yaml
    role: maintained_record
- target_id: GO:0032177
  path: data/structures/cytoskeleton/cellular_bud_neck_split_septin_rings.yaml
  label: cellular bud neck split septin rings
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c76ed8c617acf9966daa42ca587f49cc352795bc3e2b9fe702359075c49a9cff
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cellular_bud_neck_split_septin_rings.yaml
    role: maintained_record
- target_id: GO:0061493
  path: data/structures/cytoskeleton/central_plaque_of_mitotic_spindle_pole_body.yaml
  label: central plaque of mitotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7276a4205e01b2df88459ebd1d3dcd58ddf53677cd21be367e0d9e3667db70f5
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/central_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0005823
  path: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
  label: central plaque of spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b81ebcb1048c0454cde531ad51c3b0df92769b6c7236e07012ce9e3cef369527
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/central_plaque_of_spindle_pole_body.yaml
    role: maintained_record
- target_id: cellstructuremech:cetz_filament
  path: data/structures/cytoskeleton/cetz_filament.yaml
  label: CetZ filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 63215aac67bf4bbcdb4d43b73b27c0fef9420bca2eedda06d78cceacf63f253e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cetz_filament.yaml
    role: maintained_record
- target_id: GO:0032166
  path: data/structures/cytoskeleton/chlamydospore_septin_filament_array.yaml
  label: chlamydospore septin filament array
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 716764f6ed0bcbbb41f86d89e51272e96c0ac83ca56ef41c71dd5ff23f7a3481
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/chlamydospore_septin_filament_array.yaml
    role: maintained_record
- target_id: GO:0036064
  path: data/structures/cytoskeleton/ciliary_basal_body.yaml
  label: ciliary basal body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 46027bf3d3d8b3011803fa72d1229a892d34b7233d48ca290466b9afefb6b7ef
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_basal_body.yaml
    role: maintained_record
- target_id: GO:0120269
  path: data/structures/cytoskeleton/ciliary_centrin_arm.yaml
  label: ciliary centrin arm
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 459a2b5ece1620d7d617ef459cca0bd2a1020441201b80e83ecaa09c78299ec6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_centrin_arm.yaml
    role: maintained_record
- target_id: GO:1990900
  path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
  label: ciliary pocket collar
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: df0530c9582d0a40d8e0c646cdaa88cc0872d1e6e034cbdcd068b2a3f426ec3a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pocket_collar.yaml
    role: maintained_record
- target_id: GO:0120280
  path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
  label: ciliary pro-basal body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 87d2aa0682028aa4f14a6d76543eaeb475598817b8fa5fb9a29a639e8793d4e4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_pro_basal_body.yaml
    role: maintained_record
- target_id: GO:0035253
  path: data/structures/cytoskeleton/ciliary_rootlet.yaml
  label: ciliary rootlet
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a4ce875de28c94730588bfb1549dd6dc38b28658e3f3d66b8cb6fe66859433b3
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ciliary_rootlet.yaml
    role: maintained_record
- target_id: GO:0032161
  path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
  label: cleavage apparatus septin structure
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 07dd82a0f5ad6f6a473e9305c85bf0de6ca336f573878668664e2ee44dbc90e1
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cleavage_apparatus_septin_structure.yaml
    role: maintained_record
- target_id: GO:0020010
  path: data/structures/cytoskeleton/conoid.yaml
  label: conoid
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f45c77a22694ab07d2abdf0954141d0a99579150924d64e605387e067cf0a501
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/conoid.yaml
    role: maintained_record
- target_id: cellstructuremech:crescentin_filament
  path: data/structures/cytoskeleton/crescentin_filament.yaml
  label: crescentin filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8a7528bc96ddf0c0d8935ba4a308d49e7390262d09de979fe5138dbf1fcd2f0a
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained_record
- target_id: cellstructuremech:cryptophyte_cortical_centrin_network
  path: data/structures/cytoskeleton/cryptophyte_cortical_centrin_network.yaml
  label: cryptophyte cortical centrin network
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: cb0d5b64a7ea83ca03ae0ec91abad982f682314b29d0e89fe0f62cbaa2072819
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cryptophyte_cortical_centrin_network.yaml
    role: maintained_record
- target_id: GO:0097268
  path: data/structures/cytoskeleton/cytoophidium.yaml
  label: cytoophidium
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4e75070209f20d340a776a5ea708588484f39dc1f0a8859a0f0520ba2acda553
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cytoophidium.yaml
    role: maintained_record
- target_id: GO:0005881
  path: data/structures/cytoskeleton/cytoplasmic_microtubule.yaml
  label: cytoplasmic microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 23b89e56b6a009464465814315eaa0f663df8429a15f78dc62bcc79711b82005
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cytoplasmic_microtubule.yaml
    role: maintained_record
- target_id: cellstructuremech:cytostomal_cord
  path: data/structures/cytoskeleton/cytostomal_cord.yaml
  label: cytostomal cord
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 24269590b15ed4830dc083638b561e5b79f141d7d36b3b6199602a1a4ae633dd
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/cytostomal_cord.yaml
    role: maintained_record
- target_id: GO:0032123
  path: data/structures/cytoskeleton/deep_fiber.yaml
  label: deep fiber
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7868013c7bf3ce1c327c9106136b716f305afebe4efe5d49412e69278d26d702
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/deep_fiber.yaml
    role: maintained_record
- target_id: cellstructuremech:distal_connecting_fiber
  path: data/structures/cytoskeleton/distal_connecting_fiber.yaml
  label: distal connecting fiber
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3fbecc2d7d51c4e4ea53cdbc4d6e49251a300430f23fc0d76d00a3412a2a8d79
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/distal_connecting_fiber.yaml
    role: maintained_record
- target_id: GO:0036286
  path: data/structures/cytoskeleton/eisosome_filament.yaml
  label: eisosome filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: dba11b89f8cc8d874eae359238715f5fdb0d8a3da2ff551cc43b58b8aacd156b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/eisosome_filament.yaml
    role: maintained_record
- target_id: GO:0061645
  path: data/structures/cytoskeleton/endocytic_patch.yaml
  label: endocytic patch
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1712d71180fdc41b66ee9e20b120788b2db93b91e2f6638930ff08b2310c12bd
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/endocytic_patch.yaml
    role: maintained_record
- target_id: cellstructuremech:entodiniomorphid_subkinetal_myoneme_system
  path: data/structures/cytoskeleton/entodiniomorphid_subkinetal_myoneme_system.yaml
  label: Entodiniomorphid subkinetal myoneme system
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d2a4795123a8de62db9e270237cc7e5c1b3f2fb29655f4d3af6f158e6d0ebaeb
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/entodiniomorphid_subkinetal_myoneme_system.yaml
    role: maintained_record
- target_id: GO:0000923
  path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
  label: equatorial microtubule organizing center
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a8621a1fd05b6f1b997635eb62c3f743083f09c1b9e696fe0e0281ac384b9b7e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    role: maintained_record
- target_id: GO:0120119
  path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
  label: flagellum attachment zone
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1477cd38547a428f9625e08f7bf061c7a3f320b5710cfe736a7d722700221b8f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/flagellum_attachment_zone.yaml
    role: maintained_record
- target_id: cellstructuremech:funis
  path: data/structures/cytoskeleton/funis.yaml
  label: funis
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f4410ba245ffdd163c6cbff4adf7292cb348b39ff2952c7484091aaeed4aa9be
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/funis.yaml
    role: maintained_record
- target_id: GO:0000930
  path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
  label: gamma-tubulin complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c8f46fb3cb6d1a5a9c2ebdc657cc357bba4a05d8904b005c1836dadffe906182
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_complex.yaml
    role: maintained_record
- target_id: GO:0000931
  path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
  label: gamma-tubulin ring complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 411a47cbbdad6599e88f4328dc0d8e745a05a46c4815177adaf73e2c3e89f728
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_ring_complex.yaml
    role: maintained_record
- target_id: GO:0008275
  path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
  label: gamma-tubulin small complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4a9e3e657b2e17962527694dd078c1a74dbed1e83ffb32752675a25332754468
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gamma_tubulin_small_complex.yaml
    role: maintained_record
- target_id: GO:0032171
  path: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
  label: germ tube septin cap
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2b38e6f9051b64b36fe4bb52206122b35d060e5146d548622573303fe0378732
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/germ_tube_septin_cap.yaml
    role: maintained_record
- target_id: GO:0032172
  path: data/structures/cytoskeleton/germ_tube_septin_ring.yaml
  label: germ tube septin ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f1420625e020c7842cf281f96450b246edd350c32060c3d3186130d45ec012a0
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/germ_tube_septin_ring.yaml
    role: maintained_record
- target_id: GO:1990317
  path: data/structures/cytoskeleton/gin4_complex.yaml
  label: Gin4 complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 92702fe584fd086c30d5fee9fe8aaee5d8ec0e8938606710a09e6c2954428f43
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/gin4_complex.yaml
    role: maintained_record
- target_id: GO:0061496
  path: data/structures/cytoskeleton/half_bridge_of_mitotic_spindle_pole_body.yaml
  label: half bridge of mitotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 774a31a26d3323f1395c6db0de2a0f68cdeaa17d1d68b97900e364455c3b43d4
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/half_bridge_of_mitotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0005825
  path: data/structures/cytoskeleton/half_bridge_of_spindle_pole_body.yaml
  label: half bridge of spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c9420adeab4b1029037608be6b66ee738a0d5b6b1559fd7aa8742b256ce4f3bb
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/half_bridge_of_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0032117
  path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
  label: horsetail-astral microtubule array
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 73abc8f115d095e86ee315409c2221a5a97b37fad16effdb8593c6b9655568de
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/horsetail_astral_microtubule_array.yaml
    role: maintained_record
- target_id: GO:0062140
  path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
  label: hyphae septin collar
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9e143ed6218b251660020e57fd99c4758ea02e5ce91e6cf8de3133f626d08f26
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphae_septin_collar.yaml
    role: maintained_record
- target_id: GO:0032163
  path: data/structures/cytoskeleton/hyphal_septin_band.yaml
  label: hyphal septin band
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ca28b60ce59664d282f0379709392c10f211dbc1be34fc1bab90840285a429d7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphal_septin_band.yaml
    role: maintained_record
- target_id: GO:0032164
  path: data/structures/cytoskeleton/hyphal_septin_cap.yaml
  label: hyphal septin cap
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ca2f4c8585ae8b00261d85983033efe1b63fc690a5f316d4b0506200927a9d2f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphal_septin_cap.yaml
    role: maintained_record
- target_id: GO:0032168
  path: data/structures/cytoskeleton/hyphal_septin_ring.yaml
  label: hyphal septin ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9b8a399ed470a314cf73b6a4df6c4e14bf8d2cda618eb091f7c02f557c5252cf
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/hyphal_septin_ring.yaml
    role: maintained_record
- target_id: cellstructuremech:icl1e_complex
  path: data/structures/cytoskeleton/icl1e_complex.yaml
  label: ICL1e complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1c27b35fb37f183dd5aa251395e359541721525d3a76f76263664d0d09a379e0
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/icl1e_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:infraciliary_lattice
  path: data/structures/cytoskeleton/infraciliary_lattice.yaml
  label: infraciliary lattice
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 40b4b68e4354201ceabd0605deeafc8ce5a71c14e6457d075e5a6fe0d082cf9e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/infraciliary_lattice.yaml
    role: maintained_record
- target_id: GO:0036156
  path: data/structures/cytoskeleton/inner_dynein_arm.yaml
  label: inner dynein arm
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 30f955bace0501cfaac21cf19540023e78ddd2acddb1107a78412c6debdc7da3
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_dynein_arm.yaml
    role: maintained_record
- target_id: GO:0061497
  path: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
  label: inner plaque of mitotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c7d1f6c1fa0f5928a0d3bc67d245eb0d3e655798fc62e719990248707765aff8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0005822
  path: data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
  label: inner plaque of spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 663b2ccb7bf2a427807d0156bb33feb5c96ce978649f091ed5a9a2b4723a0dba
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/inner_plaque_of_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0061498
  path: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
  label: intermediate layer of mitotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6babc40661cf4080adb6b1c5e18c42a78c7b1cffddae612a3288fee4926c98e5
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intermediate_layer_of_mitotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0005821
  path: data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
  label: intermediate layer of spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3c889767d96b20dae86ccb3327892d5d33a5892591133cd4dcea4ad17a4b07c0
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intermediate_layer_of_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0031021
  path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
  label: interphase microtubule organizing center
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e16c54c5053f30b3da52fae3a7b2eeb0afb18d2580bff4e95d3b69071160b7ca
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
    role: maintained_record
- target_id: GO:0160066
  path: data/structures/cytoskeleton/interphase_sin_signaling_complex.yaml
  label: interphase SIN signaling complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b3a359eac1e3973709e48eea87d5b9b7ecdc16ad1372d573b15bcc88ad91ef40
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/interphase_sin_signaling_complex.yaml
    role: maintained_record
- target_id: GO:0033289
  path: data/structures/cytoskeleton/intraconoid_microtubule.yaml
  label: intraconoid microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6744611709c76a74cc30a2ca22fe118e1b87cc3aeabb5199df81a210b2fced41
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/intraconoid_microtubule.yaml
    role: maintained_record
- target_id: cellstructuremech:mamk_filament
  path: data/structures/cytoskeleton/mamk_filament.yaml
  label: MamK filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: fb273942dd11b99a71c61834f5ca331829a340b6a271e0f73e050c1b0128ca64
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mamk_filament.yaml
    role: maintained_record
- target_id: GO:1990819
  path: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
  label: mating projection actin fusion focus
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e0b5696c74beabb751e5334fd04492a057d4b3fceeedf87f7b1c59978e172b1e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_actin_fusion_focus.yaml
    role: maintained_record
- target_id: GO:0032162
  path: data/structures/cytoskeleton/mating_projection_septin_band.yaml
  label: mating projection septin band
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e68377ea65b5be456416810adb14479747220176a957b97f6d3ce3f5e731354d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_septin_band.yaml
    role: maintained_record
- target_id: GO:0032175
  path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
  label: mating projection septin ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1829e9907009f5d72966b7b14936288c5bb5d141ea0fb043058a6e1939a078b6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mating_projection_septin_ring.yaml
    role: maintained_record
- target_id: GO:0036391
  path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
  label: medial cortex septin ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9286b6cd14a1d4ee846f71768e3e2c167d3254af72efc0e9437738dd16caddb6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/medial_cortex_septin_ring.yaml
    role: maintained_record
- target_id: GO:0097568
  path: data/structures/cytoskeleton/median_body.yaml
  label: median body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d8acb0b396e2f02d12854bfcef95a7a2bc67b6be648058230971e38d1b7e757f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/median_body.yaml
    role: maintained_record
- target_id: GO:0110086
  path: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
  label: meiotic actomyosin contractile ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 482e30c182b04c65329ec8652cc472449ece53ac9c60657f1ae6bb6ceface019
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_actomyosin_contractile_ring.yaml
    role: maintained_record
- target_id: GO:0034993
  path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
  label: meiotic nuclear membrane microtubule tethering complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1edc92bdba11eec4c3da00ba06bd5cae3bd2593f5ba94be9d545c52a9da86049
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_nuclear_membrane_microtubule_tethering_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:meiotic_outer_plaque
  path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
  label: meiotic outer plaque
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5482b05be175efef27e7e2acd73c2a7fb6cddbd69ebe7c430ed0adc3f858bfe9
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_outer_plaque.yaml
    role: maintained_record
- target_id: GO:0032152
  path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
  label: meiotic septin complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4f10be6c6b32a3c71f43f28570d1eefac729c757657a1a28d29ff41f890aebe9
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_septin_complex.yaml
    role: maintained_record
- target_id: GO:0035974
  path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
  label: meiotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2a99651652ccaa1b26dd8149e44976824366dbe2157a708fb1df0560323b8a75
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/meiotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0005874
  path: data/structures/cytoskeleton/microtubule.yaml
  label: microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 06773fdcef54b61e7ed2a8a4c1066dfed8ba71dce8050eb39a879fab702b7498
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/microtubule.yaml
    role: maintained_record
- target_id: GO:0110085
  path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
  label: mitotic actomyosin contractile ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d74335a45d6c7037868c200e25a7fe12bc73121536cd32e68be983a3ebf6e9ac
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_actomyosin_contractile_ring.yaml
    role: maintained_record
- target_id: GO:0032151
  path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
  label: mitotic septin complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 99bf85740532379d8f9d88a2f07563cf9853a42e00a367fc5453d598ad308d1e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_septin_complex.yaml
    role: maintained_record
- target_id: GO:0072686
  path: data/structures/cytoskeleton/mitotic_spindle.yaml
  label: mitotic spindle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 85b2e3d0b8037dec88990c0d95901bd9005766e7d01067c5744c46894ec3d1a6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_spindle.yaml
    role: maintained_record
- target_id: GO:0044732
  path: data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
  label: mitotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6f26eef2c9a8c923eb0c851b4d65b90a696322095208e731be170b6b0c9f0329
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mitotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: cellstructuremech:mreb_filament
  path: data/structures/cytoskeleton/mreb_filament.yaml
  label: MreB filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b27d315ff07c11f2aa9eb1f1c1f4c65203ba62509fe6999c7804397e76ab9711
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
    role: maintained_record
- target_id: GO:0071958
  path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
  label: new mitotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 33ac955370a7476c7bb3f3fca4cfc9464120890e6a3e57fcb3b32d5e2504fb82
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/new_mitotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0160067
  path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
  label: new spindle pole body SIN signaling complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 84ade1d5217bae8fa401f096724d0892e76378469bec45c6ea25e961a0e28cae
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/new_spindle_pole_body_sin_signaling_complex.yaml
    role: maintained_record
- target_id: GO:0005880
  path: data/structures/cytoskeleton/nuclear_microtubule.yaml
  label: nuclear microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 09096977c74bdb36271d09b2a8aa1ac4c269ff8f3adbc854beae8b348f8aa252
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/nuclear_microtubule.yaml
    role: maintained_record
- target_id: cellstructuremech:nucleus_basal_body_connector
  path: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
  label: nucleus-basal body connector
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 89e5e96440535f65493ee4b2928b835f415f79358200f32d877ec59487300f0d
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/nucleus_basal_body_connector.yaml
    role: maintained_record
- target_id: GO:0071957
  path: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
  label: old mitotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 84c9dc88c397f90a6c90dc61031b9f5334baa65580eaecc16cc851cacc54840b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/old_mitotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0036157
  path: data/structures/cytoskeleton/outer_dynein_arm.yaml
  label: outer dynein arm
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: b394df130fce9a7cfd91a9d76a0c7be847e89f5bc471827f7836dbf988413fa8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_dynein_arm.yaml
    role: maintained_record
- target_id: GO:0061499
  path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
  label: outer plaque of mitotic spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9197bc8f9b1fed339d56314bb682274576fa41bb94b26e2d09823e14a26ec226
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_plaque_of_mitotic_spindle_pole_body.yaml
    role: maintained_record
- target_id: GO:0005824
  path: data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
  label: outer plaque of spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2aa7db5e2c632a9934dda8fbc3c57a85d1742c6aa7322e769f6f162103f17142
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/outer_plaque_of_spindle_pole_body.yaml
    role: maintained_record
- target_id: cellstructuremech:parm_filament
  path: data/structures/cytoskeleton/parm_filament.yaml
  label: ParM filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: d021bb88e2999e696f67403cff71a22b39801ad248f2c1aa86d8e9360a33024b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/parm_filament.yaml
    role: maintained_record
- target_id: cellstructuremech:peritrich_body_myoneme_system
  path: data/structures/cytoskeleton/peritrich_body_myoneme_system.yaml
  label: Peritrich body myoneme system
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 85563af4f17c846111f087a0c6bd31b6480a9b5fff05df9a3eff79e0b25418f9
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/peritrich_body_myoneme_system.yaml
    role: maintained_record
- target_id: cellstructuremech:phuz_spindle
  path: data/structures/cytoskeleton/phuz_spindle.yaml
  label: PhuZ spindle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 335a29b8efc518b066fdc5b44c9e6f4c777e2c1f5458f977a3b68595d9c13013
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained_record
- target_id: GO:0020031
  path: data/structures/cytoskeleton/polar_ring_of_apical_complex.yaml
  label: polar ring of apical complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ec70822af034fd9e33585bf8fa8894a6fd97cf8c2127fb6e29d91d842efd278b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/polar_ring_of_apical_complex.yaml
    role: maintained_record
- target_id: GO:1990295
  path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
  label: post-anaphase microtubule array
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: f8b698394b595d435b10633cac0cef969d32aae261b770d3ea60b974e5c4cd15
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/post_anaphase_microtubule_array.yaml
    role: maintained_record
- target_id: GO:0032157
  path: data/structures/cytoskeleton/prospore_contractile_ring.yaml
  label: prospore contractile ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 86ff161d77dbd6b182aab5d48cf4fa4376ad69ec739305c9b3c25c8aef103e51
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/prospore_contractile_ring.yaml
    role: maintained_record
- target_id: GO:0032165
  path: data/structures/cytoskeleton/prospore_septin_filament_array.yaml
  label: prospore septin filament array
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 39df294524bcae01b5a3c70410172ac4d19c6fb936a7bf970fda23a043220bfa
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/prospore_septin_filament_array.yaml
    role: maintained_record
- target_id: GO:0032169
  path: data/structures/cytoskeleton/prospore_septin_ring.yaml
  label: prospore septin ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 56b764eb06dde6d49e5ad5135ab577218f765b63791ffe0483147d4186498da5
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/prospore_septin_ring.yaml
    role: maintained_record
- target_id: GO:0032170
  path: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
  label: pseudohyphal septin ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 725c892c096cf75b48bb0a26a1aad5d657d9e5e716851f07211b161ba4d04533
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/pseudohyphal_septin_ring.yaml
    role: maintained_record
- target_id: cellstructuremech:quiescent_cell_microtubule_bundle
  path: data/structures/cytoskeleton/quiescent_cell_microtubule_bundle.yaml
  label: quiescent cell microtubule bundle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6228e65ead4750033cd105250a703ffce6dfba328d05e94de0d26ae06b100bc8
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/quiescent_cell_microtubule_bundle.yaml
    role: maintained_record
- target_id: cellstructuremech:quiescent_nuclear_microtubule_bundle
  path: data/structures/cytoskeleton/quiescent_nuclear_microtubule_bundle.yaml
  label: quiescent nuclear microtubule bundle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 87b29df8262cfbc32a1bae44f4777edb2ba44663fe0bee22733cc95bc78400ea
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/quiescent_nuclear_microtubule_bundle.yaml
    role: maintained_record
- target_id: cellstructuremech:radial_microtubule_organizing_center
  path: data/structures/cytoskeleton/radial_microtubule_organizing_center.yaml
  label: radial microtubule organizing center
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a6a2e4d87b3159afe989f1f838da6988395c5c2b0fc1b24bf1cde154f2dbc364
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_microtubule_organizing_center.yaml
    role: maintained_record
- target_id: GO:0001534
  path: data/structures/cytoskeleton/radial_spoke.yaml
  label: radial spoke
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: fdfeccafa1a5892150fe6a0da6971348e06ce6ca7123d69564ac70844f7f9993
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke.yaml
    role: maintained_record
- target_id: GO:0001535
  path: data/structures/cytoskeleton/radial_spoke_head.yaml
  label: radial spoke head
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: bec66030c7916b9cf537e93d924b97e92b7590e049547920896e39108b19adaa
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke_head.yaml
    role: maintained_record
- target_id: GO:0120343
  path: data/structures/cytoskeleton/radial_spoke_neck.yaml
  label: radial spoke neck
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 856f1fc78aecde5a603330227e494ac20ee930f25e04deca0ceb98d286c12418
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke_neck.yaml
    role: maintained_record
- target_id: GO:0001536
  path: data/structures/cytoskeleton/radial_spoke_stalk.yaml
  label: radial spoke stalk
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8747c08b214590fd435efacd64ee8fb09e56cf9e693fa193df256716c2703936
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke_stalk.yaml
    role: maintained_record
- target_id: GO:1990612
  path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
  label: Sad1-Kms1 LINC complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 2dc179231cae9404e022e417327a94b550b75c47872ef2e467330ea79d5cdf17
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sad1_kms1_linc_complex.yaml
    role: maintained_record
- target_id: GO:0032158
  path: data/structures/cytoskeleton/septin_band.yaml
  label: septin band
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 41d269f0b9bd3a3814d8fd2bb5e3e26e933763e1b06c42a30e8b13e20f2865da
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_band.yaml
    role: maintained_record
- target_id: GO:0032159
  path: data/structures/cytoskeleton/septin_cap.yaml
  label: septin cap
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 5dccebc18f9349148bd4ef1e64e29e42648d4df485e0f407c989be0d1b13f8ba
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cap.yaml
    role: maintained_record
- target_id: GO:0032173
  path: data/structures/cytoskeleton/septin_collar.yaml
  label: septin collar
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c16f869099afaf1a608e229fb19f217583156684f4a7311549af622691b556d9
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_collar.yaml
    role: maintained_record
- target_id: GO:0031105
  path: data/structures/cytoskeleton/septin_complex.yaml
  label: septin complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4de023faea51c1ea084592fda0f5db6a95ae91f1a8de69de44a208099fcd8373
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_complex.yaml
    role: maintained_record
- target_id: GO:0032156
  path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
  label: septin cytoskeleton
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a4ed43de8b89ae2f50cf586ff1b041a7865a7a717bb13c2f1885a50666627e9e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_cytoskeleton.yaml
    role: maintained_record
- target_id: GO:0032160
  path: data/structures/cytoskeleton/septin_filament_array.yaml
  label: septin filament array
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8413e81f4ac3c0daf46af8a81bbc0c819380242af370486f07865114e2edc1a0
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_filament_array.yaml
    role: maintained_record
- target_id: GO:0005940
  path: data/structures/cytoskeleton/septin_ring.yaml
  label: septin ring
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a29add3311f4b53bf4b50c2ec527d5ef450cfff625eadd312324d625b8790b93
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/septin_ring.yaml
    role: maintained_record
- target_id: GO:0160065
  path: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
  label: SIN/MEN signaling complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 59f188a29d48dab89d1c7a36aee3bd8f67efe3110c7c981bbac7b60df20d8f4b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sin_men_signaling_complex.yaml
    role: maintained_record
- target_id: GO:1990334
  path: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
  label: SIN/MEN two-component GAP complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 922665d09fdb8ddf24c904aefc3ccd0ec99a36f92d4d33f71a42c732036ecbdd
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sin_men_two_component_gap_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:sinister_fiber
  path: data/structures/cytoskeleton/sinister_fiber.yaml
  label: sinister fiber
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 9227477d7ba7b31e708bd60156ccb5d24f7051d3e0451b9138e6b3380d3664e5
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/sinister_fiber.yaml
    role: maintained_record
- target_id: GO:0005819
  path: data/structures/cytoskeleton/spindle.yaml
  label: spindle
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: da0b1e5a86542a84962f0f7ac3319c458a44941b0094d724488e8095e62d3e0e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle.yaml
    role: maintained_record
- target_id: GO:0005876
  path: data/structures/cytoskeleton/spindle_microtubule.yaml
  label: spindle microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: bd8d435d59b948878bdcc978f015029ba6f6cc236b43eab0a5a5fe8b1a350fb9
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_microtubule.yaml
    role: maintained_record
- target_id: GO:0051233
  path: data/structures/cytoskeleton/spindle_midzone.yaml
  label: spindle midzone
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7292732ff2a699422cc1b243dd2ad0651a568da206ed79f514aa6c19e2e59661
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_midzone.yaml
    role: maintained_record
- target_id: GO:0000922
  path: data/structures/cytoskeleton/spindle_pole.yaml
  label: spindle pole
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: c456f99ee99fc90e9b8fcf99e303abddf46bfa0c9c0f473ec3059ed8a0044204
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole.yaml
    role: maintained_record
- target_id: GO:0005816
  path: data/structures/cytoskeleton/spindle_pole_body.yaml
  label: spindle pole body
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 50885e021c246e17e29beb27f7dc98e37ee4d34878648fea4fd8b565bbb2fc78
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body.yaml
    role: maintained_record
- target_id: cellstructuremech:spindle_pole_body_duplication_plaque
  path: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
  label: spindle pole body duplication plaque
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: e321abc96c81de9d3b524b7a68e2cefc4f28aaf72df105b42c96e1c6b8e994c3
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body_duplication_plaque.yaml
    role: maintained_record
- target_id: cellstructuremech:spindle_pole_body_satellite
  path: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
  label: spindle pole body satellite
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a6a16f2dc3c09895fb7f4af93e1cad023c01b75dd424b99a1177ce93b516acb3
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spindle_pole_body_satellite.yaml
    role: maintained_record
- target_id: cellstructuremech:spirostomum_myoneme_fishnet
  path: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
  label: Spirostomum myoneme fishnet
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 23c2668330bc68a88153d7ed54feb0a5626a88d4ae53a8da6e250d2dda8d71af
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/spirostomum_myoneme_fishnet.yaml
    role: maintained_record
- target_id: GO:0032176
  path: data/structures/cytoskeleton/split_septin_rings.yaml
  label: split septin rings
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 580abb6f00c144e871e1fded7fbb2dca8584ecf0d47a599f646558642c3027ff
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/split_septin_rings.yaml
    role: maintained_record
- target_id: cellstructuremech:stalk_spasmoneme
  path: data/structures/cytoskeleton/stalk_spasmoneme.yaml
  label: Stalk spasmoneme
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: a3de4646f57551323b08c225176359cf3737eff71eaab9da598131d646920bdb
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stalk_spasmoneme.yaml
    role: maintained_record
- target_id: cellstructuremech:stentor_km_fiber
  path: data/structures/cytoskeleton/stentor_km_fiber.yaml
  label: Stentor Km fiber
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 66b91b45477653bcafdf1f875b9820681ea1bdeddf36f9d37f74fabe9408cae6
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_km_fiber.yaml
    role: maintained_record
- target_id: cellstructuremech:stentor_myoneme_system
  path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
  label: Stentor myoneme system
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8396ff930730d215b773b9b9f40d5b0a4444e3e2c6581cde72dbd47358570941
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_myoneme_system.yaml
    role: maintained_record
- target_id: cellstructuremech:stentor_perialgal_microtubule_meshwork
  path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
  label: Stentor perialgal microtubule meshwork
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 3a0c8634cf4fca1f7d9253d399b2f6d343d806cd6e3b81e5d92ebf6ff9ab7daf
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/stentor_perialgal_microtubule_meshwork.yaml
    role: maintained_record
- target_id: GO:0020025
  path: data/structures/cytoskeleton/subpellicular_microtubule.yaml
  label: subpellicular microtubule
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 8fb4caeb1617731d37c9ae70ea44bcea84be14499211b86922bade11cdd6af83
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/subpellicular_microtubule.yaml
    role: maintained_record
- target_id: GO:0070850
  path: data/structures/cytoskeleton/tacc_tog_complex.yaml
  label: TACC/TOG complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 7d2c57864f3928f8ab9bbc0d7e702aa142292ae00252b385f40a5a8dbcd7b787
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/tacc_tog_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:telocentrosome
  path: data/structures/cytoskeleton/telocentrosome.yaml
  label: telocentrosome
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 05d5a42ee4b63bd62b3e8c6c0137e2268964980fcc00f27769e29498cf67dca7
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/telocentrosome.yaml
    role: maintained_record
- target_id: cellstructuremech:transition_zone_stellate_fiber_system
  path: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
  label: transition zone stellate fiber system
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: ee5fc36bcda7810c550cfef29146f6b124f79703e6b73832b6f005583884ba36
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/transition_zone_stellate_fiber_system.yaml
    role: maintained_record
- target_id: GO:0120121
  path: data/structures/cytoskeleton/tripartite_attachment_complex.yaml
  label: tripartite attachment complex
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 4b20e1ac242cf6e988ee0ec52eefb537bdd7b1270c1c32c238183baa66c7dd52
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/tripartite_attachment_complex.yaml
    role: maintained_record
- target_id: cellstructuremech:tubulin_spool
  path: data/structures/cytoskeleton/tubulin_spool.yaml
  label: tubulin spool
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 1180c5c0b3a5c67f58a23b99913f7b78202beb8cf3e01c40ca5aac9c56dcf072
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/tubulin_spool.yaml
    role: maintained_record
- target_id: cellstructuremech:tubz_filament
  path: data/structures/cytoskeleton/tubz_filament.yaml
  label: TubZ filament
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 0399b1e1569592d6be671444cb03e37d481ca5022d52a476dd3a75f21337355e
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/tubz_filament.yaml
    role: maintained_record
- target_id: GO:0097597
  path: data/structures/cytoskeleton/ventral_disc.yaml
  label: ventral disc
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: da4539d720be1cfa7e1e1b5ca12d86f57ededaebc6a869bdd2fc4bf13fb5680b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc.yaml
    role: maintained_record
- target_id: GO:0097595
  path: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
  label: ventral disc crossbridge
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: bb35ddad7c8b15916d19fa6e5ad334ca3476221330372020fdf4adc8565db67b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_crossbridge.yaml
    role: maintained_record
- target_id: GO:0097594
  path: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
  label: ventral disc dorsal microribbon
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6bcdbfaaf84c4b6152147340dcbb6f5958d6dc6aca2288e034c3f2c357819425
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_dorsal_microribbon.yaml
    role: maintained_record
- target_id: GO:0097591
  path: data/structures/cytoskeleton/ventral_disc_lateral_crest.yaml
  label: ventral disc lateral crest
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 6a8127a748d9dcdb2e429d05d817626c02ffed35eb545eb501c0b101758db32b
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_lateral_crest.yaml
    role: maintained_record
- target_id: GO:0097593
  path: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
  label: ventral disc microtubule array
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 184540d5a0f41b8f04fa8e4cac937dc657481eaa999e5420ec315476801a07e3
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_microtubule_array.yaml
    role: maintained_record
- target_id: GO:0097592
  path: data/structures/cytoskeleton/ventral_disc_overlap_zone.yaml
  label: ventral disc overlap zone
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 983f27caa2fde019c9ab576e64c54bd354b6528a65e0f9ef9cdfbb87abb365ce
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_overlap_zone.yaml
    role: maintained_record
- target_id: GO:0097596
  path: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
  label: ventral disc supernumerary microtubule array
  record_class: CellStructureRecord
  kind: maintained
  semantic_digest:
    algorithm: file_sha256_v1
    sha256: 54772643689f75f239cddf783180ab3eb0443695ea60080d966cbeb2fb0efe1f
    description: Exact UTF-8 YAML bytes of the maintained CellStructureRecord.
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/ventral_disc_supernumerary_microtubule_array.yaml
    role: maintained_record
checks:
- check_id: strict_cytoskeleton
  name: Strict corpus validation covering cytoskeleton cohort
  status: passed
  required: true
  summary: All 173 cytoskeleton records pass strict LinkML and semantic validation.
  target_ids:
  - GO:0097649
  - GO:0099079
  - GO:0030479
  - GO:0005826
  - cellstructuremech:alfa_filament
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0160111
  - GO:0160112
  - GO:1990716
  - GO:1990717
  - GO:0097540
  - GO:1990718
  - GO:0097545
  - GO:0005858
  - GO:0005879
  - GO:0160113
  - GO:0160110
  - GO:0160114
  - GO:0160115
  - GO:0005931
  - GO:0005930
  - GO:0097650
  - cellstructuremech:bactofilin_filament
  - cellstructuremech:basal_body_a_b_inner_junction
  - cellstructuremech:basal_body_a_c_linker
  - cellstructuremech:basal_body_a_tusk
  - cellstructuremech:basal_body_b_c_inner_junction
  - cellstructuremech:basal_body_c_tubule_hook
  - cellstructuremech:basal_body_c_tubule_luminal_filament
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:basal_body_cartwheel_inner_density
  - cellstructuremech:basal_body_d2_rod
  - cellstructuremech:basal_body_filamentous_cartwheel_inner_density
  - cellstructuremech:basal_body_inner_scaffold
  - cellstructuremech:basal_body_pinhead
  - cellstructuremech:basal_body_triplet_base
  - GO:0020032
  - GO:0120120
  - cellstructuremech:btubab_bacterial_microtubule
  - GO:1990719
  - GO:1990720
  - GO:0000142
  - GO:0032174
  - GO:0000144
  - GO:0032177
  - GO:0061493
  - GO:0005823
  - cellstructuremech:cetz_filament
  - GO:0032166
  - GO:0036064
  - GO:0120269
  - GO:1990900
  - GO:0120280
  - GO:0035253
  - GO:0032161
  - GO:0020010
  - cellstructuremech:crescentin_filament
  - cellstructuremech:cryptophyte_cortical_centrin_network
  - GO:0097268
  - GO:0005881
  - cellstructuremech:cytostomal_cord
  - GO:0032123
  - cellstructuremech:distal_connecting_fiber
  - GO:0036286
  - GO:0061645
  - cellstructuremech:entodiniomorphid_subkinetal_myoneme_system
  - GO:0000923
  - GO:0120119
  - cellstructuremech:funis
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0032171
  - GO:0032172
  - GO:1990317
  - GO:0061496
  - GO:0005825
  - GO:0032117
  - GO:0062140
  - GO:0032163
  - GO:0032164
  - GO:0032168
  - cellstructuremech:icl1e_complex
  - cellstructuremech:infraciliary_lattice
  - GO:0036156
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:0160066
  - GO:0033289
  - cellstructuremech:mamk_filament
  - GO:1990819
  - GO:0032162
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0110086
  - GO:0034993
  - cellstructuremech:meiotic_outer_plaque
  - GO:0032152
  - GO:0035974
  - GO:0005874
  - GO:0110085
  - GO:0032151
  - GO:0072686
  - GO:0044732
  - cellstructuremech:mreb_filament
  - GO:0071958
  - GO:0160067
  - GO:0005880
  - cellstructuremech:nucleus_basal_body_connector
  - GO:0071957
  - GO:0036157
  - GO:0061499
  - GO:0005824
  - cellstructuremech:parm_filament
  - cellstructuremech:peritrich_body_myoneme_system
  - cellstructuremech:phuz_spindle
  - GO:0020031
  - GO:1990295
  - GO:0032157
  - GO:0032165
  - GO:0032169
  - GO:0032170
  - cellstructuremech:quiescent_cell_microtubule_bundle
  - cellstructuremech:quiescent_nuclear_microtubule_bundle
  - cellstructuremech:radial_microtubule_organizing_center
  - GO:0001534
  - GO:0001535
  - GO:0120343
  - GO:0001536
  - GO:1990612
  - GO:0032158
  - GO:0032159
  - GO:0032173
  - GO:0031105
  - GO:0032156
  - GO:0032160
  - GO:0005940
  - GO:0160065
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005819
  - GO:0005876
  - GO:0051233
  - GO:0000922
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_myoneme_system
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0020025
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - GO:0120121
  - cellstructuremech:tubulin_spool
  - cellstructuremech:tubz_filament
  - GO:0097597
  - GO:0097595
  - GO:0097594
  - GO:0097591
  - GO:0097593
  - GO:0097592
  - GO:0097596
  command: .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_strict_cyto
- check_id: labels_cytoskeleton
  name: ID-label correspondence across cytoskeleton cohort
  status: passed
  required: true
  summary: All ontology ID-label pairs in cytoskeleton records correspond to canonical
    labels.
  target_ids:
  - GO:0097649
  - GO:0099079
  - GO:0030479
  - GO:0005826
  - cellstructuremech:alfa_filament
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0160111
  - GO:0160112
  - GO:1990716
  - GO:1990717
  - GO:0097540
  - GO:1990718
  - GO:0097545
  - GO:0005858
  - GO:0005879
  - GO:0160113
  - GO:0160110
  - GO:0160114
  - GO:0160115
  - GO:0005931
  - GO:0005930
  - GO:0097650
  - cellstructuremech:bactofilin_filament
  - cellstructuremech:basal_body_a_b_inner_junction
  - cellstructuremech:basal_body_a_c_linker
  - cellstructuremech:basal_body_a_tusk
  - cellstructuremech:basal_body_b_c_inner_junction
  - cellstructuremech:basal_body_c_tubule_hook
  - cellstructuremech:basal_body_c_tubule_luminal_filament
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:basal_body_cartwheel_inner_density
  - cellstructuremech:basal_body_d2_rod
  - cellstructuremech:basal_body_filamentous_cartwheel_inner_density
  - cellstructuremech:basal_body_inner_scaffold
  - cellstructuremech:basal_body_pinhead
  - cellstructuremech:basal_body_triplet_base
  - GO:0020032
  - GO:0120120
  - cellstructuremech:btubab_bacterial_microtubule
  - GO:1990719
  - GO:1990720
  - GO:0000142
  - GO:0032174
  - GO:0000144
  - GO:0032177
  - GO:0061493
  - GO:0005823
  - cellstructuremech:cetz_filament
  - GO:0032166
  - GO:0036064
  - GO:0120269
  - GO:1990900
  - GO:0120280
  - GO:0035253
  - GO:0032161
  - GO:0020010
  - cellstructuremech:crescentin_filament
  - cellstructuremech:cryptophyte_cortical_centrin_network
  - GO:0097268
  - GO:0005881
  - cellstructuremech:cytostomal_cord
  - GO:0032123
  - cellstructuremech:distal_connecting_fiber
  - GO:0036286
  - GO:0061645
  - cellstructuremech:entodiniomorphid_subkinetal_myoneme_system
  - GO:0000923
  - GO:0120119
  - cellstructuremech:funis
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0032171
  - GO:0032172
  - GO:1990317
  - GO:0061496
  - GO:0005825
  - GO:0032117
  - GO:0062140
  - GO:0032163
  - GO:0032164
  - GO:0032168
  - cellstructuremech:icl1e_complex
  - cellstructuremech:infraciliary_lattice
  - GO:0036156
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:0160066
  - GO:0033289
  - cellstructuremech:mamk_filament
  - GO:1990819
  - GO:0032162
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0110086
  - GO:0034993
  - cellstructuremech:meiotic_outer_plaque
  - GO:0032152
  - GO:0035974
  - GO:0005874
  - GO:0110085
  - GO:0032151
  - GO:0072686
  - GO:0044732
  - cellstructuremech:mreb_filament
  - GO:0071958
  - GO:0160067
  - GO:0005880
  - cellstructuremech:nucleus_basal_body_connector
  - GO:0071957
  - GO:0036157
  - GO:0061499
  - GO:0005824
  - cellstructuremech:parm_filament
  - cellstructuremech:peritrich_body_myoneme_system
  - cellstructuremech:phuz_spindle
  - GO:0020031
  - GO:1990295
  - GO:0032157
  - GO:0032165
  - GO:0032169
  - GO:0032170
  - cellstructuremech:quiescent_cell_microtubule_bundle
  - cellstructuremech:quiescent_nuclear_microtubule_bundle
  - cellstructuremech:radial_microtubule_organizing_center
  - GO:0001534
  - GO:0001535
  - GO:0120343
  - GO:0001536
  - GO:1990612
  - GO:0032158
  - GO:0032159
  - GO:0032173
  - GO:0031105
  - GO:0032156
  - GO:0032160
  - GO:0005940
  - GO:0160065
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005819
  - GO:0005876
  - GO:0051233
  - GO:0000922
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_myoneme_system
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0020025
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - GO:0120121
  - cellstructuremech:tubulin_spool
  - cellstructuremech:tubz_filament
  - GO:0097597
  - GO:0097595
  - GO:0097594
  - GO:0097591
  - GO:0097593
  - GO:0097592
  - GO:0097596
  command: .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
  exit_code: 0
  expected_exit_code: 0
  evidence_ids:
  - ev_labels_cyto
evidence:
- evidence_id: ev_strict_cyto
  kind: validation
  reference: scripts/validate_strict.py
  locator: strict receipt
  accessed_at: '2026-10-23T09:16:01Z'
  support: supports
  summary: validate_strict.py exited 0 across all 978 records including all 173 cytoskeleton
    records.
  snapshot_sha256: b34bdc4f99ef4601161958120b45622535017214ba594a44bca249237869d704
- evidence_id: ev_labels_cyto
  kind: validation
  reference: scripts/validate_id_label_correspondence.py
  locator: labels receipt
  accessed_at: '2026-10-23T09:17:48Z'
  support: supports
  summary: validate_id_label_correspondence.py exited 0 across all ontology targets.
  snapshot_sha256: b5cc67214f5627a654e75cfc335d77d42113d057091884a12094aa1a71447a5e
- evidence_id: ev_cyto_subcomplex_nodes
  kind: record_content
  reference: data/structures/cytoskeleton/actin_cortical_patch.yaml
  locator: actin_cortical_patch.yaml (arp2_3_complex), equatorial/interphase_microtubule_organizing_center.yaml
    & telocentrosome.yaml (gamma_tuc), radial_spoke.yaml (radial_spoke_head/neck/stalk)
  accessed_at: '2026-10-23T09:14:20Z'
  support: supports
  summary: 'Seven causal_graphs nodes across 5 cytoskeleton records reference GO-grounded
    PROTEIN_COMPLEX components (GO:0005885, GO:0000930, GO:0001535, GO:0120343, GO:0001536)
    but carry node_type: GENE_OR_PROTEIN without grounding instead of node_type: STRUCTURE.'
  quote: "- node_id: arp2_3_complex\n    label: Arp2/3 protein complex\n    node_type:\
    \ GENE_OR_PROTEIN\n    component_ref: arp2_3_complex"
  snapshot_sha256: 4b005ca985e36cdca47ff20271c2b31cc00b47a080e1da614265469d6adaaf8a
- evidence_id: ev_cyto_discussion_issues
  kind: record_content
  reference: data/structures/cytoskeleton/crescentin_filament.yaml
  locator: 'crescentin_filament.yaml discussions[1] (#1260), mreb_filament.yaml discussions[0]
    (#119), phuz_spindle.yaml discussions[0..1] (#481, #482)'
  accessed_at: '2026-10-23T09:14:20Z'
  support: supports
  summary: 'Four discussions entries across crescentin_filament.yaml, mreb_filament.yaml,
    and phuz_spindle.yaml mention repository issues (#1260, #119, #481, #482) in prose
    without structured GitHub issue URLs in their evidence lists.'
  quote: 'prompt: Resolve exact crescentin filament dimensions and sub-filament architecture
    (#1260).'
  snapshot_sha256: 8a7528bc96ddf0c0d8935ba4a308d49e7390262d09de979fe5138dbf1fcd2f0a
assessments:
- assessment_id: assess_cyto_cohort
  area: identity
  topic: Boundary discipline, identity, composition, and evidence across all 173 cytoskeleton
    records
  outcome: supported
  summary: All 173 cytoskeleton records have distinct GO/CSM identities, valid ontology
    label correspondence, and clear boundaries between polymers, organizing centers,
    and subcomplexes.
  target_ids:
  - GO:0097649
  - GO:0099079
  - GO:0030479
  - GO:0005826
  - cellstructuremech:alfa_filament
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0160111
  - GO:0160112
  - GO:1990716
  - GO:1990717
  - GO:0097540
  - GO:1990718
  - GO:0097545
  - GO:0005858
  - GO:0005879
  - GO:0160113
  - GO:0160110
  - GO:0160114
  - GO:0160115
  - GO:0005931
  - GO:0005930
  - GO:0097650
  - cellstructuremech:bactofilin_filament
  - cellstructuremech:basal_body_a_b_inner_junction
  - cellstructuremech:basal_body_a_c_linker
  - cellstructuremech:basal_body_a_tusk
  - cellstructuremech:basal_body_b_c_inner_junction
  - cellstructuremech:basal_body_c_tubule_hook
  - cellstructuremech:basal_body_c_tubule_luminal_filament
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:basal_body_cartwheel_inner_density
  - cellstructuremech:basal_body_d2_rod
  - cellstructuremech:basal_body_filamentous_cartwheel_inner_density
  - cellstructuremech:basal_body_inner_scaffold
  - cellstructuremech:basal_body_pinhead
  - cellstructuremech:basal_body_triplet_base
  - GO:0020032
  - GO:0120120
  - cellstructuremech:btubab_bacterial_microtubule
  - GO:1990719
  - GO:1990720
  - GO:0000142
  - GO:0032174
  - GO:0000144
  - GO:0032177
  - GO:0061493
  - GO:0005823
  - cellstructuremech:cetz_filament
  - GO:0032166
  - GO:0036064
  - GO:0120269
  - GO:1990900
  - GO:0120280
  - GO:0035253
  - GO:0032161
  - GO:0020010
  - cellstructuremech:crescentin_filament
  - cellstructuremech:cryptophyte_cortical_centrin_network
  - GO:0097268
  - GO:0005881
  - cellstructuremech:cytostomal_cord
  - GO:0032123
  - cellstructuremech:distal_connecting_fiber
  - GO:0036286
  - GO:0061645
  - cellstructuremech:entodiniomorphid_subkinetal_myoneme_system
  - GO:0000923
  - GO:0120119
  - cellstructuremech:funis
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0032171
  - GO:0032172
  - GO:1990317
  - GO:0061496
  - GO:0005825
  - GO:0032117
  - GO:0062140
  - GO:0032163
  - GO:0032164
  - GO:0032168
  - cellstructuremech:icl1e_complex
  - cellstructuremech:infraciliary_lattice
  - GO:0036156
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:0160066
  - GO:0033289
  - cellstructuremech:mamk_filament
  - GO:1990819
  - GO:0032162
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0110086
  - GO:0034993
  - cellstructuremech:meiotic_outer_plaque
  - GO:0032152
  - GO:0035974
  - GO:0005874
  - GO:0110085
  - GO:0032151
  - GO:0072686
  - GO:0044732
  - cellstructuremech:mreb_filament
  - GO:0071958
  - GO:0160067
  - GO:0005880
  - cellstructuremech:nucleus_basal_body_connector
  - GO:0071957
  - GO:0036157
  - GO:0061499
  - GO:0005824
  - cellstructuremech:parm_filament
  - cellstructuremech:peritrich_body_myoneme_system
  - cellstructuremech:phuz_spindle
  - GO:0020031
  - GO:1990295
  - GO:0032157
  - GO:0032165
  - GO:0032169
  - GO:0032170
  - cellstructuremech:quiescent_cell_microtubule_bundle
  - cellstructuremech:quiescent_nuclear_microtubule_bundle
  - cellstructuremech:radial_microtubule_organizing_center
  - GO:0001534
  - GO:0001535
  - GO:0120343
  - GO:0001536
  - GO:1990612
  - GO:0032158
  - GO:0032159
  - GO:0032173
  - GO:0031105
  - GO:0032156
  - GO:0032160
  - GO:0005940
  - GO:0160065
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005819
  - GO:0005876
  - GO:0051233
  - GO:0000922
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_myoneme_system
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0020025
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - GO:0120121
  - cellstructuremech:tubulin_spool
  - cellstructuremech:tubz_filament
  - GO:0097597
  - GO:0097595
  - GO:0097594
  - GO:0097591
  - GO:0097593
  - GO:0097592
  - GO:0097596
  evidence_ids:
  - ev_strict_cyto
  - ev_labels_cyto
- assessment_id: assess_cyto_subcomplex_nodes
  area: graph
  topic: Causal-graph node typing for GO-grounded PROTEIN_COMPLEX subcomplex components
  outcome: concern
  summary: 'Seven causal-graph nodes across 5 cytoskeleton records reference GO-grounded
    multiprotein subcomplex components using node_type: GENE_OR_PROTEIN without grounding
    instead of node_type: STRUCTURE.'
  target_ids:
  - GO:0030479
  - GO:0000923
  - GO:0031021
  - GO:0001534
  - cellstructuremech:telocentrosome
  evidence_ids:
  - ev_cyto_subcomplex_nodes
- assessment_id: assess_cyto_discussion_issues
  area: evidence
  topic: 'Structured GitHub issue URLs for #NNN mentions in discussions prose'
  outcome: concern
  summary: 'Three cytoskeleton records mention repository issues (#1260, #119, #481,
    #482) in discussions prose without corresponding GitHub issue URLs in evidence.'
  target_ids:
  - cellstructuremech:crescentin_filament
  - cellstructuremech:mreb_filament
  - cellstructuremech:phuz_spindle
  evidence_ids:
  - ev_cyto_discussion_issues
findings:
- finding_id: F1
  issue_key: cytoskeleton-go-subcomplex-causal-node-types
  category: graph
  severity: minor
  status: open
  certainty: confirmed
  title: Seven causal-graph nodes across 5 cytoskeleton records type GO-grounded PROTEIN_COMPLEX
    subcomplexes as GENE_OR_PROTEIN without grounding
  description: Across 5 records in data/structures/cytoskeleton/ — actin_cortical_patch.yaml
    (node arp2_3_complex -> GO:0005885), equatorial_microtubule_organizing_center.yaml
    (node gamma_tuc -> GO:0000930), interphase_microtubule_organizing_center.yaml
    (node gamma_tuc -> GO:0000930), radial_spoke.yaml (nodes radial_spoke_head ->
    GO:0001535, radial_spoke_neck -> GO:0120343, radial_spoke_stalk -> GO:0001536),
    and telocentrosome.yaml (node gamma_tuc -> GO:0000930) — causal-graph nodes referencing
    GO-grounded PROTEIN_COMPLEX components are typed GENE_OR_PROTEIN without grounding
    instead of STRUCTURE with their GO cellular-component grounding.
  target_ids:
  - GO:0030479
  - GO:0000923
  - GO:0031021
  - GO:0001534
  - cellstructuremech:telocentrosome
  field_paths:
  - causal_graphs[*].nodes[*]
  evidence_ids:
  - ev_cyto_subcomplex_nodes
  rule_id: docs/SCHEMA.md:CausalNode-node_type
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/actin_cortical_patch.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/telocentrosome.yaml
    role: maintained_record
  tags:
  - causal-graphs
  - node-type
  - stage4-record-review
- finding_id: F2
  issue_key: cytoskeleton-discussion-prose-issue-links
  category: evidence
  severity: minor
  status: open
  certainty: confirmed
  title: 'Three cytoskeleton records cite repository issues (#1260, #119, #481, #482)
    in discussions prose without structured evidence links'
  description: 'In crescentin_filament.yaml (discussions[1] resolve_filament_architecture_and_dimensions,
    citing #1260), mreb_filament.yaml (discussions[0] resolve_filament_width_and_protofilament_number,
    citing #119), and phuz_spindle.yaml (discussions[0] dynamic_instability_parameters_unsourced
    citing #481 and discussions[1] spindle_centering_mechanism_details citing #482),
    discussions prose cites #NNN issue numbers without structured GitHub issue URLs
    in that discussion''s evidence list.'
  target_ids:
  - cellstructuremech:crescentin_filament
  - cellstructuremech:mreb_filament
  - cellstructuremech:phuz_spindle
  field_paths:
  - discussions[*].evidence
  evidence_ids:
  - ev_cyto_discussion_issues
  rule_id: docs/CURATION.md:issue-links-in-evidence
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained_record
  tags:
  - discussions
  - evidence
  - stage4-record-review
actions:
- action_id: A1
  description: 'Update the 7 subcomplex causal-graph nodes across actin_cortical_patch.yaml,
    equatorial_microtubule_organizing_center.yaml, interphase_microtubule_organizing_center.yaml,
    radial_spoke.yaml, and telocentrosome.yaml to node_type: STRUCTURE with their
    canonical GO labels and groundings.'
  finding_ids:
  - F1
  target_ids:
  - GO:0030479
  - GO:0000923
  - GO:0031021
  - GO:0001534
  - cellstructuremech:telocentrosome
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/actin_cortical_patch.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/equatorial_microtubule_organizing_center.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/interphase_microtubule_organizing_center.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/radial_spoke.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/telocentrosome.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml
- action_id: A2
  description: 'Add structured GitHub issue URLs (and cited source references) to
    the discussions[].evidence lists in crescentin_filament.yaml (#1260), mreb_filament.yaml
    (#119), and phuz_spindle.yaml (#481, #482).'
  finding_ids:
  - F2
  target_ids:
  - cellstructuremech:crescentin_filament
  - cellstructuremech:mreb_filament
  - cellstructuremech:phuz_spindle
  owner_paths:
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/crescentin_filament.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/mreb_filament.yaml
    role: maintained_record
  - repository: CultureBotAI/CellStructureMech
    path: data/structures/cytoskeleton/phuz_spindle.yaml
    role: maintained_record
  acceptance_checks:
  - .venv/bin/python scripts/validate_strict.py --out /tmp/instance_validation_failures.tsv
  - .venv/bin/python scripts/validate_history.py
boundary_decisions:
- action: retain
  target_ids:
  - GO:0097649
  - GO:0099079
  - GO:0030479
  - GO:0005826
  - cellstructuremech:alfa_filament
  - GO:0005885
  - GO:0005818
  - GO:0000235
  - GO:0160111
  - GO:0160112
  - GO:1990716
  - GO:1990717
  - GO:0097540
  - GO:1990718
  - GO:0097545
  - GO:0005858
  - GO:0005879
  - GO:0160113
  - GO:0160110
  - GO:0160114
  - GO:0160115
  - GO:0005931
  - GO:0005930
  - GO:0097650
  - cellstructuremech:bactofilin_filament
  - cellstructuremech:basal_body_a_b_inner_junction
  - cellstructuremech:basal_body_a_c_linker
  - cellstructuremech:basal_body_a_tusk
  - cellstructuremech:basal_body_b_c_inner_junction
  - cellstructuremech:basal_body_c_tubule_hook
  - cellstructuremech:basal_body_c_tubule_luminal_filament
  - cellstructuremech:basal_body_cartwheel
  - cellstructuremech:basal_body_cartwheel_inner_density
  - cellstructuremech:basal_body_d2_rod
  - cellstructuremech:basal_body_filamentous_cartwheel_inner_density
  - cellstructuremech:basal_body_inner_scaffold
  - cellstructuremech:basal_body_pinhead
  - cellstructuremech:basal_body_triplet_base
  - GO:0020032
  - GO:0120120
  - cellstructuremech:btubab_bacterial_microtubule
  - GO:1990719
  - GO:1990720
  - GO:0000142
  - GO:0032174
  - GO:0000144
  - GO:0032177
  - GO:0061493
  - GO:0005823
  - cellstructuremech:cetz_filament
  - GO:0032166
  - GO:0036064
  - GO:0120269
  - GO:1990900
  - GO:0120280
  - GO:0035253
  - GO:0032161
  - GO:0020010
  - cellstructuremech:crescentin_filament
  - cellstructuremech:cryptophyte_cortical_centrin_network
  - GO:0097268
  - GO:0005881
  - cellstructuremech:cytostomal_cord
  - GO:0032123
  - cellstructuremech:distal_connecting_fiber
  - GO:0036286
  - GO:0061645
  - cellstructuremech:entodiniomorphid_subkinetal_myoneme_system
  - GO:0000923
  - GO:0120119
  - cellstructuremech:funis
  - GO:0000930
  - GO:0000931
  - GO:0008275
  - GO:0032171
  - GO:0032172
  - GO:1990317
  - GO:0061496
  - GO:0005825
  - GO:0032117
  - GO:0062140
  - GO:0032163
  - GO:0032164
  - GO:0032168
  - cellstructuremech:icl1e_complex
  - cellstructuremech:infraciliary_lattice
  - GO:0036156
  - GO:0061497
  - GO:0005822
  - GO:0061498
  - GO:0005821
  - GO:0031021
  - GO:0160066
  - GO:0033289
  - cellstructuremech:mamk_filament
  - GO:1990819
  - GO:0032162
  - GO:0032175
  - GO:0036391
  - GO:0097568
  - GO:0110086
  - GO:0034993
  - cellstructuremech:meiotic_outer_plaque
  - GO:0032152
  - GO:0035974
  - GO:0005874
  - GO:0110085
  - GO:0032151
  - GO:0072686
  - GO:0044732
  - cellstructuremech:mreb_filament
  - GO:0071958
  - GO:0160067
  - GO:0005880
  - cellstructuremech:nucleus_basal_body_connector
  - GO:0071957
  - GO:0036157
  - GO:0061499
  - GO:0005824
  - cellstructuremech:parm_filament
  - cellstructuremech:peritrich_body_myoneme_system
  - cellstructuremech:phuz_spindle
  - GO:0020031
  - GO:1990295
  - GO:0032157
  - GO:0032165
  - GO:0032169
  - GO:0032170
  - cellstructuremech:quiescent_cell_microtubule_bundle
  - cellstructuremech:quiescent_nuclear_microtubule_bundle
  - cellstructuremech:radial_microtubule_organizing_center
  - GO:0001534
  - GO:0001535
  - GO:0120343
  - GO:0001536
  - GO:1990612
  - GO:0032158
  - GO:0032159
  - GO:0032173
  - GO:0031105
  - GO:0032156
  - GO:0032160
  - GO:0005940
  - GO:0160065
  - GO:1990334
  - cellstructuremech:sinister_fiber
  - GO:0005819
  - GO:0005876
  - GO:0051233
  - GO:0000922
  - GO:0005816
  - cellstructuremech:spindle_pole_body_duplication_plaque
  - cellstructuremech:spindle_pole_body_satellite
  - cellstructuremech:spirostomum_myoneme_fishnet
  - GO:0032176
  - cellstructuremech:stalk_spasmoneme
  - cellstructuremech:stentor_km_fiber
  - cellstructuremech:stentor_myoneme_system
  - cellstructuremech:stentor_perialgal_microtubule_meshwork
  - GO:0020025
  - GO:0070850
  - cellstructuremech:telocentrosome
  - cellstructuremech:transition_zone_stellate_fiber_system
  - GO:0120121
  - cellstructuremech:tubulin_spool
  - cellstructuremech:tubz_filament
  - GO:0097597
  - GO:0097595
  - GO:0097594
  - GO:0097591
  - GO:0097593
  - GO:0097592
  - GO:0097596
  rationale: All 173 records in data/structures/cytoskeleton/ represent distinct cytoskeletal
    filaments, MTOCs, septin assemblies, eisosome/MCC complexes, or motor/adaptor
    subcomplexes.
  evidence_ids:
  - ev_strict_cyto
  - ev_labels_cyto
limitations:
- Two minor cohort findings across 8 cytoskeleton records are queued for Stage 5 remediation.
tags:
- stage4
- category-review
- cytoskeleton
```
