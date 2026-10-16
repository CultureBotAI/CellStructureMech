"""Keep the scientific boundaries restored by the October record-review follow-up."""

from pathlib import Path

import pytest
import yaml

ROOT = Path(__file__).resolve().parents[1]


def record(category, slug):
    return yaml.safe_load((ROOT / 'data/structures' / category / f'{slug}.yaml').read_text())


def keyed(items, key):
    return {item[key]: item for item in items}


@pytest.mark.parametrize('slug', ['light_harvesting_complex', 'phycobilisome'])
def test_pcc6803_photoprotection_cites_the_state_resolved_study(slug):
    doc = record('energy_complex', slug)
    example = keyed(doc['canonical_examples'], 'taxon_id')['NCBITaxon:1148']
    assert example['reference'] == 'DOI:10.1038/s41586-022-05156-4'
    evidence = keyed(doc['evidence'], 'reference')
    assert 'Zheng et al. 2021' in evidence['DOI:10.1038/s41467-021-25813-y']['notes']


def test_coreless_antennas_do_not_inherit_a_universal_core_requirement():
    doc = record('energy_complex', 'phycobilisome')
    assert 'coreless' in doc['definition']
    core = next(c for c in doc['components'] if 'apcA' in c.get('gene_symbols', []))
    assert core['essentiality'] == 'CONDITIONAL'
    assert 'coreless' in core['role']
    assert 'conventional' in doc['causal_graphs'][0]['scope_notes']


def test_nitrogenase_variants_and_reductase_oligomer_remain_distinct():
    doc = record('energy_complex', 'nitrogenase_complex')
    assert 'tetramer' not in doc['definition']
    components = keyed(doc['components'], 'component_id')
    assert 'additional G subunits' in components['dinitrogenase']['role']
    reductase = components['nitrogenase_reductase']
    assert reductase['grounding_status'] == 'REVIEWED_LABEL_ONLY'
    assert 'not Mo-exclusive' in reductase['grounding_notes']
    assert 'homodimer' in reductase['grounding_notes']


def test_psi_examples_do_not_silently_resolve_historical_taxonomy():
    doc = record('energy_complex', 'photosystem_i')
    example = doc['canonical_examples'][0]
    assert 'unresolved' in example['note']
    assert '197221' in example['note']
    discussions = keyed(doc['discussions'], 'discussion_id')
    assert discussions['jordan_source_taxon_reconciliation']['status'] == 'OPEN'
    casella = record('energy_complex', 'plasma_membrane_derived_photosystem_i')
    assert casella['canonical_examples'][0]['taxon_id'] == 'NCBITaxon:1140'
    assert 'PCC 7942' in casella['causal_graphs'][0]['description']


def test_f_type_product_relation_and_family_scope():
    doc = record('energy_complex', 'proton_transporting_atp_synthase_complex')
    assert all(t['taxon_id'] != 'NCBITaxon:2157' for t in doc['taxonomic_distribution'])
    edge = next(e for e in doc['causal_graphs'][0]['edges'] if e['object'] == 'atp')
    assert 'predicate_id' not in edge
    stalk = keyed(doc['components'], 'component_id')['peripheral_stalk']
    assert 'not universal' in stalk['role']
    assert 'gene_symbols' not in stalk


@pytest.mark.parametrize('slug,reference', [
    ('respiratory_chain_complex_iii', 'InterPro:IPR006317'),
    ('respiratory_chain_complex_iv', 'InterPro:IPR012422'),
])
def test_domain_context_is_not_whole_protein_grounding(slug, reference):
    doc = record('energy_complex', slug)
    component = next(c for c in doc['components']
                     if any(e['reference'] == reference for e in c.get('evidence', [])))
    assert component['grounding_status'] == 'REVIEWED_LABEL_ONLY'
    assert 'grounding' not in component
    assert all(n.get('grounding') != reference
               for g in doc['causal_graphs'] for n in g['nodes'])


def test_v_atpase_activity_belongs_to_whole_pump_not_v1_alone():
    doc = record('energy_complex', 'vacuolar_proton_transporting_v_type_atpase_complex')
    graph = doc['causal_graphs'][0]
    nodes = keyed(graph['nodes'], 'node_id')
    assert nodes['rotary_atpase_activity']['node_type'] == 'MOLECULAR_FUNCTION'
    edges = [e for e in graph['edges'] if e['object'] == 'rotary_atpase_activity']
    enabled = [e for e in edges if e.get('predicate_id') == 'RO:0002327']
    assert len(enabled) == 1 and enabled[0]['subject'] == 'vacuolar_v_atpase'
    assert any(e['subject'] == 'v1_domain' and 'predicate_id' not in e for e in edges)


