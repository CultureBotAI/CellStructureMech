# Adversarial YAML Review: protocatechuate 3,4-dioxygenase complex

- PR: #1894
- Reviewed head: `1de871d332286e2927a7103bf1b2d8898810c29f`
- Record: `data/structures/other/protocatechuate_3_4_dioxygenase_complex.yaml`
- Report timestamp: `20261002T014120Z`

## Scope

Reviewed the new `GO:7770085` protocatechuate 3,4-dioxygenase complex record,
its `GO:7770085` id-label exception for the local OAK GO snapshot, the
append-only history record, generated embedding JSON, and rendered pages.

## Evidence And Identity

- QuickGO resolved `GO:7770085` as an active cellular-component term named
  `protocatechuate 3,4-dioxygenase complex`, with `PcaGH complex`, `PcaHG
  complex`, and `protocatechuate 3,4-oxygenase complex` synonymy.
- QuickGO listed `GO:7770085` as an `is_a` child of `GO:1990204`
  `oxidoreductase complex`.
- QuickGO resolved `GO:0018578` as active `protocatechuate 3,4-dioxygenase
  activity`; OLS4 also resolved `GO:7770085` and reported its 2026-07-16
  creation date.
- PubMed resolved GO's primary `PMID:25558786` citation as Yamanashi et al.
  2015, DOI `10.1080/09168451.2014.993915`.
- InterPro resolved exact family entries `IPR012786` and `IPR012785` for the
  protocatechuate 3,4-dioxygenase alpha and beta subunits.
- UniProt resolved reviewed `Pseudomonas putida` PcaG/PcaH accessions
  `P00436` and `P00437`, and their UniProt records cite Frazee et al. 1993,
  DOI `10.1128/jb.175.19.6194-6202.1993`, for the `Pseudomonas putida`
  protocatechuate dioxygenase genes.
- NCBI Taxonomy resolved `Rhodococcus jostii RHA1` to `NCBITaxon:101510` and
  `Pseudomonas putida` to `NCBITaxon:303`.

## Duplicate Check

Before adding the record, a hidden/ignored-inclusive duplicate search over
`data`, `history`, `pages`, `reports`, `scripts`, `docs`, `src`, `curation`,
`research`, and `.github` found no pre-existing exact record for:

- `GO:7770085`
- `protocatechuate 3,4-dioxygenase complex`
- `PcaGH complex`
- `PcaHG complex`
- `protocatechuate 3,4-oxygenase complex`
- `PMID:25558786`
- `pcaG`
- `pcaH`

After scaffolding, a second hidden/ignored-inclusive search for the exact GO,
synonym, DOI, PMID, InterPro, UniProt, and gene identifiers only found the new
protocatechuate files and their generated artifacts.

## Rendered Artifact Review

- Confirmed `pages/structures/other/protocatechuate_3_4_dioxygenase_complex.html`
  links `GO:7770085`, `GO:0018578`, `InterPro:IPR012786`,
  `InterPro:IPR012785`, `UniProtKB:P00436`, `UniProtKB:P00437`,
  `PMID:25558786`, `PMID:8407791`, `DOI:10.1080/09168451.2014.993915`, and
  `DOI:10.1128/jb.175.19.6194-6202.1993`.
- Confirmed `pages/data/structure_text_map.json` is byte-identical to
  `data/embeddings/structure_text_map.json`.
- Confirmed `pages/data/structure_text_neighbors.json` is byte-identical to
  `data/embeddings/structure_text_neighbors.json`.

## Validation

- `scripts/build_text_embedding_map.py --check`
- `scripts/render_pages.py --check`
- `scripts/check_docs.py --check`
- Single-record `linkml-validate`
- Single-record `scripts/validate_strict.py --quiet`
- Single-history `scripts/validate_history.py`
- Full `scripts/validate_strict.py --quiet`
- Full `scripts/validate_history.py`
- `scripts/fetch_snippets.py --verify --check`
- `scripts/check_trait_links.py --check`
- `scripts/check_curies.py --check --report reports/curie_check.tsv`
- `scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `scripts/run_qc.py`
- `git diff --check`

## Findings

No concrete defects found. No review issue filed.
