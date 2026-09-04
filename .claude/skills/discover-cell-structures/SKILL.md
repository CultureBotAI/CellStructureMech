---
name: discover-cell-structures
description: Search the literature for microbial cell structures and organelles missing from CellStructureMech, verify identities and citations, and draft or add new CellStructureRecord YAML with sourced components, functions, examples, and causal graphs. Use when asked to find structures from papers, add records from papers, source new organelles, or expand the record backlog.
metadata:
  category: workflow
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Discover Cell Structures from Literature

This skill turns a literature lead into a scoped CellStructureMech record, or
rejects it with a reason a later curator can follow.

Its job is not to rank reusable bulk sources. Put database and atlas adoption
questions through `source-queue`. Its job is not to rubber-stamp existing
evidence text. Put snippet and readability audits through `literature-evidence`.
This workflow reads the literature directly, chooses whether a named structure
belongs in this corpus, verifies its identifiers, then writes a small,
evidence-backed `PROPOSED` record.

## Read these first

- `CLAUDE.md` - branch and curation workflow rules.
- `docs/CURATION.md` - record boundaries, identifier policy, evidence rules,
  components, causal graphs, and image constraints.
- `docs/SCHEMA.md` - the sections and classes available in a
  `CellStructureRecord`.
- `curation/source_queue.tsv` and `docs/SOURCE_QUEUE.md` - sources already
  adopted or deliberately rejected.
- `just report` - the live corpus shape. Do not quote counts from prose.
- The closest existing record under `data/structures/` - copy structure, not
  claims.

## Search pattern

Search to find structures, not just papers:

1. Start with GO cellular component terms.
   Use GO labels and definitions to distinguish structures from processes,
   phenotypes, proteins, and broad placeholder parents.
2. Search review literature with broad terms:
   `bacterial organelle`, `archaeal cell structure`, `proteinaceous organelle`,
   `microbial microcompartment`, `bacterial inclusion body`,
   `bacterial cytoskeleton`, `cell envelope ultrastructure`,
   `cryo-electron tomography bacterial cell`, and the candidate's synonyms.
3. Snowball from one readable review to primary papers for one canary organism,
   one core component, one function, and one mechanistic step.
4. Search the exact strings that would identify the candidate in this repository
   before writing anything: GO CURIE, label, synonyms, component names,
   canonical taxon, DOI, and PMID.

   ```bash
   rg --no-ignore --hidden -n \
     "<GO CURIE>|<label>|<synonym>|<component>|<taxon>|<DOI>|<PMID>" \
     .
   ```

Use `rg --no-ignore --hidden` or `rg -uu` whenever the result is meant to
prove a record, source, identifier, or citation is absent. Ignored reports,
research notes, generated pages, and history records still count as prior art.
Replace every placeholder with a candidate-specific term. Never search bare
identifier prefixes such as `DOI:10` or `PMID:` when proving absence; they match
unrelated literature citations throughout the repository.

## Candidate gate

Accept a candidate only when all of these are true:

- It is a **structure a microbiologist could name as a subcellular entity**:
  an organelle, envelope layer, appendage, microcompartment, inclusion,
  cytoskeletal system, or multi-protein complex.
- It is not merely a single protein, a gene, a pathway, a phenotype, a
  cellular process, a storage compound without an organized boundary, or a
  host-cell structure.
- The finest proposed record is no smaller than a multi-protein complex unless
  a homo-oligomer creates a visually and biologically distinct structure.
- Literature names at least one component class and at least one function or
  assembly mechanism.
- A real organism can be named as a canonical example, preferably from a
  primary paper that studied the structure directly.
- The candidate is not already represented as a record, synonym, `xrefs`,
  `has_part`, `part_of`, `parent_structures`, discussion, or research note.

Reject near misses explicitly in your notes. The common rejections are:

- **protein instead of structure** - record it as a `component` of the parent
  structure or leave it for ProteinTraitsMech.
- **phenotype instead of structure** - link the structure to TraitMech via
  `associated_traits`.
- **broad parent only** - use it in `parent_structures`, not as identity.
- **speculative one-off** - keep it in `research/` until component and function
  evidence exist.

## Identity

Prefer exact GO cellular component identity:

1. Search GO for the label and synonyms.
2. Read the GO definition and relationships. A matching label on a broader term
   is not enough.
