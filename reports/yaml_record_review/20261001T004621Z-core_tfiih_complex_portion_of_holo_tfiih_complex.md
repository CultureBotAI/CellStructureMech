# Adversarial YAML Record Review: core TFIIH complex portion of holo TFIIH complex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1847
- Branch: `add-core-tfiih-holo`
- Commit reviewed: `c2d76285`
- Record: `data/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.yaml`
- History: `history/records/core_tfiih_complex_portion_of_holo_tfiih_complex/2026-10-01T002333Z-codex-995b05.yaml`
- Generated page: `pages/structures/other/core_tfiih_complex_portion_of_holo_tfiih_complex.html`
- Reviewed at: `2026-10-01T00:46:21Z`

## Scope

Reviewed the PR diff for the new `GO:0000438` CellStructureMech record, its
append-only history entry, regenerated embedding artifacts, README updates, and
the rendered HTML/index pages.

## Adversarial Checks

- Identity and duplication: PASS
  - `GO:0000438` exactly denotes `core TFIIH complex portion of holo TFIIH
    complex`.
  - The hidden/ignored-inclusive duplicate search found no standalone
    `GO:0000438` record before creation; expected hits were limited to GO
    cache/report artifacts, the parent `GO:0000439` TFIIH core record that
    discusses the narrower portion terms, and generated artifacts from this
    branch.
  - `SSL2-core TFIIH complex portion of holo TFIIH complex` is an exact GO
    synonym of `GO:0000438`, not an existing standalone record.
- Ontology boundary: PASS
  - `GO:0000439` is modeled as `parent_structures` because GO reports it as
    the is-a parent for `GO:0000438`.
  - `GO:0005675` is modeled through `part_of` because GO reports holo TFIIH as
    the larger complex containing this TFIIH-core portion.
  - The resolved interpretation discussion explicitly keeps TFIIK out of the
    component list because TFIIK is a partner subcomplex of whole holo TFIIH,
    not part of the TFIIH core portion itself.
- Component grounding: PASS
  - All seven TFIIH core protein classes named by the `GO:0000439` parent are
    present: Ssl2/XPB, Tfb1/p62, Tfb2/p52, Ssl1/p44, Tfb4/p34, Tfb5/p8, and
    Rad3/XPD.
  - Every curated protein constituent uses
    `grounding_status: REVIEWED_LABEL_ONLY`; no InterPro, Pfam, NCBIfam,
    UniProtKB, Complex Portal, or similar accession was guessed.
  - The open component-grounding TODO anchors to all seven explicit component
    IDs.
- Evidence and scope: PASS
  - Definition and exact synonymy are sourced to `GO:0000438`.
  - Component composition and Saccharomyces cerevisiae scoping are sourced to
    the GO-defined TFIIH core parent.
  - Holo-TFIIH parthood is sourced to `GO:0000438` and `GO:0005675` without
    turning the whole holo-TFIIH complex, TFIIK, or repair chemistry into
    components of this portion term.
- Graph and anchors: PASS
  - Every graph `component_ref` points to a local component row.
  - The assembly graph has exactly seven constituent-to-core edges and one
    core-to-holo `is part of` edge.
  - The graph stays nonmechanistic and does not claim an assembly order, a
    TFIIK association mechanism, or enzymatic transcription-initiation
    chemistry.
  - Discussion anchors are field-level or explicit `components#...` anchors.
- Generated artifacts: PASS
  - The rendered structure page, `pages/index.json`, GO-grounded listing,
    OTHER category page, browse page, README corpus block, and root/browser text
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
