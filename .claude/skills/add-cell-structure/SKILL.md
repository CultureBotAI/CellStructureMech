---
name: add-cell-structure
description: Add a named microbial cell structure or organelle as a new CellStructureRecord YAML with exact identity, source-backed composition, canonical examples, functions, causal graphs, history, and generated pages. Use when the target structure is already named; use discover-cell-structures for broad literature searches.
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Add a CellStructureRecord

This skill turns one named, in-scope microbial structure into a validated
CellStructureMech record.

Use `discover-cell-structures` when the task is to search broadly for missing
structures or triage a literature lead. Use `literature-evidence` when the task
is to audit readability, propose verbatim snippets, or verify that a snippet is
actually present in a cited paper. Use `source-queue` for database or atlas
adoption.

## Read first

- `CLAUDE.md` for branching, mutation, history, and PR rules.
- `docs/CURATION.md` for record boundaries, identifiers, evidence, components,
  traits, causal graphs, and images.
- `docs/SCHEMA.md` for the available `CellStructureRecord` sections.
- `just report` for live corpus counts.
- The closest existing `data/structures/<category>/*.yaml` record, to copy
  local shape but not facts.

## Accept or reject

Add the structure only if it is a named subcellular entity in microbes:

- organelle, envelope layer, appendage, microcompartment, inclusion,
  cytoskeletal system, or multi-protein complex
- finest record no smaller than a multi-protein complex, unless a
  homo-oligomer forms a visually and biologically distinct structure
- at least one literature-backed component class
- at least one literature-backed function or assembly mechanism
- at least one real organism used as a canonical example

Reject single proteins, bare genes, pathways, phenotypes, broad placeholder
parents, storage compounds without an organized boundary, and host structures.
Record the reason in notes or in the response so the same near miss is not
re-triaged as an unknown.

## Prove it is new

Before writing a record, search exact identifiers and names across the whole
repository, including ignored and hidden files:

```bash
rg --no-ignore --hidden -n \
  "<GO CURIE>|<minted slug>|<label>|<synonym>|<core component>|<DOI>|<PMID>" \
  .
```

Search `identifier`, `xrefs`, `synonyms`, `has_part`, `part_of`,
`parent_structures`, `causal_graphs`, `discussions`, generated pages, history,
and `research/`. If a prior mention is only a rejection, read it before
continuing. Never search broad prefixes such as `DOI:10` or `GO:` to prove
absence.

## Identity

Prefer an exact GO cellular-component CURIE.

1. Check the GO label, synonyms, definition, and parents.
2. Use the GO CURIE only when it denotes exactly the structure being recorded.
3. If GO is broader than the structure, mint `cellstructuremech:<slug>` and put
   the broader GO term in `parent_structures` only when it is a true is-a
   parent.
4. Use `part_of` when the new record is a layer, subassembly, or substructure
   of an enclosing structure.

Never guess CURIEs. If a candidate GO, InterPro, Pfam, CHEBI, SO,
ComplexPortal, UniProtKB, or NCBITaxon accession has not been resolved at its
issuing authority, leave it out and add a `CURATION_TODO` discussion that says
what must be checked.

## Evidence bundle

Make the first record small but complete enough to stand alone:

- `definition`: GO for exact GO-grounded records, otherwise the paper that
  defines the structure
- `components`: taxon-agnostic protein, RNA, lipid, polysaccharide, or
  peptidoglycan classes; organism-specific UniProt accessions only in
  `protein_examples`
- `taxonomic_distribution`: clades and presence levels backed by a source,
  never inferred from one imaged strain
- `canonical_examples`: organisms actually studied in the cited papers
- `functions`: biological outputs, GO-grounded when an exact process or
  molecular function exists
- `causal_graphs`: at least one `MECHANISTIC` `ASSEMBLY` or `FUNCTION` graph
  with a citation on every edge
- `evidence`: record-level DOI or PMID references for the major review and
  canary primary papers

Use a review for broad scope and primary papers for at least one component,
canonical organism, or causal edge. Put only exact copied text in `snippet`;
put paraphrase and interpretation in `notes`.

## Causal graph

The first causal graph should be readable and source-bounded:

- 5 to 8 nodes for a known mechanism
- at least 5 directed edges when the mechanism supports them
- `component_ref` on every node that is one of the record's components
- final structure node grounded to the record identifier when the record has
  an exact ontology CURIE
- `subject`, `predicate`, `object`, `description`, and `evidence` on every
  edge
- `predicate_id` only when an exact relation CURIE has been curated

Generic states, capacities, and intermediates may stay ungrounded. Do not add
an edge just to make the graph look complete.

## Write the record

Create the skeleton with the validated scaffolder:

```bash
just new-record \
  --category <CATEGORY> \
  --kind <STRUCTURE_KIND> \
  --identifier <GO-or-cellstructuremech-CURIE> \
  --label "<label>" \
  --definition "<one-sentence definition>" \
  --definition-source <DOI-or-PMID-or-GO-CURIE> \
  --curator claude \
  --llm-assisted \
  --apply
```

Then fill the rest by loading the YAML with `yaml.safe_load`, appending a
`record_curation_event(..., llm_assisted=True)`, and writing it with
`write_validated_structure`. Do not hand-serialize YAML or loosen the
round-trip test if formatting drifts.

Set `mapping_status: PROPOSED` for every model-drafted record. Promotion to
`REVIEWED` is a human decision.

For every added record, create repository-level history:

```bash
just new-history \
  --kind record \
  --slug <slug> \
  --target-root data/structures/<category> \
  --event CREATE \
  --outcome changed \
  --sections identity,composition,taxonomy,functions,causal_graphs \
  --summary "<short summary>" \
  --details "<what was added and which sources justify it>" \
  --actor-name claude \
  --model <model> \
  --agent-tool claude-code
```

## Validate

Validate the new record directly with LinkML before broader gates:

```bash
uv run linkml-validate \
  -s src/cellstructuremech/schema/cellstructuremech.yaml \
  --target-class CellStructureRecord \
  data/structures/<category>/<slug>.yaml
```

Then run the checks whose scope LinkML does not cover:

```bash
just validate-strict --quiet data/structures/<category>/<slug>.yaml
just validate-history history/records/<slug>
just check-curies-strict
just validate-products
just render
just docs-stats
git diff --check
just qc
```

Also run `just evidence-verify` before committing a new `snippet`, and run
`just check-trait-links --check` after adding or editing `associated_traits`.

## Report

End with:

- new identifier, label, and file path
- strongest identity source and strongest mechanism source
- every DOI, PMID, CURIE, source accession, and taxon id added
- history record and generated pages
- validation commands that passed
- any `CURATION_TODO` left open
- whether duplicate/absence searches included ignored and hidden files
