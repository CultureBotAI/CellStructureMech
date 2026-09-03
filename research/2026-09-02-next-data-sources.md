# Next data-source discovery (2026-09-02)

This pass searched for genuinely new sources after InterPro, CryoET Data Portal,
RCSB PDB, and PSORTdb had all been adopted. It deliberately excludes aliases,
mirrors, and sources already represented in `curation/source_queue.tsv`.

The 19-record baseline remains sparse where another source can help: only four
records contain protein examples, four contain datasets, five contain images,
one contains a complex composition, ten contain physical properties, and nine
contain causal graphs. The source ranking below favours exact identifiers,
organism linkage, primary evidence, and a representation that fits the schema
without turning predictions or associations into experimental facts.

All live checks used official project sites, APIs, downloads, or documentation.
Licensing decisions remain the downstream user's responsibility; the queue
still records what the source says and limits the proposed integration so that
the corpus does not silently overstate either rights or evidence.

## Verdict

| Rank | Source | Best use | Exact live result | Decision |
|---|---|---|---|---|
| 1 | **PRIDE Archive** | structure-specific proteomics `datasets` | search returned three public *Bacillus subtilis* spore datasets, including spore-coat experiment `PXD004473` with PMID `27790212` | **Candidate; ingest next** |
| 1 | **SwissBioPics** | reusable explanatory `images` | taxon/GO endpoint for `NCBITaxon:224308` + `GO:0009288` returned an SVG with the bacterial flagellum highlighted, embedded creator and CC BY 4.0 metadata | **Candidate; ingest next** |
| 1 | **NCBIfam** | exact protein-family `components` grounding | current model index contains exact NCBIFAM models for CcmN, MamK, magnetosome proteins, encapsulin shells, and gas-vesicle proteins | **Candidate; ingest next** |
| 2 | **IntAct** | experimentally observed component-interaction `evidence` | `UniProtKB:P23447` (FliF) returned an exact taxon-224308 physical association with YabT, PMID `25374563`, PSI-MI method/type, IntAct and IMEx ids | **Candidate; curate semantics carefully** |
| 2 | **MemProtMD** | membrane-complex simulation `datasets` and diagrams | exact `PDB:6OQR` page supplies coarse-grained and atomistic *E. coli* ATP-synthase membrane simulations, analyses and downloads | **Candidate; schema extension needed** |
| 3 | **QuickGO / GOA** | experimental protein localisation evidence | robust API and bulk annotation access, but it is an evidence lane for the already adopted GO source rather than a new source identity | **Extend existing GO; no new queue row** |
| 3 | **BacDive** | canonical strain identifiers and morphology | exact DSM 402 lookup resolves BacDive 1156 / *B. subtilis* 168 / `NCBITaxon:224308`, but its `Morphology` object is empty | **Defer; no present structure gain** |
| 4 | **BioGRID** | physical-interaction cross-checks | open bulk organism files and detailed experimental fields are available, but coverage substantially overlaps IntAct and the REST API needs a key | **Defer behind IntAct** |
| 4 | **OPM** | computed membrane placement and thickness | public API/bulk downloads expose membrane orientation data, but the current corpus can already reach OPM annotations through RCSB and an official licence statement was not located | **Extend RCSB or reassess later** |
| 5 | **STRING** | discovery of candidate associations | API and CC BY bulk data are strong operationally, but scores mix prediction, text mining, indirect functional association, and imported databases | **Reject as assertion evidence** |
| 5 | **AlphaFold DB** | predicted protein structures | over 200 million CC BY models are available by UniProt accession, but they neither establish structure membership nor represent experimental structures | **Reject for current schema/use** |

## 1. PRIDE Archive — highest-value dataset candidate (#177)

PRIDE already appears in `StructuralDatasetRepositoryEnum`, and `PROTEOMICS` is
already a supported dataset type, so this candidate does not require a schema
change. The official API offers project search and exact-accession endpoints
with organism, publication, submission type, protocol, keyword, and file
metadata. A public search for `Bacillus subtilis spore` returned:

| Accession | Project | Organism/publication |
|---|---|---|
| `PXD004473` | The influence of sporulation medium on the spore coat protein composition | *B. subtilis* subsp. *subtilis*; PMID `27790212` |
| `PXD002559` | Phosphoproteome dynamics during bacterial-spore revival | *B. subtilis*; PMID `26381121` |
| `PXD051727` | Proteomics of mature spores in wild-type and `mdfA` deletion strains | *B. subtilis* PY79; PMID `40086876` |

`PXD004473` is the clean first canary because its experimental object is the
spore coat itself, not merely a whole-cell proteome. Add it as a lightweight
dataset reference on the endospore record; do not infer that every identified
protein is a constitutive coat component. Protein-level promotion requires the
paper's analysis and a curator decision.