3. Use the GO CURIE only when it denotes exactly the structure being recorded.
4. If no exact GO term exists, mint `cellstructuremech:<slug>`. Add a broader
   structure to `parent_structures` only when it is an exact is-a parent. Use
   `part_of` when the candidate is a component, layer, subassembly, or
   substructure of an enclosing cell structure.

Never guess a CURIE. If InterPro, CHEBI, SO, Complex Portal, UniProt, GO, or
NCBI Taxonomy cannot be resolved at the issuing authority, leave the field
empty and add a `CURATION_TODO` discussion that says what should be checked.

## Evidence bundle

New records need enough evidence to stand on their own:

- **definition** - GO for exact GO-grounded records; otherwise a paper that
  defines the structure.
- **components** - taxon-agnostic protein, RNA, lipid, polysaccharide, or
  peptidoglycan classes. Store organism-specific accessions only in
  `protein_examples`.
- **taxonomic_distribution** - clades and `presence` backed by a source, never
  inferred from one imaged strain.
- **canonical_examples** - the organisms actually studied in the cited papers.
- **functions** - biological outputs of the structure, preferably GO BP/MF
  grounded when exact.
- **causal_graphs** - at least one `MECHANISTIC` `ASSEMBLY` or `FUNCTION`
  graph with evidence on every edge.
- **evidence** - record-level DOI or PMID references for the major review and
  primary canary papers.

A review can establish broad scope. A primary paper should establish at least
one component, one taxon/example, or one edge in the first causal graph.

`snippet` is verbatim only. If you did not copy the exact text from a readable
source, put the paraphrase in `notes`.

## Causal graph expectations

The first graph should be small and checkable:

- 5 to 8 nodes.
- 5 or more directed edges when the mechanism is known.
- Every local component node uses `component_ref`.
- The final structure node carries `grounding` equal to the record identifier
  when the record has an exact ontology CURIE.
- Generic states, capacities, and intermediates can be ungrounded if no exact
  CURIE is curated.
- Every edge has `subject`, `predicate`, `object`, `description`, and
  `evidence`.
- Leave `predicate_id` empty unless an exact RO or BFO relation has been
  curated. A wrong formal predicate is worse than none.

Draw only what the source supports. It is better to omit a plausible edge than
to complete a mechanism from memory.

## Writing records

Use the scaffolder for a new file:

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

Replace `claude` with the human curator name when a person is directing the
edit, but keep `--llm-assisted` for any record whose prose or evidence summary
was drafted by a model.

Then fill the remaining sections through `write_validated_structure` and
`record_curation_event` so closed-mode validation happens before the file is
written and the inline `curation_history` entry is appended. Keep
`mapping_status: PROPOSED`; a human reviewer promotes records.

For every hand-curated target, also scaffold repository-level history:

```bash
just new-history \
  --kind record \
  --slug <slug> \
  --target-root data/structures/<category> \
  --event EDIT \
  --outcome changed \
  --sections <comma,separated,sections> \
  --summary "<short summary>" \
  --details "<what was added and which sources justified it>" \
  --actor-name claude \
  --model <model> \
  --agent-tool claude-code
```

## Validation

Validate the target record directly against the LinkML schema:

```bash
uv run linkml-validate \
  -s src/cellstructuremech/schema/cellstructuremech.yaml \
  --target-class CellStructureRecord \
  data/structures/<category>/<slug>.yaml
```

Then run the gates that catch what LinkML alone does not:

```bash
just validate-strict --quiet data/structures/<category>/<slug>.yaml
just validate-history history/records/<slug>
just evidence-verify
just check-curies-strict
just validate-products
just check-trait-links --check
just render
just docs-stats
git diff --check
just qc
```

Run `just evidence-verify` before committing any `snippet`. Run
`just check-trait-links --check` only after adding or editing
`associated_traits`. Run `just check-curies-strict` whenever a new DOI, PMID,
ontology term, UniProt accession, or source accession is written.

If `tests/test_write_validated.py::test_every_record_round_trips_byte_identically`
fails, re-emit or wrap the YAML to match `emit_structure_yaml`. Do not loosen
the test.

## Output

Report:

- accepted structures, their identifiers, and the strongest source for each
- rejected candidates and the exact boundary rule they failed
- every new DOI, PMID, CURIE, and taxon id
- files changed, including history records and generated pages
- the exact validation commands that passed
- unresolved curation todos left in the record

State whether all absence checks included ignored and hidden files.
