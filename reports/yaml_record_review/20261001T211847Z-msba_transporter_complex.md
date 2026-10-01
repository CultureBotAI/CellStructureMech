# MsbA transporter complex YAML review

- PR: #1886
- Branch: `add-msba-transporter-complex`
- Head reviewed: `6167364235d390cd5f7ea65599c7f210a734a6c5`
- Record: `data/structures/other/msba_transporter_complex.yaml`
- History: `history/records/msba_transporter_complex/2026-10-01T210410Z-codex-f74164.yaml`
- Reviewer: Codex
- Date: 2026-10-01

## Candidate And Duplicate Check

The pre-addition duplicate search used `rg --no-ignore --hidden` across
`data`, `history`, `reports`, and `pages` for `GO:1990199`, `MsbA`, `MsbA
transporter complex`, `MsbA dimer`, `P60752`, `IPR011917`, `PDB:3B5W`,
`PMID:18024585`, and `DOI:10.1073/pnas.0709388104`. It found no existing
MsbA transporter complex record and no exact identifier/accession collision.

The MsbA label search did find the existing lipopolysaccharide transport
system boundary note, which explicitly excludes MsbA from the LptA-G machine
because MsbA flips nascent LPS across the inner membrane before Lpt extracts
and transports it.

The post-PR review rechecked `data`, `history`, `reports`, and `pages` with
`rg --no-ignore --hidden` for the same exact GO, PDB, PMID, DOI, UniProtKB,
and InterPro strings; only the new record, generated pages/embeddings, and
the transient CURIE checker report referenced them. The temporary
`scripts/expand_msba_transporter_complex.py` mutator was absent under both
`find` and an ignored/hidden-inclusive `rg` search.

## Authority Checks

- QuickGO reports `GO:1990199` as an active cellular-component term named
  `MsbA transporter complex`, with exact synonyms `MsbA complex` and `MsbA
  dimer`, a `PMID:18024585` definition cross-reference, and definition text
  specifying an ABC transporter complex made of an MsbA dimer.
- The `GO:1990199` `is_a` ancestor set includes `GO:1902495`
  transmembrane transporter complex.
- QuickGO reports `GO:0015437` as the active molecular-function term
  `lipopolysaccharide floppase activity`.
- UniProt REST reports `P60752` as the reviewed E. coli K-12 entry named
  `ATP-dependent lipid A-core flippase`, with primary gene `msbA`, GO
  cross-reference `GO:1990199`, PDB cross-reference `3B5W`, and InterPro
  cross-reference `IPR011917`.
- InterPro reports `IPR011917` against `UniProtKB:P60752` as `ABC
  transporter, lipid A-core flippase, MsbA`; broader ABC-transporter and
  ATPase-domain entries on the same UniProt accession are correctly unused for
  component grounding.
- RCSB reports `PDB:3B5W` as `Crystal Structure of Eschericia coli MsbA`;
  polymer entity 1 maps to `UniProtKB:P60752`.
- RCSB reports biological assembly `3B5W-1` as a homomeric protein assembly
  containing two instances of polymer entity 1.
- RCSB and PubMed both link `PDB:3B5W` / `PMID:18024585` to
  `DOI:10.1073/pnas.0709388104` and the primary citation `Flexibility in the
  ABC transporter MsbA: Alternating access with a twist.`

## Review Findings

No concrete defects were found.

The review specifically checked:

- the new record identifier is the exact GO cellular-component term for the
  MsbA homodimer, not the broader ABC transporter or lipid-translocation
  function;
- GO exact synonymy and GO parentage are represented without broadening the
  record to all ABC transporters or to the downstream LptA-G LPS transport
  system;
- `GO:0015437` is molecular-function evidence for lipopolysaccharide floppase
  activity and is kept under `functions`;
- the only component is grounded to exact MsbA InterPro family `IPR011917`,
  while broader ABC-transporter and ATPase-domain InterPro accessions are
  deliberately avoided;
- the reviewed E. coli K-12 UniProt example has the expected `msbA` gene label
  and is cross-referenced from `PDB:3B5W`;
- `PDB:3B5W` assembly 1 supports the E. coli canonical example and the
  `SUBUNIT_COUNT` value of 2;
- the record intentionally leaves `taxonomic_distribution` unset because the
  curated authority checks support the E. coli exemplar and exact MsbA class
  identity, not a broad clade-level presence row;
- the history record targets the new YAML path and summarizes the GO,
  InterPro, UniProt, PDB, DOI/PMID, function, component, and stoichiometry
  additions;
- rendered `pages/`, README statistics, and text embedding artifacts are
  regenerated from the new corpus state.

## Issues Filed

None.

## Local Verification

- `.venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/msba_transporter_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet data/structures/other/msba_transporter_complex.yaml`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py history/records/msba_transporter_complex/2026-10-01T210410Z-codex-f74164.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py`
- `.venv/bin/python scripts/fetch_snippets.py --verify --check`
- `.venv/bin/python scripts/check_trait_links.py --check`
- `.venv/bin/python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `.venv/bin/python scripts/build_text_embedding_map.py --check`
- `.venv/bin/python scripts/render_pages.py --check`
- `.venv/bin/python scripts/check_docs.py --check`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`
