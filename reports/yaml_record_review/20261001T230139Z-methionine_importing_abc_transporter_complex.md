# methionine-importing ABC transporter complex YAML review

- PR: #1889
- Branch: `add-methionine-abc-transporter`
- Head reviewed: `ae3187c49c528b7595a256e06fccb00261b70dbd`
- Record: `data/structures/other/methionine_importing_abc_transporter_complex.yaml`
- History: `history/records/methionine_importing_abc_transporter_complex/2026-10-01T224813Z-codex-2b20c0.yaml`
- Reviewer: Codex
- Date: 2026-10-01

## Candidate And Duplicate Check

The pre-addition duplicate search used `rg --no-ignore --hidden` across
`data`, `history`, `reports`, and `pages` for `GO:1990197`,
`methionine-importing ABC transporter`, `methionine ABC`, `MetNI`, `MetQ`,
`metN`, `metI`, and `metQ`. It found no existing methionine-importing ABC
transporter complex record or obvious label/gene collision.

After source lookup exposed exact accessions, the pre-addition duplicate search
was repeated with `rg --no-ignore --hidden` across `data`, `history`, `reports`,
and `pages` for `UniProtKB:P30750`, `UniProtKB:P31547`, `UniProtKB:P28635`,
`InterPro:IPR012692`, `PDB:6CVL`, `PMID:22095702`, `PMID:30352853`,
`DOI:10.1002/pro.765`, and `DOI:10.1073/pnas.1811003115`. It found no
pre-existing record or exact evidence-accession collision.

The post-PR review rechecked `data`, `history`, `reports`, and `pages` with
`rg --no-ignore --hidden` for `GO:1990197`, `methionine-importing ABC transporter`,
MetNI/MetNIQ strings, `P30750`, `P31547`, `P28635`, `IPR012692`, `PDB:6CVL`,
`PMID:22095702`, `PMID:30352853`, and both primary DOIs; only the new record,
its history, regenerated embedding references, generated pages, and the
transient `reports/curie_check.tsv` report referenced those strings. The
temporary methionine expansion and note-fix mutators were absent under both
`find` and an ignored/hidden-inclusive `rg` search.

## Authority Checks

- QuickGO reports `GO:1990197` as an active cellular-component term named
  `methionine-importing ABC transporter complex`, with ATP-dependent exact
  synonymy, MetNI/MetNIQ narrow synonymy, and a `PMID:22095702` definition
  cross-reference.
- QuickGO reports `GO:1902495` as the active cellular-component term
  `transmembrane transporter complex`; `GO:1902495` is in the `GO:1990197`
  ancestor set.
- QuickGO reports `GO:0033232` as the active molecular-function term
  `ABC-type D-methionine transporter activity`.
- QuickGO reports `GO:0015191` as the active molecular-function term
  `L-methionine transmembrane transporter activity`.
- UniProtKB reports `P30750` as the reviewed E. coli K-12 entry named
  `Methionine import ATP-binding protein MetN`, with gene names `metN`, `abc`,
  `b0199`, and `JW0195`, a `GO:1990197` cross-reference, a `PDB:6CVL`
  cross-reference, and InterPro hits including exact proteobacterial MetN
  family `IPR012692`.
- UniProtKB reports `P31547` as the reviewed E. coli K-12 entry named
  `D-methionine transport system permease protein MetI`, with gene names
  `metI`, `yaeE`, `b0198`, and `JW0194`, a `GO:1990197` cross-reference, and a
  `PDB:6CVL` cross-reference.
- UniProtKB reports `P28635` as the reviewed E. coli K-12 entry named
  `D-methionine-binding lipoprotein MetQ`, with gene names `metQ`, `yaeC`,
  `b0197`, and `JW0193`, a `GO:1990197` cross-reference, and a `PDB:6CVL`
  cross-reference.
- InterPro reports `IPR012692` against `UniProtKB:P30750` as `ABC transporter,
  methionine import, ATP-binding protein MetN, proteobacteria`; other MetN
  InterPro hits are conserved-site, domain, or broader P-loop/ABC-family
  entries and are correctly unused for the MetN component grounding.
- InterPro reports only broad MetI-like domain/superfamily or amino-acid ABC
  permease entries against `UniProtKB:P31547`; the record correctly keeps MetI
  at `REVIEWED_LABEL_ONLY` instead of asserting one as an exact family.
