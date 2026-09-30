# Adversarial YAML Record Review: core TFIIH complex portion of NEF3 complex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1844
- Branch: `add-core-tfiih-nef3`
- Commit reviewed: `e4862bfa`
- Record: `data/structures/other/core_tfiih_complex_portion_of_nef3_complex.yaml`
- History: `history/records/core_tfiih_complex_portion_of_nef3_complex/2026-09-30T230440Z-claude-code-e07674.yaml`
- Generated page: `pages/structures/other/core_tfiih_complex_portion_of_nef3_complex.html`
- Reviewed at: `2026-09-30T23:24:12Z`

## Scope

Reviewed the PR diff for the new `GO:0000440` CellStructureMech record, its
append-only history entry, regenerated embedding artifacts, README updates, and
the rendered HTML/index pages.

## Adversarial Checks

- Identity and duplication: PASS
  - `GO:0000440` exactly denotes `core TFIIH complex portion of NEF3 complex`.
  - The hidden/ignored-inclusive duplicate search found no standalone
    `GO:0000440` record before creation; previous hits were the NEF3 parent
    record, generated pages, and resolver/report artifacts.
- Ontology boundary: PASS
  - `GO:0000439` is modeled as `parent_structures` because the new record is a
    TFIIH core complex portion.
  - `GO:0000112` is modeled as `part_of` because GO's part-of relationship
    places this portion inside the NEF3 complex.
  - Rad2 is intentionally excluded from `components` and documented in a
    resolved boundary discussion because Rad2 is a NEF3 partner outside the
    TFIIH core portion.
- Component grounding: PASS
  - All seven TFIIH core protein classes from `GO:0000439` use
    `grounding_status: REVIEWED_LABEL_ONLY`.
  - No InterPro, Pfam, NCBIfam, UniProtKB or Complex Portal accessions were
    guessed.
  - The open component-grounding TODO anchors to explicit component IDs.
- Evidence and scope: PASS
  - Definition and GO synonymy are sourced to `GO:0000440`.
  - TFIIH core composition is sourced to `GO:0000439`.
  - NEF3 parthood and S. cerevisiae NEF3 scope are sourced to `GO:0000112`
    and the existing Prakash and Prakash DOI.
- Graph and anchors: PASS
  - Every `component_ref` points to a local component row.
  - The nonmechanistic graph records only composition, NEF3 parthood, and broad
    nucleotide-excision-repair context.
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
- Text embedding drift check: PASS
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