def test_envelope_graph_directions_preserve_actors_cargo_and_capacity():
    graphs = record('envelope', 'gram_negative_bacterium_type_cell_wall')['causal_graphs']
    wall = keyed(graphs, 'graph_id')['lpp_lol_pg_tether_assembly']
    assert keyed(wall['nodes'], 'node_id')['lol_pathway']['node_type'] == 'PATHWAY'
    donor = next(e for e in wall['edges']
                 if e['subject'] == 'ldt_lpp' and e['object'] == 'thin_peptidoglycan')
    assert donor['predicate'] == 'uses acyl donor from'
    assert 'lysine is the acceptor' in donor['description']
    space = record('envelope', 'outer_membrane_bounded_periplasmic_space')['causal_graphs'][0]
    crossing = [e for e in space['edges'] if e['predicate'] == 'moves across']
    assert len(crossing) == 1 and crossing[0]['subject'] == 'lps'
    pg = record('envelope', 'peptidoglycan_based_cell_wall')['causal_graphs'][0]
    assert all(n.get('grounding') != 'CHEBI:27692' for n in pg['nodes'])
    assert next(e for e in pg['edges'] if e['object'] == 'turgor_resistance')['predicate'] == 'confers'


def test_s_layer_mass_is_not_stoichiometry_and_thickness_is_scoped():
    doc = record('envelope', 's_layer')
    assert 'stoichiometry' not in doc['components'][0]
    properties = keyed(doc['physical_properties'], 'property')
    assert properties['THICKNESS']['value'] == '5-10'
    assert 'bacterial' in properties['THICKNESS']['context']
    assert properties['MOLECULAR_MASS']['value'] == '40-170 kDa'
    assert 'repository' in doc['images'][0]['notes']
    assert 'permits reuse' in doc['images'][0]['notes']


def test_plastoglobule_plant_topology_is_not_asserted_for_algae():
    doc = record('inclusion', 'plastoglobule')
    core, layer = doc['components']
    assert 'tocopherols' in core['grounding_notes']
    assert 'apparently discontinuous' in layer['grounding_notes']
    assert 'proposed' in doc['functions'][0]['description']
    graph = doc['causal_graphs'][0]
    assert 'Higher-plant' in graph['scope_notes']
    assert graph['edges'][-1]['predicate'] == 'is proposed to support'


def test_pha_assay_scope_and_unknown_classwide_formation_requirement():
    doc = record('inclusion', 'polyhydroxyalkanoate_granule')
    components = keyed(doc['components'], 'component_id')
    assert components['phasins']['essentiality'] == 'UNKNOWN'
    assert 'do not establish dispensability of all phasins' in components['phasins']['evidence'][0]['notes']
    probe = keyed(components['pha_polymer_core']['evidence'], 'reference')['DOI:10.1038/srep26612']
    assert 'LactC2' in probe['notes'] and 'not a quantitative chemical-fraction analysis' in probe['notes']
    discussion = keyed(doc['discussions'], 'discussion_id')['exclude_phospholipid_monolayer']
    assert discussion['posed_date'] == '2026-09-10'
    assert 'Correction (2026-10-16)' in discussion['rationale']
    assert 'probe sensitivity' in discussion['resolution_note']


def test_sgp_conditional_requirement_names_the_nonforming_background():
    doc = record('inclusion', 'sulfur_globule')
    proteins = [c for c in doc['components'] if c['component_type'] == 'PROTEIN']
    assert all(c['essentiality'] == 'CONDITIONAL' for c in proteins)
    assert all('sgpBC double mutant' in c['role'] for c in proteins)
    assert 'either single' in proteins[0]['role']
    assert 'smaller globules' in proteins[1]['role']
    assert 'absent from most' not in doc['taxonomic_distribution'][0]['note']


def test_acidocalcisome_keeps_both_sides_of_unresolved_identity_conflict():
    doc = record('membrane_organelle', 'acidocalcisome')
    discussion = keyed(doc['discussions'], 'discussion_id')['bacterial_identity_conflict']
    assert discussion['status'] == 'OPEN'
    assert {e['reference'] for e in discussion['evidence']} == {
        'DOI:10.1074/jbc.M304548200', 'DOI:10.1128/AEM.02759-19',
        'DOI:10.1128/MMBR.00042-23',
    }
    assert 'without TEM confirmation' in doc['canonical_examples'][0]['note']
    assert 'does not settle' in doc['causal_graphs'][0]['scope_notes']
    assert 'Docampo and Huang 2024' not in yaml.safe_dump(doc)
    assert doc['mapping_status'] == 'PROPOSED'


def test_lipid_droplet_creation_history_is_explicitly_retrospective():
    histories = [yaml.safe_load(p.read_text())
                 for p in (ROOT / 'history/records/lipid_droplet').glob('*.yaml')]
    events = [e for h in histories for e in h['events'] if e['type'] == 'CREATE']
    assert any('Recorded now, not backdated' in e['details']
               and '9a6ab4ed3aead813f3c6de82d2714a0b265c90a8' in e['details'] for e in events)
