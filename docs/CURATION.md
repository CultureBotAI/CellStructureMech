# Curation rules

What is and is not a CellStructureMech record, how it is identified, and what
evidence each part must carry. The schema and tests enforce the checkable
parts; this text explains the judgements.

## What is a record

A record is a **structure a microbiologist would point to in an electron
micrograph or name as a subcellular entity**: an organelle, an envelope layer,
an appendage, a microcompartment, an inclusion, a cytoskeletal filament
system, or a multi-protein complex.

The granularity contract:

| Level | Example | Record? |
|---|---|---|
| Whole organelle / envelope layer | carboxysome, S-layer, thylakoid | **Yes** |
| Named sub-assembly with its own identity | flagellar motor, 30S subunit, carboxysome shell | **Yes**, linked by `part_of` / `has_part` |
| Multi-protein complex | ribosome, ATP synthase, T3SS injectisome | **Yes** — the finest-grained record |
| Single protein or protein family | FliC, MotB, RuBisCO large subunit | **No** — a `component` of a record; grounds to InterPro / UniProtKB and hands off to ProteinTraitsMech |
| Phenotype conferred by a structure | motile, flagellated, Gram-negative | **No** — a TraitMech record, linked via `associated_traits` |

When a complex is small enough to be described by one protein family (a
homo-oligomer such as a gas-vesicle wall), it is still a record if it forms a
distinct cellular structure. The test is whether the entity is a *thing in
the cell*, not how many gene products build it.

## Identifiers

1. **Use the GO cellular component term** when one denotes exactly this
   structure. `GO:0005840` ribosome, `GO:0009288` bacterial-type flagellum,
   `GO:0031470` carboxysome. Check the GO definition, not just the label.
2. **Mint `cellstructuremech:` otherwise**, and record the nearest broader
   term in `parent_structures`. Do not adopt a broader GO term as identity:
   grounding "anammoxosome" to `GO:0043231` intracellular membrane-bounded
   organelle would merge every such organelle into one record.
3. **Never reuse an identifier.** A superseded record stays in place with
   `mapping_status: DEPRECATED`; the successor names it in `replaces`.

`parent_structures` is is-a; `part_of` is parthood. The carboxysome *is a*
bacterial microcompartment and the flagellar hook *is part of* the flagellum.
Both must point at another record here or at a GO term; anything else fails
`tests/test_corpus_integrity.py`.

## Files

`data/structures/<category>/<slug>.yaml`, where `<category>` is the
lower-cased `structure_category` and `<slug>` is derived from the label by
`scripts/corpus.py:slugify`. A test checks the location matches the content,
so a record is moved by changing its category or label and renaming the file
to match — never one without the other.

## Evidence

- **Record-level `evidence` is optional** for GO-grounded records: the term
  carries provenance.
- **Every `function`, every `component.protein_examples` entry, and every
  causal-graph `edge` requires evidence.** These are curator-asserted claims
  nothing upstream vouches for.
- `snippet` is for **verbatim** quotes only. When you have not seen the
  source text, use `notes` to paraphrase what the source establishes. A
  fabricated quotation is worse than none.
- Prefer DOIs; PMIDs are fine. A reference the curator has not opened is not
  evidence.

## Components

- A component is a **taxon-agnostic family or class**: "flagellin", not
  "FliC of *Salmonella* Typhimurium". Organism-specific accessions go in
  `protein_examples`, paired with the taxon the role was established in.
- Ground proteins to InterPro / Pfam / NCBIfam, sub-complexes to ComplexPortal
  or GO, lipids and polysaccharides to CHEBI, RNAs to SO. **Do not guess an
  accession.** Leave `grounding` unset and open a `CURATION_TODO` discussion;
  a wrong CURIE is harder to find than a missing one.
- `grounding_status: REVIEWED_LABEL_ONLY` means a curator looked and no exact
  term exists. It requires `grounding_notes` saying why.
- `essentiality` is about whether *the structure* forms, not whether the cell
  lives.

## Trait links

`associated_traits` points at TraitMech / METPO CURIEs. The relation matters:
the flagellum `CONFERS` motility; the peptidoglycan layer is `DIAGNOSTIC_FOR`
the Gram-positive stain result. Verify the trait CURIE exists in TraitMech's
corpus before adding it.

## Causal graphs

Same node and edge vocabulary as TraitMech so tooling can be shared, plus a
`STRUCTURE` node type and a `component_ref` on nodes that are one of this
record's own components (kept in step by a test). `graph_kind` says whether
the graph explains ASSEMBLY, FUNCTION, REGULATION or DISASSEMBLY — a record
may carry one of each.

## Images

Every record should eventually show a micrograph. An `images` entry is a
claim like any other and carries its own provenance:

- **`licence`** (required). Hostable licences — CC0, public domain, CC BY,
  CC BY-SA — get a copy under `data/images/<category>/<slug>/` and a `file`
  entry (lowercase extension) plus its `file_sha256`; the renderer copies it
  to `pages/img/`. Anything else (CC BY-NC, ND, unknown) is **link-only**:
  leave `file` unset. Tests enforce both.
- **`attribution`** (required), exactly as the licence demands. For CC BY
  that is author(s) + licence + source.
- **`taxon_id`** (required) — the organism in the picture, which must already
  appear in `taxonomic_distribution` or `canonical_examples` (test-enforced);
  an image of a taxon the record does not mention is evidence for nothing.
- **`reference`** (required) — DOI or PMID of the paper the image comes from
  or is described in.
- **`retrieved_on`** — when you verified licence, attribution and taxon at the
  source. Read the licence off the source's machine-readable metadata (Commons
  `extmetadata`, PMC `license_code`), not off a re-hosting page.
- **Never scrape in bulk.** Fetch one image, check the file and its metadata,
  then the next. Prefer sources ranked in `research/`.

## Status

| `mapping_status` | Meaning |
|---|---|
| `SEEDED` | Generated from an upstream vocabulary; unread. |
| `PROPOSED` | Drafted from literature (by a person or an LLM); unread by a second curator. |
| `REVIEWED` | A human curator has checked identity, definition, composition and every citation. Requires `evidence` or `definition_source` and a `curation_history`. |
| `DEPRECATED` | Superseded; see `replaces` on the successor. |

An LLM-drafted record is `PROPOSED`, never `REVIEWED`, regardless of how
confident it reads. Every mutation appends a `CurationEvent` through
`cellstructuremech.curate.curation_event.record_curation_event`; set
`llm_assisted: true` when a model produced the change.
