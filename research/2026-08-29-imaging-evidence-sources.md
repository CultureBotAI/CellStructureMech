# Trusted sources for cell-structure terms and imaging evidence

Deep-research report, 2026-08-29, produced by the `deep-research` workflow
(5 search angles, 23 sources fetched, 109 claims extracted, 25 verified by
3-vote adversarial check: 24 confirmed, 1 refuted). Every claim below was
checked against a live fetch on 2026-08-29; counts are snapshots.

**Purpose.** CellStructureMech wants each record page to show a microscopy
image of the structure, with the image itself carrying a licence, a DOI or
PMID, and an example taxon (NCBITaxon id). This note ranks the sources that
can supply that, and the vocabularies that can supply identifiers.

## Summary

The EMBL-EBI archives are the best imaging evidence for a public site:
**EMPIAR** (everything CC0, per-entry DOI `10.6019/EMPIAR-XXXXX`, REST API
returning the citing paper's DOI + PMID — but no organism field, so taxon
comes via the cross-referenced **EMDB** entry, which carries NCBI Taxonomy
ids and has REST + Python + FTP access). **BioImage Archive** is CC0/CC-BY
for new direct submissions but must be checked per accession. For
prokaryote-specific cryo-ET, the Jensen lab corpus (~15,000 tomograms, 88
species, in **ETDB-Caltech**) and its derived **Atlas of Bacterial &
Archaeal Cell Structure** (>150 tomograms, ~70 species, CaltechDATA DOIs
per video) are the richest structure-organised imagery, but the Atlas is
**CC BY-NC 4.0**, which constrains reuse. For identifiers, **GO cellular
component** is current and PMID-backed; **Complex Portal** covers E. coli
K-12 only among prokaryotes; **MicrO** is inactive at OBO Foundry. **IDR**
is *not* uniformly openly licensed (that claim was refuted 0-3).

## Findings

### Imaging repositories

