# Catalogue of the remaining term and image sources

Companion to [2026-08-29-imaging-evidence-sources.md](2026-08-29-imaging-evidence-sources.md),
covering the sources that run left unassessed (issue #16). Three research
agents verified each fact by live fetch on 2026-08-29; quotations are
verbatim. Anything the agents could not reach is listed under *Could not
verify* rather than guessed.

## Verdict at a glance

| Source | Role | Licence | Per-image / per-term id | Taxon id | DOI/PMID link | Verdict |
|---|---|---|---|---|---|---|
| **Wikimedia Commons** | images | Per file, machine-readable (`extmetadata.LicenseShortName`, SDC `P275`/`P6216`) | File title + `M<pageid>`; no DOI; stable `upload.wikimedia.org` URL | Via SDC `P180` → Wikidata `P685`, **sparse** | Free text in `Credit` only | **Use** — first choice; download-and-host with attribution (hot-linking "not recommended") |
| **PMC open access** | images | Article-level `license_code` (CC BY / CC BY-NC / CC BY-NC-ND / TDM / null) | JATS `<graphic>` name; S3 key `PMC…/fig.jpg`; no figure DOI | **None** — curator reads the caption | Built in (DOI, PMID) | **Use as a pool** — CC BY only, manual panel + taxon curation. **`oa.fcgi` and `oa_file_list.csv` were discontinued Feb 2026**; use the `pmc-oa-opendata` S3 bucket |
| **Cell Image Library** | images | Per image, submitter-chosen: Public Domain, CC BY, CC BY-NC-SA, CC BY-NC-ND, copyrighted | `CIL:NNNNN` **with a DOI** `10.7295/W9CILNNNNN` and an ARK | Organism *name* only on the page; taxids exist in the backend tree | Optional PMID field | **Use** PD / CC BY records only; thin prokaryote coverage (carboxysome 0, magnetosome 0, gas vesicle 0 hits) |
| **ETDB-Caltech** | images | **No licence statement found** | `etdb.caltech.edu/tomogram/<hex>`; no DOI | Paper says `NCBItaxID` field exists; unverifiable | Not on records | **Do not depend on it** — site unreachable, last Wayback capture 2022-12. Stable layer is CaltechDATA Atlas records (CC BY-NC, link-only) |
| **UniProt Subcellular Location** | vocabulary + components | CC BY 4.0 | `SL-NNNN`, Bioregistry `uniprot.location` | n/a | n/a | **Use** — 6/6 test structures, every term carries its GO CC id, and a REST query lists member proteins per structure and taxon |
| **NCIT** | vocabulary | CC BY 4.0 | `NCIT:Cnnnnn` | n/a | n/a | **Skip** — 0/6 prokaryotic structures, organelle branch eukaryote-only, no GO xrefs |
| **SubtiWiki v5** | organism DB (*B. subtilis*) | **Not stated anywhere found** | Integer ids, no registry prefix for v5 | n/a | Pubmed in free text | **Cautious** — category → genes and `structure/{id}/components` work; ask the Stülke lab about licence before copying |
| **EcoCyc / BioCyc** | organism DB (*E. coli* K-12) | Subscription terms; access free with account; redistribution restricted | Frame ids `ECOLI:CPLX0-7452`, Bioregistry `ecocyc`/`biocyc` | n/a | n/a | **Use for components with stoichiometry**, cite/link rather than copy |

## Image sources

### Wikimedia Commons

- **Licence** two ways: (1) `extmetadata` from `action=query&prop=imageinfo&iiprop=url|extmetadata|sha1` — `LicenseShortName`, `LicenseUrl`, `UsageTerms`, `AttributionRequired`, `Copyrighted`, `Artist`, `Credit` (parsed from templates; values may contain HTML); (2) Structured Data: `P275` licence item, `P6216` copyright status. Not every file has SDC licence statements.
- **Identifiers**: file page, `M<pageid>`, `sha1`; direct URL from `imageinfo.url`. `Special:FilePath/<name>?width=800` gives a thumbnail; the raw `/thumb/…/800px-…` pattern returned 400.
- **Taxon**: `P180` (depicts) → Wikidata item → `P685` NCBI id. Verified `M4508748` → Q15647449 → 927. Reverse search: `srsearch=haswbstatement:P180=Q15647449`. Many micrographs have no `P180`; the curator must add or resolve it.
- **Publication**: no structured field; DOI/PMC appears in `Credit` HTML when at all.
- **Policy**: "Directly using a Commons file via embedding its URL ('hotlinking') is also possible, but is not recommended." Requests need a descriptive User-Agent "or they may be blocked without notice".
- **Candidates verified**: `File:Carboxysomes_EM.jpg` (CC BY 3.0, Tsai et al. 2007, DOI 10.1371/journal.pbio.0050144, *H. neapolitanus* 927 — now the #15 canary); `File:Escherichia_coli_flagella_TEM.png` (public domain, CDC PHIL, *E. coli* O157:H7, no publication — fails our DOI requirement); `File:EMpylori.jpg` ("Copyrighted free use", no publication).

### PMC open access

- **What changed**: "As part of the PMC Article Dataset Changes announced on February 12, 2026, the PMC OA Web Service is no longer available." `ftp.ncbi.nlm.nih.gov/pub/pmc/` now holds only `PMC-ids.csv.gz`. Replacement: public S3 bucket `pmc-oa-opendata` (anonymous HTTPS works), per-article JSON with `license_code` and `media_urls`; "does not separate articles by license category at the directory level".
- **Coverage gap**: PMC1872035 (CC BY, 2007) is **not in the bucket** although its XML says CC BY.
- **Taxon**: none in JSON or JATS; resolve from the caption via `esearch db=taxonomy`.
- **Policy**: "Systematic downloading of batches of articles from the main PMC web site, in any way, is prohibited"; CDN blob URLs are hashed and undocumented — never hot-link.
- **Candidates verified**: PMC13106801 Fig 1a (CC BY, cryo-EM of *Vibrio alginolyticus* flagellar filaments, DOI 10.1038/s41467-026-71203-7); PMC3762834 Fig 1 (CC BY, fluorescence of carboxysomes in *S. elongatus*, DOI 10.1371/journal.pone.0076127).

### Cell Image Library

- **Licence** per record, chosen by the submitter; "The license you choose will then be noted in The Cell on the detailed image page." CC version is not shown on the page.
- **Identifiers**: `doi:10.7295/W9CIL37254` resolves (302 → `/images/37254`); also `ark:/b7295/…`. Citation format includes RRID:SCR_003510.
- **Taxon**: "NCBI Organism Classification" shows the name; the advanced-search tree is keyed `NCBITaxon_2`, `NCBITaxon_2157`, so a name → id lookup is needed.
- **API**: documented (2020) at CRBS/CIL_RS wiki; `cilia.crbs.ucsd.edu/rest/public_ids` answers 401 — key by request. No bulk download found. "Notification of Use" is a courtesy request.
- **Candidates verified**: CIL:39991 *Caulobacter crescentus* CB15 cryo-ET (CC BY, no publication); CIL:40396 *Vibrio cholerae* SEM (public domain, free-text citation, no PMID link); CIL:7321 *E. coli* F-pilus (public domain, PMID 19004777); CIL:14652 *Oscillatoria tenuis* freeze-fracture thylakoid (public domain, no publication).

### ETDB-Caltech and the Cell Structure Atlas

- `etdb.caltech.edu` resolved but refused connections; last Wayback 200 capture 2022-12-16; no shutdown notice found. Code repos last updated 2018–2019.
- The 2019 PLoS ONE paper lists `NCBItaxID, speciesName, strain` fields and an `etdb-downloads` CLI; none of it could be exercised.
- Stable layer: CaltechDATA records for Atlas videos — DOI `10.22002/D1.NNNN`, rights `cc-by-nc-4.0`, `isderivedfrom https://etdb.caltech.edu/tomogram/<id>`; 173 records match the Atlas title. No taxids, no primary-literature DOIs on those records. Atlas still images hot-link today (`cellstructureatlas.org/img/stillimages/…` → 200) but are CC BY-NC.
- **Verified link-only candidates**: carboxysome *H. neapolitanus* DOI 10.22002/D1.1500; S-layer *C. crescentus* DOI 10.22002/D1.1355; flagellum *Campylobacter jejuni* DOI 10.22002/D1.1525.

## Vocabularies and organism databases

### UniProt Subcellular Location — use

- 6/6: bacterial flagellum **SL-0307**, carboxysome **SL-0034**, S-layer **SL-0262**, gas vesicle **SL-0125**, magnetosome **SL-0510**, encapsulin nanocompartment **SL-0550**; plus sub-parts (flagellum basal body/hook/filament, gas vesicle shell/lumen, magnetosome membrane/lumen, bacterial microcompartment SL-0544).
- Each `subcell.txt` record carries `HI` (is-a), `HP` (part-of), `KW` and a `GO` line — all six map 1:1 to the GO CC term (`SL-0034 → GO:0031470`).
- Licence footer: "Distributed under the Creative Commons Attribution (CC BY 4.0) License".
- Access: `subcell.txt` (release 2026_02); `rest.uniprot.org/locations/SL-0034?format=json`; **member proteins**: `rest.uniprot.org/uniprotkb/search?query=(cc_scl_term:SL-0034)+AND+(reviewed:true)+AND+(organism_id:1140)&fields=accession,gene_primary,protein_name&format=tsv` → Q03511 ccmK2, Q31NB3 cbbL, P27134 ccaA, Q03513 ccmM, P46205 ccmO, Q31NB2 cbbS … (*S. elongatus* PCC 7942). 127 reviewed / 4287 unreviewed proteins for carboxysome overall.

### NCIT — skip

0/6; `C13269` Cytoplasmic Organelle has 43 eukaryotic descendants; `C13274` Ribosome carries UMLS/semantic-type properties only, no GO. CC BY 4.0, trademarked name.

### SubtiWiki v5 — cautious

- Swagger API at `subtiwiki.uni-goettingen.de/v5/api/`; `gene-category/387` → "Flagellar proteins", 37 genes; `structure/{id}/components` lists proteins (ribosome structure 223 → RpmGB, RplA, RplL, RpsU …); protein `localization` is free text with `[Pubmed|…]` tags. No GO anywhere; no complex endpoint with stoichiometry.
- **No licence statement** on the site, in the JS bundle, the Swagger spec, or the 2025 NAR paper.

### EcoCyc / BioCyc — use for E. coli components

- `websvc.biocyc.org/getxml?id=ECOLI:CPLX0-7452&detail=full` worked anonymously: flagellum = FLAGELLAR-MOTOR-COMPLEX + FlgE ×120 + FlgK + FlgL + FliC + FliD ×6; `F-1-CPLX` → ATPC ×1, ATPH ×1, ATPA-CPLX ×1, ATPG ×1, ATPD-CPLX ×1. GO CC terms sit on **monomers** (FlgE → GO:0009288, GO:0009424, GO:0009425), not on complex frames.
- `apixml` / `name-search` are behind the login wall; rate ≤ 1 req/s. Terms: academic use "non-commercial and academic uses"; "Licensee shall not… market, distribute, or otherwise exploit the Licensed Materials" — cite and link, do not redistribute.

## Could not verify

- SubtiWiki licence; EcoCyc complex-level GO annotations and flat-file click-through text; NCIT beyond the C13269 branch.
- ETDB-Caltech: everything live (status, licence, metadata, API).
- CIL licence versions, API key availability, taxid on public pages.
- PMC: stability of CDN blob URLs; why PMC1872035 is absent from the bucket; NCBI taxid of *S. elongatus* PCC 7942 by name search.

## What this implies

1. **Images**: Commons first, then PMC (CC BY, via S3), then CIL (PD/CC BY). Link-only for Atlas/CaltechDATA. Drop ETDB until reachable. The #15 schema already covers all of these via `ImageSourceEnum`.
2. **Vocabulary**: add UniProt SL ids to `xrefs` on every record and use `cc_scl_term` + `organism_id` queries to seed `components.protein_examples` for canonical taxa — a reviewed, taxon-paired, CC BY source that ProteinTraitsMech can also link to.
3. **Organism catalogues**: EcoCyc for *E. coli* stoichiometry, cited per component; SubtiWiki only after its licence is clarified.
