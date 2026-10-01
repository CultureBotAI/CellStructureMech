# Adversarial YAML Record Review: DnaB-DnaC complex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1850
- Branch: `add-dnab-dnac-complex`
- Initial commit reviewed: `5e338bbe`
- Follow-up fix: `e54f2d8b`
- Review issue: https://github.com/CultureBotAI/CellStructureMech/issues/1851
- Record: `data/structures/other/dnab_dnac_complex.yaml`
- Initial history: `history/records/dnab_dnac_complex/2026-10-01T024005Z-codex-126c85.yaml`
- Review-fix history: `history/records/dnab_dnac_complex/2026-10-01T030139Z-codex-776154.yaml`
- Generated page: `pages/structures/other/dnab_dnac_complex.html`
- Reviewed at: `2026-10-01T03:18:40Z`

## Scope

Reviewed the PR diff for the new `GO:1990100` CellStructureMech record, its
append-only history entries, regenerated embedding artifacts, README updates,
and the rendered HTML/index pages.

## Adversarial Checks

- Identity and duplication: PASS
  - `GO:1990100` exactly denotes `DnaB-DnaC complex`.
  - The hidden/ignored-inclusive duplicate search found no existing standalone
    DnaB-DnaC complex record or PMID/DOI match before creation.
  - GO synonymy is carried with the GO-reported scopes: `DnaB6-DnaC3 complex`
    and `DnaB6-DnaC6 complex` as narrow synonyms, and `helicase-loading complex`
    as a broad synonym.
- Ontology boundary: PASS
  - `GO:0032991` is modeled as `parent_structures` because OLS reports
    protein-containing complex as the direct is-a parent of `GO:1990100`.
  - The record stays at the bacterial DnaB-DnaC helicase-loading complex
    boundary instead of expanding into all primosome or prepriming-complex
    factors.
- Component grounding: PASS
  - The record has one DnaB helicase component and one DnaC helicase-loader
    component, matching the GO definition of the complex.
  - DnaB is given only the hexameric DnaB stoichiometry directly supported by GO
    and the primary paper; DnaC copy number remains unset because GO contains
    both `DnaB6-DnaC3 complex` and `DnaB6-DnaC6 complex` narrow synonyms.
  - Both protein constituents use `grounding_status: REVIEWED_LABEL_ONLY`; no
    InterPro, Pfam, NCBIfam, UniProtKB, Complex Portal, or similar accession was
    guessed.
  - The open component-grounding TODO anchors to both local component IDs.
- Evidence and scope: PASS
  - Definition, synonymy, component identity, and DnaC-mediated DnaB delivery
    are sourced to `GO:1990100`.
  - The GO parent assertion is sourced to `GO:0032991`.
  - DNA replication initiation function identity is sourced to `GO:0006270`.
  - The E. coli taxonomic row and canonical example are constrained to the
    species studied in PMID:20129058.
  - GO-cited PubMed and DOI identifiers are included as record-level evidence
    without unsupported verbatim snippets.
- Graph and anchors: PASS
  - Every graph `component_ref` points to a local component row.
  - The helicase-loading graph ties DnaB, DnaC, oriC, the complex, and DNA
    replication initiation together without claiming ATPase cycling,
    DnaC-release stoichiometry, or primase-triggered helicase activation
    mechanics.
  - Discussion anchors are field-level or explicit `components#...` anchors.
- Generated artifacts: PASS
  - The rendered structure page, `pages/index.json`, GO-grounded listing, OTHER
    category page, browse page, README corpus block, and root/browser text
    embedding artifacts include the added record.
- History: PASS
  - The append-only creation and review-fix history records target the new YAML
    file and validate against the vendored history schema.

## Findings

- https://github.com/CultureBotAI/CellStructureMech/issues/1851 - FIXED
  - The original `NCBITaxon:562` taxonomic-distribution row cited `GO:1990100`
    for the E. coli presence assertion. The GO term establishes the complex
    identity but does not itself directly justify species-level presence.
  - Fixed by replacing the taxonomic row reference with `PMID:20129058`,
    narrowing the note to the E. coli DnaB-DnaC helicase-loading experiment, and
    appending `2026-10-01T030139Z-codex-776154`.

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