| Source | Licence | Per-image identifier | Taxon link | Access | Confidence |
|---|---|---|---|---|---|
| **EMPIAR** | CC0 for all data ([policy](https://www.ebi.ac.uk/empiar/policies/)) | Entry-level DOI `10.6019/EMPIAR-XXXXX` (Crossref/DataCite; verified `10.6019/EMPIAR-10028` redirects to the entry). API returns `entry_doi` plus citation DOI + PMID (e.g. EMPIAR-10025 → `10.7554/eLife.06380`, PMID 25760083). | **None in the schema** — grep for organism/taxon/ncbi returns nothing; only `scale`. Resolve via `cross_references` to EMDB. | REST: `GET /empiar/api/entry/{id}`, `POST /empiar/api/entry/` with comma-separated ids or `10060-10062` ranges ([docs](https://www.ebi.ac.uk/empiar/api/documentation/)). Raw datasets are huge: extract and host frames, do not hot-link. | high (3-0) |
| **EMDB** | EMBL-EBI terms | Entry id `EMD-NNNNN`; map files on FTP | **Yes**: sample metadata carries NCBI taxid, strain and higher ranks (EMD-10093 → *Vibrio mimicus* CAIM 602, ncbi 1259812) | 3 REST services (archive, validation, EMICSS); PyPI `emdb` 0.1.12 (Apache-2.0, EMBL-EBI); `ftp.ebi.ac.uk/pub/databases/emdb` ([api](https://www.ebi.ac.uk/emdb/api/)) | high (3-0) |
| **BioImage Archive** | New direct submissions CC0 or CC-BY-4.0; brokered accessions may differ — licence is a per-dataset attribute; fallback is EMBL-EBI Terms of Use ([policy](https://www.ebi.ac.uk/bioimage-archive/help-policies)) | Accession `S-BIADnnn` | Per-study metadata | BioStudies API | high (3-0) |
| **Atlas of Bacterial & Archaeal Cell Structure** ([site](https://www.cellstructureatlas.org/), Oikonomou & Jensen, [JMBE 2021](https://doi.org/10.1128/jmbe.00128-21)) | **CC BY-NC 4.0** | Each video in CaltechDATA with a DataCite DOI (e.g. `10.22002/D1.1362`, *E. coli*), `isDerivedFrom` → the ETDB-Caltech tomogram (`etdb.caltech.edu/tomogram/b7f6a2`) | Species named per chapter; no taxid in metadata | Browse; CaltechDATA API | high (3-0) |
| **ETDB-Caltech / Jensen corpus** ([Dobro et al. 2017](https://journals.asm.org/doi/10.1128/jb.00100-17)) | **Unverified** | Per-tomogram URL | 88 species (2017) | 3D feature views on a figshare private-share link that returned 403 | high for the corpus, **unknown** for licence/API |
| **IDR** ([about](https://idr.openmicroscopy.org/about/)) | **Not uniformly CC0/CC-BY** — refuted 0-3; check per study | Study/image ids | Per study | OMERO API | medium |

### Vocabularies

| Source | Verdict | Evidence |
|---|---|---|
| **GO cellular component** | Primary identifier source. Current, prokaryote-aware (`never_in_taxon`), definitions cite PMIDs. | `GO:0140737` encapsulin nanocompartment: created 2021-11-29, not obsolete, def xref PMID:32918485 ([QuickGO](https://www.ebi.ac.uk/QuickGO/services/ontology/go/terms/GO:0140737)). Other terms may have 0 or many xrefs. |
| **Complex Portal** | Use for E. coli K-12 sub-complexes only. 324 E. coli complexes live; other prokaryotes: *P. aeruginosa* 1, *V. cholerae* 1; **no *B. subtilis*, no archaea**. | [NAR 2022](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8689886/); live species facet 2026-08-29. |
| **MicrO** | Static vocabulary only — OBO Foundry lists it **inactive** (no edits, requests not addressed). | [obofoundry.org/ontology/micro](http://obofoundry.org/ontology/micro.html) |

### Not assessed

No surviving claims covered UniProt subcellular-location vocabulary, NCIT,
PDB, Cell Image Library, Wikimedia Commons, PMC open-access figures,
SubtiWiki / EcoCyc, or ETDB-Caltech's own API and licence. These are open,
not negative, results.

## Caveats

- Snapshot numbers: Jensen 15,000 / 88 (2017), Atlas >150 / ~70 (2021),
  Complex Portal 321 (paper) vs 324 (live).
- CC0 removes the legal attribution requirement only; citing the EMPIAR
  entry DOI and the paper remains the norm. A figure reproduced from a
  journal carries the **publisher's** licence, not EMPIAR's.
- The Atlas's NC licence is a real constraint for a CC0 knowledge base:
  link to it, do not host its frames.
- `emdb` on PyPI is 0.1.x.

## Open questions

1. ETDB-Caltech's own licence, API and taxon ids — it is the common source
   for both the Atlas and Dobro et al., so it may be the single best
   prokaryote-specific feed if its terms allow hosting.
2. Is the Dobro et al. figshare deposit public under any DOI?
3. Mapping EMPIAR → NCBI taxid at scale: what fraction of cell-scale
   prokaryote entries have an EMDB cross-reference?
4. The unassessed sources above, especially Wikimedia Commons and PMC OA
   figures, which are the likeliest to give per-image CC BY licences for
   classic TEM/SEM images.

## What this implies for the schema

An `images` section on `CellStructureRecord`, each entry carrying: `url`
(hosted copy under `pages/img/` for CC0/CC-BY; external link only for NC),
`source` (enum: EMPIAR, EMDB, BIOIMAGE_ARCHIVE, ETDB_CALTECH,
CELL_STRUCTURE_ATLAS, WIKIMEDIA_COMMONS, PMC, OTHER), `source_accession`,
`licence` (enum, required), `modality` (TEM, SEM, CRYO_ET, CRYO_EM,
FLUORESCENCE, …), `taxon_id` + `taxon_label` (required), `reference`
(DOI/PMID, required), `caption`, `attribution`. Rendering shows the first
image at the top of the record page with its licence and citation line.
Tracked in the issue tracker.
