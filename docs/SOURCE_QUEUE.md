# Data source queue

The prioritised list of external sources CellStructureMech draws on, what
each one feeds, and where we are with it. **This file is the queue**; the
research notes under `research/` are the evidence behind the ranking, and
issues track the work. Keep all three in step: when a source's status changes
here, link the PR or issue that changed it.

Ranking rule: (licence we can redistribute) × (per-item identifier) ×
(taxon linkage) × (what it feeds per unit of curator effort). A source that
fails on licence sinks regardless of the rest.

Status values: `DONE` (used in the corpus, pipeline exists) · `ACTIVE` (next
up, issue open) · `READY` (assessed, usable, not started) · `CAUTION` (usable
with a constraint that must be honoured) · `BLOCKED` (cannot use yet; reason
given) · `SKIP` (assessed, rejected; reason given).

## Queue

| # | Source | Feeds | Status | Constraint / next step | Evidence |
|---|---|---|---|---|---|
| 1 | **GO cellular component** | `identifier`, `parent_structures`, `part_of`, `functions` | DONE | Primary identifier; verify each CURIE against OLS (#6 wants this automated) | [note 1](../research/2026-08-29-imaging-evidence-sources.md) |
| 2 | **Wikimedia Commons** | `images` | DONE | Per-file licence from `extmetadata`; taxon via SDC `P180`→Wikidata `P685`; descriptive User-Agent; download-and-host | [note 2](../research/2026-08-29-remaining-sources.md), PRs #22 #33 |
| 3 | **UniProt Subcellular Location** | `xrefs`, `components.protein_examples` | ACTIVE | #28: add `SL-` xrefs, seed protein examples from `cc_scl_term` + `organism_id`, canary carboxysome / PCC 7942 | note 2 |
| 4 | **TraitMech** | `associated_traits` | DONE | Cross-repo id check wanted (#11) | — |
| 5 | **PMC open access (S3 bucket)** | `images` | READY | CC BY only (`license_code`); manual panel + taxon curation; never scrape pmc.ncbi.nlm.nih.gov | note 2 |
| 6 | **EMDB + EMPIAR** | `images`, `xrefs` (EMD ids), `physical_properties` | READY | EMPIAR CC0 but no taxon field — go through the EMDB cross-reference; extract frames, do not hot-link | note 1 |
| 7 | **Cell Image Library** | `images` | READY | Public Domain / CC BY records only; per-image DOI `10.7295/W9CIL…`; name→taxid lookup needed; API key by request | note 2 |
| 8 | **EcoCyc / BioCyc** | `components` (stoichiometry, *E. coli*) | CAUTION | Cite and link, do not redistribute; `getxml` works anonymously, ≤1 req/s | note 2 |
| 9 | **Complex Portal** | `components`, `xrefs` (*E. coli* K-12 complexes) | READY | Prokaryote coverage is *E. coli* only; verify accessions — one guessed CPX id was already retracted (#2) | note 1 |
| 10 | **Cell Structure Atlas / CaltechDATA** | `images` (link-only) | CAUTION | CC BY-NC: never host; DOI per video; no taxids on records | note 2, PR #33 |
| 11 | **BioImage Archive** | `images` | READY | Check licence per accession | note 1 |
| 12 | **SubtiWiki v5** | `components` (*B. subtilis*) | BLOCKED | No licence statement anywhere; ask the Stülke lab before copying | note 2 |
| 13 | **ETDB-Caltech** | `images` | BLOCKED | Unreachable since ≥2022-12; no licence; recheck quarterly | note 2 |
| 14 | **IDR** | `images` | CAUTION | Not uniformly open; per-study licence | note 1 |
| 15 | **MicrO** | `xrefs` | CAUTION | Inactive at OBO Foundry; static vocabulary only | note 1 |
| 16 | **NCIT** | — | SKIP | No prokaryotic structures, no GO xrefs | note 2 |

## Not yet assessed

PDB (as an `xrefs` / `physical_properties` source beyond single lookups),
KEGG BRITE cellular-structure hierarchies, Bacterial Cell Structure
literature atlases (e.g. Madigan-style textbook figure banks — likely
copyrighted), NIH BioArt (public domain illustrations, not evidence).
Add a row with status `READY`/`SKIP` once assessed, with a research note.
