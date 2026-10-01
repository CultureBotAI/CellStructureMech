# Adversarial YAML Record Review: transcription factor TFIIK complex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1849
- Branch: `add-tfiik-complex`
- Commit reviewed: `9868d1c4`
- Record: `data/structures/other/transcription_factor_tfiik_complex.yaml`
- History: `history/records/transcription_factor_tfiik_complex/2026-10-01T015725Z-codex-47f17d.yaml`
- Generated page: `pages/structures/other/transcription_factor_tfiik_complex.html`
- Reviewed at: `2026-10-01T02:16:44Z`

## Scope

Reviewed the PR diff for the new `GO:0070985` CellStructureMech record, its
append-only history entry, regenerated embedding artifacts, README updates, and
the rendered HTML/index pages.

## Adversarial Checks

- Identity and duplication: PASS
  - `GO:0070985` exactly denotes `transcription factor TFIIK complex`.
  - The hidden/ignored-inclusive duplicate search found no existing standalone
    TFIIK record before creation; expected hits were limited to the just-merged
    `GO:0005675` holo-TFIIH record, its generated pages and embedding artifacts,
    `reports/curie_check.tsv`, `build/curie_cache.json`, and the prior
    holo-TFIIH review report.
  - GO synonymy is carried with the GO-reported scopes: `TFIIK complex` as an
    exact synonym, `cyclin H-CDK7 complex` as related, and
    `Mcs6/Mcs2/Pmh1 complex` as narrow.
- Ontology boundary: PASS
  - `GO:0090575` is modeled as `parent_structures` because OLS reports it as
    the direct is-a parent for `GO:0070985`.
  - `GO:0005675` is modeled through `part_of` because GO defines TFIIK as a
    complex that forms part of holo TFIIH.
  - The resolved interpretation discussion explicitly keeps TFIIK as its own
    kinase subcomplex rather than merging it into the whole TFIIH holo complex.
- Component grounding: PASS
  - The three local components match the Saccharomyces/human protein pairs named
    in the GO definition: Ccl1p/Cyclin H, Tfb3p/MAT1, and Kin28p/CDK7.
  - Every curated protein constituent uses
    `grounding_status: REVIEWED_LABEL_ONLY`; no InterPro, Pfam, NCBIfam,
    UniProtKB, Complex Portal, or similar accession was guessed.
  - The open component-grounding TODO anchors to all three explicit component
    IDs.
- Evidence and scope: PASS
  - Definition, synonymy, and TFIIK subunit composition are sourced to
    `GO:0070985`.
  - Holo-TFIIH parthood is sourced to `GO:0070985` and `GO:0005675`.
  - The Saccharomyces cerevisiae taxonomic row is constrained to the species
    named through GO:0070985's Saccharomyces subunit nomenclature.
  - GO-cited PubMed identifiers are included as record-level evidence without
    unsupported verbatim snippets.
- Graph and anchors: PASS
  - Every graph `component_ref` points to a local component row.
  - The assembly graph has exactly one edge from each curated TFIIK protein
    constituent to the TFIIK complex.
  - The graph stays nonmechanistic and does not claim a subunit recruitment
    order, kinase activation pathway, or RNA polymerase II CTD phosphorylation
    chemistry.
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
