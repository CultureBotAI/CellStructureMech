"""Offline tests for the gene-symbol accession route (#183) — no network.

The value of this adapter is entirely in what it refuses to write, so most of
these tests are about declining.
"""

from __future__ import annotations

import pytest

from scripts import uniprot_genes as G


def entry(acc, names, taxon, organism="Escherichia coli (strain K12)", locations=(), label="A protein"):
    """A UniProt search result, trimmed to the fields the adapter reads."""
    gene = {"geneName": {"value": names[0]},
            "synonyms": [{"value": n} for n in names[1:]]}
    comments = [{
        "commentType": "SUBCELLULAR LOCATION",
        "subcellularLocations": [
            {"location": {"value": name,
                          "evidences": [{"evidenceCode": "ECO:0000269", "source": "PubMed", "id": p}
                                        for p in pmids]}}
            for name, pmids in locations
        ],
    }] if locations else []
    return {
        "primaryAccession": acc,
        "genes": [gene],
        "organism": {"taxonId": taxon, "scientificName": organism},
        "proteinDescription": {"recommendedName": {"fullName": {"value": label}}},
        "comments": comments,
    }


@pytest.fixture
def fake_search(monkeypatch):
    """Route search_gene to a dict keyed by (symbol, taxon)."""
    table: dict[tuple[str, int], list[dict]] = {}
    monkeypatch.setattr(G, "search_gene", lambda s, t: table.get((s, t), []))
    return table


# ------------------------------------------------------------------ reading


def test_gene_names_includes_synonyms():
    """rodA is a synonym of mrdB; a route that only read primary names would
    never match the symbol the record actually declares."""
    assert G.gene_names(entry("P0ABG7", ["mrdB", "rodA"], 83333)) == ["mrdB", "rodA"]


def test_localisations_keeps_only_experimental_pubmed_evidence():
    e = entry("P0A9X4", ["mreB"], 83333, locations=[("Cytoplasm", ["15612918"])])
    e["comments"][0]["subcellularLocations"][0]["location"]["evidences"] += [
        {"evidenceCode": "ECO:0000255", "source": "PubMed", "id": "99999999"},
        {"evidenceCode": "ECO:0000269", "source": "Ensembl", "id": "88888888"},
    ]
    assert G.localisations(e) == [("Cytoplasm", ["15612918"])]


# ------------------------------------------------------------- what it takes


def test_one_exact_reviewed_entry_is_accepted(fake_search):
    fake_search[("mreB", 83333)] = [entry("P0A9X4", ["mreB"], 83333)]
    hit, why = G.resolve({"gene_symbols": ["mreB"]}, [(83333, "E. coli K-12")])
    assert why == "ok"
    assert hit["entry"]["primaryAccession"] == "P0A9X4"
    assert hit["narrowed"] is False


def test_symbols_are_tried_in_the_order_the_record_lists_them(fake_search):
    """The curator's ordering is the ranking; the adapter does not re-rank it."""
    fake_search[("hdh", 174633)] = [entry("Q1", ["hdh"], 174633)]
    fake_search[("hao", 174633)] = [entry("Q2", ["hao"], 174633)]
    hit, _ = G.resolve({"gene_symbols": ["hdh", "hao"]}, [(174633, "Kuenenia")])
    assert hit["entry"]["primaryAccession"] == "Q1"


def test_a_taxon_that_is_ambiguous_does_not_disqualify_the_next(fake_search):
    fake_search[("pilA", 287)] = [entry(f"P{i}", ["pilA"], 287) for i in range(5)]
    fake_search[("pilA", 264462)] = [entry("Q9", ["pilA"], 264462, organism="Bdellovibrio")]
    hit, why = G.resolve({"gene_symbols": ["pilA"]},
                         [(287, "P. aeruginosa"), (264462, "B. bacteriovorus")])
    assert why == "ok"
    assert hit["entry"]["primaryAccession"] == "Q9"


# ------------------------------------------------------------ what it refuses


def test_several_reviewed_entries_for_one_symbol_are_never_chosen_between(fake_search):
    """gene_exact:pilA returns five reviewed pilin alleles in P. aeruginosa. There
    is no honest way to pick one, so the component gets nothing."""
    fake_search[("pilA", 287)] = [entry(f"P{i}", ["pilA"], 287) for i in range(5)]
    hit, why = G.resolve({"gene_symbols": ["pilA"]}, [(287, "P. aeruginosa")])
    assert hit is None
    assert "5 reviewed entries" in why


def test_a_hit_whose_gene_names_do_not_contain_the_symbol_is_rejected(fake_search):
    """The search is trusted to find candidates, never to have understood the
    question: UniProt's matching is looser than an equality test."""
    fake_search[("flgE", 90371)] = [entry("P1", ["flgD"], 90371)]
    hit, why = G.resolve({"gene_symbols": ["flgE"]}, [(90371, "S. Typhimurium")])
    assert hit is None
    assert "none an exact gene match" in why


def test_no_reviewed_entry_is_reported_as_such(fake_search):
    hit, why = G.resolve({"gene_symbols": ["nosuchgene"]}, [(83333, "E. coli K-12")])
    assert (hit, why) == (None, "no reviewed entry")


# -------------------------------------------------------- the taxon tie-break


def test_the_entry_at_the_named_node_wins_over_sub_strain_duplicates(fake_search):
    """rodZ in E. coli K-12 returns the same protein three times, once per
    sequenced sub-strain. The node the record names is the record's own choice."""
    fake_search[("rodZ", 83333)] = [
        entry("P27434", ["rodZ", "yfgA"], 83333),
        entry("C4ZX91", ["rodZ"], 595496),
        entry("B1XAZ1", ["rodZ"], 316385),
    ]
    hit, why = G.resolve({"gene_symbols": ["rodZ"]}, [(83333, "E. coli K-12")])
    assert why == "ok"
    assert hit["entry"]["primaryAccession"] == "P27434"
    assert hit["narrowed"] is True


