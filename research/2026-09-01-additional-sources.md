# Additional source discovery (2026-09-01)

This pass looked for sources that close measured gaps in the current 19-record
corpus rather than adding another general catalogue. The baseline has 67
components, of which only 5 have a grounding; 55 are ungrounded without a
completed `REVIEWED_LABEL_ONLY` decision, including 32 protein components. Only
one record has a `datasets` assertion and five have images.

The live checks below used official licence pages and programmatic endpoints on
2026-09-01. Counts are dated observations, not promises about future coverage.

## Verdict

| Rank | Source | Best use | Rights | Live result | Decision |
|---|---|---|---|---|---|
| 1 | **InterPro** | exact protein-family groundings for `components` | downloadable InterPro data are CC0 1.0 | exact families for five representative protein examples on ungrounded components; reviewed negative controls exposed missing and scope-conflicting matches | **Candidate; ingest next** |
| 2 | **CryoET Data Portal** | taxon-linked cryo-ET `datasets` and structure annotations | public submissions are CC0 | 8 exact dataset-level GO matches; thousands of relevant annotation records | **Candidate** |
| 2 | **RCSB PDB** | experimentally determined structural `datasets` | archive and API data are CC0 | exact microbial flagellar-ring, ribosome and ATP-synthase canaries with DOI, taxon and entity links | **Candidate** |
| 4 | **PSORTdb** | experimentally supported protein-localisation examples | paper says Creative Commons but does not name the licence/version | useful TSV fields, but the live v4 download is wrapped in a binary Apple WebArchive instead of being a clean TSV | **Blocked** |

## 1. InterPro — ingest next (#122)

### Why it closes a real gap

The schema already names InterPro/Pfam/NCBIfam as the preferred grounding for a
protein family, and strict CURIE checks already know how to resolve InterPro
identifiers. What is missing is an exact-accession adapter and a reviewed mapping
layer. This is a smaller integration than either imaging source and addresses 32
currently unreviewed, ungrounded protein components.

InterPro's official licence page says downloadable InterPro, Pfam, PRINTS and
SFLD data on the site are CC0 1.0. Its REST API exposes combined entry, protein,
structure, taxonomy and proteome endpoints, so a known UniProt accession can be
resolved to integrated InterPro families without label search.

### Live canaries

The combined endpoint
`/entry/interpro/protein/uniprot/<accession>/?page_size=200` returned:

| Current component / example | Exact integrated family result |
|---|---|
| flagellin / `UniProtKB:P02968` | `InterPro:IPR001492` Flagellin |
| carboxysome BMC-H / `UniProtKB:Q03511` | `InterPro:IPR046380` Carboxysome shell protein CcmK |
| carboxysome BMC-P / `UniProtKB:Q03512` | `InterPro:IPR046387` Carboxysome shell vertex protein CcmL |
| carbonic anhydrase / `UniProtKB:P27134` | `InterPro:IPR045066` Beta carbonic anhydrases, clade B |
| scaffold / `UniProtKB:Q03513` | `InterPro:IPR017156` Carboxysome assembly protein CcmM |

Negative controls matter. `UniProtKB:P46204` (the CcmN assembly adaptor) and
`UniProtKB:Q8GJM6` (McdB positioning protein) returned no integrated entry of
type `family`. The combined MamK/MamJ component's only current protein example,
`UniProtKB:V6F519`, resolves to `InterPro:IPR060787` **MamJ**, not MamK. An
adapter must therefore refuse to ground a component when examples disagree with
its scope; that case should trigger a split/review rather than an automatic CURIE.

### Adapter boundary

- Start from curator-selected UniProt examples; never search InterPro by a
  component label.
- Consider integrated entries whose type is exactly `family`; domains and
  homologous superfamilies are supporting context, not interchangeable
  groundings.
- Auto-propose a grounding only for `component_type: PROTEIN`, when every
  reviewed example supports the same exact family. Protein complexes need GO or
  Complex Portal grounding even when their constituent proteins have InterPro
  families.
- Write only the CURIE after review. Do not copy InterPro prose.

## 2. CryoET Data Portal — high-value dataset source (#124)

The portal's submission policy states that data published publicly on the
portal are made available under CC0. The documented Python/GraphQL model exposes
stable dataset identifiers, organism names and NCBI taxids, strain identifiers,
cell-component names and GO identifiers, publications, runs, tomograms,
annotations, and public HTTPS/S3 paths.

### Live coverage

The GraphQL API currently reports 370 datasets. Matching `cellComponentId`
against the current corpus's GO identifiers returned 8 datasets:

- 7 gas-vesicle datasets (`GO:0031411`) from *Dolichospermum flos-aquae*,
  including dataset 10014 (217 runs) and dataset 10017 (14 runs), all linked to
  DOI `10.1016/j.str.2023.03.011`;
- dataset 10498, 81 runs of purified *Escherichia coli* 70S ribosomes
  (`GO:0005840`), released 2026-07-09 and linked to
  `10.1038/s41592-022-01690-1` and its preprint.

Exact annotation-object aggregates add coverage even when a dataset-level cell
component is absent:

| Object | Annotation records |
|---|---:|
| `GO:0120100` bacterial-type flagellum motor | 1,886 |
| `GO:0009288` bacterial-type flagellum | 60 |
| `GO:0044096` type IV pilus | 101 |
| `GO:0005840` ribosome | 2,053 |

The flagellar-motor cohort is not merely a text hit: sampled API annotation
98423 (deposition 10332, run 11676, dataset 10268)
is ground truth, curator recommended, and hybrid annotated. Type-IV-pilus
annotation 30707 is manually annotated, ground truth, and curator recommended
for *Bdellovibrio bacteriovorus* dataset 10155.