- InterPro reports only the broader `Lipoprotein NlpA family` against
  `UniProtKB:P28635`; the record correctly keeps MetQ at `REVIEWED_LABEL_ONLY`
  instead of treating NlpA as an exact MetQ family.
- RCSB reports `PDB:6CVL` as the crystal structure of the E. coli ATPγS-bound
  MetNI methionine ABC transporter in complex with MetQ, maps the three
  polymer entities to `UniProtKB:P30750`, `UniProtKB:P31547`, and
  `UniProtKB:P28635`, and reports an assembly with two MetN molecules, two MetI
  molecules, and one MetQ molecule.
- PubMed reports `PMID:22095702` as the Protein Science article `Inward facing
  conformations of the MetNI methionine ABC transporter: Implications for the
  mechanism of transinhibition.`, with DOI `10.1002/pro.765`.
- RCSB reports `PMID:30352853` and Crossref reports
  `DOI:10.1073/pnas.1811003115` for Nguyen et al. 2018, the PNAS article
  describing the PDB:6CVL full MetNIQ structure.

## Review Findings

No concrete defects were found.

The review specifically checked:

- the new record identifier is the exact GO cellular-component term for
  methionine-importing ABC transporter complexes, not only the broader
  `transmembrane transporter complex` parent;
- exact GO synonymy and MetNI/MetNIQ narrow synonymy are represented without
  marking narrower E. coli-specific names as exact synonyms of the broader GO
  term;
- the parent note correctly describes `GO:1902495` as an ancestor of
  `GO:1990197`;
- `GO:0033232` and `GO:0015191` are molecular-function evidence for D- and
  L-methionine transport and are kept under `functions`, not used as structure
  identifiers;
- the MetN component uses the exact proteobacterial MetN InterPro family
  grounding, while broader NTPase, ABC-domain, ACT-like, and conserved-site
  accessions exposed by the same reviewed UniProt entry are deliberately
  avoided;
- the MetI and MetQ components keep `REVIEWED_LABEL_ONLY` grounding because the
  verified InterPro/Pfam hits are too broad, and the record carries an open
  `CURATION_TODO` attached to those two components;
- the reviewed E. coli K-12 UniProt examples have the expected `metN`, `metI`,
  and `metQ` gene labels and match the RCSB 6CVL polymer entities;
- `PDB:6CVL` supports the E. coli K-12 canonical example and the modeled
  `SUBUNIT_COUNT` value of 5 through the 2:2:1 MetN/MetI/MetQ biological
  assembly;
- no broad taxonomic-distribution row was added because the reviewed evidence
  establishes the E. coli K-12 complex and one exact proteobacterial MetN
  family, not a directly cited clade-wide distribution claim;
- no exact snippets were added from the structural literature;
- the history record targets the new YAML path and summarizes the GO, InterPro,
  UniProt, PDB, DOI/PMID, function, component, stoichiometry, and follow-up
  additions;
- rendered `pages/`, README statistics, and text embedding artifacts are
  regenerated from the new corpus state.

## Issues Filed

None.

## Local Verification

- `.venv/bin/linkml-validate -s src/cellstructuremech/schema/cellstructuremech.yaml -C CellStructureRecord data/structures/other/methionine_importing_abc_transporter_complex.yaml`
- `.venv/bin/python scripts/validate_strict.py --quiet data/structures/other/methionine_importing_abc_transporter_complex.yaml`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py history/records/methionine_importing_abc_transporter_complex/2026-10-01T224813Z-codex-2b20c0.yaml`
- `.venv/bin/python scripts/build_text_embedding_map.py --check`
- `.venv/bin/python scripts/render_pages.py --check`
- `.venv/bin/python scripts/check_docs.py --check`
- `.venv/bin/python scripts/validate_strict.py --quiet`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/validate_history.py`
- `.venv/bin/python scripts/fetch_snippets.py --verify --check`
- `.venv/bin/python scripts/check_trait_links.py --check`
- `.venv/bin/python scripts/check_curies.py --check --report reports/curie_check.tsv`
- `.venv/bin/python scripts/validate_id_label_correspondence.py -c conf/id_label_targets.yaml`
- `PATH=.venv/bin:$PATH .venv/bin/python scripts/run_qc.py`
- `git diff --check`
