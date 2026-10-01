# Adversarial YAML Record Review: DnaB-DnaG complex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1852
- Branch: `add-dnab-dnag-complex`
- Commit reviewed: `55903067`
- Record: `data/structures/other/dnab_dnag_complex.yaml`
- History: `history/records/dnab_dnag_complex/2026-10-01T033828Z-codex-284f61.yaml`
- Generated page: `pages/structures/other/dnab_dnag_complex.html`
- Reviewed at: `2026-10-01T04:00:24Z`

## Scope

Reviewed the PR diff for the new `GO:1990156` CellStructureMech record, its
append-only history entry, regenerated embedding artifacts, README updates, and
the rendered HTML/index pages.

## Adversarial Checks

- Identity and duplication: PASS
  - `GO:1990156` exactly denotes `DnaB-DnaG complex`.
  - The hidden/ignored-inclusive duplicate search found no existing standalone
    DnaB-DnaG complex record or GO/PMID/DOI match before creation.
  - GO synonymy is carried with the GO-reported scope: `DnaB-DnaG primosome
    complex` as a related synonym.
- Ontology boundary: PASS
  - `GO:0033202` is modeled as `parent_structures` because OLS reports DNA
    helicase complex as the direct is-a parent for `GO:1990156`.
  - `GO:1990098` is modeled as `part_of` rather than as an is-a parent because
    OLS reports it as a distinct hierarchical parent and GO:1990098 denotes the
    DNA-containing core primosome complex.
  - The resolved interpretation discussion explicitly keeps the DnaB-DnaG
    protein complex separate from the broader core primosome.
- Component grounding: PASS
  - The DnaB and DnaG rows match the GO definition's homohexameric helicase and
    primase constituents.
  - DnaB is given only the hexameric stoichiometry named by GO; DnaG
    stoichiometry is explicitly scoped to the stabilized E. coli complex
    measured in PMID:14557266.
  - Both protein constituents use `grounding_status: REVIEWED_LABEL_ONLY`; no
    InterPro, Pfam, NCBIfam, UniProtKB, Complex Portal, or similar accession was
    guessed.
  - The open component-grounding TODO anchors to both local component IDs.
- Evidence and scope: PASS
  - Definition, synonymy, and DnaB/DnaG subunit identity are sourced to
    `GO:1990156`.
  - DNA helicase parentage is sourced to OLS and represented by `GO:0033202`.
  - Core-primosome parthood is sourced to OLS hierarchy plus the GO definitions
    of `GO:1990156` and `GO:1990098`.
  - DNA replication primer-synthesis function identity is sourced to
    `GO:0006269`.
  - The E. coli taxonomic row and canonical example are constrained to the
    species studied in PMID:14557266.
  - GO-cited PubMed and DOI identifiers are included as record-level evidence
    without unsupported verbatim snippets.
- Graph and anchors: PASS
  - Every graph `component_ref` points to a local component row.
  - The primer-synthesis graph has one edge from each curated protein
    constituent to the DnaB-DnaG complex and one function edge to DNA
    replication primer synthesis.
  - The graph stays nonmechanistic and does not claim DnaG binding kinetics,
    primase cycling, or interactions with DnaC and other replication factors.
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
