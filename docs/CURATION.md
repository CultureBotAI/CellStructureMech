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

**The minted local part is a lowercase slug of the label at minting time** —
`cellstructuremech:mreb_filament`, the corpus's first mint. A slug needs no
allocator, so two curators cannot collide on a counter, and it reads in a URL.
The cost is that it looks stale if the preferred label later changes; that is
accepted, because rule 3 forbids renaming an identifier anyway. Before minting,
search GO properly: `MreB` and `bacterial actin cytoskeleton` return nothing,
which is what justified the mint, and `GO:0005856 cytoskeleton` — the whole
framework of any cell — is the parent, not the identity.

**An empty category is a fine result.** `OTHER` exists so a record that fits
nowhere has a home, and it is currently empty. Filling it to make a coverage
number move would mean placing a structure in a bucket that describes it worse
than a real category would.

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
- **Every definition, synonym, component, taxonomic-scope assertion, canonical
  example, function, trait link, physical property, `component.protein_examples`
  entry, and causal-graph `edge` requires a source or evidence.** These are
  curator-asserted claims nothing upstream vouches for. Image provenance is
  carried by its source accession and URL, licence, attribution, taxon, and
  (when one exists) publication reference.
- **A placeholder is not a source.** `definition_source` is required and its
  pattern rejects `TODO:`, `FIXME:`, `XXX:` and `TBD:` prefixes. For a
  GO-grounded record the term id is always an honest answer; for a minted one,
  a real citation is what justifies minting in the first place.
- `snippet` is for **verbatim** quotes only. When you have not seen the
  source text, use `notes` to paraphrase what the source establishes. A
  fabricated quotation is worse than none.
- **`just evidence-verify` checks every snippet against its own source** and
  fails on any that is not there. A reference no route could reach is reported
  as unchecked and does not fail the run — a network fault is not a finding
  about the corpus. A snippet that is present but differs in case, quote or dash
  style is reported as **not verbatim** rather than passed or failed: re-copy the
  exact characters from the source. It needs the network, so it is not part of
  `just qc`; run it before committing evidence. `just evidence-audit` reports
  which references are readable at all, and `just evidence-suggest <record>`
  offers candidate sentences to choose from — it never chooses. See the
  `literature-evidence` skill.
- Prefer DOIs; PMIDs are fine. A reference the curator has not opened is not
  evidence.
