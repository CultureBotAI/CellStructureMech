# alkanesulfonate monooxygenase complex record review

## Scope

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1892
- Record: `data/structures/other/alkanesulfonate_monooxygenase_complex.yaml`
- Identifier: `GO:1990201`
- Label: `alkanesulfonate monooxygenase complex`

## Duplicate and boundary checks

- Re-ran a hidden- and ignored-inclusive duplicate sweep with
  `rg --no-ignore --hidden` for `GO:1990201`, the preferred label,
  the `SsuD complex` synonym, `ssuD`, `UniProtKB:P80645`, `PMID:10480865`,
  and `DOI:10.1074/jbc.274.38.26639`.
- The exact `GO:1990201` identifier and `alkanesulfonate monooxygenase complex`
  label were absent from `data/structures`.
- Existing hits to `SsuD`, `P80645`, `PMID:10480865`, and
  `DOI:10.1074/jbc.274.38.26639` came from the sibling `GO:1990200`
  SsuD-SsuE complex and `GO:1990202` FMN reductase complex records or from
  generated artifacts and previous review reports.
- The new record was kept separate from `GO:1990200` and `GO:1990202` because
  `GO:1990201` denotes the SsuD tetrameric monooxygenase complex, while
  `GO:1990200` denotes the SsuD-SsuE complex and `GO:1990202` denotes the SsuE
  FMN reductase dimer.

## Authority checks

- QuickGO `GO:1990201`
  - active cellular-component term
  - label: `alkanesulfonate monooxygenase complex`
  - definition source xrefs: `PMID:10480865`, `PMID:16997955`
  - narrow synonym: `SsuD complex`
  - current ancestry/parthood/function checks used for the record:
    `GO:1990204` oxidoreductase complex parent, `GO:0005829` cytosol parthood,
    and `GO:0008726` alkanesulfonate monooxygenase activity
- UniProtKB `P80645`
  - reviewed E. coli K-12 `ssuD` entry
  - protein name: `Alkanesulfonate monooxygenase`
  - GO annotations include `GO:1990201`
  - InterPro cross-references include `IPR019911`
- InterPro on `P80645`
  - verified `IPR019911`
    `Alkanesulphonate monooxygenase, FMN-dependent` as the exact family used
    for the SsuD component
  - checked broader domain/superfamily hits and the broader `IPR050172`
    SsuD/RutA family; none of those were used as the grounding
- PubMed
  - checked `PMID:10480865`: Eichhorn, van der Ploeg and Leisinger 1999,
    Journal of Biological Chemistry,
    `DOI:10.1074/jbc.274.38.26639`
  - checked `PMID:16997955`: Abdurachim and Ellis 2006, Journal of
    Bacteriology, `DOI:10.1128/JB.00966-06`; this supports the adjacent
    SsuD-SsuE interaction boundary but was not needed for a separate
    record-level assertion here
- RCSB PDB
  - checked `1M41` and `1NQK` as E. coli SsuD crystal structures
  - deliberately left them out of `xrefs` because they are crystallographic
    component structures rather than true equivalents of the complete
    `GO:1990201` cellular-component term

## PR diff review

- The PR adds one structure YAML and one matching repository history record.
- `pages/structures/other/alkanesulfonate_monooxygenase_complex.html` renders
  the new record and links `GO:1990201`, `InterPro:IPR019911`,
  `UniProtKB:P80645`, `PMID:10480865`, and
  `DOI:10.1074/jbc.274.38.26639` correctly.
- `data/embeddings/structure_text_map.json` and
  `pages/data/structure_text_map.json` are byte-identical.
- `data/embeddings/structure_text_neighbors.json` and
  `pages/data/structure_text_neighbors.json` are byte-identical.
- The PR-local history entry targets
  `data/structures/other/alkanesulfonate_monooxygenase_complex.yaml` and
  validates against the vendored history schema.
- No concrete defects were found that warranted a GitHub review issue.

## Local validation

- `python scripts/build_text_embedding_map.py --refresh`
- `python scripts/build_text_embedding_map.py --check`
- `python scripts/render_pages.py`
- `python scripts/check_docs.py --write`
- `python scripts/render_pages.py --check`
- `python scripts/check_docs.py --check`
- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/alkanesulfonate_monooxygenase_complex.yaml`
- `python scripts/validate_strict.py --quiet data/structures/other/alkanesulfonate_monooxygenase_complex.yaml`
- `PATH=.venv/bin:$PATH python scripts/validate_history.py history/records/alkanesulfonate_monooxygenase_complex/2026-10-02T001138Z-codex-dea1fa.yaml`
- `python scripts/validate_strict.py --quiet`
- `PATH=.venv/bin:$PATH python scripts/validate_history.py`
- `python scripts/fetch_snippets.py --verify --check`
- `python scripts/check_trait_links.py --check`
- `python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `PATH=.venv/bin:$PATH python scripts/run_qc.py`
- `git diff --check`
