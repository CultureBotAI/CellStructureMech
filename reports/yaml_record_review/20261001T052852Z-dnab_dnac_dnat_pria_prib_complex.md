# Adversarial YAML Record Review: DnaB-DnaC-DnaT-PriA-PriB complex

- PR: https://github.com/CultureBotAI/CellStructureMech/pull/1854
- Branch: `add-dnab-dnac-dnat-pria-prib-complex`
- Initial commit reviewed: `5e383a3c`
- Follow-up fix: `4ad1cda4`
- Review issue: https://github.com/CultureBotAI/CellStructureMech/issues/1855
- Record: `data/structures/other/dnab_dnac_dnat_pria_prib_complex.yaml`
- Initial history: `history/records/dnab_dnac_dnat_pria_prib_complex/2026-10-01T044751Z-codex-53f394.yaml`
- Validation-fix history: `history/records/dnab_dnac_dnat_pria_prib_complex/2026-10-01T050407Z-codex-f00ed4.yaml`
- Review-fix history: `history/records/dnab_dnac_dnat_pria_prib_complex/2026-10-01T051710Z-codex-db492e.yaml`
- Generated page: `pages/structures/other/dnab_dnac_dnat_pria_prib_complex.html`
- Reviewed at: `2026-10-01T05:28:52Z`

## Scope

Reviewed the PR diff for the new `GO:1990158` CellStructureMech record, its
append-only history entries, regenerated embedding artifacts, README updates,
and the rendered HTML/index pages.

## Adversarial Checks

- Identity and duplication: PASS
  - `GO:1990158` exactly denotes `DnaB-DnaC-DnaT-PriA-PriB complex`.
  - The hidden/ignored-inclusive duplicate search found no existing standalone
    DnaB-DnaC-DnaT-PriA-PriB complex record, `GO:1990158` record,
    `PMID:8663105`, or `DOI:10.1074/jbc.271.26.15649` match before creation.
  - Exact and related synonymy are carried with the GO-reported scopes:
    `DnaB-DnaC-DnaT-PriA-PriB preprimosome` as exact and `phi-X174-type
    preprimosome` as related.
  - Adjacent GO siblings for DnaB-DnaC-Rep-PriC and
    DnaB-DnaC-DnaT-PriA-PriC were treated as separate restart preprimosomes,
    not as duplicates.
- Ontology boundary: PASS
  - `GO:1990099` is modeled as `parent_structures` because OLS reports
    pre-primosome complex as the direct is-a parent of `GO:1990158`.
  - `GO:1990100` is modeled under `has_part` because GO:1990158 contains the
    grounded DnaB-DnaC helicase-loading subcomplex.
  - The record uses `NUCLEOPROTEIN_COMPLEX`, matching the GO definition's
    protein-DNA-complex scope.
  - The resolved boundary discussion leaves PriC-containing sibling complexes
    and DnaG-containing primosomes out of the GO:1990158 preprimosome record.
- Component grounding: PASS
  - The DnaB-DnaC subcomplex is grounded to `GO:1990100`.
  - DnaT, PriA and PriB use `grounding_status: REVIEWED_LABEL_ONLY`; no
    InterPro, Pfam, NCBIfam, UniProtKB or similar accession was guessed.
  - Primosome assembly site DNA is curated as the DNA constituent named by GO
    and the PhiX174 PAS evidence.
  - The open component-grounding TODO anchors to DnaT, PriA, PriB and the DNA
    component.
- Evidence and scope: PASS
  - Definition, synonymy, protein-DNA scope and DnaB-DnaC/PriA/PriB/DnaT/DNA
    identity are sourced to `GO:1990158`.
  - Pre-primosome parentage is sourced to OLS and represented by `GO:1990099`.
  - The DnaB-DnaC subcomplex is grounded to `GO:1990100` and cross-linked in
    both `has_part` and the component row.
  - Replication fork processing identity is sourced to `GO:0031297`.
  - Ng and Marians 1996 part I and II PubMed/DOI identifiers are included as
    primary PhiX174-type preprimosome assembly evidence without unsupported
    verbatim snippets.
- Graph and anchors: PASS
  - Every graph `component_ref` points to a local component row.
  - The DnaB-DnaC graph node is typed as `STRUCTURE`, matching its
    `GO:1990100` cellular-component grounding.
  - The graph stays nonmechanistic and does not claim ATPase cycling, DnaB
    transfer, DnaC release, PriC-containing alternatives or DnaG primase
    recruitment.
  - Discussion anchors are explicit `components#...` and
    `causal_graphs#...` anchors that resolve to local rows.
- Generated artifacts: PASS
  - The rendered structure page, `pages/index.json`, GO-grounded listing, OTHER
    category page, browse page, README corpus block, and root/browser text
    embedding artifacts include the added record.
- History: PASS
  - The append-only creation, validation-fix and review-fix history records
    target the new YAML file and validate against the vendored history schema.

## Findings

- https://github.com/CultureBotAI/CellStructureMech/issues/1855 - FIXED
  - The initial `dnab_dnac_complex` causal graph node had
    `node_type: GENE_OR_PROTEIN`, but that row represents the grounded
    `GO:1990100` DnaB-DnaC protein-complex substructure.
  - Fixed by changing the node to `node_type: STRUCTURE`, appending the
    `FIX_REVIEW_ISSUE` curation event, regenerating the rendered page, and
    adding `2026-10-01T051710Z-codex-db492e`.

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