- **Unreadable is a finding.** If a cited paper's text cannot be reached, say so
  in `notes` and leave `snippet` empty. Do not paraphrase a title into prose
  that reads like knowledge of the paper's contents. Establish unreadability by
  trying the routes, not by asking one index: NCBI's converter covers only PMC,
  and reporting its silence as "no PubMed record" was wrong about a paper that
  has one (#133).

## Components

- A component is a **taxon-agnostic family or class**: "flagellin", not
  "FliC of *Salmonella* Typhimurium". Organism-specific accessions go in
  `protein_examples`, paired with the taxon the role was established in.
- **Where the boundary runs.** A component is normally a constituent — one of
  the proteins, RNAs, lipids or polysaccharides the structure is built from.
  It may *also* be machinery that binds the **assembled** structure to
  position, partition or maintain it (McdB on the carboxysome, the MamK/MamJ
  filament aligning magnetosomes); such a component is `DISPENSABLE`, since the
  structure forms without it. The converse does not hold — `essentiality` says
  only whether the structure assembles without the component, so a genuine
  constituent can be `DISPENSABLE` too (the flagellar stator: the flagellum is
  built without MotA/MotB, it just cannot turn). **`component_role` carries the
  distinction** — `CONSTITUENT` or `ASSOCIATED_MACHINERY` — and is required, so
  a consumer asking what a structure is made of can filter on it. Machinery can
  never be `ESSENTIAL`; a test enforces that. A protein that acts on a **subunit before
  assembly** and then departs is **not** a component — the RuBisCO folding
  chaperone RbcX is the worked example. Its localisation annotation says where
  it acts, not what it belongs to.
- **Record a decline, don't just omit it.** When a source annotates a protein
  to the structure and you judge it out of scope, add a `RESOLVED` discussion
  saying why (see `rbcx_not_a_component` on the carboxysome). Otherwise the
  next seeding run reports it as a gap again and the reasoning is lost.
- **Colours come from tokens, in every stylesheet.** `tests/test_stylesheet_contract.py`
  refuses an undefined-token fallback, a duplicated selector, a colour literal
  outside a token block, and a token declared in one theme block but not the
  other — across `style.css` and every inline `<style>` a template ships. It
  carries mutation tests: each check is exercised against a stylesheet broken
  in exactly the way it exists to catch, because CSS never reports a failure
  and a contract that has only run against a passing file proves nothing.
- **A trait link is a claim about another repository**, so it is checked there:
  `just check-trait-links --check` confirms the CURIE is a TraitMech record and
  that its label still matches. A drifted label is the cross-repo form of the
  id-label defect — the CURIE resolves and the record says something TraitMech
  no longer says (#11).
- **Every identifier is resolved, not read.** `just check-curies-strict` resolves
  each DOI (Crossref, then DataCite), PMID, UniProt accession, InterPro and
  Complex Portal id and ontology term at the authority that issued it, and the
  resolvers themselves are exercised against a known-good and known-bad id
  first — a resolver pointed at a retired endpoint reported every accession as
  missing (#82). It runs in its own workflow, not `just qc`, because it needs
  the network, and weekly on a schedule because an identifier can be withdrawn
  long after it was written.
- Ground proteins to InterPro / Pfam / NCBIfam, sub-complexes to ComplexPortal
  or GO, lipids and polysaccharides to CHEBI, RNAs to SO. **Do not guess an
  accession.** Leave `grounding` unset and open a `CURATION_TODO` discussion;
  a wrong CURIE is harder to find than a missing one.
- `protein_examples` can be seeded from UniProt Subcellular Location
  (`just uniprot-proteins <record> --taxon <id>`): reviewed entries in a
  canonical taxon, matched to a component by gene symbol, carrying UniProt's
  `ECO:0000269` PubMed evidence for the localisation. Proteins the script
  reports as *no matching component* are candidates for new components.
- `grounding_status: REVIEWED_LABEL_ONLY` means a curator looked and no exact
  term exists. It requires `grounding_notes` saying why.
- `essentiality` is about whether *the structure* forms, not whether the cell
  lives.

Complex Portal imports are a second, deliberately separate layer:

- `components` remains the curated, taxon-agnostic model.
- `complex_compositions` preserves one source's organism-specific UniProt /
  RNAcentral participants and copy numbers without pretending those accessions
  define a family across taxa.
- Resolve an exact `CPX-N` through `scripts/complex_portal.py`; do not apply a
  search result or add it to `xrefs` unless it is genuinely equivalent to the
  entire record. A required scope note says whether the entry is the whole
  record or a subassembly.

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
  entry (lowercase extension) plus its `file_sha256`. The image is served
  from `data/images/` where it is committed — GitHub Pages publishes the
  repository root, so copying it into `pages/` only stored it twice (#31).
  A hosted image must be under 2 MiB and the set under 20 MiB (#26): the caps
  are generous, and exist so a large upload is a decision rather than an
  accident. Anything else (CC BY-NC, ND, unknown) is **link-only**:
  leave `file` unset. Tests enforce both.
- **`attribution`** (required), exactly as the licence demands. For CC BY
  that is author(s) + licence + source.
- **`taxon_id`** (required) — the organism in the picture, which must appear in
  **`canonical_examples`** (test-enforced). An image of a taxon the record does
  not mention is evidence for nothing; and it belongs there rather than in
  `taxonomic_distribution`, because satisfying the rule from the distribution
  produced rows like "E. coli O157:H7 — UNIVERSAL", a presence value that is
  meaningless for one strain (#36). A canonical example carries a note and a
  citation instead of a presence, which is what an imaged strain needs.
- **`reference`** (recommended) — DOI or PMID of the paper the image comes
  from or is described in. Decision #30: the source record
  (`source_accession` + `source_url`) is an acceptable citable identifier on
  its own — Cell Image Library mints a DOI per image, CDC PHIL an image id —
  so a reference-free public-domain micrograph is allowed. Prefer images
  that have both, and never invent a reference to satisfy the field.
- **`retrieved_on`** — when you verified licence, attribution and taxon at the
  source. Read the licence off the source's machine-readable metadata (Commons
  `extmetadata`, PMC `license_code`), not off a re-hosting page.
- **Never scrape in bulk.** Fetch one image, check the file and its metadata,
  then the next. Prefer sources ranked in `research/`.

Source-specific commands (all dry-run unless `--apply` is present):

- `scripts/emdb_empiar.py image` records the CC0 raw EMPIAR dataset and the
  small linked EMDB depositor figure. The EMDB `natural_source` taxon must
  already be present on the record; reconstruction resolution is image
  provenance, not a biological `physical_property`.
- `scripts/pmc_oa.py image` reads current-version metadata, JATS and media from
  `pmc-oa-opendata`. Only CC BY/CC0 is hostable, and the exact CC version must
  be present in JATS and agree with the metadata family. The curator supplies
  the caption-derived taxon and explicitly acknowledges likely multi-panel figures.
- `scripts/cell_image_library.py` reads one CIL item's DOI, exact licence,
  attribution and source-hosted preview from public JSON-LD. It accepts only
  Public Domain and CC BY 3.0/4.0 items. CIL supplies an organism name but no
  machine-readable taxid there, so the curator supplies a taxon already present
  on the target record.
- `scripts/bioimage_archive.py` accepts direct `S-BIAD` submissions only after
  reading their per-accession CC0/CC BY 4.0 statement. It resolves one exact
  file through the study-component manifests and checks the downloaded byte
  count. Archive TIFF channels must be named by the manifest and selected
  explicitly; the selected plane is exported losslessly to a site-ready PNG.
- `scripts/micro_xrefs.py` adds only curator-reviewed identity mappings from
  current GO-grounded records to exact, non-obsolete MicrO terms. MicrO is
  inactive and mixes structures with whole cells and qualities, so the adapter
  has a fixed allow-list and refuses label search or inferred mappings.
- `scripts/subtiwiki.py` is CURATE_ONLY because SubtiWiki publishes no database
  redistribution licence. It reads one exact category and exact per-gene
  UniProt outlinks for a fixed reviewed allow-list, then independently checks
  the accession, reviewed status, current primary gene and strain taxon at
  UniProtKB. Only identifiers and source links enter the corpus: descriptions,
  sequences, phenotypes, interaction text and bulk exports are refused. The
  historical SubtiWiki names `flgE`, `motP` and `motS` are explicitly reconciled
  to current UniProt primaries `flgG`, `ytxD` and `ytxE` rather than silently
  treated as exact symbol matches; primary literature independently supports
  the MotP/MotS stator placement.
- `scripts/psortdb.py` is CURATE_ONLY because the PSORTdb paper says Creative
  Commons without identifying the database licence or version. The maintainer
  explicitly accepts responsibility for using this public source under that
  narrow boundary. The adapter reads only a pinned ePSORTdb artifact, whose
  nominal TSV is actually a Safari WebArchive containing an HTML-wrapped table,
  and selects one exact experimental accession/PMID canary. It stores only the
  third-party UniProt identifier and evidence links, independently verifies the
  reviewed accession, gene and strain taxon at UniProtKB and the PMID at NCBI,
  and never reads cPSORTdb predictions or copies bulk prose.
- `scripts/interpro_groundings.py` resolves exact UniProt accessions through
  InterPro's combined endpoint, accepts only integrated entries whose type is
  `family`, and requires every protein response to be reviewed. Its fixed
  curator-reviewed allow-list must have an unchanged family consensus across
  all component scope examples. Domains and homologous superfamilies are never
  promoted to family groundings; combined alpha/beta-carboxysome components and
  MamK/MamJ are recorded as `REVIEWED_LABEL_ONLY` when their families differ.
- `scripts/cryoet_data_portal.py` resolves fixed, curator-reviewed dataset,
  run and annotation identifiers through the official GraphQL endpoint. It
  requires an exact NCBI taxon already asserted by the target record and either
  an exact dataset `cellComponentId` or exact annotation `objectId`. Annotation
  method, ground-truth and curator-recommendation status remain explicit. The
  adapter stores only lightweight metadata and landing-page links; it neither
  requests nor hosts tomograms or annotation volumes.
- `scripts/rcsb_pdb.py` resolves a fixed experimental PDB entry plus every
  explicitly enumerated polymer entity and biological assembly through the
  official RCSB Data API. It requires the exact source NCBI taxon to be already
  asserted by the target record, and retains the primary DOI/PMID, method,
  resolution, EMDB accession and entity-to-UniProt links. RCSB can expose
  alternate global, pseudo and local assembly stoichiometries, so the adapter
  verifies their continued presence but leaves them unflattened at the linked
  assembly endpoint. It stores no coordinates and does not treat the RCSB
  molecular render as a micrograph.
- These image scripts verify downloaded bytes (PMC md5 where supplied, corpus
  SHA-256 always), validate the complete record mutation before touching the
  destination, and confine generated filenames to the record image directory.

## Text embedding map

The text map is a derived discovery aid, not curated evidence. Its stable input
contains a record's name, definition, synonyms, category/kind, canonical
component labels and roles, functions, taxonomic scope, and physical-property
context. It deliberately excludes identifiers, citations, images, curation
history, taxon-specific `complex_compositions`, and protein examples so source
verbosity does not masquerade as biological similarity.

`just text-embeddings-refresh` runs the model- and library-version-pinned
`sentence-transformers/all-MiniLM-L6-v2` model locally and commits one vector per
record. Each labelled line is embedded independently, then the unit vectors are
mean-pooled so the model's input-length limit cannot silently drop later
components. No corpus text is sent to an external embedding service. The normal
`just text-map` command uses the cache to rebuild a two-dimensional PCA view and
full-vector cosine neighbours without network or model dependencies.

`just text-map-check` is blocking in QC: exact record coverage, semantic-text
SHA-256, model/revision/dimension, coordinates, and neighbour scores must all be
current. PCA is used because the corpus presently has too few records for a
stable nonlinear layout. The map explicitly warns that its two-dimensional
distances are lossy. The derived-file comparison tolerates only tiny floating-
point differences from platform BLAS implementations.

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
