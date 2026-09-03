---
name: curate-yaml-record
description: Review and curate one CellStructureMech structure YAML record for structure identity, hierarchy and parthood, composition, taxonomic scope, function, evidence, completeness, and resolvable gaps. Use for a named record audit or improvement; do not use for bulk source ingestion, generated page edits, or as permission to spend credits, contact anyone, or mutate GitHub.
allowed-tools: Bash, Read, Grep, Glob, WebSearch, WebFetch, Edit, Write
metadata:
  category: curation
  requires_database: false
  requires_internet: true
  version: 1.0.0
---

# Curate one CellStructureMech YAML record

Produce a defensible `CellStructureRecord` and an explicit account of what is
supported, corrected, unresolved, and genuinely unknown. Search results and
research reports are leads; only inspected sources can support a claim.

## Boundaries

- Resolve one target under `data/structures/<category>/`. Stop and disambiguate
  when a label could denote a structure, component protein, phenotype, broader
  system, or specific multi-protein complex.
- Review/audit requests are read-only. Curate, improve, complete, correct, or
  add-evidence requests authorize local edits to the named record and the
  smallest necessary provenance/generated paths.
- Never edit generated `pages/`; edit the record or template and regenerate.
- Never launch paid research, contact anyone, or create/edit a GitHub item or
  outbound message without explicit authorization.
- Preserve unrelated work and use a dedicated branch/worktree.
- Never fill an optional field for coverage or infer false from absence.

## Read before judging the record

Read the full target plus:

- `CLAUDE.md`, `docs/CURATION.md`, and `docs/SCHEMA.md`;
- relevant `CellStructureRecord`, component, composition, function, taxonomic,
  image, evidence, causal-graph, discussion, and history classes in
  `src/cellstructuremech/schema/cellstructuremech.yaml`;
- `history/README.md` and the source-queue entry when relevant;
- [references/review-checklist.md](references/review-checklist.md).

Inspect parent/part records, linked TraitMech records, source-native ontology or
database records, and cited literature. Rendered pages and raw research notes
are not independent evidence.

## Workflow

### 1. Establish the baseline

Read the whole YAML. Record identifier, definition/source, category/kind,
parents, parthood, components/compositions, taxa, examples, functions, linked
traits, properties, images, evidence, graphs, discussions, datasets, status,
and history. Run:

```bash
just validate <record-path>
just validate-strict <record-path>
```

Use `just validate-products` and `just check-trait-links --check` when the
record's ontology and trait links are in scope. A green schema gate proves
shape, not biological correctness.

### 2. Verify structure identity and relations first

A record is a microbial cell structure, not a component protein or phenotype;
the finest supported unit is a multi-protein complex. Prefer a GO cellular-
component CURIE only when it denotes the exact structure. Otherwise retain a
CellStructureMech identity and use the broader term appropriately.

Verify `parent_structures` as is-a and `part_of`/`has_part` as parthood. Check
category, kind, replacements, xrefs, and canonical labels. Never guess a CURIE
or use a broader/related term as exact identity.

### 3. Review every scientific claim

Verify each component and stoichiometry, taxonomic-distribution statement,
canonical example, function, trait link, physical property, image attribution,
dataset, and causal edge against its exact source and context. Distinguish
source database assertions, primary experiments/imaging, reviews, predictions,
and search snippets.

Every composition item, function, taxonomic-distribution entry, image, and
causal edge must meet the evidence rules in `docs/CURATION.md`. Do not
generalize a protein family's presence into structure presence or one organism's
architecture to all taxa. Snippets are short verbatim source text.

### 4. Assess completeness and resolve supported gaps

Apply the checklist and use bounded searches for consequential gaps. Prioritize:

1. wrong structure identity, granularity, hierarchy, or parthood;
2. incorrect/unsupported components or complex composition;
3. overbroad taxonomic distribution or canonical examples;
4. unsupported function, trait, physical-property, or causal claims;
5. missing imaging/experimental provenance for material assertions.

Do not manufacture a component, function, taxonomic absence, or mechanism.
Add a discussion only for a concrete conflict or consequential curation task.

### 5. Write through the guarded path

Use a narrowly scoped mutator that asserts the target ID/path, calls
`cellstructuremech.curate.curation_event.record_curation_event` with
`llm_assisted=True`, and writes through
`cellstructuremech.validation.write_validated.write_validated_structure`.
Use `curator="claude"` when no curator identity was supplied; never attribute
agent judgement to the user.

Create an append-only repository history record with `just new-history`. Do not
add either event when content is unchanged. An LLM-authored record remains
`mapping_status: PROPOSED`; only a human curator may mark it REVIEWED.

### 6. Verify and report

```bash
just validate-strict <record-path>
just validate-history
just validate-products
just check-trait-links --check
just qc
git diff --check
git diff -- <record-path> history src scripts pages
```

If a record changed, run `just render` and include the checked generated output
when repository policy requires it. Re-read the YAML and confirm citations,
status, path/category, and both histories match the actual diff.

Report corrections/additions and sources, retained claims checked, unresolved
gaps and bounded searches, mapping status and human sign-off state, history
artifact, and all validation results.
