# 3-phenylpropionate dioxygenase complex record review

## Scope

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1893
- Record: `data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml`
- Identifier: `GO:0009334`
- Label: `3-phenylpropionate dioxygenase complex`

## Duplicate and boundary checks

- Re-ran a hidden- and ignored-inclusive duplicate sweep with
  `rg --no-ignore --hidden` for `GO:0009334`, the preferred label,
  `3-phenylpropionate dioxygenase`, `HCAMULTI-CPLX`, `PMID:9603882`, and the
  exact subunit gene names `hcaE`, `hcaF`, `hcaC`, and `hcaD`.
- The exact identifier, label, MetaCyc xref, PMID, and subunit gene names were
  absent from `data/structures` and generated/review artifacts before this PR.
- The candidate denotes one four-protein bacterial enzyme complex, so it is
  not a duplicate of the adjacent SsuD/SsuE-family oxidoreductase records or
  other `GO:1990204` children.

## Authority checks

- QuickGO `GO:0009334`
  - active cellular-component term
  - label: `3-phenylpropionate dioxygenase complex`
  - definition xrefs: `MetaCyc:HCAMULTI-CPLX`, `PMID:9603882`
  - current oxidoreductase-complex parentage through `GO:1990204`
  - molecular-function handoff in the term comment to `GO:0008695`
- QuickGO `GO:0008695`
  - active molecular-function term
  - label: `3-phenylpropionate dioxygenase activity`
  - capable-of child includes `GO:0009334`
- PubMed `PMID:9603882`
  - Díaz, Ferrández and García 1998, Journal of Bacteriology
  - DOI reported by PubMed: `10.1128/JB.180.11.2915-2923.1998`
  - PubMed Central full text: `PMC107259`
- UniProtKB
  - `P0ABR5` is reviewed E. coli K-12 HcaE and carries `GO:0009334`
  - `Q47140` is reviewed E. coli K-12 HcaF and carries `GO:0009334`
  - `P0ABW0` is reviewed E. coli K-12 HcaC and carries `GO:0009334`
  - `P77650` is reviewed E. coli K-12 HcaD and carries `GO:0009334`
- InterPro on the four reviewed E. coli K-12 accessions
  - `IPR020875` verified as the exact HcaE alpha-subunit family
  - `IPR023712` verified as the exact HcaF beta-subunit family
  - `IPR023739` verified as the exact HcaC ferredoxin-subunit family
  - `IPR023744` verified as the exact HcaD ferredoxin--NAD(+) reductase family
  - Broader domain, binding-site, and superfamily hits on the same accessions
    were checked and deliberately not used as component groundings.

## PR diff review

- The PR adds one structure YAML and one matching repository history record.
- `pages/structures/other/3_phenylpropionate_dioxygenase_complex.html` renders
  the new record and links `GO:0009334`, `GO:0008695`, the four InterPro
  families, the four UniProt examples, `PMID:9603882`, and
  `DOI:10.1128/JB.180.11.2915-2923.1998` correctly.
- `data/embeddings/structure_text_map.json` and
  `pages/data/structure_text_map.json` are byte-identical.
- `data/embeddings/structure_text_neighbors.json` and
  `pages/data/structure_text_neighbors.json` are byte-identical.
- The PR-local history entry targets
  `data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml` and
  validates against the vendored history schema.
- No concrete defects were found that warranted a GitHub review issue.

## Local validation

- `python scripts/build_text_embedding_map.py --refresh`
- `python scripts/build_text_embedding_map.py --check`
- `python scripts/render_pages.py`
- `python scripts/check_docs.py --write`
- `python scripts/render_pages.py --check`
- `python scripts/check_docs.py --check`
- `linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml`
- `python scripts/validate_strict.py --quiet data/structures/other/3_phenylpropionate_dioxygenase_complex.yaml`
- `PATH=.venv/bin:$PATH python scripts/validate_history.py history/records/3_phenylpropionate_dioxygenase_complex/2026-10-02T005424Z-codex-385233.yaml`
- `python scripts/validate_strict.py --quiet`
- `PATH=.venv/bin:$PATH python scripts/validate_history.py`
- `python scripts/fetch_snippets.py --verify --check`
- `python scripts/check_trait_links.py --check`
- `python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `PATH=.venv/bin:$PATH python scripts/run_qc.py`
- `git diff --check`