ProteomeXchange's current published guidance says released public data are
intended for unrestricted dissemination and reuse, while PRIDE follows the
EMBL-EBI Terms of Use and preserves submitter ownership. That does not map
cleanly to the queue's Creative-Commons-oriented redistribution enum. The queue
therefore proposes identifier-only `REFERENCE` use and records the terms as
`UNVERIFIED`; it is not a claim that the public files are closed.

## 2. SwissBioPics — deterministic, accessible diagrams (#176)

SwissBioPics is an expert-curated library of SVG cell images. Its official help
page states that the images are CC BY 4.0 and that its API chooses an image from
an NCBI taxonomy id plus GO cellular-component or UniProt subcellular-location
ids. The official web component documents the exact endpoint shape.

The live request
`https://www.swissbiopics.org/api/224308/go/0009288` returned an SVG for the
*B. subtilis* 168 taxon context. It contains a group with
`class="subcellular_location subcell_present GO9288"`, label `Bacterial
flagellum`, creator `Philippe Le Mercier`, and an embedded CC BY 4.0 licence
link. This is much stronger provenance than a generic illustration found by
image search.

The first adapter should store the returned SVG and exact request URL, require
embedded creator/licence metadata, and verify that the requested GO class is
marked `subcell_present`. It must label the item as a diagram, not microscopy,
and retain that the drawing is a taxon-selected archetype rather than an image
of strain 168.

## 3. NCBIfam — targeted family grounding (#174)

NCBI's Protein Family Models database publishes the current PGAP HMM index and
model files. The 2026-06-25 `hmm_PGAP.tsv` index identifies each model's source,
family type, naming/structural-annotation flags, GO terms, PMIDs, taxonomic
range, and RefSeq hit count. The mixed collection contains Pfam, TIGRFAM, PRK,
and NCBIFAM records, so an adapter must filter `source == NCBIFAM` rather than
claiming the whole archive as NCBI-authored NCBIfam content.

Exact current-corpus canaries include:

| Model | Product | Useful target |
|---|---|---|
| `NF053793.1` | beta-carboxysome scaffolding protein CcmN | carboxysome `assembly_adaptor` |
| `NF040964.1` | MamK family actin-like protein | magnetosome `mamk_filament` after splitting the current MamK/MamJ scope |
| `NF041155.2` | family 1 encapsulin nanocompartment shell protein | encapsulin `shell` |
| `NF033616.1` | magnetosome biogenesis CDF transporter MamB | a future exact MamB protein component |
| `NF038051.2` | magnetosome protein MamC | a future exact MamC protein component |
| `NF045778.1` | gas vesicle protein GvpL | future expansion of gas-vesicle accessory components |

The NCBI policy says it places no restrictions on molecular data, while warning
that some records can contain material supplied by third parties. Keep only the
NCBIFAM subset and write the NF CURIE, not model prose. As with InterPro, exact
family scope must agree with the component and its reviewed protein examples;
the source is not permission to ground combined or underspecified components.

## 4. IntAct — useful interaction evidence, not causality

IntAct distributes experimentally derived molecular interactions through bulk
PSI-MI files, PSICQUIC, and web services. The official download page states
that the data and software are available under Apache 2.0. Records include
stable IntAct/IMEx ids, participant identifiers, NCBI taxids, PMID, PSI-MI
method, interaction type, roles, and feature ranges.

The exact PSICQUIC query for `UniProtKB:P23447` returned FliF from
`NCBITaxon:224308` physically associated with YabT (`UniProtKB:P37562`), PMID
`25374563`, interaction `EBI-9304566`, experiment `MI:1112` (two-hybrid prey
pooling), and type `MI:0915` (physical association). That is useful supporting
evidence around the flagellar MS ring, but it is not proof that YabT is a
structural constituent and is not a directed causal edge. An adapter must
preserve the assay, roles, taxon, PMID, interaction type, and n-ary semantics;
it should propose evidence for curator review rather than write composition.

The queue currently calls this `REFERENCE` use because the record model has no
lossless interaction object and the queue's redistribution enum cannot express
Apache-style notice terms precisely.

## 5. MemProtMD — valuable computational context

MemProtMD provides HTTP/API access to simulations of experimentally determined
membrane-protein structures in lipid bilayers. Its pages and downloads are CC
BY 4.0. The exact `PDB:6OQR` page describes *E. coli* ATP synthase simulations
at coarse-grained and atomistic resolution and exposes snapshots, simulation
inputs, membrane-distortion analyses, lipid/solvent contacts, and renders.

This complements RCSB rather than replacing it. The simulation can show a
specific assembly embedded in a model membrane and provide computed lipid
context; it must never be described as a new experimental structure or a
measured membrane thickness. Adoption should first add explicit
`COMPUTATIONAL_SIMULATION` / `MEMPROTMD` enum values (or an equivalent lossless
model) instead of hiding the source under `OTHER`.