### Adapter boundary

- Resolve exact dataset, run and annotation ids through GraphQL; do not ingest a
  browse-page text hit.
- Require a dataset organism taxid already asserted by the target record.
- Prefer exact `objectId` equality to the record or a curated `has_part` term.
  A motor annotation is evidence for a flagellar subassembly, not identity with
  the whole flagellum.
- Store lightweight dataset metadata and links first. Downloading tomograms or
  annotation volumes is a separate, explicit operation; the corpus should not
  host those large files.
- Record annotation quality fields (`groundTruthStatus`,
  `isCuratorRecommended`, method) in `findings`/`notes`; do not flatten
  predictions and manual ground truth.
- Extend the shared dataset enums with explicit CryoET/structural-imaging values
  in the adapter PR. Do not hide a first-class repository behind `OTHER`.

## 3. RCSB PDB — experimental structures and assemblies (#123)

RCSB's usage policy places PDB archive files and all programmatic API data under
CC0 1.0. Structure-summary molecular images use the same conditions. The Data
API and GraphQL API expose entry/assembly accessions, experimental method and
resolution, source organism taxids, UniProt entity links, primary DOI/PMID and
assembly stoichiometry.

### Live canaries

- `PDB:6SCN`: 3.1 Å cryo-EM structure of a 33-member flagellar MS ring;
  entity 1 is FliF (`UniProtKB:P15928`) from *Salmonella typhimurium*
  (`NCBITaxon:90371`), linked to DOI `10.1038/s41564-020-0703-3` and
  `EMD-10143`.
- `PDB:6OQR`: 3.1 Å *E. coli* ATP synthase state, DOI
  `10.1038/s41467-020-16387-2`. GraphQL returned all eight protein entity types,
  eight UniProt accessions, `NCBITaxon:562`, and assembly-level stoichiometry.
- `PDB:8RD8`: 2.62 Å cryo-EM structure of the *Psychrobacter urativorans* 70S
  ribosome, DOI `10.1038/s41586-024-07041-8`, with 55 polymer entities and one
  biological assembly.

PDB adds atomic-model and biological-assembly references that EMPIAR/EMDB and
Complex Portal do not replace. The first adapter should add `datasets` entries;
assembly composition can follow only after its alternate symmetry/stoichiometry
representations have a lossless model. RCSB renders are valuable illustrations,
but they should not be counted as the electron micrographs requested by the
curation guide. As with CryoET, add explicit RCSB/structural-data enum values
rather than recording a new source as `OTHER`.

## 4. PSORTdb — keep blocked (#125)

PSORTdb is biologically relevant: ePSORTdb reports experimentally determined
bacterial/archaeal protein localisations and provides UniProt/RefSeq accessions,
TaxID, localisation, protein/gene names and PMID fields. Its 2021 resource paper
says that all code and data are available under MIT and Creative Commons
licences, but neither that statement nor the live download page identifies the
Creative Commons licence/version for the database data.

There is also a reproducibility defect in the current bulk path. Fetching the
official `Experimental-PSORTdb-v4.00.tsv` URL returned an Apple binary-property-
list/WebArchive wrapper containing an HTML `<pre>` element around the TSV,
rather than a clean TSV response. The content can be recovered, but silently
reverse-engineering that wrapper would make a brittle ingestion contract.

Keep PSORTdb blocked until the maintainers identify the exact data licence and
publish either a clean v4 TSV checksum/version or a documented API. If unblocked,
use only ePSORTdb experimental rows with a PMID; cPSORTdb predictions must never
be presented as experimentally established component membership.

## Recommended implementation order

1. **InterPro grounding adapter**: exact UniProt-to-integrated-family mapping,
   reviewed allow-list, and fail-closed tests for ambiguous/heterogeneous cases.
2. **CryoET dataset adapter**: start with exact gas-vesicle dataset 10014 or
   10017, then an exact manual/ground-truth flagellum or type-IV-pilus annotation.
3. **RCSB PDB dataset adapter**: start with ATP synthase `PDB:6OQR`; retain DOI,
   taxon, method, resolution and entity links without flattening assembly
   alternatives.
4. Revisit PSORTdb only after its two blockers are resolved.

## Primary sources and worked endpoints

InterPro: [licence](https://www.ebi.ac.uk/interpro/about/license/) ·
[API schema](https://www.ebi.ac.uk/interpro/api/static_files/swagger/) ·
[FliF canary](https://www.ebi.ac.uk/interpro/api/entry/interpro/protein/uniprot/P23447/?page_size=200)

CryoET Data Portal: [data-submission policy](https://cryoetdataportal.czscience.com/data-submission-policy) ·
[API quickstart](https://chanzuckerberg.github.io/cryoet-data-portal/stable/cryoet_data_portal_docsite_quick_start.html) ·
[data model and GraphQL endpoint](https://chanzuckerberg.github.io/cryoet-data-portal/v4.0/data_model.html) ·
[flagellum canary dataset 10226](https://cryoetdataportal.czscience.com/datasets/10226) ·
[type-IV-pilus canary dataset 10155](https://cryoetdataportal.czscience.com/datasets/10155)

RCSB PDB: [usage policy](https://www.rcsb.org/pages/usage-policy) ·
[Data API](https://data.rcsb.org/) ·
[6SCN](https://www.rcsb.org/structure/6SCN) ·
[6OQR](https://www.rcsb.org/structure/6OQR) ·
[8RD8](https://www.rcsb.org/structure/8RD8)

PSORTdb: [v4 home and search](https://db.psort.org/) ·
[downloads](https://db.psort.org/downloads) ·
[2021 resource paper](https://pmc.ncbi.nlm.nih.gov/articles/PMC7778896/)
