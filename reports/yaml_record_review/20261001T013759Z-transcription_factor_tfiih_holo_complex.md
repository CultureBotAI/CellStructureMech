# Adversarial YAML Record Review: transcription factor TFIIH holo complex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1848
- Branch: `add-tfiih-holo-complex`
- Commit reviewed: `41be1d4e`
- Record: `data/structures/other/transcription_factor_tfiih_holo_complex.yaml`
- History: `history/records/transcription_factor_tfiih_holo_complex/2026-10-01T010714Z-codex-18d433.yaml`
- Generated page: `pages/structures/other/transcription_factor_tfiih_holo_complex.html`
- Reviewed at: `2026-10-01T01:37:59Z`

## Scope

Reviewed the PR diff for the new `GO:0005675` CellStructureMech record, its
append-only history entry, regenerated embedding artifacts, README updates, and
the rendered HTML/index pages.

## Adversarial Checks

- Identity and duplication: PASS
  - `GO:0005675` exactly denotes `transcription factor TFIIH holo complex`.
  - The hidden/ignored-inclusive duplicate search found no existing standalone
    `GO:0005675` or `GO:0070985` record before creation; expected hits were
    limited to prior generated artifacts, the GO liveness report, the newly
    added `GO:0000438` core TFIIH holo-portion record, its review report, and
    generated artifacts from this branch.
  - GO synonymy is carried with the GO-reported scopes: `holo TFIIH complex`
    and `cyclin-dependent protein kinase activating kinase holoenzyme complex`
    as exact synonyms, `CAK complex` as related, and `CDK-activating kinase` as
    broad.
- Ontology boundary: PASS
  - `GO:0019908`, `GO:0032806`, and `GO:0090575` are modeled as
    `parent_structures` because OLS reports them as direct is-a parents for
    `GO:0005675`.
  - `GO:0000438` and `GO:0070985` are modeled through `has_part` because GO
    reports the core TFIIH holo-complex portion and the TFIIK complex as parts
    of the TFIIH holo complex.
  - The resolved interpretation discussion explicitly keeps this record at the
    two-subcomplex holo-TFIIH level instead of duplicating TFIIH-core or TFIIK
    protein constituents from narrower records.
- Component grounding: PASS
  - The two local components are the two GO-grounded subcomplexes that compose
    the holo complex.
  - `core_tfiih_holo_portion` is grounded to `GO:0000438`.
  - `tfiik_complex` is grounded to `GO:0070985`.
  - No InterPro, Pfam, NCBIfam, UniProtKB, Complex Portal, or similar
    accession was guessed.
- Evidence and scope: PASS
  - Definition and synonymy are sourced to `GO:0005675`.
  - GO:0005675, GO:0000438, and GO:0070985 support the whole-holo,
    core-portion, and TFIIK subcomplex boundaries.
  - The Saccharomyces cerevisiae taxonomic row is constrained to the species
    explicitly present in the GO:0070985 definition.
  - GO-cited PubMed identifiers are included as record-level evidence without
    unsupported verbatim snippets.
- Graph and anchors: PASS
  - Every graph `component_ref` points to a local component row.
  - The assembly graph has exactly one core-TFIIH-to-holo edge and one
    TFIIK-to-holo edge.
  - The graph stays nonmechanistic and does not claim an assembly order, kinase
    activation pathway, or RNA polymerase II initiation chemistry.
  - Discussion anchors are field-level or explicit `components#...` anchors.
- Generated artifacts: PASS
  - The rendered structure page, `pages/index.json`, GO-grounded listing, OTHER
    category page, browse page, README corpus block, and root/browser text
    embedding artifacts include the added record.
- History: PASS
  - The append-only history record targets the new YAML file and validates
    against the vendored history schema.

## Findings

No concrete defects found; no GitHub issues were filed.

## Validation Reviewed

- Focused LinkML validation: PASS
- Focused strict validation: PASS
- Focused history validation: PASS
- Text embedding refresh/check: PASS
- Rendered pages drift check: PASS
- README/docs drift check: PASS
- Full strict validation: PASS
- Full history validation: PASS
- Snippet verification: PASS
- TraitMech link check: PASS
- Live CURIE check: PASS
- ID/label correspondence: PASS
- `git diff --check`: PASS
- `just qc`: PASS