## Sources reviewed but not queued

- **QuickGO / GOA:** every annotation has a GO term, evidence and reference;
  the API and monthly taxon files are excellent for evidence-filtered protein
  examples. This should extend the existing `go` adapter with exact
  experimental evidence codes and `NOT` exclusion, not create a duplicate
  source row.
- **BacDive:** the v2 API no longer requires registration and provides stable
  strain ids, taxonomic identifiers, culture collection links and literature.
  The exact DSM 402 record resolves the canonical strain correctly, but its
  morphology section is empty, so it adds no defensible structure assertion
  today.
- **BioGRID:** the latest release offers organism-separated MIT-licensed bulk
  files with experiment, PMID and taxon fields. It is a useful independent
  cross-check after IntAct, but not the first integration because its evidence
  model overlaps IntAct and API access requires a key.
- **OPM:** placement of PDB structures in membranes and computed hydrophobic
  thickness could be useful physical context. Prefer the OPM links already
  exposed through RCSB until an official reuse statement and a non-duplicative
  corpus representation are verified.
- **STRING:** although bulk/API data are CC BY 4.0, the resource intentionally
  combines known and predicted functional associations, text mining and other
  databases. STRING scores must not become experimental composition or causal
  assertions.
- **AlphaFold DB:** predicted models are CC BY 4.0 and easy to resolve by
  UniProt accession, but model confidence is not evidence that a protein is a
  component. The current schema also deliberately distinguishes experimental
  structures and has no predicted-structure lane.

## Recommended implementation order

1. PRIDE adapter for `PXD004473`, storing a lightweight dataset reference and
   validating accession, organism, publication, and project title.
2. SwissBioPics adapter for the exact flagellum SVG canary, including embedded
   licence/creator and requested-GO checks.
3. NCBIfam grounding adapter beginning with `NF053793.1` for CcmN; filter the
   current model index to NCBIFAM and fail closed on component-scope mismatch.
4. Design an interaction evidence object before integrating IntAct.
5. Extend dataset enums before integrating MemProtMD simulations.

## Primary sources and worked endpoints

PRIDE: [API guide](https://www.ebi.ac.uk/pride/ws/archive/v2/docs/api-guide.html) ·
[worked project `PXD004473`](https://www.ebi.ac.uk/pride/archive/projects/PXD004473) ·
[ProteomeXchange licence guidance](https://www.proteomexchange.org/docs/guidelines_px.pdf) ·
[EMBL-EBI licensing policy](https://www.ebi.ac.uk/licencing/)

SwissBioPics: [help, API summary and licence](https://www.swissbiopics.org/help) ·
[worked taxon/GO SVG](https://www.swissbiopics.org/api/224308/go/0009288) ·
[resource paper](https://doi.org/10.1093/database/baac026)

NCBIfam: [about Protein Family Models](https://www.ncbi.nlm.nih.gov/Structure/protfam/about.html) ·
[data access](https://www.ncbi.nlm.nih.gov/Structure/protfam/data_access.html) ·
[current model index](https://ftp.ncbi.nlm.nih.gov/hmm/current/hmm_PGAP.tsv) ·
[NCBI policies](https://www.ncbi.nlm.nih.gov/home/about/policies/)

IntAct: [user guide](https://www.ebi.ac.uk/intact/documentation/user-guide) ·
[downloads and terms](https://www.ebi.ac.uk/intact/download/ftp) ·
[worked FliF PSICQUIC query](https://www.ebi.ac.uk/Tools/webservices/psicquic/intact/webservices/current/search/query/P23447?format=tab27&firstResult=0&maxResults=10)

MemProtMD: [home](https://memprotmd.bioch.ox.ac.uk/home/) ·
[API](https://memprotmd.bioch.ox.ac.uk/api/) ·
[worked `PDB:6OQR` simulation](https://memprotmd.bioch.ox.ac.uk/_ref/PDB/6oqr/)

Other decisions: [QuickGO API](https://www.ebi.ac.uk/QuickGO/api/) ·
[GO annotation downloads](https://geneontology.org/docs/download-go-annotations/) ·
[BacDive API](https://api.bacdive.dsmz.de/) ·
[BioGRID downloads](https://downloads.thebiogrid.org/BioGRID/Latest-Release/) ·
[BioGRID REST documentation](https://wiki.thebiogrid.org/doku.php/biogridrest) ·
[OPM downloads](https://opm.phar.umich.edu/download) ·
[STRING API](https://string-db.org/help/api/) ·
[STRING access terms](https://www.string-db.org/cgi/access?footer_active_subpage=usage) ·
[AlphaFold DB](https://www.alphafold.ebi.ac.uk/) ·
[AlphaFold DB licence](https://alphafold.ebi.ac.uk/assets/License-Disclaimer.pdf)
