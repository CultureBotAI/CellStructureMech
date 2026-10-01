# Adversarial YAML Record Review: transcription factor TFIIH core complex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1846
- Branch: `add-tfiih-core-complex`
- Commit reviewed: `645a581b`
- Record: `data/structures/other/transcription_factor_tfiih_core_complex.yaml`
- History: `history/records/transcription_factor_tfiih_core_complex/2026-09-30T235047Z-codex-fbf027.yaml`
- Generated page: `pages/structures/other/transcription_factor_tfiih_core_complex.html`
- Reviewed at: `2026-10-01T00:06:39Z`

## Scope

Reviewed the PR diff for the new `GO:0000439` CellStructureMech record, its
append-only history entry, regenerated embedding artifacts, README updates, and
the rendered HTML/index pages.

## Adversarial Checks

- Identity and duplication: PASS
  - `GO:0000439` exactly denotes `transcription factor TFIIH core complex`.
  - The hidden/ignored-inclusive duplicate search found no standalone
    `GO:0000439` record before creation; previous hits were GO cache/report
    artifacts, the `GO:0000440` TFIIH-core NEF3 portion record, generated
    pages, and the previous `GO:0000440` review report.
  - `SSL2-core TFIIH complex` and `core TFIIH complex` are exact GO synonyms
    of the generic TFIIH core term, not of an existing standalone record.
- Ontology boundary: PASS
  - `GO:0090575` is modeled as `parent_structures` because GO reports it as
    the is-a parent for `GO:0000439`.
  - `GO:0000438` and `GO:0000440` are documented only in a resolved
    interpretation discussion because they are narrower context-specific
    portion terms, not broader parents or has-part targets.
  - No NEF3-specific Rad2 constituent or nucleotide-excision-repair process
    context leaked into this generic TFIIH core record.
- Component grounding: PASS
  - All seven TFIIH core protein classes named by `GO:0000439` are present:
    Ssl2/XPB, Tfb1/p62, Tfb2/p52, Ssl1/p44, Tfb4/p34, Tfb5/p8, and Rad3/XPD.
  - Every curated protein constituent uses
    `grounding_status: REVIEWED_LABEL_ONLY`; no InterPro, Pfam, NCBIfam,
    UniProtKB, Complex Portal, or similar accession was guessed.
  - The open component-grounding TODO anchors to all seven explicit component
    IDs.
- Evidence and scope: PASS
  - Definition and exact synonymy are sourced to `GO:0000439`.
  - Component composition and Saccharomyces cerevisiae scoping are sourced to
    the GO definition text.
  - Record-level parentage evidence for `GO:0090575` is included without
    over-curating unverified source-neutral protein family groundings.
- Graph and anchors: PASS
  - Every graph `component_ref` points to a local component row.
  - The assembly graph has exactly seven constituent-to-structure edges and
    stays nonmechanistic, with no unresolved assembly-order claim.
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