def test_two_entries_at_the_named_node_are_still_ambiguous(fake_search):
    """The tie-break is 'exactly one at the node', not 'prefer the node'."""
    fake_search[("dupe", 83333)] = [entry("A1", ["dupe"], 83333), entry("A2", ["dupe"], 83333)]
    hit, why = G.resolve({"gene_symbols": ["dupe"]}, [(83333, "E. coli K-12")])
    assert hit is None
    assert "2 reviewed entries" in why


def test_no_entry_at_the_named_node_still_accepts_a_lone_descendant(fake_search):
    fake_search[("pilA", 287)] = [entry("P04739", ["pilA"], 208964, organism="P. aeruginosa PAO1")]
    hit, why = G.resolve({"gene_symbols": ["pilA"]}, [(287, "P. aeruginosa")])
    assert why == "ok"
    assert hit["entry"]["primaryAccession"] == "P04739"


# ------------------------------------------------------------ what it records


def test_the_example_records_the_entrys_own_organism_not_the_records_node():
    """The record names the species; the reviewed entry often sits on a strain
    below it. Writing the record's node would misstate where the entry is."""
    hit = {"entry": entry("P04739", ["pilA"], 208964, organism="P. aeruginosa PAO1"),
           "symbol": "pilA", "taxon_label": "P. aeruginosa", "narrowed": False}
    ex = G.build_example(hit, "2026-09-07", {})
    assert ex["taxon_id"] == "NCBITaxon:208964"
    assert ex["taxon_label"] == "P. aeruginosa PAO1"


def test_the_note_names_the_location_uniprot_states_not_this_structure():
    """The entry says nothing about the record's structure; a note implying it
    did would be the fabrication this route exists to avoid."""
    hit = {"entry": entry("P0A9X4", ["mreB"], 83333, locations=[("Cytoplasm", ["15612918"])]),
           "symbol": "mreB", "taxon_label": "E. coli K-12", "narrowed": False}
    ex = G.build_example(hit, "2026-09-07", {"15612918": "Kruse T et al. 2005, ‘T’, Mol Microbiol."})
    note = ex["evidence"][0]["notes"]
    assert ex["evidence"][0]["reference"] == "PMID:15612918"
    assert "'Cytoplasm' localisation of P0A9X4" in note
    assert note.startswith("Kruse T et al. 2005,")


def test_an_entry_with_no_experimental_localisation_cites_only_itself():
    hit = {"entry": entry("I6WZG6", ["enc"], 1773, organism="M. tuberculosis"),
           "symbol": "enc", "taxon_label": "M. tuberculosis", "narrowed": False}
    ex = G.build_example(hit, "2026-09-07", {})
    assert ex["evidence"] == [{
        "reference": "https://www.uniprot.org/uniprotkb/I6WZG6",
        "notes": G.entry_note("I6WZG6", "enc", "M. tuberculosis"),
    }]
    assert "gene identity only" in ex["evidence"][0]["notes"]


def test_the_role_disclaims_membership_in_the_structure():
    hit = {"entry": entry("P0A9X4", ["mreB"], 83333), "symbol": "mreB",
           "taxon_label": "E. coli K-12", "narrowed": False}
    role = G.build_example(hit, "2026-09-07", {})["role"]
    assert "not itself evidence that the protein is part of this structure" in role


def test_the_role_names_both_symbols_when_uniprots_primary_differs():
    """rodA and mrdB are one gene; leaving the two names unexplained reads as a
    mismatch between the record and the entry."""
    hit = {"entry": entry("P0ABG7", ["mrdB", "rodA"], 83333), "symbol": "rodA",
           "taxon_label": "E. coli K-12", "narrowed": False}
    role = G.build_example(hit, "2026-09-07", {})["role"]
    assert "gene rodA, which UniProt lists under the primary name mrdB," in role


def test_evidence_is_deduplicated_and_capped():
    """One paper cited for two locations is one citation, and no entry drowns a
    component in citations."""
    locations = [("Cytoplasm", ["1", "1", "2"]), ("Cell inner membrane", ["1", "3", "4"])]
    hit = {"entry": entry("P1", ["g"], 83333, locations=locations), "symbol": "g",
           "taxon_label": "E. coli K-12", "narrowed": False}
    refs = [e["reference"] for e in G.build_example(hit, "2026-09-07", {})["evidence"]]
    assert refs == sorted(set(refs), key=refs.index)
    assert len(refs) <= G.MAX_EVIDENCE


# -------------------------------------------------------------- what it skips


def test_only_protein_components_without_an_accession_are_candidates():
    doc = {"components": [
        {"component_id": "a", "component_type": "PROTEIN", "gene_symbols": ["x"]},
        {"component_id": "b", "component_type": "PROTEIN", "gene_symbols": ["x"],
         "protein_examples": [{"uniprot_id": "UniProtKB:P1"}]},
        {"component_id": "c", "component_type": "PROTEIN_COMPLEX", "gene_symbols": ["x"]},
        {"component_id": "d", "component_type": "PROTEIN"},
    ]}
    assert [c["component_id"] for c in G.candidates(doc)] == ["a"]


def test_a_record_with_no_canonical_taxon_is_reported_not_guessed_at():
    """Every accession is taxon-paired to a taxon the record itself names; with
    none named there is nothing to pair to."""
    doc = {"components": [{"component_id": "a", "component_type": "PROTEIN",
                           "gene_symbols": ["x"]}]}
    assert G.plan_record(doc, "2026-09-07") == [("a", "no canonical taxon on the record", None)]
