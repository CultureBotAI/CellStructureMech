# Adversarial YAML Review: glycine reductase complex

- PR: #1896
- Reviewed head: `b80774de25a8c82843b80fbfb14a2f238c0ad093`
- Record: `data/structures/other/glycine_reductase_complex.yaml`
- Report timestamp: `20261002T025521Z`

## Scope

Reviewed the new `GO:0030700` glycine reductase complex record, its append-only
history record, generated embedding JSON, and rendered pages.

## Evidence And Identity

- QuickGO resolved `GO:0030700` as an active cellular-component term named
  `glycine reductase complex`.
- OLS4 listed `GO:0030700` as a direct `is_a` child of `GO:1990204`
  `oxidoreductase complex`.
- QuickGO resolved `GO:0030699` as active `glycine reductase activity`.
- PubMed resolved GO's primary `PMID:2018775` citation as Arkowitz and Abeles
  1991, DOI `10.1021/bi00230a039`.
- PubMed resolved Graentzdoerffer, Pich and Andreesen 2001 as `PMID:11271425`,
  DOI `10.1007/s002030000232`.
- PubMed resolved the GrdA papers `PMID:1429431` and `PMID:2963330`, with DOIs
  `10.1128/jb.174.22.7080-7089.1992` and `10.1073/pnas.85.2.368`.
- InterPro resolved exact family entries for glycine reductase complex
  selenoprotein A (`IPR006812`) and glycine reductase selenoprotein B
  (`IPR010186`).
- UniProt resolved reviewed `Acetoanaerobium sticklandii` DSM 519 GrdA
  accession `P26971`.
- NCBI Taxonomy resolved `Acetoanaerobium sticklandii` DSM 519 to
  `NCBITaxon:499177`.

## Duplicate Check

Before adding the record, a hidden/ignored-inclusive duplicate search over
`data`, `history`, `pages`, `reports`, `scripts`, `docs`, `src`, `curation`,
`research`, and `.github` found no pre-existing exact record for:

- `GO:0030700`
- `glycine reductase complex`
- `glycine reductase`
- `PMID:2018775`
- `PMID:11271425`
- `DOI:10.1007/s002030000232`
- `grdA`
- `grdB`
- `grdC`
- `grdE`

After scaffolding, a second hidden/ignored-inclusive search for the GO term,
label, DOI, PMID, InterPro, UniProt, and `grdA`/`grdB`/`grdC`/`grdD`
identifiers only found the new glycine reductase files and their generated
artifacts.

## Component Boundary Review

- Confirmed that only reviewed `UniProtKB:P26971` is used as a
  `protein_examples` entry.
- Confirmed unreviewed GrdB, GrdC, and GrdD UniProt accessions `Q93KD7`,
  `Q9EV93`, and `Q9EV92` are not asserted in the record.
- Confirmed reviewed `Peptoclostridium acidaminophilum` GrdC accession
  `P54935` was not reused for the `Acetoanaerobium sticklandii` protein C
  boundary.
- Confirmed broad GrdC InterPro domains `IPR013751`, `IPR045984`,
  `IPR017236`, `IPR016039`, `IPR003664`, and `IPR012116` are not asserted as
  glycine reductase protein C family groundings.
- Confirmed thioredoxin-system genes `trxA` and `trxB`, and the separately
  curated GrdE component-B product, were not modeled as top-level components of
  the three-component GO structure.

## Rendered Artifact Review

- Confirmed `pages/structures/other/glycine_reductase_complex.html` links
  `GO:0030700`, `GO:0030699`, `InterPro:IPR006812`,
  `InterPro:IPR010186`, `UniProtKB:P26971`, `PMID:2018775`,
  `PMID:11271425`, `PMID:1429431`, `PMID:2963330`,
  `DOI:10.1021/bi00230a039`, `DOI:10.1007/s002030000232`,
  `DOI:10.1128/jb.174.22.7080-7089.1992`, and
  `DOI:10.1073/pnas.85.2.368`.
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
